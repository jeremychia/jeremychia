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
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 4 | 0 | 1 | 1 | 33% | ✗ |
| data_team_maturity | early | mid | early | mid | 33% | ✗ |
| jd_authorship | mixed | mixed | hiring_manager | hiring_manager | 33% | ✗ |
| stakeholder_orientation |  | commercial | commercial | commercial | 100% | ✗ |
| autonomy_level |  | execution | execution | execution | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize precision and governance in financial calculations, documentation of KPI definitions, and row-level security implementation, with no signals of speed or iteration velocity.

**Run 2:** `rigour` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The emphasis on coding complex financial calculations and documenting KPI definitions indicates correctness and governance are primary, not delivery speed.

**Run 3:** `rigour` ✗
> Quote: "Document KPI definitions and business rules"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (documentation for reliability, row-level security governance, star schema discipline) with no velocity emphasis.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: While the role involves franchise financial calculations with P&L implications, it is framed as analytics-driven decision support rather than regulatory compliance or financial reporting.

**Run 2:** `moderate` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Financial metrics like royalties and taxable turnover carry business-critical risk for franchisee operations, but the JD lacks explicit regulatory or compliance language indicating high-risk domain.

**Run 3:** `moderate` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Financial calculations are present but framed as operational business decisions for franchise partners, not regulatory compliance or audit-driven work.

### collaboration_width
**Manual:** `4`

**Run 1:** `0` ✗
> Quote: "Design and maintain dashboards for franchisees and internal teams"
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaboration with franchisees and generic internal teams but does not explicitly name specific internal partner functions such as Finance, Product, Engineering, or Data Platform.

**Run 2:** `1` ✗
> Quote: "Support franchise partners' decisions; Design and maintain dashboards for franchisees and internal teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Franchisees are the only explicitly named distinct collaborative partner; generic references to 'internal teams' do not count as named teams.

**Run 3:** `1` ✗
> Quote: "franchise partners"
> Verified: ✓ found in JD
> Reasoning: Franchisees/franchise partners are explicitly named as external collaboration partners; no other named functions appear.

⚠ **Disagreement**: manual=`4` vs LLM majority=`1`

⚠ **LLM inconsistency**: runs gave ['0', '1', '1']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Early-stage opportunity to build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The JD frames an early-stage opportunity to expand analytics scope while describing existing infrastructure (dbt, Databricks, Tableau, established dashboards), indicating a mid-stage team extending its capabilities.

**Run 2:** `early` ✓
> Quote: "Early-stage opportunity to build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The explicit framing as an 'early-stage opportunity to build and structure' indicates the analytics function for franchises is still being established.

**Run 3:** `mid` ✗
> Quote: "Adapt existing dashboards from other business domains"
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure and deployed tools (dbt, Databricks, Tableau) are established; the role builds a new capability atop mature infrastructure.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'early', 'mid']

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Build data marts and business layers using dbt on Databricks; Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines specific technical depth (named tools with feature details, franchise domain knowledge, specific SQL/Tableau skills) with generic phrases like 'promote data-driven decision-making', indicating both hiring manager and recruiter input.

**Run 2:** `hiring_manager` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The specific reference to complex domain financial calculations (royalties, taxable turnover) demonstrates technical knowledge of the actual work rather than generic responsibility language.

**Run 3:** `hiring_manager` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Domain-specific business logic (royalties, taxable turnover), precise tool stack (dbt on Databricks), and named technical features (LODs, window functions) indicate hands-on author expertise.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `commercial` ✗
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is serving franchise partners' operational and commercial decisions, making external franchisees the dominant stakeholder audience.

**Run 2:** `commercial` ✗
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The role directly supports franchisees' commercial decisions on core business operations like pricing and supply chain, identifying franchise partners as the primary commercial stakeholder audience.

**Run 3:** `commercial` ✗
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: Role's primary orientation is enabling franchise partners' business operations and commercial decision-making.

⚠ **Disagreement**: manual=`` vs LLM majority=`commercial`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: While the role owns technical implementation (build, design, implement), the overarching framing emphasizes supporting franchise partner priorities rather than setting independent analytics strategy.

**Run 2:** `execution` ✗
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The primary role framing uses 'support' language, indicating the person executes within defined business needs rather than setting strategic direction for how analytics is delivered.

**Run 3:** `execution` ✗
> Quote: "Support franchisees in interpreting KPIs"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize supporting and executing defined analytics work (building data marts, designing dashboards) in service of franchisee needs rather than setting strategic direction.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`
