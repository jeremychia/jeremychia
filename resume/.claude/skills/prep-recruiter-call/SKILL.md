---
name: prep-recruiter-call
description: Generates a tailored recruiter call preparation document for a specific application, using the saved JD and adapted resume JSON to surface behavioural talking points, STAR stories, and research prompts.
allowed-tools: Read Write Bash WebSearch WebFetch
argument-hint: <application-folder-name or partial match>
---

`$ARGUMENTS` is a full or partial application folder name (e.g. `lego` or `2026-04-08_lego_senior-analytics-engineer`). Work through these steps **in order**, completing each fully before the next.

---

## Step 1 — Locate the application folder

```bash
ls applications/
```

Find the folder whose name contains `$ARGUMENTS` (case-insensitive). If exactly one match: proceed. If multiple: list and ask. If none: stop.

Set `{folder}` to the full folder name and `{path}` to `applications/{folder}`.

---

## Step 2 — Read the source files

Read **all** of these before proceeding to Step 3.

- `{path}/jd.md` — role title, company, responsibilities, requirements
- `{path}/{folder}.json` — `meta.behaviouralInsights`, `meta.adaptationNotes`, `summary`, `experience` bullets
- `profile/motivations.md` and `profile/values.md` — concise agent-facing versions (not `profile/verbose/`)

If `jd.md` is missing, proceed with JSON only and note the gap.

---

## Step 3 — Research the company

You are doing the research — do not ask the user. For every specific fact or figure used in the output, include a source URL as a markdown link immediately after. Don't add sources to claims from the JD or resume. If a search returns nothing useful, say so rather than inventing.

**3A — Data stack:** Search `{company} engineering blog data` and `{company} data stack dbt snowflake`. Extract: tools, platform migrations, modelling decisions, data culture signals.

**3B — Team size and structure:** Search `{company} analytics engineer linkedin` and `{company} data team size`. Infer: headcount, centralised vs. embedded, seniority signals.

**3C — Recent news:** Search `{company} news 2025 2026` and `{company} product launch funding`. Extract: growth signals, new product areas, expansion, funding rounds.

**3D — Role-specific insight:** Based on JD context, run one targeted search for something concretely useful — e.g. which ERP they use, their pricing tiers, a recent BI migration.

**3E — Business model and unit economics:** Search `{company} business model revenue` and `{company} pricing` or `{company} annual report`. How do they make money (B2B/B2C/marketplace/SaaS/transaction)? What are their key revenue drivers and cost levers? What does that imply about which data problems matter most (e.g. a marketplace needs supply/demand balance metrics; a SaaS company lives or dies on churn and ARR)?

**3F — Competitive landscape:** Search `{company} competitors` and `{company} vs {likely competitor}`. Who are their 2–3 closest competitors? How does the company differentiate (price, product, distribution)? Incumbent or challenger? This informs what the data team is likely optimising for and which business questions are highest stakes.

---

## Step 4 — Analyse for the prep document

**4A — Three Pillars:**
- *Viability:* 3–5 must-have qualifications; note whether each is clearly in the resume or is a potential gap
- *Soft skill signals:* What personality/culture language in the JD signals about the team the recruiter is screening for
- *Narrative risks:* Gaps between the resume and JD a recruiter might flag; the likely hardest question

**4B — Peak moment:** Single strongest achievement from the experience bullets — most relevant to the JD's top-listed responsibility, most quantified.

**4C — STAR candidates:** Identify 3 themes the JD emphasises. Match the best resume bullet to each.

**4D — Closing statement:** 1–2 sentence direct closing (European/grounded tone). (1) One concrete capability you bring. (2) Signal availability and readiness.

**4E — Questions to ask:** Generate 4 questions, each from a different angle. Every question must be specific to this company and role — derived from the research and JD, not generic templates. Assign each a purpose:

1. **Impact/success definition** — what does "great" look like in 6–12 months for this specific role? Anchor it to something concrete from the JD or research (e.g. a migration, a known data quality problem, a growth phase).
2. **Team problem** — what is the hardest unsolved problem the data team has right now? Frame it around something specific you observed — a gap in the JD, a scaling signal from the news, a known stack limitation.
3. **Business/strategy** — something that shows you understand their business model or competitive position. Draw from 3E/3F. Ask about a tension or trade-off you've noticed (e.g. "You're a marketplace — how does the data team balance supply-side and demand-side analytics priorities?").
4. **Ways of working** — a question about how decisions get made, how the data team interacts with the business, or what the culture signals in the JD actually look like day-to-day. Base it on something specific in the JD language (e.g. if the JD says "self-starter", ask what that looks like in practice when priorities conflict).

---

## Step 5 — Write the prep document

Write `{path}/recruiter-prep.md`:

```markdown
# Recruiter Call Prep — {Job Title} at {Company}

**Application folder:** {folder}
**Prepared:** {today's date}

---

## 1. What the recruiter is screening for

### Viability checklist
{3–5 bullets — must-haves from the JD, each noting whether clearly covered in the resume or a potential gap}

### Soft skill and culture fit signals
{2–3 sentences on the personality/culture language in the JD. One sentence on how to mirror this tone on the call.}

### Likely hard question
**"{Most likely probing question based on narrative gaps}"**
*Suggested response frame:* {1–2 sentences — handle honestly and confidently, reframe as strength or learning}

---

## 2. Your Peak moment

> {Single strongest achievement as a spoken sentence — natural language, not a resume bullet. Include the quantified result.}

*Why this works:* {One sentence on why this directly addresses the JD's top priority.}

---

## 3. STAR story prompts

For each theme, use STAR+Spark: Situation/Task (20%), Action — use "I" not "we" (60%), Result with a number (20%), Learning/Spark (1 sentence).

### Theme 1: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** Prepare a story about {specific situation} where you {action}. End with what you learned or would do differently.

### Theme 2: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** Prepare a story about {specific situation} where you {action}. End with what you learned or would do differently.

### Theme 3: {Theme from JD}
**Source bullet:** "{Relevant resume bullet}"
**Prompt:** Prepare a story about {specific situation} where you {action}. End with what you learned or would do differently.

---

## 4. Company research findings

### Business model and unit economics
{How they make money. Key revenue drivers and cost levers. What this implies about which data problems are highest stakes.}

### Competitive position
{Who their 2–3 closest competitors are. How the company differentiates. Whether they're incumbent or challenger, and what that means for data team priorities.}

### Data stack and engineering culture
{What you found about their data tools, stack, or engineering blog. If nothing found, say so.}

### Data team size and structure
{What you found about headcount, centralised vs. embedded, seniority. If nothing found, say so.}

### Recent news and growth signals
{Key funding, product launches, or expansion news. If nothing found, say so.}

### Role-specific insight
{The one targeted finding from Step 3D. If nothing found, say so.}

### Suggested opening hook
> "{Specific, direct sentence referencing one real finding. Lead with the fact, then the capability. Example: 'You hit $400M ARR in eight months. That growth means your MRR model is complex. That's the problem I solve.'}"

---

## 5. Opening and closing

### Opening (first 60 seconds)
Use the suggested hook from Section 4. Tone: grounded, European directness. Lead with a specific fact or number. Name the problem plainly. End with a statement of capability — short, confident, no flourish.

### Closing statement
> {Draft 1–2 sentence closing from Step 4D. Tone: direct and grounded. No "genuinely excited" or "move forward with the team". Instead: concrete capabilities, availability, confidence. Example: "I've built the exact thing you need. I'm in Berlin, ready to start. When do we move forward?"}

---

## 6. Questions to ask

Pick 1–2 for the call; have the others ready if the conversation opens up. Each must be specific to this company — not a generic template.

### Impact / success definition
> "{Question anchored to a concrete JD signal or research finding — what does great look like in 6–12 months for this role?}"

### Team problem
> "{Question about the hardest unsolved data problem right now — framed around something specific observed in the JD or research}"

### Business / strategy
> "{Question that shows you understand their business model or competitive position — a tension or trade-off you've noticed}"

### Ways of working
> "{Question about how decisions get made or what a specific JD culture signal actually looks like day-to-day}"

*Why specific questions work:* Generic questions ("what does success look like?") are forgettable. Questions that reference something real signal preparation, business understanding, and that you're already thinking about the role — not just trying to get it.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story — prevents rambling, gives recruiter time to finish notes.
- **Use "I" not "we"** — recruiters assess your individual contribution.
- **Salary / notice period** — state your range confidently. If pushed early: "I'm flexible depending on the full package — can you share the budgeted range for the role?"
```

---

## Step 5b — Self-critique pass (MANDATORY before saving)

After drafting, review the document against this checklist. Fix any failures before writing the file.

**Research quality:**
- [ ] Every specific fact in Section 4 has a source URL — or is explicitly marked as "not found"
- [ ] The opening hook in Section 4 contains a real number or named fact — not a generic observation about their industry
- [ ] Business model and competitive position sections contain actual claims, not hedged non-answers like "they operate in a competitive space"

**STAR story prompts:**
- [ ] Each theme is genuinely distinct — they don't all reduce to "built a data pipeline"
- [ ] Each source bullet is the strongest match for that theme, not just the first bullet encountered
- [ ] Each prompt ends with a reflection or learning question ("what would you do differently?")

**Peak moment:**
- [ ] The peak moment is phrased as natural speech, not a resume bullet ("I cut pipeline runtime from 6 hours to 40 minutes, which unblocked the finance team's month-end close" — not "Optimised pipeline performance by 89%")
- [ ] It contains a quantified result

**Questions:**
- [ ] The business/strategy question references something specific from 3E or 3F — not a generic "what are your priorities" question
- [ ] The ways-of-working question quotes or paraphrases a specific phrase from the JD

**Tone:**
- [ ] Closing statement contains no "excited", "thrilled", "passionate", or "look forward to hearing from you"
- [ ] Opening hook leads with a fact, not a compliment ("Your Series B signals aggressive expansion" not "I'm impressed by what you've built")

---

## Step 6 — Report

Tell the user:
- Output file: `{path}/recruiter-prep.md`
- The three STAR themes identified
- The selected Peak moment (one sentence)
- Two or three most useful research findings — and one finding that returned nothing (so the user knows what wasn't searchable)
