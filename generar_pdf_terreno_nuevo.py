from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Group
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os

# === CONFIGURACIÓN ===
pdf_name = "campo_santa_marta.pdf"
doc = SimpleDocTemplate(pdf_name, pagesize=A4)

# === FUNCIONES AUXILIARES ===
def crear_imagen_principal(ruta_imagen, ancho, alto):
    """Crear imagen principal grande sin marco, ocupando todo el ancho"""
    try:
        if os.path.exists(ruta_imagen):
            return Image(ruta_imagen, width=ancho, height=alto)
        else:
            return None
    except:
        return None

def crear_miniatura(ruta_imagen, ancho, alto, titulo):
    """Crear miniatura más grande sin marco"""
    try:
        if os.path.exists(ruta_imagen):
            return Image(ruta_imagen, width=ancho, height=alto)
        else:
            return None
    except:
        return None

def crear_galeria_carrusel():
    """Crear galería tipo carrusel con imagen principal y miniaturas"""
    galeria = {
        'imagen_principal': None,
        'miniaturas': []
    }
    
    # Buscar imagen principal (campo1.jpg o terreno.jpg) - TAMAÑO COMPLETO
    imagenes_principales = ['campo1.jpg', 'terreno.jpg']
    for img_principal in imagenes_principales:
        if os.path.exists(img_principal):
            # Imagen principal ocupando todo el ancho del PDF (A4 = 21cm)
            galeria['imagen_principal'] = crear_imagen_principal(img_principal, 20*cm, 12*cm)
            break
    
    # Buscar miniaturas (campo2.jpg a campo5.jpg) - MÁS GRANDES
    miniaturas_info = [
        ('campo2.jpg', 'Pasturas'),
        ('campo3.jpg', 'Agrícola'),
        ('campo4.jpg', 'Monte'),
        ('campo5.jpg', 'Panorámica')
    ]
    
    for ruta, titulo in miniaturas_info:
        if os.path.exists(ruta):
            # Miniaturas más grandes (5x3 cm cada una)
            miniatura = crear_miniatura(ruta, 5*cm, 3*cm, titulo)
            if miniatura:
                galeria['miniaturas'].append(miniatura)
    
    return galeria

# === ESTILOS SIMPLIFICADOS ===
styles = getSampleStyleSheet()

# Estilos personalizados más limpios
styles.add(ParagraphStyle(name='TituloPrincipal', fontSize=24, leading=28, alignment=1, textColor=colors.white, spaceAfter=12))
styles.add(ParagraphStyle(name='Subtitulo', fontSize=16, leading=20, alignment=1, textColor=colors.white, spaceAfter=8))
styles.add(ParagraphStyle(name='InfoDestacada', fontSize=14, leading=18, alignment=1, textColor=colors.white, spaceAfter=6))
styles.add(ParagraphStyle(name='Precio', fontSize=20, leading=24, alignment=1, textColor=colors.HexColor('#f39c12'), spaceAfter=12))
styles.add(ParagraphStyle(name='Contacto', fontSize=12, leading=16, alignment=1, textColor=colors.white, spaceAfter=4))
styles.add(ParagraphStyle(name='Enlaces', fontSize=10, leading=12, alignment=1, textColor=colors.HexColor('#3498db'), spaceAfter=6))

story = []

# === INFORMACIÓN PRINCIPAL SOBRE FONDO ===
# Título principal con overlay sobre la imagen
titulo_principal = "CAMPO EN VENTA<br/><font size='16' color='#ecf0f1'>Santa Marta, Boquerón - Paraguay</font>"

# Información esencial del campo
info_esencial = """
<font size='14'><b>1.747 Has • Mixto (Agrícola + Ganadero)</b></font><br/>
<font size='12'>Agrícolas: 191 Has • Ganaderas: 715 Has • Monte: 437 Has</font><br/>
<font size='12'>Precipitación: 800 mm anuales</font>
"""

# Precio destacado
precio_destacado = "CONSULTAR PRECIO<br/><font size='12'>Contactar para más información</font>"

# Contacto directo
contacto_directo = """
<font size='12'><b>CONTACTO DIRECTO</b></font><br/>
<font size='11'>WhatsApp: +595 981 240 099</font><br/>
"""

# === CREAR OVERLAY DE INFORMACIÓN ===
# Crear tabla con información superpuesta
overlay_data = [
    [Paragraph(titulo_principal, styles['TituloPrincipal'])],
    [Spacer(1, 20)],
    [Paragraph(info_esencial, styles['InfoDestacada'])],
    [Spacer(1, 15)],
    [Paragraph(precio_destacado, styles['Precio'])],
    [Spacer(1, 20)],
    [Paragraph(contacto_directo, styles['Contacto'])]
]

overlay_table = Table(overlay_data, colWidths=[20*cm])
overlay_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 20),
    ('BOX', (0, 0), (-1, -1), 0, colors.HexColor('#2c3e50')),
]))

# === GALERÍA DE IMÁGENES ===
galeria = crear_galeria_carrusel()

# Imagen principal como fondo
if galeria['imagen_principal']:
    story.append(galeria['imagen_principal'])
    story.append(Spacer(1, 10))
    
    # Overlay de información sobre la imagen
    story.append(overlay_table)
    story.append(Spacer(1, 20))
    
    # Miniaturas
    if galeria['miniaturas']:
        # Crear tabla para miniaturas
        miniaturas_data = []
        for i in range(0, len(galeria['miniaturas']), 4):
            fila = galeria['miniaturas'][i:i+4]
            while len(fila) < 4:
                fila.append(Paragraph("", styles['Contacto']))
            miniaturas_data.append(fila)
        
        miniaturas_table = Table(miniaturas_data, colWidths=[5*cm, 5*cm, 5*cm, 5*cm])
        miniaturas_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 3),
        ]))
        
        story.append(miniaturas_table)
        story.append(Spacer(1, 15))
    
    # Enlaces de contacto
    whatsapp_link = "https://wa.me/595981240099?text=Hola%2C%20vi%20el%20campo%20en%20venta%20en%20Santa%20Marta%2C%20Boquerón"
    maps_link = "https://maps.google.com/?q=-23.2984734,-60.5146408"
    drive_link = "https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link"
    
    # Enlaces con diseño limpio
    enlaces_data = [
        [
            Paragraph(f"<a href='{whatsapp_link}' color='white'><b>WhatsApp</b><br/>+595 981 240 099</a>", 
                     ParagraphStyle(name='EnlaceBox', fontSize=12, leading=16, alignment=1, textColor=colors.white)),
            Paragraph(f"<a href='{maps_link}' color='white'><b>Google Maps</b><br/>Ver ubicación</a>", 
                     ParagraphStyle(name='EnlaceBox', fontSize=12, leading=16, alignment=1, textColor=colors.white)),
            Paragraph(f"<a href='{drive_link}' color='white'><b>Google Drive</b><br/>Ver fotos</a>", 
                     ParagraphStyle(name='EnlaceBox', fontSize=12, leading=16, alignment=1, textColor=colors.white))
        ]
    ]
    
    enlaces_table = Table(enlaces_data, colWidths=[6.5*cm, 6.5*cm, 6.5*cm])
    enlaces_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#25d366')),  # Verde WhatsApp
        ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#4285f4')),  # Azul Google
        ('BACKGROUND', (2, 0), (2, 0), colors.HexColor('#ff6b6b')),  # Rojo Google Drive
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('BOX', (0, 0), (-1, -1), 0, colors.white),
    ]))
    
    story.append(enlaces_table)
    story.append(Spacer(1, 20))
    
    # Información adicional sobre Google Drive
    drive_info = """
    <font color='#2c3e50'><b>GALERÍA COMPLETA EN GOOGLE DRIVE</b></font><br/>
    <font color='#7f8c8d'>Accede a todas las fotos del campo en alta resolución</font>
    """
    story.append(Paragraph(drive_info, styles['Enlaces']))
    
else:
    # Si no hay imagen principal, mostrar información básica
    story.append(Paragraph("CAMPO EN VENTA - Santa Marta, Boquerón", styles['TituloPrincipal']))
    story.append(Spacer(1, 20))
    story.append(overlay_table)

# === GENERAR PDF ===
try:
    doc.build(story)
    print("✅ PDF generado correctamente:", pdf_name)
    print("🎨 Diseño simplificado y profesional")
except Exception as e:
    print("❌ Error al generar PDF:", str(e))
