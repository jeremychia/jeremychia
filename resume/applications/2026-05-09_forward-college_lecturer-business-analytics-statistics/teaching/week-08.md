# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 8: SQL — Querying, Filtering, and Aggregating
**Format:** 90-minute lab seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Write SQL queries using SELECT, FROM, WHERE, GROUP BY, HAVING, and ORDER BY to answer business questions from a relational table
- Handle NULL values correctly in aggregation and filtering
- Use window functions (ROW_NUMBER, RANK, LAG) to compute row-level analytics not possible with GROUP BY alone
- Identify the difference between a question that SQL cannot answer and one it can — and explain why

These map to the Block 2 practical objective: *"query structured data in SQL and know when SQL is the right tool."* SQL is the dominant data retrieval language in business analytics and appears in the coursework and employment contexts students will enter.

These objectives are at the **application and analysis** levels of Bloom's Taxonomy — constructing queries to answer novel questions, and identifying when the tool's limitations require a different approach.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, §17-2a Introduction to Relational Databases (p. 900, ~3 pages) — the conceptual grounding for tables, keys, and relations. (The book's own SQL coverage lives in the bonus online Chapter 18, §18-4d, for the curious.) The rest of the pre-work is practical.

Students must complete the following before class:

**SQLZoo tutorial (mandatory — ~45 minutes):**
Complete [sqlzoo.net](https://sqlzoo.net/) sections 0–4:
- Section 0: SELECT basics
- Section 1: SELECT from World
- Section 2: SELECT from Nobel
- Section 3: SELECT within SELECT
- Section 4: SUM and COUNT (GROUP BY)

Bring a note of any question where you were genuinely stuck — not just the ones you got wrong, but the ones where the correct answer surprised you.

**Note on environment:** the in-class exercises use PostgreSQL via pgAdmin, or SQLite via DB Browser — confirm with the course instructor which is in use. If you can install one of these before class, the transition to independent practice (Part 3) will be faster.

**Worked example (read before class):**

> **Dataset:** a table called `orders` with columns: `order_id`, `customer_id`, `product_name`, `category`, `quantity`, `unit_price`, `order_date`, `region`.
>
> **Business question:** "Which product category generated the most revenue last quarter, and how many orders contributed to that?"
>
> **SQL:**
> ```sql
> SELECT
>     category,
>     SUM(quantity * unit_price) AS total_revenue,
>     COUNT(*) AS order_count
> FROM orders
> WHERE order_date >= '2025-10-01' AND order_date < '2026-01-01'
> GROUP BY category
> ORDER BY total_revenue DESC;
> ```
>
> **What this does:**
> - WHERE filters to last quarter before aggregation
> - GROUP BY collapses rows to one per category
> - SUM computes revenue per category
> - COUNT(*) counts orders (not customers) per category
> - ORDER BY ranks from highest revenue
>
> **What this does NOT do:**
> - It does not tell you how many *customers* bought in each category (that requires COUNT(DISTINCT customer_id))
> - It does not tell you the average order size (that requires SUM / COUNT, not COUNT(*))
> - It does not tell you whether revenue grew or declined vs. the prior quarter (that requires a second query or a window function)
>
> The gap between "what the query returns" and "what the business wants to know" is the core skill this session develops.

**Tutorial problems (bring written answers or SQL attempts to class):**

Using the same `orders` table:

*T1:*
> Write a query that returns the total revenue per region. Order by revenue descending. (Use GROUP BY.)

*T2:*
> A manager asks: "Which categories had more than €50,000 in revenue last quarter?" Write a query. (Use HAVING, not WHERE — explain why.)

*T3:*
> The `quantity` column has some NULL values. Write a query that counts: (a) total rows, (b) rows where quantity is NOT NULL, (c) rows where quantity IS NULL. Then explain: if you run SUM(quantity), what happens to the NULLs?

*T4 (stretch):*
> Write a query that returns, for each customer, their most recent order date. Then filter to customers whose most recent order was more than 90 days ago. (This requires a subquery or CTE.)

T3 is the most important pre-work question: SQL ignores NULLs in aggregate functions (SUM, AVG, COUNT — except COUNT(*)) in ways that silently produce wrong answers. Students who don't understand this will write queries that appear to work and return incorrect results.

---

## In-Class Session (90 minutes)

### Part 1 — Query Challenge (10 minutes)

No Mentimeter this week. Instead: a live query challenge to open.

The instructor projects a result set (a table of output, no query visible) and asks: *"What query produced this? Write it in 3 minutes."*

The result set shows: `product_name | avg_revenue | rank` — clearly a window function output (RANK() OVER). Students who completed the SQLZoo pre-work through Section 4 will not have seen window functions. That's deliberate: this is the opening challenge, not a retrieval check. The goal is to make students articulate what they *don't know yet*.

After 3 minutes: "How many of you have a complete query? How many have most of it? How many don't know where to start?" A quick hands-up is sufficient — no Mentimeter, because there's no multiple-choice format for a query.

The instructor then reveals the query and the window function syntax. This is the only mini-lecture moment in the session — and it's provoked by the challenge, not pre-empted.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

T2 (HAVING vs. WHERE) is the key discussion point. Ask two students to explain in their own words why HAVING is needed: "WHERE filters rows before aggregation; HAVING filters groups after aggregation. If you write WHERE SUM(revenue) > 50000, SQL throws an error — you can't use an aggregate function in a WHERE clause."

T3 (NULLs in aggregation) is the other critical one. Demonstrate live: `SELECT COUNT(*), COUNT(quantity), SUM(quantity) FROM orders;` — show what happens with each function when some rows have NULL quantity. The discrepancy between COUNT(*) and COUNT(quantity) is the moment of clarity.

T4 is held for Part 3 independent practice.

Buffer: use it to work through one student's failed query — diagnose the error live. Seeing a query fail and being debugged is more useful than seeing only successful queries.

---

### Part 3 — Query Challenge Pairs (25 minutes)

Pairs receive a messy raw dataset (provided as a CSV or SQL dump). The dataset has: NULLs in key columns, duplicate rows, inconsistent text casing in category names, and at least one date column in an ambiguous format.

**Business scenario:** the dataset is a six-month transaction log from a fictional e-commerce company. The instructor plays the role of the manager who wants answers but doesn't know what's in the data.

**Pairs must answer three questions using SQL — no pandas, no Excel:**

1. What is the average order value by product category? (Handle NULLs in the price column.)
2. Which customers placed more than 3 orders in the period? (Identify duplicates first.)
3. What was the month-over-month change in total revenue for each month? (Window function: LAG().)

The third question is a stretch: students need LAG() OVER (ORDER BY month). If they can't complete it, they should write a comment explaining what the query would need to do — partial credit for conceptual clarity.

**The data quality challenge is intentional.** A clean dataset teaches SQL syntax. A messy dataset teaches what SQL is actually for: making implicit data problems explicit. Students who write `WHERE category = 'Electronics'` without checking case will miss rows. Students who don't handle NULLs will get wrong averages. These errors mirror real-world data analyst work.

---

### Part 4 — Live Debug and Critique (20 minutes)

Two pairs share their queries on screen — projected live. The rest of the class acts as code reviewers:
- Does this query answer the question that was asked?
- What would happen to this query if a new category was added to the data?
- Is there a row that this query would handle incorrectly?

The "critique" role mirrors professional code review. Students who can read and critique another person's SQL have a skill beyond their own query-writing ability.

**One question the instructor asks for every query presented:** *"What would make this query give the wrong answer without throwing an error?"* The silent failure mode — a query that runs, returns results, and is wrong — is the most dangerous failure mode in analytical work.

---

### Part 5 — Debrief (10 minutes)

**Close the loop:**

*"What is SQL actually good at — and what isn't it good at?"*

The answer the class should arrive at:
- SQL is excellent at: filtering, aggregating, joining, window calculations on structured relational data
- SQL is poor at: visualisation, statistical modelling, anything requiring iteration, machine learning, string manipulation at scale

**Tool decision framework (first stated in Week 6; Week 9 builds the full pipeline):**

> **Use SQL when:** the data is in a database, you need a precise filtered aggregate, or you're preparing data for Python.
> **Use Python when:** you're exploring, visualising, or running statistical models.
> **In practice:** SQL to extract and prepare, Python to analyse and communicate. They are a pipeline, not alternatives.

**Data provenance — 3 minutes within the debrief:**

The messy dataset in Part 3 had NULLs that arose from real system behaviour (e.g., the payment column was NULL for cancelled orders — not missing at random, but missing for a specific reason). Before the session ends, ask:

> *"Where did this dataset come from? Who collected it, when, and how? Does it matter?"*

It does matter — and Weeks 19–22 will surface this acutely when students choose their own datasets. A dataset from a government open data portal is a snapshot at a point in time, with a specific collection methodology, for a specific administrative purpose. A dataset from a convenience sample of 50 respondents licenses different claims than one from a random sample of 5,000.

Three questions that should become habitual when encountering any dataset:
1. **How was this collected?** (Survey, transaction log, sensor, administrative record, web scrape)
2. **Who is in it — and who isn't?** (A dataset of customers who complained is not a dataset of all customers)
3. **What was it collected for?** (Data collected for billing purposes may behave differently when used for marketing analysis)

This is not a lecture — it is a 3-minute planting. Students who encounter this question in Week 8 will recognise it again in Weeks 19–22 when it becomes a marking criterion. The SQL context makes it concrete: the NULLs in today's dataset were not random — they told you something about the system that generated them. That is data provenance in action.

**Bridge forward to Week 9:**

> *"Next week we connect these two tools. You'll write a SQL query, pull the results into a pandas DataFrame, then produce a chart — all in one notebook. The question is: where in that pipeline does something break?"*

---

## After Class (Student Post-Work)

No LMS post this week — the lab output (query file with answers to the three business questions) is the reflection artefact. Students save their `.sql` file or Jupyter notebook and submit via the course portal.

**One optional follow-up for students who completed T4:** rewrite the subquery version as a CTE (Common Table Expression). Compare readability. Is a CTE always more readable, or does it depend on complexity?

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Opening with a challenge (reverse-engineer the query) rather than a quiz | For tool sessions, a construction challenge is more informative than multiple-choice retrieval — it reveals what students can and can't build, not just what they recognise |
| Messy dataset for Part 3 (NULLs, duplicates, inconsistent casing) | Bjork (1994): desirable difficulties — real data has these properties; practising on clean data produces fragile skills that break on first real-world contact |
| Critique format in Part 4 | Chi et al. (1994): self-explanation and peer critique both strengthen understanding; reviewing another person's query requires more than copying it |
| Window functions introduced via challenge, not pre-taught | Sweller (1994): worked example effect — introducing new syntax in response to a problem the student has already felt produces better retention than introducing it cold |
| SQL tool decision framework repeated from Week 6 | Spacing effect (Cepeda et al., 2006): retrieving the SQL vs. Python distinction in a different context (Week 8) than where it was introduced (Week 6) strengthens long-term retention |
| No LMS post; lab output is the artefact | In tool lab weeks, the output is the reflection; requiring an additional post would create work without learning benefit |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Query challenge (opening) | 10 min | 3 min individual + reveal + window function introduction |
| Tutorial review | 15 min | T2 HAVING vs WHERE; T3 NULLs — live demonstration |
| Buffer (explicit) | 10 min | Absorbs live query debugging or extended NULL demonstration |
| Pair query challenge | 25 min | Three business questions on messy dataset |
| Live debug and critique | 20 min | Two pairs on screen; class as code reviewers |
| Debrief | 10 min | SQL strengths/limits; bridge to Week 9 pipeline |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

### 1. SQL skill levels will vary dramatically in a 40+ nationality cohort.

Some students will have written production SQL in jobs or internships. Others will have completed only the SQLZoo pre-work. In a 25-minute pair exercise, this gap can mean one partner does all the writing.

**Resolution:** pair assignment — put the most and least experienced students together, not the two most experienced. The stronger partner must explain what they're writing; the weaker partner must ask questions they genuinely have. Neither role allows passive observation. If pairs are self-selected, the skill clustering will be obvious and the learning asymmetric.

---

### 2. The messy dataset requires setup work the instructor must do in advance.

Preparing a dataset with authentic messiness (not artificial junk) takes time. A real e-commerce transaction log (even a synthetic one) should have NULLs that arise from system behaviour (e.g., a payment column is NULL when the order was cancelled) rather than random NULLs.

**Resolution:** prepare the dataset before the session and test every query against it. The three business questions should each have a clean answer when the data is handled correctly, and a plausibly wrong answer when it isn't. This preparation is non-negotiable — a poorly constructed dataset makes the session arbitrary rather than educational.

---

### 3. Window functions are introduced mid-session, not pre-taught.

Some students may feel ambushed by seeing LAG() in the Part 3 challenge after a short 2-minute introduction in Part 1.

**Resolution:** the T4 pre-work question (subquery for most recent order date) is a gentler version of the same problem. Students who did T4 have encountered the concept of "looking back across rows" even if they didn't use LAG(). The stretch question in Part 3 explicitly says "partial credit for conceptual clarity" — students who can describe what the query needs to do, even without correct syntax, get credit.

---

### 4. PostgreSQL vs. SQLite syntax differences may cause confusion.

`PERCENTILE_CONT` is available in PostgreSQL but not SQLite. Window functions work in both but with slightly different syntax in edge cases.

**Resolution:** the instructor specifies which environment is in use at the start of the session. If SQLite is used, any percentile examples in the course SQL materials are adjusted accordingly (SQLite has no native `PERCENTILE_CONT`). This is an administrative check, not a pedagogical challenge — but it must be resolved before Part 3 begins.

---

## References
- Anderson, L.W. & Krathwohl, D.R. (Eds.) (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing.* MIT Press.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Chi, M.T.H., de Leeuw, N., Chiu, M.H. & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Answer Key + Extended Exercises, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed.

"No textbook reading" is stated, but the book does have relevant material:

- **§17-2a Introduction to Relational Databases (p. 900)** — a compact conceptual grounding for tables/keys/relations; ~3 pages; assign it. It also makes Week 7's OLAP reading (17-2b) retroactively coherent as a pair.
- **Chapter 18 (bonus online), §18-4d "SQL Statements and M" (p. 18-26)** — A&W's actual SQL coverage. Optional pointer for students who want the book's angle; also useful to tell students the textbook's toolchain queries databases *from Excel*, which is what Week 9's Python-from-SQL pipeline replaces.

## 2. Answer Key (currently missing entirely) + Extended Exercises

Unlike Weeks 1–5, this week ships no answers for T1–T4 or the three Part 3 business questions — while Design Challenge 2 says tested reference queries are "non-negotiable." Reference solutions (PostgreSQL syntax):

**T1:**
```sql
SELECT region, SUM(quantity * unit_price) AS total_revenue
FROM orders
GROUP BY region
ORDER BY total_revenue DESC;
```

**T2:** *(HAVING, because the filter applies to an aggregate that exists only after grouping; `WHERE SUM(...)` is an error since WHERE runs row-by-row before GROUP BY):*
```sql
SELECT category, SUM(quantity * unit_price) AS total_revenue
FROM orders
WHERE order_date >= '2025-10-01' AND order_date < '2026-01-01'
GROUP BY category
HAVING SUM(quantity * unit_price) > 50000;
```
Note both clauses appear: WHERE filters *rows* (the quarter), HAVING filters *groups* (the €50k threshold) — the strongest version of the teaching point is that this query needs both.

**T3:**
```sql
SELECT COUNT(*)                          AS total_rows,
       COUNT(quantity)                   AS non_null_quantity,
       COUNT(*) - COUNT(quantity)        AS null_quantity
FROM orders;
```
`SUM(quantity)` silently skips NULLs: it returns the sum of non-null values, with no error and no warning. Consequence: `SUM(quantity)/COUNT(*)` and `AVG(quantity)` give *different* averages — the analyst must decide which denominator answers the business question.

**T4:**
```sql
WITH last_orders AS (
    SELECT customer_id, MAX(order_date) AS most_recent
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, most_recent
FROM last_orders
WHERE most_recent < CURRENT_DATE - INTERVAL '90 days';
```

**Part 3 reference solutions** (to be validated against the actual prepared dataset, per Design Challenge 2):

*Q1 — average order value by category, NULL-aware:*
```sql
SELECT category,
       AVG(quantity * unit_price)              AS avg_order_value,   -- skips NULL rows
       COUNT(*)                                AS all_orders,
       COUNT(quantity * unit_price)            AS priced_orders      -- show what AVG used
FROM orders
GROUP BY category;
```
The teaching answer includes both counts so the pair must *report* how many rows the average ignored.

*Q2 — customers with > 3 orders, after de-duplication:*
```sql
WITH dedup AS (SELECT DISTINCT * FROM orders)
SELECT customer_id, COUNT(*) AS order_count
FROM dedup
GROUP BY customer_id
HAVING COUNT(*) > 3;
```
(If duplicates share an `order_id`, `COUNT(DISTINCT order_id)` without the CTE is the cleaner solution — accept both, discuss which duplicate definition matches the business question.)

*Q3 — month-over-month revenue change:*
```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(quantity * unit_price)      AS revenue
    FROM orders
    GROUP BY 1
)
SELECT month, revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) AS mom_change
FROM monthly
ORDER BY month;
```

**Extended exercises (with answers):**

**E1 — The missing JOIN (see critique point 2).** Given a second table `customers(customer_id, country, signup_date)`: report total revenue per customer country, including countries with zero orders.
**Answer:**
```sql
SELECT c.country, COALESCE(SUM(o.quantity * o.unit_price), 0) AS revenue
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY revenue DESC;
```
Follow-up (the silent-failure version): what changes with `INNER JOIN`? — zero-order countries vanish without error; the classic "query runs, answer wrong" case for Part 4's standing question.

**E2 — COUNT(DISTINCT).** "How many *customers* bought in each category?" — the worked example says its query can't answer this; write the one that can.
**Answer:** `SELECT category, COUNT(DISTINCT customer_id) AS buyers FROM orders GROUP BY category;`

**E3 — CASE WHEN bucketing.** Label each order 'small' (< €50), 'medium' (€50–200), 'large' (> €200) and count orders per bucket.
**Answer:**
```sql
SELECT CASE WHEN quantity * unit_price < 50  THEN 'small'
            WHEN quantity * unit_price <= 200 THEN 'medium'
            ELSE 'large' END AS bucket,
       COUNT(*) AS orders
FROM orders
WHERE quantity IS NOT NULL AND unit_price IS NOT NULL
GROUP BY 1;
```
Ask what happens to NULL-priced rows without the WHERE: they fall into `ELSE 'large'` — a silent misclassification, because `NULL < 50` is *unknown*, not false. (This is the sharpest NULL lesson in the set.)

**E4 — Duplicate forensics.** Find exact duplicate rows and count them.
**Answer:** `SELECT order_id, COUNT(*) FROM orders GROUP BY order_id HAVING COUNT(*) > 1;` (or GROUP BY all columns for full-row duplicates). Then discuss: delete, or keep and understand *why* the pipeline duplicated them — provenance again.

**E5 — Predict-the-output.** `WHERE category <> 'electronics'` runs against rows where `category` is NULL. Are those rows returned?
**Answer:** **No.** NULL comparisons yield UNKNOWN, and WHERE keeps only TRUE. Rows with NULL category are excluded by *both* `= 'electronics'` and `<> 'electronics'` — the single most common silent SQL error; needs `OR category IS NULL` to include them.

## 3. Alternative In-Class Activities (additional options)

**A. SQL Murder Mystery (25 min, Part 3 alternative).** The Knight Lab "SQL Murder Mystery" (mystery.knightlab.com) — students solve a whodunit purely via SELECT/JOIN/WHERE over a small schema. High engagement, self-pacing, and it forces JOINs naturally (fixing this week's JOIN gap through play). Works in-browser: zero environment risk.

**B. Break my query (15 min, Part 4 alternative).** Each pair submits their Q1 query; the *next* pair must craft a single data row that makes it return a wrong answer without erroring (NULL price, duplicated order, `'ELECTRONICS'` casing). Rows are added live; queries visibly break or survive. This operationalises the instructor's standing question — students hunt silent failures instead of being warned about them.

**C. Human GROUP BY (8 min, energiser before Part 3).** Each student gets an index card (an order row: category, region, amount, some NULLs). Instructor calls "GROUP BY region — SUM amount": students physically cluster and one reporter per group announces the aggregate; NULL-card holders must decide where to stand (nowhere? their own group?) — which is precisely how SQL treats NULL grouping (its own group) vs NULL aggregation (skipped). Embodied and memorable.

**D. Query golf leaderboard (10 min, fast-finisher channel).** Post one target result set; shortest *correct* query (by character count) wins. Teaches that DISTINCT vs GROUP BY, and expressive built-ins, are interchangeable dialect — and keeps the professional-SQL students occupied without dominating pairs.

**E. Provenance autopsy of the NULLs (10 min, structured version of the debrief planting).** After Part 3, reveal the *system story* of the dataset's defects: payment NULL = cancelled order; duplicates = a double-fired export job; casing chaos = two source systems merged. Pairs re-answer Q1 knowing this. The point lands hard: their "correct" NULL-handling choice may have silently included cancelled orders in revenue. Data provenance stops being a speech and becomes a revision they must make.

## 4. Critique of the Lesson Plan

**What works (keep):** the reverse-engineer-the-query opener; the deliberately messy dataset with system-motivated defects; the "what would make this query wrong without erroring?" standing question (arguably the best single question in the whole 22-week set); the provenance planting for Weeks 19–22.

**Problems, reasons, and fixes:**

1. **No answers exist for anything in this week (fixed in §2 above).** Every prior week ships an answer key; this one has none for T1–T4 or Part 3 — yet Design Challenge 2 demands the instructor "test every query against" the dataset. *Fix:* adopt §2 and validate against the actual prepared data.
2. **JOINs are absent from the course's only SQL week.** The objectives and debrief both name joining as a core SQL capability; SQLZoo sections 0–4 stop *before* the JOIN section (6); no tutorial, task, or demo touches a second table. A single-table SQL week teaches half the tool, and Week 9's pipeline plus Weeks 19–22's real datasets will hit multi-table data immediately. *Fix:* add a `customers` table to the prepared dataset, swap SQLZoo section 3 (SELECT within SELECT) for section 6 (JOIN) in the pre-work, and include E1 as a fourth Part 3 question or the T4 replacement.
3. **Stale and contradictory cross-references.** Design Challenge 4 adjusts "the percentile queries from Week 6" — but week-06 is pure Python and contains no SQL (the SQL percentile material lives in the Week 2 supplementary lab document). The debrief's framework is labelled "reiterate from Week 9 preview" while the rationale table says "repeated from Week 6." *Fix:* reconcile after deciding where the Python+SQL supplementary lab actually lives in the arc (see Week 2 supplement, critique 6).
4. **The environment decision is deferred to nobody.** Pre-work says "PostgreSQL via pgAdmin, or SQLite via DB Browser — confirm with the course instructor," and installation is framed as optional ("if you can install one… Part 3 will be faster") — but Part 3 is impossible without a working environment. The reference solutions above also require PostgreSQL features (`DATE_TRUNC`, `INTERVAL`, `PERCENTILE_CONT` later). *Fix:* commit to PostgreSQL as the taught dialect; make install mandatory pre-work with the Week 6 pre-check pattern (a one-line test query); provide a browser fallback (db-fiddle.com or DuckDB shell with the CSV) as the lifeboat, mirroring Week 6's Colab protocol.
5. **The messy dataset exists only as a description.** Design Challenge 2 correctly says its construction is non-negotiable, but there's no spec. *Fix:* pin it down in an instructor note — e.g. ~5,000 rows, 6 months; defects: 3% NULL unit_price (all on cancelled orders), 120 exact-duplicate rows (one export day), category in three casings, order_date in ISO format except one month in DD/MM/YYYY; and record the *correct* answers to Q1–Q3 next to the deliberately-wrong answers naive queries produce. The gap between those two answer sets is the session.
6. **The ambiguous date column is planted but never stepped on.** The dataset spec includes "at least one date column in an ambiguous format," yet Q1–Q3 can all be answered while ignoring it (Q3's DATE_TRUNC will simply error or misparse). *Fix:* either make Q3 depend on fixing it (better), or drop it — an unused trap is prep cost without payoff.
7. **Uneven-pace risk in Part 3 has no channel for fast pairs.** Professional-SQL students finishing in 10 minutes will drift. *Fix:* Activity D (query golf) or a fourth stretch question (E1's INNER-vs-LEFT trap) as the designated overflow.
