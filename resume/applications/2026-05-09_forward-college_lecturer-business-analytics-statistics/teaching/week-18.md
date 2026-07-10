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
- §15-6 Effects of input distributions on results (pp. 811–820) — §15-6a (shape) and §15-6b (correlated inputs) are exactly Part 3's sensitivity lab and the GIGO debrief

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
> (a) Run the simulation and compare its mean profit to the deterministic €80,000. They should match (within Monte Carlo noise). Why does "plug in the means" give the correct *mean* here — and what modelling feature would break that equality? Test your answer: add a production capacity of 12,000 units (`units_sold = np.minimum(units, 12_000)`) and rerun. What happens now?
>
> *Explanation:* With independent inputs and a profit function that is linear in each term (units × price − units × cost − fixed), expectation distributes: E(profit) = E(units)E(price) − E(units)E(cost) − fixed = exactly €80,000 — the deterministic answer is unbiased *for the mean*. The **flaw of averages** appears once the function is nonlinear: with the 12,000-unit cap, E[min(units, 12,000)] ≈ 9,700 < 10,000, because the cap truncates the upside but not the downside (Jensen's inequality) — so the deterministic model now *overstates* expected sales and profit. And even without the cap, the deterministic model reports only a point: it cannot show variance, skewness, or tail risk — which is what (b)–(e) are about.
>
> (b) The deterministic model says "expected profit = €80,000." The simulation (uncapped model) agrees on the mean but adds "P(loss) ≈ 11%." What critical information does the deterministic model completely hide?
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
> Assume unit margin = retail price × FX rate − component cost × (1 + tariff rate), and total profit = units sold × unit margin − fixed costs of €18M. (The tariff is an import duty on the component, so it inflates component cost — at a 145% tariff the €42 component costs €102.90 landed.)
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

## Answer Key

### T4 — Effect of N on simulation stability

**(a)** The **mean** profit is most stable across different N. By the Law of Large Numbers, the sample mean converges to the true expected value as N increases — even at N = 100, the mean is a reasonable estimate. The **5th percentile** (and other tail statistics) are least stable. Tail statistics estimate probabilities in the tails of the distribution, which are rare events by definition. At N = 100, only about 5 observations should fall below the 5th percentile — a single unusual draw can move this estimate dramatically. At N = 10,000, about 500 observations populate the tail, giving a much more stable estimate.

**(b)** The **Law of Large Numbers** (LLN) explains stabilisation: as N increases, the sample statistic (mean, percentile, P(loss)) converges to its true population value. The variance of the sample mean decreases as 1/N — four times as many iterations halves the standard deviation of the estimate. For tail probabilities, the same principle applies but requires larger N because tail events are rare and each individual observation carries more weight.

**(c)** For P(loss) ≈ 11%: heuristic N ≥ 1,000 / 0.11 ≈ **9,100.** Use N ≥ **10,000** to ensure the 5th percentile and P(loss) are reliable to one decimal place.

**(d)** Increasing N from 10,000 to 1,000,000 narrows the 5th percentile estimate from (say) −€15,200 ± €500 to −€15,400 ± €50. The additional accuracy is 100-fold more precise. Whether this matters for the business decision: if the decision threshold is "should we launch given P(loss) ≈ 11%?" — the answer is the same whether P(loss) is 10.8% or 11.2%. The marginal benefit of 100× more computation is essentially zero for most business decisions. A good rule: run enough iterations so that repeating the simulation gives the same business conclusion, not the same decimal digit.

**(e)** `np.random.seed(42)` fixes the pseudo-random number sequence so that the simulation produces identical results on every run. This matters for **reproducibility in business reporting**: a CFO asking "what was the P(loss) from yesterday's simulation?" needs the same number when the simulation is rerun. Without a fixed seed, every run gives slightly different results, which can confuse stakeholders. The underlying statistical validity is unaffected: the simulation is equally valid with or without a fixed seed — the seed only determines which specific random draw is taken, not whether the distribution from which it is drawn is correct.

---

### T5 — Simulation vs deterministic (flaw of averages)

**(a)** The deterministic approach produces €80,000 by plugging the mean of each input into the formula. The simulation produces a slightly different mean because the **product of two random variables has a different expected value than the product of their expectations** in the presence of nonlinear interactions. In this case: Revenue = units × price. Even though units and price are independent, the product's distribution is not symmetric (it is right-skewed for positive random variables), making the median profit lower than the mean and the mean profit slightly different from the "plug in the mean" calculation. More fundamentally, the deterministic model reports only a point estimate — it cannot compute the variance, skewness, or tail risk of the output.

**(b)** The deterministic model completely hides: (i) the **probability of a loss** (which the simulation reports as 11%); (ii) the **range of outcomes** — the 5th to 95th percentile spread; (iii) the **downside risk** — how bad the worst outcomes are; (iv) the **shape of the distribution** — whether profit is symmetric or right/left-skewed. The single number "€80,000" contains none of this information.

**(c)** The investor should ask: "What is the probability the company loses money, and what would the loss be in the worst 10% of scenarios?" These questions require the simulation; the deterministic report cannot answer them.

**(d)** The deterministic approach is acceptable when: input uncertainty is small relative to the decision threshold (e.g., a cost estimate with ±1% uncertainty when the profit margin is 40%); the relationship between inputs and output is linear (so E(output) = f(E(inputs))); the decision does not depend on tail risk. It is dangerously misleading when: input uncertainties are large and multiply together (e.g., uncertain units × uncertain price × uncertain costs = highly uncertain profit); when the decision depends on the probability of exceeding a threshold (e.g., will we exceed our €60,000 fixed cost?); or when the inputs are correlated in ways that amplify tail risk.

**(e)** "Using best estimates for each input is defensible when the uncertainties are small relative to the decision margin and the relationships are approximately linear — for example, estimating headcount costs for next quarter when salary is well-known and headcount varies by ±5%. It is not defensible when multiple uncertain inputs combine multiplicatively, when tail risk matters for the decision (e.g., risk of insolvency), or when the input uncertainties are genuinely large — in those cases, plugging in mean values produces a false sense of precision while hiding the true distribution of outcomes."

---

### T6 — Sensitivity analysis and risk mitigation

**(a)** **Units demand uncertainty** has the largest impact on P(loss): halving the units SD (from 2,500 to 1,250) cuts P(loss) from 11% to 5% — the largest reduction of any input. This tells the startup that demand forecasting accuracy is the most important risk lever. Reducing uncertainty about how many units will sell has twice the risk-reduction benefit of reducing price uncertainty and more than twice the benefit of reducing variable cost uncertainty. The startup should prioritise investment in demand research over cost certainty or price negotiation.

**(b)** Baseline expected cost of loss = 0.11 × €200,000 = **€22,000.** With 40% reduction in units SD (SD drops from 2,500 to 1,500): P(loss) interpolates between 11% (baseline) and 5% (50% SD reduction) — approximately 7%. New expected cost = 0.07 × €200,000 = **€14,000.** Reduction in expected loss cost = €22,000 − €14,000 = **€8,000.** This is less than the €15,000 research cost — **not worth it at these numbers alone.** However, the analysis ignores the value of better demand information for production planning, inventory optimisation, and capital allocation — all of which benefit from reduced uncertainty beyond the direct loss probability reduction.

**(c)** The tornado analysis varies one input at a time (one-way sensitivity) because it isolates the marginal effect of each individual input on P(loss). Limitation: it ignores **interaction effects** between inputs. If units sold and price are negatively correlated (lower demand pushes prices down too, amplifying losses), the joint effect on P(loss) is larger than either individual effect alone. One-at-a-time analysis would underestimate the combined risk. A full joint sensitivity analysis (varying multiple inputs simultaneously and modelling their correlations) would require a more complex simulation setup — but would give a more accurate picture of combined uncertainty.

**(d)** Business events that can make previously fixed costs uncertain: (i) **Lease renegotiations or property market changes** (a fixed-term lease expiring during the project creates uncertain renewal costs); (ii) **Regulatory or compliance cost changes** (a new emissions regulation could add an unanticipated fixed compliance cost); (iii) **Currency movements** (if fixed costs are denominated in a foreign currency, they are fixed in that currency but uncertain in the reporting currency); (iv) **Insurance premium changes** (particularly post-COVID or post-flood events).

**(e)** "Based on our simulation, the most important risk to manage is **demand uncertainty (units sold)**, because halving the uncertainty in unit demand reduces the probability of loss from 11% to approximately 5% — the largest reduction of any input. If we can reduce the uncertainty in **projected unit sales** (e.g., through pre-orders, pilot testing, or market research), the probability of loss drops from 11% to approximately 5–7%. The main assumption behind this finding is that unit demand uncertainty is independent of price uncertainty — if a price war simultaneously reduces both volume and price, the actual P(loss) could be higher than either input individually suggests."

---

### T7 — GIGO diagnostic (property development simulation)

**(a)** Sale price: Normal(€320,000, €40,000) based on 3 comparable sales. (i) Distribution may be appropriate for a symmetric market but 3 sales is a very small sample — the mean and SD estimates carry high uncertainty. (ii) Property markets are often **right-skewed** (a few exceptional sales pull the mean up); a lognormal or right-skewed distribution may be more appropriate. Additionally, 3 comparables may not span the market conditions at time of sale. (iii) If the normal distribution overestimates the mean sale price (3 comparables included an exceptional sale), P(loss) is **underestimated.** If market conditions deteriorate by project completion (18+ months away), actual prices may be lower than comparable sales today suggest.

**(b)** Construction cost: Normal(€2,800/m², €200) based on a quote from 6 months ago. (i) Using a 6-month-old quote as the current distribution mean is risky — construction costs have been volatile. (ii) **Inflation and supply chain disruptions** can cause construction costs to rise significantly during the project (which lasts 18 months). A normal distribution also ignores the possibility of large unexpected cost overruns (structural discoveries, labour disputes), which are better captured by a right-skewed distribution. (iii) If construction costs are underestimated (as 6-month-old quotes likely are in an inflationary environment), P(loss) is **underestimated.**

**(c)** Construction time: Normal(18 months, SD 2 months). (i) A normal distribution implies a small probability of completing in 14 months (3 SD below) — theoretically possible but unrealistic. More problematically: construction projects **almost always take longer than planned** due to weather, subcontractor delays, and inspections. A right-skewed distribution (e.g., lognormal) would be more appropriate. (ii) The normal distribution assigns equal probability to finishing early and finishing late — but construction delays are far more common than early completions. (iii) If delays are underestimated, carrying costs (interest, site management) during the extended period are underestimated → P(loss) is **underestimated.**

**(d)** Inflation rate: fixed at 3%. (i) Treating inflation as fixed ignores interest rate uncertainty and macro shocks. Over an 18-month project, inflation could range from 1% to 6%+ depending on macro conditions. (ii) **Stagflation or supply-driven inflation** (as experienced in 2022–2023) could spike material costs while weakening demand for new apartments. (iii) Fixing inflation at 3% rather than treating it as uncertain means the simulation underestimates the spread of possible outcomes → P(loss) is **underestimated** (the simulation looks more precise than it should).

**(e)** Planning permission: treated as certain (P = 1). (i) Not appropriate — planning permission is never certain, even in "easy" jurisdictions. (ii) **Unexpected objections, environmental reviews, or political changes** can delay or deny permission. A project denied permission after €1–2M in pre-development costs could produce a large loss. (iii) Treating permission as certain completely ignores this tail risk → P(loss) is **severely underestimated.** A 5% probability of denial combined with a €2M sunk cost would shift P(loss) materially.

**Overall:** the P(loss) = 8% from this simulation is almost certainly a **significant underestimate** of true risk. Four of the five inputs have assumptions that bias the simulation toward optimism: construction costs are likely understated (old quote), construction time underestimates delays (symmetric normal vs right-skewed reality), inflation is treated as certain (underestimates spread), and planning permission is assumed certain (ignores a real tail risk). A corrected simulation with realistic distributions would likely show P(loss) of 15–25% or higher.

---

### T8 — GIGO diagnostic: US tariff uncertainty (April 2025)

**(a)** Before April 2025, fixing the tariff at 20% seemed reasonable because it was the established trade policy rate — US tariffs on Chinese electronics had been at approximately 20–25% for several years following the 2018–2019 US-China trade dispute. Using a known, stable policy rate as a fixed input is standard practice when there is no credible signal of imminent change. The "risk" being ignored was **policy risk (also called political risk or regulatory risk)** — the possibility that government policy could change discontinuously. Policy risk is structurally different from market risk (demand, price fluctuations): it is not modelled by continuous distributions because it involves discrete, hard-to-predict government decisions.

**(b)** Pseudocode for a discrete tariff draw:
```python
import numpy as np
rng = np.random.default_rng(42)
tariff_scenarios = [0.20, 0.54, 1.45]   # 20%, 54%, 145%
tariff_probs    = [0.35, 0.40, 0.25]    # probability weights
tariff = rng.choice(tariff_scenarios, p=tariff_probs)  # one draw
# For N=10,000 draws:
tariffs = rng.choice(tariff_scenarios, size=10_000, p=tariff_probs)
```
Each of N = 10,000 simulations draws one tariff rate with the specified probabilities.

**(c)** Compared to fixing tariff at 20%: including tariff uncertainty increases P(loss) because 65% of scenarios have tariff rates above 20% (40% at 54%, 25% at 145%), which compress profit margins. At 145% tariff, profit per unit is severely negative; this tail significantly raises P(loss). Compared to fixing tariff at 145%: the simulation with uncertainty shows lower P(loss), because 35% of scenarios use the 20% rate (near-baseline profitability). The simulation with uncertainty represents the analyst's honest uncertainty about which scenario will materialise.

**(d)** Analyst 1 (35%/40%/25%): greater weight on the pause being maintained; lower expected tariff. Analyst 2 (50%/30%/20%): greater weight on the pause, slightly lower tariff risk. The resulting P(loss) will be lower for Analyst 2's weights (more probability mass at 20% tariff). This reveals that **simulation output is sensitive to the input probability assignments**, which are themselves subjective. A 15 percentage-point difference in the probability of the 20%-scenario (35% vs 50%) could shift P(loss) by several percentage points. This is not a flaw of simulation — it is an honest acknowledgement that the analyst's judgment about policy probabilities materially drives the result.

**(e)** The analyst is right. A simulation with explicit uncertainty is more honest than a budget that assumes tariffs stay at 20% — the budget creates a false sense of precision (one specific profit figure) that hides the true decision environment. The CFO's concern about "too many unknowns" conflates simulation uncertainty with model unreliability: acknowledging uncertainty in the model does not make it meaningless; it makes it accurate. The simulation output should be used for: (i) understanding the range of possible outcomes and their probabilities; (ii) identifying which inputs drive the most risk (sensitivity analysis); (iii) informing hedging or contingency planning (e.g., how much cash buffer is needed?). The simulation should NOT be used as a precise point prediction, a basis for marketing promises, or a substitute for scenario planning that incorporates non-quantifiable strategic factors.

**(f)** The rapid change in the "right" probability weights (within 7 days) implies: (i) **Monte Carlo simulations should be presented with explicit model dates and "as of" conditions** — a simulation run on April 2 is a model of the April 2 decision environment, not a durable forecast. (ii) **Models should be updated whenever a material input changes** — in fast-moving policy environments, this may mean weekly or even daily updates for time-sensitive decisions. (iii) Decision-makers should be told: "This simulation assumes probability weights as of [date] — if the tariff policy changes again, rerun the model." The output should be accompanied by a sensitivity table showing how P(loss) changes under each analyst's probability assignment, so decision-makers understand the range of defensible conclusions rather than a single "answer."

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
- Fixed cost uncertainty added (assume fixed costs are actually normal with SD €8,000, matching T6)

For each version, record: mean profit, 5th percentile, P(loss).

The variable that reduces P(loss) most when made certain is the highest-priority risk mitigation target. This is the quantitative version of a risk ranking.

Students produce a five-row results table (baseline + four variants). In 15 minutes of computation; then 10 minutes to interpret: "If you had to choose one risk to reduce first, which would it be? What does the simulation tell you — and what does it not tell you?"

---

### Part 4 — GIGO Debrief (15 minutes)

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
| GIGO debrief | 15 min | ~90 sec per pair; input assumption challenge |
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

---

# Supplement (2026-07-06): Textbook Cross-Reference, Corrections + Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapters 15–16

Chapter 15 references are accurate (15-1 through 15-5, correct pages; @RISK correctly made optional with the Python substitution noted). Additions:

- **§15-6 (Effects of Input Distributions on Results, pp. 811–820)** is precisely Part 3's sensitivity lab and the Part 4 GIGO debrief — including 15-6b (Effect of Correlated Input Variables), which the session raises in T6(c) but never demonstrates. Assign it.
- **Chapter 16 (Simulation Models)** is where A&W apply this machinery to real business structures — 16-2 operations (bidding, warranty), 16-3 financial models, 16-4 marketing/churn. One pre-work sentence ("skim Chapter 16's contents; in Weeks 19–22 you may want one of these model templates for your own analysis") turns an unused chapter into a Block 4 resource library.

## 2. Corrections + Extended Questions

**Correction 1 — T5's "flaw of averages" example doesn't contain a flaw of averages.** With independent inputs and profit = units×price − units×cost − fixed (all linear in each variable), expectation distributes: E(profit) = 10,000×22 − 10,000×8 − 60,000 = **exactly €80,000**. The plug-in-the-means answer is *unbiased* here; the "simulation says ≈ €79,000" difference is Monte Carlo noise, not a systematic effect. The question's hint ("E(units × price) ≠ E(units) × E(price) because they are multiplied") is false under independence — and the answer key half-notices, conceding independence and then gesturing at variance and medians. What the deterministic model genuinely hides is the *distribution* (spread, P(loss), tails) — parts (b)–(e) are correct and should survive. *Fix that makes (a) true:* add a capacity constraint — `units_sold = np.minimum(units_demand, 12_000)`. Then f is concave and Jensen's inequality bites: E[min(D, 12,000)] ≈ 10,000×Φ(0.8) − 2,500×φ(0.8) + 12,000×(1−Φ(0.8)) ≈ **9,700 units**, so true expected revenue is ~3% below the plug-in-means figure — a genuine, computable flaw of averages, and exactly the structure A&W's own §15-3 example uses. Rewrite T5(a) around the capped model (see T9 below for the ready-made replacement).

**Correction 2 — T8's tariff algebra is wrong.** "Profit per unit = (retail price × FX − component cost) × (1 − tariff) − fixed costs of €18M" both (i) applies the tariff to the *entire margin* — tariffs are import duties on the component, not a tax on profit — and (ii) subtracts a total fixed cost inside a per-unit expression. *Fix:* unit margin = retail × FX − component_cost × (1 + tariff); total profit = units × unit margin − €18M. At 145%, the component cost becomes €42 × 2.45 ≈ €102.9/unit — which is what actually makes the 145% scenario catastrophic, and now for the economically correct reason. (Minor: the same question's code mixes `np.random.seed` with the `default_rng` API — use `rng = np.random.default_rng(42)` throughout.)

**T9 — The flaw of averages, done right (replacement/extension for T5(a)):**

> The startup's contract manufacturer caps production at 12,000 units. Demand D ~ Normal(10,000, 2,500); units sold = min(D, 12,000).
>
> (a) The deterministic analyst plugs in the mean: min(10,000, 12,000) = 10,000 units. Simulate: what is E[units sold]?
> (b) Why does the cap reduce the expectation even though the mean demand is *below* the cap?
> (c) State the general principle, and name one other business structure with the same shape.
>
> **Answers:** (a) ≈ **9,700 units** (simulation; analytically μΦ(z) − σφ(z) + c(1−Φ(z)) with z = 0.8). (b) The cap truncates the upside (demand above 12,000 sells only 12,000) while the downside is untouched — averaging an asymmetric outcome pulls the mean down; the plug-in-means calculation never sees the asymmetry because the *mean* demand isn't clipped. (c) E[f(X)] ≠ f(E[X]) whenever f is nonlinear (Jensen's inequality) — the flaw of averages. Same shape: overtime kicking in above a labour threshold, penalty clauses above a delivery date, option payoffs, progressive taxes, stockouts (Week 16's newsvendor logic).

**T10 — Correlated inputs (demonstrates §15-6b and T6(c)'s warning):**

> Realistically, price and demand are negatively related (higher price → fewer units). Model this with correlation ρ = −0.6 between the demand and price draws.
>
> (a) Before running: will P(loss) rise or fall vs the independent model? Reason it out.
> (b) One implementation: `cov = [[2500**2, -0.6*2500*2.31], [-0.6*2500*2.31, 2.31**2]]; draws = rng.multivariate_normal([10000, 22], cov, N)` (2.31 ≈ SD of Uniform(18,26)). Run and compare P(loss).
> (c) Why did the tornado analysis in T6 systematically understate risk if correlations exist?
>
> **Answers:** (a) With ρ < 0 between price and demand, revenue draws are *compressed* toward the middle (high demand comes with low price and vice versa) — Var(revenue) falls, and P(loss) typically **falls** relative to independence; the important lesson is that students must reason about which correlation *raises* risk: cost–demand *positive* correlation (busy market → expensive components) fattens the loss tail. (b) Expect P(loss) to move by several points; direction per (a). (c) One-at-a-time variation holds everything else fixed, so it cannot see interactions — the answer T6(c) gives verbally, now demonstrated numerically. Correlation assumptions belong on the GIGO checklist alongside distribution shapes.

**T11 — Choose the decision, not just the risk (newsvendor by simulation):**

> The startup must commit a production quantity Q before demand is known (unit cost €8, price €22, unsold units salvage €3).
>
> (a) For Q ∈ {8,000, 10,000, 12,000, 14,000}, simulate expected profit and P(loss).
> (b) Why is the profit-maximising Q above mean demand here?
> (c) Connect to Week 16 T7(c) and Week 17: what kind of tool have you just built?
>
> **Answers:** (a) Simulation gives an interior optimum (near the newsvendor quantile: underage cost 14, overage cost 5 → optimal service level 14/19 ≈ 74th percentile of demand ≈ 10,000 + 0.64×2,500 ≈ **11,600**). (b) Losing a €14 margin on a stockout hurts more than eating €5 on an unsold unit, so you deliberately overshoot the mean. (c) Simulation-based *optimisation* — using Week 18's engine to answer Week 17's "what should we do?" question when inputs are random. This is the precise hand-off Block 4's arc promises, currently only gestured at in the bridge.

## 3. Alternative In-Class Activities (additional options)

**A. Dice-and-cards Monte Carlo (12 min, before the code).** Teams run 15 hand trials of a mini profit model: a die roll sets the demand tier, a coin sets price high/low, a second die sets cost. Pool all trials into one board histogram, count losses. Then Part 2's code does the same thing 10,000 times. Like Week 11's bag-of-chips activity, the physical version inoculates against "the computer said 11%" magic — students *were* the simulation.

**B. Elicitation role-play (15 min, answers "where do inputs come from?").** Pairs: one plays product manager (given a private fact sheet), one plays analyst who may ask five questions to elicit a min / most-likely / max for demand, then builds a triangular distribution from the answers (A&W §15-2's distribution gallery includes triangular precisely for this). The GIGO debrief then has teeth: every pair can answer "where did your distribution come from?" with "we elicited it — here's the trail." This is the single most professionally realistic activity available for this week.

**C. Seed ensemble (8 min, extends T4).** Run the identical model under 20 different seeds; plot the 20 P(loss) values as a dot strip at N = 100, then N = 10,000. The Monte Carlo *standard error* becomes a picture: the spread collapses as N grows. Follow with the one-liner: "simulation estimates have confidence intervals too — Week 12 applies to Week 18."

**D. Correlation switch demo (5 min, pairs with T10).** One projected cell toggles ρ between 0 and −0.6/+0.6; the profit histogram and P(loss) update live. The fastest possible demonstration that dependence assumptions are inputs of the same rank as distributions.

**E. Risk memo speed-round (10 min, closes Part 4).** Every pair completes the post-work fill-in paragraph ("the most important risk is ___ because ___…") in five minutes, swaps with another pair, and grades it against three checks: names a specific input, quantifies the P(loss) change, states the load-bearing assumption. Converts the optional post-work into a peer-checked in-class artefact — and it's a rehearsal for the Week 20–22 limitation statements.

## 4. Critique of the Lesson Plan

**What works (keep):** the P(loss)-first opening challenge ("what does it *not* mean?"); T4's treatment of Monte Carlo error and seeds (rarely taught, professionally essential); T7's input-by-input GIGO audit with directional bias reasoning (the best question of the week); T8(f)'s model-dating point; the Block 4 close ("all three tools assume the future resembles the past").

**Problems, reasons, and fixes:**

1. **T5's flaw-of-averages demonstration doesn't demonstrate it (Correction 1).** The week's central contrast rests on a linear model where plug-in-means is provably unbiased; strong students will simulate, get €80,000 ± noise, and correctly conclude the question is wrong. Adopt the capacity cap (T9) — it is one `np.minimum` line and makes the claim true.
2. **T8's tariff formula is economically wrong (Correction 2)** — and this is the question explicitly built for realism, sourced to real April 2025 events. Fix the algebra before students who follow trade news fix it for you.
3. **The timing table sums to 95 minutes** — fourth occurrence (Weeks 9, 16, 17). At this point the fix is structural: the Block 4 template's Part 4 should be 15 minutes, and all four files corrected in one pass.
4. **The model criticises a practice it also commits.** T7(c) rightly attacks Normal(18, 2) construction time for permitting impossible negative values — but the worked example draws units and variable cost from unbounded normals too (negative-probability mass is negligible here, ~3×10⁻⁵, but the *principle* is identical). One line in Part 2 ("check: how many draws were negative? what would you do if it mattered?" → `np.maximum(units, 0)` or a lognormal) makes the session practise its own audit standard.
5. **§15-2 is assigned but distribution *choice* is never exercised.** Every distribution in the session is handed to students pre-chosen; the reading's catalogue (uniform vs triangular vs normal vs discrete) never becomes a decision anyone makes. Activity B closes this — and it's the skill Weeks 19–22 will actually demand, since students' own analyses will have no one to hand them distributions.
6. **Small consistency slips:** Part 3 says "4-row results table" but specifies five model versions (baseline + four variants); T6's table is the same five rows — make it five. And the tornado lab's fixed-cost variant (SD €10,000) differs from T6's printed scenario (SD €8,000) — harmonise so the in-class table can be checked against the tutorial's.
7. **The decision layer is missing until the bridge.** The session measures risk (P(loss)) but never *chooses* anything with it — yet Week 17 was optimisation and Weeks 19–22 demand recommendations. T11 (newsvendor-by-simulation) adds the missing "so what should we do?" step in ~15 lines of code, and directly discharges the Week 16 T7(c) newsvendor promissory note.
