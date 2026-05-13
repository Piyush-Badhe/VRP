import fitz
import pdfplumber
from docx import Document


def extract_pdf_text(file):
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception:
        file.seek(0)

        pdf = fitz.open(stream=file.read(), filetype="pdf")

        for page in pdf:
            text += page.get_text()

    return text


def extract_docx_text(file):
    document = Document(file)

    paragraphs = []

    for para in document.paragraphs:
        if para.text.strip():
            paragraphs.append(para.text)

    return "\n".join(paragraphs)


def extract_txt_text(file):
    return file.read().decode("utf-8")


def extract_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)

    if file_name.endswith(".docx"):
        return extract_docx_text(uploaded_file)

    if file_name.endswith(".txt"):
        return extract_txt_text(uploaded_file)

    return ""