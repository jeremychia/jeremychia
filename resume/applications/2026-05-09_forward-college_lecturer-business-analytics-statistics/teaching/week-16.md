# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 16: Time Series Analysis and Forecasting
**Format:** 90-minute lab seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Decompose a time series into trend, seasonal, and residual components using Python (statsmodels)
- Apply exponential smoothing and Holt-Winters forecasting to a business time series
- Evaluate a forecast by computing MAE and RMSE on a held-out test set
- Critique a forecast model by identifying the assumption about the future that must hold for it to be valid

These map to ST2187 syllabus topic 13 (time series and forecasting) and close the loop on the question planted in Week 2: "what if your variable has a time dimension?" Students who engage with this session will see why summary statistics compress — and lose — the sequence information that defines a time series.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 12 — read the following sections only:
- §12-1 Introduction to time series analysis (pp. 540–541)
- §12-2 Forecasting methods overview and components of time series data (pp. 541–548)
- §12-6 Moving averages forecasts (pp. 565–570)
- §12-7 Exponential smoothing forecasts — simple and Holt's trend model (pp. 570–580)
- §12-8 Seasonal models — Winters' exponential smoothing (pp. 580–590)

The regression-based trend models (§12-4) and random walk model (§12-5) are optional further reading — skip them on first pass unless you want a fuller picture of trend-based approaches.

**Videos (~20 minutes total):**
- [Time Series Decomposition in Python](https://www.youtube.com/watch?v=sAUx8y-rr10) (10 min) — walks through trend, seasonal, and residual decomposition using statsmodels, the same library used in Part 3. *Active watching: when the video plots the three components (trend, seasonal, residual) separately, pause and write: what does the residual component represent — what is "left over" after the trend and seasonal patterns are removed? This is what the assumption statement in Part 3 asks you to be specific about.*
- [Simple Exponential Smoothing](https://www.youtube.com/watch?v=uWCVyQ5GcBM) (10 min) — explains the weighted-average logic and the smoothing parameter α, including what happens at α = 0 and α = 1. *Active watching: when the video shows what happens at the extreme values of α (near 0 vs near 1), pause and write: what kind of series would each extreme be appropriate for — a stable, slowly-changing series or a volatile one? This is T6(d).*

**Pre-work environment check:**
Confirm that `statsmodels` is installed. Test with:
```python
from statsmodels.tsa.seasonal import seasonal_decompose
print("statsmodels OK")
```

*The decomposition video's visual of the residual component is the intuition behind the assumption statement task in Part 3. The exponential smoothing video's α parameter explanation maps directly to T6(d). If either video felt opaque, re-read §12-6 and §12-7 before the tutorial.*

**Worked example (read carefully — class will reproduce and extend this):**

> Dataset: monthly retail sales for a coffee shop chain, 48 months (4 years).
>
> ```python
> import pandas as pd
> import matplotlib.pyplot as plt
> from statsmodels.tsa.seasonal import seasonal_decompose
> from statsmodels.tsa.holtwinters import ExponentialSmoothing
>
> # Load data
> df = pd.read_csv('coffee_sales.csv', parse_dates=['month'], index_col='month')
>
> # Decompose
> result = seasonal_decompose(df['sales'], model='multiplicative', period=12)
> result.plot()
> plt.tight_layout()
> plt.show()
>
> # Fit Holt-Winters
> model = ExponentialSmoothing(df['sales'], trend='add', seasonal='mul', seasonal_periods=12)
> fit = model.fit()
>
> # Forecast 12 months ahead
> forecast = fit.forecast(12)
> print(forecast)
> ```
>
> **What the decomposition shows:**
> - Trend component: overall sales growing ~8% per year
> - Seasonal component: December spikes (holiday gifts), August trough (summer closures)
> - Residual: irregular variation not captured by trend or seasonality
>
> **The critical question:** the Holt-Winters model assumes the seasonal pattern and trend from the past 48 months will continue. If the coffee shop chain opens a new market (say, entering Germany), the historical seasonal pattern from Portuguese stores may not apply. What must stay true for the forecast to be valid?

**Tutorial (attempt before class):**
Using the worked example dataset (shared on the course portal):
1. Run the decomposition and describe the three components
2. Fit a Holt-Winters model and forecast the next 12 months
3. Split the data: use months 1–36 as training, months 37–48 as test. Compute RMSE on the test set
4. What would you tell a manager who asks "how accurate is this forecast for next month?"

**Additional tutorial questions (attempt after the main tutorial tasks above):**

*T5 — Boundary case: what happens when trend and seasonality interact:*

> A sports equipment retailer has monthly sales data for 60 months (5 years). The series shows a strong upward trend (roughly 15% annual growth) and a clear seasonal pattern: January (new year's resolutions) and September (back-to-school/sport season) are consistently the highest months, while June–July is the lowest.
>
> (a) If you decompose this series using an **additive** model (trend + seasonal + residual), the seasonal component adds or subtracts a fixed number of units regardless of trend level. If the business uses a **multiplicative** model, the seasonal swings grow proportionally with the trend. For a business growing rapidly, which model is more appropriate, and why?
> (b) In year 1, the January seasonal effect is +150 units (additive) or +1.30 (multiplicative — meaning January is 30% above trend). By year 5, the trend level has doubled. Under the multiplicative model, what is the January seasonal effect in units?
>
> *Solution:* If trend doubles and multiplier is 1.30, January in year 5 is 30% above a trend level that is twice the year-1 trend level. The absolute seasonal swing has doubled in size. Under the additive model, it would still be only +150 units.
>
> (c) Fit both an additive and multiplicative Holt-Winters model to the first 48 months of your dataset, then evaluate RMSE on months 49–60. Which model has lower RMSE? What does this tell you about which assumption is better supported by the data?
> (d) After month 60, the company enters a price war and lowers prices by 20%. The subsequent 12 months show sharply elevated volumes. What would happen to the accuracy of a Holt-Winters forecast made before the price war, applied to the post-price-war period?
> (e) "A forecast is a conditional projection, not a prediction." Explain what this means in the context of your answer to (d).

*T6 — Comparison: moving average versus exponential smoothing:*

> A manufacturer tracks weekly widget production (units) for 26 weeks. They are considering two forecasting methods:
>
> - **3-week moving average:** forecast for week t = average of weeks t−1, t−2, t−3
> - **Simple exponential smoothing (α = 0.3):** Fₜ₊₁ = α × Yₜ + (1−α) × Fₜ
>
> The last 6 weeks of data are: Week 21: 840, Week 22: 910, Week 23: 875, Week 24: 950, Week 25: 920, Week 26: 990.
>
> (a) Compute the 3-week moving average forecast for week 27.
>
> *Solution:* F₂₇ = (950 + 920 + 990) / 3 = 2,860 / 3 ≈ **953 units**
>
> (b) Assume the exponential smoothing forecast for week 26 is F₂₆ = 880. Compute the SES forecast for week 27 using α = 0.3.
>
> *Solution:* F₂₇ = 0.3 × 990 + 0.7 × 880 = 297 + 616 = **913 units**
>
> (c) Which method responds more quickly to the recent spike at week 26 (990 units)? Explain why in terms of how each method weights historical data.
> (d) For a business with volatile week-to-week demand (noise-dominated series), would a high or low α be more appropriate for exponential smoothing? What about a business with stable underlying demand?
> (e) Neither method captures trend or seasonality. If production has a 4-week seasonal cycle (production spikes at the end of each month due to order deadlines), what would happen to the 3-week MA and the SES forecasts for week 27 if the spike has occurred in weeks 24 and 28 historically?

*T7 — Interpretation: error metrics in business context:*

> A demand forecasting system generates forecasts for two products. You evaluate both on a 12-month test set:
>
> | Product | MAE (units) | RMSE (units) | Mean actual demand |
> |---|---|---|---|
> | Product A (commodity) | 120 | 145 | 1,200 |
> | Product B (perishable) | 85 | 210 | 900 |
>
> (a) For Product A, calculate the Mean Absolute Percentage Error (MAPE): MAPE = MAE / mean actual demand × 100%. Is 10% MAPE good or bad for a commodity product?
> (b) For Product B, the RMSE is more than twice the MAE (210 vs 85). What does this tell you about the pattern of forecasting errors? Are the errors mostly small with a few large ones, or consistently medium-sized?
> (c) Product B is a perishable food item. Over-forecasting leads to wastage (cost: €8 per unit over-forecast); under-forecasting leads to stockouts (cost: €15 per unit under-forecast). Which error direction is more costly? What does this imply for how the forecast should be biased?
> (d) A manager proposes measuring forecasting performance using only RMSE. A data scientist argues MAE is better. In what business situations would you prefer each, and why?
> (e) Neither MAE nor RMSE tells you the *direction* of errors. Explain why tracking the mean error (ME = mean of (actual − forecast)) is also important, and what a consistently positive ME tells you about the forecasting system.

*T8 — Real-world translation: identify the right time series model from a business description:*

> For each of the following business situations, state: (i) whether an additive or multiplicative seasonal model is more likely to be appropriate; (ii) whether simple, Holt's (trend only), or Holt-Winters (trend + seasonal) exponential smoothing should be used; (iii) one assumption that would need to hold for the chosen model to remain valid.
>
> (a) A UK toy retailer's monthly sales data for 8 years. Sales are flat most of the year but spike dramatically in November–December. The spike has been growing in absolute size year on year as the company expands.
>
> (b) A German electricity distributor's daily electricity consumption over 3 years. Consumption follows a weekly seasonal pattern (high on weekdays, low on weekends) and a longer annual pattern (high in winter). No significant trend is observed.
>
> (c) A technology startup's monthly subscription revenue over 18 months. The series shows strong month-on-month growth (35% year-on-year) with no seasonal pattern visible yet.
>
> (d) A restaurant chain's weekly covers (number of customers served) over 2 years. There is a clear weekly cycle (Friday/Saturday peak), a slight annual trend upward, and the seasonal pattern appears to scale proportionally with the growth trend.

*T9 — Current affairs: when a forecast assumption breaks in real time:*

> Throughout 2024–2025, OPEC+ (the alliance of oil-producing countries including Saudi Arabia and Russia) repeatedly changed its production decisions, sometimes reversing announced plans within weeks. In June 2024, OPEC+ announced plans to gradually unwind production cuts starting in Q4 2024, then in September 2024 delayed the unwinding again. In May 2025, eight OPEC+ members announced a larger-than-expected output increase, which pushed Brent crude oil prices below $60/barrel for the first time since 2021.
>
> An energy trading firm had a time series model for monthly Brent crude prices built on 5 years of data (January 2020 – December 2024). The model incorporated historical OPEC+ production patterns and had achieved an RMSE of $3.20/barrel on the 2023 test set. In January 2025, the firm's model forecast Brent crude at approximately $75–80/barrel for Q2 2025. Actual Q2 2025 prices fell to $58–62/barrel.
>
> (a) The forecasting model was trained on data from 2020–2024. What specific assumption was embedded in the model about OPEC+ production behaviour — and why did this assumption fail?
>
> (b) The Q2 2025 RMSE calculated after the fact was approximately $18/barrel, compared to a test-set RMSE of $3.20/barrel from 2023. Does this mean the model was badly built, or that the model was built correctly and applied to a regime it was not designed for? What is the difference?
>
> (c) The firm's risk manager says: "No time series model could have predicted this — it was a structural break." A data scientist responds: "We should have added scenario weights or a Bayesian update for OPEC+ policy risk." What does each person mean? Which is more useful going forward?
>
> (d) The Holt-Winters model you studied assumes that trend and seasonal patterns observed in the past will continue. Identify three specific features of the 2025 oil price situation that each violated a different Holt-Winters assumption.
>
> (e) A junior analyst proposes retraining the model every month with rolling data to "stay current." What would be the advantage and the risk of this approach in an environment where OPEC+ decisions are intermittent and unpredictable?

This question uses verified events: the OPEC+ output increase announcement of May 2025 and subsequent oil price falls are documented by Reuters, the IEA, and the OPEC Secretariat. The specific firm and RMSE figures are illustrative. The question surfaces the key limitation of all time series models — assumption stability — through a live 2025 example where the assumption broke visibly.

---

## Answer Key

### T5 — Additive vs multiplicative seasonality

**(a)** For a rapidly growing business (15% annual growth), the **multiplicative model** is more appropriate. Under an additive model, the seasonal swing is a fixed absolute amount (e.g., +150 units in January every year) regardless of the trend level. But if total volume is growing, it is more realistic for the seasonal swing to scale with the level — January might be 30% above trend whether trend is 500 units or 1,000 units. The multiplicative model captures this: as the trend grows, the absolute seasonal effect grows proportionally.

**(b)** Under the multiplicative model, the January seasonal multiplier is 1.30 (30% above trend). In year 5, trend has doubled vs year 1. The January seasonal effect in units = 1.30 × (2 × year-1 trend level) − (2 × year-1 trend level) = 0.30 × (2 × year-1 trend level). The absolute January spike has **doubled** in unit terms. Under the additive model, it would still be +150 units — half as large in year 5 as the multiplicative model predicts.

**(c)** If the RMSE on months 49–60 is lower for the multiplicative model, the data support that seasonal swings have been scaling with trend — the multiplicative assumption is better supported. If the additive model has lower RMSE, the seasonal swings have been roughly constant in absolute size despite growth. Comparing RMSE on the held-out test set is the correct empirical method for choosing between the two structures.

**(d)** The Holt-Winters model assumes the trend and seasonal pattern observed in the training data will continue. A 20% price cut causing a structural demand shift violates this assumption: the model's parameters (trend, seasonal factors, smoothing weights) were estimated from pre-price-war data and cannot anticipate the regime change. Forecasts would systematically under-predict post-price-war demand because the model does not know a structural break has occurred.

**(e)** "A forecast is a conditional projection, not a prediction" means: every forecast is contingent on the assumption that the conditions underlying the model remain unchanged. The Holt-Winters forecast says: "If pricing, competitive conditions, and market behaviour continue as in the training period, then demand will be approximately X." The price war violates that condition. The forecast is not wrong in a modelling sense — it is applying the right model to the wrong regime. A prediction (in the colloquial sense) claims to state what will actually happen; a conditional projection states what would happen if specific conditions hold.

---

### T6 — Moving average vs exponential smoothing

**(a)** 3-week moving average forecast for week 27 = (Week 24 + Week 25 + Week 26) / 3 = (950 + 920 + 990) / 3 = 2,860 / 3 ≈ **953 units.**

**(b)** SES forecast for week 27: F₂₇ = 0.3 × Y₂₆ + 0.7 × F₂₆ = 0.3 × 990 + 0.7 × 880 = 297 + 616 = **913 units.**

**(c)** The 3-week moving average responds more quickly to the recent spike. In the MA, week 26 (990 units) receives equal weight (1/3) as weeks 24 and 25 — the spike enters the forecast immediately at full weight. In SES with α = 0.3, week 26 receives only 30% weight; the remaining 70% is spread across all prior history via F₂₆ = 880. The SES forecast (913) is further from week 26 than the MA forecast (953) precisely because SES dampens recent observations. Higher α → more responsive to recent observations.

**(d)** For **volatile demand (noise-dominated):** a **low α** is more appropriate — it averages over recent fluctuations rather than chasing noise, producing more stable forecasts. For **stable underlying demand with meaningful recent signals:** a **high α** is more appropriate — it responds quickly to genuine shifts in the level. The key judgment: is recent variation signal (a real change in demand) or noise (random fluctuation)? High α treats recent observations as signal; low α treats them as noise.

**(e)** Neither the 3-week MA nor the SES model captures the 4-week seasonal cycle. If production spikes in weeks 24 and 28 historically: the 3-week MA for week 27 uses weeks 24, 25, 26 — it includes the week-24 spike (950) and the non-spike weeks (920, 990), so it averages in the spike but doesn't predict week 27 correctly if the cycle puts the spike at week 28. Both methods would produce forecasts that lag behind the seasonal pattern — consistently under-forecasting spike weeks and over-forecasting off-peak weeks. Seasonal adjustment (using Holt-Winters with a period of 4) would be needed to capture this cycle.

---

### T7 — Error metrics in business context

**(a)** Product A MAPE = MAE / mean actual demand × 100% = 120 / 1,200 × 100% = **10%.** Whether 10% is good depends on the industry and the purpose of the forecast. For a commodity product (relatively stable demand), 10% MAPE is moderate — acceptable for strategic planning but potentially too wide for tight inventory management. Comparison with industry benchmarks or the business decision's sensitivity to forecast error is necessary.

**(b)** Product B RMSE (210) is more than twice the MAE (85). RMSE penalises large errors more heavily than MAE. When RMSE >> MAE, it indicates a distribution of errors with **mostly small errors but a few very large outliers** — the average absolute error is 85 units (small), but some months have errors large enough to drive the RMSE to 210. The squared errors from those few large deviations dominate the RMSE. This pattern is often seen in demand with occasional sharp spikes that the model misses.

**(c)** Under-forecasting (stockout) costs €15/unit; over-forecasting (wastage) costs €8/unit. Since stockouts are more costly, **under-forecasting is worse.** The forecast should be **biased upward** (systematically over-forecast slightly) to reduce the expected cost of stockouts. This is equivalent to building a safety stock or using a demand quantile above the median as the forecast target — the optimal bias point balances the asymmetric costs. (Formally: the newsvendor model sets the optimal stocking level at the demand quantile q = cost_of_underage / (cost_of_underage + cost_of_overage) = 15/(15+8) ≈ 65th percentile.)

**(d)** RMSE is preferred when **large errors are disproportionately costly** — production schedule disruptions, emergency air freight, lost large contracts — because it squares errors and weights large deviations heavily. Use it when a few large misses are much worse than many small ones. MAE is preferred when **errors of all sizes are roughly equally costly** — steady inventory decisions, routine reordering — because it treats each unit of error the same. MAE is also more robust to outliers and easier to explain to non-technical stakeholders.

**(e)** Mean Error (ME) tracks the **direction** of systematic bias. A consistently positive ME (actual > forecast) means the system is systematically under-forecasting — it is biased low. This is operationally important even if RMSE and MAE are acceptable: a biased system causes systematic stockouts (or systematic overstock if ME is negative), regardless of how small the average magnitude of errors is. RMSE and MAE tell you error size; ME tells you error direction. A good forecasting system should have ME ≈ 0 (unbiased on average) alongside low MAE/RMSE.

---

### T8 — Identifying the right time series model

**(a)** Toy retailer (UK, 8 years, flat most of year, growing November–December spike): (i) **Multiplicative** — the spike is growing in absolute size as the company expands, consistent with the seasonal swing scaling with trend level. (ii) **Holt-Winters (trend + seasonal)** — both a growing trend and a strong seasonal cycle are present. (iii) Required assumption: the growth rate and the seasonal multiplier remain stable going forward. A change in the mix of in-store vs online sales, or a competitor entry, could change the seasonal pattern.

**(b)** German electricity distributor (daily, weekly + annual seasonality, no trend): (i) **Additive** — electricity consumption has a relatively stable baseline; the weekly and annual swings are roughly constant in size rather than scaling with an absent trend. (ii) **Holt-Winters seasonal only** (or a double-seasonal Holt-Winters) — trend component is not needed; the seasonal cycle is present at two frequencies (weekly and annual). (iii) Required assumption: grid load patterns remain stable. A large-scale adoption of EVs or industrial demand shifts could change the seasonal structure.

**(c)** Technology startup (monthly, 18 months, 35% YoY growth, no seasonal pattern yet): (i) Not applicable — no seasonality visible. (ii) **Holt's (trend only) exponential smoothing** — captures the exponential growth trend without seasonal adjustment. Simple SES would lag a rapidly growing series. (iii) Required assumption: the growth rate is stable. Startup revenue growth is highly uncertain; if the company saturates a market segment or faces competition, the trend assumption could break quickly.

**(d)** Restaurant chain (weekly, Friday/Saturday peak, slight annual trend, proportional seasonal cycle): (i) **Multiplicative** — the seasonal pattern (Friday/Saturday vs weekday covers ratio) appears to scale with the upward trend. (ii) **Holt-Winters (trend + seasonal, multiplicative)** — both trend and scaling seasonal pattern present. (iii) Required assumption: the weekly seasonal multipliers are stable. Menu changes, pricing strategy, or a new competitor opening nearby could shift the peak/off-peak ratio.

---

### T9 — When a forecast assumption breaks: OPEC+ 2025

**(a)** The model embedded the assumption that **OPEC+ production behaviour would follow patterns similar to 2020–2024** — specifically, that production cuts would be maintained or only gradually unwound, consistent with the group's stated coordination objectives. This assumption failed because OPEC+ members made a larger-than-expected, faster-than-expected output increase in May 2025, driven by internal disagreements (particularly members exceeding quotas), Saudi Arabia's decision to defend market share over price, and geopolitical dynamics that were not predictable from historical production patterns. The structural relationship between OPEC+ policy and oil price that the model was trained on broke.

**(b)** The model was **built correctly and applied to a regime it was not designed for** — not badly built. A test-set RMSE of $3.20 on 2023 data was a legitimate performance evaluation under the conditions that prevailed during that period. The 2025 structural break (a large coordinated policy reversal driven by internal OPEC+ dynamics) is fundamentally different from the "noise" that validation RMSE measures. A bad model would have poor RMSE on the 2023 test set. The 2025 failure reveals the limits of what historical calibration can predict, not a modelling error.

**(c)** The risk manager means: "A structural break is a regime change — a qualitative shift in the data-generating process — that cannot be forecast by extrapolating from prior patterns. No amount of model sophistication can predict genuinely novel policy decisions." The data scientist means: "We can incorporate model uncertainty about OPEC+ behaviour by assigning probabilities to different policy scenarios (e.g., hold cuts / gradually unwind / accelerate unwind) and weighting the forecasts accordingly. A Bayesian update would adjust these probabilities as new signals (meeting announcements, market data) arrive." The data scientist's approach is more useful going forward: it cannot predict the decision but can produce a forecast with honest uncertainty bands and contingency scenarios, which is more useful for risk management than a single-point forecast.

**(d)** Three 2025 oil price features that violated different Holt-Winters assumptions: (i) **Trend assumption violated:** Holt-Winters assumes the trend is relatively stable (slow acceleration/deceleration). The shift from gradual unwinding to rapid output expansion caused a sharp downward price trend that reversed the model's prior upward or stable trend estimate. (ii) **Seasonal pattern assumption violated:** Holt-Winters assumes seasonal patterns repeat with consistent timing. The OPEC+ decision in May 2025 (an unusual month for large production shifts) created a non-seasonal shock that the model attributed to seasonal variation rather than a structural policy change. (iii) **Error term independence assumption violated:** Holt-Winters assumes residuals are random and independent. After the May announcement, oil price errors became serially correlated — the price stayed below $65/barrel consistently, not randomly — because a persistent structural cause (higher output) was driving prices down, not mean-reverting noise.

**(e)** Advantage of monthly retraining: the model's parameters (trend, smoothing weights) adapt quickly to recent data, making it more responsive to genuine regime changes once they are visible in the data. In an environment where conditions actually change, a model retrained on recent data will track the new level/trend faster than one calibrated on a long historical window that dilutes recent signals. Risk: in a volatile environment where OPEC+ decisions are intermittent and unpredictable, retraining monthly may cause the model to **overfit to noise** — chasing short-term price movements that will mean-revert, rather than tracking a genuine new trend. If a policy surprise pushes prices to $58/barrel in month 1 but the "true" structural level is $68/barrel, monthly retraining may embed the temporary shock into the model's parameters, causing systematic forecast errors in subsequent months.

---

## In-Class Session (90 minutes)

### Part 1 — Opening Challenge (10 minutes)

No Mentimeter this week — replaced by a live challenge.

The instructor projects a time series plot (raw data, no decomposition). Students spend 3 minutes writing answers to:
- Does this series have a trend? An upward or downward one?
- Is there a seasonal pattern? How can you tell?
- If you had to make a guess about the next month — what would it be, and how confident are you?

After 3 minutes: the instructor runs the decomposition in Python live. Students compare their intuitions against the decomposed components.

This is the "prediction before computation" principle: students who commit to an estimate before seeing the answer engage more actively with the gap between intuition and model output.

---

### Part 2 — Live Coding: Decompose and Forecast (20 minutes + 10 minutes buffer)

Instructor walks through the full worked example code, explaining each choice:

- **Model type (multiplicative vs additive):** if the seasonal swings grow proportionally with the trend (larger highs and lower lows as sales grow), use multiplicative. If they stay constant, use additive. The decomposition plots help judge which applies.

- **`seasonal_periods=12`:** this tells the model to look for patterns that repeat every 12 months. If the data is weekly, use 52. If daily with a 7-day pattern, use 7.

- **Forecasting horizon:** the model will forecast reliably for approximately 1 seasonal period ahead (12 months for monthly data). Beyond that, uncertainty compounds rapidly.

**Error metrics live:**
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

train = df['sales'].iloc[:36]
test = df['sales'].iloc[36:]

model = ExponentialSmoothing(train, trend='add', seasonal='mul', seasonal_periods=12)
fit = model.fit()
pred = fit.forecast(12)

mae = mean_absolute_error(test, pred)
rmse = np.sqrt(mean_squared_error(test, pred))
print(f"MAE: {mae:.1f}, RMSE: {rmse:.1f}")
```

Buffer: if the environment has issues, the buffer absorbs setup time. Also use it to compare MAE vs RMSE — "RMSE penalises large errors more heavily than MAE. For a business that can absorb small errors but not large ones (e.g., a perishable goods supplier), RMSE is the better metric."

---

### Part 3 — Forecast Critique (25 minutes)

**Orientation (5 minutes before pairs start):** Time series analysis is new for most students — unlike descriptive statistics or regression, it is unlikely to have appeared in any prior course. Before pairs begin, the instructor projects a 3-point orientation:

1. *The structure of a time series*: observations in sequence, where the order matters. A histogram of the same values would lose that order entirely.
2. *What decomposition does*: separates the systematic (trend, seasonality) from the noise (residual). The forecast extrapolates only the systematic parts.
3. *The one question to hold throughout*: "What has to stay true in the future for this extrapolation to be valid?"

This is not a mini-lecture — it is framing. Two minutes, three points, then pairs begin. Students who already understood the worked example will find this fast; students for whom the code felt opaque will find it clarifying.

Pairs receive a dataset (different from the worked example) and must:

1. Decompose the series and describe what they see
2. Fit a Holt-Winters model and produce a 6-month forecast
3. Evaluate on a 6-month held-out test set
4. Write one paragraph: "This forecast assumes ___. This assumption would break if ___."

**Revised deliverable expectation:** the fourth task is the core, and it is sufficient on its own. Pairs who complete the decomposition and assumption statement but don't finish the evaluation have still done the most important work. The evaluation (RMSE on test set) is a check, not the point — the point is the assumption paragraph. Do not compress the assumption statement to finish the evaluation.

Examples of assumption statements:
- "This forecast assumes the seasonal pattern from the past 3 years will repeat. It would break if the business changed its product mix, expanded to a new market, or faced a supply shock."
- "This forecast assumes the current growth trend continues. It would break if the market reaches saturation or a competitor enters."

The assumption statement is not a weakness of the model — it is the responsible communication of what the model requires. Students who can write this paragraph clearly have understood what forecasting actually is: not prediction, but conditional projection.

---

### Part 4 — Debrief and Peer Review (20 minutes)

Two pairs present their forecasts (5 minutes each: chart + assumption statement). The rest of the class asks:
- Is the assumption statement specific enough? ("It would break if anything changes" is not useful.)
- What data could you collect to test whether the assumption is currently holding?
- If the forecast is wrong, in which direction is it more likely to be wrong — and why?

The directional error question is practically important: a retailer who over-forecasts demand will overstock; one who under-forecasts will have stockouts. For perishables, over-forecasting is worse (waste); for non-perishables, under-forecasting may be worse (lost sales). The direction of likely error depends on the nature of the business.

---

### Part 5 — Debrief (10 minutes)

**Close the loop:**

*"We decomposed time series and built forecasts. The question planted in Week 2 was: 'What if your variable has a time dimension?' What's the answer?"*

The answer: if a variable has a time dimension, summary statistics (mean, SD, histogram) lose the most important information — the sequence. A time series model explicitly preserves and models the sequence. The decomposition separates what's systematic (trend, seasonality) from what's noise (residual). A forecast is an extrapolation of the systematic parts.

**Bridge forward to Week 17:**

> *"Time series models describe what happened and project what might happen next. Next week we ask a different question: what should happen? Given constraints — staff hours, budgets, machine capacity — what's the optimal allocation? That's linear programming, and the tools are completely different from everything we've done so far."*

---

## After Class (Student Post-Work)

No separate LMS post — the forecast notebook (with decomposition, model, evaluation, and assumption statement) is the lab output. Students who finish early: extend the model by comparing Holt-Winters against a simple moving-average forecast. Which has lower RMSE on the test set?

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Opening challenge: predict before computing | Bjork (1994): generation effect — predictions made before seeing the answer encode more deeply than passive exposure; comparing intuition to model output is more engaging than running the model cold |
| Week 2 callback ("what if your variable has a time dimension?") | Cepeda et al. (2006): spacing effect — retrieving the Week 2 question after 14 weeks of material and resolving it provides durable closure; the course arc has been building toward this |
| Assumption statement as mandatory deliverable | Forward College Year 3: accountability and communication; a forecast without a stated assumption is not a complete analytical product; teaching students to write the assumption statement produces professional-grade output |
| Error metrics (MAE, RMSE) introduced in context of a business decision | The choice between MAE and RMSE depends on the cost structure of errors; framing it as a business decision rather than a formula makes the choice meaningful |
| No Mentimeter this week | Block 4 (Weeks 16–22): opening challenge replaces retrieval quiz in lab weeks; the challenge is more diagnostic for applied skills than multiple-choice questions |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Opening challenge: predict from raw series | 10 min | 3 min individual prediction; reveal decomposition |
| Live coding: decompose and forecast | 20 min | Full pipeline; error metrics |
| Buffer (explicit) | 10 min | Environment setup; MAE vs RMSE discussion |
| Forecast critique: pairs | 25 min | Decompose + forecast + evaluate + assumption statement |
| Peer review | 20 min | Two pairs present; directional error question |
| Debrief | 10 min | Week 2 callback; bridge to Week 17 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Students may report a forecast without uncertainty intervals.

Holt-Winters produces point forecasts; the prediction interval requires additional computation. Students who report "sales will be 1,240 units in January" without any uncertainty band are missing a critical element.

**Resolution:** in the live coding, add: `fit.forecast(12, confidence_intervals=0.95)` if the library supports it, or explicitly note: "This is a point forecast. The actual value will almost certainly be different. At minimum, state that forecasting accuracy typically degrades as the horizon extends." Professional forecasts always include a confidence band; the session should model that expectation.

---

### 2. The seasonality type (multiplicative vs additive) is a judgment call that students may not make confidently.

The textbook rule (multiplicative if swings grow proportionally with level) is straightforward to state but requires visual judgment to apply.

**Resolution:** show both decompositions for the same dataset and ask which fits better. The multiplicative model with heteroskedastic residuals is the visual test. If students can't tell from the decomposition plot, they should try both models and compare RMSE.

---

### 3. The "assumption statement" paragraph is a writing task embedded in a technical session.

Students in a statistics session may resist being asked to write a paragraph. They came to code, not write.

**Resolution:** frame it explicitly as the most important output: "The code runs; any machine can run code. The paragraph tells your manager what to watch out for. That's the analyst's job, not the algorithm's." For Forward College Year 3 students who have had two years of communication training, this framing should land.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
