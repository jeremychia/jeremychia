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

**Volunteering:** Only include volunteering experience if it directly reinforces a skill or theme the JD explicitly calls for. Omit it entirely for technical or business roles where it adds no signal.

**Business impact framing:** For business, analytics, or data roles, frame every achievement in terms of business outcome — revenue, cost, retention, decision-quality — not technical process. Lead the metric, follow with the mechanism. Avoid tool-centric bullets that describe what was built without stating what changed for the business.

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
| **TARGET** (67–69 LU) | Optimal — full page, no orphans. Render directly. |
| **GREEN** (< 70 LU) | Safe to render; expand lightly if < 67 LU. |
| **AMBER** (70–77 LU) | Render HTML first, verify page count, then PDF. Trim until GREEN. |
| **RED** (> 77 LU) | Aggressive trim required before any render. |

**Trimming / expanding strategy:**
- Target 67–69 LU (fills the page completely, one orphan-free LU ≈ one physical line).
- Each bullet costs `ceil(len / 110)` LU: ≤110 chars = 1 LU; 111–220 chars = 2 LU; 221–330 chars = 3 LU.
- **Orphan zone (111–154 chars):** costs 2 LU but leaves the second line mostly empty. Fix by shortening to ≤ 110 chars OR extending to ≥ 155 chars.
- **Bullet sweet spots:** ≤ 110 chars (1 LU, clean line) or 155–220 chars (2 LU, both lines ≥ 40% full).
- If under 67 LU: expand short bullets by adding context, or restore trimmed bullets from the base resume.
- If over 70 LU: trim least-relevant roles first. Prefer Vinted and Tourlane; trim Keppel/LucaNet/Community first.
- Re-run after each change. Only render once GREEN.

---

## Step 8 — Render HTML and PDF

```bash
python3 .claude/tools/render_resume.py \
  "applications/{base name}/{base name}.json" \
  "applications/{base name}/{base name}.html"
```

- **GREEN**: render with PDF (default). The renderer will report page count — if > 1 page, trim and re-render.
- **AMBER**: add `--no-pdf` first, check HTML in browser, then re-run without `--no-pdf`. Verify page count in output.

If PDF generation fails, tell the user to open the HTML in Chrome → File → Print → Save as PDF.

---

## Step 9 — Generate the cover letter

Write `applications/{base name}/{base name}-cover-letter.md`.

**For teaching / academic roles:** write as a **motivation statement**, not a cover letter. The structure is personal and reflective — why I teach, why this institution, what I would do with this course — not a credentials parade. The CV carries the credentials.

**For industry roles:** write as a cover letter. 4 paragraphs, max 350 words.

---

### Motivation statement structure (teaching roles)

**Opening:** Address a specific person by name if known (e.g. "Dear Dr. [Name],"). Open with a personal statement of intent — what drives Jeremy at the level of values, not skills. The "I strive to live intentionally" register. Not "I am writing to apply for...".

**P1 — Why I teach:** The personal motivation, grounded in a specific moment or realisation. The transformation Jeremy cares about: from "I do not know how to approach this" to "I know how to approach this." Long-term student connection as part of what makes teaching meaningful.

**P2 — Why this institution:** A genuine critique or observation about education in general, then why this institution's approach is designed against that failure. Use the institution's own language and frameworks correctly. Be specific about the pedagogy — class size, format, tutorials, mission — not generic praise.

**P3 — What I would do with this course:** Concrete course vision. Use project examples anchored in decisions students are already living with. Break out parallel projects as bullet lists when there are multiple examples. Connect project outputs to practical outcomes — portfolio, public communication, building a voice — and link to the institution's stated competencies where relevant.

**P4 — Closing:** Dual fluency or distinctive positioning (e.g. accountant-turned-practitioner). Acknowledge any genuine gaps honestly, one sentence, no apology. Right to work and availability. Location and date in the sign-off.

---

### Cover letter structure (industry roles)

**P1 — Why this company:** Something specific — a product decision, growth signal, technical choice, or mission element that connects with Jeremy's values. Not "I am writing to apply for...". Tone: curious, direct, grounded.

**P2 — Why you fit:** 2–3 concrete capability matches, leading with the most relevant quantified achievement. Connect directly to the JD's top-listed responsibilities and Layer B repeated themes. Not a resume recap — a tight argument for fit.

**P3 — Gaps (conditional):** Include only if genuine gaps from Step 6. One honest, forward-looking sentence per gap: what it is, closest relevant experience, how it's being addressed. No apology. Frame as context.

**P4 — Alignment and intent:** From `motivations.md` and `values.md`. State what Jeremy is optimising for (1–2 sentences) and why this role fits those criteria specifically. End with one direct sentence of readiness.

---

**Tone rules (both types):** European directness — confident without enthusiasm marketing. No "excited to", "passionate about", "thrilled to", "look forward to hearing from you". First person throughout. Dashes freely used. Close: `Best regards,\nJeremy Chia\n{City}, {Month} {Year}`

---

## Step 10 — Report

Tell the user:
- Output folder: `applications/{base name}/`
- Which files were created (JSON, HTML, PDF, cover letter)
- Short bullet list of key adaptations (from `adaptationNotes`)
- One sentence on main alignment and one on main gap (if any)
