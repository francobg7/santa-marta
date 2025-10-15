from pypdf import PdfReader, PdfWriter
import shutil
import os

TARGET = "SANTA-MARTA.pdf"
REPLACEMENT_PAGE_PDF = os.environ.get("REPLACEMENT_PDF", "_info_page_updated.pdf")  # single-page pdf
BACKUP = "SANTA-MARTA_backup_before_p3_updated.pdf"
TEMP_OUTPUT = "SANTA-MARTA_temp_updated.pdf"

if not os.path.exists(TARGET):
    raise SystemExit(f"No existe {TARGET}")
if not os.path.exists(REPLACEMENT_PAGE_PDF):
    raise SystemExit(f"No existe {REPLACEMENT_PAGE_PDF}")

shutil.copyfile(TARGET, BACKUP)

target_reader = PdfReader(TARGET)
replacement_reader = PdfReader(REPLACEMENT_PAGE_PDF)

if len(replacement_reader.pages) != 1:
    raise SystemExit("El PDF de reemplazo debe tener exactamente 1 página")

writer = PdfWriter()

# Keep pages 1 and 2 from target
for i in range(min(2, len(target_reader.pages))):
    writer.add_page(target_reader.pages[i])

# Add replacement as page 3
writer.add_page(replacement_reader.pages[0])

with open(TEMP_OUTPUT, "wb") as f:
    writer.write(f)

shutil.move(TEMP_OUTPUT, TARGET)

print(f"✅ Página 3 reemplazada con {REPLACEMENT_PAGE_PDF}")

