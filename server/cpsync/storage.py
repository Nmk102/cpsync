"""Хранилище CP Sync: SQLite (пользователи, токены, проекты, файлы, тесты) + содержимое файлов на диске."""

import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import threading
import time
import uuid

MAX_FILE_BYTES = 1024 * 1024
MAX_PROJECTS_PER_USER = 300
MAX_FILES_PER_PROJECT = 3000
MAX_USER_BYTES = 300 * 1024 * 1024
LINK_CODE_TTL = 10 * 60

LOGIN_RE = re.compile(r'^[A-Za-z0-9_.\-]{3,32}$')
PROJECT_NAME_RE = re.compile(r'^[^/\\:*?"<>|\x00-\x1f]{1,100}$')

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    login TEXT NOT NULL UNIQUE COLLATE NOCASE,
    pw TEXT NOT NULL,
    created INTEGER NOT NULL,
    is_admin INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS tokens(
    hash TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    kind TEXT NOT NULL,
    created INTEGER NOT NULL,
    last_seen INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS link_codes(
    code TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    expires INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    revision INTEGER NOT NULL DEFAULT 0,
    created INTEGER NOT NULL,
    updated INTEGER NOT NULL,
    updated_by TEXT NOT NULL DEFAULT '',
    UNIQUE(user_id, name)
);
CREATE TABLE IF NOT EXISTS files(
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    path TEXT NOT NULL,
    hash TEXT NOT NULL,
    size INTEGER NOT NULL,
    mtime INTEGER NOT NULL,
    deleted INTEGER NOT NULL,
    rev INTEGER NOT NULL,
    by TEXT NOT NULL,
    PRIMARY KEY(project_id, path)
);
CREATE INDEX IF NOT EXISTS files_hash ON files(hash);
CREATE TABLE IF NOT EXISTS tests(
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    path TEXT NOT NULL,
    data TEXT NOT NULL,
    updated INTEGER NOT NULL,
    PRIMARY KEY(project_id, path)
);
"""


def now_ms():
    return int(time.time() * 1000)


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


class ApiError(Exception):
    def __init__(self, status, message, extra=None):
        super().__init__(message)
        self.status = status
        self.message = message
        self.extra = extra or {}


def valid_project_name(name):
    return bool(name) and isinstance(name, str) and PROJECT_NAME_RE.match(name) \
        and not name.startswith('.') and name.strip() == name


def normalize_path(path):
    """Относительный путь внутри проекта с '/' или None."""
    if not path or not isinstance(path, str) or len(path) > 400 or '\\' in path or '\x00' in path:
        return None
    if path.startswith('/') or re.match(r'^[A-Za-z]:', path):
        return None
    parts = path.split('/')
    if len(parts) > 40:
        return None
    for p in parts:
        if p in ('', '.', '..'):
            return None
    return path


def hash_password(pw):
    salt = secrets.token_bytes(16)
    h = hashlib.scrypt(pw.encode('utf-8'), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    return 'scrypt$%s$%s' % (salt.hex(), h.hex())


def check_password(pw, stored):
    try:
        kind, salt, h = stored.split('$')
        if kind != 'scrypt':
            return False
        got = hashlib.scrypt(pw.encode('utf-8'), salt=bytes.fromhex(salt), n=2 ** 14, r=8, p=1, dklen=32)
        return hmac.compare_digest(got.hex(), h)
    except Exception:
        return False


class Storage:
    def __init__(self, root):
        self.root = root
        self.blob_dir = os.path.join(root, 'blobs')
        os.makedirs(self.blob_dir, exist_ok=True)
        self.lock = threading.RLock()
        self.db = sqlite3.connect(os.path.join(root, 'cpsync.db'), check_same_thread=False, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.executescript(SCHEMA)

    # ------------------------------------------------------------------ helpers
    def q(self, sql, args=()):
        with self.lock:
            return self.db.execute(sql, args).fetchall()

    def q1(self, sql, args=()):
        with self.lock:
            return self.db.execute(sql, args).fetchone()

    def tx(self):
        return _Tx(self)

    # ------------------------------------------------------------------ blobs
    def _blob_path(self, h):
        return os.path.join(self.blob_dir, h[:2], h)

    def put_blob(self, data):
        h = sha256_hex(data)
        p = self._blob_path(h)
        if not os.path.exists(p):
            os.makedirs(os.path.dirname(p), exist_ok=True)
            tmp = p + '.tmp' + uuid.uuid4().hex[:6]
            with open(tmp, 'wb') as f:
                f.write(data)
            os.replace(tmp, p)
        return h

    def get_blob(self, h):
        if not re.fullmatch(r'[0-9a-f]{64}', h or ''):
            return None
        try:
            with open(self._blob_path(h), 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def user_owns_blob(self, user_id, h):
        r = self.q1('SELECT 1 FROM files f JOIN projects p ON p.id = f.project_id '
                    'WHERE f.hash = ? AND p.user_id = ? LIMIT 1', (h, user_id))
        return r is not None

    # ------------------------------------------------------------------ users / auth
    def user_count(self):
        return self.q1('SELECT COUNT(*) AS n FROM users')['n']

    def create_user(self, login, password):
        if not isinstance(login, str) or not LOGIN_RE.match(login):
            raise ApiError(400, 'Логин: 3–32 символа, латинские буквы, цифры, точка, дефис или подчёркивание')
        if not isinstance(password, str) or len(password) < 6:
            raise ApiError(400, 'Пароль должен быть не короче 6 символов')
        if len(password) > 200:
            raise ApiError(400, 'Слишком длинный пароль')
        pw = hash_password(password)
        with self.lock:
            if self.q1('SELECT 1 FROM users WHERE login = ?', (login,)):
                raise ApiError(409, 'Такой логин уже занят')
            is_admin = 1 if self.user_count() == 0 else 0
            cur = self.db.execute('INSERT INTO users(login, pw, created, is_admin) VALUES (?,?,?,?)',
                                  (login, pw, now_ms(), is_admin))
            return cur.lastrowid

    def verify_user(self, login, password):
        r = self.q1('SELECT id, pw FROM users WHERE login = ?', (login or '',))
        if r is None or not check_password(password or '', r['pw']):
            raise ApiError(401, 'Неверный логин или пароль')
        return r['id']

    def set_password(self, user_id, password):
        if not isinstance(password, str) or len(password) < 6:
            raise ApiError(400, 'Пароль должен быть не короче 6 символов')
        with self.lock:
            self.db.execute('UPDATE users SET pw = ? WHERE id = ?', (hash_password(password), user_id))

    def get_user(self, user_id):
        return self.q1('SELECT id, login, created, is_admin FROM users WHERE id = ?', (user_id,))

    def issue_token(self, user_id, name, kind):
        tok = secrets.token_urlsafe(32)
        h = sha256_hex(tok.encode())
        t = now_ms()
        with self.lock:
            self.db.execute('INSERT INTO tokens(hash, user_id, name, kind, created, last_seen) VALUES (?,?,?,?,?,?)',
                            (h, user_id, (name or 'устройство')[:80], kind if kind in ('ide', 'web') else 'web', t, t))
        return tok

    def user_by_token(self, tok):
        if not tok:
            return None
        h = sha256_hex(tok.encode())
        r = self.q1('SELECT t.hash, t.user_id, t.name, t.kind, t.last_seen, u.login, u.is_admin '
                    'FROM tokens t JOIN users u ON u.id = t.user_id WHERE t.hash = ?', (h,))
        if r is None:
            return None
        if now_ms() - r['last_seen'] > 60_000:
            with self.lock:
                self.db.execute('UPDATE tokens SET last_seen = ? WHERE hash = ?', (now_ms(), h))
        return dict(r)

    def list_tokens(self, user_id):
        return [dict(id=r['hash'][:12], name=r['name'], kind=r['kind'], created=r['created'], lastSeen=r['last_seen'])
                for r in self.q('SELECT * FROM tokens WHERE user_id = ? ORDER BY last_seen DESC', (user_id,))]

    def revoke_token(self, user_id, token_id=None, token_hash=None):
        with self.lock:
            if token_hash:
                self.db.execute('DELETE FROM tokens WHERE user_id = ? AND hash = ?', (user_id, token_hash))
            else:
                self.db.execute("DELETE FROM tokens WHERE user_id = ? AND substr(hash, 1, 12) = ?", (user_id, token_id))

    def create_link_code(self, user_id):
        alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        code = ''.join(secrets.choice(alphabet) for _ in range(10))
        with self.lock:
            self.db.execute('DELETE FROM link_codes WHERE expires < ?', (now_ms(),))
            self.db.execute('INSERT INTO link_codes(code, user_id, expires) VALUES (?,?,?)',
                            (code, user_id, now_ms() + LINK_CODE_TTL * 1000))
        return code, now_ms() + LINK_CODE_TTL * 1000

    def link_code_valid(self, code):
        r = self.q1('SELECT user_id FROM link_codes WHERE code = ? AND expires >= ?', (code or '', now_ms()))
        return r is not None

    def use_link_code(self, code):
        code = (code or '').strip().upper().replace('-', '')
        with self.lock:
            r = self.db.execute('SELECT user_id FROM link_codes WHERE code = ? AND expires >= ?',
                                (code, now_ms())).fetchone()
            if r is None:
                raise ApiError(401, 'Ссылка для входа устарела или уже использована. Получите новую.')
            self.db.execute('DELETE FROM link_codes WHERE code = ?', (code,))
            return r['user_id']

    # ------------------------------------------------------------------ projects
    def _project(self, user_id, name, create=False):
        r = self.q1('SELECT * FROM projects WHERE user_id = ? AND name = ?', (user_id, name))
        if r is None and create:
            n = self.q1('SELECT COUNT(*) AS n FROM projects WHERE user_id = ?', (user_id,))['n']
            if n >= MAX_PROJECTS_PER_USER:
                raise ApiError(403, 'Слишком много проектов')
            t = now_ms()
            with self.lock:
                self.db.execute('INSERT OR IGNORE INTO projects(user_id, name, created, updated) VALUES (?,?,?,?)',
                                (user_id, name, t, t))
            r = self.q1('SELECT * FROM projects WHERE user_id = ? AND name = ?', (user_id, name))
        return r

    def project_or_404(self, user_id, name):
        r = self._project(user_id, name)
        if r is None:
            raise ApiError(404, 'Проект не найден')
        return r

    def create_project(self, user_id, name):
        if not valid_project_name(name):
            raise ApiError(400, 'Некорректное имя проекта')
        if self._project(user_id, name) is not None:
            raise ApiError(409, 'Проект с таким именем уже есть')
        return self._project(user_id, name, create=True)

    def list_projects(self, user_id):
        rows = self.q('SELECT p.*, (SELECT COUNT(*) FROM files f WHERE f.project_id = p.id AND f.deleted = 0) AS n '
                      'FROM projects p WHERE p.user_id = ? ORDER BY p.updated DESC', (user_id,))
        return [dict(name=r['name'], revision=r['revision'], updatedAt=r['updated'],
                     updatedBy=r['updated_by'], fileCount=r['n']) for r in rows]

    def manifest(self, user_id, name):
        p = self._project(user_id, name)
        if p is None:
            return None
        files = {}
        for r in self.q('SELECT * FROM files WHERE project_id = ?', (p['id'],)):
            files[r['path']] = dict(hash=r['hash'], size=r['size'], mtime=r['mtime'],
                                    deleted=bool(r['deleted']), rev=r['rev'], by=r['by'])
        return dict(name=p['name'], revision=p['revision'], files=files)

    def user_bytes(self, user_id):
        r = self.q1('SELECT COALESCE(SUM(f.size), 0) AS s FROM files f JOIN projects p ON p.id = f.project_id '
                    'WHERE p.user_id = ? AND f.deleted = 0', (user_id,))
        return r['s']

    def put_file(self, user_id, name, path, data, base, mtime, device):
        if len(data) > MAX_FILE_BYTES:
            raise ApiError(413, 'Файл больше 1 МБ')
        with self.lock:
            p = self._project(user_id, name, create=True)
            cur = self.q1('SELECT * FROM files WHERE project_id = ? AND path = ?', (p['id'], path))
            cur_hash = '' if (cur is None or cur['deleted']) else cur['hash']
            new_hash = sha256_hex(data)
            if base is not None and base != cur_hash and new_hash != cur_hash:
                raise ApiError(409, 'conflict', {'current': cur_hash})
            if new_hash == cur_hash:
                return {'hash': new_hash, 'revision': p['revision'], 'changed': False}
            if cur is None:
                n = self.q1('SELECT COUNT(*) AS n FROM files WHERE project_id = ?', (p['id'],))['n']
                if n >= MAX_FILES_PER_PROJECT:
                    raise ApiError(403, 'Слишком много файлов в проекте')
            if self.user_bytes(user_id) + len(data) > MAX_USER_BYTES:
                raise ApiError(403, 'Закончилось место (лимит 300 МБ на аккаунт)')
            self.put_blob(data)
            rev = p['revision'] + 1
            t = now_ms()
            self.db.execute('BEGIN')
            try:
                self.db.execute('INSERT OR REPLACE INTO files(project_id, path, hash, size, mtime, deleted, rev, by) '
                                'VALUES (?,?,?,?,?,0,?,?)',
                                (p['id'], path, new_hash, len(data), int(mtime or t), rev, device))
                self.db.execute('UPDATE projects SET revision = ?, updated = ?, updated_by = ? WHERE id = ?',
                                (rev, t, device, p['id']))
                self.db.execute('COMMIT')
            except Exception:
                self.db.execute('ROLLBACK')
                raise
            return {'hash': new_hash, 'revision': rev, 'changed': True}

    def delete_file(self, user_id, name, path, base, device):
        with self.lock:
            p = self._project(user_id, name)
            cur = self.q1('SELECT * FROM files WHERE project_id = ? AND path = ?', (p['id'], path)) if p else None
            if cur is None or cur['deleted']:
                return {'revision': p['revision'] if p else 0, 'changed': False}
            if base is not None and base != cur['hash']:
                raise ApiError(409, 'conflict', {'current': cur['hash']})
            rev = p['revision'] + 1
            t = now_ms()
            self.db.execute('BEGIN')
            try:
                self.db.execute("UPDATE files SET hash = '', size = 0, mtime = ?, deleted = 1, rev = ?, by = ? "
                                'WHERE project_id = ? AND path = ?', (t, rev, device, p['id'], path))
                self.db.execute('UPDATE projects SET revision = ?, updated = ?, updated_by = ? WHERE id = ?',
                                (rev, t, device, p['id']))
                self.db.execute('COMMIT')
            except Exception:
                self.db.execute('ROLLBACK')
                raise
            return {'revision': rev, 'changed': True}

    def delete_project(self, user_id, name):
        with self.lock:
            p = self._project(user_id, name)
            if p is None:
                return False
            self.db.execute('DELETE FROM projects WHERE id = ?', (p['id'],))
            return True

    def file_content(self, user_id, name, path):
        p = self.project_or_404(user_id, name)
        r = self.q1('SELECT hash, deleted FROM files WHERE project_id = ? AND path = ?', (p['id'], path))
        if r is None or r['deleted']:
            raise ApiError(404, 'Файл не найден')
        data = self.get_blob(r['hash'])
        if data is None:
            raise ApiError(500, 'Содержимое файла потеряно')
        return r['hash'], data

    # ------------------------------------------------------------------ tests
    def get_tests(self, user_id, name, path):
        p = self.project_or_404(user_id, name)
        r = self.q1('SELECT data FROM tests WHERE project_id = ? AND path = ?', (p['id'], path))
        return json.loads(r['data']) if r else []

    def put_tests(self, user_id, name, path, tests):
        p = self.project_or_404(user_id, name)
        if not isinstance(tests, list) or len(tests) > 50:
            raise ApiError(400, 'Можно сохранить не больше 50 тестов')
        clean = []
        for t in tests:
            t = t if isinstance(t, dict) else {}
            clean.append({'input': str(t.get('input') or '')[:200_000],
                          'expected': str(t.get('expected') or '')[:200_000]})
        data = json.dumps(clean, ensure_ascii=False)
        with self.lock:
            self.db.execute('INSERT OR REPLACE INTO tests(project_id, path, data, updated) VALUES (?,?,?,?)',
                            (p['id'], path, data, now_ms()))
        return clean


class _Tx:
    def __init__(self, s):
        self.s = s

    def __enter__(self):
        self.s.lock.acquire()
        self.s.db.execute('BEGIN')
        return self.s.db

    def __exit__(self, et, e, tb):
        try:
            self.s.db.execute('ROLLBACK' if et else 'COMMIT')
        finally:
            self.s.lock.release()
