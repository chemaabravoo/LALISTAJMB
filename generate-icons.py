#!/usr/bin/env python3
"""
Script para generar iconos PWA desde una imagen base
Requiere: pip install Pillow
Uso: python generate-icons.py logo.png
"""

import sys
import os
from PIL import Image

ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

def generate_icons(input_path):
    """Genera iconos en diferentes tamaños desde una imagen base"""
    
    if not os.path.exists(input_path):
        print(f"❌ Error: No se encuentra el archivo {input_path}")
        sys.exit(1)
    
    # Crear carpeta icons si no existe
    icons_dir = "icons"
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir)
        print(f"📁 Carpeta '{icons_dir}' creada")
    
    # Abrir imagen original
    try:
        img = Image.open(input_path)
        print(f"✅ Imagen cargada: {input_path} ({img.size[0]}x{img.size[1]})")
    except Exception as e:
        print(f"❌ Error al abrir la imagen: {e}")
        sys.exit(1)
    
    # Convertir a RGB si es necesario
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Generar cada tamaño
    for size in ICON_SIZES:
        output_path = os.path.join(icons_dir, f"icon-{size}x{size}.png")
        
        # Redimensionar con alta calidad
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Guardar
        resized.save(output_path, 'PNG', optimize=True)
        print(f"✅ Generado: {output_path}")
    
    print(f"\n🎉 ¡Completado! {len(ICON_SIZES)} iconos generados en la carpeta '{icons_dir}/'")
    print("\nSiguiente paso:")
    print("1. Sube la carpeta 'icons/' a tu repositorio GitHub")
    print("2. Verifica que las rutas en manifest.json sean correctas")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python generate-icons.py <imagen-base.png>")
        print("Ejemplo: python generate-icons.py logo.png")
        sys.exit(1)
    
    input_image = sys.argv[1]
    generate_icons(input_image)
