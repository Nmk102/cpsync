package dev.cpsync

import com.intellij.ide.BrowserUtil
import com.intellij.openapi.ide.CopyPasteManager
import com.intellij.openapi.progress.ProgressManager
import com.intellij.openapi.project.Project
import com.intellij.openapi.ui.DialogWrapper
import com.intellij.openapi.ui.ValidationInfo
import com.intellij.ui.components.JBCheckBox
import com.intellij.ui.components.JBPasswordField
import com.intellij.ui.components.JBTextField
import com.intellij.ui.dsl.builder.AlignX
import com.intellij.ui.dsl.builder.panel
import java.awt.datatransfer.StringSelection
import javax.imageio.ImageIO
import javax.swing.Action
import javax.swing.ImageIcon
import javax.swing.JComponent

/** Вход в аккаунт CP Sync: логин/пароль, регистрация или одноразовая ссылка с сайта. */
class LoginDialog(project: Project?) : DialogWrapper(project) {
    private val st = CpSettings.get()
    private val serverField = JBTextField(st.conf.serverUrl)
    private val loginField = JBTextField(st.conf.login)
    private val passField = JBPasswordField()
    private val registerBox = JBCheckBox("У меня ещё нет аккаунта — создать новый")
    private val linkField = JBTextField()

    /** (адрес сервера, токен, логин) после успешного входа */
    var result: Triple<String, String, String>? = null
        private set

    init {
        title = "Вход в CP Sync"
        setOKButtonText("Войти")
        registerBox.addActionListener { setOKButtonText(if (registerBox.isSelected) "Создать аккаунт" else "Войти") }
        init()
    }

    override fun getPreferredFocusedComponent(): JComponent =
        if (serverField.text.isBlank()) serverField else if (loginField.text.isBlank()) loginField else passField

    override fun createCenterPanel(): JComponent = panel {
        row("Сервер:") {
            cell(serverField).align(AlignX.FILL).comment(
                if (CpSettings.BUNDLED_SERVER.isNotBlank()) "Адрес уже указан — менять не нужно"
                else "Адрес сайта CP Sync, например https://cpsync.example.com"
            )
        }
        row("Логин:") { cell(loginField).align(AlignX.FILL) }
        row("Пароль:") { cell(passField).align(AlignX.FILL) }
        row("") { cell(registerBox) }
        separator()
        row {
            label("Или вставьте ссылку для входа с сайта (Аккаунт → «Войти без пароля»):")
        }
        row { cell(linkField).align(AlignX.FILL) }
    }.apply { preferredSize = java.awt.Dimension(520, preferredSize.height) }

    override fun doValidate(): ValidationInfo? {
        if (linkField.text.isNotBlank()) {
            return if (Api.parseLink(linkField.text) == null) ValidationInfo("Это не ссылка для входа CP Sync", linkField) else null
        }
        if (serverField.text.isBlank()) return ValidationInfo("Укажите адрес сервера", serverField)
        if (loginField.text.isBlank()) return ValidationInfo("Введите логин", loginField)
        if (passField.password.isEmpty()) return ValidationInfo("Введите пароль", passField)
        return null
    }

    override fun doOKAction() {
        if (!okAction.isEnabled) return
        val link = Api.parseLink(linkField.text)
        val device = st.conf.deviceName
        try {
            val r = ProgressManager.getInstance().runProcessWithProgressSynchronously<Triple<String, String, String>, Exception>({
                if (link != null) {
                    val (tok, login) = Api.authenticate(link.first, "link",
                        mapOf("code" to link.second, "deviceName" to device, "kind" to "ide"))
                    Triple(link.first, tok, login)
                } else {
                    val server = serverField.text.trim()
                    val (tok, login) = Api.authenticate(server, if (registerBox.isSelected) "register" else "login",
                        mapOf("login" to loginField.text.trim(), "password" to String(passField.password),
                            "deviceName" to device, "kind" to "ide"))
                    Triple(server, tok, login)
                }
            }, if (registerBox.isSelected) "Создание аккаунта…" else "Вход…", true, null)
            result = r
            super.doOKAction()
        } catch (e: Exception) {
            setErrorText(e.message ?: e.toString())
        }
    }
}

/** QR-код для входа с телефона. */
class PhoneDialog(project: Project?, private val url: String, png: ByteArray) : DialogWrapper(project) {
    private val image = ImageIcon(ImageIO.read(png.inputStream()))

    init {
        title = "Подключить телефон"
        setOKButtonText("Готово")
        init()
    }

    override fun createCenterPanel(): JComponent = panel {
        row { label("Наведите камеру iPhone на код — откроется CP Sync, и вход выполнится сам.") }
        row { icon(image).align(AlignX.CENTER) }
        row { comment("Код одноразовый и действует 10 минут. Потом установите сайт на экран «Домой»: «Поделиться» → «На экран „Домой“».") }
        row {
            button("Скопировать ссылку") { CopyPasteManager.getInstance().setContents(StringSelection(url)) }
            button("Открыть в браузере") { BrowserUtil.browse(url) }
        }
    }

    override fun createActions(): Array<Action> = arrayOf(okAction)
}
