from pathlib import Path

tasks = [("Check invoices", 12), ("Prepare report", 28),
         ("Rename attachments", 7)]
total = sum(minutes for _, minutes in tasks)
summary = ["OFFICE TASK SUMMARY", f"Tasks: {len(tasks)}",
           f"Estimated minutes: {total}"]
output = Path("task_summary.txt")
output.write_text("\n".join(summary), encoding="utf-8")
print(output.resolve())
