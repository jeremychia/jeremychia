# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 15: Regression Analysis — Statistical Inference
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Interpret t-tests on regression coefficients: what the null hypothesis is, what rejection implies, and what it does not imply
- Interpret the F-test for overall model significance and distinguish it from the individual coefficient t-tests
- Identify when adding a variable changes the sign or magnitude of an existing coefficient — and explain why
- Evaluate whether a stepwise regression result is trustworthy, given the risks of data dredging

These map to ST2187 syllabus topic 11 (regression inference) and close the regression arc (Weeks 14–15). Students who leave this session can read a full regression output table — not just the coefficients (Week 14) but the standard errors, t-statistics, p-values, and F-test — and say something intelligent about what each number means for the conclusion being drawn.

These objectives are at the **analysis and evaluation** levels of Bloom's Taxonomy — evaluating whether inference conclusions follow from the output, and identifying when they don't.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 11 — read the following sections:
- §11-1 Introduction: what statistical inference adds to regression (p. 484)
- §11-2 The statistical model: assumptions behind OLS inference (pp. 484–488)
- §11-3 Inferences about the regression coefficients — t-tests and p-values (pp. 488–496)
- §11-4 Multicollinearity (pp. 496–502)
- §11-5 Include/exclude decisions (pp. 502–507)
- §11-6 Stepwise regression (pp. 507–512)
- §11-7 Outliers and influential observations (pp. 512–517)
- §11-8 Violations of regression assumptions (pp. 517–521) — §11-8a (nonconstant error variance) is exactly T3; §11-8c (autocorrelated residuals) is the bridge to Week 16
- From Chapter 10: §10-5 Multiple regression and §10-6a–b Dummy and interaction variables (pp. 443–460) — the encodings used by T2, T6, and T7

*Rationale:* Chapter 11 is inference-only — it picks up exactly where Chapter 10 (estimating relationships) ended. Students who read §11-2 and §11-3 carefully will arrive able to read a full regression output table with t-statistics and p-values; the session converts that reading into active interpretation practice.

**Videos (~20 minutes total):**
- [Multiple Regression — StatQuest](https://www.youtube.com/watch?v=EkAQAi3a4js) (12 min) — adding variables and interpreting coefficients. *Active watching: when StatQuest shows that adding a correlated predictor changes the coefficient on an existing predictor, pause and write: why does the slope on variable X change when you add variable Z? This is what T2 tests — the ad spend slope drops from 11.2 to 8.4 when store size is added.*
- [p-values and the t-test in regression — StatQuest](https://www.youtube.com/watch?v=I10q6fjPxJ0) (8 min). *Active watching: when StatQuest states what the null hypothesis is for a coefficient t-test, pause and write it in your own words. This is T1(a) — the null that p = 0.000 on Ad spend is rejecting.*

**Worked example (read this before attempting the tutorial problems):**

> **Multiple regression output (Excel):**
>
> Dependent variable: **Monthly sales (€000s)**
> Predictors: Ad spend (€000s), Store size (m²), Competitor count
>
> | | Coefficients | Std Error | t Stat | p-value |
> |---|---|---|---|---|
> | Intercept | 15.3 | 6.2 | 2.47 | 0.031 |
> | Ad spend | 8.4 | 1.1 | 7.64 | 0.000 |
> | Store size | 0.042 | 0.015 | 2.80 | 0.018 |
> | Competitor count | −4.1 | 1.8 | −2.28 | 0.041 |
>
> R² = 0.894, Adjusted R² = 0.871
> F-statistic = 39.2, p-value for F = 0.000
>
> **Interpretation line by line:**
> - Ad spend slope = 8.4: holding store size and competitor count constant, each additional €1,000 in advertising predicts €8,400 more in monthly sales. Significant (p = 0.000).
> - Store size slope = 0.042: each additional m² predicts €42 more in monthly sales, holding other variables constant. Significant (p = 0.018).
> - Competitor count slope = −4.1: each additional nearby competitor predicts €4,100 less in monthly sales. Significant (p = 0.041).
> - R² = 0.894: together, these three variables explain 89.4% of variation in sales.
> - F-test: the overall model is statistically significant — the three predictors together explain more than chance.
>
> **What changed from simple regression (Week 14)?**
> In Week 14 (simple regression of sales on ad spend only), the slope was 11.2. In this model it is 8.4. The difference arises because ad spend and store size are correlated — larger stores tend to spend more on advertising. The multiple regression partitions the effect, assigning part of what appeared to be "ad spend effect" to store size.

*This worked example is marked optional for students who feel confident reading a regression output table — interpreting each coefficient, its t-statistic and p-value, and the F-test and adjusted R². If you answered T1(a) and (c) without the example, you don't need it. If any of the five output elements (slope, t, p, R², F) felt unclear after the reading, work through the line-by-line interpretation.* (On expertise reversal, see Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems (submitted before class, reviewed in Part 2):**

*T1 — Reading the output:*

*The coefficient on Ad spend in the worked example (8.4, t = 7.64, p = 0.000) is the template for T1(a): the null is H₀: β_adspend = 0; rejection means ad spend has a statistically significant effect on sales, controlling for the other variables. The StatQuest video's null hypothesis statement is the exact phrasing.*
> Using the multiple regression output in the worked example:
>
> (a) What is the null hypothesis for the t-test on Ad spend? What does rejection (p = 0.000) imply?
> (b) Could the F-test be significant while some individual t-tests are not? Give an example of when this would happen.
> (c) Adjusted R² = 0.871 < R² = 0.894. Why is this, and which one should you report?

*T2 — Coefficient sign change:*
> In a simple regression of salary (Y) on years of experience (X), the slope is +8,000.
> When gender (Female = 1) is added as a second predictor, the slope on experience drops to +2,000 and the slope on gender is −15,000 (women earn €15,000 less controlling for experience).
>
> (a) What does the drop from 8,000 to 2,000 tell you about the relationship between experience and gender?
> (b) Which model better isolates the effect of experience on salary?
> (c) A manager says "experience barely affects salary (slope = 2,000 in the full model)" — critique this statement.

T2 is the confound/omitted variable session's payoff. The experience slope dropped because experience and gender were correlated — in the simple model, the experience slope was absorbing some of the gender pay gap. The correct interpretation is: "Controlling for gender, experience adds €2,000 per year. The simple model's €8,000 was partially confounded by gender."

*T3 — Residual diagnostics:*
> A regression residual plot shows residuals that fan out as X increases (larger residuals at high X values).
>
> (a) What is this pattern called?
> (b) What OLS assumption does it violate?
> (c) What transformation of Y might help?

T3 introduces heteroskedasticity — the most common OLS violation students will encounter in practice.

*T4 — Boundary case: multicollinearity — what happens when predictors are nearly identical:*

> A researcher builds a multiple regression model to predict employee productivity (units/hour) using two predictors: hours of training completed (X1) and training certification score (X2). Both predictors were collected in the same training programme — employees who spent more hours training also tend to have higher scores.
>
> Regression output (n = 80 employees):
>
> | | Coefficient | Std Error | t Stat | p-value |
> |---|---|---|---|---|
> | Intercept | 12.4 | 2.1 | 5.90 | 0.000 |
> | Hours (X1) | 0.08 | 0.71 | 0.11 | 0.912 |
> | Score (X2) | 0.12 | 0.68 | 0.18 | 0.859 |
>
> R² = 0.68, Adjusted R² = 0.67, F = 82.4, p(F) = 0.000
>
> (a) The F-test is highly significant (p < 0.001), meaning the model as a whole explains a significant amount of variance. Yet neither individual predictor is statistically significant. How can both things be true simultaneously?
> (b) This is a classic symptom of multicollinearity. What does multicollinearity mean, and what is its likely cause in this specific example?
> (c) If the researcher drops X2 (score) and runs a simple regression with only X1 (hours), the slope on X1 becomes 0.47 with p = 0.001. Why did the slope and its significance change so dramatically when the collinear variable was removed?
> (d) The Variance Inflation Factor (VIF) for X1 is 18.3 (any VIF > 10 indicates serious multicollinearity). Interpret what this means for the reliability of the coefficient on X1 in the full model.
> (e) The researcher considers three solutions: (i) drop one of the correlated predictors; (ii) create a combined score (e.g., average of normalised X1 and X2); (iii) collect more data. For each, state one advantage and one disadvantage.

*T5 — Multi-step: the F-test and what it tests vs what it doesn't:*

> A real estate analyst builds a model to predict apartment prices (€000s) using four predictors: size (m²), distance to city centre (km), number of bedrooms, and floor level. The regression output (n = 120 apartments) gives:
>
> R² = 0.74, Adjusted R² = 0.73, F-statistic = 82.4, p-value for F < 0.001
>
> Individual p-values: size p = 0.000; distance p = 0.003; bedrooms p = 0.312; floor p = 0.218
>
> (a) What is the null hypothesis of the F-test? What does rejecting it imply?
> (b) The F-test is significant, but two individual predictors (bedrooms and floor) are not. Should the analyst remove them? What does the Adjusted R² criterion say?
>
> *Solution:* Compare Adjusted R² with and without the non-significant predictors. If removing them increases Adjusted R², they should be removed. In general, predictors that are not significant and do not meaningfully increase Adjusted R² should be dropped for parsimony.
>
> (c) After removing bedrooms and floor from the model, the researcher finds: Adjusted R² = 0.74 (same as before). What does this tell you about the contribution of bedrooms and floor to the model?
> (d) A journalist reports: "The study found that floor level has no effect on apartment price." Critique this statement. What does a p-value of 0.218 for floor level actually mean?
> (e) The analyst uses stepwise regression to select variables. A colleague warns: "Stepwise regression can produce models that overfit." Explain what overfitting means in the context of multiple regression, and describe one consequence of overfitting for the model's usefulness on new data.

*T6 — Coefficient sign reversal: a worked example in context:*

> A hospital administrator wants to understand what predicts patient length of stay (days in hospital). She runs the following regressions (n = 500 patients):
>
> **Model A (simple regression):** Length of stay = 3.2 + 0.8 × Age. Slope on Age: p = 0.000.
>
> **Model B (multiple regression):** Length of stay = 2.1 + 0.3 × Age + 2.4 × Severity. Slope on Age: p = 0.012. Slope on Severity: p = 0.000.
>
> **Model C (multiple regression):** Length of stay = 2.0 + 0.3 × Age + 2.3 × Severity − 0.8 × Elective (1 = elective procedure, 0 = emergency). Slope on Age: p = 0.008.
>
> (a) In Model A, the age slope is 0.8. In Model B, it drops to 0.3. What does this suggest about the relationship between age and disease severity?
> (b) Is the administrator wrong to interpret Model A as meaning "older patients stay longer"? What is missing from that statement?
> (c) In Model C, the slope on Elective is −0.8. Interpret this coefficient carefully, making sure to state what is held constant.
> (d) The slope on Age did not change much between Models B and C (0.3 → 0.3). What does this tell you about the relationship between age and procedure type (elective vs emergency)?
> (e) A policy recommendation based on Model A would say "reduce age to reduce length of stay" — which is obviously impossible. What can a hospital actually do with the findings from Model C to reduce mean length of stay?

*T7 — Diagnostic: is this regression output trustworthy?*

> A student submits the following regression output as part of their coursework:
>
> Dependent variable: Weekly sales (€)
> Predictors: Number of customers, Average transaction value (€), Number of customers × Average transaction value
>
> | | Coefficient | Std Error | t Stat | p-value |
> |---|---|---|---|---|
> | Intercept | 128 | 54 | 2.37 | 0.019 |
> | Customers | 14.2 | 89.3 | 0.16 | 0.874 |
> | Avg transaction | 8.7 | 74.1 | 0.12 | 0.907 |
> | Customers × Avg transaction | 1.02 | 0.003 | 340 | 0.000 |
>
> R² = 0.998, Adjusted R² = 0.998, F = 12,451, p < 0.001
>
> (a) Note that Sales = Customers × Average Transaction Value is an accounting identity, not a statistical relationship. What does this imply about the regression above?
> (b) The interaction term (Customers × Avg transaction) has a t-statistic of 340. Is this evidence of a strong relationship, or is it revealing something else?
> (c) The standard errors on Customers and Average transaction are very large relative to their coefficients (SE ≈ 6× the coefficient), while the interaction term's SE is tiny. What does this pattern suggest about multicollinearity?
> (d) R² = 0.998 and F is enormous. Should the student conclude this is an excellent regression model? What fundamental modelling error has been made?
> (e) What would you advise the student to do instead to model the relationship between customer behaviour and sales?

---

## Answer Key

### T1 — Reading the regression output

**(a)** The null hypothesis for the t-test on Ad spend is: **H₀: β_adspend = 0** — the coefficient on Ad spend equals zero (ad spend has no linear relationship with sales, controlling for store size and competitor count). Rejection (p = 0.000) implies that ad spend has a statistically significant positive effect on sales even after controlling for the other variables. It does not imply that ad spend *causes* sales — only that the relationship is unlikely to be zero in the population.

**(b)** Yes — the F-test can be significant while some individual t-tests are not. This happens most commonly when predictors are **multicollinear** (highly correlated with each other): together they explain a significant proportion of Y's variation (F is significant), but each variable's *marginal* contribution after controlling for the others is not distinguishable from zero (individual t not significant). The pattern is: significant F + non-significant individual t-tests = multicollinearity. The predictors collectively contain information about Y, but the model cannot attribute that information cleanly to one predictor or the other.

**(c)** Adjusted R² = 0.871 < R² = 0.894 because Adjusted R² **penalises for adding variables** that do not meaningfully improve fit. R² never decreases when a variable is added (it always increases or stays the same), so it cannot be used to compare models with different numbers of predictors. Adjusted R² applies a penalty: Adj R² = 1 − [(1 − R²)(n − 1) / (n − k − 1)], where k is the number of predictors. Adding a variable that improves fit by more than the penalty increases Adj R²; adding a weak variable decreases it. **Report Adjusted R²** when comparing models with different numbers of predictors — it is the appropriate criterion for model selection.

---

### T2 — Coefficient sign change (experience and gender)

**(a)** The drop from 8,000 to 2,000 reveals that **experience and gender are correlated** in the data — specifically, men in this sample tend to have more years of experience than women (e.g., because women have shorter average tenure in the company, or career interruptions). In the simple regression, the experience coefficient was absorbing some of the gender pay gap: it was partly acting as a proxy for gender. When gender is explicitly included, the model partitions the effect correctly: experience explains €2,000/year of salary, and the remaining gap (€15,000) is attributed to gender directly.

**(b)** The **multiple regression model** (with gender included) better isolates the effect of experience on salary. It controls for the confound: it compares employees with the same gender who differ in experience. The simple regression confounds the experience effect with the gender effect — it does not hold gender constant.

**(c)** The manager's statement is misleading in two ways: (i) €2,000 per year of experience is still a meaningful economic effect — it is the **ceteris paribus effect** (holding gender constant), which is the relevant quantity for understanding returns to experience. (ii) "Barely affects" imports a practical significance judgment without evidence: whether €2,000/year is economically meaningful depends on the salary level, typical experience range, and what the question is. The statement confuses a smaller coefficient with an unimportant one. The correct interpretation: "Controlling for gender, each additional year of experience is associated with approximately €2,000 more in annual salary."

---

### T3 — Residual diagnostics (heteroskedasticity)

**(a)** The pattern — residuals fanning out as X increases — is called **heteroskedasticity.** The variance of the residuals increases with X.

**(b)** It violates the OLS assumption of **homoskedasticity** — the assumption that the variance of the error term is constant across all values of X. This assumption is required for the OLS standard errors (and therefore t-statistics and p-values) to be valid. With heteroskedasticity, OLS coefficient estimates are still unbiased but no longer efficient, and the standard errors are incorrect — making hypothesis tests unreliable.

**(c)** A **log transformation of Y** (replacing Y with ln(Y)) often stabilises the variance. If the standard deviation of the error is proportional to Y (multiplicative rather than additive errors), a log transform converts the model from Y = a + bX + ε to ln(Y) = a + bX + ε, where the new error is more homoskedastic. Other options include: a square root transformation of Y; using robust standard errors (heteroskedasticity-consistent SEs) that correct the standard errors without transforming the model; or switching to weighted least squares.

---

### T4 — Multicollinearity (training hours vs score)

**(a)** Both things can be true simultaneously because the **F-test and the t-tests ask different questions.** The F-test asks: "Do the predictors together explain more variation in Y than a model with no predictors?" With R² = 0.68, they clearly do — hence the significant F. The individual t-tests ask: "Does each predictor contribute *marginally*, after the other predictor has already been included?" When X1 and X2 are highly correlated, each predictor contains much of the same information as the other — so neither adds much *beyond what the other already explains*. The predictors share credit for the explained variance, and neither can be identified as the "cause" in isolation.

**(b)** Multicollinearity means two or more predictors are highly correlated with each other, making it difficult to estimate their individual coefficients reliably. In this example: employees who spent more hours in training also tend to have higher certification scores — the two variables move together. The regression cannot disentangle how much of the productivity improvement is due to hours vs scores.

**(c)** When X2 (score) is removed, the model now only has X1 (hours). X1 is no longer competing with a correlated partner — it absorbs all the explanatory power that was previously shared. The slope rises from 0.08 to 0.47, and the p-value drops from 0.912 to 0.001, because X1 is now picking up the variation previously "attributed" ambiguously between X1 and X2. The underlying relationship (training hours predict productivity) is real; multicollinearity just made it impossible to detect in the presence of the correlated partner.

**(d)** VIF = 18.3 >> 10 means the variance of the coefficient on X1 is inflated by a factor of 18.3 relative to what it would be if X1 were uncorrelated with X2. In practice: the standard error of the X1 coefficient is √18.3 ≈ 4.3 times larger than it would be without multicollinearity. This is why the t-statistic for X1 is tiny (0.11) even if training genuinely predicts productivity — the standard error is so inflated that the coefficient cannot be distinguished from zero.

**(e)**
- **(i) Drop one predictor:** Advantage: resolves multicollinearity, produces stable coefficients. Disadvantage: loses information; if both variables have genuine independent effects (even small ones), dropping one causes omitted variable bias.
- **(ii) Create a combined score:** Advantage: retains both variables' information while reducing collinearity; theoretically motivated if both measure "training intensity." Disadvantage: the combined variable requires an assumption about the relative weighting of hours vs score, which may be arbitrary.
- **(iii) Collect more data:** Advantage: larger n reduces standard errors generally and may allow both coefficients to be estimated with adequate precision even with moderate correlation. Disadvantage: if X1 and X2 are structurally collinear (always measured together in this training programme), more data does not help — the correlation between them does not decrease with more observations.

---

### T5 — F-test and model selection

**(a)** The null hypothesis of the F-test: **H₀: β₁ = β₂ = β₃ = β₄ = 0** — all slope coefficients are simultaneously zero (none of the predictors explain any variation in apartment price beyond chance). Rejecting this null (p < 0.001) means at least one predictor has a non-zero relationship with price. It does not tell you which predictor(s) are significant individually — only that the set of predictors as a whole is informative.

**(b)** The analyst should not automatically remove non-significant predictors without checking the Adjusted R² criterion. The Adjusted R² criterion says: remove a predictor if doing so increases (or maintains) Adjusted R². Non-significant predictors that add no Adjusted R² improvement should be dropped for parsimony. However, if a predictor has a theoretical reason to be in the model (e.g., floor level has a known effect on real estate values in some cities), it may be retained even if not statistically significant in this sample.

**(c)** Adjusted R² = 0.74 with all four predictors, and Adjusted R² = 0.74 with only two: bedrooms and floor added zero explanatory power beyond size and distance to city centre. Their omission costs nothing in fit. This confirms they should be removed — they are redundant (their effect is already captured by the other predictors), not just individually weak.

**(d)** The journalist's statement is too strong. p = 0.218 means: if floor level truly had no effect on apartment price, we would observe an effect as large as the estimated coefficient 21.8% of the time by chance — this does not cross the 5% significance threshold, so we cannot conclude the effect is non-zero. But this is very different from concluding "floor level has no effect." The data are **consistent with** a null effect, but also consistent with a real but modest effect that this sample size lacked the power to detect. "No statistically significant effect" ≠ "no effect."

**(e)** **Overfitting** in multiple regression means the model has been tuned too closely to the specific sample data — it captures patterns in the sample (including random noise) that do not generalise to new data. Stepwise regression, by repeatedly selecting variables that reduce in-sample residuals, can produce models with inflated R² and biased coefficients that over-represent noise. Consequence: the model predicts very well in-sample but poorly on new observations. The coefficients are also misleading for inference — the standard errors are too small because the model has been optimised to fit this particular data.

---

### T6 — Coefficient sign reversal (hospital length of stay)

**(a)** The drop from 0.8 (Model A) to 0.3 (Model B) suggests that **age and disease severity are positively correlated** — older patients tend to have more severe conditions. In Model A, the age coefficient was absorbing some of the severity effect: it was acting as a proxy for severity because older patients were, on average, more severely ill. Model B separates the two effects, showing that conditional on severity, the age effect on length of stay is smaller (0.3 vs 0.8).

**(b)** The administrator is not wrong in a descriptive sense: "older patients stay longer" accurately describes the unconditional pattern in Model A. What is missing is "controlling for other factors." The statement invites a causal interpretation (age per se causes longer stays) when the actual driver may be severity. A complete statement would be: "Older patients stay longer on average, largely because they tend to have more severe conditions — not directly because of their age."

**(c)** Slope on Elective = −0.8: **holding age and severity constant**, patients undergoing elective procedures (vs emergency) stay 0.8 days fewer, on average. The "holding age and severity constant" qualifier is critical — the coefficient does not compare all elective vs all emergency patients (who differ in severity); it compares patients of the same age and severity level who differ only in whether their procedure was elective.

**(d)** The near-identical slope on Age in Models B (0.3) and C (0.3) tells you that **age and procedure type (elective vs emergency) are largely uncorrelated** in this sample — adding Elective to the model did not change the age coefficient, meaning the age-length-of-stay relationship is not confounded by procedure type. Elective procedures explain additional variation in length of stay, but they don't alter the age effect because elective vs emergency is not strongly related to age in this dataset.

**(e)** The hospital cannot change patients' ages, but Model C reveals two actionable insights: (i) **Severity management:** Model B shows that severity is the dominant driver of length of stay. Investments in earlier intervention, preventive care, or better management of chronic conditions to reduce severity at admission could meaningfully shorten stays. (ii) **Scheduling management:** the Elective coefficient (−0.8 days) suggests elective patients have shorter stays than emergency patients of similar age and severity. The hospital could investigate what differs about elective patient pathways (better preparation, scheduled resource allocation) and whether those practices can be extended to emergency patients where applicable.

---

### T7 — Regression output diagnostic (accounting identity)

**(a)** Sales = Customers × Average Transaction Value is an **accounting identity** — by definition, total revenue equals the number of transactions multiplied by the average value per transaction. Regressing Sales on Customers, Average Transaction, and their interaction is regressing a variable on the components of its own definition. This is not a statistical relationship to be estimated — it is a mathematical tautology. The "regression" is not modelling anything about the world; it is just recovering an algebraic identity.

**(b)** The t-statistic of 340 on the interaction term is not evidence of a strong relationship — it is evidence of a **definitional relationship.** The interaction term (Customers × Avg Transaction) is essentially Sales itself (with rounding), so the model is regressing Sales on Sales. The enormous t-statistic reflects perfect (or near-perfect) multicollinearity between the interaction term and the dependent variable, not an informative statistical finding.

**(c)** The pattern — huge standard errors on Customers and Average Transaction, tiny standard error on the interaction — is the signature of extreme multicollinearity. The interaction term is a near-perfect linear combination of the other two predictors (and the outcome), making the individual coefficients on Customers and Average Transaction unidentifiable. Their enormous standard errors reflect the instability of their coefficients — the model cannot distinguish their marginal contributions from the joint contribution already captured by the interaction.

**(d)** **No** — R² = 0.998 and F = 12,451 do not indicate an excellent regression model. They indicate a fundamental modelling error: the analyst has included a variable that is (nearly) a linear function of the dependent variable. This produces apparent fit without discovering any real relationship. The model is essentially predicting Sales from Sales, which trivially gives R² ≈ 1. This is not a good model; it is a tautology dressed as a model.

**(e)** The student should: (i) **Separate the question from the identity.** If the goal is to understand what drives sales, the relevant model would regress Sales on genuinely independent predictors: marketing spend, store traffic, day of week, promotions, pricing — not the arithmetic components of Sales itself. (ii) **Alternatively:** if the goal is to decompose revenue changes into volume effects (customer count) and price effects (average transaction), the appropriate tool is a decomposition analysis, not a regression. Regression is for estimating relationships between conceptually distinct variables — not for recovering algebraic definitions.

---

**Pre-class submission (on the course portal):**

Find a regression analysis reported in a news article, investor report, or academic abstract. Submit:
1. What is the dependent variable? What are the predictors?
2. What coefficient or finding is highlighted?
3. Is there an omitted variable that might change the interpretation?

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

**Easy — vocabulary and recall:**

- Q1: In regression output, the t-statistic for a coefficient is:
  *(a) Coefficient × Standard Error  (b) Coefficient / Standard Error  (c) Standard Error / Coefficient  (d) Coefficient − Standard Error)*

- Q2: The null hypothesis for the t-test on slope b₁ is:
  *(a) b₁ = 1  (b) b₁ = Y-bar  (c) b₁ = 0  (d) b₁ ≠ 0)*

- Q3: A p-value of 0.042 for a coefficient means (at α = 0.05):
  *(a) The coefficient is definitely non-zero  (b) We reject H₀: b = 0 — the coefficient is statistically significant  (c) There is a 4.2% chance the relationship is real  (d) The coefficient is practically important)*

- Q4: Adjusted R² differs from R² because:
  *(a) It uses the full sample  (b) It penalises for adding variables that don't improve fit  (c) It is always higher than R²  (d) It adjusts for outliers)*

- Q5: Heteroskedasticity means:
  *(a) The errors are normally distributed  (b) The variance of the errors is not constant across values of X  (c) The predictors are correlated with each other  (d) The model has too many variables)*

- Q6: Multicollinearity is a problem in multiple regression when:
  *(a) The dependent variable has outliers  (b) The predictor variables are highly correlated with each other  (c) The residuals show a curved pattern  (d) R² is too high)*

**Medium — application:**

- Q7: Adding a new predictor to a regression model will:
  *(a) Always increase R²  (b) Always increase Adjusted R²  (c) Always improve predictions on new data  (d) Always decrease the slope on existing predictors)*

Q7(a) is the most important: R² never decreases when you add a variable, even a useless one. That's why Adjusted R² exists.

- Q8: A coefficient has a p-value of 0.002. Which is the correct interpretation?
  *(a) There is a 0.2% probability that this variable matters  (b) If H₀: b = 0 were true, we'd see a t-statistic this large only 0.2% of the time by chance  (c) The coefficient is larger than 99.8% of possible values  (d) The effect size is large)*

**Hard — conceptual:**

- Q9: A model with 20 predictors is fit to 50 observations. R² = 0.92. This is:
  *(a) An excellent model — 92% of variance explained  (b) Suspicious — with 20 predictors and 50 observations, overfitting is almost certain  (c) Appropriate — more predictors always mean better models  (d) Invalid — you need at least as many observations as predictors)*

**Instructor acts on results (5 minutes)**

Q3 and Q8 are the p-value interpretation questions — the same issue as hypothesis testing (Week 13) applied to regression. Q7 (adding variables always increases R²) is the motivation for Adjusted R². Q9 (overfitting) is the conceptual punchline for the confound hunt in Part 3.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T1(b) — F-test significant but individual t-tests not — is the most counterintuitive. Example: two predictors that are individually not significant but together explain variance through collinearity. The F-test says the model as a whole matters; the t-tests say which individual predictors we can identify.

T2 is the confound hunt payoff. Draw the two-model comparison on the board: the experience slope dropped by 6,000 when gender was added. "What does that tell us about the simple regression?" It was picking up part of the gender effect.

T3 — heteroskedasticity — is brief: "Fan pattern in residuals. OLS standard errors are wrong. Coefficients may still be unbiased but SEs are unreliable. Transformation or weighted least squares as solutions."

Buffer: use it on T2 — the interpretation of coefficient changes when a variable is added is the conceptual core of multiple regression and deserves depth.

---

### Part 3 — Confound Hunt: Add Variables, Watch Coefficients Change (25 minutes)

Pairs receive a dataset with 3–4 predictor variables and a dependent variable. The dataset is provided as an Excel file or loaded via Python.

**Dataset:** city-level data (25 cities). Variables:
- Y: crime rate (crimes per 100,000 residents)
- X1: unemployment rate (%)
- X2: urban density (residents per km²)
- X3: median household income (€000s)
- X4: police force size per 100,000 residents

**Task:** build regression models in this order, recording coefficients and R²:
1. Y on X1 only (simple regression)
2. Y on X1 + X2
3. Y on X1 + X2 + X3
4. Y on all four predictors

Questions after each model:
- Did the slope on unemployment change when you added the next variable?
- Did any coefficient change sign?
- Which model would you present if you wanted to argue that unemployment causes crime?
- Which model is most honest?

**What the class should find:**
The unemployment slope typically drops substantially when income is added (unemployment and low income are correlated — both drive crime, and the simple model was giving unemployment credit for income's effect). If police force size is added, the slope may become counterintuitive (larger police forces in high-crime cities — reverse causality).

**The learning:** regression coefficients are not fixed properties of the predictor — they depend on what else is in the model. "The effect of unemployment on crime, controlling for income and density, is X" is a different claim from "the effect of unemployment on crime, unadjusted, is Y." Both are true; they answer different questions.

---

### Part 4 — Peer Discussion: Present and Challenge the Model (20 minutes)

Two pairs present their models. For each, the rest of the class acts as a sceptical stakeholder:
- "Why did you include those four variables and not others?"
- "The coefficient on unemployment changed sign — does that mean the direction of the effect reversed, or something else?"
- "If you were advising a city government, which model would you report — and would you report all of them?"

The last question is the ethical moment: in practice, analysts often have discretion about which model specification to present. Presenting only the model that tells the story you want is a form of selective reporting. The question "which model would you report?" surfaces this without moralising about it.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop:**

*"What is a regression coefficient telling you — really? Not just 'the slope' but what it assumes."*

A coefficient tells you: holding all other included variables constant, a one-unit change in X predicts a β-unit change in Y. The phrase "holding all other variables constant" is the key. It means the coefficient is conditional on what else is in the model. Change the model, and the coefficient may change.

**Bridge to Block 4:**

> *"In the next three weeks we cover time series, optimisation, and simulation — the final three syllabus topics. Then Weeks 19–22 are yours: a full analysis pipeline from dataset to conclusion. Everything in this course — description, probability, inference, regression — is a tool. The question in Weeks 19–22 is whether you can choose the right tool for the question in front of you. What question would you want to answer, if you could use all of this?"*

---

## After Class (Student Post-Work, ~30 minutes)

Students write an LMS post on one of:
- The regression study they submitted before class: is the highlighted coefficient trustworthy? What variable would change it if added?
- The city-crime model: which specification would they present to a city council, and what caveats would they attach?
- One question they'd want to ask before trusting a published regression result

Peer response: one comment that identifies a different potential confound or a specification choice the poster didn't consider.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Part 3 builds 4 sequential models, recording coefficient changes | Chi et al. (1994): self-explanation — students who build the models themselves and observe the changes understand them more durably than students who are shown the progression; the sequence is the mechanism |
| Last question in Part 3: "which model is most honest?" | Forward College Year 3 curriculum: accountability and wise decision-making; the statistical question (which model fits best?) is distinct from the ethical question (which model should I present?); the session should raise both |
| Q7 (adding variables always increases R²) as medium question | This is the most consequential fact about R² — it's why Adjusted R² exists; building the intuition before explaining Adjusted R² makes the latter obvious |
| Confound hunt uses crime dataset | Real-world, politically contested, and has genuine reverse-causality risk (police force size) — these properties make the exercise substantively interesting rather than academically clean |
| Bridge forward names Weeks 19–22 explicitly | Ausubel (1968): advance organiser for the integration block; students who know they will own a full analysis problem in four weeks approach Weeks 16–18 with a different sense of purpose |
| LMS post asks about reporting caveats | Professional communication skill: analysts who can state the limits of their model are more credible than analysts who overstate its implications |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Q3/Q8 (p-value interpretation in regression); Q9 (overfitting) |
| Tutorial review | 15 min | T1(b) F-test; T2 coefficient change; T3 heteroskedasticity |
| Buffer (explicit) | 10 min | Extended T2 discussion; T3 if needed |
| Confound hunt: sequential models | 25 min | 4 models + 4 questions; 15 min build + 10 min comparison |
| Peer discussion: present and challenge | 20 min | Two pairs; three challenge questions; ethical reporting question |
| Instructor debrief | 10 min | What a coefficient really says; bridge to Block 4 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Overfitting is conceptually important but hard to demonstrate in 90 minutes.

Q9 asks about a model with 20 predictors and 50 observations — an obvious overfitting case. But the general principle (more predictors is not always better) is easier to state than to show without a train/test split.

**Resolution:** the sequential model building in Part 3 shows the spirit of the issue: as variables are added, R² increases every time, even when the added variable is not theoretically meaningful. Adjusted R² penalises for this. If time allows, a brief demonstration: "If I add random noise as a predictor, R² increases. Try it." This is the most visceral demonstration of overfitting that's achievable in 90 minutes without Python.

---

### 2. The ethical question ("which model would you report?") may feel like an ambush.

Some students may feel that asking about model selection in a statistics class is outside the course's scope. It's not — but the transition from "which model fits best" to "which model should I present" should be made explicit.

**Resolution:** frame it at the start of Part 4: "The statistical question is: which model has the best fit? The professional question is: which model should I present, and what should I say about the others? Those are different questions. Both matter." Year 3 students at Forward College have had two years of personal development around accountability — they are ready for this question.

---

### 3. The crime dataset may produce coefficient instability that surprises students.

If the police force size coefficient changes sign or becomes very large when other variables are added, students may think they've made an error.

**Resolution:** this is the finding, not the error. The sign reversal in police force size is a classic reverse-causality issue: cities with high crime rates hire more police. When crime rate is the Y variable and police size is the X, the positive coefficient in a simple regression reflects this selection, not the causal effect of policing. This is one of the most famous examples in econometrics (the "police and crime" identification problem). Name it explicitly: "You found something real. This is why observational data is hard."

---

### 4. Multiple regression output has many numbers — students may focus on the wrong ones.

In the tutorial worked example, there are 12 numbers in the regression table (4 rows × 3 columns of coefficient, SE, t-stat, p-value). Students who focus only on the p-values miss the coefficients and standard errors. Students who focus only on R² miss the individual predictor tests.

**Resolution:** the tutorial asks specific questions about specific numbers. The quiz tests the conceptual role of each. T1(b) specifically requires students to hold F-test and t-tests in mind simultaneously — which is the most demanding multi-number question in the output.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Chi, M.T.H., de Leeuw, N., Chiu, M.H. & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Farmus, L., Cribbie, R.A. & Rotondi, M. (2020). The flipped classroom in introductory statistics. *Journal of Statistics Education*, 28(3). DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Questions, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed., Chapters 10–11

The §11-1 to §11-7 references are accurate (the best-cited week alongside 11 and 13). But the session *uses* material from three unassigned sections:

1. **T3 tests §11-8a (Nonconstant Error Variance, p. 517) — which is not in the reading.** Heteroskedasticity, its assumption violation, and remedies are exactly 11-8's content. *Fix:* extend the reading to §11-8 (pp. 517–521). Bonus: **11-8c (Autocorrelated Residuals) is the natural bridge to Week 16's time series** — one sentence in the debrief ("when the data has a time order, residuals violate independence in a special way — that's next week") converts an unassigned section into the bridge-forward.
2. **T2 and T6 hinge on dummy variables (Female, Elective) and T7 on an interaction term — §10-6a/10-6b, which no week ever assigns** (Week 14's supplement flags that 10-5/10-6 are unhomed). Students are being examined on encoding conventions they've never read: why Female = 1 vs 0, what the reference category is, why a 3-category variable needs 2 dummies. *Fix:* add §10-5 and §10-6a–b (pp. 443–460) to this week's reading — the worked example is already a multiple regression, so the content belongs here anyway.
3. **§11-9 (Prediction, pp. 521–527)** would close the loop with Week 12's CI-vs-prediction-interval distinction; optional but cheap.

## 2. Extended Question Bank (with answers)

**T8 — Dummy variables done properly (fills the §10-6a gap):**

> A salary model uses `Region` with three values (North, Central, South). An analyst creates three dummies (N, C, S) and includes all three plus an intercept. Excel returns an error / drops one automatically.
>
> (a) Why can't all three dummies enter the model?
> (b) With South as the reference category, the fitted model is Salary = 41,000 + 3,200·N + 5,100·C. Interpret both coefficients.
> (c) A colleague re-runs the model with North as the reference and gets different coefficients. Has the model changed?
>
> **Answers:** (a) N + C + S = 1 for every row — a perfect linear combination of the intercept (the "dummy variable trap"); the model is unidentifiable, so one category must be omitted as the baseline. (b) *Relative to South*, Northern employees earn €3,200 more and Central €5,100 more, holding nothing else constant (no other predictors here). Coefficients on dummies are always *comparisons against the reference*, not absolute effects. (c) No — same fitted values, same R², same predictions; only the *parameterisation* changed (each coefficient now compares against North). Reading dummy coefficients without asking "reference category?" is the most common exam error on this topic.

**T9 — The F-statistic from R² (demystifies the output table):**

> Verify the T4 output's internal consistency: with R² = 0.68, n = 80, k = 2, compute F = (R²/k)/((1−R²)/(n−k−1)).
>
> **Answer:** F = (0.68/2)/(0.32/77) = 0.34/0.004156 ≈ **81.8 ≈ the printed 82.4** (rounding in R²). Two payoffs: students see F is not new information but R² rescaled by sample size and model size — which *explains* T4(a): high R² forces a big F regardless of what individual t-tests do; and they acquire a checksum for any output table (the same check confirms T5: (0.74/4)/(0.26/115) ≈ 81.8 ≈ 82.4 ✓).

**T10 — Residuals with a time order (bridges to Week 16 via §11-8c):**

> A regression of monthly sales on advertising is fit to 36 months of data. The residuals, plotted *in time order*, are positive for months 1–14, negative for 15–27, positive for 28–36.
>
> (a) Which OLS assumption is violated, and why doesn't the standard residual-vs-X plot catch it?
> (b) What is the practical consequence for the reported standard errors?
> (c) What structural feature of the data is the model probably missing?
>
> **Answers:** (a) Independence of errors — the residuals are **autocorrelated** (each one resembles its neighbour). A residual-vs-X plot destroys the time ordering, so the runs are invisible; only a residual-vs-time plot reveals them. (b) SEs are typically *understated* with positive autocorrelation — t-statistics too big, p-values too small, overconfident inference. (c) A trend, seasonality, or an omitted slowly-moving variable (e.g. market growth) — exactly what Week 16's decomposition handles. This question makes the Week 15 → 16 hand-off explicit.

*Additional quiz questions:*

- Q10: A model includes a categorical predictor with 4 levels. How many dummy variables should enter (with an intercept)? *(a) 4 (b) 3 (c) 1 (d) 2)* — **Answer: (b).**
- Q11: A VIF of 25 on a predictor means its coefficient's standard error is inflated by a factor of: *(a) 25 (b) 5 (c) √5 (d) 625)* — **Answer: (b)** (√25) — T4(d) as retrieval.
- Q12: For a given x₀, the 95% *prediction interval* for a new observation, compared to the 95% CI for the mean response, is: *(a) narrower (b) identical (c) wider (d) undefined)* — **Answer: (c)** — Week 12's T10 distinction, now inside regression (§11-9).

## 3. Alternative In-Class Activities (additional options)

**A. RAND() predictor demo (5 min, structured version of Design Challenge 1's suggestion).** Everyone adds `=RAND()` as a fifth predictor to their Part 3 model and refits: R² rises for all, Adjusted R² falls for most, and the noise column sometimes shows p < 0.05 for someone in the room — which is the Week 13 multiple-testing lesson materialising in regression. Two birds, five minutes, zero prep.

**B. Coefficient betting slips (runs inside Part 3).** Before each model step, pairs write a prediction: "adding X3 will move the unemployment slope [up/down/sign-flip] because ___." Commit, run, compare. Converts the confound hunt from observation into hypothesis-test-your-intuition — and the wrong bets are the teachable moments (Bjork's generation effect, already cited in Week 14's rationale).

**C. Specification number-line (10 min, Part 4 alternative).** Every pair posts their preferred model's unemployment coefficient on one axis drawn on the whiteboard, labelled with its specification. The class sees one dataset produce a *range* of "the effect of unemployment" — the analyst-degrees-of-freedom point from Week 13's forking paths, now in regression clothing. Then the ethical question ("which would you report?") has a visual anchor.

**D. Train/test overfitting demo (10 min, answers Design Challenge 1 properly).** Split the crime dataset 60/40. Fit the kitchen-sink model and the two-predictor model on the training rows; compute prediction errors on the held-out rows. The kitchen-sink model wins in-sample and loses out-of-sample. This is achievable in Excel (INDEX ranges) or five lines of Python, and it converts "overfitting" from a warning into an observed event — also planting A&W §10-7 (Validation) for the full-analysis weeks.

**E. Output-table relay (8 min, Part 2 alternative).** Project the worked-example table; students in sequence each take one number (a coefficient, an SE, a t, a p, R², Adj R², F) and must say its one-sentence meaning aloud, no repeats. Fourteen sentences later the whole table has been verbalised — directly attacks Design Challenge 4's "too many numbers" problem.

## 4. Critique of the Lesson Plan

**What works (keep):** the sequential four-model confound hunt (the strongest single activity in the course — the coefficient-instability *experience* is what multiple regression pedagogy usually lacks); T7's accounting-identity diagnostic (superb, and rare in textbooks); the "which model is most honest?" ethical turn with its Forward-College framing; T4/T5's internally consistent output tables (they check out against the F-from-R² formula — most fabricated outputs don't).

**Problems, reasons, and fixes:**

1. **The session examines three topics its reading never assigns (see §1):** heteroskedasticity (§11-8a) in T3, dummy variables (§10-6a) in T2/T6, interactions (§10-6b) in T7. The flipped-classroom contract — pre-work covers the concepts, class applies them — breaks in the week with the heaviest conceptual load. *Fix:* extend the reading as in §1; total added pages ≈ 25, offset by making §11-6 (stepwise) skim-only since it gets one question part.
2. **The Part 3 dataset doesn't exist yet.** The activity requires a 25-city dataset engineered so that (i) the unemployment slope drops materially when income enters, and (ii) police force size carries a reverse-causality signature. That takes deliberate construction (generate income correlated ~−0.7 with unemployment, both driving crime; make police size a *function* of crime plus noise) and pre-testing — the same "non-negotiable prep" standard Week 8's Design Challenge 2 set for its messy dataset. *Fix:* an instructor-notes spec with the generating equations and the expected coefficient path, so the "what the class should find" paragraph is guaranteed rather than hoped for.
3. **The n = 25 cities choice undercuts the inference theme.** With four predictors and 25 observations, every SE is huge and *nothing* will be significant — which muddies the "watch the coefficient change" story with "and also everything is insignificant." *Fix:* 60–80 cities keeps the confounding phenomenon while leaving enough power for the t-test discussion to make sense. (Alternatively, keep 25 and make small-n fragility an explicit fifth question — but choose deliberately.)
4. **Toolchain still undecided mid-sentence** ("provided as an Excel file or loaded via Python"). By Week 15 this should be a settled convention (see Weeks 12/14 supplements): Excel primary for exam alignment, a mirrored notebook available. One line fixes it.
5. **The multiple-testing thread from Week 13 is left implicit.** Part 3 runs four models × four coefficients ≈ 16 implicit tests, and the bridge question in Week 13 explicitly promised this concern would be "revisited directly in Week 15" — but no part of this session names it. *Fix:* Activity A above, or one debrief line: "you just ran ~16 coefficient tests; at α = 0.05, roughly one significant-looking coefficient in this room is noise."
6. **T5(b) prints its solution inside the question** — the only leakage this week; move to the key. (Notably, this week is otherwise the cleanest on answer separation — its structure should be the template for retro-fixing Weeks 4, 5, 11, 12, 13.)
