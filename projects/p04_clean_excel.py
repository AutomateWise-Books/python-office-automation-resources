from pathlib import Path
from openpyxl import load_workbook, Workbook

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_04" / "contacts.xlsx"
DEST = ROOT / "output" / "project_04" / "clean_contacts.xlsx"

def main():
    source = load_workbook(SOURCE, read_only=True, data_only=True).active
    output = Workbook()
    clean = output.active
    clean.title = "Clean"
    clean.append(["Name", "Email", "Amount"])
    review = output.create_sheet("Needs Review")
    review.append(["Name", "Email", "Amount", "Reason"])
    for row in list(source.iter_rows(values_only=True))[1:]:
        name, email, amount = (list(row) + [None] * 3)[:3]
        name = " ".join(str(name or "").split()).title()
        email = str(email or "").strip().lower()
        try:
            amount = float(str(amount).replace("$", "").replace(",", ""))
        except ValueError:
            amount = None
        if not name or "@" not in email or amount is None:
            review.append([name, email, amount, "Missing/invalid field"])
        else:
            clean.append([name, email, amount])
    DEST.parent.mkdir(parents=True, exist_ok=True)
    output.save(DEST)
    print(f"Saved {clean.max_row-1} clean records; {review.max_row-1} to review.")

if __name__ == "__main__":
    main()
