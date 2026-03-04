from __future__ import annotations
from dataclasses import dataclass
from typing import List
from .skill_extractor import extract_skills, extract_job_skills, score_match

@dataclass
class MatchResult:
    score: int
    resume_skills: List[str]
    job_skills: List[str]
    matched: List[str]
    missing: List[str]

def match_resume_to_job(resume_text: str, job_text: str) -> MatchResult:
    rskills = extract_skills(resume_text)
    jskills = extract_job_skills(job_text)
    score, matched, missing = score_match(rskills, jskills)
    return MatchResult(score=score, resume_skills=rskills, job_skills=jskills, matched=matched, missing=missing)
