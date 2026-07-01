# Trace: 2026-06-27_lexroom_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Lexroom.ai

**Location:** Milan, Italy (Hybrid)
**Date Posted:** 2026-06-27
**Salary:** €45,000–€70,000 EUR

---

At Lexroom.ai, we set the bar for legal AI—clear, fast, and built for trust.

In just a few years, what began as an idea has become a reliable platform adopted by thousands of legal professionals across Europe.

Our mission is clear: make the law faster, clearer, and more reliable, giving lawyers, law firms, and companies the time and confidence to focus on what truly matters.

We're scaling rapidly, backed by top-tier investors and a world-class team dedicated to rigor, clarity, and impact.

Today, Lexroom is a trusted partner, shaping the future of legal AI with discipline and purpose.

Why Lexroom.ai?
Shape the Standard: Be part of the team setting the benchmark for legal AI in Europe.

Work with the Best: Collaborate with exceptional colleagues in a culture that values competence, curiosity, and ambition.

Deliver Meaningful Results: Your work will directly influence how legal professionals operate—faster, clearer, and more efficiently.

At Lexroom.ai, we leave buzzwords behind. Here, you'll build something that lasts: a trusted platform, a strong reputation, a new standard for the legal world.

What You'll Do
Own the data transformation layer from raw sources to trusted, documented datasets—designing and maintaining a dbt project on BigQuery with staging, intermediate, and mart layers.

Model product analytics events (user interactions, feature adoption, feedback signals), engineering metrics, and business KPIs into reliable, self-service data models.

Build and maintain the data foundations powering our dashboards, decisions, and team health metrics.

Implement data quality frameworks: tests, freshness checks, anomaly detection, and clear ownership and SLAs on key datasets.

Collaborate with engineers to improve event tracking and data contracts at the source (Pub/Sub, application events).

Create and curate dashboards and semantic layers that Product, CS, and Sales teams can query directly—enabling true self-service analytics.

Partner with the AI & Search Platform team to instrument and measure model performance, feedback loops, and benchmark results.

Support Product teams with ad-hoc analysis: feature impact, user segmentation, satisfaction trends, and power-user behavior.

What You'll Bring
3+ years of experience in analytics engineering, data engineering, or a data analyst role with a strong engineering mindset.

Expert SQL skills and hands-on experience with dbt (dbt Core or dbt Cloud).

Solid experience with BigQuery or comparable cloud data warehouses (Snowflake, Redshift).

Strong understanding of dimensional modeling, data testing, and documentation-as-code practices.

Comfortable working in a Python ecosystem (scripting, basic ETL, notebooks for exploration).

Experience building data models that serve multiple stakeholders (product, engineering, business).

Fluent English; Italian is a strong plus.

Nice to Have

Experience with event-driven architectures (Pub/Sub, Kafka) and streaming data.

Familiarity with Elasticsearch, Pinecone, or vector databases.

Exposure to engineering metrics (DORA, PR analytics) or developer productivity measurement.

Experience with BI/visualization tools (Retool, Looker Studio, Metabase).

Interest in AI/ML model evaluation and LLM output quality measurement.

Previous experience in legal-tech, RegTech, or B2B SaaS.

What Sets Us Apart
An Exceptional Team

At Lexroom.ai, you'll work alongside top talent in tech and legal AI.

Our focused teams operate with purpose and autonomy, so every contribution delivers visible results.

You'll collaborate with people who pair innovation with rigor, curiosity with discipline, ambition with depth.

A Foundational Role

This is our first dedicated analytics hire. You won't inherit a legacy stack or fight bureaucracy—you'll design the analytics function from scratch with direct executive sponsorship, a moder…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 5 | 5 | 5 | 100% |
| data_team_maturity | early | early | early | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | product | product | product | 100% |
| autonomy_level | strategic | strategic | strategic | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Implement data quality frameworks: tests, freshness checks, anomaly detection, and clear ownership and SLAs on key datasets."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, data contracts, SLAs, and reliability as core expectations, with no velocity-oriented language present.

**Run 2:** `rigour`
> Quote: "Implement data quality frameworks: tests, freshness checks, anomaly detection, and clear ownership and SLAs on key datasets."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, SLAs, and reliability throughout the responsibilities, with no competing velocity signals.

**Run 3:** `rigour`
> Quote: "Implement data quality frameworks: tests, freshness checks, anomaly detection, and clear ownership and SLAs on key datasets."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (data quality, testing, SLAs, data contracts, documentation-as-code) dominate the responsibilities, while velocity signals are absent, making rigour the primary orientation.

### domain_risk

**Run 1:** `moderate`
> Quote: "Model product analytics events (user interactions, feature adoption, feedback signals), engineering metrics, and business KPIs into reliable, self-serve data models."
> Verified: ⚠ NOT found verbatim
> Reasoning: The role focuses on product analytics and business KPIs without explicit financial reporting, compliance, or regulatory language, placing it in moderate rather than high risk.

**Run 2:** `moderate`
> Quote: "Your work will directly influence how legal professionals operate—faster, clearer, and more efficiently."
> Verified: ✓ found in JD
> Reasoning: While the platform affects legal professionals' workflows, there is no explicit financial reporting, regulatory compliance, or audit language that would indicate high risk.

**Run 3:** `moderate`
> Quote: "make the law faster, clearer, and more reliable"
> Verified: ✓ found in JD
> Reasoning: Although the platform serves legal professionals in a regulated sector, the specific role focuses on product analytics and business metrics rather than regulatory, compliance, or financial reporting.

### collaboration_width

**Run 1:** `5`
> Quote: "engineers; Product, CS, and Sales teams; AI & Search Platform team"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names five distinct partner functions across engineering, product, customer success, sales, and the AI platform team.

**Run 2:** `5`
> Quote: "engineers; Product, CS, and Sales teams; AI & Search Platform team"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names five distinct partner teams: engineers, Product teams, Customer Success, Sales, and the AI & Search Platform team.

**Run 3:** `5`
> Quote: "engineers; Product, CS, and Sales teams; AI & Search Platform team"
> Verified: ⚠ NOT found verbatim
> Reasoning: Five distinct named partner functions are explicitly identified across responsibilities: Engineers, Product, Customer Success, Sales, and the AI & Search Platform team.

### data_team_maturity

**Run 1:** `early`
> Quote: "This is our first dedicated analytics hire. You won't inherit a legacy stack or fight bureaucracy—you'll design the analytics function from scratch with direct executive sponsorship"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly states this is the first analytics hire and emphasizes designing the analytics function from scratch, hallmarks of early-stage data teams.

**Run 2:** `early`
> Quote: "This is our first dedicated analytics hire."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly states this is the first analytics hire and the role will design the analytics function from scratch.

**Run 3:** `early`
> Quote: "This is our first dedicated analytics hire. You won't inherit a legacy stack or fight bureaucracy—you'll design the analytics function from scratch"
> Verified: ✓ found in JD
> Reasoning: Explicit positioning as the first analytics hire building the data function from scratch with modern infrastructure is the canonical early-stage signal.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Own the data transformation layer from raw sources to trusted, documented datasets—designing and maintaining a dbt project on BigQuery with staging, intermediate, and mart layers. Model product analytics events (user interactions, feature adoption, feedback signals), engineering metrics, and business KPIs into reliable, self-serve data models."
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain technical specificity about dbt architecture patterns, dimensional modeling, data contracts, and semantic layers that indicates hands-on experience writing them.

**Run 2:** `hiring_manager`
> Quote: "designing and maintaining a dbt project on BigQuery with staging, intermediate, and mart layers."
> Verified: ✓ found in JD
> Reasoning: The specific dbt architecture (staging, intermediate, mart layers), named tools with precise context (BigQuery, Pub/Sub, data contracts), and technical specificity indicate someone who has done this job.

**Run 3:** `hiring_manager`
> Quote: "designing and maintaining a dbt project on BigQuery with staging, intermediate, and mart layers"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain technical specificity only an experienced practitioner would include: named tools with precise architectural context (dbt layer structure, BigQuery, event-driven architectures), dimensional modeling, and data contracts.

### stakeholder_orientation

**Run 1:** `product`
> Quote: "Model product analytics events (user interactions, feature adoption, feedback signals), engineering metrics, and business KPIs into reliable, self-serve data models. Support Product teams with ad-hoc analysis: feature impact, user segmentation, satisfaction trends, and power-user behavior."
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary emphasis is on product analytics—user interactions, feature adoption, and feature impact analysis—with product teams as the core audience.

**Run 2:** `product`
> Quote: "Model product analytics events (user interactions, feature adoption, feedback signals)"
> Verified: ✓ found in JD
> Reasoning: The core responsibilities emphasize product analytics—feature adoption, user behavior analysis, feature impact measurement—with CS/Sales support secondary.

**Run 3:** `product`
> Quote: "Model product analytics events (user interactions, feature adoption, feedback signals), engineering metrics, and business KPIs into reliable, self-service data models."
> Verified: ✓ found in JD
> Reasoning: Product-focused responsibilities (feature impact analysis, user segmentation, power-user behavior) appear with the highest specificity and frequency, establishing Product as the primary audience.

### autonomy_level

**Run 1:** `strategic`
> Quote: "This is our first dedicated analytics hire. You won't inherit a legacy stack or fight bureaucracy—you'll design the analytics function from scratch with direct executive sponsorship, a modern stack (BigQuery, dbt, Pub/Sub, Python, GCP), and real strategic impact from day one."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes designing and establishing the analytics function from scratch with executive support and clearly positions this as setting strategic direction, not executing pre-defined work.

**Run 2:** `strategic`
> Quote: "you'll design the analytics function from scratch with direct executive sponsorship"
> Verified: ✓ found in JD
> Reasoning: The role owns the analytics function design and has explicit strategic impact, not just executing pre-defined work.

**Run 3:** `strategic`
> Quote: "you'll design the analytics function from scratch with direct executive sponsorship"
> Verified: ✓ found in JD
> Reasoning: Explicit framing as the foundational hire responsible for designing the analytics function from scratch with executive support places this in a direction-setting, strategic role rather than execution-only.

### ai_role
**Run 1:** `none` ✓
> Quote: "a modern stack (BigQuery, dbt, Pub/Sub, Python, GCP)"
> Reasoning: Tech stack mentions traditional data tools only; no AI coding tools, AI-ready infrastructure, or GenAI responsibilities signaled.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Implement data quality frameworks: tests, freshness checks, anomaly detection, and clear ownership and SLAs on key datasets"
> Reasoning: Candidate owns quality practice via 'Implement' verb paired with frameworks, tests, and SLA accountability.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "clear ownership and SLAs on key datasets; freshness checks, anomaly detection"
> Reasoning: Operational reliability framed through SLAs and data correctness checks, not compliance or stakeholder-trust dominance.

