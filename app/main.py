from __future__ import annotations
import argparse
from datetime import datetime

from .resume_parser import extract_text
from .job_matcher import match_resume_to_job
from .report import save_json, save_chart

def main():
    parser = argparse.ArgumentParser(description="AI Resume Analyzer (PDF/DOCX)")
    parser.add_argument("--resume", required=True, help="Path to resume .pdf or .docx")
    parser.add_argument("--job", required=True, help="Path to job description .txt")
    parser.add_argument("--outdir", default="reports", help="Output directory")
    args = parser.parse_args()

    resume_text = extract_text(args.resume)
    with open(args.job, "r", encoding="utf-8") as f:
        job_text = f.read()

    result = match_resume_to_job(resume_text, job_text)

    report = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "resume_skills": result.resume_skills,
        "job_skills": result.job_skills,
        "matched": result.matched,
        "missing": result.missing,
        "score": result.score
    }

    json_path = f"{args.outdir}/report.json"
    chart_path = f"{args.outdir}/report.png"
    save_json(report, json_path)
    save_chart(result.score, len(result.matched), len(result.missing), chart_path)

    print(" Done!")
    print(f"- Score: {result.score}/100")
    print(f"- JSON:  {json_path}")
    print(f"- Chart: {chart_path}")
    print(f"- Matched: {result.matched}")
    print(f"- Missing: {result.missing}")

if __name__ == "__main__":
    main()
