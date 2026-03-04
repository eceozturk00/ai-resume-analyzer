# AI Resume Analyzer (Python)

A lightweight **NLP-style** resume analyzer that:
- extracts skills from **PDF/DOCX** resumes
- extracts required skills from a **job description**
- computes a match score + skill gap
- exports a **JSON report** and a **chart**

## Tech Stack
Python, pdfplumber, python-docx, matplotlib

## Run
```bash
pip install -r requirements.txt
python -m app.main --resume resume.pdf --job job.txt --outdir reports
