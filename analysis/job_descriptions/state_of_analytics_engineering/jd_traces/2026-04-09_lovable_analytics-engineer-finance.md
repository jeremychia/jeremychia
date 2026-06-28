# Trace: 2026-04-09_lovable_analytics-engineer-finance

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer - Finance — Lovable

**URL:** https://jobs.ashbyhq.com/lovable/081be99e-95bf-4992-9cf2-d16371635ac1
**Location:** Stockholm, Sweden
**Employment Type:** Full Time
**Salary:** Not listed

---

## Key Responsibilities

- Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics
- Establish foundational tables for monthly/annual recurring revenue, churn analysis, and revenue patterns
- Oversee data ingestion from Stripe, billing platforms, and payment processors
- Verify data consistency across systems and reporting layers
- Document business logic for financial metrics including revenue recognition and deferred income
- Implement quality assurance protocols for financial data
- Collaborate with Finance to convert requirements into structured data solutions

---

## Required Qualifications

- Knowledge of subscription economy metrics (MRR, ARR, churn, LTV)
- Background with payment platforms like Stripe or Chargebee
- SQL and dbt expertise including data modeling and testing
- Understanding of dimensional modeling and semantic layers
- Experience with cloud data warehouses (Snowflake, BigQuery, Redshift, Databricks)
- Familiarity with BI platforms (Looker, Tableau, Power BI, Metabase)
- Meticulous attention to financial data accuracy

---

## Preferred / Bonus Skills

Not listed in the posting.

---

## Benefits

Not specified in the posting.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 1 | 1 | 1 | 1 | 100% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | hiring_manager | hiring_manager | hiring_manager | 100% | ✗ |
| stakeholder_orientation |  | finance | finance | finance | 100% | ✗ |
| autonomy_level |  | execution | execution | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data accuracy, consistency verification, and QA protocols without any mention of speed or rapid iteration, indicating a rigour-focused orientation.

**Run 2:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasises quality assurance, data consistency verification, and meticulous accuracy with no velocity or shipping pace language present.

**Run 3:** `rigour` ✓
> Quote: "Meticulous attention to financial data accuracy"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes accuracy, QA protocols, verification, and documentation—all rigour signals—with no velocity framing.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition is a core financial reporting concern where errors directly impact P&L and regulatory compliance, making this high-risk.

**Run 2:** `high` ✓
> Quote: "Document business logic for financial metrics including revenue recognition and deferred income"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and deferred income are core financial reporting items subject to accounting standards and regulatory compliance requirements.

**Run 3:** `high` ✓
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly focuses on revenue recognition and financial metrics, with emphasis on data accuracy and QA for financial data—hallmarks of high-risk domains.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "Finance"
> Verified: ✓ found in JD
> Reasoning: Only Finance is explicitly named as a collaboration partner; no other named teams or functions are mentioned.

**Run 2:** `1` ✓
> Quote: "Finance"
> Verified: ✓ found in JD
> Reasoning: Only the Finance team is explicitly named as a collaboration partner in the responsibilities section.

**Run 3:** `1` ✓
> Quote: "Finance"
> Verified: ✓ found in JD
> Reasoning: Only Finance is explicitly named as a collaboration partner; other references are to data sources rather than internal partner teams.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The word 'sustain' indicates existing infrastructure with named tools, while the need to establish foundational metrics suggests growth and formalization of a growing function.

**Run 2:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: Named tools with specific application context (SQLMesh) and references to existing systems/reporting layers indicate established infrastructure, while active model development suggests active growth phase.

**Run 3:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The JD mentions specific named tools in responsibilities (SQLMesh, dbt) with operational context ('develop and sustain'), suggesting an established data function growing rather than starting from zero.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The JD includes specific technical context (SQLMesh, dimensional modeling, revenue recognition) and domain-specific metrics (MRR, ARR, churn, LTV) that only someone who performs this role would articulate.

**Run 2:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The specific tool (SQLMesh), precise domain context (revenue recognition, subscription metrics), and technical depth only emerge from someone actively working in financial data infrastructure.

**Run 3:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The JD contains technical specificity including named tools with precise domain context (SQLMesh for revenue recognition), specific subscription metrics (MRR, ARR, churn), and accounting concepts (deferred income) that only come from someone who has done this work.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

### stakeholder_orientation
**Manual:** ``

**Run 1:** `finance` ✗
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: Finance is explicitly named as the primary stakeholder, and the role's responsibilities center entirely on delivering financial metrics and revenue data.

**Run 2:** `finance` ✗
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: Finance is the explicitly named primary stakeholder, and all responsibilities centre on serving their financial reporting and metrics needs.

**Run 3:** `finance` ✗
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: All responsibilities focus on financial metrics (revenue recognition, ARR, churn) and accuracy, with Finance explicitly named as the primary collaboration partner.

⚠ **Disagreement**: manual=`` vs LLM majority=`finance`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: Finance sets the requirements (revenue recognition, churn metrics) and this role executes the technical solution to deliver against those requirements.

**Run 2:** `execution` ✗
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: The role receives scoped requirements from Finance and executes their conversion into data solutions rather than setting the direction for analytics delivery.

**Run 3:** `mixed` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The role strategically defines dimensional models and establishes foundational tables but executes in service of Finance requirements, combining both strategic and execution orientations.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'mixed']
