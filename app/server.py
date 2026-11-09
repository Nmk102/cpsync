"""Сайт с оценками из ManageBac: вход тем же логином/паролем, таблица всех заданий."""
from __future__ import annotations

import hashlib
import json
import mimetypes
import os
import secrets
import threading
import time
import traceback
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from managebac import LoginError, ManageBac

SCHOOL = os.environ.get("MB_SCHOOL", "theislandprivateschool")
DATA = Path(os.environ.get("DATA_DIR", "/data"))
STATIC = Path(__file__).parent / "static"
STALE_MIN = int(os.environ.get("STALE_MINUTES", "20"))        # обновлять при открытии, если старше
BACKGROUND_MIN = int(os.environ.get("BACKGROUND_MINUTES", "120"))  # фоновое обновление
COOKIE = "grades_session"
CONTENT = Path(__file__).parent / "content"

DATA.mkdir(parents=True, exist_ok=True)
(DATA / "cache").mkdir(exist_ok=True)
os.chmod(DATA, 0o700)

_lock = threading.Lock()
_sync_locks: dict[str, threading.Lock] = {}
_syncing: set[str] = set()
_login_attempts: dict[str, list[float]] = {}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read(path: Path, default):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _write(path: Path, obj):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False))
    os.chmod(tmp, 0o600)
    tmp.replace(path)


def users() -> dict:
    return _read(DATA / "users.json", {})


def sessions() -> dict:
    return _read(DATA / "sessions.json", {})


def cache_path(email: str) -> Path:
    return DATA / "cache" / (hashlib.sha256(email.encode()).hexdigest()[:24] + ".json")


def mat_path(email: str) -> Path:
    return DATA / "cache" / (hashlib.sha256(email.encode()).hexdigest()[:24] + ".mat.json")


def _h(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


# ---------------------------------------------------------------- синхронизация

def sync_user(email: str, force: bool = False):
    lock = _sync_locks.setdefault(email, threading.Lock())
    if not lock.acquire(blocking=False):
        return
    _syncing.add(email)
    try:
        u = users().get(email)
        if not u:
            return
        path = cache_path(email)
        old = _read(path, {})
        try:
            mb = ManageBac(SCHOOL, u["login"], u["password"])
            mb.login()
            data = mb.fetch_all()
        except LoginError:
            old["error"] = "ManageBac больше не принимает сохранённый пароль. Выйдите и войдите заново с новым паролем."
            old["error_kind"] = "login"
            _write(path, old)
            return
        except Exception as e:  # сеть, изменения вёрстки и т.п.
            traceback.print_exc()
            old["error"] = f"Не удалось обновить данные: {e}"
            old["error_kind"] = "other"
            _write(path, old)
            return

        # когда оценка впервые появилась — чтобы подсвечивать новые
        first_seen = old.get("graded_seen", {})
        initial = not old.get("tasks")
        stamp = now_iso()
        for t in data["tasks"]:
            key = f'{t["class_id"]}:{t["id"]}'
            sig = json.dumps(t["grade"], sort_keys=True) if t["grade"]["type"] == "graded" else ""
            prev = first_seen.get(key)
            if sig and (not prev or prev.get("sig") != sig):
                first_seen[key] = {"sig": sig, "at": "" if initial else stamp}
            t["graded_at"] = first_seen.get(key, {}).get("at", "") if sig else ""

        data.update({"fetched_at": stamp, "error": "", "error_kind": "", "graded_seen": first_seen})
        _write(path, data)
        print(f"[sync] {email}: {len(data['tasks'])} заданий", flush=True)

        # материалы предметов (юниты, описания заданий, файлы) — отдельно, чтобы сбой не мешал оценкам
        try:
            mp = mat_path(email)
            mat = mb.fetch_materials(data["classes"], data["tasks"], _read(mp, {}), force=force)
            _write(mp, mat)
            print(f"[sync] {email}: материалы {len(mat['tasks'])} заданий, {len(mat['units'])} юнитов", flush=True)
        except Exception:
            traceback.print_exc()
    finally:
        _syncing.discard(email)
        lock.release()


def sync_async(email: str, force: bool = False):
    if email in _syncing:
        return
    threading.Thread(target=sync_user, args=(email, force), daemon=True).start()


def background_loop():
    while True:
        time.sleep(BACKGROUND_MIN * 60)
        for email in list(users()):
            try:
                sync_user(email)
            except Exception:
                traceback.print_exc()


def is_stale(cache: dict) -> bool:
    ts = cache.get("fetched_at")
    if not ts:
        return True
    age = datetime.now(timezone.utc) - datetime.fromisoformat(ts)
    return age.total_seconds() > STALE_MIN * 60


# ---------------------------------------------------------------- конспекты (app/content/<class_id>/*.md)

def _front_matter(text: str) -> tuple[dict, str]:
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            for line in text[3:end].strip().splitlines():
                k, _, v = line.partition(":")
                k, v = k.strip(), v.strip()
                if not k:
                    continue
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
                elif len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
                    v = v[1:-1]
                meta[k] = v
            text = text[end + 4:].lstrip("\n")
    return meta, text


def _as_list(v) -> list:
    if not v:
        return []
    return [str(x) for x in v] if isinstance(v, list) else [str(v)]


def notes_index() -> dict:
    """{class_id: [ {slug, title, summary, units, tasks, order, kind} ]}"""
    out: dict[str, list] = {}
    if not CONTENT.is_dir():
        return out
    for d in sorted(CONTENT.iterdir()):
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            meta, _ = _front_matter(f.read_text())
            out.setdefault(d.name, []).append({
                "slug": f.stem,
                "title": meta.get("title", f.stem),
                "summary": meta.get("summary", ""),
                "kind": meta.get("kind", "notes"),
                "units": _as_list(meta.get("units")),
                "tasks": _as_list(meta.get("tasks")),
                "order": float(meta.get("order", 100) or 100),
            })
        out.get(d.name, []).sort(key=lambda n: (n["order"], n["title"]))
    return out


NOTES = notes_index()


def file_url(f: dict, mat: dict) -> str:
    if f["url"].startswith("/attachments/"):
        sg = mat.get("signed", {}).get(f.get("asset", ""))
        return sg["url"] if sg else f"https://{SCHOOL}.managebac.com{f['url']}"
    return f["url"]


def pending_notes(tasks: list) -> list:
    """Свежие задания с файлами учителя, к которым ещё нет конспекта/разбора."""
    since = (datetime.now() - timedelta(days=14)).isoformat(timespec="minutes")
    return [t for t in tasks if t.get("files") and not t.get("notes") and (t.get("date") or "") >= since]


def subject_payload(cache: dict, mat: dict, cid: str) -> dict | None:
    cls = next((c for c in cache.get("classes", []) if c["id"] == cid), None)
    if not cls:
        return None
    cm = mat.get("classes", {}).get(cid, {})
    units = [{**u, "info": mat.get("units", {}).get(u["id"], {}).get("info", {})} for u in cm.get("units", [])]
    # юниты, к которым привязаны задания (могут отсутствовать в списке юнитов класса) + дата последнего задания
    by_id = {u["id"]: u for u in units}
    for t in cache.get("tasks", []):
        if t["class_id"] != cid:
            continue
        d = mat.get("tasks", {}).get(f'{cid}:{t["id"]}', {})
        uid = d.get("unit_id")
        if not uid:
            continue
        if uid not in by_id:
            by_id[uid] = {"id": uid, "title": d.get("unit_title", ""), "start": "", "duration": "", "current": False,
                          "info": mat.get("units", {}).get(uid, {}).get("info", {}), "extra": True}
            units.append(by_id[uid])
        if t.get("date") and t["date"] > by_id[uid].get("last_task", ""):
            by_id[uid]["last_task"] = t["date"]
    notes = NOTES.get(cid, [])
    by_task: dict[str, list] = {}
    for n in notes:
        for t in n["tasks"]:
            by_task.setdefault(t, []).append(n["slug"])
    tasks = []
    for t in cache.get("tasks", []):
        if t["class_id"] != cid:
            continue
        d = mat.get("tasks", {}).get(f'{cid}:{t["id"]}', {})
        tasks.append({**t, "description_html": d.get("description_html", ""),
                      "files": [{**f, "url": file_url(f, mat)} for f in d.get("files", [])],
                      "links": d.get("links", []), "unit_id": d.get("unit_id", ""),
                      "unit_title": d.get("unit_title", ""), "notes": by_task.get(str(t["id"]), [])})
    pend = {t["id"] for t in pending_notes(tasks)}
    for t in tasks:
        t["needs_notes"] = t["id"] in pend
    return {"class": cls, "units": units, "tasks": tasks, "files": cm.get("files", []), "notes": notes,
            "materials_at": mat.get("fetched_at"), "school_url": f"https://{SCHOOL}.managebac.com"}


# ---------------------------------------------------------------- HTTP

class Handler(BaseHTTPRequestHandler):
    server_version = "grades/1"

    def log_message(self, fmt, *args):
        if args and "/api/" in str(args[0]):
            super().log_message(fmt, *args)

    # --- helpers
    def _json(self, code: int, obj, cookie: str | None = None):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        if cookie is not None:
            self.send_header("Set-Cookie", cookie)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if not getattr(self, "_head_only", False):
            self.wfile.write(body)

    def _body(self) -> dict:
        n = int(self.headers.get("Content-Length") or 0)
        if n > 10_000:
            return {}
        try:
            return json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            return {}

    def _token(self) -> str:
        for part in (self.headers.get("Cookie") or "").split(";"):
            k, _, v = part.strip().partition("=")
            if k == COOKIE:
                return v
        return ""

    def _user(self) -> str | None:
        tok = self._token()
        if not tok:
            return None
        s = sessions().get(_h(tok))
        if s and s["email"] in users():
            return s["email"]
        return None

    def _ip(self) -> str:
        return (self.headers.get("X-Forwarded-For") or self.client_address[0]).split(",")[0].strip()

    # --- routes
    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/healthz":
            return self._json(200, {"ok": True})
        if path == "/api/data":
            email = self._user()
            if not email:
                return self._json(401, {"error": "auth"})
            cache = _read(cache_path(email), {})
            if email not in _syncing and is_stale(cache) and cache.get("error_kind") != "login":
                sync_async(email)
            cache.pop("graded_seen", None)
            cache["syncing"] = email in _syncing
            cache["school_url"] = f"https://{SCHOOL}.managebac.com"
            return self._json(200, cache)
        if path == "/api/subjects":
            email = self._user()
            if not email:
                return self._json(401, {"error": "auth"})
            cache, mat = _read(cache_path(email), {}), _read(mat_path(email), {})
            out, now = [], datetime.now().isoformat(timespec="minutes")
            for c in cache.get("classes", []):
                cm = mat.get("classes", {}).get(c["id"], {})
                ts = [t for t in cache.get("tasks", []) if t["class_id"] == c["id"]]
                up = sorted((t for t in ts if (t.get("date") or "") >= now), key=lambda t: t["date"])
                sp = subject_payload(cache, mat, c["id"]) or {"units": [], "tasks": []}
                pending = pending_notes(sp["tasks"])
                out.append({**c, "units": [{k: u.get(k) for k in ("id", "title", "start", "current", "last_task")}
                                           for u in sp["units"]],
                            "tasks": len(ts), "notes": len(NOTES.get(c["id"], [])),
                            "pending": [{"id": t["id"], "title": t["title"], "date": t["date"]} for t in pending],
                            "upcoming": [{"title": t["title"], "date": t["date"], "kind": t["kind"]} for t in up[:3]]})
            return self._json(200, {"subjects": out, "materials_at": mat.get("fetched_at"),
                                    "syncing": email in _syncing})
        if path.startswith("/api/subject/"):
            email = self._user()
            if not email:
                return self._json(401, {"error": "auth"})
            p = subject_payload(_read(cache_path(email), {}), _read(mat_path(email), {}), path.rsplit("/", 1)[-1])
            if p is not None:
                p["syncing"] = email in _syncing
            return self._json(200, p) if p else self._json(404, {"error": "not found"})
        if path.startswith("/api/note/"):
            if not self._user():
                return self._json(401, {"error": "auth"})
            parts = path.split("/")
            if len(parts) != 5 or not parts[3].isdigit() or not parts[4] or \
                    not all(c.isalnum() or c in "-_" for c in parts[4]):
                return self._json(404, {"error": "not found"})
            f = CONTENT / parts[3] / (parts[4] + ".md")
            if not f.is_file():
                return self._json(404, {"error": "not found"})
            meta, body = _front_matter(f.read_text())
            return self._json(200, {"meta": meta, "markdown": body})
        return self._static(path)

    def do_HEAD(self):
        # как GET, но без тела (нужно некоторым сервисам предпросмотра ссылок)
        self._head_only = True
        try:
            self.do_GET()
        finally:
            self._head_only = False

    def do_POST(self):
        path = self.path.split("?")[0]
        if self.headers.get("X-Requested-With") != "grades":
            return self._json(403, {"error": "bad request"})
        if path == "/api/login":
            return self._login()
        if path == "/api/logout":
            tok = self._token()
            if tok:
                with _lock:
                    s = sessions()
                    s.pop(_h(tok), None)
                    _write(DATA / "sessions.json", s)
            return self._json(200, {"ok": True}, cookie=f"{COOKIE}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax")
        if path == "/api/refresh":
            email = self._user()
            if not email:
                return self._json(401, {"error": "auth"})
            sync_async(email, force=True)
            return self._json(200, {"ok": True})
        self._json(404, {"error": "not found"})

    def _login(self):
        ip = self._ip()
        tries = [t for t in _login_attempts.get(ip, []) if t > time.time() - 900]
        if len(tries) >= 8:
            return self._json(429, {"error": "Слишком много попыток. Подождите 15 минут."})
        tries.append(time.time())
        _login_attempts[ip] = tries

        b = self._body()
        login, password = (b.get("login") or "").strip(), b.get("password") or ""
        if not login or not password:
            return self._json(400, {"error": "Введите почту и пароль от ManageBac."})
        try:
            ManageBac(SCHOOL, login, password).login()
        except LoginError:
            return self._json(401, {"error": "ManageBac не принял почту или пароль."})
        except Exception as e:
            traceback.print_exc()
            return self._json(502, {"error": f"ManageBac сейчас недоступен: {e}"})

        email = login.lower()
        tok = secrets.token_urlsafe(32)
        with _lock:
            u = users()
            u[email] = {"login": login, "password": password, "updated": now_iso()}
            _write(DATA / "users.json", u)
            s = sessions()
            s[_h(tok)] = {"email": email, "created": now_iso()}
            _write(DATA / "sessions.json", s)
        c = _read(cache_path(email), {})
        if c.get("error_kind") == "login":
            c["error"] = c["error_kind"] = ""
            _write(cache_path(email), c)
        sync_async(email)
        _login_attempts.pop(ip, None)
        cookie = f"{COOKIE}={tok}; Path=/; Max-Age=31536000; HttpOnly; Secure; SameSite=Lax"
        return self._json(200, {"ok": True}, cookie=cookie)

    def _static(self, path: str):
        if path in ("", "/"):
            path = "/index.html"
        f = (STATIC / path.lstrip("/")).resolve()
        if STATIC.resolve() not in f.parents or not f.is_file():
            f = STATIC / "index.html"
        data = f.read_bytes()
        if f.name == "index.html":  # превью ссылок в мессенджерах требует полный адрес картинки
            host = (self.headers.get("Host") or "").split(",")[0].strip()
            if host and all(c.isalnum() or c in ".-:" for c in host):
                data = data.replace(b'content="/preview.png"', f'content="https://{host}/preview.png"'.encode())
        ctype = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/javascript", "application/json"):
            ctype += "; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if not getattr(self, "_head_only", False):
            self.wfile.write(data)


def main():
    threading.Thread(target=background_loop, daemon=True).start()
    port = int(os.environ.get("PORT", "8080"))
    print(f"grades: http://0.0.0.0:{port}  (школа {SCHOOL})", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
