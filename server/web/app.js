'use strict';
/* CP Sync — веб-приложение (телефон и компьютер). Без сборки и зависимостей. */

const VERSION = '2.0.0';
const RUNNABLE = ['cpp', 'cc', 'cxx', 'c', 'py'];
const HEADER_EXT = ['h', 'hpp', 'hh', 'hxx', 'inc'];
const TEMPLATES = {
  cpp: '#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    ios::sync_with_stdio(false);\n    cin.tie(nullptr);\n\n    \n    return 0;\n}\n',
  c: '#include <stdio.h>\n\nint main(void) {\n    \n    return 0;\n}\n',
  py: 'import sys\ninput = sys.stdin.readline\n\n\n',
};

// ------------------------------------------------------------------ helpers
const app = document.getElementById('app');
const enc = encodeURIComponent;
const extOf = (p) => (p.includes('.') ? p.split('.').pop().toLowerCase() : '');
const baseName = (p) => p.split('/').pop();
const dirName = (p) => (p.includes('/') ? p.slice(0, p.lastIndexOf('/')) : '');
const isRunnable = (p) => RUNNABLE.includes(extOf(p));
const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
const isStandalone = () => window.matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
const isPhone = () => window.matchMedia('(max-width: 700px)').matches || isIOS;

function h(tag, props, ...children) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(props || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'style') el.style.cssText = v;
    else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
    else if (k === 'html') el.innerHTML = v; // только для встроенных иконок
    else if (k in el && typeof v !== 'string') el[k] = v;
    else el.setAttribute(k, v === true ? '' : v);
  }
  for (const c of children.flat(Infinity)) {
    if (c === null || c === undefined || c === false) continue;
    el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return el;
}

const ICONS = {
  back: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
  plus: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
  user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
  chev: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
  folder: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 6.5A2.5 2.5 0 015.5 4h4l2 2.5h7A2.5 2.5 0 0121 9v8.5a2.5 2.5 0 01-2.5 2.5h-13A2.5 2.5 0 013 17.5z"/></svg>',
  trash: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/></svg>',
  copy: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 00-1-1H5a1 1 0 00-1 1v10a1 1 0 001 1h3"/></svg>',
  paste: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4h6v3H9z"/></svg>',
  timer: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M9 2h6"/></svg>',
  mem: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 6V3M12 6V3M16 6V3M8 21v-3M12 21v-3M16 21v-3"/></svg>',
  code: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>',
  laptop: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/></svg>',
  phone: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/></svg>',
  sync: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10a8 8 0 00-14.6-3.5M4 14a8 8 0 0014.6 3.5"/><path d="M5 2.5v4h4M19 21.5v-4h-4"/></svg>',
  play: '<svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M7 4.5v15a1 1 0 001.5.86l12.5-7.5a1 1 0 000-1.72L8.5 3.64A1 1 0 007 4.5z"/></svg>',
  share: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-3px"><path d="M12 3v12M7 8l5-5 5 5M5 13v6a2 2 0 002 2h10a2 2 0 002-2v-6"/></svg>',
  more: '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></svg>',
};
const icon = (name, cls) => h('span', { class: cls || '', html: ICONS[name], style: 'display:inline-flex' });

function ago(ms) {
  if (!ms) return '';
  const s = Math.max(0, (Date.now() - ms) / 1000);
  if (s < 45) return 'только что';
  if (s < 3600) return Math.round(s / 60) + ' мин назад';
  if (s < 86400) return Math.round(s / 3600) + ' ч назад';
  if (s < 86400 * 7) return Math.round(s / 86400) + ' дн назад';
  return new Date(ms).toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' });
}
const fmtMem = (kb) => (kb >= 1024 ? (kb / 1024).toFixed(kb >= 10240 ? 0 : 1) + ' МБ' : kb + ' КБ');
const plural = (n, a, b, c) => { const m = n % 10, mm = n % 100; return n + ' ' + (m === 1 && mm !== 11 ? a : m >= 2 && m <= 4 && (mm < 12 || mm > 14) ? b : c); };

// iOS заменяет кавычки и «--» при наборе — в коде и тестах возвращаем обычные символы
const normalizeTyping = (s) => s.replace(/[“”„«»]/g, '"').replace(/[‘’]/g, "'").replace(/—/g, '--');

function deviceName() {
  const ua = navigator.userAgent;
  const dev = /iPhone/.test(ua) ? 'iPhone' : /iPad/.test(ua) || (isIOS && !/iPhone/.test(ua)) ? 'iPad' : /Android/.test(ua) ? 'Android'
    : /Mac/.test(ua) ? 'Mac' : /Windows/.test(ua) ? 'Windows' : /Linux/.test(ua) ? 'Linux' : 'устройство';
  const br = /YaBrowser/.test(ua) ? 'Яндекс Браузер' : /Edg\//.test(ua) ? 'Edge' : /Firefox|FxiOS/.test(ua) ? 'Firefox'
    : /Chrome|CriOS/.test(ua) ? 'Chrome' : /Safari/.test(ua) ? 'Safari' : 'браузер';
  return isStandalone() ? dev + ' · приложение' : dev + ' · ' + br;
}

let toastTimer;
function toast(msg) {
  let t = document.querySelector('.toast');
  if (!t) { t = h('div', { class: 'toast' }); document.body.append(t); }
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2400);
}

function modal(build) {
  return new Promise((resolve) => {
    const back = h('div', { class: 'modal-back' });
    const close = (v) => { back.remove(); resolve(v); };
    back.addEventListener('click', (e) => { if (e.target === back) close(null); });
    const box = h('div', { class: 'modal' });
    build(box, close);
    back.append(box);
    document.body.append(back);
    const inp = box.querySelector('input');
    if (inp) setTimeout(() => inp.focus(), 50);
  });
}

function askText({ title, text, placeholder, value = '', ok = 'Готово', validate }) {
  return modal((box, close) => {
    const input = h('input', { class: 'input', placeholder, value, autocapitalize: 'off', autocorrect: 'off', spellcheck: 'false' });
    const err = h('div', { class: 'error-box hidden' });
    const submit = () => {
      const v = input.value.trim();
      const msg = validate ? validate(v) : (v ? null : 'Введите значение');
      if (msg) { err.textContent = msg; err.classList.remove('hidden'); return; }
      close(v);
    };
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter') submit(); });
    box.append(h('h2', {}, title), text ? h('p', {}, text) : null, input, err,
      h('div', { class: 'btn-row' }, h('button', { class: 'btn', style: 'flex:1', onclick: () => close(null) }, 'Отмена'),
        h('button', { class: 'btn primary', style: 'flex:1', onclick: submit }, ok)));
  });
}

function confirmBox({ title, text, ok = 'OK', danger = false }) {
  return modal((box, close) => {
    box.append(h('h2', {}, title), text ? h('p', {}, text) : null,
      h('div', { class: 'btn-row' }, h('button', { class: 'btn', style: 'flex:1', onclick: () => close(false) }, 'Отмена'),
        h('button', { class: 'btn ' + (danger ? 'danger' : 'primary'), style: 'flex:1', onclick: () => close(true) }, ok)));
  });
}

async function copyText(text) {
  try { await navigator.clipboard.writeText(text); toast('Скопировано'); } catch (e) { toast('Не удалось скопировать'); }
}

// ------------------------------------------------------------------ api
const S = {
  token: localStorage.getItem('cpsync.token') || '',
  login: localStorage.getItem('cpsync.login') || '',
  cleanups: [],
  guard: null, // функция, спрашивающая подтверждение ухода со страницы
};

class ApiError extends Error { constructor(msg, status) { super(msg); this.status = status; } }

async function api(path, { method = 'GET', body, raw, signal } = {}) {
  const headers = {};
  if (S.token) headers.Authorization = 'Bearer ' + S.token;
  let payload;
  if (raw !== undefined) payload = raw;
  else if (body !== undefined) { headers['Content-Type'] = 'application/json'; payload = JSON.stringify(body); }
  let r;
  try {
    r = await fetch(path, { method, headers, body: payload, signal, cache: 'no-store' });
  } catch (e) {
    if (e.name === 'AbortError') throw e;
    throw new ApiError('Нет связи с сервером. Проверьте интернет.', 0);
  }
  if (r.status === 401 && S.token && !path.startsWith('/api/auth/')) {
    setSession('', '');
    location.hash = '#/welcome';
    throw new ApiError('Сессия закончилась — войдите снова', 401);
  }
  if (!r.ok) {
    let msg = '';
    let extra = {};
    try { extra = await r.json(); msg = extra.error; } catch (e) { /* not json */ }
    const err = new ApiError(msg || 'Ошибка сервера (' + r.status + ')', r.status);
    err.extra = extra;
    throw err;
  }
  const ct = r.headers.get('Content-Type') || '';
  if (ct.includes('json')) return r.json();
  return { text: await r.text(), hash: r.headers.get('X-Hash') };
}

function setSession(token, login) {
  S.token = token; S.login = login;
  if (token) { localStorage.setItem('cpsync.token', token); localStorage.setItem('cpsync.login', login); }
  else { localStorage.removeItem('cpsync.token'); localStorage.removeItem('cpsync.login'); }
}

const projUrl = (p) => '/api/projects/' + enc(p);

// ------------------------------------------------------------------ layout
function page({ title, sub, back, actions = [], big = false }, ...content) {
  const top = h('header', { class: 'top' },
    h('div', { class: 'top-row' },
      back ? h('button', { class: 'icon-btn back', 'aria-label': 'Назад', onclick: () => go(back) }, icon('back')) : big ? null : h('span', { class: 'spacer' }),
      h('h1', { class: big ? 'big' : '' }, title, sub ? h('span', { class: 'sub' }, sub) : null),
      actions.length ? actions : big ? null : h('span', { class: 'spacer' })));
  const main = h('main', {}, content);
  app.replaceChildren(top, main);
  const onScroll = () => top.classList.toggle('scrolled', window.scrollY > 4);
  window.addEventListener('scroll', onScroll, { passive: true });
  S.cleanups.push(() => window.removeEventListener('scroll', onScroll));
  window.scrollTo(0, 0);
  return main;
}

function go(hash) { location.hash = hash; }

function errorBox(e) { return h('div', { class: 'error-box' }, e.message || String(e)); }

function loading() { return h('div', { class: 'empty' }, h('span', { class: 'spinner' })); }

function every(ms, fn) {
  const t = setInterval(() => { if (!document.hidden) fn(); }, ms);
  const vis = () => { if (!document.hidden) fn(); };
  document.addEventListener('visibilitychange', vis);
  S.cleanups.push(() => { clearInterval(t); document.removeEventListener('visibilitychange', vis); });
}

// ------------------------------------------------------------------ install hint
function installBanner() {
  if (isStandalone() || localStorage.getItem('cpsync.hideInstall')) return null;
  const hide = () => { localStorage.setItem('cpsync.hideInstall', '1'); el.remove(); };
  let el;
  if (isIOS) {
    el = h('div', { class: 'banner' },
      h('div', { class: 'grow' }, h('b', {}, 'Установите как приложение'),
        h('span', {}, 'Нажмите ', h('span', { html: ICONS.share }), ' «Поделиться» → «На экран „Домой“».')),
      h('button', { class: 'icon-sm', onclick: hide, 'aria-label': 'Скрыть' }, '✕'));
  } else if (window.deferredInstall) {
    el = h('div', { class: 'banner' },
      h('div', { class: 'grow' }, h('b', {}, 'Установите как приложение'), 'Будет открываться с рабочего стола, как обычная программа.'),
      h('button', { class: 'btn small primary', onclick: async () => { window.deferredInstall.prompt(); hide(); } }, 'Установить'),
      h('button', { class: 'icon-sm', onclick: hide, 'aria-label': 'Скрыть' }, '✕'));
  }
  return el || null;
}
window.addEventListener('beforeinstallprompt', (e) => { e.preventDefault(); window.deferredInstall = e; });

// ------------------------------------------------------------------ screens
function viewWelcome(mode = 'login') {
  const main = page({ title: '' });
  main.closest('body').querySelector('.top').classList.add('hidden');
  const err = h('div', { class: 'error-box hidden' });
  const login = h('input', { class: 'input', autocomplete: 'username', autocapitalize: 'off', autocorrect: 'off', spellcheck: 'false', placeholder: 'например, danis' });
  const pass = h('input', { class: 'input', type: 'password', autocomplete: mode === 'login' ? 'current-password' : 'new-password', placeholder: mode === 'login' ? '' : 'не короче 6 символов' });
  const btn = h('button', { class: 'btn primary block', type: 'submit' }, mode === 'login' ? 'Войти' : 'Создать аккаунт');
  const form = h('form', {
    onsubmit: async (e) => {
      e.preventDefault();
      err.classList.add('hidden');
      btn.disabled = true;
      try {
        const r = await api('/api/auth/' + (mode === 'login' ? 'login' : 'register'), {
          method: 'POST', body: { login: login.value.trim(), password: pass.value, deviceName: deviceName(), kind: 'web' } });
        setSession(r.token, r.login);
        go('#/');
      } catch (e2) {
        err.textContent = e2.message; err.classList.remove('hidden');
      } finally { btn.disabled = false; }
    },
  },
  h('label', { class: 'field' }, h('span', {}, 'Логин'), login),
  h('label', { class: 'field' }, h('span', {}, 'Пароль'), pass),
  err, btn);
  const seg = h('div', { class: 'seg' },
    h('button', { class: mode === 'login' ? 'on' : '', onclick: () => viewWelcome('login') }, 'Вход'),
    h('button', { class: mode === 'register' ? 'on' : '', onclick: () => viewWelcome('register') }, 'Регистрация'));
  const feat = (ic, t, d) => h('div', { class: 'feature' }, h('div', { class: 'dot', html: ICONS[ic] }), h('div', {}, h('b', {}, t), d));
  main.replaceChildren(h('div', { class: 'welcome' },
    h('img', { class: 'logo', src: '/icons/icon-192.png', alt: '' }),
    h('h1', {}, 'CP Sync'),
    h('p', { class: 'lead' }, 'Олимпиадные задачи из CLion — на всех ваших устройствах. Тесты запускаются прямо с телефона.'),
    h('div', { class: 'card' }, seg, form),
    h('div', { class: 'features' },
      feat('sync', 'Синхронизация CLion', 'Сохранили файл на одном ноутбуке — он уже на другом и в телефоне.'),
      feat('play', 'Тесты с телефона', 'Вводите тесты и смотрите вердикты: код компилируется на сервере, ноутбук может быть выключен.'),
      feat('code', 'Правка кода где угодно', 'Исправьте решение прямо в телефоне — изменения сами придут в CLion.')),
    h('div', { class: 'footer' }, 'CP Sync ' + VERSION)));
  if (!isPhone()) login.focus();
}

async function viewLink(code) {
  const main = page({ title: 'Подключение…' }, loading());
  try {
    const r = await api('/api/auth/link', { method: 'POST', body: { code, deviceName: deviceName(), kind: 'web' } });
    setSession(r.token, r.login);
    toast('Готово! Вы вошли как ' + r.login);
    go('#/');
  } catch (e) {
    main.replaceChildren(errorBox(e), h('div', { class: 'btn-row' }, h('a', { class: 'btn primary', href: '#/welcome' }, 'Войти по логину')));
  }
}

async function viewProjects() {
  const newProject = async () => {
    const name = await askText({ title: 'Новый проект', placeholder: 'Название, например «Отбор 2026»', ok: 'Создать',
      validate: (v) => (!v ? 'Введите название' : /[/\\:*?"<>|]/.test(v) || v.startsWith('.') ? 'Нельзя использовать символы / \\ : * ? " < > |' : null) });
    if (!name) return;
    try { await api('/api/projects', { method: 'POST', body: { name } }); go('#/p/' + enc(name)); } catch (e) { toast(e.message); }
  };
  const main = page({ title: 'Проекты', big: true, actions: [
    h('button', { class: 'icon-btn', 'aria-label': 'Новый проект', onclick: newProject }, icon('plus')),
    h('button', { class: 'icon-btn', 'aria-label': 'Аккаунт', onclick: () => go('#/account') }, icon('user'))] });
  const listBox = h('div', {}, loading());
  main.append(installBanner() || '', listBox);
  const load = async () => {
    try {
      const { projects } = await api('/api/projects');
      if (!projects.length) {
        listBox.replaceChildren(h('div', { class: 'empty' }, h('span', { html: ICONS.folder }),
          h('h3', {}, 'Пока нет проектов'),
          h('p', {}, 'Подключите CLion — проекты появятся здесь сами. Или создайте проект прямо тут.'),
          h('div', { class: 'btn-row', style: 'justify-content:center' },
            h('button', { class: 'btn primary', onclick: newProject }, 'Создать проект'),
            h('a', { class: 'btn', href: '#/account' }, 'Подключить CLion'))));
        return;
      }
      listBox.replaceChildren(h('div', { class: 'list', style: 'margin-top:12px' }, projects.map((p) =>
        h('a', { class: 'row', href: '#/p/' + enc(p.name) },
          h('div', { class: 'row-icon proj', html: ICONS.folder }),
          h('div', { class: 'main' }, h('div', { class: 'title' }, p.name),
            h('div', { class: 'meta' }, plural(p.fileCount, 'файл', 'файла', 'файлов'), ' · ', ago(p.updatedAt), p.updatedBy ? ' · ' + p.updatedBy : '')),
          h('span', { class: 'chev', html: ICONS.chev })))));
    } catch (e) { listBox.replaceChildren(errorBox(e)); }
  };
  await load();
  every(10000, load);
}

async function viewProject(name) {
  const addFile = async () => {
    const path = await askText({ title: 'Новый файл', text: 'Например A.cpp, B.py или tasks/C.cpp', placeholder: 'A.cpp', ok: 'Создать',
      validate: (v) => (!v ? 'Введите имя файла' : /(^|\/)\.\.?(\/|$)|^\/|\\|\/\/|\/$/.test(v) ? 'Некорректное имя' : null) });
    if (!path) return;
    try {
      const m = await api(projUrl(name) + '/manifest').catch(() => null);
      if (m && m.files[path] && !m.files[path].deleted) { toast('Такой файл уже есть'); return; }
      await api(projUrl(name) + '/file?path=' + enc(path) + '&base=', { method: 'PUT', raw: TEMPLATES[extOf(path)] || '' });
      go('#/p/' + enc(name) + '/f/' + enc(path) + (isRunnable(path) ? '/code' : ''));
    } catch (e) { toast(e.message); }
  };
  const menu = async () => {
    const ok = await confirmBox({ title: 'Удалить проект «' + name + '»?', text: 'Он исчезнет с сервера и из телефона. Папки на ноутбуках останутся, но перестанут синхронизироваться.', ok: 'Удалить', danger: true });
    if (!ok) return;
    try { await api(projUrl(name), { method: 'DELETE' }); toast('Проект удалён'); go('#/'); } catch (e) { toast(e.message); }
  };
  const main = page({ title: name, back: '#/', actions: [
    h('button', { class: 'icon-btn', 'aria-label': 'Новый файл', onclick: addFile }, icon('plus')),
    h('button', { class: 'icon-btn', 'aria-label': 'Ещё', onclick: menu }, icon('more'))] });
  const box = h('div', {}, loading());
  main.append(box);
  const load = async () => {
    try {
      const m = await api(projUrl(name) + '/manifest');
      const files = Object.entries(m.files).filter(([, f]) => !f.deleted).sort((a, b) => b[1].mtime - a[1].mtime);
      const runnable = files.filter(([p]) => isRunnable(p));
      const other = files.filter(([p]) => !isRunnable(p));
      const row = ([p, f]) => {
        const e = extOf(p);
        const cls = ['cpp', 'cc', 'cxx'].includes(e) ? 'cpp' : e === 'c' ? 'c' : e === 'py' ? 'py' : HEADER_EXT.includes(e) ? 'h' : 'txt';
        return h('a', { class: 'row', href: '#/p/' + enc(name) + '/f/' + enc(p) + (isRunnable(p) ? '' : '/code') },
          h('div', { class: 'row-icon ' + cls }, (e || 'txt').slice(0, 3).toUpperCase()),
          h('div', { class: 'main' }, h('div', { class: 'title mono' }, baseName(p)),
            h('div', { class: 'meta' }, dirName(p) ? dirName(p) + ' · ' : '', ago(f.mtime), f.by ? ' · ' + f.by : '')),
          h('span', { class: 'chev', html: ICONS.chev }));
      };
      box.replaceChildren(h('div', {},
        !files.length ? h('div', { class: 'empty' }, h('h3', {}, 'В проекте нет файлов'), h('p', {}, 'Создайте решение — например, A.cpp.'),
          h('button', { class: 'btn primary', onclick: addFile }, 'Создать файл')) : null,
        runnable.length ? [h('div', { class: 'section-title' }, 'Решения · новые сверху'), h('div', { class: 'list' }, runnable.map(row))] : null,
        other.length ? [h('div', { class: 'section-title' }, 'Другие файлы'), h('div', { class: 'list' }, other.map(row))] : null));
    } catch (e) { box.replaceChildren(errorBox(e)); }
  };
  await load();
  every(10000, load);
}

// ------------------------------------------------------------------ file: tests + code
async function viewFile(project, path, tab) {
  const runnable = isRunnable(path);
  if (!runnable) tab = 'code';
  const st = {
    tab: tab || 'tests',
    tests: null, result: null, error: null, running: false, status: '',
    code: null, codeHash: null, dirty: false, jobAbort: null,
    tl: +(localStorage.getItem('cpsync.tl') || 2000),
    ml: +(localStorage.getItem('cpsync.ml') || 256),
    std: localStorage.getItem('cpsync.std') || 'c++20',
  };
  const fileUrl = '#/p/' + enc(project) + '/f/' + enc(path);
  const main = page({ title: baseName(path), sub: project, back: '#/p/' + enc(project) });
  const tabsEl = h('div', { class: 'seg tabs' });
  const body = h('div', {});
  const bottom = h('div', { class: 'bottom' });
  main.append(runnable ? tabsEl : null, body);
  if (runnable) document.body.append(bottom);
  S.cleanups.push(() => { bottom.remove(); if (st.jobAbort) st.jobAbort.abort(); });
  S.guard = () => !st.dirty || window.confirm('Изменения в коде не сохранены. Уйти без сохранения?');
  const beforeUnload = (e) => { if (st.dirty) { e.preventDefault(); e.returnValue = ''; } };
  window.addEventListener('beforeunload', beforeUnload);
  S.cleanups.push(() => window.removeEventListener('beforeunload', beforeUnload));

  // ---------- data
  const loadCode = async () => {
    const r = await api(projUrl(project) + '/file?path=' + enc(path));
    st.code = r.text; st.codeHash = r.hash; st.dirty = false;
  };
  let saveTimer;
  const saveTests = () => {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => api(projUrl(project) + '/tests?path=' + enc(path), { method: 'PUT', body: { tests: st.tests } }).catch(() => {}), 700);
  };
  S.cleanups.push(() => { if (saveTimer) { clearTimeout(saveTimer); api(projUrl(project) + '/tests?path=' + enc(path), { method: 'PUT', body: { tests: st.tests } }).catch(() => {}); } });

  try {
    const [t] = await Promise.all([
      runnable ? api(projUrl(project) + '/tests?path=' + enc(path)) : Promise.resolve({ tests: [] }),
      loadCode(),
    ]);
    st.tests = t.tests.length ? t.tests : [{ input: '', expected: '' }];
  } catch (e) {
    body.replaceChildren(errorBox(e));
    return;
  }

  // ---------- render
  const renderTabs = () => {
    tabsEl.replaceChildren(
      h('button', { class: st.tab === 'tests' ? 'on' : '', onclick: () => { st.tab = 'tests'; history.replaceState(null, '', fileUrl); render(); } }, 'Тесты'),
      h('button', { class: st.tab === 'code' ? 'on' : '', onclick: () => { st.tab = 'code'; history.replaceState(null, '', fileUrl + '/code'); render(); } }, 'Код' + (st.dirty ? ' •' : '')));
  };

  const chip = (ic, label, value, options, onchange) => h('label', { class: 'chip' }, h('span', { html: ICONS[ic], style: 'display:inline-flex' }), label,
    h('select', { onchange: (e) => onchange(e.target.value), 'aria-label': label },
      options.map(([v, t]) => h('option', { value: v, selected: String(v) === String(value) }, t))));

  const renderTests = () => {
    const r = st.result;
    const lang = extOf(path);
    const els = [h('div', { class: 'chips' },
      chip('timer', st.tl < 1000 ? st.tl + ' мс' : st.tl / 1000 + ' с', st.tl, [[500, '0,5 с'], [1000, '1 с'], [2000, '2 с'], [3000, '3 с'], [5000, '5 с'], [10000, '10 с']],
        (v) => { st.tl = +v; localStorage.setItem('cpsync.tl', v); render(); }),
      chip('mem', st.ml + ' МБ', st.ml, [[64, '64 МБ'], [128, '128 МБ'], [256, '256 МБ'], [512, '512 МБ']],
        (v) => { st.ml = +v; localStorage.setItem('cpsync.ml', v); render(); }),
      lang !== 'py' && lang !== 'c' ? chip('code', st.std.toUpperCase().replace('C++', 'C++'), st.std, [['c++17', 'C++17'], ['c++20', 'C++20'], ['c++23', 'C++23']],
        (v) => { st.std = v; localStorage.setItem('cpsync.std', v); render(); }) : null)];

    if (st.error) els.push(errorBox({ message: st.error }));
    if (r && !r.compile.ok) {
      els.push(h('div', { class: 'compile' }, h('h3', {}, h('span', { class: 'badge v-CE' }, 'CE'), 'Ошибка компиляции'),
        h('pre', { class: 'out' }, r.compile.output || '')));
    } else if (r && r.compile.output) {
      els.push(h('details', { class: 'compile' }, h('summary', {}, 'Предупреждения компилятора'), h('pre', { class: 'out', style: 'margin-top:8px' }, r.compile.output)));
    }

    st.tests.forEach((t, i) => {
      const res = r && r.compile.ok ? r.tests[i] : null;
      const input = h('textarea', { class: 'code', rows: 3, spellcheck: 'false', autocapitalize: 'off', autocorrect: 'off', placeholder: 'Входные данные' });
      input.value = t.input;
      input.addEventListener('input', () => { const v = normalizeTyping(input.value); if (v !== input.value) input.value = v; t.input = v; saveTests(); });
      const exp = h('textarea', { class: 'code small', rows: 2, spellcheck: 'false', autocapitalize: 'off', autocorrect: 'off', placeholder: 'Ожидаемый ответ — можно не заполнять' });
      exp.value = t.expected || '';
      exp.addEventListener('input', () => { const v = normalizeTyping(exp.value); if (v !== exp.value) exp.value = v; t.expected = v; saveTests(); });
      const paste = async () => {
        try { const s = await navigator.clipboard.readText(); input.value = t.input = s; saveTests(); } catch (e) { toast('Нет доступа к буферу обмена — вставьте вручную'); }
      };
      els.push(h('div', { class: 'test' },
        h('div', { class: 'test-head' },
          h('b', {}, 'Тест ' + (i + 1)),
          res ? h('span', { class: 'badge v-' + res.verdict, title: verdictTitle(res.verdict) }, res.verdict) : null,
          res ? h('span', { class: 'stat' }, res.timeMs + ' мс · ' + fmtMem(res.memoryKb || 0)) : null,
          h('span', { class: 'grow' }),
          h('button', { class: 'icon-sm', title: 'Вставить из буфера', 'aria-label': 'Вставить из буфера', onclick: paste, html: ICONS.paste }),
          st.tests.length > 1 ? h('button', { class: 'icon-sm', title: 'Удалить тест', 'aria-label': 'Удалить тест', html: ICONS.trash,
            onclick: () => { st.tests.splice(i, 1); st.result = null; saveTests(); render(); } }) : null),
        input,
        h('div', { class: 'lbl' }, 'Ожидаемый ответ'),
        exp,
        res ? [
          h('div', { class: 'lbl' }, h('span', {}, res.truncated ? 'Вывод (показано начало)' : 'Вывод'),
            res.stdout ? h('button', { onclick: () => copyText(res.stdout) }, 'Копировать') : null),
          h('pre', { class: 'out' + (res.verdict === 'WA' ? ' bad' : '') }, res.stdout || '(пусто)'),
          res.exitInfo ? h('div', { class: 'info-line' }, verdictTitle(res.verdict) + ': ' + res.exitInfo) : null,
          res.stderr ? [h('div', { class: 'lbl' }, 'stderr'), h('pre', { class: 'out err' }, res.stderr)] : null,
        ] : null));
    });
    els.push(h('button', { class: 'btn block', style: 'margin-top:4px', onclick: () => { st.tests.push({ input: '', expected: '' }); st.result = null; saveTests(); render(); } },
      h('span', { html: ICONS.plus, style: 'display:inline-flex;width:20px' }), 'Добавить тест'));
    if (r) {
      const parts = [];
      if (r.compile.cached) parts.push('скомпилированная версия из кэша');
      else if (r.compile.timeMs) parts.push('компиляция ' + (r.compile.timeMs / 1000).toFixed(1) + ' с');
      if (r.tool) parts.push(r.tool);
      if (r.edited) parts.push('запущен несохранённый код');
      els.push(h('p', { class: 'note center' }, parts.join(' · ')));
    }
    return els;
  };

  let gutter;
  const renderCode = () => {
    const ta = h('textarea', { class: 'src', spellcheck: 'false', autocapitalize: 'off', autocorrect: 'off', autocomplete: 'off', wrap: 'off' });
    ta.value = st.code;
    gutter = h('div', { class: 'gutter' });
    const updGutter = () => {
      const n = ta.value.split('\n').length;
      if (gutter.childElementCount !== 1 || gutter.dataset.n !== String(n)) {
        gutter.dataset.n = n;
        gutter.textContent = Array.from({ length: n }, (_, i) => i + 1).join('\n');
      }
      ta.style.height = 'auto';
      ta.style.height = Math.max(ta.scrollHeight, window.innerHeight * 0.6) + 'px';
    };
    const saveBtn = h('button', { class: 'btn small primary', disabled: !st.dirty, onclick: () => saveCode() }, 'Сохранить');
    const status = h('span', { class: 'grow' }, st.dirty ? 'Не сохранено' : 'Сохранено');
    ta.addEventListener('input', () => {
      const v = normalizeTyping(ta.value);
      if (v !== ta.value) { const pos = ta.selectionStart; ta.value = v; ta.selectionStart = ta.selectionEnd = Math.min(pos, v.length); }
      st.code = ta.value;
      if (!st.dirty) { st.dirty = true; saveBtn.disabled = false; status.textContent = 'Не сохранено'; renderTabs(); renderBottom(); }
      updGutter();
    });
    ta.addEventListener('keydown', (e) => {
      if (e.key === 'Tab' && !e.shiftKey) { e.preventDefault(); document.execCommand('insertText', false, '    '); }
      else if (e.key === 'Enter' && !e.isComposing) {
        const before = ta.value.slice(0, ta.selectionStart);
        const line = before.slice(before.lastIndexOf('\n') + 1);
        let indent = line.match(/^\s*/)[0];
        if (/[{(\[:]\s*$/.test(line)) indent += '    ';
        e.preventDefault();
        document.execCommand('insertText', false, '\n' + indent);
      } else if ((e.ctrlKey || e.metaKey) && e.key === 's') { e.preventDefault(); saveCode(); }
      else if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); runTests(); }
    });
    const wrap = h('div', { class: 'editor-wrap' },
      h('div', { class: 'editor-bar' }, status, h('button', { class: 'icon-sm', title: 'Копировать код', html: ICONS.copy, onclick: () => copyText(st.code) }), saveBtn),
      h('div', { class: 'editor' }, gutter, ta));
    setTimeout(updGutter, 0);
    return [wrap, h('p', { class: 'note' }, (isPhone() ? '' : 'Ctrl/⌘+S — сохранить, Ctrl/⌘+Enter — запустить. ') +
      'После сохранения файл сам появится в CLion.' + (runnable ? ' Несохранённый код тоже можно запускать.' : ''))];
  };

  const saveCode = async (force = false) => {
    try {
      const r = await api(projUrl(project) + '/file?path=' + enc(path) + (force ? '' : '&base=' + enc(st.codeHash || '')), { method: 'PUT', raw: st.code });
      st.codeHash = r.hash; st.dirty = false;
      toast('Сохранено — CLion получит изменения');
      render();
    } catch (e) {
      if (e.status === 409) {
        const ok = await confirmBox({ title: 'Файл изменился на другом устройстве', text: 'Пока вы редактировали, файл сохранили в другом месте (например, в CLion). Перезаписать его вашей версией?', ok: 'Перезаписать', danger: true });
        if (ok) saveCode(true);
      } else toast(e.message);
    }
  };

  function verdictTitle(v) {
    return { AC: 'Верно', WA: 'Неверный ответ', OK: 'Выполнено', TLE: 'Превышено время', MLE: 'Превышена память', RE: 'Ошибка выполнения', CE: 'Ошибка компиляции' }[v] || v;
  }

  const renderBottom = () => {
    if (!runnable) return;
    let status;
    if (st.running) status = h('div', { class: 'status' }, h('span', { class: 'spinner' }), ' ', st.status);
    else if (st.result) {
      const r = st.result;
      if (!r.compile.ok) status = h('div', { class: 'status bad' }, h('b', {}, 'Ошибка компиляции'));
      else {
        const good = r.tests.filter((t) => t.verdict === 'AC' || t.verdict === 'OK').length;
        const all = r.tests.length === good;
        status = h('div', { class: 'status ' + (all ? 'good' : 'bad') }, h('b', {}, all ? '✓ ' : '', good + ' из ' + r.tests.length), ' без ошибок');
      }
    } else status = h('div', { class: 'status' }, st.dirty ? 'Будет запущен изменённый код' : plural(st.tests.length, 'тест', 'теста', 'тестов'));
    bottom.replaceChildren(h('div', { class: 'bottom-inner' }, status,
      h('button', { class: 'btn primary', disabled: st.running, onclick: runTests }, h('span', { html: ICONS.play, style: 'display:inline-flex' }), 'Запустить')));
  };

  const render = () => {
    renderTabs();
    body.replaceChildren(...(st.tab === 'tests' ? renderTests() : renderCode()));
    renderBottom();
  };

  const runTests = async () => {
    if (st.running) return;
    document.activeElement && document.activeElement.blur && document.activeElement.blur();
    st.running = true; st.error = null; st.status = 'Отправка…';
    renderBottom();
    const abort = new AbortController();
    st.jobAbort = abort;
    try {
      const job = await api('/api/run', { method: 'POST', signal: abort.signal, body: {
        project, file: path, tests: st.tests.map((t) => ({ input: t.input, expected: (t.expected || '').trim() ? t.expected : null })),
        timeLimitMs: st.tl, memoryLimitMb: st.ml, std: st.std, source: st.dirty ? st.code : undefined } });
      let j = job;
      while (j.status === 'queued' || j.status === 'running') {
        st.status = j.status === 'queued' && j.queuePosition > 1 ? 'В очереди: ' + j.queuePosition : 'Компиляция и тесты…';
        renderBottom();
        j = await api('/api/jobs/' + job.id + '?wait=20', { signal: abort.signal });
      }
      if (j.status === 'done') {
        st.result = j.result;
        if (navigator.vibrate) navigator.vibrate(30);
      } else st.error = j.error || 'Не удалось выполнить';
    } catch (e) {
      if (e.name === 'AbortError') return;
      st.error = e.message;
    } finally {
      st.jobAbort = null;
    }
    st.running = false;
    if (st.tab !== 'tests') { st.tab = 'tests'; history.replaceState(null, '', fileUrl); }
    render();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  render();
}

// ------------------------------------------------------------------ account
async function viewAccount() {
  const main = page({ title: 'Аккаунт', back: '#/' });
  main.append(loading());
  let me, cfg;
  try { [me, cfg] = await Promise.all([api('/api/me'), api('/api/config')]); } catch (e) { main.replaceChildren(errorBox(e)); return; }

  const qrBox = h('div', {});
  const showQr = async () => {
    qrBox.replaceChildren(loading());
    try {
      const l = await api('/api/link-codes', { method: 'POST', body: {} });
      qrBox.replaceChildren(
        h('img', { class: 'qr', src: l.qrSvg.replace(/^https?:\/\/[^/]+/, ''), alt: 'QR-код для входа' }),
        h('p', { class: 'center' }, 'Наведите камеру iPhone и откройте ссылку. Код одноразовый и действует 10 минут.'),
        h('div', { class: 'copy-field' }, h('code', {}, l.url), h('button', { class: 'btn small', onclick: () => copyText(l.url) }, 'Копировать')));
    } catch (e) { qrBox.replaceChildren(errorBox(e)); }
  };
  const linkBox = h('div', {});
  const ideLink = async () => {
    try {
      const l = await api('/api/link-codes', { method: 'POST', body: {} });
      linkBox.replaceChildren(h('p', {}, 'Вставьте эту ссылку в окне входа CP Sync в CLion (действует 10 минут):'),
        h('div', { class: 'copy-field' }, h('code', {}, l.url), h('button', { class: 'btn small', onclick: () => copyText(l.url) }, 'Копировать')));
    } catch (e) { linkBox.replaceChildren(errorBox(e)); }
  };

  const devices = h('div', { class: 'list' }, me.devices.map((d) => h('div', { class: 'row plain', style: 'cursor:default' },
    h('div', { class: 'dev-kind', html: d.kind === 'ide' || !/iPhone|iPad|Android/.test(d.name) ? ICONS.laptop : ICONS.phone }),
    h('div', { class: 'main' }, h('div', { class: 'title' }, d.name, d.id === me.currentDevice ? h('span', { class: 'tag' }, 'это устройство') : null),
      h('div', { class: 'meta' }, (d.kind === 'ide' ? 'CLion' : 'браузер') + ' · активность ' + ago(d.lastSeen))),
    d.id === me.currentDevice ? null : h('button', { class: 'btn small danger', onclick: async () => {
      if (!(await confirmBox({ title: 'Отключить «' + d.name + '»?', text: 'На этом устройстве придётся войти заново.', ok: 'Отключить', danger: true }))) return;
      try { await api('/api/devices/' + d.id, { method: 'DELETE' }); viewAccount(); } catch (e) { toast(e.message); }
    } }, 'Отключить'))));

  const oldP = h('input', { class: 'input', type: 'password', autocomplete: 'current-password' });
  const newP = h('input', { class: 'input', type: 'password', autocomplete: 'new-password', placeholder: 'не короче 6 символов' });
  const passForm = h('details', { class: 'card' }, h('summary', { style: 'font-weight:600;cursor:pointer' }, 'Сменить пароль'),
    h('label', { class: 'field' }, h('span', {}, 'Текущий пароль'), oldP),
    h('label', { class: 'field' }, h('span', {}, 'Новый пароль'), newP),
    h('button', { class: 'btn primary', onclick: async () => {
      try { await api('/api/me/password', { method: 'POST', body: { old: oldP.value, new: newP.value } }); toast('Пароль изменён'); oldP.value = newP.value = ''; } catch (e) { toast(e.message); }
    } }, 'Сохранить'));

  main.replaceChildren(
    h('div', { class: 'card' }, h('h2', {}, me.login), h('p', {}, 'Сервер: ' + location.host),
      h('div', { class: 'btn-row' }, h('button', { class: 'btn danger', onclick: async () => {
        try { await api('/api/auth/logout', { method: 'POST', body: {} }); } catch (e) { /* всё равно выходим */ }
        setSession('', ''); go('#/welcome');
      } }, 'Выйти'))),

    h('div', { class: 'card' }, h('h2', {}, 'Подключить CLion'),
      h('ol', {},
        h('li', {}, h('b', {}, 'Скачайте плагин'), ' — кнопка ниже (адрес этого сервера уже внутри).'),
        h('li', {}, 'В CLion: ', h('b', {}, 'Settings → Plugins → ⚙ → Install Plugin from Disk…'), ' и выберите скачанный файл (распаковывать не нужно).'),
        h('li', {}, 'Справа появится окно ', h('b', {}, 'CP Sync'), '. Нажмите «Войти» и введите этот же логин и пароль.'),
        h('li', {}, 'Откройте проект и нажмите ', h('b', {}, 'Поделиться проектом'), ' — дальше всё синхронизируется само.')),
      h('div', { class: 'btn-row' }, h('a', { class: 'btn primary', href: '/download/cpsync-plugin.zip', download: 'cpsync-plugin.zip' }, 'Скачать плагин'),
        h('button', { class: 'btn', onclick: ideLink }, 'Войти без пароля')),
      linkBox),

    h('div', { class: 'card' }, h('h2', {}, isPhone() ? 'Это устройство' : 'Подключить телефон'),
      isPhone()
        ? h('p', {}, isStandalone() ? 'CP Sync установлен как приложение.' : isIOS ? 'Чтобы открывать CP Sync как приложение: «Поделиться» → «На экран „Домой“».' : 'Добавьте CP Sync на главный экран через меню браузера.')
        : [h('p', {}, 'Покажите QR-код и наведите на него камеру телефона — вход выполнится сам.'), h('div', { class: 'btn-row' }, h('button', { class: 'btn primary', onclick: showQr }, 'Показать QR-код')), qrBox]),

    h('div', { class: 'section-title' }, 'Устройства'), devices,
    passForm,
    h('div', { class: 'footer' }, 'CP Sync ' + VERSION + (me.isAdmin ? ' · вы администратор сервера' : '') + (cfg.registration === 'closed' ? ' · регистрация закрыта' : '')));
}

// ------------------------------------------------------------------ router
let lastHash = location.hash;
function route() {
  if (S.guard && !S.guard()) { history.replaceState(null, '', lastHash); return; }
  S.guard = null;
  lastHash = location.hash;
  S.cleanups.forEach((f) => { try { f(); } catch (e) { /* ignore */ } });
  S.cleanups = [];
  document.querySelectorAll('.modal-back, .bottom').forEach((e) => e.remove());
  const parts = location.hash.replace(/^#\/?/, '').split('/').filter(Boolean).map(decodeURIComponent);
  if (parts[0] === 'link' && parts[1]) return viewLink(parts[1]);
  if (!S.token) return viewWelcome(parts[0] === 'register' ? 'register' : 'login');
  if (parts[0] === 'welcome' || parts[0] === 'register') { go('#/'); return; }
  if (parts[0] === 'account') return viewAccount();
  if (parts[0] === 'p' && parts[1] && parts[2] === 'f' && parts[3]) return viewFile(parts[1], parts[3], parts[4] === 'code' ? 'code' : 'tests');
  if (parts[0] === 'p' && parts[1]) return viewProject(parts[1]);
  return viewProjects();
}
window.addEventListener('hashchange', route);
route();

if ('serviceWorker' in navigator && location.protocol === 'https:') {
  navigator.serviceWorker.register('/sw.js').catch(() => {});
}
