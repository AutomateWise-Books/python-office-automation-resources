from pathlib import Path
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "samples" / "project_08" / "pdfs"
DEST = ROOT / "output" / "project_08" / "combined.pdf"

def main():
    writer = PdfWriter()
    files = sorted(SOURCE.glob("*.pdf"))
    if not files:
        raise FileNotFoundError("No PDF sample files found")
    for path in files:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with DEST.open("wb") as handle:
        writer.write(handle)
    print(f"Combined {len(files)} PDFs into {len(writer.pages)} pages.")

if __name__ == "__main__":
    main()
