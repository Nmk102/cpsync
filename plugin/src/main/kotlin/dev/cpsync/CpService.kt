package dev.cpsync

import com.intellij.notification.NotificationGroupManager
import com.intellij.notification.NotificationType
import com.intellij.openapi.Disposable
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.application.ModalityState
import com.intellij.openapi.components.Service
import com.intellij.openapi.diagnostic.Logger
import com.intellij.openapi.fileEditor.FileDocumentManager
import com.intellij.openapi.project.Project
import com.intellij.openapi.util.io.FileUtil
import com.intellij.openapi.vfs.VfsUtil
import com.intellij.util.concurrency.AppExecutorUtil
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths
import java.text.SimpleDateFormat
import java.util.Date
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.CopyOnWriteArrayList
import java.util.concurrent.CountDownLatch
import java.util.concurrent.Future
import java.util.concurrent.ScheduledFuture
import java.util.concurrent.TimeUnit

@Service(Service.Level.APP)
class CpService : Disposable {
    private val log = Logger.getInstance(CpService::class.java)

    @Volatile var connected = false
        private set
    @Volatile var statusText = "Не настроено"
        private set
    @Volatile var projects: List<Map<String, Any?>> = emptyList()
        private set

    private val history = ArrayDeque<String>()
    private val listeners = CopyOnWriteArrayList<() -> Unit>()

    private val syncExecutor = AppExecutorUtil.createBoundedApplicationPoolExecutor("CP Sync", 1)
    private val scheduler = AppExecutorUtil.getAppScheduledExecutorService()
    private val pending = ConcurrentHashMap<String, ScheduledFuture<*>>()

    @Volatile private var pollThread: Thread? = null
    @Volatile private var generation = 0
    @Volatile private var disposed = false
    @Volatile private var lastErrorNotified = ""
    @Volatile private var rootsCache: List<String> = emptyList()
    private var lastListsRefresh = 0L

    private val timeFmt = SimpleDateFormat("HH:mm:ss")

    companion object {
        fun get(): CpService = ApplicationManager.getApplication().getService(CpService::class.java)
    }

    init {
        refreshRootsCache()
    }

    // ---------------------------------------------------------------- UI hooks
    fun addListener(l: () -> Unit, parent: Disposable) {
        listeners += l
        com.intellij.openapi.util.Disposer.register(parent) { listeners -= l }
    }

    private fun changed() {
        ApplicationManager.getApplication().invokeLater({ listeners.forEach { it() } }, ModalityState.any())
    }

    fun history(): List<String> = synchronized(history) { history.toList() }

    fun logLine(s: String) {
        synchronized(history) {
            history.addFirst("${timeFmt.format(Date())}  $s")
            while (history.size > 200) history.removeLast()
        }
        changed()
    }

    fun notify(project: Project?, title: String, text: String, type: NotificationType = NotificationType.INFORMATION) {
        ApplicationManager.getApplication().invokeLater {
            NotificationGroupManager.getInstance().getNotificationGroup("CP Sync")
                .createNotification(title, text, type).notify(project)
        }
    }

    // ---------------------------------------------------------------- API
    fun api(): Api? {
        val st = CpSettings.get()
        val s = st.conf
        val token = st.token
        if (s.serverUrl.isBlank() || token.isBlank()) return null
        return Api(s.serverUrl, token, s.deviceId, s.deviceName)
    }

    /** Вход выполнен: сохраняем токен и перезапускаем опрос. */
    fun loggedIn(server: String, token: String, login: String) {
        val st = CpSettings.get()
        st.conf.serverUrl = Api.normalizeServer(server)
        st.conf.login = login
        st.token = token
        logLine("Вход выполнен: $login")
        restart()
    }

    fun logout(revoke: Boolean = true) {
        val api = api()
        val st = CpSettings.get()
        st.token = ""
        st.conf.login = ""
        if (revoke && api != null) {
            ApplicationManager.getApplication().executeOnPooledThread {
                try {
                    api.logout()
                } catch (_: Exception) {
                }
            }
        }
        projects = emptyList()
        logLine("Выход из аккаунта")
        restart()
    }

    // ---------------------------------------------------------------- poller
    @Synchronized
    fun start() {
        if (disposed || pollThread?.isAlive == true) return
        val gen = generation
        pollThread = Thread({ pollLoop(gen) }, "CP Sync poller").apply { isDaemon = true; start() }
    }

    @Synchronized
    fun restart() {
        generation++
        pollThread?.interrupt()
        pollThread = null
        connected = false
        lastErrorNotified = ""
        refreshRootsCache()
        start()
        changed()
    }

    private fun setStatus(ok: Boolean, text: String) {
        if (connected != ok || statusText != text) {
            connected = ok
            statusText = text
            changed()
        }
    }

    private fun pollLoop(gen: Int) {
        var since = -1L
        var backoff = 1000L
        var wasConnected = false
        while (!disposed && gen == generation) {
            val api = api()
            if (api == null) {
                setStatus(false, "Вход не выполнен")
                if (!sleep(3000)) return
                continue
            }
            try {
                val r = api.poll(since, 25)
                if (gen != generation) return
                val st = CpSettings.get().conf
                setStatus(true, "${st.login.ifBlank { "Аккаунт" }} · ${st.serverUrl.removePrefix("https://").removePrefix("http://")}")
                backoff = 1000
                if (!wasConnected) {
                    wasConnected = true
                    lastErrorNotified = ""
                    logLine("Подключено к серверу")
                    refreshLists(api)
                    syncAllLinked("подключение", 300)
                }
                if (r["resync"].jBool() && since >= 0) syncAllLinked("пропущены события", 300)
                since = r["seq"].jLong(since)

                val myId = CpSettings.get().conf.deviceId
                val changedProjects = LinkedHashSet<String>()
                var listsDirty = false
                for (e in r["events"].jArr().map { it.jObj() }) {
                    listsDirty = true
                    if (e["byId"].jStr() == myId) continue
                    when (e["type"].jStr()) {
                        "project_changed" -> changedProjects += e["project"].jStr()
                        "project_deleted" -> onRemoteProjectDeleted(e["project"].jStr(), e["by"].jStr())
                    }
                }
                for (p in changedProjects) {
                    for (root in rootsFor(p)) scheduleSync(root, 400, "изменения от другого устройства")
                }
                if (listsDirty || System.currentTimeMillis() - lastListsRefresh > 15_000) refreshLists(api)
            } catch (e: InterruptedException) {
                return
            } catch (e: Exception) {
                if (gen != generation || Thread.currentThread().isInterrupted) return
                if (wasConnected) logLine("Связь с сервером потеряна: ${e.message ?: e.javaClass.simpleName}")
                wasConnected = false
                val msg = (e as? ApiException)?.message ?: (e.message ?: e.javaClass.simpleName)
                setStatus(false, "Нет связи с сервером: $msg")
                if (e is ApiException && e.status == 401) {
                    // устройство отключили на сайте или сменили пароль
                    CpSettings.get().token = ""
                    notify(null, "CP Sync", "Нужно войти в аккаунт заново (это устройство отключили или сессия устарела).", NotificationType.WARNING)
                    setStatus(false, "Вход не выполнен")
                    continue
                }
                if (!sleep(backoff)) return
                backoff = minOf(backoff * 2, 30_000)
            }
        }
    }

    private fun sleep(ms: Long): Boolean = try {
        Thread.sleep(ms)
        true
    } catch (e: InterruptedException) {
        false
    }

    fun refreshLists(api: Api? = api()) {
        if (api == null) return
        lastListsRefresh = System.currentTimeMillis()
        try {
            projects = api.projects()
            changed()
        } catch (e: Exception) {
            log.debug(e)
        }
    }

    private fun onRemoteProjectDeleted(name: String, by: String) {
        val roots = rootsFor(name)
        for (r in roots) unlink(Paths.get(r))
        if (roots.isNotEmpty()) {
            logLine("Проект «$name» удалён с сервера ($by) — локальная папка оставлена, синхронизация выключена")
            notify(null, "CP Sync", "Проект «$name» удалён с сервера устройством $by. Локальные файлы не тронуты.")
        }
    }

    // ---------------------------------------------------------------- links
    fun refreshRootsCache() {
        rootsCache = CpSettings.get().linkedRoots().map { FileUtil.toSystemIndependentName(it) }
    }

    fun linkedRootFor(path: String): String? {
        val p = FileUtil.toSystemIndependentName(path)
        return rootsCache.firstOrNull { FileUtil.pathsEqual(p, it) || FileUtil.startsWith(p, "$it/") }
    }

    fun rootsFor(project: String): List<String> =
        CpSettings.get().linkedRoots().filter { Link.read(Paths.get(it))?.project == project }

    fun linkOf(project: Project): Pair<Path, LinkInfo>? {
        val base = project.basePath ?: return null
        val root = Paths.get(base)
        val info = Link.read(root) ?: return null
        return root to info
    }

    fun link(root: Path, name: String) {
        val existing = Link.read(root)
        val info = if (existing != null && existing.project == name) existing else LinkInfo(name, LinkedHashMap())
        Link.write(root, info)
        CpSettings.get().addLinkedRoot(root)
        refreshRootsCache()
        changed()
    }

    fun unlink(root: Path) {
        try {
            Link.remove(root)
        } catch (_: Exception) {
        }
        CpSettings.get().removeLinkedRoot(root)
        refreshRootsCache()
        changed()
    }

    // ---------------------------------------------------------------- sync
    fun scheduleSync(root: String, delayMs: Long, reason: String) {
        pending.compute(root) { _, old ->
            old?.cancel(false)
            scheduler.schedule({
                pending.remove(root)
                syncExecutor.execute { syncRoot(Paths.get(root), reason, null, false) }
            }, delayMs, TimeUnit.MILLISECONDS)
        }
    }

    fun syncAllLinked(reason: String, delayMs: Long) {
        for (r in CpSettings.get().linkedRoots()) scheduleSync(r, delayMs, reason)
    }

    /** Синхронизация, запущенная пользователем: ждём результата. */
    fun syncNow(root: Path, project: Project?, manual: Boolean): Future<SyncResult?> =
        syncExecutor.submit<SyncResult?> { syncRoot(root, "вручную", project, manual) }

    private fun saveDocumentsUnder(root: Path) {
        val rootSi = FileUtil.toSystemIndependentName(root.toString())
        val latch = CountDownLatch(1)
        ApplicationManager.getApplication().invokeLater({
            try {
                val fdm = FileDocumentManager.getInstance()
                for (doc in fdm.unsavedDocuments) {
                    val vf = fdm.getFile(doc) ?: continue
                    if (FileUtil.startsWith(vf.path, "$rootSi/")) fdm.saveDocument(doc)
                }
            } finally {
                latch.countDown()
            }
        }, ModalityState.nonModal())
        latch.await(3, TimeUnit.SECONDS)
    }

    private fun syncRoot(root: Path, reason: String, project: Project?, manual: Boolean): SyncResult? {
        val api = api()
        if (api == null) {
            if (manual) notify(project, "CP Sync", "Сначала войдите в аккаунт CP Sync (окно CP Sync справа → «Войти»)", NotificationType.WARNING)
            return null
        }
        if (!Files.isDirectory(root) || Link.read(root) == null) {
            unlink(root)
            return null
        }
        val name = Link.read(root)?.project ?: return null
        return try {
            saveDocumentsUnder(root)
            val engine = SyncEngine(api, FileRules.Rules(CpSettings.get().excludesList()))
            val res = engine.sync(root)
            if (res.changedLocal) VfsUtil.markDirtyAndRefresh(true, true, true, root.toFile())
            if (res.changedAnything) logLine("«$name»: ${res.summary()} ($reason)")
            if (res.conflicts.isNotEmpty()) {
                notify(
                    project, "CP Sync: конфликт в «$name»",
                    "Файлы менялись на двух устройствах: ${res.conflicts.joinToString(", ")}.<br>" +
                            "Оставлена более новая версия, вторая сохранена в ${res.conflictDir}",
                    NotificationType.WARNING,
                )
            }
            if (manual) notify(project, "CP Sync", "«$name»: ${res.summary()}")
            if (res.changedAnything) refreshLists(api)
            res
        } catch (e: Exception) {
            log.warn("CP Sync failed for $root", e)
            val msg = e.message ?: e.javaClass.simpleName
            logLine("«$name»: ошибка синхронизации — $msg")
            if (manual || project != null) notify(project, "CP Sync: ошибка", msg, NotificationType.ERROR)
            null
        }
    }

    override fun dispose() {
        disposed = true
        pollThread?.interrupt()
        pending.values.forEach { it.cancel(false) }
    }
}
