# Pedagogy Presentation — 10–15 minutes
**For:** Haikel (try-out)
**Topic:** Flipped classroom activity tied to ST2187 — Week 2: Univariate Data Visualisation and Descriptive Statistics

---

## Opening (1 min)

I'm going to walk you through a 90-minute seminar I designed for Week 2 of ST2187 — descriptive statistics and univariate data visualisation.

But I want to start with a question, not a slide:

> *"You have monthly crime rates for 50 years. You compute the mean, median, and standard deviation, then build a histogram. What's wrong with this approach?"*

Hold that. We'll come back to it.

The reason I open there is that question is on the quiz at the start of this class. And the answer — that histograms and summary statistics destroy the time dimension entirely — is the chapter's sharpest insight. Most students skim past it. The session is designed to make sure they don't.

---

## The Design Logic (2 min)

The flipped classroom structure does one thing: it separates *exposure to content* from *doing something hard with it*.

Before class, students read three targeted sections of Albright & Winston Chapter 2 — not the full chapter. The full chapter is 61 pages; I scope the reading to what's needed for the seminar, capped at roughly 1.5 times the in-class session length. Research on flipped classroom pre-work design (Fischer et al., 2023) is clear that full chapters, without that constraint, produce time that's spent rather than invested.

They also watch two short videos, complete a three-part tutorial, and submit a dataset of their own choosing from a country other than their own.

Then — after they've attempted the tutorial — they read a worked example. An annotated walk-through of the complete reasoning chain: dataset to summary statistics to a plausible claim to what that claim hides. They see the template before class, so the pair work in the session is interpretation, not guessing at what the task even requires.

That last design choice — the worked example — is grounded in cognitive load theory (Sweller, 1994). The reasoning chain in Part 3 is high element interactivity: you have to hold the statistics, the shape, the claim, and the critique simultaneously. Exposition alone doesn't build that schema. A worked example does.

The cross-national dataset constraint is deliberate. Forward College cohorts have 40+ nationalities. The dataset owner will know things the analyst pair won't — not just statistically, but contextually. That asymmetry is a teaching mechanism, not a nice-to-have.

---

## The Retrieval Quiz (2 min)

The session opens with a nine-question Mentimeter quiz. It runs easy to hard — deliberately. And it's doing two distinct jobs, which call for different instructor responses.

Questions one through six are **retrieval practice**. They confirm vocabulary: what's a median, what's the IQR, is a zip code numerical or categorical. The zip code question is a trap — it's stored as a number, but arithmetic on it is meaningless, so it's categorical. Students who skimmed the chapter will guess numerical. If the room splits on Q6, that's a 30-second clarification. If everyone gets Q1–Q6, I move on immediately — dwelling on what everyone knows wastes the retrieval benefit.

Questions seven through nine are **diagnostic**. This is where it gets interesting.

Q8: Two suppliers both produce parts with a mean diameter of 100mm. Supplier A has SD = 1mm; Supplier B has SD = 12mm. Which do you choose?

Q9 — back to the opening question — is the hardest. The answer is that summary statistics and a histogram tell you the *distribution* of monthly crime rates across 50 years. They tell you nothing about when those values occurred or in what order. The time dimension is gone.

If Q7–Q9 split the room, that's expected. But the right response isn't a mini-lecture — it's to let the pair work surface the answer, and name it in the debrief. Students who arrive at an insight through their own analysis retain it longer than students who are told.

The quiz format recurs every week. A meta-analysis specifically on introductory statistics courses (Farmus, Cribbie & Rotondi, 2020) found that weekly in-class quizzes significantly moderated the flipped classroom advantage. It's not a compliance check — it's the mechanism.

---

## A Concrete Moment: The Tutorial (2 min)

Let me show you what the pre-class tutorial looks like in practice.

One of the three tutorial problems gives students this:

> Weekly salaries for 10 employees: 1200, 1400, 1350, 1250, 1300, 1450, 1200, 1380, 4800, 1290.
> A new analyst suggests removing the €4,800 value to "clean up" the data before reporting. What would you say to them?

The wrong answer is "remove it because it skews the data." The right answer is: run both analyses, with and without the CEO's salary, and report both — with an explanation of why they were treated separately.

That question is sitting in the submitted tutorial when students walk in. Two or three volunteers present their solutions. Others push back. My role in that time is to prompt, not narrate: *"Does anyone want to push back on that? What would change if the dataset were larger?"*

Peer presentation activates the testing effect — retrieval strengthens retention more than re-reading. But more importantly, it surfaces who has the right instinct about outliers before they go into the pair work.

---

## Pair Work and Peer Discussion (3 min)

Each pair is assigned a classmate's submitted dataset — not their own.

One student is the **analyst**: runs the notebook, calls the numbers, produces the histogram and summary statistics. The other is the **sceptic**: questions every assumption, proposes alternative interpretations, pushes back on the claim. Roles swap at the twelve-minute mark.

Their deliverable is three things, no more:
1. A histogram and summary statistics table in Jupyter Notebook
2. One claim someone could plausibly make from these statistics — a government press release, a company headline
3. One thing that claim would be hiding

The role structure is intentional. In a Year 3 cohort that's been working together for two years, pair work can collapse into one person doing analysis while the other nods. Making the sceptic role explicit and non-optional means the interaction — which is the actual learning mechanism here, not the output — cannot be discharged by agreement.

The three-output constraint is also intentional. An open-ended task in 25 minutes produces anxiety, not analysis. Tight scope frees cognitive capacity for the harder interpretation work.

After 25 minutes, each pair presents in 2.5 minutes. The student who *submitted* the dataset responds: did they expect this? Does the critique match what they know about the context?

This is Vygotsky's zone of proximal development in practice. The dataset owner has real-world context the analyst pair doesn't. The analyst pair has statistical framing the owner hasn't applied. Neither is complete alone. The discussion is where they integrate.

---

## The Debrief (1 min)

The session closes with one sentence from each pair:

*"What did we learn today about how to describe a dataset — and what are the limits of that description?"*

I synthesise: descriptive statistics compress information. Compression is useful. Compression also hides things. A good analyst knows both.

Then one harder question — addressed to the room, not the output:

*"Did you actually change your mind today, or did you just confirm what you already thought?"*

This is the Year 3 version of that question. A first-year cohort in Lisbon needs scaffolding around giving and receiving feedback — they're still building the trust norms. A third-year cohort in Berlin has two years of shared history. The risk isn't insufficient trust; it's a cohort so fluent in each other that they stop updating on new evidence. One exchange on this, handled briefly, is enough.

Then one question to leave with — not to answer today:

*"What if your variable has a time dimension? If I gave you 65 years of monthly crime rates and asked you to summarise them — would mean, median, and SD be meaningful?"*

That's the answer to the question I opened with. And it's the thread that runs through to Week 13.

---

## Why This Fits Forward College (1 min)

Nothing in this session is passive. There's no lecture. Students do the intellectual work — before class and in it.

The flipped structure isn't a technique added on top of a conventional class. It's the only structure that makes the Bloom's levels possible. You cannot do analysis and evaluation if the seminar is still delivering content.

The pre-work is scoped, sequenced, and includes a model of the reasoning students are about to do. The quiz is diagnostic and recurs every week. The pair work has structure that makes the interaction non-optional. The debrief closes the loop and plants one unanswered question.

Each of those choices has a reason. The cross-national dataset constraint, the analyst/sceptic roles, the single bridge-forward question — they're not add-ons. They're the design working.

---

*Total: ~12 minutes at a moderate pace, leaving 2–3 minutes for questions.*
