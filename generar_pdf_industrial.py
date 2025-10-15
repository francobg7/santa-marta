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

# === CONFIGURACIÓN ===
pdf_name = "campo_santa_marta_industrial.pdf"
doc = SimpleDocTemplate(pdf_name, pagesize=A4, 
                       rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)

# === PALETA DE COLORES INDUSTRIAL ===
COLOR_PRIMARY = colors.HexColor('#2c3e50')      # Azul oscuro industrial
COLOR_SECONDARY = colors.HexColor('#e74c3c')    # Rojo industrial
COLOR_ACCENT = colors.HexColor('#f39c12')       # Naranja industrial
COLOR_TEXT_LIGHT = colors.HexColor('#ecf0f1')   # Blanco suave
COLOR_TEXT_DARK = colors.HexColor('#2c3e50')    # Azul oscuro
COLOR_BG_DARK = colors.HexColor('#1a1a1a')      # Negro industrial
COLOR_METAL = colors.HexColor('#7f8c8d')        # Gris metal
COLOR_STEEL = colors.HexColor('#95a5a6')        # Gris acero

# === FUNCIONES DE DISEÑO INDUSTRIAL ===
def crear_fondo_industrial():
    """Crear fondo industrial usando tabla en lugar de Drawing"""
    fondo_data = [[Paragraph("", ParagraphStyle(name='Fondo', fontSize=1))]]
    fondo_table = Table(fondo_data, colWidths=[21*cm], rowHeights=[29.7*cm])
    fondo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_DARK),
        ('BOX', (0, 0), (-1, -1), 0, COLOR_BG_DARK),
    ]))
    return fondo_table

def crear_barra_industrial(ancho, alto, color):
    """Crear barra industrial decorativa"""
    drawing = Drawing(ancho, alto)
    drawing.add(Rect(0, 0, ancho, alto, fillColor=color, strokeColor=None))
    # Textura industrial
    for i in range(0, int(ancho), 3):
        drawing.add(Line(i, 0, i, alto, strokeColor=COLOR_BG_DARK, strokeWidth=0.1))
    return drawing

# === ESTILOS INDUSTRIALES ===
styles = getSampleStyleSheet()

# Estilos tipográficos industriales
styles.add(ParagraphStyle(name='TituloIndustrial', fontSize=52, leading=56, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=20, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='SubtituloIndustrial', fontSize=32, leading=36, alignment=1, 
                         textColor=COLOR_ACCENT, spaceAfter=15, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='InfoIndustrial', fontSize=18, leading=22, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=10, fontName='Helvetica'))
styles.add(ParagraphStyle(name='PrecioIndustrial', fontSize=36, leading=40, alignment=1, 
                         textColor=COLOR_SECONDARY, spaceAfter=15, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='ContactoIndustrial', fontSize=20, leading=24, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=8, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='EnlacesIndustrial', fontSize=16, leading=20, alignment=1, 
                         textColor=COLOR_ACCENT, spaceAfter=8, fontName='Helvetica'))
styles.add(ParagraphStyle(name='DescripcionIndustrial', fontSize=14, leading=18, alignment=0, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=10, fontName='Helvetica'))
styles.add(ParagraphStyle(name='TituloSeccion', fontSize=24, leading=28, alignment=0, 
                         textColor=COLOR_ACCENT, spaceAfter=10, fontName='Helvetica-Bold'))

# === FUNCIONES DE IMÁGENES ===
def crear_imagen_principal(ruta_imagen, ancho, alto):
    """Crear imagen principal grande sin marco"""
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

# === HEADER INDUSTRIAL ===
header_data = [
    [Paragraph("INDUSTRIAL PROPERTY", styles['TituloIndustrial'])],
    [Paragraph("SANTA MARTA • BOQUERÓN • PARAGUAY", styles['SubtituloIndustrial'])],
    [Spacer(1, 30)],
    [Paragraph("1,747 HECTÁREAS • OPERACIÓN MIXTA", styles['InfoIndustrial'])],
    [Paragraph("AGRÍCOLA + GANADERA + DESARROLLO", styles['InfoIndustrial'])],
]

header_table = Table(header_data, colWidths=[21*cm])
header_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 25),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_BG_DARK),
]))

story.append(header_table)
story.append(Spacer(1, 40))

# === ESPECIFICACIONES TÉCNICAS ===
especificaciones_data = [
    [
        Paragraph("ESPECIFICACIONES TÉCNICAS", styles['TituloSeccion']),
        Paragraph("INVERSIÓN", styles['TituloSeccion'])
    ],
    [
        Paragraph("• Superficie Total: 1,747 Has<br/>• Agrícolas: 191 Has<br/>• Ganaderas: 715 Has<br/>• Monte: 437 Has<br/>• Desarrollables: 154 Has<br/>• Excedente: 103 Has<br/>• Precipitación: 800 mm anuales", styles['DescripcionIndustrial']),
        Paragraph("CONSULTAR PRECIO<br/><br/>Contactar para información detallada de inversión y financiamiento", styles['PrecioIndustrial'])
    ]
]

especificaciones_table = Table(especificaciones_data, colWidths=[10.5*cm, 10.5*cm])
especificaciones_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_PRIMARY),
    ('BACKGROUND', (1, 0), (1, 0), COLOR_SECONDARY),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('BACKGROUND', (1, 1), (1, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 20),
    ('BOX', (0, 0), (-1, -1), 3, COLOR_METAL),
    ('LINEAFTER', (0, 0), (0, 0), 3, COLOR_METAL),
]))

story.append(especificaciones_table)
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
                fila1.append(Paragraph("", styles['ContactoIndustrial']))
            miniaturas_data.append(fila1)
        
        # Segunda fila
        if len(galeria['miniaturas']) >= 3:
            fila2 = galeria['miniaturas'][2:4]
            while len(fila2) < 2:
                fila2.append(Paragraph("", styles['ContactoIndustrial']))
            miniaturas_data.append(fila2)
        
        miniaturas_table = Table(miniaturas_data, colWidths=[10.5*cm, 10.5*cm])
        miniaturas_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('SPACEAFTER', (0, 0), (-1, -1), 15),
        ]))
        
        story.append(miniaturas_table)
        story.append(Spacer(1, 30))

# === CONTACTO INDUSTRIAL ===
whatsapp_link = "https://wa.me/595981240099?text=Hola%20vi%20el%20campo%20en%20venta%20en%20Santa%20Marta%2C%20Boquer%C3%B3n"
maps_link = "https://maps.google.com/?q=-23.2984734,-60.5146408"
drive_link = "https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link"

contacto_industrial_data = [
    [
        Paragraph("CONTACTO DIRECTO", styles['TituloSeccion']),
        Paragraph("MAURICIO GRANADA", styles['ContactoIndustrial']),
        Paragraph("+595 981 240 099", styles['ContactoIndustrial'])
    ],
    [
        Paragraph(f"<a href='{whatsapp_link}' color='#f39c12'><b>WHATSAPP</b><br/><u>+595 981 240 099</u></a>", 
                 ParagraphStyle(name='EnlaceIndustrial', fontSize=18, leading=22, alignment=1, textColor=COLOR_ACCENT)),
        Paragraph(f"<a href='{maps_link}' color='#e74c3c'><b>UBICACIÓN</b><br/><u>Ver en Maps</u></a>", 
                 ParagraphStyle(name='EnlaceIndustrial', fontSize=18, leading=22, alignment=1, textColor=COLOR_SECONDARY)),
        Paragraph(f"<a href='{drive_link}' color='#2c3e50'><b>GALERÍA</b><br/><u>Ver Fotos</u></a>", 
                 ParagraphStyle(name='EnlaceIndustrial', fontSize=18, leading=22, alignment=1, textColor=COLOR_PRIMARY))
    ]
]

contacto_industrial_table = Table(contacto_industrial_data, colWidths=[7*cm, 7*cm, 7*cm])
contacto_industrial_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_ACCENT),
    ('BACKGROUND', (1, 0), (1, 0), COLOR_SECONDARY),
    ('BACKGROUND', (2, 0), (2, 0), COLOR_PRIMARY),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('BACKGROUND', (1, 1), (1, 1), COLOR_BG_DARK),
    ('BACKGROUND', (2, 1), (2, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 20),
    ('BOX', (0, 0), (-1, -1), 3, COLOR_METAL),
]))

story.append(contacto_industrial_table)
story.append(Spacer(1, 30))

# === INFORMACIÓN DETALLADA ===
info_detallada_data = [
    [
        Paragraph("DESCRIPCIÓN", styles['TituloSeccion']),
        Paragraph("INFRAESTRUCTURA", styles['TituloSeccion'])
    ],
    [
        Paragraph("Campo muy bien desarrollado con 715 Has ganaderas de pastura Gatton Panic y con 191 agrícolas. Además, la propiedad cuenta con 154 Has que aún se pueden desarrollar y un excedente de 103 Has, sumando así 1.850 Has en total.", styles['DescripcionIndustrial']),
        Paragraph("• Corriente eléctrica con generador<br/>• Acceso por 4 caminos, 76 km del asfalto<br/>• Potreros ganaderos subdivididos en 4 potreros<br/>• 7 tanques australianos<br/>• 1 manga<br/>• 1 casa principal<br/>• 1 casa de peón", styles['DescripcionIndustrial'])
    ]
]

info_detallada_table = Table(info_detallada_data, colWidths=[10.5*cm, 10.5*cm])
info_detallada_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_PRIMARY),
    ('BACKGROUND', (1, 0), (1, 0), COLOR_SECONDARY),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('BACKGROUND', (1, 1), (1, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 20),
    ('BOX', (0, 0), (-1, -1), 3, COLOR_METAL),
    ('LINEAFTER', (0, 0), (0, 0), 3, COLOR_METAL),
]))

story.append(info_detallada_table)
story.append(Spacer(1, 30))

# === PUNTOS DE INTERÉS ===
puntos_interes_data = [
    [Paragraph("PUNTOS DE INTERÉS", styles['TituloSeccion'])],
    [Paragraph("• Ruta de la leche: 76km<br/>• Neuland: 150km<br/>• Filadelfia: 190km<br/>• Mariscal Estigarribia: 250km<br/>• Asunción: 500km", styles['DescripcionIndustrial'])]
]

puntos_interes_table = Table(puntos_interes_data, colWidths=[21*cm])
puntos_interes_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), COLOR_ACCENT),
    ('BACKGROUND', (0, 1), (0, 1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 20),
    ('BOX', (0, 0), (-1, -1), 3, COLOR_METAL),
]))

story.append(puntos_interes_table)

# === GENERAR PDF ===
try:
    doc.build(story)
    print("✅ PDF INDUSTRIAL generado correctamente:", pdf_name)
    print("🎨 Diseño industrial moderno aplicado")
    print("🔥 ¡Diseño vanguardista y profesional!")
except Exception as e:
    print("❌ Error al generar PDF:", str(e))
