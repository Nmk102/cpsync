#!/usr/bin/env python3
"""
Исполнитель CP Sync. Запускается внутри изолированного контейнера (без сети, с лимитами).

Читает <job>/job.json, компилирует (если нужно) и прогоняет тесты, пишет <job>/result.json.
  job.json: {compile: [cmd...] | null, run: [cmd...], cwd, tests: n, timeLimitMs, memoryLimitMb,
             expected: [str|null, ...]}
  входы тестов: <job>/in/<i>.txt
"""
import json
import math
import os
import resource
import signal
import subprocess
import sys
import time

DISPLAY_CAP = 64 * 1024
COMPARE_CAP = 32 * 1024 * 1024
FSIZE = 64 * 1024 * 1024

SIGNAL_INFO = {
    signal.SIGSEGV: 'ошибка доступа к памяти (SIGSEGV)',
    signal.SIGFPE: 'деление на ноль или переполнение (SIGFPE)',
    signal.SIGABRT: 'abort() или assert (SIGABRT)',
    signal.SIGBUS: 'ошибка памяти (SIGBUS)',
    signal.SIGILL: 'недопустимая инструкция (SIGILL)',
    signal.SIGKILL: 'процесс убит (SIGKILL)',
    signal.SIGXCPU: 'превышено процессорное время (SIGXCPU)',
    signal.SIGXFSZ: 'слишком большой вывод (SIGXFSZ)',
    signal.SIGPIPE: 'SIGPIPE',
}


def read_cap(path, cap):
    try:
        with open(path, 'rb') as f:
            data = f.read(cap + 1)
    except FileNotFoundError:
        return '', False
    return data[:cap].decode('utf-8', 'replace'), len(data) > cap


def tokens_equal(actual, expected):
    a = actual.split()
    e = expected.split()
    if len(a) != len(e):
        return False
    for x, y in zip(a, e):
        if x == y:
            continue
        if '.' not in y and 'e' not in y.lower():
            return False
        try:
            fx, fy = float(x), float(y)
        except ValueError:
            return False
        if abs(fx - fy) > 1e-6 * max(1.0, abs(fy)):
            return False
    return True


def run_limited(cmd, cwd, stdin_path, out_path, err_path, cpu_sec, mem_bytes, wall_sec, env):
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_sec, cpu_sec + 1))
        if mem_bytes:
            resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
            resource.setrlimit(resource.RLIMIT_STACK, (mem_bytes, mem_bytes))
        resource.setrlimit(resource.RLIMIT_FSIZE, (FSIZE, FSIZE))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))

    same = out_path == err_path
    with open(stdin_path, 'rb') as fin, open(out_path, 'wb') as fout, \
            open(os.devnull if same else err_path, 'wb') as ferr:
        t0 = time.monotonic()
        p = subprocess.Popen(cmd, cwd=cwd, stdin=fin, stdout=fout, stderr=subprocess.STDOUT if same else ferr,
                             preexec_fn=limits, start_new_session=True, close_fds=True, env=env)
        killed = False
        while True:
            pid, status, ru = os.wait4(p.pid, os.WNOHANG)
            if pid:
                break
            if time.monotonic() - t0 > wall_sec:
                try:
                    os.killpg(p.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                pid, status, ru = os.wait4(p.pid, 0)
                killed = True
                break
            time.sleep(0.002)
        wall = time.monotonic() - t0
        p.returncode = os.waitstatus_to_exitcode(status)
        # добиваем возможных потомков
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
    sig = -p.returncode if p.returncode < 0 else 0
    return {
        'exit': p.returncode if p.returncode >= 0 else None,
        'signal': sig,
        'cpuMs': int((ru.ru_utime + ru.ru_stime) * 1000),
        'wallMs': int(wall * 1000),
        'memKb': ru.ru_maxrss,
        'wallKilled': killed,
    }


def main():
    job_dir = sys.argv[1] if len(sys.argv) > 1 else '/job'
    with open(os.path.join(job_dir, 'job.json'), encoding='utf-8') as f:
        job = json.load(f)
    env = {
        'PATH': '/usr/local/bin:/usr/bin:/bin',
        'HOME': '/tmp',
        'TMPDIR': '/tmp',
        'LANG': 'C.UTF-8',
        'PYTHONIOENCODING': 'utf-8',
        'PYTHONDONTWRITEBYTECODE': '1',
        'PYTHONUTF8': '1',
    }
    result = {'compile': None, 'tests': []}
    cwd = os.path.join(job_dir, job.get('cwd') or '.')

    def save():
        tmp = os.path.join(job_dir, 'result.json.tmp')
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
        os.replace(tmp, os.path.join(job_dir, 'result.json'))

    devnull = os.path.join(job_dir, 'empty.txt')
    open(devnull, 'wb').close()

    if job.get('compile'):
        out = os.path.join(job_dir, 'compile.txt')
        r = run_limited(job['compile'], cwd, devnull, out, out, 60, 0, 90, env)
        text, _ = read_cap(out, DISPLAY_CAP)
        text = text.replace(os.path.join(job_dir, 'src') + '/', '')
        ok = r['exit'] == 0 and not r['wallKilled']
        result['compile'] = {'ok': ok, 'output': text if (ok or text) else 'Компилятор завершился без сообщений',
                             'timeMs': r['wallMs'], 'cached': False}
        if r['wallKilled']:
            result['compile']['output'] = 'Компиляция не уложилась в 90 секунд\n' + text
        if not ok:
            save()
            return
    else:
        result['compile'] = {'ok': True, 'output': '', 'timeMs': 0, 'cached': bool(job.get('cached')),
                             'skipped': not job.get('cached')}

    tl = int(job.get('timeLimitMs') or 2000)
    ml = int(job.get('memoryLimitMb') or 256)
    expected = job.get('expected') or []
    cpu_sec = int(math.ceil(tl / 1000.0)) + 1
    wall_sec = tl * 2 / 1000.0 + 1.0
    os.makedirs(os.path.join(job_dir, 'out'), exist_ok=True)
    for i in range(int(job.get('tests') or 0)):
        inp = os.path.join(job_dir, 'in', '%d.txt' % i)
        outp = os.path.join(job_dir, 'out', '%d.txt' % i)
        errp = os.path.join(job_dir, 'out', '%d.err' % i)
        try:
            r = run_limited(job['run'], cwd, inp, outp, errp, cpu_sec, ml * 1024 * 1024, wall_sec, env)
        except OSError as e:
            result['tests'].append({'verdict': 'RE', 'timeMs': 0, 'memoryKb': 0, 'exitCode': None,
                                    'exitInfo': 'не удалось запустить: %s' % e, 'stdout': '', 'stderr': '',
                                    'truncated': False})
            continue
        stdout, trunc = read_cap(outp, DISPLAY_CAP)
        stderr, trunc2 = read_cap(errp, 16 * 1024)
        exp = expected[i] if i < len(expected) else None
        sig = r['signal']
        info = None
        mem_hit = r['memKb'] * 1024 >= ml * 1024 * 1024 * 0.95 or 'bad_alloc' in stderr or 'MemoryError' in stderr
        if r['wallKilled'] or r['cpuMs'] > tl or sig == signal.SIGXCPU:
            verdict = 'TLE'
            info = 'превышено ограничение %d мс' % tl
        elif (sig or r['exit']) and mem_hit:
            verdict = 'MLE'
            info = 'превышено ограничение памяти %d МБ' % ml
        elif sig:
            verdict = 'RE'
            info = SIGNAL_INFO.get(sig, 'сигнал %d' % sig)
        elif r['exit']:
            verdict = 'RE'
            info = 'код выхода %d' % r['exit']
        elif exp is None or not str(exp).strip():
            verdict = 'OK'
        else:
            full, _ = read_cap(outp, COMPARE_CAP)
            verdict = 'AC' if tokens_equal(full, str(exp)) else 'WA'
        result['tests'].append({
            'verdict': verdict,
            'timeMs': max(r['cpuMs'], tl) if verdict == 'TLE' else r['cpuMs'],
            'wallMs': r['wallMs'],
            'memoryKb': r['memKb'],
            'exitCode': r['exit'] if r['exit'] is not None else -sig,
            'exitInfo': info,
            'stdout': stdout,
            'stderr': stderr,
            'truncated': trunc or trunc2,
        })
    save()


if __name__ == '__main__':
    main()
