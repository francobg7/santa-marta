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

def crear_fondo_negro():
    """Crear fondo negro para el PDF usando tabla"""
    fondo_data = [[Paragraph("", ParagraphStyle(name='Fondo', fontSize=1))]]
    fondo_table = Table(fondo_data, colWidths=[19*cm], rowHeights=[27*cm])
    fondo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.black),
        ('BOX', (0, 0), (-1, -1), 0, colors.black),
    ]))
    return fondo_table

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

# === ESTILOS SIMPLIFICADOS ===
styles = getSampleStyleSheet()

# Estilos personalizados más grandes
styles.add(ParagraphStyle(name='TituloPrincipal', fontSize=36, leading=42, alignment=1, textColor=colors.white, spaceAfter=20))
styles.add(ParagraphStyle(name='Subtitulo', fontSize=24, leading=28, alignment=1, textColor=colors.white, spaceAfter=12))
styles.add(ParagraphStyle(name='InfoDestacada', fontSize=20, leading=24, alignment=1, textColor=colors.white, spaceAfter=10))
styles.add(ParagraphStyle(name='Precio', fontSize=28, leading=32, alignment=1, textColor=colors.HexColor('#f39c12'), spaceAfter=16))
styles.add(ParagraphStyle(name='Contacto', fontSize=18, leading=22, alignment=1, textColor=colors.white, spaceAfter=8))
styles.add(ParagraphStyle(name='Enlaces', fontSize=14, leading=18, alignment=1, textColor=colors.HexColor('#3498db'), spaceAfter=8))

story = []

# === INICIO DIRECTO CON CONTENIDO ===

# === INFORMACIÓN PRINCIPAL SOBRE FONDO ===
# Título principal con overlay sobre la imagen
titulo_principal = "CAMPO EN VENTA<br/><font size='24' color='#ecf0f1'>Santa Marta, Boquerón - Paraguay</font>"

# Información esencial del campo
info_esencial = """
<font size='20'><b>1.747 Has • Mixto (Agrícola + Ganadero)</b></font><br/>
<font size='18'>Agrícolas: 191 Has • Ganaderas: 715 Has • Monte: 437 Has</font><br/>
<font size='18'>Precipitación: 800 mm anuales</font>
"""

# Precio destacado
precio_destacado = "CONSULTAR PRECIO<br/><font size='18'>Contactar para más información</font>"

# Contacto directo
contacto_directo = """
<font size='18'><b>CONTACTO DIRECTO</b></font><br/>
<font size='16'>WhatsApp: +595 981 240 099</font><br/>
<font size='14'><b>Mauricio Granada</b></font><br/>
<font size='14'>Disponible 24/7</font>
"""

# === CREAR OVERLAY DE INFORMACIÓN ===
# Crear tabla con información superpuesta
overlay_data = [
    [Paragraph(titulo_principal, styles['TituloPrincipal'])],
    [Spacer(1, 30)],
    [Paragraph(info_esencial, styles['InfoDestacada'])],
    [Spacer(1, 25)],
    [Paragraph(precio_destacado, styles['Precio'])],
    [Spacer(1, 30)],
    [Paragraph(contacto_directo, styles['Contacto'])]
]

overlay_table = Table(overlay_data, colWidths=[21*cm])
overlay_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.black),  # Fondo negro
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 30),
    ('BOX', (0, 0), (-1, -1), 0, colors.black),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.black]),
]))

# === GALERÍA DE IMÁGENES ===
galeria = crear_galeria_carrusel()

# Imagen principal como fondo
if galeria['imagen_principal']:
    story.append(galeria['imagen_principal'])
    story.append(Spacer(1, 10))
    
    # Overlay de información sobre la imagen
    story.append(overlay_table)
    story.append(Spacer(1, 20))  # Reducir espacio antes de las miniaturas
    
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
    story.append(Paragraph(drive_info, styles['Enlaces']))
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
