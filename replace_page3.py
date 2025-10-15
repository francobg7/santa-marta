from pypdf import PdfReader, PdfWriter
import shutil
import os

SOURCE = "SANTA-MARTA_backup_sin_p2.pdf"
TARGET = "SANTA-MARTA.pdf"
BACKUP = "SANTA-MARTA_backup_before_p3_replace.pdf"
TEMP_OUTPUT = "SANTA-MARTA_temp.pdf"

if not os.path.exists(SOURCE):
    raise SystemExit(f"No existe {SOURCE}")
if not os.path.exists(TARGET):
    raise SystemExit(f"No existe {TARGET}")

# Backup target
shutil.copyfile(TARGET, BACKUP)

# Read both PDFs
source_reader = PdfReader(SOURCE)
target_reader = PdfReader(TARGET)

writer = PdfWriter()

# Add pages 1 and 2 from target (SANTA-MARTA.pdf)
for i in range(2):  # pages 0 and 1 (1-based: 1 and 2)
    writer.add_page(target_reader.pages[i])

# Add page 3 from source (SANTA-MARTA_backup_sin_p2.pdf)
if len(source_reader.pages) >= 3:  # page index 2 (1-based: 3)
    writer.add_page(source_reader.pages[2])
else:
    raise SystemExit(f"Source PDF has only {len(source_reader.pages)} pages, need at least 3")

# Write result
with open(TEMP_OUTPUT, "wb") as f:
    writer.write(f)

# Replace original
shutil.move(TEMP_OUTPUT, TARGET)

print(f"✅ Página 3 reemplazada. Backup guardado en {BACKUP}")
print(f"📄 SANTA-MARTA.pdf ahora tiene la página 3 correcta de {SOURCE}")
