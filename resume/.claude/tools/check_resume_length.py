#!/usr/bin/env python3
"""
check_resume_length.py — Estimate whether a resume JSON will fit on one A4 page.

Usage:
    python check_resume_length.py <input.json> [--verbose]

Exit codes:
    0 — GREEN or AMBER (safe or borderline)
    1 — RED (definitely over budget; trim before rendering)

Layout model (Georgia 9pt, A4, 0.65cm margins, line-height 1.18):
  - CHARS_PER_LINE: ~110 chars fit per line before wrapping (empirical)
  - bullet_lu = max(1.0, len(text) / CHARS_PER_LINE)
    Using float (not ceil) because Georgia wrap spillover is usually thin;
    ceil() massively over-counts bullets just past a line boundary.

Calibration against 9 real renders:
  1-page renders: 57.8, 66.0, 67.5, 68.8, 69.3, 72.8, 78.5  (min 57.8, max 78.5)
  2-page renders: 73.3, 73.6

Thresholds:
  < 70   GREEN  — confidently fits; render PDF directly
  70–78  AMBER  — likely fits but borderline; render HTML first, check visually
  > 78   RED    — definitely 2+ pages; trim bullet lines before rendering

Rule of thumb for writing bullets:
  - Prefer ≤ 100 chars per bullet (one clean line, zero wrap risk)
  - Accept up to 200 chars per bullet (2-liner)
  - Avoid > 200 chars — contributes 2+ LU and quickly blows the budget
"""

import json
import math
import sys
from pathlib import Path

CHARS_PER_LINE = 110
GREEN_MAX = 70.0
RED_MIN = 78.0


def bullet_lu(text: str) -> float:
    return max(1.0, len(text) / CHARS_PER_LINE)


def estimate(data: dict) -> tuple[float, list[str]]:
    lu = 0.0
    breakdown = []

    lu += 4.0
    breakdown.append(f"  header block:          4.0 LU")

    summary = data.get("summary", "")
    if summary:
        lu += 2.0
        s_lu = max(1.0, len(summary) / CHARS_PER_LINE) + 0.3
        lu += s_lu
        breakdown.append(f"  Summary heading:       2.0 LU")
        breakdown.append(f"  Summary text ({len(summary)} chars): {s_lu:.1f} LU")

    experience = data.get("experience", [])
    if experience:
        lu += 2.0
        breakdown.append(f"  Experience heading:    2.0 LU")
    for job in experience:
        lu += 2.0
        entry_lu = sum(bullet_lu(b) for b in job.get("bullets", []))
        lu += entry_lu + 0.3
        breakdown.append(
            f"  {job.get('company','?')[:25]:<25} {2 + entry_lu + 0.3:.1f} LU"
            f"  ({len(job.get('bullets',[]))} bullets)"
        )

    education = data.get("education", [])
    if education:
        lu += 2.0
        breakdown.append(f"  Education heading:     2.0 LU")
    for edu in education:
        lu += 2.0
        entry_lu = sum(bullet_lu(b) for b in edu.get("bullets", []))
        lu += entry_lu + 0.3
        breakdown.append(
            f"  {edu.get('institution','?')[:25]:<25} {2 + entry_lu + 0.3:.1f} LU"
        )

    community = data.get("community", [])
    if community:
        lu += 2.0
        breakdown.append(f"  Community heading:     2.0 LU")
    for item in community:
        lu += 2.0
        entry_lu = sum(bullet_lu(b) for b in item.get("bullets", []))
        lu += entry_lu + 0.3
        breakdown.append(
            f"  {item.get('organisation','?')[:25]:<25} {2 + entry_lu + 0.3:.1f} LU"
        )

    skills = data.get("skills", {})
    tech = skills.get("technical", [])
    certs = skills.get("certifications", [])
    langs = skills.get("languages", [])
    if tech or certs or langs:
        lu += 2.0
        breakdown.append(f"  Skills heading:        2.0 LU")
    skills_lu = len(tech)
    if certs:
        cert_str = " · ".join(certs)
        skills_lu += max(1.0, len(cert_str) / CHARS_PER_LINE)
    if langs:
        skills_lu += 1
    lu += skills_lu
    breakdown.append(f"  Skills rows:           {skills_lu:.1f} LU")

    return lu, breakdown


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if not args:
        print("Usage: check_resume_length.py <input.json> [--verbose]", file=sys.stderr)
        sys.exit(1)

    path = Path(args[0])
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text(encoding="utf-8"))
    total, breakdown = estimate(data)

    if total < GREEN_MAX:
        status = "GREEN  — render PDF directly"
        code = 0
    elif total <= RED_MIN:
        status = "AMBER  — render HTML first and check visually before PDF"
        code = 0
    else:
        status = "RED    — trim bullet lines before rendering"
        code = 1

    print(f"Estimated: {total:.1f} LU  →  {status}")
    if verbose or code == 1:
        print(f"\nThresholds: GREEN < {GREEN_MAX}  |  AMBER {GREEN_MAX}–{RED_MIN}  |  RED > {RED_MIN}")
        print("\nBreakdown:")
        for line in breakdown:
            print(line)
    if code == 1:
        over = total - RED_MIN
        print(f"\n  Trim ~{math.ceil(over)} bullet-line(s) before rendering.")
        print(f"  Tip: shorten any bullet > 110 chars (each 110 chars = 1 LU).")

    sys.exit(code)


if __name__ == "__main__":
    main()
