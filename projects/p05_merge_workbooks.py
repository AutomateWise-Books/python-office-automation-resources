from pathlib import Path
from openpyxl import load_workbook, Workbook

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_05" / "departments"
DEST = ROOT / "output" / "project_05" / "merged.xlsx"
FIELDS = ["Employee", "Department", "Hours"]

def main():
    result = Workbook()
    sheet = result.active
    sheet.title = "Combined"
    sheet.append(FIELDS + ["Source File"])
    count = 0
    for path in sorted(SOURCE.glob("*.xlsx")):
        data = load_workbook(path, read_only=True, data_only=True).active
        records = data.iter_rows(values_only=True)
        headings = next(records, None)
        if headings is None or list(headings)[:3] != FIELDS:
            raise ValueError(f"Unexpected columns in {path.name}")
        for values in records:
            if not any(v is not None for v in values):
                continue
            sheet.append(list(values)[:3] + [path.name])
            count += 1
    DEST.parent.mkdir(parents=True, exist_ok=True)
    result.save(DEST)
    print(f"Merged {count} rows from {len(list(SOURCE.glob('*.xlsx')))} files.")

if __name__ == "__main__":
    main()
