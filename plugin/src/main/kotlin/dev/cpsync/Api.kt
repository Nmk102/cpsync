package dev.cpsync

import java.io.IOException
import java.net.URI
import java.net.URLEncoder
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.nio.charset.StandardCharsets.UTF_8
import java.time.Duration

class ApiException(val status: Int, message: String) : IOException(message)

data class RemoteFile(val hash: String, val size: Long, val mtime: Long, val deleted: Boolean)

data class Manifest(val name: String, val revision: Long, val files: Map<String, RemoteFile>) {
    val live: Map<String, RemoteFile> get() = files.filterValues { !it.deleted }
}

/** Клиент HTTP API сервера CP Sync. */
class Api(
    baseUrl: String,
    private val token: String,
    private val deviceId: String,
    private val deviceName: String,
) {
    private val base = normalizeServer(baseUrl)

    private fun req(path: String, timeoutSec: Long = 30): HttpRequest.Builder =
        HttpRequest.newBuilder(URI.create(base + path))
            .timeout(Duration.ofSeconds(timeoutSec))
            .header("Authorization", "Bearer $token")
            .header("X-Device-Id", deviceId)
            .header("X-Device-Name", seg(deviceName))

    private fun send(r: HttpRequest): ByteArray {
        val resp = http.send(r, HttpResponse.BodyHandlers.ofByteArray())
        val body = resp.body() ?: ByteArray(0)
        val code = resp.statusCode()
        if (code !in 200..299) {
            val msg = try {
                Json.parse(String(body, UTF_8)).jObj()["error"].jStr()
            } catch (e: Exception) {
                ""
            }.ifBlank { "HTTP $code" }
            throw ApiException(code, if (code == 401) "Нужно войти в аккаунт заново" else msg)
        }
        return body
    }

    private fun json(r: HttpRequest): Map<String, Any?> = Json.parse(String(send(r), UTF_8)).jObj()

    private fun jsonBody(v: Any?) = HttpRequest.BodyPublishers.ofString(Json.stringify(v), UTF_8)

    fun me(): Map<String, Any?> = json(req("/api/me", 15).GET().build())

    fun logout() {
        send(req("/api/auth/logout", 15).POST(jsonBody(emptyMap<String, Any>())).header("Content-Type", "application/json").build())
    }

    fun linkCode(): Map<String, Any?> =
        json(req("/api/link-codes").POST(jsonBody(emptyMap<String, Any>())).header("Content-Type", "application/json").build())

    fun bytes(url: String): ByteArray =
        send(HttpRequest.newBuilder(URI.create(url)).timeout(Duration.ofSeconds(20)).GET().build())

    fun projects(): List<Map<String, Any?>> =
        json(req("/api/projects").GET().build())["projects"].jArr().map { it.jObj() }

    /** null — проекта на сервере ещё нет. */
    fun manifest(project: String): Manifest? {
        val m = try {
            json(req("/api/projects/${seg(project)}/manifest").GET().build())
        } catch (e: ApiException) {
            if (e.status == 404) return null
            throw e
        }
        val files = LinkedHashMap<String, RemoteFile>()
        for ((path, v) in m["files"].jObj()) {
            val f = v.jObj()
            files[path] = RemoteFile(f["hash"].jStr(), f["size"].jLong(), f["mtime"].jLong(), f["deleted"].jBool())
        }
        return Manifest(m["name"].jStr(project), m["revision"].jLong(), files)
    }

    fun download(project: String, path: String): ByteArray =
        send(req("/api/projects/${seg(project)}/file?path=${qp(path)}", 60).GET().build())

    fun blob(hash: String): ByteArray = send(req("/api/blobs/$hash", 60).GET().build())

    /** base — хэш, от которого мы отталкивались ("" — файла не было). 409 => конфликт. */
    fun upload(project: String, path: String, data: ByteArray, base: String, mtime: Long): Map<String, Any?> =
        json(
            req("/api/projects/${seg(project)}/file?path=${qp(path)}&base=${qp(base)}&mtime=$mtime", 60)
                .PUT(HttpRequest.BodyPublishers.ofByteArray(data)).build()
        )

    fun delete(project: String, path: String, base: String): Map<String, Any?> =
        json(req("/api/projects/${seg(project)}/file?path=${qp(path)}&base=${qp(base)}").DELETE().build())

    fun deleteProject(project: String) {
        send(req("/api/projects/${seg(project)}").DELETE().build())
    }

    fun poll(since: Long, waitSec: Int): Map<String, Any?> =
        json(
            req("/api/poll", waitSec + 20L)
                .POST(jsonBody(mapOf("since" to since, "wait" to waitSec)))
                .header("Content-Type", "application/json")
                .build()
        )

    companion object Auth {
        private val http: HttpClient = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(8))
            .followRedirects(HttpClient.Redirect.NORMAL)
            .build()

        fun seg(s: String): String = URLEncoder.encode(s, UTF_8).replace("+", "%20")
        fun qp(s: String): String = URLEncoder.encode(s, UTF_8)

        fun normalizeServer(url: String): String = url.trim().trimEnd('/').let {
            if (it.startsWith("http://") || it.startsWith("https://")) it else "https://$it"
        }

        /** Ссылка вида https://сервер/#/link/КОД -> (сервер, код). */
        fun parseLink(text: String): Pair<String, String>? {
            val m = Regex("""^(https?://[^/#?\s]+)[^#]*#/link/([A-Za-z0-9-]+)\s*$""").find(text.trim()) ?: return null
            return m.groupValues[1] to m.groupValues[2]
        }

        /** mode: "login", "register" или "link". Возвращает (токен, логин). */
        fun authenticate(server: String, mode: String, body: Map<String, Any?>): Pair<String, String> {
            val r = HttpRequest.newBuilder(URI.create(normalizeServer(server) + "/api/auth/" + mode))
                .timeout(Duration.ofSeconds(20))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(Json.stringify(body), UTF_8))
                .build()
            val resp = try {
                http.send(r, HttpResponse.BodyHandlers.ofString(UTF_8))
            } catch (e: java.net.ConnectException) {
                throw IOException("Сервер не отвечает: ${normalizeServer(server)}")
            } catch (e: java.net.http.HttpConnectTimeoutException) {
                throw IOException("Сервер не отвечает: ${normalizeServer(server)}")
            }
            val m = try {
                Json.parse(resp.body()).jObj()
            } catch (e: Exception) {
                throw IOException("По этому адресу не сервер CP Sync (HTTP ${resp.statusCode()})")
            }
            if (resp.statusCode() !in 200..299) throw ApiException(resp.statusCode(), m["error"].jStr("HTTP ${resp.statusCode()}"))
            return m["token"].jStr() to m["login"].jStr()
        }
    }
}
