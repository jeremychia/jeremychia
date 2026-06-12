# Recruiter Call Prep — Analytics Engineer at Distribusion Technologies

**Application folder:** 2026-04-22_distribusion_analytics-engineer
**Prepared:** 2026-04-24

---

## 1. What the recruiter is screening for

### Viability checklist
- **Looker dashboard development** → Clearly covered: multiple bullets at Vinted and Tourlane, calculated-field architecture, sprint delivery, finance and ops dashboards.
- **BigQuery + GCP + Kafka** → Clearly covered: Vinted bullet on tracing Kafka event streams, BigQuery ETL, Cloud Functions / Pub/Sub / Cloud Storage.
- **Apache Airflow** → Listed in skills; no dedicated story in the resume. Minor gap — prepare a sentence on any Airflow exposure (even monitoring pipelines, or awareness from Vinted's orchestration layer).
- **Python and SQL scripting** → Clearly covered: dbt/SQL at Vinted and Tourlane; Python teaching at ReDI; scripting implied by GCP automation work.
- **Git / GitLab / GCP** → Covered for GCP and Git. Resume lists GitHub; JD says GitLab specifically. Be ready to acknowledge the GitLab gap and bridge to Git fundamentals.

### Soft skill and culture fit signals
The JD uses "rapid", "tight deadlines", "single-day timeframes", "rigorous accuracy", "independently", and "anticipate future challenges" — this is a fast-moving IC role where speed and accuracy must coexist without hand-holding. The recruiter is screening for someone who acts first and escalates rarely. Mirror this tone on the call: be direct, quantify everything, avoid governance or architecture framing.

### Likely hard question
**"You come from a finance-heavy background — how quickly can you get up to speed on ground transportation data?"**
*Suggested response frame:* At Vinted I ramped independently on complex, undocumented data infrastructure — Kafka streams, carrier billing feeds, BigQuery ETL — with no documentation handoff. New domain, same problem. I trace lineage, read pipeline code, and build context fast. That's what your JD is actually asking for.

---

## 2. Your Peak moment

> "At Vinted, I owned the full analytics stack for shipping finance — built Looker dashboards delivering accurate reporting on €40m+ of financial exposure, redesigned BigQuery queries for 75% faster runtimes, and cut cloud compute costs by 15%, all while working autonomously against tight sprint deadlines."

*Why this works:* Directly addresses the top JD responsibility (rapid Looker delivery), the secondary ask (infrastructure ownership and optimisation), and the accuracy constraint — all in one answer.

---

## 3. STAR story prompts

For each theme, use STAR+Spark: Situation/Task (20%), Action — use "I" not "we" (60%), Result with a number (20%), Learning/Spark (1 sentence).

### Theme 1: Rapid dashboard delivery under tight deadlines
**Source bullet:** "Delivered Looker dashboards within tight sprint deadlines for Finance Ops and Group Reporting; built and iterated calculated-field architecture to enable rapid metric changes while maintaining 100% accuracy on €40m+ of financial exposure."
**Prompt:** Prepare a story about a moment at Vinted when a stakeholder needed a dashboard fast — walk through how you structured it for speed without sacrificing accuracy, and what the specific deadline pressure looked like. End with what you would do differently to go even faster.

### Theme 2: Independent data infrastructure navigation
**Source bullet:** "Worked independently to understand and navigate data infrastructure: traced upstream Kafka event streams and carrier billing feeds, understood BigQuery ETL dependencies, diagnosed data quality issues, and optimised queries without hand-holding."
**Prompt:** Prepare a story about joining Vinted and having to understand a complex, partially undocumented pipeline — walk through how you traced the data lineage, what tools you used, what you found, and how long it took. End with the diagnostic pattern you now apply by default.

### Theme 3: Proposing and implementing reporting enhancements
**Source bullet:** "Proposed and implemented enhancements to reporting systems: identified pipeline inefficiencies, redesigned BigQuery queries for 75% faster runtimes, and cut cloud compute costs by 15% through workload pattern optimisation."
**Prompt:** Prepare a story about identifying a reporting inefficiency that no one had asked you to fix — how you spotted it, built the case to act on it, and what the measurable outcome was. End with what this tells you about how to operate in an IC role.

---

## 4. Company research findings

### Business model and unit economics
Distribusion is a middleman between two groups: transportation companies (buses, trains, ferries) and travel websites (Google, Booking.com, Alipay, Trainline, Amadeus). Every time someone books a ticket through one of those websites, Distribusion takes a small cut. The more bookings, the more money they make. For the data team, this means tracking: how many people complete a booking (conversion rates), which carriers are performing well, and making sure commission payments are accurate.

*Technical angle:* Key revenue drivers are booking volume, the number of carriers on the platform, and retailer integrations. Every new carrier partnership adds new data sources — each with slightly different formats and quality issues — that need to be modeled and monitored. [Source: PhocusWire](https://www.phocuswire.com/b2b-ground-transportation-marketplace-distribusion-raises-80m)

### Competitive position
**Who they're up against:** Distribusion's main competitors are [Transferz](https://www.transferz.com/) (founded 2020, focuses on airport transfers), [Busbud](https://www.busbud.com) (launched B2B API offering "Busbud Business" in 2015, emphasizes bus + train), and [Bookaway](https://www.cbinsights.com/company/bookaway) (buses, trains, ferries but primarily consumer-facing). [Source: CBInsights](https://www.cbinsights.com/company/busbud/alternatives-competitors)

**Distribusion's edge:** They developed the first global B2B booking API and operate across 70 markets with coverage of all major European rail carriers (Deutsche Bahn, SNCF, Trenitalia). [Source: Tech.eu](https://tech.eu/2024/09/26/berlin-based-distribusion-secures-80m-for-global-ground-transport-accessibility/) They're the only platform covering multi-modal ground transport (buses, trains, ferries, public transport) with a single API — competitors typically specialize in one mode or focus on B2C rather than B2B. 

**Why this matters for the data team:** The data team is likely focused on proving that the API works reliably across heterogeneous carriers, demonstrating ROI to both travel retailers (Google, Booking.com) and carriers, and optimizing the booking flow to increase conversion rates and carrier adoption.

### Data stack and engineering culture
Confirmed from the JD itself: BigQuery (data warehouse), Kafka (event streaming), Airflow (orchestration), Looker and Grafana (BI / monitoring), GCP (cloud platform), GitLab (version control). Crunchbase confirms Kafka in the tech stack. No public engineering blog found. The JD signals a GCP-native setup — expect BigQuery-centred analytics with Kafka feeding real-time booking events.

### Data team size and structure
~369 employees total as of February 2026. [Source: Distribusion news/funding data] A concurrent Senior Data Engineer role is also open, suggesting a small but actively hiring data function. The JD framing — no mention of team leadership, governance, or data modeling layers — signals a lean IC team where each person owns a full domain end-to-end. Likely centralised data team serving product and commercial stakeholders.

### Recent news and growth signals
- **$80M Series C** closed September 2024 led by TQ Ventures and Lightrock, total raised $118M. Purpose: global expansion and advanced retail technology for partners. [Source: Distribusion](https://www.distribusion.com/news/distribusion-announces-$80m-series-c-led-by-tq-ventures-to-drive-global-expansion-and-to-double-down-on-advanced-retail-technology-for-its-partners)
- **Deutsche Bahn tender won** September 2024 — multi-carrier sales solution; signals major enterprise contract with a tier-1 rail operator. [Source: Distribusion news]
- **Named Top 100 Next Unicorns 2024** by Viva Technology / GP Bullhound.
- Active geographic expansion in 2025: Brazil, Indonesia (KAI), Slovakia, Italy — each new market adds carrier data sources.

### Role-specific insight
Deutsche Bahn is Germany's largest rail operator. Winning their business means Distribusion now has to build dashboards and analytics specifically for how their tickets are selling across all the travel websites. This is complex because Deutsche Bahn's data is different from other carriers (buses, ferries, etc.), and the dashboards need to be fast and accurate. As Distribusion adds more carriers (Brazil, Indonesia, Slovakia), each one has slightly different data formats and quality issues. The dashboards need to work across all of them without slowing down.

### Suggested opening hook
> "You won the Deutsche Bahn tender in September for a multi-carrier sales solution — that contract requires analytics across heterogeneous carrier data models at speed. I built exactly that at Vinted: fast, accurate dashboards on complex, multi-source BigQuery pipelines. That's the problem I solve."

---

## 5. Opening and closing

### Opening (first 60 seconds)
Use the hook above. Lead with the Deutsche Bahn fact — it shows you've done the research. Name the data problem plainly (multi-source, high-velocity, accuracy-critical). End with one concrete capability statement. Keep it under 4 sentences. Don't explain your career history unprompted — wait for them to ask.

### Closing statement
> "I've built fast, accurate Looker dashboards on BigQuery and GCP in a high-stakes, autonomous environment — that's the core of what you need. I'm in Berlin, available to start within a few weeks. What's the next step?"

---

## 6. Questions to ask

Pick 1–2 for the call; have the others ready if the conversation opens up.

### Impact / success definition
> "You won the Deutsche Bahn tender in September for a multi-carrier sales solution. In the first 6 months, is the analytics work primarily oriented around that contract — building dashboards for carrier performance, booking funnel, or SLA reporting — or is there a broader dashboard backlog this role is expected to clear?"

### Team problem
> "The JD asks candidates to independently navigate data sources and processing workflows — which suggests the infrastructure may be complex or partially undocumented. Is the hardest data challenge right now about data discovery and lineage as the carrier network scales, or more about keeping dashboard delivery fast enough to match the speed of commercial expansion?"

### Business / strategy
> "You're a B2B marketplace — revenue flows through booking volume on both sides of the network. How does the data team balance analytics priorities between the retailer side (API conversion, performance) and the carrier side (yield, inventory)? Or does this role own one side more than the other?"

### Ways of working
> "The JD says 'leverage available tools and resources to solve problems independently' — what does that look like when I hit a data quality issue that blocks a dashboard? Do I own the full resolution — investigation, fix, redelivery — or is there a data engineering team I hand off pipeline problems to?"

*Why specific questions work:* Generic questions ("what does success look like?") are forgettable. Questions that reference the Deutsche Bahn contract, the carrier data complexity, or the two-sided marketplace dynamic signal that you understand the business — and that you're already thinking about the problems, not just the job title.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story — prevents rambling, gives recruiter time to finish notes.
- **Use "I" not "we"** — recruiters assess your individual contribution.
- **Salary / notice period** — state your range confidently. If pushed early: "I'm flexible depending on the full package — can you share the budgeted range for the role?"

---

## 8. Technical Assignment Presentation

> [TODO: describe the assignment prompt and what you built before filling this section]

### Presentation structure (5–7 minutes)

1. **Problem statement** (30 sec) — restate the brief in one sentence to confirm you understood the ask.
2. **Approach** (1 min) — what you chose to do and why. Name alternatives you explicitly rejected and the reasoning.
3. **Implementation walkthrough** (2–3 min) — walk through the key artefact (SQL, dashboard, model). Narrate decisions, not just steps: "I partitioned by date here because the query was scanning the full table and that's expensive in BigQuery."
4. **Result / output** (1 min) — what the output actually answers. If it's a dashboard: what question does each chart answer? If it's SQL/model: what does the output grain represent?
5. **Limitations and what you'd do next** (1 min) — proactively name one real limitation and the concrete next step. Shows self-awareness and production thinking.

### Anticipated Q&A

**"Why did you structure it this way rather than X?"**
Anchor on a concrete constraint: "I chose Y because the grain of the raw data meant Z would produce fan-out" or "Y was faster to build and the brief asked for a working prototype, not production code." Avoid defending blindly — if X is better, say so and explain what would need to change.

**"How would you take this to production?"**
Hit three things: testing / data quality checks (dbt tests or assertions), scheduling/orchestration (Airflow DAG or equivalent), and access control / permissions. Mention that at Vinted you implemented dbt tests and monitoring that detected anomalies early.

**"What assumptions did you make?"**
Prepare two or three explicit assumptions you made about the data, grain, or scope. Naming them confidently signals rigour. Hiding them signals you didn't notice them.

**"Walk me through this piece of SQL / logic."**
Narrate at the level of intent, not syntax: "This CTE isolates one row per booking because downstream I need a booking-level grain — without it you'd get duplicates in the join." Don't read the code line by line.

**"What would you do if you had more time?"**
Have one concrete answer that addresses a real gap in your submission, not a generic "I'd add more charts." Specific = credible.

### Context from discovery call to weave in
The team is actively migrating away from Looker (on free tier) to a new reporting tool with proper permission systems — if your assignment involved Looker, acknowledge you're aware the tooling is in transition and your approach would transfer. They've recently introduced dbt with core models living there; if your assignment includes SQL or modelling, tie it to dbt patterns you'd use in production.

---

## 9. Technical Deep Dive — Airflow, SQL, Data Modelling, Statistics

### Airflow

**What they're likely testing:** whether you can read and reason about DAGs, understand scheduling, and diagnose failures — not necessarily that you've built pipelines from scratch.

**Key concepts to know cold:**
- **DAG** — directed acyclic graph; tasks + dependencies; each run is a DAG run.
- **Operators** — unit of work: `PythonOperator`, `BashOperator`, `BigQueryInsertJobOperator`, `BigQueryCheckOperator` (for data quality assertions).
- **Scheduling** — cron expression on the DAG; `start_date` + `schedule_interval`. `catchup=True` will backfill missed runs.
- **XCom** — cross-communication between tasks; push/pull values. Avoid large payloads; XCom is not for passing datasets.
- **Connections / Variables** — store credentials and config outside code; accessed via `BaseHook.get_connection()` or `Variable.get()`.
- **Retries and SLAs** — `retries`, `retry_delay`, `sla` on tasks; SLA miss triggers a callback.
- **Idempotency** — a task should produce the same result regardless of how many times it runs. Critical for reruns and backfills. Achieved by overwriting rather than appending, or using `WRITE_TRUNCATE` in BigQuery.

**Honest gap statement if asked about depth:**
> "At Vinted I worked with Airflow at the consumption end — monitoring DAG runs, reading logs to diagnose upstream failures, and working with the data engineers to unblock my pipeline dependencies. I haven't owned DAG authorship end-to-end, but I understand the orchestration model well enough to build and extend DAGs."

**Likely question:** "If a downstream table is empty this morning and your dashboard is wrong, how do you diagnose it?"
*Answer frame:* Check Airflow for DAG run status and task logs. Identify which task failed or produced zero rows. Check if it's a data availability issue (late-arriving Kafka events), a task failure (exception in the operator), or a silent bug (task succeeded but wrote zero rows — this is why you need `BigQueryCheckOperator` or a dbt test on row count). Fix at source, re-trigger from the failed task.

---

### SQL

**What they're testing:** ability to write correct, efficient BigQuery SQL for analytical problems — not just basic SELECT; expect window functions, performance reasoning, and BigQuery-specific behaviour.

**Window functions — know these by heart:**
| Function | Use case |
|---|---|
| `ROW_NUMBER() OVER (PARTITION BY x ORDER BY y)` | Deduplicate; pick the latest row per entity |
| `RANK()` / `DENSE_RANK()` | Leaderboard ranking; DENSE skips no numbers |
| `LAG(col, n)` / `LEAD(col, n)` | Compare current row to previous/next; useful for churn, retention |
| `SUM() OVER (PARTITION BY x ORDER BY y ROWS UNBOUNDED PRECEDING)` | Running total |
| `FIRST_VALUE()` / `LAST_VALUE()` | First/last booking per carrier, per day |
| `NTILE(n)` | Quartile / decile bucketing |

**BigQuery-specific performance patterns:**
- **Partition pruning** — always filter on the partition column in WHERE; otherwise BigQuery scans the full table. Ask: "Is this table partitioned? On what column?"
- **Clustering** — secondary sort on frequently filtered columns (e.g. `carrier_id`); reduces bytes scanned within a partition.
- **Avoid `SELECT *`** — BigQuery bills by bytes scanned; projecting only needed columns is a real cost reduction. This is how you cut 15% cloud costs at Vinted.
- **`UNNEST`** — for array/struct columns common in event schemas (e.g. Kafka payloads stored as JSON arrays); use `CROSS JOIN UNNEST(array_col) AS item`.
- **`APPROX_COUNT_DISTINCT`** — for large datasets where exact cardinality isn't needed; orders of magnitude cheaper than `COUNT(DISTINCT)`.
- **CTEs vs subqueries** — CTEs improve readability; in BigQuery, CTEs are not materialised by default (they're inlined), so very heavy CTEs referenced multiple times may benefit from temp tables.

**Likely live coding question:** "Write a query to find the top 3 carriers by booking volume in each country over the last 30 days."
```sql
WITH ranked AS (
  SELECT
    country,
    carrier_id,
    COUNT(*) AS booking_count,
    ROW_NUMBER() OVER (PARTITION BY country ORDER BY COUNT(*) DESC) AS rk
  FROM bookings
  WHERE booking_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  GROUP BY country, carrier_id
)
SELECT country, carrier_id, booking_count
FROM ranked
WHERE rk <= 3
```
*Walk through:* aggregate first, then rank within partition — avoids self-join. Mention that if you needed ties to both appear, you'd use `RANK()` instead of `ROW_NUMBER()`.

---

### Data Modelling

**What they're testing:** whether you can design models that are correct, maintainable, and serve self-service analytics — Distribusion explicitly mentioned self-service as a priority.

**Core concepts:**
- **Grain** — the single most important modelling decision. Define it before writing any SQL: "One row = one booking leg." Mis-specified grain causes fan-out or data loss in joins.
- **Star schema** — fact table (events/transactions) surrounded by dimension tables (carriers, routes, retailers). Minimises joins for analytics queries.
- **Slowly Changing Dimensions (SCD):**
  - Type 1: overwrite — no history, simplest.
  - Type 2: add a new row with valid_from/valid_to — full history, more complex queries.
  - Type 3: add a previous_value column — limited history.
  - At Distribusion: carrier attributes (e.g. pricing tiers, route coverage) probably change over time → Type 2 for anything history-sensitive.
- **dbt layer conventions** (align to what they've just introduced):
  - `staging` — one-to-one with source; rename columns, cast types, no business logic.
  - `intermediate` — joins and transformations; not exposed to BI.
  - `mart` — business-grain, self-service ready; what analysts and dashboards query.
- **Denormalisation for BI** — mart tables should be wide and flat so a non-technical user can drag columns into a chart without knowing joins.

**Likely question:** "How would you model a booking event that can have multiple legs (e.g. bus + train + ferry)?"
*Answer:* Define two tables — a `fct_bookings` at booking level (one row per booking, total price, retailer, status) and a `fct_booking_legs` at leg level (one row per leg, carrier, mode, segment price). Booking-level metrics aggregate over `fct_bookings`; carrier performance metrics aggregate over `fct_booking_legs` joined back to booking context. Keeps grain clean and avoids double-counting.

**Distribusion-specific context:** Every new carrier market adds new source schemas with different naming and quality. Model defensively: staging layer absorbs schema variation, intermediate layer standardises, mart layer is stable. This is exactly the pattern you used at Vinted (multi-carrier billing feeds, each with different formats).

---

### Statistics / Probability Theory

**What they're testing:** analytical reasoning under uncertainty — conversion rate analysis, A/B test interpretation, anomaly detection. This is likely light (screening for numeracy), not a statistics PhD exam.

**Know these cold:**

**Hypothesis testing:**
- Null hypothesis (H₀): no effect / no difference.
- p-value: probability of observing this result if H₀ is true. p < 0.05 means "unlikely under the null" — not that the effect is meaningful.
- Type I error (false positive): reject H₀ when it's true. Controlled by significance level α.
- Type II error (false negative): fail to reject H₀ when it's false. Controlled by statistical power (1 − β), typically ≥ 80%.
- **Always ask:** Is the sample size large enough? (Power analysis.) Is the test duration long enough to avoid peeking bias?

**A/B testing:**
- Sample size formula depends on: baseline conversion rate, minimum detectable effect, α, and power.
- Peeking problem: stopping a test early because it "looks significant" inflates Type I error — use sequential testing or pre-commit to a fixed runtime.
- Practical significance vs statistical significance: a 0.1% conversion lift may be statistically significant with a huge sample but commercially irrelevant.

**Distributions relevant to Distribusion:**
- **Binomial** — booking conversion (did the user complete a booking? yes/no).
- **Poisson** — booking arrival rate per hour; inter-arrival times follow exponential distribution.
- **Normal** — aggregated revenue distributions, query latency distributions (CLT).

**Common traps to name if asked:**
- **Simpson's paradox** — a trend appears in all subgroups but disappears or reverses in the aggregate. Common in marketplace data (e.g. carrier A has higher conversion in every country, but lower overall because it operates in lower-volume markets).
- **Survivorship bias** — analysing only completed bookings ignores abandoned sessions; conversion funnel metrics must include the full funnel denominator.
- **Seasonality / confounding** — booking volume changes with school holidays, events, weather. Comparing periods without controlling for these inflates perceived effects.

**Likely question:** "Carrier X's conversion rate dropped 5% last week. How do you investigate?"
*Answer:* First, establish the baseline — is 5% within normal week-to-week variance or a real signal? Segment by: retailer (is it all retailers or one?), route (specific origin-destination?), time of day, device. Check for data pipeline issues (are events even arriving correctly?). If segmentation isolates it, form a hypothesis and check against external events (price change, route cancellation, competitor entry). Only then conclude.

---

## 10. Day-to-Day Challenges and Projects (Most Recent Roles)

*Use these when asked "walk me through a typical week" or "what were the hardest problems you worked on?"*

### Vinted — Shipping Finance Analytics (Aug 2023 – Present)

**The core challenge:** Shipping finance sits at the intersection of carrier contracts, Kafka event streams, and financial reporting — any data quality issue has direct P&L impact. The hardest part was that none of this was documented when I joined.

**Day-to-day:**
- **Dashboard sprint cycle:** Most weeks involved 1–2 stakeholder requests for new Looker views or metric changes. The pattern: understand the business question, trace back to the correct BigQuery grain, build the calculated field or derived table, validate against known numbers, deliver. Iteration speed mattered more than perfection on the first draft — but the numbers had to be right because Finance Ops was using these dashboards for month-end close.
- **Data quality firefighting:** Carrier billing feeds are messy. A carrier might send a corrected invoice that changes historical figures, or send duplicate events that inflate cost accruals. I built dbt reconciliation models that ran daily and flagged discrepancies above a threshold — this is how I detected the €1.6m billing discrepancy. Before those checks existed, it was reactive; after, it was early detection.
- **Pipeline debugging:** When a dashboard showed wrong numbers, the first step was always to trace upstream — Kafka event → BigQuery raw table → ETL transformation → dbt model → Looker. Usually the issue was in one of those layers. I learned to read BigQuery ETL code and Airflow logs well enough to diagnose without needing a data engineer in every investigation.
- **Cost and performance work:** Identified that several finance dashboards were triggering full table scans on large Kafka-derived tables. Rewrote the underlying queries to use partition pruning and clustering — that's where the 75% faster runtime and 15% cost reduction came from. It wasn't a project I was asked to do; I noticed the cost anomaly in GCP billing and traced it back.

**What was hardest:**
> "The hardest thing was maintaining accuracy on financial dashboards that stakeholders trusted completely, while making rapid changes to the underlying models. A calculated field change that looks small can break a metric across 10 existing tiles. I solved this by introducing a change-testing habit: for every model change, I validated output against the previous period's known-good numbers before merging."

### Tourlane — Finance Data (Jul 2022 – Aug 2023)

**The core challenge:** A startup finance data stack built by someone who had left. No documentation, mixed SQL quality, and an upcoming month-end close deadline.

**Day-to-day:**
- **dbt transformation layer:** Built from scratch integrating four source systems (Salesforce for pipeline, Stripe for payments, Twilio for comms costs, backend for bookings). Each source had different conventions and data quality issues. The staging layer absorbed that complexity so the mart layer was clean.
- **Dashboard performance:** Tourlane's Looker dashboards were slow because the underlying Snowflake queries weren't using clustering or materialised views. I profiled the slow queries, identified the bottlenecks, and rewrote — 60% load time reduction meant analysts stopped waiting and started using the data.
- **Month-end close support:** Finance needed to close the books with accurate actuals against forecast. I built the reporting views they used for that process and got it to a point where the cycle was 2 days shorter.

**Transition note for Distribusion:** Tourlane was also a marketplace (buyers and suppliers), so I understand two-sided data problems — tracking conversion on one side while managing supplier/carrier data on the other. That's structurally the same as Distribusion's carrier vs retailer split.
