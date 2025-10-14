# 🏡 SANTA-MARTA - Generador de PDFs Profesionales para Campos

Este proyecto genera PDFs profesionales para la venta de campos con información detallada, galería fotográfica y enlaces de contacto directo a Google Drive.

## ✨ Características Principales

- **🎨 Diseño profesional** con iconos y colores corporativos
- **📸 Galería fotográfica** con soporte para múltiples imágenes
- **🔗 Enlaces directos** a WhatsApp, Google Maps y Google Drive
- **📊 Información detallada** del campo con datos específicos
- **🏢 Nav bar corporativa** con identidad de marca
- **📱 Responsive** y optimizado para impresión A4

## 🚀 Requisitos

- Python 3.13+
- reportlab (ya instalado en el entorno virtual)
- Imágenes del campo (opcional)

## 📦 Instalación

1. **Activar el entorno virtual:**
```bash
source venv/bin/activate
```

2. **Instalar dependencias (si es necesario):**
```bash
pip install reportlab
```

## 🎯 Uso Rápido

1. **Activar el entorno virtual:**
```bash
source venv/bin/activate
```

2. **Generar el PDF:**
```bash
python generar_pdf_terreno.py
```

3. **El PDF se generará como `campo_santa_marta.pdf`**

## 📸 Galería Tipo Carrusel

### Estructura de la Galería
- **1 imagen principal grande** (12x8 cm) en la parte superior
- **4 miniaturas pequeñas** (3x2 cm cada una) en la parte inferior
- **Títulos descriptivos** para cada miniatura

### Nombres de Archivos
- `campo1.jpg` - **Imagen principal** (Vista general del campo)
- `campo2.jpg` - **Pasturas** (Gatton Panic)
- `campo3.jpg` - **Agrícola** (191 Has)
- `campo4.jpg` - **Monte** (437 Has)
- `campo5.jpg` - **Panorámica** (Vista aérea)

### Generar Imágenes de Ejemplo
```bash
# Imágenes básicas
python crear_imagenes_ejemplo.py

# Imágenes específicas para carrusel
python crear_imagenes_carrusel.py
```

## 🔗 Integración con Google Drive

### Configurar Enlaces
1. Suba las fotos a una carpeta en Google Drive
2. Comparta con acceso público
3. Copie el ID de la carpeta
4. Reemplace `XXXXXXX` en el código con el ID real

### Enlaces Automáticos
- **WhatsApp:** Contacto directo con mensaje predefinido
- **Google Maps:** Ubicación exacta del campo
- **Google Drive:** Galería completa de fotos

## 📋 Información del Campo

El PDF incluye automáticamente:
- **📍 Ubicación:** Santa Marta, Boquerón, Paraguay
- **🌱 Aptitud:** Mixto (Agrícola + Ganadero)
- **🌧️ Precipitación:** 800 mm anuales
- **📏 Superficie:** 1.747 Has totales
- **🌾 Desglose:** Agrícolas (191 Has), Ganaderas (715 Has), Monte (437 Has)
- **🗺️ Puntos de interés:** Distancias a ciudades importantes

## 🎨 Personalización

### Modificar Información
Edite las variables en `generar_pdf_terreno.py`:
- `info_campo` - Información del campo
- `puntos_interes` - Puntos de interés
- `whatsapp_link` - Enlace de WhatsApp
- `maps_link` - Enlace de Google Maps
- `drive_link` - Enlace de Google Drive

### Cambiar Estilos
Use los estilos en `navbar_estilos.py`:
1. **Corporativo Clásico** - Azul oscuro
2. **Moderno con Gradiente** - Azul claro
3. **Minimalista** - Gris claro
4. **Elegante con Sombra** - Morado

## 📁 Estructura del Proyecto

```
SANTA-MARTA/
├── generar_pdf_terreno.py        # Script principal
├── navbar_estilos.py             # Estilos de nav bar
├── crear_imagenes_ejemplo.py     # Generador de imágenes básicas
├── crear_imagenes_carrusel.py    # Generador de imágenes para carrusel
├── INSTRUCCIONES_IMAGENES.md     # Guía de imágenes
├── INSTRUCCIONES_CARRUSEL.md     # Guía específica del carrusel
├── README.md                     # Este archivo
├── venv/                         # Entorno virtual
├── campo_santa_marta.pdf         # PDF generado
└── campo1-5.pdf                  # Imágenes de ejemplo
```

## 🔧 Archivos de Configuración

- **`generar_pdf_terreno.py`** - Script principal con toda la lógica
- **`navbar_estilos.py`** - 4 estilos diferentes de nav bar
- **`crear_imagenes_ejemplo.py`** - Genera imágenes de prueba
- **`INSTRUCCIONES_IMAGENES.md`** - Guía completa para imágenes

## 📱 Características Técnicas

- **Formato:** PDF A4 optimizado
- **Imágenes:** JPG, PNG, GIF soportados
- **Enlaces:** Clicables en el PDF
- **Iconos:** Emojis integrados
- **Colores:** Paleta corporativa profesional
- **Tipografía:** Helvetica con múltiples pesos

## 🎯 Casos de Uso

- **Inmobiliarias** - Presentación de campos
- **Agentes inmobiliarios** - Material de marketing
- **Propietarios** - Venta directa de campos
- **Inversionistas** - Análisis de propiedades

## 📞 Soporte

Para personalizaciones adicionales o dudas:
- Revisar `INSTRUCCIONES_IMAGENES.md`
- Modificar variables en el código principal
- Usar estilos predefinidos en `navbar_estilos.py`

¡El PDF está listo para usar con Google Drive y contacto directo! 🚀
# santa-marta
