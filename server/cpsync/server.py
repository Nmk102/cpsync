"""CP Sync — сервер: аккаунты, синхронизация проектов, запуск тестов, веб-приложение."""

import argparse
import io
import json
import os
import secrets
import sys
import threading
import time
import zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

from .jobs import JobManager, make_sandbox
from .storage import ApiError, Storage, normalize_path, now_ms, valid_project_name

VERSION = '2.0.0'
MAX_BODY_BYTES = 8 * 1024 * 1024
MAX_EVENTS = 5000
POLL_MAX_WAIT = 30

HERE = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(os.path.dirname(HERE), 'web')
CONTENT_TYPES = {
    '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.webmanifest': 'application/manifest+json',
    '.png': 'image/png', '.svg': 'image/svg+xml', '.ico': 'image/x-icon', '.txt': 'text/plain; charset=utf-8',
}


class Hub:
    """События об изменениях проектов для long-poll клиентов (плагин CLion)."""

    def __init__(self):
        self.cond = threading.Condition()
        self.seq = 0
        self.events = []

    def emit(self, user_id, ev):
        with self.cond:
            self.seq += 1
            ev.update(seq=self.seq, time=now_ms())
            self.events.append((user_id, ev))
            if len(self.events) > MAX_EVENTS:
                del self.events[:len(self.events) - MAX_EVENTS]
            self.cond.notify_all()

    def poll(self, user_id, since, wait):
        deadline = time.time() + max(0.0, min(wait, POLL_MAX_WAIT))
        with self.cond:
            if since < 0:  # первый опрос: сразу сообщаем текущую позицию
                return {'seq': self.seq, 'resync': False, 'events': []}
            while True:
                resync = since > self.seq or (bool(self.events) and since < self.events[0][1]['seq'] - 1)
                evs = [] if since > self.seq else [e for u, e in self.events if u == user_id and e['seq'] > since]
                if evs or resync:
                    break
                left = deadline - time.time()
                if left <= 0:
                    break
                self.cond.wait(timeout=min(left, 5))
            return {'seq': self.seq, 'resync': resync, 'events': evs}


class RateLimiter:
    def __init__(self, limit, window):
        self.limit, self.window = limit, window
        self.hits = {}
        self.lock = threading.Lock()

    def check(self, key):
        t = time.time()
        with self.lock:
            h = [x for x in self.hits.get(key, []) if t - x < self.window]
            if len(h) >= self.limit:
                raise ApiError(429, 'Слишком много попыток, попробуйте через несколько минут')
            h.append(t)
            self.hits[key] = h


class App:
    def __init__(self, data_dir, public_url=None, registration='open', plugin_zip=None, workers=2):
        os.makedirs(data_dir, exist_ok=True)
        self.store = Storage(data_dir)
        self.hub = Hub()
        self.jobs = JobManager(self.store, data_dir, make_sandbox(data_dir), workers)
        self.public_url = (public_url or '').rstrip('/')
        self.registration = registration
        self.plugin_zip = plugin_zip
        self.plugin_cache = {}
        self.auth_limiter = RateLimiter(30, 600)

    def plugin_bytes(self, server_url):
        """Плагин с «вшитым» адресом этого сервера — пользователю не нужно его вводить."""
        if not self.plugin_zip or not os.path.exists(self.plugin_zip):
            return None
        key = (server_url, os.path.getmtime(self.plugin_zip))
        if key in self.plugin_cache:
            return self.plugin_cache[key]
        out = io.BytesIO()
        with zipfile.ZipFile(self.plugin_zip) as src, zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as dst:
            for info in src.infolist():
                data = src.read(info)
                name = info.filename.rsplit('/', 1)[-1]
                if info.filename.endswith('.jar') and name.startswith('cpsync-plugin'):
                    jin = io.BytesIO(data)
                    jout = io.BytesIO()
                    with zipfile.ZipFile(jin) as jz, zipfile.ZipFile(jout, 'w', zipfile.ZIP_DEFLATED) as jw:
                        for ji in jz.infolist():
                            if ji.filename != 'cpsync-server.txt':
                                jw.writestr(ji, jz.read(ji))
                        jw.writestr('cpsync-server.txt', server_url)
                    data = jout.getvalue()
                dst.writestr(info, data)
        self.plugin_cache = {key: out.getvalue()}
        return self.plugin_cache[key]


def qr_image(text, fmt):
    try:
        import segno
    except ImportError:
        return None
    q = segno.make(text, error='m')
    buf = io.BytesIO()
    if fmt == 'svg':
        q.save(buf, kind='svg', scale=8, border=2, dark='#111', light='#fff')
    else:
        q.save(buf, kind='png', scale=8, border=2)
    return buf.getvalue()


def make_handler(app):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'
        server_version = 'cpsync/' + VERSION

        def log_message(self, fmt, *args):
            if os.environ.get('CPSYNC_VERBOSE'):
                sys.stderr.write('%s %s\n' % (self.client_ip(), fmt % args))

        def client_ip(self):
            fwd = self.headers.get('X-Forwarded-For')
            return fwd.split(',')[0].strip() if fwd else self.client_address[0]

        def base_url(self):
            if app.public_url:
                return app.public_url
            proto = self.headers.get('X-Forwarded-Proto') or 'http'
            host = self.headers.get('X-Forwarded-Host') or self.headers.get('Host') or 'localhost'
            return '%s://%s' % (proto, host)

        # ------------------------------------------------------------------ io
        def send(self, status, body=b'', ctype='application/json; charset=utf-8', headers=None):
            if isinstance(body, (dict, list)):
                body = json.dumps(body, ensure_ascii=False).encode('utf-8')
            elif isinstance(body, str):
                body = body.encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Referrer-Policy', 'no-referrer')
            h = {'Cache-Control': 'no-store'}
            h.update(headers or {})
            for k, v in h.items():
                self.send_header(k, v)
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(body)

        def json_body(self):
            try:
                return json.loads(self.raw.decode('utf-8')) if self.raw else {}
            except Exception:
                raise ApiError(400, 'Некорректный JSON')

        def auth(self):
            h = self.headers.get('Authorization') or ''
            tok = h[7:].strip() if h.lower().startswith('bearer ') else ''
            user = app.store.user_by_token(tok)
            if user is None:
                raise ApiError(401, 'Нужно войти в аккаунт')
            self.token_hash = user['hash']
            return user

        def device_name(self, user):
            return user['name']

        def do_GET(self):
            self.dispatch('GET')

        def do_HEAD(self):
            self.dispatch('GET')

        def do_POST(self):
            self.dispatch('POST')

        def do_PUT(self):
            self.dispatch('PUT')

        def do_DELETE(self):
            self.dispatch('DELETE')

        def dispatch(self, method):
            self.raw = b''
            try:
                n = int(self.headers.get('Content-Length') or 0)
                if n > MAX_BODY_BYTES:
                    self.close_connection = True
                    raise ApiError(413, 'Слишком большой запрос')
                self.raw = self.rfile.read(n) if n else b''
                u = urlparse(self.path)
                q = parse_qs(u.query)
                parts = [unquote(p) for p in u.path.split('/') if p]
                if parts[:1] == ['api']:
                    return self.api(method, parts[1:], q)
                return self.public(method, u.path, parts)
            except ApiError as e:
                body = {'error': e.message}
                body.update(e.extra)
                self.send(e.status, body)
            except (BrokenPipeError, ConnectionResetError):
                pass
            except Exception as e:  # noqa
                import traceback
                traceback.print_exc()
                try:
                    self.send(500, {'error': 'Внутренняя ошибка сервера'})
                except Exception:
                    pass

        # ------------------------------------------------------------------ public pages
        def public(self, method, path, parts):
            if path == '/healthz':
                return self.send(200, 'ok', 'text/plain')
            if parts[:1] == ['qr'] and len(parts) == 2:
                code, _, fmt = parts[1].partition('.')
                if fmt not in ('svg', 'png') or not app.store.link_code_valid(code):
                    raise ApiError(404, 'Код устарел')
                img = qr_image('%s/#/link/%s' % (self.base_url(), code), fmt)
                if img is None:
                    raise ApiError(404, 'QR недоступен')
                return self.send(200, img, CONTENT_TYPES['.' + fmt])
            if path == '/download/cpsync-plugin.zip':
                data = app.plugin_bytes(self.base_url())
                if data is None:
                    raise ApiError(404, 'Плагин ещё не собран')
                return self.send(200, data, 'application/zip',
                                 {'Content-Disposition': 'attachment; filename="cpsync-plugin.zip"',
                                  'Cache-Control': 'no-cache'})
            if path == '/':
                path = '/index.html'
            fn = os.path.normpath(os.path.join(WEB_DIR, path.lstrip('/')))
            if not fn.startswith(WEB_DIR + os.sep) or not os.path.isfile(fn):
                # SPA: неизвестные пути отдаём как приложение
                if '.' in path.rsplit('/', 1)[-1]:
                    raise ApiError(404, 'Не найдено')
                fn = os.path.join(WEB_DIR, 'index.html')
            ext = os.path.splitext(fn)[1]
            with open(fn, 'rb') as f:
                data = f.read()
            cache = 'no-cache' if ext in ('.html', '.js', '.css', '.webmanifest') else 'public, max-age=86400'
            headers = {'Cache-Control': cache}
            if ext == '.html':
                headers['Content-Security-Policy'] = (
                    "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
                    "script-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
            if fn.endswith('sw.js'):
                headers['Service-Worker-Allowed'] = '/'
            return self.send(200, data, CONTENT_TYPES.get(ext, 'application/octet-stream'), headers)

        # ------------------------------------------------------------------ api
        def api(self, method, p, q):
            store, hub = app.store, app.hub

            def qp(name, default=None):
                v = q.get(name)
                return v[0] if v else default

            if p == ['config'] and method == 'GET':
                return self.send(200, {'version': VERSION, 'registration': app.registration,
                                       'serverUrl': self.base_url(), 'users': store.user_count() > 0})

            if p[:1] == ['auth'] and method == 'POST':
                b = self.json_body()
                name = str(b.get('deviceName') or 'браузер')[:80]
                kind = 'ide' if b.get('kind') == 'ide' else 'web'
                if p == ['auth', 'register']:
                    app.auth_limiter.check('reg:' + self.client_ip())
                    if app.registration != 'open' and store.user_count() > 0:
                        raise ApiError(403, 'Регистрация на этом сервере закрыта')
                    uid = store.create_user(str(b.get('login') or '').strip(), b.get('password'))
                elif p == ['auth', 'login']:
                    app.auth_limiter.check('login:' + self.client_ip())
                    uid = store.verify_user(str(b.get('login') or '').strip(), b.get('password'))
                elif p == ['auth', 'link']:
                    app.auth_limiter.check('link:' + self.client_ip())
                    uid = store.use_link_code(b.get('code'))
                elif p == ['auth', 'logout']:
                    user = self.auth()
                    store.revoke_token(user['user_id'], token_hash=self.token_hash)
                    return self.send(200, {'ok': True})
                else:
                    raise ApiError(404, 'Неизвестный запрос')
                tok = store.issue_token(uid, name, kind)
                u = store.get_user(uid)
                return self.send(200, {'token': tok, 'login': u['login'], 'isAdmin': bool(u['is_admin'])})

            user = self.auth()
            uid = user['user_id']
            dev = self.device_name(user)

            if p == ['me'] and method == 'GET':
                return self.send(200, {'login': user['login'], 'isAdmin': bool(user['is_admin']),
                                       'device': user['name'], 'devices': store.list_tokens(uid),
                                       'currentDevice': self.token_hash[:12]})
            if p == ['me', 'password'] and method == 'POST':
                b = self.json_body()
                store.verify_user(user['login'], b.get('old'))
                store.set_password(uid, b.get('new'))
                return self.send(200, {'ok': True})
            if p[:1] == ['devices'] and len(p) == 2 and method == 'DELETE':
                store.revoke_token(uid, token_id=p[1])
                return self.send(200, {'ok': True})
            if p == ['link-codes'] and method == 'POST':
                code, exp = store.create_link_code(uid)
                base = self.base_url()
                return self.send(200, {'code': code, 'url': '%s/#/link/%s' % (base, code), 'expiresAt': exp,
                                       'qrSvg': '%s/qr/%s.svg' % (base, code), 'qrPng': '%s/qr/%s.png' % (base, code)})

            if p == ['projects'] and method == 'GET':
                return self.send(200, {'projects': store.list_projects(uid)})
            if p == ['projects'] and method == 'POST':
                b = self.json_body()
                store.create_project(uid, b.get('name'))
                hub.emit(uid, {'type': 'project_changed', 'project': b.get('name'), 'by': dev, 'byId': ''})
                return self.send(200, {'ok': True})

            if len(p) >= 2 and p[0] == 'projects':
                name = p[1]
                if not valid_project_name(name):
                    raise ApiError(400, 'Некорректное имя проекта')
                rest = p[2:]
                dev_id = self.headers.get('X-Device-Id', '')
                if rest == [] and method == 'DELETE':
                    ok = store.delete_project(uid, name)
                    if ok:
                        hub.emit(uid, {'type': 'project_deleted', 'project': name, 'by': dev, 'byId': dev_id})
                    return self.send(200 if ok else 404, {'deleted': ok})
                if rest == ['manifest'] and method == 'GET':
                    m = store.manifest(uid, name)
                    if m is None:
                        raise ApiError(404, 'Проект не найден')
                    return self.send(200, m)
                if rest in (['file'], ['tests']):
                    path = normalize_path(qp('path', ''))
                    if not path:
                        raise ApiError(400, 'Некорректный путь')
                    if rest == ['tests']:
                        if method == 'GET':
                            return self.send(200, {'tests': store.get_tests(uid, name, path)})
                        if method == 'PUT':
                            return self.send(200, {'tests': store.put_tests(uid, name, path,
                                                                            self.json_body().get('tests'))})
                    elif method == 'GET':
                        h, data = store.file_content(uid, name, path)
                        return self.send(200, data, 'application/octet-stream', {'X-Hash': h})
                    elif method == 'PUT':
                        r = store.put_file(uid, name, path, self.raw, qp('base'), int(qp('mtime', '0') or 0), dev)
                        if r['changed']:
                            hub.emit(uid, {'type': 'project_changed', 'project': name, 'revision': r['revision'],
                                           'path': path, 'by': dev, 'byId': dev_id})
                        return self.send(200, r)
                    elif method == 'DELETE':
                        r = store.delete_file(uid, name, path, qp('base'), dev)
                        if r['changed']:
                            hub.emit(uid, {'type': 'project_changed', 'project': name, 'revision': r['revision'],
                                           'path': path, 'by': dev, 'byId': dev_id})
                        return self.send(200, r)

            if p[:1] == ['blobs'] and len(p) == 2 and method == 'GET':
                if not store.user_owns_blob(uid, p[1]):
                    raise ApiError(404, 'Нет такого содержимого')
                data = store.get_blob(p[1])
                if data is None:
                    raise ApiError(404, 'Нет такого содержимого')
                return self.send(200, data, 'application/octet-stream')

            if p == ['poll'] and method == 'POST':
                b = self.json_body()
                return self.send(200, hub.poll(uid, int(b.get('since', -1)), float(b.get('wait', 25))))

            if p == ['run'] and method == 'POST':
                return self.send(200, app.jobs.submit(user, self.json_body()))
            if p[:1] == ['jobs'] and len(p) == 2 and method == 'GET':
                return self.send(200, app.jobs.get(user, p[1], float(qp('wait', '0') or 0)))

            raise ApiError(404, 'Неизвестный запрос')

    return Handler


def main(argv=None):
    ap = argparse.ArgumentParser(description='CP Sync server')
    ap.add_argument('--host', default=os.environ.get('CPSYNC_HOST', '0.0.0.0'))
    ap.add_argument('--port', type=int, default=int(os.environ.get('CPSYNC_PORT', 8080)))
    ap.add_argument('--data', default=os.environ.get('CPSYNC_DATA', 'cpsync-data'))
    ap.add_argument('--public-url', default=os.environ.get('CPSYNC_PUBLIC_URL'))
    ap.add_argument('--registration', default=os.environ.get('CPSYNC_REGISTRATION', 'open'),
                    choices=['open', 'closed'])
    ap.add_argument('--plugin-zip', default=os.environ.get('CPSYNC_PLUGIN_ZIP') or os.path.join(
        os.path.dirname(os.path.dirname(HERE)), 'dist', 'cpsync-plugin.zip'))
    ap.add_argument('--workers', type=int, default=int(os.environ.get('CPSYNC_WORKERS', max(1, (os.cpu_count() or 2)))))
    args = ap.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors='replace')
        except Exception:
            pass

    app = App(os.path.abspath(args.data), args.public_url, args.registration, args.plugin_zip, args.workers)
    httpd = ThreadingHTTPServer((args.host, args.port), make_handler(app))
    httpd.daemon_threads = True
    print('CP Sync %s: http://%s:%d  (данные: %s, песочница: %s, регистрация: %s)' % (
        VERSION, args.host, args.port, os.path.abspath(args.data), app.jobs.sandbox.name, args.registration),
        flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
