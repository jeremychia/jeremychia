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
- [Monte Carlo Simulation — Investopedia](https://www.youtube.com/watch?v=7ESK5SaP-bc) (8 min) — business applications. *Active watching: when the video shows the output distribution of a Monte Carlo simulation, pause and write: what does the shape of this distribution tell you that a single "expected value" calculation does not? This is the core argument of T5 (simulation vs deterministic).*
- [Monte Carlo Simulations: Data Science Basics — ritvikmath](https://www.youtube.com/watch?v=EaR3C4e600k) (7 min) — code walkthrough using numpy, directly analogous to the simulation built in Part 2. *Active watching: when ritvikmath runs the simulation and plots the results, pause and identify: what are the three numpy functions he uses to generate the random inputs? These are the same functions in the worked example — recognising them before class makes Part 2 faster.*

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

*The Investopedia video's output distribution is the visual version of the profit histogram in this worked example. The three numpy functions (np.random.normal, np.random.uniform, np.random.normal) from the ritvikmath video are the three lines that generate units, price, and var_cost. The tutorial tasks are direct adaptations — changing one input at a time to observe the effect on the output distribution.*

**Tutorial (attempt before class):**

Adapt the worked example:
1. Change the price distribution to normal (mean €22, SD €2) instead of uniform. How does the profit distribution change?
2. Add sensitivity analysis: run three versions of the simulation with units mean = 8,000, 10,000, 12,000. Plot all three profit distributions on the same chart.
3. Identify the input that has the largest effect on P(loss) — change one input at a time and observe.

**Additional tutorial questions (attempt after the main tutorial tasks above):**

*T4 — Boundary case: what happens when you change N (number of simulations):*

> Using the product launch model from the worked example, run three versions of the simulation with different numbers of iterations: N = 100, N = 1,000, and N = 10,000. For each, record: mean profit, 5th percentile profit, and P(loss).
>
> (a) Which output statistic is most stable across the three versions? Which is least stable? Explain why tail statistics (like the 5th percentile) are more sensitive to N than the mean.
> (b) At N = 100, you might observe P(loss) anywhere from 6% to 16% across different runs (due to random seed variation). At N = 10,000, the estimate stabilises. What principle from probability theory explains this stabilisation?
> (c) A risk manager requests that P(loss) be reported to one decimal place (e.g., 11.4%). What minimum N would you recommend to ensure this precision is reliable? (You may use the heuristic that for tail probabilities, N should be at least 1,000 / p, where p is the probability being estimated.)
>
> *Solution:* For P(loss) ≈ 11%, the heuristic gives N ≥ 1,000 / 0.11 ≈ 9,100. **N = 10,000 is appropriate.**
>
> (d) If you increase N from 10,000 to 1,000,000, the computational time increases 100-fold. What do you gain? What marginal benefit does the additional accuracy provide for a business decision where the 5th percentile estimate changes from −€15,200 to −€15,400?
> (e) Set `np.random.seed(42)` vs running without a fixed seed. Why does seed-fixing matter for reporting a business result, but not for the underlying statistical validity of the simulation?

*T5 — Comparison: simulation versus deterministic ("plug in the mean") approach:*

> The product launch model has these input parameters:
> - Units sold: normal(10,000, 2,500)
> - Price: uniform(18, 26) → mean = 22
> - Variable cost: normal(8, 1.5)
> - Fixed cost: 60,000
>
> **Deterministic approach (plug in the means):**
> Revenue = 10,000 × 22 = €220,000
> Profit = 220,000 − (10,000 × 8) − 60,000 = 220,000 − 80,000 − 60,000 = **€80,000**
>
> **Simulation approach:**
> Run the Monte Carlo model (N = 10,000). Observe mean profit and P(loss).
>
> (a) Why does the deterministic approach produce a different (likely higher) profit estimate than the simulation mean? (Hint: this is the "flaw of averages" from the reading. Revenue = units × price; when both are uncertain, E(units × price) ≠ E(units) × E(price) because they are multiplied together.)
>
> *Explanation:* E(units × price) = E(units) × E(price) only when units and price are **independent** — which they are in this model. However, the **variance** of the product is Var(units × price) = (E[units])² × Var(price) + (E[price])² × Var(units) + Var(units) × Var(price), which is nonzero. The distribution of the product is not symmetric, so the median profit differs from the mean profit.
>
> (b) The deterministic model says "expected profit = €80,000." The simulation says "mean profit ≈ €79,000 with P(loss) = 11%." What critical information does the deterministic model completely hide?
> (c) A startup investor receives both reports. What additional question should they ask that the deterministic report cannot answer?
> (d) When is the deterministic approach (plugging in mean values) acceptable, and when is it dangerously misleading? Give one example of each.
> (e) A CFO says: "I don't need simulation — I just use our best estimate for each input." Write a two-sentence response explaining when this approach is defensible and when it is not.

*T6 — Multi-step: sensitivity analysis and risk mitigation:*

> The product launch model has four uncertain inputs. You run a tornado analysis, varying each input's standard deviation by ±50% while holding others at baseline, and record the resulting P(loss):
>
> | Scenario | P(loss) |
> |---|---|
> | Baseline | 11% |
> | Units SD halved (1,250 instead of 2,500) | 5% |
> | Price range halved (22 ± 1 instead of 18–26) | 9% |
> | Variable cost SD halved (0.75 instead of 1.5) | 10% |
> | Fixed cost SD added (normal 60,000, SD 8,000) | 14% |
>
> (a) Which input uncertainty has the largest impact on P(loss)? What does this tell the startup about which risk to prioritise?
> (b) Reducing units SD from 2,500 to 1,250 requires better demand forecasting. A market research firm offers to conduct a study that would reduce unit demand uncertainty by 40% (not 50%) for a cost of €15,000. At the baseline P(loss), if a loss costs the startup €200,000 on average, what is the expected cost of loss, and is €15,000 worth paying for a partial uncertainty reduction?
>
> *Solution:* Expected loss cost = P(loss) × average loss = 0.11 × 200,000 = €22,000. Reduced P(loss) after 40% reduction in units SD would be approximately (interpolating) slightly above 5%; call it ~7%. New expected cost = 0.07 × 200,000 = €14,000. Reduction = €8,000 < €15,000 research cost. **Not worth it at these numbers.** However, this ignores the upside — a more accurate demand forecast also helps production planning.
>
> (c) Explain why the tornado analysis in this question varies one input at a time. What limitation does this have compared to varying inputs simultaneously?
> (d) The fixed cost becomes uncertain (SD = €8,000) in the last scenario. What business event might cause previously fixed costs to become variable or uncertain?
> (e) Write the risk communication paragraph (from the optional post-work task in the main lesson plan) for this analysis: "Based on our simulation, the most important risk to manage is ___ because ___. If we can reduce the uncertainty in ___, the probability of loss drops from ___% to approximately ___%. The main assumption behind this finding is ___."

*T7 — GIGO diagnostic: evaluate the input assumptions:*

> A property development company builds a Monte Carlo simulation to evaluate whether to develop a 50-unit apartment block. The key inputs and their assumed distributions are:
>
> | Input | Distribution assumed | Basis for assumption |
> |---|---|---|
> | Sale price per apartment | Normal(€320,000, €40,000) | Average of 3 comparable recent sales |
> | Construction cost per m² | Normal(€2,800, €200) | Contractor quote from 6 months ago |
> | Construction time | Normal(18 months, 2 months) | Project manager's estimate |
> | Inflation rate over project | Fixed at 3% | "Our standard assumption" |
> | Planning permission probability | Fixed at 100% (assumed granted) | "It always gets approved here" |
>
> The simulation reports: mean profit €4.2M, P(loss) = 8%.
>
> For each input, identify: (i) whether the distribution assumption is appropriate; (ii) one specific way it could be wrong; (iii) the likely direction of bias in the P(loss) estimate if the assumption is wrong.
>
> (a) Sale price: normal distribution based on 3 comparable sales.
> (b) Construction cost: normal distribution based on a quote from 6 months ago.
> (c) Construction time: normal distribution (implying it could theoretically be negative, or very short).
> (d) Inflation rate: fixed at 3% (treated as certain).
> (e) Planning permission: treated as certain (probability = 1).
>
> After your analysis, answer: does the P(loss) = 8% from this simulation likely underestimate or overestimate the true risk? Justify your answer with reference to at least three of the inputs above.

*T8 — Real-world GIGO: US tariff uncertainty and Monte Carlo input distributions (April 2025):*

> On 2 April 2025, the US government announced a sweeping set of tariffs under the name "Liberation Day," imposing import duties ranging from 10% to 145% on goods from multiple countries. The announcement introduced genuine uncertainty about input costs for businesses with US-facing supply chains: the tariff rates were announced, then partially paused (90-day pause for most countries except China announced April 9), then revised again. By late April 2025, companies running supply chain cost models faced a situation where the "right" tariff rate to use in a simulation was genuinely unknown.
>
> A European consumer electronics manufacturer produces headphones with the following supply chain cost structure (simplified). Its primary components come from China; it sells primarily in the US market.
>
> | Cost component | Previous distribution (pre-April 2025) | After April 2025 announcement |
> |---|---|---|
> | Component tariff rate (China imports) | Fixed at 20% | Unknown — scenarios: 20%, 54%, 145% |
> | US demand (units sold, millions) | Normal(2.5, 0.3) | Possibly lower if tariffs raise retail prices |
> | Retail price (USD) | Normal($149, $12) | Uncertain if tariffs must be passed on |
> | Component cost (EUR, per unit) | Normal(€42, €5) | Already absorbed in current contracts |
>
> Assume the company's profit per unit = (retail price × FX rate − component cost) × (1 − tariff rate) − fixed costs of €18M.
>
> (a) Before April 2025, the Monte Carlo model used a fixed tariff rate of 20%. Why might this have seemed reasonable at the time? What type of "risk" was being ignored?
>
> (b) After April 2025, the company's analyst proposes three scenarios for the tariff rate: 20% (pause maintained), 54% (new China baseline), 145% (full tariff imposed). Rather than modelling the tariff as a continuous distribution, she assigns probabilities: 35% / 40% / 25%. How would you represent this as a discrete random variable in a simulation? Write the logic (in pseudocode or Python) that generates one random draw for the tariff rate.
>
> (c) Run the full simulation (N = 10,000) with this tariff uncertainty included as a random input. How does P(loss) change compared to a model that fixes the tariff at 20%? How does it change compared to fixing it at 145%?
>
> (d) The analyst's probability assignments (35% / 40% / 25%) came from her subjective reading of trade policy news in April 2025. Another analyst assigns 50% / 30% / 20%. Run both and compare the resulting P(loss) estimates. What does this tell you about the sensitivity of the simulation to the input probability weights?
>
> (e) The company's CFO says: "This simulation has too many unknowns — the output is meaningless." The analyst responds: "A simulation with explicit uncertainty is more honest than a budget that assumes tariffs stay at 20%." Who is right, and why? What should the simulation output be used for — and what should it not be used for?
>
> (f) The US government's 90-day pause was announced on April 9, 2025. If the model had been run on April 2 (before the pause) and again on April 10 (after the pause), the "right" probability weights would have changed within one week. What does this imply for how Monte Carlo simulations should be communicated to decision-makers — and how frequently models should be updated in a fast-moving policy environment?

This question uses a verified 2025 event: the US "Liberation Day" tariff announcement (April 2, 2025) and the subsequent 90-day pause (April 9, 2025) are documented by multiple official and news sources including the White House, USTR, Reuters, and FT. The company and specific numbers are illustrative. The scenario makes concrete the session's core lesson: simulation output depends entirely on input distributions — and when input distributions cannot be reliably specified, the analyst's job is not to hide that uncertainty but to make it explicit and actionable.

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

**Orientation (5 minutes before pairs start):** Monte Carlo simulation is unlikely to have appeared in any prior course. Before pairs begin, the instructor places the tool in context with three sentences:

> "A deterministic model gives one answer. A simulation gives a *distribution* of answers — one for every possible combination of inputs, sampled thousands of times. The question we are asking is not 'what will happen?' but 'what is the range of things that could happen, and how likely is each?'"

Then one grounding question to the room: "In the worked example, why did we run 10,000 simulations rather than just plugging in the mean values for each input?" Expected answer: because using the mean ignores the spread — the 'flaw of averages' from the pre-work reading. If no one raises it, the instructor names it: `profit(mean inputs) ≠ mean(profit across all input combinations)`. This is the conceptual anchor for everything in Part 3.

This is not a re-run of Part 2. It is a formulation-first frame: before pairs vary inputs, they should be able to say what they are varying and why. Students who can't articulate the flaw of averages need these 5 minutes; students who can will move through Part 3 faster.

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
