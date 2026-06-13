# Chapter 2: Describing the Distribution of a Single Variable
## Core Concepts Summary
*Albright & Winston, Business Analytics: Data Analysis & Decision Making (6th ed.)*

---

## The Central Question

Before calculating anything, ask: **what are we actually trying to learn from this data?**

For any single variable, the questions are:
1. What value is most *typical*?
2. How *spread out* are the values?
3. What are the *extremes*?
4. Is the distribution *symmetric*, or skewed?
5. Are there anything *unusual* about the shape — outliers, clusters, gaps?

The chapter builds from data types → summary measures → charts → special cases (time series, outliers, missing data).

---

## 1. Types of Data

**Why it matters first:** the type of data determines what you can do with it.

### Categorical vs. Numerical

| Type | Definition | Examples | Arithmetic? |
|------|-----------|---------|-------------|
| Categorical | Values are labels, not quantities | Gender, Region, Opinion (1–5 scale) | No |
| Numerical | Arithmetic is meaningful | Age, Salary, Children | Yes |

**Trap:** Numbers that look numerical but are actually categorical — phone numbers, zip codes, Social Security numbers, Likert scale codes. Performing arithmetic on these produces meaningless results.

### Within Categorical: Nominal vs. Ordinal

- **Nominal**: no natural ordering (Gender, Region)
- **Ordinal**: natural ordering exists (Opinion: Strongly Disagree → Strongly Agree)

### Within Numerical: Discrete vs. Continuous

- **Discrete**: arises from counting (number of children, defects per shipment)
- **Continuous**: arises from measurement (salary, height, temperature)

### Binning (Discretising)

A continuous variable can be converted to categorical by grouping values into ranges (e.g. salary → "under $40K / $40K–$70K / over $70K"). Called **binning** or **discretising**. Common in practice; the appropriate bin widths depend on the analysis purpose.

### Dummy Variables

A 0/1 coded categorical variable. E.g. Gender coded as 1 = Male, 0 = Female. Useful because the SUM gives a count and the AVERAGE gives a percentage — no COUNTIF needed. Dummy variables appear throughout analytics (especially in regression).

### Cross-Sectional vs. Time Series

- **Cross-sectional**: snapshot of many observations at one point in time (survey responses)
- **Time series**: one or more variables tracked over time (monthly DJIA, annual crime rates)

Different data types require different analyses.

---

## 2. Describing Categorical Variables

The only meaningful way to summarise a categorical variable: **count observations in each category**.

- Raw counts (e.g. 560 Males, 440 Females)
- Percentages (56% Male, 44% Female)
- Visualisation: column chart (preferred) or pie chart

**Key Excel function:** `COUNTIF(range, criterion)`

**Chart advice:** Always set the vertical axis to start at zero. A scale starting at 6700 can make a near-even split look like a large gap — the same information, misleading interpretation.

---

## 3. Describing Numerical Variables

### 3a. Measures of Central Tendency

**Mean** — the arithmetic average. Sensitive to extreme values.

$$\bar{X} = \frac{\sum X_i}{n}$$

**Median** — the middle value when sorted. Unaffected by outliers. For skewed data, the better representation of "typical."

**Mode** — the most frequently occurring value. Often not meaningful for continuous data; more useful when data cluster at specific values (e.g. minimum salary occurring 44 times in baseball data).

**The key insight:** When the mean and median diverge substantially, the data is skewed. The gap tells you something real about the distribution — not just a calculation quirk.

> Example: MLB 2015 salaries — mean $4.2M, median $1.65M. The mean is inflated by a handful of star players (Clayton Kershaw at $31M). Most players earn far less. For "typical player salary," the median is the honest answer.

### 3b. Minimum, Maximum, Percentiles, and Quartiles

For percentage *p*, the **p-th percentile** is the value below which p% of observations fall.

**Quartiles** divide data into four equal groups:
- Q1 (25th percentile)
- Q2 (50th percentile = median)
- Q3 (75th percentile)

The inverse question: given a value (e.g. $1M salary), what percentage of observations fall below it? Use `COUNTIF` with concatenated condition: `=COUNTIF(range,"<="&value)/COUNT(range)`

### 3c. Measures of Variability

**Range** = Max − Min. Simple but sensitive to extremes.

**Interquartile Range (IQR)** = Q3 − Q1. The range of the middle 50% of data. More robust to outliers than range.

**Variance** — average of squared deviations from the mean. In squared units (e.g. dollars²), which is not interpretable on its own.

$$s^2 = \frac{\sum(X_i - \bar{X})^2}{n-1}$$

**Standard Deviation** — square root of variance. Returns units to the original scale (e.g. dollars). The most commonly quoted measure of spread.

**Mean Absolute Deviation (MAD)** — average of absolute (not squared) deviations. More intuitive, less mathematically convenient. Rule of thumb: SD ≈ 1.25 × MAD.

> "Variability is the enemy." — a supplier with parts averaging 100cm diameter but with SD = 25cm is far more dangerous than one with SD = 3cm, even if the means are identical.

### 3d. The Empirical Rules (68-95-99.7 Rule)

For data that is **approximately normally distributed** (symmetric, bell-shaped):

- ~68% of observations fall within **1 SD** of the mean (X̄ ± s)
- ~95% fall within **2 SD** of the mean (X̄ ± 2s)
- ~99.7% fall within **3 SD** of the mean (X̄ ± 3s)

**Crucial caveat:** These rules break down for skewed distributions. For the baseball salaries, the lower bounds go negative (impossible for salaries), and only 85% — not 68% — fall within 1 SD. Always check whether the assumption of normality holds before applying these rules.

### 3e. Measures of Shape

**Skewness** — measures asymmetry.
- Positive (right) skew: a few very large values pull the mean above the median
- Negative (left) skew: a few very small values pull the mean below the median
- Zero: symmetric

**Kurtosis** — measures "fat tails" (extreme observations relative to a normal distribution). High kurtosis means more extreme events than you'd expect from normality. Relevant to financial risk: the 2008 Wall Street crisis was partly attributed to models that assumed normal distributions when real distributions had far fatter tails.

---

## 4. Charts for Numerical Variables

### Histograms

A column chart where values are grouped into bins and bar height represents count (or frequency). The most common chart for showing the full shape of a distribution.

Key decisions:
- How many bins? Too few: hides structure. Too many: looks noisy.
- Where to start? Bin convention: bars are "greater than" the left boundary and "≤" the right boundary.

A histogram reveals what no single summary measure can: centre, spread, skewness, and shape all at once.

> Summary measures describe one aspect. A histogram gives the complete picture.

### Box Plots (Box-Whisker Plots)

Shows: Q1, median, Q3 (the box), whiskers extending to 1.5×IQR from the box edges, and individual outliers beyond that.

- **Box**: the middle 50% of data
- **Line inside box**: median
- **Asterisk**: mean
- **Whiskers**: most observations outside the box
- **Dots beyond whiskers**: mild outliers (1.5–3 IQR) and extreme outliers (>3 IQR)

Most useful for **comparing distributions** side by side (e.g. salaries for pitchers vs. non-pitchers, revenue by region).

---

## 5. Time Series Data

Standard summary measures (mean, median, SD) and histograms **lose the time dimension** — often the most important thing about time series data.

Use **time series graphs** instead: values on the Y-axis, time on the X-axis. These reveal trends, seasonality, and structural breaks.

**Useful transformation:** instead of summarising raw time series values, compute **period-to-period percentage changes** and summarise those. These are often more stable and interpretable.

> Example: The Dow Jones from 1950–2015. Mean = 4,137, median = 1,020 — neither is meaningful for understanding current or future values. But the percentage changes have a near-normal distribution with mean ≈ 0.66% and SD ≈ 4.1%, and the empirical rules apply well.

---

## 6. Outliers

An **outlier** is a value that lies well outside the norm. Not necessarily an error.

**Detection methods:**
- Values more than 3 SDs from the mean (empirical rule definition)
- Box plot definition: mild outliers > 1.5 IQR from box edge; extreme > 3 IQR

**What to do:**
- If it's a data entry error → correct it
- If it's legitimate → do **not** simply delete it to produce "nicer" results
- Best practice: **run the analysis twice** — with and without the outlier — and report both

> Eliminating Clayton Kershaw's $31M salary to get a "better" picture of typical player salaries might be defensible; eliminating it to make your model look cleaner is not.

Outliers can also be **unusual combinations** of otherwise-normal values (e.g. Age = 10, Height = 72 inches). These require scatter plots to detect — not univariate analysis.

---

## 7. Missing Values

Real datasets almost always have gaps. Two issues:

**Detection:** Missing data isn't always blank cells. Common coding conventions: −9999, 9999, asterisks, dashes. Replace with blanks using Find & Replace before analysis.

**What to do:**
- **Ignore** (let Excel/StatTools handle): Excel's AVERAGE and StatTools both automatically exclude missing values from calculations
- **Impute with column mean**: a common but often poor choice — there's no reason to assume missing values are average values
- **Impute using related variables**: a person's age, education, and job type can predict a missing salary. More defensible but complex.

No universally correct answer. The best approach depends on how much data is missing and why.

---

## 8. Excel Tables

A formal Excel Table (Insert → Table or Ctrl+T) provides:

- **Filtering** by any variable via dropdown arrows — hides rows rather than deleting them
- **Sorting** in ascending/descending order
- **Total row** that summarises only visible (non-filtered) rows
- **Auto-expansion**: adding new rows/columns automatically extends the table, updating any linked charts or formulas

**Key Excel functions introduced in this chapter:**

| Function | Purpose |
|----------|---------|
| `AVERAGE` | Mean |
| `MEDIAN` | Median |
| `MODE` / `MODE.SNGL` | Mode |
| `MIN`, `MAX` | Extremes |
| `PERCENTILE` / `PERCENTILE.INC` | Arbitrary percentile |
| `QUARTILE` / `QUARTILE.INC` | Quartiles |
| `VAR.S`, `VAR.P` | Sample/population variance |
| `STDEV.S`, `STDEV.P` | Sample/population SD |
| `AVEDEV` | Mean absolute deviation |
| `SKEW` | Skewness |
| `KURT` | Kurtosis |
| `COUNTIF` | Count matching a condition |
| `VLOOKUP` | Lookup table transformations |

---

## The Takeaway

Descriptive statistics **compress** information. Compression is useful — it makes data interpretable. But compression also **hides** things: outliers, skewness, bimodal distributions, time trends. A good analyst knows what they're reporting *and* what their summary measure is unable to show.

> "The average rent in Berlin is €1,200/month — affordable for most residents."
> Mean = €1,200, Median = €950, SD = €800.
> The average is technically correct. But it obscures that half of renters pay under €950, and that a wide spread means affordability varies enormously across the city. A single number cannot carry that story.

---

*Source: Albright, S.C. & Winston, W.L. (2017). Business Analytics: Data Analysis & Decision Making (6th ed.). Cengage. Chapter 2, pp. 19–78.*
