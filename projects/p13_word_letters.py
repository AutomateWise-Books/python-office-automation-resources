from pathlib import Path
import csv
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_13" / "clients.csv"
DEST = ROOT / "output" / "project_13"

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    with SOURCE.open(newline="", encoding="utf-8") as handle:
        records = list(csv.DictReader(handle))
    for number, row in enumerate(records, 1):
        document = Document()
        document.add_heading("Your Service Update", 0)
        document.add_paragraph(f"Dear {row['Name']},")
        document.add_paragraph(
            f"Your service plan {row['Plan']} is scheduled for review on "
            f"{row['ReviewDate']}. Please contact our office with questions."
        )
        document.add_paragraph("Kind regards,\nThe Operations Team")
        document.save(DEST / f"letter_{number:03d}.docx")
    print(f"Generated {len(records)} Word letters.")

if __name__ == "__main__":
    main()
