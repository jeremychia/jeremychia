# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 5: Common Probability Distributions in Business Applications
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Identify which probability distribution (Normal, Binomial, Poisson, Exponential) is appropriate for a given business situation and justify that choice
- Apply NORM.DIST, BINOM.DIST, and POISSON.DIST in Excel to solve probability questions
- Critique a published business decision that assumed the wrong distribution
- Recognise the normal approximation to the binomial and the conditions under which it is valid

These map directly to ST2187 syllabus topic 6 (probability distributions) and to the course's repeated emphasis on *"identifying which analytical technique is appropriate."* This is the last theory week before Block 2 (practical tools); students leave Week 5 with the conceptual vocabulary they need for everything that follows.

These objectives operate at the **application and evaluation** levels of Bloom's Taxonomy — not just naming distributions, but choosing and applying them, and spotting when others have chosen wrongly.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 5 — read the following sections only:
- §5-2 The normal distribution — density function, z-values, standardisation (pp. 168–178)
- §5-3 Applications of the normal distribution (pp. 178–190)
- §5-4 The binomial distribution (pp. 190–207)
- §5-6 The Poisson and exponential distributions (pp. 207–212)

The normal approximation to the binomial is covered in §5-4c — read it carefully. The rule of thumb (valid when np > 5 and n(1−p) > 5) appears in the chapter and will appear in the quiz.

*Rationale:* Chapter 5 introduces four distributions in one chapter. The reading is dense. Students who skim will struggle in Part 3 (error autopsy). The worked example below requires recognising which distribution applies — which requires having read all four.

**Videos (~20 minutes total):**
- [The Normal Distribution — StatQuest](https://www.youtube.com/watch?v=rzFX5NWojp0) (8 min)
- [The Binomial Distribution — Khan Academy](https://www.youtube.com/watch?v=qIzC1-9PwQo) (7 min)
- [Poisson Distribution — StatQuest](https://www.youtube.com/watch?v=jmqZG6roVqU) (5 min)

**Worked example (attempt T1–T3 first, then read this):**

> **Scenario:** An airline operates a flight with 200 seats. From historical data, each booked passenger has a 10% probability of not showing up (no-show), independently. The airline wants to know: if it books 210 passengers (10 more than seats), what is the probability that more than 200 show up — causing the flight to be oversold?
>
> **Step 1 — Identify the distribution:**
> X = number of passengers who show up. Each passenger either shows up (probability 0.90) or doesn't (probability 0.10), independently. n = 210, p = 0.90. This is binomial: X ~ Bin(210, 0.90).
>
> **Step 2 — Compute in Excel:**
> P(X > 200) = 1 − P(X ≤ 200) = 1 − BINOM.DIST(200, 210, 0.90, TRUE)
> = 1 − 0.9197 ≈ **8.0%**
>
> So with 10 extra bookings, about 8% of flights will be oversold.
>
> **Step 3 — What does this mean for the airline?**
> 8% oversold flights — roughly 1 in 12 flights — means frequent customer compensation, regulatory risk, and reputational damage. Airlines who overbook use this calculation to find the optimal number of extra bookings where the expected revenue gain exceeds the expected cost of compensation.
>
> **Step 4 — Normal approximation check:**
> n = 210, p = 0.90. np = 189 > 5; n(1−p) = 21 > 5. The normal approximation is valid.
> μ = np = 189, σ = √(npq) = √(210 × 0.90 × 0.10) ≈ 4.35.
> P(X > 200) using normal ≈ P(Z > (200.5 − 189) / 4.35) = P(Z > 2.64) ≈ 0.004 — notably different from 8%.
> The difference arises from the continuity correction: use 200.5, not 200.
>
> **The lesson:** the binomial exact calculation and the normal approximation give different answers depending on how the continuity correction is applied. For an overbooking decision, the correct answer matters — using the wrong approximation by 4 percentage points could change the optimal overbooking policy.

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T1 — Normal distribution:*
> Daily demand for a product is normally distributed with mean 500 units and standard deviation 80 units.
>
> (a) What percentage of days have demand below 400 units? [NORM.DIST(400, 500, 80, TRUE)]
> (b) What is the probability demand exceeds 650 units?
> (c) The warehouse holds 620 units. On what percentage of days will there be a stockout?
> (d) How many units must the warehouse hold to ensure stockouts occur on fewer than 5% of days? [NORM.INV(0.95, 500, 80)]

*T2 — Binomial distribution:*
> A mutual fund manager claims to "beat the market" consistently. In reality, assume each week there is a 50% chance (coin flip) that the fund beats the market.
>
> (a) Over 52 weeks, what is the expected number of weeks the fund beats the market?
> (b) What is the probability the fund beats the market in exactly 30 of 52 weeks? [BINOM.DIST(30, 52, 0.5, FALSE)]
> (c) What is the probability of beating the market in 37 or more of 52 weeks? [1 − BINOM.DIST(36, 52, 0.5, TRUE)]
> (d) If there are 400 such fund managers (each with p = 0.5), what is the probability that *at least one* of them beats the market in 37+ of 52 weeks?

Part (d) is the key insight: even with random performance, at least one fund manager will appear brilliant purely by chance. The answer: P(at least one) = 1 − (1 − p_single)^400. This is the "multiple testing" problem in disguise — a recurring theme in regression (Week 15) and hypothesis testing (Week 13).

*T3 — Poisson distribution:*
> A TV repair shop receives an average of 17 calls per day. Assume calls arrive according to a Poisson process.
>
> (a) What is the probability of receiving exactly 20 calls on a given day? [POISSON.DIST(20, 17, FALSE)]
> (b) What is the probability of receiving 20 or fewer calls? [POISSON.DIST(20, 17, TRUE)]
> (c) The shop has capacity for 25 calls per day. What is the probability that demand exceeds capacity?
> (d) What assumption about the arrival process makes the Poisson distribution appropriate here? Name one condition under which this assumption would break.

T3(d) is the critical question: the Poisson distribution assumes calls arrive independently at a constant average rate. In a real shop, calls may cluster (e.g., after a product recall announcement) — violating the constant-rate assumption.

**Pre-class submission (on the course portal):**

Find one business example — from news, your own experience, or a case study — where a company's decision was affected by uncertainty in the number of events (arrivals, failures, occurrences). Submit:
1. What is the business situation?
2. Which distribution seems appropriate, and why?
3. What would break the distribution assumption?

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

**Easy — vocabulary and recall:**

- Q1: The normal distribution is defined by its:
  *(a) Mean and median  (b) Mean and standard deviation  (c) Min and max  (d) Skewness and kurtosis)*

- Q2: The binomial distribution is appropriate when:
  *(a) Events arrive at a constant average rate  (b) You are counting successes in a fixed number of independent Bernoulli trials  (c) The variable is continuous and symmetric  (d) The wait time between events follows an exponential distribution)*

- Q3: λ (lambda) is the parameter of which distribution?
  *(a) Normal  (b) Binomial  (c) Poisson  (d) Uniform)*

- Q4: In Excel, BINOM.DIST(k, n, p, TRUE) gives:
  *(a) P(X = k)  (b) P(X ≤ k)  (c) P(X ≥ k)  (d) P(X > k))*

- Q5: The normal approximation to the binomial requires:
  *(a) n > 30  (b) np > 5 and n(1−p) > 5  (c) p = 0.5  (d) The distribution is symmetric)*

- Q6: Which distribution would you use to model the number of customer complaints received per hour at a call centre?
  *(a) Normal  (b) Binomial  (c) Poisson  (d) Exponential)*

**Medium — application:**

- Q7: A process produces 2% defective items. A sample of 50 items is taken. Using the binomial distribution, the expected number of defectives is:
  *(a) 0.02  (b) 1  (c) 2  (d) 5)*

- Q8: A factory machine breaks down on average once every 8 hours. The time between breakdowns follows an exponential distribution with mean 8 hours. What is the probability the next breakdown occurs within 4 hours?
  *(a) 50%  (b) About 39%  (c) About 61%  (d) 25%)*

Q8 requires knowing that for Exp(λ), P(X ≤ t) = 1 − e^(−λt) = 1 − e^(−4/8) = 1 − e^(−0.5) ≈ 0.394.

**Hard — conceptual:**

- Q9: A financial analyst models daily stock returns as normally distributed. The distribution has thin tails (kurtosis ≈ 0). In reality, extreme market moves occur far more frequently than the normal distribution predicts. This is known as:
  *(a) Heteroskedasticity  (b) Skewness  (c) Fat tails / leptokurtosis  (d) Multicollinearity)*

Q9 is the bridge from distributions to risk: the normal distribution systematically underestimates the probability of extreme events — which is why financial models failed in 2008 and why distribution assumptions always deserve scrutiny.

**Instructor acts on results (5 minutes)**

Q1–Q6 are retrieval practice. Q4 (cumulative vs. exact) is the most commonly confused: "TRUE gives the cumulative (P ≤ k), FALSE gives the exact (P = k) — this distinction will appear on the exam."

Q8 (exponential) may fail broadly — the formula is not immediately obvious. A 60-second derivation: "mean = 1/λ = 8 hours, so λ = 0.125; P(X ≤ 4) = 1 − e^(−0.5) ≈ 39%."

Q9 is the conceptual anchor for the error autopsy in Part 3.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T1(d) — using NORM.INV to find the stock level — is the most practically important and the one students most often attempt incorrectly (confusing the quantile argument with the probability argument).

T2(d) — the multiple fund managers problem — should be discussed as a class: "What is the probability that at least one of 400 funds beats the market in 37+ weeks if all are just guessing?" Answer: 1 − (1 − 0.00159)^400 ≈ 47%. Nearly a coin flip. The implication: among 400 fund managers, we'd expect about 0–2 of them to look brilliant purely by chance. This connects directly to Week 13 (multiple testing in hypothesis testing).

T3(d) is held for Part 3.

The buffer: use it to work through Q8 (exponential) if the quiz showed it hadn't landed, or to let the T2(d) implications sink in.

---

### Part 3 — Error Autopsy (25 minutes)

The format: the instructor presents 3 brief published business failures caused by wrong distribution assumptions. For each, pairs have 4 minutes to identify: (a) what distribution was assumed, (b) what the actual data behaviour was, and (c) one question they would have asked before accepting the model.

**Case 1 — Airline overbooking with seasonal clustering**

> An airline uses a binomial model (n = 250 bookings, p = 0.10 no-show) to calibrate its overbooking policy. The model works well 40 weeks of the year, but consistently underestimates no-show rates in the December holiday period.

**What went wrong:** the binomial assumes p is constant. In December, business travellers (who no-show at 15%) shift to leisure travellers (who no-show at 3%). The mixture produces a bimodal distribution, not a single binomial. The airline's model used the annual average p — which was wrong for the period when it mattered most.

**Case 2 — Inventory system assuming Poisson demand**

> A retailer models daily demand for a product as Poisson with λ = 50 units per day. During a social media trend, demand spikes to 500 units per day for three days. The inventory system had no stockout buffer for this.

**What went wrong:** Poisson assumes a constant average rate. A viral social media event violates the constant-rate assumption catastrophically. The model was correct on average and catastrophically wrong during the events that mattered most.

**Case 3 — Financial risk model assuming normal returns (VaR failure)**

> A bank uses a Value at Risk (VaR) model that assumes daily stock returns are normally distributed. The model estimates a 1-in-100 event (1% tail) corresponds to a loss of X. In the 2008 financial crisis, 1-in-100 events occurred multiple days in a row.

**What went wrong:** financial returns have fat tails — extreme events are far more common than the normal distribution predicts. The model was systematically wrong about precisely the losses that mattered for solvency. (Taleb, 2007.)

**After the three cases:** class discussion — "What is the common thread?" The answer: every model assumes a distribution, and that assumption is always about the future behaving like the past. When the behaviour changes (seasonality, virality, market crisis), the distribution assumption breaks — often exactly when the stakes are highest.

---

### Part 4 — Pre-Submission Debrief (20 minutes)

Each student shares their submitted example (90 seconds each). The instructor asks for each: "What would break the assumption?" The point is not to identify which distribution is technically correct — it is to develop the habit of questioning the assumption before using the model.

This produces a gallery of 12–15 real cases across retail, finance, logistics, healthcare, and operations. With 40+ nationalities in the room, some examples will be from markets or industries others haven't encountered. The instructor should name this: "We just covered 12 countries' business environments in 20 minutes — that's not something a textbook example can do."

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop:**

*"We've now covered four distributions. What's the right way to choose which one to use?"*

The answer: it's not a mechanical rule — it's a question about the data-generating process. Ask: Is the variable continuous or discrete? Is there a fixed number of trials (binomial) or a count of events over time/space (Poisson)? Is the variable a sum of many small independent effects (normal)? Is it a waiting time between Poisson events (exponential)? The distribution follows from the process, not the data alone.

**Bridge forward — and the hard question:**

> *"Everything we've done in Weeks 1–5 is about describing data and probability. Starting next week, you'll have tools to work with data computationally. But here's a question that will sit over the next 17 weeks: where do the numbers in your model — the p, the λ, the μ, the σ — actually come from? You estimated them from historical data. But historical data reflects the past. What are you assuming when you use a past estimate to make a future decision?"*

This is the stability-of-distribution assumption question. It recurs in Week 16 (time series), Week 17 (optimisation), and Week 18 (Monte Carlo sensitivity analysis). Planting it here gives the recurring question a home.

---

## After Class (Student Post-Work, ~30 minutes)

Students write an LMS post in professional format on one of:
- The error autopsy case that surprised them most, and what they'd check before deploying the model
- A distribution assumption they've seen in their own work or field — and whether it was defensible
- The "where do the numbers come from" question: what would it mean to test a distribution assumption with data?

Peer response required: one comment that challenges or extends the example.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Worked example uses airline overbooking — distinct from tutorial inventory and fund problems | Kalyuga et al. (2003): different examples across domains deepen schema formation; the same algorithm applied to flight seats, stock markets, and factory output generalises better than three examples from one domain |
| Error autopsy format for Part 3 | Bjork (1994): studying failure is more memorable than studying correct examples; the VaR and overbooking cases are real and consequential, not textbook-clean |
| T2(d) — multiple fund managers — is the key question | The multiple-testing problem embedded in this question is the conceptual link to Week 13 (hypothesis testing) and Week 15 (stepwise regression); surfacing it here as a probability question means it won't be new when it appears formally |
| Q9 (fat tails / leptokurtosis) as hardest quiz question | Connects distributions to real risk; Taleb (2007) is the cultural reference students will encounter in finance; naming it in Week 5 gives them the vocabulary for the 2008 crisis discussion |
| Four distributions in one week | The ST2187 syllabus groups all four distributions in a single topic; the pre-work reading and videos carry the content; in-class time is used for application and critique, not re-teaching the reading |
| Bridge-forward question about parameter stability | Seeds the meta-question about model validity that runs through Weeks 11–18; students who carry this question into later weeks arrive at the answer through experience rather than being told |
| Weekly Mentimeter quiz | Farmus, Cribbie & Rotondi (2020): weekly quizzes moderated flipped classroom advantage (g=0.43) |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Q4 (TRUE vs FALSE), Q8 (exponential), Q9 (fat tails) most worth addressing |
| Tutorial review | 15 min | T1(d) NORM.INV; T2(d) multiple managers; T3(d) held for Part 3 |
| Buffer (explicit) | 10 min | Absorbs extended T2(d) discussion or Q8 re-working |
| Error autopsy | 25 min | 3 cases × 4 min pair work + 4 min class discussion + 5 min synthesis |
| Pre-submission debrief | 20 min | ~90 sec per student; instructor probes "what would break the assumption?" |
| Instructor debrief | 10 min | Close loop; bridge forward with parameter stability question |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Four distributions in one session is a content risk.

Students may learn the names and formulas without acquiring the judgment to choose between them. The quiz (Q6, which maps call centre complaints to Poisson) and T3(d) (which asks for the Poisson assumption) are specifically designed to test selection, not just application.

**Resolution:** the error autopsy in Part 3 is the key mechanism. Students who can identify *why* the wrong distribution was chosen in Case 1–3 have genuinely understood the selection logic, not just memorised the formula.

---

### 2. The airline overbooking example recurs in both the pre-work worked example and Case 1 of the error autopsy.

Using the same domain twice risks students treating Part 3 as a retrieval task ("we just read about this") rather than a genuinely new application.

**Resolution:** the pre-work example uses the overbooking direction (what probability of oversell?). The error autopsy uses the failure mode (why did the model fail in December?). The question is different even though the domain is the same. If students conflate them, the instructor should name it: "You've seen this scenario — but I'm asking a different question now. The pre-work told you how to use the model. The autopsy asks why the model failed."

---

### 3. The exponential distribution is the hardest for students who've never seen it.

The formula P(X ≤ t) = 1 − e^(−λt) has no intuitive entry point for students who haven't encountered the natural exponential function before. Q8 will likely fail broadly.

**Resolution:** the tutorial does not include an exponential problem (T1–T3 cover normal, binomial, and Poisson). The exponential is introduced through Q8 in the quiz and then addressed briefly in the tutorial buffer. This is an intentional sequencing choice: the exponential is the least commonly tested distribution in the ST2187 context, and 60 seconds of clarification in class is sufficient.

---

### 4. The VaR failure case (2008 financial crisis) may generate a political or emotional response from students with finance backgrounds.

Some students may have worked in finance, have family in finance, or have strong views about the 2008 crisis. The error autopsy is designed to be analytical ("what assumption failed?"), not political ("who is responsible?").

**Resolution:** frame Case 3 explicitly as a modelling question, not a policy question. "We're not discussing whether banks should have been bailed out. We're asking: what did the model assume, and what was the reality? That's a statistics question, and it has a clear answer."

---

### 5. Week 5 is the last theory week before Block 2 (practical tools).

Students need to arrive at Week 6 (Python) with the distributional vocabulary to name what they're computing — not just run `df.describe()` without knowing what the standard deviation means in terms of spread of a distribution.

**Resolution:** the bridge-forward question at the end ("where do the numbers come from?") links distributions to estimation, which is what Block 2's practical tools are computing. The parameter stability question is not just a philosophical musing — it's the question that makes NORM.INV and BINOM.DIST useful rather than decorative.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Farmus, L., Cribbie, R.A. & Rotondi, M. (2020). The flipped classroom in introductory statistics. *Journal of Statistics Education*, 28(3). DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Kalyuga, S., Ayres, P., Chandler, P. & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1). DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Taleb, N.N. (2007). *The Black Swan: The Impact of the Highly Improbable.* Random House.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
