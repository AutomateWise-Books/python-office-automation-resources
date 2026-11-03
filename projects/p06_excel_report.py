from pathlib import Path
from collections import defaultdict
from datetime import datetime
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, PatternFill

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_06" / "sales.xlsx"
DEST = ROOT / "output" / "project_06" / "sales_report.xlsx"

def main():
    data = load_workbook(SOURCE, read_only=True, data_only=True).active
    totals = defaultdict(float)
    records = list(data.iter_rows(min_row=2, values_only=True))
    for day, team, amount in records:
        date = day if isinstance(day, datetime) else datetime.fromisoformat(str(day))
        totals[(date.strftime("%Y-%m"), str(team))] += float(amount)
    book = Workbook()
    summary = book.active
    summary.title = "Summary"
    summary.append(["Month", "Team", "Total Sales"])
    for (month, team), total in sorted(totals.items()):
        summary.append([month, team, round(total, 2)])
    details = book.create_sheet("Source Records")
    details.append(["Date", "Team", "Amount"])
    for item in records:
        details.append(list(item))
    for page in [summary, details]:
        for cell in page[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="183A60")
        page.freeze_panes = "A2"
        page.column_dimensions["A"].width = 20
        page.column_dimensions["B"].width = 20
        page.column_dimensions["C"].width = 20
    for cell in summary["C"][1:]:
        cell.number_format = '#,##0.00'
    DEST.parent.mkdir(parents=True, exist_ok=True)
    book.save(DEST)
    print(f"Generated {len(totals)} summary groups in {DEST.name}.")

if __name__ == "__main__":
    main()
