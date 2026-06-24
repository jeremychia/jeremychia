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

**Reading:** Albright & Winston, *Business Analytics*, Chapter 1 — read the following sections only:
- §1.1 Introduction to business analytics (pp. 1–5)
- §1.2 The three types of analytics (pp. 5–10)
- §1.3 Uncertainty and the modelling process (pp. 10–18)

The case study appendix and the DecisionTools Suite introduction in Chapter 1 are optional this week. The tools are introduced properly in Weeks 6–9; reading tool instructions before you understand what problems they solve wastes preparation time.

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
| Tutorial T1–T3 scaffold from definitional to ethical to reflexive | T1 establishes vocabulary; T2 requires context-to-model reasoning; T3 (algorithmic hiring) surfaces the feedback loop and objectivity problems before students have calcified views about "what analytics does" |
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

### 3. The ethical dimension of T3 (algorithmic hiring) risks derailing the session.

T3 introduces a genuinely contested domain — algorithmic hiring — in a cohort where at least some students are themselves recent applicants, and where views on bias, automation, and fairness are likely to be strong. The tutorial problem is designed to surface the conceptual issue (the model is optimising for the wrong objective) without requiring a normative verdict on algorithmic hiring generally.

**The risk:** students who feel strongly about the topic may treat Part 3 as an opportunity to rehearse an argument they already hold, rather than to analyse the specific modelling problem. The question "is algorithmic hiring ethical?" is not what T3 is asking. T3 is asking: *given this model's structure, what is it actually doing?*

**Design implication:** if T3 becomes contested in Part 4, the instructor should redirect with a specific question: "Set aside whether this is fair — what is the model being *asked* to predict? And is the training data a valid basis for that prediction?" This keeps the discussion analytical rather than normative. The ethical question is real and worth raising in a later session (Week 10, decision trees, is a natural home for it) — but not as the first conceptual move of the course.

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
