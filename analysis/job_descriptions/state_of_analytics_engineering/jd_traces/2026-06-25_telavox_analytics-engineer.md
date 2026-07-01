# Trace: 2026-06-25_telavox_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Telavox
**URL:** https://career.telavox.com/jobs/7661845-analytics-engineer

**Company:** Telavox
**Location:** Malmö
**Salary:** Not stated
**Date saved:** 2026-06-25

---

## Role summary

Telavox seeks an Analytics Engineer to manage the complete lifecycle of data, from raw backend events to executive dashboards. The role emphasises trustworthy data and making information findable and useful throughout the organisation.

## Key responsibilities

- Own the dbt project, transforming raw data into staged, modelled, documented, and tested tables across bronze, silver, and gold layers
- Design and evolve data marts encoding Telavox business logic
- Operate CDC pipelines, monitor health, manage failures, and optimise BigQuery costs and performance
- Build and maintain semantic layers powering self-service and agentic analytics
- Partner with analysts and stakeholders to create durable data products

## Required qualifications

- Advanced SQL and strong dbt fundamentals
- Solid BigQuery knowledge including partitioning and performance tuning
- Experience building dimensional models or analytical schemas
- Ability to translate business questions into data models
- Working Python proficiency
- Fluent English (Swedish preferred)

## Preferred experience

- CDC concepts
- Fivetran
- Semantic layers (Cube or MetricFlow)

## Classification

| Field | Value |
|---|---|
| Seniority | mid |
| Role type | analytics_engineering_bi |
| JD authorship | hiring_manager |
| Greenfield vs fix | fix_scale |
| Velocity vs rigour | rigour |
| Domain risk | moderate |
| Collaboration width | 1 |
| Data team maturity | mid |
| Urgency | standard |
| Language gate | soft — Swedish |
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 1 | 1 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | mixed | strategic | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "The role emphasises trustworthy data and making information findable and useful throughout the organisation."
> Verified: ✓ found in JD
> Reasoning: The role summary explicitly prioritizes trustworthy data and the responsibilities detail documented, tested tables and durable data products—strong rigour signals with no velocity language present.

**Run 2:** `rigour`
> Quote: "documented, and tested tables"
> Verified: ✓ found in JD
> Reasoning: The emphasis on documentation and testing reflects rigour-focused values with no velocity-oriented language present.

**Run 3:** `rigour`
> Quote: "transforming raw data into staged, modelled, documented, and tested tables"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize documented, tested, and durable data products with no velocity signals present.

### domain_risk

**Run 1:** `moderate`
> Quote: "Build and maintain semantic layers powering self-serve and agentic analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role supports internal business intelligence and analytics decision-making rather than regulatory compliance or financial reporting, indicating moderate risk.

**Run 2:** `moderate`
> Quote: "executive dashboards"
> Verified: ✓ found in JD
> Reasoning: Executive dashboards indicate business decision-making impact, but the JD lacks explicit financial, compliance, or regulatory language typical of high-risk domains.

**Run 3:** `moderate`
> Quote: "manage the complete lifecycle of data, from raw backend events to executive dashboards"
> Verified: ✓ found in JD
> Reasoning: Data affects executive-level business decisions but the JD contains no financial reporting, compliance, or regulatory language.

### collaboration_width

**Run 1:** `1`
> Quote: "analysts"
> Verified: ✓ found in JD
> Reasoning: Only analysts are named as a distinct collaborative partner group; stakeholders and other generic references do not count.

**Run 2:** `1`
> Quote: "analysts"
> Verified: ✓ found in JD
> Reasoning: Only 'analysts' is a named partner team; 'stakeholders' is generic language and does not count.

**Run 3:** `1`
> Quote: "analysts"
> Verified: ✓ found in JD
> Reasoning: Only 'analysts' counts as a named role cohort; 'stakeholders' is generic and does not meet the counting criteria.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Own the dbt project, transforming raw data into staged, modelled, documented, and tested tables across bronze, silver, and gold layers"
> Verified: ✓ found in JD
> Reasoning: Named tools deployed in operations (dbt, BigQuery, CDC, semantic layers) indicate an established data function scaling and evolving, not early-stage or fully mature.

**Run 2:** `mid`
> Quote: "Design and evolve data marts encoding Telavox business logic"
> Verified: ✓ found in JD
> Reasoning: The word 'evolve' indicates an existing data function with established infrastructure being improved rather than built from scratch.

**Run 3:** `mid`
> Quote: "Operate CDC pipelines, monitor health, manage failures, and optimise BigQuery costs and performance"
> Verified: ✓ found in JD
> Reasoning: The JD describes operating established tools (dbt, CDC, BigQuery, semantic layers) in an existing function, not a greenfield build or highly mature multi-team structure.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Own the dbt project, transforming raw data into staged, modelled, documented, and tested tables across bronze, silver, and gold layers"
> Verified: ✓ found in JD
> Reasoning: The bronze/silver/gold medallion architecture pattern and specific operational details (CDC pipelines, BigQuery optimization, dimensional models) reflect hands-on data engineering expertise.

**Run 2:** `hiring_manager`
> Quote: "transforming raw data into staged, modelled, documented, and tested tables across bronze, silver, and gold layers"
> Verified: ✓ found in JD
> Reasoning: Specific data modeling methodology (bronze/silver/gold medallion pattern) and precise tool context demonstrate domain expertise only found in hiring managers.

**Run 3:** `hiring_manager`
> Quote: "Own the dbt project, transforming raw data into staged, modelled, documented, and tested tables across bronze, silver, and gold layers"
> Verified: ✓ found in JD
> Reasoning: The specific mention of dbt methodology, bronze/silver/gold layers, CDC pipeline operations, and BigQuery optimization indicates hands-on domain knowledge from someone who does this work.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Build and maintain semantic layers powering self-serve and agentic analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's primary focus is building data infrastructure and platforms for internal analytics consumers, not commercial, product, or finance stakeholders.

**Run 2:** `internal_data`
> Quote: "Build and maintain semantic layers powering self-service and agentic analytics"
> Verified: ✓ found in JD
> Reasoning: The explicit focus on self-service analytics infrastructure and semantic layers positions this role as serving data consumers and the data function itself.

**Run 3:** `internal_data`
> Quote: "Build and maintain semantic layers powering self-serve and agentic analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's primary purpose is building analytics infrastructure (dbt models, data marts, semantic layers) that serves internal data consumers (analysts, data engineers).

### autonomy_level

**Run 1:** `strategic`
> Quote: "Design and evolve data marts encoding Telavox business logic"
> Verified: ✓ found in JD
> Reasoning: The role designs and owns the data architecture rather than executing scoped work, with strategic responsibility for how analytics is delivered.

**Run 2:** `mixed`
> Quote: "Own the dbt project"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of the data platform (own, design, evolve) with operational execution responsibilities (operate, monitor, maintain).

**Run 3:** `strategic`
> Quote: "Own the dbt project"
> Verified: ✓ found in JD
> Reasoning: The role explicitly owns and designs key data infrastructure (dbt project, data marts with business logic, semantic layers) rather than executing pre-defined direction.

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'strategic']

### ai_role
**Run 1:** `ai_enabler` ✓
> Quote: "Build and maintain semantic layers powering self-serve and agentic analytics"
> Reasoning: Builds semantic infrastructure consumed by agentic (AI-driven) analytics.

**Run 2:** `ai_enabler` ✓
> Quote: "Build and maintain semantic layers powering self-serve and agentic analytics"
> Reasoning: Candidate builds semantic layers that AI agents consume for agentic analytics.

**Run 3:** `ai_enabler` ✓
> Quote: "Build and maintain semantic layers powering self-serve and agentic analytics"
> Reasoning: Semantic layers purpose-built to power agentic analytics indicates infrastructure built for AI consumption.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Own the dbt project, transforming raw data into staged, modeled, documented, and tested tables"
> Reasoning: Owns testing and documentation as part of core dbt project responsibility.

**Run 2:** `responsibility` ✓
> Quote: "Own the dbt project, transforming raw data into staged, modeled, documented, and tested tables"
> Reasoning: Candidate owns end-to-end dbt project with explicit testing and documentation responsibility.

**Run 3:** `responsibility` ✓
> Quote: "Own the dbt project, transforming raw data into staged, modeled, documented, and tested tables"
> Reasoning: Explicit ownership of dbt project includes tested tables as a deliverable, indicating ownership of quality practice.


### loss_aversion_framing
**Run 1:** `high` ✗
> Quote: "trustworthy data and making information findable and useful throughout the organization"
> Reasoning: Trust and data reliability dominate framing as primary organizational concern, not just delivery.

**Run 2:** `moderate` ✓
> Quote: "trustworthy data and making information findable and useful throughout the organization"
> Reasoning: Emphasis on trustworthy data and stakeholder access frames quality as operational reliability concern.

**Run 3:** `moderate` ✓
> Quote: "trustworthy data and making information findable and useful throughout the organization"
> Reasoning: Trustworthiness framing suggests operational reliability and data quality concern, but balanced with utility rather than compliance-dominant.

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']
