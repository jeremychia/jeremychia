# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 19: Full Analysis 1 — Describe and Question
**Format:** 90-minute seminar, 12–15 students in groups of 3–4

---

## Learning Objectives

By the end of this session, students will be able to:
- Select a real, publicly available dataset and frame a specific, answerable business or policy question
- Produce a complete descriptive analysis of that dataset: distribution, summary statistics, visualisations
- Identify what the descriptive analysis reveals and what it cannot answer
- Formulate a precise analytical question that a model or test could answer — one that goes beyond what description alone can tell you

This is Week 1 of the four-week full analysis cycle (Weeks 19–22). No new technical content is introduced. The entire session is devoted to question quality: what question is worth asking, what description is sufficient for framing it, and what the limits of description are.

---

## Before Class (Student Pre-Work)

**No reading this week.** All pre-work is group preparation.

**Group formation and dataset selection:**

Groups of 3–4 are assigned in Week 18. Each group selects a real dataset from an open data source:
- [daten.berlin.de](https://daten.berlin.de) — Berlin Open Data
- [data.gov.sg](https://data.gov.sg) — Singapore Government Data
- [datos.gob.es](https://datos.gob.es) — Spanish Government Open Data
- [data.gov.uk](https://data.gov.uk) — UK Open Data
- [data.worldbank.org](https://data.worldbank.org) — World Bank Data

**The constraint:** the dataset must be from a domain none of the group members specialise in. A group of finance students cannot analyse a financial dataset; an engineering student cannot lead a transport dataset analysis. This constraint is intentional — it forces reliance on each other's analytical skills rather than domain expertise.

**Pre-class preparation:**
1. Download the dataset and clean it sufficiently to load in Python (handle missing values, confirm data types)
2. Run `df.describe()` and produce at least two plots (one distribution, one relationship)
3. Write three questions: one descriptive (what does the data show?), one analytical (what hypothesis could you test?), one that goes beyond the data (what would you need to know that this dataset cannot tell you?)

**Submit before class:** the dataset metadata (source, size, variable names) + the three questions.

---

## In-Class Session (90 minutes)

### Part 1 — Opening Question (5 minutes)

No quiz. The instructor opens with one question for the room:

*"If I gave you the best possible descriptive analysis of this dataset — every chart, every summary statistic — what would you still not know? What question could not be answered by description alone?"*

Two or three students respond briefly. This primes the session: description is necessary but not sufficient for decisions. The rest of the session is about identifying what "sufficient" requires.

---

### Part 2 — Group Presentation: Dataset and Description (25 minutes)

Each group has 5–6 minutes to present:
1. **What is the dataset?** (source, size, time period, variables) — 60 seconds
2. **What does the description show?** (at least two charts, key statistics) — 2 minutes
3. **What does the description NOT show?** — 1 minute
4. **What is your analytical question?** — 1 minute

**The fourth element is the most important.** A good analytical question:
- Is specific (not "what affects X" but "is there a statistically significant difference in X between group A and group B?")
- Is answerable with the data or with additional data that could plausibly be collected
- Is decision-relevant (answering it should change what someone does)

**After each presentation: the class asks one question.** The question must be about the analytical question, not the description — "Is that question testable with this data?" or "What assumption are you making about the population the data represents?"

---

### Part 3 — Question Refinement Workshop (25 minutes)

Groups have 20 minutes to refine their analytical question based on the feedback from Part 2. The instructor circulates and pushes each group on:
- **Specificity:** "is there a relationship" is too vague. "Is the correlation between X and Y statistically significant at the 5% level?" is specific.
- **Testability:** can this actually be tested with the methods from the course? If the question requires causal inference beyond regression, say so explicitly — "this question would require a randomised experiment; with this data, we can test whether X and Y are associated."
- **Decision relevance:** "knowing the answer would change the recommendation in the following way: ___"

After 20 minutes: each group states their refined question in one sentence. The instructor (and class) confirms whether it meets all three criteria. This is the contract for Weeks 20 and 21.

---

### Part 4 — Cross-Group Challenge (20 minutes)

Groups swap their analytical question with the adjacent group. The receiving group has 5 minutes to produce:
1. One alternative way of answering the same question (e.g., different test, different subset of data)
2. One condition under which the answer might be "no" even if the data suggest "yes"
3. One question that the original group's question does not answer but probably should

This exercise is designed to reveal blind spots. Groups who have been working with their own dataset for a week may not see the limitations that a fresh pair of eyes finds immediately.

After 5 minutes: each group reports back to the group whose question they reviewed. 3 minutes per exchange.

---

### Part 5 — Instructor Debrief (15 minutes)

**Close the loop:**

*"What separates a good analytical question from a vague one?"*

Answer: specificity, testability, and decision relevance. A question that satisfies all three can be answered with a methodology, evaluated against a standard, and acted on.

**Preview of Weeks 20 and 21:**

Week 20: groups return with a model or test applied to their refined question. They present the method, the result, and the interpretation. Week 21: other groups challenge the analysis. Week 22: formal presentation to an audience that includes an external evaluator.

*"By Week 21, someone will ask: 'What would make you wrong?' You should be able to answer that. If you can't, your analysis is not finished."*

**Group log entry (replaces individual LMS post for Weeks 19–22):**

Groups write a 1-paragraph log entry: "This week we decided on ___. We refined our question from ___ to ___ because ___. The main thing we still need to figure out before Week 20 is ___."

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| No new technical content in Weeks 19–22 | Lovett & Greenhouse (2000): integrative practice is distinct from skill acquisition; mixing new content and integration tasks in the same session fragments attention; these four weeks are entirely for application and synthesis |
| Domain constraint for dataset selection | Vygotsky (1978): ZPD — complementary knowledge within groups; forcing students to work outside their domain expertise ensures the group must reason analytically rather than rely on background knowledge |
| Three-criteria framework for analytical questions (specific, testable, decision-relevant) | Ausubel (1968): explicit advance organiser for what "good" means; without the criteria, students present vague questions and don't know how to improve them |
| Cross-group challenge in Part 4 | Chi et al. (1994): self-explanation and peer critique; a fresh group reviewing a question sees limitations the original group normalised; this is the mechanism for improving question quality |
| Group log entry replaces individual LMS post | Weeks 19–22 are group work; the group's collective reasoning is the relevant artefact, not individual reflection; the log entry tracks what changed between sessions |
| Week 19 planted in bridge forward from Week 15 | Bjork (1994): forward testing effect — students who were told "you'll own the full problem in four weeks" from Week 15 arrive at Week 19 with a sense of purpose |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Opening question | 5 min | Prime the session: what can description not tell you? |
| Group presentations: dataset and description | 25 min | 5–6 min per group; one class question per group |
| Question refinement workshop | 25 min | 20 min group work + 5 min one-sentence refinement to class |
| Cross-group challenge | 20 min | 5 min per receiving group + 3 min per exchange |
| Instructor debrief | 15 min | Three criteria; Week 20–22 preview; group log |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Group dynamics established over 18 weeks may produce social loafing or one-person domination.

By Week 19, some groups will have a de facto leader and other members who contribute less. In a 4-week arc, this imbalance compounds.

**Resolution:** the cross-group challenge in Part 4 requires every group member to engage with another group's question. If a group's presentation in Part 2 clearly reflects one person's work (one person presents, others look passive), the instructor can allocate the cross-group challenge tasks by person, not by group. "Group A's question goes to member 3 of Group B, not the full group."

---

### 2. Students may select datasets that are technically tractable but analytically trivial.

A dataset with a clear answer (e.g., "is Berlin hotter in summer than winter?" — obviously yes) satisfies the "testable" criterion but not the "decision-relevant" one. Students may gravitate toward datasets where the answer is obvious or where the data is particularly clean.

**Resolution:** the three-criteria framework addresses this directly. "Is your question decision-relevant?" forces students to state what would change if the answer were different. For the seasonal temperature question: the answer doesn't change any decision a reasonable actor would make. For "Is the difference in summer vs. winter ozone levels large enough to warrant policy intervention?" — the answer might.

---

### 3. Week 19 presentations may vary widely in readiness — some groups will have done the pre-work and some won't.

The pre-submission (dataset metadata and three questions) is the accountability mechanism. Groups who arrive without it will have nothing to present in Part 2.

**Resolution:** the pre-submission is required by class time the day before. Students who haven't submitted are given 10 minutes at the start of Part 3 (question refinement) to write their questions — but they lose the benefit of Part 2 feedback. This is not punitive; it is a natural consequence that the group log entry should address honestly: "We arrived without a prepared dataset."

---

### 4. The domain constraint (no expertise allowed) may frustrate high-achieving students.

A student with a background in public health may feel constrained by being assigned a transport dataset. The constraint exists for good reason — but some students will see it as arbitrary.

**Resolution:** frame it explicitly: "Your background in public health is an asset in Week 22 (the audience will ask questions about implications) and in Week 21 (critiquing your own analysis from the perspective of someone who knows the domain). For Weeks 19–20, the constraint forces you to reason from the data, not from background knowledge. That's the skill we're testing."

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Chi, M.T.H., de Leeuw, N., Chiu, M.H. & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
