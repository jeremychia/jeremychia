# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 13: Hypothesis Testing
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Construct** the logic of a hypothesis test — formulating H₀ and Hₐ, computing the appropriate test statistic, and interpreting the p-value in relation to a chosen significance level α (Bloom's: Apply).
2. **Select** the correct test for a given scenario — one-sample t-test, two-sample t-test, paired t-test, z-test for proportion, or chi-square test for independence — and execute it correctly in Excel (Bloom's: Analyse).
3. **Distinguish** between statistical significance and practical significance, explaining why a small p-value does not, by itself, justify a business decision (Bloom's: Evaluate).
4. **Critique** a set of hypothesis test results for the multiple testing problem and propose a corrected threshold or adjusted procedure (Bloom's: Evaluate).

---

## Before Class (Student Pre-Work)

**Reading:**

- Albright & Winston, Chapter 9: "Hypothesis Testing" — read pp. 363–406 in full. Pay particular attention to §9-3 (tests for a population mean, pp. 372–377), §9-4b (differences between means, pp. 379–387), §9-5 (tests for normality, pp. 395–401), and §9-6 (chi-square test for independence, pp. 401–406). The concepts around p-value interpretation in §9-2e (pp. 368–370) should be read twice.
- Skip the StatTools appendix walkthroughs on first pass — the Excel functions are covered in the worked example below.

**Videos (~20 minutes total):**

- *Crash Course Statistics #22: "Hypothesis Testing"* (approximately 10 minutes). This video establishes the logic of the null hypothesis, test statistic, and p-value using simple, memorable examples. *Active watching: pause after the p-value definition and write it in your own words before the video explains it. Then resume and compare your version to theirs. This is T0.*
- *StatQuest with Josh Starmer: "p-values: What they are and how to interpret them"* (approximately 8 minutes). This is the most precise plain-language explanation of the p-value interpretation problem available. *Active watching: when Starmer states what a p-value does NOT mean, pause and write one specific wrong interpretation — the one he most strongly rejects. That wrong interpretation is what T0 asks you to identify.*
- Optional (students who have not seen hypothesis testing before): Khan Academy *"Simple hypothesis testing"* (6 minutes) — recommended before watching the two above if the textbook felt abstract.

**Worked example (read this before attempting the tutorial problems):**

A fast-food manager wants to know whether the mean customer satisfaction rating for a new sandwich is above the minimum acceptable level of 5 (on a 1–10 scale). She collects ratings from n = 40 customers.

Data: x̄ = 6.25, s = 1.597, n = 40

**Step 1 — State the hypotheses.**

- H₀: μ = 5 (mean rating equals the minimum acceptable level)
- Hₐ: μ > 5 (mean rating exceeds the minimum acceptable level)
- This is a one-tailed (upper-tail) test because the manager only cares about ratings *above* 5.
- Significance level: α = 0.05

**Step 2 — Compute the test statistic.**

The one-sample t-statistic is:

t = (x̄ − μ₀) / (s / √n)
t = (6.25 − 5) / (1.597 / √40)
t = 1.25 / (1.597 / 6.325)
t = 1.25 / 0.2525
t = **4.95**

Degrees of freedom = n − 1 = 39.

**Step 3 — Find the p-value and decide.**

In Excel: `=T.DIST.RT(4.95, 39)` returns p ≈ 0.000008 (one-tailed).

Because p < α (0.05), we **reject H₀**.

Conclusion: "At the 5% significance level, there is sufficient evidence to conclude that the mean satisfaction rating exceeds 5. The sample mean of 6.25 is 4.95 standard errors above the hypothesised mean — this is extremely unlikely to occur by chance if the true mean were 5."

**Critical interpretation check:** Does this mean the sandwich is good? Not necessarily. It means the mean rating is statistically higher than 5. Whether a mean of 6.25 is *practically* meaningful depends on what the business does with this rating, what competitors score, and whether the effect size (6.25 − 5 = 1.25 points on a 10-point scale) matters to customers.

*This worked example is marked optional for students who can already state H₀ and Hₐ, compute a t-statistic, and find the p-value using Excel's T.DIST.RT function. If you can do those three steps without guidance, you don't need it. If the distinction between one-tailed and two-tailed tests, or the formula for the t-statistic, felt unclear after the reading, work through each step carefully before the tutorials.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems:**

**T0 — Entry question (lower floor):**

*The p-value definition you wrote during the Crash Course video pause, and the wrong interpretation you noted from StatQuest, are the two sentences T0 asks you to produce. If you did the active-watching exercises, you have already completed T0.*

Before computing anything, answer in your own words:

> A newspaper reports: "A new drug reduced blood pressure. The result was statistically significant (p = 0.03)." Write two sentences: one that correctly states what p = 0.03 means, and one that states something p = 0.03 does NOT mean.

This question has no formula. It requires only the p-value definition from the reading and the StatQuest video. Students who cannot answer it have not yet understood the conceptual foundation; the rest of T1 would not help them. Students who answer it confidently can move directly to T1.

*Why this matters for ST2187 students specifically:* unlike ST104a, where hypothesis testing may have been introduced as a pure procedure, ST2187 requires students to critique conclusions from test results. The T0 question establishes whether a student can do that before the tutorial goes further.

*Self-check for T0:* One correct sentence: "p = 0.03 means that if the drug had no effect, there is a 3% probability of observing a result at least as extreme as this one by chance." One common incorrect sentence: "p = 0.03 means there is a 97% probability that the drug works" — this is wrong because p-values say nothing about the probability that H₀ is true or false. If you wrote something similar to the incorrect sentence, re-read §9-2e twice before T1.

**T1 — Straightforward computation:**

*The worked example's three-step structure — state H₀/Hₐ, compute t = (x̄ − μ₀)/(s/√n), find p-value using T.DIST.2T — is exactly what T1 requires. The only difference is the numbers.*
A coffee shop chain claims the average customer wait time is 3 minutes. A quality inspector samples n = 25 customers and records their wait times. The sample mean is x̄ = 3.8 minutes with sample standard deviation s = 1.2 minutes.

(a) State H₀ and Hₐ for a two-tailed test at α = 0.05.
(b) Compute the t-statistic. Show all working.
(c) Find the p-value using `=T.DIST.2T(ABS(t), df)` in Excel.
(d) State your conclusion in a sentence appropriate for a non-technical manager.
(e) Construct a 95% confidence interval for the true mean wait time. Does your CI agree with your hypothesis test conclusion?

**T2 — Interpretation:**

> In early 2025, Meta Platforms published its Q4 2024 Adversarial Harmful Standards Enforcement Report, which included data on the prevalence of hate speech content on Facebook. According to the report, an estimated 0.07–0.08% of content views on Facebook involved content that violated Meta's hate speech policy — roughly 7–8 views in every 10,000.
>
> Meta's automated content moderation system flagged a random sample of 2,000,000 content items for review. In Group A (items shown the new AI moderation algorithm), 150 violations were detected. In Group B (items shown the previous algorithm), 120 violations were detected.
>
> Assume equal group sizes (1,000,000 items each). A z-test for the difference in proportions comparing detection rates gives p = 0.018.
>
> (a) At α = 0.05, what is the statistical conclusion?
>
> (b) The detection rate in Group A is 150/1,000,000 = 0.000150. In Group B it is 120/1,000,000 = 0.000120. What is the absolute difference in detection rates? Is this a practically meaningful improvement?
>
> (c) Meta's trust and safety team argues: "A statistically significant improvement in detection rate means we should deploy the new algorithm." A civil liberties researcher argues: "A difference of 0.003 percentage points in detection rate is not meaningful — we should worry about false positives." What additional information about the new algorithm would you need before deciding which argument is stronger?
>
> (d) Suppose the new algorithm also increases false positives (incorrectly flagging legitimate content) by 0.001 percentage points. On a platform with 1 billion daily content views, how many additional items per day would be incorrectly flagged? Is this a meaningful cost?
>
> (e) The report covers a sample of content views, not a census. What does p = 0.018 tell us — and what does it not tell us — about content moderation performance across all of Meta's platforms?

This question uses a verified published source: Meta's Adversarial Harmful Standards Enforcement Reports are publicly available at transparency.fb.com, published quarterly. The specific figures in the scenario are illustrative, but the prevalence rate (0.07–0.08%) is from reported data. The scenario surfaces the core T2 lesson: very large n makes trivially small differences statistically significant — and at platform scale, even 0.001 percentage points can represent millions of items. This is the most consequential version of the "statistical vs. practical significance" problem.

**T3 — Edge case (multiple testing):**
A marketing researcher is studying factors that predict customer loyalty. She measures 50 different variables (demographic, behavioural, and attitudinal) and runs 50 separate hypothesis tests against customer loyalty score, each at α = 0.05. She finds 4 variables with p < 0.05.

(a) Under the null hypothesis (all 50 variables truly have no effect), what is the expected number of false positives? Show the calculation.
(b) Is it likely that at least one of the 4 "significant" results is a false positive? Compute the probability that at least one false positive occurs in 50 tests.
(c) What should the researcher do? Name and describe at least one corrected threshold or procedure (Bonferroni correction is acceptable; Benjamini-Hochberg is a stretch goal).
(d) If the researcher pre-registered exactly 3 hypotheses before data collection, does the multiple testing problem still apply?

*T4 — Boundary case: what happens when n approaches very large values:*

> A logistics company tracks on-time delivery rates. Historically, the on-time rate was exactly 92% (μ₀ = 0.92). After implementing new routing software, they sample deliveries to test whether performance has changed.
>
> **Trial A:** n = 200 deliveries, p̂ = 0.935 (93.5% on time). z-test for proportion.
> **Trial B:** n = 200,000 deliveries, p̂ = 0.921 (92.1% on time).
>
> (a) For Trial A, compute the test statistic and p-value (two-tailed). What do you conclude at α = 0.05?
>
> *Solution:* z = (0.935 − 0.92) / √(0.92 × 0.08 / 200) = 0.015 / √(0.000368) = 0.015 / 0.01918 ≈ 0.782. p-value = 2 × (1 − NORM.DIST(0.782, 0, 1, TRUE)) ≈ 2 × 0.217 ≈ **0.434**. Fail to reject H₀. Insufficient evidence of change.
>
> (b) For Trial B, compute the test statistic and p-value (two-tailed). What do you conclude at α = 0.05?
>
> *Solution:* z = (0.921 − 0.92) / √(0.92 × 0.08 / 200,000) = 0.001 / √(3.68 × 10⁻⁷) = 0.001 / 0.000607 ≈ 1.649. p-value ≈ 2 × (1 − NORM.DIST(1.649, 0, 1, TRUE)) ≈ 2 × 0.0496 ≈ **0.099**. Fail to reject H₀ at α = 0.05.
>
> (c) Trial A has a 1.5 percentage point improvement; Trial B has only a 0.1 percentage point improvement. Yet Trial A is less significant. Explain this apparent paradox. What does it reveal about the relationship between effect size and significance?
>
> (d) If the company runs with n = 2,000,000 deliveries and observes p̂ = 0.9201 (just 0.01 percentage points above 92%), calculate the z-statistic. Would this be statistically significant at α = 0.05?
>
> *Solution:* z = 0.0001 / √(0.92 × 0.08 / 2,000,000) = 0.0001 / 0.0000192 ≈ 5.21. p ≈ 0. Yes, highly significant — despite a trivially small improvement.
>
> (e) Write a one-paragraph memo to the company's COO explaining the difference between statistical significance and operational significance, using the contrast between Trial A and (d) as your example.

*T5 — Comparison: one-tailed versus two-tailed tests:*

> A manufacturer claims its packaging machine fills bottles to exactly 500ml on average. A quality inspector suspects the machine might be under-filling (to save product). The inspector samples n = 36 bottles; sample mean = 498.2ml; sample SD = 4.8ml.
>
> (a) State H₀ and Hₐ for a two-tailed test (the inspector has no prior suspicion about the direction).
> (b) State H₀ and Hₐ for a one-tailed test (the inspector suspects under-filling specifically).
> (c) Compute the t-statistic.
>
> *Solution:* t = (498.2 − 500) / (4.8 / √36) = −1.8 / 0.8 = **−2.25**
>
> (d) Compute the p-value for: (i) the two-tailed test; (ii) the one-tailed (lower-tail) test. [Use T.DIST.2T and T.DIST respectively.]
>
> *Solution:* (i) p = T.DIST.2T(2.25, 35) ≈ **0.031.** (ii) p = T.DIST(−2.25, 35, TRUE) ≈ **0.0155.**
>
> (e) At α = 0.05: which test rejects H₀? Why does the one-tailed test have a smaller p-value for the same t-statistic?
> (f) The inspector chose a one-tailed test *after* seeing the data showed under-filling. Is this valid statistical practice? What is the concern?
> (g) If the inspector had correctly pre-specified a one-tailed test before collecting data (with clear business justification that over-filling was impossible), and the result is p = 0.0155: write the conclusion for a regulatory report.

*T6 — Multi-step: chi-square test for independence, from table to conclusion:*

> A supermarket chain runs a promotion in three store regions (North, Central, South) and tracks whether customers redeem the promotional voucher (Yes/No). The observed counts are:
>
> | | Yes | No | Total |
> |---|---|---|---|
> | North | 85 | 115 | 200 |
> | Central | 120 | 80 | 200 |
> | South | 60 | 140 | 200 |
> | **Total** | **265** | **335** | **600** |
>
> (a) If region and redemption were independent, what would the expected count be in each cell? Show the calculation for the North/Yes cell.
>
> *Solution:* Expected(North, Yes) = (200 × 265) / 600 = 53,000 / 600 ≈ **88.33.**
> Full expected table: North: 88.33/111.67; Central: 88.33/111.67; South: 88.33/111.67.
>
> (b) Calculate the chi-square test statistic. [χ² = Σ (O − E)² / E]
>
> *Solution:*
> Contributions: North/Yes: (85−88.33)²/88.33 = 11.09/88.33 ≈ 0.126; North/No: (115−111.67)²/111.67 ≈ 0.099; Central/Yes: (120−88.33)²/88.33 = 1002.9/88.33 ≈ 11.355; Central/No: (80−111.67)²/111.67 ≈ 8.990; South/Yes: (60−88.33)²/88.33 = 802.0/88.33 ≈ 9.079; South/No: (140−111.67)²/111.67 ≈ 7.184.
> χ² ≈ 0.126 + 0.099 + 11.355 + 8.990 + 9.079 + 7.184 ≈ **36.8**
>
> (c) How many degrees of freedom does this test have? State the decision rule at α = 0.05.
>
> *Solution:* df = (rows − 1)(cols − 1) = 2 × 1 = 2. Critical value = CHISQ.INV.RT(0.05, 2) ≈ 5.99. Since 36.8 >> 5.99, **reject H₀.**
>
> (d) State the conclusion in business terms: what does the result imply about the promotion's effectiveness across regions?
> (e) The test tells you that redemption rates differ by region. It does not tell you *which* region drives the difference, or *why.* What follow-up analysis would you conduct?
> (f) A minimum expected cell count of 5 is required for the chi-square approximation to be valid. Is this assumption met here? What would you do if one expected cell had a count of 2?

*T7 — Diagnostic: identify everything wrong with this hypothesis test:*

> A marketing analyst submits the following report:
>
> *"We tested whether our new email subject line improved open rates. The old subject line had a 22% open rate. We sent 50 emails with the new subject line and got 14 opens (28%). We ran a t-test comparing 0.28 to 0.22 and got p = 0.023. Since p < 0.05, we conclude the new subject line is better and will roll it out to all 400,000 subscribers."*
>
> Identify every problem with this analysis. There are at least five. For each, state what the analyst should have done differently.
>
> *(Expected issues:) (1) A t-test is wrong for testing a proportion — should use a z-test for proportions or binomial test. (2) n = 50 is very small for an email A/B test; statistical power is low. (3) The comparison is between a single sample proportion and a claimed historical value (0.22), but the analyst doesn't state whether the 22% was measured under identical conditions. (4) The result may be statistically significant but practically trivial — 6 percentage points difference in open rate; what is the actual business value? (5) Rolling out to 400,000 based on n = 50 is an extreme extrapolation. (6) One-sided vs two-sided test not specified. (7) No check on whether the 50 emails form a representative sample.)*

**Pre-class submission (due midnight before class):**

Using your open-data dataset from a country other than your own (data.gov.sg, daten.berlin.de, opendata.paris.fr, or dados.gov.pt), post to the LMS discussion board:

1. The name and URL of your dataset.
2. One hypothesis you could test with your data — written formally as H₀ and Hₐ (e.g., "H₀: the mean daily ridership on this metro line does not differ from 100,000 passengers").
3. One reason your hypothesis test conclusion might be statistically significant but practically meaningless for this dataset.

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mentimeter quiz (students use phones/laptops at menti.com):**

The instructor sets up a 9-question Mentimeter quiz displayed on screen. Students submit answers individually in real time; the class distribution of answers is revealed after each question. The instructor does NOT announce correct answers immediately — responses are used to identify which concepts to revisit in Part 2.

---

**Q1 (Easy — recall):**
The p-value is defined as:

A) The probability that H₀ is true
B) The probability of getting a result at least as extreme as observed, assuming H₀ is true ✓
C) The probability that the research hypothesis is correct
D) One minus the probability of a Type I error

---

**Q2 (Easy — recall):**
In a one-sample t-test with n = 25 observations, the degrees of freedom are:

A) 25
B) 24 ✓
C) 23
D) Depends on the test statistic

---

**Q3 (Easy — recall):**
A Type I error occurs when:

A) You fail to reject H₀ when it is false
B) You reject H₀ when it is true ✓
C) Your sample size is too small
D) The p-value is exactly equal to α

---

**Q4 (Easy — recall):**
Which Excel function computes the two-tailed p-value for a t-test with test statistic t and df degrees of freedom?

A) `=T.DIST(t, df, TRUE)`
B) `=T.DIST.RT(t, df)`
C) `=T.DIST.2T(ABS(t), df)` ✓
D) `=TTEST(t, df, 2, 2)`

---

**Q5 (Easy — recall):**
The chi-square test for independence is used when:

A) Both variables are continuous
B) One variable is continuous and one is categorical
C) Both variables are categorical ✓
D) The sample size is below 30

---

**Q6 (Easy — recall):**
Power = 1 − β means:

A) The probability of making a Type I error
B) The probability of correctly rejecting H₀ when it is false ✓
C) The probability that the null hypothesis is true
D) The probability of failing to reject a true H₀

---

**Q7 (Medium — application):**
A test gives t = 2.1, df = 18, two-tailed test. Using `=T.DIST.2T(2.1, 18)`, Excel returns p = 0.051. At α = 0.05, you:

A) Reject H₀ — p is close enough
B) Fail to reject H₀ — p > 0.05 ✓
C) Reject H₀ — t > 2
D) Cannot decide without the effect size

---

**Q8 (Medium — interpretation):**
A researcher tests H₀: μ = 100 and obtains p = 0.001 with n = 1,000,000. Which of the following is most appropriate to conclude?

A) The effect is very large and practically important
B) The result is statistically significant but may be practically trivial ✓
C) The null hypothesis is almost certainly false
D) The probability that μ = 100 is 0.1%

---

**Q9 (Hard — synthesis):**
A company runs 20 A/B tests simultaneously, each at α = 0.05. All 20 null hypotheses are actually true. How many "statistically significant" results should they expect to find purely by chance?

A) 0 — if all nulls are true, no test will be significant
B) 1 expected, but could be 0 or higher ✓
C) 20 — every test will show significance
D) It depends on the sample size

---

**Instructor response protocol:**

- If > 60% of students answer Q1 incorrectly (confusing p-value with "probability H₀ is true"): spend 3 additional minutes on p-value interpretation in Part 2. This misconception is the conceptual centrepiece of the week.
- If Q7 or Q8 show high error rates: the session requires more time on the significance-vs-practical importance distinction; compress Part 2's tutorial review by 5 minutes.
- If Q9 confuses the class: the multiple testing problem (T3) is not yet understood; ensure T3 is reviewed in Part 2 even if T1/T2 feel solid.
- Record the class response distribution — it is formative data for the Week 14 assumption-checking discussion.

---

### Part 2 — Tutorial Review (15 minutes + 10 min buffer)

The instructor reviews T1–T3 selectively based on the Mentimeter results. The worked example from pre-work is assumed to be complete; T1 is the baseline check.

**T1 walkthrough (5 minutes if Q1–Q6 are mostly correct; 8 minutes if not):**

Put the coffee shop scenario on screen. Ask a volunteer to state H₀ and Hₐ aloud before showing the answer. Work through the t-statistic calculation on the whiteboard, emphasising the formula structure: (observed − hypothesised) / standard error. Ask the class: "What would happen to the t-statistic if n were 100 instead of 25, with the same x̄ and s?" (Answer: t would increase because SE shrinks with larger n — and thus even a small difference from μ₀ becomes detectable. This is the bridge to T2 and the practical significance discussion.)

**T2 walkthrough (5 minutes):**

Do not compute anything new — T2 is about interpretation. Put the A/B test numbers on screen:
- 50,000 visitors each; 10 additional conversions in the treatment group
- p = 0.031; absolute difference = 0.02 percentage points

Ask the class: "Would you recommend this company redesign its homepage?" Let students respond without guidance first. Then surface the missing information: cost of redesign, lifetime value of each converted customer, the fact that with n = 100,000 even a trivially small difference will have a small p-value. Introduce the concept of effect size: Cohen's d, or in this case, the simple number of additional conversions (10 per 50,000 visitors). State the core principle explicitly: **statistical significance is a function of sample size; practical significance is a function of effect size.**

**T3 walkthrough (5 minutes):**

Multiple testing: 50 tests × 0.05 = 2.5 expected false positives under the global null. The probability of at least one false positive in 50 independent tests = 1 − (0.95)^50 = 1 − 0.077 = 0.923, or about 92%. Bonferroni correction: use α = 0.05/50 = 0.001 as the per-test threshold. Connect to the Mentimeter Q9 discussion. If time permits, note that Bonferroni is conservative and the Benjamini-Hochberg procedure controls the false discovery rate more efficiently in large-scale testing.

**10-minute buffer:** Available if any of T1–T3 requires more time, or if the Mentimeter results reveal a pervasive misconception that must be addressed before the structured controversy.

---

### Part 3 — Structured Controversy (25 minutes)

**Format note:** Part 3 this week replaces the analyst/sceptic pair work used in most sessions. Instead, students are assigned opposing advocacy positions on the same dataset and must argue for their assigned conclusion — regardless of their personal view. This is a structured controversy adapted from Johnson & Johnson (1988), generating productive cognitive conflict (Bjork, 1994) at the evaluate level of Bloom's taxonomy.

**Setup (3 minutes):**

The instructor projects the following result on screen and posts it to the class channel:

> A Berlin city authority tests whether the mean monthly rent per square metre in Prenzlauer Berg differs from the city-wide mean of €14.50/m². A random sample of n = 120 listings gives x̄ = €14.78/m², s = €2.10/m². The t-statistic is 1.46, df = 119, p = 0.147 (two-tailed). A separate analysis on the full administrative dataset of n = 48,000 listings gives t = 12.3, p < 0.001.

The instructor assigns pairs. In each pair, Student A holds the "statistically significant / reject H₀" brief; Student B holds the "practically meaningless / fail to act" brief.

**Students are told explicitly:** "You are not expressing your personal view. You are arguing for your assigned position as rigorously as possible. Your job is to find the best evidence for your position, not to 'win' — the goal is to surface every consideration so the class can evaluate the full picture."

**Pair advocacy (12 minutes):**

Students A and B argue their positions, alternating turns (3 minutes each, two rounds). The instructor circulates and listens. Students should be prompted if they get stuck with the following scaffolding questions:

- *For Student A (arguing significance on the full dataset):* "What does p < 0.001 on 48,000 listings tell you? How confident are you that the neighbourhood mean is truly above €14.50? What policy action might you recommend?"
- *For Student B (arguing practical meaninglessness):* "The difference is €0.28/m² on a monthly rent. What does that amount to per year on a 50m² flat? Is €168/year a meaningful difference for housing policy? What would you need to see to consider this practically important?"
- *For both:* "Why do the two datasets — n=120 and n=48,000 — give such different p-values for what appears to be a similar difference from €14.50?"

**Swap and debrief (10 minutes):**

At the 12-minute mark, students swap positions: A now argues for the "practically meaningless" brief; B argues for "statistically significant." This forces both students to engage seriously with the opposing view (Vygotsky, 1978 — articulating the ZPD of the opposing position).

Instructor brings the full class back together and asks:

1. "Which position was harder to argue — and why?"
2. "Is the €0.28/m² difference real? (Yes — both datasets agree.) Does it matter for housing policy?"
3. "What does this tell you about reporting hypothesis test results in a business context?"

**Instructor resolution (3 minutes within the 25-minute total):**

The core insight to surface: both datasets produce the same point estimate (approximately €0.28 above the city mean), but the larger dataset has a much smaller standard error, so the same difference becomes highly "significant." The effect is real. Whether it is important depends on what decision depends on it. The structured controversy format makes this visceral rather than abstract.

---

### Part 4 — Peer Discussion (20 minutes)

**Activity: Test your own hypothesis**

Students retrieve their pre-class LMS submission (their chosen open-data dataset and hypothesised H₀ / Hₐ). Working individually for 10 minutes, they:

1. Load their dataset into Excel (or use a summary statistic they computed in a previous week).
2. Run the appropriate test — one-sample t-test using the T.TEST function or `=T.DIST.2T(ABS(t), df)` — and note the p-value.
3. Write two sentences: one reporting the statistical conclusion, one assessing whether the result is practically significant.

After 10 minutes, students share their results in groups of 3 (instructor assigns groups across nationalities and dataset countries). Each student has 2 minutes to present their result and receive one question from each groupmate.

The instructor circulates and listens for the following productive conflicts to surface in the full-group debrief:

- A student with a very large n (e.g., Singapore bus ridership dataset with n = 10,000+) who finds p < 0.05 for a trivially small difference.
- A student with a small n who fails to reject H₀ despite a seemingly large difference — and asks whether the test "worked."
- A student who realises their variable is not continuous and tries to apply a t-test to count data.

These moments are the primary evidence of formative assessment (Black & Wiliam, 1998) — the instructor uses them to calibrate the Week 14 assumption-checking discussion.

**Full group (final 5 minutes of Part 4):**

Instructor asks three students to report a single sentence each: "My p-value was [X]; my practical significance assessment was [Y]." Instructor thanks each response without evaluating it — reserves evaluation for Part 5.

---

### Part 5 — Instructor Debrief (10 minutes)

**Closing the structured controversy:**

Return to the Berlin rent result from Part 3. Write the following on the whiteboard:

```
n = 120:   x̄ = 14.78, p = 0.147  → fail to reject H₀
n = 48,000: x̄ = 14.78, p < 0.001  → reject H₀
```

Ask: "Same difference. Different conclusions. Which is the better analysis?" The expected student answer: neither is "better" — the question reveals that the p-value is a function of sample size and the same underlying reality. The practical significance assessment (€0.28/m²) is the same in both cases.

**Key principles to state explicitly (write on board):**

1. p < 0.05 does **not** mean the null hypothesis has a 5% chance of being true.
2. p < 0.05 does **not** tell you the size of the effect.
3. p < 0.05 does **not** tell you whether the result is practically important.
4. A very large sample can make any non-zero difference statistically significant.
5. Report effect sizes alongside p-values. Always.

**Bridge-forward question (last 3 minutes):**

"Next week we move to regression analysis. In regression, each predictor has its own p-value for the hypothesis H₀: β = 0. Given what we discussed today — the multiple testing problem, and the distinction between statistical and practical significance — what concerns might you already have about interpreting a regression model with 10 predictors, each tested at α = 0.05?"

Expected answers: 10 tests means up to 0.5 expected false positives; a significant coefficient does not mean the predictor is practically important; a large dataset could make every coefficient significant even for trivial effects. These concerns will be revisited directly in Week 15.

---

## After Class (~30 min)

**LMS post (LinkedIn/social format):**

Post the following to the class LMS discussion board, written in the style of a LinkedIn post (first-person, 150–250 words, paragraph format, no bullet points):

> Reflect on the following prompt: "A colleague sends you a report showing p < 0.05 on a business metric and recommends a significant budget reallocation. What three questions do you ask before acting on this result — and why?"

Your post should reference at least one specific finding from today's session (the Berlin rent example, the A/B test scenario, or your own dataset result). Engage with at least one classmate's post by the morning of Week 14 — not to agree or disagree reflexively, but to add a consideration they did not mention.

This post counts as formative participation. Exemplary posts will be anonymised and shared in the Week 14 Mentimeter debrief as "what good critical thinking sounds like."

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Structured controversy (Part 3) instead of standard pair work | Bjork (1994) desirable difficulties: assigning students to argue a position they may not hold generates deeper processing than confirming a position they already believe. The controversy format forces evaluation-level engagement with competing interpretations of the same p-value. |
| Mentimeter Q9 (multiple testing) as the hardest question | Roediger & Karpicke (2006) testing effect: placing the hardest question last, before instruction is complete, encodes the problem without the answer — students carry the unresolved question into Part 2, making the T3 walkthrough more retrievable. |
| Students argue from their own open-data dataset in Part 4 | Ausubel (1968) assimilation theory: hypothesis testing must attach to a specific dataset the student already knows. The meaning of "statistical significance" is clearer when the underlying data is familiar than when it is an abstract textbook example. |
| Berlin rent worked example using two sample sizes (n=120 vs n=48,000) | Kalyuga et al. (2003) expertise reversal: contrasting two analyses of the same data with different conclusions makes the p-value / sample size relationship salient. For novices, simultaneous comparison is more effective than sequential presentation of each case. |
| Explicit "what p-value does NOT mean" list on whiteboard | Lovett & Greenhouse (2000) cognitive load: students carry several misconceptions about p-values into the session. Stating the list explicitly, and keeping it on the whiteboard throughout Part 5, reduces the cognitive work of tracking which claims are and are not licensed. |
| Bridge-forward question anticipating regression inference | Cepeda et al. (2006) spacing effect: previewing the Week 15 inference problem (multiple t-tests on regression coefficients) during Week 13 creates a distributed encoding opportunity. When students encounter F-tests and adjusted R² in Week 15, they will have already formulated the question those tools answer. |
| Peer discussion across nationalities and dataset countries (Part 4) | Vygotsky (1978) ZPD: a student working with Singapore bus ridership data and a student working with Paris open data have different baseline intuitions about what a "large" difference looks like in context. Cross-national grouping makes the context-dependence of practical significance visible. |
| LMS post in LinkedIn/social format | Black & Wiliam (1998) formative assessment: the social format lowers the perceived stakes while raising the authenticity of the reflective task. Posts are legible to the instructor without being marked, creating a low-cost feedback loop that informs Week 14 planning. |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Part 1 — Retrieval Check (Mentimeter) | 10 min | 9 questions; instructor records class response distribution for formative use |
| Part 2 — Tutorial Review | 15 min + 10 min buffer | T1 (5 min), T2 (5 min), T3 (5 min); buffer used if Mentimeter reveals pervasive misconceptions |
| Part 3 — Structured Controversy | 25 min | 3 min setup, 12 min pair advocacy, 7 min swap and debrief, 3 min instructor resolution |
| Part 4 — Peer Discussion | 20 min | 10 min individual hypothesis test, 5 min group sharing, 5 min full-group reporting |
| Part 5 — Instructor Debrief | 10 min | Board summary of 5 key principles; bridge-forward question to regression inference |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

**1. The p-value misconception is deep and persistent**

Research consistently shows (Haller & Krauss, 2002; Gigerenzer, 2004) that even trained researchers misinterpret p-values — most commonly, believing that p = 0.04 means there is a 4% probability that H₀ is true. This misconception is resistant to correction because it is logically appealing: it maps onto how people naturally reason about probability. In a seminar setting, the instructor cannot simply state the correct definition and move on. The structured controversy in Part 3 is designed to force students to encounter the p-value in a context where the misconception leads to an obviously wrong business recommendation (recommending a €50,000 homepage redesign for 10 additional conversions per 50,000 visitors). The visceral wrongness of the recommendation is more corrective than a definitional restatement. However, the instructor must be prepared for students who, even after the structured controversy, continue to conflate "p < 0.05" with "the effect is real" — and must have a ready counter-example (the n = 48,000 Berlin rent case, where the same difference flips from non-significant to highly significant) to revisit the point.

**2. The practical significance problem has no formula — and students want one**

Students trained in quantitative disciplines expect that every concept has a precise computational rule. When the instructor says "practical significance depends on the business context," students often respond with frustration: "But how do we know when an effect is large enough?" Cohen's d provides a partial answer (d = 0.2 small, 0.5 medium, 0.8 large by convention), but the conventions are themselves context-dependent and were derived from psychological research, not business analytics. The instructor should be explicit that practical significance is a judgment — and that this judgment requires domain knowledge (what a conversion rate difference means for a specific business model) that statistics alone cannot supply. This is a feature of the field, not a gap in the curriculum.

**3. The multiple testing problem requires mathematical formulation that some students find difficult**

The calculation in T3 — P(at least one false positive) = 1 − (1 − α)^k — involves compound probability reasoning. Students who are comfortable with this will find T3 trivial; students who are not will find it confusing even with the formula given. In a cohort of 40+ nationalities and varied mathematical backgrounds, the gap between these two groups can be significant. The instructor should present the formula and its derivation briefly, then focus more time on the intuition (if you test 20 variables and each has a 5% chance of a false positive, you should expect one false alarm — even if nothing is truly related). The Bonferroni correction is simple enough that all students can apply it; the Benjamini-Hochberg procedure should be presented as a "knowing it exists is enough" extension for this level.

**4. The structured controversy format requires careful facilitation to avoid superficiality**

Structured controversy works only if students engage seriously with their assigned position rather than treating it as a game. In a 12-15 student cohort, it is common for students to make their advocacy argument in one or two sentences and then stop, waiting for the instructor to fill the silence. The instructor must be prepared with the scaffolding questions listed in Part 3 and must resist the urge to resolve the controversy early — the productive tension of holding two conflicting positions simultaneously is the learning mechanism. If the class moves too quickly to "obviously B is right," the instructor should push back: "Make the strongest possible case for A. What would A need to be true for you to take seriously?" This requires the instructor to have a clear model of what the best version of each argument is.

**5. Connecting the seminar to the individual coursework assessment**

The 30% individual case study coursework requires students to run and interpret hypothesis tests on real open-data datasets. Some students will use the pre-class submission and Part 4 activity as their coursework data — which is appropriate and expected — but may not realise that the coursework standard requires explicit engagement with practical significance, effect size, and the limitations of the test (including the multiple testing problem if they run more than one test). The instructor should mention explicitly at the close of Part 5 that the bridge-forward question — "three questions to ask before acting on a p-value" — maps directly onto the assessment criteria. This is a low-cost alignment move that prevents students from producing technically correct but analytically shallow coursework.

---

## References

Albright, S. C., & Winston, W. L. (2019). *Business analytics: Data analysis and decision making* (6th ed.). Cengage Learning.

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's educational objectives*. Longman.

Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart and Winston.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300.

Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. https://doi.org/10.1080/0969595980050102

Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354

Gigerenzer, G. (2004). Mindless statistics. *The Journal of Socio-Economics, 33*(5), 587–606. https://doi.org/10.1016/j.socec.2004.09.033

Haller, H., & Krauss, S. (2002). Misinterpretations of significance: A problem students share with their teachers? *Methods of Psychological Research Online, 7*(1), 1–20.

Johnson, D. W., & Johnson, R. T. (1988). Critical thinking through structured controversy. *Educational Leadership, 45*(8), 58–64.

Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. https://doi.org/10.1207/S15326985EP3801_4

Lovett, M. C., & Greenhouse, J. B. (2000). Applying cognitive theory to statistics instruction. *The American Statistician, 54*(3), 196–206. https://doi.org/10.1080/00031305.2000.10474545

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
