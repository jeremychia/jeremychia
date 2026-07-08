# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 11: Sampling and Sampling Distributions
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Distinguish between a population parameter and a sample statistic, and explain why we estimate rather than calculate
- State the Central Limit Theorem (CLT) and identify the conditions under which it applies
- Compute the standard error of the mean and interpret it as a measure of sampling variability
- Evaluate a claim about sampling bias — identifying when a sample is likely to systematically misrepresent the population

These map to ST2187 syllabus topics 8 and 9 (sampling and estimation) and form the conceptual foundation for Weeks 12 (confidence intervals) and 13 (hypothesis testing). Students who don't understand the sampling distribution of the mean cannot correctly interpret a confidence interval or a p-value.

These objectives operate at the **application and analysis** levels of Bloom's Taxonomy — not just stating the CLT, but reasoning about when it holds and what it implies for a specific inferential claim.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 7 — read the following sections only:
- §7-2 Sampling terminology: population, sample, statistic, parameter (pp. 280–282)
- §7-3 Methods for selecting random samples — simple random, stratified, cluster (pp. 282–292)
- §7-4 Introduction to estimation: sampling distribution of the sample mean and the Central Limit Theorem (pp. 292–307)

Note: §7-4c is the Sampling Distribution of the *Sample Mean* — the core of this session, not optional. Chapter 7 has no sample-proportion section; the proportion analogue used in T5–T6 follows the same σ/√n logic with σ = √(p(1−p)) and is treated formally in §8-5 (Week 12). §7-4a (Sources of Estimation Error, p. 292) is the textbook's own treatment of this week's central distinction between sampling error and bias.

*Rationale:* the CLT is counterintuitive. The reading alone is unlikely to produce genuine understanding for most students — the in-class simulation (Part 3) is the mechanism. The pre-work establishes vocabulary and the formal statement; understanding comes in class.

**A note on pre-work expectations for this week:** The CLT is counterintuitive. Many students find the formal statement in the reading clear but cannot yet see why it matters or feel confident about it — that is expected and normal. The in-class simulation (Part 3) is designed to resolve this. Your job in pre-work is to arrive knowing the vocabulary (sampling distribution, standard error, standard error formula, CLT conditions) so the simulation makes sense when you see it. If you finish the reading and still feel uncertain about the CLT itself, that is the correct outcome of Week 11 pre-work. Confidence with the CLT comes after the simulation, not before it.

**Videos (~20 minutes total):**
- [Sampling Distributions — StatQuest](https://www.youtube.com/watch?v=XLCWeSVzHUU) (12 min) — visual walkthrough of what happens when you draw repeated samples. *Active watching: watch for the moment the histogram of sample means appears. Pause and write: what happens to the shape and width of this histogram as the sample size n increases? The answer you write is the CLT in plain language. This visual is exactly what the simulation in Part 3 will produce — your T2(b) calculation is the numerical version of what you just watched.*
- [Central Limit Theorem — 3Blue1Brown](https://www.youtube.com/watch?v=zeJD6dqJ5lo) (8 min) — geometric intuition. *Active watching: when 3Blue1Brown explains why the normal shape emerges regardless of the original distribution's shape, pause and write: what is it about repeated averaging that produces this result? The answer connects to T4(a) — what n is "large enough" for the CLT to apply.*

The StatQuest video is essential. Students who watch it will arrive with the visual model of a sampling distribution that makes the simulation in Part 3 legible.

**Worked example (read this before attempting the tutorial problems):**

> **Scenario:** A factory produces bolts. The target diameter is 10mm. The production process has a mean of 10.05mm and a standard deviation of 0.8mm. The diameter distribution is slightly right-skewed.
>
> **Question:** A quality inspector takes a sample of n = 36 bolts and computes the sample mean diameter. What is the probability that the sample mean is more than 10.2mm?
>
> **Step 1 — Identify the sampling distribution:**
> Even though the population is slightly right-skewed, with n = 36 ≥ 30, the CLT applies. The sample mean X̄ is approximately normally distributed with:
> - Mean μ_X̄ = μ = 10.05
> - Standard error SE = σ / √n = 0.8 / √36 = 0.8 / 6 = 0.133mm
>
> **Step 2 — Standardise:**
> Z = (X̄ − μ) / SE = (10.2 − 10.05) / 0.133 = 0.15 / 0.133 ≈ 1.13
>
> **Step 3 — Compute probability:**
> P(X̄ > 10.2) = P(Z > 1.13) = 1 − NORM.DIST(10.2, 10.05, 0.133, TRUE) ≈ 1 − 0.871 = **12.9%**
>
> **Interpretation:** Even though the process is slightly off-target, about 13% of samples of 36 bolts will have a sample mean above 10.2mm — not because individual bolts are that far off, but because of sampling variability. This is not a quality failure in a single sample; it is expected variation.
>
> **The key insight:** the standard error (0.133mm) is much smaller than the population SD (0.8mm). The sample mean is far less variable than individual measurements. This is *why* we average: averaging reduces noise.

*This worked example is marked optional for students who already feel confident computing standard error (SE = σ/√n) and using the CLT to find a probability about a sample mean. If you can write the formula for SE and apply it to a new scenario without guidance, you don't need this. If the steps from "population is slightly skewed" to "CLT applies, so X̄ is approximately normal" felt unclear, work through each step carefully.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T0 — Entry question (lower floor):*

> A hospital records the blood pressure (systolic, in mmHg) of every patient admitted last year — 12,000 patients in total. The population mean is 128 mmHg and the population standard deviation is 18 mmHg.
>
> A researcher then draws a random sample of 100 patients from those records and computes the sample mean blood pressure.
>
> (a) Write one sentence identifying which number (128 or the sample mean) is the parameter, and which is the statistic.
> (b) Without doing any calculation, write one sentence explaining why the sample mean is unlikely to be exactly 128 mmHg, even if the sample is randomly drawn.
> (c) Would you expect the sample mean to be more or less variable than any individual patient's blood pressure? Write one sentence explaining why.
>
> No formula required. Plain language only.

T0 establishes the vocabulary — parameter vs statistic, sampling variability, why averages are less variable than individuals — that T1–T3 assume. Students who cannot answer T0 have not yet understood what sampling is for. The question requires only conceptual understanding from §7-2, not any calculation.

*Self-check for T0:* (a) 128 mmHg is the parameter (the true population mean); the sample mean is the statistic (an estimate from one sample). (b) Random sampling produces different samples each time; chance variation means the sample mean will rarely equal the population mean exactly. (c) The sample mean will be less variable — averaging 100 values reduces random fluctuation compared to a single observation; this is why we sample. If any of these felt uncertain, re-read §7-2 and the worked example before T1.

*T1 — Vocabulary and identification:*

*The StatQuest video's histogram of sample means narrowing as n increases is the visual version of what T2(b) calculates: SE = σ/√n = 18,000/√100 = 1,800. The wider the histogram, the larger the SE; the narrower, the smaller.*
> A national survey of 2,000 adults finds that 58% prefer remote work. The true proportion in the entire working population is 61%.
>
> (a) Which number is the parameter? Which is the statistic?
> (b) What is the sampling error?
> (c) Why is the sampling error not zero, even with a well-designed survey?
> (d) What would reduce the sampling error — and what wouldn't?

T1(d) is the key question: increasing sample size reduces sampling error; better design doesn't reduce random sampling error (it reduces bias). Students often conflate these.

*Self-check for T1(a)–(b):* (a) Parameter: 61% (the true population proportion); statistic: 58% (the sample proportion). (b) Sampling error = 58% − 61% = −3 percentage points (the sample underestimates the true value). If you reversed parameter and statistic, re-read §7-2 before T2.

*T2 — Standard error:*

> According to the UK Office for National Statistics (ONS) Family Resources Survey 2022/23, median household disposable income in the UK was approximately £35,400 per year (equivalised). The distribution of household income is substantially right-skewed — a small number of very high-income households pull the mean above the median. For this question, use the following approximate parameters for UK household disposable income:
>
> - Mean (μ) = £38,000 per year
> - Standard deviation (σ) = £22,000 per year
> - Distribution: highly right-skewed (individual household incomes cannot be modelled as normal)
>
> (a) A journalist samples n = 9 households in a single postcode district and computes a sample mean income of £45,000. Can she use the CLT to make probability statements about this sample mean? Why or why not?
>
> (b) The ONS Annual Survey of Hours and Earnings (ASHE) samples approximately n = 180,000 employees for its earnings estimates. A regional analyst takes a much smaller random sample of n = 100 households from a city. Compute the standard error of the sample mean, and calculate P(X̄ > £42,000).
>
> *Solution:* SE = 22,000 / √100 = 2,200. Z = (42,000 − 38,000) / 2,200 = 1.818. P(X̄ > 42,000) ≈ **3.4%**
>
> (c) Your answer to (b) gives the probability that the *sample mean* from 100 households exceeds £42,000. What is the probability that a *single randomly chosen household* has income above £42,000? Why are these two questions different — and why can't you calculate the second one from the parameters given?
>
> (d) A think tank publishes a report saying: "In a random sample of 100 UK households, we found a mean income of £44,500. This is substantially above the ONS reported mean of £38,000 — suggesting ONS figures understate actual income." Using the standard error from (b), assess whether a sample mean of £44,500 is surprising under the null hypothesis that μ = £38,000. What is the Z-score for this sample mean?
>
> *Solution:* Z = (44,500 − 38,000) / 2,200 = 6,500 / 2,200 ≈ 2.95. P(X̄ ≥ 44,500) ≈ 0.16% — very unlikely under H₀. But this does not mean the ONS figures are wrong; it may mean the think tank's sample was not representative (e.g., oversampled high-income areas).

T2 now uses publicly available ONS data (ONS Family Resources Survey 2022/23 is accessible at ons.gov.uk). The right-skewed income distribution is a real feature of UK household income data, and the right-skew/CLT tension is the core learning point. Part (d) adds a realistic misinterpretation of sample evidence — the kind that appears in advocacy reports and policy debates — which students must evaluate using standard error logic.

*T3 — Sampling bias:*
> An online retailer surveys customer satisfaction by emailing customers immediately after purchase. 78% of respondents rate their experience as "excellent."
>
> (a) Identify two sources of sampling bias in this design.
> (b) The CEO says "78% of our customers are satisfied." Critique this claim.
> (c) How would you redesign the survey to reduce bias — while keeping it practical?

T3(a): response bias (customers who respond to satisfaction emails are not random — they are likely either very satisfied or very dissatisfied) and timing bias (immediately post-purchase captures the emotional high, not the considered view). T3(c) requires practical trade-offs: random sampling from the customer database at 30 days post-delivery is better but more expensive.

*T4 — Boundary case: what the CLT does and does not guarantee:*

> A population of invoice payment times at a company is extremely right-skewed: most invoices are paid within 7 days, but some large corporate clients take 90–180 days to pay. The distribution has mean μ = 22 days and SD σ = 35 days.
>
> (a) An auditor takes a sample of n = 9 invoices. Can she use the CLT to compute probabilities about the sample mean? Explain your answer.
> (b) The auditor increases her sample to n = 100 invoices. Now calculate P(X̄ > 28 days).
>
> *Solution:* SE = 35 / √100 = 3.5 days. Z = (28 − 22) / 3.5 = 1.714. P(X̄ > 28) = 1 − NORM.DIST(28, 22, 3.5, TRUE) ≈ 1 − 0.9567 ≈ **4.3%**
>
> (c) A colleague says: "With n = 100, the sample mean will be normally distributed and we can compute any probability we want." Is this statement fully accurate? What might limit its reliability for extreme percentiles (e.g., the 99th percentile of X̄)?
> (d) The company's finance team wants to know: "What is the probability that a single randomly selected invoice takes more than 60 days to pay?" Can you answer this from the population parameters alone (without knowing the full distribution shape)? Explain.
> (e) What sample size would be required to ensure the standard error is less than 2 days?
>
> *Solution:* SE = σ/√n < 2 → √n > 35/2 = 17.5 → n > 306.25 → **n ≥ 307**

*T5 — Multi-step: effect of sample size on inference decisions:*

> A public health agency estimates disease prevalence (proportion of population infected) using a random sample from a city of 2 million people. The true proportion is unknown; based on early data, they expect approximately p ≈ 0.08 (8%).
>
> (a) What is the standard error of the sample proportion p̂ for: (i) n = 100; (ii) n = 400; (iii) n = 1,600?
>
> *Solution:* SE = √(p(1−p)/n) = √(0.08 × 0.92 / n) = √(0.0736/n)
> n=100: SE ≈ 0.0271; n=400: SE ≈ 0.0136; n=1,600: SE ≈ 0.0068
>
> (b) Each quadrupling of n halves the SE. If the agency is working with a fixed budget that covers n = 400, but the SE of 1.36 percentage points is considered too wide, what n would be required to halve the SE again to 0.68 percentage points?
> (c) A researcher argues: "We sampled 400 people from a city of 2 million — that's only 0.02% of the population. Our estimate cannot possibly be representative." Is this argument valid? What matters more: the sampling fraction or the absolute sample size?
> (d) Suppose the agency takes samples from two different cities of very different sizes: City A (population 50,000) and City B (population 2,000,000). Both samples have n = 400. Will the standard error of p̂ be the same for both cities, or will it differ? Explain.
> (e) What assumption about the sampling process is required for the formulas in (a) to be valid? Name the sampling method and describe what would bias the estimate.

*T6 — Comparison: sampling bias versus sampling variability:*

> A political polling company wants to estimate the proportion of voters who support a proposed infrastructure policy. They conduct two studies:
>
> **Study 1 — Random telephone survey:** 600 randomly selected registered voters are contacted. Of these, 180 respond (response rate 30%), and 54% support the policy.
>
> **Study 2 — Online opt-in poll:** A link is shared on the company's website. 2,400 people complete the poll, and 62% support the policy.
>
> (a) Which study has lower sampling variability (smaller standard error)? Calculate the SE for both studies (use p̂ = 0.54 and p̂ = 0.62 respectively).
>
> *Solution:* SE₁ = √(0.54 × 0.46 / 600) ≈ 0.0204. But with only 180 respondents: SE₁ (effective) = √(0.54 × 0.46 / 180) ≈ 0.0372. SE₂ = √(0.62 × 0.38 / 2400) ≈ 0.0099.
>
> (b) Which study gives a more reliable estimate of true voter opinion, and why? (The answer is not determined by which has the larger n.)
> (c) In Study 1, the response rate is 30%. What is this an example of, and in what direction might it bias the estimate if policy supporters are more likely to respond?
> (d) In Study 2, only people who visit the website and choose to respond are included. Name this type of bias. Would you expect it to systematically over- or under-estimate support for an infrastructure policy?
> (e) A manager says: "The online study has a much bigger sample, so we should use its results." Write a two-sentence response that distinguishes between sampling variability and sampling bias, and explains why larger n cannot correct for the latter.

*T7 — Real-world translation: design a sampling strategy:*

> A supermarket chain operates 85 stores across three regions: North (25 stores), Midlands (35 stores), South (25 stores). The company wants to estimate mean weekly revenue per store (to within ±€2,000 at 95% confidence), and also to be able to compare revenues across regions. Historical data suggests the SD of weekly revenue across all stores is approximately €18,000, though it is higher in the South (€22,000) due to more variable demand.
>
> (a) If the company takes a simple random sample of stores, how many stores must be sampled to achieve the desired margin of error? (Use σ = €18,000 and assume z = 1.96.)
>
> *Solution:* n = (z × σ / ME)² = (1.96 × 18,000 / 2,000)² = (17.64)² ≈ 311. Since there are only 85 stores total, n = 85 means a census. The required precision may need to be relaxed, or the margin of error treated as approximately achievable from the full population.
>
> (b) The calculation in (a) suggests the company would need to survey most or all stores. What does this tell you about the relationship between the desired precision and the population size?
> (c) Instead of simple random sampling, the company proposes stratified sampling: sample proportional to the number of stores in each region (25/85, 35/85, 25/85). If the total sample is n = 30 stores, how many would be selected from each region?
> (d) The company wants to compare revenues across regions as well as estimate the overall mean. For the regional comparison, would simple random or stratified sampling be more appropriate? Why?
> (e) A store manager says: "Instead of random sampling, we should include the 30 largest stores — they account for the most revenue." What type of bias would this introduce, and how would it affect the estimate of mean revenue per store?

---

## Answer Key

### T0 — Population parameter vs sample statistic

**(a)** 128 mmHg is the **parameter** — it is the true population mean, calculated from all 12,000 patients. The sample mean computed from the 100-patient sample is the **statistic** — it is an estimate derived from the sample, not the full population.

**(b)** The sample mean is unlikely to equal exactly 128 mmHg because random sampling produces different samples each time. Even a perfectly designed random sample will, by chance, contain slightly different patients in different draws — their average will fluctuate randomly around the true population mean, rarely landing exactly on it.

**(c)** The sample mean will be **less variable** than any individual patient's blood pressure. Averaging 100 measurements smooths out the random variation in individual readings: extreme high values in one patient are offset by lower values in another. The sample mean is a more stable quantity than any single measurement.

---

### T1 — Vocabulary and sampling error

**(a)** Parameter: **61%** (the true proportion in the entire working population). Statistic: **58%** (the proportion found in the sample of 2,000 adults).

**(b)** Sampling error = 58% − 61% = **−3 percentage points.** The sample underestimates the true proportion by 3 percentage points.

**(c)** Sampling error is not zero even in a well-designed survey because random sampling involves selecting different individuals each time. By chance, the 2,000 people selected may include slightly more remote-work opponents than the underlying population — not because of bias, but because of random variation inherent in any finite sample.

**(d)** What would reduce sampling error: **increasing the sample size** (a larger sample produces a smaller standard error, reducing random fluctuation). What would NOT reduce sampling error: using a telephone survey instead of an online survey; improving the question wording; increasing the response rate. These may reduce bias but do not reduce the random variation inherent in sampling. The key distinction: sampling error (random) vs bias (systematic) require different solutions.

---

### T2 — Standard error and CLT (UK income)

**(a)** No — she **cannot** use the CLT to make probability statements about a sample of n = 9. The CLT requires approximately n ≥ 30 for a highly right-skewed distribution; household income has extreme right-skew, so n = 9 is far too small. The sampling distribution of the mean from 9 households will still be noticeably right-skewed — the CLT has not yet kicked in. Additionally, a single postcode district is not a random sample of the UK population, so any inference to the national mean would be invalid regardless of n.

**(b)** SE = σ/√n = 22,000/√100 = **£2,200.** Z = (42,000 − 38,000)/2,200 = 1.818. P(X̄ > £42,000) = 1 − NORM.DIST(42,000, 38,000, 2,200, TRUE) ≈ 1 − 0.9655 ≈ **3.45%.** With n = 100 and the CLT invoked (n = 100 ≥ 30), the sample mean is approximately normally distributed even though individual incomes are right-skewed.

**(c)** P(X̄ > £42,000) ≈ 3.4% is the probability that the **sample mean** from 100 households exceeds £42,000. The probability that a **single household** has income above £42,000 requires knowing the shape of the individual income distribution — which is highly right-skewed and cannot be treated as normal for a single observation. We cannot compute it from μ and σ alone without knowing the shape. The sample mean is averaging out the extreme skew; a single observation is still subject to it.

**(d)** Z = (44,500 − 38,000)/2,200 = 6,500/2,200 ≈ **2.95.** P(X̄ ≥ £44,500) = 1 − NORM.DIST(44,500, 38,000, 2,200, TRUE) ≈ **0.16%.** A sample mean this high is very unlikely under the null hypothesis μ = £38,000. However, this does not mean the ONS figures are wrong. The most likely explanation is that the think tank's sample was not representative — for example, it oversampled high-income areas, used a convenience sample, or had a specific response bias. The conclusion "ONS figures understate actual income" requires establishing that the think tank's sampling method was superior to the ONS's, which the report does not do.

---

### T3 — Sampling bias (retailer satisfaction survey)

**(a)** Two sources of bias: (i) **Response bias (self-selection):** customers who choose to respond to a satisfaction email are not a random subset. Those with very strong experiences — either very positive or very negative — are more likely to respond; indifferent customers (who may be the majority) tend not to respond. This systematically skews the sample away from the centre. (ii) **Timing bias:** surveying customers immediately after purchase captures an initial emotional response (the "purchase high"), not their considered view based on actual product use, delivery experience, or customer service over time. Customers who later experience problems were surveyed before those problems occurred.

**(b)** The CEO's claim is misleading. The statistic "78% of respondents rated their experience as 'excellent'" describes satisfied survey-respondents, not all customers. The denominator is the wrong population — the meaningful comparison is all customers, not the self-selected minority who chose to respond. A defensible claim would be: "78% of customers who responded to our post-purchase satisfaction email within [X days] rated their experience as 'excellent'."

**(c)** A more representative design would: (i) randomly sample from the customer database (not wait for voluntary responses) at a fixed time post-delivery (e.g., 14 days after receipt, capturing the full product experience); (ii) use a short, multi-channel survey (SMS or in-app) with a small incentive to reduce non-response bias; (iii) track the non-response rate and, if it exceeds ~30%, run a brief follow-up to the non-respondents to assess whether they differ systematically from respondents. The key trade-off: random sampling with follow-up is more expensive but more credible; the current email approach is cheap but produces a statistic the CEO cannot meaningfully use.

---

### T4 — Boundary cases: CLT conditions

**(a)** **No** — with n = 9 and an extremely right-skewed distribution (most invoices paid in 7 days, some taking 90–180 days), the CLT does not apply. The sampling distribution of the mean from n = 9 will still be substantially right-skewed. The rule of thumb of n ≥ 30 for the CLT assumes moderate skewness; for this extreme distribution, n may need to be 100+ before the sampling distribution is approximately normal.

**(b)** SE = 35/√100 = **3.5 days.** Z = (28 − 22)/3.5 = 1.714. P(X̄ > 28) = 1 − NORM.DIST(28, 22, 3.5, TRUE) ≈ **4.3%.** At n = 100, the CLT applies well enough for practical purposes even with this skewed distribution.

**(c)** The statement is not fully accurate. The CLT guarantees approximate normality for the bulk of the distribution, but the approximation is less reliable in the extreme tails. For the 99th or 99.9th percentile of X̄, the normal approximation may still be inaccurate even at n = 100 when the population is very skewed. In risk management or tail-risk contexts (e.g., estimating the probability of an extreme average payment delay), this caveat matters.

**(d)** **No** — this question cannot be answered from μ and σ alone. P(single invoice takes more than 60 days) requires knowing the full distributional shape of individual invoice times. With μ = 22 and σ = 35, and a highly right-skewed distribution, a single observation of 60+ days is plausible but cannot be quantified without knowing the specific shape (e.g., exponential, log-normal, or empirical). The CLT tells us about sample means, not individual observations.

**(e)** SE = σ/√n < 2 → √n > 35/2 = 17.5 → n > 306.25 → **n ≥ 307** invoices.

---

### T5 — Effect of sample size (disease prevalence)

**(a)** SE = √(p(1−p)/n) = √(0.08 × 0.92/n):
- n = 100: SE = √(0.000736) ≈ **0.0271 (2.71 percentage points)**
- n = 400: SE = √(0.000184) ≈ **0.0136 (1.36 percentage points)**
- n = 1,600: SE = √(0.0000460) ≈ **0.0068 (0.68 percentage points)**

**(b)** To halve SE from 1.36% to 0.68%: need to quadruple n. **n = 1,600.** Precision improves with the square root of n — halving SE requires four times the sample.

**(c)** The researcher's argument is **invalid.** What matters for the precision of a sample estimate is the **absolute sample size**, not the sampling fraction (n/N). The formula SE = √(p(1−p)/n) does not involve the population size N (for large populations where the finite population correction is negligible). A sample of 400 from a population of 2 million is just as precise as a sample of 400 from a population of 50,000, as long as the sample is drawn randomly. The sampling fraction of 0.02% is irrelevant; n = 400 is n = 400.

**(d)** The standard error will be **essentially the same** for both cities. SE = √(p(1−p)/n) does not depend on population size (for large populations). The only case where population size matters is when the sampling fraction exceeds ~5% (use a finite population correction factor). With n = 400 and City A's population of 50,000: sampling fraction = 0.8%, which is small — the correction is negligible. Both estimates are equally precise.

**(e)** Required assumption: **simple random sampling** (every member of the population has an equal probability of being selected). What would bias the estimate: quota sampling (interviewing only people who happen to be at certain locations); telephone surveys (excluding those without phones or who don't answer); voluntary response (those who self-select to respond may differ systematically in health behaviour from the general population).

---

### T6 — Sampling bias vs sampling variability (political poll)

**(a)** The correct effective sample size for Study 1 is the 180 respondents (not the 600 contacted). SE₁ = √(0.54 × 0.46/180) ≈ √(0.001380) ≈ **0.0372 (3.72 percentage points).** SE₂ = √(0.62 × 0.38/2,400) ≈ √(0.0000982) ≈ **0.0099 (0.99 percentage points).** Study 2 has lower sampling variability — its larger n produces a narrower spread of estimates across repeated samples.

**(b)** **Study 1 gives a more reliable estimate of true voter opinion**, despite its smaller effective sample. The key is the randomness of the sampling frame. Study 1 used randomly selected registered voters — even with only 180 responses, the sample is drawn from the correct population with a known selection mechanism. Study 2 drew only from self-selected website visitors, which is not representative of all voters. Large n cannot substitute for a representative sampling frame.

**(c)** The 30% response rate introduces **non-response bias.** If policy supporters are more likely to respond to phone surveys (perhaps because they're more engaged with public issues), the estimate of 54% support may overstate true support. The direction and magnitude of the bias depend on how systematically non-responders differ from responders in their policy views.

**(d)** **Self-selection bias (or voluntary response bias).** Website visitors who choose to complete a poll tend to be more engaged with the company's content — potentially more likely to support infrastructure investment if the company operates in that sector, or more opinionated in either direction than the general voter. The direction of bias is context-dependent but the bias is likely systematic.

**(e)** Sampling variability measures how much a statistic fluctuates across different random samples of the same size — it is reducible by increasing n. Sampling bias is a systematic distortion caused by the sampling mechanism itself — it affects every sample drawn using the same method, regardless of size. A larger biased sample gives a more precise but equally wrong estimate. No increase in n can fix a non-representative sampling frame.

---

### T7 — Sampling strategy design (supermarket chain)

**(a)** Required n = (z × σ / ME)² = (1.96 × 18,000 / 2,000)² = (17.64)² ≈ **311 stores.** Since the chain has only 85 stores total, the required sample size exceeds the population. The precise margin of error (±€2,000) is unachievable without a census of all 85 stores — or by relaxing the margin of error requirement.

**(b)** This tells you that when the population is small relative to the desired precision, the standard sample size formula can suggest a census. For a population of 85 stores: to achieve ±€2,000 precision with σ = €18,000, you would need to sample virtually all of them. The practical lesson: for small populations, the finite population correction factor reduces the required n below the formula's naïve answer. Corrected n = 311 / (1 + 310/85) ≈ **67 stores** — still most of the population.

**(c)** Proportional stratified allocation across 85 stores (total n = 30):
- North: (25/85) × 30 ≈ **8.8 → 9 stores**
- Midlands: (35/85) × 30 ≈ **12.4 → 12 stores**
- South: (25/85) × 30 ≈ **8.8 → 9 stores**
(Rounding to integers while keeping total at 30: 9 + 12 + 9 = 30.)

**(d)** For comparing revenues across regions, **stratified sampling with equal or near-equal allocation to each region** is more appropriate than proportional sampling. With proportional allocation, the North and South each get only 9 stores — too few for a reliable regional comparison. Equal allocation (10 per region) would allow 10 vs 10 vs 10 comparisons with equal precision, at the cost of slightly less efficient overall estimation. The choice depends on the primary goal: overall precision (proportional) vs regional comparison (equal allocation).

**(e)** Selecting the 30 largest stores introduces **size-biased sampling.** The largest stores have systematically higher revenue than smaller ones — so the sample estimate of mean revenue per store would significantly **overestimate** the true mean across all 85 stores. This is not random error; it is a structural bias that cannot be corrected without knowing the selection mechanism. The store manager's intuition conflates importance (the large stores matter more to total revenue) with representativeness (the sample should reflect the distribution across all stores, not the revenue distribution).

---

**Pre-class submission (on the course portal):**

Find one example of a survey or study cited in news, policy, or business communications where the sampling method is described (or suspiciously absent). Submit:
1. What population is being claimed?
2. How was the sample drawn? What was the sample size?
3. What potential bias do you see?

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

**Easy — vocabulary and recall:**

- Q1: The standard deviation of the sampling distribution of the sample mean is called:
  *(a) The population standard deviation  (b) The standard error  (c) The margin of error  (d) The confidence interval)*

- Q2: The Central Limit Theorem says that, for large n, the sampling distribution of X̄ is approximately:
  *(a) The same shape as the population distribution  (b) Right-skewed regardless of population shape  (c) Normal, regardless of population shape  (d) Uniform)*

- Q3: The standard error of the mean is calculated as:
  *(a) σ / n  (b) σ / √n  (c) σ × √n  (d) σ²)*

- Q4: A simple random sample means:
  *(a) A small, convenient sample  (b) Every member of the population has an equal probability of being selected  (c) The sample is selected without replacement  (d) The sample is taken from a single geographic cluster)*

- Q5: As the sample size increases, the standard error:
  *(a) Increases  (b) Decreases  (c) Stays the same  (d) Becomes equal to the population standard deviation)*

- Q6: For the CLT to apply, the sample size should be roughly:
  *(a) n ≥ 5  (b) n ≥ 20  (c) n ≥ 30  (d) n ≥ 100)*

**Medium — application:**

- Q7: A population has mean 50 and standard deviation 20. A sample of n = 100 is taken. The standard error is:
  *(a) 20  (b) 2  (c) 0.2  (d) 200)*

- Q8: The same population (mean 50, SD 20). P(X̄ > 52) for n = 100 is approximately:
  *(a) 84%  (b) 16%  (c) 50%  (d) 2.5%)*

Q8: SE = 2; Z = (52 − 50)/2 = 1; P(Z > 1) ≈ 16%. Students who confuse SD with SE will get the wrong answer.

**Hard — conceptual:**

- Q9: A researcher claims that because her sample of n = 50 was randomly selected, it must be representative of the population. This claim is:
  *(a) Correct — random sampling guarantees representativeness  (b) Incorrect — random sampling minimises bias but cannot guarantee representativeness for any single sample  (c) Correct for a sample this large  (d) Incorrect — only a census guarantees representativeness)*

Q9 is the most important conceptual question. Random sampling does not guarantee representativeness in any given sample — it guarantees that the *expected* sample statistic equals the population parameter. Any individual sample may be unrepresentative purely by chance.

**Instructor acts on results (5 minutes)**

Q3 (standard error formula) and Q7 (calculation) are the mechanical baseline — if failing broadly, spend 60 seconds. Q8 connects to NORM.DIST — if failing, bridge from the formula to Excel. Q9 is the conceptual one to hold for Part 3 discussion.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T1(d) is the key point: increasing sample size reduces sampling error; changing the survey design reduces bias; these are different problems with different solutions.

T2(b) vs (c) is the comparison that matters: P(X̄ > £42,000 | n = 100) ≈ 3.4% — the sample mean has standard error £2,200, so £42,000 sits 1.8 standard errors above the mean — whereas a single household at £42,000 is only (42,000 − 38,000)/22,000 ≈ 0.18 standard deviations above the mean, entirely unremarkable. And per T2(c), the exact single-household probability cannot be computed at all without knowing the shape of the (highly skewed) income distribution.

T3 is held for Part 3.

Buffer: use on Q9 if it split the room — the distinction between "minimises bias" and "guarantees representativeness" is the conceptual anchor for Week 12.

---

### Part 3 — Simulation Lab (25 minutes)

Students run a simulation in Python or Excel that demonstrates the CLT directly.

**Python version (recommended):**

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate a right-skewed population (exponential)
np.random.seed(42)
population = np.random.exponential(scale=10, size=100_000)

# Plot the population distribution
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].hist(population, bins=50, edgecolor='black')
axes[0].set_title('Population Distribution (Exponential)')
axes[0].set_xlabel('Value')

# Draw 1000 samples of size n=5 and compute means
sample_means_5 = [np.mean(np.random.choice(population, size=5)) for _ in range(1000)]
axes[1].hist(sample_means_5, bins=30, edgecolor='black')
axes[1].set_title('Sample Means (n=5, 1000 samples)')
axes[1].set_xlabel('Sample Mean')

# Draw 1000 samples of size n=30
sample_means_30 = [np.mean(np.random.choice(population, size=30)) for _ in range(1000)]
axes[2].hist(sample_means_30, bins=30, edgecolor='black')
axes[2].set_title('Sample Means (n=30, 1000 samples)')
axes[2].set_xlabel('Sample Mean')

plt.tight_layout()
plt.show()

# Verify CLT numerically
print(f"Population mean: {population.mean():.3f}")
print(f"Population SD:   {population.std():.3f}")
print(f"SE (n=30):       {population.std() / np.sqrt(30):.3f}")
print(f"SD of means (n=30): {np.std(sample_means_30):.3f}")  # Should ≈ SE
```

**What students observe:**
- The population distribution is highly right-skewed (exponential)
- With n = 5, the distribution of sample means is still skewed — CLT hasn't kicked in
- With n = 30, the distribution of sample means is approximately bell-shaped — CLT has kicked in
- The standard deviation of sample means ≈ σ/√n (the theoretical standard error)

This is the CLT in action. Students who see this histogram transition from skewed to normal in their own code will remember it in a way that reading the theorem does not produce.

**Discussion questions after running the simulation:**
1. What would happen if we increased n to 100? (Further narrowing of the distribution, more normal)
2. What would happen if we used a different population distribution — e.g., uniform? (Same: sample means normalise with increasing n)
3. At what n does the CLT start to apply for a highly skewed distribution? (n ≥ 30 is a rule of thumb; for very heavy-tailed distributions, it may require n ≥ 100+)

---

### Part 4 — Sampling Bias Debrief (20 minutes)

Each student shares their pre-submission example (90 seconds each). The class asks for each:
- What population was being claimed?
- How was the sample actually drawn?
- What bias does this introduce?

**Target exchange:** the student who submitted the online retailer satisfaction survey from T3 (or a real equivalent). Ask: "If 78% say they're satisfied, is that a claim about customers, or about customers who respond to satisfaction emails?" The distinction is the lesson.

**Running theme:** the instructor should keep a tally on the board of the most common bias type across all examples. Typical result: selection bias (non-random sampling) dominates, followed by response bias (self-selection among those who are invited). This pattern surfaces the structural limits of survey-based claims.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop:**

*"The Central Limit Theorem tells us something remarkable: no matter how the population is distributed — skewed, bimodal, whatever — if we average enough observations, those averages will be normally distributed. Why does that matter?"*

It matters because it is the foundation for every confidence interval and hypothesis test in Weeks 12 and 13. The tools of statistical inference don't work on raw data — they work on sample means (and proportions), which, by the CLT, behave predictably even when the raw data doesn't.

**Bridge forward:**

> *"If sample means follow a normal distribution with mean μ and standard error σ/√n — we can put a range around any sample mean that we're confident contains the true μ. That range is a confidence interval. But what does '95% confident' actually mean? It doesn't mean there's a 95% probability that μ is in the interval. What does it mean?"*

Leave that question unanswered. It is the first question of Week 12.

---

## After Class (Student Post-Work, ~30 minutes)

Students write an LMS post on one of:
- A real survey they've used or read about — and one concrete way the sampling design introduced bias
- What the CLT simulation showed them that the textbook definition didn't — or didn't show them that they expected it to
- The bridge question: what do they think "95% confident" means?

Peer response: one comment that challenges the interpretation or extends the example.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Simulation as the CLT teaching mechanism, not a lecture | The CLT is counterintuitive — that averaging reduces skewness in distributions of means, not individual values. Seeing it happen in student-run code is more durable than being told it. Lovett & Greenhouse (2000): simulation-based statistics instruction produces better understanding of sampling variability |
| Exponential population chosen for simulation (highly skewed) | Makes the CLT result more dramatic and more memorable: the transformation from highly skewed to approximately normal as n increases is impossible to explain verbally but obvious visually |
| T2(c) forces distinction between P(X̄ > k) and P(X > k) | This confusion causes errors on exams and in practice; naming it in tutorial review before the student meets it on a problem set is the right time to establish the distinction |
| Q9 (random sampling ≠ guaranteed representativeness) as hardest question | The most consequential conceptual error in sampling; students who hold this misconception will misinterpret every confidence interval and p-value in Weeks 12–13 |
| Pre-submission: real survey with visible sampling method | Ausubel (1968): anchoring to a concrete example the student found themselves; 40+ nationalities produces survey examples from a wide range of public health, economic, and political contexts |
| Bridge forward leaves "95% confident" unanswered | Bjork (1994): desirable difficulties; leaving the question open creates a cognitive need that Week 12 satisfies; the answer lands better when students have already tried to form their own definition |
| Weekly Mentimeter quiz returns after Block 2 | Farmus, Cribbie & Rotondi (2020): weekly quizzes specifically moderated flipped classroom advantage in introductory statistics (g=0.43) — returning to this format in Block 3 reinforces it as a course norm |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Q3, Q8 (SE calculation); Q9 (random ≠ representative) |
| Tutorial review | 15 min | T1(d) sample size vs. bias; T2(b)+(c) comparison |
| Buffer (explicit) | 10 min | Extended Q9 discussion; T3 if it runs over |
| Simulation lab | 25 min | Python CLT simulation; three discussion questions |
| Sampling bias debrief | 20 min | ~90 sec per student; tally bias types on board |
| Instructor debrief | 10 min | Why CLT matters; bridge to Week 12 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. The CLT is taught in one session but underpins three weeks of content.

Weeks 11, 12, and 13 all depend on understanding the sampling distribution of the mean. A student who leaves Week 11 with only a procedural understanding of SE = σ/√n will struggle when Week 12 asks them to interpret what a confidence interval means.

**Resolution:** the simulation is the mechanism that bridges procedural to conceptual. The bridge question ("what does 95% confident mean?") is planted in Week 11 precisely so students arrive at Week 12 already wrestling with it. The answer to that question is not procedural — it requires understanding that the interval is constructed to cover the true parameter in 95% of repeated samples.

---

### 2. Simulation requires Python fluency that not all students have at Week 11.

Block 2 (Weeks 6–9) built Python skills. But the gap between "I followed along with live coding" and "I can run this simulation independently" is real. Some students will struggle with `np.random.choice()` or the list comprehension in the simulation.

**Resolution:** provide the simulation code as a pre-written notebook cell. Students run it, observe the output, and modify parameters (change n, change the population distribution) rather than writing it from scratch. The learning is in the observation and modification, not the writing. A student who changes `scale=10` to `scale=100` and reruns is doing genuine experimentation — that's the goal.

---

### 3. Sampling bias examples from pre-submission may cluster around surveys students have seen in their own countries.

With 40+ nationalities, some students will bring examples from political polling, others from health surveys, others from business customer satisfaction. The clustering is actually useful — but it requires the instructor to actively draw connections across domains.

**Resolution:** the instructor keeps the tally of bias types on the board (not the domains). "Selection bias appeared in the German political poll, the Singapore housing survey, and the US retail survey — the mechanism is the same even though the context is different." This actively produces the cross-domain generalisation that the diverse cohort enables.

---

### 4. The distinction between SE and SD is persistent source of confusion.

Q7 and Q8 test this directly. Many students will compute P(X̄ > 52) using σ = 20 rather than SE = 2 — getting an answer of P(Z > 0.1) ≈ 46% instead of P(Z > 1) ≈ 16%.

**Resolution:** make the distinction explicit in tutorial review with T2(b) vs (c). Draw two number lines: one for individual observations (using σ) and one for sample means (using SE). The narrower one is the sample mean distribution. "When you're asking about an individual, use σ. When you're asking about a mean, use SE."

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

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapter 7

The main section references are correct (7-2 pp. 280–282, 7-3 pp. 282–292, 7-4 pp. 292–307) — the most accurate reading list so far. Three refinements:

1. **The §7-4c note is mislabelled.** 7-4c is "Sampling Distribution of the *Sample Mean*" (p. 295) — the very heart of this session, not optional material for Week 12. There is no sample-proportion section in Chapter 7; **proportions live in Chapter 8 (§8-5)**. Consequence: T5 and T6 use SE(p̂) = √(p(1−p)/n), a formula the assigned reading never introduces. *Fix:* correct the label, and either add a two-line derivation-by-analogy in the pre-work ("a proportion is the mean of 0/1 data, so the same σ/√n logic applies with σ = √(p(1−p))") or preview §8-5 explicitly.
2. **§7-4a "Sources of Estimation Error" (p. 292) deserves explicit emphasis** — it is the textbook's own treatment of the sampling-error-vs-bias distinction that T1(d), T3, and T6 all hinge on. Cite it in the T1(d) commentary so the week's central distinction has a page number.
3. **§7-4e "Sample Size Selection" (p. 304) backs T7** and the finite-population issue that T7(b) hits; a pointer helps students who want the formula's provenance.

## 2. Extended Question Bank (with answers)

**T8 — Finite population correction (closes T7's loop with a computation):**

> The supermarket chain samples n = 30 of its N = 85 stores.
>
> (a) Compute the finite population correction factor √((N−n)/(N−1)) and the corrected SE, given σ = €18,000.
> (b) At what sampling fraction is the FPC conventionally ignored, and why was it ignorable in T5(d) but not here?
>
> **Answers:** (a) FPC = √(55/84) ≈ **0.809**. Uncorrected SE = 18,000/√30 ≈ €3,286; corrected SE ≈ 0.809 × 3,286 ≈ **€2,659** — sampling a third of the population buys ~19% more precision than the naive formula suggests. (b) Rule of thumb: ignore when n/N < ~5%. In T5(d), 400/50,000 = 0.8% — negligible; here 30/85 = 35% — material. The general lesson: population size is irrelevant to precision *except* when the sample is a large slice of it.

**T9 — Design identification drill (uses §7-3, currently under-tested):**

> Name each sampling design and its main risk: (i) A bank audits every 50th transaction in the ledger. (ii) A hotel chain randomly picks 6 of its 40 hotels and surveys *every* guest in those 6. (iii) A regulator groups firms by size band (small/medium/large) and randomly samples within each band. (iv) A researcher surveys whoever is in the university cafeteria at noon.
>
> **Answers:** (i) **Systematic sampling** — risk: periodicity in the ledger (e.g. batch postings every 50 entries) aligns with the interval, producing a badly unrepresentative sample. (ii) **Cluster sampling** — risk: guests within a hotel resemble each other, so the effective sample size is far below the guest count (intra-cluster correlation); cheap per response but statistically expensive. (iii) **Stratified sampling** — risk: essentially none for the estimate if strata weights are right; wrong weights ⇒ bias; it *improves* precision vs SRS when strata differ (the T7(d) logic). (iv) **Convenience sampling** — not a probability design at all; no SE formula applies, and no n fixes it (the T6(e) principle).

**T10 — The CLT is about means, not everything:**

> Using the Part 3 simulation population (exponential, scale 10), a student modifies the code to compute the sample **maximum** (instead of the mean) for 1,000 samples of n = 30.
>
> (a) Will the histogram of sample maxima be approximately normal? What will its shape be?
> (b) Will the sample **median**'s histogram be approximately normal? Does σ/√n give its standard error?
> (c) State precisely which statistics the CLT covers.
>
> **Answers:** (a) **No** — sample maxima follow extreme-value behaviour: right-skewed, drifting further right as n grows; averaging logic never applies to a max. (b) The median's sampling distribution *is* approximately normal for large n (medians have their own CLT-like result) but its standard error is **not** σ/√n — it is ≈ 1/(2f(m)√n), generally larger than the mean's SE for the same data. (c) The classical CLT covers **sums and means** of independent observations (and functions of them like proportions); it is not a blanket licence to treat any statistic as normal. One code edit in Part 3 makes this a live demonstration — recommended as discussion question 4.

*Additional quiz questions:*

- Q10: The standard error of a sample proportion p̂ is: *(a) p(1−p)/n (b) √(p(1−p)/n) (c) √(p(1−p))/n (d) p/√n)* — **Answer: (b)** (needed before T5; see §1.1).
- Q11: Quadrupling the sample size changes the SE by a factor of: *(a) ¼ (b) ½ (c) 2 (d) it depends on σ)* — **Answer: (b)** — the √n law in one line.
- Q12: A biased sampling method is used with n = 10,000 instead of n = 100. The estimate becomes: *(a) unbiased (b) more precise but still biased (c) less biased but less precise (d) both unbiased and precise)* — **Answer: (b)** — T6(e) as retrieval.

## 3. Alternative In-Class Activities (additional options)

**A. Random Rectangles / word-length sampling (15 min, no-code Part 3 alternative or opener).** Give students a news article; ask them to *choose* 5 "representative" words and compute mean word length, then draw 5 words using random numbers. Human-chosen samples run reliably long (salience bias); random samples centre on the truth. Plot both sets of means on the board. This classic activity demonstrates *both* of the week's ideas — bias (human selection) and sampling variability (spread of random-sample means) — with zero technology, and de-risks the Python dependency in Design Challenge 2.

**B. Class-built sampling distribution with dice or a bag (12 min, before the code).** Each student draws 5 chips from a bag whose values are right-skewed (many 1s and 2s, a few 20s), computes the mean, posts it to Mentimeter; the histogram builds live, then repeat with n = 10. The code in Part 3 then *replicates what the room just did physically* — the simulation stops being a black box.

**C. n-slider widget (5 min, Part 3 extension).** Wrap the simulation in `ipywidgets.interact(n=(2, 200))` so students drag n and watch the histogram morph continuously from skewed to normal. The "at what n does it kick in?" question (discussion Q3) becomes something they answer empirically per distribution — and heavy-tail distributions visibly need larger n.

**D. Poll postmortem (15 min, Part 4 alternative).** Present two real polls of the same event with different methods and different misses (e.g. a 2016/2020 US state poll vs exit-adjusted results, or a German election poll). Class votes which method they'd trust *before* seeing outcomes, then reveal. Discussion: was the miss variance or bias? Connects T6 to documented history rather than hypotheticals.

**E. German tank problem teaser (10 min, stretch/fast-finisher).** From 5 "captured serial numbers," teams estimate the total number of taxis in a city. Reveals that *estimator design* is a choice (max + gap correction beats 2×mean), planting the idea that statistics beyond the mean have sampling distributions too — pairs neatly with T10.

## 4. Critique of the Lesson Plan

**What works (keep):** the explicit "confusion after pre-work is the correct outcome" note (the most honest pre-work framing in the 22 weeks — it should be the template); the simulation as the teaching mechanism with parameters-not-syntax framing; T6's variance-vs-bias contrast (Study 1 vs Study 2 is exam-grade); the unanswered "95% confident" bridge.

**Problems, reasons, and fixes:**

1. **Part 2's tutorial-review guidance describes a different T2 than the one in the document.** It cites "P(X̄ > 50,000 | n=100) ≈ 0.1%", "standard error of €1,800", "(50,000 − 42,000)/18,000 = 0.44 SD" — i.e. a mean of 42,000, SD of 18,000, in **euros** — while the actual T2 uses mean £38,000, SD £22,000, SE £2,200, thresholds £42,000/£44,500, in **pounds**. This is stale text from a pre-revision draft, and it's the guidance the instructor will have open while teaching. *Fix:* rewrite the paragraph around the current numbers — the (b)-vs-(c) contrast survives: P(X̄ > 42,000) ≈ 3.4% (Z = 1.82 on SE £2,200) vs a single household at Z = (42,000 − 38,000)/22,000 = 0.18 above the mean, which is common — and the *shape* caveat from T2(c) still blocks an exact single-household number.
2. **The proportion formula is examined before it's taught (see §1.1).** T5/T6 and Week 12's CIs all need SE(p̂); the reading note points at a section that doesn't cover it. Fix per §1.
3. **Inline solutions inside submitted problems, again** — T2(b)(d), T4(b)(e), T5(a), T6(a), T7(a). Same systematic fix as Weeks 4–5: student version without keys.
4. **Q6 canonises "n ≥ 30" one question before the course complicates it.** T4(a)/(c) correctly teach that extreme skew pushes the requirement to 100+, but the quiz scores n ≥ 30 as *the* answer. *Fix:* reword Q6 to "for a moderately skewed population, the usual rule of thumb is…" — keeps the retrieval value without hard-coding the exception students just read about.
5. **Part 4's per-student arithmetic fails again** (90 s × 12–15 students = 18–22.5 min before any tallying/discussion). Same structural fix as Weeks 4–5: instructor pre-selects 5–6 diverse submissions; the bias-type tally can still cover *all* submissions since it needs only the classification, not the presentation.
6. **The simulation's discussion question 2 deserves the T10 twist.** "Try a uniform population" produces the same happy convergence — a *confirming* variation. Adding "now compute the sample maximum instead" (one-line edit) gives a *disconfirming* variation, which is what protects students from over-generalising the CLT. Recommended as the stretch task for fast finishers.
7. **Mixed currencies inside T2.** The scenario is UK/ONS (£) but downstream summaries relapse into € (see point 1). Trivial, but a document that teaches attention to units should model it.
