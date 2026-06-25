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

---

## Answer Key

### T0 — Slope interpretation (entry question)

**Correct sentence:** "A slope of 6.2 means that each additional hour of study is associated with a predicted increase of 6.2 points in exam score, on average."

**What it does NOT tell you:** "It does not tell you that studying *causes* higher exam scores — the relationship could be explained by a confound (e.g., motivated students both study more and have higher prior ability), and the slope does not tell you the score for any specific student, only the average prediction."

---

### T1 — Simple regression (hours studied vs exam score)

**(a)** With X: 1, 2, 3, 4, 5, 6 and Y: 45, 52, 58, 65, 72, 78: r ≈ **0.999** — almost perfectly linear. The relationship is extremely strong.

**(b)** Using Excel Data Analysis: **Score ≈ 38.6 + 6.6 × Hours.** (Exact values from OLS: intercept ≈ 38.6, slope ≈ 6.6.)

**(c)** Slope = 6.6: each additional hour of study predicts an average increase of **6.6 points** in exam score. This is the expected difference in exam scores between two students who differ by one hour of studying, according to the model.

**(d)** Predicted score for 7 hours: 38.6 + 6.6 × 7 = **84.8 points.** This is a modest extrapolation just beyond the data range (which goes up to 6 hours). The prediction is reasonably reliable because the relationship is very linear and 7 hours is close to the edge of the training data — but any extrapolation carries additional uncertainty since we cannot verify the model holds outside the observed range.

**(e)** Predicted score for 0 hours: 38.6 + 6.6 × 0 = **38.6 points.** This prediction is of limited meaningfulness: 0 hours is outside the data range (data runs from 1 to 6 hours), and predicting what happens when someone does literally no studying may involve behaviour (e.g., no attendance, prior knowledge only) that differs qualitatively from the student population in the data. The intercept is technically "the predicted score when hours = 0" but should be treated with caution.

---

### T2 — R² and residuals

**(a)** R² ≈ **0.998** (very close to 1, given the near-perfect linear relationship). About 0.2% of variation in exam scores is **unexplained** by study hours — a tiny residual variation.

**(b)** Predicted values and residuals (using ŷ = 38.6 + 6.6x):
| X (hours) | Y (actual) | Ŷ (predicted) | Residual (Y − Ŷ) |
|---|---|---|---|
| 1 | 45 | 45.2 | −0.2 |
| 2 | 52 | 51.8 | +0.2 |
| 3 | 58 | 58.4 | −0.4 |
| 4 | 65 | 65.0 | 0.0 |
| 5 | 72 | 71.6 | +0.4 |
| 6 | 78 | 78.2 | −0.2 |

**(c)** If the linear model is appropriate, residuals plotted against X should show **random scatter around zero** — no systematic pattern. Residuals should be roughly equal in magnitude at all X values (homoskedasticity) and show no trend.

**(d)** A curved pattern in residuals (positive → negative → positive) indicates **non-linearity** — the true relationship is curved, not straight. The linear model is misspecified: a quadratic or other transformation of X is likely needed. This pattern is the key diagnostic: if you see it, the straight-line model is wrong regardless of the R² value.

---

### T3 — Causation vs correlation (RTO context)

**(a)** Slope = 3.1: each additional day per week in the office predicts a 3.1-point increase in productivity score, on average. R² = 0.18 means 18% of the variation in productivity scores is explained by days in office — **low for a study of individual human behaviour**, where many factors (role complexity, tenure, team quality, motivation) affect productivity. R² = 0.18 is not high enough to support strong causal claims, but the slope may still be informative about the direction of association.

**(b)** Two problems with the causal claim: (i) **Reverse causality:** high performers may be more likely to come to the office because they enjoy their work, feel socially engaged, or are in roles (e.g., leadership, sales) that benefit from in-person presence. The productivity advantage precedes office attendance, not vice versa. (ii) **Omitted variable bias:** prior performance, role type, tenure, and team composition are all plausible confounders that predict both office attendance and productivity — the regression slope on office days may be capturing the effect of these omitted variables, not office attendance itself.

**(c)** The most plausible confound is **prior performance / motivation level.** High-performing, highly motivated employees are more likely to both attend the office voluntarily (they are self-directing and engaged) and to score highly on productivity metrics (they are high performers). This creates a spurious positive correlation between office attendance and productivity that would exist even if the office had zero causal effect.

**(d)** The drop from 3.1 to 0.7 (and loss of significance after adding prior performance as a control) reveals **omitted variable bias** in the original regression. Prior performance is a confounder: it was positively correlated with both days in office and productivity score, inflating the apparent coefficient on office attendance. Once prior performance is controlled for, the marginal effect of office attendance shrinks dramatically. This suggests the original 3.1 coefficient was largely capturing the effect of employee quality, not office attendance.

**(e)** This describes **self-selection bias** (a form of omitted variable bias / endogeneity). Employees who choose to come to the office more are systematically different from those who don't — they differ in motivation, role type, commuting distance, and team culture. To rule this out, you would need: (i) a randomised experiment assigning some employees to mandatory in-office and others to mandatory remote work; or (ii) a natural experiment using an exogenous variation in attendance (e.g., a specific team's building lost heating and they worked remotely for a quarter) to compare otherwise-similar employees.

**(f)** If high-performing remote workers leave post-RTO, the in-office group increasingly consists of those who were already more willing to come in — who are not a representative cross-section of the original workforce. Over time, the average productivity score of the in-office group may **appear to rise** because low-performing reluctant commuters remain while high-performing remote-preferring employees leave. This is **attrition bias (sample selection):** the composition of the sample changes, affecting the regression. The analyst might then claim "RTO improved productivity" when in reality only a selected higher-performing subset stayed, while the true causal effect of RTO could be zero or negative.

---

### T4 — Slope and intercept boundary cases

**(a)** Slope = 800: the model predicts that a 40-year-old earns €800 more than a 39-year-old, on average, for this sample of employees. This is the average annual salary increase associated with one additional year of age.

**(b)** Intercept: the model predicts a newborn (age = 0) would earn €25,000. This is not meaningful — a child cannot work, and 0 years is far outside the data range (employees are likely aged 22–65+). The technical term for using a model outside the training data range is **extrapolation.** Extrapolation is always risky; the linear model has no guarantee of validity at X = 0.

**(c)** The colleague who says "this regression is useless" overstates the case; the one who says "the slope is still informative" is more correct — but both have a point. R² = 0.08 means age alone explains very little of salary variation: most of the variation comes from factors like role, seniority, performance, and industry. However, the slope of €800/year is informative as a descriptive statistic — it quantifies the average salary-age gradient in this sample, even if age is a poor single predictor. Additional context that would help: how does R² = 0.08 compare to other single-variable models? Is the coefficient statistically significant? What is the salary range across employees?

**(d)** Residual for age-23 new hire: Predicted = 25,000 + 800 × 23 = €43,400. Residual = €48,000 − €43,400 = **€4,600.** The employee earns €4,600 more than the model predicts for their age — a positive residual indicating above-model compensation.

**(e)** A negative slope (salary decreasing with age) within the technology division could reflect **Simpson's Paradox** or **compositional effects.** For example: the technology division may have hired many junior employees very recently at higher market rates than senior employees hired years ago under different market conditions. Young employees hired in 2022–2024 at inflated tech-sector salaries earn more than older employees hired in 2015 at lower rates. Within the division, age and salary are negatively correlated — not because seniority is punished, but because the timing of hiring (and prevailing market rates) drives salary more than age. The overall positive correlation across divisions disappears within this subgroup.

---

### T5 — Build, predict, evaluate residuals (apartments)

**(a)** Using Excel Data Analysis on the 8-apartment data: **Rent ≈ 256 + 16.4 × Size.** Slope: each additional m² of apartment size predicts approximately **€16.40 more in monthly rent**, on average. (Student answers may vary slightly depending on rounding in Excel output.)

**(b)** R² ≈ **0.988** — approximately 98.8% of the variation in monthly rents across these 8 apartments is explained by apartment size. Very high: size is an excellent predictor of rent in this sample.

**(c)** Predicted rent for Apt 4 (70m²): 256 + 16.4 × 70 = 256 + 1,148 = **€1,404.** Residual = 1,400 − 1,404 ≈ **−€4.** The apartment is priced essentially at the model's prediction — a residual of −€4 is negligible. (Apt 4 is effectively at the regression line.)

**(d)** With R² ≈ 0.988, residuals should be small and show random scatter around zero with no systematic trend. A random pattern means: residuals have no visible relationship with size (no fan-shape, no curve, no clustering). Given the near-perfect fit in this dataset, the residual plot should show very small, randomly scattered points.

**(e)** Predicted rent for 100m²: 256 + 16.4 × 100 = 256 + 1,640 = **€1,896.** The data ranges from 40m² to 85m², so 100m² is an extrapolation. This prediction is less reliable than predicting rent for a 65m² apartment (which is squarely within the data range). For a 65m² apartment: 256 + 16.4 × 65 = **€1,322** — the model's validity is well-established at this size.

**(f)** Predicted rent for 65m²: €1,322 (from above). Listed price: €1,600. Percentage above prediction: (1,600 − 1,322)/1,322 × 100% ≈ **21% above prediction.** Whether this is "significantly" higher depends on the standard error of the estimate from the regression output. If the standard error is ~€80 (approximate, given the tight fit), €1,600 is approximately (1,600 − 1,322)/80 ≈ 3.5 standard errors above prediction — quite high. The apartment appears expensive relative to its size.

---

### T6 — High vs low R²: when does it matter?

**(a)** R² = 0.78: **22%** of tomorrow's temperature variation is unexplained by today's temperature. This residual variance comes from chaotic weather dynamics, fronts, and atmospheric events that today's temperature alone cannot capture — these require additional meteorological variables (pressure, humidity, wind direction) for better prediction.

**(b)** Both are right in context. R² = 0.78 is strong for a single-predictor physical science model where the predictor is directly related to the outcome. R² = 0.06 is very low for predicting a complex economic variable from a single prior-period value — corporate earnings are affected by macroeconomic conditions, management decisions, and industry disruptions, making single-predictor prediction inherently weak. The usefulness of R² depends entirely on the domain: in physics and meteorology, R² > 0.7 with one predictor is excellent; in economics and social science, R² < 0.3 with many predictors is common. Comparing R² across domains without context is meaningless.

**(c)** Yes — a statistically significant but practically weak predictor is both possible and common. Statistical significance at p = 0.003 with n = 200 says the slope is distinguishable from zero with high confidence. Practical weakness (R² = 0.06) says the predictor explains very little of the outcome's variation. With 200 observations, even a tiny true effect can be detected with high confidence. The slope of 0.14 is real in the sense that it is non-zero — but it explains only 6% of earnings variation, meaning 94% is driven by other factors. A significant but weak predictor is useful as one of many inputs in a larger model, but not as a standalone forecasting tool.

**(d)** R² is **the same** regardless of which variable is X and which is Y — R² = r², and the correlation between X and Y is symmetric (r(X,Y) = r(Y,X)). The slope **changes**: if slope of Y on X is b = r(σ_Y/σ_X), then slope of X on Y is b' = r(σ_X/σ_Y) = b × (σ_X²/σ_Y²). Unless r = ±1, the two slopes are different.

**(e)** Prediction: 0.14 × 20 = **2.8% earnings growth** predicted for next year. Caveat: R² = 0.06 means the model explains only 6% of earnings variation — the remaining 94% is driven by factors outside the model (macroeconomic conditions, management quality, competitive dynamics). The 2.8% prediction carries enormous uncertainty: the 95% prediction interval would be very wide (roughly ±2 standard errors of the estimate). This model should not be used for individual company forecasts; at best it provides a weak population-level tendency.

---

### T7 — Education and GDP: causation claim

**(a)** r = 0.82 across 90 countries is plausible — there is a well-documented association between educational attainment and economic development in cross-country data. The strongest causal argument: human capital theory (Becker, 1964) predicts that education raises worker productivity, which drives GDP per capita. More educated workforces can adopt more complex technologies, move into higher-value industries, and generate larger economic surpluses. Countries with higher secondary enrolment produce more skilled workers → higher productivity → higher GDP per capita. The correlation is consistent with this mechanism.

**(b)** Two confounding variables: (i) **Institutional quality:** countries with strong property rights, rule of law, and low corruption invest more in education AND have higher economic productivity independently. Institutional quality drives both, making the education-GDP correlation partly spurious. (ii) **Historical wealth:** countries that were already wealthy in the 20th century could afford to invest in education AND grew richer independently. Wealth enables education investment; education does not necessarily cause the initial wealth accumulation.

**(c)** This is **ecological correlation** — the unit of analysis is the country, not the individual. Ecological correlations cannot be used to draw individual-level inferences (the ecological fallacy). Additional problems: countries differ systematically in many ways — culture, geography, colonial history, natural resources — any of which could independently explain both educational attainment and GDP. The regression of country-level averages on country-level averages cannot identify individual-level mechanisms and may produce coefficients that do not apply at lower levels of aggregation.

**(d)** The dramatic drop from 4,200 to 850 after controlling for 1990 GDP reveals severe **omitted variable bias** in the original model. Countries that were already wealthy in 1990 had both the resources to expand secondary enrolment AND the existing economic base for high GDP per capita. The original coefficient (4,200) was capturing the effect of historical wealth, not the causal effect of education. After controlling for the starting point (1990 GDP), the marginal return to secondary enrolment is much smaller and statistically indistinguishable from zero.

**(e)** "The r = 0.82 association is real and worth taking seriously as a basis for policy prioritisation — governments allocating limited budgets should favour education where other evidence suggests it contributes to development. However, to make the causal claim more credible, we would need evidence from natural experiments or quasi-experimental designs: for example, countries where secondary enrolment expanded sharply due to an exogenous policy change (a school construction programme, a legal change in compulsory schooling age) and whether GDP per capita subsequently grew faster than comparable countries that did not experience the same shock. The correlation alone, while suggestive, cannot distinguish between education causing growth and wealth enabling both."

---

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
