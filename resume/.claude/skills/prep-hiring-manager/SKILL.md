---
name: prep-hiring-manager
description: Generates a tailored hiring manager interview prep document for a specific application. Researches the hiring manager's LinkedIn profile, career background, and motivations to surface what they need from this hire, likely probes, STAR stories calibrated to their perspective, and questions designed to build rapport.
allowed-tools: Read Write Bash WebSearch WebFetch
argument-hint: <application-folder-name> <hiring-manager-name or LinkedIn profile>
---

`$ARGUMENTS` contains two parts: (1) a full or partial application folder name and (2) the hiring manager's name and/or LinkedIn profile URL or any biographical information the user has provided inline. Parse these from the input.

Work through these steps **in order, completing each fully before starting the next**.

---

## Step 1 — Locate the application folder

```bash
ls applications/
```

Find the folder whose name contains the application identifier (case-insensitive). If exactly one match: proceed. If multiple: list and ask. If none: stop.

Set `{folder}` to the full folder name and `{path}` to `applications/{folder}`.

---

## Step 2 — Read the source files

Read **all** of these before proceeding. Do not proceed to Step 3 until all reads are complete.

- `{path}/jd.md` — role title, company, responsibilities, requirements
- `{path}/{folder}.json` — `meta.behaviouralInsights`, `meta.adaptationNotes`, `summary`, `experience` bullets
- `{path}/recruiter-prep.md` — if it exists: (a) carry the **Suggested opening hook** from Section 4 into Section 6 of the HM prep, adapting the framing for a hiring manager audience (more technical/strategic, less pitch); (b) carry any **hard question** the recruiter flagged (Section 1) into Section 3 probes — a question a recruiter flagged is very likely to resurface; (c) do not repeat company research verbatim, but do update it if new signals emerged during the recruiter call (check `notes.md` if present)
- `profile/motivations.md` and `profile/values.md` — concise agent-facing versions (not `profile/verbose/`)

---

## Step 3 — Research the hiring manager

You are doing the research — do not ask the user. If the user provided a LinkedIn URL, fetch it. Otherwise search for the person.

**3A — Career history:** How long at this company? What was their last role before current? Are they a long-tenured insider or a recent hire? What was their path into the role?

**3B — Did they hold this role?** If the hiring manager was previously in the exact role being hired for (promoted from within), flag this prominently — it means they know the job from the inside and will see through vague answers.

**3C — Background type — business or engineering?** Look at education and early career. A finance/business degree with analytics progression reads differently from a CS degree with engineering progression. Business-first managers respond to outcome framing; engineering-first managers respond to technical rigour.

**3D — Tenure signals:** Long tenure (3+ years at one company) signals they value culture fit and longevity. Short tenure signals they're outcome-focused and less attached to company lore. This shapes how to answer "why this company".

**3E — What they are now responsible for:** As a team lead or manager, what has shifted in their remit since their promotion? What can they no longer do themselves that the new hire must own? This is the most useful inference for what they need.

**3F — Any public writing, talks, or shared content?** If they have any public presence — blog posts, conference talks, LinkedIn activity — extract one concrete insight to reference naturally in the interview. This is low-confidence signal; only use if found.

---

## Step 4 — Analyse for the prep document

**4A — What the hiring manager needs from this hire:**
Based on their background and current role, infer what the hiring manager needs the new person to do for them — not just the company. What have they stopped doing since their promotion? What would make their job easier? What would make them look good internally?

**4B — What they will probe:**
Based on their background, what are they best qualified to test? A manager who came from the same role will probe technical depth and independence. A manager from a business background will probe stakeholder communication and business impact. A new manager will probe whether you can work without direction.

**4C — Their implicit fear:**
What is the hire they most dread making? (e.g. someone who leaves in 12 months, someone who needs constant management, someone who alienates stakeholders). Frame the fear specifically — not generically.

**4D — STAR story adjustments:**
Take 3 themes from the JD. For each, adjust the STAR story angle based on what this specific hiring manager will respond to. A business-first manager wants to hear about the business outcome; an engineering-first manager wants to hear about the technical decision; a new manager wants to hear about initiative and independence.

**4E — Questions for the hiring manager:**
Generate 4 questions. Each must:
- Be specific to this hiring manager's background or current situation (reference something real from Steps 3A–3F)
- Have a clear purpose: what does the answer tell you, and why does it help you decide?
- Not feel like a gotcha — they should feel like thoughtful curiosity, not a test

1. **What they need from this hire** — ask directly but frame it around enabling their success (e.g. "what would you most want this hire to own so you can focus on what the team lead role actually requires?")
2. **Team health or technical state** — probe the real state of the data infrastructure or team practices, grounded in a JD signal or something from the research
3. **Their own career or company journey** — a question that lets them tell their own story; people open up when invited to reflect on their own trajectory
4. **Ways of working / ambiguity handling** — how does the team actually work when requirements are unclear or priorities conflict? Grounded in a specific JD phrase.

---

## Step 5 — Write the prep document

Write `{path}/hiring-manager-prep.md`:

```markdown
# Hiring Manager Prep — {Job Title} at {Company}

**Application folder:** {folder}
**Interviewer:** {Hiring Manager Name}, {Title}
**Date:** {interview date if known, otherwise TBD}
**Prepared:** {today's date}

---

## 1. Who is {First Name}

**Career path at {Company}:**
{Bullet summary of their progression at this company, most recent first}

**Background before {Company}:**
{Bullet summary of their pre-company career — highlight background type: business-first or engineering-first}

**Education:**
{Degrees and institutions, one line each}

**What this means:**
{2–3 sentences on what their background implies about how they think, what they value, and how to frame your experience for them. Be specific — not generic.}

---

## 2. What {First Name} needs from this hire

{3–5 sentences on what the hiring manager needs the new person to own or solve for them — not for the company in general. Include what they have stopped doing since their promotion, and what would make their job easier.}

**Their implicit fear:** {One sentence naming the hire they most dread making.}

---

## 3. What {First Name} will evaluate

### {Probe 1 — most important given their background}
{2–3 sentences on what they will test and why, given their background. What does "good" look like here from their perspective?}

### {Probe 2}
{2–3 sentences}

### {Probe 3}
{2–3 sentences}

---

## 4. STAR stories — adjusted for this round

This is not a screening call. Stories need more depth. Use STAR+Spark but allocate more time to the Action — walk through your actual reasoning, not just what you did.

### Theme 1: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** {Specific story prompt adjusted for what this hiring manager responds to. End with a reflection question.}
**Why this matters to {First Name}:** {One sentence connecting this theme to what the manager needs right now.}

### Theme 2: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** {Story prompt}
**Why this matters to {First Name}:** {One sentence}

### Theme 3: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** {Story prompt}
**Why this matters to {First Name}:** {One sentence}

---

## 5. Questions for {First Name}

Pick 2 for the interview. The first two are highest signal.

### What they need from this hire
> "{Question that asks directly but frames it around enabling their success as a manager}"

### {Technical or team health}
> "{Question grounded in a specific JD signal or research finding}"

### {Their own journey}
> "{Question that invites them to reflect on their own career or company experience}"

### Ways of working
> "{Question about how ambiguity or competing priorities get resolved in practice, grounded in a specific JD phrase}"

---

## 6. Opening and closing

### Opening (first 60 seconds)
{1–2 sentences of guidance on what to lead with. Reference the specific hook from recruiter-prep if it still applies, or adjust for this audience. Do not recap the CV.}

> "{Draft opening hook — one fact about their business, one direct statement of capability}"

### Closing
> "{Draft 1–2 sentence closing. Concrete capabilities + availability + readiness. No enthusiasm marketing.}"

---

## 7. Interview mechanics

- {Mechanic 1 — specific to this interview format or manager context}
- {Mechanic 2}
- **Use "I" not "we"** — they will be assessing individual contribution.
- **Concrete over general** — every time you are tempted to say "the team" or "we built", replace with what you specifically did and decided.
- **Pause before answering** — 2–3 seconds signals confidence and prevents over-talking.
- **Salary / next steps** — if asked, state your range confidently. Do not deflect.
```

---

## Step 5b — Self-critique pass (MANDATORY before saving)

After drafting the document, review it against this checklist. Fix any failures before writing the file.

**Research quality:**
- [ ] Section 1 contains at least one specific, sourced fact about the hiring manager (not just their title)
- [ ] "What this means" in Section 1 is specific to this person — not a generic statement about business-first managers
- [ ] The implicit fear in Section 2 names a specific failure mode, not a generic one ("someone who leaves in 12 months because they find the ambiguity frustrating" beats "someone who underperforms")

**STAR stories:**
- [ ] Each "Why this matters to {First Name}" sentence connects to what the manager personally needs right now — not just to what the JD says
- [ ] Story prompts are adjusted for background type (business-first → outcome framing; engineering-first → decision and technical depth)
- [ ] No two STAR themes overlap — they cover genuinely different dimensions

**Questions:**
- [ ] Each question references something specific from the research or JD (not a template)
- [ ] The "ways of working" question quotes or paraphrases a specific phrase from the JD
- [ ] The "their own journey" question would feel like an invitation to the interviewer, not an interrogation

**Opening hook:**
- [ ] Contains one specific fact (a number, a product decision, a growth signal) — not a generic observation
- [ ] Does not contain "I am very interested in" or "I was thrilled to see"

If the research in Step 3 returned little (LinkedIn blocked, no public presence), note that explicitly in Section 1 rather than filling with inference. Low-confidence claims must be labelled as such.

---

## Step 6 — Report

Tell the user:
- Output file: `{path}/hiring-manager-prep.md`
- The three STAR themes and which angle was used for each (business outcome / technical decision / initiative)
- The most important thing to know about the hiring manager (one sentence — specific, not generic)
- The one question from Section 5 most likely to create a memorable impression, and why
