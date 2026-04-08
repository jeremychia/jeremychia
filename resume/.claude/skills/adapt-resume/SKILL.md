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

## Step 4 — Read the base resume

Read `resume-base.json` from the current directory (not from the output folder).

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

## Step 6 — Write the HTML file

Write `applications/{base name}/{base name}.html`. ATS-safe Word-document style:

### Page / typography
- White background, black text, no colours
- Font: Georgia or Times New Roman (serif); fallback to serif
- Font size: 10pt
- `@page { margin: 0.9cm; }`
- Body: `max-width: 780px; margin: 0 auto; padding: 0.5cm 1cm;`

### Header (centred)
- Name: bold, ~16pt, all caps, letter-spacing
- Line 2: phone · email (linked) · GitHub (linked) · LinkedIn (linked) separated by ` &middot; `
- Line 3: location

### Section headings
- ALL CAPS, bold, 10pt, letter-spacing 0.1em
- Followed by `<hr style="margin:2px 0 6px; border:none; border-top:1px solid #000;">`

### Entries
- Company/institution row: `<div style="display:flex; justify-content:space-between;">`
- Company: `<strong>`, Role: `<em>`, date right-aligned
- Bullets: `<ul style="list-style-type:disc; margin:3px 0; padding-left:1.2em;">` with `<li style="margin-bottom:2px;">`

### Skills section
One `<p>` per technical category: `<strong>Category:</strong> item1, item2, item3`.
Then certifications and languages the same way.

### ATS rules
- No images, SVGs, tables, text boxes, or JavaScript
- Section heading strings: "Professional Experience", "Education", "Community and Volunteering", "Skills"
- All links use full URLs
- No `display:none` on any content

---

## Step 7 — Convert to PDF

Try browsers in this order, using the absolute path to the HTML file:

```bash
DIR="applications/{base name}"
HTML="${DIR}/{base name}.html"
PDF="${DIR}/{base name}.pdf"
ABS_HTML="$(pwd)/${HTML}"
ABS_PDF="$(pwd)/${PDF}"

for BROWSER in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
  "chromium-browser" \
  "google-chrome"; do
  if [ -f "$BROWSER" ] || command -v "$BROWSER" &>/dev/null; then
    "$BROWSER" \
      --headless=new \
      --print-to-pdf="$ABS_PDF" \
      --print-to-pdf-no-header-footer \
      --no-margins \
      --disable-gpu \
      --paper-width=8.27 --paper-height=11.69 \
      "$ABS_HTML" 2>/dev/null
    break
  fi
done

[ -f "$ABS_PDF" ] && echo "PDF OK" || echo "PDF FAILED"
```

If PDF generation fails, tell the user to open the HTML in Chrome and use File → Print → Save as PDF, saving to `applications/{base name}/{base name}.pdf`.

---

## Step 8 — Report and probe for gaps

Tell the user:
- Output folder: `applications/{base name}/`
- Which of the 3 files were successfully created (JSON, HTML, PDF)
- A short bullet list of key adaptations made (from `adaptationNotes`)

Then identify gaps — JD requirements or themes that are weakly covered or absent in the base resume. For each gap, ask the user a targeted question to find out if there is an experience or achievement that could fill it. Frame each question specifically, e.g.:

> "The JD emphasises Unity Catalog / Databricks governance. Have you worked with any data catalog or governance tooling (Databricks, Alation, DataHub, Apache Atlas) in your current or previous roles — even partially?"

> "They mention driving data literacy across Markets & Channels teams. Do you have a specific example of running training, office hours, or documentation initiatives beyond the ReDI School teaching?"

Ask only for gaps that are genuinely missing — do not ask about things already in the base resume. Limit to 3–5 questions so it is not overwhelming. After the user answers, offer to update the adapted JSON and regenerate the PDF with the new information.
