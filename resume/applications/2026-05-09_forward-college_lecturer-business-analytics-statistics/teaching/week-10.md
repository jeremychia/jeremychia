# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 10: Decision-Making Under Uncertainty Using Decision Trees
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Construct** a multi-stage decision tree using decision nodes, probability nodes, and end nodes, and apply the folding-back procedure to identify the optimal strategy (Bloom's: Apply)
2. **Apply** Bayes' rule to update prior probabilities given imperfect information and recalculate posterior probabilities in a business context (Bloom's: Apply / Analyse)
3. **Evaluate** the expected value of information and distinguish between EVPI and EVI to judge whether purchasing a market research report is worth its cost (Bloom's: Evaluate)
4. **Critique** a published decision that failed due to base-rate neglect or miscalibrated probabilities, identifying what went wrong and proposing a corrected analysis (Bloom's: Evaluate)

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, Chapter 6 — Sections 6-1 through 6-6 (pp. 222–264; §6-7 is a one-page conclusion). Focus especially on the Acme new product example (§6-3, pp. 232–236) and the Bayes' rule treatment within §6-5 (pp. 239–257) — this is the textbook's formal home for the Bayesian machinery used informally in Week 4. Simulation-based approaches to decision problems come in Week 18.

**Videos (~20 minutes total):**

- "Decision Trees — How to Make Better Decisions" by MindTools (YouTube, ~7 min): visual walkthrough of tree construction and folding back; good for visual learners. *Active watching: when the video introduces the folding-back procedure (averaging probabilities × payoffs at a chance node), pause and apply it to a simple example: two outcomes, 0.6 and 0.4, with payoffs 100 and −20. What is the EMV? This is the exact calculation in T1(c).*
- "Bayes' Theorem — Medical Testing Example" by 3Blue1Brown (YouTube, ~15 min): accessible frequency-based intuition; the disease-testing scenario maps directly to the textbook Joe's disease example. *Active watching: when the video updates the posterior probability using new evidence, pause and write: what is the new base rate (prior) before the update? This Bayesian updating structure is exactly what T3(b) requires.*
- Optional (strong students only): Palisade PrecisionTree tutorial video from the textbook companion site (~10 min) — shows how to build the Acme tree in Excel.

**Worked example (read this before attempting the tutorial problems):**

A Berlin street-food entrepreneur, Maya, is deciding whether to rent a pitch at a weekend market. She has gathered the following information:

- **Decision:** Rent the pitch (cost €500) or stay home (€0, €0 payoff)
- **If she rents**, three outcomes are possible based on weather and foot traffic:
  - Great day: probability 0.30, revenue €2,200 → net = €2,200 − €500 = **€1,700**
  - Average day: probability 0.50, revenue €900 → net = €900 − €500 = **€400**
  - Poor day: probability 0.20, revenue €300 → net = €300 − €500 = **−€200**

**Step 1 — Build the tree.** Draw a square decision node with two branches: "Rent" and "Stay home." From the "Rent" branch, draw a circle probability node with three branches (Great/Average/Poor) leading to triangular end nodes showing the net payoffs. The "Stay home" branch leads directly to a €0 end node.

**Step 2 — Apply EMV at the probability node.**
EMV(Rent) = 0.30 × €1,700 + 0.50 × €400 + 0.20 × (−€200)
= €510 + €200 − €40
= **€670**

**Step 3 — Fold back at the decision node.** Compare €670 (Rent) vs €0 (Stay home). The maximum is €670, so the optimal decision is to **rent the pitch**.

**Critique:** Maya's numbers rest on two shaky assumptions. First, she estimated her own probabilities from memory — she has only attended this market twice before. Second, "revenue" assumes she sells out; if she has leftovers, her actual revenue is lower. The tree is only as good as the numbers inside it.

*This worked example is marked optional for students who feel confident building a decision tree from a probability description and applying the folding-back procedure. If you can complete T1(a)–(c) without a template, you don't need it. If the folding-back procedure felt abstract from the reading, work through this example step by step before the tutorials.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

---

**Tutorial problems:**

*T0 — Entry question (lower floor):*

> Before drawing any decision tree, answer in plain language:
>
> (a) You are deciding whether to carry an umbrella today. There is a 30% chance of rain. If it rains and you have an umbrella, you stay dry (value: +10). If it rains and you don't, you get soaked (value: −5). If it doesn't rain and you carry the umbrella, it's slightly inconvenient (value: −1). If it doesn't rain and you leave it at home, you're fine (value: 0).
>
> What are your two decision options? What are the two possible states of the world? Write the four combinations of (decision, state) and their values. No formal tree or EMV calculation required — just identify the structure.

T0 tests whether students can identify the fundamental structure of a decision problem — decision alternatives, uncertain states, and outcomes — before any formal notation. This is the vocabulary the worked example and T1 assume. A student who cannot answer T0 has not yet understood what a decision tree represents. No formula or Excel is required.

*Self-check for T0:* Two decisions: carry umbrella / leave it. Two states: rain / no rain. Four combinations: carry + rain = +10; carry + no rain = −1; leave + rain = −5; leave + no rain = 0. If you identified these four combinations correctly, you have the structure. If the distinction between "your decision" and "the uncertain state" felt unclear, re-read §6-1 before T1.

**T1 — Straightforward computation:**

*The MindTools video's folding-back procedure is exactly the calculation in T1(c): sum each branch's (probability × net payoff) across the three market states. The video's simple numerical example is the same structure — the only difference is that T1 has three branches instead of two.*

A student entrepreneur is deciding whether to launch a food stall at a Berlin weekend market. Use the following data:

- Renting the stall costs €600.
- If the market is **busy** (probability 0.40), she earns gross revenue of €2,500.
- If the market is **moderate** (probability 0.40), she earns gross revenue of €1,100.
- If the market is **quiet** (probability 0.20), she earns gross revenue of €400.
- The alternative is to not attend (payoff = €0).

(a) Calculate the net payoff (revenue minus stall cost) for each of the three market scenarios.

(b) Draw a decision tree with one decision node and one probability node. Label all branches, probabilities, and end-node payoffs.

(c) Apply the folding-back procedure to calculate EMV(Launch). Should she launch?

(d) Suppose the stall cost rises to €900. Does the optimal decision change? Recalculate EMV(Launch) and interpret.

*Self-check for T1(a) and (c):* Net payoffs: busy = €2,500 − €600 = €1,900; moderate = €1,100 − €600 = €500; quiet = €400 − €600 = −€200. EMV(Launch) = 0.40 × 1,900 + 0.40 × 500 + 0.20 × (−200) = 760 + 200 − 40 = **€920**. Since €920 > €0 (not attending), she should launch. If your EMV is substantially different, re-check that you subtracted the stall cost from revenue before multiplying by probabilities — the most common error.

**T2 — Interpretation:**

A PrecisionTree output for a pharmaceutical company's licensing decision shows the following (simplified):

- Decision: License the drug now vs Continue clinical trial
- **License now:** EMV = €8.4M (certain payment from partner)
- **Continue trial:** Three outcomes after 12 months:
  - Trial succeeds (p=0.55): launch independently, EMV = €22M
  - Trial partially succeeds (p=0.30): renegotiate deal, EMV = €7M
  - Trial fails (p=0.15): write-off, payoff = −€3M
- The optimal path (TRUE branch in PrecisionTree) is highlighted on "Continue trial."

(a) Verify the EMV of "Continue trial" by hand.

(b) PrecisionTree marks "Continue trial" as optimal. By how much does it beat "License now"?

(c) The CEO is risk-averse and prefers the certain €8.4M. What does this tell you about the relationship between EMV maximisation and utility maximisation? Is the CEO wrong?

(d) A junior analyst says "the model tells us the trial will succeed." Correct this misstatement precisely.

**T3 — Edge case (Bayesian updating):**

A market research firm offers to predict whether a new product will succeed or fail before launch. Historical data shows:

- Prior probability: P(product succeeds) = 0.35; P(product fails) = 0.65
- Firm accuracy: P(firm predicts "success" | product actually succeeds) = 0.75
- Firm accuracy: P(firm predicts "failure" | product actually fails) = 0.80

(a) Construct a frequency table (out of 10,000 launches) showing the joint frequencies of actual outcome × firm prediction.

(b) The firm predicts "success." Use your table (or Bayes' rule directly) to calculate P(product succeeds | firm predicts "success").

(c) Compare your posterior probability to the prior. By how much has the firm's report updated your belief?

(d) Suppose the firm charges €50,000 for its report. The payoff from launching a successful product is €500,000 and the loss from launching a failed product is −€200,000. Without the report: calculate EMV of launching. With the report, using your posterior: calculate EMV of launching given a "success" prediction, and EMV of not launching (€0). What is the EVI? Is the report worth buying?

*T4 — Boundary case: what happens when probabilities are extreme:*

> A mining company is evaluating whether to drill for oil at a promising site. The decision tree has the following structure:
>
> - **Drill** (cost €2M): if oil found (probability p), revenue €15M (net +€13M); if no oil (probability 1−p), net −€2M.
> - **Don't drill:** payoff €0.
>
> (a) For p = 0.20, calculate EMV(Drill). Should the company drill?
>
> *Solution:* EMV = 0.20 × 13,000,000 + 0.80 × (−2,000,000) = 2,600,000 − 1,600,000 = **€1,000,000 > 0.** Drill.
>
> (b) Find the break-even probability p* at which EMV(Drill) = 0.
>
> *Solution:* p × 13,000,000 + (1−p) × (−2,000,000) = 0 → 13,000,000p − 2,000,000 + 2,000,000p = 0 → 15,000,000p = 2,000,000 → p* = 2/15 ≈ **0.133 (13.3%)**. The company should drill whenever its assessed probability of finding oil exceeds 13.3%.
>
> (c) The company commissions a seismic survey at a cost of €300,000, which correctly predicts oil 85% of the time (when oil is present) and correctly predicts no oil 90% of the time (when no oil is present). Using p = 0.20 as the prior, build the frequency table and calculate the posterior probabilities after a positive seismic signal.
>
> *Solution (frequency table, out of 10,000 sites with p = 0.20):*
> Oil present: 2,000 sites. No oil: 8,000 sites.
> Survey says "oil": 0.85 × 2,000 = 1,700 true positives; 0.10 × 8,000 = 800 false positives.
> Total predicted "oil": 2,500.
> P(oil | survey positive) = 1,700 / 2,500 = **68%**
>
> (d) Using this posterior (68% probability of oil given a positive survey), calculate the EMV of drilling after a positive survey. Is it worth paying €300,000 for the survey?
>
> *Solution:* EMV(Drill | positive) = 0.68 × 13,000,000 + 0.32 × (−2,000,000) = 8,840,000 − 640,000 = €8,200,000. Net of drilling cost (already included): still €8.2M. Survey cost €300,000. Without survey: EMV = €1,000,000. With survey, if positive: drill for €8,200,000; if negative, don't drill (€0). Expected payoff from buying survey = P(positive signal) × EMV(drill | positive) + P(negative signal) × 0 − survey cost. P(positive signal) = 2,500/10,000 = 0.25. Expected payoff from survey = 0.25 × 8,200,000 − 300,000 = 2,050,000 − 300,000 = **€1,750,000 > €1,000,000 (without survey).** Yes, the survey is worth buying.
>
> (e) At what survey cost would the company be indifferent between buying and not buying the survey? (Find the cost at which the value with survey = value without survey.)

*T5 — Interpretation: reading a PrecisionTree output with risk aversion:*

> The following simplified decision tree output is given for a company choosing between two product development strategies:
>
> **Strategy X — Fast-to-market:** EMV = €3.2M. Outcomes: 60% chance of €6M; 40% chance of −€1.0M.
> **Strategy Y — Deliberate development:** EMV = €2.8M. Outcomes: 90% chance of €3.2M; 10% chance of −€0.2M.
>
> (a) Verify both EMVs by hand.
>
> *Solution:* EV(X) = 0.60 × 6,000,000 + 0.40 × (−1,000,000) = 3,600,000 − 400,000 = **€3,200,000.** EV(Y) = 0.90 × 3,200,000 + 0.10 × (−200,000) = 2,880,000 − 20,000 = **€2,860,000 ≈ €2.9M.** Both match the stated outputs.
>
> (b) Strategy X has higher EMV but also a 40% chance of a €1.0M loss. A CFO says: "We can only sustain a maximum loss of €0.8M without triggering a covenant breach on our debt." How does this constraint change the analysis?
> (c) The board requests that the team calculate the probability of achieving a positive return under each strategy. What are these probabilities?
> (d) If the company must choose one strategy and cannot revisit the decision, which strategy would you recommend — and to whom does your recommendation depend on?
> (e) A junior analyst says: "The decision tree tells us the answer: choose X." Correct this misstatement. What does the decision tree actually tell you, and what does it leave to human judgment?

*T6 — Multi-step: EVPI and the value of conducting research:*

> A retailer is deciding whether to expand into a new geographic market. Preliminary assessment:
>
> - P(market is favourable) = 0.45; if favourable, net payoff = €800,000
> - P(market is unfavourable) = 0.55; if unfavourable, net payoff = −€300,000
> - Alternative: do not expand, payoff = €0
>
> (a) Calculate EMV(Expand) and determine whether expansion is the optimal decision without information.
>
> *Solution:* EMV(Expand) = 0.45 × 800,000 + 0.55 × (−300,000) = 360,000 − 165,000 = **€195,000 > 0.** Expand.
>
> (b) Calculate the EVPI (Expected Value of Perfect Information).
>
> *Solution:* EMV with perfect information = P(favourable) × best payoff if favourable + P(unfavourable) × best payoff if unfavourable = 0.45 × 800,000 + 0.55 × 0 = €360,000. EVPI = €360,000 − €195,000 = **€165,000.**
>
> (c) A market research firm offers a study costing €100,000. The firm has a 70% accuracy rate: P(firm predicts "favourable" | market is favourable) = 0.70; P(firm predicts "unfavourable" | market is unfavourable) = 0.70. Using a frequency table (out of 10,000 scenarios), compute the posterior probabilities for each signal.
>
> *Solution:* Favourable: 4,500. Unfavourable: 5,500.
> "Favourable" signal: 0.70 × 4,500 = 3,150 correct; 0.30 × 5,500 = 1,650 false. Total "favourable" signals: 4,800.
> P(favourable | "favourable" signal) = 3,150 / 4,800 ≈ **65.6%**
> "Unfavourable" signal: 0.70 × 5,500 = 3,850 correct; 0.30 × 4,500 = 1,350 false. Total "unfavourable" signals: 5,200.
> P(favourable | "unfavourable" signal) = 1,350 / 5,200 ≈ **26.0%**
>
> (d) Given a "favourable" signal, should the retailer expand? Calculate the EMV. Given an "unfavourable" signal, should the retailer expand? Calculate the EMV.
>
> *Solution:*
> EMV(Expand | "favourable") = 0.656 × 800,000 + 0.344 × (−300,000) = 524,800 − 103,200 = **€421,600.** Expand.
> EMV(Expand | "unfavourable") = 0.260 × 800,000 + 0.740 × (−300,000) = 208,000 − 222,000 = **−€14,000.** Do not expand.
>
> (e) Calculate the EVI (Expected Value of Imperfect Information). Is the €100,000 study worth commissioning?
>
> *Solution:*
> P("favourable" signal) = 4,800/10,000 = 0.48. P("unfavourable" signal) = 0.52.
> EMV with study = 0.48 × 421,600 + 0.52 × 0 = **€202,368.**
> EVI = 202,368 − 195,000 = **€7,368.** No — the study costs €100,000 but adds only €7,368 in expected value. Do not commission it.

*T7 — Diagnostic: find the decision tree error:*

> A junior analyst presents the following decision tree analysis to a marketing team. Identify all errors.
>
> *"We modelled the decision to launch a new product. We have two options: launch now or wait one year. If we launch now: P(success) = 0.60, payoff = €500,000; P(failure) = 0.40, payoff = −€200,000. EMV = 0.60 × 500,000 + 0.40 × 200,000 = 300,000 + 80,000 = €380,000.*
>
> *If we wait: P(success) = 0.70 (market conditions improve), payoff = €600,000; P(failure) = 0.30, payoff = −€150,000. EMV = 0.70 × 600,000 + 0.30 × 150,000 = 420,000 + 45,000 = €465,000.*
>
> *The waiting option has higher EMV (€465,000 > €380,000), so we recommend waiting."*
>
> (a) Identify the arithmetic error in the "launch now" calculation.
> (b) Identify the arithmetic error in the "wait" calculation.
> (c) After correcting both EMVs, does the recommendation change?
>
> *Correct solutions:*
> EMV(now) = 0.60 × 500,000 + 0.40 × (−200,000) = 300,000 − 80,000 = **€220,000**
> EMV(wait) = 0.70 × 600,000 + 0.30 × (−150,000) = 420,000 − 45,000 = **€375,000**
> Recommendation unchanged (wait has higher EMV), but the margin is €155,000, not €85,000.
>
> (d) The analyst did not account for the time value of money. If the "wait" payoffs occur one year later and the appropriate discount rate is 10%, what are the present values of each "wait" scenario?
> (e) The "wait" option assumes competitive conditions remain stable. Name two business events that might eliminate the advantage of waiting, and explain how you would model them in the tree.

---

## Answer Key

### T0 — Decision tree structure (umbrella)

Two decisions: **carry umbrella** / **leave umbrella at home.**
Two states of the world: **rain** (probability 0.30) / **no rain** (probability 0.70).

Four (decision, state) combinations and their values:
| Decision | State | Value |
|---|---|---|
| Carry umbrella | Rain | +10 |
| Carry umbrella | No rain | −1 |
| Leave at home | Rain | −5 |
| Leave at home | No rain | 0 |

The umbrella decision is the decision node (your choice); rain/no rain is the probability node (outside your control). These are the two fundamentally different elements in any decision tree.

---

### T1 — Food stall EMV (Berlin market)

**(a)** Net payoffs (revenue − €600 stall cost):
- Busy: €2,500 − €600 = **€1,900**
- Moderate: €1,100 − €600 = **€500**
- Quiet: €400 − €600 = **−€200**

**(b)** Decision tree: square decision node with two branches: "Launch" and "Not attend (€0)." From the "Launch" branch, a circle probability node with three branches: Busy (0.40/€1,900), Moderate (0.40/€500), Quiet (0.20/−€200).

**(c)** EMV(Launch) = 0.40 × 1,900 + 0.40 × 500 + 0.20 × (−200) = 760 + 200 − 40 = **€920.** Since €920 > €0, she should launch.

Common error: students subtract the stall cost from EMV rather than from each payoff first. The correct approach subtracts cost per scenario before multiplying by probabilities — because the cost is incurred whenever she launches, regardless of the outcome.

**(d)** With €900 stall cost: net payoffs become Busy = €1,600, Moderate = €200, Quiet = −€500. EMV = 0.40 × 1,600 + 0.40 × 200 + 0.20 × (−500) = 640 + 80 − 100 = **€620.** Still positive, so she should still launch — but the margin above the "do not attend" option has narrowed from €920 to €620.

---

### T2 — Pharmaceutical licensing (PrecisionTree interpretation)

**(a)** EMV(Continue trial) = 0.55 × €22M + 0.30 × €7M + 0.15 × (−€3M) = €12.1M + €2.1M − €0.45M = **€13.75M.**

**(b)** EMV(Continue) − EMV(License now) = €13.75M − €8.4M = **€5.35M.** Continue trial has higher EMV by €5.35M.

**(c)** The CEO is not wrong — she is making a utility-based decision rather than an EMV-based one. EMV maximisation assumes the decision-maker is risk-neutral (values money linearly). A risk-averse firm, or one in a fragile financial position, rationally prefers a certain €8.4M over a risky €13.75M in expected value if the −€3M outcome (15% probability) would cause disproportionate harm. The CEO's preference reflects utility maximisation, not irrational behaviour. The decision depends on the company's risk tolerance, current financial health, and whether this is a repeated or one-off decision.

**(d)** The correct statement: "The model tells us that the strategy with the highest expected (average) monetary value is to continue the trial. It says nothing about what will actually happen in this specific trial." The model cannot predict whether this trial will succeed — it can only compute the probability-weighted average across all possible outcomes. Misreading the TRUE branch as a prediction of success confuses the optimal *strategy* with a *prediction* of outcome.

---

### T3 — Bayesian updating (market research firm)

**(a)** Frequency table for 10,000 launches (prior: 35% succeed, 65% fail):

| | Firm predicts "success" | Firm predicts "failure" | Total |
|---|---|---|---|
| Product succeeds | 0.75 × 3,500 = **2,625** | 0.25 × 3,500 = **875** | 3,500 |
| Product fails | 0.20 × 6,500 = **1,300** | 0.80 × 6,500 = **5,200** | 6,500 |
| **Total** | **3,925** | **6,075** | 10,000 |

**(b)** P(success | firm predicts "success") = 2,625 / 3,925 ≈ **66.9%.** Up from the prior of 35%.

**(c)** The firm's "success" prediction updates the prior from 35% to 66.9% — almost doubling the assessed probability of success. The report provides meaningful information: it more than halves the uncertainty in the "failure" direction.

**(d)** Without the report:
- EMV(Launch) = 0.35 × €500,000 + 0.65 × (−€200,000) = €175,000 − €130,000 = **€45,000.** Launch (positive EMV).

With a "success" prediction (posterior = 66.9%):
- EMV(Launch | "success") = 0.669 × €500,000 + 0.331 × (−€200,000) = €334,500 − €66,200 = **€268,300.** Launch.

With a "failure" prediction (posterior from table: P(success | "failure") = 875/6,075 ≈ 14.4%):
- EMV(Launch | "failure") = 0.144 × €500,000 + 0.856 × (−€200,000) = €72,000 − €171,200 = **−€99,200.** Do not launch.

EVI = expected payoff with the report − expected payoff without the report.
P("success" signal) = 3,925/10,000 = 0.3925. P("failure" signal) = 0.6075.
Expected payoff with report = 0.3925 × €268,300 + 0.6075 × €0 (best action after "failure" is not to launch) = **€105,313.**
EVI = €105,313 − €45,000 = **€60,313.** Since EVI (€60,313) > report cost (€50,000), the report is worth buying.

---

### T4 — Boundary case: extreme probability (oil drilling)

**(a)** EMV(Drill | p = 0.20) = 0.20 × €13M + 0.80 × (−€2M) = €2.6M − €1.6M = **€1.0M > 0.** Drill.

**(b)** Break-even: p × 13M + (1−p) × (−2M) = 0 → 15M × p = 2M → **p* ≈ 13.3%.** The company should drill whenever the assessed probability of finding oil exceeds 13.3%.

**(c)** Frequency table (10,000 sites, p = 0.20): Oil present: 2,000. No oil: 8,000.
Survey predicts "oil": 0.85 × 2,000 = 1,700 true positives; 0.10 × 8,000 = 800 false positives. Total: 2,500.
P(oil | survey says "oil") = 1,700 / 2,500 = **68%.**

**(d)** EMV(Drill | positive survey) = 0.68 × €13M + 0.32 × (−€2M) = €8.84M − €0.64M = **€8.2M.** P(positive signal) = 2,500/10,000 = 0.25. P(negative signal) = 0.75.
Expected payoff from buying survey = 0.25 × €8.2M + 0.75 × €0 − €0.3M (survey cost) = €2.05M − €0.3M = **€1.75M.** Without survey: €1.0M. Survey increases expected payoff by €0.75M — yes, it is worth buying.

**(e)** Indifference: 0.25 × €8.2M − survey cost = €1.0M (no survey). So survey cost = €2.05M − €1.0M = **€1.05M.** At any cost below €1.05M, the survey adds expected value and is worth commissioning.

---

### T5 — Risk aversion vs EMV (product strategies)

**(a)** EV(X) = 0.60 × €6M + 0.40 × (−€1.0M) = €3.6M − €0.4M = **€3.2M.** EV(Y) = 0.90 × €3.2M + 0.10 × (−€0.2M) = €2.88M − €0.02M = **€2.86M.** Strategy X has higher EMV by ≈ €0.34M.

**(b)** The covenant constraint transforms the analysis: Strategy X has a 40% probability of a −€1.0M loss, which exceeds the €0.8M maximum survivable loss. A Strategy X loss could trigger covenant breach — a qualitatively catastrophic outcome (forced asset sale, debt renegotiation, reputational damage) that is not captured in a linear EMV calculation. The CFO's constraint is not irrational: it reflects the asymmetric cost of a breach versus the marginal value of higher expected earnings.

**(c)** P(positive return | X) = 60% (the 60% probability of €6M). P(positive return | Y) = 90% (the 90% probability of €3.2M). If the board wants to maximise the probability of at least breaking even (any positive payoff), Y is clearly preferable.

**(d)** The recommendation depends on who is receiving it. For a risk-neutral investor making this decision repeatedly: Strategy X. For a risk-averse firm near a financial constraint, or for a single non-repeatable decision: likely Strategy Y. The answer is not universal — it depends on the firm's risk tolerance, financial position, and whether this is a recurring or one-off decision.

**(e)** The decision tree computes the EMV — the probability-weighted average monetary outcome — and identifies the highest-EMV option. It leaves to human judgment: (i) whether the firm is risk-neutral or risk-averse; (ii) the relevance of non-monetary outcomes (reputational effects, strategic positioning, employee morale); (iii) whether the probabilities themselves are well-calibrated; and (iv) whether the stated payoffs capture all relevant costs. The tree is a decision support tool, not a decision-making oracle.

---

### T6 — EVPI and EVI (market expansion)

**(a)** EMV(Expand) = 0.45 × €800,000 + 0.55 × (−€300,000) = €360,000 − €165,000 = **€195,000.** Since €195,000 > €0 (do not expand), the optimal decision without information is to expand.

**(b)** EVPI = EMV with perfect information − best EMV without information.
EMV with perfect information = 0.45 × €800,000 (expand if favourable) + 0.55 × €0 (don't expand if unfavourable) = €360,000.
EVPI = €360,000 − €195,000 = **€165,000.** This is the maximum amount the retailer should pay for any information source. The €100,000 study charges less than this ceiling — but it's imperfect, so we need EVI.

**(c)** Frequency table (10,000 scenarios): Favourable: 4,500. Unfavourable: 5,500.
"Favourable" signal: 0.70 × 4,500 = 3,150 true; 0.30 × 5,500 = 1,650 false. Total: 4,800.
P(favourable | "favourable" signal) = 3,150/4,800 ≈ **65.6%.**
"Unfavourable" signal: 0.70 × 5,500 = 3,850 true; 0.30 × 4,500 = 1,350 false. Total: 5,200.
P(favourable | "unfavourable" signal) = 1,350/5,200 ≈ **26.0%.**

**(d)** EMV(Expand | "favourable") = 0.656 × €800,000 + 0.344 × (−€300,000) = €524,800 − €103,200 = **€421,600.** → Expand.
EMV(Expand | "unfavourable") = 0.260 × €800,000 + 0.740 × (−€300,000) = €208,000 − €222,000 = **−€14,000.** → Do not expand.

**(e)** P("favourable") = 4,800/10,000 = 0.48. P("unfavourable") = 0.52.
EMV with study = 0.48 × €421,600 + 0.52 × €0 = **€202,368.**
EVI = €202,368 − €195,000 = **€7,368.** The study costs €100,000 but adds only €7,368 in expected value. **Do not commission the study.** The 70% accuracy rate is too low to justify the price — the study barely changes the decision (expand is optimal before and after a "favourable" signal; the only case where it changes the decision is after an "unfavourable" signal, but this occurs 52% of the time at an expected saving of €14,000 per occurrence, which is not enough to cover the €100,000 fee).

---

### T7 — Decision tree diagnostic (find the errors)

**(a)** Arithmetic error in "launch now": the analyst used +€200,000 (positive) for the failure payoff instead of −€200,000 (negative). Correct calculation: 0.60 × €500,000 + 0.40 × (−€200,000) = €300,000 − €80,000 = **€220,000**, not €380,000.

**(b)** Arithmetic error in "wait": the analyst used +€150,000 (positive) for the failure payoff instead of −€150,000 (negative). Correct: 0.70 × €600,000 + 0.30 × (−€150,000) = €420,000 − €45,000 = **€375,000**, not €465,000.

**(c)** Corrected recommendation: EMV(wait) = €375,000 vs EMV(now) = €220,000. The recommendation to wait is unchanged — but the margin is €155,000, not €85,000. Both errors happened to preserve the direction of the recommendation by coincidence, but reported the margin incorrectly.

**(d)** Present values of "wait" payoffs at 10% discount rate (one year later): PV(success) = €600,000 / 1.10 ≈ **€545,455.** PV(failure) = −€150,000 / 1.10 ≈ **−€136,364.** Discounted EMV(wait) = 0.70 × €545,455 + 0.30 × (−€136,364) = €381,818 − €40,909 = **€340,909.** Discounted EMV(wait) (€340,909) is still higher than EMV(now) (€220,000), so the recommendation doesn't change — but the margin shrinks slightly when time value is accounted for.

**(e)** Two business events that could eliminate the waiting advantage: (i) **Competitor entry:** a rival launches a comparable product during the 12-month wait, reducing the addressable market and the €600,000 upside — model this as an additional probability node after the "wait" branch: P(competitor enters) reduces the success payoff. (ii) **Technology shift:** the product becomes obsolete before launch (e.g., a new platform or regulatory change renders the product irrelevant) — model as a third outcome ("market disappears") with payoff −€0 (or a sunk cost) and a probability to estimate from industry dynamics.

---

**Pre-class submission (due 11:59pm the night before class):**

Using your open-data dataset (from a country other than your own), identify one binary decision your dataset's context suggests (e.g., "Should the city government invest in a new cycling lane?"). Submit:

1. The decision and its two branches
2. At least two uncertain outcomes you would include at the probability node, with rough probability estimates and your reasoning for those numbers
3. One question you cannot answer from the data alone (e.g., you need a cost figure, a probability you cannot observe)

This is not graded for correctness — it is scaffolding for the in-class pair activity.

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mentimeter quiz — 9 questions, displayed one at a time, 45 seconds each.**

Students respond on phones/laptops. Instructor watches live bar chart; pauses if one wrong answer dominates.

---

**Q1 (Easy — recall).** In a decision tree, what shape represents a decision node?

A) Circle
B) Triangle
C) Square ← correct
D) Diamond

*Instructor note: If >20% choose circle, briefly re-draw both shapes on the whiteboard before continuing.*

---

**Q2 (Easy — recall).** What does the folding-back procedure do at a probability node?

A) Takes the maximum of the possible payoffs
B) Takes the minimum of the possible payoffs
C) Takes the probability-weighted average (EMV) of the payoffs ← correct
D) Takes the most likely payoff only

---

**Q3 (Easy — recall).** In the Acme example from the textbook, the probability of a "Great" market scenario is 0.45. If the net revenue in this scenario is €10.8M, what is this scenario's contribution to the EMV?

A) €10.8M
B) €4.86M ← correct (0.45 × 10.8)
C) €0.45M
D) €24M

---

**Q4 (Easy — recall).** Which of the following best describes the EMV criterion?

A) Choose the decision with the highest guaranteed minimum payoff
B) Choose the decision with the highest probability-weighted average payoff ← correct
C) Choose the decision with the best worst-case outcome
D) Choose the decision that a risk-averse manager would prefer

---

**Q5 (Easy — recall).** In Bayes' rule, what are "prior probabilities"?

A) Probabilities calculated after seeing new information
B) Probabilities that are always 0.5 by default
C) Probabilities assigned before new information is received ← correct
D) Probabilities derived from a frequency table only

---

**Q6 (Easy — recall).** EVPI stands for:

A) Expected Variance of Posterior Information
B) Expected Value of Perfect Information ← correct
C) Estimated Value of Predicted Inputs
D) Exact Value of Predicted Intervals

---

**Q7 (Medium — application).** A decision tree has two branches: "Launch" (EMV = €200K) and "Wait" (certain payoff = €150K). With perfect information you would Launch when the market is good (p = 0.60, payoff €400K) and Wait when it is bad (p = 0.40, payoff €150K). What is the EVPI?

A) €400K
B) €100K ← correct
C) €240K
D) €40K

*Instructor note: EMV with perfect information = 0.60 × 400K + 0.40 × 150K = €300K; best EMV without information = €200K (Launch); EVPI = €300K − €200K = €100K. Distractor (d) €40K is the classic error — forgetting that in the bad state the best action under perfect information is still the certain €150K Wait, not €0.*

---

**Q8 (Medium — application).** A market research firm gives a "positive" signal. Prior P(success)=0.40. The firm correctly identifies successes 80% of the time and correctly identifies failures 70% of the time. Using Bayes' rule (frequency table approach for 1,000 cases): how many true successes receive a positive signal?

A) 400
B) 320 ← correct (400 × 0.80 = 320)
C) 280
D) 120

*Instructor note: This is a building block. Use the board if half the class is wrong — it sets up the Bayesian discussion in Part 3.*

---

**Q9 (Hard — conceptual).** A medical test for a rare disease (prevalence 1%) has sensitivity 95% (correctly identifies disease) and specificity 90% (correctly identifies no disease). A patient tests positive. Which statement is correct?

A) There is a 95% chance the patient has the disease
B) There is approximately a 8.7% chance the patient has the disease ← correct (base-rate neglect trap)
C) There is a 90% chance the patient has the disease
D) The test result is meaningless because the disease is rare

*Instructor note: This is the Joe's disease example from the textbook restated. Most students will choose A. Do NOT reveal the answer yet — let the tension sit. Return to it in Part 3 as the error autopsy anchor.*

---

**Instructor response protocol:**

- Q1–Q6: If any answer has >25% wrong responses, spend 60 seconds re-explaining the concept before moving on.
- Q7–Q8: Work through on the board if fewer than 60% correct.
- Q9: Do not explain yet. Say: "Hold this in mind — we will return to it."

---

### Part 2 — Tutorial Review (15 minutes + 10-minute buffer)

**Structure:** Students work in groups of 3–4. Each group gets a different starting point.

- Group A: T1(c) — the folding-back step only. Check their EMV arithmetic.
- Group B: T2(a) — verify the pharmaceutical EMV by hand.
- Group C: T3(b) — build the frequency table and derive the posterior.

After 8 minutes, one spokesperson from each group writes their answer on the whiteboard section assigned to them. The instructor runs a brief gallery walk (3 minutes), pointing out one correct insight and one common error per group. Final 4 minutes: any question from T1–T3 that students flagged in their pre-class submission.

**Common errors to watch for:**

- Using gross revenue instead of net payoff (forgetting to subtract costs)
- Multiplying probabilities incorrectly in the frequency table (e.g., multiplying column proportions rather than row proportions)
- Confusing P(signal|outcome) with P(outcome|signal) — the classic Bayesian inversion error

---

### Part 3 — Pair Work: Error Autopsy (25 minutes)

**Setup:** Students work in pairs. One student plays the **Analyst** who built the original decision model; the other plays the **Sceptic** who must find the flaw. Roles swap at the 12-minute mark.

**The two cases (one per pair, alternating around the room):**

**Case A — Medical Testing Base-Rate Neglect**

A hospital introduces mandatory screening for a disease affecting 1% of the population. The test has 95% sensitivity and 90% specificity. The hospital's communications team announces: "If you test positive, there is a 95% chance you have the disease." A decision tree is used to model whether to start aggressive treatment immediately vs wait for a confirmatory test. The tree uses P(disease|positive) = 0.95 as an input.

*Task:*
1. The Analyst explains what the hospital's decision tree looks like and why P=0.95 seems reasonable to a non-statistician.
2. The Sceptic constructs the frequency table (out of 10,000 people) and calculates the correct P(disease|positive). State the correct posterior.
3. Together: how does this change the decision tree? Would the optimal strategy (treat immediately vs wait) change? What is the cost of the error?
4. **Three-output deliverable:** (i) the corrected probability, (ii) a one-sentence explanation of what went wrong suitable for a hospital administrator, (iii) a recommendation for how the decision tree should be built to avoid this error in future.

**Case B — Insurance Pricing Mispricing**

An insurer prices flood insurance using historical flood data from 1950–2000. The model assumes P(major flood in any given year) = 0.02. A decision tree for pricing shows the EMV suggests charging €800 per policy. After Hurricane-level flooding events in 2002, 2010, and 2017, the insurer faces catastrophic losses. A post-mortem shows the actual probability in the modern climate era is closer to 0.08.

*Task:*
1. The Analyst defends the original model: the historical data showed 1 major flood in 50 years, so 0.02 was reasonable. What is defensible about this reasoning?
2. The Sceptic shows how the premium changes if P(major flood) = 0.08, assuming the claim payout is €40,000 and operating cost is €200. Recalculate the fair premium (approximately EMV of claims + cost margin).
3. Together: what type of data or reasoning would have produced a better probability estimate? How should sensitivity analysis have been used before pricing?
4. **Three-output deliverable:** (i) the corrected premium estimate, (ii) a one-sentence explanation of the error, (iii) one concrete method for stress-testing the probability assumption.

**Role-swap at 12 minutes:** The Sceptic becomes the Analyst defending a corrected version; the Analyst must now challenge whether the correction goes far enough.

---

### Part 4 — Peer Discussion (20 minutes)

**Format:** Each pair presents their three-output deliverable (~2.5 minutes per pair, strict timekeeping). The dataset owner — or in this case the pair who built the correction — responds first to any challenge.

**Instructor facilitation questions (to keep discussion analytical rather than descriptive):**

- "What would have to be true about the probabilities for the original decision to have been correct?"
- "Is this a data problem or a model problem — or both?"
- "What is the cost of being wrong in this direction versus the other direction?"

**Bring back Q9 from Mentimeter here.** After the Case A pairs have presented, return to the Mentimeter bar chart showing how many students said 95%. Ask the class: "How many of us would have made the same mistake as the hospital's communications team? Raise your hands." This is not punitive — it establishes that base-rate neglect is a documented, widespread cognitive bias (cite Kahneman & Tversky, 1972), not a personal failing.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop on the core tension:** "The decision tree is a rational framework — but it is only as good as the numbers you put in it. We have seen two real-world cases today where the probabilities were wrong, and the consequences were serious. This is not a reason to distrust decision trees; it is a reason to take probability estimation and Bayes' rule seriously."

**Synthesise the three key ideas:**

1. EMV maximisation is the right criterion for repeated decisions — but a single, high-stakes decision may warrant risk aversion (connect to utility functions in Section 6.6).
2. Bayes' rule is not just a formula — it is a correction for the natural human tendency to ignore base rates.
3. EVPI tells you the theoretical ceiling on the value of information; EVI tells you what imperfect information is actually worth. If a research firm charges more than EVI, don't buy the report.

**Reflective question (students write one sentence on paper or a sticky note):**
"Name one decision in your own dataset context where you think the probability estimates would be hardest to get right. Why?"

**Bridge-forward question:**
"Next week we study sampling distributions. Before you can put a probability into a decision tree, you often have to estimate it from data. How confident should we be in a probability estimated from a sample of 50 observations? We will build the tools to answer that question."

---

## After Class (~30 minutes)

**LMS reflection post — LinkedIn/professional format:**

Write a post of 150–200 words (as if publishing on LinkedIn) responding to the following prompt:

*"A major business decision — a product launch, a market entry, an insurance pricing model — failed because the decision-makers used the wrong probability. Drawing on this week's session on decision trees and Bayes' rule, what is the single most important safeguard you would build into any decision analysis process? Justify your choice."*

Requirements:
- Write in first person, professional but accessible tone
- Include at least one specific reference to a concept from the session (EMV, EVPI, Bayes' rule, base-rate neglect, etc.)
- End with a question addressed to your professional network
- Submit to the LMS discussion board before the next session; respond substantively to at least one classmate's post

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Pre-class worked example with explicit critique step | Ausubel (1968): new knowledge anchors to existing schemas; the critique step prevents inert knowledge by forcing students to interrogate assumptions before class |
| Mentimeter Q9 left unresolved until Part 3 | Bjork (1994) desirable difficulties: productive confusion about the correct posterior probability creates a retrieval hook that is resolved during the error autopsy |
| Error autopsy as primary seminar format | Kalyuga et al. (2003) expertise reversal: students at Level 5 benefit from evaluating flawed worked examples rather than constructing from scratch; errors are more cognitively engaging than correct cases |
| Analyst/Sceptic role structure with role swap | Vygotsky (1978) ZPD: structured controversy places students at the edge of their current competence; the swap forces them to defend a position they just attacked, deepening understanding |
| Frequency table approach to Bayes' rule | Gigerenzer & Hoffrage (1995): natural frequencies reduce cognitive load vs conditional probability notation; students at this level find the table construction concrete and verifiable |
| Return to Q9 bar chart during peer discussion | Black & Wiliam (1998) formative assessment: making the class's prior misconception visible in aggregate, then correcting it publicly, is more memorable than private correction |
| LMS post in LinkedIn format | Authentic task design: professional-register writing activates transfer of learning to workplace contexts; peer response requirement extends the spacing effect (Cepeda et al., 2006) beyond the classroom |
| Bridge-forward question linking to Week 11 | Spacing effect (Cepeda et al., 2006): explicitly flagging the connection to next week's topic primes retrieval at the next session |
| Cultural knowledge asymmetry in dataset selection | Vygotsky (1978): students choosing datasets from unfamiliar countries creates genuine peer expertise gaps; the student from Singapore genuinely knows more about Singapore datasets than their German classmate |
| EVPI vs EVI distinction in T3 | Bloom's Evaluate: distinguishing the theoretical ceiling from the practical value of imperfect information requires genuine evaluative reasoning, not just formula application |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Part 1: Mentimeter retrieval check | 10 min | 9 questions; pause if >25% wrong on Q1–6 |
| Part 2: Tutorial review (group + gallery) | 15 min | Groups A/B/C on different problems; 8 min work, 3 min gallery, 4 min Q&A |
| Buffer (tutorial overflow / admin) | 10 min | Use for any Q3 Bayesian step that needs board work |
| Part 3: Pair work — error autopsy | 25 min | 12 min each role; strict swap at halfway |
| Part 4: Peer discussion | 20 min | ~2.5 min per pair; return to Q9 bar chart |
| Part 5: Instructor debrief | 10 min | Close loop, reflective question, bridge forward |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

1. **Probability calibration is a skill, not a fact.** Students can learn to apply Bayes' rule mechanically without developing any intuition for whether a given probability is reasonable. The error autopsy addresses this by asking students to evaluate probability inputs, not just calculate outputs — but the instructor must resist the urge to give students "the right probability" and instead model the process of interrogating where numbers come from.

2. **The Analyst/Sceptic role structure can produce shallow debate.** If students read their roles as "defend the model" vs "attack the model," the discussion stays at the surface level of arithmetic errors rather than the deeper level of probability elicitation failures. The instructor should explicitly prime students to ask "where did this probability come from?" as the Sceptic's central question, not "is the arithmetic right?"

3. **Cultural diversity creates uneven knowledge of base rates.** The medical testing example works on a universal disease, but the insurance example uses European flood data. Students from Singapore, Seoul, or São Paulo may have sharply different intuitions about what "plausible" flood probabilities look like. This is a feature, not a bug — but the instructor must surface these differences explicitly rather than letting one dominant cultural frame (European or North American) set the baseline.

4. **Risk aversion vs EMV maximisation is philosophically contentious.** The textbook presents utility functions as the "correct" way to handle risk aversion, but some students will argue that a rational CEO who takes the certain payoff is simply making a different (defensible) choice, not an inferior one. This tension is genuine and the instructor should not resolve it too quickly. The goal is for students to understand that EMV maximisation is optimal for repeated decisions under specific assumptions, and that real decisions often violate those assumptions.

5. **PrecisionTree is not available in pre-class work.** Students can read about PrecisionTree and watch tutorial videos, but they cannot build trees in the add-in until the computer lab sessions. This means the in-class session must bridge from hand-drawn tree intuition to software output interpretation. Tutorial T2 is designed to support this — students interpret a PrecisionTree screenshot rather than build from scratch — but some students will find software output intimidating without hands-on experience.

---

## References

Albright, S. C., & Winston, W. L. (2019). *Business analytics: Data analysis and decision making* (6th ed.). Cengage Learning.

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives*. Longman.

Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart & Winston.

Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74.

Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380.

Farmus, L., Arpin-Cribbie, C. A., & Cribbie, R. A. (2020). The flipped classroom in introductory statistics: Early evidence from a systematic review and meta-analysis. *Journal of Statistics Education, 28*(3), 316–325.

Gigerenzer, G., & Hoffrage, U. (1995). How to improve Bayesian reasoning without instruction: Frequency formats. *Psychological Review, 102*(4), 684–704.

Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. *Cognitive Psychology, 3*(3), 430–454.

Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31.

Lovett, M. C., & Greenhouse, J. B. (2000). Applying cognitive theory to statistics instruction. *The American Statistician, 54*(3), 196–206.

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255.

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapter 6

- **The "skip §6-7 (simulation approach)" instruction is wrong on both counts.** Chapter 6's sections are: 6-1 Introduction, 6-2 Elements of Decision Analysis, 6-3 One-Stage Decision Problems (p. 232), 6-4 The PrecisionTree Add-In (p. 236), 6-5 Multistage Decision Problems (p. 239), 6-6 The Role of Risk Aversion (p. 257), 6-7 **Conclusion** (p. 264). There is no simulation section to skip — and simulation is Week 18 in the arc, not "Week 14" (regression). Fix the note to: "read 6-1 through 6-6; 6-4 (PrecisionTree) may be skimmed — see software note below."
- The reading correctly lands on 6-5 for Bayes' rule — worth noting this is where A&W formally treat Bayesian revision (Week 4's supplement flagged that Chapter 4 doesn't), so this session is the textbook's actual Bayes anchor. Frame it as such: "the formula you used informally in Week 4 gets its full treatment here."
- **§6-6 is read but under-used.** Risk aversion carries T2(c) and all of T5, yet utility functions, exponential utility, and certainty equivalents (6-6a–c) never get a computation. T8 below fixes this with one question — and certainty equivalents give T5(d) a *quantitative* answer instead of a rhetorical one.
- **The PrecisionTree dependency needs a decision.** T2 interprets PrecisionTree output (fine — interpretation needs no licence), but the optional video and Design Challenge 5's promised "computer lab sessions" assume Palisade software the course never schedules and Forward may not licence. *Options:* (a) commit to spreadsheet-built trees (a data table gives one-way sensitivity — A&W's own SolverTable idea from Ch13); (b) a 20-line Python folding-back function in Week 18's lab; (c) drop the references. Any is fine; a dangling dependency isn't.

## 2. Extended Question Bank (with answers)

**T8 — Certainty equivalent (uses §6-6, closes the T2(c) loop):**

> Return to T2. Model the firm's risk aversion with exponential utility U(x) = 1 − e^(−x/R), risk tolerance R = €10M.
>
> (a) Compute the certainty equivalent (CE) of "Continue trial" (outcomes €22M / €7M / −€3M with p = 0.55/0.30/0.15). Use CE = −R·ln(E[e^(−x/R)]).
> (b) The partner offers a certain €8.4M. Given (a), does a firm with R = €10M license or continue?
> (c) The CEO chooses the certain €8.4M anyway. What does that reveal about her implied risk tolerance?
>
> **Answers:** (a) E[e^(−x/R)] = 0.55e^(−2.2) + 0.30e^(−0.7) + 0.15e^(0.3) = 0.55(0.1108) + 0.30(0.4966) + 0.15(1.3499) = 0.0609 + 0.1490 + 0.2025 = 0.4124. CE = −10·ln(0.4124) ≈ **€8.86M.** (b) CE (8.86) > 8.4 → still continue the trial, but the €13.75M EMV gap has shrunk to €0.46M of *certainty-equivalent* advantage — risk aversion nearly erases it. (c) Her implied R is just below €10M (solving CE = 8.4 gives R ≈ €9M): she behaves like a firm that can absorb roughly €9M of risk. The payoff of this question: "risk-averse" stops being a vibe and becomes a measurable parameter — exactly what 6-6 is for.

**T9 — Risk profiles and dominance (deepens T5):**

> Using T5's two strategies, plot each strategy's risk profile (cumulative probability vs payoff).
>
> (a) Does either strategy first-order stochastically dominate the other?
> (b) A colleague says "Y is safer, so any risk-averse decision-maker prefers Y." Is that guaranteed?
>
> **Answers:** (a) No. X has the higher maximum (€6M vs €3.2M) but the worse minimum (−€1.5M vs −€0.2M); their cumulative curves cross, so neither dominates — which is *why* the choice requires a risk attitude at all. (b) Not guaranteed — "risk-averse" is a family of utility functions, not one; a mildly risk-averse decision-maker can still prefer X (per T8's machinery, a large-R firm does). Only if Y dominated first-order would *every* rational decision-maker prefer it. This kills the common student shortcut "risk-averse ⇒ pick the safe one."

**T10 — When information is worthless:**

> A firm faces a decision where "launch" has EMV €50k > 0 under the prior, and running the proposed market study cannot produce any posterior under which "don't launch" becomes optimal (even the worst signal leaves EMV(launch) > 0).
>
> (a) What is the EVI of this study, before doing any arithmetic? Why?
> (b) State the general principle connecting information value to decisions.
>
> **Answers:** (a) **Zero.** Information has value only if some possible signal would *change the optimal action*; if you'd launch regardless, the study buys nothing (except perhaps confidence — which EMV doesn't price). (b) EVI = expected gain from *acting differently* on some signals; no action change on any signal ⇒ EVI = 0; and always 0 ≤ EVI ≤ EVPI. This is the conceptual backbone behind T6's €7,368 — the study there *barely* changes any action, so its value is barely above zero.

*Additional quiz questions:*

- Q10: Which is always true? *(a) EVI > EVPI (b) EVI ≤ EVPI (c) EVI = EVPI when information is expensive (d) EVPI < 0 for risky decisions)* — **Answer: (b)** — imperfect information can never beat perfect information.
- Q11: If the same action is optimal in every state of the world, EVPI equals: *(a) the best payoff (b) the EMV (c) zero (d) cannot be determined)* — **Answer: (c)** — T10's principle in one line.
- Q12: A decision-maker's certainty equivalent for a gamble is below its EMV. They are: *(a) risk-seeking (b) risk-neutral (c) risk-averse (d) irrational)* — **Answer: (c).**

## 3. Alternative In-Class Activities (additional options)

**A. Calibration challenge (15 min, opener alternative).** Students write 90%-confidence intervals for ten estimable quantities (Berlin's population, the year the University of London was founded, Singapore-to-Lisbon distance…). Score how many of each student's intervals contain the truth: typically 4–6 of 10, not 9. Debrief: "these are the same brains that will supply the probabilities in your decision trees." The single most direct answer to Design Challenge 1 (calibration is a skill), and it feeds the Part 5 reflective question with personal evidence.

**B. Information auction (15 min, between Parts 3 and 4).** Run T4's oil case live: teams start with the prior, and the instructor auctions a sealed envelope containing the survey result. Teams bid real (points) currency; after the sale, reveal and let everyone re-decide. Teams that bid above the EVI overpaid by construction — the debrief computes what the envelope was actually worth. EVI stops being a formula and becomes a price they got wrong.

**C. Sensitivity tornado by hand (15 min, Part 3 extension).** Each pair takes T1 and varies one input ±25% (stall cost, P(busy), busy revenue), recording the EMV swing on a shared board sorted longest-bar-first — a handmade tornado chart. Connects to A&W's SolverTable idea (Ch13) and previews Week 18's sensitivity analysis; also answers Case B's "how should sensitivity analysis have been used?" with a method, not a moral.
 
**D. Build-the-tree relay (10 min, Part 2 alternative).** Groups of three at the whiteboard: person 1 may draw only nodes and branches, person 2 only probabilities/payoffs, person 3 only the folding-back numbers — for a scenario none has seen (a variant of T0's umbrella with a paid weather forecast, which sneaks in EVI). Same relay logic as Week 4's activity E; tests whether tree grammar is shared or private.

**E. Two-envelope regret debrief (5 min, Part 5 add-on).** After the reflective question, one quick provocation: "You chose Launch and the market was quiet — did you make a bad decision?" Establish the decision-vs-outcome distinction explicitly (good decision ≠ good outcome under uncertainty). It's the week's deepest transferable idea and currently only implicit in T2(d).

## 4. Critique of the Lesson Plan

**What works (keep):** T0's structure-before-notation entry; the EVPI→EVI arc across T4/T6 with a study that *isn't* worth buying (most textbooks rig it the other way); Q9 held unresolved until Part 4 (excellent use of the desirable-difficulty pattern); T7's find-the-error format; the explicit response protocol per quiz band.

**Problems, reasons, and fixes:**

1. **Q7 is broken twice and must be rewritten.** (i) The document still contains the drafting accident — the first option list with the author's mid-stream self-correction ("wait: recalculate…") sits above the corrected list. (ii) The "correct" €40K is itself wrong: with perfect information, when the market is bad the best action is the *certain €150K wait*, not €0. EVPI = [0.6 × 400K + 0.4 × 150K] − 200K = 300K − 200K = **€100K**. The €40K answer silently deletes the Wait option from the perfect-information world. *Fix:* clean the duplicate block; either re-key the answer to €100K, or (if €40K is wanted for simplicity) remove the Wait branch from the question.
2. **T5's problem statement ships a known-wrong number and asks students to absorb the inconsistency.** Stated EMV(X) = €3.2M; the outcomes given produce €3.0M, and the answer key instructs assessors to "accept values in the spirit of the stated outputs." *Fix:* set Strategy X's loss to −€1.0M — then 0.6 × 6M + 0.4 × (−1M) = **€3.2M exactly** — and nudge the covenant threshold in (b) to €0.8M so X's loss still breaches it. Two-number edit, restores a clean key.
3. **The reading note misdescribes the chapter (see §1).** No §6-7 simulation exists; the pointer says Week 14 where it means Week 18.
4. **Only two autopsy cases for six-plus pairs.** Part 4 will hear the same two corrections three times each, and by the third telling the room is done listening. *Fix:* keep A and B but issue each pair different parameters (prevalence 0.5%/1%/2% for Case A; flood probability 0.05/0.08/0.12 for Case B) — same structure, different numbers, and Part 4 becomes a sensitivity analysis across pairs for free (pairs see how the *same error's cost* scales with the base rate).
5. **Week 4 overlap is unacknowledged.** T3, T4(c), and Case A re-run the Week 4 frequency-table machinery almost verbatim. Spaced retrieval is good design, but only if named — otherwise students experience it as the course repeating itself. *Fix:* one sentence in the pre-work ("you built these tables in Week 4 for tests and fraud; this week they price *decisions*") and push the new difficulty into EVI, which genuinely is new.
6. **Part 4 arithmetic, fourth week running:** 6–7 pairs × 2.5 min + the Q9 revisit > 20 min. With fix 4 (parameter variants) presentations can compress to one number per pair on a shared board plus discussion — 12 minutes total, leaving room for the Q9 moment.
7. **LinkedIn post prompt asks for "a major business decision that failed because of a wrong probability" but neither taught case is a published real event** (the insurance case is stylised, medical case generic). Students will invent or hand-wave examples. *Fix:* attach two genuinely documented anchors to choose from (e.g. the 1986 Challenger launch-risk estimates, or UK PPI/flood-repricing coverage), or explicitly permit the in-class cases as the subject.
