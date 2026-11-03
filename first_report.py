from datetime import date
from pathlib import Path

tasks = [
    ("Organize invoices", 15),
    ("Update Excel report", 25),
    ("Find missing PDFs", 10),
]

saved_minutes = sum(minutes for _, minutes in tasks)
lines = [
    "OFFICE AUTOMATION: FIRST REPORT",
    f"Date: {date.today().isoformat()}",
    "",
    "Tasks to automate:",
]
for task, minutes in tasks:
    lines.append(f"- {task}: {minutes} min")
lines.append("")
lines.append(f"Potential time saved: {saved_minutes} min")

output = Path("output")
output.mkdir(exist_ok=True)
file_path = output / "first_report.txt"
file_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Created: {file_path}")
