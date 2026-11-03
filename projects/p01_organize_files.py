from pathlib import Path
import shutil
import filecmp

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_01" / "inbox"
DEST = ROOT / "output" / "project_01"
GROUPS = {".pdf": "PDFs", ".xlsx": "Spreadsheets",
          ".csv": "Spreadsheets", ".jpg": "Images",
          ".png": "Images"}

def free_name(path):
    if not path.exists():
        return path
    counter = 2
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    count = 0
    for file in sorted(SOURCE.iterdir()):
        if not file.is_file():
            continue
        group = GROUPS.get(file.suffix.lower(), "Other")
        folder = DEST / group
        folder.mkdir(exist_ok=True)
        target = folder / file.name
        if target.exists() and filecmp.cmp(file, target, shallow=False):
            continue  # Already copied: safe to rerun without duplication
        shutil.copy2(file, free_name(target))
        count += 1
    print(f"Copied {count} new files to {DEST}")

if __name__ == "__main__":
    main()
