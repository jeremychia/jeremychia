# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 3: Exploring Relationships Between Variables
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Construct a crosstab with correct row or column percentages and explain which orientation answers which type of question
- Interpret a correlation coefficient and articulate what it does and does not imply about the relationship between two variables
- Identify at least one plausible confounding variable for a given correlation and explain the mechanism by which it might produce the observed association
- Evaluate a causal claim made from correlation data, specifying what additional evidence would be needed to support or refute it

These map directly to the ST2187 course outcome of developing students who can *"identify limitations and possible misuse"* of quantitative tools, and who are equipped to critically assess data-driven arguments in real business and policy contexts.

These objectives operate at the **analysis and evaluation** levels of Bloom's Taxonomy (Anderson & Krathwohl, 2001) — students must not only compute correlations and crosstabs but interrogate the inferential leap from association to causation.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 3 — read the following sections only:
- §3.1 Introduction to relationships (pp. 79–82)
- §3.2 Relationships among categorical variables — crosstabs (pp. 82–92)
- §3.3 Relationships between categorical and numerical variables (pp. 92–98)
- §3.4 Relationships between two numerical variables (pp. 98–112)

The pivot chart and slicer material in §3.5 is optional this week. It is surfaced in Block 2 (Tableau and Excel practical sessions). Reading it now adds tool complexity before the conceptual groundwork is secure.

*Rationale:* §3.1–3.4 cover everything needed for the spurious correlation gallery in Part 3. The full chapter including §3.5 is approximately 55 pages; the assigned sections are the conceptual core. Fischer et al. (2023) recommend capping pre-work at ~1.5× in-class time — the sections above, combined with the tutorial problems and pre-class submission, hit that ceiling without exceeding it.

**Videos (~20 minutes total):**
- [Correlation — Simply Explained](https://www.youtube.com/watch?v=GtV-VYdNt_g) (~10 min) — covers positive, negative, zero correlation and the correlation coefficient. *Active watching: at the point where the presenter introduces r = 0 (no linear relationship), pause and write one example from business or daily life where two variables have r = 0 but might still have a non-linear relationship. This primes T4(b).*
- [The danger of mixing up causality and correlation — Ionica Smeets](https://www.youtube.com/watch?v=8B271L3NtAw) (~10 min, TEDx) — a statistician explains why strong correlations can be entirely spurious, using examples that mirror the gallery in Part 3. *Active watching: when Smeets introduces her first spurious correlation example, pause and write the three-step structure she uses: (1) state the correlation, (2) construct the causal story, (3) identify the confounder. This is exactly the structure T2 and the Part 3 gallery require.*

**Worked example (read this before attempting the tutorial problems):**

This walks through the full reasoning chain you will use in Part 3. Read it carefully and annotate each of the three steps. The three-step structure — causal story → confounder → evidence threshold — is what T1–T3 ask you to apply.

*This worked example is marked optional for students who already feel confident with the three-step reasoning. If you can write a one-sentence causal story and name a specific confounder for T2(c) without reading this, you don't need it. If the confounder identification felt vague, read it before the tutorials.* (On expertise reversal, see Kalyuga, Ayres, Chandler & Sweller, 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

> **Dataset:** Monthly data from a European city: (1) average daily temperature (°C), (2) ice cream sales (€000s). n = 36 months.
> Correlation coefficient: r = 0.91. The scatterplot shows a strong positive relationship.
>
> **Step 1 — Construct the strongest possible causal story.**
> "Hot weather causes people to want cold food and drink. Higher temperatures drive higher ice cream sales. The r = 0.91 is consistent with a causal mechanism. This is not spurious."
>
> **Step 2 — Identify the confounders.**
> Temperature is correlated with: the number of people outdoors, tourist season (more visitors in summer), school holidays (children driving discretionary food purchases), daylight hours (longer evenings, more social eating). Any of these, or their combination, could be the actual driver. The causal story in Step 1 is plausible — but it's not the only one consistent with r = 0.91.
>
> **Step 3 — What would make the causal claim credible?**
> You would need to show that temperature affects ice cream sales *independently* of tourist season, school holidays, and outdoor activity. This requires: (a) data that separates these variables, (b) a model that controls for them, and (c) ideally, a natural experiment (e.g. an unusually cold July — does ice cream sales fall even when everything else is the same?). The correlation alone gets you to suspicion. It does not get you to causation.
>
> **What you are looking for in your own dataset:** the gap between the correlation you can compute and the causal claim a reader might draw from it. The ice cream example has multiple confounders. Your dataset may have one, or a different kind. The question is always: what else changes when X changes?

**Tutorial problems (submitted before class, reviewed in Part 2):**

These confirm mechanical competence with crosstabs and correlation — the prerequisite for the higher-order causal reasoning work in Parts 3 and 4. Students bring written answers; two or three will present.

*T0 — Entry question (lower floor):*

> For each of the following pairs of variables, write: (a) whether the correlation is likely to be positive, negative, or approximately zero, and (b) one sentence explaining why. No formula or calculation required.
>
> (i) Hours of sunshine per day and ice cream sales in a city.
> (ii) Number of fire stations in a city and number of fires recorded.
> (iii) A person's shoe size and their vocabulary test score.
> (iv) Distance from city centre and average apartment price per square metre.

T0 tests intuition about the *direction* of correlation before any computation. It also plants two traps: (ii) is a classic spurious correlation (both are driven by city size) and (iii) is approximately zero. Students who answer all four confidently can move directly to T1. Students who are uncertain about (ii) or (iii) should re-read §3.4 before continuing.

*Self-check for T0:* (i) positive — temperature drives both; (ii) positive — but both driven by city size, not a causal relationship; (iii) approximately zero — no plausible direct mechanism; (iv) typically negative — prices fall with distance from centre in most European cities, though exceptions exist. If your direction for (ii) is positive but your reasoning stopped at "more fire stations → more fires recorded," re-read the worked example section on confounders before continuing.

*T1 — Straightforward computation (no ambiguity):*

*The three-step structure in the worked example — strongest causal story → named confounder → evidence that would change your mind — maps directly onto T2 and T3. The row vs column percentage logic from the worked example's crosstab reasoning applies to T1(a)–(b).*

> The following table shows survey data for 200 customers of a travel company: whether they purchased travel insurance (Yes/No) and whether they had previously made a claim (Yes/No).
>
> | | Purchased insurance | Did not purchase | Total |
> |---|---|---|---|
> | Previous claim | 60 | 20 | 80 |
> | No previous claim | 40 | 80 | 120 |
> | **Total** | **100** | **100** | **200** |
>
> (a) Calculate row percentages. What question does the row percentage answer?
> (b) Calculate column percentages. What question does the column percentage answer?
> (c) A manager says: "60% of people who had a previous claim bought insurance, vs only 33% of those who didn't — so past claims predict purchase." Is this correct? Which percentages support this?
> (d) Another manager says: "Of all insurance buyers, 60% had a previous claim — so most of our insurance customers are repeat claimers." Is this correct? Which percentages support this?
> (e) Are (c) and (d) both correct? Do they tell the same story?
> (f) Calculate the correlation between "previous claim" (coded 1=Yes, 0=No) and "purchased insurance" (coded 1=Yes, 0=No) using CORREL in Excel. What does this coefficient tell you that the crosstab doesn't?
> (g) A marketing team wants to target future insurance campaigns. Which percentage — row or column — is more useful for targeting, and why?

Parts (a)–(b) are mechanical. Part (e) is the key conceptual move: both managers are correct, but they're answering different questions. Students who understand this understand crosstabs. Students who think one manager must be wrong haven't read the chapter carefully enough. Part (g) is the decision link — targeting requires row percentages (given someone has a prior claim, what's the probability they buy?), not column percentages.

*Self-check for T1(a)–(b):* Row percentage for "Previous claim" row: 60/80 = 75% purchased; 20/80 = 25% did not. Column percentage for "Purchased insurance" column: 60/100 = 60% had a previous claim; 40/100 = 40% had no previous claim. If you computed these correctly, continue. If the row/column distinction felt unclear, re-read §3.2 before T2.

*T2 — Interpretation, not just computation:*

> A researcher publishes the following findings: "In a dataset of 50 European cities, per capita chocolate consumption is strongly correlated with the number of Nobel Prize winners per 10 million population (r = 0.79, p < 0.05)."
>
> (a) Sketch what this scatterplot would look like.
> (b) Does the correlation coefficient tell you which direction causation runs? Explain.
> (c) Identify one plausible confounding variable — something that might cause both high chocolate consumption AND more Nobel Prize winners. Explain the mechanism.
> (d) The researcher adds: "I also found that cheese consumption has the same correlation with Nobel Prize winners (r = 0.78)." Does this strengthen or weaken the causal case for chocolate? Why?
> (e) What would need to be true for this correlation to reflect a genuine causal effect of chocolate on cognitive performance?

This problem uses the actual Messerli (2012) finding (NEJM) — a paper published in a peer-reviewed journal that made a causal claim from country-level ecological correlation. Students who have seen the correlation may recognise it; that's fine — the analytical framework applies regardless. Part (d) is the trap: a second variable with the same correlation does not strengthen the first causal claim; it weakens it, because it suggests both are proxies for the same confounder (wealth, broadly).

*T3 — Edge case that requires genuine thought:*

> In 2025, a major social media platform published internal research showing that teenage users who spent more than 3 hours per day on the platform reported higher rates of anxiety symptoms (r = +0.41, n = 18,000). Several governments cited this correlation as justification for proposed screen-time limits for under-16s.
>
> (a) Interpret r = +0.41 in plain English. Is this a strong, moderate, or weak correlation?
>
> (b) A policy advisor concludes: "More social media use causes anxiety — we should legislate a 1-hour daily cap." What is the most important thing wrong with this causal story?
>
> (c) The dataset includes users from two groups: those who reported using the platform mainly for passive scrolling (watching others' content) and those who reported using it mainly for active connection (messaging, commenting, group participation). You split the data:
>
> - Passive scrolling group: r = +0.48 (more time → more anxiety)
> - Active connection group: r = −0.12 (more time → slightly less anxiety)
>
> What happened to the aggregate r = +0.41? Does it describe either group's experience well?
>
> (d) This phenomenon has a name. What is it, and what does it mean for how social media research — or any aggregate correlation — should be interpreted?
>
> (e) The platform's research was funded by the platform itself. A critic says: "They only published this to pre-empt regulation — they would have buried it if it showed a stronger effect." A defender says: "The data is the data — who funded the study doesn't change the correlation." Who is right, and what additional information would you want before relying on this study for policy?

T3 uses a structurally real 2025 policy context: the debate about social media use and adolescent mental health was active in multiple legislatures in 2024–2025 (Australia's Social Media Minimum Age Act passed November 2024; UK Online Safety Act 2023 came into force in 2024; US Senate hearings in January 2024 featured similar correlational claims). The specific correlation and subgroup data in the question are illustrative, but the Simpson's Paradox structure — aggregate correlation reversing within subgroups defined by use type — reflects a genuine complexity documented in academic literature (Orben & Przybylski, 2019, critiqued the coarseness of aggregate screen-time measures; Twenge et al. versus Orben/Przybylski debate is ongoing). Part (e) adds a funding-bias dimension that applies to all industry-sponsored research. Students who understand T3 will never again trust an aggregate correlation without asking about subgroup structure — and will ask who funded the study.

*T4 — Boundary case: what happens when r approaches its limits:*

> Consider the following three datasets, each with 20 observations. For each, you are told the correlation coefficient.
>
> **Dataset A:** r = +1.00 between monthly marketing spend and monthly sales.
> **Dataset B:** r = 0.00 between shoe size and annual salary across 500 employees.
> **Dataset C:** r = −0.12 between ice cream consumption and reported stress levels.
>
> (a) In Dataset A (r = +1.00), does this mean advertising *causes* sales? What would a scatterplot look like, and what exactly does r = +1.00 imply about the data points?
> (b) In Dataset B (r = 0.00), does this mean there is definitely no relationship between shoe size and salary? Name one type of relationship r cannot detect.
> (c) In Dataset C (r = −0.12), a manager concludes "there's essentially no relationship here — ignore it." Is this conclusion valid? What determines whether a small r is meaningful?
> (d) Can r = +1.00 exist in real business data? Under what conditions would you be suspicious of a correlation this high?
> (e) A dataset has two variables X and Y. When you multiply every Y value by 3, what happens to r? When you add 100 to every X value, what happens to r? Explain why, using the definition of correlation.

*T5 — Multi-step reasoning: Simpson's Paradox applied:*

> A bank is evaluating two loan officers: Officer M and Officer N. You are given the following approval rate data:
>
> | | Officer M | Officer N |
> |---|---|---|
> | Low-risk applicants approved | 90 out of 100 (90%) | 45 out of 50 (90%) |
> | High-risk applicants approved | 30 out of 100 (30%) | 6 out of 10 (60%) |
> | **Overall** | **120 out of 200 (60%)** | **51 out of 60 (85%)** |
>
> (a) Based on overall approval rates, which officer appears more lenient?
> (b) Within each risk category, which officer approves a higher proportion of applicants?
> (c) Explain precisely why the two perspectives give contradictory rankings. What is the name of this phenomenon?
> (d) The bank's compliance team uses overall approval rate to assess whether officers are discriminating against high-risk applicants. Is this the right metric? What should they use instead?
> (e) Officer N's caseload has 50 low-risk and 10 high-risk applicants; Officer M's has 100 of each. Is this difference in caseload composition a problem with the data, the analysis, or the bank's allocation process? What would you investigate next?

This question directly extends T3 (which introduced Simpson's Paradox conceptually) into a business context with a numerical worked example. Students must apply the concept rather than recognise it.

*T6 — Confound identification: negative correlation variant:*

> A hospital network analysing discharge data finds a strong negative correlation (r = −0.74) between the number of doctors per 100 beds and patient mortality rate. The network's CEO concludes: "More doctors clearly saves lives — we should hire immediately."
>
> (a) Is the correlation (negative relationship between doctors per bed and mortality) plausible? Construct a causal story that supports the CEO's conclusion.
> (b) Identify at least two confounding variables that could explain this correlation without a direct causal effect of doctor-to-patient ratio on mortality.
> (c) The data is aggregated at the hospital level (not patient level). What additional problem does this create for causal inference? (Recall the ecological correlation issue from the reading.)
> (d) Suppose the network runs a natural experiment: one region doubles its doctor-to-bed ratio over three years while another maintains its ratio. What would you look for in the resulting data to assess whether more doctors causes lower mortality?
> (e) A statistician argues: "The correlation is real — we just don't know the mechanism." A manager says: "If we can't confirm causation, we shouldn't act." Who is right? At what point is a correlation actionable without established causation?

*T7 — Crosstab orientation: which percentage to use, and what happens when you use the wrong one:*

> An airline surveys 800 passengers on flight experience, categorising them by seat class (Economy / Business) and satisfaction (Satisfied / Unsatisfied).
>
> | | Satisfied | Unsatisfied | Total |
> |---|---|---|---|
> | Economy | 390 | 260 | 650 |
> | Business | 120 | 30 | 150 |
> | **Total** | **510** | **290** | **800** |
>
> (a) Compute row percentages. What question does each row percentage answer?
> (b) Compute column percentages. What question does each column percentage answer?
> (c) The airline's marketing team wants to know: "Among satisfied passengers, what proportion flew Business?" Which percentage do you use, and what is the answer?
> (d) The operations team wants to know: "Among Business class passengers, how satisfied are they?" Which percentage do you use, and what is the answer?
> (e) A junior analyst reports: "51% of all passengers were satisfied — that's our overall satisfaction rate." Is this a row percentage, a column percentage, or something else? Is it the most useful number for the airline?
> (f) The airline proposes improving Economy service to raise overall satisfaction. Based on this data, which group is numerically the larger source of unsatisfied passengers? Does this mean Economy service is the priority, or could there be a different reason?
> (g) Compute CORREL in Excel between seat class (Economy=0, Business=1) and satisfaction (Satisfied=1, Unsatisfied=0). What does this coefficient tell you that the crosstab doesn't?

*T8 — Real-world translation: set up the correlation analysis from a description:*

> You are a data analyst at a European retailer with stores in 12 cities. Your manager says: "I think our stores in larger cities perform better — can you check if there's a relationship between city population and our store revenue?"
>
> (a) Identify the two variables. Which is X (explanatory) and which is Y (response)? Does it matter which is which for computing r?
> (b) Your dataset has population in millions (ranging from 0.3 to 8.5) and annual store revenue in €millions (ranging from 1.2 to 22.7). You compute r = 0.61. Interpret this in plain English.
> (c) Your manager says: "Great — r = 0.61, so city size explains 61% of the variation in revenue." Correct this statement precisely.
> (d) You notice that one store in the dataset is in London (population 9.0 million, revenue €18.2 million). London is larger than any other city. How would removing London from the dataset likely affect r? Would the direction change?
> (e) Your manager now asks: "Does this mean we should open more stores in large cities?" Write a two-sentence response that correctly uses the correlation result without over-claiming causation, and names the most important confound to investigate before making this recommendation.

**Pre-class submission (on the course portal):**

Students find a dataset with at least two columns (one categorical + one numerical, or two numerical) from an open data source (e.g. [data.gov.sg](https://data.gov.sg), [Berlin Open Data](https://daten.berlin.de), [Paris Data](https://opendata.paris.fr), [dados.gov.pt](https://dados.gov.pt)) and:
1. Produce a crosstab OR a scatterplot (or both if time allows)
2. Report the correlation coefficient between two numerical variables if applicable
3. Write answers to three questions: What is this dataset? What relationship were you looking for, and why? What causal story is most tempting — and what would undermine it?

**Choose a dataset from a country other than your own.** The cultural context of a dataset matters for evaluating spurious correlations: a strong association in data from Singapore may have a completely different explanatory mechanism than the same association in data from Portugal, because the institutional, demographic, and historical context differs. The analyst pair in Part 3 will have different prior knowledge than the dataset owner — that gap is the point.

**Optional current affairs extension (no submission required):** In 2024–2025, governments in Australia, the UK, and the US debated legislation limiting social media use by teenagers, partly on the basis of correlational studies linking screen time to anxiety and depression. Before class, read one headline or article summarising this debate. Come ready to answer: what correlation was cited, and what alternative explanations were left out of the headline? You do not need to find the original study — the newspaper version is enough to identify what causal claim was made.

The "what causal story is most tempting" question in Q3 is intentional: it primes students to notice whether they are being seduced by a plausible mechanism before they've checked whether the data actually supports it. This activates the desirable difficulty of prediction-then-check (Bjork, 1994) — students who commit to a causal story are better positioned to notice when the pair work or Part 4 undermines it.

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

Questions run from straightforward to genuinely difficult. Easy questions confirm vocabulary and build momentum; hard questions find where understanding stops. Run all nine — the spread across the difficulty gradient is the informative signal.

**Easy — vocabulary and recall:**

- Q1: What does a correlation coefficient of r = 0 indicate?
  *(a) The two variables are identical  (b) There is no linear relationship between the variables  (c) The variables move in opposite directions  (d) The data has been collected incorrectly)*

- Q2: In a crosstab, row percentages answer which question?
  *(a) Given this column category, what percentage are in each row?  (b) Given this row category, what percentage are in each column?  (c) What percentage of all respondents fall in each cell?  (d) What is the ratio of row totals to column totals?)*

- Q3: Which Excel function computes the correlation between two ranges?
  *(a) COVAR  (b) CORREL  (c) PEARSON  (d) Both (b) and (c))*

- Q4: A scatterplot shows points forming a line from bottom-left to top-right. The correlation is:
  *(a) Negative  (b) Zero  (c) Positive  (d) Cannot be determined from a scatterplot)*

- Q5: Covariance and correlation measure similar things. The key advantage of correlation is:
  *(a) It is always positive  (b) It is not affected by the units of measurement  (c) It accounts for outliers automatically  (d) It works with categorical variables)*

- Q6: Which of the following is an example of ecological correlation?
  *(a) Correlation between two individuals' heights and weights  (b) Correlation between country-level average income and country-level life expectancy  (c) Correlation between a company's revenue and its number of employees  (d) Correlation between two products' weekly sales)*

Q6 is the trap question. Ecological correlation uses aggregate data (country-level, city-level, district-level averages) rather than individual-level data. The distinction matters because ecological correlations can be misleadingly strong — averages suppress variance, and the correlation between averages is not the same as the correlation between individuals. Students who haven't read §3.4 carefully may guess (c) or (d) as "business-sounding" answers.

**Medium — application:**

- Q7: A retailer finds that stores with more square footage have higher total sales (r = 0.88). A competitor concludes: "Larger stores cause more sales — we should expand all our stores." What is the most important missing piece of evidence?
  *(a) Whether the correlation is positive or negative  (b) Whether sales per square foot also increases with store size, or whether bigger stores are just in higher-footfall locations  (c) Whether the r value is statistically significant  (d) Whether total sales were measured in the same currency across stores)*

- Q8: You produce a crosstab of commute method (car / public transport / cycle) by income bracket (low / medium / high). You want to understand whether higher-income earners are more likely to drive. Which percentages do you compute?
  *(a) Column percentages — because income is in the columns  (b) Row percentages — because you're asking, within each income bracket, what percentage drives  (c) Cell percentages — because you want to see the whole table at once  (d) It doesn't matter — both tell the same story)*

**Hard — conceptual, requires genuine thought:**

- Q9: You analyse data across 50 countries and find that countries with higher smartphone penetration have lower child mortality rates (r = −0.83). A public health researcher concludes: "Smartphone access reduces child mortality." A statistician responds: "This is spurious." Who is right?
  *(a) The researcher — r = −0.83 is very strong, so the relationship is real  (b) The statistician — ecological correlations are always spurious  (c) Neither: the correlation is real but it doesn't prove causation; both variables likely reflect a third factor (development level); and the ecological unit of analysis (country average) cannot support conclusions about individual-level mechanisms  (d) Both — high correlations are always causal, but country-level data shouldn't be used)*

Q9 is the sharpest question in the set. The correct answer (c) requires students to hold three ideas simultaneously: the correlation is real (it exists in the data), it may not be causal (a confound is likely), and the ecological unit makes individual-level causal inference impossible regardless of strength. Students who choose (a) haven't absorbed the chapter's core message. Students who choose (b) have over-corrected — not all ecological correlations are spurious. (b) is a common learner misconception worth addressing explicitly.

**Instructor acts on results (5 minutes)**

**Q1–Q6 are retrieval practice.** If most students answer correctly, move on immediately. If Q3 produces a split (many students not knowing that both CORREL and PEARSON work), give a 20-second clarification — this is the kind of mechanical confusion that will cause problems in Excel labs. If Q1–Q6 are failing broadly, the reading did not land — acknowledge it, adjust Part 3 to provide more scaffolding for the causal reasoning task.

**Q7–Q9 are diagnostic.** Q8 (which percentage to use) splits rooms regularly — the confusion between "what is in the columns" and "what question you're answering" is fundamental. If the room splits on Q8, use the buffer to resolve it with a concrete example before Part 3. Q9 should not be resolved by a mini-lecture — let Part 3 surface the answer through the spurious correlation gallery.

This is formative assessment in action, consistent with Black & Wiliam's (1998) evidence that real-time feedback loops are among the highest-leverage interventions in learning. The weekly quiz format is supported by Farmus, Cribbie & Rotondi (2020): weekly in-class quizzes significantly moderated the flipped classroom advantage in introductory statistics (g = 0.43, DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)).

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

Two or three volunteers present their solutions to T1 and T2. Others ask questions. T3 (Simpson's Paradox) is held back — it surfaces naturally in Part 4 if any submitted dataset produces the phenomenon, and is used as the bridge forward in Part 5 if it doesn't.

The instructor's role here is to prompt, not narrate: *"Which manager in T1 is right — or are they both right?"* *"What additional data would you need to strengthen the chocolate-Nobel claim in T2?"* *"Did anyone get a different answer for (d)?"*

The 10-minute buffer is explicit and named. It absorbs: slow starts, extended debate on T2(d) (whether a second confounded correlation strengthens or weakens the first), or re-covering Q8 if the row/column percentage distinction didn't land in the quiz. If none of these apply, the buffer compresses and Part 3 starts early.

**If the quiz showed Q7–Q9 splitting the room:** spend the buffer on Q8 (crosstab orientation) or Q9 (ecological correlation). These are the conceptual pivots the rest of the session depends on.

Students are doing retrieval practice on crosstab mechanics and correlation computation so that the pair-work can focus on causal reasoning, not calculation. Peer presentation activates the **testing effect** (Roediger & Karpicke, 2006): retrieving and articulating learned material strengthens long-term retention more than passive review.

---

### Part 3 — Pair Work (25 minutes)

Each pair is assigned one of two tasks — the **spurious correlation gallery** format — drawing on both the pre-class datasets and a set of provided "gallery" examples.

**Gallery examples (instructor prepares in advance — 4–5 famous spurious correlations):**
- Per capita cheese consumption and death by bedsheet tangling (Tyler Vigen dataset)
- Nicolas Cage films released per year and pool drownings in the US
- Organic food sales and autism diagnoses in the US
- Correlation between margarine consumption and divorce rate in Maine (r = 0.99)
- Smartphone penetration and Nobel Prize laureates by country

**Roles: advocate and sceptic.** The advocate argues for the strongest possible causal interpretation of the assigned correlation. The sceptic tries to tear it down — naming specific confounders, alternative mechanisms, or data problems that would explain the correlation without causation. Roles swap at the 12-minute mark.

**Deliverable — three things, no more:**
1. The best causal story for the assigned correlation (one sentence — make it sound plausible)
2. The single most damaging confounder (one sentence — what else explains this?)
3. One specific piece of evidence that would move you from "suspicious" to "confident" about causation

**Framing for the task:**

> *"Your job first is to be the most compelling possible advocate for causation. Pretend you're writing the press release. Then your partner destroys it. The goal is not to win the argument — it's to understand what makes a causal claim credible versus what makes it merely a good story."*

If pairs are stuck constructing the causal story, the instructor can prompt: "What is the mechanism? How would X get from here to Y — step by step, biologically, economically, behaviourally?" A causal claim without a mechanism is a correlation in disguise.

**One additional prompt for pairs:** Look at your partner's submitted dataset from the pre-class work. Is there a correlation in it that looks compelling? Apply the same framework: best causal story → single strongest confounder → evidence that would make you confident. This connects the gallery exercise to real data the student chose.

The constrained deliverable (three outputs, no more) is deliberate. Lovett & Greenhouse (2000) identify mental overload as a direct inhibitor of learning efficiency; the advocate/sceptic structure already imposes cognitive demand — the deliverable must be tight to leave room for the reasoning itself.

---

### Part 4 — Peer Discussion (20 minutes)

Each pair presents in ~2.5 minutes:
- Their assigned correlation (stated briefly)
- The best causal story they could construct
- The confounder that most damages it
- What evidence they'd need to be convinced

The student who submitted a related dataset (if any) then responds: did the same causal temptation appear in their data? Did the confounder apply?

This is the highest-value exchange in the session. Students encounter multiple spurious correlations in rapid succession, each with its own mechanism and its own confounder — the cognitive effect is cumulative. By the fourth or fifth pair, students should be spontaneously asking "but what else changes when X changes?" without being prompted. That spontaneous question is the target: it means the causal scepticism has become habitual, not just recalled.

This structure draws on Vygotsky's (1978) **zone of proximal development**: students are constructing and dismantling causal claims in public, with peers who hold different contextual and disciplinary knowledge. A student from a biology background may identify a biological mechanism that an economics student missed. A student familiar with Singaporean data may know that smartphone penetration in that dataset is confounded by a specific government subsidy programme that has no parallel elsewhere.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop on this session first:**

*"We spent 25 minutes arguing for causal claims we didn't believe. What did that feel like — and why does it matter?"*

One sentence from each pair on what made a causal story compelling even when they knew it was spurious. Synthesise into: the strength of a mechanism is not the same as evidence for causation. A compelling story is easy to construct. Evidence is what's hard.

Then surface the T3 concept if it didn't appear in Part 4:

*"One thing we didn't discuss: what happens when a correlation is positive in every subgroup but negative in the aggregate? Does anyone's dataset show that?"*

Name Simpson's Paradox explicitly if it hasn't come up. Give one sentence on the implication: you must always ask whether an aggregate correlation is telling a consistent story across subgroups, or whether the composition of the sample is driving the result.

Then one question to leave them with — don't answer it today:

> *"You've seen that correlation is easy to find and causation is hard to establish. But business decisions can't wait for randomised controlled trials. At what point does a correlation become actionable — and who decides?"*

This is the bridge into Week 10 (decision trees under uncertainty) and the regression weeks (Weeks 14–15). It also connects to the exam's style of question: students will be asked to interpret a correlation in a business context and say what it supports — not what it proves.

One question. Not three. Working memory is depleted at the end of 90 minutes.

---

## After Class (~30 min)

Students write a short reflection — posted to the LMS, formatted as a public social media post — about one correlation from the session:
- What was the correlation?
- What was the best causal story — and why was it compelling?
- What undermined it?
- At what threshold would you act on a correlation like this, even without proof of causation?

**Format constraint:** write it as if posting to LinkedIn or a data science community. One to three paragraphs, a headline, something a stranger could engage with. The discipline of writing publicly forces students to commit to a position rather than hedging every sentence.

Other students are expected to leave at least one comment — identifying a confounder the poster missed, proposing a different mechanism, or naming a comparable example from their own experience. The peer comment is the consolidation mechanism: articulating why a causal story is wrong is harder and more retention-building than agreeing that it might be.

Optional further reading: Vigen, T. (2015). *Spurious Correlations.* Hachette Books. (The gallery in Part 3 draws on this source — the book is short and worth reading in full.)

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Cross-national dataset from open data portal | Ausubel (1968): self-relevance and prediction anchor new material; cross-national constraint sharpens Vygotskian knowledge asymmetry in Part 4 |
| "What causal story is most tempting" in pre-class submission | Bjork (1994): desirable difficulty — committing to a prediction before analysis creates a memorable cognitive event when the prediction fails |
| Reading scoped to §3.1–3.4; pivot charts deferred to Block 2 | Fischer et al. (2023): tool complexity before conceptual grounding impedes learning; ecological correlation (§3.4) is the conceptual move that must land before Excel labs add value |
| Worked example placed before T1–T3, marked optional for confident students | Rosenshine (2012): worked examples should precede independent practice — the three-step structure (causal story → confounder → evidence threshold) must be modelled before students are asked to produce it. Marked optional per Kalyuga et al. (2003): students who can already complete T2(c) without it do not benefit and may disengage. Active-watching video prompts ensure the Smeets TEDx video is a retrieval exercise, not passive viewing. |
| Quiz includes Q6 (ecological correlation trap) and Q9 (ecological vs causal) | Black & Wiliam (1998): formative diagnosis; ecological correlation is consistently misunderstood — surfacing it early prevents it calcifying as a misconception |
| T2 uses actual Messerli (2012) chocolate-Nobel finding | Authenticity increases engagement and transfers the lesson to real peer-reviewed literature, not just toy data; also signals that journals are not immune to causal overclaiming |
| T3 introduces Simpson's Paradox | Bjork (1994): desirable difficulties — Simpson's Paradox is genuinely counterintuitive; discovering it through computation is more durable than being told about it |
| Spurious correlation gallery: advocate-then-sceptic structure | The move of constructing the strongest possible case for a claim you're about to demolish is a core professional skill (devil's advocate, pre-mortem, red-teaming); assigning the advocate role makes it non-optional |
| Roles swap at 12 minutes | Prevents one partner doing all the sceptical work; forces both to inhabit both positions; mirrors professional peer review |
| Three-output deliverable: story → confounder → evidence threshold | Bloom levels 4–5 (analysis, evaluation); the evidence threshold question is the hardest — most students can name a confounder but struggle to specify what evidence would move them |
| Simpson's Paradox planted in debrief, not taught in tutorial | Bjork (1994): unresolved counterintuitive questions create retrieval motivation; if it appears in Part 4, the debrief names it; if not, it returns in Week 14 (regression) as a named phenomenon |
| Single bridge-forward question about actionable correlations | Working memory is depleted at end of 90 minutes; one question that connects to Weeks 10, 14, 15 plants a more durable hook than three separate connections |
| LMS post in social media format with peer comment | Constructivist consolidation (Piaget, 1952); peer comments activate testing effect (Roediger & Karpicke, 2006); public format forces position commitment |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Act only on contested questions; Q8 (crosstab orientation) and Q9 (ecological correlation) are most likely to need time |
| Tutorial review | 15 min | T1–T2 only; T3 (Simpson's Paradox) held for debrief or bridge |
| Buffer (explicit) | 10 min | Absorbs slow starts, extended debate on T2(d), or re-covering Q8 if the row/column distinction didn't land |
| Pair work (spurious correlation gallery) | 25 min | Advocate/sceptic roles; swap at 12 min; gallery + partner's dataset |
| Peer discussion | 20 min | ~2.5 min per pair; dataset owner responds if applicable |
| Instructor debrief | 10 min | Close the loop, name Simpson's Paradox, one unanswered bridge-forward question |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

This section documents live tensions in the lesson design — choices that could have gone differently, and the reasoning behind what was chosen.

---

### 1. The advocate role creates the risk of students arguing for claims they find offensive.

The spurious correlation gallery asks students to construct "the best causal story" for correlations that may, in some cases, touch on sensitive topics — correlations between race and outcome variables, or between nationality and economic behaviour, are exactly the type that appear in both genuine and spurious research. The gallery examples in this plan (Nicolas Cage films, cheese consumption, margarine and divorce) avoid that category deliberately.

**Design implication:** the instructor should screen submitted datasets before assigning gallery pairings. A dataset that correlates a demographic variable with a negative outcome (e.g., immigration rate and crime, or ethnicity and employment) should not be assigned for the "construct the best causal story" task. It should be held back and addressed differently — the causal reasoning framework still applies, but the advocacy framing is inappropriate. The screening takes 10 minutes before class and prevents a situation where a student is instructed to argue for a claim that dehumanises a group represented in the room.

**Trade-off:** pulling a student's submitted dataset from the gallery (without explanation) may feel arbitrary to them. A brief private word before class ("I'm using your dataset for a different purpose in Part 4") is sufficient.

---

### 2. The correlation-causation lesson is one students think they already know.

"Correlation is not causation" is one of the most widely repeated statistical phrases in popular discourse. Year 3 students in a Business Analytics course have almost certainly heard it. The risk is that they arrive at this seminar believing they already understand the concept — and therefore engage with the lesson at the level of performance rather than genuine inquiry.

**The structural fix:** the tutorial problems (T1–T3) probe beneath the slogan. T1 asks students to distinguish row from column percentages — a mechanical test that reveals whether they understand what a crosstab is actually computing. T2 asks whether a second correlated variable strengthens the causal case — the correct answer (no, it weakens it) contradicts the intuition students who "already know" the concept will have. T3 introduces a case (Simpson's Paradox) where the correlation-causation distinction isn't the issue — the issue is that the aggregate correlation doesn't describe any subgroup. These problems are designed to find the edge of what students actually understand, not what they believe they understand.

**Design implication:** if the quiz shows Q1–Q6 universally correct in the first 30 seconds, the instructor should treat that as a red flag, not a green light. It may mean students are pattern-matching to expected answers. The diagnostic value in Q7–Q9 is more reliable.

---

### 3. The spurious correlation gallery risks becoming entertainment rather than analysis.

The famous spurious correlations (Nicolas Cage, margarine, cheese) are funny. Students will laugh. The risk is that laughter substitutes for analysis — students leave having enjoyed the examples without having done the cognitive work of explaining *why* they're spurious and *what evidence would change their mind*.

**The structural fix:** the deliverable requires a specific evidence threshold (Output 3), not just a named confounder. Naming a confounder ("the correlation is explained by wealth") is relatively easy. Specifying what data you'd need to be convinced of causation despite the confounder ("a controlled experiment varying chocolate consumption while holding GDP constant") is harder and requires genuine reasoning. The instructor should push on this in Part 4: "What would convince you? Not that it's possible — what would you actually need to see?"

**Trade-off:** the humour in the gallery examples is not a bug — it reduces anxiety and signals that statistics can be surprising and even absurd. The instructor's job is to ensure the analysis follows the laughter, not stops at it.

---

### 4. Crosstab orientation (row vs column percentages) is memorised rather than understood.

Students frequently learn a rule ("row percentages answer row questions") that they can apply but cannot explain. The rule works in standard cases but fails when the table is transposed or when the research question is ambiguous. If a student can't explain *why* they chose a particular orientation — only that they followed the rule — they will produce the wrong table in an exam question that flips the framing.

**Design implication:** T1(a)–(b) explicitly ask students to state what question each percentage answers, not just to compute it. The presentation of T1 in Part 2 should push on this: "Don't tell me which percentage you calculated — tell me what question a manager would be asking that makes this the right percentage." Students who can answer that question understand crosstabs. Students who can only compute them don't.

**Trade-off:** this takes more time in Part 2 than a mechanical check-your-answers session. The 10-minute buffer is there partly to absorb this — crosstab orientation is tested on the exam and worth the time.

---

### 5. The cohort's multinational composition is a double-edged asset in this session.

Week 3 is the first session where the cross-national dataset constraint really bites: students are analysing relationships in datasets from countries they know little about. A student from South Korea analysing a Berlin public transport usage dataset may not know that Berlin's transport network was geographically bifurcated until 1990, which affects any analysis of east-west usage patterns. A student from Germany analysing Singaporean housing data may not know that 80% of Singaporeans live in state-built HDB flats, which makes the housing market unlike any European equivalent.

**The opportunity:** these knowledge gaps produce precisely the kind of contextual challenge that makes the causal reasoning exercise difficult in the right way. A correlation that seems obvious in the context of German urban planning may be entirely puzzling without that context — and the puzzle is the point.

**The risk:** a student who doesn't know enough about the dataset's context may construct a causal story that is not merely wrong but incoherent — missing a fundamental institutional fact that changes the interpretation entirely. The dataset owner's response in Part 4 is the correction mechanism, but it only works if the owner is attending carefully during the other pairs' presentations.

**Design implication:** the instructor should explicitly frame Part 4 as an accuracy-checking exercise, not just an appreciation of peers' work. The dataset owner is not congratulating the pair — they are assessing whether the pair's causal story is coherent in context. A correction delivered politely but precisely ("actually, that correlation is explained by the fact that Berlin's eastern districts were planned under a different economic system, which produced a different commercial structure") is the most valuable output of the session.

---

## References

- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
- Farmus, L., Cribbie, R.A. & Rotondi, M.A. (2020). The flipped classroom in introductory statistics. *Journal of Statistics Education*, 28(3), 316–325. DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Fischer, J., Torcasio, S., Sweller, J. & Kalyuga, S. (2023). Flipped classroom design: Managing cognitive load. *BMC Medical Education*, 23(1), 345. DOI: [10.1186/s12909-023-04325-x](https://doi.org/10.1186/s12909-023-04325-x)
- Kalyuga, S., Ayres, P., Chandler, P. & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Messerli, F.H. (2012). Chocolate consumption, cognitive function, and Nobel Laureates. *New England Journal of Medicine*, 367(16), 1562–1564.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Vigen, T. (2015). *Spurious Correlations.* Hachette Books.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
