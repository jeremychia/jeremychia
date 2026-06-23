# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 18: Monte Carlo Simulation
**Format:** 90-minute lab seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Build a Monte Carlo simulation in Python (numpy) to model a business risk scenario with uncertain inputs
- Compute output statistics from simulation results: mean, percentiles, probability of exceeding a threshold
- Vary input distributions and observe sensitivity of the output distribution (what-if analysis)
- Identify the GIGO principle (garbage in, garbage out) in the context of simulation — and identify where the input assumptions come from

These map to ST2187 syllabus topic 15 (Monte Carlo simulation) and complete Block 4 theory sessions. This is the capstone of the probability and distributions thread: students who built intuition about distributions in Week 5, about expected value in Week 4, and about model assumptions throughout the course will now use those concepts to build a simulation from scratch.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 15 (Introduction to Simulation Modeling) — read the following sections only:
- §15-1 Introduction to simulation (pp. 760–762)
- §15-2 Probability distributions for input variables (pp. 762–780)
- §15-3 Simulation and the flaw of averages (pp. 780–783)
- §15-4 Simulation with built-in Excel tools (pp. 783–794)

Students who have @RISK installed can additionally read §15-5 Introduction to @RISK (pp. 794–811). In class, we will use Python — the concepts are identical, the tool differs.

**Videos (~15 minutes total):**
- [Monte Carlo Simulation — Investopedia](https://www.youtube.com/watch?v=7ESK5SaP-bc) (8 min) — business applications
- [Monte Carlo in Python — Sentdex](https://www.youtube.com/watch?v=2BZVD-GJAL0) (7 min) — code walkthrough

**Worked example (read carefully — you will adapt this in class):**

> **Problem:** A startup is evaluating a new product launch. Uncertain inputs:
> - Units sold: normally distributed, mean 10,000, SD 2,500
> - Price per unit: uniformly distributed between €18 and €26 (uncertain due to competitor pricing)
> - Variable cost per unit: normally distributed, mean €8, SD €1.5
> - Fixed costs: €60,000 (known)
>
> **Revenue = units × price; Profit = Revenue − (units × variable_cost) − fixed_costs**
>
> **Python simulation:**
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> np.random.seed(42)
> N = 10_000  # number of simulations
>
> units = np.random.normal(10000, 2500, N)
> price = np.random.uniform(18, 26, N)
> var_cost = np.random.normal(8, 1.5, N)
> fixed = 60_000
>
> revenue = units * price
> profit = revenue - (units * var_cost) - fixed
>
> # Output statistics
> print(f"Mean profit:    €{profit.mean():,.0f}")
> print(f"Median profit:  €{np.median(profit):,.0f}")
> print(f"5th percentile: €{np.percentile(profit, 5):,.0f}")
> print(f"95th percentile:€{np.percentile(profit, 95):,.0f}")
> print(f"P(loss):        {(profit < 0).mean():.1%}")
>
> plt.hist(profit, bins=50, edgecolor='black', alpha=0.7)
> plt.axvline(0, color='red', linestyle='--', label='Break-even')
> plt.xlabel('Profit (€)')
> plt.title('Monte Carlo Simulation: Product Launch Profit')
> plt.legend()
> plt.show()
> ```
>
> **Questions the simulation answers:**
> - What is the expected profit? (Mean)
> - What is the downside risk? (5th percentile, P(loss))
> - What is the upside potential? (95th percentile)
>
> **The GIGO question:** the simulation assumes units follow a normal distribution with mean 10,000. Where did that number come from? If it came from a market research survey with 50 respondents, it carries substantial uncertainty. If it came from comparable product launches across 500 similar markets, it is far more reliable. The output distribution is only as good as the input distributions.

**Tutorial (attempt before class):**

Adapt the worked example:
1. Change the price distribution to normal (mean €22, SD €2) instead of uniform. How does the profit distribution change?
2. Add sensitivity analysis: run three versions of the simulation with units mean = 8,000, 10,000, 12,000. Plot all three profit distributions on the same chart.
3. Identify the input that has the largest effect on P(loss) — change one input at a time and observe.

---

## In-Class Session (90 minutes)

### Part 1 — Opening Challenge (10 minutes)

Instructor projects one number: **"P(loss) = 11%"**

Students write down for 2 minutes: "What does this mean? What does it not mean? What would you want to know before acting on it?"

After 2 minutes: share responses. Expected answers — it means roughly 1 in 9 scenarios end in a loss; it doesn't mean there's an 11% probability in the real world (that depends entirely on the quality of the input distributions); what you'd want to know: where did the input distributions come from?

This is the session's core tension, planted at the start: simulation output is only as reliable as the inputs. The rest of the session explores that tension.

---

### Part 2 — Live Coding: Build the Simulation (20 minutes + 10 minutes buffer)

Instructor reproduces the worked example from scratch in Jupyter. Students follow along.

Key decision points to explain:
- **Number of simulations (N):** 10,000 is standard for business purposes. More gives more stable estimates of tail probabilities; fewer is faster but noisier. Show: run with N=100 vs N=10,000 and compare P(loss) estimates.
- **Seed setting:** `np.random.seed(42)` makes the simulation reproducible. Without it, every run produces different results — which is correct statistically but inconvenient for reporting.
- **Distribution choice:** why normal for units? Why uniform for price? These are assumptions — the simulation would behave differently with different distributions. The GIGO principle applies here.

Buffer: use it to extend the sensitivity analysis — change units mean from 10,000 to 8,000 and observe the shift in the profit distribution. This sets up Part 3.

---

### Part 3 — Sensitivity Analysis Lab (25 minutes)

Pairs receive the same base model (product launch) with a business twist: they are advising a risk-averse investor who wants to know:
1. What is the worst-case profit (5th percentile)?
2. What is the probability of losing more than €50,000?
3. Which single input, if I could make it more certain, would reduce the downside risk most?

**Task — tornado analysis by simulation:**
Run 5 versions of the model:
- Baseline
- Units SD reduced by 50% (better demand forecasting)
- Price SD reduced by 50% (longer-term contract with fixed pricing)
- Variable cost SD reduced by 50% (supply contract with fixed unit cost)
- Fixed cost uncertainty added (assume fixed costs are actually normal with SD €10,000)

For each version, record: mean profit, 5th percentile, P(loss).

The variable that reduces P(loss) most when made certain is the highest-priority risk mitigation target. This is the quantitative version of a risk ranking.

Students produce a 4-row results table. In 15 minutes of computation; then 10 minutes to interpret: "If you had to choose one risk to reduce first, which would it be? What does the simulation tell you — and what does it not tell you?"

---

### Part 4 — GIGO Debrief (20 minutes)

Each pair presents their results (90 seconds each). The class asks one question for every presentation:

*"Where did the input distributions come from in your simulation?"*

If the answer is "we assumed normal with these parameters" — follow up: "What would change if the demand distribution was actually bimodal?" or "What if demand has a fat tail?"

The purpose: students who run a simulation and report P(loss) = 11% as though it's a fact have misunderstood the tool. P(loss) = 11% given these input assumptions is accurate. P(loss) = 11% in reality is a different claim entirely, and only as valid as the inputs.

**The GIGO moment:** the instructor picks the pair whose input assumptions were weakest (e.g., assumed normal demand with no empirical basis) and asks: "If the true demand distribution is exponential rather than normal — right-skewed, with occasional very high demand and frequent very low demand — would P(loss) be higher or lower than 11%? Qualitatively, what happens?"

Students reason through it: right-skewed demand means more scenarios with very low units sold → higher P(loss). The simulation with normal demand was optimistic.

---

### Part 5 — Debrief (10 minutes)

**Close the loop on Block 4:**

*"We've now covered time series (Week 16), optimisation (Week 17), and simulation (this week). What do all three have in common?"*

They all make assumptions about the future: that patterns continue (time series), that constraints are known (LP), that distributions are stable (simulation). When the assumptions hold, the tools produce defensible outputs. When they break, the outputs mislead with confidence.

**Bridge to Weeks 19–22:**

> *"Everything in this course has been building to the next four weeks. You get to own the full problem: choose a question, choose a dataset, choose the tools, and defend your conclusions. The analytical skills are in place. What's left is the hardest part: knowing which question is worth asking and which answer you can actually defend."*

---

## After Class (Student Post-Work)

No LMS post. The simulation notebook is the lab output. Students who want to extend: use the tornado analysis framework to write a one-paragraph risk communication for a non-technical decision-maker: "Based on our simulation, the most important risk to manage is ___ because ___. If we can reduce the uncertainty in ___, the probability of loss drops from ___% to approximately ___%. The main assumption behind this finding is ___."

This is the communication standard for Block 4 (Weeks 19–22): technical output translated into a decision-relevant recommendation with stated assumptions.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| GIGO framing introduced at the start (P(loss) = 11% challenge) | Ausubel (1968): advance organiser for the session's key tension; students who hold the GIGO question throughout the session see the tornado analysis as answering it, not just as a computational exercise |
| Tornado analysis via simulation (not Excel spider chart) | Students have Python from Block 2; doing the tornado analysis computationally is faster and more transparent than a static chart; the code also shows exactly which parameter was changed, removing ambiguity |
| N = 100 vs N = 10,000 demonstration | Lovett & Greenhouse (2000): making variability visible; students who see the P(loss) estimate fluctuate at N = 100 but stabilise at N = 10,000 understand convergence without a formal proof |
| GIGO debrief targets the weakest input assumption in each pair | Bjork (1994): desirable difficulties — being challenged on your assumptions is uncomfortable; it produces better understanding than unchallenged results |
| Block 4 close: "what do all three tools assume?" | Cepeda et al. (2006): spacing effect — retrieving the assumption-questioning thread from Weeks 16 and 17 in Week 18 strengthens the overarching principle |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Opening challenge (P(loss) = 11%) | 10 min | 2 min individual + class share; GIGO question planted |
| Live coding: build simulation | 20 min | N=100 vs N=10,000; seed; distribution choice |
| Buffer (explicit) | 10 min | Sensitivity preview; distribution change demonstration |
| Sensitivity analysis lab | 25 min | 15 min computation + 10 min interpretation |
| GIGO debrief | 20 min | ~90 sec per pair; input assumption challenge |
| Debrief | 10 min | Block 4 close; bridge to Weeks 19–22 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Students may treat P(loss) = 11% as a fact rather than a conditional probability.

The simulation produces a number with apparent precision. Presenting it as "the probability of loss is 11%" without qualification misleads decision-makers.

**Resolution:** the opening challenge explicitly asks "what does it not mean?" before any simulation is run. The GIGO debrief reinforces it. The optional post-work paragraph requires students to state the assumption. Three exposures to the same conceptual point in one session.

---

### 2. Generating 10,000 random numbers may feel like magic.

Students who don't understand why 10,000 is better than 100 will not understand the trade-off between simulation scale and reliability.

**Resolution:** the N = 100 vs N = 10,000 demonstration in Part 2 makes this concrete: P(loss) at N = 100 varies from 8% to 14% across different runs (due to random seed variation); at N = 10,000, it stabilises around 11%. This is the Law of Large Numbers in action, though we don't need to name it.

---

### 3. The tornado analysis requires five simulations and a results table — which is more bookkeeping than analysis.

Students may spend most of Part 3 running models and not enough time interpreting them.

**Resolution:** the instructor should suggest the following workflow: write the loop before the session (a for loop over SD values), run it in one cell, then spend the remaining time on the table and interpretation. Provide a results table template (blank DataFrame with the right columns) on the course portal.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Taleb, N.N. (2007). *The Black Swan: The Impact of the Highly Improbable.* Random House.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
