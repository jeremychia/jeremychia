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
- **Company name** (short slug, lowercase, hyphens, e.g. `lego`)
- **Job title** (slug form, e.g. `senior-analytics-engineer`)
- **Required skills and tools** — explicit tech stack mentioned
- **Preferred/bonus skills** — flagged as nice-to-have
- **Domain context** — industry, team size, stack maturity signals

### Layer B — Behavioural and cognitive reading

Go beyond what the JD literally says. Apply the following lenses to infer what the hiring manager and TA team are *actually* optimising for:

**Signal ordering (primacy bias):** What is listed first in the responsibilities and requirements? Hiring managers write JDs with their top priority first, even when they claim "all requirements are equal." Weight the resume to match that order.

**Repetition = fear or desire:** Any word or theme that appears more than twice signals either a pain point they've suffered (fear) or a capability they're desperate for (desire). For example, "data quality" appearing 4 times means they've been burned by bad data. "Ownership" appearing 3 times means their last hire didn't take initiative. Surface the resume content that directly addresses that fear or desire.

**Seniority signals:** Look for phrases like "take ownership", "accountability of large initiatives", "champion best practices", "translating to senior leadership." These reveal they want someone autonomous, not someone who needs managing. The resume should lead with outcomes and scale, not tasks.

**Loss aversion triggers:** Compliance language ("highly controlled compliant environment"), governance ("Unity Catalog governance", "data integrity"), and reliability language ("fit for purpose", "assertion checks") signal fear of failure more than excitement about growth. Frame the candidate's achievements as risk reduction and reliability wins, not just speed.

**Culture and identity signals:** Note the specific personality language used ("energetic", "pioneering", "#OneTeam", "bravery to challenge constructively", "curiosity"). These are not filler — they describe who the hiring manager identifies with. Mirror this language subtly in the summary and framing, without copy-pasting it.

**What is conspicuously absent:** If a JD for a senior role doesn't mention mentorship or team leadership, they probably don't want a manager — they want a strong individual contributor. If they don't mention stakeholder management but do mention "business teams", they want someone who collaborates but isn't a project manager. Use absence as a signal too.

**ATS keyword extraction:** TA teams typically configure ATS filters using exact phrases from the JD. Extract the 10–15 most distinctive phrases (not generic terms like "SQL") that are likely used as filters. These must appear verbatim in the resume, either in bullets or skills.

Summarise this layer as a short list of **behavioural insights** to carry forward into the adaptation step.

Derive the base name: `YYYY-MM-DD_company_job-title` using today's date.

---

## Step 2 — Create the output folder

Run:
```bash
mkdir -p "applications/{base name}"
```

All output files go inside this folder:
- `applications/{base name}/jd.md` ← job description record
- `applications/{base name}/{base name}.json`
- `applications/{base name}/{base name}.html`
- `applications/{base name}/{base name}.pdf`
- `applications/{base name}/{base name}-cover-letter.md`

---

## Step 3 — Save the JD as markdown

Write `applications/{base name}/jd.md` with this structure:

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

Use the full verbatim text from the fetched page — do not summarise or paraphrase. Preserve all original wording from every section. This gives a complete, accurate record of the JD alongside the tailored resume.

---

## Step 4 — Read the base resume and profile

Read the following files:
- `resume-base.json` from the current directory (not from the output folder)
- `profile/motivations.md` — what Jeremy is optimising for in a next role
- `profile/values.md` — non-negotiables and culture preferences
- `profile/narrative.md` — career arc and the "why" behind each move

These profile files inform both the summary rewrite and the cover letter in Step 9. Note the specific "what I'm optimising for" priorities from `motivations.md` and the culture green/red flags from `values.md` — use these to judge genuine role alignment.

---

## Step 5 — Produce the adapted JSON

Write `applications/{base name}/{base name}.json`. Rules:

### What you MUST NOT change
- Employer names, dates, locations, degree names, certification names
- Quantified metrics (€1.6m, 90%, 75%, etc.) — never alter numbers
- Any factual claim that would require the candidate to lie

### What you SHOULD adapt

**Summary**: Rewrite using the behavioural insights from Step 1. Mirror the JD's exact seniority signals and cultural identity language. Address the top fear or desire first. If the JD signals loss aversion (compliance, governance, reliability), open with a risk-reduction or quality framing. If it signals ambition (growth, pioneering, innovation), open with scale and impact. Keep to 3 sentences max. No personal pronouns.

**Experience bullets**: Apply primacy bias — the hiring manager's eyes land on the first bullet of each role and often stop there if it doesn't match. For the most recent role, the first bullet must directly address the JD's top-listed responsibility or biggest repeated theme. Reorder all bullets by JD relevance. You may lightly rephrase (word choice, emphasis) but must preserve the underlying fact. Omit genuinely irrelevant bullets — but keep at least 2 per role.

Apply the **peak-end rule**: make the last bullet of the most recent role also strong — this is the last thing a recruiter reads before forming their impression of the candidate's current work.

Apply **fluency**: prefer short, declarative sentences over long compound ones. A recruiter scanning in 6 seconds will parse "Cut pipeline costs by 15%" before they parse "Through systematic optimisation of workload configuration and storage partitioning strategies, achieved a 15% reduction in billed compute costs."

Apply **concrete anchoring**: always lead metrics first within a sentence. "90% reduction" before the explanation, not after.

**Skills — technical categories**: Reorder categories so the most relevant appear first. Prioritise exact ATS keyword matches from Layer B. Within each category, move matching tools to the front of the `items` array.

**pillHighlights**: Replace with the 10–15 exact ATS phrases identified in Layer B.

**meta**: Set `"version"` to the base name, update `"lastUpdated"` to today's date. Add `"targetRole"`, `"targetCompany"`, and `"sourceUrl"` fields. Add `"behaviouralInsights"` array summarising the key Layer B findings (fear/desire signals, seniority signals, culture signals, absence signals) — this is the analytical record alongside `"adaptationNotes"`.

---

## Step 6 — Probe for gaps (BEFORE rendering)

Before generating HTML or PDF, identify gaps — JD requirements or themes that are weakly covered or absent in the base resume.

For each gap, ask the user a targeted question to find out if there is an experience or achievement that could fill it. Frame each question specifically, e.g.:

> "The JD emphasises Unity Catalog / Databricks governance. Have you worked with any data catalog or governance tooling (Databricks, Alation, DataHub, Apache Atlas) in your current or previous roles — even partially?"

> "They mention driving data literacy across Markets & Channels teams. Do you have a specific example of running training, office hours, or documentation initiatives beyond the ReDI School teaching?"

Ask only for gaps that are genuinely missing — do not ask about things already in the base resume. Limit to 3–5 questions so it is not overwhelming.

**Wait for the user to respond.** Then update the adapted JSON with any new information before proceeding to rendering.

---

## Step 7 — Check length BEFORE rendering

Run the length estimator on the adapted JSON. This avoids wasting a render on content that will overflow to 2 pages.

```bash
python3 .claude/tools/check_resume_length.py \
  "applications/{base name}/{base name}.json" --verbose
```

**Interpret the result:**

| Result | Action |
|--------|--------|
| **TARGET** (65–68 LU) | Optimal — good content density with breathing room. Render HTML + PDF directly. |
| **GREEN** (< 70 LU) | Safe to render, but if > 68 LU, consider light trimming for tighter fit. |
| **AMBER** (70–78 LU) | Borderline — trim bullets, then re-run estimator to get below 70 LU. |
| **RED** (> 78 LU) | Over budget — aggressive trim required. |

**Trimming strategy:**
- **Target 65–68 LU first.** This gives optimal one-page fit with breathing room for PDF rendering variance.
- Each bullet costs `max(1.0, len / 110)` LU. A 220-char bullet costs ~2 LU; a 100-char bullet costs 1 LU.
- Trim by priority: remove bullets from least-relevant roles first, or shorten long bullets (> 150 chars).
- Prefer keeping Vinted (most recent, most relevant) and Tourlane bullets; trim Keppel/LucaNet/Community first.
- Re-run the estimator after each trim — do not guess and re-render.
- Only render once the estimator returns 65–70 LU (TARGET or GREEN).

**Tip when writing bullets:** Prefer ≤ 100 chars per bullet (guaranteed single line). Tolerate up to 200 chars (2-liner). Avoid > 200 chars.

---

## Step 8 — Render HTML and PDF

Once the estimator is GREEN or AMBER:

```bash
python3 .claude/tools/render_resume.py \
  "applications/{base name}/{base name}.json" \
  "applications/{base name}/{base name}.html"
```

- **GREEN**: render with PDF (default). Done.
- **AMBER**: add `--no-pdf` first, open the HTML in a browser to confirm it fits, then re-run without `--no-pdf`.

If PDF generation fails entirely, tell the user to open the HTML in Chrome and use File → Print → Save as PDF.

---

## Step 9 — Generate the cover letter

Using the profile files read in Step 4 and the JD analysis from Step 1, write `applications/{base name}/{base name}-cover-letter.md`.

### Structure (4 paragraphs, max 350 words)

**Paragraph 1 — Why this company**
Open with something specific about the company — a product decision, a growth signal, a technical choice, or a mission element that connects with Jeremy's values or interests. Do not open with "I am writing to apply for...". Reference one thing from the JD or company that signals you have done more than read the posting. Tone: curious, direct, grounded.

**Paragraph 2 — Why you fit**
Surface 2–3 concrete capability matches, connecting experience directly to the JD's top-listed responsibilities and repeated themes from Layer B. Lead with the most relevant quantified achievement. This is not a resume recap — it is a tight argument for why the technical match is strong.

**Paragraph 3 — Gaps (conditional)**
Include only if gaps were identified in Step 6. For each genuine gap: one honest, forward-looking sentence — what the gap is, the closest relevant experience, and how it is being addressed. Do not apologise or over-explain. Frame as context, not a defence.

**Paragraph 4 — Alignment and intent**
Draw from `motivations.md` and `values.md`. State what Jeremy is optimising for in the next role (1–2 sentences) and why this specific role and company fit those criteria. This should be specific and logical — not "I'm passionate about your mission" but a concrete reason grounded in his actual stated priorities. End with one direct sentence of readiness.

### Tone rules
- European directness: confident without enthusiasm marketing
- No filler: "excited to", "passionate about", "thrilled to", "look forward to hearing from you"
- First person throughout; trust the reader to have read the resume
- Close: `Best regards,\nJeremy Chia`

---

## Step 10 — Report

Tell the user:
- Output folder: `applications/{base name}/`
- Which of the 4 files were successfully created (JSON, HTML, PDF, cover letter)
- A short bullet list of key adaptations made (from `adaptationNotes`)
- One sentence on the main alignment and one sentence on the main gap (if any) surfaced in the cover letter
