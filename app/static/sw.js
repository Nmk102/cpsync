// Удаляет service worker, который оставил прежний сайт (CP Sync), и его кэш,
// чтобы браузер показывал новый сайт, а не сохранённую старую страницу.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    for (const key of await caches.keys()) await caches.delete(key);
    await self.registration.unregister();
    for (const client of await self.clients.matchAll({ type: "window" })) client.navigate(client.url);
  })());
});
