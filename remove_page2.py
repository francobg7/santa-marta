from pypdf import PdfReader, PdfWriter
import shutil
import os

INPUT = "SANTA-MARTA.pdf"
BACKUP = "SANTA-MARTA_backup.pdf"
TEMP_OUTPUT = "SANTA-MARTA_tmp.pdf"

if not os.path.exists(INPUT):
    raise SystemExit(f"No existe {INPUT}")

# Backup
shutil.copyfile(INPUT, BACKUP)

reader = PdfReader(INPUT)
writer = PdfWriter()

# Remove page 2 (1-based). 0-based index -> 1
remove_index = 1

for i in range(len(reader.pages)):
    if i == remove_index:
        continue
    writer.add_page(reader.pages[i])

with open(TEMP_OUTPUT, "wb") as f:
    writer.write(f)

# Replace original
shutil.move(TEMP_OUTPUT, INPUT)

print("✅ Página 2 eliminada. Archivo actualizado:", INPUT)

