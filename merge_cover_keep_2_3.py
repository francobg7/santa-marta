from pypdf import PdfReader, PdfWriter

COVER = "_cover_temp.pdf"
TRIMMED = "campo_santa_marta_sin_1_5.pdf"
OUTPUT = "SANTA-MARTA.pdf"

writer = PdfWriter()

# Add cover (single page)
cover_reader = PdfReader(COVER)
writer.add_page(cover_reader.pages[0])

# Keep pages 2 and 3 from trimmed (1-based indexing -> 0-based 1 and 2)
trim_reader = PdfReader(TRIMMED)
for idx in [1, 2]:
    if idx < len(trim_reader.pages):
        writer.add_page(trim_reader.pages[idx])

with open(OUTPUT, "wb") as f:
    writer.write(f)

print(f"✅ Created {OUTPUT} with: cover + pages 2,3 from {TRIMMED}")

