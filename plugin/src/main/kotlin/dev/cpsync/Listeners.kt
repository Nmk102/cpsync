package dev.cpsync

import com.intellij.ide.AppLifecycleListener
import com.intellij.openapi.project.Project
import com.intellij.openapi.startup.ProjectActivity
import com.intellij.openapi.vfs.VirtualFile
import com.intellij.openapi.vfs.newvfs.BulkFileListener
import com.intellij.openapi.vfs.newvfs.events.VFileEvent
import com.intellij.openapi.vfs.newvfs.events.VFileMoveEvent
import com.intellij.openapi.vfs.newvfs.events.VFilePropertyChangeEvent
import java.nio.file.Paths

/** Запускаем опрос сервера сразу при старте IDE (чтобы телефон видел ноутбук даже на экране приветствия). */
class CpAppListener : AppLifecycleListener {
    override fun appFrameCreated(commandLineArgs: List<String>) {
        CpService.get().start()
    }
}

/** При открытии проекта: если он привязан — синхронизируем. */
class CpStartup : ProjectActivity {
    override suspend fun execute(project: Project) {
        val svc = CpService.get()
        svc.start()
        val base = project.basePath ?: return
        val root = Paths.get(base)
        if (Link.read(root) != null) {
            CpSettings.get().addLinkedRoot(root)
            svc.refreshRootsCache()
            svc.scheduleSync(com.intellij.openapi.util.io.FileUtil.toSystemIndependentName(root.toString()), 500, "открытие проекта")
        }
    }
}

/** Сохранение/создание/удаление файлов в привязанных папках -> отложенная синхронизация. */
class CpFileListener : BulkFileListener {
    override fun after(events: List<VFileEvent>) {
        if (!CpSettings.get().conf.autoSync) return
        val svc = CpService.get()
        val rules = FileRules.Rules(CpSettings.get().excludesList())
        val roots = HashSet<String>()
        for (e in events) {
            val paths = mutableListOf(e.path)
            if (e is VFileMoveEvent) paths += e.oldPath
            if (e is VFilePropertyChangeEvent && e.propertyName == VirtualFile.PROP_NAME) paths += e.oldPath
            for (p in paths) {
                val root = svc.linkedRootFor(p) ?: continue
                val rel = p.substring(minOf(p.length, root.length)).trimStart('/')
                if (rel.isEmpty() || rel.startsWith(".cpsync")) continue
                if (rules.skipPath(rel)) continue
                roots += root
            }
        }
        for (r in roots) svc.scheduleSync(r, 1500, "сохранение")
    }
}
