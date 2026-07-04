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
| stakeholder_orientation | finance | finance | finance | finance | 100% | ✓ |
| autonomy_level | execution | mixed | execution | execution | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: Multiple quality and rigor signals (verify, document, implement QA) with no delivery velocity mentions establish rigour as the primary orientation.

**Run 2:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes verification, quality assurance, and accuracy as core responsibilities with no velocity language present.

**Run 3:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, verification, and accuracy throughout with no velocity-oriented language, signaling a rigour-focused orientation.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and financial metrics are core to financial reporting and regulatory compliance, indicating high domain risk.

**Run 2:** `high` ✓
> Quote: "revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and deferred income are explicit financial reporting concepts with direct regulatory and audit exposure.

**Run 3:** `high` ✓
> Quote: "Document business logic for financial metrics including revenue recognition and deferred income"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and deferred income are regulated accounting concepts that directly affect financial reporting, placing this in the high-risk domain.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "Finance"
> Verified: ✓ found in JD
> Reasoning: Only Finance is explicitly named as a collaborating team; no other functions are mentioned.

**Run 2:** `1` ✓
> Quote: "Finance"
> Verified: ✓ found in JD
> Reasoning: Only Finance is explicitly named as a collaboration partner; other references like 'systems' and 'reporting layers' are not named teams.

**Run 3:** `1` ✓
> Quote: "Collaborate with Finance"
> Verified: ✓ found in JD
> Reasoning: Only Finance is explicitly named as a collaborative partner; no other named teams or functions are identified.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Establish foundational tables for monthly/annual recurring revenue, churn analysis, and revenue patterns"
> Verified: ✓ found in JD
> Reasoning: The combination of establishing foundational tables with sustaining existing models, plus specific tooling like SQLMesh and dbt, indicates a mid-stage team building out capabilities.

**Run 2:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: Named tools (SQLMesh, dbt, cloud DWs) appear in responsibilities indicating existing infrastructure, and the role combines building new models with sustaining existing ones.

**Run 3:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The combination of sustaining existing models while establishing foundational tables, plus named infrastructure tools, suggests a growing but not yet mature data function.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: Specific technical context (SQLMesh for revenue recognition, subscription economy metrics, payment platform integration) can only come from someone who has done this work.

**Run 2:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The specificity of tool stacks (SQLMesh), subscription economy metrics (MRR, ARR, churn, LTV), and financial domain concepts (revenue recognition, deferred income) exceeds boilerplate.

**Run 3:** `hiring_manager` ✗
> Quote: "Document business logic for financial metrics including revenue recognition and deferred income"
> Verified: ✓ found in JD
> Reasoning: The technical specificity (SQLMesh, dimensional modeling, revenue recognition, deferred income) and domain precision indicate someone with hands-on financial data engineering experience wrote this.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

### stakeholder_orientation
**Manual:** `finance`

**Run 1:** `finance` ✓
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: Finance is explicitly named as the primary collaborator and all responsibilities directly serve financial reporting and business requirements.

**Run 2:** `finance` ✓
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: Finance is the explicitly named primary stakeholder, and all responsibilities centre on financial reporting and revenue metrics.

**Run 3:** `finance` ✓
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The entire role is centered on delivering revenue recognition and subscription metrics in service to Finance, making Finance the primary stakeholder.

### autonomy_level
**Manual:** `execution`

**Run 1:** `mixed` ✗
> Quote: "Develop and sustain"
> Verified: ✓ found in JD
> Reasoning: Strategic technical verbs (develop, establish, oversee, implement) indicate architectural autonomy, balanced by Finance setting the business requirements and direction.

**Run 2:** `execution` ✓
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: The role executes requirements set by Finance rather than defining analytics strategy or priorities.

**Run 3:** `execution` ✓
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: While the role has technical implementation autonomy, the strategic direction (requirements) originates from Finance, making this fundamentally an execution role.

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, coding assistance, or AI-enabled infrastructure required of the candidate.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI coding tools, AI-assisted development, or building AI-ready data infrastructure.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No AI-related skills, tools, or competencies are mentioned for the candidate to demonstrate in any capacity.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The responsibility uses an ownership verb (implement) to frame QA as something the candidate defines and owns, not merely a tool to use.

**Run 2:** `responsibility` ✗
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: Testing and QA are framed as an ownership responsibility with an action verb (implement) indicating the candidate defines the protocols.

**Run 3:** `responsibility` ✗
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: Testing and quality frameworks are framed as owned responsibilities with action verbs, not merely as tool skills in a requirements list.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: Operational reliability through accuracy, consistency verification, and QA protocols is central to the role, though without explicit compliance or regulatory framing.

**Run 2:** `moderate` ✗
> Quote: "Verify data consistency across systems and reporting layers"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and accuracy without explicit compliance or regulatory language, reflecting concern for data pipeline stability rather than regulatory exposure.

**Run 3:** `moderate` ✗
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: Quality and accuracy are emphasized in a financial context, but without explicit compliance, regulatory, or audit framing, the loss aversion appears operationally motivated rather than existentially risk-driven.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
