from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_09" / "pdfs"
DEST = ROOT / "output" / "project_09" / "extracted_text.txt"

def main():
    sections = []
    for path in sorted(SOURCE.glob("*.pdf")):
        reader = PdfReader(path)
        pieces = [page.extract_text() or "" for page in reader.pages]
        sections.append(f"FILE: {path.name}\n" + "\n".join(pieces))
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text("\n\n---\n\n".join(sections), encoding="utf-8")
    print(f"Extracted text from {len(sections)} PDFs. Scanned images need OCR.")

if __name__ == "__main__":
    main()
