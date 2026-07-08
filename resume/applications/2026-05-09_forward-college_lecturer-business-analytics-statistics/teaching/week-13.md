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

> In early 2025, Meta Platforms published its Q4 2024 Community Standards Enforcement Report, which included data on the prevalence of hate speech content on Facebook. According to the report, an estimated 0.07–0.08% of content views on Facebook involved content that violated Meta's hate speech policy — roughly 7–8 views in every 10,000.
>
> Meta's automated content moderation system flagged a random sample of 2,000,000 content items for review. In Group A (items shown the new AI moderation algorithm), 160 violations were detected. In Group B (items shown the previous algorithm), 120 violations were detected.
>
> Assume equal group sizes (1,000,000 items each). A z-test for the difference in proportions comparing detection rates gives p = 0.018.
>
> (a) At α = 0.05, what is the statistical conclusion?
>
> (b) The detection rate in Group A is 160/1,000,000 = 0.000160. In Group B it is 120/1,000,000 = 0.000120. What is the absolute difference in detection rates? Is this a practically meaningful improvement?
>
> (c) Meta's trust and safety team argues: "A statistically significant improvement in detection rate means we should deploy the new algorithm." A civil liberties researcher argues: "A difference of 0.003 percentage points in detection rate is not meaningful — we should worry about false positives." What additional information about the new algorithm would you need before deciding which argument is stronger?
>
> (d) Suppose the new algorithm also increases false positives (incorrectly flagging legitimate content) by 0.001 percentage points. On a platform with 1 billion daily content views, how many additional items per day would be incorrectly flagged? Is this a meaningful cost?
>
> (e) The report covers a sample of content views, not a census. What does p = 0.018 tell us — and what does it not tell us — about content moderation performance across all of Meta's platforms?

This question uses a verified published source: Meta's Community Standards Enforcement Reports are publicly available at transparency.fb.com, published quarterly. The specific figures in the scenario are illustrative, but the prevalence rate (0.07–0.08%) is from reported data. The scenario surfaces the core T2 lesson: very large n makes trivially small differences statistically significant — and at platform scale, even 0.001 percentage points can represent millions of items. This is the most consequential version of the "statistical vs. practical significance" problem.

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
> (d) If the company runs with n = 2,000,000 deliveries and observes p̂ = 0.921 (the same 0.1 percentage-point improvement as Trial B), calculate the z-statistic. Would this be statistically significant at α = 0.05?
>
> *Solution:* z = 0.001 / √(0.92 × 0.08 / 2,000,000) = 0.001 / 0.000192 ≈ 5.21. p ≈ 0. Yes, highly significant — the same small improvement that could not be distinguished from noise at n = 200,000 (p = 0.099) becomes overwhelming with ten times the data.
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

---

## Answer Key

### T0 — p-value definition and common misinterpretation

**Correct statement:** "p = 0.03 means that if the drug truly had no effect on blood pressure (i.e., H₀ were true), there is a 3% probability of observing a reduction at least as large as the one measured, purely by chance."

**Incorrect statement (what p = 0.03 does NOT mean):** "p = 0.03 does not mean there is a 97% probability that the drug works." The p-value says nothing about the probability that H₀ is true or false; it is a probability calculated *assuming* H₀ is true, not a probability assigned to H₀ itself.

---

### T1 — One-sample t-test (coffee shop wait times)

**(a)** H₀: μ = 3 minutes (mean wait time equals the claimed 3 minutes). Hₐ: μ ≠ 3 minutes (mean wait time differs from 3 minutes). Two-tailed test at α = 0.05.

**(b)** t = (x̄ − μ₀) / (s/√n) = (3.8 − 3.0) / (1.2/√25) = 0.8 / (1.2/5) = 0.8 / 0.24 = **3.33.** df = n − 1 = 24.

**(c)** p-value = T.DIST.2T(3.33, 24) ≈ **0.003.** Since p = 0.003 < α = 0.05, we reject H₀.

**(d)** "At the 5% significance level, there is strong evidence that the mean customer wait time differs from the claimed 3 minutes. The sample mean of 3.8 minutes is 3.33 standard errors above the claimed mean — this is unlikely to occur by chance if the true mean were 3 minutes. The chain should investigate whether wait times have increased."

**(e)** 95% CI: t* = T.INV.2T(0.05, 24) ≈ 2.064. SE = 0.24. ME = 2.064 × 0.24 ≈ 0.495. CI: (3.8 − 0.495, 3.8 + 0.495) = **(3.31, 4.29) minutes.** Agreement: the claimed value of 3 minutes is outside this interval — consistent with rejecting H₀. The CI and the hypothesis test always agree for two-tailed tests at the same α level: if H₀ value is outside the 95% CI, the test rejects at α = 0.05.

---

### T2 — Statistical vs practical significance (Meta content moderation)

**(a)** At α = 0.05, p = 0.018 < 0.05, so we **reject H₀** and conclude the new algorithm detects a statistically significantly higher proportion of violations than the previous algorithm.

**(b)** Absolute difference in detection rates: 160/1,000,000 − 120/1,000,000 = 0.000160 − 0.000120 = **0.00004 (0.004 percentage points).** This is not practically meaningful in isolation — it is 4 additional violations detected per 100,000 content items reviewed. On a platform with billions of views, it scales to many items, but as a proportional improvement in detection rate it is tiny.

**(c)** Additional information needed: (i) **False positive rate of the new algorithm** — does catching 30 more violations come at the cost of incorrectly flagging thousands of legitimate posts? (ii) **Computational cost** — does the new algorithm require significantly more compute per item? (iii) **Nature of violations** — does the new algorithm preferentially catch more severe violations (incitement to violence) or trivial ones? (iv) **User experience cost** — are false positives applied to high-reach accounts or marginal ones, and what are the consequences of wrongful removal? The civil liberties researcher's concern about false positives is analytically valid: a 0.004 percentage point improvement in true positive rate is only defensible if the false positive rate is not substantially worsened.

**(d)** 0.001 percentage points = 0.00001 as a proportion. On 1 billion daily content views: 0.00001 × 1,000,000,000 = **10,000 additional items per day** incorrectly flagged. This is a meaningful operational cost — tens of thousands of content creators or posts affected daily — even though the proportion sounds negligible.

**(e)** p = 0.018 tells us: if the two algorithms had identical detection rates in the underlying population, there is a 1.8% probability of observing a difference at least this large by chance. It does not tell us: whether the detected violation rate generalises across all of Meta's platforms (Facebook, Instagram, WhatsApp each have different content and user behaviour profiles); whether the effect would persist under different content compositions; or whether the difference is stable over time as adversarial actors adapt to the new algorithm.

---

### T3 — Multiple testing problem

**(a)** Expected false positives = number of tests × α = 50 × 0.05 = **2.5.** Under the global null (all 50 variables truly have no effect), we expect on average 2.5 of the 50 tests to produce p < 0.05 purely by chance.

**(b)** P(at least one false positive in 50 tests) = 1 − P(no false positives) = 1 − (1 − 0.05)^50 = 1 − (0.95)^50 ≈ 1 − 0.077 ≈ **92.3%.** It is almost certain that at least one of the 4 "significant" results is a false positive.

**(c)** **Bonferroni correction:** use adjusted threshold α* = α/k = 0.05/50 = **0.001** as the per-test significance level. Only variables with p < 0.001 should be considered significant. This controls the Family-Wise Error Rate (FWER) — the probability of making at least one false positive across all tests — at 5%. **Benjamini-Hochberg (stretch goal):** rank all 50 p-values from smallest to largest. For each rank k, compare p_k to (k/50) × 0.05. The largest k for which this holds identifies which tests are significant. B-H controls the False Discovery Rate (FDR) — the expected proportion of false positives among significant results — rather than the FWER. B-H is less conservative than Bonferroni and rejects more hypotheses, making it appropriate when some false discoveries are tolerable.

**(d)** **No — the multiple testing problem does not apply to pre-registered hypotheses.** If the researcher specified exactly 3 hypotheses before data collection — not after seeing which variables looked promising — then running 3 tests at α = 0.05 means the expected number of false positives is only 3 × 0.05 = 0.15, and the probability of any false positive is 1 − (0.95)³ ≈ 14.3%. Pre-registration separates confirmatory testing (few pre-specified hypotheses, standard α) from exploratory analysis (many tests, correction required). This is why pre-registration is a cornerstone of replication in science.

---

### T4 — Boundary case: large n and practical significance

**(a)** Trial A: z = (0.935 − 0.92) / √(0.92 × 0.08/200) = 0.015 / √(0.000368) = 0.015 / 0.01918 ≈ **0.782.** p = 2 × (1 − NORM.DIST(0.782, 0, 1, TRUE)) ≈ 2 × 0.217 ≈ **0.434.** Since 0.434 > 0.05, **fail to reject H₀.** Insufficient evidence that performance has changed.

**(b)** Trial B: z = (0.921 − 0.92) / √(0.92 × 0.08/200,000) = 0.001 / √(3.68 × 10⁻⁷) = 0.001 / 0.000607 ≈ **1.649.** p ≈ 2 × (1 − NORM.DIST(1.649, 0, 1, TRUE)) ≈ 2 × 0.0496 ≈ **0.099.** Since 0.099 > 0.05, **fail to reject H₀** at α = 0.05 (barely — a higher α would change this).

**(c)** Trial A has a **larger effect size** (1.5 percentage points) but is less statistically significant because n = 200 is small — the standard error is large and the t-statistic is modest. Trial B has a **smaller effect size** (0.1 percentage point) but larger n, so the standard error is much smaller and the statistic is larger relative to the standard error. The apparent paradox reveals that statistical significance measures effect size relative to sampling variability, not absolute importance. With large enough n, any non-zero effect becomes significant; with small n, even meaningful effects may not reach significance.

**(d)** n = 2,000,000: z = 0.001 / √(0.92 × 0.08/2,000,000) = 0.001 / 0.000192 ≈ **5.21.** p ≈ 0 (essentially zero). **Yes, highly significant** — for a 0.1 percentage-point improvement (2,000 deliveries in 2 million) that was statistically invisible at n = 200,000. At n = 2 million, the hypothesis test detects even operationally marginal deviations from 92%.

**(e)** *(Memo to COO)* "Statistical significance and operational significance are distinct concepts that are easily confused. A result is statistically significant when it is unlikely to have occurred by chance — which depends critically on sample size. With n = 200 deliveries (Trial A), our 1.5 percentage-point improvement cannot be distinguished from random fluctuation. With n = 2,000,000 deliveries (our full operational data), even a 0.1 percentage-point difference — equivalent to 2,000 additional on-time deliveries out of 2 million — produces a highly significant p-value. Operational significance asks a different question: does this improvement matter for our customers and our business? A 1.5 percentage-point improvement in on-time delivery is operationally meaningful (it affects thousands of customers daily); a 0.1 percentage-point improvement is marginal. I recommend we report both: the p-value for the statistical test, and the absolute improvement in on-time deliveries as the operational metric."

---

### T5 — One-tailed vs two-tailed tests

**(a)** H₀: μ = 500ml (machine fills to exactly 500ml). Hₐ: μ ≠ 500ml (machine does not fill to exactly 500ml). Two-tailed test.

**(b)** H₀: μ = 500ml. Hₐ: μ < 500ml (machine under-fills). One-tailed (lower-tail) test.

**(c)** t = (498.2 − 500) / (4.8/√36) = −1.8 / 0.8 = **−2.25.** df = 35.

**(d)** (i) Two-tailed: p = T.DIST.2T(2.25, 35) ≈ **0.031.** (ii) One-tailed (lower): p = T.DIST(−2.25, 35, TRUE) ≈ **0.0155.**

**(e)** The two-tailed test rejects H₀ at α = 0.05 (p = 0.031 < 0.05). The one-tailed test also rejects (p = 0.016 < 0.05) — and its p-value is exactly half the two-tailed p-value. The one-tailed p-value is smaller because it concentrates all the rejection probability in one tail rather than splitting it across two. Both tests reject here, but the one-tailed test would also reject cases where the two-tailed test would not (when p is between 0.05 and 0.10 in the relevant tail).

**(f)** Choosing a one-tailed test **after** seeing the data showed under-filling is **not valid statistical practice.** This is called p-hacking or data-driven hypothesis selection: the analyst effectively chose the test that would give a smaller p-value after observing the direction of the result. A one-tailed test is only valid if the direction of the alternative (e.g., μ < 500) was pre-specified before data collection, based on subject-matter knowledge or prior hypothesis. Post-hoc direction selection inflates the effective Type I error rate — you are no longer controlling α at 5%.

**(g)** "At the 5% significance level, we reject the null hypothesis that the machine fills to 500ml on average. Based on a random sample of 36 bottles with mean fill 498.2ml and standard deviation 4.8ml, the one-tailed t-statistic is −2.25 (df = 35), giving p = 0.016. There is sufficient statistical evidence to conclude that the machine is under-filling. The business impact is an average shortfall of 1.8ml per bottle; at this scale, the manufacturer is advised to recalibrate the filling mechanism."

---

### T6 — Chi-square test for independence (supermarket regions)

**(a)** Expected count for any cell = (Row total × Column total) / Grand total. North/Yes: (200 × 265)/600 = 53,000/600 ≈ **88.33.** All expected counts are 88.33 (Yes) and 111.67 (No) for each region — because all three regions have the same row total of 200.

**(b)** χ² contributions:
| Cell | Observed | Expected | (O−E)²/E |
|---|---|---|---|
| North/Yes | 85 | 88.33 | 0.126 |
| North/No | 115 | 111.67 | 0.099 |
| Central/Yes | 120 | 88.33 | 11.355 |
| Central/No | 80 | 111.67 | 8.990 |
| South/Yes | 60 | 88.33 | 9.079 |
| South/No | 140 | 111.67 | 7.184 |

χ² ≈ 0.126 + 0.099 + 11.355 + 8.990 + 9.079 + 7.184 ≈ **36.8.**

**(c)** df = (3 − 1)(2 − 1) = 2. Critical value at α = 0.05: CHISQ.INV.RT(0.05, 2) ≈ 5.99. Since 36.8 >> 5.99, **reject H₀.** There is strong evidence that voucher redemption and region are not independent.

**(d)** In business terms: redemption rates differ significantly across regions. The Central region has a redemption rate of 120/200 = 60%, well above the overall rate of 265/600 = 44.2%. The South is 60/200 = 30%, well below average. The North is close to average (85/200 = 42.5%). This suggests the promotion is working very differently across regions — perhaps due to different demographics, store formats, or local marketing execution. The Central region's strong performance warrants investigation to understand what can be replicated.

**(e)** The chi-square test identifies that a difference exists but not which region drives it. Follow-up analysis options: (i) pairwise proportion tests (North vs Central, North vs South, Central vs South) with Bonferroni correction for multiple comparisons; (ii) analysis of what differs between regions — store format, promotional placement, customer demographics, basket size; (iii) a regression model with region as a predictor alongside other voucher characteristics to isolate the regional effect from confounders.

**(f)** Minimum expected cell count ≥ 5 is required. All expected counts here are 88.33 (Yes) or 111.67 (No) — well above 5, so the assumption is **met.** If a cell had an expected count of 2, the standard chi-square approximation would be invalid. Options: (i) collapse rare categories (merge regions with similar counts); (ii) use Fisher's Exact Test, which does not require the minimum expected count assumption (available for 2×2 tables); (iii) increase the sample size.

---

### T7 — Diagnostic: email subject line A/B test (find all errors)

There are at least seven problems:

1. **Wrong test statistic.** A t-test is inappropriate for comparing two proportions. The correct test is a **z-test for proportions** (or a binomial test, since n = 50 is small). A t-test assumes a continuous outcome with approximately normal distribution; a binary open/no-open variable does not meet this assumption.

2. **Tiny sample size.** n = 50 emails is far too small for an email A/B test. The standard error of a proportion at p = 0.28 with n = 50 is √(0.28 × 0.72/50) ≈ 0.063, giving a 95% CI of roughly 28% ± 12.4% — almost the entire range (15.6% to 40.4%). The result has very low statistical power and very wide uncertainty.

3. **Invalid comparison to historical baseline.** The analyst compares the new subject line (tested under current conditions) to "22% open rate" without stating when and how that rate was measured. If the 22% was from a different list, different time, or different content, the comparison is invalid.

4. **Statistical vs practical significance.** The 6-percentage-point difference (28% vs 22%) may or may not be practically meaningful. For an email list of 400,000 subscribers, 6% more opens = approximately 24,000 more opens. Whether that matters depends on the value of an open, the cost of the subject line change, and downstream conversion rates — none of which are discussed.

5. **Dangerous extrapolation.** Rolling out to 400,000 subscribers based on a test of 50 emails is an extreme generalisation. The 50-email sample may not be representative of the full subscriber base (e.g., if the test was sent to a particular segment).

6. **One-sided vs two-sided test not specified.** The analyst reports "p = 0.023" without stating whether the test was one-tailed (hypothesising improvement in advance) or two-tailed. If one-tailed was chosen after seeing the data improved, this is post-hoc hypothesis selection.

7. **No representativeness check.** The 50 test emails may not be a random sample from the subscriber list — they could be a particular time-of-day batch, a specific geographic segment, or early subscribers. Without knowing how the 50 were selected, the 28% rate cannot be generalised.

**What the analyst should have done:** pre-specify H₀ and Hₐ and test direction; use a z-test for proportions; determine the required sample size via a power calculation before running the test; report a confidence interval for the difference in open rates; and calculate the practical value of the improvement before recommending a full rollout.

---

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

Do not compute anything new — T2 is about interpretation. Put the Meta numbers on screen:
- 1,000,000 items per group; 160 vs 120 violations detected
- p = 0.018; absolute difference = 0.004 percentage points

Ask the class: "Would you recommend deploying the new algorithm?" Let students respond without guidance first. Then surface the missing information: the false-positive rate, the compute cost, the severity mix of what is caught, and the fact that with n = 2,000,000 even a trivially small difference produces a small p-value. Introduce the concept of effect size: here, the absolute difference in detection rates (40 extra detections per million items). State the core principle explicitly: **statistical significance is a function of sample size; practical significance is a function of effect size.**

**T3 walkthrough (5 minutes):**

Multiple testing: 50 tests × 0.05 = 2.5 expected false positives under the global null. The probability of at least one false positive in 50 independent tests = 1 − (0.95)^50 = 1 − 0.077 = 0.923, or about 92%. Bonferroni correction: use α = 0.05/50 = 0.001 as the per-test threshold. Connect to the Mentimeter Q9 discussion. If time permits, note that Bonferroni is conservative and the Benjamini-Hochberg procedure controls the false discovery rate more efficiently in large-scale testing.

**10-minute buffer:** Available if any of T1–T3 requires more time, or if the Mentimeter results reveal a pervasive misconception that must be addressed before the structured controversy.

---

### Part 3 — Structured Controversy (25 minutes)

**Format note:** Part 3 this week replaces the analyst/sceptic pair work used in most sessions. Instead, students are assigned opposing advocacy positions on the same dataset and must argue for their assigned conclusion — regardless of their personal view. This is a structured controversy adapted from Johnson & Johnson (1988), generating productive cognitive conflict (Bjork, 1994) at the evaluate level of Bloom's taxonomy.

**Setup (3 minutes):**

The instructor projects the following result on screen and posts it to the class channel:

> A Berlin city authority tests whether the mean monthly rent per square metre in Prenzlauer Berg differs from the city-wide mean of €14.50/m². A random sample of n = 120 listings gives x̄ = €14.78/m², s = €2.10/m². The t-statistic is 1.46, df = 119, p = 0.147 (two-tailed). A separate analysis on the full administrative dataset of n = 48,000 listings (where s = €5.00/m² — the administrative data covers a far more heterogeneous housing stock) gives t = 12.3, p < 0.001.

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

Research consistently shows (Haller & Krauss, 2002; Gigerenzer, 2004) that even trained researchers misinterpret p-values — most commonly, believing that p = 0.04 means there is a 4% probability that H₀ is true. This misconception is resistant to correction because it is logically appealing: it maps onto how people naturally reason about probability. In a seminar setting, the instructor cannot simply state the correct definition and move on. The structured controversy in Part 3 is designed to force students to encounter the p-value in a context where the misconception leads to an obviously wrong business recommendation (deploying a platform-wide algorithm change on the strength of p = 0.018 and 40 extra detections per million items, without asking about false positives). The visceral wrongness of the recommendation is more corrective than a definitional restatement. However, the instructor must be prepared for students who, even after the structured controversy, continue to conflate "p < 0.05" with "the effect is real" — and must have a ready counter-example (the n = 48,000 Berlin rent case, where the same difference flips from non-significant to highly significant) to revisit the point.

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

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapter 9

Reading references are accurate (pp. 363–406; 9-2e, 9-3, 9-4b, 9-5, 9-6 all correctly located). Two alignment issues:

1. **§9-5 (Tests for Normality) gets "pay particular attention" and then zero use.** No tutorial, quiz question, or activity checks normality before running a t-test — even though the instructor response protocol explicitly plans a "Week 14 assumption-checking discussion." Either add T10 below or soften the reading emphasis; assigning emphatic reading with no retrieval contradicts the course's own testing-effect logic.
2. **§9-4d (differences between proportions, p. 388) is doing heavy lifting** — T2 and T4 are both two-proportion/one-proportion z-tests — but it isn't on the "pay particular attention" list. Swap it in.

## 2. Extended Question Bank (with answers)

**T8 — Paired t-test (in the learning objectives, currently practised nowhere):**

> A retailer trials a new shelf layout in 10 stores. Weekly sales (€000s) are recorded for each store before and after the change. The differences (after − before) have mean d̄ = 4.2 and SD s_d = 6.0.
>
> (a) Why is a paired t-test correct here and a two-sample t-test wrong?
> (b) Compute the test statistic and two-tailed p-value.
> (c) The result sits just above α = 0.05. A manager says "so the layout doesn't work." Give the two reasons this conclusion overreaches.
>
> **Answers:** (a) The same stores are measured twice; store-level differences (location, size, clientele) are enormous but *cancel within each pair*. A two-sample test would pour all that between-store variance into the SE and destroy the signal — pairing is a variance-reduction design, not a formality. (b) t = 4.2/(6.0/√10) = 4.2/1.897 ≈ **2.21**, df = 9; p = T.DIST.2T(2.21, 9) ≈ **0.054**. (c) First, failing to reject ≠ evidence of no effect — with n = 10 the power is low, and the point estimate (+€4,200/week/store) is commercially large; second, 0.054 vs 0.050 is not a cliff — the CI for the mean difference, (−0.09, +8.49), shows the data are consistent with anything from nil to a very large gain. Decision: extend the trial, don't kill it. (This is the best available antidote to α-as-bright-line thinking.)

**T9 — Power and sample size (gives Q6 something to do):**

> Before the shelf-layout trial, the retailer asks: "How many stores do we need to detect a true mean uplift of €4,000/week (SD of differences ≈ €6,000) with 80% power at α = 0.05 (two-tailed)?"
>
> (a) Use the planning approximation n ≈ ((z_{α/2} + z_{β})·s_d/δ)².
> (b) The trial above used 10 stores. Roughly what power did it have — and what does that mean for interpreting its p = 0.054?
>
> **Answers:** (a) n ≈ ((1.96 + 0.84) × 6/4)² = (2.8 × 1.5)² = 4.2² ≈ **18 stores**. (b) With n = 10, power ≈ 50% (the observed effect equals the design effect but n is barely half of what 80% power needs): the trial was a coin flip to detect a real €4k effect. A non-significant result from an underpowered design is close to uninformative — which is exactly why T8(c)'s manager is wrong, now with a number attached.

**T10 — Check before you test (fills the §9-5 gap):**

> A colleague hands you n = 12 daily revenue figures from a new store and asks for a one-sample t-test against a €10,000 target. A histogram shows one day at €85,000 (a corporate bulk order) and the rest between €6,000 and €14,000.
>
> (a) What assumption of the t-test is threatened, and why does n = 12 make it worse?
> (b) Name two defensible responses.
>
> **Answers:** (a) With small n, the t-test leans on approximate normality of the population; a single extreme outlier in 12 observations makes the sample mean and SD unstable and the t-statistic unreliable (the CLT hasn't rescued anything at n = 12 — the Week 11 T4 lesson recurring). (b) (i) Investigate the outlier's provenance — if it's a structurally different event (bulk order), analyse it separately and test the remaining regular-trade days, *reporting both* (Week 2's T1(g) rule); (ii) use a test that doesn't need normality (sign test / Wilcoxon on the median vs €10,000 — name-drop level, per the course's B-H precedent); (iii) collect more data. Running §9-5's normality checks (or just looking at the histogram) *before* testing is the professional habit this question installs.

*Additional quiz questions:*

- Q10: Two groups of different customers vs the same customers measured twice — which needs the paired test, and what does pairing buy? *(a) first; smaller α (b) second; removes between-subject variance from the SE (c) second; increases df (d) either; identical results)* — **Answer: (b).**
- Q11: If H₀ is true and the test assumptions hold, the p-value is distributed: *(a) around 0.05 (b) uniformly between 0 and 1 (c) normally (d) near 1)* — **Answer: (b)** — the fact that makes the multiple-testing arithmetic (T3) work, and the punchline of Activity A below.
- Q12: A study reports p = 0.20 with n = 15 and concludes "the treatment has no effect." The best critique: *(a) α was too high (b) absence of evidence ≠ evidence of absence, especially with low power (c) they should have used a one-tailed test (d) p should have been Bonferroni-corrected)* — **Answer: (b)** — T8(c)/T9(b) as retrieval.

## 3. Alternative In-Class Activities (additional options)

**A. p-value factory (15 min, Part 3 alternative or opener).** Using Week 11's simulation skills: draw 1,000 pairs of samples from the *same* population, run a t-test on each, plot the 1,000 p-values. The histogram is flat, and ~50 fall below 0.05 with H₀ true by construction. Then plant a real difference and re-run — the distribution piles up near zero. One notebook, both core ideas of the week (false positives are guaranteed at scale; power moves mass toward zero), discovered rather than asserted.

**B. Green jelly beans opener (3 min).** Project the xkcd "Significant" cartoon (jelly beans and acne, 20 colours, one p < 0.05, headline follows). It is T3 in comic form, takes three minutes, and gives the class a shared shorthand ("that's a jelly-bean result") for the rest of the course.

**C. The garden of forking paths (20 min, Part 4 alternative).** All teams get the same messy dataset and the same vague brief: "test whether weekday affects sales." Each team makes its own choices (which days to group, outliers in or out, one- or two-tailed, mean or median) and reports its p-value. The board fills with different p-values from identical data. Debrief: none of these teams cheated — that's what researcher degrees of freedom means, and why T5(f)'s pre-specification rule exists.

**D. Significance court (15 min, Part 3 alternative).** A p = 0.049 result (from a small-n trial) is "on trial": prosecution argues for the budget reallocation, defence argues against, jury (rest of class) must issue a verdict *and* name what evidence would have settled it (bigger n, effect size, replication). Rehearses the after-class LinkedIn prompt live.

**E. Assumption triage drill (10 min, fast-finisher).** Eight one-line scenarios; students pick the right test (one-sample t / two-sample t / paired t / z-proportion / chi-square / "none of these — data violate assumptions"). The sixth option is the point: knowing when *not* to test is objective 2's missing half.

## 4. Critique of the Lesson Plan

**What works (keep):** the two-sample-size Berlin rent controversy (the cleanest statistical-vs-practical design in the 22 weeks); T5(f) on post-hoc one-tailing; T3(d) on pre-registration; the five-principles whiteboard list; Part 4's individual-then-triads structure (which finally solves the per-student timing problem the earlier weeks kept hitting — reuse this pattern in Weeks 4, 5, 11, 12).

**Problems, reasons, and fixes:**

1. **T4(d) is mathematically wrong — the flagship example fails.** With n = 2,000,000, SE = √(0.92 × 0.08/2,000,000) = **0.000192**, not 0.0000192 (the key dropped a factor of √100). So z = 0.0001/0.000192 ≈ **0.52, p ≈ 0.60 — not remotely significant**, and the intended lesson ("trivially small improvement, highly significant") collapses. *Fix:* keep n = 2,000,000 but use p̂ = 0.921 (the same 0.1pp effect as Trial B): z = 0.001/0.000192 ≈ **5.21** — a clean escalation of Trial B (same effect, 10× data, p ≈ 0 instead of 0.099). Then update the (e) memo: 0.1pp on 2M deliveries = 2,000 deliveries, not "0.01pp / 200."
2. **T2's given p-value contradicts its own data.** 150 vs 120 violations per 1,000,000: pooled p̂ = 0.000135, SE ≈ 1.64 × 10⁻⁵, z ≈ 1.83, two-tailed p ≈ **0.068** — not 0.018. Any student who checks (and T7 trains them to check) finds the question wrong. *Fix:* change Group A to 160 detections (z ≈ 2.39, p ≈ 0.017 ≈ the stated 0.018), and update (b)'s difference to 0.004pp. Also: Meta's report is the **Community Standards Enforcement Report** (the "Adversarial Threat Report" is a different publication) — correct the name of a source students are invited to look up.
3. **Part 2's T2 walkthrough and Design Challenge 1 describe a T2 that no longer exists.** Both discuss "50,000 visitors each; 10 additional conversions; p = 0.031; €50,000 homepage redesign" — an A/B-test scenario from an earlier draft, replaced by the Meta case. This is the third week (with 4 and 11) where instructor-facing guidance describes superseded questions; a systematic consistency pass across all 22 files is now clearly warranted. *Fix:* rewrite both passages around the Meta numbers (the corrected ones from point 2).
4. **Part 3's n = 48,000 t-statistic doesn't follow from the stated inputs.** With x̄ = 14.78, μ₀ = 14.50, s = 2.10: t = 0.28/(2.10/√48,000) ≈ **29**, not 12.3. *Fix:* either state that the administrative dataset has s ≈ €5.00 (plausible — administrative data is more heterogeneous, and saying so is itself instructive) or change the printed t to ≈29. The pedagogy survives either way; the arithmetic must cohere because students are explicitly prompted to ask "why do the two datasets differ?"
5. **The paired t-test appears in objective 2 and nowhere else.** No tutorial, quiz item, or activity touches it, yet it's exam-relevant (A&W §8-7b/9-4b territory). *Fix:* adopt T8/Q10; it also carries the week's best power discussion (T8(c)–T9).
6. **§9-5 emphasised, never used (see §1.1).** Adopt T10 or soften.
7. **Inline solutions still printed inside submitted problems** (T4, T5, T6). Recurring defect, same fix — and this week it's sharpest: T4's inline "solution" is the *wrong* one (point 1), which students would have transcribed as their submission.
