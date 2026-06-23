# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 20: Full Analysis 2 — Model and Infer
**Format:** 90-minute seminar, 12–15 students in groups of 3–4

---

## Learning Objectives

By the end of this session, students will be able to:
- Apply an appropriate statistical model or test to their Week 19 analytical question and justify the choice
- Interpret the output of that model in terms of the business or policy question — not just the statistical output
- State the assumptions required for the model to be valid and evaluate whether the data meets them
- Receive and respond to critical feedback on their modelling choices from peers

This is Week 2 of the four-week full analysis cycle. Groups return with a model or test applied to the question refined in Week 19. The session is structured around presenting, interpreting, and defending modelling choices.

---

## Before Class (Student Pre-Work)

**Group preparation (between Week 19 and Week 20):**

Each group must:
1. Choose an appropriate analytical method from the course (t-test, chi-square test, regression, confidence interval, time series, simulation — or a combination)
2. Apply the method to their dataset
3. Write a 1-page group brief:
   - Method chosen and why
   - Key result (one number or interval or model equation)
   - Interpretation in plain language
   - One assumption the method requires and whether the data satisfies it

**Submit the brief before class** so the instructor can review and identify the most productive challenges for Part 3.

**Opening question planted in Week 19 (students should have thought about this):** "What would make you wrong?"

If a group ran a t-test and found a statistically significant difference, what conditions would make that conclusion incorrect? (Sample not random, test assumption violated, effect size too small to matter practically, confound not controlled.) Students who can answer this question have understood their model.

---

## In-Class Session (90 minutes)

### Part 1 — Opening Check-In (5 minutes)

One question to the room:

*"Did your model answer your question from Week 19? If not — did the question change, or did the model reveal a problem with the question?"*

This is not rhetorical. Some groups will have found that their question wasn't answerable with the data they have (e.g., they wanted to test causation but only have observational data). Others will have found that their original question was too vague and the model forced them to be specific. Both outcomes are productive — the question should acknowledge them.

---

### Part 2 — Group Presentations: Model and Result (30 minutes)

Each group has 7–8 minutes:
1. **Recap the question** (30 seconds — the refined version from Week 19)
2. **Method and justification** (2 minutes): what method did you use, why this method, why not another?
3. **Key result** (2 minutes): what did the model find? Present the number, the interval, or the coefficient — with its uncertainty
4. **Plain-language interpretation** (1 minute): "based on this analysis, the data suggests ___. We are uncertain about ___ because ___."
5. **Assumption check** (1 minute): what assumption did the method require? Does the data satisfy it?

**The class asks one question per group.** In Week 20, questions should be about the model choice and assumptions, not the description:
- "Why a t-test and not a regression?"
- "Your data is clustered by region — does that violate the independence assumption of your test?"
- "You used a 5% significance level. If you'd used 1%, would your conclusion change?"

---

### Part 3 — Instructor-Led Challenge Round (25 minutes)

The instructor, having read the group briefs before class, poses one prepared challenge to each group. These are targeted: based on what the instructor identified as the weakest assumption or the most consequential modelling choice in each brief.

Examples of prepared challenges:
- **To a group that ran a simple regression without checking residuals:** "Your R² is 0.72. Can you show me a residual plot? What does it look like?"
- **To a group that ran a t-test on non-random data:** "You said the data came from a convenience sample of volunteers. Does the t-test give you a valid inference about the general population?"
- **To a group that ignored multiple testing:** "You tested 8 variables and found 2 significant at p < 0.05. With 8 tests, how many significant results would you expect by chance?"
- **To a group with perfect statistical significance but tiny effect size:** "Your p-value is 0.003 and your slope is 0.0012. Is this effect large enough to matter for any decision?"

Groups have 3 minutes to respond to the challenge before the class can add follow-up questions.

The tone is adversarial in the most constructive sense: these are the questions a real stakeholder or regulator would ask. Students who can respond clearly are ready for Week 21 (the formal challenge round) and Week 22 (the external evaluator).

---

### Part 4 — Group Revision Time (20 minutes)

Groups have 20 minutes to revise their analysis in response to the feedback. Revision can mean:
- Checking and presenting a residual plot that was missing
- Rerunning the model on a subset of the data to address the convenience sample concern
- Adding a Bonferroni correction for multiple testing
- Adding an effect size measure (Cohen's d, R²) alongside the p-value

Not all revisions are solvable in 20 minutes. The outcome is not a perfect analysis — it is a specific, documented list of what changed and what still needs to change before Week 22.

**Group log entry for this week:**

"We applied ___ to answer the question ___. The result was ___. The most important challenge we received was ___. We responded by ___. The limitation we have not yet addressed is ___."

---

### Part 5 — Debrief (10 minutes)

**Close the loop:**

*"What did the model tell you that the description couldn't? And what did the model still not tell you?"*

This is the core distinction of the inference block (Weeks 11–15) applied to real data. Description compresses. Models are conditional — their output depends on assumptions. The question is whether the assumptions are defensible.

**Preview of Week 21:**

> *"Next week is the challenge round. Every group will have their analysis formally challenged by another group. You should come prepared to defend your choice of method, your interpretation, and your answer to 'what would make you wrong?' The group whose challenge is most incisive — not the harshest, but the most analytically precise — will be named."*

This notice should sharpen both the presenting groups and the challenging groups for Week 21.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Pre-submission brief (1 page, four elements) | Rosenshine (2012): checking for understanding before the class; the instructor who reads all briefs before Week 20 can prepare targeted challenges rather than generic feedback |
| Instructor-led challenge round (not peer-only) | Black & Wiliam (1998): formative assessment with targeted feedback; instructor challenges are more precise than peer challenges at this stage — peers will be more effective challengers in Week 21 once they've seen the instructor's model |
| Revision time within the session | Constructivist learning (Piaget, 1952): knowledge is built through action; groups who revise their analysis in real time are doing more learning than groups who receive feedback and wait until next week to act |
| "What would make you wrong?" as the running question | Week 21 is built around this question; establishing it as the standard in Week 20 gives groups a week to prepare a genuine answer |
| Group log entry tracks what changed between sessions | Weeks 19–22 are a narrative arc; the log entries document the evolution of the analysis; at Week 22, groups should be able to say "we started with ___ and ended with ___ because ___" |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Opening check-in | 5 min | Did the model answer the question? |
| Group presentations | 30 min | 7–8 min per group; one class question per group |
| Instructor-led challenge round | 25 min | One prepared challenge per group; 3 min response + class follow-up |
| Group revision time | 20 min | Document what changed; update log entry |
| Debrief | 10 min | What did the model add? Bridge to Week 21 challenge round |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. The instructor challenge round may feel intimidating.

A targeted, public challenge to a group's weakest assumption can feel like an attack rather than feedback. Year 3 students have had two years of feedback practice, but a statistical challenge is different from a presentation feedback.

**Resolution:** the instructor models the tone in the first challenge: direct, precise, and not personal. "The question is about the method, not the people. If the method has a gap, we're going to find it now, not in Week 22 in front of an external evaluator." Naming the purpose — "this is practice for the harder challenge you'll face" — reframes it as preparation.

---

### 2. Some groups may not have produced a meaningful model.

If a group ran a correlation and reported r = 0.45 as their "model," they have not done inference. A correlation coefficient is a descriptive statistic, not a model. The group brief should have caught this — but it may not.

**Resolution:** the instructor challenge for these groups: "What is the null hypothesis you're testing? What's the p-value? Is r = 0.45 statistically significant at n = 30?" This redirects them from description to inference without requiring a full restart. The revision time (Part 4) can be used to run the actual significance test.

---

### 3. Groups with significant p-values may confuse statistical significance with practical significance.

A group that finds p = 0.001 may conclude their result is "highly significant" without asking whether the effect size is meaningful for any decision.

**Resolution:** the instructor should ask for every significant result: "What is the effect size? A difference of 2.3mm in bolt diameter — is that operationally meaningful?" For business analytics students, the answer to "does it matter?" is always "it depends on the decision context" — and specifying that context is the analyst's job.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Chi, M.T.H., de Leeuw, N., Chiu, M.H. & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Piaget, J. (1952). *The Origins of Intelligence in Children.* International Universities Press.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Rosenshine, B. (2012). Principles of instruction. *American Educator*, Spring 2012. ERIC EJ971753.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
