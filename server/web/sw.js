// CP Sync service worker: оболочка приложения открывается и без сети; данные API не кэшируются.
const CACHE = 'cpsync-shell-v2.0.0';
const SHELL = ['/', '/app.js', '/app.css', '/manifest.webmanifest', '/icons/icon-192.png', '/icons/apple-touch-icon.png', '/icons/favicon.svg'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  if (url.pathname.startsWith('/api/') || url.pathname.startsWith('/qr/') || url.pathname.startsWith('/download/')) return;
  // сначала сеть (чтобы обновления приходили сразу), без сети — из кэша
  const key = e.request.mode === 'navigate' ? '/' : e.request;
  e.respondWith(
    fetch(e.request).then((r) => {
      if (r.ok && SHELL.includes(url.pathname)) {
        const copy = r.clone();
        caches.open(CACHE).then((c) => c.put(key, copy));
      }
      return r;
    }).catch(() => caches.match(key).then((m) => m || caches.match('/')))
  );
});
