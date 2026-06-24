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

**Reading:** no textbook reading for this week. The pre-work is entirely practical.

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

**Tool decision framework (reiterate from Week 9 preview):**

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

**Resolution:** the instructor specifies which environment is in use at the start of the session. If SQLite is used, the percentile queries from Week 6 are adjusted accordingly. This is an administrative check, not a pedagogical challenge — but it must be resolved before Part 3 begins.

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
