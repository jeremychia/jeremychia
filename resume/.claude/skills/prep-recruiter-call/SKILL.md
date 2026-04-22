---
name: prep-recruiter-call
description: Generates a tailored recruiter call preparation document for a specific application, using the saved JD and adapted resume JSON to surface behavioural talking points, STAR stories, and research prompts.
allowed-tools: Read Write Bash WebSearch WebFetch
argument-hint: <application-folder-name or partial match>
---

`$ARGUMENTS` is either a full application folder name (e.g. `2026-04-08_lego_senior-analytics-engineer`) or a partial match (e.g. `lego` or `finn`). Run through these steps in order.

---

## Step 1 — Locate the application folder

List `applications/` and find the folder whose name contains `$ARGUMENTS` (case-insensitive). If exactly one match is found, proceed. If multiple match, list them and ask the user to clarify. If none match, tell the user and stop.

```bash
ls applications/
```

Once identified, set `{folder}` to the full folder name and `{path}` to `applications/{folder}`.

---

## Step 2 — Read the source files

Read both:
- `{path}/jd.md` — for role title, company name, responsibilities, and requirements
- `{path}/{folder}.json` — for `meta.behaviouralInsights`, `meta.adaptationNotes`, `summary`, and `experience` bullets

If `jd.md` is missing, proceed using the JSON only and note the gap.

---

## Step 3 — Research the company

Actively research the company using WebSearch and WebFetch. You are doing the research — do not ask the user to do it. Compile real findings; if a search returns nothing useful, note that explicitly rather than inventing facts.

### 3A — Engineering / data blog
Search `{company} engineering blog data` and `{company} data stack dbt snowflake`. Fetch any relevant posts. Extract: what data tools they use, any platform migrations, modelling decisions, or data culture signals.

### 3B — Data team size and structure
Search `{company} analytics engineer linkedin` and `{company} data team size`. Try to infer: how many people are in the data function, whether analytics engineers are centralised or embedded, and how senior the team appears.

### 3C — Recent company news
Search `{company} news 2025 2026` and `{company} product launch funding`. Extract: growth signals, new product areas, expansion, or funding rounds that would affect the data team's priorities.

### 3D — Company-specific signal from JD
Based on the JD context (e.g. ERP integration, subscription metrics, logistics costs), run one targeted search to find something concretely useful before the call — e.g. which ERP they use, their pricing model tiers, or whether they recently migrated BI tools.

### Sourcing rule
For every specific fact, figure, or quote used anywhere in the output document, include the source URL as a markdown link immediately after — e.g. "ARR hit $400M in February 2026 ([Bloomberg](https://...))". This applies throughout Sections 4 and 5. Do not add sources to claims derived from the JD or resume JSON.

---

## Step 4 — Analyse for the prep document

Before writing, derive the following from the source files and research:

### 4A — The Three Pillars assessment
**Viability signals** (from jd.md requirements):
- The 3–5 "must-have" qualifications — what will the recruiter check first?
- Any likely sticking points (e.g. location, notice period, tools not in resume)

**Coachability & soft skill signals** (from JD language):
- What personality or working-style language does the JD use?
- What does this signal about the team culture the recruiter is screening for?

**Narrative consistency risks**:
- Are there gaps between the adapted resume and the JD requirements a recruiter might flag?
- What is the likely "hardest question" based on those gaps?

### 4B — Peak moment selection
From the `experience` bullets in the adapted JSON, select the single strongest achievement — most relevant to the JD's top-listed responsibility and most quantified.

### 4C — STAR story candidates
Identify 3 distinct themes the JD emphasises. For each, identify the best matching bullet from experience.

### 4D — Closing statement
Draft a 2–3 sentence enthusiastic closing statement: (1) restate specific interest using one genuine detail from the JD, (2) confirm availability and intent to move forward, (3) leave one memorable phrase.

### 4E — Culture-refining question
Draft one specific question using the "90-day perfect hire" framing, tailored to what the JD signals the team is building or fixing.

---

## Step 5 — Write the prep document

Write the output to `{path}/recruiter-prep.md`.

Use this structure exactly:

```markdown
# Recruiter Call Prep — {Job Title} at {Company}

**Application folder:** {folder}
**Prepared:** {today's date}

---

## 1. What the recruiter is screening for

### Viability checklist
{3–5 bullet points the recruiter will tick off — must-haves from the JD. For each, note whether it is clearly covered in the resume or is a potential gap.}

### Soft skill and culture fit signals
{2–3 sentences on the personality/culture language in the JD and what it signals about the team. One sentence on how to mirror this tone on the call.}

### Likely hard question
**"{The most likely probing question based on narrative gaps}"**
*Suggested response frame:* {1–2 sentences on how to handle it honestly and confidently — don't dodge, reframe as a strength or learning.}

---

## 2. Your Peak moment

> {The single strongest achievement, written as a spoken sentence — natural language, not a resume bullet. Include the quantified result. Deliver this with high energy.}

*Why this works:* {One sentence on why this directly addresses the JD's top priority.}

---

## 3. STAR story prompts

For each theme below, use the STAR+Spark structure: Situation/Task (20%), Action — use "I" not "we" (60%), Result with a number (20%), Learning/Spark (1 sentence).

### Theme 1: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** Prepare a story about {specific situation type} where you {action}. End with what you learned or would do differently.

### Theme 2: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** Prepare a story about {specific situation type} where you {action}. End with what you learned or would do differently.

### Theme 3: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** Prepare a story about {specific situation type} where you {action}. End with what you learned or would do differently.

---

## 4. Company research findings

### Data stack and engineering culture
{What you found about their data tools, stack, or engineering blog. If nothing found, say so.}

### Data team size and structure
{What you found about headcount, centralised vs embedded, seniority signals. If nothing found, say so.}

### Recent news and growth signals
{Key funding, product launches, or expansion news relevant to why the data team is hiring. If nothing found, say so.}

### Role-specific insight
{The one targeted finding from Step 3D — e.g. which ERP they use, their pricing tiers, a recent BI migration. If nothing found, say so.}

### Suggested opening hook
> "{A specific, genuine sentence to open the call with — referencing one real finding from the research above. Not generic.}"

---

## 5. Opening and closing

### Opening (first 60 seconds)
Use the suggested hook from Section 4 above. The goal is one specific, genuine observation — not "I love your mission."

### Closing statement
> {Draft 2–3 sentence closing statement from Step 4D.}

---

## 6. Question to ask

> "{Culture-refining question from Step 4E}"

*Why this question works:* It forces the recruiter to visualise you succeeding in the role, and signals you are thinking about impact from day one — not just salary and perks.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story before moving on — prevents rambling and gives the recruiter time to finish their notes.
- **Use "I" not "we"** when describing achievements — recruiters need to assess your individual contribution.
- **Salary / notice period** — be ready to state your range confidently. If pushed early, it is fine to say: "I am flexible depending on the full package — can you share the budgeted range for the role?"
```

---

## Step 6 — Report

Tell the user:
- The output file path: `{path}/recruiter-prep.md`
- The three STAR themes identified
- The selected Peak moment (one sentence)
- Two or three of the most useful research findings
