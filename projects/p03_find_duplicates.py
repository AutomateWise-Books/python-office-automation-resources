from pathlib import Path
import hashlib
import csv

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_03" / "documents"
DEST = ROOT / "output" / "project_03" / "duplicates.csv"

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    seen = {}
    matches = []
    for file in sorted(SOURCE.rglob("*")):
        if not file.is_file():
            continue
        signature = (file.stat().st_size, sha256(file))
        if signature in seen:
            matches.append((str(file.relative_to(SOURCE)),
                            str(seen[signature].relative_to(SOURCE))))
        else:
            seen[signature] = file
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with DEST.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["duplicate", "same_content_as"])
        writer.writerows(matches)
    print(f"Found {len(matches)} duplicates. Review {DEST}; no files deleted.")

if __name__ == "__main__":
    main()
