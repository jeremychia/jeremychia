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
| data_team_maturity | mature | mid | mature | mid | 33% | ✗ |
| jd_authorship | hiring_manager | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | mixed | mixed | mixed | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit rigour signals (quality, trustworthiness, data contracts) with no competing velocity language like speed or iteration.

**Run 2:** `rigour` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, trustworthiness, data contracts, attention to detail, and expert-level skills throughout the responsibilities, with no velocity language present.

**Run 3:** `rigour` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly prioritizes data quality, trustworthiness, and data contracts as core expectations with no counterbalancing velocity language.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Design solutions for KPIs and business metrics"
> Verified: ✓ found in JD
> Reasoning: Business metrics suggest decision-making impact, but no explicit financial reporting, compliance, or regulatory language that would elevate to high risk.

**Run 2:** `moderate` ✓
> Quote: "Own the quality, availability, and trustworthiness of data"
> Verified: ✓ found in JD
> Reasoning: While data errors impact business operations in a ride-hailing platform, the JD lacks explicit financial reporting, compliance, or regulatory language that would indicate high risk.

**Run 3:** `moderate` ✓
> Quote: "Design solutions for KPIs and business metrics"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational metrics and business decision support rather than financial reporting, regulatory compliance, or mission-critical consequences.

### collaboration_width
**Manual:** `4`

**Run 1:** `3` ✗
> Quote: "Engage with analysts and scientists to understand problems and translate them into data solutions; Work with developers on data creation"
> Verified: ⚠ NOT found verbatim
> Reasoning: Explicitly names three distinct groups: analysts, data scientists, and developers/engineers.

**Run 2:** `3` ✗
> Quote: "analysts and scientists; developers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct collaboration partners: analysts, scientists (data scientists), and developers.

**Run 3:** `3` ✗
> Quote: "analysts and scientists; developers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names three distinct role cohorts as collaboration partners: analysts, data scientists (referred to as scientists), and developers.

⚠ **Disagreement**: manual=`4` vs LLM majority=`3`

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: A Data Mesh architecture indicates an established, distributed data function with existing infrastructure and multiple teams, beyond early-stage but not at massive scale.

**Run 2:** `mature` ✓
> Quote: "Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: The Data Mesh architecture is an advanced pattern deployed at scale, combined with a sophisticated tech stack (Databricks, Airflow, Kafka, Debezium), indicating an established mature data organization.

**Run 3:** `mid` ✗
> Quote: "Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: The mention of an existing Data Mesh architecture indicates an established organizational pattern, but focus on developing new data products suggests active growth rather than full maturity.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'mature', 'mid']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: Data contracts and quality methodology reflect specific practitioner knowledge, but balanced with generic collaboration verbs like "engage" and "translate" elsewhere.

**Run 2:** `mixed` ✗
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts; Design solutions for KPIs and business metrics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains specific technical concepts (Data Mesh, data contracts, SparkSQL) alongside generic action verbs like engage and collaborate, indicating input from both hiring manager and recruiter.

**Run 3:** `mixed` ✗
> Quote: "Expert level of SQL (especially SparkSQL) and experience in building data pipelines; Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines specific technical expectations (SQL/SparkSQL proficiency, data pipelines, data contracts) with generic stakeholder collaboration boilerplate.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Build an environment where self-service capabilities are available for analysts and data consumers"
> Verified: ✓ found in JD
> Reasoning: The role serves the data platform itself and internal data consumers (analysts, scientists, developers), not external commercial, product, or finance functions.

**Run 2:** `internal_data` ✗
> Quote: "Build an environment where self-serve capabilities are available for analysts and data consumers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role primarily serves the data function itself—building data products, infrastructure, and self-serve capabilities for analysts and data professionals rather than external commercial, product, or finance teams.

**Run 3:** `internal_data` ✗
> Quote: "Build an environment where self-service capabilities are available for analysts and data consumers"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves internal data consumers and analysts through platform and infrastructure work rather than commercial, product, or finance audiences.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment"
> Verified: ✓ found in JD
> Reasoning: Combines strategic development and ownership of data products with collaborative execution supporting analysts and scientists in a shared environment.

**Run 2:** `mixed` ✗
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership of data quality and design decisions while also executing in service of the data function by engaging with teams to translate their problems into solutions.

**Run 3:** `mixed` ✗
> Quote: "Own the quality, availability, and trustworthiness of data; Design solutions for KPIs and business metrics; Build an environment where self-service capabilities are available"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic ownership of data quality and infrastructure design with execution-focused troubleshooting and collaboration responsibilities.

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

### ai_role
**Run 1:** `none` ✓
> Quote: "Design solutions for KPIs and business metrics"
> Reasoning: No AI signals present; role focuses on standard data engineering and product development without AI tools, infrastructure, or AI-first practices.

**Run 2:** `none` ✓
> Quote: "develop new data products within a Data Mesh environment"
> Reasoning: No AI tool usage or infrastructure-for-AI signals; standard data product development work without AI-specific framing.

**Run 3:** `none` ✓
> Quote: "develop new data products within a Data Mesh environment"
> Reasoning: No mention of AI tool usage or infrastructure building; standard data engineering expected


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Reasoning: Explicit ownership responsibility verb 'own' paired with quality checks and data contracts indicates candidate owns quality practice.

**Run 2:** `responsibility` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Reasoning: Explicit ownership verb with defined mechanisms (quality checks, data contracts); candidate owns quality practice.

**Run 3:** `responsibility` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Reasoning: Explicit ownership verb combined with quality/data contracts shows responsibility for quality practices and data governance


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Own the quality, availability, and trustworthiness of data"
> Reasoning: Operational reliability concerns (quality, availability, trustworthiness) emphasized without explicit regulatory or compliance dominance.

**Run 2:** `moderate` ✓
> Quote: "Own the quality, availability, and trustworthiness of data"
> Reasoning: Operational reliability and trustworthiness concerns present, but no compliance or regulatory language.

**Run 3:** `moderate` ✓
> Quote: "Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"
> Reasoning: Trustworthiness and data contracts signal governance concerns; balanced with operational availability suggests operational + governance focus

