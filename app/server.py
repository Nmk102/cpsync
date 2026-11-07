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
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from managebac import LoginError, ManageBac

SCHOOL = os.environ.get("MB_SCHOOL", "theislandprivateschool")
DATA = Path(os.environ.get("DATA_DIR", "/data"))
STATIC = Path(__file__).parent / "static"
STALE_MIN = int(os.environ.get("STALE_MINUTES", "20"))        # обновлять при открытии, если старше
BACKGROUND_MIN = int(os.environ.get("BACKGROUND_MINUTES", "120"))  # фоновое обновление
COOKIE = "grades_session"

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


def _h(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


# ---------------------------------------------------------------- синхронизация

def sync_user(email: str):
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
    finally:
        _syncing.discard(email)
        lock.release()


def sync_async(email: str):
    if email in _syncing:
        return
    threading.Thread(target=sync_user, args=(email,), daemon=True).start()


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


# ---------------------------------------------------------------- HTTP

class Handler(BaseHTTPRequestHandler):
    server_version = "grades/1"

    def log_message(self, fmt, *args):
        if "/api/" in (args[0] if args else ""):
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
        return self._static(path)

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
            sync_async(email)
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
        self.wfile.write(data)


def main():
    threading.Thread(target=background_loop, daemon=True).start()
    port = int(os.environ.get("PORT", "8080"))
    print(f"grades: http://0.0.0.0:{port}  (школа {SCHOOL})", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
