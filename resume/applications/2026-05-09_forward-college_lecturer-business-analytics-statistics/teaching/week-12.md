# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 12: Confidence Interval Estimation
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Construct confidence intervals for a population mean (t-distribution), a population proportion (z-distribution), and a population standard deviation (chi-square distribution) using Excel functions
- Interpret a confidence interval correctly — and identify the most common misinterpretation
- Determine the required sample size to achieve a specified margin of error for a mean or proportion
- Critique a published confidence interval from a real report or news article

These map to ST2187 syllabus topic 9 (estimation) and are the direct application of the sampling distribution framework established in Week 11. Without the CLT and standard error, confidence intervals are just a formula. With them, they are a precise statement about how uncertain our estimate is.

These objectives operate at the **application and evaluation** levels of Bloom's Taxonomy — constructing intervals from data and evaluating published intervals for validity and honest interpretation.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 8 — read the following sections only:
- §8-1 Introduction to confidence intervals (pp. 312–314)
- §8-2 Sampling distributions — the t distribution and others (pp. 314–317)
- §8-3 Confidence interval for a mean (pp. 317–326)
- §8-5 Confidence interval for a proportion (pp. 326–331)
- §8-6 Confidence interval for a standard deviation — chi-square interval (pp. 331–335)
- §8-9 Sample size selection (pp. 344–352)

The two-sample CI sections (§8-7 and §8-8, pp. 335–344) are in scope for the exam but not the focus of this session — read them before Week 13 if you want a preview.

*Rationale:* Chapter 8 is formula-heavy. The formulas must be in place before the session, because in-class time is for interpretation and application, not transcription. Students who arrive without having computed at least T1 and T2 will lose the pair-work benefit.

**Videos (~20 minutes total):**
- [Confidence Intervals — StatQuest](https://www.youtube.com/watch?v=TqOeMYtOc1w) (12 min) — builds from CLT to CI. *Active watching: when StatQuest explains what "95% confident" actually means — the sampling procedure, not the probability that the true mean is inside one specific interval — pause and write the correct interpretation in your own words before the video continues. This is the single most tested concept in Week 12 and the exact question T5 asks.*
- [t-Distribution vs z-Distribution — StatQuest](https://www.youtube.com/watch?v=T0xRanwAIiI) (8 min) — when to use which. *Active watching: when the video explains why we use t instead of z when σ is unknown and n is small, pause and note: what would go wrong if you used z anyway? This reasoning tells you when to apply T.INV.2T vs NORM.INV in T1 and T2.*

**Worked example (read this before attempting the tutorial problems):**

> **Scenario:** A courier company times 25 randomly selected deliveries. The sample mean is 43 minutes; the sample standard deviation is 8 minutes. The population distribution of delivery times is approximately normal. Construct a 95% confidence interval for the mean delivery time.
>
> **Step 1 — Choose the right interval:**
> Population variance is unknown (we only have the sample SD); n = 25 < 30. Use the t-distribution with df = n − 1 = 24.
>
> **Step 2 — Excel:**
> t* = T.INV.2T(0.05, 24) = 2.064
> Margin of error = t* × (s / √n) = 2.064 × (8 / √25) = 2.064 × 1.6 = 3.30 minutes
> 95% CI: (43 − 3.30, 43 + 3.30) = **(39.7, 46.3) minutes**
>
> **Step 3 — Interpretation:**
> We are 95% confident that the population mean delivery time is between 39.7 and 46.3 minutes.
>
> **The wrong interpretation (extremely common):** "There is a 95% probability that the true mean is in this interval." This is wrong. The true mean is fixed — it is either in the interval or it isn't. The 95% refers to the *method*: if we drew 100 samples and built 100 CIs this way, about 95 of them would contain the true mean.
>
> **Step 4 — Sample size planning:**
> If the company wants the margin of error to be at most 2 minutes (and they still believe σ ≈ 8), how large a sample do they need?
> n = (z × σ / B)² = (1.96 × 8 / 2)² = (7.84)² = 61.5 → **n = 62**

*This worked example is marked optional for students who feel confident constructing a t-interval from a sample mean and SD and can state the correct interpretation of a CI without prompting. If you already wrote the correct interpretation (from the StatQuest video pause exercise) before reading this, you don't need it. If the "wrong interpretation" in Step 3 surprised you — if you would have written that sentence yourself — read the worked example carefully.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T0 — Entry question (lower floor):*

> A polling company surveys 500 randomly selected voters and finds that 47% support a proposed policy. The company reports: "The margin of error is ±4 percentage points at 95% confidence."
>
> (a) Write the confidence interval in the form (lower bound, upper bound).
> (b) Write one sentence correctly interpreting what "95% confidence" means in this context.
> (c) A journalist reports: "There is a 95% probability that the true level of support is between 43% and 51%." Is this statement correct? If not, what is wrong with it?
>
> No calculation required — the numbers are provided. This is an interpretation question only.

T0 establishes whether students understand confidence intervals as a property of the *method* rather than a probability statement about a fixed (unknown) parameter. This is the most persistent misconception in Week 12 and is explicitly tested in T5. Students who cannot answer T0(b) correctly have not yet understood the CI concept; the formula mechanics of T1–T3 will not help them.

*Self-check for T0:* (a) (43%, 51%). (b) Correct interpretation: if this polling procedure were repeated many times, approximately 95% of the resulting intervals would contain the true proportion. (c) The journalist's statement is incorrect — the true proportion is fixed (not random), so "probability" that it falls in this specific interval is either 0 or 1; the 95% refers to the long-run reliability of the method. If you initially wrote an interpretation similar to the journalist's, re-read the "wrong interpretation" in the worked example before T1.

*T1 — t-interval for mean:*

*The worked example's Step 2 formula (t* × s/√n) is exactly what T1(a) requires. The StatQuest video on t vs z is the reason you use T.INV.2T, not NORM.INV, in T1(a): n = 30 and σ is unknown.*
> Supplier A delivers machine parts. A sample of 30 parts has mean diameter 99.8mm and SD 1.2mm.
>
> (a) Construct a 95% CI for the population mean diameter. [T.INV.2T(0.05, 29)]
> (b) Is 100mm (the target diameter) inside the interval? What does this imply?
> (c) A second supplier (Supplier B) gives a different sample of 30 parts with mean 100.3mm and SD 4.5mm. Construct a 95% CI for Supplier B's mean diameter.
> (d) The CIs for A and B overlap. Does that mean there's no difference between the suppliers? (Be careful.)

T1(d) is the most important conceptual question: overlapping CIs do not prove the means are equal. The formal test is a two-sample t-test (Week 13). This is a preview of why Week 13 is necessary.

*Self-check for T1(a):* t* = T.INV.2T(0.05, 29) ≈ 2.045. SE = 1.2/√30 ≈ 0.219. Margin of error = 2.045 × 0.219 ≈ 0.448. 95% CI: (99.8 − 0.45, 99.8 + 0.45) = **(99.35, 100.25) mm**. If your interval is substantially wider or narrower, check that you used the t-distribution (not z) and df = 29.

*T2 — Proportion interval:*
> A random sample of 200 customers shows 72 preferred the new product design (36%).
>
> (a) Construct a 90% CI for the proportion. [Use p̂ = 0.36, z = NORM.INV(0.95, 0, 1)]
> (b) A manager claims "about a third of our customers prefer the new design." Is this supported by the interval?
> (c) How large a sample would be needed to reduce the margin of error to ±3 percentage points at 95% confidence? [n = (1.96 / 0.03)² × 0.36 × 0.64]

*T3 — Chi-square interval for SD:*
> A machine produces components with a target standard deviation of 0.030mm. A sample of 50 components has SD = 0.034mm.
>
> (a) Construct a 95% CI for the population standard deviation. [CHISQ.INV.RT(0.025, 49) and CHISQ.INV(0.025, 49)]
> (b) Does the CI include 0.030mm? What does this tell you about the machine's consistency?

T3 is the least intuitive of the three — the chi-square CI is asymmetric, which surprises students who expected the same symmetric interval as the t and z cases.

*T4 — Boundary cases: what happens when n is very small or very large:*

> (a) **Very small n:** A pharmacist measures the active ingredient concentration in n = 5 samples from a new batch. The sample mean is 98.2mg and the sample SD is 3.1mg. Construct a 95% CI for the population mean concentration.
>
> *Solution:* df = 4; t* = T.INV.2T(0.05, 4) = 2.776. SE = 3.1/√5 = 1.386. ME = 2.776 × 1.386 = 3.847. 95% CI: (98.2 − 3.85, 98.2 + 3.85) = **(94.4, 102.1) mg.** Note how wide the interval is for n = 5.
>
> (b) With n = 5, is the t-interval valid? What assumption about the population distribution is especially important when n is this small?
>
> (c) **Very large n:** A streaming platform measures satisfaction scores from n = 50,000 users, with sample mean 7.12 and SD 1.85 (on a 1–10 scale). Construct a 99% CI for the mean satisfaction score.
>
> *Solution:* For large n, t* ≈ z* = NORM.INV(0.995, 0, 1) = 2.576. SE = 1.85/√50,000 = 0.00828. ME = 2.576 × 0.00828 = 0.0213. 99% CI: **(7.099, 7.141).** The interval is extremely narrow.
>
> (d) The 99% CI from part (c) is (7.099, 7.141). The company's satisfaction target is 7.0. A manager says: "The CI doesn't include 7.0, so we've clearly met the target." Is this an appropriate use of the confidence interval?
>
> (e) With n = 50,000, the CI is so narrow that it is almost always going to exclude any specific target value. What does this imply about using CIs for decision-making at very large n?

*T5 — Interpretation: the correct and incorrect statements:*

> A 95% CI for the mean time (in seconds) to complete an online checkout process is (42.3, 47.1), based on a sample of n = 80 customers.
>
> For each of the following statements, state whether it is **correct** or **incorrect**, and explain in one sentence why.
>
> (a) "There is a 95% probability that the true mean checkout time is between 42.3 and 47.1 seconds."
> (b) "If we collected 100 random samples of the same size and built 95% CIs for each, approximately 95 of those intervals would contain the true mean checkout time."
> (c) "95% of all customers complete checkout between 42.3 and 47.1 seconds."
> (d) "We are 95% confident that the sample mean is between 42.3 and 47.1 seconds."
> (e) "The true mean checkout time is definitely between 42.3 and 47.1 seconds."
> (f) "This interval is consistent with a true mean of 44 seconds."
>
> *Answers:* (a) Incorrect — the true mean is fixed; probability statements about fixed values are not valid in the frequentist framework. (b) Correct — this is the textbook definition of the frequentist CI. (c) Incorrect — this confuses the CI for the mean with a prediction interval for individual values. (d) Incorrect — the sample mean is a fixed number (44.7); it is not in an interval. (e) Incorrect — we cannot say "definitely"; we can only say "this method produces intervals that contain the true mean 95% of the time." (f) Correct — 44 is within (42.3, 47.1).

*T6 — Multi-step: sample size determination and its trade-offs:*

> A consultancy is designing a customer satisfaction survey for a European bank. The bank has approximately 800,000 retail customers. The consultancy wants to estimate the proportion satisfied with the bank's mobile app.
>
> (a) Using a conservative estimate p̂ = 0.50 (maximises required n) and a margin of error of ±4 percentage points at 95% confidence, what sample size is needed?
>
> *Solution:* n = (1.96/0.04)² × 0.50 × 0.50 = (49)² × 0.25 = 2,401 × 0.25 = **600.25 → n = 601**
>
> (b) A pilot study of 100 customers finds that 72% are satisfied with the mobile app. Using this estimate (p̂ = 0.72) instead of the conservative p̂ = 0.50, recalculate the required sample size. How does it compare?
>
> *Solution:* n = (1.96/0.04)² × 0.72 × 0.28 = 2,401 × 0.2016 = **484.2 → n = 485.** Less than with p̂ = 0.50.
>
> (c) The bank requests a margin of error of ±2 percentage points instead of ±4. How does halving the margin of error affect the required sample size?
>
> *Solution:* Halving ME quadruples n. Required n ≈ 601 × 4 = **2,404** (using conservative p̂ = 0.50).
>
> (d) The consultancy proposes surveying 400 customers — less than the required 601. What is the actual margin of error achieved with n = 400 at 95% confidence (using p̂ = 0.50)?
>
> *Solution:* ME = 1.96 × √(0.50 × 0.50 / 400) = 1.96 × 0.025 = **±4.9 percentage points.**
>
> (e) The bank's CEO says: "With 800,000 customers, surely we need to survey a lot more than 601." Explain why the required sample size for estimating a proportion to a given precision does not depend on the population size (for large populations), and what this means for survey design.

*T7 — Comparison: three CI types side by side:*

> A quality control engineer samples 40 components from a new production line. She records the diameter of each component. Results: sample mean = 50.4mm, sample SD = 1.2mm, sample proportion meeting spec = 0.82, sample variance = 1.44mm².
>
> (a) Construct a 95% CI for the population mean diameter using the t-distribution. [T.INV.2T(0.05, 39)]
>
> *Solution:* t* = 2.023. SE = 1.2/√40 = 0.190. ME = 2.023 × 0.190 = 0.384. 95% CI: **(50.02, 50.78) mm**
>
> (b) Construct a 95% CI for the population proportion meeting specification.
>
> *Solution:* z* = 1.96. SE = √(0.82 × 0.18 / 40) = √(0.00369) = 0.0607. ME = 1.96 × 0.0607 = 0.119. 95% CI: **(0.701, 0.939)**
>
> (c) Construct a 95% CI for the population standard deviation of diameter using the chi-square interval. [CHISQ.INV.RT(0.025, 39) and CHISQ.INV(0.025, 39)]
>
> *Solution:* χ²_{0.025, 39} = CHISQ.INV.RT(0.025, 39) ≈ 58.12; χ²_{0.975, 39} = CHISQ.INV(0.025, 39) ≈ 23.65.
> Lower bound: √((39 × 1.44) / 58.12) = √(0.9664) ≈ **0.983 mm**
> Upper bound: √((39 × 1.44) / 23.65) = √(2.374) ≈ **1.541 mm**
> 95% CI for σ: **(0.983, 1.541) mm**
>
> (d) The chi-square interval in (c) is asymmetric — the lower bound is 0.417mm below the sample SD (1.2), while the upper bound is 0.341mm above it. Explain why this asymmetry occurs and why the interval is not symmetric around s = 1.2mm.
>
> (e) The specification requires diameter SD ≤ 1.0mm. The CI for σ is (0.983, 1.541). What does this tell you about whether the process meets the specification? Can you conclusively say it does or does not meet spec?

---

## Answer Key

### T0 — Interpreting a margin of error (entry question)

**(a)** 95% CI: **(43%, 51%).**

**(b)** Correct interpretation: "If this polling procedure were repeated many times with different random samples of 500 voters, approximately 95% of the resulting confidence intervals would contain the true proportion of voters who support the policy."

**(c)** The journalist's statement is **incorrect.** "There is a 95% probability that the true level of support is between 43% and 51%" implies the true proportion is a random variable with a 95% chance of falling in this specific interval. That is not correct: the true population proportion is a fixed (unknown) number — it does not have a probability of being anywhere. Once the interval is computed, it either contains the true proportion or it doesn't. The 95% refers to the *long-run reliability of the method*, not to any probability statement about this particular interval.

---

### T1 — t-interval for mean (machine parts)

**(a)** t* = T.INV.2T(0.05, 29) ≈ 2.045. SE = 1.2/√30 ≈ 0.219. ME = 2.045 × 0.219 ≈ 0.448. 95% CI: (99.8 − 0.45, 99.8 + 0.45) = **(99.35, 100.25) mm.**

**(b)** Yes — 100mm is inside the interval (99.35, 100.25). This implies the data are consistent with the target diameter of 100mm: we cannot conclude from this sample that Supplier A's mean diameter differs significantly from 100mm at the 5% level.

**(c)** t* = T.INV.2T(0.05, 29) ≈ 2.045. SE = 4.5/√30 ≈ 0.822. ME = 2.045 × 0.822 ≈ 1.681. 95% CI for Supplier B: (100.3 − 1.68, 100.3 + 1.68) = **(98.62, 101.98) mm.**

**(d)** Overlapping CIs do **not** prove the means are equal. CI overlap means the data are consistent with the means being equal — but it does not formally test for a difference. Two CIs can overlap while the two-sample t-test still detects a statistically significant difference. The formal test for comparing means is the two-sample t-test (Week 13), not a visual inspection of CI overlap. Supplier A's interval is much narrower (tight supplier); Supplier B's is wide (high variability). The appropriate action is to run a formal two-sample test, not to conclude "no difference" from overlapping intervals.

---

### T2 — Proportion interval (product preference)

**(a)** p̂ = 72/200 = 0.36. z = NORM.INV(0.95, 0, 1) ≈ 1.645 (for 90% CI, use z corresponding to 0.05 in each tail). SE = √(0.36 × 0.64/200) = √(0.001152) ≈ 0.03394. ME = 1.645 × 0.03394 ≈ 0.0558. 90% CI: (0.36 − 0.056, 0.36 + 0.056) = **(0.304, 0.416)** or approximately **(30.4%, 41.6%).**

**(b)** Yes — "about a third" (33.3%) is contained within the interval (30.4%, 41.6%). The manager's claim is supported by the data at 90% confidence.

**(c)** n = (z/ME)² × p̂ × (1 − p̂) = (1.96/0.03)² × 0.36 × 0.64 = (65.33)² × 0.2304 = 4,268 × 0.2304 ≈ **983.** Approximately 983 customers are needed to achieve a margin of error of ±3 percentage points at 95% confidence. (Using p̂ = 0.36 from the existing sample — if using the conservative p̂ = 0.50, the required n rises to (1.96/0.03)² × 0.25 ≈ 1,068.)

---

### T3 — Chi-square CI for standard deviation

**(a)** χ²_{upper} = CHISQ.INV.RT(0.025, 49) ≈ 70.22; χ²_{lower} = CHISQ.INV(0.025, 49) ≈ 31.55.
Lower bound for σ: √((49 × 0.034²)/70.22) = √((49 × 0.001156)/70.22) = √(0.000806) ≈ **0.0284 mm.**
Upper bound for σ: √((49 × 0.001156)/31.55) = √(0.001795) ≈ **0.0424 mm.**
95% CI for σ: **(0.0284, 0.0424) mm.**

**(b)** The target of σ = 0.030mm is **inside** the interval (0.0284, 0.0424). This means the data are consistent with the machine's target consistency — we cannot conclude from this sample that the true SD differs significantly from 0.030mm. However, the interval also includes values up to 0.0424mm — substantially above target — so the data cannot rule out worse-than-target consistency either. The machine may or may not be meeting spec; a larger sample is needed to narrow this interval.

---

### T4 — Boundary cases (small n and large n)

**(a)** df = 4; t* = T.INV.2T(0.05, 4) ≈ 2.776. SE = 3.1/√5 ≈ 1.386. ME = 2.776 × 1.386 ≈ 3.847. 95% CI: (98.2 − 3.85, 98.2 + 3.85) = **(94.35, 102.05) mg.** The interval spans nearly 8mg — very wide relative to the acceptable range for a pharmaceutical product.

**(b)** With n = 5, the t-interval is technically valid if the **population distribution is approximately normal.** When n is this small, the CLT has not kicked in; the t-distribution's derivation assumes the original population is normal. If the distribution of active ingredient concentrations is skewed (e.g., due to batch contamination), the t-interval may be unreliable. For pharmaceutical quality control, n = 5 is dangerously small — regulatory bodies typically require larger validation samples.

**(c)** For n = 50,000, t* ≈ z* = NORM.INV(0.995, 0, 1) ≈ 2.576. SE = 1.85/√50,000 ≈ 0.00828. ME = 2.576 × 0.00828 ≈ 0.0213. 99% CI: **(7.099, 7.141)** — a width of only 0.042 points on a 1–10 scale.

**(d)** This is an **inappropriate use** of the CI. With n = 50,000, the standard error is so tiny that the interval excludes almost any specific target value — including values that are practically indistinguishable from the true mean. The CI says "7.0 is excluded" — but the difference between the interval's lower bound (7.099) and the target (7.0) is 0.099 points on a 10-point scale. Is a 0.099-point difference in satisfaction score a meaningful business achievement? Probably not. The CI tells you the estimate is precise; it does not tell you whether the estimate is practically significant.

**(e)** At very large n, CIs become so narrow that they will almost always exclude any specific target value — making every business comparison "statistically significant." This renders the CI useless for decision-making if the decision threshold is a single point (e.g., "is the mean at least 7.0?"). The appropriate remedy is to combine the CI with an effect-size consideration: "Is the difference between our estimate and the target practically meaningful?" A CI from n = 50,000 tells you very precisely what the mean is; it does not tell you whether that mean is good enough.

---

### T5 — Correct and incorrect CI interpretations

**(a)** **Incorrect.** The true mean checkout time is a fixed unknown number — it does not have a probability of being in any interval. The 95% refers to the method, not to the probability that this specific interval contains the fixed true mean.

**(b)** **Correct.** This is the frequentist definition of a 95% CI: if the procedure of sampling and computing the interval were repeated many times, 95% of the resulting intervals would contain the true mean.

**(c)** **Incorrect.** This confuses the CI for the **mean** with a prediction interval for **individual values.** The CI bounds where the population mean is likely to lie. The statement would require a prediction interval, which is wider — it captures where an individual observation is likely to fall, accounting for both estimation uncertainty and individual variability.

**(d)** **Incorrect.** The sample mean is a single computed number — in this case, the midpoint of the interval (42.3 + 47.1)/2 = 44.7 seconds. The sample mean is not "in an interval"; it is a fixed point used to construct the interval. This statement confuses the parameter being estimated with the point estimate itself.

**(e)** **Incorrect.** We cannot say "definitely" — we are 95% confident, which means this interval was constructed by a method that works 95% of the time. This particular interval may be one of the 5% that does not contain the true mean. The word "definitely" is not warranted.

**(f)** **Correct.** 44 seconds lies within (42.3, 47.1), so 44 seconds is a plausible value for the true mean at this confidence level. The interval is consistent with a true mean of 44 seconds.

---

### T6 — Sample size determination (bank survey)

**(a)** n = (1.96/0.04)² × 0.50 × 0.50 = (49)² × 0.25 = 2,401 × 0.25 = 600.25 → **n = 601.** Using the conservative estimate p̂ = 0.50 (which maximises the required sample size, providing a safety margin regardless of the true proportion).

**(b)** With p̂ = 0.72: n = (1.96/0.04)² × 0.72 × 0.28 = 2,401 × 0.2016 ≈ 484.2 → **n = 485.** Lower than the conservative estimate, because the proportion is further from 0.50 — a less uncertain prior reduces the required sample.

**(c)** Halving the margin of error (from 4% to 2%) **quadruples** the required sample size. Required n ≈ 601 × 4 = **2,404** (using conservative p̂ = 0.50). This is because the ME formula involves n in the denominator under a square root: to halve ME, n must increase by a factor of 4.

**(d)** ME with n = 400: ME = 1.96 × √(0.50 × 0.50/400) = 1.96 × 0.025 = **±4.9 percentage points.** The consultancy's proposed n = 400 achieves only ±4.9pp precision instead of the required ±4pp.

**(e)** The required sample size formula for a proportion, n = (z/ME)² × p̂(1−p̂), does not include the population size N. This is correct for large populations (when the sampling fraction n/N is small, as is the case here with n/N ≈ 601/800,000 ≈ 0.075%). The precision of an estimate depends on the **absolute sample size**, not on what fraction of the population is sampled. Intuitively: drawing 601 people from 800,000 and drawing 601 people from 8,000,000 produce equally precise estimates, as long as both samples are random. The CEO's intuition — that a larger population requires a larger sample — is a common misconception without statistical justification for large populations.

---

### T7 — Three CI types side by side

**(a)** t* = T.INV.2T(0.05, 39) ≈ 2.023. SE = 1.2/√40 ≈ 0.190. ME = 2.023 × 0.190 ≈ 0.384. 95% CI for mean: **(50.016, 50.784) mm** ≈ **(50.02, 50.78) mm.**

**(b)** z* = 1.96. SE = √(0.82 × 0.18/40) = √(0.003690) ≈ 0.0607. ME = 1.96 × 0.0607 ≈ 0.119. 95% CI for proportion: (0.82 − 0.119, 0.82 + 0.119) = **(0.701, 0.939).**

**(c)** χ²_{0.025, 39} = CHISQ.INV.RT(0.025, 39) ≈ 58.12; χ²_{0.975, 39} = CHISQ.INV(0.025, 39) ≈ 23.65.
Lower σ = √((39 × 1.44)/58.12) = √(0.9664) ≈ 0.983 mm. Upper σ = √((39 × 1.44)/23.65) = √(2.374) ≈ 1.541 mm. 95% CI for σ: **(0.983, 1.541) mm.**

**(d)** The asymmetry arises because the chi-square distribution is **right-skewed**, not symmetric. The chi-square critical values at the 2.5th and 97.5th percentiles (23.65 and 58.12) are not equidistant from the mean (39). The interval for σ is constructed by dividing (n−1)s² by these two different critical values — a larger divisor (58.12) produces a smaller lower bound; a smaller divisor (23.65) produces a larger upper bound. Since 58.12 − 39 ≠ 39 − 23.65, the bounds are not symmetric around s.

**(e)** The specification requires σ ≤ 1.0mm, but the 95% CI for σ is (0.983, 1.541) mm. The lower bound of 0.983mm is just below the target of 1.0mm, while the upper bound (1.541mm) is well above it. This means the data are **consistent with meeting the specification** (σ could be below 1.0mm) but also **consistent with failing it** (σ could be up to 1.541mm). We cannot conclusively say the process does or does not meet spec — the interval straddles the specification threshold. A larger sample would narrow this interval. If precision to σ ≤ 1.0mm matters for product quality, the current evidence is ambiguous and additional sampling is recommended before certifying the process as in-spec.

---

**Pre-class submission (on the course portal):**

Find a published confidence interval — from a news article, an academic abstract, a government report, or a company investor communication. Submit:
1. What is the interval? What is it an interval for?
2. How is it described or interpreted in the source?
3. Is the interpretation correct? (Check: does the source say "95% probability" or "95% confident"?)

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

**Easy — vocabulary and recall:**

- Q1: When the population standard deviation is unknown and n is small, we use:
  *(a) z-distribution  (b) t-distribution  (c) Chi-square distribution  (d) F-distribution)*

- Q2: As sample size increases, the width of a confidence interval:
  *(a) Increases  (b) Decreases  (c) Stays the same  (d) Depends only on the confidence level)*

- Q3: T.INV.2T(0.05, 29) gives the t-value for:
  *(a) 95% CI with df = 29  (b) 90% CI with df = 30  (c) 95% CI with n = 30  (d) 5% significance level, one-tailed)*

- Q4: The margin of error for a proportion CI is:
  *(a) z × σ/√n  (b) z × √(p̂(1−p̂)/n)  (c) t × s/√n  (d) χ² × s)*

- Q5: If the 95% CI for a mean is (42.3, 49.7), the point estimate is:
  *(a) 42.3  (b) 49.7  (c) 46.0  (d) 3.7)*

- Q6: A 99% CI is ___ than a 95% CI for the same data.
  *(a) Narrower  (b) Wider  (c) The same width  (d) More accurate)*

**Medium — application:**

- Q7: A 95% CI for a proportion is (0.31, 0.45). Which statement is correct?
  *(a) There is a 95% probability that the true proportion is between 0.31 and 0.45  (b) If we repeated this sampling 100 times, about 95 intervals would contain the true proportion  (c) 95% of all observations in the population are between 0.31 and 0.45  (d) The true proportion is 0.38)*

Q7 is the most important question in the quiz — and the most commonly wrong. The correct answer is (b). Option (a) is the nearly universal misinterpretation.

- Q8: To halve the margin of error (keeping confidence level fixed), you need to:
  *(a) Double the sample size  (b) Quadruple the sample size  (c) Halve the sample size  (d) Double the confidence level)*

**Hard — conceptual:**

- Q9: A report states: "We found no significant difference between the groups because the 95% CIs overlapped." This conclusion is:
  *(a) Correct — overlapping CIs confirm no difference  (b) Incorrect — overlapping CIs are consistent with differences; a formal two-sample test is needed  (c) Correct if and only if the samples are the same size  (d) Incorrect — overlapping CIs confirm a difference)*

**Instructor acts on results (5 minutes)**

Q7 is the anchor — name the misinterpretation directly: "The probability interpretation is wrong. Once the interval is calculated, the true mean is either in it or it isn't — there is no probability left. The 95% refers to the method, not this interval." Q9 previews Week 13 — if it splits the room, let it: "We'll resolve that next week."

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T1(d) — overlapping CIs don't prove equal means — is the most important to establish before Week 13. This is a conceptual prerequisite: if students leave today believing that overlapping CIs prove no difference, Week 13 is harder.

T3 — the asymmetric chi-square CI — is worth showing: "The lower bound uses CHISQ.INV.RT(0.025, 49) and the upper bound uses CHISQ.INV(0.025, 49). The interval is not symmetric because the chi-square distribution is not symmetric."

The buffer: use it on T1(d) or Q7 — the correct interpretation of a CI is the hardest conceptual lift in this session.

---

### Part 3 — Case Study: Interpret a Real Interval (25 minutes)

The class receives three published confidence intervals from real sources (instructor prepares in advance):

**Case 1 — A news headline about a poll:**
"A survey of 1,200 adults found that 54% support the policy, with a margin of error of ±3 percentage points (95% confidence)."

Questions for pairs:
- What is the 95% CI? (51%–57%)
- The headline says "majority support." Is that warranted by the interval?
- What does "95% confidence" mean — and what would the journalist need to change to make the claim stronger?

**Case 2 — A company investor report:**
"Our new process reduces mean production time to 34.2 minutes (95% CI: 33.8 to 34.6 minutes). The previous process had a mean of 36.0 minutes."

Questions for pairs:
- Is the CI consistent with a genuine reduction vs. the previous 36.0 minutes? (Yes — 36.0 is far outside the interval)
- The report does not give the CI for the old process. Why does that matter?
- What assumptions underlie this CI — and what would violate them?

**Case 3 — A medical study abstract:**
"The intervention group had a mean recovery time of 7.3 days (95% CI: 5.9 to 8.7 days); the control group had a mean of 9.1 days (95% CI: 7.6 to 10.6 days). The authors conclude the intervention is effective."

Questions for pairs:
- Do the CIs overlap? What does that mean for the conclusion?
- Does overlapping CIs mean there's no difference? (Q9 revisited — no. Need a formal two-sample test.)
- What additional information would you need to evaluate the claim?

After 15 minutes, pairs report back (2 minutes each). Instructor synthesises: what makes a CI claim honest vs. misleading?

---

### Part 4 — Pre-Submission Debrief (20 minutes)

Students share their published CIs from the pre-submission. For each:
- What is it an interval for?
- Is the interpretation in the source correct?
- What would change if the confidence level were 90% instead of 95%?

The instructor collects the misinterpretations on the board. Expected result: most published sources use "95% probability" language. This is almost always wrong — and it appears in medical journals, news articles, and corporate filings.

**Punchline:** the most common misinterpretation of CIs is not made by students — it's made by professionals who publish for a living. Understanding the correct interpretation is a competitive advantage, not a pedantic distinction.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop:**

*"What is a confidence interval actually telling you? Not the common misinterpretation — the correct one."*

It is a procedure, not a probability. The interval is constructed so that if we used this procedure on 100 different random samples, 95 of the 100 intervals would contain the true parameter. We have one interval. We don't know if it's one of the 95 or one of the 5. That uncertainty is not reducible by looking at the interval — it's inherent in the method.

**Bridge forward to Week 13:**

> *"The confidence interval gave us a range. Hypothesis testing asks a sharper question: is a specific value plausible? If our 95% CI for the mean delivery time is (39.7, 46.3) minutes — and the company's target is 40 minutes — does the data support the claim that we're hitting the target? That's a hypothesis test. Same data, different question."*

---

## After Class (Student Post-Work, ~30 minutes)

Students write an LMS post on one of:
- The most egregious misinterpretation they found in their pre-submission — and how they'd correct it
- The Case 3 medical study: does the conclusion hold? What would make it more convincing?
- What they'd want to know before acting on a published CI from an investor communication

Peer response: one comment that adds a condition under which the CI interpretation would change (e.g., what if the sampling was not random?).

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Three distinct CI types in one session (t, z, chi-square) | The ST2187 exam tests all three; the pre-work establishes the formulas; in-class time is for interpretation and critique, not formula derivation |
| Q7 as the most important quiz question (not hardest) | Black & Wiliam (1998): formative assessment with feedback loops — Q7 reveals the single most consequential misconception and allows real-time correction before the case study |
| Case study uses three real published intervals | Ausubel (1968): self-relevance and concreteness; published intervals from news, business, and medical contexts mirror exactly where students will encounter CIs in professional life |
| Overlapping CIs question (T1(d), Q9, Case 3) introduced three times | Cepeda et al. (2006): spacing effect — the same conceptual point encountered in tutorial, quiz, and case study produces stronger retention than a single exposure |
| Pre-submission asks students to find and critique a published CI | Bjork (1994): desirable difficulties; finding and critiquing a real example requires more than recognising a correct definition — it requires active evaluation |
| Bridge forward uses delivery time example to connect CI to hypothesis test | Ausubel (1968): assimilation theory — new concept (hypothesis test) is introduced as a variant of the existing concept (CI) using the same data; the contrast makes the distinction clear |
| LMS post focuses on misinterpretation correction, not CI construction | Week 12's learning goal is interpretation; the post reinforces that goal; construction exercises belong in the tutorial |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Q7 (correct interpretation) and Q9 (overlapping CIs) are the key moments |
| Tutorial review | 15 min | T1(d) overlapping CIs; T3 asymmetric chi-square |
| Buffer (explicit) | 10 min | Extended Q7 discussion or T1(d) deliberation |
| Case study: interpret real intervals | 25 min | Three cases; 15 min pairs + 10 min class report-back |
| Pre-submission debrief | 20 min | ~90 sec per student; collect misinterpretations on board |
| Instructor debrief | 10 min | Correct interpretation; bridge to Week 13 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. The correct interpretation of a CI is counterintuitive and hard to hold onto.

Students who correctly state "95% of intervals constructed this way contain the true mean" in Week 12 often revert to "there's a 95% probability the true mean is in this interval" when answering exam questions. The distinction is subtle and degrades under time pressure.

**Resolution:** the quiz (Q7), the case study (all three cases), and the debrief all require correct interpretation. The pre-submission requires finding and critiquing a published misinterpretation. Four separate encounters with the correct formulation in one session produces better retention than one definitional statement.

---

### 2. Three CI types (t, z, chi-square) may feel like three separate things rather than one general framework.

Students who memorise three separate formulas will struggle on questions that require choosing the right one. The fundamental logic is the same: point estimate ± margin of error, where the margin depends on the distribution, the confidence level, and the standard error.

**Resolution:** frame all three explicitly as variants of the same structure before diving into formulas. "The method is always: point estimate ± (critical value × standard error). What changes is (a) which critical value (t, z, or chi-square) and (b) what the standard error formula is." Draw one template, fill it in three times.

---

### 3. The chi-square CI is asymmetric — which surprises students trained on symmetric intervals.

The formula involves (n−1)s²/χ²_upper and (n−1)s²/χ²_lower, with different chi-square critical values for the upper and lower bounds. This produces an interval that is not symmetric around s.

**Resolution:** explain why: the chi-square distribution is right-skewed — the critical values are not equidistant from the mean. Show a sketch of the chi-square distribution with the 0.025 and 0.975 tails marked. The asymmetry follows from the shape; it is not arbitrary.

---

### 4. Students may over-generalise from the case study and conclude CIs from news or medical studies are always wrong.

After seeing three published intervals with problematic interpretations, some students may conclude "no published CI is trustworthy." This is too strong.

**Resolution:** in the Part 5 debrief, the instructor should name the gradation: some CIs are correctly stated (just use the right language); some have interpretation errors (fixable with a correction); some have sampling or design flaws (no CI can fix those). The skill is distinguishing which problem you're looking at.

---

### 5. Sample size calculation (T2(c)) requires a circular argument that students find confusing.

To find n for a proportion CI, you need to plug in p̂ — but you don't have p̂ until you've collected the data. The conservative assumption (p̂ = 0.5, which maximises n) is the standard solution, but it isn't obvious why.

**Resolution:** show both: "If you have a prior estimate of p = 0.36 from a previous study, use 0.36. If you don't, use 0.5 — it gives the largest required n, which is the safest assumption." The key principle is: conservatism in sample size planning costs money (larger sample) but protects against underpowering (which costs credibility). For an exam question, always state the assumption being made.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Farmus, L., Cribbie, R.A. & Rotondi, M. (2020). The flipped classroom in introductory statistics. *Journal of Statistics Education*, 28(3). DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
