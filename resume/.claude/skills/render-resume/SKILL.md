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

## Step 1 — Write the HTML file

Produce a single self-contained HTML file with inline CSS. The visual style must match a clean, ATS-friendly Word document:

### Page / typography
- White background, black text, no colours
- Font: Georgia or Times New Roman (serif); fallback to serif
- Font size: 10pt equivalent
- `@page { margin: 0.9cm; }`
- Body: `max-width: 780px; margin: 0 auto; padding: 0.5cm 1cm;`

### Header (centred)
- Name: bold, ~16pt, all caps, letter-spacing
- Line 2: phone · email (linked) · GitHub (linked) · LinkedIn (linked) — separated by ` &middot; `
- Line 3: location

### Section headings
- ALL CAPS, bold, font-size 10pt, letter-spacing 0.1em
- Followed by a full-width `<hr style="margin: 2px 0 6px; border: none; border-top: 1px solid #000;">`
- No colour, no accent bar

### Experience / Education / Community entries
- Use a `<div style="display:flex; justify-content:space-between;">` for the company/date row only
- Company/institution: `<strong>`
- Role/degree: `<em>`
- Location and date range: right-aligned in the flex row
- Bullet list: `<ul style="list-style-type:disc; margin:3px 0; padding-left:1.2em;">`
- `<li style="margin-bottom:2px;">`

### Skills section
Render each `technical` category as a `<p>` with `<strong>Category:</strong> item1, item2, item3`.
Then certifications and languages the same way.

### ATS rules (must follow)
- No images, SVGs, tables, text boxes, or complex layouts in the main content (flex only on the company/date row)
- Section headings must use these exact strings: "Professional Experience", "Education", "Community and Volunteering", "Skills"
- All links use full URLs
- No `display:none` on any content
- No JavaScript
- Include `@page { size: A4; margin: 0.55cm; }` so Chrome headless renders A4 (it defaults to Letter, which is shorter)
- `@media print` must include `-webkit-print-color-adjust: exact; print-color-adjust: exact;` and suppress any URL/title headers Chrome might add via `@page { margin: 0.55cm; }` (the `--print-to-pdf-no-header-footer` flag handles this, but the CSS should not fight it)

---

## Step 2 — Convert HTML to PDF using Chrome headless

After writing the HTML file, run this Bash command:

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HTML="resume-$ARGUMENTS.html"
PDF="resume-$ARGUMENTS.pdf"

"$CHROME" \
  --headless=new \
  --print-to-pdf="$PDF" \
  --print-to-pdf-no-header-footer \
  --no-margins \
  --disable-gpu \
  --paper-width=8.27 --paper-height=11.69 \
  "$HTML" 2>/dev/null

echo "exit:$?"
```

If Chrome is not found at that path, try `/usr/bin/chromium-browser` or `chromium`. If none found, tell the user to open the HTML in Chrome and use File → Print → Save as PDF.

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
