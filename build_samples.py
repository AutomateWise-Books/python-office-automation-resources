from pathlib import Path
import csv
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

ROOT = Path(__file__).resolve().parent
SAMPLES = ROOT / "samples"

def folder(n, name=""):
    path = SAMPLES / f"project_{n:02d}" / name
    path.mkdir(parents=True, exist_ok=True)
    return path

def rows_csv(path, headings, records):
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(headings)
        writer.writerows(records)

def workbook(path, headings, records):
    book = Workbook()
    sheet = book.active
    sheet.append(headings)
    for row in records:
        sheet.append(row)
    book.save(path)

def pdf(path, label):
    c = canvas.Canvas(str(path), pagesize=letter)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(60, 730, label)
    c.setFont("Helvetica", 11)
    c.drawString(60, 700, "Fictional document for Python practice only.")
    c.save()

def main():
    inbox = folder(1, "inbox")
    (inbox / "notes.txt").write_text("Meeting notes", encoding="utf-8")
    (inbox / "image.jpg").write_bytes(b"SAMPLE IMAGE PLACEHOLDER")
    pdf(inbox / "brief.pdf", "Office Brief")
    workbook(inbox / "tasks.xlsx", ["Task"], [["Inventory"]])
    scans = folder(2, "scans")
    for i, filename in enumerate(["scan_c.txt", "scan_a.txt", "scan_b.txt"]):
        (scans / filename).write_text(f"Sample scan {i}", encoding="utf-8")
    dup = folder(3, "documents")
    for name, value in [("a.txt", "same"), ("a_copy.txt", "same"),
                        ("b.txt", "unique"), ("b_copy.txt", "unique")]:
        (dup / name).write_text(value, encoding="utf-8")
    workbook(folder(4) / "contacts.xlsx", ["Name", "Email", "Amount"], [
        ["  jane   doe  ", " JANE@EXAMPLE.COM ", "$1,200"],
        ["sam lee", "sam@example.com", 54],
        ["", "unknown.example.com", "N/A"]
    ])
    deps = folder(5, "departments")
    workbook(deps / "north.xlsx", ["Employee", "Department", "Hours"],
             [["Maya", "Support", 36], ["Noah", "Finance", 39]])
    workbook(deps / "south.xlsx", ["Employee", "Department", "Hours"],
             [["Ava", "Support", 40], ["Leo", "Sales", 37]])
    workbook(folder(6) / "sales.xlsx", ["Date", "Team", "Amount"], [
        ["2026-09-02", "North", 120.5], ["2026-09-05", "South", 200],
        ["2026-10-03", "North", 80], ["2026-10-06", "South", 95.25]
    ])
    rows_csv(folder(7) / "orders.csv", ["Order", "Customer", "Value"],
             [["A101", "Alice", 30], ["A102", "Bob", 40]])
    pdf(folder(8,"pdfs") / "01_summary.pdf", "Summary Report")
    pdf(folder(8,"pdfs") / "02_appendix.pdf", "Appendix")
    pdf(folder(9,"pdfs") / "meeting.pdf", "Meeting Notes")
    rows_csv(folder(10) / "weekly_metrics.csv", ["Department", "Completed"],
             [["Finance", 14], ["Operations", 27], ["Support", 19]])
    pdf(folder(12) / "attachment.pdf", "Document for Review")
    rows_csv(folder(13) / "clients.csv", ["Name", "Plan", "ReviewDate"],
             [["Emma Smith", "Standard", "2026-12-01"],
              ["Noah Brown", "Premium", "2026-12-15"]])
    print("Fictional practice files created in samples/.")

if __name__ == "__main__":
    main()
