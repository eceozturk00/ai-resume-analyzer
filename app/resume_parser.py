from __future__ import annotations
from typing import Optional
import pdfplumber
from docx import Document

def extract_text(path: str) -> str:
    p = path.lower()
    if p.endswith(".pdf"):
        return _extract_pdf(path)
    if p.endswith(".docx"):
        return _extract_docx(path)
    raise ValueError("Unsupported file type. Use .pdf or .docx")

def _extract_pdf(path: str) -> str:
    parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text() or ""
            if txt.strip():
                parts.append(txt)
    return "\n".join(parts)

def _extract_docx(path: str) -> str:
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
