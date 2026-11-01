package dev.cpsync

import com.intellij.openapi.fileChooser.FileChooserDescriptorFactory
import com.intellij.openapi.options.BoundConfigurable
import com.intellij.openapi.ui.DialogPanel
import com.intellij.ui.components.JBLabel
import com.intellij.ui.dsl.builder.AlignX
import com.intellij.ui.dsl.builder.bindSelected
import com.intellij.ui.dsl.builder.bindText
import com.intellij.ui.dsl.builder.panel
import javax.swing.JButton

class CpConfigurable : BoundConfigurable("CP Sync") {
    private val settings = CpSettings.get()
    private val s = settings.conf
    private val accountLabel = JBLabel()
    private lateinit var loginButton: JButton
    private lateinit var logoutButton: JButton

    private fun refreshAccount() {
        val st = CpSettings.get()
        if (st.isLoggedIn) {
            accountLabel.text = "Вы вошли как ${st.conf.login.ifBlank { "?" }} · ${st.conf.serverUrl}"
        } else {
            accountLabel.text = "Вход не выполнен"
        }
        if (::loginButton.isInitialized) {
            loginButton.isVisible = !st.isLoggedIn
            logoutButton.isVisible = st.isLoggedIn
        }
    }

    override fun createPanel(): DialogPanel {
        val p = panel {
            group("Аккаунт") {
                row { cell(accountLabel) }
                row {
                    loginButton = button("Войти…") { CpActions.login(null); refreshAccount() }.component
                    logoutButton = button("Выйти") { CpActions.logout(null); refreshAccount() }.component
                    button("Подключить телефон…") { CpActions.connectPhone(null) }
                    button("Открыть сайт") { CpActions.openWebsite() }
                }
                row("Имя этого компьютера:") {
                    textField().bindText(s::deviceName).align(AlignX.FILL)
                        .comment("Так компьютер будет подписан в списке устройств и у изменённых файлов")
                }
            }
            group("Синхронизация") {
                row {
                    checkBox("Синхронизировать автоматически (при сохранении и при изменениях на других устройствах)")
                        .bindSelected(s::autoSync)
                }
                row("Папка для проектов с сервера:") {
                    textFieldWithBrowseButton(
                        FileChooserDescriptorFactory.createSingleFolderDescriptor().withTitle("Папка для проектов CP Sync"),
                    ).bindText(s::syncRoot).align(AlignX.FILL)
                }
                row("Не синхронизировать также:") {
                    textField().bindText(s::extraExcludes).align(AlignX.FILL)
                        .comment("Маски имён через запятую, например: *.txt, tests, stress*. " +
                                "Всегда пропускаются .idea, .git, cmake-build-*, build, бинарники и файлы больше 1 МБ.")
                }
            }
            row {
                comment("Тесты запускаются на сервере: откройте сайт CP Sync на телефоне или нажмите «Подключить телефон».")
            }
        }
        refreshAccount()
        return p
    }

    override fun apply() {
        super.apply()
        if (s.deviceName.isBlank()) s.deviceName = CpSettings.defaultDeviceName()
        CpService.get().restart()
    }
}
