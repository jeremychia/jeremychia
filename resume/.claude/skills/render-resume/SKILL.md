---
name: render-resume
description: Renders resume-base.json into a one-page ATS-optimised HTML and PDF, ready to attach to job applications
allowed-tools: Read Write Bash
---

Read `resume-base.json` from the current directory, write an HTML file, then convert it to PDF using Chrome headless.

**Output filenames:**
- HTML: `resume-$ARGUMENTS.html`
- PDF:  `resume-$ARGUMENTS.pdf`

If no argument is given, use `resume-rendered` as the base name.

Work through these steps **in order**.

---

## Step 1 — Read and validate the source JSON

Read `resume-base.json` now — do not proceed until the read completes.

Before rendering, run a quick sanity check:
- [ ] `summary` field exists and is non-empty
- [ ] `experience` array has at least one entry with `bullets`
- [ ] `header` contains `name` and at least one contact field
- [ ] No `null` or empty-string values in required fields

If any check fails, report the specific field and stop — do not render a broken file.

---

## Step 2 — Run the renderer

HTML generation and PDF conversion are handled by `.claude/tools/render_resume.py`. Run:

```bash
BASE="resume-${ARGUMENTS:-rendered}"
python3 .claude/tools/render_resume.py resume-base.json "${BASE}.html"
```

If the script exits with a non-zero code, read and report the stderr output to the user. If PDF generation fails, tell the user to open the HTML in Chrome and use File → Print → Save as PDF.

---

## Step 3 — Verify output

After the renderer completes:

```bash
BASE="resume-${ARGUMENTS:-rendered}"
# Check files exist
ls -lh "${BASE}.html" "${BASE}.pdf" 2>&1
# Check page count
pdfinfo "${BASE}.pdf" 2>/dev/null | grep "Pages:" || echo "pdfinfo not available — open PDF manually to verify page count"
```

- [ ] HTML file exists and is non-zero size
- [ ] PDF file exists and is non-zero size
- [ ] Page count is exactly 1 — if > 1, report that the base resume needs trimming before this render will be usable

If page count > 1, tell the user which sections are candidates for trimming (longest experience section, oldest roles, community section).

---

## Data mapping

- `header` → name, location, contact links (skip `tagline` in ATS version)
- `summary` → plain `<p>` under "Summary" section
- `experience[]` → "Professional Experience" (already reverse-chron)
- `education[]` → "Education"
- `community[]` → "Community and Volunteering"
- `skills.technical[]` → "Skills", one line per category
- `skills.certifications[]` → "Certifications" line
- `skills.languages[]` → "Languages" line (format: `Language (Level)`)
- Omit `pillHighlights` entirely

---

## Step 4 — Report

Tell the user:
- Paths of the HTML and PDF files
- Page count
- Any validation failures from Step 1 or Step 3
