from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "output" / "project_14" / "run_history.csv"

def main():
    DEST.parent.mkdir(parents=True, exist_ok=True)
    new_file = not DEST.exists()
    with DEST.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new_file:
            writer.writerow(["run_utc", "status"])
        writer.writerow([datetime.now(timezone.utc).isoformat(), "ok"])
    print(f"Recorded run in {DEST}")

if __name__ == "__main__":
    main()
