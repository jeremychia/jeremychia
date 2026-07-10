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

The tone is adversarial in the most constructive sense: these are the questions a real stakeholder or regulator would ask. Students who can respond clearly are ready for Week 21 (the formal challenge round) and Week 22 (the formal presentation and Q&A).

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

**Resolution:** the instructor models the tone in the first challenge: direct, precise, and not personal. "The question is about the method, not the people. If the method has a gap, we're going to find it now, not in Week 22 in front of the full audience." Naming the purpose — "this is practice for the harder challenge you'll face" — reframes it as preparation.

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

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Materials, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed.

- **Appendix A-2b ("Developing a Report") and A-2c–e (clear/concise/precise)** are the writing standard for this week's one-page brief — assign alongside the brief template (Week 19's supplement makes A-1/A-2 the block reading; this is where it pays off).
- The method-selection step (pre-work item 1) should explicitly reference the course's own selection artefacts: the **Week 5 distribution decision tree**, the **Week 13 test-triage drill** (one-sample t / two-sample t / paired t / z-proportion / chi-square / "none — assumptions violated"), and **Week 12's which-interval triage**. Groups choosing methods from a menu they built themselves is the payoff of those exercises.

## 2. Extended Materials (with answers)

**E1 — Method-matching drill (10 min warm-up or pre-work, with answers).** For each, name the method and its most fragile assumption:

1. "Do flats east and west of the former Wall differ in mean rent per m²?" — **Two-sample t-test**; fragile: independence within groups (rents cluster by neighbourhood) and equal-variance choice.
2. "Is the proportion of delayed trains above the franchise's 10% ceiling?" — **One-sample z-test for a proportion**; fragile: whether logged delays are a complete/random record (provenance).
3. "Same 40 stores, revenue before vs after the levy" — **Paired t-test** (Week 13 T8); fragile: no contemporaneous shock other than the levy (time confound).
4. "Does bike-counter volume relate to temperature, controlling for weekday?" — **Multiple regression with a weekday dummy**; fragile: autocorrelated residuals in daily data (Week 15 T10).
5. "Is voucher redemption independent of district?" — **Chi-square independence**; fragile: expected counts ≥ 5 in small districts.
6. "What range is plausible for mean processing time?" — **t confidence interval**; fragile: extreme skew with modest n (Week 11 T4).
7. "Will next quarter's ridership continue the recovery?" — **Holt-Winters / trend model with test-set validation and naive benchmark**; fragile: post-COVID regime stability.
8. "How likely is the project to exceed budget given uncertain costs?" — **Monte Carlo simulation**; fragile: input distributions and their correlations (GIGO).

**E2 — Assumption checklist per method (require it in the brief; the current brief asks for only one assumption).** Printable grid — each group marks every row **Met / Unmet / Unknown** with one line of evidence:

| Method | Must check |
|---|---|
| t-tests | random/representative sample; independence; normality or n large enough for the skew; (two-sample) variance assumption; (paired) pairing valid |
| Proportion z-test | np̂ and n(1−p̂) ≥ ~10; independence; denominator is the right population |
| Chi-square | expected counts ≥ 5; observations independent; categories exhaustive/exclusive |
| Regression | linearity (residual plot); independence (esp. time/cluster); homoskedasticity; no severe multicollinearity (VIF); outlier influence; omitted-variable story |
| Time series | regime stability; seasonality type; beat-the-naive check |
| Simulation | input distribution provenance; independence/correlation of inputs; N large enough for tail estimates |

"Unknown" is an honest and acceptable entry — it becomes the limitation statement. This grid *is* the instructor's challenge-preparation sheet: challenges in Part 3 target Unmet/Unknown rows.

**E3 — Effect-size companion (fills a course-wide gap the challenges assume).** Which effect size accompanies which result: mean difference in original units + Cohen's d (difference ÷ pooled SD; 0.2/0.5/0.8 as loose anchors, with Week 13's caveat that context beats conventions); regression: coefficient in real units + R²/ΔR²; proportions: absolute difference in percentage points (Week 13 T2's lesson: report the pp difference, not just the ratio); chi-square: Cramér's V. Rule for the brief: **no p-value may appear without its effect size beside it** — this operationalises Week 13's principle 5 as a submission requirement rather than advice.

## 3. Alternative In-Class Activities (additional options)

**A. Publish the red-team menu (0 min — a design change).** Post the four challenge archetypes (residuals unchecked / non-random sample / multiple testing / significance-vs-size) *with the pre-work*, not as surprises. Groups self-audit against them before submitting; the instructor then challenges whatever survives. This matches the course's own Week 22 philosophy ("criteria made explicit, not secret") and raises the floor of every brief — the gotcha version only teaches the group that got caught.

**B. Assumption audit wall (10 min, replaces the one class question in Part 2).** Every group's E2 grid goes on the wall; the class walks it and places one sticky note per group on the row they find least convincing. Part 3's challenges then start from the room's collective diagnosis — and quiet students participate through placement rather than speech.

**C. Robustness one-liner (formalises Part 4).** Every group must run exactly one robustness check in revision time — drop the outlier / change α to 0.01 / re-run on a subset / add the obvious control — and append one sentence to the log: "our conclusion [survived / changed] when ___." A conclusion that has survived one deliberate attack is qualitatively different from one that has never been attacked; this makes Part 4 produce evidence, not just edits.

**D. Method-swap thought experiment (5 min, debrief extension).** Each group answers: "If your method were banned, what would you use instead, and what would you lose?" (E.g. regression → grouped comparison: lose the controls; t-test → CI: lose nothing but gain interpretability.) Tests whether the Part 2 justification was a choice or a default.

**E. Clinic rotation in Part 4.** The instructor spends a fixed 4 minutes per group (timer visible) rather than circulating freely — guarantees the weakest group isn't skipped and prevents the strongest group from consuming the revision window.

## 4. Critique of the Lesson Plan

**What works (keep):** the brief-before-class → prepared-challenges loop (the strongest instructor-preparation design in the course); revision time *inside* the session with the honest "not all revisions are solvable in 20 minutes" framing; DC2's "a correlation is not a model" trap with its non-punitive redirect; the log entry's "limitation we have not yet addressed" field.

**Problems, reasons, and fixes:**

1. **The external evaluator appears again (Design Challenge 1: "in Week 22 in front of an external evaluator") and still doesn't exist in Week 22's plan.** Second file with this dependency (see Week 19 supplement, point 1). Decide and reconcile all three files.
2. **The brief requires only one assumption.** Every method in the course carries three to six; asking for one invites naming the safest ("we assume the data is accurate") and leaves the real fragilities for the instructor to find. *Fix:* require the E2 grid — it's the same work the challenge round does, moved to where it teaches the authors rather than exposes them.
3. **Part 2's arithmetic:** 4 groups × 7–8 min + a class question each ≈ 32–36 minutes in a 30-minute slot. The internal breakdown sums to 6.5 minutes — *Fix:* cap at 6.5 + one question, or run 3-group cohorts at 8 minutes.
4. **No fallback challenge for a genuinely strong brief.** The prepared-challenge design assumes every brief has a visible weakness; occasionally one won't. *Fix:* the universal escalation is already in the course's vocabulary — "what would make you wrong, and what did you *do* to check?" followed by a robustness demand (Activity C's menu). Prepared strength deserves a harder question, not a softer one.
5. **The coursework connection is implicit.** Week 13's Design Challenge 5 promised that the assessment criteria map onto these questions, and this brief is structurally a draft of the 30% individual case study — but nothing here says so. *Fix:* one line in the pre-work: "this brief is the skeleton of the coursework submission; the marking criteria are the four brief elements plus the limitation statement." Alignment costs a sentence and redirects effort students will spend anyway.
6. **Effect sizes are demanded by the challenges but never formally taught.** Cohen's d appears once (Week 13, Design Challenge 2) as an aside; Part 4 lists it as a revision option. E3 closes the gap as a hand-out — without it, "add an effect size measure" is an instruction some groups can't execute in 20 minutes.
7. **Logistics line missing:** Part 4 assumes every group has laptops, data, and their environment live in the seminar room; after Weeks 16–18's lab formats this is probably true, but say it in the pre-work ("bring the working notebook — revision happens in class").
