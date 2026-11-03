from pathlib import Path
from datetime import datetime, timezone
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "project_15" / "toolkit_summary.txt"
STEPS = ["p01_organize_files.py", "p05_merge_workbooks.py",
         "p08_merge_pdfs.py"]

def main():
    results = []
    for script in STEPS:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "projects" / script)],
            check=True, capture_output=True, text=True
        )
        results.append(f"{script}: {completed.stdout.strip()}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    lines = ["OFFICE AUTOMATION TOOLKIT",
             f"Run UTC: {datetime.now(timezone.utc).isoformat()}", ""]
    OUTPUT.write_text("\n".join(lines + results), encoding="utf-8")
    print(f"Ran {len(STEPS)} workflows; summary saved to {OUTPUT}")

if __name__ == "__main__":
    main()
