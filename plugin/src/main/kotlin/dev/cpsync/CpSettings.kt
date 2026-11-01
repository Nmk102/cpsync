package dev.cpsync

import com.intellij.credentialStore.CredentialAttributes
import com.intellij.credentialStore.generateServiceName
import com.intellij.ide.passwordSafe.PasswordSafe
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.PersistentStateComponent
import com.intellij.openapi.components.Service
import com.intellij.openapi.components.State
import com.intellij.openapi.components.Storage
import com.intellij.openapi.util.io.FileUtil
import java.net.InetAddress
import java.nio.file.Path
import java.nio.file.Paths
import java.util.UUID

@Service(Service.Level.APP)
@State(name = "CpSyncSettings", storages = [Storage("cpsync.xml")])
class CpSettings : PersistentStateComponent<CpSettings.S> {

    class S {
        var serverUrl: String = ""
        var login: String = ""
        var deviceId: String = ""
        var deviceName: String = ""
        var syncRoot: String = ""
        var autoSync: Boolean = true
        var extraExcludes: String = ""
        var linkedRoots: MutableList<String> = mutableListOf()
    }

    private var s = S()

    override fun getState(): S = s

    override fun loadState(state: S) {
        s = state
    }

    val conf: S
        get() {
            if (s.deviceId.isBlank()) s.deviceId = UUID.randomUUID().toString()
            if (s.deviceName.isBlank()) s.deviceName = defaultDeviceName()
            if (s.syncRoot.isBlank()) s.syncRoot = Paths.get(System.getProperty("user.home"), "CPSync").toString()
            if (s.serverUrl.isBlank()) s.serverUrl = BUNDLED_SERVER
            return s
        }

    // ---- токен входа хранится в системном хранилище паролей ----
    private val tokenAttrs = CredentialAttributes(generateServiceName("CP Sync", "account-token"))

    @Volatile
    private var cachedToken: String? = null

    var token: String
        get() = cachedToken ?: (
            PasswordSafe.instance.getPassword(tokenAttrs)?.takeIf { it.isNotBlank() }
                ?: System.getProperty("cpsync.token") // только для разработки: -Dcpsync.token=...
                ?: ""
            ).also { cachedToken = it }
        set(value) {
            cachedToken = value.trim()
            PasswordSafe.instance.setPassword(tokenAttrs, value.trim().ifBlank { null })
        }

    val isLoggedIn: Boolean get() = conf.serverUrl.isNotBlank() && token.isNotBlank()

    // ---- связанные папки ----
    @Synchronized
    fun linkedRoots(): List<String> = conf.linkedRoots.toList()

    @Synchronized
    fun addLinkedRoot(root: Path) {
        val p = FileUtil.toSystemIndependentName(root.toAbsolutePath().normalize().toString())
        if (conf.linkedRoots.none { FileUtil.pathsEqual(it, p) }) conf.linkedRoots.add(p)
    }

    @Synchronized
    fun removeLinkedRoot(root: Path) {
        val p = FileUtil.toSystemIndependentName(root.toAbsolutePath().normalize().toString())
        conf.linkedRoots.removeIf { FileUtil.pathsEqual(it, p) }
    }

    fun excludesList(): List<String> =
        conf.extraExcludes.split(',', ';', '\n').map { it.trim() }.filter { it.isNotEmpty() }

    companion object {
        fun get(): CpSettings = ApplicationManager.getApplication().getService(CpSettings::class.java)

        /** Адрес сервера, «вшитый» в плагин при скачивании с сайта CP Sync. */
        val BUNDLED_SERVER: String by lazy {
            try {
                CpSettings::class.java.getResourceAsStream("/cpsync-server.txt")
                    ?.use { String(it.readAllBytes(), Charsets.UTF_8).trim() } ?: ""
            } catch (e: Exception) {
                ""
            }
        }

        fun defaultDeviceName(): String = try {
            InetAddress.getLocalHost().hostName.substringBefore('.')
        } catch (e: Exception) {
            System.getProperty("user.name") + "-" + System.getProperty("os.name")
        }
    }
}
