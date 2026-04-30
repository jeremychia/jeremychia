#!/usr/bin/env python3
"""
check_resume_length.py — Estimate whether a resume JSON will fit on one A4 page.

Usage:
    python check_resume_length.py <input.json> [--verbose]

Exit codes:
    0 — GREEN (safe to render)
    1 — AMBER or RED (trim or verify before finalising)

Layout model (Georgia 9pt, A4, 0.65cm margins, line-height 1.18):
  - CHARS_PER_LINE: ~110 chars fit per line for body text; bullets have a list
    indent so effective width is slightly less, but 110 is used as the ceiling.
  - bullet_lu = ceil(len / CHARS_PER_LINE)  — physical line count.
    Using ceil (not float) because each wrap produces a real extra line on the page.

Orphan detection:
  A bullet that wraps such that the last line is under 40% of the line width is an
  "orphan" — it wastes space and looks bad. Orphan bullets are penalised +0.3 LU
  and reported in verbose output so they can be fixed.

  Orphan zone: (CHARS_PER_LINE + 1) to (CHARS_PER_LINE * 1.4) chars.
  Fix by: shortening to ≤ CHARS_PER_LINE chars, OR extending to ≥ 1.4× chars.

Thresholds (recalibrated for ceil+orphan model):
  < 70   GREEN  — confident one-page fit; render PDF directly
  70–77  AMBER  — borderline; render HTML, verify page count, then PDF
  > 77   RED    — trim required

  Orphan-free 69–70 LU reliably fits one A4 page because each LU maps to one
  physical line with no wasted space. The old float model at 70 LU could 2-page
  because undetected orphans added uncounted physical lines.

Rule of thumb for bullet writing:
  - ≤ 130 chars → 1 LU, clean single line. PREFERRED.
  - 155–220 chars → 2 LU, two well-filled lines. ACCEPTABLE (last line ≥ 40% full).
  - 111–154 chars → ORPHAN ZONE. Costs 2 LU + 0.3 penalty. AVOID.
  - > 220 chars → 3 LU. Too long.
"""

import json
import math
import sys
from pathlib import Path

CHARS_PER_LINE = 110
ORPHAN_RATIO = 0.40   # last line under 40% of line width = orphan
GREEN_MAX = 70.0
RED_MIN = 77.0


def bullet_lu(text: str) -> tuple[float, bool]:
    """Return (lu_cost, is_orphan). Uses ceil for physical line count."""
    n = len(text)
    lines = max(1, math.ceil(n / CHARS_PER_LINE))
    last_line = n % CHARS_PER_LINE or CHARS_PER_LINE
    orphan = (lines > 1) and (last_line < CHARS_PER_LINE * ORPHAN_RATIO)
    cost = float(lines) + (0.3 if orphan else 0.0)
    return cost, orphan


def estimate(data: dict) -> tuple[float, list[str], list[str]]:
    lu = 0.0
    breakdown = []
    orphan_report = []

    lu += 4.0
    breakdown.append("  header block:          4.0 LU")

    summary = data.get("summary", "")
    if summary:
        lu += 2.0
        s_lu = max(1.0, len(summary) / CHARS_PER_LINE) + 0.3
        lu += s_lu
        breakdown.append("  Summary heading:       2.0 LU")
        breakdown.append(f"  Summary text ({len(summary)} chars): {s_lu:.1f} LU")

    experience = data.get("experience", [])
    if experience:
        lu += 2.0
        breakdown.append("  Experience heading:    2.0 LU")
    for job in experience:
        lu += 2.0
        entry_lu = 0.0
        for b in job.get("bullets", []):
            cost, orphan = bullet_lu(b)
            entry_lu += cost
            if orphan:
                orphan_report.append(
                    f"  [{job.get('company','?')[:18]}] {len(b)} chars — orphan: \"{b[:60]}...\""
                )
        lu += entry_lu + 0.3
        breakdown.append(
            f"  {job.get('company','?')[:25]:<25} {2 + entry_lu + 0.3:.1f} LU"
            f"  ({len(job.get('bullets', []))} bullets)"
        )

    education = data.get("education", [])
    if education:
        lu += 2.0
        breakdown.append("  Education heading:     2.0 LU")
    for edu in education:
        lu += 2.0
        entry_lu = 0.0
        for b in edu.get("bullets", []):
            cost, orphan = bullet_lu(b)
            entry_lu += cost
            if orphan:
                orphan_report.append(
                    f"  [{edu.get('institution','?')[:18]}] {len(b)} chars — orphan: \"{b[:60]}...\""
                )
        lu += entry_lu + 0.3
        breakdown.append(
            f"  {edu.get('institution','?')[:25]:<25} {2 + entry_lu + 0.3:.1f} LU"
        )

    community = data.get("community", [])
    if community:
        lu += 2.0
        breakdown.append("  Community heading:     2.0 LU")
    for item in community:
        lu += 2.0
        entry_lu = 0.0
        for b in item.get("bullets", []):
            cost, orphan = bullet_lu(b)
            entry_lu += cost
            if orphan:
                orphan_report.append(
                    f"  [{item.get('organisation','?')[:18]}] {len(b)} chars — orphan: \"{b[:60]}...\""
                )
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
        breakdown.append("  Skills heading:        2.0 LU")
    skills_lu = len(tech)
    if certs:
        cert_str = " · ".join(certs)
        skills_lu += max(1.0, len(cert_str) / CHARS_PER_LINE)
    if langs:
        skills_lu += 1
    lu += skills_lu
    breakdown.append(f"  Skills rows:           {skills_lu:.1f} LU")

    return lu, breakdown, orphan_report


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
    total, breakdown, orphan_report = estimate(data)

    if total < GREEN_MAX:
        status = "GREEN  — render PDF directly"
        code = 0
    elif total <= RED_MIN:
        status = "AMBER  — render HTML first, verify page count, then PDF"
        code = 1
    else:
        status = "RED    — trim bullets before rendering"
        code = 1

    print(f"Estimated: {total:.1f} LU  →  {status}")

    if verbose or code == 1:
        print(f"\nThresholds: GREEN < {GREEN_MAX}  |  AMBER {GREEN_MAX}–{RED_MIN}  |  RED > {RED_MIN}")
        print("\nBreakdown:")
        for line in breakdown:
            print(line)

    if orphan_report:
        print(f"\nOrphan bullets ({len(orphan_report)} found — each costs +0.3 LU; fix to ≤ 105 or ≥ 145 chars):")
        for line in orphan_report:
            print(line)

    if code == 1 and total > RED_MIN:
        over = total - RED_MIN
        print(f"\n  Must trim ~{math.ceil(over)} LU before rendering.")
        print(f"  Tip: each bullet costs ceil(len / 110) LU. Target ≤ 105 chars (1 LU) or 145–200 chars (2 LU).")
    elif code == 1:
        print(f"\n  Render HTML first and check page count before generating PDF.")

    sys.exit(code)


if __name__ == "__main__":
    main()
