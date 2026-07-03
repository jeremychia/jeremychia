# Trace: 2026-07-02_sii-poland_data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data Analytics Engineer (f/m/x) — Sii Poland

**URL:** https://sii.pl/en/job-ads/id/37337/?sii_source=10#apply-contact-form
**Location:** Poland (Remote/Hybrid/Office)
**Date Posted:** 2026-07-02

---

# Data Analytics Engineer (f/m/x) - Senior Level

Company: Sii Poland
Location: Multiple locations in Poland (Remote, Hybrid, or Office options available)
Salary: Not stated

## Overview
Sii is recruiting an Analytics Engineer for a strategic fintech project based in Copenhagen. The role involves building and scaling critical data models that support decision-making across credit, payments, and fraud/AML domains.

## Key Responsibilities
- Build and maintain core data models using dbt for critical reporting
- Partner with stakeholders, Data Engineers, and Analysts on requirements
- Work collaboratively across technical and non-technical teams
- Contribute to the semantic layer (LookML) for consistent reporting
- Ensure data quality through testing, monitoring, and documentation
- Support reliable data workflows using orchestration tools like Airflow
- Uphold analytics engineering practices including code reviews
- Balance work across multiple data domains with adaptability

## Requirements
Must-Have:
- Min. 5 years of hands-on experience with dbt and modern cloud data warehouses (BigQuery)
- SQL proficiency and experience with layered model architecture
- Ability to translate unclear business requirements into clean solutions
- Git-based workflows and CI/CD familiarity
- Strong ownership mindset for business-critical data
- Comfort in high engineering/governance standard environments
- English language proficiency
- Fluent Polish required and residence in Poland mandatory

Nice-to-Have:
- Apache Airflow experience
- AML domain knowledge

## Tech Stack
Required: dbt, SQL, Git, BigQuery, LookML, Looker, Data Governance, Data Modeling
Optional: Apache Airflow, AML

Job no. JOB-22E63

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 3 | 2 | 2 | 2 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | finance | 33% | ✓ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | high | moderate | moderate | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit signals emphasize testing, quality, governance, and reliability with no velocity language present.

**Run 2:** `rigour` ✓
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, monitoring, and governance standards as core expectations with no velocity signals present.

**Run 3:** `rigour` ✓
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, monitoring, governance standards, and reliable workflows as core expectations with no counterbalancing velocity signals.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "strategic fintech project based in Copenhagen. The role involves building and scaling critical data models that support decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: Fintech sector combined with credit, payments, and regulatory fraud/AML domains represent direct financial and compliance risk.

**Run 2:** `high` ✓
> Quote: "credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: Fintech with explicit focus on credit risk, payment systems, and AML compliance where data errors directly affect regulatory and financial outcomes.

**Run 3:** `high` ✓
> Quote: "critical data models that support decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: Credit decisions, payments processing, and fraud/AML are inherently high-risk financial and regulatory domains where data errors have direct compliance and financial consequences.

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: Two named distinct partner teams identified (Data Engineers and Analysts); generic stakeholder reference does not count.

**Run 2:** `2` ✗
> Quote: "Data Engineers; Analysts"
> Verified: ✓ found in JD
> Reasoning: Two explicitly named teams identified as collaboration partners: Data Engineers and Analysts.

**Run 3:** `2` ✗
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: Two explicitly named partner teams are identified: Data Engineers and Analysts.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support reliable data workflows using orchestration tools like Airflow"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, LookML, Airflow) indicate existing infrastructure being maintained and scaled rather than built from zero.

**Run 2:** `mid` ✓
> Quote: "Build and maintain core data models using dbt for critical reporting"
> Verified: ✓ found in JD
> Reasoning: References existing named tools (dbt, LookML, Airflow) requiring maintenance and multiple data roles, indicating established function growing beyond early stage.

**Run 3:** `mid` ✓
> Quote: "Build and maintain core data models using dbt for critical reporting"
> Verified: ✓ found in JD
> Reasoning: Named tools and infrastructure already exist (dbt, Airflow, LookML, Looker) and the role maintains/scales them rather than building from scratch, indicating a developing data function.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain technical specificity (dbt, LookML, Airflow, specific domains) that indicates domain expertise from someone actively doing this work.

**Run 2:** `hiring_manager` ✓
> Quote: "Build and maintain core data models using dbt for critical reporting"
> Verified: ✓ found in JD
> Reasoning: Names specific tools with precise context about domains and infrastructure, alongside domain knowledge of credit/payments/AML workflows, indicating technical author experience.

**Run 3:** `hiring_manager` ✓
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain technical specificity about tool usage in precise contexts (semantic layer for LookML, models with dbt for reporting, Airflow orchestration) that only comes from someone doing this work.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: Role primarily serves data platform consumers (other analysts and engineers) building and maintaining analytics infrastructure.

**Run 2:** `internal_data` ✓
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: Role emphasizes building analytics infrastructure (semantic layer, analytics engineering practices) for internal data consumers rather than serving external business stakeholders.

**Run 3:** `finance` ✗
> Quote: "decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: The primary audience for the role's work is financial and compliance decision-makers, as credit, payments, and fraud/AML are inherently finance and risk domains.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'finance']

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: Role receives scoped requirements from stakeholders and executes delivery; no strategic verbs like define, establish, or lead appear.

**Run 2:** `execution` ✓
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: The role receives requirements from external parties and partners to deliver within established patterns, rather than setting strategy or defining priorities.

**Run 3:** `execution` ✓
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: The role partners with stakeholders to understand requirements rather than defining strategic direction, and executes against scoped work set by business domains.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: JD lists specific technical stack (dbt, SQL, BigQuery, LookML) but contains no mention of AI tools, coding assistants, or AI-ready data infrastructure.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI coding tools, AI-enabled infrastructure, or candidate AI skill expectations anywhere in the JD.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, AI-assisted coding, or AI data infrastructure appears anywhere in the job description.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as core responsibilities the candidate owns using the action verb Ensure.

**Run 2:** `responsibility` ✗
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as core responsibilities the candidate owns through the action verb 'Ensure' rather than as a tool to use.

**Run 3:** `responsibility` ✗
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality through testing is framed as a core responsibility owned by the candidate via the action verb 'ensure', not merely a tool they should know.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `high` ✗
> Quote: "Comfort in high engineering/governance standard environments"
> Verified: ✓ found in JD
> Reasoning: Explicit governance and compliance emphasis combined with fintech context and repeated critical framing indicates high risk aversion to regulatory failure and bad data reaching stakeholders.

**Run 2:** `moderate` ✗
> Quote: "Comfort in high engineering/governance standard environments"
> Verified: ✓ found in JD
> Reasoning: Governance and data criticality are emphasized multiple times, but without explicit compliance or regulatory risk language; focus is operational reliability rather than preventing regulatory exposure.

**Run 3:** `moderate` ✗
> Quote: "Comfort in high engineering/governance standard environments"
> Verified: ✓ found in JD
> Reasoning: Governance and operational reliability are concerns (testing, monitoring, fraud/AML domains), but the primary framing is about building and scaling critical models rather than preventing regulatory failure.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']
