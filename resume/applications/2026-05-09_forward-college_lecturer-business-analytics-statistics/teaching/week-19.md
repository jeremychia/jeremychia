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

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Materials, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed.

"No reading this week" misses the one part of the textbook written for exactly this block: **Appendix A, "Statistical Reporting" (pp. A-1–A-18)** — planning a report, developing it, and the be-clear/be-concise/be-precise standards, with worked examples of full statistical reports (A-3). Assign A-1 and A-2 now (≈8 pages); the example reports in A-3 become the reference models for Week 22's presentations. This is also the only place the textbook shows what a *finished* analysis looks like — which is the entire subject of Weeks 19–22.

Also worth a pointer: **Chapter 16's model gallery and Chapter 2/3's chart guidance** as a menu ("if your question is an inventory/waiting/churn question, Chapter 16 has a template"), so groups don't reinvent structures the book already provides.

## 2. Extended Materials (with answers) — question-quality drill and gates

**E1 — Question triage drill (10 min, printable; run as a warm-up or give as pre-work).** Rate each against the three criteria (specific / testable-with-course-methods / decision-relevant):

1. "What affects apartment rents in Berlin?" — **Fails specificity** (no variables, no comparison); salvage: "Do listed rents per m² differ significantly between flats inside and outside the S-Bahn ring, controlling for size?"
2. "Is Berlin hotter in summer than winter?" — Specific, testable, **fails decision-relevance** (the plan's own example; no decision changes).
3. "Does the new bike lane *cause* reduced traffic accidents?" — Specific and relevant, **fails testability as stated** (causal claim; observational data) — acceptable if reworded as an association question with the causal limitation named (the Part 3 protocol).
4. "Is the mean processing time for citizenship applications above the government's 90-day target?" — **Passes all three** (one-sample test, clear threshold, clear action).
5. "Can we predict which library branches will see falling visits?" — Borderline: testable (regression), relevant, but "predict" needs a stated accuracy criterion to be specific.
6. "Do districts with more trees have less crime?" — Testable as correlation; decision-relevance weak until a confound plan is stated (income — Week 15's exact case); good refinement candidate.
7. "How satisfied are Singaporeans with public transport?" — **Fails testability with this data** unless a survey variable exists; a dataset of ridership counts cannot answer a satisfaction question — the classic variable-vs-concept gap.
8. "Did average waiting times change after the 2024 policy reform?" — Passes if the data spans the reform date; before/after two-sample structure; limitation: time confounds (anything else that changed in 2024).

The drill calibrates the room *before* groups assess their own questions — the same worked-example-first logic the course applies everywhere else.

**E2 — Dataset gate (instructor screen between Weeks 18 and 19).** A dataset is admissible if: ≥ ~200 rows (enough for inference); has at least one numeric and one categorical/grouping variable (so both test families from Weeks 12–15 are available); has a data dictionary or interpretable column names; open licence; and the group can answer Week 8's three provenance questions (how collected / who's in it / collected for what). Groups submit this checklist with the metadata — it converts Design Challenge 3's "accountability mechanism" into a concrete pass/fail gate and prevents Week 20 discovering the dataset can't support any test.

**E3 — Pre-mortem prompt (5 min, end of Part 3).** "It is Week 22 and your analysis failed to convince anyone. Write the two most likely reasons." Typical honest answers — "our question quietly became a causal claim," "our dataset couldn't measure the thing we cared about" — are precisely the failure modes Parts 3–4 exist to catch; writing them down makes the group its own first challenger (and seeds Week 21's challenge session).

## 3. Alternative In-Class Activities (additional options)

**A. Instructor-modelled refinement (8 min, before Part 3).** The instructor takes a deliberately vague question ("what drives café success in Berlin?") and refines it live through the three criteria, thinking aloud, ending at a testable one-sentence version with its limitation stated. Every week of this course models worked examples before independent practice — except this one, where the skill (question formulation) is newest. Eight minutes closes that gap.

**B. Question speed-dating (12 min, Part 3 alternative opening).** Before groups settle, each member pitches one candidate question to a rotating partner from another group in 60 seconds; the partner's only job is to repeat the question back in their own words. Questions that can't survive being repeated back aren't specific yet. Three rotations, then groups convene holding the survivors.

**C. Stakeholder pitch test (5 min, Part 3 close).** Each group delivers its refined question to the instructor playing a busy commissioning manager, who responds only with "so what will you tell me to *do* differently?" — the decision-relevance criterion, enforced in character.

**D. Data-dictionary treasure hunt (pre-work upgrade).** Require each group's submission to include a ten-line data dictionary (variable, type, unit, missing-value count, one anomaly noticed). Groups who cannot produce it discover their dataset problem in Week 19, not Week 20 — and the anomaly line almost always seeds the descriptive presentation.

## 4. Critique of the Lesson Plan

**What works (keep):** the three-criteria contract (specific/testable/decision-relevant) as the block's spine; the domain-exclusion constraint with its honest Design Challenge 4 defence; the cross-group challenge's three-output structure; "what would make you wrong?" planted two weeks before it's asked; the timing table actually sums to 90 (alone among the lab-format weeks).

**Problems, reasons, and fixes:**

1. **The external evaluator exists only in this file.** Part 5 promises Week 22 will include "an external evaluator," but the Week 22 plan's audience is the class and instructor only. *Fix:* decide once. Inviting one is strongly aligned with Forward's Berlin Year 3 professional-exposure model (a Beta-House-style collaborator — see the student-voice research — would be ideal), but it needs Week 22 logistics (brief for the guest, adjusted Q&A order). If not, cut the promise here — students plan differently for external audiences.
2. **Group formation "assigned in Week 18" is not in the Week 18 plan.** Nothing there allocates groups, applies the domain constraint, or triggers dataset selection. *Fix:* add a 5-minute logistics block to Week 18's debrief (groups announced, constraint explained, E2 gate issued) — otherwise this week's pre-work has no launch point.
3. **The pre-work drops the course's own provenance standard.** Week 8 planted three habitual questions (how collected / who's in and out / collected for what) explicitly "for Weeks 19–22 when it becomes a marking criterion" — but the submission here asks only for metadata and three questions. *Fix:* fold the provenance questions into the submission (E2 does this).
4. **Part 2's arithmetic only works with discipline.** Four groups × (5–6 min + a class question) = 26–30 minutes in a 25-minute slot. *Fix:* cap at 5 minutes hard (the internal breakdown sums to 4:20, so it's feasible), or with four groups borrow 5 minutes from Part 5.
5. **No worked example of the target skill (see Activity A).** Question formulation is the one skill this session teaches, and it's the only skill in the course taught without a model.
6. **Descriptive-quality feedback has no channel.** Part 2's charts and statistics get no structured critique (the class question must target the analytical question) — yet Week 2's claim/hide standards and Week 7's design-choice standards are exactly the rubric these plots should meet. *Fix:* one line in Part 2: the instructor annotates each group's charts against the Week 2/7 checklist in written feedback after class; keeps the session focused on questions without letting the visual craft regress.
