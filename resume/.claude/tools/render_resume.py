#!/usr/bin/env python3
"""
render_resume.py  —  Convert resume-*.json → HTML → PDF

Usage:
    python render_resume.py <input.json> <output.html> [--no-pdf]

The script reads a resume JSON file (base or adapted) and writes a
self-contained, ATS-safe HTML file, then attempts to convert it to PDF
using Chrome/Chromium headless.

Exit codes:
    0  — HTML (and PDF if requested) created successfully
    1  — input JSON not found or invalid
    2  — HTML write failed
"""

import json
import subprocess
import sys
from html import escape
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _esc(text: str) -> str:
    return escape(str(text), quote=False)


def _link(url: str, label: str) -> str:
    return f'<a href="{_esc(url)}" style="color:#000;text-decoration:none;">{_esc(label)}</a>'


def _section_heading(title: str) -> str:
    return (
        f'<p style="font-size:9.5pt;font-weight:bold;letter-spacing:0.1em;'
        f'text-transform:uppercase;margin:7px 0 0;">{_esc(title)}</p>'
        f'<hr style="margin:2px 0 4px;border:none;border-top:1px solid #000;">'
    )


def _flex_row(left_html: str, right_html: str) -> str:
    return (
        f'<div style="display:flex;justify-content:space-between;align-items:baseline;">'
        f'{left_html}<span style="white-space:nowrap;">{right_html}</span></div>'
    )


def _bullets(items: list[str]) -> str:
    lis = "".join(
        f'<li style="margin-bottom:1px;font-size:9pt;">{_esc(b)}</li>' for b in items if b
    )
    return f'<ul style="list-style-type:disc;margin:2px 0;padding-left:1.1em;">{lis}</ul>'


# ---------------------------------------------------------------------------
# Section renderers
# ---------------------------------------------------------------------------

def _render_header(header: dict) -> str:
    c = header.get("contact", {})
    name = _esc(header.get("name", ""))
    location = _esc(header.get("location", ""))

    links = []
    if c.get("phone"):
        links.append(_esc(c["phone"]))
    if c.get("email"):
        links.append(_link(f'mailto:{c["email"]}', c["email"]))
    if c.get("github"):
        gh = c["github"]
        links.append(_link(gh.get("url", ""), gh.get("label", gh.get("url", ""))))
    if c.get("linkedin"):
        li = c["linkedin"]
        links.append(_link(li.get("url", ""), li.get("label", li.get("url", ""))))

    contact_line = " &middot; ".join(links)

    return f"""
<div style="text-align:center;margin-bottom:6px;">
  <p style="font-size:14pt;font-weight:bold;letter-spacing:0.1em;
             text-transform:uppercase;margin:0 0 2px;">{name}</p>
  <p style="font-size:8.5pt;margin:1px 0;">{location}</p>
  <p style="font-size:8.5pt;margin:1px 0;">{contact_line}</p>
</div>"""


def _render_summary(summary: str) -> str:
    if not summary:
        return ""
    return (
        _section_heading("Summary")
        + f'<p style="margin:0 0 4px;font-size:9pt;">{_esc(summary)}</p>'
    )


def _render_experience(experience: list[dict]) -> str:
    parts = [_section_heading("Professional Experience")]
    for job in experience:
        date_range = f'{_esc(job.get("startDate",""))} – {_esc(job.get("endDate",""))}'
        loc_date = f'<span style="font-size:8.5pt;white-space:nowrap;">{_esc(job.get("location",""))} &nbsp;|&nbsp; {date_range}</span>'
        left = f'<strong style="font-size:9.5pt;">{_esc(job.get("company",""))}</strong>'
        row1 = _flex_row(left, loc_date)
        row2 = f'<div style="font-style:italic;font-size:9pt;margin:1px 0 2px;">{_esc(job.get("title",""))}</div>'
        entry = row1 + "\n" + row2
        if job.get("bullets"):
            entry += "\n" + _bullets(job["bullets"])
        parts.append(f'<div style="margin-bottom:4px;">{entry}</div>')
    return "\n".join(parts)


def _render_education(education: list[dict]) -> str:
    parts = [_section_heading("Education")]
    for edu in education:
        date_range = f'{_esc(edu.get("startDate",""))} – {_esc(edu.get("endDate",""))}'
        loc_date = f'<span style="font-size:8.5pt;white-space:nowrap;">{_esc(edu.get("location",""))} &nbsp;|&nbsp; {date_range}</span>'
        left = f'<strong style="font-size:9.5pt;">{_esc(edu.get("institution",""))}</strong>'
        row1 = _flex_row(left, loc_date)
        row2 = f'<div style="font-style:italic;font-size:9pt;margin:1px 0 2px;">{_esc(edu.get("degree",""))}</div>'
        entry = row1 + "\n" + row2
        if edu.get("bullets"):
            entry += "\n" + _bullets(edu["bullets"])
        parts.append(f'<div style="margin-bottom:4px;">{entry}</div>')
    return "\n".join(parts)


def _render_community(community: list[dict]) -> str:
    if not community:
        return ""
    parts = [_section_heading("Community and Volunteering")]
    for item in community:
        date_range = f'{_esc(item.get("startDate",""))} – {_esc(item.get("endDate",""))}'
        loc_date = f'<span style="font-size:8.5pt;white-space:nowrap;">{_esc(item.get("location",""))} &nbsp;|&nbsp; {date_range}</span>'
        left = f'<strong style="font-size:9.5pt;">{_esc(item.get("organisation",""))}</strong>'
        row1 = _flex_row(left, loc_date)
        row2 = f'<div style="font-style:italic;font-size:9pt;margin:1px 0 2px;">{_esc(item.get("title",""))}</div>'
        entry = row1 + "\n" + row2
        if item.get("bullets"):
            entry += "\n" + _bullets(item["bullets"])
        parts.append(f'<div style="margin-bottom:4px;">{entry}</div>')
    return "\n".join(parts)


def _render_skills(skills: dict) -> str:
    parts = [_section_heading("Skills")]

    for cat in skills.get("technical", []):
        name = _esc(cat.get("category", ""))
        items = ", ".join(_esc(i) for i in cat.get("items", []))
        parts.append(f'<p style="margin:2px 0;font-size:9pt;"><strong>{name}:</strong> {items}</p>')

    certs = skills.get("certifications", [])
    if certs:
        cert_str = " &middot; ".join(_esc(c) for c in certs)
        parts.append(f'<p style="margin:2px 0;font-size:9pt;"><strong>Certifications:</strong> {cert_str}</p>')

    langs = skills.get("languages", [])
    if langs:
        lang_str = ", ".join(
            f'{_esc(l.get("language",""))} ({_esc(l.get("level",""))})'
            for l in langs
        )
        parts.append(f'<p style="margin:2px 0;font-size:9pt;"><strong>Languages:</strong> {lang_str}</p>')

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Full document
# ---------------------------------------------------------------------------

def render_html(data: dict) -> str:
    body_parts = [
        _render_header(data.get("header", {})),
        _render_summary(data.get("summary", "")),
        _render_experience(data.get("experience", [])),
        _render_education(data.get("education", [])),
        _render_community(data.get("community", [])),
        _render_skills(data.get("skills", {})),
    ]
    body = "\n".join(p for p in body_parts if p)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{_esc(data.get("header", {}).get("name", "Resume"))}</title>
<style>
  @page {{
    size: A4;
    margin: 0.65cm;
  }}
  @media print {{
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 9.5pt;
    line-height: 1.18;
    color: #000;
    background: #fff;
    max-width: 780px;
    margin: 0 auto;
    padding: 0;
  }}
  a {{ color: #000; text-decoration: none; }}
  p {{ margin: 0; }}
  ul {{ margin: 2px 0; padding-left: 1.1em; list-style-type: disc; }}
  li {{ margin-bottom: 1px; font-size: 9pt; }}
</style>
</head>
<body>
{body}
</body>
</html>"""


# ---------------------------------------------------------------------------
# PDF conversion
# ---------------------------------------------------------------------------

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "chromium-browser",
    "google-chrome",
    "chromium",
]


def find_chrome() -> str | None:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).is_file():
            return candidate
        result = subprocess.run(
            ["command", "-v", candidate], capture_output=True, text=True, shell=False
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    return None


def count_pdf_pages(pdf_path: Path) -> int | None:
    """Return page count using pdfinfo or pypdf, or None if unavailable."""
    try:
        result = subprocess.run(
            ["pdfinfo", str(pdf_path)], capture_output=True, text=True
        )
    except FileNotFoundError:
        result = None
    if result is not None and result.returncode == 0:
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                try:
                    return int(line.split(":", 1)[1].strip())
                except ValueError:
                    pass
    try:
        import pypdf  # type: ignore
        with open(pdf_path, "rb") as f:
            return len(pypdf.PdfReader(f).pages)
    except (ImportError, Exception):
        pass
    return None


def html_to_pdf(html_path: Path, pdf_path: Path) -> bool:
    chrome = find_chrome()
    if not chrome:
        print("  ⚠  No Chrome/Chromium found. Open the HTML in Chrome and print to PDF.", file=sys.stderr)
        return False

    cmd = [
        chrome,
        "--headless=new",
        f"--print-to-pdf={pdf_path.resolve()}",
        "--print-to-pdf-no-header-footer",
        "--no-margins",
        "--disable-gpu",
        "--paper-width=8.27",
        "--paper-height=11.69",
        str(html_path.resolve()),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if pdf_path.exists() and pdf_path.stat().st_size > 0:
        return True
    print(f"  ⚠  Chrome exited {result.returncode}. stderr:\n{result.stderr}", file=sys.stderr)
    return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]
    no_pdf = "--no-pdf" in args
    args = [a for a in args if not a.startswith("--")]

    if len(args) < 2:
        print("Usage: render_resume.py <input.json> <output.html> [--no-pdf]", file=sys.stderr)
        sys.exit(1)

    json_path = Path(args[0])
    html_path = Path(args[1])
    pdf_path = html_path.with_suffix(".pdf")

    # --- Read JSON ---
    if not json_path.exists():
        print(f"Error: {json_path} not found.", file=sys.stderr)
        sys.exit(1)
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON — {exc}", file=sys.stderr)
        sys.exit(1)

    # --- Write HTML ---
    html_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        html_path.write_text(render_html(data), encoding="utf-8")
        print(f"  ✓ HTML → {html_path}")
    except OSError as exc:
        print(f"Error writing HTML: {exc}", file=sys.stderr)
        sys.exit(2)

    # --- Write PDF ---
    if not no_pdf:
        ok = html_to_pdf(html_path, pdf_path)
        if ok:
            pages = count_pdf_pages(pdf_path)
            if pages is not None and pages > 1:
                print(f"  ✗ PDF  → {pdf_path}  ⚠  {pages} PAGES — trim before submitting!", file=sys.stderr)
            else:
                suffix = f" ({pages}p)" if pages else ""
                print(f"  ✓ PDF  → {pdf_path}{suffix}")
        else:
            print(f"  ✗ PDF  → failed (see above)")


if __name__ == "__main__":
    main()
