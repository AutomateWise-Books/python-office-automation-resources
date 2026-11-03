from pathlib import Path
import csv
from openpyxl import Workbook

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_07" / "orders.csv"
DEST = ROOT / "output" / "project_07" / "orders.xlsx"

def main():
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        rows = csv.reader(handle)
        book = Workbook()
        sheet = book.active
        sheet.title = "Orders"
        for row in rows:
            sheet.append(row)
    sheet.freeze_panes = "A2"
    DEST.parent.mkdir(parents=True, exist_ok=True)
    book.save(DEST)
    print(f"Converted {sheet.max_row - 1} data rows to Excel.")

if __name__ == "__main__":
    main()
