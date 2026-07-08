# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 6: Python — Descriptive Statistics and Visualisation
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Apply** Python (pandas, matplotlib, seaborn) to compute descriptive statistics — mean, median, standard deviation, quartiles, skewness, kurtosis — on real-world datasets (Bloom's: Apply).
2. **Translate** manually computed Week 2 statistics into equivalent Python code and reconcile discrepancies caused by differing quartile methods, NaN handling, and floating-point arithmetic (Bloom's: Analyse).
3. **Construct** histogram and box-plot visualisations, adjusting parameters (bin count, axis labels, titles) to accurately represent distributional shape without misleading the reader (Bloom's: Apply / Evaluate).
4. **Diagnose** common data-loading issues — missing values, dtype inference errors, encoding problems — using `df.info()`, `df.describe()`, and `df.isnull().sum()` (Bloom's: Analyse).

---

## Before Class (Student Pre-Work)

**Environment check / install:**

Students must confirm the following are installed and working before arriving. A `pre-check.py` script will be posted to the LMS; running it without errors is the minimum bar.

```python
# pre-check.py — paste into terminal: python pre-check.py
import sys
print("Python:", sys.version)
import pandas as pd; print("pandas:", pd.__version__)
import matplotlib; print("matplotlib:", matplotlib.__version__)
import seaborn as sns; print("seaborn:", sns.__version__)
import numpy as np; print("numpy:", np.__version__)
print("All packages OK")
```

Required: Python 3.10+, pandas >= 1.5, matplotlib >= 3.6, seaborn >= 0.12. Recommended install path: Anaconda or `pip install pandas matplotlib seaborn`. Students on Windows should use Anaconda; students on Mac can use either.

**Reading:**

- Albright & Winston, Chapter 2: "Describing the Distribution of a Single Variable" — focus on §2-4, pp. 30–54 (measures of centre, spread, shape; charts), plus §2-6, pp. 61–63 (outliers and missing values — directly behind Tasks 3 and 5). Skip the StatTools walkthroughs: this course replaces the book's Excel/StatTools toolchain with Python — the statistics transfer, the keystrokes don't.
- Albright & Winston, Chapter 3: revisit §3-4, pp. 95–108 (scatter plots, correlation coefficient — first assigned in Week 3). Regression returns properly in Weeks 14–15.
- Optional: Python for Data Analysis (McKinney), Chapter 5: "Getting Started with pandas" — pp. 130–155 for students who have not used pandas before.

**Pre-work task:**

Return to the open-data dataset you used in Week 2 (from data.gov.sg, daten.berlin.de, opendata.paris.fr, or dados.gov.pt). Your task before class is to:

1. Download the dataset as a CSV (if you used Excel previously, export it).
2. Open a Jupyter notebook and run the following three lines successfully:

```python
import pandas as pd
df = pd.read_csv('your_dataset.csv')
print(df.head())
```

3. Write down (in your notebook, as a markdown cell): the column you will use for your in-class analysis, and the mean and median you computed manually in Week 2.

If your Week 2 dataset no longer works (broken URL, format changed), a fallback dataset — `berlin_wages_2023.csv` — is available on the LMS. The pre-work is intentionally short: the goal is to arrive with a working environment and a clear variable in mind, not to complete any analysis.

---

## In-Class Session (90 minutes)

### Part 1 — Live Tool Challenge (10 minutes)

**Challenge:** "In 5 minutes, use pandas to produce the mean, median, and standard deviation of this dataset. Go."

The instructor projects a 10-row CSV on screen (also posted to the class Slack/Teams channel so students can download it immediately):

```
employee_id,weekly_salary_eur
1,1200
2,1400
3,1350
4,1250
5,1300
6,1450
7,1200
8,1380
9,4800
10,1290
```

Students open Jupyter and write whatever they can in 5 minutes. No scaffolding provided. The instructor circulates silently, noting what students attempt.

After 5 minutes, the instructor calls time. Three students read their output aloud. The instructor does not correct errors immediately — instead, asks the class: "Did everyone get the same mean? Why or why not?" Common divergences at this stage:

- Some students compute mean on the wrong column (object dtype not caught)
- Some use `.mean()` on the DataFrame rather than the Series
- Some have NaN in their result because of a whitespace issue on import

The instructor notes divergences on the whiteboard and says: "We'll resolve all of these in the demo. Keep your notebook open."

This replaces the Mentimeter retrieval check used in theory weeks. The tool challenge activates prior knowledge (Week 2 manual calculations) while creating productive confusion (Bjork, 1994 — desirable difficulties) before the instructor resolves it.

---

### Part 2 — Live Coding / Instructor Demo (30 minutes)

The instructor codes from scratch in a projected Jupyter notebook. Students follow on their own machines. The notebook is NOT distributed in advance — students must type along or adapt in real time.

**Step 1: Recreate the Week 2 salary dataset as a pandas Series (5 minutes)**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The salary dataset from Week 2 — same data, now in code
salaries = pd.Series([1200, 1400, 1350, 1250, 1300, 1450, 1200, 1380, 4800, 1290])

# Measures of centre
print("Mean:  ", salaries.mean())
print("Median:", salaries.median())

# Stop here — ask the class: "Is the mean or median a better summary of this dataset? Why?"
# Expected answer: median, because of the CEO outlier (4800).
# Connect to Week 2 theory: right-skewed distribution, mean pulled toward tail.
```

**Step 2: Spread and shape (7 minutes)**

```python
# Standard deviation — pandas uses ddof=1 (sample) by default
print("Std (sample):", salaries.std())
print("Std (pop):   ", salaries.std(ddof=0))

# Quartiles — THIS IS THE KEY MOMENT
print("\nQuartiles (pandas default = linear interpolation):")
print(salaries.quantile([0.25, 0.5, 0.75]))

# Pause — show students: pandas uses 'linear' interpolation by default.
# Excel's QUARTILE function uses a different method.
# NumPy's np.percentile also differs depending on the `method` argument.
# This is why the number you compute by hand may not match pandas.

import numpy as np
print("\nNumPy (method='hazen'):", np.percentile(salaries, [25, 50, 75], method='hazen'))
print("NumPy (method='linear'):", np.percentile(salaries, [25, 50, 75], method='linear'))

# Skewness and kurtosis
print("\nSkewness:", salaries.skew())    # Fisher's definition
print("Kurtosis:", salaries.kurt())     # Excess kurtosis (normal = 0)
# Ask: what does positive skewness mean for this salary distribution?
```

**Step 3: The `.describe()` shortcut vs the full picture (2 minutes)**

```python
# Show the full picture first, then the shortcut
print(salaries.describe())

# .describe() gives: count, mean, std, min, 25%, 50%, 75%, max
# What it does NOT give: skewness, kurtosis, mode
# Students often over-rely on .describe() — make the omissions explicit

# Mode
print("Mode:", salaries.mode()[0])  # returns a Series — take first element
```

**Step 4: Loading a CSV and handling real data (6 minutes)**

```python
# Load from CSV — this is how real work begins
df = pd.read_csv('berlin_wages_2023.csv', encoding='utf-8')

# First look
print(df.head())        # first 5 rows
print(df.info())        # dtypes, non-null counts
print(df.describe())    # numeric columns only

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Two strategies for missing values:
# 1. Drop rows with any missing value
df_clean_drop = df.dropna()
print("Rows after dropna:", len(df_clean_drop))

# 2. Fill with median (better for skewed distributions)
df_clean_fill = df.copy()
df_clean_fill['salary'] = df_clean_fill['salary'].fillna(df_clean_fill['salary'].median())
print("Rows after fillna:", len(df_clean_fill))

# Key question: which strategy is more honest?
# dropna = smaller N, but no imputed values in your statistics
# fillna = preserves N, but artificially compresses variance
```

**Step 5: Histogram — bins matter (5 minutes)**

```python
# Histogram of salaries
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for i, bins in enumerate([3, 5, 10]):
    salaries.hist(bins=bins, ax=axes[i], color='steelblue', edgecolor='white')
    axes[i].set_title(f'bins={bins}')
    axes[i].set_xlabel('Weekly salary (€)')
    axes[i].set_ylabel('Frequency')

plt.suptitle('How bin count changes the story', fontsize=13, y=1.02)
plt.tight_layout()
plt.show()

# Ask students: at bins=3, is the outlier visible? At bins=10?
# Key insight: bin count is an analytical choice, not a neutral parameter.
# A poorly chosen bin count can hide or manufacture apparent patterns.
```

**Step 6: Box plot — where the outlier lives (5 minutes)**

```python
# Box plot reveals outlier structure immediately
plt.figure(figsize=(4, 6))
sns.boxplot(y=salaries, color='lightcoral')
plt.title('Salary distribution — box plot')
plt.ylabel('Weekly salary (€)')
plt.show()

# Ask: where does the CEO (4800) appear on this plot?
# Ask: what does the box represent? (IQR = Q3 - Q1)
# Ask: what is the whisker rule? (default: 1.5 * IQR beyond Q1/Q3)
# The point beyond the whisker IS the outlier.
```

---

### Part 3 — Guided Practice (25 minutes)

Students now apply the same workflow to their own Week 2 dataset. The instructor posts the following task list to Slack/Teams so students can work independently.

**Task list (students work through as many as they can in 25 minutes):**

```
Task 1. Load your dataset with pd.read_csv(). Run df.info() and df.describe().
        Write a markdown cell: what does df.info() tell you that df.describe() does not?

Task 2. Identify one numeric column of interest. Compute mean, median, std, skewness,
        and kurtosis. Compare to your Week 2 manual calculation.
        Write a markdown cell: do the numbers match? If not, why not?

Task 3. Handle missing values: decide whether to dropna() or fillna().
        Justify your choice in a markdown cell.

Task 4. Produce a histogram with at least two different bin counts.
        Which bin count gives the most honest picture of the distribution?

Task 5. Produce a box plot. Identify any outliers. Are they genuine extreme values
        or likely data errors?

Task 6 (stretch). Overlay a KDE (kernel density estimate) on your histogram:
        ax = df['salary'].plot(kind='hist', density=True)
        df['salary'].plot(kind='kde', ax=ax)  — same column, same axes. What does the KDE add?
```

**Common errors to watch for (instructor circulates):**

| Error | Cause | Fix |
|---|---|---|
| `UnicodeDecodeError` on `read_csv` | Non-UTF-8 file (common with Berlin open data) | Add `encoding='latin-1'` or `encoding='cp1252'` |
| Column dtype is `object` instead of `float` | Thousands separator (1.234,56 European format) or currency symbol | Reload with `pd.read_csv(..., decimal=',', thousands='.')` — a bare `str.replace(',', '.')` breaks on values with both separators |
| `KeyError` on column name | Trailing space in header | Use `df.columns.str.strip()` after loading |
| `.mean()` returns `NaN` | Column contains NaN values | Use `.mean(skipna=True)` (default) or `dropna()` first |
| Histogram shows only one bar | Integer column with low cardinality | Cast to float or use more bins |
| Box plot flipped horizontally | Using `x=` instead of `y=` in seaborn | Switch argument |

Students who finish Task 6 early are prompted to explore: "What happens to your statistics if you remove the outliers? Is that an honest thing to do?"

---

### Part 4 — Build-and-Critique / Peer Review (15 minutes)

Students pair up (instructor assigns pairs — mix datasets and nationalities). Each student has their histogram and box plot visible on screen.

**Structured critique protocol (5 minutes each direction, 5 minutes discussion):**

Each reviewer answers three questions about their partner's visualisation:

1. **What story is this chart telling?** (Can you read it without the student explaining it?)
2. **What design choice do you disagree with?** (Bin count, colour, axis labels, title — pick one and say why.)
3. **What does this chart NOT tell you?** (What question remains unanswered?)

The instructor listens to two or three pairs and surfaces the most generative disagreements for the whole group. Common productive conflicts:

- "You used 20 bins but the distribution looks like noise — is that real variation or data error?"
- "Your title says 'salaries' but the x-axis unit isn't labelled — I don't know if this is euros or thousands."
- "You kept the outlier in the histogram but removed it from the box plot — that's inconsistent."

Instructor closes with: "Every visualisation is an argument. The choices you made — what to include, what to exclude, how many bins, which scale — those are claims about the data. Be able to defend them."

---

### Part 5 — Debrief (10 minutes)

**Closing the tool decision framework:**

The instructor returns to the whiteboard note from Part 1 (the divergent means from the tool challenge). Now resolve each:

- Dtype issue → `df.info()` would have caught it
- NaN in result → `df.isnull().sum()` first
- Different quartile method → pandas documentation, `quantile(interpolation=...)` parameter

**Bridge question (last 3 minutes):**

"Next week we build dashboards in Tableau. Tableau does the visualisation for you — you just drag and drop. Given what you've discovered today about bin count and outlier handling, what risk does drag-and-drop introduce that code does not?"

Expected student answers: you don't see the defaults; Tableau may silently exclude nulls; you can't inspect or reproduce the exact computation; defaults may not match your analytical intent.

Instructor validates these and adds: "In Week 7 we will deliberately find where Tableau's defaults mislead — and that will be our critique framework."

---

## After Class (~20 minutes)

**Lab notebook completion:**

Finalise your Jupyter notebook from today. It should contain:

1. All six tasks from Part 3, with markdown cells explaining each decision.
2. At least two visualisations (histogram + box plot) with proper titles and axis labels.
3. A final markdown cell (minimum 100 words) answering: *"In at least one place, Python gave me a different number than my manual Week 2 calculation. I identified the cause as [X]. This matters for practice because [Y]."*

If your numbers matched exactly, explain why — don't just write "they matched." Think about which quartile method you used by hand.

**Submission:** Upload the `.ipynb` file to the shared class folder (link on LMS) by the day before Week 7. File naming convention: `W06_[your_initials]_[dataset_name].ipynb`.

No LMS reflection post required this block. The notebook IS the reflection.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Live tool challenge before instruction (not after) | Bjork (1994) desirable difficulties: productive failure before instruction deepens encoding. Students who struggle first retain the corrective instruction better than students who receive instruction first. |
| Returning to Week 2 dataset | Ausubel (1968) assimilation theory: new material (Python code) must connect to existing cognitive schema (manual calculations). The mismatch between manual and code outputs is the learning, not an obstacle to it. |
| Instructor codes from scratch, projected | Lovett & Greenhouse (2000) cognitive load: live coding with visible errors and corrections is more authentic than distributing a finished notebook. Students see the debugging process, not just the solution. |
| Three bin-count histograms side by side | Kalyuga et al. (2003) expertise reversal: for novices, comparing three variants simultaneously is more effective than sequential presentation, because the contrast itself carries the instruction. |
| Structured 3-question critique protocol | Black & Wiliam (1998) formative assessment: peer critique generates evidence of understanding without requiring instructor intervention. The three questions scaffold analysis at the evaluate level of Bloom's taxonomy. |
| No LMS reflection post in Block 2 | Vygotsky (1978) ZPD: the lab notebook functions as the zone of proximal development scaffold — students articulate reasoning in the medium where they are working, not in a separate reflective channel. |
| Bridge question pointing to Week 7 | Roediger & Karpicke (2006) testing effect: asking students to predict a future problem activates prospective encoding, making Week 7 content more retrievable. |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Part 1 — Live Tool Challenge | 10 min | Students code immediately; instructor circulates silently; divergences noted on whiteboard |
| Part 2 — Live Coding Demo | 30 min | 6 steps; students type along; questions embedded in demo, not after |
| Part 3 — Guided Practice | 25 min | 6 tasks of increasing difficulty; instructor circulates; common error table available |
| Part 4 — Build-and-Critique | 15 min | Structured 3-question peer review; instructor surfaces 2-3 productive disagreements |
| Part 5 — Debrief | 10 min | Resolve tool challenge divergences; bridge question to Week 7 Tableau |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

**1. Tool fluency vs. conceptual depth — the "it works" trap**

The greatest risk in a coding lab is that students focus on getting code to run rather than understanding what the code computes. A student who produces `salaries.mean()` correctly but cannot explain why it differs from their manual calculation has gained tool fluency without analytical depth. The mitigation — requiring markdown cells at every step and the discrepancy reflection in the post-work — is necessary but not sufficient. The instructor must actively ask "why" questions during Part 3 to prevent students from treating the notebook as a script to execute rather than an argument to construct.

**2. The expertise reversal problem in a mixed-ability cohort**

With 40+ nationalities and varied programming backgrounds, some students will arrive having never used Python; others will have used pandas professionally. For novices, the live demo may move too fast; for experts, it may be frustratingly slow. The six-task practice structure partially addresses this (Tasks 1–4 are accessible, Tasks 5–6 provide stretch), but the instructor must resist the temptation to slow the demo for novices at the expense of experts, or vice versa. Pairing during Part 4 should deliberately mix experience levels to leverage the expertise gradient (Kalyuga et al., 2003 expertise reversal: expert students benefit from teaching novices; novice students get scaffolded explanation).

**3. The quartile method problem — when being precise undermines confidence**

The revelation that pandas, Excel, and manual calculation use different quartile methods is analytically important but pedagogically risky. Students who discover their Week 2 calculation was "wrong by a different method" may lose confidence in their manual work, or worse, conclude that statistics is arbitrary. The instructor must frame this explicitly: there is no single correct quartile method; each method makes different interpolation assumptions; the differences are small for large datasets and larger for small ones; what matters is consistency and documentation. This framing should be explicit in the demo, not left for students to infer.

**4. Data loading friction absorbing lab time**

Real open-data CSVs from Berlin, Singapore, and Paris frequently have encoding issues, European decimal separators, multi-row headers, or columns that appear numeric but are stored as strings. These are genuinely important data engineering skills, but if half the students spend 15 of their 25 practice minutes on `UnicodeDecodeError`, the session loses its statistical focus. The mitigation is the instructor-provided fallback dataset (`berlin_wages_2023.csv`), pre-cleaned for the most common errors, so students who cannot load their own data can still complete all six tasks. Students using their own data who encounter loading errors should switch to the fallback for today and post their loading error to the class forum for debugging — a signal that the error is worth solving but not worth burning lab time on.

---

## References

Albright, S. C., & Winston, W. L. (2019). *Business analytics: Data analysis and decision making* (6th ed.). Cengage Learning.

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's educational objectives*. Longman.

Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart and Winston.

Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. https://doi.org/10.1080/0969595980050102

Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. https://doi.org/10.1207/S15326985EP3801_4

Lovett, M. C., & Greenhouse, J. B. (2000). Applying cognitive theory to statistics instruction. *The American Statistician, 54*(3), 196–206. https://doi.org/10.1080/00031305.2000.10474545

McKinney, W. (2022). *Python for data analysis: Data wrangling with pandas, NumPy, and Jupyter* (3rd ed.). O'Reilly Media.

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Exercises, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed.

- **Chapter 2 reference is close but should be pp. 30–54** (2-4 Descriptive Measures for Numerical Variables, incl. 2-4a summary measures and 2-4d charts). The cited pp. 33–58 straddles the section boundaries. Also add **2-6 Outliers and Missing Values (pp. 61–63)** — Tasks 3 and 5 (dropna/fillna decisions, outlier judgement) are exactly this section's content, and it's currently unassigned in the week that most needs it.
- **The Chapter 3 reference is wrong twice.** Scatterplots and correlation are at **3-4, pp. 95–108**, not pp. 75–82 (p. 79 is the chapter's first page). And this exact material was already the *required* reading in Week 3 — re-assigning it here as new is redundant; label it "revisit" instead. Separately, "we will return to correlation in Week 10" contradicts the course arc, where Week 10 is decision trees and correlation/regression returns in **Weeks 14–15**. Fix the pointer.
- The "skip the StatTools walkthrough sections; those are for the Excel lab" note refers to a lab that doesn't exist in the 22-week arc (Block 2 is Python/Tableau/SQL). Either delete the clause or say plainly: "the course replaces the book's StatTools/Excel toolchain with Python — the statistics transfer, the keystrokes don't." That sentence also pre-empts student confusion every time the book says "use StatTools" for the rest of the course.

## 2. Extended Exercise Bank (with answers) — predict-the-output and debugging drills

Lab weeks need a question bank too; these are printable warm-ups or homework, answers inline for the instructor version.

**E1 — ddof by hand.** For `s = pd.Series([2, 4, 6])`, what do `s.std()` and `s.std(ddof=0)` return?
**Answer:** sample SD = √(((−2)²+0²+2²)/2) = √4 = **2.0**; population SD = √(8/3) ≈ **1.633**. The Week 2 salary answer-key ambiguity (sample vs population SD) is this exact issue — worth saying aloud.

**E2 — Quantile interpolation.** For `s = pd.Series([1, 2, 3, 4])`, what is `s.quantile(0.25)` with default interpolation, and with `interpolation='lower'`?
**Answer:** default (linear): position = 0.25×(4−1) = 0.75 → 1 + 0.75×(2−1) = **1.75**; `'lower'` → **1**. There is no single "correct" Q1 — the Design Challenge 3 framing, made computable.

**E3 — Whisker rule applied.** Using the salary data (Q1 = 1250, Q3 = 1400), compute the box-plot fences and state which points are flagged.
**Answer:** IQR = 150; upper fence = 1400 + 1.5×150 = **1625**; lower fence = 1250 − 225 = **1025**. Only 4800 is outside → the CEO is the single flagged outlier. (Connects the seaborn default to the Week 2 T1(g) debate — flagged ≠ removed.)

**E4 — fillna and variance.** A column has 20% missing values. You `fillna(median)`. What happens, mechanically, to the column's standard deviation, and why does the demo call this "artificially compressing variance"?
**Answer:** SD falls: every imputed value sits exactly at the centre, adding zero-deviation observations while increasing n — deviations are diluted. Any subsequent inference understates uncertainty. (Dropna instead reduces n but leaves spread honest — the trade-off Task 3 asks students to argue.)

**E5 — Debugging drill.** `pd.read_csv('data.csv')` loads a salary column as `object`, and values look like `"1.234,56"`. Write the two-line fix and explain each step.
**Answer:** European formatting — `df['salary'] = df['salary'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)`: remove thousands separators first, then convert the decimal comma, then cast. (The common-errors table's one-liner `str.replace(',', '.')` is **incomplete for values with both separators** — see critique point 4.)

**E6 — describe() blind spots.** Name three statistics this week's session computed that `df.describe()` does not report, and one decision each affects.
**Answer:** skewness (mean-vs-median choice), kurtosis/tail weight (risk of extreme values; Week 5's Q9), mode (typical category/floor wage). Optionally missing-value count (describe reports non-null count only indirectly).

## 3. Alternative In-Class Activities (additional options)

**A. Driver–navigator pair programming (swap at 12 min, Part 3 alternative).** One types, one instructs; the navigator holds the task list and the driver may not act without instruction. Directly addresses the mixed-ability problem the Design Challenges name but don't structurally solve — the expert navigating a novice driver is forced to verbalise, the novice driver gets hands-on time.

**B. Broken-notebook relay (20 min, Part 3 alternative).** Distribute a notebook with six planted defects (encoding error, dtype trap, silent NaN mean, misleading bin count, mislabelled axis, fillna-before-describe). Pairs fix as many as they can; each fix requires a one-line markdown note of *what the bug would have done to a business conclusion*. Converts the common-errors table from reference material into the game itself.

**C. Chart-crime contest (15 min, Part 4 alternative).** Each student makes the *most misleading honest-data histogram* they can from their dataset (bin abuse, axis truncation, cherry-picked subset), posts it; class votes on the most deceptive; winners explain their technique, then everyone fixes their own. Teaching deception inoculates against it — and it lands the "every visualisation is an argument" point harder than critique of good-faith charts.

**D. Reproduce-the-figure (15 min, stretch replacement for Task 6).** Post a target PNG (histogram with specific bins, titles, annotated outlier). Task: reproduce it exactly from the raw data. Pixel-matching forces engagement with every parameter the demo touched, and gives fast finishers a concrete finish line instead of open-ended exploration.

**E. Colab lifeboat protocol (0 min in class — logistics).** Publish a Google Colab link with the fallback dataset pre-loaded. Anyone whose environment fails in the first 5 minutes of Part 1 switches to Colab immediately, no debugging in class; the local-install fix moves to the forum/tutorial. Caps the single biggest downside risk of the whole session.

## 4. Critique of the Lesson Plan

**What works (keep):** the tool challenge *before* instruction (correctly applied productive-failure design); returning to the Week 2 salary data so discrepancies are meaningful; the ddof and quantile-interpolation moments (the week's real intellectual content); the common-errors table; "the notebook IS the reflection."

**Problems, reasons, and fixes:**

1. **Wrong and contradictory Chapter 3 reference (see §1).** Pages point at the wrong section; the Week 10 pointer contradicts the arc. Fix both.
2. **Part 2's step timings don't add up.** Steps 1–6 total 5+7+5+8+5+5 = **35 minutes in a 30-minute slot** — with students typing along, live coding always runs over, never under. *Fix:* cut Step 3 (`describe()` shortcut) to 2 minutes or fold it into Step 2, and pre-load the CSV for Step 4 rather than typing the load live.
3. **No assessment criteria for the deliverable.** The notebook is the week's only output and is submitted, but students have no rubric — and the plan's own philosophy (Week 22's "criteria made explicit, not secret") argues against that. *Fix:* a four-line rubric: runs top-to-bottom without errors / every task has a markdown decision note / charts are titled and labelled / the discrepancy reflection names a specific cause. Pass–revise, not graded.
4. **The common-errors table's European-decimal fix is itself buggy.** `str.replace(',', '.')` breaks on values like `1.234,56` (yields `1.234.56` → `astype(float)` raises). Given that the table exists to save lab time, its one wrong entry costs more than it saves. *Fix:* two-step replacement as in E5, or `pd.read_csv(..., decimal=',', thousands='.')` — which is the cleaner teaching point anyway.
5. **Task 6's KDE snippet mixes two objects.** It overlays `salaries` (the demo Series) and `df['salary']` (the student's own data) on "the same axes" — as written it either errors or plots unrelated data together. *Fix:* one consistent object: `ax = df['salary'].plot(kind='hist', density=True); df['salary'].plot(kind='kde', ax=ax)`.
6. **Slack/Teams is invoked for the first time with no decision made.** Weeks 1–5 use Mentimeter + LMS; Part 1 and Part 3 here depend on a chat channel that has never been introduced. *Fix:* pick the stack once (e.g. "LMS forum + Mentimeter + class Slack") and name it in Week 1's logistics; mid-course tool sprawl is a real friction cost for a 22-week arc.
7. **The mixed-ability plan stops at diagnosis.** Design Challenge 2 describes the novice/expert tension well, but the only structural response is Tasks 5–6 as stretch. Activities A (driver–navigator) and D (reproduce-the-figure) above are concrete mechanisms; adopting either converts the challenge section from commentary into design.
8. **Dependency on Week 2's fix.** Task 2 assumes every student has manual Week 2 statistics for their dataset. If Week 2 ran as originally written (Jupyter-based Part 3 — see Week 2 supplement critique 2), some students' "manual" numbers are pandas numbers, and the discrepancy exercise collapses. If Week 2 moves to Excel/by-hand, this week works as designed — the two plans need to be revised together.
