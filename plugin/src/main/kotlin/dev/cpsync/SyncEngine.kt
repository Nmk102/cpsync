package dev.cpsync

import java.io.IOException
import java.nio.charset.StandardCharsets.UTF_8
import java.nio.file.FileVisitResult
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.SimpleFileVisitor
import java.nio.file.StandardCopyOption
import java.nio.file.attribute.BasicFileAttributes
import java.security.MessageDigest
import java.text.SimpleDateFormat
import java.util.Date
import java.util.concurrent.ConcurrentHashMap

/** Какие файлы не синхронизируем. */
object FileRules {
    const val MAX_FILE_BYTES = 1_000_000L
    const val MAX_FILES = 3000

    private val dirNames = setOf(
        ".idea", ".git", ".svn", ".hg", ".cpsync", ".vs", ".vscode", ".fleet", ".gradle", ".cache",
        "node_modules", "__pycache__", "venv", ".venv", "build", "out", "bin", "obj",
    )
    private val fileExts = setOf(
        "exe", "o", "obj", "out", "a", "lib", "so", "dylib", "dll", "pdb", "ilk", "exp",
        "class", "pyc", "gch", "pch", "swp", "tmp",
    )
    private val fileNames = setOf(".DS_Store", "Thumbs.db", "desktop.ini")

    fun globToRegex(glob: String): Regex {
        val sb = StringBuilder()
        for (c in glob) {
            when (c) {
                '*' -> sb.append(".*")
                '?' -> sb.append('.')
                else -> sb.append(Regex.escape(c.toString()))
            }
        }
        return Regex(sb.toString(), RegexOption.IGNORE_CASE)
    }

    class Rules(extra: List<String>) {
        private val extraRx = extra.map { globToRegex(it) }

        fun skipDir(name: String): Boolean =
            name in dirNames || name.startsWith("cmake-build-") || extraRx.any { it.matches(name) }

        fun skipFile(name: String): Boolean {
            if (name in fileNames || name.endsWith("~")) return true
            val ext = name.substringAfterLast('.', "").lowercase()
            if (ext in fileExts) return true
            return extraRx.any { it.matches(name) }
        }

        /** Проверка относительного пути вида a/b/c.cpp. */
        fun skipPath(rel: String): Boolean {
            val parts = rel.split('/')
            for (i in 0 until parts.size - 1) if (skipDir(parts[i])) return true
            return skipFile(parts.last())
        }
    }

    fun looksBinary(data: ByteArray): Boolean {
        val n = minOf(data.size, 8000)
        for (i in 0 until n) if (data[i] == 0.toByte()) return true
        return false
    }
}

fun sha256(data: ByteArray): String {
    val d = MessageDigest.getInstance("SHA-256").digest(data)
    val sb = StringBuilder(64)
    for (b in d) sb.append(String.format("%02x", b))
    return sb.toString()
}

fun relPath(root: Path, file: Path): String = root.relativize(file).joinToString("/") { it.toString() }

/** .cpsync/link.json: к какому проекту на сервере привязана папка + последнее согласованное состояние. */
class LinkInfo(var project: String, val base: MutableMap<String, String>)

object Link {
    fun dir(root: Path): Path = root.resolve(".cpsync")
    private fun file(root: Path): Path = dir(root).resolve("link.json")

    fun read(root: Path): LinkInfo? {
        val f = file(root)
        if (!Files.isRegularFile(f)) return null
        return try {
            val m = Json.parse(String(Files.readAllBytes(f), UTF_8)).jObj()
            val base = LinkedHashMap<String, String>()
            for ((k, v) in m["base"].jObj()) base[k] = v.jStr()
            val p = m["project"].jStr()
            if (p.isBlank()) null else LinkInfo(p, base)
        } catch (e: Exception) {
            null
        }
    }

    fun write(root: Path, info: LinkInfo) {
        val d = dir(root)
        Files.createDirectories(d)
        val gi = d.resolve(".gitignore")
        if (!Files.exists(gi)) Files.write(gi, "*\n".toByteArray())
        val tmp = d.resolve("link.json.tmp")
        Files.write(tmp, Json.stringify(mapOf("project" to info.project, "base" to info.base)).toByteArray(UTF_8))
        Files.move(tmp, file(root), StandardCopyOption.REPLACE_EXISTING)
    }

    fun remove(root: Path) {
        Files.deleteIfExists(file(root))
    }
}

class SyncResult {
    var uploaded = 0
    var downloaded = 0
    var deletedLocal = 0
    var deletedRemote = 0
    val conflicts = mutableListOf<String>()
    var conflictDir: Path? = null
    val changedLocal get() = downloaded + deletedLocal > 0
    val changedAnything get() = uploaded + downloaded + deletedLocal + deletedRemote > 0 || conflicts.isNotEmpty()

    fun summary(): String {
        val p = mutableListOf<String>()
        if (uploaded > 0) p += "отправлено $uploaded"
        if (downloaded > 0) p += "получено $downloaded"
        if (deletedRemote > 0) p += "удалено на сервере $deletedRemote"
        if (deletedLocal > 0) p += "удалено локально $deletedLocal"
        if (conflicts.isNotEmpty()) p += "конфликтов ${conflicts.size}"
        return if (p.isEmpty()) "без изменений" else p.joinToString(", ")
    }
}

/**
 * Трёхсторонняя синхронизация папки с проектом на сервере:
 * base (последнее согласованное состояние) / локальные файлы / сервер.
 */
class SyncEngine(private val api: Api, private val rules: FileRules.Rules) {

    private class Local(val file: Path, val hash: String, val size: Long, val mtime: Long)

    companion object {
        /** кэш хэшей: путь -> (размер, mtime, хэш), чтобы не перечитывать неизменённые файлы */
        private val hashCache = ConcurrentHashMap<String, Triple<Long, Long, String>>()
        private val stampFmt = SimpleDateFormat("yyyyMMdd-HHmmss")
    }

    fun sync(rootPath: Path): SyncResult {
        val root = rootPath.toAbsolutePath().normalize()
        var attempt = 0
        while (true) {
            try {
                return syncOnce(root)
            } catch (e: ApiException) {
                // 409: кто-то успел изменить файл между чтением манифеста и отправкой — повторяем
                if (e.status != 409 || ++attempt >= 4) throw e
            }
        }
    }

    private fun scan(root: Path): Map<String, Local> {
        val out = LinkedHashMap<String, Local>()
        Files.walkFileTree(root, object : SimpleFileVisitor<Path>() {
            override fun preVisitDirectory(dir: Path, attrs: BasicFileAttributes): FileVisitResult {
                if (dir != root && rules.skipDir(dir.fileName.toString())) return FileVisitResult.SKIP_SUBTREE
                return FileVisitResult.CONTINUE
            }

            override fun visitFile(file: Path, attrs: BasicFileAttributes): FileVisitResult {
                if (!attrs.isRegularFile || attrs.size() > FileRules.MAX_FILE_BYTES) return FileVisitResult.CONTINUE
                if (rules.skipFile(file.fileName.toString())) return FileVisitResult.CONTINUE
                if (out.size >= FileRules.MAX_FILES) {
                    throw IOException("В папке больше ${FileRules.MAX_FILES} файлов — похоже, выбрана не та папка")
                }
                val mtime = attrs.lastModifiedTime().toMillis()
                val key = file.toAbsolutePath().toString()
                val cached = hashCache[key]
                val hash = if (cached != null && cached.first == attrs.size() && cached.second == mtime) {
                    cached.third
                } else {
                    val data = try {
                        Files.readAllBytes(file)
                    } catch (e: IOException) {
                        return FileVisitResult.CONTINUE
                    }
                    if (FileRules.looksBinary(data)) "" else sha256(data).also {
                        hashCache[key] = Triple(attrs.size(), mtime, it)
                    }
                }
                if (hash.isNotEmpty()) out[relPath(root, file)] = Local(file, hash, attrs.size(), mtime)
                return FileVisitResult.CONTINUE
            }

            override fun visitFileFailed(file: Path, exc: IOException): FileVisitResult = FileVisitResult.CONTINUE
        })
        return out
    }

    private fun syncOnce(root: Path): SyncResult {
        val link = Link.read(root) ?: throw IOException("Папка не привязана к проекту на сервере")
        val res = SyncResult()
        val project = link.project
        val remoteManifest = api.manifest(project)
        if (remoteManifest == null && link.base.isNotEmpty()) {
            // проекта на сервере нет (удалён или сервер начисто переустановлен) — заливаем заново, ничего не удаляя
            link.base.clear()
        }
        val remote = remoteManifest?.live ?: emptyMap()
        val remoteAll = remoteManifest?.files ?: emptyMap()
        val local = scan(root)
        val base = link.base
        val stamp = stampFmt.format(Date())

        val paths = (base.keys + local.keys + remote.keys).toSortedSet()
        try {
            for (p in paths) {
                if (rules.skipPath(p)) continue
                val b = base[p]
                val l = local[p]?.hash
                val r = remote[p]?.hash
                when {
                    l == r -> if (l == null) base.remove(p) else base[p] = l

                    l == b -> { // локально не меняли, изменилось на сервере
                        if (r == null) {
                            moveAside(root, p, "trash", stamp)
                            base.remove(p)
                            res.deletedLocal++
                        } else {
                            writeLocal(root, p, fetch(project, p, r))
                            base[p] = r
                            res.downloaded++
                        }
                    }

                    r == b -> { // на сервере не меняли, изменилось локально
                        if (l == null) {
                            api.delete(project, p, b ?: "")
                            base.remove(p)
                            res.deletedRemote++
                        } else {
                            upload(project, p, local.getValue(p), b ?: "")
                            base[p] = l
                            res.uploaded++
                        }
                    }

                    else -> { // изменили с обеих сторон
                        when {
                            l == null -> { // удалили у нас, но изменили на сервере — изменение важнее
                                writeLocal(root, p, fetch(project, p, r!!))
                                base[p] = r
                                res.downloaded++
                            }
                            r == null -> { // удалили на сервере, но изменили у нас
                                val curRemote = remoteAll[p]?.hash ?: ""
                                upload(project, p, local.getValue(p), curRemote)
                                base[p] = l
                                res.uploaded++
                            }
                            else -> {
                                val lf = local.getValue(p)
                                val rf = remote.getValue(p)
                                if (lf.mtime >= rf.mtime) {
                                    // побеждает локальная версия, серверную сохраняем рядом
                                    saveConflictCopy(root, p, fetch(project, p, r), "server", stamp, res)
                                    upload(project, p, lf, r)
                                    base[p] = l
                                    res.uploaded++
                                } else {
                                    saveConflictCopy(root, p, Files.readAllBytes(lf.file), "local", stamp, res)
                                    writeLocal(root, p, fetch(project, p, r))
                                    base[p] = r
                                    res.downloaded++
                                }
                                res.conflicts += p
                            }
                        }
                    }
                }
            }
        } finally {
            Link.write(root, link)
        }
        return res
    }

    private fun fetch(project: String, path: String, expectedHash: String): ByteArray {
        val data = try {
            api.blob(expectedHash)
        } catch (e: ApiException) {
            if (e.status != 404) throw e
            api.download(project, path)
        }
        return data
    }

    private fun upload(project: String, path: String, lf: Local, base: String) {
        val data = Files.readAllBytes(lf.file)
        if (sha256(data) != lf.hash) throw ApiException(409, "файл изменился во время синхронизации")
        api.upload(project, path, data, base, lf.mtime)
    }

    private fun writeLocal(root: Path, rel: String, data: ByteArray) {
        val target = root.resolve(rel.replace('/', java.io.File.separatorChar)).normalize()
        if (!target.startsWith(root)) throw IOException("Недопустимый путь: $rel")
        Files.createDirectories(target.parent)
        val tmp = target.resolveSibling(".${target.fileName}.cpsync-tmp")
        Files.write(tmp, data)
        try {
            Files.move(tmp, target, StandardCopyOption.REPLACE_EXISTING, StandardCopyOption.ATOMIC_MOVE)
        } catch (e: IOException) {
            Files.move(tmp, target, StandardCopyOption.REPLACE_EXISTING)
        }
        hashCache.remove(target.toAbsolutePath().toString())
    }

    private fun moveAside(root: Path, rel: String, kind: String, stamp: String) {
        val src = root.resolve(rel.replace('/', java.io.File.separatorChar)).normalize()
        if (!src.startsWith(root) || !Files.exists(src)) return
        val dst = Link.dir(root).resolve(kind).resolve(stamp).resolve(rel.replace('/', java.io.File.separatorChar))
        Files.createDirectories(dst.parent)
        Files.move(src, dst, StandardCopyOption.REPLACE_EXISTING)
        // убираем опустевшие папки
        var d = src.parent
        while (d != null && d != root && d.startsWith(root)) {
            val empty = Files.list(d).use { !it.findAny().isPresent }
            if (!empty) break
            Files.delete(d)
            d = d.parent
        }
    }

    private fun saveConflictCopy(root: Path, rel: String, data: ByteArray, who: String, stamp: String, res: SyncResult) {
        val dir = Link.dir(root).resolve("conflicts").resolve(stamp)
        val dst = dir.resolve("$rel.$who".replace('/', java.io.File.separatorChar))
        Files.createDirectories(dst.parent)
        Files.write(dst, data)
        res.conflictDir = dir
    }
}
