package dev.cpsync

import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import java.io.File
import java.net.ServerSocket
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.nio.file.Files
import java.nio.file.Path

/**
 * Поднимает настоящий сервер (python3 ../server/cpsync_server.py) и гоняет через него
 * синхронизацию двух «ноутбуков» и запуск тестов «с телефона».
 */
class EndToEndTest {
    private lateinit var server: Process
    private var port = 0
    private var token = ""
    private val http = HttpClient.newHttpClient()

    @Before
    fun startServer() {
        port = ServerSocket(0).use { it.localPort }
        val data = Files.createTempDirectory("cpsync-srv")
        val pb = ProcessBuilder(
            "python3", "-m", "cpsync", "--host", "127.0.0.1", "--port", "$port", "--data", data.toString(),
        ).redirectErrorStream(true).redirectOutput(File(data.toFile(), "log.txt"))
        pb.environment()["PYTHONPATH"] = File("../server").absolutePath
        pb.environment()["CPSYNC_SANDBOX"] = "local"
        server = pb.start()
        repeat(80) {
            try {
                token = Api.authenticate("http://127.0.0.1:$port", "register",
                    mapOf("login" to "tester", "password" to "secret1", "deviceName" to "Ноутбук с CLion", "kind" to "ide")).first
                return
            } catch (e: Exception) {
                Thread.sleep(100)
            }
        }
        error("server did not start")
    }

    @After
    fun stopServer() {
        server.destroy()
    }

    private fun api(id: String) = Api("http://127.0.0.1:$port", token, id, "dev-$id")
    private fun engine(id: String) = SyncEngine(api(id), FileRules.Rules(listOf("*.log")))

    private fun write(root: Path, rel: String, text: String) {
        val f = root.resolve(rel)
        Files.createDirectories(f.parent)
        Files.writeString(f, text)
    }

    private fun read(root: Path, rel: String): String? =
        root.resolve(rel).takeIf { Files.exists(it) }?.let { Files.readString(it) }

    private fun raw(method: String, path: String, body: String? = null): Map<String, Any?> {
        val b = HttpRequest.newBuilder(URI.create("http://127.0.0.1:$port$path"))
            .header("Authorization", "Bearer $token")
            .header("Content-Type", "application/json")
        val req = if (body != null) b.method(method, HttpRequest.BodyPublishers.ofString(body)).build()
        else b.method(method, HttpRequest.BodyPublishers.noBody()).build()
        val resp = http.send(req, HttpResponse.BodyHandlers.ofString())
        return Json.parse(resp.body()).jObj() + mapOf("_status" to resp.statusCode().toLong())
    }

    @Test
    fun syncBetweenTwoLaptops() {
        val a = Files.createTempDirectory("laptopA")
        val b = Files.createTempDirectory("laptopB")
        write(a, "CMakeLists.txt", "cmake_minimum_required(VERSION 3.20)\nproject(olymp)\nadd_executable(A A.cpp)\n")
        write(a, "A.cpp", "#include <bits/stdc++.h>\nint main(){long long a,b;std::cin>>a>>b;std::cout<<a+b<<\"\\n\";}\n")
        write(a, "lib/util.h", "#pragma once\n")
        write(a, "cmake-build-debug/junk.txt", "should not sync")
        write(a, ".idea/workspace.xml", "<x/>")
        write(a, "debug.log", "excluded by extra rule")
        Files.write(a.resolve("a.out"), byteArrayOf(0x7f, 0x45, 0x4c, 0x46, 0, 0, 1))
        Files.write(a.resolve("main"), byteArrayOf(1, 2, 0, 3)) // бинарник без расширения

        Link.write(a, LinkInfo("Олимп", LinkedHashMap()))
        val r1 = engine("A").sync(a)
        assertEquals(3, r1.uploaded)

        val m = api("A").manifest("Олимп")!!
        assertEquals(setOf("A.cpp", "CMakeLists.txt", "lib/util.h"), m.live.keys)

        // второй ноутбук скачивает
        Link.write(b, LinkInfo("Олимп", LinkedHashMap()))
        val r2 = engine("B").sync(b)
        assertEquals(3, r2.downloaded)
        assertEquals(read(a, "A.cpp"), read(b, "A.cpp"))
        assertEquals("#pragma once\n", read(b, "lib/util.h"))

        // правка на B -> попадает на A
        write(b, "A.cpp", "// edited on B\n")
        write(b, "B.cpp", "int main(){}\n")
        assertEquals(2, engine("B").sync(b).uploaded)
        val r3 = engine("A").sync(a)
        assertEquals(2, r3.downloaded)
        assertEquals("// edited on B\n", read(a, "A.cpp"))
        assertEquals("int main(){}\n", read(a, "B.cpp"))

        // повторная синхронизация — без изменений
        assertFalse(engine("A").sync(a).changedAnything)

        // удаление на A -> удаляется на B (в корзину .cpsync/trash)
        Files.delete(a.resolve("lib/util.h"))
        assertEquals(1, engine("A").sync(a).deletedRemote)
        assertEquals(1, engine("B").sync(b).deletedLocal)
        assertFalse(Files.exists(b.resolve("lib/util.h")))
        assertFalse("пустая папка lib должна удалиться", Files.exists(b.resolve("lib")))
        assertTrue(Files.walk(b.resolve(".cpsync/trash")).anyMatch { it.fileName.toString() == "util.h" })

        // конфликт: оба меняют A.cpp; у B версия новее
        write(a, "A.cpp", "// version A\n")
        Files.setLastModifiedTime(a.resolve("A.cpp"), java.nio.file.attribute.FileTime.fromMillis(System.currentTimeMillis() - 60_000))
        write(b, "A.cpp", "// version B (newer)\n")
        engine("A").sync(a) // A успел первым
        val rc = engine("B").sync(b) // B видит конфликт, его версия новее -> побеждает
        assertEquals(listOf("A.cpp"), rc.conflicts)
        assertEquals("// version B (newer)\n", read(b, "A.cpp"))
        assertNotNull(rc.conflictDir)
        assertTrue(Files.walk(rc.conflictDir!!).anyMatch { it.fileName.toString() == "A.cpp.server" })
        engine("A").sync(a)
        assertEquals("// version B (newer)\n", read(a, "A.cpp"))

        // проект удалили с сервера -> следующая синхронизация заливает заново, ничего не удаляя локально
        api("A").deleteProject("Олимп")
        val rr = engine("A").sync(a)
        assertTrue(rr.uploaded >= 3)
        assertEquals(0, rr.deletedLocal)
        // имя устройства (из входа) записывается как автор изменения
        api("x").upload("Олимп", "name.txt", "x".toByteArray(), "", 0)
        assertEquals("Ноутбук с CLion", api("x").projects()[0]["updatedBy"])
        println("sync OK: " + api("A").manifest("Олимп")!!.live.keys)
    }

    @Test
    fun accountsAndLinks() {
        val base = "http://127.0.0.1:$port"
        // неверный пароль
        val e = try {
            Api.authenticate(base, "login", mapOf("login" to "tester", "password" to "wrong"))
            null
        } catch (x: ApiException) {
            x
        }
        assertEquals(401, e!!.status)
        assertEquals("Неверный логин или пароль", e.message)
        // занятый логин
        val e2 = try {
            Api.authenticate(base, "register", mapOf("login" to "TESTER", "password" to "secret1"))
            null
        } catch (x: ApiException) {
            x
        }
        assertEquals("Такой логин уже занят", e2!!.message)
        // ссылка для входа (как из окна «Подключить телефон» / с сайта)
        val link = api("a").linkCode()
        val url = link["url"].jStr()
        val parsed = Api.parseLink("  $url  ")!!
        assertEquals(base, parsed.first)
        val (tok2, login) = Api.authenticate(parsed.first, "link", mapOf("code" to parsed.second, "kind" to "ide"))
        assertEquals("tester", login)
        assertEquals(api("a").projects().size, Api(base, tok2, "b", "b").projects().size)
        // QR-картинка
        val png = api("a").bytes(api("a").linkCode()["qrPng"].jStr())
        assertTrue(png.size > 100 && png[1] == 'P'.code.toByte())
        // выход отзывает токен
        Api(base, tok2, "b", "b").logout()
        val e3 = try {
            Api(base, tok2, "b", "b").projects()
            null
        } catch (x: ApiException) {
            x
        }
        assertEquals(401, e3!!.status)
        assertEquals(null, Api.parseLink("https://example.com/просто/ссылка"))
        assertEquals("https://host.example" to "ABCD-EF23", Api.parseLink("https://host.example/#/link/ABCD-EF23"))
        assertEquals("https://h.sslip.io", Api.normalizeServer("h.sslip.io/"))
        println("accounts OK")
    }
}
