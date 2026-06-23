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
- [Confidence Intervals — StatQuest](https://www.youtube.com/watch?v=TqOeMYtOc1w) (12 min) — builds from CLT to CI
- [t-Distribution vs z-Distribution — StatQuest](https://www.youtube.com/watch?v=T0xRanwAIiI) (8 min) — when to use which

**Worked example (attempt T1–T3 first, then read this):**

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

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T1 — t-interval for mean:*
> Supplier A delivers machine parts. A sample of 30 parts has mean diameter 99.8mm and SD 1.2mm.
>
> (a) Construct a 95% CI for the population mean diameter. [T.INV.2T(0.05, 29)]
> (b) Is 100mm (the target diameter) inside the interval? What does this imply?
> (c) A second supplier (Supplier B) gives a different sample of 30 parts with mean 100.3mm and SD 4.5mm. Construct a 95% CI for Supplier B's mean diameter.
> (d) The CIs for A and B overlap. Does that mean there's no difference between the suppliers? (Be careful.)

T1(d) is the most important conceptual question: overlapping CIs do not prove the means are equal. The formal test is a two-sample t-test (Week 13). This is a preview of why Week 13 is necessary.

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
