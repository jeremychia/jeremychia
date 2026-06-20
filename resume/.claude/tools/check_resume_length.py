#!/usr/bin/env python3
"""
check_resume_length.py — Estimate whether a resume JSON will fit on one A4 page.

Usage:
    python check_resume_length.py <input.json> [--verbose]

Exit codes:
    0 — GREEN or SPARSE (safe to render; SPARSE means add content)
    1 — AMBER or RED (trim or verify before finalising)

Layout model (Georgia 9pt, A4, 0.65cm margins, line-height 1.18):
  Uses per-character pixel widths from the actual Georgia TTF font.
  Falls back to average lowercase width (5.99px) for unmeasured characters.

  Line width: A4 197mm usable × 96dpi/25.4 = 744.5px body.
              Bullet list-indent 1.1em at 12px = 13.2px → effective 731.4px per bullet.
  Page capacity: A4 284mm usable height / (12px × 1.18 line-height) ≈ 75.8 physical lines.

  Each section heading counts as 2.0 LU (text line + rule + spacing).
  Each job/edu/community entry has 2.0 LU overhead (company + title rows) + 0.3 LU gap.
  Each bullet costs ceil(pixel_width / 731.4) LU; orphan adds +0.3 LU.

Orphan detection:
  A bullet whose last line is under 40% of the line width wastes space and looks bad.
  Orphans are penalised +0.3 LU and flagged in verbose output.
  Fix by shortening the bullet until it fits on one line, or extending it until the
  second line is at least 40% full.

Thresholds:
  < 63   SPARSE — page will have significant whitespace; restore trimmed bullets
  63–73  TARGET — optimal fill; render directly
  < 74   GREEN  — safe to render PDF directly
  74–80  AMBER  — render HTML first, verify page count, then PDF
  > 80   RED    — trim required before any render

Font location: /System/Library/Fonts/Supplemental/Georgia.ttf (macOS default)
If the font is not found, falls back to a flat 110 chars/line estimate.
"""

import json
import math
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Georgia 9pt character widths at 96dpi (px)
# Generated from /System/Library/Fonts/Supplemental/Georgia.ttf
# Font size: 9pt × 96dpi / 72 = 12px; scale = 12 / 2048 (units per em)
# ---------------------------------------------------------------------------
GEORGIA_WIDTHS: dict[int, float] = {
    32: 2.8945,   # ' '
    33: 3.9727,   # '!'
    37: 9.8086,   # '%'
    38: 8.5254,   # '&'
    40: 4.5000,   # '('
    41: 4.5000,   # ')'
    43: 7.7168,   # '+'
    44: 3.2344,   # ','
    45: 4.4883,   # '-'
    46: 3.2344,   # '.'
    47: 5.6250,   # '/'
    48: 7.3652,   # '0'
    49: 5.1562,   # '1'
    50: 6.7031,   # '2'
    51: 6.6211,   # '3'
    52: 6.7793,   # '4'
    53: 6.3398,   # '5'
    54: 6.7910,   # '6'
    55: 6.0293,   # '7'
    56: 7.1543,   # '8'
    57: 6.7910,   # '9'
    58: 3.7500,   # ':'
    59: 3.7500,   # ';'
    60: 7.7168,   # '<'
    62: 7.7168,   # '>'
    63: 5.7422,   # '?'
    65: 8.0508,   # 'A'
    66: 7.8457,   # 'B'
    67: 7.7051,   # 'C'
    68: 8.9883,   # 'D'
    69: 7.8398,   # 'E'
    70: 7.1895,   # 'F'
    71: 8.7012,   # 'G'
    72: 9.7793,   # 'H'
    73: 4.6758,   # 'I'
    74: 6.2109,   # 'J'
    75: 8.3320,   # 'K'
    76: 7.2422,   # 'L'
    77: 11.1270,  # 'M'
    78: 9.2051,   # 'N'
    79: 8.9297,   # 'O'
    80: 7.3184,   # 'P'
    81: 8.9297,   # 'Q'
    82: 8.4199,   # 'R'
    83: 6.7324,   # 'S'
    84: 7.4238,   # 'T'
    85: 9.0762,   # 'U'
    86: 7.9980,   # 'V'
    87: 11.7070,  # 'W'
    88: 8.5254,   # 'X'
    89: 7.3828,   # 'Y'
    90: 7.2188,   # 'Z'
    91: 4.5000,   # '['
    93: 4.5000,   # ']'
    95: 7.7168,   # '_'
    97: 6.0469,   # 'a'
    98: 6.7207,   # 'b'
    99: 5.4492,   # 'c'
    100: 6.8906,  # 'd'
    101: 5.8008,  # 'e'
    102: 3.9023,  # 'f'
    103: 6.1113,  # 'g'
    104: 6.9844,  # 'h'
    105: 3.5156,  # 'i'
    106: 3.5039,  # 'j'
    107: 6.4277,  # 'k'
    108: 3.4336,  # 'l'
    109: 10.5703, # 'm'
    110: 7.0898,  # 'n'
    111: 6.4688,  # 'o'
    112: 6.8555,  # 'p'
    113: 6.7148,  # 'q'
    114: 4.9160,  # 'r'
    115: 5.1855,  # 's'
    116: 4.1426,  # 't'
    117: 6.9023,  # 'u'
    118: 5.9590,  # 'v'
    119: 8.8477,  # 'w'
    120: 6.0586,  # 'x'
    121: 5.9062,  # 'y'
    122: 5.3262,  # 'z'
    232: 5.8008,  # 'è'
    233: 5.8008,  # 'é'
    234: 5.8008,  # 'ê'
    8212: 10.2832, # '—'
    8217: 2.7188,  # '''
    8364: 7.7051,  # '€'
}

FALLBACK_WIDTH = 5.99  # average lowercase letter width

# Layout constants
EFFECTIVE_WIDTH_PX = 731.4  # usable bullet text width (A4 minus margins minus indent)
ORPHAN_RATIO = 0.40          # last line under 40% of line width = orphan

# Thresholds (LU)
SPARSE_MAX = 63.0
GREEN_MAX = 74.0
RED_MIN = 81.0


def char_width_px(ch: str) -> float:
    return GEORGIA_WIDTHS.get(ord(ch), FALLBACK_WIDTH)


def text_width_px(s: str) -> float:
    return sum(char_width_px(c) for c in s)


def bullet_lu(text: str) -> tuple[float, bool]:
    """Return (lu_cost, is_orphan) using pixel-accurate Georgia metrics."""
    px = text_width_px(text)
    lines = max(1, math.ceil(px / EFFECTIVE_WIDTH_PX))
    last_line_px = px % EFFECTIVE_WIDTH_PX or EFFECTIVE_WIDTH_PX
    orphan = (lines > 1) and (last_line_px < EFFECTIVE_WIDTH_PX * ORPHAN_RATIO)
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
        s_px = text_width_px(summary)
        s_lu = max(1.0, float(math.ceil(s_px / EFFECTIVE_WIDTH_PX)))
        lu += s_lu
        breakdown.append("  Summary heading:       2.0 LU")
        breakdown.append(f"  Summary text ({len(summary)} chars, {s_px:.0f}px): {s_lu:.1f} LU")

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
                    f"  [{job.get('company','?')[:18]}] {len(b)}ch/{text_width_px(b):.0f}px"
                    f" — orphan: \"{b[:55]}...\""
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
                    f"  [{edu.get('institution','?')[:18]}] {len(b)}ch/{text_width_px(b):.0f}px"
                    f" — orphan: \"{b[:55]}...\""
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
                    f"  [{item.get('organisation','?')[:18]}] {len(b)}ch/{text_width_px(b):.0f}px"
                    f" — orphan: \"{b[:55]}...\""
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
    skills_lu = float(len(tech))
    if certs:
        cert_str = " · ".join(certs)
        skills_lu += max(1.0, float(math.ceil(text_width_px(cert_str) / EFFECTIVE_WIDTH_PX)))
    if langs:
        skills_lu += 1.0
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

    if total < SPARSE_MAX:
        status = "SPARSE — page underfilled; restore trimmed bullets or expand existing ones"
        code = 0
    elif total < GREEN_MAX:
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
        print(
            f"\nThresholds: SPARSE < {SPARSE_MAX}"
            f"  |  GREEN < {GREEN_MAX}"
            f"  |  AMBER {GREEN_MAX}–{RED_MIN}"
            f"  |  RED > {RED_MIN}"
        )
        print("\nBreakdown:")
        for line in breakdown:
            print(line)

    if orphan_report:
        print(
            f"\nOrphan bullets ({len(orphan_report)} found — each costs +0.3 LU):"
            f"\n  Fix: shorten until pixel width fits in one line,"
            f" or extend until last line ≥ 40% full."
        )
        for line in orphan_report:
            print(line)

    if total < SPARSE_MAX:
        under = SPARSE_MAX - total
        print(f"\n  Page underfilled by ~{under:.1f} LU. Restore trimmed bullets or expand short ones.")
    elif code == 1 and total > RED_MIN:
        over = total - RED_MIN
        print(f"\n  Must trim ~{math.ceil(over)} LU before rendering.")
        print(f"  Tip: long bullets (>731px) wrap to 2 lines. Trim until pixel width < 731px.")
    elif code == 1:
        print(f"\n  Render HTML first and check page count before generating PDF.")

    sys.exit(code)


if __name__ == "__main__":
    main()
