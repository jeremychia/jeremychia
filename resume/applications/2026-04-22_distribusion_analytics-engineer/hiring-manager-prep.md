# Hiring Manager Interview Prep — Kilian Brandt, PM @ Distribusion

**Interview focus:** analytics, cross-functional collaboration, problem-solving, alignment with broader business goals.

---

## Who is Kilian Brandt

**Career path:** TU Dresden (vehicle mechatronics engineering) → Audi internship (Python/Matlab tools for automated test evaluation) → TU Dresden research (Python, distributed systems, sensor data detection) → Capgemini (BA → Lead BA; requirements engineering, Scaled Agile) → Distribusion PM (Mar 2024) → Senior PM (Jan 2026, 5 months ago).

**What this means for you:**

- **He is technically literate.** He has written Python, built data tools at Audi, and did research on distributed sensor networks. He will notice hand-waving. Use precise language — "partition pruning", "dbt staging layer", "grain" — without stopping to define them.

- **He thinks in requirements.** Capgemini trained him to probe: *what exactly does "done" mean, and did you understand the ask before building?* When telling stories, be explicit that you clarified the business question before writing a line of SQL. The Tourlane framing — "I asked what decision they needed to make, not what chart they wanted" — is pitched perfectly for him.

- **He has lived through Distribusion's data pain.** He joined in March 2024, before the dbt migration, before proper data quality tooling, during the period of limited analytical capacity. He is not hypothesising about the problems — he has felt them. The question "what's the one analytical question you can't currently answer?" will land hard. He will have a real answer.

- **He was just promoted to Senior PM.** Fast progression (22 months to Senior). He is likely carrying expanded scope and thinking about how to make the data team a force multiplier for his roadmap — not just a ticket queue. Frame yourself as someone who reduces his workload structurally through self-service models, proactive detection, and initiative.

- **His diagnostic instinct.** Years of building checks on physical systems (sensor networks, vehicle diagnostics) means he thinks about "how do you know the reading is correct?" Use this in the €1.6m story: *"I treated the pipeline like an instrumented system — if there's no check on the output, you don't know if it's reading correctly."*

---

## Context to carry in

**Team priorities right now (from Evgeny/Dmitry calls):**
- AI cost guardrails — no guardrails currently, €1,000/day exposure
- Deciding which ad-hoc queries to convert to materialised tables
- Self-service data platform for technical stakeholders
- Looker replacement (free tier → tool with proper permission systems)
- dbt migration is complete; catalog enriched; elementary for data quality

**Kilian's lens as a PM:** data requests that take too long, dashboards that break without notice, not having reliable numbers for decisions. Make his job easier — that's the whole interview.

---

## Opening hook

> "You won the Deutsche Bahn tender in September — a tier-1 rail contract requiring accurate, fast analytics across heterogeneous carrier data models. I built exactly that at Vinted: dashboards on complex multi-source pipelines, tight sprint deadlines, zero margin for error. I'd like to understand where the biggest analytical gaps are right now and whether I can close them."

---

## STAR Stories

### Story 1 — Rapid delivery without sacrificing accuracy
*Use for: speed, reliability, Finance/Ops stakeholder questions*

**S/T:** Finance Ops at Vinted needed dashboards on €40m+ of financial exposure. Sprint deadlines were tight. Numbers had to be right — Finance used these for month-end close.

**A:** Built a change-testing habit: for every model change, validate output against the previous period's known-good numbers before merging. Iterated fast on structure; never iterated on correctness.

**R:** Delivered dashboards within tight sprint deadlines with 100% accuracy on financial reporting. Zero incidents on month-end close.

**PM framing:** "A PM shouldn't have to chase data reliability. I built the habit of validating proactively so they never found a problem before I did."

---

### Story 2 — Found and fixed a problem no one asked me to fix
*Use for: IC initiative, proactiveness, cost/efficiency questions*

**S/T:** Noticed a cost anomaly in GCP billing. Nobody flagged it, no ticket existed.

**A:** Traced it back to finance dashboards triggering full table scans on large Kafka-derived tables. Rewrote the underlying queries using partition pruning and clustering. Did not ask for permission — just fixed it and reported back.

**R:** 75% faster query runtimes. 15% cloud compute cost reduction.

**PM framing:** "I didn't wait for a ticket. That's the operating mode I default to."

**Distribusion link:** Maps directly to their current "AI cost guardrails / query-to-table" priority. Say so if it comes up.

---

### Story 3 — Navigating undocumented infrastructure independently
*Use for: onboarding speed, ambiguity, autonomous working questions*

**S/T:** Joined Vinted with no documentation handoff on shipping finance data — Kafka event streams, carrier billing feeds, BigQuery ETL, all undocumented.

**A:** Traced lineage from source to dashboard manually. Read pipeline code. Built dbt reconciliation models that ran daily and flagged discrepancies above a threshold — set this up proactively after understanding the data.

**R:** Caught a €1.6m billing discrepancy before it hit the books. Before those checks existed, detection was reactive; after, it was early.

**PM framing:** "A PM shouldn't need to explain the data to me. I go find it."

---

### Story 4 — Cross-functional collaboration under deadline
*Use for: stakeholder management, working with non-technical teams*

**S/T:** Joined Tourlane with a finance stack built by someone who had left. No docs, four source systems (Salesforce, Stripe, Twilio, backend), month-end close coming up.

**A:** Treated Finance as a product owner — asked what decision they needed to make, not what chart they wanted. Built the dbt transformation layer from scratch with that framing. Coordinated directly on requirements, validated against their close process.

**R:** Month-end close cycle shortened by 2 days.

**PM framing:** "Asking about the decision first, not the chart, is what gets you something useful on the first iteration."

---

## Alignment with Distribusion's business goals

| Topic | What to say |
|---|---|
| Two-sided marketplace | Carrier side (yield, inventory) vs retailer side (API conversion). Identical structure to Tourlane (buyers/suppliers). I've modelled both sides. |
| Deutsche Bahn contract | Tier-1 rail operator, heterogeneous data. My Vinted experience — multi-carrier billing feeds with different formats — is the direct analogue. |
| Self-service | I build mart tables wide and flat — no joins needed — so stakeholders answer their own questions without pinging me. That's deliberate, not accidental. |
| New carrier markets | Every new market adds a new source schema with different naming and quality. Staging layer absorbs that; mart layer stays stable. I've done this at Vinted and Tourlane. |

---

## Likely PM questions

**"How do you prioritise competing requests?"**
> Ask what decision each request is unblocking. Weight by: how many people are blocked, how time-sensitive the decision is, whether the data even exists. At Vinted, Finance requests took precedence when month-end was close — I made that call explicitly and communicated the queue to other stakeholders.

**"Tell me about a time you pushed back on a stakeholder."**
> A stakeholder at Vinted asked for a metric mixing booking-level and shipment-level grain in the same chart. It would have looked right but produced misleading numbers. I explained the grain problem, proposed an alternative that answered the underlying question cleanly, and we used that. The business question mattered; the specific chart didn't.

**"How do you ensure the data you deliver is accurate?"**
> Validate every model change against known-good historical numbers before it goes live. At Vinted I also built dbt reconciliation tests running daily — that's how I caught the €1.6m billing issue before it hit the books.

**"What does good cross-functional collaboration look like?"**
> Show up knowing enough about the business to ask clarifying questions, not just take orders. Ask about the decision, not the chart. At Tourlane that's what cut the close cycle by 2 days.

**"You come from finance — how quickly can you get up to speed on ground transportation data?"**
> At Vinted I ramped independently on complex, undocumented infrastructure — Kafka streams, carrier billing feeds, BigQuery ETL — with no documentation handoff. New domain, same problem. I trace lineage, read pipeline code, and build context fast.

---

## Questions to ask Kilian

1. **"How does the data team interact with the PM team day-to-day? Are requests mostly reactive — you come to us with a question — or are analytics engineers expected to proactively surface insights that shape your roadmap?"**

2. **"What's the one analytical question you can't currently answer that you most want answered?"**

---

## Mechanics

- Use **"I"** not **"we"** throughout — he's assessing your individual contribution
- Lead with **impact and speed** — he doesn't need to hear about infrastructure elegance
- Wait 2 seconds after finishing a story — don't rush to fill silence
- If asked about Airflow or GitLab gaps: acknowledge briefly, bridge to what you do know, move on
