# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 1: Decision-Making Under Uncertainty and Modelling
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Distinguish the three branches of analytics (descriptive, predictive, prescriptive) and identify which applies to a given business situation
- Classify sources of uncertainty as aleatory (irreducible) or epistemic (knowledge-based) and explain the implication of that distinction for modelling choices
- Evaluate a business model by articulating what it deliberately omits — and why that omission is a design choice, not a failure
- Critique a framing assumption in a real business decision by asking what type of model would help and what it would require

These map directly to the ST2187 course outcome of developing students who can *"identify limitations and possible misuse"* of quantitative approaches and who are *"more critical of advice given to them."*

These objectives operate at the **analysis and evaluation** levels of Bloom's Taxonomy (Anderson & Krathwohl, 2001) — requiring students not merely to recall definitions of modelling types but to judge which applies, and to identify what assumptions are hidden inside that choice.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 1 in full (pp. 1–15) — it is short and conceptual. Focus especially on:
- §1-2 Overview of the Book (pp. 4–9) — the methods and the software
- §1-3 Modeling and Models (pp. 10–15) — graphical, algebraic, and spreadsheet models, and §1-3d's Seven-Step Modeling Process, which is the skeleton of the worked example below

Note: the descriptive/predictive/prescriptive trichotomy and the aleatory/epistemic distinction used in this session go beyond the textbook — they are carried by the videos below and a one-page handout on the LMS. A&W frame the same territory as *data analysis* versus *decision making under uncertainty* (§1-2a). §1-2b (The Software) explains the book's tool choices; this course's Python/SQL track replaces them — the concepts transfer, the keystrokes don't. The tools are introduced properly in Weeks 6–9; reading tool instructions before you understand what problems they solve wastes preparation time.

*Rationale:* Chapter 1 is conceptual, not computational. The reading asks students to think about what analytics is for before asking them to do any. The pre-work load is intentionally lighter this week — students are orienting to the course, not yet processing dense technical material. This is consistent with Fischer et al. (2023), who recommend calibrating pre-work volume against the cognitive complexity of the in-class task, not the number of pages available.

**Videos (~20 minutes total):**
- [Descriptive, Predictive, & Prescriptive Analytics](https://www.youtube.com/watch?v=lxCaYg1G9fE) (~8 min) — covers the continuum of analytics types with business examples. *Active watching: at the point where the presenter distinguishes predictive from prescriptive analytics (around 4:00), pause and write in your own words: what is the key difference? Then resume. This distinction is the one students most often conflate in T1.*
- [The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) (~10 min, Veritasium) — covers the distinction between what we don't know (epistemic) and what is inherently random (aleatory) through the lens of updating beliefs with evidence. *Active watching: when Veritasium introduces the idea of updating beliefs with new information (around 3:00), pause and write one sentence: what changes when you get new evidence — the world, or your model of the world? This is the epistemic/aleatory distinction you need for T1(b).*

**Worked example (read this before attempting the tutorial problems):**

This walks through the kind of reasoning the session is built around. Read it carefully and annotate it — underline the step where the model's scope is defined, and circle the step where an omission is justified. You are looking for the *structure* of the reasoning chain so you can apply it yourself in T1–T3.

*This worked example is marked optional for students who already feel confident identifying model types, uncertainty types, and deliberate omissions from a business description. If you can write a sentence answering T1(a), (b), and (d) without reading the example, you don't need it. If any of those three felt unclear after the reading and videos, read this carefully before attempting the tutorials.* (On expertise reversal in pre-work design, see Kalyuga, Ayres, Chandler & Sweller, 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

> **Scenario:** A European airline needs to decide how many aircraft to schedule on a new Berlin–Lisbon route for the summer season. Demand is uncertain. The airline's planning team builds a model.
>
> **Step 1 — What kind of uncertainty is this?**
> Two types are present. *Aleatory:* actual passenger demand on any given flight will vary randomly — weather events, a football tournament, a public holiday in either city. No model eliminates this. *Epistemic:* the airline doesn't yet know how price-sensitive this route's passengers will be, or how full competitors' flights typically run. That uncertainty shrinks as data accumulates.
>
> **Step 2 — What does the model do?**
> The planning team builds a demand forecast based on comparable routes. It models average load factor as a function of ticket price, season, and day of the week. The model has three inputs (price, season, day) and one output (expected load factor). It ignores: fuel prices, ATC delays, competitor pricing responses, and passenger no-show rates.
>
> **Step 3 — What does the model give up — and why is that the right trade-off?**
> The model ignores fuel prices because the scheduling decision is made six months ahead, and a fuel price model would require an entirely separate forecasting chain with its own uncertainties. The team is making a *scheduling* decision, not a *pricing* decision — so fuel costs are excluded by design, not by oversight. The model ignores no-show rates because those affect overbooking policy (a separate decision made by a different team). Realism was sacrificed for tractability. The model is not trying to be the world — it is trying to answer one question, given what is known.
>
> **What you are looking for in your pre-class scenario:** the gap between what the model is designed to answer and what a decision-maker might ask it to answer. That gap is not a flaw in the model — it is a flaw in how the model is being used.

**Tutorial problems (submitted before class, reviewed in Part 2):**

These establish conceptual fluency — the prerequisite for the scenario-sorting work in Parts 3 and 4. Students bring written answers; two or three will present.

*T1 — Straightforward computation (no ambiguity):*

*The prescriptive vs predictive distinction you noted while watching the first video is exactly what T1(a) tests. The model-omission reasoning from the worked example maps directly onto T1(d).*

> A city government is trying to decide how to allocate its road maintenance budget across 50 districts for the coming year.
>
> (a) Identify whether this is primarily a descriptive, predictive, or prescriptive analytics problem. Explain in one sentence why.
> (b) What is the main source of uncertainty? Is it aleatory or epistemic? Explain the difference, and explain which applies here.
> (c) Name two inputs a model for this decision would need.
> (d) Name one thing a realistic model of this decision would have to leave out — and explain why leaving it out might still be acceptable.
> (e) The city government is told: "Our model says District 12 needs €200,000 of maintenance." A councillor responds: "But the model doesn't account for political pressure to favour districts in the upcoming election." Is this a critique of the model or the decision-maker? Explain.
> (f) The same model is then used to forecast how much the entire city's roads will deteriorate over the next five years. Is this the same type of analytics problem as (a)? What changes?
> (g) At what point does a model become so simplified that it is no longer useful? Who decides?

Parts (a)–(d) are definitional — students either know the vocabulary or they don't, and the quiz will surface this. Part (e) is the first point of genuine difficulty: the right answer is that the critique is about how the model is being *used*, not about the model itself. The model's omission of political dynamics may be correct — political pressure is not a road condition. Part (g) is the ethical question, with no single right answer.

*Self-check for T1(a)–(d):* T1(a): prescriptive — the government is deciding how to allocate, not just describing or predicting. T1(b): primarily epistemic — the government doesn't know current road condition data; with better surveys, this uncertainty shrinks. T1(c): examples include current condition scores per district, traffic volume, age of road surface. T1(d): any example of a second-order effect (political priorities, future land use changes) left out by design is correct. If your answers are roughly consistent with these, continue. If T1(a) felt unclear, re-read the worked example before attempting T2.

*T2 — Interpretation, not just computation:*

> You are advising a mid-sized retailer that wants to reduce overstock — goods that are ordered but don't sell, sitting in warehouse costing money. A consultant proposes a "predictive analytics solution." Another consultant proposes an "optimisation model."
>
> (a) What would a predictive analytics solution tell the retailer — and what decision would it support?
> (b) What would an optimisation model do — and what would it need to assume?
> (c) Can you use both? In what order, and why?
> (d) The retailer is a fashion company. New collections arrive twice a year. Demand for last season's items drops to near zero within weeks. Does this change your answer to (b)? How?

This problem asks students to reason from the business context to the model choice — not to recall definitions. Part (d) is where many students will realise that the uncertainty type affects the model choice: fashion demand has a discontinuity (a cliff, not a trend), which breaks the assumptions of most standard inventory models.

*T3 — Edge case that requires genuine thought:*

> In January 2025, the Chinese AI lab DeepSeek released a model (DeepSeek-R1) that matched the performance of OpenAI's o1 on standard benchmarks, reportedly trained at a fraction of the cost. Within 24 hours, Nvidia's share price fell approximately 17%, wiping roughly $600 billion from its market capitalisation — one of the largest single-day losses in US stock market history.
>
> Several analysts had been using prescriptive models to recommend holding or buying Nvidia stock, based on projections that AI training demand would continue to require massive GPU capacity.
>
> (a) What type of analytics were the Nvidia buy-recommendation models performing? What was their objective?
>
> (b) What did the DeepSeek release change about the assumptions those models were built on?
>
> (c) The models' inputs included: GPU shipment forecasts, hyperscaler capital expenditure plans, and historical AI compute demand growth rates. None of these inputs directly accounted for the possibility of a competitor achieving the same model performance at dramatically lower compute cost. Is the omission of this possibility a flaw in the model design, or an acceptable scope decision? Who should have decided?
>
> (d) A commentator said: "The models were accurate for the world that existed before January 20th. They failed because the world changed, not because the models were wrong." Do you agree? What does this imply about how prescriptive analytics models should be communicated to decision-makers?
>
> (e) OpenAI's benchmark score of 88% on the ARC-AGI reasoning test was widely reported as evidence of near-human reasoning. What does a benchmark score measure — and what does it not measure? Is "88% on ARC-AGI" a descriptive, predictive, or prescriptive output?

T3 uses a verified 2025 event (DeepSeek-R1 release, 20 January 2025; Nvidia market cap loss reported by multiple financial outlets including Bloomberg and FT). It surfaces the limits of the analytics framework before the course is a week old: the right answer to (d) is contested — some analysts would say the models failed to account for tail risk, others that model omissions were reasonable given available information. There is no single correct answer, which is the point. Students who arrived confident that "a model is wrong if it gives a bad recommendation" leave with a more careful view of the difference between model validity and model scope.

*T4 — Boundary case: model with zero data:*

> A city council wants to build a model to decide where to locate a new emergency ambulance depot. The city has never had an ambulance depot before and has no historical call-out data.
>
> (a) What type of analytics problem is this? Can it be prescriptive without any historical data to train on?
> (b) What inputs would the model need — and where would the numbers come from, if there is no local history?
> (c) A consultant proposes using data from a comparable city in another country. What assumptions does this introduce? What would make those assumptions defensible or indefensible?
> (d) The council is advised: "With no data, any model is just guesswork." Do you agree? What is the minimum information needed before a model is useful?
> (e) Is the uncertainty here primarily aleatory or epistemic? What does your answer imply about whether more data collection would help?

This question targets the edge case where models must be built without historical data — which is common in public policy, new markets, and novel products. Part (d) is the hardest: students who say "no model is better than a bad model" need to defend that claim against the alternative that no decision is also a decision, and it is made with even less information.

*T5 — Comparison: two models for the same decision:*

> A supermarket chain is deciding how much stock of fresh bread to order each morning. Two analysts propose different approaches:
>
> **Analyst A** proposes a predictive model: use the past 90 days of sales data, day-of-week effects, and weather forecasts to predict tomorrow's demand.
>
> **Analyst B** proposes a prescriptive model: define the objective (minimise waste + minimise stockouts, weighted by cost), model demand uncertainty, and solve for the optimal order quantity each day.
>
> (a) What is the fundamental difference between what the two models produce?
> (b) Can you use Analyst A's model as an input to Analyst B's model? If so, in what order?
> (c) Analyst A's model has R² = 0.78 on historical data. Analyst B's model optimises given a demand distribution. Which model requires more assumptions? Which model's output is more useful to the store manager — and does the answer depend on who the manager is?
> (d) A new store manager arrives and immediately orders twice the quantity that Analyst B's model recommends, because she "knows from experience that models underestimate demand near Christmas." In what sense is she right, and in what sense might she be wrong?
> (e) After three months, actual waste and stockout costs with Analyst B's model are lower than with the manager's manual overrides. What does this tell you about the model — and what doesn't it tell you?

*T6 — Diagnostic question: find the modelling error:*

> A ride-hailing company builds a model to predict surge pricing. The model's inputs are: number of ride requests in the last 5 minutes, number of available drivers in the last 5 minutes, and day of week. The model's output is a surge multiplier (1.0 = no surge, 2.0 = double price). The company reports: "Our model achieves 94% accuracy in predicting whether surge pricing will be applied."
>
> (a) What kind of model is this — descriptive, predictive, or prescriptive?
> (b) The company's 94% accuracy claim is measured against historical data. Identify one reason why 94% accuracy on historical data might be misleading about the model's true usefulness.
> (c) A driver says: "The model always predicts surge when there are fewer than 10 available drivers — it's not learning anything, it's just restating a threshold." Could this be true? How would you test it?
> (d) The model is used to automatically set prices without human review. Is this a modelling problem, a deployment problem, or a governance problem? Explain the distinction.
> (e) After the model is deployed, drivers start logging off the app when they see surge pricing increasing, expecting to log back on at a higher rate — which reduces the number of available drivers, causing the model to predict even higher surge. What fundamental problem does this create, and what does it imply for how the model's training data should be collected?

*T7 — Real-world translation: set up the problem from a business description:*

> You work for a national postal service. Management wants to reduce the cost of parcel sorting at their main distribution centre. Currently, sorting is done manually by staff who read addresses and route parcels to conveyor belts. The centre processes 50,000 parcels per day, with a 3% misrouting rate. Each misrouted parcel costs an additional €4.50 in correction costs.
>
> (a) Identify the decision management is actually trying to make. Is it "reduce misrouting" or something else? What is the objective?
> (b) What type of analytics would help most — and what would it produce as an output?
> (c) What inputs would a useful model need? List at least four. For each, state whether the input is currently available or would need to be collected.
> (d) Calculate the expected current annual cost of misrouting (assume 250 working days). Then calculate the cost at a 1% misrouting rate. This is the upper bound on what a perfect model is worth — what is this called?
> (e) A vendor proposes an AI-powered optical character recognition (OCR) system that promises "99% accuracy." What additional information would you ask for before accepting or rejecting this claim?

---

## Answer Key

### T1 — Road maintenance allocation

**(a)** **Prescriptive.** The government is deciding *how to allocate* a budget — the output is a recommendation (an allocation), not a description of what happened or a forecast of what will happen.

**(b)** **Primarily epistemic.** The government lacks reliable current condition data across all 50 districts. Better surveys would shrink this uncertainty. Aleatory uncertainty would be something irreducibly random (e.g. future weather damage) — the primary unknown here is knowledge-based and data-reducible.

**(c)** Any two reasonable inputs: current condition scores per district, traffic volume, age of road surface, historical repair frequency, cost of materials by region.

**(d)** Any second-order effect left out by design is acceptable — e.g. political priorities, future land-use changes, long-term population shifts. Leaving these out is acceptable because the model answers one narrow question (maintenance allocation), not the whole urban system.

**(e)** This is a critique of the **decision-maker**, not the model. Political pressure is not a road condition. A model that correctly excludes political factors to focus on infrastructure need is well-scoped. The councillor's critique reveals how the model is being *used*, not a flaw in how it was *designed*.

**(f)** The five-year deterioration question is **predictive**, not prescriptive. Part (a) asks "what *should* we do?" — prescriptive. The new question asks "what *will* happen?" — predictive. They are different analytics problems requiring different model types.

**(g)** No single right answer — this is an ethical question. The key principle: a model becomes too simplified when it can no longer answer the question it was built for. Who decides is ultimately the decision-maker, though the modeller has an obligation to state limitations clearly.

---

### T2 — Retailer overstock

**(a)** A predictive analytics solution forecasts demand by product/SKU — it tells the retailer what they expect to sell, supporting the decision of *how much to order*.

**(b)** An optimisation model defines an objective (minimise waste + stockout cost weighted by their costs), models demand uncertainty as a distribution, and solves for the optimal order quantity. It must *assume* a demand distribution and the relative costs of over- vs under-stocking.

**(c)** Yes — use both, in order. The predictive model produces the demand distribution; the prescriptive model takes that distribution as input to solve for the optimal order.

**(d)** Fashion demand has a **discontinuity** — last season's items drop to near-zero demand when the new collection launches. Standard inventory models assume smooth demand trends. The optimisation model needs to account for end-of-season obsolescence, not just mean demand.

---

### T3 — DeepSeek / Nvidia

**(a)** The Nvidia buy-recommendation models were performing **prescriptive analytics**: recommending an action (hold/buy stock) in service of an objective (maximise return). Some had a predictive layer (forecasting GPU demand), but the recommendation itself was prescriptive.

**(b)** DeepSeek's release invalidated the core assumption that AI training requires massive GPU compute. If the same model performance can be achieved at a fraction of the cost, projected Nvidia GPU demand is structurally lower than the models assumed. The training-cost relationship was broken.

**(c)** The omission is a **defensible scope decision** — but one that should have been communicated as a tail risk. Before January 2025 there was no public evidence of an imminent efficiency breakthrough. Who should have decided: the model builders should have included an explicit scope note — "this model does not account for structural shifts in AI compute efficiency."

**(d)** The commentator is partially right. The models were not wrong for the world they described — they accurately extrapolated historical trends under stable assumptions. But prescriptive models that ignore tail risks (technology disruption, regulatory change) are incomplete. Implication: prescriptive models should be communicated with explicit assumption statements, not as point recommendations.

**(e)** "88% on ARC-AGI" is a **descriptive** output — it describes performance on a defined test. A benchmark score measures performance on a specific set of problems under specific conditions. It does not measure general reasoning, real-world robustness, or capability outside the benchmark's domain.

---

### T4 — Ambulance depot with no data

**(a)** **Prescriptive** — the council must decide *where* to locate the depot. Yes, it can be prescriptive without historical data: you can build an optimisation model on structural data (population density, road network distances) without historical call records.

**(b)** Inputs needed: population density by area, road network distances and travel speeds, estimated incident locations (from demographic data), and response time targets. Numbers come from census data, mapping databases, and comparable-city studies.

**(c)** Using data from a comparable city assumes call patterns, demographics, road infrastructure, and emergency response norms are similar enough to apply. Defensible if cities are genuinely comparable in size, density, and infrastructure. Indefensible if the cities differ fundamentally in health system structure, emergency density, or road network.

**(d)** "No model without data is guesswork" is **false**. Even a structural optimisation model (locating a depot to minimise expected response distance given population density) is better than no process — because no decision is also a decision, made with even less structure. The minimum needed is a defensible estimate of likely demand locations and a response time objective.

**(e)** Primarily **epistemic** — the council lacks call-pattern knowledge that data collection would provide. More data collection *would* help. This contrasts with aleatory uncertainty (inherently random), which data cannot reduce.

---

### T5 — Supermarket bread ordering

**(a)** Analyst A produces a **demand forecast** (a number: expected tomorrow's demand). Analyst B produces an **optimal order quantity** (a decision). Forecast ≠ recommendation — they answer different questions.

**(b)** Use Analyst A first, then B. A's model produces the demand distribution that B's optimisation takes as input. Prescriptive models require predictive inputs.

**(c)** Analyst B's model requires more assumptions: a demand distribution, a cost structure (waste cost vs stockout cost), and an objective function. A's model needs only historical data and relationships. Which output is more useful depends on the manager's role: a manager making daily ordering decisions needs B's recommendation; one seeking to understand demand patterns may find A's forecast sufficient.

**(d)** She may be right that models underestimate Christmas demand if the seasonal effect wasn't fully captured in 90 days of data. She may be wrong if the model already captured that seasonality and she is double-counting it.

**(e)** Lower costs over three months confirm the model outperformed manual overrides in aggregate. It does **not** tell you: whether the model was correctly designed (the improvement could be partly coincidental), whether performance will hold next quarter, or how the model handles rare edge cases not yet encountered.

---

### T6 — Ride-hailing surge pricing

**(a)** **Predictive** — the model predicts whether surge will be applied based on current conditions. It forecasts a label; it doesn't produce a recommendation.

**(b)** 94% accuracy on historical data may be misleading because: (i) the historical data was itself generated by a threshold rule, so the model may simply be learning that threshold rather than a real pattern; (ii) overall accuracy masks performance on the rare cases where surge is applied — precision/recall matter more than accuracy when classes are imbalanced.

**(c)** The driver may be right. To test: check whether removing all inputs except "available drivers < 10" preserves nearly the same accuracy. If so, the other inputs add nothing.

**(d)** This is primarily a **governance problem**. Automated pricing without human review is a deployment and oversight decision, not a modelling error. A governance problem is a failure of the decision about how to use the model; a modelling problem would be a flaw in the model itself.

**(e)** This is a **feedback loop**: the model's output changes driver behaviour, which changes the model's inputs, which changes the output — making the historical training data invalid. The training data was collected in a world where drivers did not respond to surge signals; in deployment, they do. The model needs retraining on data that reflects driver behaviour *after* surge signals exist.

---

### T7 — Postal service sorting

**(a)** The true decision is **whether and how to automate parcel sorting** to reduce total cost. "Reduce misrouting" is a means, not the objective. The objective is cost minimisation (or equivalent margin improvement).

**(b)** A combination of **descriptive** (current misrouting cost) and **prescriptive** (what automation option minimises total cost). Output: a recommendation on whether to invest in automation and which type.

**(c)** Inputs: address legibility/OCR confidence by parcel type; current staff throughput and error rate by parcel category; equipment capital cost; correction cost per misrouted parcel. Most are trackable from current operations; capital cost requires vendor quotes.

**(d)** Current annual cost: 50,000 × 0.03 × €4.50 × 250 = **€1,687,500/year.** At 1% misrouting: 50,000 × 0.01 × €4.50 × 250 = **€562,500/year.** The savings ceiling (perfect sorting) is €1,687,500. This is the upper bound on what any sorting improvement is worth — sometimes called the **Value of Perfect Information** in this context.

**(e)** Additional questions before accepting "99% accuracy": On what test dataset — vendor-curated or independently validated? Accuracy across all parcel types and handwriting conditions, or only on clean labels? What is the false-positive and false-negative rate separately? What happens to rejected/uncertain parcels — manual re-sort? What accuracy level is required for the *overall system* misrouting rate to fall below a target?

---

**Pre-class submission (on the course portal):**

Students identify **three business decisions they have personally encountered or read about** — from their own country — and **one** they have encountered from a different country. For each, they answer:

1. What is the decision?
2. What type of analytics would most directly help with it (descriptive / predictive / prescriptive)?
3. What is the primary source of uncertainty — is it aleatory or epistemic?
4. What would a model for this decision deliberately leave out?

**Choose at least one example from a different country than your own.** With 40+ nationalities in the cohort, the scenario-sorting in Parts 3 and 4 is richer when students bring different business contexts — a logistics decision from São Paulo, a crop pricing decision from Singapore, a hiring decision from Lagos. The cultural and institutional context often determines what a model *can* leave out.

The cross-national constraint is intentional from Week 1: it signals that "business analytics" is not culturally neutral, and that the decisions models support are shaped by institutional context, data availability, and regulatory environment.

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

Questions run from straightforward to genuinely difficult. The easy questions confirm vocabulary and build momentum; the hard questions find where understanding stops. Run all nine — the spread of results across the difficulty gradient is more informative than any individual question.

**Easy — vocabulary and recall:**

- Q1: Which type of analytics answers the question "What happened?"
  *(a) Prescriptive  (b) Predictive  (c) Descriptive  (d) Inferential)*

- Q2: A hospital wants to forecast how many patients will arrive in the emergency department next Tuesday. Which type of analytics is this?
  *(a) Descriptive  (b) Prescriptive  (c) Predictive  (d) Diagnostic)*

- Q3: Which type of uncertainty CAN be reduced by gathering more information?
  *(a) Aleatory  (b) Epistemic  (c) Both  (d) Neither)*

- Q4: The modelling cycle begins with:
  *(a) Data collection  (b) Model building  (c) Problem formulation  (d) Sensitivity analysis)*

- Q5: Sensitivity analysis asks:
  *(a) How does the output change when inputs change?  (b) How sensitive is the data to measurement error?  (c) How sensitive is the model to its number of variables?  (d) How does model accuracy change with sample size?)*

- Q6: A company wants to determine the optimal price for a new product to maximise revenue. This is primarily:
  *(a) A descriptive analytics problem  (b) A predictive analytics problem  (c) A prescriptive analytics problem  (d) A data collection problem)*

Q6 is a mild trap. The answer is prescriptive — the question asks what *should* the company do (set the price). Students who conflate "predict demand at a given price" with "prescribe the optimal price" will answer predictive. The distinction matters: prescriptive analytics requires an objective function (maximise revenue) and a decision variable (price). This is worth 30 seconds of discussion if the room splits.

**Medium — application:**

- Q7: A logistics company builds a route-optimisation model. It assumes traffic is constant throughout the day and ignores school holidays. A manager uses it to plan Christmas Eve deliveries. What is the most likely source of model failure?
  *(a) The model ignores epistemic uncertainty about road conditions  (b) The model's assumptions are violated by the specific context  (c) Route optimisation is the wrong type of analytics for this decision  (d) The model needed more historical data)*

- Q8: A pharmaceutical company is deciding how much vaccine to manufacture for a new flu strain. The strain may mutate before the winter season. Is the mutation uncertainty primarily aleatory or epistemic?
  *(a) Aleatory — mutation is inherently random  (b) Epistemic — with better virology research, this uncertainty could be reduced  (c) Both — some mutation is random, but research could bound the likely range  (d) Neither — the company should not model this at all)*

**Hard — conceptual, requires the chapter's final insight:**

- Q9: A city council builds a model to decide where to locate three new schools over the next ten years. The model optimises for travel time from residential areas. After the schools are built, residential patterns shift because families move to be near the schools. What does this illustrate?
  *(a) The model should have used predictive rather than prescriptive analytics  (b) The model's objective function was miscalibrated  (c) The model's output changed the conditions its assumptions were based on — the model was not wrong, the world changed in response to it  (d) School location decisions should not be modelled)*

Q9 is the sharpest question in the set. It captures the feedback loop problem: a prescriptive model that changes the system it was designed to optimise. The "right" answer (c) is counterintuitive — most students will assume the model was simply wrong rather than recognising that the model succeeded in its terms, and that success produced a new epistemic uncertainty. This is the reflexivity problem in social systems modelling, and it appears throughout the course (economic models, demand forecasting, hiring algorithms).

**Instructor acts on results (5 minutes)**

The quiz is doing two distinct jobs and they call for different responses:

**Q1–Q6 are retrieval practice.** Their purpose is to strengthen retention by forcing recall — not to diagnose gaps. If most students answer correctly, move on immediately. Extended discussion of questions everyone got right wastes the retrieval benefit and signals that the quiz is a teaching moment rather than a practice one. If Q1–Q6 are failing badly (more than a third wrong on vocabulary questions), that signals the reading did not happen — acknowledge it, give a 60-second clarification, and adjust Part 3 accordingly.

**Q7–Q9 are diagnostic.** Splitting the room here is expected and is where the session's value lies. Q9 in particular should not be resolved with a mini-lecture — let Parts 3 and 4 surface the answer through the scenario work, then name it explicitly in the debrief.

This is formative assessment in action — the quiz result drives real-time instructional adjustment, consistent with Black & Wiliam's (1998) evidence that formative feedback loops are among the highest-leverage interventions in learning. The quiz format (recurring weekly, Mentimeter) is also specifically supported by evidence from introductory statistics courses: Farmus, Cribbie & Rotondi (2020) found that the presence of weekly in-class quizzes significantly moderated the flipped classroom advantage (Hedge's g = 0.43, DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)).

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

Two or three volunteers present their solutions to T1 and T2. Others ask questions. T3 is held back — it surfaces naturally in Part 3 if a scenario involves a self-referential model, and is used as the bridge forward in Part 5 if it doesn't.

The instructor's role here is to prompt, not narrate: *"Does anyone want to challenge that classification?"* *"What would change if the company had more historical data?"* *"Is that a critique of the model or the decision-maker?"*

The 10-minute buffer is explicit and named. It is not filled with additional content. It absorbs: slow starts, extended debate on T1(g) (the "when is a model too simplified" question), T2(d) (the fashion inventory cliff), or re-covering Q1–Q6 if the quiz revealed the reading hadn't landed. If none of these apply, the buffer compresses and Part 3 starts early.

**If the quiz showed Q7–Q9 splitting the room:** spend the buffer there rather than on T1–T3 mechanics. The reflexivity problem in Q9 is more valuable than re-defining aleatory vs epistemic.

Students are doing retrieval practice on the definitions so that the pair-work can focus on application, not vocabulary. Peer presentation activates the **testing effect** (Roediger & Karpicke, 2006): retrieving and articulating learned material strengthens long-term retention more than re-reading or passive review.

---

### Part 3 — Pair Work (25 minutes)

Each pair is assigned two scenarios from the pre-class submissions — one submitted by each partner — that the *other* pair member did not write.

**Roles: analyst and challenger.** The analyst argues for a specific model type and explains what uncertainty the model addresses. The challenger interrogates every assumption: Why that model and not another? What does it leave out? Who benefits from the framing? Roles swap at the 12-minute mark.

**Deliverable — three things, no more:**
1. For each scenario: a one-sentence classification (descriptive / predictive / prescriptive) with one reason
2. The biggest omission in the most complex of the two scenarios — what is the model designed to leave out, and is that justified?
3. One question the model cannot answer — even in principle — given its type

**Framing for the task:**

> *"Read your partner's scenario. Before you classify it, ask: what decision is at stake? A model is always built in service of a decision. If you can't name the decision, you can't classify the model."*
>
> *"If you don't know the context of your partner's scenario — that's fine. That's the point. Name what you don't know. The scenario owner will tell you in Part 4 whether your classification survived contact with the actual context."*

If pairs are stuck on classification, the instructor can offer a prompt: "What would the person who commissioned this model do with the output?" That usually resolves the ambiguity between predictive and prescriptive — a predictive model produces a forecast; a prescriptive model produces a recommendation.

**One additional prompt for pairs:** For the scenario you classified as prescriptive — does the model change the system it's trying to optimise? (This is the Q9 question in applied form. Most real prescriptive models have this property: a recommendation, once acted on, changes the conditions the recommendation was based on.) If pairs don't encounter this naturally, the instructor can surface it in Part 4.

The constrained deliverable (three outputs, no more) is deliberate. Lovett & Greenhouse (2000) identify mental overload as a direct inhibitor of learning efficiency; an open-ended task in 25 minutes produces anxiety, not analysis.

---

### Part 4 — Peer Discussion (20 minutes)

Each pair presents in ~2.5 minutes:
- Their classification of both scenarios
- The biggest omission in the most complex scenario
- The question the model cannot answer

The student who *submitted* each scenario then responds: is the classification right? Does the critique match what they know about the business context?

This is the highest-value exchange in the session. The scenario owner has real-world and cultural context the analyst pair doesn't — that asymmetry is the point.

This structure draws on Vygotsky's (1978) **zone of proximal development**: students are working at the edge of their competence, supported not by the instructor but by peers who hold complementary knowledge. A student from Singapore who submitted a scenario about hawker centre demand forecasting knows things about informal food economies that a student from Germany classifying the scenario doesn't — and that knowledge gap enriches the discussion in a way that no case study from a textbook can replicate.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop on this session first:**

*"What did we learn today about what a model is for — and what it is not for?"*

One sentence from each pair. Synthesise into: a model is not a description of reality. It is a deliberate simplification built in service of a specific decision. Its value comes from being answerable, not from being complete. A good analyst knows what the model answers and what it doesn't.

Then one more question — addressed to the room, not requiring a full answer:

*"Did the model in your scenario change the system it was trying to describe? Or would it, if someone acted on it?"*

This is the reflexivity question from Q9, now grounded in their own examples. Year 3 students who have studied social science or management will recognise it. Students who haven't will find it genuinely surprising. One exchange here, handled briefly, plants the question for the whole course — the relationship between models and the systems they model is not stable.

**A grounding question before the bridge-forward:**

> *"You've all just done something models struggle with: moved to a new city — twice now — with no historical data about yourself in that context. What did you predict about your experience before you arrived somewhere new — and what turned out to be wrong? What type of uncertainty was that?"*

This takes 60–90 seconds. It grounds the epistemic/aleatory distinction in something the cohort has lived, and signals from Week 1 that this course will treat their own experience as data. Don't over-explain the connection — plant it and move on.

**Then one question to leave them with — don't answer it today:**

> *"All three types of analytics — descriptive, predictive, prescriptive — require data. But data is always collected in the past. What does it mean to use past data to prescribe a future decision in a changing world?"*

The answer is non-obvious and requires the rest of the course to develop properly. It surfaces again in the time series weeks (Block 4) and the regression weeks (Block 3). This is its first planting.

One question. Not three. Working memory is depleted at the end of a 90-minute session — opening multiple threads produces noise, not retention.

---

## After Class (~30 min)

Students write a short reflection — posted to the LMS (Moodle or Canvas), formatted as though it were a public social media post — about one scenario from the session:
- What type of analytics applied, and why?
- What did the model leave out — and was that the right call?
- One question the model cannot answer, even in principle

**Format constraint:** write it as if posting to LinkedIn or a data science community. One to three paragraphs, a headline, something a stranger could engage with. The discipline of writing for a non-specialist public audience forces clarity of argument and requires the student to commit to a position.

Other students are expected to leave at least one comment — a pushback, a follow-up question, or a connection to their own scenario. That's the consolidation mechanism. A comment that forces you to articulate why a colleague's model framing is incomplete is more cognitively demanding than writing the original post.

If you encountered a version of this decision in a different country or institutional context than the scenario describes — add it. The cohort has 40+ nationalities between them. That is a richer dataset than any textbook.

Optional further reading: Breiman, L. (2001). Statistical modelling: The two cultures. *Statistical Science*, 16(3), 199–215. (A short accessible read on the tension between models that explain and models that predict — relevant to Week 3 onward.)

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Student-submitted scenarios from their own country (with one from another) | Ausubel (1968): self-relevance anchors new conceptual frameworks; cross-national constraint sharpens the Vygotskian knowledge asymmetry in Part 4 |
| Reading scoped to §1.1–1.3 only; tools chapter deferred | Fischer et al. (2023): cap pre-work at ~1.5× in-class time; tool instruction before conceptual grounding produces mechanical fluency without understanding |
| Worked example before T1–T3, marked optional for confident students | Rosenshine (2012): worked examples should precede independent practice — students need a model of the reasoning chain before attempting to produce it. Marked optional per Kalyuga et al. (2003) expertise reversal: students who can already complete T1(a)–(d) do not benefit from the example and may disengage from reading it. Active-watching video prompts supplement this by ensuring the videos are retrieval opportunities, not passive viewing. |
| Quiz runs easy → hard across 9 questions; runs every week | Q1–Q6 are retrieval practice; Q7–Q9 are diagnostic. Farmus, Cribbie & Rotondi (2020): weekly in-class quizzes moderated flipped classroom advantage (g = 0.43) in introductory statistics |
| Tutorial T1–T3 scaffold from definitional to contextual to reflexive | T1 establishes vocabulary; T2 requires context-to-model reasoning; T3 (DeepSeek/Nvidia) surfaces the model-scope and tail-risk problems before students have calcified views about "what analytics does" |
| Pairs work on each other's scenarios, not a shared case | Vygotsky (1978): ZPD — complementary contextual knowledge produces richer critique than shared case studies; scenario owner can validate or complicate the analyst's reading |
| Analyst/challenger roles with swap at 12 min | Bjork (1994): desirable difficulties — being forced to argue the position you're uncertain about strengthens understanding; role swap prevents free-riding on the more confident partner |
| Constrained deliverable (3 outputs) | Lovett & Greenhouse (2000): tight scope preserves cognitive capacity for higher-order classification work |
| Reflexivity question planted in debrief, not resolved | Bjork (1994): desirable difficulties include unresolved questions that create retrieval motivation; the reflexivity question returns in Weeks 11, 15, and 17 |
| Single bridge-forward question about past data → future decisions | Working memory is depleted at end of 90 minutes; one counterintuitive unanswered question plants a more durable hook than three connections |
| LMS post in social media format with peer comment requirement | Constructivist consolidation (Piaget, 1952); public-format writing forces argument clarity; peer comments activate the testing effect (Roediger & Karpicke, 2006) |
| Three-touchpoint structure (pre-work → in-class → post-work) | Cepeda et al. (2006): spacing effect — distributed practice improves long-term retention over massed practice |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Act only on contested questions; Q1–Q6 retrieval, Q7–Q9 diagnostic |
| Tutorial review | 15 min | T1–T2 only; T3 held for bridge or Part 4 use |
| Buffer (explicit) | 10 min | Absorbs slow starts, extended debate on T1(g) or T3(d), or re-covering basics if quiz showed gaps |
| Pair work | 25 min | Analyst/challenger roles; swap at 12 min; scenarios from pre-class submissions |
| Peer discussion | 20 min | ~2.5 min per pair; scenario owner responds to classification and critique |
| Instructor debrief | 10 min | Close the loop, reflexivity question, one unanswered bridge-forward question |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

This section documents live tensions in the lesson design — choices that could have gone differently, and the reasoning behind what was chosen.

---

### 1. Week 1 is Week 1 — the cohort does not yet know what the course expects.

This is the first seminar of ST2187. Students arrive with different prior exposures to analytics: some have worked in data-adjacent roles, some have taken statistics courses, some are encountering the framework for the first time. Unlike later weeks, the pre-class submission cannot be read as a reliable signal of preparation — it is also, partially, an act of self-presentation by students who don't yet know what the instructor values.

**Trade-off:** the scenario-sorting format is flexible enough to accommodate this range. A student who arrives with thin conceptual vocabulary can still argue about a business decision they've encountered in the real world. A student who knows the terminology cold is asked to do something harder: interrogate the assumptions behind a scenario submitted by a peer who may have framed the problem very differently.

**Design implication:** the quiz in Part 1 is calibrating the room, not testing it. The instructor should treat a split on Q6 (prescriptive vs predictive) as an invitation to surface the distinction, not as evidence of inadequate preparation. Week 1's value is establishing that the course rewards reasoning over recall — that norm takes the first two or three sessions to set.

---

### 2. "Scenario sorting" risks becoming vocabulary labelling.

The core intellectual move of this session — classifying a business decision by analytics type and uncertainty type — is easy to perform superficially. A student who can say "this is prescriptive, the uncertainty is epistemic" without being able to explain what a prescriptive model would actually do has produced a label, not an analysis.

**The structural fix:** the deliverable requires not just classification but a specific named omission and a question the model cannot answer. Those outputs cannot be produced from vocabulary alone — they require engaging with the scenario content. The challenger role in the pair is the enforcement mechanism: it is the challenger's job to ask "but what does the model actually produce — what number, what recommendation?" A classification that can't answer that question hasn't done the work.

**Trade-off:** this constraint slows the pace of the pair work and may mean some pairs only get through one scenario properly rather than two. That is acceptable. One scenario interrogated rigorously is more valuable than two classified superficially.

---

### 3. The contested dimension of T3 (DeepSeek/Nvidia) risks derailing the session.

T3 introduces a genuinely contested domain — US–China technology competition and an AI market shock — in a cohort where some students will hold strong views about AI hype, markets, or the countries involved. The tutorial problem is designed to surface the conceptual issue (the recommendation models' scope excluded a structural break) without requiring a verdict on the geopolitics or on AI itself.

**The risk:** students who feel strongly about the topic may treat the discussion as an opportunity to rehearse an argument they already hold, rather than to analyse the specific modelling problem. "Was the market right about DeepSeek?" is not what T3 is asking. T3 is asking: *given these models' inputs, was the omission a design flaw or a scope decision — and who owned that decision?*

**Design implication:** if T3 becomes contested in Part 4, the instructor should redirect with a specific question: "Set aside whose view of the AI market is right — what did these models assume, and how should that assumption have been communicated?" This keeps the discussion analytical rather than partisan. The same screening logic applies to student-submitted scenarios touching sensitive demographic or political material (Week 3 formalises a screening protocol).

---

### 4. Cross-national scenarios produce unequal knowledge bases.

A scenario submitted by a student from Singapore about CPF (Central Provident Fund) pension contributions may be entirely opaque to a student from Germany who hasn't encountered mandatory savings schemes. The pair work deliberately exploits this asymmetry — but unequal knowledge can tip into one partner doing all the contextual explanation while the other does all the modelling, which splits the cognitive labour in an unhelpful direction.

**The fix:** the analyst/challenger structure makes this explicit. The analyst is responsible for the modelling classification — which does not require deep local knowledge. The challenger is responsible for interrogating assumptions — which benefits from contextual knowledge that the scenario owner can provide. The scenario owner's role in Part 4 is specifically to validate or complicate what the pair found. This three-way structure (analyst, challenger, scenario owner) distributes the labour more evenly than a pure pair.

**Trade-off:** this structure only works if the scenario owner's response in Part 4 is substantive — which requires them to have been thinking about the critique during the other pairs' presentations, not drafting their own. The instructor should name this expectation explicitly before Part 4 begins: "While other pairs present, the person whose scenario they're analysing should be thinking — did they get it right? What did they miss?"

---

### 5. The pre-class submission format introduces selection bias in what scenarios get brought.

Students are asked to bring business decisions they have "personally encountered or read about." In practice, this means students will tend to bring decisions from sectors they find familiar or interesting — finance, technology, e-commerce — and underrepresent sectors they find boring or unfamiliar — agriculture, public health, infrastructure, manufacturing. This skews the Part 4 discussion toward a narrow range of decision types.

**Design implication:** the instructor should, before Part 4, do a quick scan of what sectors are represented and call out an underrepresented one: "I notice no one has brought an agriculture scenario — does anyone know about commodity price forecasting? That's one of the oldest prescriptive analytics problems in existence, and it has all three types of uncertainty at once." This takes 60 seconds and signals that analytics is not synonymous with tech.

**Trade-off:** this intervention is instructor-driven, not student-driven, and partially contradicts the flipped-classroom principle that in-class time should be student-led. The instructor should make this correction once, efficiently, and then step back — not use it as a gateway to a mini-lecture on agricultural economics.

---

## References

- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Breiman, L. (2001). Statistical modelling: The two cultures. *Statistical Science*, 16(3), 199–215.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
- Farmus, L., Cribbie, R.A. & Rotondi, M.A. (2020). The flipped classroom in introductory statistics: Early evidence from a systematic review and meta-analysis. *Journal of Statistics Education*, 28(3), 316–325. DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Fischer, J., Torcasio, S., Sweller, J. & Kalyuga, S. (2023). Flipped classroom design: Managing cognitive load. *BMC Medical Education*, 23(1), 345. DOI: [10.1186/s12909-023-04325-x](https://doi.org/10.1186/s12909-023-04325-x)
- Kalyuga, S., Ayres, P., Chandler, P. & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Rosenshine, B. (2012). Principles of instruction: Research-based strategies that all teachers should know. *American Educator*, Spring 2012. ERIC EJ971753.
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapter 1

**Coverage check: mostly sufficient, but the reading references do not match the actual book.**

The pre-work cites "§1.1 Introduction to business analytics (pp. 1–5), §1.2 The three types of analytics (pp. 5–10), §1.3 Uncertainty and the modelling process (pp. 10–18)". The 6th edition's Chapter 1 is actually structured:

| Actual section | Pages | Content |
|---|---|---|
| 1-1 Introduction | 3 | What business analytics is |
| 1-2 Overview of the Book | 4–9 | 1-2a The Methods; 1-2b The Software |
| 1-3 Modeling and Models | 10–15 | 1-3a Graphical; 1-3b Algebraic; 1-3c Spreadsheet models; 1-3d A Seven-Step Modeling Process |
| 1-4 Conclusion | 15 | — |

Two consequences:

1. **Fix the section references** to "Chapter 1 in full (pp. 1–15), with emphasis on 1-3 Modeling and Models." Students who self-select for flipped classrooms check the reading against the seminar (student-voice point 2); a mismatched reference in Week 1 undermines the pre-work contract before it's established.
2. **The descriptive/predictive/prescriptive trichotomy and the aleatory/epistemic distinction are not in Albright & Winston.** A&W frame the book as *data analysis* vs *decision making under uncertainty* (1-2a); they never use "prescriptive" as a category or "aleatory/epistemic" at all. Both frameworks are pedagogically sound, but they currently rest entirely on two YouTube videos. Provide a one-page instructor handout defining both frameworks and mapping them onto A&W's structure (descriptive ≈ Part 1 Exploring Data; predictive ≈ Parts 3–4; prescriptive ≈ Part 5 Optimization/Simulation). Otherwise students hunting for "epistemic" in Chapter 1 will conclude they read the wrong book.

**Topics from Chapter 1 worth incorporating (currently unused):**

- **The Seven-Step Modeling Process (1-3d)** — the strongest omission. It is exactly the session's theme (problem definition → model scope → what gets left out), and it gives the airline worked example a formal skeleton. Add it to the pre-reading emphasis and have pairs in Part 3 locate which of the seven steps their scenario's model is stuck at.
- **Graphical vs algebraic vs spreadsheet models (1-3a–c)** — one quiz question's worth of vocabulary that pays off in Weeks 6–9 when spreadsheet models arrive; costs nothing now.
- **1-2b The Software** — reinforces the plan's own advice that tool chapters are deferred; cite it so students know the deferral is deliberate.

## 2. Extended Question Bank (with answers)

*Additional tutorial problems — continue numbering from T7:*

**T8 — The seven-step process (definitional → applied):**

> Albright & Winston describe a seven-step modeling process: (1) define the problem, (2) collect and summarise data, (3) develop a model, (4) verify the model, (5) select one or more suitable decisions, (6) present the results to the organisation, (7) implement and evaluate.
>
> (a) The airline worked example (Berlin–Lisbon scheduling) shows steps 1–3. Which step would reveal that the model ignores competitor pricing responses — and is that a problem for *verification* (step 4) or *problem definition* (step 1)?
> (b) A data analyst spends three months perfecting step 3 and skips step 6 because "the model speaks for itself." Using the DeepSeek/Nvidia case (T3), explain what step 6 should have contained.
> (c) At which step does the reflexivity problem (quiz Q9 — the model changing the system) become visible? Why can't it be caught earlier?

**Answers:** (a) Verification (step 4) tests whether the model behaves sensibly *given its scope*; the omission of competitor pricing was set at step 1 (problem definition). If the omission is wrong, it's a step-1 error, not a step-4 error — the model can verify perfectly and still answer the wrong question. (b) Step 6 should have contained explicit assumption statements: "this recommendation assumes AI compute demand follows historical trends; it does not price structural efficiency breakthroughs." Presentation is where scope limits get communicated to decision-makers. (c) Step 7 (implement and evaluate) — only after implementation does the system respond to the model's output. It can't be caught earlier by *observation*, only anticipated by *reasoning* (which is why the debrief question matters).

**T9 — Model representations:**

> A&W distinguish graphical, algebraic, and spreadsheet models. A café owner wants to decide how many croissants to bake daily.
>
> (a) Sketch (in words) what a graphical model of this decision looks like. What does it communicate that an equation doesn't?
> (b) Write the algebraic model: define the decision variable, the objective, and at least one constraint.
> (c) Why might a spreadsheet model be preferred over the algebraic one for this owner — and what is lost in the translation?

**Answers:** (a) E.g. a diagram of inputs (demand, price, cost, waste) flowing into the order decision and out to profit — it communicates *structure and dependencies* at a glance, accessible to non-quantitative stakeholders. (b) Decision variable: q = croissants baked. Objective: maximise expected profit = p·E[min(q, D)] − c·q, where D is random demand, p price, c unit cost. Constraint: q ≥ 0 (and perhaps oven capacity q ≤ K). (c) A spreadsheet makes the model manipulable without algebra — the owner can try values, see sensitivity. What's lost: generality and transparency of assumptions; a formula cell hides its logic more than an equation on paper does.

**T10 — Rapid classification set (retrieval volume):**

Classify each as descriptive (D), predictive (P), or prescriptive (Pr), one line of justification:

> (i) A dashboard showing last quarter's sales by region.
> (ii) A churn score for each current subscriber.
> (iii) A staffing roster generated to minimise overtime subject to shift-coverage rules.
> (iv) An A/B test report showing conversion rates in each arm.
> (v) A credit limit assigned automatically to each new customer.
> (vi) A weather forecast used to decide whether to cancel an outdoor event.

**Answers:** (i) D — summarises what happened. (ii) P — forecasts a future behaviour per customer. (iii) Pr — an optimisation output; produces a decision. (iv) D — describes observed outcomes (the *decision* to roll out a variant would be a further prescriptive step). (v) Pr — an automated decision, though built on a predictive score; good answer notes the pipeline P → Pr. (vi) The forecast itself is P; the cancel/don't-cancel rule applied to it is Pr. (iv)–(vi) reward students who see analytics types as stages in a pipeline rather than exclusive labels.

*Additional quiz questions (append to the Mentimeter set):*

- Q10: In A&W's seven-step modeling process, which step comes immediately before developing the model? *(a) Verify the model (b) Collect and summarise data (c) Present results (d) Select decisions)* — **Answer: (b).**
- Q11: A spreadsheet model differs from an algebraic model primarily in: *(a) accuracy (b) the type of uncertainty it can handle (c) how the logic is represented and manipulated (d) whether it can be prescriptive)* — **Answer: (c).**
- Q12: A churn-prediction score is fed into a rule that automatically offers discounts to high-risk customers. The end-to-end system is best described as: *(a) descriptive (b) predictive (c) prescriptive (d) diagnostic)* — **Answer: (c)** — the system's output is an action; the predictive score is an input. Good discriminator between students who label components and students who see the pipeline.

## 3. Alternative In-Class Activities (additional options — choose to swap for Part 3 or 4)

**A. Model autopsy gallery walk (25 min, replaces Part 3).** Post three one-paragraph model-failure vignettes around the room (e.g. Google Flu Trends; the 2016 US election forecasts; a rules-based ambulance dispatch failure). Pairs rotate every 7 minutes and must write on each poster: *was this a scope failure, a data failure, or a use failure?* Debrief maps answers onto the three failure types. Strength: uses real cases, no dependency on the quality of student-submitted scenarios in Week 1 (a genuine risk — see critique). Weakness: loses the cross-national student-owned material.

**B. Structured controversy: "No model is better than a bad model" (20 min, replaces Part 4).** Johnson & Johnson (1988) format: pairs are assigned a side, argue it for 5 minutes, then *swap sides* and argue the opposite, then drop roles and write a joint position. Directly develops T4(d). Fits Forward's debate-centred seminar culture and forces students off their initial intuition.

**C. Uncertainty sort with physical cards (15 min, insert before Part 3).** 12 pre-printed cards with uncertainty sources (flight demand variance, unknown competitor costs, coin flips, a new virus's severity, exchange rates next year, sensor measurement noise…). Small groups sort into aleatory / epistemic / genuinely contested. The contested pile is the point — several cards (exchange rates, virus severity) are defensibly both, which pre-empts the false binary. Low-stakes, fast, kinesthetic — good for a Week 1 cohort still forming.

**D. "Commission the model" role-play (25 min, replaces Part 3).** One student is the executive, one the analyst. The executive has a business problem (from the pre-class submissions); the analyst may ask only five questions before proposing a model type and scope. The class scores whether the five questions found the decision, the uncertainty, and the acceptable omissions. Trains exactly the consulting behaviour Forward's external partners praised (student-voice point 10).

**E. One-minute paper + live re-poll (5 min, alternative Part 5 close).** Students write for 60 seconds: "the most useful distinction I learned today, and one thing still fuzzy." Instructor re-runs quiz Q6 and Q9 live — visible score movement closes the retrieval loop and gives the instructor a written diagnostic for tutorial follow-ups (supports the "know all the names, all the voices" expectation).

## 4. Critique of the Lesson Plan

**What works (keep):** explicit buffer time; constrained three-output deliverable; answer keys written to first-class standard; the reflexivity thread planted rather than resolved; cross-national scenario constraint that genuinely exploits the 40+-nationality cohort; the Design Challenges section shows unusual reflective honesty.

**Problems, reasons, and fixes:**

1. **Reading references are wrong (see §1 above).** *Reason it matters:* Forward students self-select for the flipped model and check pre-work against class; a broken reference in Week 1 damages the pre-work contract the whole course depends on. *Fix:* correct to 1-1–1-3 and add the framework handout for aleatory/epistemic.

2. **Internal inconsistency: the plan describes T3 as "algorithmic hiring" in two places (Design Rationale table row 5; Design Challenge 3) but T3 as written is DeepSeek/Nvidia.** *Reason:* an earlier revision was partially applied; anyone reading the plan closely (a course leader, an interview panel) will spot it. *Fix:* either restore an algorithmic-hiring tutorial as T8-equivalent or rewrite the two stale references.

3. **Pre-work volume contradicts the plan's own principle.** The plan claims Week 1 pre-work is "intentionally lighter" and cites Fischer et al.'s ~1.5× cap, but assigns: a chapter, two videos with pause-tasks, a worked example, T1–T7 (≈35 sub-questions), and a four-scenario submission. That is 4–6 hours against a 90-minute seminar. *Reason:* overload in Week 1 causes corner-cutting that then looks like non-compliance; the plan would punish what it caused. *Fix:* require T1–T3 + submission; label T4–T7 explicitly as a stretch bank / tutorial-session material. (The extended bank in §2 above should likewise be marked optional or used for the weekly one-on-one tutorials.)

4. **The answer key sits in the same document as the questions.** *Reason:* if this file is distributed, the self-check instruction for T1 becomes answer-copying for T2–T7, killing the testing effect the plan cites (Roediger & Karpicke). *Fix:* split into a student version and an instructor version; release answers after submission.

5. **Part 4 arithmetic is fragile.** 12–15 students = 6–7 pairs × 2.5 min presenting + owner responses ≈ 20–25 min before any discussion. *Reason:* the highest-value exchange (owner responds) is the first thing squeezed. *Fix:* each pair presents only their *more complex* scenario; the second is submitted in writing to the LMS thread.

6. **No contingency for the tech stack.** Mentimeter + LMS submission + projected slides, Week 1, new cohort norms. *Fix:* paper fallback for the quiz (hold up 1–4 fingers or coloured cards) and a stated grace policy for the first submission.

7. **Missed alignment with the one-on-one tutorial system.** Forward's weekly 60–90-minute tutorials (pedagogy doc) are the natural home for the T4–T7 stretch problems and for following up quiz diagnostics — the plan never mentions them. *Fix:* one line in After Class routing: "quiz misconceptions and stretch problems T4–T7 are tutorial material this week."
