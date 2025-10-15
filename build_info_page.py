from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from urllib.parse import quote

OUTPUT = "_info_page_updated.pdf"

def build_info_page(path: str):
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='InfoTitleCustom', fontSize=22, leading=26, alignment=0, textColor=colors.white, spaceAfter=10))
    styles.add(ParagraphStyle(name='InfoBodyCustom', fontSize=16, leading=20, alignment=0, textColor=colors.HexColor('#bdc3c7'), spaceAfter=8))
    styles.add(ParagraphStyle(name='InfoLinkCustom', fontSize=18, leading=22, alignment=1, textColor=colors.white))

    story = []

    # Sección: Puntos de interés (como en la hoja 3)
    puntos_interes_html = """
    <font color='#ecf0f1' size='18'><b>PUNTOS DE INTERÉS</b></font><br/><br/>
    <font color='#bdc3c7' size='16'>
    • Ruta de la leche: 76km<br/>
    • Neuland: 150km<br/>
    • Filadelfia: 190km<br/>
    • Mariscal Estigarribia: 250km<br/>
    • Asunción: 500km
    </font>
    """

    # Sección: Descripción e Infraestructura
    descripcion_html = """
    <font color='#ecf0f1' size='18'><b>DESCRIPCIÓN</b></font><br/><br/>
    <font color='#bdc3c7' size='16'>
    Campo muy bien desarrollado con 715 Has ganaderas de pastura Gatton Panic y con 191 agrícolas. Además, la propiedad cuenta con 154 Has que aún se pueden desarrollar y un excedente de 103 Has, sumando así 1.850 Has en total.
    </font>
    """

    infraestructura_html = """
    <font color='#ecf0f1' size='18'><b>INFRAESTRUCTURA</b></font><br/><br/>
    <font color='#bdc3c7' size='16'>
    • Corriente eléctrica con generador.<br/>
    • Acceso al campo por 4 caminos, camino de tierra en buen estado a 76 km del asfalto de la ruta de la leche.<br/>
    • Potreros ganaderos subdivididos en 4 potreros con un bebedero en el medio.<br/>
    • 7 tanques australianos, 1 manga, 1 casa principal y 1 casa de peón.
    </font>
    """

    # Enlaces con WhatsApp actualizado (mensaje codificado)
    mensaje = "Hola Ing. Granada, Me interesa el campo en venta en Santa Marta, Boquerón"
    whatsapp_link = f"https://wa.me/595981240099?text={quote(mensaje)}"
    maps_link = "https://maps.google.com/?q=-23.2984734,-60.5146408"
    drive_link = "https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link"

    enlaces_row = [
        Paragraph(f"<a href='{whatsapp_link}' color='white'><b>WhatsApp</b><br/><u>+595 981 240 099</u></a>", styles['InfoLinkCustom']),
        Paragraph(f"<a href='{maps_link}' color='white'><b>Google Maps</b><br/><u>Ver ubicación</u></a>", styles['InfoLinkCustom']),
        Paragraph(f"<a href='{drive_link}' color='white'><b>Google Drive</b><br/><u>Ver fotos</u></a>", styles['InfoLinkCustom'])
    ]

    # Tabla principal (fondo negro)
    content = [
        [Paragraph(puntos_interes_html, styles['InfoBodyCustom'])],
        [Spacer(1, 20)],
        [Table([[Paragraph(descripcion_html, styles['InfoBodyCustom']), Paragraph(infraestructura_html, styles['InfoBodyCustom'])]], colWidths=[10.5*cm, 10.5*cm])],
        [Spacer(1, 20)],
        [Table([enlaces_row], colWidths=[7*cm, 7*cm, 7*cm])]
    ]

    outer = Table(content, colWidths=[21*cm])
    outer.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('BOX', (0, 0), (-1, -1), 0, colors.black),
    ]))

    story.append(outer)
    doc.build(story)


if __name__ == "__main__":
    build_info_page(OUTPUT)
    print(f"✅ Página de información creada: {OUTPUT}")


