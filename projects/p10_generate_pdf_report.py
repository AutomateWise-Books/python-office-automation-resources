from pathlib import Path
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_10" / "weekly_metrics.csv"
DEST = ROOT / "output" / "project_10" / "weekly_report.pdf"

def main():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        data = list(csv.DictReader(handle))
    total = sum(int(row["Completed"]) for row in data)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    page = canvas.Canvas(str(DEST), pagesize=letter)
    page.setTitle("Weekly Office Metrics")
    page.setFont("Helvetica-Bold", 18)
    page.drawString(54, 735, "Weekly Office Metrics")
    page.setFont("Helvetica", 11)
    page.drawString(54, 704, f"Total completed tasks: {total}")
    page.line(54, 686, 558, 686)
    page.setFont("Helvetica-Bold", 11)
    page.drawString(54, 660, "Department")
    page.drawRightString(535, 660, "Completed")
    page.setFont("Helvetica", 11)
    for index, row in enumerate(data):
        y = 638 - index * 22
        if y < 70:
            page.showPage()
            y = 740
        page.drawString(54, y, row["Department"][:50])
        page.drawRightString(535, y, row["Completed"])
    page.save()
    print(f"Created report at {DEST}")

if __name__ == "__main__":
    main()
