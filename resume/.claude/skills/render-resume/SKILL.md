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

---

## Step 1 — Run the renderer

HTML generation and PDF conversion are handled by `.claude/tools/render_resume.py`. Run:

```bash
BASE="resume-${ARGUMENTS:-rendered}"
python3 .claude/tools/render_resume.py resume-base.json "${BASE}.html"
```

If the script exits with a non-zero code, read and report the stderr output to the user. If PDF generation fails, tell the user to open the HTML in Chrome and use File → Print → Save as PDF.

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

After both steps, report the paths of the HTML and PDF files.
