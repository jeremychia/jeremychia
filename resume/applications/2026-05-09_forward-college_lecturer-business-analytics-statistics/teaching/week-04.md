# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 4: Probability and Probability Distributions
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Apply the addition, multiplication, and conditional probability rules to solve multi-event probability problems
- Compute expected value and variance for a discrete random variable using SUMPRODUCT
- Identify when a situation involves base rate neglect and correct a faulty probability intuition with Bayes' rule
- Evaluate a probability claim from a newspaper or policy document for mathematical validity

These map directly to the ST2187 course outcome of enabling students to *"identify limitations and possible misuse"* of quantitative reasoning, and to the Week 4 position in the course arc: students can now describe data (Weeks 1–3) and must now quantify uncertainty before modelling decisions (Weeks 5–10).

These objectives operate at the **application and evaluation** levels of Bloom's Taxonomy (Anderson & Krathwohl, 2001) — not just rule recall but deployment of probability rules to real situations where the correct formulation is not obvious.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 4 — read the following sections only:
- §4-2 Probability essentials — rules, notation, conditional probability and Bayes' rule (pp. 142–150)
- §4-3 Probability distribution of a single random variable (pp. 150–160)

The simulation sections (§4-4–4-5) are covered in Week 18 (Monte Carlo). §4-4 is optional this week if students want a preview, but should not replace the reading above.

*Rationale:* Chapter 4 is the conceptual core that Weeks 5, 10, 11, and 12 all depend on. The sections above cover all the material needed for this session. Reading further this week reduces the returns — the later sections require the foundation established here.

**Videos (~20 minutes total):**
- [Bayes' Theorem — 3Blue1Brown](https://www.youtube.com/watch?v=HZGCoVF3YvM) — visual intuition for Bayesian updating (12 min)
- [Expected Value — StatQuest](https://www.youtube.com/watch?v=KLs_7b7SKi4) — discrete random variables and expected value (8 min)

The 3Blue1Brown video is important. Bayes' rule is algebraically simple but counterintuitive. The visual frequency-tree approach in the video is more likely to produce durable understanding than the formula alone.

**Worked example (attempt T1–T3 first, then read this):**

Read this *after* completing the tutorial problems. It models the reasoning chain for the structured controversy in Part 3.

> **Scenario:** A factory produces electronic components. 2% of components are defective. A quality control test correctly identifies 90% of defective components (sensitivity = 90%) and incorrectly flags 5% of good components as defective (false positive rate = 5%).
>
> **Question:** A component has just been flagged by the test. What is the probability it is actually defective?
>
> **Step 1 — Most people's intuition:** "The test is 90% accurate, so the component is probably defective." This is wrong.
>
> **Step 2 — Frequency tree approach:**
> Start with 10,000 components.
> - Defective: 2% × 10,000 = 200
> - Good: 98% × 10,000 = 9,800
>
> Of the 200 defective: 90% flagged → 180 correctly flagged; 20 missed.
> Of the 9,800 good: 5% flagged → 490 false positives.
>
> Total flagged = 180 + 490 = 670.
> P(defective | flagged) = 180 / 670 ≈ **26.9%**
>
> **Step 3 — Why intuition fails:**
> The base rate (2% defective) dominates. Even with a highly sensitive test, most flagged components are false positives because there are so many good components. This is base rate neglect — ignoring the prior probability.
>
> **Bayes' rule formulation:**
> P(defective | flagged) = P(flagged | defective) × P(defective) / P(flagged)
> = 0.90 × 0.02 / [(0.90 × 0.02) + (0.05 × 0.98)]
> = 0.018 / (0.018 + 0.049) = 0.018 / 0.067 ≈ 26.9% ✓
>
> **Lesson for analysts:** when someone quotes you a test's accuracy, ask: accuracy at what base rate? A test's predictive value depends on how common the thing you're testing for actually is.

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T1 — Basic probability rules:*
> A card is drawn from a standard 52-card deck.
>
> (a) What is the probability of drawing a heart?
> (b) What is the probability of drawing a king or a heart? (Be careful with overlap.)
> (c) Two cards are drawn without replacement. What is the probability both are hearts?
> (d) Are the events "first card is a heart" and "second card is a heart" independent? Explain why or why not.

Parts (a)–(c) are mechanical. Part (d) is conceptual and requires students to correctly identify that sampling without replacement creates dependence — a common error in later inference questions.

*T2 — Expected value:*
> A business can invest in one of two projects.
>
> **Project A:** 60% chance of earning €80,000; 40% chance of losing €20,000.
> **Project B:** 30% chance of earning €200,000; 70% chance of breaking even (€0).
>
> (a) Calculate the expected value of each project.
> (b) Which project has higher expected value? Which has higher variance? (Calculate both.)
> (c) A risk-averse investor chooses Project A. Is this irrational?
> (d) What additional information would you want before making a real investment recommendation?

Part (c) is the key question: expected value maximisation is not always rational — it ignores risk. Part (d) is the bridge to Week 10 (decision trees) and Week 18 (simulation): in practice, you need the full probability distribution, not just the mean.

*T3 — Conditional probability / Bayes:*
> A medical study finds that 1% of people in a population have a rare disease. A diagnostic test has 95% sensitivity (true positive rate) and 90% specificity (true negative rate, i.e., 10% false positive rate).
>
> (a) Draw a frequency tree for 100,000 people.
> (b) If a person tests positive, what is the probability they actually have the disease?
> (c) If a person tests negative, what is the probability they are disease-free?
> (d) A policy-maker says "the test is 95% accurate — we should use it for mass screening." Critique this statement.

T3 is the high-difficulty question and the core of the structured controversy in Part 3. Students who attempt this correctly are ready for the nuanced debate. Students who don't will be brought there by the class discussion.

**Pre-class submission (on the course portal):**

Find a real probability claim from a news article, government health communication, or business report. Submit:
1. What probability claim is being made?
2. What base rate is (or isn't) stated?
3. What question would you ask the author to assess whether the claim is valid?

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

**Easy — vocabulary and recall:**

- Q1: The probability that event A or event B occurs (where they can both occur) is:
  *(a) P(A) + P(B)  (b) P(A) + P(B) − P(A and B)  (c) P(A) × P(B)  (d) P(A) / P(B))*

- Q2: Two events are independent if:
  *(a) They cannot both occur at the same time  (b) Knowing one occurred doesn't change the probability of the other  (c) They have equal probabilities  (d) They are both rare)*

- Q3: The expected value of a discrete random variable is:
  *(a) The most likely outcome  (b) The average of all possible outcomes (unweighted)  (c) The weighted average of outcomes, weighted by probabilities  (d) The outcome that occurs with probability greater than 50%)*

- Q4: P(A | B) means:
  *(a) The probability of A and B  (b) The probability of A or B  (c) The probability of A given that B has occurred  (d) The probability of B given that A has occurred)*

- Q5: In a frequency tree for 10,000 people, 3% have a disease. How many in the tree have the disease?
  *(a) 3  (b) 30  (c) 300  (d) 3,000)*

- Q6: If P(A) = 0.4 and P(B) = 0.3, and A and B are independent, what is P(A and B)?
  *(a) 0.7  (b) 0.1  (c) 0.12  (d) 0.58)*

**Medium — application:**

- Q7: A coin is flipped 10 times and lands heads each time. What is the probability it lands heads on the 11th flip?
  *(a) Much less than 50% — it's "due" for tails  (b) Much more than 50% — it seems to be a biased coin  (c) Exactly 50% — past flips don't affect the next flip for a fair coin  (d) Cannot be determined)*

Q7 is the gambler's fallacy question. The correct answer depends on the assumption: if the coin is fair, (c); if we have reason to believe it's biased, (b) is partially defensible. This nuance is worth surfacing.

- Q8: You test positive for a rare disease (1% prevalence). The test is 90% accurate. Without doing any calculation, you think the probability you actually have the disease is:
  *(a) About 90%  (b) About 50%  (c) Much lower than 90% — maybe 10-20%  (d) About 1% — the base rate dominates)*

**Hard — conceptual:**

- Q9: A pharmaceutical company reports that their drug reduces the risk of a disease by 50%. The disease affects 2 in 1,000 people. After the drug, it affects 1 in 1,000. The absolute risk reduction is:
  *(a) 50%  (b) 1 in 1,000  (c) 1%  (d) The same as the relative risk reduction)*

Q9 is the relative vs. absolute risk reduction question — one of the most commonly misrepresented statistics in public health and business communications. The 50% figure is the relative risk reduction; the absolute reduction is 0.1 percentage points (1 in 1,000). Both are technically correct but dramatically different in how they frame the benefit.

**Instructor acts on results (5 minutes)**

Q1–Q6 are retrieval practice. If Q6 (independence multiplication) fails broadly, a 60-second correction is warranted. Q7 (gambler's fallacy) will typically split the room — name the nuance immediately. Q8 and Q9 are diagnostic for the structured controversy in Part 3: if students are correctly suspicious of intuition on Q8, the controversy will be substantive.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T1(d) — independence and sampling without replacement — is the most important to review. If pairs are being used for other analysis tasks later, they need to understand dependence.

T2(c) — whether choosing Project A is irrational — opens the question of risk aversion that will recur in Weeks 10 and 18. The instructor should ask: "Is there a situation where choosing B would be obviously wrong even if it has higher expected value?" (Yes: if losing is catastrophic — a small company choosing B might face bankruptcy in the loss scenario.)

T3 is held back for Part 3. Volunteers can present parts (a) and (b); part (d) is the debate prompt.

The 10-minute buffer: use it on T2(c) if the risk aversion discussion is productive. Or on Q9 (relative vs. absolute risk) if the quiz showed students couldn't distinguish them.

---

### Part 3 — Structured Controversy (25 minutes)

**Setup:** the class divides into two groups of 6–7. Both groups receive the same scenario:

> **Scenario:** A government health department is considering rolling out a mass screening programme for a rare condition (prevalence: 0.5% of the population). The test has 95% sensitivity and 92% specificity.
>
> A policy adviser says: "This test is 93.5% accurate on average. We should roll it out immediately — it will save lives."
>
> **Group A argues: the mass screening programme is justified.**
> **Group B argues: the mass screening programme needs more scrutiny before rollout.**

Each group has 10 minutes to prepare their argument. They must use at least one probability calculation to support their position.

After 10 minutes, each group has 3 minutes to present. Then 5 minutes of open debate. Then 2 minutes for the instructor to name what both sides got right.

**What both sides should find:**
- The positive predictive value: P(disease | positive) = (0.95 × 0.005) / [(0.95 × 0.005) + (0.08 × 0.995)] ≈ 5.6%
- The negative predictive value: P(no disease | negative) ≈ 99.97%
- Group A's strongest argument: the test almost perfectly rules out the disease (high NPV) — it's excellent for reassurance
- Group B's strongest argument: 94.4% of positive results are false positives — rollout will produce mass anxiety, unnecessary follow-up procedures, and stigma, for a condition only 0.5% of people have

The correct outcome is not "B wins" — it's that both arguments are mathematically grounded, and the policy decision depends on values (what is the cost of a false positive vs. a missed case?) as much as numbers.

**Why controversy format:** structured controversy (Johnson & Johnson, 1988) consistently produces deeper understanding than lecture or individual problem-solving on material where reasonable people disagree. Probability and Bayes' rule are precisely this kind of material — the mathematics is unambiguous, but how to act on the result is genuinely contested.

---

### Part 4 — Pre-Submission Debrief (20 minutes)

Students share the probability claims they submitted before class. For each:
- What is the claim?
- What base rate was stated or hidden?
- Is the claim valid as stated?

The instructor should be looking for the most egregious example — the claim with the largest gap between what is stated and what the numbers actually say. That example becomes the class's "star case": the one most worth keeping in mind for subsequent weeks.

**Target domains for collection:** public health (cancer screening, disease testing), finance (investment returns), business (customer conversion rates, A/B test results), sport. Students from 40+ nationalities will bring examples from contexts others in the room haven't encountered — the cross-national richness of the cohort is particularly valuable here.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop:**

*"We spent this session applying probability rules to situations where the correct answer is counterintuitive. What does that tell us about how people reason about probability in practice?"*

The answer: human probability intuition systematically fails at low base rates, relative vs. absolute comparisons, and conditional reasoning. The tools we learned today (frequency trees, Bayes' rule, expected value) correct for those failures — but they only help if someone bothers to use them.

**Bridge forward:**

> *"Next week we add a new tool: specific probability distributions. Today we worked with raw probabilities. What if we knew the data follows a particular pattern — say, that a call centre receives an average of 17 calls per hour? Is there a formula that tells us the probability of receiving exactly 20 calls in the next hour? What would we need to assume?"*

This plants the Poisson distribution question for Week 5.

---

## After Class (Student Post-Work, ~30 minutes)

Students write an LMS post in professional/social media format on one of:
- A real instance of base rate neglect they've encountered or read about
- The structured controversy: which argument was more compelling, and why (it's fine to say "B convinced me" as long as they state which calculation swayed them)
- A follow-up question they'd ask a government health communicator about a screening programme claim

Peer response required: one comment that engages with the probability calculation, not just the narrative.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Worked example uses factory defect scenario, distinct from tutorial medical scenario | Kalyuga et al. (2003): expertise reversal — different examples for pre-work and in-class prevents pattern-matching that bypasses reasoning; each domain applies the same concept differently |
| Frequency tree approach emphasised alongside formula | 3Blue1Brown (2019) visual approach; Gigerenzen & Hoffrage (1995) showed that natural frequencies reduce Bayes' rule errors more than probability notation for non-experts; both representations required |
| T3 held back for Part 3 structured controversy | T3(d) is a debate prompt disguised as a calculation question; surfacing it in context of structured argument produces richer engagement than a short individual answer |
| Structured controversy format for probability/Bayes content | Johnson & Johnson (1988): structured controversy produces deeper understanding than lecture; probability and Bayes' rule are the statistics topics most likely to produce genuine disagreement even among people who've done the calculation correctly |
| Q9 (relative vs. absolute risk reduction) as hardest quiz question | This distinction is one of the most consequential probability misrepresentations in public health and corporate communications; spotting it at Week 4 sets a standard the course maintains through Week 15 |
| Pre-submission: find a real probability claim | Ausubel (1968): self-relevance anchors learning; students who bring their own example have a personal stake in the question; 40+ nationalities produces a gallery of claims no instructor could curate alone |
| Expected value taught with two projects of equal EV but different variance | Bridge to Week 10 (decision trees with risk aversion) and Week 18 (Monte Carlo with distribution sensitivity); the variance insight is the conceptual prerequisite for understanding why EMV alone is insufficient |
| Weekly Mentimeter quiz | Farmus, Cribbie & Rotondi (2020): weekly in-class quizzes significantly moderated flipped classroom advantage (g=0.43) |
| Three-touchpoint structure | Cepeda et al. (2006): spacing effect |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Q7 and Q8 most likely to need clarification; Q9 sets up the debate |
| Tutorial review | 15 min | T1(d) independence; T2(c) risk aversion; T3(a)+(b) only |
| Buffer (explicit) | 10 min | Use on T2(c) debate or Q9 relative/absolute risk clarification |
| Structured controversy | 25 min | 10 min prep + 3+3 min presentations + 5 min debate + 2 min instructor synthesis |
| Pre-submission debrief | 20 min | ~90 sec per student; identify the star case for the class |
| Instructor debrief | 10 min | Close the loop; bridge forward to distributions (Week 5) |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Bayes' rule is algebraically simple and conceptually hard — students may compute correctly and still not understand.

The calculation is straightforward: multiply, divide, get a number. But many students who get 26.9% in the frequency tree still can't explain *why* it's so much lower than 90%. They followed the algorithm without grasping what drives the result (the base rate).

**Resolution:** the worked example explicitly names the mechanism — "the base rate dominates." The structured controversy (Part 3) is designed to force students to reason about *why* the PPV is so low, not just compute it. A student who can only compute, not explain, will not win a group argument.

---

### 2. The gambler's fallacy question (Q7) has a defensible non-obvious answer.

A fair coin lands heads 10 times: the probability on the 11th flip is still 50% — this is the textbook answer. But a Bayesian would note: 10 consecutive heads is evidence (weak, but real) that the coin might be biased. The strict frequentist answer is (c); the Bayesian nuance is (b).

**Resolution:** name the nuance directly. "If you assumed the coin is fair, (c) is correct. If you updated on the evidence of 10 heads, (b) becomes partially defensible — and next week we'll have the tools to quantify exactly how much that sequence should update your belief." This is the most honest answer and the best bridge to Week 5 (binomial distribution).

---

### 3. The structured controversy may collapse if one group is clearly more quantitatively prepared.

If Group B (the sceptics) includes all the students who computed the PPV correctly in T3, while Group A (the defenders) didn't, the debate becomes asymmetric and the learning is only on one side.

**Resolution:** assign groups deliberately, not randomly. Put at least two students who clearly engaged with T3 in each group. The instructor has the pre-submission data and can see who engaged with the calculation. This is a 30-second allocation decision before class.

---

### 4. The "relative vs. absolute risk reduction" distinction (Q9) may feel like a trick question.

Students who correctly identify that 50% is relative and 0.1 percentage points is absolute may still feel the question was unfairly adversarial — the drug company's claim is technically true.

**Resolution:** the instructor should confirm: "Both numbers are correct. The question is which one you should lead with when communicating to the public — and why." This is not a trick; it's the distinction that drives much of public health miscommunication. Students who leave today able to ask "is that relative or absolute?" have a skill they'll use outside this course.

---

### 5. T2 (expected value with risk aversion) is an economics question wearing a statistics costume.

Risk aversion is a utility theory concept — the correct treatment requires a utility function, not just expected value. Students with economics backgrounds may push toward utility; students without may be confused by the concept.

**Resolution:** for this session, frame it as "expected value tells you the average outcome; it doesn't tell you whether the spread matters to you." Week 10 (decision trees) introduces the exponential utility function formally. For now, the intuition is sufficient: "Would you bet your entire savings on a 51% coin flip for double or nothing? Most people wouldn't, even though the EV is positive."

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Farmus, L., Cribbie, R.A. & Rotondi, M. (2020). The flipped classroom in introductory statistics. *Journal of Statistics Education*, 28(3). DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Gigerenzen, G. & Hoffrage, U. (1995). How to improve Bayesian reasoning without instruction. *Psychological Review*, 102(4), 684–704.
- Johnson, D.W. & Johnson, R.T. (1988). Critical thinking through structured controversy. *Educational Leadership*, 45(8), 58–64.
- Kalyuga, S., Ayres, P., Chandler, P. & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1). DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
