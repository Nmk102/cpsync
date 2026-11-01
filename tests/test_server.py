#!/usr/bin/env python3
"""
Интеграционные тесты сервера CP Sync: поднимают настоящий сервер и проверяют API.
    python3 tests/test_server.py              # песочница: локальный процесс
    CPSYNC_SANDBOX=docker python3 tests/test_server.py   # песочница: Docker (нужен образ cpsync-sandbox)
"""
import io
import json
import os
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def free_port():
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Client:
    def __init__(self, base, token=None, device_id=''):
        self.base, self.token, self.device_id = base, token, device_id

    def req(self, method, path, body=None, raw=None, expect=200):
        data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
        path = urllib.parse.quote(path, safe='/?=&%:')
        r = urllib.request.Request(self.base + path, data=data, method=method)
        if self.token:
            r.add_header('Authorization', 'Bearer ' + self.token)
        if self.device_id:
            r.add_header('X-Device-Id', self.device_id)
        if body is not None:
            r.add_header('Content-Type', 'application/json')
        try:
            with urllib.request.urlopen(r, timeout=60) as f:
                status, out, ctype = f.status, f.read(), f.headers.get('Content-Type', '')
        except urllib.error.HTTPError as e:
            status, out, ctype = e.code, e.read(), e.headers.get('Content-Type', '')
        if expect is not None and status != expect:
            raise AssertionError('%s %s -> %d (ожидали %d): %s' % (method, path, status, expect, out[:300]))
        if 'json' in ctype:
            return json.loads(out)
        return out

    def run(self, project, file, tests, **kw):
        body = dict(project=project, file=file, tests=tests, **kw)
        job = self.req('POST', '/api/run', body)
        while True:
            j = self.req('GET', '/api/jobs/%s?wait=20' % job['id'])
            if j['status'] in ('done', 'error'):
                return j


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = tempfile.mkdtemp(prefix='cpsync-test-')
        cls.port = free_port()
        env = dict(os.environ, PYTHONPATH=os.path.join(ROOT, 'server'))
        env.setdefault('CPSYNC_SANDBOX', 'local')
        plugin_zip = os.path.join(cls.data, 'plugin.zip')
        jar = io.BytesIO()
        with zipfile.ZipFile(jar, 'w') as z:
            z.writestr('META-INF/plugin.xml', '<idea-plugin/>')
        with zipfile.ZipFile(plugin_zip, 'w') as z:
            z.writestr('cpsync-plugin/lib/cpsync-plugin-2.0.0.jar', jar.getvalue())
        cls.proc = subprocess.Popen(
            [sys.executable, '-m', 'cpsync', '--host', '127.0.0.1', '--port', str(cls.port),
             '--data', cls.data, '--plugin-zip', plugin_zip, '--workers', '2'],
            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        cls.base = 'http://127.0.0.1:%d' % cls.port
        for _ in range(100):
            try:
                urllib.request.urlopen(cls.base + '/healthz', timeout=1)
                break
            except Exception:
                time.sleep(0.1)
        anon = Client(cls.base)
        cls.alice = Client(cls.base, anon.req('POST', '/api/auth/register',
                                              {'login': 'alice', 'password': 'secret1', 'deviceName': 'Ноутбук', 'kind': 'ide'})['token'], 'dev-a')
        cls.bob = Client(cls.base, anon.req('POST', '/api/auth/register',
                                            {'login': 'bob', 'password': 'secret2'})['token'])

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        out = cls.proc.communicate(timeout=10)[0].decode('utf-8', 'replace')
        if os.environ.get('SHOW_LOG'):
            print(out)

    # ------------------------------------------------------------------ auth
    def test_auth(self):
        anon = Client(self.base)
        self.assertEqual(anon.req('POST', '/api/auth/register', {'login': 'ALICE', 'password': 'xxxxxx'}, expect=409)['error'],
                         'Такой логин уже занят')
        anon.req('POST', '/api/auth/register', {'login': 'a', 'password': 'xxxxxx'}, expect=400)
        anon.req('POST', '/api/auth/register', {'login': 'carol', 'password': '123'}, expect=400)
        anon.req('POST', '/api/auth/login', {'login': 'alice', 'password': 'wrong'}, expect=401)
        tok = anon.req('POST', '/api/auth/login', {'login': 'Alice', 'password': 'secret1', 'deviceName': 'iPhone'})['token']
        me = Client(self.base, tok).req('GET', '/api/me')
        self.assertEqual(me['login'], 'alice')
        self.assertTrue(me['isAdmin'])  # первый пользователь — администратор
        self.assertIn('iPhone', [d['name'] for d in me['devices']])
        anon.req('GET', '/api/projects', expect=401)
        Client(self.base, 'nonsense').req('GET', '/api/projects', expect=401)
        # выход отзывает токен
        c = Client(self.base, tok)
        c.req('POST', '/api/auth/logout', {})
        c.req('GET', '/api/me', expect=401)
        self.assertFalse(Client(self.base, self.bob.token).req('GET', '/api/me')['isAdmin'])

    def test_link_code_and_qr(self):
        link = self.alice.req('POST', '/api/link-codes', {})
        self.assertIn('/#/link/', link['url'])
        svg = Client(self.base).req('GET', '/qr/%s.svg' % link['code'])
        self.assertIn(b'<svg', svg)
        png = Client(self.base).req('GET', '/qr/%s.png' % link['code'])
        self.assertTrue(png.startswith(b'\x89PNG'))
        tok = Client(self.base).req('POST', '/api/auth/link', {'code': link['code'], 'deviceName': 'iPhone'})['token']
        self.assertEqual(Client(self.base, tok).req('GET', '/api/me')['login'], 'alice')
        # одноразовый
        Client(self.base).req('POST', '/api/auth/link', {'code': link['code']}, expect=401)
        Client(self.base).req('GET', '/qr/%s.svg' % link['code'], expect=404)

    def test_devices_revoke(self):
        tok = Client(self.base).req('POST', '/api/auth/login', {'login': 'bob', 'password': 'secret2', 'deviceName': 'old phone'})['token']
        devs = self.bob.req('GET', '/api/me')['devices']
        dev = [d for d in devs if d['name'] == 'old phone'][0]
        self.bob.req('DELETE', '/api/devices/' + dev['id'])
        Client(self.base, tok).req('GET', '/api/me', expect=401)

    def test_change_password(self):
        anon = Client(self.base)
        tok = anon.req('POST', '/api/auth/register', {'login': 'dave', 'password': 'first1'})['token']
        c = Client(self.base, tok)
        c.req('POST', '/api/me/password', {'old': 'bad', 'new': 'second2'}, expect=401)
        c.req('POST', '/api/me/password', {'old': 'first1', 'new': 'second2'})
        anon.req('POST', '/api/auth/login', {'login': 'dave', 'password': 'second2'})

    # ------------------------------------------------------------------ projects / sync
    def test_projects_isolated_between_users(self):
        a, b = self.alice, self.bob
        r = a.req('PUT', '/api/projects/Секрет/file?path=a.cpp&base=', raw=b'int main(){}')
        a.req('PUT', '/api/projects/Секрет/file?path=a.cpp&base=bad', raw=b'changed', expect=409)
        self.assertNotIn('Секрет', [p['name'] for p in b.req('GET', '/api/projects')['projects']])
        b.req('GET', '/api/projects/Секрет/manifest', expect=404)
        b.req('GET', '/api/blobs/' + r['hash'], expect=404)
        self.assertEqual(a.req('GET', '/api/blobs/' + r['hash']), b'int main(){}')
        # у Боба может быть проект с тем же именем
        b.req('PUT', '/api/projects/Секрет/file?path=b.py&base=', raw=b'print(1)')
        self.assertEqual(set(b.req('GET', '/api/projects/Секрет/manifest')['files']), {'b.py'})
        self.assertEqual(set(a.req('GET', '/api/projects/Секрет/manifest')['files']), {'a.cpp'})

    def test_create_delete_project_and_bad_paths(self):
        a = self.alice
        a.req('POST', '/api/projects', {'name': 'Пустой'})
        a.req('POST', '/api/projects', {'name': 'Пустой'}, expect=409)
        a.req('POST', '/api/projects', {'name': 'a/b'}, expect=400)
        self.assertIn('Пустой', [p['name'] for p in a.req('GET', '/api/projects')['projects']])
        a.req('PUT', '/api/projects/Пустой/file?path=../x', raw=b'x', expect=400)
        a.req('PUT', '/api/projects/Пустой/file?path=/etc/passwd', raw=b'x', expect=400)
        a.req('PUT', '/api/projects/Пустой/file?path=big.txt', raw=b'x' * (1024 * 1024 + 1), expect=413)
        a.req('DELETE', '/api/projects/Пустой')
        a.req('GET', '/api/projects/Пустой/manifest', expect=404)

    def test_poll_events(self):
        a = self.alice
        since = a.req('POST', '/api/poll', {'since': -1, 'wait': 0})['seq']
        out = {}

        def waiter():
            out['r'] = a.req('POST', '/api/poll', {'since': since, 'wait': 10})

        th = threading.Thread(target=waiter)
        th.start()
        time.sleep(0.3)
        self.bob.req('PUT', '/api/projects/Чужой/file?path=x.cpp&base=', raw=b'1')  # чужие события не видны
        time.sleep(0.3)
        self.assertTrue(th.is_alive())
        t0 = time.time()
        Client(self.base, a.token, 'other-device').req('PUT', '/api/projects/Live/file?path=a.cpp&base=', raw=b'x')
        th.join(5)
        self.assertLess(time.time() - t0, 2)
        ev = out['r']['events']
        self.assertEqual([e['project'] for e in ev], ['Live'])
        self.assertEqual(ev[0]['byId'], 'other-device')
        self.assertTrue(a.req('POST', '/api/poll', {'since': 10 ** 9, 'wait': 0})['resync'])

    def test_tests_storage(self):
        a = self.alice
        a.req('PUT', '/api/projects/T/file?path=a.cpp&base=', raw=b'int main(){}')
        self.assertEqual(a.req('GET', '/api/projects/T/tests?path=a.cpp')['tests'], [])
        a.req('PUT', '/api/projects/T/tests?path=a.cpp', {'tests': [{'input': '1 2', 'expected': '3'}, {'input': '5'}]})
        self.assertEqual(a.req('GET', '/api/projects/T/tests?path=a.cpp')['tests'],
                         [{'input': '1 2', 'expected': '3'}, {'input': '5', 'expected': ''}])
        self.bob.req('GET', '/api/projects/T/tests?path=a.cpp', expect=404)

    # ------------------------------------------------------------------ run
    def upload(self, project, path, text, who=None):
        (who or self.alice).req('PUT', '/api/projects/%s/file?path=%s' % (project, urllib.request.quote(path, safe='')),
                                raw=text.encode())

    def test_run_verdicts(self):
        P = 'Run'
        self.upload(P, 'sum.cpp', '#include <bits/stdc++.h>\nusing namespace std;\nint main(){long long a,b;cin>>a>>b;cout<<a+b<<"\\n";}\n')
        j = self.alice.run(P, 'sum.cpp', [{'input': '2 3', 'expected': '5'}, {'input': '2 2', 'expected': '5'},
                                          {'input': '1000000000000 1'}])
        self.assertEqual(j['status'], 'done', j)
        r = j['result']
        self.assertTrue(r['compile']['ok'])
        self.assertEqual([t['verdict'] for t in r['tests']], ['AC', 'WA', 'OK'])
        self.assertEqual(r['tests'][2]['stdout'], '1000000000001\n')
        self.assertGreater(r['tests'][0]['memoryKb'], 0)
        # повторный запуск — из кэша
        r2 = self.alice.run(P, 'sum.cpp', [{'input': '1 1', 'expected': '2'}])['result']
        self.assertTrue(r2['compile']['cached'])

        self.upload(P, 'tle.cpp', 'int main(){volatile long long x=0; for(;;) x++;}\n')
        t = self.alice.run(P, 'tle.cpp', [{'input': ''}], timeLimitMs=500)['result']['tests'][0]
        self.assertEqual(t['verdict'], 'TLE', t)

        self.upload(P, 'sleep.cpp', '#include <unistd.h>\nint main(){sleep(30);}\n')
        t = self.alice.run(P, 'sleep.cpp', [{'input': ''}], timeLimitMs=300)['result']['tests'][0]
        self.assertEqual(t['verdict'], 'TLE', t)

        self.upload(P, 're.cpp', 'int main(){int *p=nullptr; *p=1; return 0;}\n')
        t = self.alice.run(P, 're.cpp', [{'input': ''}])['result']['tests'][0]
        self.assertEqual(t['verdict'], 'RE')
        self.assertIn('SIGSEGV', t['exitInfo'])

        self.upload(P, 'exit3.cpp', 'int main(){return 3;}\n')
        t = self.alice.run(P, 'exit3.cpp', [{'input': ''}])['result']['tests'][0]
        self.assertEqual((t['verdict'], t['exitInfo']), ('RE', 'код выхода 3'))

        self.upload(P, 'mle.cpp', '#include <vector>\n#include <cstdio>\nint main(){std::vector<long long> v; for(int i=0;i<100000000;i++) v.push_back(i); printf("%d", (int)v.size());}\n')
        t = self.alice.run(P, 'mle.cpp', [{'input': ''}], memoryLimitMb=64)['result']['tests'][0]
        self.assertEqual(t['verdict'], 'MLE', t)

        self.upload(P, 'deep.cpp', '#include <cstdio>\nint f(int n){return n?f(n-1)+1:0;}\nint main(){printf("%d",f(1000000));}\n')
        t = self.alice.run(P, 'deep.cpp', [{'input': '', 'expected': '1000000'}])['result']['tests'][0]
        self.assertEqual(t['verdict'], 'AC', t)  # глубокая рекурсия не падает

        self.upload(P, 'ce.cpp', 'int main(){ return x; }\n')
        r = self.alice.run(P, 'ce.cpp', [{'input': ''}])['result']
        self.assertFalse(r['compile']['ok'])
        self.assertIn("was not declared", r['compile']['output'])
        self.assertTrue(r['compile']['output'].startswith('ce.cpp'))
        self.assertEqual(r['tests'], [])

        self.upload(P, 'oj.cpp', '#include <cstdio>\nint main(){\n#ifndef ONLINE_JUDGE\nfreopen("input.txt","r",stdin);\n#endif\nint x; scanf("%d",&x); printf("%d",x*2);}\n')
        t = self.alice.run(P, 'oj.cpp', [{'input': '21', 'expected': '42'}])['result']['tests'][0]
        self.assertEqual(t['verdict'], 'AC')

        self.upload(P, 'sol.py', 'a, b = map(int, input().split())\nprint(a * b)\n')
        r = self.alice.run(P, 'sol.py', [{'input': '6 7', 'expected': '42'}, {'input': 'x'}])['result']
        self.assertEqual(r['tests'][0]['verdict'], 'AC')
        self.assertEqual(r['tests'][1]['verdict'], 'RE')
        self.assertIn('ValueError', r['tests'][1]['stderr'])

        self.upload(P, 'c/main.c', '#include <stdio.h>\n#include <math.h>\n#include "h.h"\nint main(){printf("%.3f", sqrt(TWO));}\n')
        self.upload(P, 'c/h.h', '#define TWO 2.0\n')
        t = self.alice.run(P, 'c/main.c', [{'input': '', 'expected': '1.41421356'}])['result']['tests'][0]
        self.assertEqual(t['verdict'], 'WA')  # 1.414 vs 1.41421356 — точность 1e-6 не проходит
        t = self.alice.run(P, 'c/main.c', [{'input': '', 'expected': '1.414'}])['result']['tests'][0]
        self.assertEqual(t['verdict'], 'AC')

        # запуск несохранённого кода из редактора
        r = self.alice.run(P, 'sum.cpp', [{'input': '2 3', 'expected': '6'}],
                           source='#include <iostream>\nint main(){int a,b;std::cin>>a>>b;std::cout<<a*b;}\n')['result']
        self.assertEqual(r['tests'][0]['verdict'], 'AC')
        self.assertTrue(r['edited'])

        # большой вывод обрезается для показа, но проверяется целиком
        self.upload(P, 'big.py', 'print("\\n".join(str(i) for i in range(200000)))\n')
        t = self.alice.run(P, 'big.py', [{'input': '', 'expected': '\n'.join(str(i) for i in range(200000))}])['result']['tests'][0]
        self.assertEqual(t['verdict'], 'AC')
        self.assertTrue(t['truncated'])

        # C++ стандарт
        self.upload(P, 'cpp23.cpp', '#include <iostream>\n#include <ranges>\nint main(){ for (int x : std::views::iota(1, 4)) std::cout << x; }\n')
        t = self.alice.run(P, 'cpp23.cpp', [{'input': '', 'expected': '123'}], std='c++20')['result']['tests'][0]
        self.assertEqual(t['verdict'], 'AC')

    def test_run_errors_and_limits(self):
        self.upload('Lim', 'a.cpp', 'int main(){}')
        self.alice.req('POST', '/api/run', {'project': 'Lim', 'file': 'a.txt', 'tests': [{'input': ''}]}, expect=400)
        self.alice.req('POST', '/api/run', {'project': 'Lim', 'file': 'nope.cpp', 'tests': [{'input': ''}]}, expect=404)
        self.alice.req('POST', '/api/run', {'project': 'Lim', 'file': 'a.cpp', 'tests': []}, expect=400)
        self.bob.req('POST', '/api/run', {'project': 'Lim', 'file': 'a.cpp', 'tests': [{'input': ''}]}, expect=404)
        j = self.alice.req('POST', '/api/run', {'project': 'Lim', 'file': 'a.cpp', 'tests': [{'input': ''}]})
        self.bob.req('GET', '/api/jobs/' + j['id'], expect=404)

    # ------------------------------------------------------------------ public
    def test_static_and_plugin(self):
        anon = Client(self.base)
        html = anon.req('GET', '/')
        self.assertIn(b'CP Sync', html)
        self.assertIn(b'CP Sync', anon.req('GET', '/p/whatever'))  # SPA-маршрут
        anon.req('GET', '/nope.js', expect=404)
        anon.req('GET', '/../server.py', expect=404)
        z = zipfile.ZipFile(io.BytesIO(anon.req('GET', '/download/cpsync-plugin.zip')))
        jar = zipfile.ZipFile(io.BytesIO(z.read('cpsync-plugin/lib/cpsync-plugin-2.0.0.jar')))
        self.assertEqual(jar.read('cpsync-server.txt').decode(), self.base)
        self.assertIn(b'plugin', jar.read('META-INF/plugin.xml'))
        cfg = anon.req('GET', '/api/config')
        self.assertEqual(cfg['registration'], 'open')


if __name__ == '__main__':
    unittest.main(verbosity=2)
