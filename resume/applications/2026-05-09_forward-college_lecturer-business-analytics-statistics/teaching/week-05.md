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
- [The Normal Distribution — StatQuest](https://www.youtube.com/watch?v=rzFX5NWojp0) (8 min). *Active watching: when StatQuest explains the standard deviation and the 68-95-99.7 rule, pause and write: what percentage of values fall more than 2 standard deviations above the mean? This is directly what T1(b) asks.*
- [The Binomial Distribution — Khan Academy](https://www.youtube.com/watch?v=qIzC1-9PwQo) (7 min). *Active watching: when the video specifies the three conditions that make a distribution binomial (fixed n, independent trials, constant p), pause and check whether the T2 scenario meets all three before resuming.*
- [Poisson Distribution — StatQuest](https://www.youtube.com/watch?v=jmqZG6roVqU) (5 min). *Active watching: when StatQuest states the key Poisson assumption (events arrive at a constant average rate, independently), pause and write one real-world situation where this assumption would break — this is T3(d).*

**Worked example (read this before attempting the tutorial problems):**

> **Scenario:** An airline operates a flight with 200 seats. From historical data, each booked passenger has a 10% probability of not showing up (no-show), independently. The airline wants to know: if it books 210 passengers (10 more than seats), what is the probability that more than 200 show up — causing the flight to be oversold?
>
> **Step 1 — Identify the distribution:**
> X = number of passengers who show up. Each passenger either shows up (probability 0.90) or doesn't (probability 0.10), independently. n = 210, p = 0.90. This is binomial: X ~ Bin(210, 0.90).
>
> **Step 2 — Compute in Excel:**
> P(X > 200) = 1 − P(X ≤ 200) = 1 − BINOM.DIST(200, 210, 0.90, TRUE)
> = 1 − 0.9981 ≈ **0.19%**
>
> So with 10 extra bookings, about 0.2% of flights will be oversold.
>
> **Step 3 — What does this mean for the airline?**
> 0.19% oversold flights — roughly 1 in 500 flights — means the airline is overbooking very conservatively. Airlines who overbook use this calculation to find the optimal number of extra bookings where the expected revenue gain exceeds the expected cost of compensation.
>
> **Step 4 — Normal approximation check:**
> n = 210, p = 0.90. np = 189 > 5; n(1−p) = 21 > 5. The normal approximation is valid.
> μ = np = 189, σ = √(npq) = √(210 × 0.90 × 0.10) ≈ 4.35.
> P(X > 200) using normal ≈ P(Z > (200.5 − 189) / 4.35) = P(Z > 2.64) ≈ 0.41% — about twice the exact value.
> The difference arises from the continuity correction: use 200.5, not 200.
>
> **The lesson:** the binomial exact calculation and the normal approximation give different answers even when the rule of thumb (np > 5 and n(1−p) > 5) is satisfied. For an overbooking decision, the direction of the error matters — the normal approximation overstates the probability of overselling by a factor of roughly two.

*This worked example is marked optional for students who can already identify a distribution from a scenario description and state the Excel function to use. If you answered T0 correctly before reading this, the example will add limited value. If the Step 1 selection logic felt unclear after the reading, read it carefully — Step 1 is the skill the entire session tests.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T0 — Entry question (lower floor):*

> For each of the following situations, write which distribution you would use (Normal, Binomial, Poisson, or Exponential) and one sentence explaining why. No formula required.
>
> (a) The number of customers who arrive at a coffee shop in a 30-minute period, given arrivals are random and independent.
> (b) Whether each of 20 randomly selected products passes a quality check, given each has a 5% defect rate.
> (c) The time between successive machine failures in a factory, given failures occur randomly.
> (d) The daily revenue of a large supermarket, which results from thousands of small independent transactions.

T0 tests selection logic, not computation. A student who cannot match scenarios to distributions before class will struggle with T1–T3 and with the error autopsy in Part 3. The question is deliberately formula-free: the right answer is a named distribution and a plain-language reason, not a probability. For ST2187 students who completed ST104a, this is a retrieval task; for students who have not, it surfaces the conceptual gap before the session.

*Self-check for T0:* (a) Poisson — random independent arrivals, counting events per time interval; (b) Binomial — fixed n = 20 trials, each is pass/fail with constant p = 0.05; (c) Exponential — models time between events (not count of events); (d) Normal — by the CLT, the sum of thousands of small independent transactions is normally distributed. If you were uncertain about (c) vs (d), re-read §5-6 before T3.

*T1 — Normal distribution:*

*The 68-95-99.7 rule from the StatQuest video applies directly to T1(b): more than 650 units is more than (650−500)/80 = 1.875 standard deviations above the mean. The video's visual of the distribution tells you this is in the tail.*
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

> In 2024, the US experienced a severe outbreak of Highly Pathogenic Avian Influenza (HPAI H5N1) — commonly called bird flu — affecting commercial poultry flocks. By late 2024, over 100 million birds had been culled. As a result, US egg prices surged dramatically: the average retail price per dozen eggs rose from approximately $2.50 in January 2024 to over $4.50 by December 2024, with wholesale prices spiking even higher in early 2025.
>
> A grocery chain had been planning its egg inventory using a Poisson distribution. Historically, demand for eggs varied randomly around a mean of 800 dozen per week at a typical store, and the Poisson model had worked well for safety stock planning.
>
> (a) Using the historical λ = 800 as the weekly demand rate, calculate the probability that weekly demand exceeds 850 dozen. Use P(X > 850) = 1 − P(X ≤ 850).
>
> *Solution:* P(X > 850) ≈ **3.4%** — a rare event under normal conditions.
>
> (b) The chain's supply of eggs fell sharply due to the outbreak. At the same time, consumers began panic-buying and hoarding. In week 3 of the supply crisis, actual demand was 1,150 dozen. Calculate P(X ≤ 1150) using λ = 800. What does this tell you about the model's predictions in crisis conditions?
>
> *Solution:* P(X ≤ 1150 | λ = 800) is essentially 1 — demand of 1,150 is so far above the assumed rate that the model treats it as virtually impossible. The model assigned near-zero probability to what actually happened.
>
> (c) The Poisson distribution assumes events arrive at a constant average rate λ. Identify three distinct ways the avian flu outbreak violated this assumption simultaneously.
>
> (d) The supply chain team argued: "The model wasn't wrong — the world changed." The analytics manager responded: "If the model assigns probability ≈ 0 to an event that actually happened, the model was wrong for this situation." Who is right? What does this imply for how Poisson models should be used in planning?
>
> (e) After the crisis, the team considers two fixes: (i) use a higher λ to account for potential future shocks; (ii) add a separate scenario model that captures "crisis weeks" as a different distribution. Which approach is more statistically sound, and why?

T3 uses a verified 2024–2025 event (HPAI H5N1 egg price data is documented by the USDA Agricultural Marketing Service and widely reported). It illustrates the key Poisson assumption — constant rate λ — by showing what happens when all three conditions (constant rate, independent events, stable supply) break simultaneously. Part (d) is the high-leverage conceptual question: the model was not misapplied in the past, but it was inappropriate for the crisis period — understanding that distinction is essential for any analyst using statistical models in real operations.

*T4 — Boundary cases: what happens at the edges of distribution parameters:*

> (a) **Normal distribution, extreme z-scores:** A factory's component weights are normally distributed with mean 200g and SD 5g. Compute the probability that a randomly selected component weighs more than 220g. Now compute the probability it weighs more than 250g. What does the second answer tell you about the normal distribution's behaviour in the tails?
>
> *Solution:* P(X > 220) = P(Z > (220−200)/5) = P(Z > 4.0) ≈ 0.003%. P(X > 250) = P(Z > 10.0) ≈ effectively 0. In practice, these extreme weights would almost certainly have a different explanation (equipment failure, wrong batch), which the normal model cannot account for. The normal distribution assigns non-zero probability to every value, no matter how extreme — but for real physical processes, true extremes may be structurally impossible.
>
> (b) **Binomial with p near 0:** A payment system processes 10,000 transactions per day. The probability any individual transaction is fraudulent is 0.0005 (0.05%). Using the binomial distribution, calculate: (i) the expected number of fraudulent transactions per day; (ii) the probability of exactly 0 fraudulent transactions; (iii) the probability of 10 or more fraudulent transactions. Check whether the Poisson approximation gives similar answers (λ = np).
>
> *Solution:* n = 10,000, p = 0.0005. E(X) = np = 5.
> P(X = 0) = (0.9995)^10,000 ≈ e^{−5} ≈ 0.00674 (Poisson gives the same: P(X=0|λ=5) = e^{−5} ≈ 0.0067).
> P(X ≥ 10) = 1 − BINOM.DIST(9, 10000, 0.0005, TRUE) ≈ 1 − POISSON.DIST(9, 5, TRUE) ≈ 1 − 0.9682 ≈ **3.2%**. The Poisson approximation is excellent here because n is large and p is very small.
>
> (c) **When does the normal approximation to the binomial fail?** For n = 20 and p = 0.05: (i) Check the rule of thumb (np > 5 and n(1−p) > 5). Does it hold? (ii) Calculate P(X = 0) exactly using the binomial. (iii) Approximate using the normal. Compare the two answers and explain the discrepancy.
>
> *Solution:* np = 1 < 5. The approximation rule fails. P(X = 0) exactly = BINOM.DIST(0, 20, 0.05, FALSE) = (0.95)^20 ≈ 0.358. Normal approximation: μ = 1, σ = √(20 × 0.05 × 0.95) ≈ 0.975. P(X ≤ 0.5) = NORM.DIST(0.5, 1, 0.975, TRUE) ≈ 0.306. The normal approximation underestimates P(X = 0) because the distribution is highly right-skewed — the normal is symmetric and cannot capture this.

*T5 — Conceptual variant: what changes if the assumption is violated:*

> The Poisson distribution assumes events occur independently at a constant average rate λ. For each of the following business scenarios, the Poisson assumption is partially or fully violated. Describe (i) how it is violated, and (ii) whether the Poisson model would overestimate or underestimate the probability of rare extreme events (e.g., an unusually high count in a given period).
>
> (a) Customers arrive at a restaurant at an average rate of 12 per hour. However, a large party of 20 arrives every Friday evening at 7pm.
> (b) A call centre receives support calls at an average rate of 50 per hour. When the company releases a software update, calls spike to 300 per hour for the first few hours.
> (c) A bank's ATM machine processes transactions at a mean rate of 8 per hour. Each transaction takes a variable amount of time; if a machine freezes, all subsequent arrivals are blocked until the freeze clears.
> (d) Website page views average 500 per hour. A celebrity tweets a link to the website, causing views to spike to 80,000 in 10 minutes.
>
> In each case, would you expect the Poisson model to underpredict the probability of very high counts during the spike period? Explain your reasoning.

*T6 — Multi-step: combine two distributions, interpret in business context:*

> A logistics company operates a delivery fleet. Two sources of delay are relevant:
> - **Loading delay:** the time to load a truck is normally distributed, mean 45 minutes, SD 10 minutes.
> - **Traffic delay:** the probability of encountering a significant traffic delay on any given route is 0.25 (binomial; each route is independent). If a traffic delay occurs, it adds exactly 30 minutes; otherwise, it adds 0 minutes.
>
> A truck must complete its route within 150 minutes of departure to guarantee same-day delivery. The loading starts at noon; the driving time (excluding loading and traffic delays) is fixed at 60 minutes.
>
> Total time = loading delay + driving time + traffic delay.
>
> (a) What is the expected total time? Show the calculation.
>
> *Solution:* E(total) = E(loading) + 60 + E(traffic) = 45 + 60 + (0.25 × 30) = 45 + 60 + 7.5 = **112.5 minutes**
>
> (b) For the total time to exceed 150 minutes, what combinations of events would cause this? Is it: (i) a traffic delay plus a normally long loading time, (ii) an extreme loading delay without traffic, or (iii) both? Identify the threshold loading time (in minutes) that causes a breach, both with and without a traffic delay.
>
> *Solution:* Without traffic delay: need loading > 90 minutes → Z = (90−45)/10 = 4.5 → P ≈ 0.0003%. With traffic delay: need loading > 60 minutes → Z = (60−45)/10 = 1.5 → P ≈ 6.7%.
>
> (c) P(total time > 150) ≈ P(traffic delay) × P(loading > 60 min) + P(no traffic delay) × P(loading > 90 min). Calculate this.
>
> *Solution:* ≈ 0.25 × 0.067 + 0.75 × 0.000003 ≈ 0.01675 + 0.0000023 ≈ **1.68%**
>
> (d) Interpret this probability in business terms. If the company runs 200 routes per day, how many same-day delivery failures should it expect?
> (e) Which source of delay should the company prioritise reducing — loading time variability or traffic delay occurrence — if the goal is to reduce late deliveries? Support your answer using the numbers from (c).

*T7 — Distribution selection: diagnosis task:*

> For each of the following, a modeller has chosen a distribution. Identify whether the choice is appropriate, and if not, state what the correct distribution should be and why.
>
> (a) A hospital models the number of emergency admissions per 8-hour shift using a Normal distribution with mean 12 and SD 3. The modeller notes that admissions must be a non-negative integer.
>
> (b) A bank models whether each of 500 mortgage applicants will default (yes/no) using a Poisson distribution with λ = 20 (the expected number of defaults).
>
> (c) An airline models the wait time between aircraft landings at a busy airport using a Binomial distribution (n = 100 time slots, p = 0.1 chance of a landing in any slot).
>
> (d) A supermarket models daily total revenue (from tens of thousands of small transactions) using a Uniform distribution between €50,000 and €200,000.
>
> (e) A software firm models the number of code bugs found in a 1,000-line code review using a Normal distribution. Bug discovery has historically averaged 3 bugs per 1,000 lines, and the firm assumes the events are independent.

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

**T0 first (5 minutes).** Ask the room: "Who put Poisson for (d)?" — the supermarket revenue question. Some will: revenue per transaction is a random variable, so many small transactions might suggest Poisson. But the Central Limit Theorem is the correct reasoning: a sum of many small independent random variables converges to normal, regardless of the individual transaction distribution. This distinction — Poisson models a *count* of events; normal models a *sum* of a large number of contributions — is exactly what the error autopsy in Part 3 requires. The T0 answer reveals who has the conceptual map and who is guessing by elimination. Students who chose correctly but for the wrong reason (e.g., "it's big so it must be normal") need this conversation as much as students who chose incorrectly.

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
