import sys
from pypdf import PdfReader, PdfWriter

# Usage: python remove_pages.py input.pdf output.pdf 1 5

def main():
    if len(sys.argv) < 4:
        print("Usage: python remove_pages.py input.pdf output.pdf <page_numbers_to_remove...>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_pages = sorted({int(p) for p in sys.argv[3:]})

    reader = PdfReader(input_path)
    writer = PdfWriter()

    total = len(reader.pages)
    remove_zero_based = {p-1 for p in remove_pages if 1 <= p <= total}

    for idx in range(total):
        if idx not in remove_zero_based:
            writer.add_page(reader.pages[idx])

    with open(output_path, "wb") as f:
        writer.write(f)

    kept = [i+1 for i in range(total) if i not in remove_zero_based]
    print(f"Saved {output_path}. Kept pages: {kept}")

if __name__ == "__main__":
    main()
