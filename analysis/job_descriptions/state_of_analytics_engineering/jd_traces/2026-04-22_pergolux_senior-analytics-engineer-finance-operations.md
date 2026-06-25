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
| collaboration_width | 3 | 3 | 2 | 3 | 33% | ✓ |
| data_team_maturity | early | early | mid | early | 33% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | mixed | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The emphasis on 'establishing the foundation' and maintaining a 'Single Source of Truth' frames the role around accuracy, structure, and reliability rather than speed.

**Run 2:** `rigour` ✗
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The entire role is framed around building a reliable, accurate financial foundation with a Single Source of Truth governance model, with no signals of speed, iteration velocity, or rapid delivery prioritization.

**Run 3:** `rigour` ✗
> Quote: "Finance Single Source of Truth"
> Verified: ✓ found in JD
> Reasoning: The emphasis on establishing a single authoritative source for financial data prioritizes accuracy and data quality over delivery speed.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Financial reporting data errors directly impact regulatory compliance and financial accuracy, placing this in the high-risk domain.

**Run 2:** `high` ✓
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Financial reporting errors directly affect financial statements and regulatory compliance obligations, placing data accuracy errors in the highest-consequence category.

**Run 3:** `high` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Direct responsibility for financial reporting foundations means data errors directly affect regulatory and financial documentation.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "finance; operations; leadership teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named partner teams (Finance, Operations, Leadership) are explicitly mentioned as collaboration partners.

**Run 2:** `2` ✗
> Quote: "finance; operations"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names Finance and Operations as collaboration partners; leadership is mentioned but refers to senior stakeholders rather than a distinct functional team.

**Run 3:** `3` ✓
> Quote: "finance; operations; leadership teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct teams explicitly named as collaboration partners in the responsibilities.

⚠ **LLM inconsistency**: runs gave ['3', '2', '3']

### data_team_maturity
**Manual:** `early`

**Run 1:** `early` ✓
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The primary mission stated as 'establishing the foundation' signals an early-stage team building financial data infrastructure from the ground up.

**Run 2:** `mid` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The language of 'establishing the foundation' indicates building a new pillar, but the hiring of a Senior person and requirement for modern tools (Snowflake, Airbyte, dbt) signals an existing data team with some organizational structure.

**Run 3:** `early` ✓
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The phrase "establishing the foundation" indicates financial data infrastructure is being built from scratch, characteristic of early-stage data teams.

⚠ **LLM inconsistency**: runs gave ['early', 'mid', 'early']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specific mention of finance data domains (revenue, COGS, EBITDA) and architectural pattern (SSOT) demonstrates domain expertise that only someone with hands-on finance data experience would articulate.

**Run 2:** `hiring_manager` ✓
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specific technical details about the Finance SSoT, specific metrics (COGS, EBITDA), ERP integration, and modeling work clearly originate from someone with direct experience in this role, despite some generic collaboration language.

**Run 3:** `mixed` ✗
> Quote: "Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ✓ found in JD
> Reasoning: The specific enumeration of financial metrics demonstrates hiring manager domain expertise, but generic phrases like "align on metrics" and "embed data in decision-making" suggest recruiter involvement.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']
