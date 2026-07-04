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
| collaboration_width | 3 | 3 | 2 | 2 | 33% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | finance | finance | finance | finance | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | none | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "building scalable, well-structured models"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes correctness, structure, and governance (Foundation for financial reporting, Single Source of Truth, scalable models) with no velocity or speed framing.

**Run 2:** `rigour` ✗
> Quote: "building scalable, well-structured models"
> Verified: ✓ found in JD
> Reasoning: The emphasis on scalability, structure, and establishing foundational financial infrastructure prioritizes correctness and reliability over speed.

**Run 3:** `rigour` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness and building a reliable foundation for financial reporting, with no velocity signals present.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Financial reporting is explicitly mentioned and directly affects regulatory compliance and financial statement accuracy.

**Run 2:** `high` ✓
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: Revenue, COGS, and EBITDA are core financial reporting metrics where errors directly affect financial statements and regulatory compliance.

**Run 3:** `high` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Financial reporting is explicitly the primary output and directly affects regulated financial statements.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "finance; operations; leadership teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams are counted: finance, operations, and leadership are explicitly listed as collaboration partners.

**Run 2:** `2` ✗
> Quote: "finance; operations"
> Verified: ✓ found in JD
> Reasoning: Finance and Operations are the two explicitly named distinct functions listed as collaboration partners; leadership is a stakeholder group rather than a distinct operational team.

**Run 3:** `2` ✗
> Quote: "finance, operations, and leadership teams"
> Verified: ✓ found in JD
> Reasoning: Finance and Operations are explicitly named as collaboration partners; leadership is generic and does not count.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

⚠ **LLM inconsistency**: runs gave ['3', '2', '2']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "proven experience with dbt building scalable, well-structured models"
> Verified: ✓ found in JD
> Reasoning: Named tools (Snowflake, Airbyte, dbt) are already in use and the role is establishing the financial reporting layer within existing infrastructure, signaling growth beyond early stage.

**Run 2:** `mid` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The language 'establishing the foundation' indicates building infrastructure beyond greenfield, but financial reporting systems are not yet mature.

**Run 3:** `mid` ✗
> Quote: "establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The language of establishing foundations with existing named tools (Snowflake, Airbyte, dbt) signals a mid-stage team building out capabilities rather than greenfield or mature at scale.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Developing product profitability models by combining purchasing, operational, and financial data"
> Verified: ✓ found in JD
> Reasoning: Responsibilities include specific financial modeling concepts (demand forecasting, product profitability, revenue recognition) and precise data domain knowledge that indicate hands-on experience.

**Run 2:** `hiring_manager` ✓
> Quote: "Developing product profitability models by combining purchasing, operational, and financial data"
> Verified: ✓ found in JD
> Reasoning: The specific reference to distinct data domains (purchasing, operational, financial) and profitability modeling shows domain expertise from someone who has done this work.

**Run 3:** `hiring_manager` ✓
> Quote: "Creating and maintaining a Finance Single Source of Truth covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specificity of named financial metrics, domain knowledge of revenue recognition, and detailed business context indicate direct domain experience in authorship.

### stakeholder_orientation
**Manual:** `finance`

**Run 1:** `finance` ✓
> Quote: "Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves financial reporting, FP&A metrics, and business financial outcomes for finance teams.

**Run 2:** `finance` ✓
> Quote: "Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: Revenue, COGS, and EBITDA are FP&A metrics, and the explicit focus on 'financial reporting' makes finance the primary audience.

**Run 3:** `finance` ✓
> Quote: "Creating and maintaining a Finance Single Source of Truth covering revenue, COGS, logistics costs, and EBITDA"
> Verified: ⚠ NOT found verbatim
> Reasoning: The explicit naming of a Finance Single Source of Truth and focus entirely on financial metrics places the primary audience as the finance team.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: The role uses strategic verbs (leading, establishing) and is responsible for defining how the financial reporting layer is built.

**Run 2:** `strategic` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: 'Leading' and 'establishing the foundation' signal strategic ownership of direction-setting rather than execution of predefined work.

**Run 3:** `strategic` ✓
> Quote: "Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting"
> Verified: ✓ found in JD
> Reasoning: Leading and establishing are strategic verbs indicating the role defines the financial data strategy and architecture rather than executing predefined work.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, machine learning, or AI-assisted coding; it focuses on traditional data stack skills (SQL, dbt, Snowflake, Python).

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no expectations for AI tool usage, AI-assisted workflows, or AI-ready data infrastructure.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding practices, or AI infrastructure capabilities expected of the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or data quality signal in JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD does not mention testing practices, data contracts, observability, or data quality frameworks.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal anywhere in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: Despite the high-risk financial domain, the JD contains no mention of testing frameworks, data contracts, or data quality assurance practices.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of testing frameworks, data quality practices, observability tooling, or data contracts.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Finance Single Source of Truth"
> Verified: ✓ found in JD
> Reasoning: The financial reporting domain and Single Source of Truth concept implicitly signal concern for data accuracy and preventing conflicting data reaching decision-makers, but the JD is framed around building capabilities rather than explicitly managing risk.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role in capability and delivery terms (establishing, creating, designing) rather than risk prevention, compliance, or stakeholder trust concerns.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames all responsibilities in capability and delivery terms with no explicit mention of compliance, audit, operational reliability, or preventing data quality risks.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'none']
