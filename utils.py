import fitz

def extract_text_from_pdf(file_path):
    """
    Extract text from pdf file.

    Args:
        file_path: the path of pdf file
    """
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text
