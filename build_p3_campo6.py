from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
import os

OUTPUT_P3 = "_p3_campo6.pdf"

MAIN_IMAGE = "campo6.jpg"
THUMBS = [
    ("campo2.jpg", "Pasturas"),
    ("campo3.jpg", "Agrícola"),
    ("campo4.jpg", "Monte"),
    ("campo5.jpg", "Panorámica"),
]


def safe_image(path: str, width: float, height: float):
    if os.path.exists(path):
        return Image(path, width=width, height=height)
    return None


def build_p3(path: str):
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
    story = []

    main = safe_image(MAIN_IMAGE, 21*cm, 12*cm)
    if main:
        story.append(main)
        story.append(Spacer(1, 18))

    # Build 2x2 thumbnails filling width
    thumbs = []
    for img, _label in THUMBS:
        t = safe_image(img, 10.5*cm, 6.5*cm)
        if t:
            thumbs.append(t)

    data = []
    if thumbs:
        row1 = thumbs[0:2]
        while len(row1) < 2:
            row1.append(Spacer(1, 1))
        data.append(row1)

        row2 = thumbs[2:4]
        while len(row2) < 2:
            row2.append(Spacer(1, 1))
        data.append(row2)

        tbl = Table(data, colWidths=[10.5*cm, 10.5*cm])
        tbl.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('PADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(tbl)

    # Keep black background look by wrapping entire page content if needed
    # but since the rest of the document already has consistent margins, we focus on images here

    doc.build(story)


if __name__ == "__main__":
    build_p3(OUTPUT_P3)
    print(f"✅ Página 3 con campo6 y miniaturas generada: {OUTPUT_P3}")


