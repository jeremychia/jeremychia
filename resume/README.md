# Resume

## How it works

`resume-base.json` is the single source of truth. All skills read from it and produce output files — never edit the HTML or PDF directly.

Two Claude Code skills are available (run them from inside this `resume/` directory):

---

## `/render-resume` — generate a PDF from the base resume

Renders `resume-base.json` into a clean, ATS-optimised HTML + PDF in a Word-document style.

```
/render-resume <name>
```

**Example:**
```
/render-resume base
```
Outputs: `resume-base.html`, `resume-base.pdf`

Use this when you want a generic copy not tailored to a specific role.

---

## `/adapt-resume` — tailor the resume to a job posting

Fetches a job posting URL, adapts the resume content to match, and outputs a tailored JSON, HTML, and PDF.

```
/adapt-resume <job-posting-url>
```

**Example:**
```
/adapt-resume https://www.lego.com/de-de/careers/job/senior-analytics-engineer-...
```

Creates a folder per application under `applications/`, named by date, company, and job title:
```
applications/
  2026-04-08_lego_senior-analytics-engineer/
    2026-04-08_lego_senior-analytics-engineer.json
    2026-04-08_lego_senior-analytics-engineer.html
    2026-04-08_lego_senior-analytics-engineer.pdf
```

The skill will:
- Reorder and lightly rephrase bullets to match the JD's priorities
- Rewrite the summary to mirror the JD's language
- Reorder skill categories so the most relevant appear first
- Report what was adapted and flag any JD requirements not covered by the base resume

Facts, dates, and numbers are never changed.

---

## Updating the base resume

Edit `resume-base.json` directly. Key fields:

| Field | Purpose |
|---|---|
| `summary` | The professional summary paragraph |
| `experience[].bullets` | Bullet points per role — order matters for `/render-resume` |
| `skills.technical` | Ordered list of skill categories |
| `skills.certifications` | Certifications list |
| `pillHighlights` | Tags shown in the interactive HTML version only |

After editing, run `/render-resume base` to regenerate the base PDF.

---

## Prerequisites

- **Chrome** must be installed at `/Applications/Google Chrome.app` for PDF generation. If not found, the skill will output the HTML and ask you to print it manually via File → Print → Save as PDF.
- Skills require Claude Code to be running inside this `resume/` directory.
