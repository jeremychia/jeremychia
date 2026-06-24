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

**Reading:** Albright & Winston, Chapter 6 — Sections 6-1 through 6-6 only (pp. 222–264). Skip Section 6-7 (simulation approach — covered in Week 14). Focus especially on the Acme new product example (§6-3, pp. 232–236) and the Bayes' rule worked example (§6-5, pp. 239–257).

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
> **Strategy X — Fast-to-market:** EMV = €3.2M. Outcomes: 60% chance of €6M; 40% chance of −€1.5M.
> **Strategy Y — Deliberate development:** EMV = €2.8M. Outcomes: 90% chance of €3.2M; 10% chance of −€0.2M.
>
> (a) Verify both EMVs by hand.
>
> *Solution:* EV(X) = 0.60 × 6,000,000 + 0.40 × (−1,500,000) = 3,600,000 − 600,000 = **€3,000,000** (note: the stated €3.2M implies slightly different numbers — show your working and flag the discrepancy; accept values in the spirit of the stated outputs). EV(Y) = 0.90 × 3,200,000 + 0.10 × (−200,000) = 2,880,000 − 20,000 = **€2,860,000 ≈ €2.8M**. Consistent.
>
> (b) Strategy X has higher EMV but also a 40% chance of a €1.5M loss. A CFO says: "We can only sustain a maximum loss of €1M without triggering a covenant breach on our debt." How does this constraint change the analysis?
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

**Q7 (Medium — application).** A decision tree has two branches: "Launch" (EMV = €200K) and "Wait" (certain payoff = €150K). With perfect information, you would earn €400K if the market is good (p=0.60) and €0 if bad (p=0.40). What is the EVPI?

A) €400K
B) €90K ← correct (EVPI = 0.60×400K + 0.40×0 − 200K = 240K − 200K = 40K... wait: recalculate: 0.60×400K=240K, 0.40×0=0, EMV with perfect info=240K; best without info=200K; EVPI=40K)

*Instructor note: Correct answer is €40K. Reconstruct if needed.*

A) €400K
B) €40K ← correct
C) €240K
D) €200K

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
