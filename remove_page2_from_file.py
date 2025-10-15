from pypdf import PdfReader, PdfWriter
import os
import sys

def remove_second_page(input_path: str, output_path: str) -> None:
    reader = PdfReader(input_path)
    writer = PdfWriter()

    remove_index = 1  # zero-based index for page 2
    for i in range(len(reader.pages)):
        if i == remove_index:
            continue
        writer.add_page(reader.pages[i])

    with open(output_path, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Uso: python remove_page2_from_file.py <input.pdf> [output.pdf]")

    input_pdf = sys.argv[1]
    if not os.path.exists(input_pdf):
        raise SystemExit(f"No existe {input_pdf}")

    if len(sys.argv) >= 3:
        output_pdf = sys.argv[2]
    else:
        root, ext = os.path.splitext(input_pdf)
        output_pdf = f"{root}_sin_p2{ext}"

    remove_second_page(input_pdf, output_pdf)
    print(f"✅ Página 2 eliminada: {output_pdf}")


