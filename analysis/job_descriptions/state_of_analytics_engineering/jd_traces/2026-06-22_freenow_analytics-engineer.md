# Trace: 2026-06-22_freenow_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — FREE NOW (Freenow by Lyft)

**URL:** https://job-boards.greenhouse.io/freenow/jobs/7189275?gh_src=0c92915e1us
**Location:** Hamburg, Berlin, or Barcelona

---

## Key Responsibilities

- Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment
- Engage with analysts and scientists to understand problems and translate them into data solutions
- Work with developers on data creation aligned with business logic
- Own the quality, availability, and trustworthiness of data — through quality checks and data contracts
- Design solutions for KPIs and business metrics
- Troubleshoot data issues across the stack
- Build an environment where self-service capabilities are available for analysts and data consumers

---

## Required Qualifications

- Curiosity in your essence, aligned with attention to detail
- Background in data-driven analytics environments, ideally within tech product organisations
- Expert level of SQL (especially SparkSQL) and experience in building data pipelines
- Knowledge of at least one programming language (Python preferred)
- Exceptional analytical skills, lateral thinking, and proven experience in solving complex data problems
- Experience with data visualisation tools (e.g. Tableau) and event tracking platforms (e.g. Mixpanel)
- Excellent English communication skills

---

## Preferred / Bonus Skills

- Experience with AWS, Hive, Spark, Trino, Databricks, and Airflow
- Familiarity with streaming tools such as Kafka and Debezium
- Experience working in Data Mesh or distributed data ownership architectures

---

## Tech Stack

SQL | Python | Databricks | Tableau | Mixpanel | Airflow | AWS | Kafka | Debezium

---

## Benefits

- Flexible working arrangements
- LinkedIn Learning access
- Sabbatical and special leave policies
- WeRoad partnership (travel benefits)
- Health insurance
- Employee Assistance Programme
- Location-specific additional benefits (Hamburg, Berlin, Barcelona)

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 4 | 3 | 3 | 3 | 100% | ✗ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | recruiter | mixed | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: The responsibilities explicitly frame quality assurance, data contracts, and trustworthiness as core expectations with no corresponding velocity signals present.

**Run 2:** `rigour` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality checks, data contracts, and trustworthiness as core expectations with no velocity signals like fast-paced or rapid delivery present.

**Run 3:** `rigour` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, trustworthiness, and data contracts as core expectations with no counterbalancing velocity language.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Design solutions for KPIs and business metrics"
> Verified: ✓ found in JD
> Reasoning: The role focuses on business intelligence and analytical products without explicit financial reporting, compliance, or regulatory language, indicating moderate risk to business decision-making.

**Run 2:** `moderate` ✓
> Quote: "Design solutions for KPIs and business metrics"
> Verified: ✓ found in JD
> Reasoning: The role focuses on internal analytics infrastructure and business metric design rather than financial reporting, regulatory compliance, or public-facing product impact.

**Run 3:** `moderate` ✓
> Quote: "Design solutions for KPIs and business metrics"
> Verified: ✓ found in JD
> Reasoning: The role focuses on business intelligence and metrics without explicit financial reporting, regulatory, or compliance signals typical of high-risk domains.

### collaboration_width
**Manual:** `4`

**Run 1:** `3` ✗
> Quote: "Engage with analysts and scientists to understand problems and translate them into data solutions; Work with developers on data creation aligned with business logic"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct partner groups are explicitly named: analysts, scientists (data scientists), and developers (engineering).

**Run 2:** `3` ✗
> Quote: "analysts; scientists; developers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named collaborating groups are explicitly identified in the responsibilities: analysts, data scientists, and developers.

**Run 3:** `3` ✗
> Quote: "Engage with analysts and scientists to understand problems and translate them into data solutions; Work with developers on data creation aligned with business logic"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named teams are explicitly identified as collaboration partners: analysts, data scientists, and developers.

⚠ **Disagreement**: manual=`4` vs LLM majority=`3`

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: Data Mesh architecture indicates an established, sophisticated data function, while the emphasis on actively developing new products and building self-service capabilities suggests they remain in a growth/scaling phase.

**Run 2:** `mid` ✗
> Quote: "Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: The existing Data Mesh architecture and references to multiple data roles indicate an established function that is evolving and scaling, not greenfield but not yet massive and specialized.

**Run 3:** `mid` ✗
> Quote: "Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: The Data Mesh environment signal indicates an established, sophisticated data infrastructure with multiple existing roles rather than a greenfield or early-stage data function.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `recruiter` ✗
> Quote: "Engage with analysts and scientists to understand problems and translate them into data solutions"
> Verified: ✓ found in JD
> Reasoning: Most responsibilities rely on generic collaboration and ownership language (collaborate, engage, work with, troubleshoot, build) without explaining specific technical context, methodologies, or how the named tools are actually applied.

**Run 2:** `mixed` ✗
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: Technical specificity (data contracts, data mesh architecture, self-service capabilities) indicates hiring manager input, but generic collaboration language and boilerplate action verbs suggest significant recruiter contribution.

**Run 3:** `mixed` ✗
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts; Engage with analysts and scientists to understand problems and translate them into data solutions"
> Verified: ⚠ NOT found verbatim
> Reasoning: Technical specificity with data contracts mixed with generic boilerplate collaboration language suggests contributions from both hiring manager and recruiter.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'mixed']
