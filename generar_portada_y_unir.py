from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from pypdf import PdfReader, PdfWriter
import os

INPUT_TRIMMED = "campo_santa_marta_sin_1_5.pdf"
COVER_PATH = "_cover_temp.pdf"
OUTPUT_PATH = "SANTA-MARTA.pdf"
IMAGE_PATH = "campo1.jpg"


def build_cover_pdf(path: str):
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(name='HeroTitle', fontSize=36, leading=40, alignment=1, textColor=colors.white, spaceAfter=6))
    styles.add(ParagraphStyle(name='HeroSub', fontSize=18, leading=22, alignment=1, textColor=colors.white, spaceAfter=10))
    styles.add(ParagraphStyle(name='HeroInfo', fontSize=14, leading=18, alignment=1, textColor=colors.white, spaceAfter=6))
    styles.add(ParagraphStyle(name='HeroPrice', fontSize=20, leading=24, alignment=1, textColor=colors.white, spaceAfter=10))
    styles.add(ParagraphStyle(name='HeroContact', fontSize=14, leading=18, alignment=1, textColor=colors.white, spaceAfter=4))

    story = []

    # Imagen de portada a todo el ancho
    if os.path.exists(IMAGE_PATH):
        story.append(Image(IMAGE_PATH, width=21*cm, height=10*cm))
        story.append(Spacer(1, 8))

    # Cuadro negro con toda la info
    hero_data = [[
        Paragraph("CAMPO EN VENTA", styles['HeroTitle']),
    ], [
        Paragraph("Santa Marta, Boquerón - Paraguay", styles['HeroSub'])
    ], [
        Paragraph("<b>1.747 Has • Mixto (Agrícola + Ganadero)</b>", styles['HeroInfo'])
    ], [
        Paragraph("Agrícolas: 191 Has • Ganaderas: 715 Has • Monte: 437 Has", styles['HeroInfo'])
    ], [
        Paragraph("Precipitación: 800 mm anuales", styles['HeroInfo'])
    ], [
        Paragraph("CONSULTAR PRECIO", styles['HeroPrice'])
    ], [
        Paragraph("Contactar para más información", styles['HeroInfo'])
    ], [
        Paragraph("MAURICIO GRANADA", styles['HeroContact'])
    ], [
        Paragraph("WhatsApp: +595 981 240 099", styles['HeroContact'])
    ]]

    # La tabla tiene una sola columna; usamos estilos para fondo negro
    table = Table(hero_data, colWidths=[21*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 0, colors.black),
    ]))

    story.append(table)

    # Imagen adicional campo7.jpg al final de la página 1 (si existe)
    extra_image_path = "campo7.jpg"
    if os.path.exists(extra_image_path):
        # Espacio pequeño para separar del bloque negro
        story.append(Spacer(1, 6))
        # Ajuste de tamaño para ocupar más espacio sin desbordar
        story.append(Image(extra_image_path, width=21*cm, height=9.5*cm))

    doc.build(story)


def merge_cover_with_existing(cover_path: str, input_path: str, output_path: str):
    writer = PdfWriter()
    for src in [cover_path, input_path]:
        reader = PdfReader(src)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, 'wb') as f:
        writer.write(f)


if __name__ == "__main__":
    if not os.path.exists(INPUT_TRIMMED):
        raise SystemExit(f"No existe {INPUT_TRIMMED}.")

    build_cover_pdf(COVER_PATH)
    merge_cover_with_existing(COVER_PATH, INPUT_TRIMMED, OUTPUT_PATH)
    print(f"✅ Portada creada y unida: {OUTPUT_PATH}")

