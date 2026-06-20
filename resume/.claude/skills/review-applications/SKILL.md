---
name: review-applications
description: Reads all application folders to synthesise patterns across rejections, feedback, and notes — surfaces what is working, what is failing, and what to change in the base resume or approach.
allowed-tools: Read Bash Write
---

No arguments required. Work through these steps **in order, completing each fully before starting the next**.

---

## Step 1 — Inventory all applications

```bash
ls applications/
```

For each folder, check which of these files exist:
- `rejection_feedback.md` — external feedback from recruiters/hiring managers
- `notes.md` — Jeremy's own notes on the process, interview, or outcome
- `recruiter-prep.md` — exists if a recruiter call happened
- `hiring-manager-prep.md` — exists if a hiring manager interview happened

Categorise each application into one of:
- **Active** — no rejection file, recent date
- **Rejected — early** (rejection with no recruiter call prepped)
- **Rejected — after recruiter** (recruiter-prep exists, rejected before or after)
- **Rejected — late stage** (hiring-manager-prep or meet-the-team-prep exists)
- **Outcome unknown** — no signal files, older date

---

## Step 2 — Read all signal files

Read every `rejection_feedback.md` and `notes.md` across all folders. Do not summarise prematurely — extract verbatim phrases and assign them to themes as you go.

Read the `meta.behaviouralInsights` and `meta.adaptationNotes` from the JSON in each application folder too. This surfaces what the resume was adapted to claim — which helps distinguish "resume promised X but interview revealed we couldn't deliver X" from "resume never mentioned X and got filtered".

---

## Step 3 — Synthesise patterns

Group findings into these categories:

### 3A — Rejection reasons (verbatim where possible)
List every stated rejection reason. Note which are explicit (recruiter said X) vs. inferred (no feedback given, pattern across similar roles).

### 3B — Stage distribution
How many rejections happened at each stage? Early rejections (no call) suggest ATS or resume filtering. Late rejections suggest interview performance gaps, not resume gaps.

### 3C — Themes appearing 3+ times
Any reason, concern, or gap mentioned across 3+ applications is a systemic issue, not a one-off. Flag these prominently.

### 3D — What is working
Which applications progressed furthest? What do those roles have in common (industry, seniority, tech stack, company size)? What did the adapted resume do well in those cases?

### 3E — Resume gaps vs. interview gaps
Distinguish: is the pattern a resume problem (not getting calls) or an interview problem (getting calls but not offers)? Different fixes.

### 3F — Role-type fit signals
Are certain role types (e.g. data engineering vs. analytics engineering vs. BI analyst) converting better? This informs which roles to prioritise.

---

## Step 3b — Challenge your own interpretation (MANDATORY)

Before writing recommendations, interrogate the synthesis against these questions. If any answer is "no" or "uncertain", revisit the evidence.

**Stage attribution:**
- [ ] Have you correctly attributed early rejections to resume/ATS filtering rather than assuming interview issues? Evidence: were there any recruiter calls for these roles?
- [ ] Have you correctly attributed late rejections to interview performance rather than assuming resume issues? Evidence: what stage did they reach?

**Pattern confidence:**
- [ ] Is the "systemic theme" truly systemic (3+ explicit mentions) or is it appearing to repeat because you're pattern-matching across thin evidence?
- [ ] For each theme in 3C: what is the verbatim evidence count? If it's 1 explicit + 2 inferred, label it as low-confidence.

**What's working — genuine signal or survivorship:**
- [ ] Are the applications that progressed furthest doing so because of the resume adaptations, or because of role type, seniority fit, or company culture? Try to disentangle.

**Resume vs. interview split:**
- [ ] Can you point to at least one specific piece of evidence (a recruiter quote, a note) that distinguishes interview gaps from resume gaps? If not, label the split as inferred.

Document any "low-confidence" or "inferred" labels in the synthesis — do not present inferred conclusions as firm findings.

---

## Step 4 — Generate recommendations

Produce three lists:

**Immediate changes to `resume-base.json`:**
Changes with clear evidence from 3+ rejection signals. Be specific — which bullet, which section, what to add or remove. Only include changes supported by explicit evidence, not inference.

**Interview preparation gaps:**
Skills, stories, or framings that came up in late-stage rejections. These belong in practice, not the resume.

**Application strategy:**
Which role types or companies to deprioritise based on conversion data. Which signals suggest better fit.

For each recommendation, note the evidence count and confidence level: **High** (3+ explicit mentions), **Medium** (2 explicit or 1 explicit + pattern), **Low** (inferred from thin evidence).

---

## Step 5 — Write the synthesis report

Write `applications/review-{YYYY-MM-DD}.md`:

```markdown
# Application Review — {date}

**Applications reviewed:** {N total}
**Stage breakdown:** {N early rejections} | {N after recruiter} | {N late stage} | {N active/unknown}

---

## Systemic themes (3+ applications)

{Bullet list of recurring rejection signals with count and example quotes. Label each as High/Medium/Low confidence.}

---

## Stage analysis

### Early rejections (resume/ATS filtering)
{What the early rejections have in common. ATS keyword gaps? Role-type mismatch? Seniority? Note if thin evidence.}

### Late-stage rejections (interview gaps)
{What came up in hiring manager or panel rejections. Skill gaps? Framing issues? Fit concerns? Note if inferred.}

---

## What is working

{Which applications progressed furthest and what they have in common. Note if the sample is too small to draw firm conclusions.}

---

## Recommended changes

### Resume (`resume-base.json`)
{Specific, evidence-backed changes — section, bullet, what to change. Evidence count and confidence level for each.}

### Interview preparation
{Specific stories or framings to build out. Evidence for each.}

### Application strategy
{Role types to prioritise or deprioritise based on conversion data.}

---

## Raw rejection log

| Folder | Stage reached | Stated reason (verbatim or inferred) | Confidence |
|--------|--------------|--------------------------------------|------------|
{One row per rejected application}
```

---

## Step 6 — Report

Tell the user:
- Output file: `applications/review-{date}.md`
- The single most impactful change to make based on the evidence — and its confidence level
- The most common rejection stage and what it implies
- Whether the primary issue is resume filtering or interview performance — and how confident you are in that distinction
- Any finding you would have reported confidently but downgraded after the Step 3b challenge
