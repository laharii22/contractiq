from contractiq.extract import extract_text_from_pdf
from contractiq.llm_client import analyse_contract


def analyse_pdf(pdf_path: str) -> str:
    # Helps in extracting text from the selected PDF
    text = extract_text_from_pdf(pdf_path)

    # Helps in analysing the extracted contract text
    result = analyse_contract(text)

    return result