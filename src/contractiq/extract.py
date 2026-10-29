from pathlib import Path
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    """Return all the text in a PDF as one string."""
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)

if __name__ == "__main__":
    import sys

    text = extract_text_from_pdf(sys.argv[1])
    print(text[:1000])        