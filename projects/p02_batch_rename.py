from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_02" / "scans"
DEST = ROOT / "output" / "project_02"

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    items = sorted(p for p in SOURCE.iterdir() if p.is_file())
    for number, source in enumerate(items, 1):
        name = f"invoice_{number:03d}{source.suffix.lower()}"
        shutil.copy2(source, DEST / name)
        print(f"{source.name} -> {name}")
    print("Original files were not modified.")

if __name__ == "__main__":
    main()
