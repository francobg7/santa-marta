from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle, PageBreak, KeepTogether, Frame, PageTemplate, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line, Polygon
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Group
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus.flowables import HRFlowable
import os
from urllib.parse import quote

# === CONFIGURACIÓN ===
pdf_name = "campo_santa_marta_moderno.pdf"
doc = SimpleDocTemplate(pdf_name, pagesize=A4, 
                       rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)

# === PALETA DE COLORES MONOCROMÁTICA (NEGRO/BLANCO) ===
COLOR_PRIMARY = colors.black
COLOR_SECONDARY = colors.black
COLOR_ACCENT = colors.black
COLOR_SUCCESS = colors.black
COLOR_WARNING = colors.black
COLOR_TEXT_LIGHT = colors.white
COLOR_TEXT_DARK = colors.black
COLOR_BG_LIGHT = colors.black
COLOR_BG_DARK = colors.black
COLOR_METAL = colors.white
COLOR_GRADIENT = colors.black
# Acento para el hero (contraste)
COLOR_HERO = colors.HexColor('#f39c12')

# === FUNCIONES DE DISEÑO MODERNO ===
def crear_icono_moderno(tipo, tamaño, color):
    """Crear iconos modernos con bordes redondeados"""
    drawing = Drawing(tamaño, tamaño)
    radio = tamaño/2 - 2
    
    if tipo == "whatsapp":
        # Círculo con W
        drawing.add(Circle(tamaño/2, tamaño/2, radio, fillColor=color, strokeColor=COLOR_TEXT_LIGHT, strokeWidth=2))
        drawing.add(String(tamaño/2, tamaño/2-2, "W", textAnchor="middle", fontSize=tamaño/3, fillColor=COLOR_TEXT_LIGHT))
    elif tipo == "maps":
        # Cuadrado con M
        drawing.add(Rect(2, 2, tamaño-4, tamaño-4, fillColor=color, strokeColor=COLOR_TEXT_LIGHT, strokeWidth=2))
        drawing.add(String(tamaño/2, tamaño/2-2, "M", textAnchor="middle", fontSize=tamaño/3, fillColor=COLOR_TEXT_LIGHT))
    elif tipo == "drive":
        # Triángulo con D
        points = [(tamaño/2, tamaño-2), (2, 2), (tamaño-2, 2)]
        drawing.add(Polygon(points, fillColor=color, strokeColor=COLOR_TEXT_LIGHT, strokeWidth=2))
        drawing.add(String(tamaño/2, tamaño/2-2, "D", textAnchor="middle", fontSize=tamaño/3, fillColor=COLOR_TEXT_LIGHT))
    
    return drawing

# === ESTILOS MODERNOS ===
styles = getSampleStyleSheet()

# Estilos tipográficos modernos
styles.add(ParagraphStyle(name='TituloModerno', fontSize=48, leading=52, alignment=1, 
                         textColor=COLOR_HERO, spaceAfter=20, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='SubtituloModerno', fontSize=28, leading=32, alignment=1, 
                         textColor=COLOR_HERO, spaceAfter=15, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='InfoModerno', fontSize=18, leading=22, alignment=1, 
                         textColor=COLOR_HERO, spaceAfter=10, fontName='Helvetica'))
styles.add(ParagraphStyle(name='PrecioModerno', fontSize=32, leading=36, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=15, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='ContactoModerno', fontSize=20, leading=24, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=8, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='EnlacesModerno', fontSize=16, leading=20, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=8, fontName='Helvetica'))
styles.add(ParagraphStyle(name='DescripcionModerno', fontSize=14, leading=18, alignment=0, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=10, fontName='Helvetica'))
styles.add(ParagraphStyle(name='TituloSeccion', fontSize=22, leading=26, alignment=0, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=10, fontName='Helvetica-Bold'))

# === FUNCIONES DE IMÁGENES ===
def crear_imagen_principal(ruta_imagen, ancho, alto):
    """Crear imagen principal con bordes redondeados"""
    try:
        if os.path.exists(ruta_imagen):
            return Image(ruta_imagen, width=ancho, height=alto)
        else:
            return None
    except:
        return None

def crear_miniatura(ruta_imagen, ancho, alto, titulo):
    """Crear miniatura con bordes redondeados"""
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
    
    # Buscar imagen principal
    imagenes_principales = ['campo1.jpg', 'terreno.jpg']
    for img_principal in imagenes_principales:
        if os.path.exists(img_principal):
            galeria['imagen_principal'] = crear_imagen_principal(img_principal, 21*cm, 12*cm)
            break
    
    # Buscar miniaturas
    miniaturas_info = [
        ('campo2.jpg', 'Pasturas'),
        ('campo3.jpg', 'Agrícola'),
        ('campo4.jpg', 'Monte'),
        ('campo5.jpg', 'Panorámica')
    ]
    
    for ruta, titulo in miniaturas_info:
        if os.path.exists(ruta):
            miniatura = crear_miniatura(ruta, 10.5*cm, 6.5*cm, titulo)
            if miniatura:
                galeria['miniaturas'].append(miniatura)
    
    return galeria

# === CONTENIDO PRINCIPAL ===
story = []

# === HEADER MODERNO CON GRADIENTE ===
header_data = [
    [Paragraph("🏡 CAMPO EN VENTA", styles['TituloModerno'])],
    [Paragraph("Santa Marta • Boquerón • Paraguay", styles['SubtituloModerno'])],
    [Spacer(1, 30)],
    [Paragraph("1,747 HECTÁREAS • OPERACIÓN MIXTA", styles['InfoModerno'])],
    [Paragraph("Agrícola + Ganadera + Desarrollo", styles['InfoModerno'])],
]

header_table = Table(header_data, colWidths=[21*cm])
header_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 30),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_GRADIENT),
    ('ROUNDEDCORNERS', (0, 0), (-1, -1), 20),
]))

story.append(header_table)
story.append(Spacer(1, 40))

# === TARJETAS DE INFORMACIÓN ===
info_cards_data = [
    [
        Paragraph("📊 ESPECIFICACIONES", styles['TituloSeccion']),
        Paragraph("💰 INVERSIÓN", styles['TituloSeccion'])
    ],
    [
        Paragraph("• Superficie Total: 1,747 Has<br/>• Agrícolas: 191 Has<br/>• Ganaderas: 715 Has<br/>• Monte: 437 Has<br/>• Desarrollables: 154 Has<br/>• Excedente: 103 Has<br/>• Precipitación: 800 mm anuales", styles['DescripcionModerno']),
        Paragraph("CONSULTAR PRECIO<br/><br/>Contactar para información detallada de inversión y financiamiento", styles['PrecioModerno'])
    ]
]

info_cards_table = Table(info_cards_data, colWidths=[10.5*cm, 10.5*cm])
info_cards_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_BG_DARK),
    ('BACKGROUND', (1, 0), (1, 0), COLOR_BG_DARK),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('BACKGROUND', (1, 1), (1, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 25),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_METAL),
    ('ROUNDEDCORNERS', (0, 0), (-1, -1), 15),
    ('LINEAFTER', (0, 0), (0, 0), 3, COLOR_METAL),
]))

story.append(info_cards_table)
story.append(Spacer(1, 40))

# === GALERÍA DE IMÁGENES ===
galeria = crear_galeria_carrusel()

if galeria['imagen_principal']:
    story.append(galeria['imagen_principal'])
    story.append(Spacer(1, 30))
    
    # Miniaturas en formato 2x2
    if galeria['miniaturas']:
        miniaturas_data = []
        
        # Primera fila
        if len(galeria['miniaturas']) >= 2:
            fila1 = galeria['miniaturas'][0:2]
            while len(fila1) < 2:
                fila1.append(Paragraph("", styles['ContactoModerno']))
            miniaturas_data.append(fila1)
        
        # Segunda fila
        if len(galeria['miniaturas']) >= 3:
            fila2 = galeria['miniaturas'][2:4]
            while len(fila2) < 2:
                fila2.append(Paragraph("", styles['ContactoModerno']))
            miniaturas_data.append(fila2)
        
        miniaturas_table = Table(miniaturas_data, colWidths=[10.5*cm, 10.5*cm])
        miniaturas_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 10),
            ('SPACEAFTER', (0, 0), (-1, -1), 20),
            ('ROUNDEDCORNERS', (0, 0), (-1, -1), 10),
        ]))
        
        story.append(miniaturas_table)
        story.append(Spacer(1, 30))

# === TARJETAS DE CONTACTO ===
# Mensaje predeterminado de WhatsApp (codificado)
mensaje = "Hola, vi el campo en venta en Santa Marta, Boquerón"
whatsapp_link = f"https://wa.me/595981240099?text={quote(mensaje)}"
maps_link = "https://maps.google.com/?q=-23.2984734,-60.5146408"
drive_link = "https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link"

contacto_cards_data = [
    [
        Paragraph("📞 CONTACTO DIRECTO", styles['TituloSeccion']),
        Paragraph("MAURICIO GRANADA", styles['ContactoModerno']),
        Paragraph("+595 981 240 099", styles['ContactoModerno'])
    ],
    [
        Paragraph(f"<a href='{whatsapp_link}' color='white'><b>💬 WHATSAPP</b><br/><u>+595 981 240 099</u></a>", 
                 ParagraphStyle(name='EnlacesModerno', fontSize=18, leading=22, alignment=1, textColor=COLOR_TEXT_LIGHT)),
        Paragraph(f"<a href='{maps_link}' color='white'><b>📍 UBICACIÓN</b><br/><u>Ver en Maps</u></a>", 
                 ParagraphStyle(name='EnlacesModerno', fontSize=18, leading=22, alignment=1, textColor=COLOR_TEXT_LIGHT)),
        Paragraph(f"<a href='{drive_link}' color='white'><b>📁 GALERÍA</b><br/><u>Ver Fotos</u></a>", 
                 ParagraphStyle(name='EnlacesModerno', fontSize=18, leading=22, alignment=1, textColor=COLOR_TEXT_LIGHT))
    ]
]

contacto_cards_table = Table(contacto_cards_data, colWidths=[7*cm, 7*cm, 7*cm])
contacto_cards_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_BG_DARK),
    ('BACKGROUND', (1, 0), (1, 0), COLOR_BG_DARK),
    ('BACKGROUND', (2, 0), (2, 0), COLOR_BG_DARK),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('BACKGROUND', (1, 1), (1, 1), COLOR_BG_DARK),
    ('BACKGROUND', (2, 1), (2, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 25),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_METAL),
    ('ROUNDEDCORNERS', (0, 0), (-1, -1), 20),
]))

story.append(contacto_cards_table)
story.append(Spacer(1, 30))

# === TARJETAS DE INFORMACIÓN DETALLADA ===
info_detallada_data = [
    [
        Paragraph("📝 DESCRIPCIÓN", styles['TituloSeccion']),
        Paragraph("🏗️ INFRAESTRUCTURA", styles['TituloSeccion'])
    ],
    [
        Paragraph("Campo muy bien desarrollado con 715 Has ganaderas de pastura Gatton Panic y con 191 agrícolas. Además, la propiedad cuenta con 154 Has que aún se pueden desarrollar y un excedente de 103 Has, sumando así 1.850 Has en total.", styles['DescripcionModerno']),
        Paragraph("• Corriente eléctrica con generador<br/>• Acceso por 4 caminos, 76 km del asfalto<br/>• Potreros ganaderos subdivididos en 4 potreros<br/>• 7 tanques australianos<br/>• 1 manga<br/>• 1 casa principal<br/>• 1 casa de peón", styles['DescripcionModerno'])
    ]
]

info_detallada_table = Table(info_detallada_data, colWidths=[10.5*cm, 10.5*cm])
info_detallada_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_BG_DARK),
    ('BACKGROUND', (1, 0), (1, 0), COLOR_BG_DARK),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('BACKGROUND', (1, 1), (1, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 25),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_METAL),
    ('ROUNDEDCORNERS', (0, 0), (-1, -1), 15),
    ('LINEAFTER', (0, 0), (0, 0), 3, COLOR_METAL),
]))

story.append(info_detallada_table)
story.append(Spacer(1, 30))

# === TARJETA DE PUNTOS DE INTERÉS ===
puntos_interes_data = [
    [Paragraph("🗺️ PUNTOS DE INTERÉS", styles['TituloSeccion'])],
    [Paragraph("• Ruta de la leche: 76km<br/>• Neuland: 150km<br/>• Filadelfia: 190km<br/>• Mariscal Estigarribia: 250km<br/>• Asunción: 500km", styles['DescripcionModerno'])]
]

puntos_interes_table = Table(puntos_interes_data, colWidths=[21*cm])
puntos_interes_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_BG_DARK),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 25),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_METAL),
    ('ROUNDEDCORNERS', (0, 0), (-1, -1), 20),
]))

story.append(puntos_interes_table)

# === GENERAR PDF ===
try:
    doc.build(story)
    print("✅ PDF MODERNO generado correctamente:", pdf_name)
    print("🎨 Diseño moderno con bordes redondeados aplicado")
    print("✨ ¡Diseño elegante y contemporáneo!")
except Exception as e:
    print("❌ Error al generar PDF:", str(e))
