# Lesson Brief
## ST2187 — Week 2: Univariate Data Visualisation and Descriptive Statistics
**Format:** 90-minute in-person seminar · 12–15 students · Berlin (Year 3 cohort)
**Prepared for:** Haikel — pedagogy try-out presentation

---

## What this session is trying to do

Descriptive statistics is Week 2. Students have just read the chapter and watched videos at home. They can compute a mean. The seminar is not for that.

The session is for the harder work: interpreting what the numbers mean, constructing a claim from them, and identifying what that claim hides. Those are Bloom's levels 4–5 — analysis and evaluation. They are only reachable in 90 minutes because computation was offloaded to the pre-work.

**By the end, students can:**
- Interpret descriptive statistics for a real dataset they have never seen
- Construct a plausible claim from summary statistics
- Identify what that claim obscures — and why that matters

---

## Before class (student pre-work)

| What | Why |
|------|-----|
| Read Albright & Winston Ch. 2 — three targeted sections only (§2.1, §2.3, §2.4) | Full chapter is 61 pages; scoped to what the seminar actually requires |
| Watch two short videos (~20 min total) | Exposition at own pace; students can rewind |
| Complete tutorial T1–T3 and submit written answers | Confirms mechanical competence before class; surfaces who struggled |
| Submit a dataset from a country other than their own | Creates the knowledge asymmetry that drives Part 4 |
| Read worked example — *after* the tutorial, not before | Provides the reasoning template for Part 3; sequenced after attempt to avoid false confidence |

**The worked example** walks through an air quality dataset (mean AQI = 48, median = 41, SD = 22) — showing how to move from numbers to a plausible claim to what the claim hides. This is the cognitive template for Part 3. Students who have seen it once will engage as analysts; students who haven't will guess at what the task requires.

---

## In class (90 minutes)

### Part 1 — Retrieval quiz · 10 min
*Tool: Mentimeter*

Nine questions, easy to hard. Two distinct jobs:

- **Q1–Q6 — retrieval practice.** Vocabulary and recall. If correct: move on immediately. If badly split: 30-second clarification, then slow down Part 3.
- **Q7–Q9 — diagnostic.** Application and edge cases. Splits here are expected. The right response is not a mini-lecture — it is to let Part 3 surface the answer, then name it in the debrief.

Hardest question (Q9): *"You have monthly crime rates for 50 years. You compute the mean, median, SD, and build a histogram. What is fundamentally wrong?"* Answer: summary statistics and histograms destroy the time dimension. Most students will have skimmed past this in the chapter. The session is designed to make sure they don't leave without it.

The quiz recurs every week. Farmus, Cribbie & Rotondi (2020) found weekly in-class quizzes significantly moderated the flipped classroom advantage in introductory statistics (g = 0.43).

---

### Part 2 — Tutorial review · 15 min + 10 min buffer
*2–3 volunteers present; others push back*

Instructor role: prompt, not narrate. *"Does anyone want to push back on that? What would change if the dataset were larger?"*

The buffer is named and explicit — it absorbs slow starts, extended debate, or re-covering basics if the quiz showed gaps. It is not filled with additional content.

Key question to surface here: T1(g) — a new analyst suggests removing the CEO's €4,800 salary to "clean up" the data. The wrong answer is "remove it." The right answer: run both analyses, report both, explain why they were separated. Students who write "remove it because it skews the data" haven't read the chapter carefully enough. Surfacing this before Part 3 primes students not to make the same mistake with their own data.

---

### Part 3 — Pair work · 25 min
*Each pair assigned a classmate's dataset — not their own*

**Roles (explicit, non-optional):**
- **Analyst** — runs Jupyter Notebook, produces histogram and summary statistics table, calls the numbers
- **Sceptic** — questions every assumption, proposes alternative interpretations, pushes back on the claim
- Roles swap at the 12-minute mark

**Deliverable — three things, no more:**
1. Histogram + summary statistics table
2. One plausible claim from the statistics (press release, company headline, news story)
3. One thing that claim hides

The role structure exists because a Year 3 Berlin cohort has two years of shared history. Pair work in a high-trust cohort can collapse into agreement — one person analyses, the other nods. Making the sceptic role explicit makes the interaction non-optional. The constrained deliverable prevents the anxiety of open-ended tasks in 25 minutes.

---

### Part 4 — Peer discussion · 20 min
*~2.5 minutes per pair*

Each pair presents: one sentence of context, the claim, what it hides. The student who *submitted* the dataset responds: did they expect this? Does the critique match what they know?

This is the highest-value exchange in the session. The dataset owner has real-world context the analyst pair doesn't. The analyst pair has statistical framing the owner hasn't applied. With 40+ nationalities in the cohort, that asymmetry is real — a dataset from Singapore or Portugal carries contextual knowledge that a German-Swedish pair of analysts won't have.

---

### Part 5 — Instructor debrief · 10 min

One sentence from each pair: *"What did we learn about how to describe a dataset — and what are the limits of that description?"*

Synthesis: descriptive statistics compress information. Compression is useful. Compression hides things. A good analyst knows both.

Then the Year 3 question — harder than a first-year cohort gets:
> *"Did you actually change your mind today, or did you just confirm what you already thought?"*

A Lisbon Year 1 cohort needs scaffolded feedback norms — they're still building trust. A Berlin Year 3 cohort has two years of shared history; the risk is fluency collapsing into confirmation. One exchange on this, briefly, is enough.

Close with one unanswered question:
> *"What if your variable has a time dimension? If I gave you 65 years of monthly crime rates — would mean, median, and SD be meaningful?"*

The answer is no. It connects back to Q9 from the quiz and plants the thread that runs through to Week 13 (time series and forecasting).

---

## After class (student post-work · ~30 min)

Students post a short reflection to the LMS, written in the style of a LinkedIn post or data community update — not an essay. One to three paragraphs, a headline, something a non-specialist could engage with. Other students leave at least one comment: a pushback, a follow-up question, a connection to their own dataset.

The social-media format is deliberate: writing for a public audience forces clarity, strips jargon, and requires standing behind a claim. The cohort audience (not the internet) means the comment thread is substantive rather than performative.

---

## Why the flipped classroom here

The alternative — spending seminar time on content delivery — would leave no room for Parts 3 and 4, which are where the learning at levels 4–5 actually happens. A conventional seminar on descriptive statistics produces students who can define a standard deviation. This session produces students who can catch a government press release misusing one.

The design is grounded in:
- Farmus, Cribbie & Rotondi (2020) on flipped classroom effectiveness in introductory statistics — DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Sweller (1994) on cognitive load and worked examples for high element interactivity material — DOI: [10.1016/0959-4752(94)90003-5](https://doi.org/10.1016/0959-4752(94)90003-5)
- Fischer et al. (2023) on pre-work design and the 1.5× time cap — DOI: [10.1186/s12909-023-04325-x](https://doi.org/10.1186/s12909-023-04325-x)
- Kalyuga et al. (2003) on expertise reversal — why the worked example is optional for confident students — DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)

---

*This brief is the handout version. The verbal presentation covers the same arc in 10–12 minutes, opening with Q9 from the quiz and closing by answering it.*
