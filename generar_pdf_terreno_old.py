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
def crear_imagen_con_marco(ruta_imagen, ancho, alto, titulo=""):
    """Crear una imagen con marco decorativo y título"""
    try:
        if os.path.exists(ruta_imagen):
            # Crear tabla para la imagen con marco
            img_data = [
                [Image(ruta_imagen, width=ancho, height=alto)]
            ]
            img_table = Table(img_data, colWidths=[ancho + 1*cm])
            img_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#f8f9fa')),
                ('ALIGN', (0, 0), (0, 0), 'CENTER'),
                ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
                ('PADDING', (0, 0), (0, 0), 8),
                ('BOX', (0, 0), (0, 0), 2, colors.HexColor('#2c3e50')),
                ('LINEBELOW', (0, 0), (0, 0), 1, colors.HexColor('#3498db')),
            ]))
            return img_table
        else:
            return None
    except:
        return None

def crear_imagen_principal(ruta_imagen, ancho, alto):
    """Crear imagen principal grande sin marco, ocupando todo el ancho"""
    try:
        if os.path.exists(ruta_imagen):
            # Imagen sin marco, ocupando todo el ancho del PDF
            return Image(ruta_imagen, width=ancho, height=alto)
        else:
            return None
    except:
        return None

def crear_miniatura(ruta_imagen, ancho, alto, titulo):
    """Crear miniatura más grande sin marco"""
    try:
        if os.path.exists(ruta_imagen):
            # Imagen sin marco
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

def crear_background_decorativo():
    """Crear elementos decorativos de fondo"""
    drawing = Drawing(16*cm, 2*cm)
    
    # Líneas decorativas
    drawing.add(Line(0, 1*cm, 16*cm, 1*cm, strokeColor=colors.HexColor('#3498db'), strokeWidth=2))
    drawing.add(Line(0, 0.5*cm, 16*cm, 0.5*cm, strokeColor=colors.HexColor('#e74c3c'), strokeWidth=1))
    
    return drawing

styles = getSampleStyleSheet()

# === ESTILOS MEJORADOS ===
# Estilo para el título principal
styles.add(ParagraphStyle(
    name='TituloPrincipal', 
    fontSize=24, 
    leading=28, 
    spaceAfter=15, 
    alignment=1,
    textColor=colors.HexColor('#2c3e50'),
    fontName='Helvetica-Bold'
))

# Estilo para subtítulos
styles.add(ParagraphStyle(
    name='Subtitulo', 
    fontSize=16, 
    leading=20, 
    spaceAfter=8, 
    alignment=0,
    textColor=colors.HexColor('#34495e'),
    fontName='Helvetica-Bold'
))

# Estilo para texto descriptivo
styles.add(ParagraphStyle(
    name='Descripcion', 
    fontSize=13, 
    leading=18, 
    spaceAfter=12, 
    alignment=0,
    textColor=colors.HexColor('#2c3e50'),
    fontName='Helvetica'
))

# Estilo para información destacada
styles.add(ParagraphStyle(
    name='InfoDestacada', 
    fontSize=14, 
    leading=20, 
    spaceAfter=8, 
    alignment=0,
    textColor=colors.HexColor('#27ae60'),
    fontName='Helvetica-Bold'
))

# Estilo para precios
styles.add(ParagraphStyle(
    name='Precio', 
    fontSize=20, 
    leading=24, 
    spaceAfter=10, 
    alignment=1,
    textColor=colors.HexColor('#e74c3c'),
    fontName='Helvetica-Bold'
))

# Estilo para enlaces
styles.add(ParagraphStyle(
    name='Enlaces', 
    fontSize=12, 
    leading=16, 
    spaceAfter=8, 
    alignment=0,
    textColor=colors.HexColor('#3498db'),
    fontName='Helvetica'
))

# Estilos para la nav bar
styles.add(ParagraphStyle(name='NavBar', fontSize=14, leading=18, alignment=1, textColor=colors.white))
styles.add(ParagraphStyle(name='NavItem', fontSize=11, leading=14, alignment=1, textColor=colors.white))

story = []

# === NAV BAR MEJORADA ===
# Crear la barra de navegación con diseño moderno y gradiente
nav_data = [
    [
        Paragraph("■ <b>SANTA MARTA</b><br/><font size='9' color='#ecf0f1'>◆ Inmobiliaria Premium</font>", styles['NavBar']),
        Paragraph("●<br/><b>■ Inicio</b>", styles['NavItem']),
        Paragraph("▲<br/><b>■ Propiedades</b>", styles['NavItem']),
        Paragraph("◆<br/><b>⚙ Servicios</b>", styles['NavItem']),
        Paragraph("☎<br/><b>● Contacto</b>", styles['NavItem']),
        Paragraph("📱<br/><b>☎ +595 981 240 099</b>", styles['NavItem'])
    ]
]

nav_table = Table(nav_data, colWidths=[3.5*cm, 2.2*cm, 2.2*cm, 2.2*cm, 2.2*cm, 3.5*cm])
nav_table.setStyle(TableStyle([
    # Fondo con gradiente simulado
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#1a252f')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    
    # Estilo del logo/título
    ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (0, 0), 13),
    ('FONTSIZE', (1, 0), (-1, -1), 10),
    
    # Padding y espaciado mejorado
    ('PADDING', (0, 0), (-1, -1), 12),
    ('LEFTPADDING', (0, 0), (0, 0), 20),
    ('RIGHTPADDING', (0, 0), (0, 0), 20),
    
    # Bordes redondeados simulados
    ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#34495e')),
    ('LINEBEFORE', (1, 0), (1, 0), 1, colors.HexColor('#2c3e50')),
    ('LINEBEFORE', (2, 0), (2, 0), 1, colors.HexColor('#2c3e50')),
    ('LINEBEFORE', (3, 0), (3, 0), 1, colors.HexColor('#2c3e50')),
    ('LINEBEFORE', (4, 0), (4, 0), 1, colors.HexColor('#2c3e50')),
    ('LINEBEFORE', (5, 0), (5, 0), 1, colors.HexColor('#2c3e50')),
    
    # Efectos visuales
    ('BACKGROUND', (1, 0), (4, 0), colors.HexColor('#2c3e50')),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.HexColor('#1a252f'), colors.HexColor('#2c3e50')]),
]))

story.append(nav_table)
story.append(Spacer(1, 20))

# === CONTENIDO MEJORADO ===
# Título principal con diseño atractivo
titulo = "■ <font color='#2c3e50'>CAMPO EN VENTA</font><br/><font size='14' color='#7f8c8d'>Santa Marta, Boquerón - Paraguay</font>"

# Información del campo con iconos y colores
info_campo = """
<font color='#34495e'><b>● UBICACIÓN</b></font><br/>
<font color='#2c3e50'>■ Santa Marta, Boquerón, Paraguay</font><br/><br/>

<font color='#34495e'><b>◆ APTITUD</b></font><br/>
<font color='#2c3e50'>▲ Mixto (Agrícola + Ganadero)</font><br/><br/>

<font color='#34495e'><b>☂ PRECIPITACIÓN ANUAL</b></font><br/>
<font color='#2c3e50'>● 800 mm</font><br/><br/>

<font color='#34495e'><b>◆ DESCRIPCIÓN</b></font><br/>
<font color='#2c3e50'>■ Campo muy bien desarrollado con 715 Has ganaderas de pastura Gatton Panic y con 191 agrícolas. Además, la propiedad cuenta con 154 Has que aún se pueden desarrollar y un excedente de 103 Has, sumando así 1.850 Has en total.</font><br/><br/>

<font color='#34495e'><b>■ SUPERFICIE TOTAL</b></font><br/>
<font color='#2c3e50'>● 1.747 Has</font><br/><br/>

<font color='#34495e'><b>▲ DESGLOSE POR TIPO</b></font><br/>
<font color='#27ae60'>▲ Agrícolas: 191 Has</font><br/>
<font color='#27ae60'>● Ganaderas: 715 Has</font><br/>
<font color='#27ae60'>■ Monte: 437 Has</font><br/>
"""

# Información de puntos de interés
puntos_interes = """
<font color='#34495e'><b>■ PUNTOS DE INTERÉS</b></font><br/>
<font color='#2c3e50'>● Ruta de la leche: 76 km</font><br/>
<font color='#2c3e50'>■ Neuland: 150 km</font><br/>
<font color='#2c3e50'>■ Filadelfia: 190 km</font><br/>
<font color='#2c3e50'>■ Mariscal Estigarribia: 250 km</font><br/>
<font color='#2c3e50'>◆ Asunción: 500 km</font><br/>
"""

# Precio destacado (actualizar con precio real)
precio_destacado = """
<font color='#e74c3c' size='18'><b>● CONSULTAR PRECIO</b></font><br/>
<font color='#c0392b' size='22'><b>☎ Contactar para más información</b></font><br/>
<font color='#7f8c8d' size='10'>■ Campo de 1.747 Has - Oportunidad única</font>
"""

whatsapp_link = "https://wa.me/595981240099?text=Hola%2C%20vi%20el%20campo%20en%20venta%20en%20Santa%20Marta%2C%20Boquerón"
maps_link = "https://maps.google.com/?q=-23.2984734,-60.5146408"
drive_link = "https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link"

# === AÑADIR AL PDF ===
# Título principal
story.append(Paragraph(titulo, styles['TituloPrincipal']))
story.append(Spacer(1, 15))

# Crear tabla para información del campo
info_data = [
    [Paragraph(info_campo, styles['Descripcion']), Paragraph(precio_destacado, styles['Precio'])]
]

info_table = Table(info_data, colWidths=[10*cm, 6*cm])
info_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#f8f9fa')),
    ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#fff5f5')),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 15),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#e9ecef')),
    ('LINEBEFORE', (1, 0), (1, 0), 2, colors.HexColor('#e74c3c')),
]))

story.append(info_table)
story.append(Spacer(1, 20))

# Sección de puntos de interés
puntos_titulo = "🗺️ <font color='#2c3e50'><b>PUNTOS DE INTERÉS</b></font>"
story.append(Paragraph(puntos_titulo, styles['Subtitulo']))
story.append(Spacer(1, 10))

# Crear tabla para puntos de interés
puntos_data = [
    [Paragraph(puntos_interes, styles['Descripcion'])]
]

puntos_table = Table(puntos_data, colWidths=[16*cm])
puntos_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#e8f5e8')),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 15),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#27ae60')),
]))

story.append(puntos_table)
story.append(Spacer(1, 20))

# Sección de contacto mejorada
contacto_titulo = "☎ <font color='#2c3e50'><b>CONTACTO DIRECTO</b></font>"
story.append(Paragraph(contacto_titulo, styles['Subtitulo']))
story.append(Spacer(1, 10))

# Enlaces con diseño mejorado y enlaces clicables
links_data = [
    [
        Paragraph(f"●<br/><b><a href='{whatsapp_link}' color='white'>WhatsApp</a></b><br/><font size='9'>☎ Contacto inmediato</font>", 
                 ParagraphStyle(name='LinkBox', fontSize=11, leading=14, alignment=1, textColor=colors.white)),
        Paragraph(f"■<br/><b><a href='{maps_link}' color='white'>Google Maps</a></b><br/><font size='9'>● Ver ubicación</font>", 
                 ParagraphStyle(name='LinkBox', fontSize=11, leading=14, alignment=1, textColor=colors.white)),
        Paragraph(f"◆<br/><b><a href='{drive_link}' color='white'>Fotos</a></b><br/><font size='9'>■ Galería completa</font>", 
                 ParagraphStyle(name='LinkBox', fontSize=11, leading=14, alignment=1, textColor=colors.white))
    ]
]

links_table = Table(links_data, colWidths=[5.3*cm, 5.3*cm, 5.3*cm])
links_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#25d366')),  # Verde WhatsApp
    ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#4285f4')),  # Azul Google
    ('BACKGROUND', (2, 0), (2, 0), colors.HexColor('#ff6b6b')),  # Rojo Drive
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 15),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#1e1e1e')),
    ('LINEBEFORE', (1, 0), (1, 0), 1, colors.white),
    ('LINEBEFORE', (2, 0), (2, 0), 1, colors.white),
]))

story.append(links_table)
story.append(Spacer(1, 15))

# Enlaces de texto adicionales para asegurar funcionalidad
enlaces_texto = f"""
<font color='#2c3e50'><b>● ENLACES DIRECTOS:</b></font><br/>
<font color='#3498db'>● <a href="{whatsapp_link}">☎ Contactar por WhatsApp (+595 981 240 099)</a></font><br/>
<font color='#3498db'>■ <a href="{maps_link}">● Ver ubicación en Google Maps</a></font><br/>
<font color='#3498db'>◆ <a href="{drive_link}">■ Ver fotos del campo (Google Drive)</a></font>
"""
story.append(Paragraph(enlaces_texto, styles['Enlaces']))
story.append(Spacer(1, 20))

# Sección de galería tipo carrusel
imagen_titulo = "■ <font color='#2c3e50'><b>GALERÍA FOTOGRÁFICA DEL CAMPO</b></font>"
story.append(Paragraph(imagen_titulo, styles['Subtitulo']))
story.append(Spacer(1, 10))

# Agregar elemento decorativo
story.append(crear_background_decorativo())
story.append(Spacer(1, 10))

# Crear galería tipo carrusel
galeria = crear_galeria_carrusel()

if galeria['imagen_principal'] or galeria['miniaturas']:
    # Imagen principal
    if galeria['imagen_principal']:
        story.append(galeria['imagen_principal'])
        story.append(Spacer(1, 15))
    
    # Miniaturas
    if galeria['miniaturas']:
        # Crear tabla para miniaturas (máximo 4 por fila) - TAMAÑOS AJUSTADOS
        miniaturas_data = []
        for i in range(0, len(galeria['miniaturas']), 4):
            fila = galeria['miniaturas'][i:i+4]
            # Rellenar con celdas vacías si no hay 4 miniaturas
            while len(fila) < 4:
                fila.append(Paragraph("", styles['Descripcion']))
            miniaturas_data.append(fila)
        
        # Ajustar ancho de columnas para miniaturas más grandes (5cm cada una)
        miniaturas_table = Table(miniaturas_data, colWidths=[5*cm, 5*cm, 5*cm, 5*cm])
        miniaturas_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 3),
        ]))
        
        story.append(miniaturas_table)
        story.append(Spacer(1, 15))
    
    # Información sobre Google Drive
    drive_info = """
    <font color='#2c3e50'><b>◆ GALERÍA COMPLETA EN GOOGLE DRIVE</b></font><br/>
    <font color='#7f8c8d'>Accede a todas las fotos del campo en alta resolución</font><br/>
    <font color='#3498db'><a href='https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link'>● Ver galería completa</a></font>
    """
    story.append(Paragraph(drive_info, styles['Enlaces']))
    
else:
    # Placeholder mejorado si no hay imágenes
    placeholder_data = [
        [Paragraph("📷<br/><font size='14' color='#7f8c8d'><b>Galería fotográfica</b></font><br/><font size='12' color='#95a5a6'>Agregue imágenes del campo:</font><br/><font size='10' color='#bdc3c7'>• campo1.jpg - Imagen principal (12x8 cm)</font><br/><font size='10' color='#bdc3c7'>• campo2.jpg - Pasturas (miniatura)</font><br/><font size='10' color='#bdc3c7'>• campo3.jpg - Agrícola (miniatura)</font><br/><font size='10' color='#bdc3c7'>• campo4.jpg - Monte (miniatura)</font><br/><font size='10' color='#bdc3c7'>• campo5.jpg - Panorámica (miniatura)</font><br/><br/><font size='11' color='#3498db'>📂 <a href='https://drive.google.com/drive/folders/XXXXXXX'>Ver galería en Google Drive</a></font>", 
                 ParagraphStyle(name='Placeholder', fontSize=12, leading=16, alignment=1, textColor=colors.HexColor('#7f8c8d')))]
    ]
    placeholder_table = Table(placeholder_data, colWidths=[16*cm])
    placeholder_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#f8f9fa')),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('PADDING', (0, 0), (0, 0), 20),
        ('BOX', (0, 0), (0, 0), 2, colors.HexColor('#3498db')),
        ('LINEBELOW', (0, 0), (0, 0), 1, colors.HexColor('#e74c3c')),
    ]))
    story.append(placeholder_table)

story.append(Spacer(1, 25))

# Footer profesional
footer_data = [
    [
        Paragraph("■ <b>SANTA MARTA</b><br/><font size='9'>◆ Inmobiliaria Premium</font>", 
                 ParagraphStyle(name='Footer', fontSize=11, leading=14, alignment=0, textColor=colors.white)),
        Paragraph("☎ +595 981 240 099<br/><font size='8'>● WhatsApp disponible 24/7</font>", 
                 ParagraphStyle(name='Footer', fontSize=10, leading=12, alignment=2, textColor=colors.white)),
    ]
]

footer_table = Table(footer_data, colWidths=[8*cm, 8*cm])
footer_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
    ('ALIGN', (0, 0), (0, 0), 'LEFT'),
    ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 12),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#34495e')),
]))

story.append(footer_table)

doc.build(story)

print(f"✅ PDF generado correctamente: {pdf_name}")
print("🎨 Diseño mejorado con iconos, colores y elementos visuales profesionales")
