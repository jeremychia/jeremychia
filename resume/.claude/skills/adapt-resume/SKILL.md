---
name: adapt-resume
description: Fetches a job posting URL, adapts resume-base.json to match the role, and outputs a tailored JSON, HTML, and PDF inside applications/{base-name}/
allowed-tools: WebFetch Read Write Bash
argument-hint: <job-posting-url>
---

`$ARGUMENTS` is a job posting URL. Work through these steps **in order, completing each fully before starting the next**. Steps marked **[BLOCKING]** require the agent to stop and wait for user input before continuing.

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

**Seniority signals:** Phrases like "take ownership", "champion best practices", "translating to senior leadership" signal they want an autonomous IC. Phrases like "manage stakeholders", "drive alignment", "own the roadmap" signal a manager-adjacent scope.
- Autonomous IC signal → lead with outcomes and scale, not tasks
- Manager-adjacent signal → lead with cross-functional influence and team multiplier effects

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

Append a **Layer B — Behavioural Analysis** section at the end of the file, after Benefits (or at the end if no Benefits section). Format it as:

```
## Layer B — Behavioural Analysis

**Signal ordering:** {top priority interpretation}

**Repetition = fear/desire:** {themes appearing 3+ times and what they signal}

**Seniority signals:** {phrases and what they imply about autonomy/scope}

**Loss aversion:** {compliance/reliability language and framing implication}

**Culture signals:** {personality language if present; or note absence}

**Absence signals:** {what the JD omits and what that implies}

**ATS keywords:**
- {verbatim phrase 1}
- {verbatim phrase 2}
- ...
```

---

## Step 4 — Read the base resume and profile

Read **all** of these files now. Do not proceed to Step 5 until all reads are complete.

- `resume-base.json` from the current directory
- `profile/motivations.md`
- `profile/values.md`
- `profile/narrative.md`

Use these to inform the summary rewrite and cover letter. Note the "what I'm optimising for" priorities from `motivations.md` and the green/red flags from `values.md` to judge genuine role alignment.

**Alignment flag (carry into Step 5 meta):** After reading both the JD and the profile, make an honest judgement: does this role match what Jeremy is optimising for? Green = clear match. Amber = partial match with noted reservations. Red = genuine misalignment. Record this in `meta.alignmentSignal`.

---

## Step 5 — Produce the adapted JSON

Re-read `resume-base.json` immediately before writing — do not rely on memory from Step 4.

Write `applications/{base name}/{base name}.json`.

### Do NOT change
- Employer names, dates, locations, degree names, certification names
- Quantified metrics (€1.6m, 90%, 75%, etc.)
- Any factual claim that would require the candidate to lie

### Adapt

**Summary:** Rewrite using Layer B insights. Apply seniority framing from Step 1:
- Autonomous IC signal → open with outcomes and scale; make the first sentence a quantified result
- Manager-adjacent signal → open with cross-functional influence or team multiplier
- Loss aversion signal → open with risk reduction or reliability win
- Ambition signal → open with scale and impact

Max 3 sentences. Each sentence under 20 words. No personal pronouns. No sentence lists more than two things — split if needed.

**Experience bullets:** Apply primacy bias — the first bullet of each role must directly address the JD's top-listed responsibility or biggest repeated theme. Reorder all bullets by JD relevance. Lightly rephrase (word choice, emphasis) but preserve the underlying fact. Keep at least 2 bullets per role.

Apply the **peak-end rule**: the last bullet of the most recent role must also be strong — a quantified result, not a process description.

Apply **fluency**: short declarative sentences over long compound ones. Lead metrics first within a sentence ("90% reduction" before the explanation).

**Skills:** Reorder categories so most relevant appear first. Move ATS keyword matches to the front of each `items` array.

**Volunteering:** Only include volunteering experience if it directly reinforces a skill or theme the JD explicitly calls for. Omit it entirely for technical or business roles where it adds no signal.

**Business impact framing:** For business, analytics, or data roles, frame every achievement in terms of business outcome — revenue, cost, retention, decision-quality — not technical process. Lead the metric, follow with the mechanism. Avoid tool-centric bullets that describe what was built without stating what changed for the business.

**pillHighlights:** Replace with the 10–15 ATS phrases from Layer B.

**meta:** Set `"version"` to base name, `"lastUpdated"` to today. Add `"targetRole"`, `"targetCompany"`, `"sourceUrl"`, `"alignmentSignal"` (from Step 4), `"behaviouralInsights"` array (Layer B findings), and `"adaptationNotes"`.

---

## Step 5b — Self-critique pass (MANDATORY before proceeding)

After writing the JSON, review every line of the summary and all bullets against this checklist. Fix any failures before moving to Step 6.

**Summary checklist — fail any of these and rewrite:**
- [ ] Sentence 1 contains a quantified result or a named scale signal
- [ ] No sentence exceeds 20 words
- [ ] No personal pronouns (I, my, me, we, our)
- [ ] No sentence lists more than two things with commas
- [ ] Does not open with "Experienced", "Seasoned", "Results-driven", or any other throat-clearing adjective

**Bullet checklist — fail any of these and rewrite the offending bullet:**
- [ ] No bullet opens with a gerund clause ("Leveraging...", "Working with...", "Collaborating...")
- [ ] No bullet contains "demonstrating ability to", "showcasing expertise in", "with a track record of", "leveraging", "utilizing"
- [ ] No bullet stacks more than one unrelated achievement — split it if so
- [ ] No bullet ends with a gerund tail ("...delivering X while maintaining Y" → two sentences)
- [ ] No bullet exceeds 2 lines — if it does, it is trying to do too much; split or trim
- [ ] Every bullet in the most recent role leads with the impact, not the method
- [ ] The first bullet of each role directly addresses the JD's top responsibility

**After fixing:** Re-read the summary aloud. If any sentence takes more than one breath, shorten it. Re-read the first 3 bullets of the most recent role. If any sounds like a LinkedIn post or a ChatGPT response, rewrite it to sound like a person.

---

## Step 6 — Probe for gaps [BLOCKING]

**Complete Step 5b before starting this step.**

Identify JD requirements or themes weakly covered or absent in the base resume. For each genuine gap, ask a targeted question, e.g.:

> "The JD emphasises Unity Catalog governance. Have you worked with any data catalog or governance tooling — even partially?"

Limit to 3–5 questions. **Stop here and wait for the user to respond.** Do not render or proceed until the user answers. Then update the JSON with any new information before moving on.

If the user says "no gaps" or "continue", proceed directly.

---

## Step 7 — Check length BEFORE rendering

```bash
python3 .claude/tools/check_resume_length.py \
  "applications/{base name}/{base name}.json" --verbose
```

The checker uses pixel-accurate Georgia 9pt character widths — not a flat chars/line estimate. Each bullet's cost is `ceil(pixel_width / 731px)` physical lines. Orphans (last line < 40% full) cost +0.3 LU.

| Result | Action |
|--------|--------|
| **SPARSE** (< 63 LU) | Page underfilled — restore trimmed bullets or expand existing ones. |
| **TARGET** (63–73 LU) | Optimal fill — render directly. |
| **GREEN** (< 74 LU) | Safe to render PDF directly. |
| **AMBER** (74–81 LU) | Render HTML first, verify page count, then PDF. Trim until GREEN. |
| **RED** (> 81 LU) | Aggressive trim required before any render. |

**Trimming / expanding strategy:**
- Target 63–73 LU. The checker reports pixel widths — use those, not char counts.
- A bullet fits on one line if its pixel width < 731px. If it wraps, it costs 2 LU; if the second line is < 40% full, it's an orphan (+0.3 LU).
- **Orphan fix:** shorten until the bullet fits on one line (pixel width < 731px), or extend until the second line is at least 40% full (pixel width > 731 × 1.4 = 1024px).
- If SPARSE: expand short bullets by adding context, or restore trimmed bullets from the base resume.
- If over 74 LU: trim least-relevant roles first. Prefer Vinted and Tourlane; trim Keppel/LucaNet/Community first.
- Re-run after each change. Only render once GREEN or TARGET.

**After any trim or expand, re-run the Step 5b bullet checklist** on any bullet you changed — trimming can introduce orphan clauses or strip the metric.

**ATS keyword verification (run after reaching GREEN/TARGET):**

After the length check passes, verify that the ATS keywords from Layer B actually appear in the visible resume text (summary + bullets + skills). Run:

```bash
python3 -c "
import json, sys
data = json.load(open('applications/{base name}/{base name}.json'))
keywords = data.get('meta', {}).get('pillHighlights', [])
text = ' '.join([data.get('summary','')] +
  [b for job in data.get('experience',[]) for b in job.get('bullets',[])] +
  [b for edu in data.get('education',[]) for b in edu.get('bullets',[])] +
  [i for cat in data.get('skills',{}).get('technical',[]) for i in cat.get('items',[])])
missing = [k for k in keywords if k.lower() not in text.lower()]
if missing:
    print('MISSING keywords (not in visible text):')
    for k in missing: print(f'  - {k}')
else:
    print('All ATS keywords present in visible text.')
"
```

For any missing keyword: either weave it into a bullet or the summary, or remove it from `pillHighlights` if it genuinely cannot be covered without fabricating.

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

## Step 9 — Pre-send checklist

Before generating the cover letter, run this checklist and report any failures:

1. **Page count:** PDF renders as exactly 1 page. (Check pdfinfo output from Step 8, or open in Preview.)
2. **ATS keywords:** All `pillHighlights` keywords appear in visible resume text. (Verified in Step 7.)
3. **Company/role match:** The company name and job title in the JSON `meta` match the JD.
4. **No personal pronouns:** Summary contains none of: I, my, me, we, our.
5. **Metrics preserved:** All quantified figures from base resume (€1.6m, 90%, 75%, 88%→97%) that were included are unchanged.

Report: `✓ Pre-send checklist: N/5 passed` — list any failures with a one-line fix. Do not proceed to Step 10 until all 5 pass.

---

## Step 10 — Generate the cover letter

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

**P1 — Why this company:** Something specific — a product decision, growth signal, technical choice, or mission element that connects with Jeremy's values. Not "I am writing to apply for...". Tone: curious, direct, grounded. If a `recruiter-prep.md` exists in the application folder, pull the **Suggested opening hook** from Section 4 of that document and adapt it here — that research is already done. Otherwise derive the hook from the JD and Layer B analysis.

**P2 — Why you fit:** 2–3 concrete capability matches, leading with the most relevant quantified achievement. Connect directly to the JD's top-listed responsibilities and Layer B repeated themes. Not a resume recap — a tight argument for fit.

**P3 — Gaps (conditional):** Include only if genuine gaps from Step 6. One honest, forward-looking sentence per gap: what it is, closest relevant experience, how it's being addressed. No apology. Frame as context.

**P4 — Alignment and intent:** From `motivations.md` and `values.md`. State what Jeremy is optimising for (1–2 sentences) and why this role fits those criteria specifically. End with one direct sentence of readiness.

---

### Cover letter self-critique (run before saving)

After drafting, check every sentence against these rules. Fix before writing the file.

- [ ] P1 does not open with "I am writing to apply" or "I was excited to see"
- [ ] No sentence contains "passionate about", "excited to", "thrilled to", "look forward to hearing from you"
- [ ] No paragraph exceeds 4 sentences
- [ ] P2 leads with a quantified achievement, not a capability claim
- [ ] P3 is omitted if there are no genuine gaps from Step 6
- [ ] Total word count ≤ 350 (industry) — count and trim if over
- [ ] Closing is `Best regards,\nJeremy Chia\n{City}, {Month} {Year}` — nothing after it

---

**Tone rules (both types):** European directness — confident without enthusiasm marketing. No "excited to", "passionate about", "thrilled to", "look forward to hearing from you". First person throughout. Dashes freely used. Close: `Best regards,\nJeremy Chia\n{City}, {Month} {Year}`

---

## Step 11 — Report

Tell the user:
- Output folder: `applications/{base name}/`
- Which files were created (JSON, HTML, PDF, cover letter)
- Short bullet list of key adaptations (from `adaptationNotes`)
- One sentence on main alignment and one on main gap (if any)
- The `alignmentSignal` verdict from Step 4 — if Amber or Red, name the specific tension
