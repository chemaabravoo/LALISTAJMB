// Service Worker v2.0 - Actualización forzada
const CACHE_NAME = 'lalista-v2.0';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/icon.png'
];

// Instalar y cachear recursos
self.addEventListener('install', event => {
  console.log('✅ Service Worker v2.0 instalando...');
  // Forzar activación inmediata
  self.skipWaiting();
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('📦 Cacheando archivos...');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activar y limpiar cachés antiguas
self.addEventListener('activate', event => {
  console.log('🔄 Service Worker v2.0 activado');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('🗑️ Borrando caché antigua:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      // Tomar control de todos los clientes inmediatamente
      return self.clients.claim();
    })
  );
});

// Estrategia: Network First, luego Cache
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Si la respuesta es válida, cachearla
        if (response && response.status === 200) {
          const responseToCache = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseToCache);
          });
        }
        return response;
      })
      .catch(() => {
        // Si falla la red, usar caché
        return caches.match(event.request);
      })
  );
});
