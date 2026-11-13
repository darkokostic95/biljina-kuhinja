// Biljina Kuhinja: offline support. Pages and files you have opened keep working without signal.
const CACHE = 'bk-v1';
const BASE = '/biljina-kuhinja/';
const SHELL = [BASE, BASE + 'search-index.json', BASE + 'brand/mark.svg', BASE + 'brand/logo-horizontal.svg'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const req = e.request;
  const u = new URL(req.url);
  if (req.method !== 'GET' || u.origin !== location.origin || !u.pathname.startsWith(BASE)) return;
  const isPage = req.mode === 'navigate';
  e.respondWith(
    caches.open(CACHE).then(async (cache) => {
      const hit = await cache.match(req, { ignoreSearch: isPage });
      const net = fetch(req).then((res) => { if (res.ok) cache.put(req, res.clone()); return res; }).catch(() => null);
      if (isPage) return (await net) || hit || cache.match(BASE);   // pages: fresh first, saved copy when offline
      return hit || (await net) || Response.error();                // files: saved copy first
    })
  );
});
