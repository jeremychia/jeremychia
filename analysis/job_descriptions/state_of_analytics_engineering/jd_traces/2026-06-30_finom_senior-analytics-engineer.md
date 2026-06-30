# Trace: 2026-06-30_finom_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Finom

**URL:** https://jobs.eu.lever.co/pnlfin/512862cb-695e-4fee-9b44-d95793739f68
**Location:** Spain / Poland / Serbia / Slovenia (Remote)
**Date Posted:** 2026-06-30

---

Senior Analytics Engineer at Finom

Location: Spain / Poland / Serbia / Slovenia (Remote)
Employment Type: Full Time

About Finom:
Finom is an Amsterdam-based fintech startup that recently closed €115 million Series C funding, bringing total capital to approximately $346 million. Their mission focuses on creating integrated financial management solutions for entrepreneurs.

About the Role:
Finom seeks a Senior Analytics Engineer to join their newly formed Data Team building a Data Delivery Platform on Databricks. The role offers significant autonomy in developing data products from scratch in a remote setting across European locations.

Key Responsibilities:
- Developing data warehouse core models that transform Kafka topics into documented, easy-to-use data products
- Collaborating with data engineers on streaming ETL framework development
- Contributing to OpenMetadata data catalog features and maintenance
- Implementing data quality and governance processes
- Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation — partner with data consumers across the business, supporting their daily data needs and turning requirements into reliable, well-documented data products
- Addressing platform-building challenges from inception

Requirements:
- Analytics engineering or analyst experience with data platform projects
- Excellent SQL writing capabilities for analytical work
- Python and PySpark proficiency
- Git and ETL tool expertise (dbt preferred)
- Experience building data products or DWH models on modern platforms like Databricks
- Understanding of streaming pipeline mechanics
- Ability to gather stakeholder requirements and convert to technical solutions
- High autonomy and self-direction
- Banking/fintech background (preferred)

Benefits:
- Stock options available to all employees
- Remote work flexibility across Europe
- Work & Swim Program offering one month in a comfortable corporate apartment in enchanting Cyprus
- Professional development opportunities
- Inclusive workplace culture

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | moderate | high | moderate | 33% | ✗ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | early | mid | early | mid | 33% | ✗ |
| jd_authorship | mixed | mixed | mixed | hiring_manager | 33% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implementing data quality and governance processes"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, governance, and reliable, well-documented data products with no velocity framing present.

**Run 2:** `rigour` ✓
> Quote: "Implementing data quality and governance processes"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, documentation, and reliability with no corresponding velocity signals like fast-paced or rapid delivery.

**Run 3:** `rigour` ✓
> Quote: "Implementing data quality and governance processes"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, and well-documented products with no velocity-focused language, establishing rigour as the primary orientation.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation — partner with data consumers across the business, supporting their daily data needs and turning requirements into reliable, well-documented data products"
> Verified: ✓ found in JD
> Reasoning: Although Finom is fintech, the JD language frames data work as supporting internal analytics and data consumers rather than explicitly linking to financial reporting or regulatory compliance.

**Run 2:** `high` ✓
> Quote: "creating integrated financial management solutions for entrepreneurs"
> Verified: ✓ found in JD
> Reasoning: Fintech is a sector that defaults to high domain risk due to financial and regulatory exposure inherent to the business model.

**Run 3:** `moderate` ✗
> Quote: "creating integrated financial management solutions for entrepreneurs"
> Verified: ✓ found in JD
> Reasoning: While in the fintech sector (high-risk by default), the JD focuses on data infrastructure work without explicit financial reporting, compliance, or regulatory language, placing it at moderate risk.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'moderate']

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Collaborating with data engineers on streaming ETL framework development; Supporting data consumers (ML engineers, analysts, stakeholders)"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct groups: data engineers, ML engineers, and analysts as collaboration partners.

**Run 2:** `3` ✓
> Quote: "data engineers; ML engineers; analysts"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct partner functions as collaboration partners in the responsibilities section.

**Run 3:** `3` ✓
> Quote: "Collaborating with data engineers on streaming ETL framework development; Supporting data consumers (ML engineers, analysts, stakeholders)"
> Verified: ⚠ NOT found verbatim
> Reasoning: Explicitly named collaboration partners are data engineers, ML engineers, and analysts—three distinct teams.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Newly formed Data Team building a Data Delivery Platform on Databricks"
> Verified: ✓ found in JD
> Reasoning: The phrase 'newly formed' indicates a growing team with foundational platform work underway, but the plural 'data engineers' and existing data consumers suggest beyond first-hire stage.

**Run 2:** `early` ✓
> Quote: "newly formed Data Team building a Data Delivery Platform"
> Verified: ✓ found in JD
> Reasoning: The 'newly formed' descriptor combined with 'building' and 'from inception' language signals a data function being established rather than operating at scale.

**Run 3:** `mid` ✗
> Quote: "newly formed Data Team building a Data Delivery Platform on Databricks"
> Verified: ✓ found in JD
> Reasoning: The team is newly formed but has specific modern tools and infrastructure (Databricks, dbt, OpenMetadata) with defined responsibilities, indicating mid-stage rather than early-stage.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'early', 'mid']

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Developing data warehouse core models that transform Kafka topics into documented, easy-to-use data products; Contributing to OpenMetadata data catalog features and maintenance"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical responsibilities (Kafka transformations, OpenMetadata maintenance, DWH models) indicate hiring manager input, while generic collaboration language suggests recruiter contribution.

**Run 2:** `mixed` ✓
> Quote: "Developing data warehouse core models that transform Kafka topics into documented, easy-to-use data products"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about Kafka transformations and warehouse architecture indicates hiring manager input, but other responsibilities use generic collaboration language.

**Run 3:** `hiring_manager` ✗
> Quote: "Developing data warehouse core models that transform Kafka topics into documented, easy-to-use data products"
> Verified: ✓ found in JD
> Reasoning: Specific tool workflows and technical context (Kafka transformation, warehouse models) demonstrate hiring manager knowledge of the actual technical work rather than generic recruiter language.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation — partner with data consumers across the business, supporting their daily data needs and turning requirements into reliable, well-documented data products"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves internal data platform users (ML engineers, analysts) and exists to build infrastructure for the data team itself.

**Run 2:** `internal_data` ✓
> Quote: "Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building data infrastructure and serving internal data team consumers, not external GTM, revenue, or finance functions.

**Run 3:** `internal_data` ✓
> Quote: "Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation"
> Verified: ✓ found in JD
> Reasoning: The role serves internal data consumers and is framed around building a data platform for internal infrastructure, not external commercial, product, or financial audiences.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "The role offers significant autonomy in developing data products from scratch in a remote setting"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly grants 'significant autonomy' and requires 'self-direction' in developing and architecting platform solutions from inception, indicating strategic ownership rather than execution of predefined scope.

**Run 2:** `strategic` ✓
> Quote: "significant autonomy in developing data products from scratch"
> Verified: ✓ found in JD
> Reasoning: The role explicitly offers 'significant autonomy' and involves defining and building platform components 'from inception', establishing strategic direction rather than executing pre-scoped work.

**Run 3:** `strategic` ✓
> Quote: "The role offers significant autonomy in developing data products from scratch"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of significant autonomy to develop products from scratch combined with ownership of platform building indicates strategic direction-setting rather than execution of defined work.
