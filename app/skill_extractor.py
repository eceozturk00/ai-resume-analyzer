from __future__ import annotations
import re
from typing import Dict, List, Tuple


SKILL_MAP: Dict[str, List[str]] = {
    "Python": [r"\bpython\b"],
    "C/C++": [r"\bc\+\+\b", r"\bc\b(?!#)"],
    "Java": [r"\bjava\b"],
    "SQL": [r"\bsql\b", r"\bmysql\b", r"\bpostgres\b", r"\bsqlite\b"],
    "Git": [r"\bgit\b", r"\bgithub\b"],
    "Linux": [r"\blinux\b", r"\bbash\b", r"\bshell\b"],
    "Flask": [r"\bflask\b"],
    "FastAPI": [r"\bfastapi\b"],
    "REST API": [r"\brest\b", r"\bapi\b"],
    "Docker": [r"\bdocker\b", r"\bcompose\b"],
    "Pandas": [r"\bpandas\b"],
    "NumPy": [r"\bnumpy\b"],
    "Matplotlib": [r"\bmatplotlib\b"],
    "NLP": [r"\bnlp\b", r"\btokenization\b", r"\bkeyword extraction\b"],
    "Machine Learning": [r"\bmachine learning\b", r"\bml\b", r"\bclassification\b", r"\bregression\b"],
    "Computer Networks": [r"\bnetwork\b", r"\btcp/ip\b", r"\bhttp\b", r"\bosi\b"],
    "Microcontrollers": [r"\barduino\b", r"\bmicrocontroller\b", r"\bembedded\b"],
}

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

def extract_skills(text: str) -> List[str]:
    t = normalize(text)
    found = []
    for skill, patterns in SKILL_MAP.items():
        for pat in patterns:
            if re.search(pat, t):
                found.append(skill)
                break
    return sorted(set(found))

def score_match(resume_skills: List[str], job_skills: List[str]) -> Tuple[int, List[str], List[str]]:
    rs = set(resume_skills)
    js = set(job_skills)
    matched = sorted(rs & js)
    missing = sorted(js - rs)
    score = 0 if not js else int((len(matched) / len(js)) * 100)
    return score, matched, missing

def extract_job_skills(job_text: str) -> List[str]:
    
    return extract_skills(job_text)
