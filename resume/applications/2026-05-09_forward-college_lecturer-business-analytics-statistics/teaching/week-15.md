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
