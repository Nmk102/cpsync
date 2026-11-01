package dev.cpsync

import com.intellij.ide.impl.ProjectUtil
import com.intellij.openapi.actionSystem.ActionUpdateThread
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.options.ShowSettingsUtil
import com.intellij.openapi.progress.ProgressIndicator
import com.intellij.openapi.progress.ProgressManager
import com.intellij.openapi.progress.Task
import com.intellij.openapi.project.DumbAwareAction
import com.intellij.openapi.project.Project
import com.intellij.openapi.ui.InputValidator
import com.intellij.openapi.ui.Messages
import com.intellij.openapi.ui.popup.JBPopupFactory
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

object CpActions {
    private val badChars = Regex("[/\\\\:*?\"<>|\\x00-\\x1f]")

    private val nameValidator = object : InputValidator {
        override fun checkInput(s: String?): Boolean {
            val t = s ?: return false
            return t.isNotBlank() && t.trim() == t && t.length <= 100 && !t.startsWith(".") && !badChars.containsMatchIn(t)
        }

        override fun canClose(s: String?): Boolean = checkInput(s)
    }

    fun safeDirName(name: String): String =
        name.replace(badChars, "_").trimEnd('.', ' ').ifBlank { "project" }

    fun configure(project: Project?) {
        ShowSettingsUtil.getInstance().showSettingsDialog(project, CpConfigurable::class.java)
    }

    private fun ensureConfigured(project: Project?): Boolean {
        if (CpService.get().api() != null) return true
        return login(project)
    }

    /** Показывает окно входа. true — вход выполнен. */
    fun login(project: Project?): Boolean {
        val d = LoginDialog(project)
        if (!d.showAndGet()) return false
        val (server, token, login) = d.result ?: return false
        CpService.get().loggedIn(server, token, login)
        CpService.get().notify(project, "CP Sync", "Вы вошли как $login. Откройте проект и нажмите «Поделиться проектом» — " +
                "или «Открыть проект с сервера», если он уже есть на другом устройстве.")
        return true
    }

    fun logout(project: Project?) {
        val r = Messages.showYesNoDialog(project, "Выйти из аккаунта CP Sync на этом компьютере?\nСинхронизация остановится, файлы останутся.",
            "CP Sync", "Выйти", "Отмена", null)
        if (r == Messages.YES) CpService.get().logout()
    }

    fun connectPhone(project: Project?) {
        if (!ensureConfigured(project)) return
        val api = CpService.get().api() ?: return
        val data = try {
            ProgressManager.getInstance().runProcessWithProgressSynchronously<Pair<String, ByteArray>, Exception>({
                val l = api.linkCode()
                l["url"].jStr() to api.bytes(l["qrPng"].jStr())
            }, "Получение кода…", true, project)
        } catch (e: Exception) {
            Messages.showErrorDialog(project, "Не удалось получить код: ${e.message}", "CP Sync")
            return
        }
        PhoneDialog(project, data.first, data.second).show()
    }

    fun openWebsite() {
        val url = CpSettings.get().conf.serverUrl
        if (url.isNotBlank()) com.intellij.ide.BrowserUtil.browse(Api.normalizeServer(url))
    }

    private fun background(project: Project?, title: String, body: (ProgressIndicator) -> Unit, after: () -> Unit = {}) {
        ProgressManager.getInstance().run(object : Task.Backgroundable(project, title, true) {
            override fun run(indicator: ProgressIndicator) = body(indicator)
            override fun onSuccess() = after()
        })
    }

    fun syncProject(project: Project) {
        if (!ensureConfigured(project)) return
        val svc = CpService.get()
        val link = svc.linkOf(project)
        if (link == null) {
            val r = Messages.showYesNoDialog(
                project, "Этот проект ещё не синхронизируется. Отправить его на сервер?",
                "CP Sync", "Поделиться…", "Отмена", null,
            )
            if (r == Messages.YES) share(project)
            return
        }
        CpSettings.get().addLinkedRoot(link.first)
        svc.refreshRootsCache()
        background(project, "CP Sync: синхронизация «${link.second.project}»", {
            svc.syncNow(link.first, project, true).get()
        })
    }

    fun share(project: Project) {
        if (!ensureConfigured(project)) return
        val base = project.basePath ?: return
        val root = Paths.get(base)
        val svc = CpService.get()
        val current = Link.read(root)?.project
        val name = Messages.showInputDialog(
            project,
            "Имя проекта на сервере (под этим именем он появится на других устройствах и в телефоне):",
            "CP Sync: поделиться проектом", null, current ?: root.fileName.toString(), nameValidator,
        ) ?: return
        val exists = try {
            ProgressManager.getInstance().runProcessWithProgressSynchronously<Boolean, Exception>(
                { svc.api()!!.manifest(name) != null }, "Проверка имени…", true, project,
            )
        } catch (e: Exception) {
            Messages.showErrorDialog(project, "Сервер недоступен: ${e.message}", "CP Sync")
            return
        }
        if (exists && current != name) {
            val r = Messages.showYesNoDialog(
                project,
                "На сервере уже есть проект «$name». Объединить с ним эту папку?\n\n" +
                        "Совпадающие файлы останутся как есть; если файл отличается — победит более новая версия, " +
                        "а другая сохранится в папке .cpsync/conflicts.",
                "CP Sync", "Объединить", "Отмена", null,
            )
            if (r != Messages.YES) return
        }
        svc.link(root, name)
        background(project, "CP Sync: отправка «$name»", { svc.syncNow(root, project, true).get() })
    }

    fun unshare(project: Project) {
        val svc = CpService.get()
        val link = svc.linkOf(project) ?: return
        val r = Messages.showYesNoDialog(
            project,
            "Перестать синхронизировать эту папку с «${link.second.project}»?\nФайлы на сервере и здесь останутся.",
            "CP Sync", "Отключить", "Отмена", null,
        )
        if (r == Messages.YES) {
            svc.unlink(link.first)
            svc.notify(project, "CP Sync", "Синхронизация «${link.second.project}» отключена для этой папки")
        }
    }

    fun openFromServer(project: Project?) {
        if (!ensureConfigured(project)) return
        val api = CpService.get().api() ?: return
        val list = try {
            ProgressManager.getInstance().runProcessWithProgressSynchronously<List<Map<String, Any?>>, Exception>(
                { api.projects() }, "Загрузка списка проектов…", true, project,
            )
        } catch (e: Exception) {
            Messages.showErrorDialog(project, "Сервер недоступен: ${e.message}", "CP Sync")
            return
        }
        if (list.isEmpty()) {
            Messages.showInfoMessage(
                project, "На сервере пока нет проектов. Откройте проект в CLion и нажмите «Поделиться проектом».",
                "CP Sync",
            )
            return
        }
        val names = list.map { it["name"].jStr() }
        val popup = JBPopupFactory.getInstance().createPopupChooserBuilder(names)
            .setTitle("Открыть проект с сервера")
            .setItemChosenCallback { openProject(project, it) }
            .createPopup()
        if (project != null) popup.showCenteredInCurrentWindow(project) else popup.showInFocusCenter()
    }

    /** Скачивает проект в папку синхронизации (или находит уже привязанную) и открывает его. */
    fun openProject(current: Project?, name: String) {
        val svc = CpService.get()
        val existing = svc.rootsFor(name).firstOrNull()?.let { Paths.get(it) }
        val root: Path = existing ?: Paths.get(CpSettings.get().conf.syncRoot, safeDirName(name))
        if (existing == null) {
            val nonEmpty = Files.isDirectory(root) && Files.list(root).use { it.findAny().isPresent }
            if (nonEmpty && Link.read(root)?.project != name) {
                val r = Messages.showYesNoDialog(
                    current,
                    "Папка $root уже существует и не пуста. Связать её с проектом «$name» и объединить файлы?",
                    "CP Sync", "Объединить", "Отмена", null,
                )
                if (r != Messages.YES) return
            }
            Files.createDirectories(root)
            svc.link(root, name)
        }
        var ok = false
        background(current, "CP Sync: загрузка «$name»", {
            ok = svc.syncNow(root, current, false).get() != null
        }) {
            if (!ok) {
                Messages.showErrorDialog(current, "Не удалось скачать проект — подробности в окне CP Sync.", "CP Sync")
                return@background
            }
            val open = ProjectUtil.findAndFocusExistingProjectForPath(root)
            if (open == null) ProjectUtil.openOrImport(root.toString(), null, true)
        }
    }

    fun deleteFromServer(project: Project?, name: String) {
        val r = Messages.showYesNoDialog(
            project,
            "Удалить проект «$name» с сервера?\nЛокальные папки на всех ноутбуках останутся, но перестанут синхронизироваться.",
            "CP Sync", "Удалить", "Отмена", Messages.getWarningIcon(),
        )
        if (r != Messages.YES) return
        val svc = CpService.get()
        val api = svc.api() ?: return
        background(project, "CP Sync: удаление «$name»", {
            api.deleteProject(name)
            for (root in svc.rootsFor(name)) svc.unlink(Paths.get(root))
            svc.logLine("Проект «$name» удалён с сервера")
            svc.refreshLists(api)
        })
    }
}

abstract class CpBaseAction : DumbAwareAction() {
    override fun getActionUpdateThread() = ActionUpdateThread.BGT
}

class SyncNowAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.syncProject(e.project ?: return)
    }

    override fun update(e: AnActionEvent) {
        e.presentation.isEnabled = e.project != null
    }
}

class ShareProjectAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.share(e.project ?: return)
    }

    override fun update(e: AnActionEvent) {
        e.presentation.isEnabled = e.project?.basePath != null
    }
}

class UnshareProjectAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.unshare(e.project ?: return)
    }

    override fun update(e: AnActionEvent) {
        val p = e.project
        e.presentation.isEnabled = p != null && p.basePath?.let { Link.read(Paths.get(it)) } != null
    }
}

class OpenFromServerAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.openFromServer(e.project)
    }
}

class OpenSettingsAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.configure(e.project)
    }
}

class LoginAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.login(e.project)
    }

    override fun update(e: AnActionEvent) {
        e.presentation.isEnabledAndVisible = !CpSettings.get().isLoggedIn
    }
}

class LogoutAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.logout(e.project)
    }

    override fun update(e: AnActionEvent) {
        e.presentation.isEnabledAndVisible = CpSettings.get().isLoggedIn
    }
}

class ConnectPhoneAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.connectPhone(e.project)
    }
}

class OpenWebsiteAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        CpActions.openWebsite()
    }

    override fun update(e: AnActionEvent) {
        e.presentation.isEnabled = CpSettings.get().conf.serverUrl.isNotBlank()
    }
}

class RefreshListsAction : CpBaseAction() {
    override fun actionPerformed(e: AnActionEvent) {
        ApplicationManager.getApplication().executeOnPooledThread { CpService.get().refreshLists() }
    }
}
