---
name: adapt-resume
description: Fetches a job posting URL, adapts resume-base.json to match the role, and outputs a tailored JSON, HTML, and PDF inside applications/{base-name}/
allowed-tools: WebFetch Read Write Bash
argument-hint: <job-posting-url>
---

`$ARGUMENTS` is a job posting URL. Run through these steps in order.

---

## Step 1 — Fetch and analyse the job posting

Fetch `$ARGUMENTS` with WebFetch. Do two layers of analysis:

### Layer A — Surface extraction
- **Company name** (slug: lowercase, hyphens)
- **Job title** (slug form)
- **Required skills and tools**
- **Preferred/bonus skills**
- **Domain context** — industry, team size, stack maturity

### Layer B — Behavioural and cognitive reading

**Signal ordering:** What is listed first in responsibilities/requirements is the top priority. Weight the resume to match that order.

**Repetition = fear or desire:** Any theme appearing 3+ times signals a pain point (fear) or critical need (desire). Surface resume content that directly addresses it.

**Seniority signals:** Phrases like "take ownership", "champion best practices", "translating to senior leadership" signal they want an autonomous IC. Lead the resume with outcomes and scale, not tasks.

**Loss aversion:** Compliance, governance, and reliability language signals fear of failure. Frame achievements as risk reduction and reliability wins, not just speed.

**Culture signals:** Personality language ("energetic", "pioneering", "bravery to challenge") describes who the hiring manager identifies with. Mirror subtly — no copy-paste.

**Absence signals:** What the JD omits is also informative. No mentorship = they want a strong IC. No stakeholder management = collaborator, not project manager.

**ATS keywords:** Extract 10–15 distinctive phrases likely used as ATS filters (not generics like "SQL"). These must appear verbatim in the resume.

Summarise as a short **behavioural insights** list to carry into Step 5.

Derive the base name: `YYYY-MM-DD_company_job-title` using today's date.

---

## Step 2 — Create the output folder

```bash
mkdir -p "applications/{base name}"
```

All output files go inside this folder:
- `applications/{base name}/jd.md`
- `applications/{base name}/{base name}.json`
- `applications/{base name}/{base name}.html`
- `applications/{base name}/{base name}.pdf`
- `applications/{base name}/{base name}-cover-letter.md`

---

## Step 3 — Save the JD as markdown

Write `applications/{base name}/jd.md`:

```
# {Job Title} — {Company}

**URL:** {source URL}
**Location:** {location}
{Salary if listed}

---

## Key Responsibilities
{bullet list}

---

## Required Qualifications
{bullet list}

---

## Preferred / Bonus Skills
{bullet list}

---

## Benefits
{bullet list if present}
```

Use full verbatim text — do not summarise or paraphrase.

---

## Step 4 — Read the base resume and profile

Read the concise agent-facing versions (not `profile/verbose/`):
- `resume-base.json` from the current directory
- `profile/motivations.md`
- `profile/values.md`
- `profile/narrative.md`

Use these to inform the summary rewrite and cover letter. Note the "what I'm optimising for" priorities from `motivations.md` and the green/red flags from `values.md` to judge genuine role alignment.

---

## Step 5 — Produce the adapted JSON

Write `applications/{base name}/{base name}.json`.

### Do NOT change
- Employer names, dates, locations, degree names, certification names
- Quantified metrics (€1.6m, 90%, 75%, etc.)
- Any factual claim that would require the candidate to lie

### Adapt

**Summary:** Rewrite using Layer B insights. Mirror the JD's seniority and culture signals. Address the top fear or desire first. If the JD signals loss aversion, open with risk-reduction framing. If it signals ambition, open with scale and impact. Max 3 sentences. No personal pronouns.

**Experience bullets:** Apply primacy bias — the first bullet of each role must directly address the JD's top-listed responsibility or biggest repeated theme. Reorder all bullets by JD relevance. Lightly rephrase (word choice, emphasis) but preserve the underlying fact. Keep at least 2 bullets per role.

Apply the **peak-end rule**: the last bullet of the most recent role must also be strong.

Apply **fluency**: short declarative sentences over long compound ones. Lead metrics first within a sentence ("90% reduction" before the explanation).

**Skills:** Reorder categories so most relevant appear first. Move ATS keyword matches to the front of each `items` array.

**pillHighlights:** Replace with the 10–15 ATS phrases from Layer B.

**meta:** Set `"version"` to base name, `"lastUpdated"` to today. Add `"targetRole"`, `"targetCompany"`, `"sourceUrl"`, `"behaviouralInsights"` array (Layer B findings), and `"adaptationNotes"`.

---

## Step 6 — Probe for gaps (BEFORE rendering)

Identify JD requirements or themes weakly covered or absent in the base resume. For each genuine gap, ask a targeted question, e.g.:

> "The JD emphasises Unity Catalog governance. Have you worked with any data catalog or governance tooling — even partially?"

Limit to 3–5 questions. **Wait for the user to respond**, then update the JSON before proceeding.

---

## Step 7 — Check length BEFORE rendering

```bash
python3 .claude/tools/check_resume_length.py \
  "applications/{base name}/{base name}.json" --verbose
```

| Result | Action |
|--------|--------|
| **TARGET** (65–68 LU) | Optimal — render directly. |
| **GREEN** (< 70 LU) | Safe to render; trim lightly if > 68 LU. |
| **AMBER** (70–78 LU) | Trim bullets, re-run until below 70 LU. |
| **RED** (> 78 LU) | Aggressive trim required. |

**Trimming strategy:**
- Target 65–68 LU first (optimal one-page fit with rendering variance headroom).
- Each bullet costs `max(1.0, len / 110)` LU. A 220-char bullet = ~2 LU; a 100-char bullet = 1 LU.
- Trim least-relevant roles first. Prefer keeping Vinted and Tourlane; trim Keppel/LucaNet/Community first.
- Prefer ≤ 100 chars per bullet (single line). Tolerate up to 200 chars. Avoid > 200 chars.
- Re-run after each trim. Only render once ≤ 70 LU.

---

## Step 8 — Render HTML and PDF

```bash
python3 .claude/tools/render_resume.py \
  "applications/{base name}/{base name}.json" \
  "applications/{base name}/{base name}.html"
```

- **GREEN**: render with PDF (default).
- **AMBER**: add `--no-pdf` first, check HTML in browser, then re-run without `--no-pdf`.

If PDF generation fails, tell the user to open the HTML in Chrome → File → Print → Save as PDF.

---

## Step 9 — Generate the cover letter

Write `applications/{base name}/{base name}-cover-letter.md`. 4 paragraphs, max 350 words.

**P1 — Why this company:** Open with something specific — a product decision, growth signal, technical choice, or mission element that connects with Jeremy's values. Not "I am writing to apply for...". Tone: curious, direct, grounded.

**P2 — Why you fit:** 2–3 concrete capability matches, leading with the most relevant quantified achievement. Connect directly to the JD's top-listed responsibilities and Layer B repeated themes. Not a resume recap — a tight argument for fit.

**P3 — Gaps (conditional):** Include only if genuine gaps from Step 6. One honest, forward-looking sentence per gap: what it is, closest relevant experience, how it's being addressed. No apology. Frame as context.

**P4 — Alignment and intent:** From `motivations.md` and `values.md`. State what Jeremy is optimising for (1–2 sentences) and why this role fits those criteria specifically. End with one direct sentence of readiness.

**Tone rules:** European directness — confident without enthusiasm marketing. No "excited to", "passionate about", "thrilled to", "look forward to hearing from you". First person throughout. Close: `Best regards,\nJeremy Chia`

---

## Step 10 — Report

Tell the user:
- Output folder: `applications/{base name}/`
- Which files were created (JSON, HTML, PDF, cover letter)
- Short bullet list of key adaptations (from `adaptationNotes`)
- One sentence on main alignment and one on main gap (if any)
