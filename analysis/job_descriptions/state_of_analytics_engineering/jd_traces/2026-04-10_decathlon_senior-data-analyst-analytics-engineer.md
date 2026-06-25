# Trace: 2026-04-10_decathlon_senior-data-analyst-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Data Analyst & Analytics Engineer - Franchise (H/F) — Decathlon Digital FR

**URL:** https://job-boards.eu.greenhouse.io/decathlontechnology/jobs/4796699101?gh_src=cb30d7c2teu
**Location:** Lille - Btwin Village, Nord, France
**Salary:** Not listed

---

## Key Responsibilities

### Business Analysis & Insights
- Support franchise partners' decisions regarding stock, supply chain, and pricing
- Identify trends and anomalies; translate findings into "clear, actionable recommendations"

### Data Visualization & Delivery (Tableau)
- Design and maintain dashboards for franchisees and internal teams
- Adapt existing dashboards from other business domains
- Implement row-level security

### Analytics Engineering (dbt & SQL)
- Build data marts and business layers using dbt on Databricks
- Code complex business logic (royalties, taxable turnover, margins)

### Stakeholder Management
- Negotiate access to internal data sources
- Support franchisees in interpreting KPIs
- Gather feedback for product improvement

### Data Culture
- Promote data-driven decision-making
- Document KPI definitions and business rules

---

## Required Qualifications

- 3+ years in BI, data analysis, or analytics engineering
- Advanced SQL (window functions, joins, performance optimization)
- Expert Tableau proficiency (LODs, parameters, complex blending)
- Understanding of data modeling and star schema concepts
- Fluent English (mandatory); French preferred
- Self-directed problem-solving approach
- Ability to communicate technical concepts to non-technical audiences

---

## Preferred Qualifications

- Retail industry experience
- Understanding of supply chain, inventory rotation, pricing elasticity
- Tableau Server management experience

---

## Technical Stack

- **Storage/Compute:** Databricks (Lakehouse)
- **Transformation:** dbt with SQL
- **Visualization:** Tableau Software

---

## Why Join

- Direct business impact on partner operations
- Early-stage opportunity to build and structure analytics capabilities
- Modern data technology environment

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | high | moderate | high | 33% | ✗ |
| collaboration_width | 4 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | early | mid | early | mid | 33% | ✗ |
| jd_authorship | mixed | mixed | hiring_manager | mixed | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Implement row-level security"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance and control (row-level security, documentation of KPIs and business rules) with no corresponding velocity signals like 'fast-paced' or 'rapid delivery' in the responsibilities section.

**Run 2:** `rigour` ✗
> Quote: "Implement row-level security"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance controls, documentation, and structured data architecture rather than speed or delivery pace.

**Run 3:** `rigour` ✗
> Quote: "Document KPI definitions and business rules"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize documentation, governance, and technical correctness with no velocity language, signaling a rigour-oriented culture.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `high` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Errors in royalty calculations, taxable turnover, and margin logic directly affect partner financial reporting and tax compliance, making this financial data work with immediate consequences.

**Run 2:** `moderate` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Financial calculations like royalties are involved in business operations, but the language emphasizes operational support without explicit regulatory or compliance requirements.

**Run 3:** `high` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of taxable turnover indicates financial and tax compliance reporting, placing data errors in a high-risk domain.

⚠ **Disagreement**: manual=`moderate` vs LLM majority=`high`

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'high']

### collaboration_width
**Manual:** `4`

**Run 1:** `1` ✗
> Quote: "franchise partners; franchisees"
> Verified: ⚠ NOT found verbatim
> Reasoning: One distinct external partner group (franchise partners/franchisees) is explicitly named as a collaboration partner; internal teams do not count per exclusion guidelines.

**Run 2:** `1` ✗
> Quote: "franchise partners"
> Verified: ✓ found in JD
> Reasoning: Only franchise partners/franchisees are explicitly named as collaboration partners; references to 'internal teams' are too generic to count as distinct named teams.

**Run 3:** `1` ✗
> Quote: "franchise partners; franchisees"
> Verified: ⚠ NOT found verbatim
> Reasoning: Only one explicitly named external collaboration partner group (franchisees/franchise partners) appears; internal teams are mentioned generically without specific names.

⚠ **Disagreement**: manual=`4` vs LLM majority=`1`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Build data marts and business layers using dbt on Databricks"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities with specific application context (building data marts), combined with the ability to adapt existing dashboards, indicates an established data infrastructure at mid-stage growth rather than early-stage or mature.

**Run 2:** `early` ✓
> Quote: "Early-stage opportunity to build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly signals this is an early-stage opportunity to establish analytics capabilities for the franchise business.

**Run 3:** `mid` ✗
> Quote: "Build data marts and business layers using dbt on Databricks"
> Verified: ✓ found in JD
> Reasoning: Named tools in the responsibilities section (dbt, Databricks, Tableau) indicate an existing infrastructure being built upon, characteristic of mid-stage maturity.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'early', 'mid']

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The Analytics Engineering section contains specific technical details only a hiring manager would write (royalty/taxable turnover logic, dbt/Databricks specifics), while business analysis and stakeholder management sections use generic boilerplate language.

**Run 2:** `hiring_manager` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The specific mention of domain-level business logic (royalties, taxable turnover calculations) reflects technical knowledge specific to franchise accounting, indicating authorship by someone with hands-on experience.

**Run 3:** `mixed` ✓
> Quote: "Build data marts and business layers using dbt on Databricks"
> Verified: ✓ found in JD
> Reasoning: Specific tool choices and named business context indicate hiring manager involvement, while generic phrases like 'Support franchise partners' decisions' show recruiter contribution.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']
