---
name: prep-recruiter-call
description: Generates a tailored recruiter call preparation document for a specific application, using the saved JD and adapted resume JSON to surface behavioural talking points, STAR stories, and research prompts.
allowed-tools: Read Write Bash
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

## Step 3 — Analyse for the prep document

Before writing, derive the following from the source files:

### 3A — The Three Pillars assessment
For this specific role, determine:

**Viability signals** (from jd.md requirements):
- The 3–5 "must-have" qualifications — what will the recruiter check first?
- Any likely sticking points (e.g. location, notice period, tools not in resume)

**Coachability & soft skill signals** (from JD language):
- What personality or working-style language does the JD use? (e.g. "ownership", "pioneering", "collaborative")
- What does this signal about the team culture the recruiter is screening for?

**Narrative consistency risks**:
- Are there any gaps between the adapted resume and the JD requirements that a recruiter might flag?
- What is the likely "hardest question" based on those gaps?

### 3B — Peak moment selection
From the `experience` bullets in the adapted JSON, select the single strongest achievement — the one that is most relevant to the JD's top-listed responsibility and most quantified. This is the "Peak" to deliver with energy.

### 3C — STAR story candidates
Identify 3 distinct themes the JD emphasises (from `behaviouralInsights` or repeated JD language). For each theme, identify the best matching bullet from experience. These become STAR story prompts.

### 3D — Closing statement ("End")
Draft a 2–3 sentence enthusiastic closing statement the candidate can use to end the call. It should: (1) restate specific interest in this role at this company using one genuine detail from the JD, (2) confirm availability and intent to move forward, (3) leave the recruiter with one memorable phrase.

### 3E — Culture-refining question
Draft one specific question using the "90-day perfect hire" framing, tailored to what the JD signals the team is building or fixing.

---

## Step 4 — Write the prep document

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

## 4. Company and recruiter research checklist

### Company (do before the call)
- [ ] **Engineering or data blog** — search `{company} engineering blog` or `{company} data blog`. Look for posts on their data stack (dbt, Airflow, Spark, Snowflake/BigQuery, etc.), data platform migrations, or modelling decisions. A post here tells you more about the actual work than the JD does.
- [ ] **LinkedIn "People" tab filtered to data roles** — search within the company for "analytics engineer", "data engineer", "analytics". How many people? How senior? This signals whether you'd be building from scratch or joining a mature team.
- [ ] **Data team structure signal** — are analytics engineers centralised (one data team serving the whole company) or embedded (sitting in product/commercial squads)? Look at job titles and reporting lines in LinkedIn profiles. This affects your day-to-day autonomy significantly.
- [ ] **Company LinkedIn posts in the last 30 days** — look for product launches, data-related announcements, or culture posts. Note one specific post to reference on the call.
- [ ] {Company-specific prompt derived from JD context — e.g. "Check if they've recently announced a data platform migration, a new product area generating new data, or a move from a legacy BI tool to a modern stack."}

### Recruiter (if name is known)
- [ ] Career trajectory — did they move from agency to in-house? They likely value brand loyalty and stability.
- [ ] Do they specialise in data/tech roles? A recruiter who places data roles regularly will understand the stack — you can use technical language with them.
- [ ] Recent activity feed — what topics do they engage with? Mirror one if relevant.
- [ ] Shared connections — use for vibe-check of their professional circle, not necessarily to name-drop.

---

## 5. Opening and closing

### Opening (first 60 seconds)
Start with one genuine thing you admire about the company. Use a specific detail from your research — not "I love your mission." Example framing:
> "Before we dive in, I wanted to say I came across [specific post/initiative] and it really resonated — it's exactly the kind of [data culture / product thinking / engineering rigour] I want to be part of."

### Closing statement
> {Draft 2–3 sentence closing statement from Step 3D.}

---

## 6. Question to ask

> "{Culture-refining question from Step 3E}"

*Why this question works:* It forces the recruiter to visualise you succeeding in the role, and signals you are thinking about impact from day one — not just salary and perks.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story before moving on — prevents rambling and gives the recruiter time to finish their notes.
- **Use "I" not "we"** when describing achievements — recruiters need to assess your individual contribution.
- **Salary / notice period** — be ready to state your range confidently. If pushed early, it is fine to say: "I am flexible depending on the full package — can you share the budgeted range for the role?"
```

---

## Step 5 — Report

Tell the user:
- The output file path: `{path}/recruiter-prep.md`
- The three STAR themes identified
- The selected Peak moment (one sentence)
- A reminder to do the LinkedIn research before the call
