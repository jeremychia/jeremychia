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

The sampling distribution of the sample proportion (§7-4c) is important for Week 12 — read it if time allows, but it is not the focus of this session.

*Rationale:* the CLT is counterintuitive. The reading alone is unlikely to produce genuine understanding for most students — the in-class simulation (Part 3) is the mechanism. The pre-work establishes vocabulary and the formal statement; understanding comes in class.

**Videos (~20 minutes total):**
- [Sampling Distributions — StatQuest](https://www.youtube.com/watch?v=XLCWeSVzHUU) (12 min) — visual walkthrough of what happens when you draw repeated samples
- [Central Limit Theorem — 3Blue1Brown](https://www.youtube.com/watch?v=zeJD6dqJ5lo) (8 min) — geometric intuition

The StatQuest video is essential. Students who watch it will arrive with the visual model of a sampling distribution that makes the simulation in Part 3 legible.

**Worked example (attempt T1–T3 first, then read this):**

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

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T1 — Vocabulary and identification:*
> A national survey of 2,000 adults finds that 58% prefer remote work. The true proportion in the entire working population is 61%.
>
> (a) Which number is the parameter? Which is the statistic?
> (b) What is the sampling error?
> (c) Why is the sampling error not zero, even with a well-designed survey?
> (d) What would reduce the sampling error — and what wouldn't?

T1(d) is the key question: increasing sample size reduces sampling error; better design doesn't reduce random sampling error (it reduces bias). Students often conflate these.

*T2 — Standard error:*
> Household incomes in a city are distributed with mean €42,000 and standard deviation €18,000. Incomes are right-skewed.
>
> (a) A sample of n = 9 households is taken. Can you use the CLT to find P(X̄ > €50,000)? Why or why not?
> (b) A sample of n = 100 households is taken. Now compute P(X̄ > €50,000).
> (c) What does your answer to (b) tell you about the probability of a single randomly chosen household having income > €50,000? (Different question — don't confuse them.)

T2(c) is the most common confusion in probability questions about means: P(X̄ > 50,000) with n = 100 is not the same as P(X > 50,000) for a single observation. The standard error for a sample mean is smaller than the population SD by √n.

*T3 — Sampling bias:*
> An online retailer surveys customer satisfaction by emailing customers immediately after purchase. 78% of respondents rate their experience as "excellent."
>
> (a) Identify two sources of sampling bias in this design.
> (b) The CEO says "78% of our customers are satisfied." Critique this claim.
> (c) How would you redesign the survey to reduce bias — while keeping it practical?

T3(a): response bias (customers who respond to satisfaction emails are not random — they are likely either very satisfied or very dissatisfied) and timing bias (immediately post-purchase captures the emotional high, not the considered view). T3(c) requires practical trade-offs: random sampling from the customer database at 30 days post-delivery is better but more expensive.

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

T2(b) vs (c) is the comparison that matters: P(X̄ > 50,000 | n=100) ≈ 0.1% vs P(X > 50,000 | single household) ≈ 33%. The mean of 100 incomes has a standard error of €1,800 — a value of €50,000 is 4.4 standard errors above the mean. A single income of €50,000 is only (50,000 − 42,000)/18,000 = 0.44 standard deviations above the mean — far more likely.

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
