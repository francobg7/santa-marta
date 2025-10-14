# 📸 Instrucciones para Imágenes del Campo

## 🖼️ Cómo agregar fotos al PDF

### Opción 1: Imágenes individuales
Agregue las fotos del campo con estos nombres en el directorio del proyecto:
- `campo1.jpg` - Vista principal del campo
- `campo2.jpg` - Vista de pasturas
- `campo3.jpg` - Vista agrícola
- `campo4.jpg` - Vista del monte
- `campo5.jpg` - Vista aérea o panorámica

### Opción 2: Imagen principal
- `terreno.jpg` - Imagen principal del campo

## 📁 Integración con Google Drive

### Configuración del enlace
1. Suba todas las fotos a una carpeta en Google Drive
2. Comparta la carpeta con acceso público
3. Copie el enlace de la carpeta
4. Reemplace `XXXXXXX` en el código con el ID de la carpeta

### Ejemplo de enlace:
```
https://drive.google.com/drive/folders/1ABC123DEF456GHI789JKL
```

## 🎨 Formatos soportados
- JPG/JPEG
- PNG
- GIF

## 📏 Tamaños recomendados
- **Resolución:** Mínimo 800x600 píxeles
- **Relación de aspecto:** 4:3 o 16:9
- **Tamaño de archivo:** Máximo 5MB por imagen

## 🔧 Personalización

### Cambiar nombres de archivos
Edite la función `crear_galeria_imagenes()` en `generar_pdf_terreno.py`:

```python
# Cambiar los nombres de archivo aquí
for i in range(1, 6):
    ruta = f"mi_campo_{i}{ext}"  # Cambiar aquí
```

### Agregar más imágenes
Modifique el rango en la función:
```python
for i in range(1, 10):  # Cambiar 6 por 10 para más imágenes
```

## 🚀 Uso
1. Agregue las imágenes al directorio
2. Ejecute: `python generar_pdf_terreno.py`
3. El PDF se generará automáticamente con las imágenes

## 📱 Enlaces de Google Drive
Los enlaces se actualizarán automáticamente en:
- Botones de contacto
- Sección de galería
- Enlaces de texto
- Footer del PDF
