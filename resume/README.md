# Resume

## How it works

`resume-base.json` is the single source of truth for resume content. `profile/` is the source of truth for who you are, what you want, and why. Skills read from both — never edit the HTML or PDF directly.

Three Claude Code skills are available (run them from inside this `resume/` directory):

---

## `/adapt-resume` — tailor the resume and cover letter to a job posting

Fetches a job posting URL, adapts the resume content to match, generates a cover letter, and outputs a full application package.

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
    jd.md
    2026-04-08_lego_senior-analytics-engineer.json
    2026-04-08_lego_senior-analytics-engineer.html
    2026-04-08_lego_senior-analytics-engineer.pdf
    2026-04-08_lego_senior-analytics-engineer-cover-letter.md
```

The skill will:
- Analyse the JD for behavioural signals: fear/desire themes, seniority signals, ATS keywords, culture language
- Reorder and lightly rephrase bullets to match the JD's priorities
- Rewrite the summary to mirror the JD's language
- Reorder skill categories so the most relevant appear first
- Probe for gaps before rendering — wait for your response before producing files
- Generate a cover letter using your profile (motivations, values, narrative) that explains why this company, what you bring, where you have gaps and how you're addressing them, and what you're optimising for
- Report what was adapted and flag any JD requirements not covered

Facts, dates, and numbers are never changed.

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

## `/prep-recruiter-call` — prepare for a recruiter conversation

Generates a tailored preparation document for a specific job application, surfacing behavioural talking points, STAR stories, and research prompts based on the saved JD and adapted resume.

```
/prep-recruiter-call <application-folder-name>
```

**Example:**
```
/prep-recruiter-call 2026-04-08_lego_senior-analytics-engineer
```

Outputs `recruiter-prep.md` inside the application folder with:
- **Viability checklist** — the must-haves a recruiter will tick off, with coverage status
- **Peak moment** — single strongest achievement framed as a spoken sentence
- **STAR story prompts** — 3 themes from the JD with matched resume bullets
- **Company research** — data stack, team size, recent news, role-specific insight
- **Opening hook** — one specific sentence referencing a real company finding
- **Closing statement** — direct, confident, no marketing language
- **Culture-refining question** — one question that forces the recruiter to visualise you succeeding

Use this before recruiter calls or first-round interviews.

---

## Profile

The `profile/` directory holds the raw material about who you are and what you want. Skills read from these files — they are the source of genuine motivation, not something derivable from the resume.

| File | Purpose |
|---|---|
| `narrative.md` | Career arc in plain English — the "tell me about yourself" backbone |
| `motivations.md` | What energises you, what drains you, what you're optimising for in a next role |
| `values.md` | Non-negotiables and strong preferences — culture, management, work arrangement |
| `personality.md` | Assessment results + commentary on how they land in practice |
| `working-style.md` | How you work best — team size, management style, ambiguity, feedback |
| `star-stories.md` | Pre-written STAR stories organised by theme, reusable across interviews |
| `logistics.md` | Notice period, location, salary range, visa situation |

Keep these current. `/adapt-resume` uses `narrative.md`, `motivations.md`, and `values.md` to write the cover letter. `/prep-recruiter-call` uses `star-stories.md` (if present) to enrich STAR prompts.

See [`profile/README.md`](profile/README.md) for the full file/folder listing (including `verbose/`, `academic/`, `quarterly_reviews/`, and `sources/`) and for guidance on building an equivalent system from scratch.

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

## Job market analysis dashboard

Every application and classified JD feeds an interactive dashboard at `analysis/index.html`. See [`analysis/README.md`](analysis/README.md) for how to launch it and how the dataset is structured — quick start:

```bash
cd resume/analysis
python3 -m http.server 8765
open http://localhost:8765
```

Opening `index.html` directly (double-click / `file://`) will fail with a "Failed to fetch" error — it must be served over HTTP.

---

## Prerequisites

- **Chrome** must be installed at `/Applications/Google Chrome.app` for PDF generation. If not found, the skill will output the HTML and ask you to print it manually via File → Print → Save as PDF.
- Skills require Claude Code to be running inside this `resume/` directory.
