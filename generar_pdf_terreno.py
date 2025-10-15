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
pdf_name = "campo_santa_marta.pdf"
doc = SimpleDocTemplate(pdf_name, pagesize=A4, 
                       rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)

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

def crear_fondo_industrial():
    """Crear fondo industrial con gradiente y elementos geométricos"""
    drawing = Drawing(20.4*cm, 29.0*cm)
    
    # Fondo principal
    drawing.add(Rect(0, 0, 20.4*cm, 29.0*cm, fillColor=COLOR_BG_DARK, strokeColor=None))
    
    # Elementos geométricos industriales
    # Líneas diagonales
    for i in range(0, 29, 3):
        drawing.add(Line(0, i*cm, 20.4*cm, (i+1)*cm, strokeColor=COLOR_METAL, strokeWidth=0.5, strokeDashArray=[5, 3]))
    
    # Rectángulos decorativos
    drawing.add(Rect(1*cm, 24.5*cm, 3*cm, 0.5*cm, fillColor=COLOR_ACCENT, strokeColor=None))
    drawing.add(Rect(16.5*cm, 2*cm, 3*cm, 0.5*cm, fillColor=COLOR_SECONDARY, strokeColor=None))
    
    # Círculos industriales
    drawing.add(Circle(2*cm, 5*cm, 0.3*cm, fillColor=COLOR_METAL, strokeColor=None))
    drawing.add(Circle(18.7*cm, 23.5*cm, 0.3*cm, fillColor=COLOR_METAL, strokeColor=None))
    
    return drawing

def crear_barra_industrial(ancho, alto, color):
    """Crear barra industrial decorativa"""
    drawing = Drawing(ancho, alto)
    drawing.add(Rect(0, 0, ancho, alto, fillColor=color, strokeColor=None))
    # Agregar textura
    for i in range(0, int(ancho), 2):
        drawing.add(Line(i, 0, i, alto, strokeColor=COLOR_BG_DARK, strokeWidth=0.2))
    return drawing

def crear_icono_industrial(tipo, tamaño):
    """Crear iconos industriales simples"""
    drawing = Drawing(tamaño, tamaño)
    
    if tipo == "whatsapp":
        # Círculo con W
        drawing.add(Circle(tamaño/2, tamaño/2, tamaño/2-2, fillColor=COLOR_ACCENT, strokeColor=COLOR_TEXT_LIGHT, strokeWidth=2))
        drawing.add(String(tamaño/2, tamaño/2-2, "W", textAnchor="middle", fontSize=tamaño/3, fillColor=COLOR_TEXT_LIGHT))
    elif tipo == "maps":
        # Cuadrado con M
        drawing.add(Rect(2, 2, tamaño-4, tamaño-4, fillColor=COLOR_SECONDARY, strokeColor=COLOR_TEXT_LIGHT, strokeWidth=2))
        drawing.add(String(tamaño/2, tamaño/2-2, "M", textAnchor="middle", fontSize=tamaño/3, fillColor=COLOR_TEXT_LIGHT))
    elif tipo == "drive":
        # Triángulo con D
        points = [(tamaño/2, tamaño-2), (2, 2), (tamaño-2, 2)]
        drawing.add(Polygon(points, fillColor=COLOR_PRIMARY, strokeColor=COLOR_TEXT_LIGHT, strokeWidth=2))
        drawing.add(String(tamaño/2, tamaño/2-2, "D", textAnchor="middle", fontSize=tamaño/3, fillColor=COLOR_TEXT_LIGHT))
    
    return drawing

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
            galeria['imagen_principal'] = crear_imagen_principal(img_principal, 21*cm, 12*cm)
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
            # Miniaturas mucho más grandes (10.5x6.5 cm cada una) para ocupar todo el ancho
            miniatura = crear_miniatura(ruta, 10.5*cm, 6.5*cm, titulo)
            if miniatura:
                galeria['miniaturas'].append(miniatura)
    
    return galeria

# === ESTILOS INDUSTRIALES MODERNOS ===
styles = getSampleStyleSheet()

# Paleta de colores industrial
COLOR_PRIMARY = colors.HexColor('#2c3e50')      # Azul oscuro industrial
COLOR_SECONDARY = colors.HexColor('#e74c3c')    # Rojo industrial
COLOR_ACCENT = colors.HexColor('#f39c12')       # Naranja industrial
COLOR_TEXT_LIGHT = colors.HexColor('#ecf0f1')   # Blanco suave
COLOR_TEXT_DARK = colors.HexColor('#2c3e50')    # Azul oscuro
COLOR_BG_DARK = colors.HexColor('#1a1a1a')      # Negro industrial
COLOR_METAL = colors.HexColor('#7f8c8d')        # Gris metal
COLOR_STEEL = colors.HexColor('#95a5a6')        # Gris acero

# Estilos tipográficos industriales
styles.add(ParagraphStyle(name='TituloIndustrial', fontSize=48, leading=52, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=15, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='SubtituloIndustrial', fontSize=28, leading=32, alignment=1, 
                         textColor=COLOR_ACCENT, spaceAfter=10, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='InfoIndustrial', fontSize=16, leading=20, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=8, fontName='Helvetica'))
styles.add(ParagraphStyle(name='PrecioIndustrial', fontSize=32, leading=36, alignment=1, 
                         textColor=COLOR_SECONDARY, spaceAfter=12, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='ContactoIndustrial', fontSize=18, leading=22, alignment=1, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=6, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='EnlacesIndustrial', fontSize=14, leading=18, alignment=1, 
                         textColor=COLOR_ACCENT, spaceAfter=6, fontName='Helvetica'))
styles.add(ParagraphStyle(name='DescripcionIndustrial', fontSize=12, leading=16, alignment=0, 
                         textColor=COLOR_TEXT_LIGHT, spaceAfter=8, fontName='Helvetica'))
styles.add(ParagraphStyle(name='TituloSeccion', fontSize=20, leading=24, alignment=0, 
                         textColor=COLOR_ACCENT, spaceAfter=8, fontName='Helvetica-Bold'))

story = []

# === DISEÑO INDUSTRIAL MODERNO ===

# Fondo industrial
# Fondo industrial (tamaño seguro para el frame)
story.append(crear_fondo_industrial())

# === HEADER INDUSTRIAL ===
header_data = [
    [Paragraph("INDUSTRIAL PROPERTY", styles['TituloIndustrial'])],
    [Paragraph("SANTA MARTA • BOQUERÓN • PARAGUAY", styles['SubtituloIndustrial'])],
    [Spacer(1, 20)],
    [Paragraph("1,747 HECTÁREAS • OPERACIÓN MIXTA", styles['InfoIndustrial'])],
    [Paragraph("AGRÍCOLA + GANADERA + DESARROLLO", styles['InfoIndustrial'])],
]

header_table = Table(header_data, colWidths=[21*cm])
header_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_DARK),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('PADDING', (0, 0), (-1, -1), 20),
    ('BOX', (0, 0), (-1, -1), 0, COLOR_BG_DARK),
]))

story.append(header_table)
story.append(Spacer(1, 30))

# === ESPECIFICACIONES TÉCNICAS ===
especificaciones_data = [
    [
        Paragraph("ESPECIFICACIONES TÉCNICAS", styles['TituloSeccion']),
        Paragraph("INVERSIÓN", styles['TituloSeccion'])
    ],
    [
        Paragraph("• Superficie Total: 1,747 Has<br/>• Agrícolas: 191 Has<br/>• Ganaderas: 715 Has<br/>• Monte: 437 Has<br/>• Desarrollables: 154 Has<br/>• Excedente: 103 Has", styles['DescripcionIndustrial']),
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
    ('PADDING', (0, 0), (-1, -1), 15),
    ('BOX', (0, 0), (-1, -1), 2, COLOR_METAL),
    ('LINEAFTER', (0, 0), (0, 0), 2, COLOR_METAL),
]))

story.append(especificaciones_table)
story.append(Spacer(1, 30))

# === GALERÍA DE IMÁGENES ===
galeria = crear_galeria_carrusel()

# Imagen principal como fondo
if galeria['imagen_principal']:
    story.append(galeria['imagen_principal'])
    story.append(Spacer(1, 20))
    
    # Miniaturas en formato 2x2
    if galeria['miniaturas']:
        # Crear tabla para miniaturas en formato 2x2
        miniaturas_data = []
        
        # Primera fila: primeras 2 imágenes
        if len(galeria['miniaturas']) >= 2:
            fila1 = galeria['miniaturas'][0:2]
            # Rellenar con espacio vacío si solo hay 1 imagen
            while len(fila1) < 2:
                fila1.append(Paragraph("", styles['Contacto']))
            miniaturas_data.append(fila1)
        
        # Segunda fila: siguientes 2 imágenes
        if len(galeria['miniaturas']) >= 3:
            fila2 = galeria['miniaturas'][2:4]
            # Rellenar con espacio vacío si no hay suficientes imágenes
            while len(fila2) < 2:
                fila2.append(Paragraph("", styles['Contacto']))
            miniaturas_data.append(fila2)
        
        # Ajustar ancho de columnas para miniaturas más grandes (10.5cm cada una)
        miniaturas_table = Table(miniaturas_data, colWidths=[10.5*cm, 10.5*cm])
        miniaturas_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 5),
            ('SPACEAFTER', (0, 0), (-1, -1), 10),  # Espacio entre filas
        ]))
        
        story.append(miniaturas_table)
        story.append(Spacer(1, 20))  # Espacio después de las miniaturas
        
        # === PUNTOS DE INTERÉS EN PÁGINA 2 ===
        puntos_interes_info = """
        <font color='#ecf0f1' size='18'><b>PUNTOS DE INTERÉS</b></font><br/><br/>
        <font color='#bdc3c7' size='16'>
        • Ruta de la leche: 76km<br/>
        • Neuland: 150km<br/>
        • Filadelfia: 190km<br/>
        • Mariscal Estigarribia: 250km<br/>
        • Asunción: 500km
        </font>
        """
        
        # Crear tabla para puntos de interés que ocupe todo el ancho
        puntos_interes_data = [
            [Paragraph(puntos_interes_info, ParagraphStyle(name='PuntosInteres', fontSize=16, leading=20, alignment=0, textColor=colors.white))]
        ]
        
        puntos_interes_table = Table(puntos_interes_data, colWidths=[21*cm])
        puntos_interes_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.black),  # Fondo negro
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 15),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#34495e')),  # Borde
        ]))
        
        story.append(puntos_interes_table)
    
    # Enlaces de contacto
    whatsapp_link = "https://wa.me/595981240099?text=Hola%2C%20vi%20el%20campo%20en%20venta%20en%20Santa%20Marta%2C%20Boquerón"
    maps_link = "https://maps.google.com/?q=-23.2984734,-60.5146408"
    drive_link = "https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link"
    
    # Enlaces con diseño limpio y subrayados
    enlaces_data = [
        [
            Paragraph(f"<a href='{whatsapp_link}' color='white'><b>WhatsApp</b><br/><u>+595 981 240 099</u></a>", 
                     ParagraphStyle(name='EnlaceBox', fontSize=18, leading=22, alignment=1, textColor=colors.white)),
            Paragraph(f"<a href='{maps_link}' color='white'><b>Google Maps</b><br/><u>Ver ubicación</u></a>", 
                     ParagraphStyle(name='EnlaceBox', fontSize=18, leading=22, alignment=1, textColor=colors.white)),
            Paragraph(f"<a href='{drive_link}' color='white'><b>Google Drive</b><br/><u>Ver fotos</u></a>", 
                     ParagraphStyle(name='EnlaceBox', fontSize=18, leading=22, alignment=1, textColor=colors.white))
        ]
    ]
    
    enlaces_table = Table(enlaces_data, colWidths=[7*cm, 7*cm, 7*cm])
    enlaces_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.black),  # Fondo negro WhatsApp
        ('BACKGROUND', (1, 0), (1, 0), colors.black),  # Fondo negro Google Maps
        ('BACKGROUND', (2, 0), (2, 0), colors.black),  # Fondo negro Google Drive
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 2, colors.white),  # Borde blanco para contraste
    ]))
    
    story.append(enlaces_table)
    story.append(Spacer(1, 10))
    
    # Información adicional sobre Google Drive
    drive_info = """
    <font color='#ecf0f1' size='18'><b>GALERÍA COMPLETA EN GOOGLE DRIVE</b></font><br/>
    <font color='#7f8c8d' size='16'>Accede a todas las fotos del campo en alta resolución</font>
    """
    # Usar estilo existente en este archivo para evitar KeyError
    story.append(Paragraph(drive_info, styles['EnlacesIndustrial']))
    story.append(Spacer(1, 30))
    
    # === INFORMACIÓN DETALLADA EN DOS COLUMNAS ===
    # Descripción (lado izquierdo)
    descripcion_info = """
    <font color='#ecf0f1' size='18'><b>DESCRIPCIÓN</b></font><br/><br/>
    <font color='#bdc3c7' size='16'>
    Campo muy bien desarrollado con 715 Has ganaderas de pastura Gatton Panic y con 191 agrícolas. Además, la propiedad cuenta con 154 Has que aún se pueden desarrollar y un excedente de 103 Has, sumando así 1.850 Has en total.
    </font>
    """
    
    # Infraestructura (lado derecho)
    infraestructura_info = """
    <font color='#ecf0f1' size='18'><b>INFRAESTRUCTURA</b></font><br/><br/>
    <font color='#bdc3c7' size='16'>
    • Corriente eléctrica con generador.<br/>
    • Acceso al campo por 4 caminos, camino de tierra en buen estado a 76 km del asfalto de la ruta de la leche.<br/>
    • Potreros ganaderos subdivididos en 4 potreros con un bebedero en el medio, haciendo la ganadería más eficiente.<br/>
    • 7 tanques australianos.<br/>
    • 1 manga.<br/>
    • 1 casa principal.<br/>
    • 1 casa de peón.
    </font>
    """
    
    # Crear tabla de dos columnas
    info_detallada_data = [
        [
            Paragraph(descripcion_info, ParagraphStyle(name='InfoColumna', fontSize=16, leading=20, alignment=0, textColor=colors.white)),
            Paragraph(infraestructura_info, ParagraphStyle(name='InfoColumna', fontSize=16, leading=20, alignment=0, textColor=colors.white))
        ]
    ]
    
    info_detallada_table = Table(info_detallada_data, colWidths=[10.5*cm, 10.5*cm])
    info_detallada_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.black),  # Fondo negro para descripción (mismo que overlay)
        ('BACKGROUND', (1, 0), (1, 0), colors.black),  # Fondo negro para infraestructura (mismo que overlay)
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (0, 0), 1, colors.HexColor('#34495e')),  # Borde izquierdo
        ('BOX', (1, 0), (1, 0), 1, colors.HexColor('#34495e')),  # Borde derecho
        ('LINEAFTER', (0, 0), (0, 0), 1, colors.HexColor('#34495e')),  # Línea divisoria
    ]))
    
    story.append(info_detallada_table)
    
    # === FONDO NEGRO HASTA EL FINAL DE LA PÁGINA ===
    # Agregar espacio adicional para llenar la página y forzar las miniaturas a la página 2
    espacio_adicional = 12*cm  # Reducir espacio para evitar página 4
    fondo_final_data = [[Paragraph("", ParagraphStyle(name='FondoFinal', fontSize=1))]]
    fondo_final_table = Table(fondo_final_data, colWidths=[21*cm], rowHeights=[espacio_adicional])
    fondo_final_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.black),
        ('BOX', (0, 0), (-1, -1), 0, colors.black),
    ]))
    story.append(fondo_final_table)
    
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