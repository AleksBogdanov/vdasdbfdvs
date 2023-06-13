from PyPDF2 import PdfReader


def pdf_to_string(pdf_file) -> str:
    """Extract the pdf and load it to string"""
    text = ''
    pdf_reader = PdfReader(pdf_file)  # Load the pdf
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text