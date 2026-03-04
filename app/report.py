from __future__ import annotations
import json
import os
from typing import Dict, Any
import matplotlib.pyplot as plt

def save_json(report: Dict[str, Any], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

def save_chart(score: int, matched_count: int, missing_count: int, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    labels = ["Match Score", "Matched Skills", "Missing Skills"]
    values = [score, matched_count, missing_count]
    plt.figure()
    plt.bar(labels, values) 
    plt.title("Resume vs Job Match")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
