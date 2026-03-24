# 📱 Guía para generar iconos PWA

Necesitas crear iconos en 8 tamaños diferentes para que la PWA funcione correctamente.

## Opción 1: Herramienta Online (MÁS FÁCIL) ⭐

1. Ve a **https://www.pwabuilder.com/imageGenerator**
2. Sube tu logo (idealmente 512x512px con fondo)
3. Haz clic en "Download"
4. Descomprime el archivo ZIP
5. Copia todos los archivos a la carpeta `icons/` de tu proyecto

## Opción 2: Script Python (si tienes Python instalado)

```bash
# Instalar dependencia
pip install Pillow

# Ejecutar script
python generate-icons.py logo.png

# Los iconos se generarán en la carpeta icons/
```

## Opción 3: Manualmente con Photoshop/GIMP

Crea estas versiones de tu logo y guárdalas en la carpeta `icons/`:

- `icon-72x72.png` (72 x 72 píxeles)
- `icon-96x96.png` (96 x 96 píxeles)
- `icon-128x128.png` (128 x 128 píxeles)
- `icon-144x144.png` (144 x 144 píxeles)
- `icon-152x152.png` (152 x 152 píxeles)
- `icon-192x192.png` (192 x 192 píxeles)
- `icon-384x384.png` (384 x 384 píxeles)
- `icon-512x512.png` (512 x 512 píxeles)

## ⚠️ Importante

- Todos los iconos deben ser **cuadrados** (mismo ancho y alto)
- Formato: **PNG**
- Usa el logo con **fondo** (no transparente) para mejor visualización
- El color de fondo debe ser `#0B1022` (azul oscuro) para coincidir con la app

## 🎨 Recomendaciones

- **Logo centrado** con algo de padding (no tocar los bordes)
- **Fondo sólido** del color de la app
- **Alta resolución** en el original (mínimo 512x512)
- **Exportar con calidad máxima** para evitar pixelación

## ✅ Verificar instalación

Una vez generados y subidos a GitHub:

1. Espera 1-2 minutos para que GitHub Pages actualice
2. Abre https://chemaabravoo.github.io/LALISTAJMB/
3. Abre DevTools (F12) → Application → Manifest
4. Deberías ver todos los iconos cargados correctamente

## 🚨 Si los iconos no aparecen

- Verifica que la carpeta se llame exactamente `icons` (minúsculas)
- Verifica los nombres de archivo (deben coincidir exactamente con manifest.json)
- Asegúrate de que los archivos sean PNG (no JPG o JPEG)
- Limpia la caché del navegador y recarga
