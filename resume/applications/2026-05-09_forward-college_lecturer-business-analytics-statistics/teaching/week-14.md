# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 14: Regression Analysis — Estimating Relationships
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Estimate a simple linear regression model (OLS) in Excel and Python, and interpret the output: intercept, slope, R², and the regression equation
- Use a fitted regression model to generate point predictions
- Identify when the linear relationship assumption is unreasonable for a given dataset
- Critique a claim that "correlation implies causation" by identifying a plausible confound

These map to ST2187 syllabus topic 11 (regression analysis) and build on the correlation analysis introduced in Week 3. Students who completed Week 3 can describe linear relationships; this week they can model and quantify them.

These objectives operate at the **application and analysis** levels of Bloom's Taxonomy — not just interpreting a pre-fitted model, but building, using, and questioning one.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 10 — read the following sections only:
- §10.1 Overview of regression analysis (pp. 508–514)
- §10.2 Simple linear regression — model and estimation (pp. 514–526)
- §10.3 Measuring goodness of fit — R² and standard error of estimate (pp. 526–533)
- §10.4 Regression in Excel (pp. 533–540)

The statistical inference sections (§10.5–10.6: t-tests on coefficients, F-test) are the topic of Week 15. This week is estimation; next week is inference. The division is deliberate — students who try to interpret p-values before understanding what the coefficients mean confuse both.

*Rationale:* the regression output table from Excel's Data Analysis ToolPak is dense. Students need to have seen it before class. Pre-work reading of §10.4 is not optional.

**Videos (~20 minutes total):**
- [Linear Regression — StatQuest](https://www.youtube.com/watch?v=nk2CQITm_eo) (12 min) — intuition for OLS. *Active watching: when StatQuest explains what "least squares" means — minimising the sum of squared residuals — pause and write in one sentence: what is a residual? This concept is what T2 tests.*
- [R-squared explained — StatQuest](https://www.youtube.com/watch?v=2AQKmw14mHM) (7 min). *Active watching: when the video shows that R² = 0 means the model explains nothing and R² = 1 means it explains everything, pause and write: what does R² = 0.968 mean in plain language? This is the exact interpretation T1(c) asks for.*

**Worked example (read this before attempting the tutorial problems):**

> **Dataset:** 10 retail stores. X = advertising spend (€000s); Y = monthly sales (€000s).
>
> | Store | Ad spend (X) | Sales (Y) |
> |-------|-------------|-----------|
> | 1 | 1.5 | 45 |
> | 2 | 3.0 | 62 |
> | 3 | 2.0 | 52 |
> | 4 | 4.5 | 75 |
> | 5 | 1.0 | 38 |
> | 6 | 5.0 | 88 |
> | 7 | 2.5 | 58 |
> | 8 | 3.5 | 68 |
> | 9 | 4.0 | 80 |
> | 10 | 6.0 | 95 |
>
> **Fitted model (using Excel Data Analysis → Regression):**
> Sales = 28.4 + 11.2 × AdSpend
> R² = 0.968, Standard Error = 3.1
>
> **Interpretation:**
> - Intercept (28.4): if ad spend is €0, predicted sales are €28,400. (Caution: extrapolation below the data range — this intercept may not be meaningful.)
> - Slope (11.2): for each additional €1,000 in advertising, predicted sales increase by €11,200.
> - R² = 0.968: 96.8% of the variation in sales across stores is explained by variation in advertising spend. This is very high.
>
> **Prediction:**
> A new store plans to spend €3,500 on advertising. Predicted sales = 28.4 + 11.2 × 3.5 = **67.6 (€67,600)**.
>
> **The important question:** does high R² prove that advertising causes sales? No. It is possible that profitable stores (which have high sales) also choose to spend more on advertising — the causality could run the other way. Or a third variable (store location, foot traffic) drives both. R² measures fit, not causation.

*This worked example is marked optional for students who can already interpret a slope, an intercept, and an R² value from a fitted regression output and use the equation to make a prediction. If you answered T0 correctly before reading this, you don't need it. If any of the three interpretations (slope, intercept, R²) felt unclear after the reading, work through the example carefully.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T0 — Entry question (lower floor):*

Before computing anything, answer in your own words:

> You are told: "We ran a regression of exam scores on study hours and got a slope of 6.2." Write two sentences: one that correctly states what this slope means, and one that states something it does NOT tell you.

No formula or computation needed — just the reading. A student who completed ST104a will have seen slope interpretation before; a student who hasn't will be engaging with it for the first time. The T0 answer reveals which situation applies, so the tutorial review can adjust accordingly.

This lower floor matters because Week 14 assumes the pre-work reading was done. If the reading was skimmed, T0 surfaces that immediately — before T1–T3 give the impression that the concept has landed.

*Self-check for T0:* One correct sentence: "A slope of 6.2 means that each additional hour of study predicts an increase of 6.2 points in exam score, on average, holding all else constant." One example of what it does NOT tell you: it does not tell you that studying *causes* higher scores (confounds like prior ability could explain the relationship), and it does not tell you the score for a specific student — only the average predicted score.

*T1 — Fitting by hand (estimation only):*

*The worked example's slope interpretation ("for each additional €1,000 in advertising, predicted sales increase by €11,200") is the same structure as T1(c). The R² interpretation you wrote during the StatQuest video pause ("R² = 0.968 means 96.8% of variation is explained") applies directly to T1(a) and (the implicit question in T2).*
> Dataset (n = 6): X = hours studied, Y = exam score.
> X: 1, 2, 3, 4, 5, 6 | Y: 45, 52, 58, 65, 72, 78
>
> (a) Compute the correlation coefficient r. Is the linear relationship strong?
> (b) Using Excel Data Analysis, fit Y on X. Write down the regression equation.
> (c) Interpret the slope in context. What does a one-hour increase in study time predict for exam score?
> (d) Predict the exam score for a student who studies 7 hours. Comment on the reliability of this prediction.
> (e) Predict the score for a student who studies 0 hours. Is this prediction meaningful?

T1(d)–(e) introduce extrapolation risk — predicting outside the range of the data. T1(d) at 7 hours is a modest extrapolation; T1(e) at 0 hours is a conceptual test.

*T2 — R² and residuals:*
> Using the fitted model from T1:
>
> (a) What is R²? What percentage of variation in exam scores is unexplained?
> (b) Compute the residuals for each observation. (Residual = actual − predicted.)
> (c) Plot residuals against X (a residual plot). What pattern should you see if the linear model is appropriate?
> (d) If the residuals show a curved pattern (first positive, then negative, then positive), what does this suggest?

T2 introduces residual analysis — the diagnostic tool for checking whether the linear model is appropriate. This is foundational for Week 15.

*T3 — Causation vs. correlation (2025 context):*

> In 2024–2025, several major companies mandated a return to office (RTO). Amazon announced in September 2024 that employees must return to the office five days a week from January 2025, citing "strengthened collaboration and culture." JPMorgan Chase followed with a similar mandate in early 2025. Both companies cited internal data showing correlations between in-person presence and various productivity and performance metrics.
>
> Suppose an analyst at a large firm fits the following regression using 18 months of employee data (n = 2,400 employees):
>
> Productivity score = 42.0 + 3.1 × (days per week in office), R² = 0.18
>
> (a) Interpret the slope and R² in plain English. Is R² = 0.18 high or low for this type of study?
>
> (b) A manager reads the output and says: "Our data shows that each additional day in the office predicts a 3.1-point increase in productivity score. This proves that returning to the office improves performance." Identify at least two specific problems with the causal claim.
>
> (c) Identify the most plausible confounding variable in this regression. Describe the mechanism — how might this variable affect both office attendance and productivity score?
>
> (d) The analyst adds a new control variable: the employee's prior-year performance rating (measured before the RTO policy). After adding this control, the slope on days-in-office falls from 3.1 to 0.7 and is no longer statistically significant (p = 0.23). What does this reveal? What does it suggest about the original regression?
>
> (e) A critic argues: "Maybe the employees who come in more are the ones who were already high performers — and they come in more because they enjoy their work, not because the office makes them productive." Explain what type of bias this describes and what data you would need to rule it out.
>
> (f) Amazon's RTO decision also increased employee attrition, particularly among high-performing remote workers who lived far from offices. If higher-performing remote employees leave after the RTO mandate, what happens to the average productivity score of the in-office group over time — and how does this affect the regression?

T3 uses a verified 2025 policy context: Amazon's five-day RTO mandate was announced September 2024 and implemented January 2025; JPMorgan's mandate was announced January 2025 (both widely reported by Reuters, WSJ, FT). The regression numbers are illustrative. This question updates T3 from a generic example to one students have likely read about, converting the correlation-causation framework into a live policy debate they can engage with from their own context. Part (d) — the control variable reducing the slope to non-significance — is the most important result: it shows how an apparent relationship can largely disappear once prior performance is accounted for.

*T4 — Boundary case: what happens when the slope is zero or the intercept is misleading:*

> A researcher fits a simple linear regression of annual salary (€) on age (years) for a sample of 120 employees at a large company. The output is:
>
> Salary = 25,000 + 800 × Age, R² = 0.08
>
> (a) Interpret the slope. What does it predict about the salary of a 40-year-old compared to a 39-year-old?
> (b) Interpret the intercept. What would the model predict for a newborn child (age = 0)? Is this meaningful? What is the technical term for using a model outside the range of the training data?
> (c) R² = 0.08 means only 8% of salary variation is explained by age. A colleague says: "This regression is useless." Another says: "The slope is still informative." Who is right? What additional context would help evaluate whether 8% is meaningful?
> (d) A new hire, age 23, has a salary of €48,000. The model predicts €43,400. What is the residual?
>
> *Solution:* Residual = 48,000 − 43,400 = **€4,600.** This employee earns more than the model predicts — a positive residual.
>
> (e) A negative slope (salary decreasing with age) is theoretically impossible in this context. However, the model produces a negative slope when fit to a subset of employees in the technology division. What might explain a negative slope within that division, even though the overall relationship is positive?

*T5 — Multi-step: build, predict, and evaluate residuals:*

> A property company has the following data on apartments (n = 8): square metres (X) and monthly rent in €:
>
> | Apt | Size (m²) | Rent (€/month) |
> |-----|----------|----------------|
> | 1 | 40 | 850 |
> | 2 | 55 | 1,050 |
> | 3 | 62 | 1,180 |
> | 4 | 70 | 1,400 |
> | 5 | 48 | 920 |
> | 6 | 85 | 1,650 |
> | 7 | 58 | 1,100 |
> | 8 | 77 | 1,520 |
>
> (a) Using Excel Data Analysis, fit rent on size. Write the regression equation and interpret the slope.
>
> *Solution (approximate, students compute in Excel):* Rent ≈ 256 + 16.4 × Size. Slope: each additional m² predicts approximately €16.40 more in monthly rent, on average.
>
> (b) What is R²? How much of the variation in rent is explained by apartment size?
> (c) Compute the residual for Apartment 4 (70m², €1,400). Is the apartment over- or under-priced relative to the model?
> (d) Plot the residuals against size (X). Describe what a random scatter pattern looks like and whether your residual plot shows it.
> (e) Predict the monthly rent for a 100m² apartment. Comment on the reliability of this prediction relative to predicting rent for a 65m² apartment.
> (f) A new apartment of 65m² is listed at €1,600/month. Using your model, is this significantly higher than predicted? What percentage above prediction is it?

*T6 — Comparison: high R² versus low R² — when does it matter:*

> Two regression models are presented:
>
> **Model 1:** Predicting tomorrow's temperature (°C) from today's temperature. n = 365 daily observations. R² = 0.78. Slope = 0.82.
>
> **Model 2:** Predicting annual corporate earnings growth (%) from the prior year's earnings growth. n = 200 companies. R² = 0.06. Slope = 0.14.
>
> (a) In Model 1, R² = 0.78. What percentage of tomorrow's temperature variation is *unexplained* by today's temperature? What explains the rest?
> (b) A meteorologist says: "R² = 0.78 is excellent for a single-predictor model." An economist says: "R² = 0.06 is too low to be useful." Are they both right? Does the usefulness of R² depend on the domain?
> (c) In Model 2, despite R² = 0.06, the slope is statistically significant (p = 0.003). Is it meaningful to have a statistically significant but practically weak predictor?
> (d) Suppose you reversed the regression in Model 1 — predicting today's temperature from tomorrow's (using the future to predict the past). Would R² change? Would the slope change?
>
> *Answer on R²:* R² is the same regardless of which variable is called X and which Y — the correlation between X and Y is symmetric. The slope would change (slope of Y on X ≠ slope of X on Y unless r² = 1).
>
> (e) A business analyst proposes using Model 2 to predict a specific company's earnings growth next year. The slope is 0.14. If last year's growth was 20%, what is the model's point prediction for next year? Given R² = 0.06, what caveat would you attach to this prediction?

*T7 — Causation vs. correlation: construct and dismantle a causal claim:*

> An analyst at a government ministry reports: "We have found that countries with higher rates of secondary school enrolment (X) have higher GDP per capita (Y). The correlation is r = 0.82 and the regression slope is €4,200 per percentage point of enrolment. Our recommendation is to increase secondary school enrolment to drive economic growth."
>
> (a) Is the correlation (r = 0.82) plausible? Construct the strongest possible causal argument for the recommendation.
> (b) Identify at least two confounding variables that could explain the relationship without secondary education causing GDP growth.
> (c) The regression is at the country level (n = 90 countries). What type of correlation is this? Why does the ecological unit of analysis create additional problems for causal inference?
> (d) The analyst adds a control variable: initial GDP per capita in 1990 (a measure of how wealthy countries already were). After adding this control, the slope on secondary enrolment drops from 4,200 to 850 and is no longer statistically significant. What does this reveal?
> (e) A policy maker says: "Even if it's not proven to be causal, an r = 0.82 is strong enough to act on." Write a two-sentence response that acknowledges the pragmatic argument while stating what specific evidence would make the causal claim more credible.

**Pre-class submission (on the course portal):**

Find a relationship that someone (a news article, a study, a company) has described as causal — "X causes Y" or "X leads to Y." Submit:
1. What is X, what is Y?
2. Why might the relationship be correlation rather than causation?
3. What variable would you add to test whether the relationship is spurious?

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

**Easy — vocabulary and recall:**

- Q1: In simple linear regression Ŷ = a + bX, what does b represent?
  *(a) The intercept — the predicted value of Y when X = 0  (b) The slope — the change in predicted Y for a one-unit increase in X  (c) The R² — the proportion of variance explained  (d) The standard error of the estimate)*

- Q2: R² = 0.82 means:
  *(a) The correlation coefficient is 0.82  (b) 82% of variation in Y is explained by variation in X  (c) The slope is 0.82  (d) The model predicts 82% of observations correctly)*

- Q3: The residual for an observation is:
  *(a) The predicted value  (b) Actual Y minus predicted Y  (c) The slope times the error  (d) R² times actual Y)*

- Q4: If the correlation between X and Y is −0.9, then in the regression of Y on X:
  *(a) The slope must be positive  (b) The slope must be negative  (c) The slope could be either sign  (d) R² will be 0.81)*

- Q5: Extrapolation in regression means:
  *(a) Fitting a curved model  (b) Predicting outside the range of the training data  (c) Using too many predictor variables  (d) Using a model with high R²)*

- Q6: Which Excel function fits a linear regression line to a scatter chart automatically?
  *(a) SLOPE()  (b) INTERCEPT()  (c) LINEST()  (d) All of the above can give slope and intercept separately)*

**Medium — application:**

- Q7: A regression model gives Ŷ = 12 + 3.5X. For X = 10, the predicted Y is:
  *(a) 47  (b) 47.5  (c) 35  (d) 50)*

- Q8: R² for a model is 0.05. This means:
  *(a) The model is useless — throw it away  (b) 5% of the variation in Y is explained by X — the relationship is weak but may still be present  (c) The slope is 0.05  (d) 95% of the model is wrong)*

Q8 tests whether students understand that low R² doesn't automatically mean no relationship — it means the linear model explains little of the variance. For some questions (e.g., what explains city murder rates?), an R² of 0.05 is meaningful.

**Hard — conceptual:**

- Q9: A fitted regression shows R² = 0.90 and a steep positive slope between ice cream sales (X) and drowning deaths (Y). The correct interpretation is:
  *(a) Ice cream causes drowning — ban ice cream near water  (b) Drowning risk causes people to eat more ice cream  (c) A third variable (summer temperature / season) drives both  (d) The regression is invalid because Y should not be regressed on X)*

**Instructor acts on results (5 minutes)**

Q4 — if students answer "slope must be 0.81" instead of "slope must be negative, R² = 0.81", they're confusing r and r². Fix it quickly. Q9 is the ice cream–drowning confound — name it as the session's running example for Part 3.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T1(d) extrapolation (7 hours) vs T1(e) extrapolation (0 hours): 7 hours is a modest extrapolation and may be defensible; 0 hours produces a negative exam score prediction (if the intercept is below zero), which is clearly nonsensical. The point: extrapolation is not always wrong, but it always carries additional uncertainty not captured by R².

T2 residual plot: draw on the board what a "good" residual plot looks like (horizontal band, random scatter, no pattern) vs. what a curved residual plot implies (the relationship is non-linear; a quadratic or log transform may be better). This is the diagnostic skill for Week 15.

T3 held for Part 3.

Buffer: if T1(d)–(e) produce debate about when extrapolation is acceptable, stay with it. This is worth 10 minutes.

---

### Part 3 — Prediction Game + Confound Hunt (25 minutes)

**Part A — Prediction game (10 minutes):**

The instructor projects a scatter plot of a real dataset (chosen in advance — e.g., GDP per capita vs. life expectancy from World Bank data, or city size vs. average commute time).

Students first estimate the regression line *by eye* — drawing a line on a printed copy or estimating the slope and intercept without computing. Then the instructor reveals the fitted OLS line.

Questions:
- Where did your eye get it right? Where did it go wrong?
- What does R² tell you that your eye couldn't judge?
- Is there an observation that is pulling the line noticeably?

**Part B — Confound hunt (15 minutes):**

Each pair receives one causation claim from the pre-submission gallery (not their own submission). Their task:
1. State the claimed relationship (X → Y)
2. Identify the most plausible confound Z
3. Explain how controlling for Z would affect the regression: "If we added Z to the model, the slope for X would probably [increase / decrease / change sign / disappear]"

The last point is a preview of multiple regression (Week 15). Students don't need to run it — they need to reason about it. This activates the conceptual foundation for coefficient interpretation in the presence of covariates.

---

### Part 4 — Peer Discussion (20 minutes)

Pairs present their confound hunt results. The student who submitted the original causation claim responds: "Is the confound Z plausible? Is there a better one?"

The instructor tracks: how many of the confounds proposed are actually potential mediators (Z is on the causal path from X to Y) rather than true confounds (Z drives both X and Y independently)? This distinction will recur in Week 15's "confound vs. mediator" discussion but is worth planting now.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop:**

*"Regression tells us the best linear fit and how much of Y's variation X explains. What are the three things it does NOT tell us?"*

1. Whether the relationship is causal (Q9 — ice cream and drowning)
2. Whether the model fits the data well everywhere (residuals — T2)
3. Whether the prediction is reliable outside the data range (extrapolation — T1(d)+(e))

**Bridge forward to Week 15:**

> *"We have the coefficients. Next week we ask: are they statistically significant? Could a slope of 11.2 have arisen by chance if the true slope were 0? And what happens to the slope on advertising when we add a second variable — say, store location? Does the coefficient change? Can it change sign? These are the questions statistical inference on regression answers."*

---

## After Class (Student Post-Work, ~30 minutes)

Students write an LMS post on one of:
- The causation claim they submitted before class: now that they've identified the confound, how would they communicate this finding to someone who made the original claim?
- What the prediction game revealed about using intuition vs. statistics
- A dataset from their own experience where regression was (or could be) applied — and the most important confound to control for

Peer response: one comment that suggests a different confound or a way to test whether the relationship is causal.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Week 14 is estimation only; Week 15 is inference | Cognitive load (Sweller, 1994): splitting estimation and inference into two weeks prevents students from prematurely fixating on p-values before understanding what the coefficients mean; the exam tests both separately |
| Prediction game (estimate by eye first) | Bjork (1994): desirable difficulties — generating an answer before knowing the correct one deepens encoding; students who drew their own line and were wrong remember the OLS line better than students who saw it first |
| Confound hunt uses student-submitted causation claims | Ausubel (1968): self-relevance; the claim a student found is more interesting to them than a textbook example; 40+ nationalities produces causation claims from press in 15+ countries |
| T2 introduces residual plots | Residual analysis is the diagnostic tool that Week 15 relies on; introducing it as a pre-work concept and reinforcing it in tutorial review means Week 15 doesn't have to re-teach it |
| Ice cream / drowning as canonical confound example | Memorable and slightly absurd — produces the "that's obviously wrong" reaction that makes the abstract concept of confounding concrete; use it as the reference case throughout the confound hunt |
| Part 4 asks original claim submitter to respond | Vygotsky (1978): ZPD — the claim submitter has contextual knowledge the analyst pair doesn't; this asymmetry is productive, mirrors Week 2 dataset exchange structure |
| Bridge forward names specific questions Week 15 will answer | Ausubel (1968): advance organiser — framing what comes next before it arrives reduces disorientation and gives the inference machinery a purpose before it's introduced |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Q4 (r vs r²); Q8 (low R² ≠ useless); Q9 (ice cream confound) |
| Tutorial review | 15 min | T1(d)+(e) extrapolation; T2 residual plots |
| Buffer (explicit) | 10 min | Extended extrapolation debate or residual plot discussion |
| Prediction game + confound hunt | 25 min | 10 min eye estimate; 15 min pair confound hunt |
| Peer discussion | 20 min | ~2.5 min per pair; original submitter responds |
| Instructor debrief | 10 min | Three things regression doesn't tell you; bridge to Week 15 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Students may confuse correlation and R² with causation even after repeated warnings.

The ice cream–drowning example in the quiz is obvious. The causation claims students bring in the pre-submission are less obvious — they involve plausible mechanisms and real-world authority (published studies, news articles). When the relationship seems sensible, the confounding question is harder.

**Resolution:** the confound hunt (Part 3B) requires students to actively generate the confound, not just identify it. Generation requires genuine reasoning about what drives both X and Y independently. This is different from recognising the error in an obviously absurd example.

---

### 2. The prediction game assumes the instructor can project a scatter plot and reveal the OLS line live.

This requires preparation: a dataset loaded into Excel or Python, a scatter plot already prepared with a "before" (raw data) and "after" (fitted line) version.

**Resolution:** prepare both versions before class. Use World Bank data (GDP per capita vs. life expectancy at birth, latest year available) — it is real, publicly available, and produces a visually obvious positive relationship with a clear influential point (the very poorest countries). The influential point (a country far below the fitted line) adds a natural discussion: "Why is this point below the predicted value? What's the confound?" The answer is often conflict, disease burden, or governance failure — each a genuine third variable.

---

### 3. T1(e) — predicting exam score at 0 hours — may produce a negative intercept.

If the fitted intercept is, say, 38 (not negative), the extrapolation problem is less stark. The worked example uses a dataset where the intercept is positive and meaningful — students may replicate that pattern and not notice the extrapolation issue.

**Resolution:** use a dataset in T1 where the intercept is clearly implausible — e.g., fitting weekly sales on number of employees, where the intercept implies positive sales with zero employees. The implausibility is the lesson.

---

### 4. The confound vs. mediator distinction is introduced informally in Part 4 but not taught formally.

Some pairs will propose mediators (variables on the causal path between X and Y) rather than confounds (variables that drive both X and Y independently). The distinction matters but is not the focus of this week.

**Resolution:** the instructor plants the distinction at the end of Part 4 ("some of what you called confounds are actually mediators — a variable on the pathway from X to Y, not a common cause. We'll formalise that next week") but does not dwell on it. The conceptual seed is sufficient for Week 15 to build on.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Farmus, L., Cribbie, R.A. & Rotondi, M. (2020). The flipped classroom in introductory statistics. *Journal of Statistics Education*, 28(3). DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
