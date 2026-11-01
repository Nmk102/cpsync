"""Очередь запусков и песочница: Docker (для сервера) или локальный процесс (только для разработки)."""

import hashlib
import http.client
import json
import os
import queue
import shutil
import socket
import subprocess
import sys
import threading
import time
import uuid

from .storage import ApiError, normalize_path, now_ms

HERE = os.path.dirname(os.path.abspath(__file__))
RUNNER = os.path.join(os.path.dirname(HERE), 'sandbox', 'runner.py')

LANGS = {
    'cpp': 'cpp', 'cc': 'cpp', 'cxx': 'cpp', 'c++': 'cpp',
    'c': 'c',
    'py': 'py',
}
CPP_STDS = {'c++17', 'c++20', 'c++23'}
MAX_JOB_SOURCE_BYTES = 8 * 1024 * 1024
JOB_KEEP_SECONDS = 15 * 60
MAX_ACTIVE_PER_USER = 2
MAX_PER_MINUTE = 30


def lang_of(path):
    ext = path.rsplit('.', 1)[-1].lower() if '.' in path else ''
    return LANGS.get(ext)


# ---------------------------------------------------------------------------- sandboxes
class LocalSandbox:
    """Без изоляции! Только для разработки и тестов на своём компьютере."""
    name = 'local'

    def run(self, job_dir, timeout):
        try:
            subprocess.run([sys.executable, RUNNER, job_dir], timeout=timeout,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        except subprocess.TimeoutExpired:
            raise ApiError(500, 'Запуск не уложился в общее ограничение времени')


class _UnixConn(http.client.HTTPConnection):
    def __init__(self, path, timeout):
        super().__init__('localhost', timeout=timeout)
        self.unix_path = path

    def connect(self):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        s.connect(self.unix_path)
        self.sock = s


class DockerSandbox:
    """Каждый запуск — отдельный контейнер: без сети, только чтение ФС, лимиты памяти/процессов/CPU."""
    name = 'docker'

    def __init__(self, socket_path, image, data_dir, host_data_dir):
        self.socket_path = socket_path
        self.image = image
        self.data_dir = os.path.abspath(data_dir)
        self.host_data_dir = host_data_dir or self.data_dir

    def _api(self, method, path, body=None, timeout=30):
        c = _UnixConn(self.socket_path, timeout)
        try:
            data = json.dumps(body).encode() if body is not None else None
            c.request(method, '/v1.41' + path, body=data,
                      headers={'Content-Type': 'application/json'} if data else {})
            r = c.getresponse()
            raw = r.read()
            if r.status >= 400:
                raise RuntimeError('docker %s %s -> %d %s' % (method, path, r.status, raw[:300]))
            return json.loads(raw) if raw else None
        finally:
            c.close()

    def check(self):
        self._api('GET', '/images/%s/json' % self.image)

    def run(self, job_dir, timeout):
        rel = os.path.relpath(os.path.abspath(job_dir), self.data_dir)
        host_dir = os.path.join(self.host_data_dir, rel)
        name = 'cpsync-job-' + uuid.uuid4().hex[:12]
        body = {
            'Image': self.image,
            'Cmd': ['python3', '/opt/runner.py', '/job'],
            'User': '65534:65534',
            'WorkingDir': '/job',
            'NetworkDisabled': True,
            'Env': ['HOME=/tmp'],
            'HostConfig': {
                'Binds': ['%s:/job:rw' % host_dir],
                'NetworkMode': 'none',
                'Memory': 1024 * 1024 * 1024,
                'MemorySwap': 1024 * 1024 * 1024,
                'NanoCpus': 1_000_000_000,
                'PidsLimit': 128,
                'ReadonlyRootfs': True,
                'Tmpfs': {'/tmp': 'rw,exec,nosuid,size=128m'},
                'CapDrop': ['ALL'],
                'SecurityOpt': ['no-new-privileges'],
                'Ulimits': [{'Name': 'nofile', 'Soft': 256, 'Hard': 256}],
            },
        }
        cid = self._api('POST', '/containers/create?name=' + name, body)['Id']
        try:
            self._api('POST', '/containers/%s/start' % cid)
            try:
                self._api('POST', '/containers/%s/wait' % cid, timeout=timeout)
            except (socket.timeout, TimeoutError):
                try:
                    self._api('POST', '/containers/%s/kill' % cid)
                except Exception:
                    pass
                raise ApiError(500, 'Запуск не уложился в общее ограничение времени')
        finally:
            try:
                self._api('DELETE', '/containers/%s?force=1' % cid)
            except Exception:
                pass


def make_sandbox(data_dir):
    mode = os.environ.get('CPSYNC_SANDBOX', 'auto')
    sock = os.environ.get('CPSYNC_DOCKER_SOCKET', '/var/run/docker.sock')
    if mode == 'docker' or (mode == 'auto' and os.path.exists(sock)):
        sb = DockerSandbox(sock, os.environ.get('CPSYNC_SANDBOX_IMAGE', 'cpsync-sandbox:latest'),
                           data_dir, os.environ.get('CPSYNC_HOST_DATA'))
        try:
            sb.check()
            return sb
        except Exception as e:
            if mode == 'docker':
                raise
            print('! Docker недоступен (%s) — запуск кода без изоляции' % e, file=sys.stderr)
    print('! ВНИМАНИЕ: код пользователей запускается БЕЗ изоляции (режим разработки)', file=sys.stderr)
    return LocalSandbox()


# ---------------------------------------------------------------------------- jobs
class JobManager:
    def __init__(self, storage, data_dir, sandbox, workers=2):
        self.store = storage
        self.sandbox = sandbox
        self.jobs_dir = os.path.join(data_dir, 'jobs')
        self.cache_dir = os.path.join(data_dir, 'cache')
        os.makedirs(self.jobs_dir, exist_ok=True)
        os.makedirs(self.cache_dir, exist_ok=True)
        self.cond = threading.Condition()
        self.jobs = {}
        self.order = []
        self.q = queue.Queue()
        self.recent = {}  # user_id -> [timestamps]
        for i in range(max(1, workers)):
            threading.Thread(target=self._worker, name='job-worker-%d' % i, daemon=True).start()
        threading.Thread(target=self._janitor, daemon=True).start()

    # ---- API
    def submit(self, user, req):
        uid = user['user_id']
        project = req.get('project')
        path = normalize_path(req.get('file') or '')
        if not path:
            raise ApiError(400, 'Некорректный файл')
        lang = lang_of(path)
        if not lang:
            raise ApiError(400, 'Запускать можно только .cpp, .c и .py')
        tests = req.get('tests')
        if not isinstance(tests, list) or not tests:
            raise ApiError(400, 'Нужен хотя бы один тест')
        if len(tests) > 50:
            raise ApiError(400, 'Не больше 50 тестов за раз')
        tl = max(100, min(int(req.get('timeLimitMs') or 2000), 10000))
        ml = max(16, min(int(req.get('memoryLimitMb') or 256), 512))
        std = req.get('std') if req.get('std') in CPP_STDS else 'c++20'
        manifest = self.store.manifest(uid, project) if isinstance(project, str) else None
        if manifest is None:
            raise ApiError(404, 'Проект не найден')
        source = req.get('source')
        if source is not None and not isinstance(source, str):
            raise ApiError(400, 'Некорректный код')
        live = {p: f for p, f in manifest['files'].items() if not f['deleted']}
        if path not in live and source is None:
            raise ApiError(404, 'Файл не найден в проекте')

        t = time.time()
        with self.cond:
            active = [j for j in self.jobs.values() if j['userId'] == uid and j['status'] in ('queued', 'running')]
            if len(active) >= MAX_ACTIVE_PER_USER:
                raise ApiError(429, 'Подождите: предыдущий запуск ещё выполняется')
            rec = [x for x in self.recent.get(uid, []) if t - x < 60]
            if len(rec) >= MAX_PER_MINUTE:
                raise ApiError(429, 'Слишком много запусков за минуту, подождите немного')
            rec.append(t)
            self.recent[uid] = rec
            jid = uuid.uuid4().hex[:16]
            job = {
                'id': jid, 'userId': uid, 'project': project, 'file': path, 'lang': lang, 'std': std,
                'timeLimitMs': tl, 'memoryLimitMb': ml,
                'tests': [{'input': str((x or {}).get('input') or ''),
                           'expected': None if (x or {}).get('expected') in (None, '') else str(x['expected'])}
                          for x in tests],
                'source': source, 'live': live, 'revision': manifest['revision'],
                'status': 'queued', 'createdAt': now_ms(), 'result': None, 'error': None,
            }
            self.jobs[jid] = job
            self.order.append(jid)
            self.q.put(jid)
            return self.view(job)

    def view(self, j):
        with self.cond:
            pos = None
            if j['status'] == 'queued':
                pos = [x for x in self.order if self.jobs.get(x, {}).get('status') == 'queued'].index(j['id']) + 1
        return {'id': j['id'], 'status': j['status'], 'project': j['project'], 'file': j['file'],
                'queuePosition': pos, 'result': j['result'], 'error': j['error']}

    def get(self, user, jid, wait):
        deadline = time.time() + max(0.0, min(float(wait), 30.0))
        with self.cond:
            while True:
                j = self.jobs.get(jid)
                if j is None or j['userId'] != user['user_id']:
                    raise ApiError(404, 'Запуск не найден')
                if j['status'] in ('done', 'error'):
                    break
                left = deadline - time.time()
                if left <= 0:
                    break
                self.cond.wait(timeout=min(left, 5))
        return self.view(j)

    # ---- worker
    def _worker(self):
        while True:
            jid = self.q.get()
            with self.cond:
                job = self.jobs.get(jid)
                if job is None:
                    continue
                job['status'] = 'running'
                self.cond.notify_all()
            try:
                result = self._execute(job)
                with self.cond:
                    job['result'] = result
                    job['status'] = 'done'
            except ApiError as e:
                with self.cond:
                    job['error'] = e.message
                    job['status'] = 'error'
            except Exception as e:  # noqa
                import traceback
                traceback.print_exc()
                with self.cond:
                    job['error'] = 'Внутренняя ошибка запуска: %s' % e
                    job['status'] = 'error'
            with self.cond:
                job['finishedAt'] = now_ms()
                job['live'] = None
                job['source'] = None
                self.cond.notify_all()

    def _janitor(self):
        while True:
            time.sleep(60)
            t = now_ms()
            with self.cond:
                for jid in list(self.jobs):
                    j = self.jobs[jid]
                    if j['status'] in ('done', 'error') and t - j.get('finishedAt', t) > JOB_KEEP_SECONDS * 1000:
                        del self.jobs[jid]
                self.order = [x for x in self.order if x in self.jobs]
            # кэш бинарников: оставляем 400 самых свежих
            try:
                items = sorted((os.path.getmtime(os.path.join(self.cache_dir, f)), f) for f in os.listdir(self.cache_dir))
                for _, f in items[:-400]:
                    os.remove(os.path.join(self.cache_dir, f))
            except OSError:
                pass

    def _execute(self, job):
        live = job['live']
        path = job['file']
        jdir = os.path.join(self.jobs_dir, job['id'])
        src = os.path.join(jdir, 'src')
        os.makedirs(os.path.join(jdir, 'in'), exist_ok=True)
        os.makedirs(src, exist_ok=True)
        try:
            # исходники проекта (чтобы работали #include "util.h" и т.п.)
            total = 0
            override = job['source'].encode('utf-8') if job['source'] is not None else None
            files = sorted(live.items(), key=lambda kv: kv[0] != path)
            for p, f in files:
                if p == path and override is not None:
                    continue
                if total + f['size'] > MAX_JOB_SOURCE_BYTES:
                    continue
                data = self.store.get_blob(f['hash'])
                if data is None:
                    continue
                total += len(data)
                dst = os.path.join(src, *p.split('/'))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(dst, 'wb') as fh:
                    fh.write(data)
            if override is not None:
                dst = os.path.join(src, *path.split('/'))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(dst, 'wb') as fh:
                    fh.write(override)
            for i, t in enumerate(job['tests']):
                with open(os.path.join(jdir, 'in', '%d.txt' % i), 'wb') as fh:
                    fh.write(t['input'].encode('utf-8'))

            in_box = '/job' if self.sandbox.name == 'docker' else jdir
            rel_dir = os.path.dirname(path)
            cwd = 'src/' + rel_dir if rel_dir else 'src'
            box_src = in_box + '/src/' + path
            lang = job['lang']
            spec = {'cwd': cwd, 'tests': len(job['tests']), 'timeLimitMs': job['timeLimitMs'],
                    'memoryLimitMb': job['memoryLimitMb'], 'expected': [t['expected'] for t in job['tests']]}
            cached_bin = None
            tool = ''
            if lang == 'py':
                spec['compile'] = None
                spec['run'] = ['python3', '-B', box_src]
                tool = 'Python 3'
            else:
                if lang == 'cpp':
                    flags = ['g++', '-std=' + job['std'], '-O2', '-pipe', '-DONLINE_JUDGE']
                    tool = 'g++ ' + job['std']
                else:
                    flags = ['gcc', '-std=c17', '-O2', '-pipe', '-DONLINE_JUDGE']
                    tool = 'gcc c17'
                h = hashlib.sha256()
                h.update(json.dumps([flags, path]).encode())
                # в ключ кэша входят сам файл и заголовки проекта (их могут подключать через #include)
                for p in sorted(live):
                    if p == path and override is not None:
                        continue
                    if p == path or p.rsplit('.', 1)[-1].lower() in ('h', 'hpp', 'hh', 'hxx', 'inc', 'ipp', 'tpp'):
                        h.update(('%s:%s\n' % (p, live[p]['hash'])).encode())
                if override is not None:
                    h.update(b'override:' + hashlib.sha256(override).hexdigest().encode())
                key = h.hexdigest()[:32]
                cached_bin = os.path.join(self.cache_dir, key)
                prog = os.path.join(jdir, 'prog')
                if os.path.exists(cached_bin):
                    shutil.copy2(cached_bin, prog)
                    os.utime(cached_bin)
                    spec['compile'] = None
                    spec['cached'] = True
                    cached_bin = None
                else:
                    spec['compile'] = flags + [box_src, '-o', in_box + '/prog'] + (['-lm'] if lang == 'c' else [])
                spec['run'] = [in_box + '/prog']
            with open(os.path.join(jdir, 'job.json'), 'w', encoding='utf-8') as fh:
                json.dump(spec, fh)
            # контейнер работает от непривилегированного пользователя
            for root, dirs, fs in os.walk(jdir):
                os.chmod(root, 0o777)
                for f in fs:
                    os.chmod(os.path.join(root, f), 0o666)
            if os.path.exists(os.path.join(jdir, 'prog')):
                os.chmod(os.path.join(jdir, 'prog'), 0o777)

            budget = 100 + len(job['tests']) * (job['timeLimitMs'] * 2 / 1000 + 2) + 15
            self.sandbox.run(jdir, budget)

            rp = os.path.join(jdir, 'result.json')
            if not os.path.exists(rp):
                raise ApiError(500, 'Программа сломала песочницу — результат не получен')
            with open(rp, encoding='utf-8') as fh:
                result = json.load(fh)
            if cached_bin and result.get('compile', {}).get('ok') and os.path.exists(os.path.join(jdir, 'prog')):
                try:
                    shutil.copy2(os.path.join(jdir, 'prog'), cached_bin)
                except OSError:
                    pass
            result['revision'] = job['revision']
            result['language'] = lang
            result['tool'] = tool
            result['edited'] = job['source'] is not None
            result['timeLimitMs'] = job['timeLimitMs']
            result['memoryLimitMb'] = job['memoryLimitMb']
            return result
        finally:
            shutil.rmtree(jdir, ignore_errors=True)
