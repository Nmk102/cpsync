package dev.cpsync

import com.intellij.openapi.Disposable
import com.intellij.openapi.actionSystem.ActionManager
import com.intellij.openapi.actionSystem.DefaultActionGroup
import com.intellij.openapi.project.DumbAware
import com.intellij.openapi.project.Project
import com.intellij.openapi.wm.ToolWindow
import com.intellij.openapi.wm.ToolWindowFactory
import com.intellij.ui.ColoredListCellRenderer
import com.intellij.ui.JBColor
import com.intellij.ui.SimpleTextAttributes
import com.intellij.ui.components.JBLabel
import com.intellij.ui.components.JBList
import com.intellij.ui.components.JBScrollPane
import com.intellij.ui.components.JBTabbedPane
import com.intellij.ui.components.JBTextArea
import com.intellij.ui.content.ContentFactory
import com.intellij.util.ui.JBUI
import java.awt.BorderLayout
import java.awt.FlowLayout
import java.awt.Font
import java.awt.event.MouseAdapter
import java.awt.event.MouseEvent
import java.text.SimpleDateFormat
import java.util.Date
import javax.swing.BoxLayout
import javax.swing.DefaultListModel
import javax.swing.JButton
import javax.swing.JList
import javax.swing.JPanel

class CpToolWindowFactory : ToolWindowFactory, DumbAware {
    override fun createToolWindowContent(project: Project, toolWindow: ToolWindow) {
        val panel = CpPanel(project, toolWindow.disposable)
        val content = ContentFactory.getInstance().createContent(panel, "", false)
        toolWindow.contentManager.addContent(content)
    }
}

private typealias JMap = Map<String, Any?>

class CpPanel(private val project: Project, parent: Disposable) : JPanel(BorderLayout()) {
    private val svc = CpService.get()
    private val status = JBLabel()
    private val projectInfo = JBLabel()
    private val loginPanel = JPanel(FlowLayout(FlowLayout.LEFT, 0, 6)).apply {
        isOpaque = false
        alignmentX = 0f
        add(JButton("Войти или создать аккаунт").apply { addActionListener { CpActions.login(project) } })
    }
    private val projectsModel = DefaultListModel<JMap>()
    private val projectsList = JBList(projectsModel)
    private val logArea = JBTextArea().apply {
        isEditable = false
        font = Font(Font.MONOSPACED, Font.PLAIN, JBUI.scaleFontSize(12f))
    }
    private val dateFmt = SimpleDateFormat("dd.MM HH:mm")

    init {
        val group = DefaultActionGroup()
        val am = ActionManager.getInstance()
        listOf("dev.cpsync.SyncNow", "dev.cpsync.Share", "dev.cpsync.OpenFromServer", "dev.cpsync.ConnectPhone",
            "dev.cpsync.OpenWebsite", "dev.cpsync.Refresh", "dev.cpsync.Settings")
            .mapNotNull { am.getAction(it) }.forEach { group.add(it) }
        val toolbar = am.createActionToolbar("CpSyncToolWindow", group, true)
        toolbar.targetComponent = this

        val header = JPanel().apply {
            layout = BoxLayout(this, BoxLayout.Y_AXIS)
            border = JBUI.Borders.empty(4, 8)
            add(status)
            add(projectInfo)
            add(loginPanel)
        }
        val top = JPanel(BorderLayout()).apply {
            add(toolbar.component, BorderLayout.NORTH)
            add(header, BorderLayout.CENTER)
        }
        add(top, BorderLayout.NORTH)

        projectsList.cellRenderer = ProjectRenderer()
        projectsList.emptyText.text = "На сервере пока нет проектов"
        projectsList.addMouseListener(object : MouseAdapter() {
            override fun mouseClicked(e: MouseEvent) {
                if (e.clickCount == 2) selectedProject()?.let { CpActions.openProject(project, it) }
            }
        })
        val openBtn = JButton("Открыть").apply {
            addActionListener { selectedProject()?.let { CpActions.openProject(project, it) } }
        }
        val delBtn = JButton("Удалить с сервера").apply {
            addActionListener { selectedProject()?.let { CpActions.deleteFromServer(project, it) } }
        }
        val projectsPanel = JPanel(BorderLayout()).apply {
            add(JBScrollPane(projectsList), BorderLayout.CENTER)
            add(JPanel(FlowLayout(FlowLayout.LEFT)).apply { add(openBtn); add(delBtn) }, BorderLayout.SOUTH)
        }

        val tabs = JBTabbedPane()
        tabs.addTab("Проекты", projectsPanel)
        tabs.addTab("Журнал", JBScrollPane(logArea))
        add(tabs, BorderLayout.CENTER)

        svc.addListener({ refresh() }, parent)
        refresh()
    }

    private fun selectedProject(): String? = projectsList.selectedValue?.get("name")?.jStr()

    private fun refresh() {
        val loggedIn = CpSettings.get().isLoggedIn
        status.text = (if (svc.connected) "● " else "○ ") + svc.statusText
        status.foreground = if (svc.connected) JBColor(0x2E7D32, 0x6CC070) else JBColor.GRAY
        loginPanel.isVisible = !loggedIn
        projectsList.emptyText.text = if (loggedIn) "На сервере пока нет проектов" else "Войдите, чтобы увидеть свои проекты"

        val link = svc.linkOf(project)
        projectInfo.text = if (link != null) {
            "Этот проект синхронизируется как «${link.second.project}»"
        } else {
            "Этот проект не синхронизируется — нажмите «Поделиться проектом»"
        }

        val sel = selectedProject()
        projectsModel.clear()
        svc.projects.forEach { projectsModel.addElement(it) }
        if (sel != null) {
            for (i in 0 until projectsModel.size()) {
                if (projectsModel[i]["name"].jStr() == sel) projectsList.selectedIndex = i
            }
        }
        logArea.text = svc.history().joinToString("\n")
        logArea.caretPosition = 0
    }

    private inner class ProjectRenderer : ColoredListCellRenderer<JMap>() {
        override fun customizeCellRenderer(list: JList<out JMap>, value: JMap?, index: Int, selected: Boolean, hasFocus: Boolean) {
            if (value == null) return
            val name = value["name"].jStr()
            append(name, SimpleTextAttributes.REGULAR_BOLD_ATTRIBUTES)
            if (svc.rootsFor(name).isNotEmpty()) append("  ✓ есть здесь", SimpleTextAttributes.GRAYED_ATTRIBUTES)
            val updated = value["updatedAt"].jLong()
            val by = value["updatedBy"].jStr()
            append(
                "   ${value["fileCount"].jLong()} файл.  ·  изменён ${if (updated > 0) dateFmt.format(Date(updated)) else "—"}" +
                        if (by.isNotBlank()) " ($by)" else "",
                SimpleTextAttributes.GRAYED_SMALL_ATTRIBUTES,
            )
        }
    }
}
