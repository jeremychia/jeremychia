# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 9: SQL + Python Pipeline — From Query to Visualisation
**Format:** 90-minute lab seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Connect to a SQL database from a Jupyter notebook using `psycopg2` or `sqlite3` and load query results into a pandas DataFrame with `pd.read_sql()`
- Build a complete end-to-end analysis pipeline: raw database → SQL query → pandas → matplotlib/seaborn chart
- Identify where in the pipeline data quality issues surface — and at which stage they are best handled
- Articulate the design rationale for using SQL at one stage and Python at another (not just one or the other)

This session closes Block 2 (Weeks 6–9). It is the practical integration of everything in the block: descriptive statistics in Python (Week 6), chart design in Tableau (Week 7), SQL querying (Week 8), and now the pipeline that connects them. Students who complete this session can build a minimal viable analytics workflow from scratch.

---

## Before Class (Student Pre-Work)

**Reading:** no textbook reading. Pre-work is practical setup and one code example.

**Environment check (10 minutes):**
Confirm that you can:
1. Open a Jupyter notebook
2. Import `pandas`, `matplotlib.pyplot`, `seaborn`
3. Connect to either PostgreSQL via `psycopg2` or SQLite via `sqlite3`

Test this before class with the following cell:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3  # or: import psycopg2

conn = sqlite3.connect('test.db')  # or PostgreSQL connection
print("Connection successful")
```

If the connection fails, bring the error message to class. Do not spend more than 20 minutes debugging — that's what the first part of the session is for.

**Worked example (read carefully — you will reproduce this in class):**

> ```python
> import pandas as pd
> import sqlite3
> import matplotlib.pyplot as plt
>
> # Step 1: Connect to the database
> conn = sqlite3.connect('sales.db')
>
> # Step 2: Write SQL query and load directly into pandas
> query = """
>     SELECT
>         category,
>         SUM(quantity * unit_price) AS total_revenue,
>         COUNT(*) AS order_count
>     FROM orders
>     WHERE order_date >= '2025-10-01'
>     GROUP BY category
>     ORDER BY total_revenue DESC
> """
> df = pd.read_sql(query, conn)
>
> # Step 3: Visualise
> plt.figure(figsize=(10, 5))
> plt.bar(df['category'], df['total_revenue'])
> plt.xlabel('Category')
> plt.ylabel('Total Revenue (€)')
> plt.title('Revenue by Category — Q4 2025')
> plt.tight_layout()
> plt.show()
>
> # Step 4: Close connection
> conn.close()
> ```
>
> **Key moments in this pipeline:**
> - Line 2: the SQL lives inside the Python string — it runs in the database, not in memory
> - Line 3: `pd.read_sql()` executes the query and returns a DataFrame — you don't need to write a loop to parse rows
> - The aggregation (SUM, GROUP BY) happens in SQL before the data reaches Python — this is faster than loading all rows and aggregating in pandas
> - The visualisation is Python's job — SQL can't draw charts

**Pre-work question (written, submit before class):**

Write down one business question you'd want to answer from the sales dataset. Express it as:
1. A plain English question
2. A SQL query that would answer it
3. What chart type you'd use to communicate the result and why

---

## In-Class Session (90 minutes)

### Part 1 — Environment Check and Opening Challenge (10 minutes)

No quiz this week. Instead:

**3-minute environment check:** every student confirms their connection works. Those who can't connect are paired with a neighbour — they'll work together and debug in the first buffer window.

**Opening question (no technology needed):**

> *"You're an analyst. A manager hands you a database with 10 million rows of transaction data. She wants a chart showing monthly revenue trends for the last two years. What is the worst way to approach this — and what's the right way?"*

Worst way: load all 10 million rows into pandas, then filter and aggregate in Python. Right way: filter and aggregate in SQL first, then load the ~24-row result into pandas and chart it.

This is the core architectural principle of the session. Every design decision in the pipeline follows from it: push the heavy lifting to SQL; use Python only when SQL can't do it.

---

### Part 2 — Live Coding: End-to-End Pipeline (20 minutes + 10 minutes buffer)

Instructor codes live from an empty notebook. Students follow along. Dataset is the same `orders` table from Week 8.

**Stage 1 — Connect:**
```python
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('orders.db')
```

**Stage 2 — Query:**
```python
query = """
    SELECT
        strftime('%Y-%m', order_date) AS month,
        SUM(quantity * unit_price)    AS monthly_revenue
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY month
    ORDER BY month
"""
df = pd.read_sql(query, conn)
```

**Teaching moment:** `strftime('%Y-%m', ...)` is SQLite-specific date formatting. PostgreSQL uses `TO_CHAR(order_date, 'YYYY-MM')`. The principle is the same; the syntax differs. If you switch databases, this line breaks — document it.

**Stage 3 — Check:**
```python
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
```

This is the checkpoint. Before charting, always: look at the first rows, check data types (is `monthly_revenue` float or string?), check for nulls. Students who skip this step build charts with silent errors.

**Stage 4 — Visualise:**
```python
plt.figure(figsize=(12, 5))
plt.plot(df['month'], df['monthly_revenue'], marker='o', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Revenue (€)')
plt.title('Monthly Revenue Trend 2024–2025')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Stage 5 — Close:**
```python
conn.close()
```

Always close. In a notebook that runs multiple times, forgetting to close creates stale connections.

Buffer: use it to handle connection failures from Part 1, or to extend Stage 3 (the check step) — which is where most real analysis errors live.

---

### Part 3 — Independent Pipeline (25 minutes)

Each student builds their own pipeline answering the pre-class question they submitted. They must:
1. Write the SQL query (may reuse or modify their pre-class answer)
2. Load into pandas via `pd.read_sql()`
3. Run the checkpoint (head, dtypes, nulls)
4. Produce a chart with correct axis labels and title
5. Write one sentence in a markdown cell: "This chart shows ___. It doesn't show ___."

The last step — articulating what the chart hides — is the connection back to Week 2. Every visualisation is a compression that omits as much as it shows. Students who can name what their chart omits have gone beyond chart production to chart literacy.

**Instructor circulates.** Common failures to anticipate:
- `pd.read_sql()` returning a column as object (string) when it should be float — requires `.astype(float)` before charting
- Missing `conn.close()` causing the second run to fail silently
- Group BY but not ORDER BY — chart bars in arbitrary order
- SQL date formatting differing between SQLite and PostgreSQL

If more than three students are stuck on the same issue, pause the class and fix it together — this is more efficient than fixing it individually twelve times.

---

### Part 4 — Pipeline Critique (20 minutes)

Two students project their notebooks. The class answers three questions for each:

1. **Does the chart answer the business question?** (Is what's visualised actually what was asked?)
2. **Where could this pipeline silently fail?** (What change to the data would break it without an error?)
3. **What would you change — SQL side? Python side?**

The "silently fail" question is the hardest and most important. Examples of silent failure:
- A new category added to the data appears in the chart without a label (string column not in ORDER BY)
- A NULL in `unit_price` causes `SUM(quantity * unit_price)` to silently exclude some rows (NULL arithmetic propagates)
- `strftime` format changes from `'%Y-%m'` to `'%m-%Y'` in a report template, breaking the sort order

These are not hypothetical — they are real analyst errors. Students who can name them before they happen are more valuable than students who can only fix them after.

---

### Part 5 — Debrief (10 minutes)

**Close the loop:**

*"We've now covered Python (Week 6), Tableau (Week 7), SQL (Week 8), and the pipeline (this week). What is the decision you should make before starting any analysis — before you write a single line of code?"*

The answer: "What question am I trying to answer?" Every tool choice follows from the question. If the question is "what is the trend?" — a line chart in Python on aggregated SQL data. If the question is "explore this for me" — pandas profiling or Tableau. If the question is "how many X are there?" — a single SQL SELECT COUNT(*).

**Bridge to Block 3 (Week 10, decision trees):**

> *"In Block 2 we built tools to describe and query data. In Block 3 we're going to use data to make inferences and decisions. Those are different things — and the line between them is where most analytical mistakes happen. Next week: a manager has two projects. She asks you which one to recommend. How do you decide?"*

---

## After Class (Student Post-Work)

No separate LMS post. The notebook from Part 3 is the artefact. Students who want to extend it: add a second chart (a different question from the same database), and a markdown cell comparing what each chart shows and what it hides.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Pipeline introduced as architecture principle, not just syntax | Rosenshine (2012): present new material in small steps — the architectural principle (SQL for aggregation, Python for visualisation) comes before the syntax; students who understand why they're building the pipeline write better code than students who copy it |
| Live coding with deliberate checkpoint stage (head, dtypes, nulls) | Models expert practice — professional analysts always check before charting; demonstrating this explicitly establishes it as a norm, not an optional step |
| Independent practice uses student's own pre-work question | Ausubel (1968): self-relevance anchors learning; a student who wrote their own question has a personal stake in whether the pipeline answers it correctly |
| "What does this chart hide?" as mandatory final step | Week 2 thread: descriptive statistics compress; visualisations compress; compression hides; the analyst's job is to know what was hidden. Returning to this framing in Week 9 (with a pipeline that the student built) is more durable than re-stating it abstractly |
| Critique format in Part 4 with "silent failure" question | Chi et al. (1994): self-explanation and critique strengthen understanding; "silently fail" is the hardest failure mode to teach and the most important for professional practice |
| No LMS post; notebook is the artefact | Tool lab weeks: output is the reflection; a post would be redundant |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Environment check + opening question | 10 min | Fix connection failures; establish SQL-Python architecture principle |
| Live coding pipeline | 20 min | 5 stages: connect, query, check, chart, close |
| Buffer (explicit) | 10 min | Connection debugging; extend checkpoint stage if needed |
| Independent pipeline | 25 min | Student's own pre-work question → notebook with 5 required elements |
| Pipeline critique | 20 min | Two projected notebooks; three questions; "silent failure" emphasis |
| Debrief | 10 min | Tool decision framework; bridge to Block 3 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. Connection setup is the highest-risk technical point.

If students can't connect to the database, they can't do anything else. The environment check at the start is not a formality — it is the session's most critical operational step.

**Resolution:** the pre-work explicitly asks students to test the connection before arriving. Students who couldn't connect are paired with a neighbour in the first 3 minutes. The 10-minute buffer in Part 2 is explicitly reserved for this if needed. The instructor should have a pre-loaded dataset available as a fallback (e.g., a CSV loaded via `pd.read_csv()` instead of a SQL database) — not ideal, but it allows the rest of the session to proceed.

---

### 2. The level of SQL fluency varies widely after only one SQL session (Week 8).

Students who struggled with GROUP BY in Week 8 will struggle to write the SQL query for their pre-work question in Week 9. This creates a bottleneck at Part 3 — some students spend 20 of 25 minutes writing SQL and never get to the chart.

**Resolution:** the pre-work asks students to write the SQL query before class. Students who bring a working query to Part 3 spend 25 minutes on the pipeline; students who bring a broken query spend the first 5–10 minutes debugging with instructor support. The balance is imperfect but the pre-work preparation reduces the worst cases.

---

### 3. Closing Block 2 creates pressure to demonstrate everything the block covered.

The temptation is to make this session a showcase of SQL, Python, and Tableau together. That's too much: trying to bring in all three tools in 90 minutes produces shallow contact with each.

**Resolution:** the session is SQL + Python only. Tableau is the comparison point in the debrief ("Tableau would be better for exploring; SQL+Python is better for reproducible, auditable pipelines") — it doesn't need to be open on screen. Depth in two tools is more valuable than breadth across three.

---

### 4. The "silent failure" concept in Part 4 is genuinely hard to make vivid without a live example.

Naming silent failure modes in the abstract doesn't land the same way as seeing one happen. If neither projected notebook has a visible silent failure, the question becomes hypothetical.

**Resolution:** the instructor introduces a deliberate silent failure into one of the projected notebooks before the session: a NULL in a price column that causes a category to be excluded from the sum, producing a plausible-looking chart that's wrong. If no student's notebook has a natural silent failure, this prepared example substitutes. The teaching point is the same.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Chi, M.T.H., de Leeuw, N., Chiu, M.H. & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Rosenshine, B. (2012). Principles of instruction. *American Educator*, Spring 2012. ERIC EJ971753.
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
