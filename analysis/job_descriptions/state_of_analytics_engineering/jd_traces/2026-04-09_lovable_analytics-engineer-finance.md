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

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Verify data consistency across systems and reporting layers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data verification, quality assurance, and accuracy protocols with no velocity signals, clearly prioritizing correctness over speed.

**Run 2:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasises quality assurance, data verification, and documentation of financial metrics as core expectations with zero velocity signals present.

**Run 3:** `rigour` ✓
> Quote: "Implement quality assurance protocols for financial data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize QA, verification, and meticulous accuracy for financial data with no competing velocity signals.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Document business logic for financial metrics including revenue recognition and deferred income"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and deferred income are core GAAP/IFRS accounting requirements where data errors directly impact financial reporting compliance.

**Run 2:** `high` ✓
> Quote: "Document business logic for financial metrics including revenue recognition and deferred income"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and deferred income are direct financial reporting concepts where data errors would materially affect P&L and potentially regulatory compliance.

**Run 3:** `high` ✓
> Quote: "Document business logic for financial metrics including revenue recognition and deferred income"
> Verified: ✓ found in JD
> Reasoning: Revenue recognition and deferred income are core accounting concepts that directly impact financial reporting and regulatory compliance.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "Collaborate with Finance to convert requirements into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: Only Finance is explicitly named as a partner team in the JD.

**Run 2:** `1` ✓
> Quote: "Collaborate with Finance"
> Verified: ✓ found in JD
> Reasoning: Only one named team, Finance, is explicitly identified as a collaboration partner.

**Run 3:** `1` ✓
> Quote: "Finance"
> Verified: ✓ found in JD
> Reasoning: Finance is the only explicitly named team mentioned for collaboration in the JD.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The use of 'sustain' indicates existing infrastructure while 'develop' shows ongoing growth, suggesting a team with established tooling building out new capabilities.

**Run 2:** `mid` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The named tool SQLMesh appears in responsibilities indicating existing infrastructure, and specific financial analytics capabilities are being established, suggesting a growing but not yet mature data function.

**Run 3:** `mid` ✗
> Quote: "Establish foundational tables for monthly/annual recurring revenue, churn analysis, and revenue patterns"
> Verified: ✓ found in JD
> Reasoning: The emphasis on establishing foundational infrastructure within a named functional area suggests a growing data team building specific capabilities rather than early-stage or fully mature.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The responsibility names a specific tool (SQLMesh) with precise business context (revenue recognition, subscription metrics) that only someone doing this job would articulate.

**Run 2:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The responsibilities demonstrate specific technical knowledge of tools (SQLMesh) combined with deep domain expertise in financial metrics and accounting concepts (revenue recognition, deferred income) that only comes from hands-on experience in this role.

**Run 3:** `hiring_manager` ✗
> Quote: "Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics"
> Verified: ✓ found in JD
> Reasoning: The specific choice of SQLMesh paired with precise domain terminology (revenue recognition) indicates technical authorship from someone who understands the actual work.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`
