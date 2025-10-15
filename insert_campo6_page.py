from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from pypdf import PdfReader, PdfWriter
import os

COVER = "_cover_temp.pdf"
BACKUP_SIN_P2 = "SANTA-MARTA_backup_sin_p2.pdf"
MIDDLE_PAGE = "_middle_campo6.pdf"
OUTPUT = "SANTA-MARTA.pdf"

# 1) Build middle page with campo6.jpg + thumbnails (campo2-5)

def build_middle_page(path: str):
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
    story = []

    # Main image: campo6.jpg
    if os.path.exists("campo6.jpg"):
        story.append(Image("campo6.jpg", width=21*cm, height=12*cm))
        story.append(Spacer(1, 20))

    # Thumbnails 2x2 from campo2-5 if available
    thumbs = []
    for name in ["campo2.jpg", "campo3.jpg", "campo4.jpg", "campo5.jpg"]:
        if os.path.exists(name):
            thumbs.append(Image(name, width=10.5*cm, height=6.5*cm))

    if thumbs:
        rows = []
        rows.append(thumbs[0:2] if len(thumbs) >= 1 else [])
        if len(thumbs) > 2:
            rows.append(thumbs[2:4])

        # Ensure 2 columns
        for r in rows:
            while len(r) < 2:
                r.append(Spacer(10.5*cm, 6.5*cm))

        mini_table = Table(rows, colWidths=[10.5*cm, 10.5*cm])
        mini_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('PADDING', (0, 0), (-1, -1), 5),
            ('BACKGROUND', (0, 0), (-1, -1), colors.black),
        ]))
        story.append(mini_table)

    doc.build(story)


# 2) Assemble: COVER (p1) + MIDDLE (p2) + last page from backup_sin_p2 (p2 there)

def assemble():
    writer = PdfWriter()

    # cover
    cover_reader = PdfReader(COVER)
    writer.add_page(cover_reader.pages[0])

    # middle
    mid_reader = PdfReader(MIDDLE_PAGE)
    writer.add_page(mid_reader.pages[0])

    # last page from backup_sin_p2 (index 1)
    tail_reader = PdfReader(BACKUP_SIN_P2)
    if len(tail_reader.pages) >= 2:
        writer.add_page(tail_reader.pages[1])

    with open(OUTPUT, 'wb') as f:
        writer.write(f)


if __name__ == "__main__":
    if not os.path.exists(COVER):
        raise SystemExit(f"No existe {COVER}")
    if not os.path.exists(BACKUP_SIN_P2):
        raise SystemExit(f"No existe {BACKUP_SIN_P2}")

    build_middle_page(MIDDLE_PAGE)
    assemble()
    print(f"✅ Generado {OUTPUT} con portada + página campo6 + última página")
