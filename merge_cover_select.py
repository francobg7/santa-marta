from pypdf import PdfReader, PdfWriter

COVER = "_cover_temp.pdf"
SOURCE = "campo_santa_marta_sin_1_5.pdf"
OUTPUT = "SANTA-MARTA.pdf"

# Merge cover (single page) + pages 2 and 3 (1-based) from SOURCE

def main():
    writer = PdfWriter()

    cover_reader = PdfReader(COVER)
    if len(cover_reader.pages) == 0:
        raise SystemExit("Cover PDF has no pages")
    writer.add_page(cover_reader.pages[0])

    src_reader = PdfReader(SOURCE)
    # Keep pages 2 and 3 (1-based) => indices 1 and 2 if exist
    for idx in [1, 2]:
        if idx < len(src_reader.pages):
            writer.add_page(src_reader.pages[idx])

    with open(OUTPUT, "wb") as f:
        writer.write(f)
    print(f"✅ Combined to {OUTPUT} (cover + pages 2-3)")


if __name__ == "__main__":
    main()
