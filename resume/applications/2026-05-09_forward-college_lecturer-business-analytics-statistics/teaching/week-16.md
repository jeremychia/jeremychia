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
- [Time Series Decomposition — StatQuest](https://www.youtube.com/watch?v=2Sw3_ALJ3GE) (10 min)
- [Exponential Smoothing — StatQuest](https://www.youtube.com/watch?v=k4HFQCMoVrc) (10 min)

**Pre-work environment check:**
Confirm that `statsmodels` is installed. Test with:
```python
from statsmodels.tsa.seasonal import seasonal_decompose
print("statsmodels OK")
```

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

Pairs receive a dataset (different from the worked example) and must:

1. Decompose the series and describe what they see
2. Fit a Holt-Winters model and produce a 6-month forecast
3. Evaluate on a 6-month held-out test set
4. Write one paragraph: "This forecast assumes ___. This assumption would break if ___."

The fourth task is the core. Examples of assumption statements:
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
