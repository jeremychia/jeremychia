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
- §5-2 The normal distribution — density function, z-values, standardisation (pp. 168–178); note §5-2f (Empirical Rules Revisited — the formal version of the rule used informally in Week 2) and §5-2g (weighted sums of normal random variables — the theory behind T6)
- §5-3 Applications of the normal distribution (pp. 178–190)
- §5-4–5-5 The binomial distribution and its applications (pp. 190–207)
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
> *Solution:* P(X > 850) = 1 − POISSON.DIST(850, 800, TRUE) ≈ **3.7%** — a rare event under normal conditions.
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

---

## Answer Key

### T0 — Distribution identification (entry question)

**(a)** **Poisson.** Customers arrive randomly and independently at a constant average rate — the defining conditions for the Poisson distribution, which models the count of events per time interval.

**(b)** **Binomial.** Fixed number of trials (n = 20 products), each trial is independent with a constant probability of "success" (defect) p = 0.05, and each outcome is binary (pass/fail).

**(c)** **Exponential.** The exponential distribution models the *time between* events when events occur as a Poisson process (random and independent). The question is about time, not count.

**(d)** **Normal.** By the Central Limit Theorem, the sum of a large number of small independent random variables (individual transactions) converges to a normal distribution, regardless of the distribution of any single transaction.

---

### T1 — Normal distribution

**(a)** P(X < 400) = NORM.DIST(400, 500, 80, TRUE) = P(Z < (400−500)/80) = P(Z < −1.25) ≈ **10.6%** of days have demand below 400 units.

**(b)** P(X > 650) = 1 − NORM.DIST(650, 500, 80, TRUE) = P(Z > (650−500)/80) = P(Z > 1.875) ≈ **3.0%.** (The 68-95-99.7 rule gives ~2.5% above 1.96 SD; 1.875 SD is slightly closer to the mean, so ~3%.)

**(c)** P(X > 620) = 1 − NORM.DIST(620, 500, 80, TRUE) = P(Z > 1.5) ≈ **6.7%** of days result in a stockout.

**(d)** NORM.INV(0.95, 500, 80) ≈ **632 units.** This is the 95th percentile: on 95% of days, demand falls at or below 632 units. Common error: students confuse P(X ≤ k) = 0.95 with using NORM.DIST; NORM.INV takes the probability and returns the quantity threshold.

---

### T2 — Binomial distribution (fund managers)

**(a)** E(X) = np = 52 × 0.50 = **26 weeks.** A fund manager who is purely guessing is expected to beat the market in exactly half the weeks.

**(b)** P(X = 30) = BINOM.DIST(30, 52, 0.5, FALSE) ≈ **6.0%.** Beating the market in 30 of 52 weeks has a reasonable probability even by chance.

**(c)** P(X ≥ 37) = 1 − BINOM.DIST(36, 52, 0.5, TRUE) ≈ **0.159%** — fewer than 2 in 1,000 purely random managers would beat the market in 37+ of 52 weeks.

**(d)** P(at least one of 400 beats market in 37+ weeks) = 1 − (1 − 0.00159)^400 ≈ 1 − 0.527 ≈ **47.3%.** Among 400 fund managers all performing at random, there is nearly a coin-flip chance that at least one will appear brilliant purely by luck. This is the multiple-testing problem: when you observe many managers, the probability that *someone* looks exceptional by chance is high — even when no one has skill.

---

### T3 — Poisson distribution (bird flu / egg demand)

**(a)** P(X > 850 | λ = 800) = 1 − P(X ≤ 850) = 1 − POISSON.DIST(850, 800, TRUE) ≈ **3.7%.** Under normal conditions, demand exceeding 850 was a rare event (roughly 1 in 27 weeks). (The normal approximation with continuity correction, Z = (850.5 − 800)/√800 ≈ 1.79, gives the same value.)

**(b)** P(X ≤ 1,150 | λ = 800) is effectively **1.000** — demand of 1,150 is so far above the Poisson rate of 800 (about 10+ standard deviations, since SD = √800 ≈ 28) that the model assigns near-zero probability to any demand that high. The model treated what actually happened as essentially impossible.

**(c)** Three distinct violations of the constant-rate assumption: (i) **Supply shock:** the outbreak directly reduced supply, which may have changed purchasing patterns and accelerated panic demand. (ii) **Consumer behaviour shift:** consumers engaged in panic-buying and hoarding, so demand in any given week was no longer independent of previous weeks — those who hoarded in week 1 shifted their demand forward, violating independence of events. (iii) **Price signal:** the dramatic price increase (from $2.50 to $4.50) would normally suppress demand, but in this case, fear of shortage overrode price sensitivity — the demand rate changed qualitatively, not just in magnitude.

**(d)** Both parties are partially correct, and reconciling their positions is the key analytical insight. The analytics manager is right that the model was wrong **for this situation**: if a model assigns probability ≈ 0 to an event that actually happened, it failed to capture the true data-generating process. The supply chain team is right that the model was appropriate during normal operations — it was calibrated on a period when the assumption of constant λ held. The practical implication: Poisson models (and all statistical models) should specify the conditions under which they are valid. They should not be used mechanically outside those conditions. A well-designed planning system would include a protocol for when to switch from the baseline model to a "crisis mode" scenario — which requires monitoring leading indicators (outbreak reports, supply alerts) rather than waiting for demand data to break the model.

**(e)** **Option (ii) — a separate scenario model for crisis weeks — is more statistically sound.** Raising λ as a single correction in Option (i) blurs the two regimes: in normal weeks, the inflated λ would cause over-ordering and excess inventory. In crisis weeks, a single higher λ may still be too low, and more importantly, the distributional shape of crisis-week demand (highly variable, path-dependent) is fundamentally different from Poisson. A mixture model or regime-switching approach (normal Poisson in ordinary weeks; a separate crisis distribution activated by trigger conditions) is more honest about the underlying process and more useful for decision-making.

---

### T4 — Boundary cases

**(a)** P(X > 220) = P(Z > (220−200)/5) = P(Z > 4.0) ≈ **0.003%.** P(X > 250) = P(Z > (250−200)/5) = P(Z > 10.0) ≈ effectively **0.** The normal distribution assigns non-zero probability to any value, no matter how extreme — technically, a component weighing 250g has a non-zero probability under this model, but it is so small it is indistinguishable from zero in any calculation. In practice, a component weighing 250g (ten standard deviations above the mean) would almost certainly indicate equipment failure, wrong batch, or measurement error — causes the normal distribution cannot represent. The model should never be used to claim such an observation is "impossible"; it should trigger an investigation.

**(b)** n = 10,000, p = 0.0005, so E(X) = np = **5** fraudulent transactions per day. P(X = 0) = (0.9995)^10,000 ≈ e^−5 ≈ **0.674%.** P(X ≥ 10) = 1 − BINOM.DIST(9, 10000, 0.0005, TRUE) ≈ **3.2%.** Poisson with λ = 5 gives essentially identical answers (P(X = 0 | λ = 5) = e^−5 ≈ 0.0067; P(X ≥ 10 | λ = 5) ≈ 3.2%), confirming the Poisson approximation is excellent when n is large and p is very small (λ = np stays moderate).

**(c)** Check rule of thumb: np = 20 × 0.05 = **1 < 5.** The approximation rule fails — the distribution is too skewed for the normal to approximate it well. Exact: P(X = 0) = BINOM.DIST(0, 20, 0.05, FALSE) = (0.95)^20 ≈ **0.358.** Normal approximation: μ = 1, σ = √(20 × 0.05 × 0.95) ≈ 0.975. P(X ≤ 0.5) = NORM.DIST(0.5, 1, 0.975, TRUE) ≈ **0.306.** The normal approximation underestimates P(X = 0) by about 15% because the binomial distribution here is strongly right-skewed — most of the probability mass is at X = 0 and X = 1. The symmetric normal cannot capture a distribution piled up near zero.

---

### T5 — Poisson assumption violations

**(a)** A party of 20 arriving simultaneously violates the **independence** assumption: arrivals are not independent events — one "event" generates 20 arrivals. The Poisson model would **underestimate** the probability of very high counts during Friday evenings (the spike is systematic and correlated, not random), but would also underestimate variance in general.

**(b)** A software update drives a correlated surge: all callers who experienced the bug are calling for the same reason at roughly the same time. This violates **independence** (arrivals are correlated — each new user discovering the bug causes a call) and **constant rate** (λ shifts dramatically). The Poisson model would vastly **underestimate** spike probabilities during update releases.

**(c)** A machine freeze creates dependency between arrivals and the queue: subsequent customers are blocked (not processed), so the effective arrival rate at the machine drops to zero during a freeze. The Poisson model assumes continuous independent arrivals — the freeze creates a **non-stationary process with memory** (the machine's state affects future arrivals). The Poisson model would **mismatch** the true distribution in either direction depending on whether "arrivals" means customers wanting service or transactions processed.

**(d)** A viral celebrity tweet creates a spike driven by a single external event that affects all potential visitors simultaneously. This violates **independence** (all views from that tweet are correlated) and **constant rate** (λ jumps by two orders of magnitude in minutes). The Poisson model would assign near-zero probability to 80,000 views in 10 minutes, making the model useless for capacity planning around viral events. Extreme spike probabilities would be wildly **underestimated**.

In all cases: when the constant-rate and independence assumptions break, real-world processes exhibit much heavier tails (larger extreme counts) than the Poisson model predicts. The Poisson underestimates the probability of rare large counts in the presence of clustering, correlation, or regime shifts.

---

### T6 — Multi-distribution: logistics delivery

**(a)** E(total) = E(loading) + driving + E(traffic delay) = 45 + 60 + (0.25 × 30 + 0.75 × 0) = 45 + 60 + 7.5 = **112.5 minutes.**

**(b)** For total time to exceed 150 minutes (= 112.5 + 37.5 minutes above expectation):
- **Without traffic delay:** total time = loading + 60. Breach requires loading > 90 minutes → Z = (90 − 45)/10 = 4.5 → P ≈ **0.0003%.** Essentially impossible without traffic.
- **With traffic delay (adds 30 min):** total time = loading + 60 + 30. Breach requires loading > 60 minutes → Z = (60 − 45)/10 = 1.5 → P ≈ **6.7%.** A meaningful risk when traffic occurs.
- Conclusion: the traffic delay is the dominant driver of late deliveries; an unusually long loading time alone will almost never cause a breach.

**(c)** P(total > 150) ≈ P(traffic) × P(loading > 60) + P(no traffic) × P(loading > 90) = 0.25 × 0.067 + 0.75 × 0.000003 ≈ 0.01675 + 0.000002 ≈ **1.68%.** The no-traffic term is negligible; virtually all late deliveries occur when traffic delays coincide with above-average loading times.

**(d)** With 200 routes per day: expected late deliveries = 0.0168 × 200 ≈ **3.4 routes per day.** If same-day delivery is a premium service with a penalty clause (e.g., refund or compensation), this translates directly into daily cost. A logistics planner should weigh the cost of 3–4 daily failures against the cost of the interventions in part (e).

**(e)** The traffic delay is the dominant driver (it accounts for nearly 100% of the 1.68% failure probability). Reducing P(traffic delay) from 0.25 to 0.15 would cut failures by roughly 40%; reducing loading SD from 10 to 5 minutes would barely move the number (it only matters when combined with traffic, and the loading threshold in that case is already only 1.5 SD away). **Priority: reduce traffic delay** — either via route optimisation, time-of-day scheduling, or real-time rerouting.

---

### T7 — Distribution diagnosis

**(a)** **Inappropriate — use Poisson instead.** Emergency admissions are non-negative integers (counts). The Normal distribution is continuous and can assign probability to negative values (e.g., −2 admissions), which is impossible. With mean 12 and SD 3, the normal model assigns about 0.01% probability to negative admissions — a structural error. Poisson with λ = 12 is correct: it is defined over non-negative integers, and at λ = 12 it is approximately symmetric anyway, so the Normal is also numerically close — but it is the wrong model in principle.

**(b)** **Inappropriate — use Binomial instead.** Whether each of 500 applicants defaults is a binary outcome (default/no default), which fits Binomial(n=500, p=0.04). While Poisson(λ=20) is an acceptable approximation (n large, p small, λ = np = 20), it is technically the wrong generative model. The key distinction: Binomial has a hard upper bound (500 defaults maximum); Poisson is unbounded — it could theoretically assign non-zero probability to 1,000 defaults from 500 applicants, which is impossible. For exam purposes: full credit for identifying the Binomial as more appropriate; partial credit for noting Poisson is a reasonable approximation.

**(c)** **Inappropriate — use Exponential instead.** The wait time between aircraft landings is a continuous waiting time between events, not a count of events in discrete slots. The Binomial models the *count* of landings in n time slots — a different question. Exponential with rate parameter λ = (1/mean interarrival time) is the correct distribution for waiting times between Poisson arrivals.

**(d)** **Inappropriate — use Normal instead.** Daily total revenue from tens of thousands of transactions is a sum of many small independent contributions, which by the Central Limit Theorem converges to Normal. The Uniform distribution assigns equal probability to every value between €50,000 and €200,000 — implying a €50,001 day is as likely as a €125,000 day, which contradicts real revenue patterns. The Normal would be centred on the mean daily revenue with a standard deviation derived from historical variability.

**(e)** **Inappropriate — use Poisson instead.** Bug counts are non-negative integers (counts of events) arriving at an average rate (3 per 1,000 lines), which matches the Poisson assumptions. The Normal distribution is continuous and assigns probability to negative bug counts. With λ = 3, the Poisson distribution is right-skewed (P(X = 0) ≈ 5%), which the Normal approximation would underestimate. At very small λ, the Poisson–Normal approximation is poor: np = 3 < 5, so the rule of thumb for the approximation fails.

---

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

> An airline uses a binomial model (n = 250 bookings, p = 0.10 no-show) to calibrate its overbooking policy. The model works well 40 weeks of the year, but consistently overestimates no-show rates in the December holiday period — and the airline oversells seats exactly when flights are fullest.

**What went wrong:** the binomial assumes p is constant. In December, the passenger mix shifts from business travellers (who no-show at 15%) to leisure travellers (who no-show at 3%), so the true December no-show rate falls far below the annual average. The changing mix also makes the counts overdispersed — no single binomial fits the whole year. The airline's model used the annual average p — far too high for December — so it kept selling extra tickets to passengers who all showed up.

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

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapter 5

**Coverage check: strong alignment; section labels need one correction and two high-value subsections are unused.**

- The cited "§5-4 The binomial distribution (pp. 190–207)" actually spans **two** sections: 5-4 The Binomial Distribution (190–195, incl. 5-4c the normal approximation) *and* 5-5 Applications of the Binomial Distribution (195–207). Relabel as "§5-4–5-5" — students told to "read §5-4" who stop at the section boundary will miss the applications material the tutorials draw on.
- **5-2f "Empirical Rules Revisited" (p. 177) closes the loop that Week 2 planted.** Week 2's T1(f) and T3 used the empirical rule with a promissory note that it would be formalised here. Add one line to the reading list flagging 5-2f explicitly, and one sentence in Part 2 ("remember the salary data where the empirical rule failed? Now you know what it assumes").
- **5-2g "Weighted Sums of Normal Random Variables" (p. 177) is exactly the theory behind T6** (total time = loading + fixed + traffic), and it's the foundation for portfolio examples in Week 17. It's two pages; add it to the reading rather than letting T6 rest on intuition.
- The exponential distribution (5-6b) is assigned reading and quizzed (Q8) but never practised — see critique point 4.

## 2. Extended Question Bank (with answers)

**T8 — Exponential distribution and memorylessness (fills the Q8 gap):**

> A server component fails on average once every 200 days; time between failures is exponential.
>
> (a) Compute P(failure within 100 days).
> (b) The component has already survived 300 days. What is the probability it fails in the *next* 100 days? What property is this?
> (c) A maintenance manager says: "It's overdue — it's more likely to fail now." Under the exponential model, is she right? Name a real physical reason the exponential model might be wrong here.
>
> **Answers:** (a) λ = 1/200; P(X ≤ 100) = 1 − e^(−100/200) = 1 − e^(−0.5) ≈ **39.3%.** (b) Identical: **39.3%** — the exponential is **memoryless**; survival so far tells you nothing about the future under this model. (c) Under the model she is wrong; in reality, components *wear out* (hazard rate increases with age), which the exponential cannot represent — a Weibull with increasing hazard would fit better. The point mirrors the week's theme: the model's convenience (memorylessness) is an assumption about the process, not a fact.

**T9 — Two-sided specification limits (bridges to quality control):**

> A bottling machine fills bottles with volume ~ Normal(μ = 500 ml, σ = 4 ml). Regulation requires 492–508 ml.
>
> (a) What proportion of bottles violates the spec?
> (b) The firm can either re-centre the machine (μ stays 500, this is already centred) or upgrade it to σ = 2 ml. What does the violation rate become after the upgrade?
> (c) Why does halving σ reduce violations by far more than half? Connect to the shape of the normal tails.
>
> **Answers:** (a) Spec is ±8 ml = ±2σ; violations = 2 × P(Z > 2) ≈ 2 × 2.28% = **4.55%.** (b) ±8 ml is now ±4σ; violations = 2 × P(Z > 4) ≈ 2 × 0.0032% = **0.006%** — roughly a 700-fold reduction. (c) Normal tail probability decays super-exponentially in z, so pushing the spec limit from 2σ to 4σ collapses the tail mass — this non-linearity is why quality programmes obsess over variance reduction (and the intuition behind "six sigma").

**T10 — CLT in reverse (conceptual):**

> T0(d) used the CLT to justify a normal model for supermarket daily revenue. For each modification, say whether the normal model survives and why: (i) The store adds a lottery counter where one transaction in 10,000 is a €50,000 jackpot payout. (ii) Revenue is recorded per *customer* rather than per day. (iii) The store has only ~30 transactions per day.
>
> **Answers:** (i) No — the CLT needs many *small* independent contributions; one dominant heavy-tailed component (rare €50k payouts) makes the daily total mixture-distributed with a spike — the normal will badly understate tail risk (Q9's fat-tails point, arrived at constructively). (ii) No — individual transaction values are typically right-skewed (many small, few large); the CLT applies to sums/averages of many, not to single draws. (iii) Weakened — 30 skewed transactions may not be enough for the sum to look normal; check the skew before trusting normal-based stockout maths.

*Additional quiz questions:*

- Q10: For a Poisson distribution, the variance equals: *(a) λ² (b) λ (c) √λ (d) nλ)* — **Answer: (b)**; the mean-equals-variance property is also the standard test for whether count data is genuinely Poisson (overdispersion check — used in Activity C below).
- Q11: A component has survived 500 hours. Under an exponential lifetime model, its probability of failing in the next hour, compared with a brand-new component's, is: *(a) higher (b) lower (c) the same (d) undefined)* — **Answer: (c)** (memorylessness).
- Q12: Which quantity does NORM.INV(0.99, μ, σ) return? *(a) the probability of exceeding μ (b) the value below which 99% of the distribution lies (c) the 99% confidence interval (d) P(X ≤ 0.99))* — **Answer: (b)** — rehearses the T1(d) confusion in reverse.

## 3. Alternative In-Class Activities (additional options)

**A. Dice CLT build (10 min, energiser before Part 3).** Every student rolls five dice, sums them, posts the sum to Mentimeter; repeat three times. Plot the histogram of sums live — a bell shape emerges from uniform ingredients in front of them. Sixty seconds of debrief: "That's the only reason T0(d) is 'normal'." Cheap, physical, and makes the CLT an *event* rather than an acronym.

**B. Distribution decision tree, built by the room (15 min, alternative Part 2 use).** Pairs get 90 seconds to draft a flowchart ("Is the variable a count / binary trial / waiting time / sum of many small things?"). Instructor consolidates one class flowchart on the board, then stress-tests it with five rapid scenarios (including one that genuinely doesn't fit — e.g. customer satisfaction scores — to establish that "none of the four" is a legal answer). The artefact can be photographed and pinned in the LMS as the course's selection heuristic.

**C. Overdispersion hunt on real data (20 min, alternative Part 3).** Give pairs a real hourly count series (Berlin bike-counter data or café transactions). Task: compute mean and variance of the counts; a Poisson process requires them equal. Every real dataset will be overdispersed — pairs must propose *why* (clustering, weather regimes, weekday mixture). This is the error-autopsy insight discovered in data rather than narrated in a vignette, and it directly rehearses the λ-stability theme of T3.

**D. Overbooking tournament (20 min, alternative Part 3/4).** Teams choose how many tickets to sell for a 100-seat flight (no-show p = 0.10, ticket revenue and bump-compensation costs given). Instructor simulates 20 flights per team with a pre-built spreadsheet; profit leaderboard on the board. Teams that overbooked aggressively occasionally get destroyed by a low no-show draw — variance made visceral. Directly extends the worked example into a decision, previewing Weeks 10 and 18.

**E. Fat-tail forensic (10 min, Part 3 Case 3 upgrade).** Show 10 years of daily returns for a real index next to a simulated normal series with identical mean and SD. Task: count |z| > 3 days in each. Real data: dozens; normal simulation: ~7 expected. The Taleb point becomes a counting exercise, not an anecdote.

## 4. Critique of the Lesson Plan

**What works (keep):** T0 as a selection-logic gate; T2(d)'s multiple-testing plant for Week 13 (genuinely elegant); the T3 bird-flu case with its regime-change lesson; the "distribution follows from the process, not the data" debrief line; the deliberate deferral of the exponential.

**Problems, reasons, and fixes:**

1. **T2(b) answer is wrong.** P(X = 30 | n = 52, p = 0.5) ≈ **6.0%**, not 7.2% (normal check: mean 26, SD √13 ≈ 3.61; continuity band 29.5–30.5 gives Φ(1.25) − Φ(0.97) ≈ 0.060; Excel `BINOM.DIST(30,52,0.5,FALSE)` confirms ≈ 0.0598). *Fix:* correct the key.
2. **T3(a)'s value should be re-verified.** P(X > 850 | λ = 800): normal approximation with continuity correction gives Z = (850.5 − 800)/√800 ≈ 1.79 → ≈ **3.7%**, not 3.4%. Run `1-POISSON.DIST(850,800,TRUE)` once and print the exact value — for a question students submit, the key must match Excel's output to the decimal they'll see.
3. **Inline solutions inside submitted problems, again.** T3(a)–(b), all of T4, and T6(a)–(c) print full solutions inside the question text. Same defect as Week 4, same fix: strip to the Answer Key, issue a student version. (By Week 5 this is systematic — fixing it across the whole 22-week set should be one editing pass, not per-week patches.)
4. **The exponential is quizzed but never practised — and the plan says that's deliberate while still putting it in the learning objectives.** Objective 1 includes identifying the exponential; Design Challenge 3 says the tutorial "does not include an exponential problem" by intention; Q8 then demands a *computation* (1 − e^(−λt)) that nothing in the pre-work rehearses beyond a 5-minute video. Either add T8 above (10 minutes of pre-work) or downgrade Q8 to a selection question and keep the computation for the buffer. Testing unpractised computation contradicts the plan's own retrieval-practice logic.
5. **Error-autopsy Case 1 is internally reversed.** The vignette says the model "consistently underestimates no-show rates in the December holiday period," but the explanation says December shifts toward leisure travellers who no-show at **3%** — i.e. actual December no-shows are *lower* than the modelled 10%, so the model **over**estimates no-shows and the airline oversells seats. *Fix:* flip the vignette's verb (and note the operational consequence — bumped passengers at Christmas — which makes the story stronger). Also soften "the mixture produces a bimodal distribution": a two-p binomial mixture is overdispersed but rarely visibly bimodal; "overdispersed — fatter-tailed than any single binomial" is the accurate claim.
6. **Part 4 arithmetic again: 90 seconds × 12–15 students = 18–22.5 minutes in a 20-minute slot.** Same fix as Week 4: instructor pre-selects 5–6 submissions spanning domains; remainder get LMS feedback. This is the third week running with this issue — worth fixing structurally in the template.
7. **The four-distribution week carries hidden prerequisite risk from the Week 4 gap.** T9/T4 use variance fluently, but Week 4's variance objective was unpractised (see Week 4 supplement §1.3). If Week 4's T9 (variance via SUMPRODUCT) isn't adopted, students meet σ = √(npq) in the worked example with no prior computation of a distribution variance anywhere in the course. Sequencing fix, zero content cost.
