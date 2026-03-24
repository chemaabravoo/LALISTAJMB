# La Lista

**Tus objetivos. Tu historia.**

Una Progressive Web App para guardar y cumplir tus objetivos de vida.

## 🚀 Instalación

### En móvil (Android/iOS)

1. Abre https://chemaabravoo.github.io/LALISTAJMB/
2. **Android (Chrome)**: Toca "Añadir a pantalla de inicio" o el botón de instalar
3. **iOS (Safari)**: Toca el botón de compartir → "Añadir a pantalla de inicio"

### En desktop (Chrome/Edge)

1. Abre https://chemaabravoo.github.io/LALISTAJMB/
2. Haz clic en el icono de instalar en la barra de direcciones
3. La app se abrirá como aplicación independiente

## ✨ Características

- 📝 Crea objetivos con fotos, descripción y tareas
- ✅ Marca objetivos como cumplidos
- 📊 Seguimiento de progreso con porcentajes
- 🗂️ Organiza por categorías personalizadas
- 🌍 Añade ubicaciones con mapa
- 📤 Comparte tus logros en redes sociales
- 👥 Conecta con amigos y ve sus objetivos públicos
- 💾 Funciona sin conexión (PWA)
- 🔐 Autenticación segura con Firebase

## 🛠️ Tecnología

- Progressive Web App (PWA)
- Firebase Authentication & Firestore
- Vanilla JavaScript (sin frameworks)
- CSS moderno con variables
- Leaflet para mapas
- Service Workers para offline

## 📱 Estructura

```
LALISTAJMB/
├── index.html          # App principal
├── manifest.json       # Configuración PWA
├── service-worker.js   # Cache offline
├── logo.png           # Logo principal
├── logo-blanco.png    # Logo para fondo oscuro
└── icons/             # Iconos PWA
    ├── icon-72x72.png
    ├── icon-96x96.png
    ├── icon-128x128.png
    ├── icon-144x144.png
    ├── icon-152x152.png
    ├── icon-192x192.png
    ├── icon-384x384.png
    └── icon-512x512.png
```

## 🔧 Desarrollo local

```bash
# Clonar repositorio
git clone https://github.com/chemaabravoo/LALISTAJMB.git
cd LALISTAJMB

# Servir localmente (necesitas un servidor HTTP)
python -m http.server 8000
# o
npx serve

# Abrir en navegador
open http://localhost:8000
```

## 📝 Notas

- Los datos se guardan en Firebase Firestore
- Las fotos se comprimen automáticamente para ahorrar espacio
- Las categorías personalizadas se guardan en localStorage
- La app funciona offline una vez instalada

## 🙏 Créditos

Desarrollado por Chema Abravo
