# 📸 Instrucciones para Galería Tipo Carrusel

## 🎯 Estructura de la Galería

La galería ahora tiene una estructura tipo carrusel con:
- **1 imagen principal grande** (12x8 cm) en la parte superior
- **4 miniaturas pequeñas** (3x2 cm cada una) en la parte inferior
- **Títulos descriptivos** para cada miniatura

## 📁 Nombres de Archivos Requeridos

### Imagen Principal (Grande)
- `campo1.jpg` - **Imagen principal del campo** (12x8 cm)
- `terreno.jpg` - **Alternativa** si no existe campo1.jpg

### Miniaturas (Pequeñas)
- `campo2.jpg` - **Pasturas** (3x2 cm)
- `campo3.jpg` - **Agrícola** (3x2 cm)  
- `campo4.jpg` - **Monte** (3x2 cm)
- `campo5.jpg` - **Panorámica** (3x2 cm)

## 🎨 Características Visuales

### Imagen Principal
- **Tamaño:** 12x8 cm
- **Marco:** Triple borde (negro, rojo, azul)
- **Fondo:** Gris claro
- **Padding:** 12px

### Miniaturas
- **Tamaño:** 3x2 cm cada una
- **Títulos:** Debajo de cada imagen
- **Marco:** Borde gris con línea azul
- **Layout:** 4 por fila (máximo)

## 📋 Cómo Agregar Imágenes

### Paso 1: Preparar las Imágenes
1. **Imagen principal:** Use la mejor foto del campo
2. **Miniaturas:** Seleccione 4 fotos representativas
3. **Formatos:** JPG, PNG, GIF soportados
4. **Resolución:** Mínimo 800x600 píxeles

### Paso 2: Renombrar Archivos
```
campo1.jpg  ← Imagen principal (Vista general del campo)
campo2.jpg  ← Pasturas Gatton Panic
campo3.jpg  ← Área agrícola
campo4.jpg  ← Zona de monte
campo5.jpg  ← Vista panorámica
```

### Paso 3: Colocar en Directorio
```
SANTA-MARTA/
├── campo1.jpg  ← Imagen principal
├── campo2.jpg  ← Miniatura 1
├── campo3.jpg  ← Miniatura 2
├── campo4.jpg  ← Miniatura 3
├── campo5.jpg  ← Miniatura 4
└── generar_pdf_terreno.py
```

### Paso 4: Generar PDF
```bash
source venv/bin/activate
python generar_pdf_terreno.py
```

## 🔧 Personalización

### Cambiar Títulos de Miniaturas
Edite la función `crear_galeria_carrusel()` en `generar_pdf_terreno.py`:

```python
miniaturas_info = [
    ('campo2.jpg', 'Tu Título 1'),
    ('campo3.jpg', 'Tu Título 2'),
    ('campo4.jpg', 'Tu Título 3'),
    ('campo5.jpg', 'Tu Título 4')
]
```

### Cambiar Tamaños
Modifique los parámetros en las funciones:
- `crear_imagen_principal(img_principal, 12*cm, 8*cm)` - Imagen principal
- `crear_miniatura(ruta, 3*cm, 2*cm, titulo)` - Miniaturas

### Agregar Más Miniaturas
1. Agregue más archivos: `campo6.jpg`, `campo7.jpg`, etc.
2. Modifique `miniaturas_info` en el código
3. Ajuste `colWidths` en `miniaturas_table`

## 📱 Integración con Google Drive

### Enlaces Automáticos
- **Imagen principal:** Se muestra grande en el PDF
- **Miniaturas:** Navegación visual
- **Google Drive:** Enlace a galería completa

### Configuración
1. Suba todas las fotos a Google Drive
2. Comparta la carpeta públicamente
3. Reemplace `XXXXXXX` en el código con el ID de la carpeta

## 🎯 Casos de Uso

### Campo Agrícola
- `campo1.jpg` - Vista aérea del campo completo
- `campo2.jpg` - Cultivos de soja
- `campo3.jpg` - Maquinaria agrícola
- `campo4.jpg` - Silo de almacenamiento
- `campo5.jpg` - Vista panorámica

### Campo Ganadero
- `campo1.jpg` - Vista general del campo
- `campo2.jpg` - Pasturas Gatton Panic
- `campo3.jpg` - Ganado pastando
- `campo4.jpg` - Corrales y instalaciones
- `campo5.jpg` - Vista desde el monte

## ✅ Verificación

### Checklist
- [ ] `campo1.jpg` existe (imagen principal)
- [ ] Al menos una miniatura existe
- [ ] Archivos están en el directorio correcto
- [ ] Enlace de Google Drive configurado
- [ ] PDF se genera sin errores

### Resultado Esperado
- **Imagen principal** grande en la parte superior
- **Miniaturas** en fila horizontal debajo
- **Títulos** descriptivos en cada miniatura
- **Enlace** a Google Drive para galería completa

¡La galería tipo carrusel está lista para usar! 🚀
