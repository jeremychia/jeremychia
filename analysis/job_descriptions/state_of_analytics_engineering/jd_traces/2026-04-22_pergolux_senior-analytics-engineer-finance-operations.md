# Trace: 2026-04-22_pergolux_senior-analytics-engineer-finance-operations

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer - Finance & Operations — Pergolux LLC

**URL:** https://talents.studysmarter.de/companies/pergolux-llc/senior-analytics-engineer-finance-operations-32039219/
**Location:** Berlin, Germany (Full-time, on-site)
**Salary:** €60,000–€80,000 annually (estimated)

---

## Key Responsibilities

- Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting
- Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA
- Designing demand and revenue forecasting models for company-wide planning
- Developing product profitability models by combining purchasing, operational, and financial data
- Collaborating with finance, operations, and leadership teams to align on metrics and embed data in decision-making

---

## Required Qualifications

- Expert SQL proficiency and proven experience with dbt building scalable, well-structured models
- Hands-on experience with modern data stacks (Snowflake, Airbyte, Python)
- Strong business acumen with ability to prioritize impactful work
- Comfort navigating uncertainty and bringing structure to developing systems
- Experience with financial or supply chain data, understanding revenue recognition and KPIs

---

## Preferred / Bonus Skills

- Not explicitly listed

---

## Benefits

- Competitive salary aligned with experience and impact
- Structured pension contributions for long-term financial security
- Significant responsibility directly influencing business outcomes
- International team across Europe
- Product discounts, bike leasing program, career advancement opportunities
- Team culture emphasizing collaboration and regular events

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 3 | 3 | 3 | 2 | 33% | ✓ |
| data_team_maturity | early | mid | mid | early | 33% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation |  | finance | finance | finance | 100% | ✗ |
| autonomy_level |  | strategic | strategic | strategic | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes financial accuracy, establishing foundations, and maintaining centralized data integrity with no counterbalancing velocity language about speed or iteration.

**Run 2:** `rigour` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes financial reporting accuracy, data governance, and reliable systems with zero velocity signals present.

**Run 3:** `rigour` ✗
> Quote: "Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ✓ found in JD
> Reasoning: The emphasis on maintaining a reliable single source of truth for financial data and establishing proper financial reporting foundations signals rigour as the primary orientation.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Explicit focus on financial reporting with revenue, COGS, and EBITDA metrics indicates data errors directly impact financial statements and potentially regulatory compliance.

**Run 2:** `high` ✓
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Financial reporting errors directly impact compliance, P&L accuracy, regulatory obligations, and investor confidence.

**Run 3:** `high` ✓
> Quote: "Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ✓ found in JD
> Reasoning: Data errors directly impact financial reporting, P&L calculation, and business decision-making based on accurate financial metrics.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Collaborating with finance, operations, and leadership teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named functions are explicitly listed as collaboration partners: Finance, Operations, and Leadership.

**Run 2:** `3` ✓
> Quote: "finance, operations, and leadership teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named functions are explicitly listed as collaboration partners in the responsibilities.

**Run 3:** `2` ✗
> Quote: "finance; operations"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two explicitly named functional teams (finance and operations) are identified as primary collaboration partners.

⚠ **LLM inconsistency**: runs gave ['3', '3', '2']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Comfort navigating uncertainty and bringing structure to developing systems"
> Verified: ✓ found in JD
> Reasoning: The JD signals existing infrastructure (Snowflake, Airbyte, dbt) but ongoing development and structuring, positioning the team beyond early-stage startup but not yet mature.

**Run 2:** `mid` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Modern data infrastructure (Snowflake, Airbyte) is in place but the financial analytics layer and reporting systems are being built out.

**Run 3:** `early` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The primary mission of "establishing the foundation" for financial reporting indicates the data function for finance is in early development.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'mid', 'early']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Developing product profitability models by combining purchasing, operational, and financial data"
> Verified: ✓ found in JD
> Reasoning: Responsibilities specify precise technical context—named data sources (ERP), exact metrics (revenue recognition, COGS, EBITDA), and methodology (forecasting/profitability models)—indicating firsthand knowledge of the role.

**Run 2:** `hiring_manager` ✓
> Quote: "Developing product profitability models by combining purchasing, operational, and financial data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific financial domain knowledge (revenue recognition, profitability models, ERP integration context) only someone performing this work would know.

**Run 3:** `hiring_manager` ✓
> Quote: "Designing demand and revenue forecasting models for company-wide planning; Developing product profitability models by combining purchasing, operational, and financial data"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain specific technical context (demand forecasting, product profitability logic, data source combinations) that only someone performing financial analytics would describe with this precision.

### stakeholder_orientation
**Manual:** ``

**Run 1:** `finance` ✗
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary audience is Finance and FP&A functions; responsibilities center on financial reporting, profitability analysis, and forecasting rather than product, commercial, or platform work.

**Run 2:** `finance` ✗
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary deliverables and role framing center on financial reporting, FP&A metrics, and finance team enablement.

**Run 3:** `finance` ✗
> Quote: "Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ✓ found in JD
> Reasoning: The primary stakeholder is the Finance function, with explicit focus on financial reporting and FP&A-specific metrics.

⚠ **Disagreement**: manual=`` vs LLM majority=`finance`

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Verbs like 'leading', 'establishing', and 'designing' paired with responsibility for aligning metrics and shaping decision-making indicate strategic direction-setting rather than execution of prescribed work.

**Run 2:** `strategic` ✗
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The role is expected to lead and establish systems architecture, not execute pre-defined work, granting strategic direction-setting authority.

**Run 3:** `strategic` ✗
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The use of "leading" and "establishing" indicates the role sets direction for financial data infrastructure rather than executing direction set by others.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`

### ai_role
**Run 1:** `none` ✓
> Quote: ""
> Reasoning: No mention of AI tools, AI-assisted coding, or AI infrastructure responsibilities.

**Run 2:** `none` ✓
> Quote: "establishing the foundation for all financial reporting"
> Reasoning: No mention of AI tools, AI-assisted coding, or AI infrastructure—standard financial data warehouse work.

**Run 3:** `none` ✓
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Reasoning: Standard financial analytics work with no AI tool usage or infrastructure-building signals.


### testing_framing
**Run 1:** `responsibility` ✗
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Reasoning: Candidate leads data integration and establishes financial reporting foundation, indicating ownership of data quality and integrity practices.

**Run 2:** `absent` ✓
> Quote: "n/a"
> Reasoning: No testing, quality practices, or data contract language in the phrases.

**Run 3:** `absent` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Reasoning: No testing ownership, quality practices, or testing tools mentioned in responsibilities.

⚠ **LLM inconsistency**: runs gave ['responsibility', 'absent', 'absent']

### loss_aversion_framing
**Run 1:** `high` ✓
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Reasoning: Single source of truth for critical financial metrics to leadership teams reflects regulatory/audit concerns and high business impact of data quality failures.

**Run 2:** `high` ✓
> Quote: "establishing the foundation for all financial reporting"
> Reasoning: Financial reporting is compliance-driven; accurate data to finance/leadership teams carries regulatory and audit risk.

**Run 3:** `moderate` ✗
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Reasoning: Emphasis on reliable single source of truth for finance/leadership stakeholders signals operational reliability concern without explicit regulatory framing.

⚠ **LLM inconsistency**: runs gave ['high', 'high', 'moderate']
