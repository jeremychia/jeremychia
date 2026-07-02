# Trace: 2026-07-02_fullenrich_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — FullEnrich

**URL:** https://www.linkedin.com/jobs/view/analytics-engineer-at-fullenrich-4404764125/
**Location:** Paris, France
**Date Posted:** 2026-07-02

---

# Analytics Engineer at FullEnrich

Location: Paris, Ile-de-France, France
Salary: Not stated
Seniority Level: Entry level (as listed on LinkedIn, though role is described as a senior first data hire)
Employment Type: Full-time

## Company Overview
FullEnrich aggregates 20+ data providers into a single waterfall system to deliver contact enrichment services. The company serves 3,500+ customers including major firms like AWS and Shopify, and operates profitably.

## Role Summary
This is FullEnrich's inaugural dedicated data hire. The position bridges data infrastructure and business operations, with the successful candidate reporting directly to Simon (RevOps). The role involves owning the data layer end-to-end while building foundational systems for organizational growth.

## Key Responsibilities
- Maintain and enhance the existing dbt/BigQuery data stack
- Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams
- Create self-serve dashboards using Basedash for metric consumption
- Conduct analytical work addressing business problems including provider cost/margin analysis, activation scoring, credit consumption pattern analysis
- Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot
- Write tests and maintain documentation standards

## Required Experience & Skills
- 4+ years in analytics engineering, data engineering, or senior data analysis
- Proven ability conducting end-to-end analyses for demanding stakeholders
- Strong SQL proficiency in BigQuery or equivalent platforms
- Active use of AI tools (Cursor, Claude) for work augmentation
- Solid understanding of SaaS metrics (ARR, churn, activation, unit economics)
- Builder mindset preferring automation over repetition
- Comfort with ambiguity and rigorous data quality standards

## Bonus Qualifications
- BigQuery-specific expertise (materialized views, partitioning, clustering)
- Segment platform familiarity as data source and reverse ETL tool
- Experience in fast-moving startup environments

## Technology Stack
Data Warehouse: BigQuery
Transformation: dbt Cloud
Ingestion: Fivetran and Airbyte
Reverse ETL: Segment
BI Tool: Basedash (LLM-native)
Development: Cursor or Claude Code with AI assistance

## Hiring Process
1. Initial call (45 minutes) with Simon
2. Technical case study (1 hour)
3. Founders' interview

Culture: high-ownership, entrepreneurial approach with rapid execution, business-focused outcomes, and autonomous decision-making with full scope ownership.

---
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
| stakeholder_orientation | mixed | commercial | commercial | 33% |
| autonomy_level | strategic | strategic | strategic | 100% |
| ai_role | ai_user | ai_user | ai_user | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Rigour signals (testing, documentation, data quality standards) appear consistently throughout and outnumber velocity signals (rapid execution, startup pace).

**Run 2:** `rigour`
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, documentation, and rigorous data quality standards as core expectations, outweighing the secondary mention of 'rapid execution' in the culture description.

**Run 3:** `rigour`
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: The JD emphasises testing, documentation, and 'rigorous data quality standards' (appearing twice in required experience) more heavily than velocity signals, which appear only in bonus qualifications.

### domain_risk

**Run 1:** `moderate`
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Role serves financial and operational stakeholders with direct business impact, but lacks explicit regulatory, compliance, or audit language.

**Run 2:** `moderate`
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: While the role serves Finance and RevOps teams including cost/margin analysis, the JD contains no language about financial reporting, regulatory compliance, or audit—indicating internal operational reporting risk rather than high-stakes financial/compliance risk.

**Run 3:** `moderate`
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Data errors affect internal business decisions across multiple functions but lack regulatory, compliance, or P&L reporting language typical of high-risk domains.

### collaboration_width

**Run 1:** `5`
> Quote: "Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Five distinct named internal functions are explicitly identified as stakeholders receiving metrics and analytical outputs.

**Run 2:** `5`
> Quote: "Finance; Marketing; RevOps; Sales; Support"
> Verified: ⚠ NOT found verbatim
> Reasoning: Five distinct named functions are explicitly mentioned as stakeholders requiring analytics access in the responsibilities section.

**Run 3:** `5`
> Quote: "Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Five distinct named functions are explicitly listed as audiences for data models and metrics.

### data_team_maturity

**Run 1:** `early`
> Quote: "This is FullEnrich's inaugural dedicated data hire"
> Verified: ✓ found in JD
> Reasoning: Despite existing dbt/BigQuery infrastructure, the inaugural nature of this hire and explicit focus on building foundational systems signals data function establishment rather than scaling.

**Run 2:** `early`
> Quote: "This is FullEnrich's inaugural dedicated data hire."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly identifies this as a first-time dedicated data hire with a mission to build foundational systems, clearly signaling an early-stage data function despite existing infrastructure.

**Run 3:** `early`
> Quote: "This is FullEnrich's inaugural dedicated data hire"
> Verified: ✓ found in JD
> Reasoning: Despite existing dbt/BigQuery infrastructure, the data organisation is being established with this first dedicated hire, placing it in the early stage of team formation.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot"
> Verified: ✓ found in JD
> Reasoning: Specific named tools with precise application context (dbt/BigQuery, Basedash, reverse ETL targets) and business problems (activation scoring, credit consumption patterns) indicate hands-on technical knowledge.

**Run 2:** `hiring_manager`
> Quote: "Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific operational workflows (reverse ETL to named CRM systems), specific analytical domains (provider cost/margin analysis, activation scoring), and precise tool stack context that only someone managing this workflow would describe.

**Run 3:** `hiring_manager`
> Quote: "Conduct analytical work addressing business problems including provider cost/margin analysis, activation scoring, credit consumption pattern analysis"
> Verified: ✓ found in JD
> Reasoning: The JD specifies exact analytical problems (cost/margin, activation scoring) and named tools (dbt, BigQuery, Basedash, Intercom, HubSpot) with precise use cases that only someone performing this work would define.

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize both commercial stakeholders (RevOps, Sales, Marketing) and finance with equal weight across the role scope.

**Run 2:** `commercial`
> Quote: "reporting directly to Simon (RevOps)"
> Verified: ✓ found in JD
> Reasoning: The role reports to a RevOps stakeholder (Revenue Operations), and responsibilities include reverse ETL to customer-facing systems (Intercom, HubSpot), establishing commercial/GTM as the primary audience.

**Run 3:** `commercial`
> Quote: "reporting directly to Simon (RevOps)"
> Verified: ✓ found in JD
> Reasoning: The role reports to Revenue Operations and focuses on commercial metrics (cost/margin analysis, activation scoring), establishing RevOps as the primary stakeholder.

⚠ **LLM inconsistency**: runs gave ['mixed', 'commercial', 'commercial']

### autonomy_level

**Run 1:** `strategic`
> Quote: "owning the data layer end-to-end while building foundational systems for organizational growth"
> Verified: ✓ found in JD
> Reasoning: Ownership and establishment language combined with culture emphasizing autonomous decision-making signal responsibility to define the data function direction.

**Run 2:** `strategic`
> Quote: "owning the data layer end-to-end while building foundational systems for organizational growth"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly framed as building and defining the data function (first dedicated hire), not receiving priorities from others, which constitutes strategic ownership of a domain.

**Run 3:** `strategic`
> Quote: "owning the data layer end-to-end while building foundational systems"
> Verified: ✓ found in JD
> Reasoning: The role owns the complete data layer and builds foundational systems, reinforced by culture language stating 'autonomous decision-making with full scope ownership'.

### ai_role

**Run 1:** `ai_user`
> Quote: "Active use of AI tools (Cursor, Claude) for work augmentation"
> Verified: ✓ found in JD
> Reasoning: Candidate is explicitly required to actively use AI coding assistants as a core part of work execution.

**Run 2:** `ai_user`
> Quote: "Active use of AI tools (Cursor, Claude) for work augmentation"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly requires the candidate to actively use AI coding tools (Cursor, Claude Code) to accelerate their own development work.

**Run 3:** `ai_user`
> Quote: "Active use of AI tools (Cursor, Claude) for work augmentation"
> Verified: ✓ found in JD
> Reasoning: Required experience explicitly expects candidates to actively use AI coding tools to accelerate their own analytical and development work.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing appears in responsibilities as an action to execute, reinforced by emphasis on rigorous data quality standards as a core expectation.

**Run 2:** `responsibility`
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing and documentation are framed as explicit responsibilities with action verbs, indicating the candidate owns these practices rather than merely listing testing tools.

**Run 3:** `responsibility`
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing appears as an owned responsibility with an action verb ('Write'), not as a tool listed in a skill requirement.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality are valued concerns, but secondary to delivery framing; absent regulatory or stakeholder-trust language.

**Run 2:** `moderate`
> Quote: "rigorous data quality standards"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality are concerns (ensuring reliable access, rigorous standards), but the overall framing emphasizes building and rapid execution rather than preventing compliance or stakeholder trust failures.

**Run 3:** `moderate`
> Quote: "rigorous data quality standards"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are clearly expected (mentioned twice), but the framing emphasises operational capability rather than regulatory compliance or risk catastrophe prevention.
