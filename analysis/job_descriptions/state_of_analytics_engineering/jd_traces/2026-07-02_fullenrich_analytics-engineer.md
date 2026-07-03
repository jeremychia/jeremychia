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

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 5 | 5 | 5 | 5 | 100% | ✓ |
| data_team_maturity | early | early | early | early | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | mixed | commercial | internal_data | mixed | 0% | ✗ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | ai_user | ai_user | ai_user | 100% | ✗ |
| testing_framing |  | tool_listed | responsibility | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, documentation, and data quality as core expectations, with velocity signals appearing only in culture description and bonus qualifications.

**Run 2:** `rigour` ✗
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section explicitly names testing and documentation maintenance as owned responsibilities, establishing quality-first orientation despite the company's rapid-execution culture.

**Run 3:** `rigour` ✗
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize testing, documentation, and rigorous data quality standards as core expectations, with no velocity-oriented language in the primary responsibilities.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Data errors affect business decisions and potentially P&L visibility through Finance and RevOps, but the JD contains no explicit regulatory, compliance, or financial reporting language that would elevate to high risk.

**Run 2:** `moderate` ✓
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: The role touches Finance and RevOps functions indicating business-decision impact, but lacks explicit financial reporting, compliance, or regulatory language typical of high-risk domains.

**Run 3:** `moderate` ✓
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Role serves business operations and SaaS metrics without regulatory, compliance, or mission-critical language that would indicate high financial/compliance risk.

### collaboration_width
**Manual:** `5`

**Run 1:** `5` ✓
> Quote: "Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Five distinct named stakeholder teams are explicitly listed as recipients of data models and metrics.

**Run 2:** `5` ✓
> Quote: "Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names five distinct business functions as stakeholders and metric consumers that the role serves.

**Run 3:** `5` ✓
> Quote: "Finance; Marketing; RevOps; Sales; Support"
> Verified: ✓ found in JD
> Reasoning: JD explicitly names five distinct business functions as stakeholder partners requiring reliable data access.

### data_team_maturity
**Manual:** `early`

**Run 1:** `early` ✓
> Quote: "This is FullEnrich's inaugural dedicated data hire"
> Verified: ✓ found in JD
> Reasoning: The first dedicated data hire is the definitive early-stage signal, despite some existing ad-hoc infrastructure already in place.

**Run 2:** `early` ✓
> Quote: "This is FullEnrich's inaugural dedicated data hire"
> Verified: ✓ found in JD
> Reasoning: Despite existing technical infrastructure, the role is explicitly positioned as the first dedicated data hire responsible for building foundational systems, indicating early-stage data function establishment.

**Run 3:** `early` ✓
> Quote: "This is FullEnrich's inaugural dedicated data hire"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly the company's first dedicated data hire, signaling early-stage data function despite existing infrastructure already in place.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical contexts (tool names paired with specific use cases) that only someone performing this job would know to specify.

**Run 2:** `hiring_manager` ✓
> Quote: "Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot"
> Verified: ✓ found in JD
> Reasoning: The responsibility specifies precise technical application and business context (reverse ETL to particular systems) that demonstrates hands-on authorship rather than templated language.

**Run 3:** `hiring_manager` ✓
> Quote: "Conduct analytical work addressing business problems including provider cost/margin analysis, activation scoring, credit consumption pattern analysis"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain specific analytical domains and domain-specific methods only someone who has performed this work would articulate.

### stakeholder_orientation
**Manual:** `mixed`

**Run 1:** `commercial` ✗
> Quote: "Conduct analytical work addressing business problems including provider cost/margin analysis, activation scoring, credit consumption pattern analysis"
> Verified: ✓ found in JD
> Reasoning: The analytical work specified is explicitly revenue operations work (cost/margin analysis, activation scoring), with the role reporting directly to RevOps.

**Run 2:** `internal_data` ✗
> Quote: "building foundational systems for organizational growth"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is establishing and maintaining the data infrastructure foundation itself, with business analytical work secondary; the infrastructure serves other teams but internal data platform building is the core mission.

**Run 3:** `mixed` ✓
> Quote: "Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Role serves Finance, RevOps/commercial, Marketing, Sales, and operations with equal emphasis across multiple business functions rather than a single primary audience.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`commercial`

⚠ **LLM inconsistency**: runs gave ['commercial', 'internal_data', 'mixed']

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "owning the data layer end-to-end while building foundational systems for organizational growth"
> Verified: ✓ found in JD
> Reasoning: The role is framed around establishing and defining the data function as the inaugural data hire, not executing against pre-defined priorities.

**Run 2:** `strategic` ✓
> Quote: "owning the data layer end-to-end while building foundational systems for organizational growth"
> Verified: ✓ found in JD
> Reasoning: The role carries end-to-end ownership and responsibility for defining foundational systems, reinforced by the culture statement emphasizing autonomous decision-making with full scope ownership.

**Run 3:** `strategic` ✓
> Quote: "owning the data layer end-to-end while building foundational systems for organizational growth"
> Verified: ✓ found in JD
> Reasoning: Role is framed around ownership and building foundational systems with explicit mention of autonomous decision-making and full scope ownership in the culture section.

### ai_role
**Manual:** ``

**Run 1:** `ai_user` ✗
> Quote: "Active use of AI tools (Cursor, Claude) for work augmentation"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly requires the candidate to use AI coding tools (Cursor, Claude) to enhance their own productivity.

**Run 2:** `ai_user` ✗
> Quote: "Active use of AI tools (Cursor, Claude) for work augmentation"
> Verified: ✓ found in JD
> Reasoning: The candidate is explicitly expected to use AI coding tools like Cursor and Claude as personal productivity tools to accelerate their own work.

**Run 3:** `ai_user` ✗
> Quote: "Active use of AI tools (Cursor, Claude) for work augmentation"
> Verified: ✓ found in JD
> Reasoning: Candidate is explicitly required to actively use AI coding tools like Cursor and Claude Code to accelerate their own analytical and development work.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

### testing_framing
**Manual:** ``

**Run 1:** `tool_listed` ✗
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing appears as a responsibility action but is framed as maintaining standards rather than defining or owning a testing strategy.

**Run 2:** `responsibility` ✗
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing and documentation are framed as responsibilities the candidate owns and executes using action verbs, not merely as tools listed in a requirements section.

**Run 3:** `responsibility` ✗
> Quote: "Write tests and maintain documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing is framed as an owned responsibility using an action verb, making the candidate accountable for defining and implementing test practices.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'responsibility', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "rigorous data quality standards"
> Verified: ✓ found in JD
> Reasoning: Data quality appears as a core expectation through reliability and standards language, but the framing centers on operational reliability rather than preventing bad data reaching stakeholders or regulatory exposure.

**Run 2:** `moderate` ✗
> Quote: "ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Operational reliability is a stated concern (ensuring reliable access echoes SLO thinking) but secondary to delivery of data infrastructure; no compliance, regulatory, or stakeholder-trust risk framing is present.

**Run 3:** `moderate` ✗
> Quote: "ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality standards are concerns, but framed around business access and SaaS execution rather than compliance, regulatory, or stakeholder trust risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
