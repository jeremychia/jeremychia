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
| domain_risk | moderate | high | high | moderate | 33% | ✗ |
| collaboration_width | 4 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | early | mid | mid | early | 33% | ✗ |
| jd_authorship | mixed | mixed | hiring_manager | mixed | 33% | ✓ |
| stakeholder_orientation | commercial | commercial | commercial | commercial | 100% | ✓ |
| autonomy_level | execution | execution | execution | mixed | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | moderate | moderate | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Financial data (royalties, taxable turnover) and complex logic requirements signal prioritization of correctness over delivery speed.

**Run 2:** `rigour` ✗
> Quote: "Document KPI definitions and business rules"
> Verified: ✓ found in JD
> Reasoning: Governance and documentation signals (row-level security, documentation requirements) outnumber any velocity language, with no explicit pace-oriented framing.

**Run 3:** `rigour` ✗
> Quote: "Build data marts and business layers using dbt on Databricks"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize structured data modeling with dbt, complex financial logic, row-level security implementation, and documentation—all governance and correctness indicators with no velocity language present.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `high` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The explicit reference to taxable turnover signals regulatory/tax compliance sensitivity, classifying the domain as high-risk.

**Run 2:** `high` ✗
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The role codes financial logic (royalties affect partner payments, taxable turnover is compliance/tax) where errors have direct regulatory and financial consequences.

**Run 3:** `moderate` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The role involves financial calculations (royalties, taxable turnover) affecting franchise operations, but lacks explicit regulatory or compliance framing typical of high-risk financial reporting roles.

⚠ **Disagreement**: manual=`moderate` vs LLM majority=`high`

⚠ **LLM inconsistency**: runs gave ['high', 'high', 'moderate']

### collaboration_width
**Manual:** `4`

**Run 1:** `1` ✗
> Quote: "franchisees"
> Verified: ✓ found in JD
> Reasoning: Only franchisees are explicitly named as a collaboration partner; internal stakeholders are mentioned generically.

**Run 2:** `1` ✗
> Quote: "franchisees"
> Verified: ✓ found in JD
> Reasoning: Only franchisees are explicitly named as a distinct external collaboration partner; internal teams are mentioned but fall under the exclusion for generic vague references.

**Run 3:** `1` ✗
> Quote: "Support franchisees in interpreting KPIs"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly identifies franchisees as a named collaboration partner for dashboard design and KPI interpretation, representing one distinct stakeholder group.

⚠ **Disagreement**: manual=`4` vs LLM majority=`1`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Early-stage opportunity to build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The phrase indicates the analytics function is growing but not from zero; responsibilities involve building on existing Databricks infrastructure.

**Run 2:** `mid` ✗
> Quote: "Early-stage opportunity to build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: Infrastructure exists (Databricks, dbt, Tableau in responsibilities) with existing dashboards to adapt, indicating a growing established function rather than greenfield early-stage.

**Run 3:** `early` ✓
> Quote: "Early-stage opportunity to build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames this as an early-stage role to build and structure the analytics function, indicating the data capability is being established rather than operating at mature scale.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'mid', 'early']

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Technical specificity appears in data engineering and domain logic but stakeholder management responsibilities remain generic.

**Run 2:** `hiring_manager` ✗
> Quote: "Build data marts and business layers using dbt on Databricks"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about tools in their application context plus named business logic (royalties, taxable turnover, margins) indicates someone who understands this job deeply.

**Run 3:** `mixed` ✓
> Quote: "Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: The JD blends technical specificity (dbt, Databricks, specific business logic domains, row-level security implementation) with generic boilerplate (support decisions, promote data-driven thinking), indicating hybrid authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `commercial` ✓
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The primary role framing emphasizes supporting franchisees' commercial decisions about stock and pricing, positioning them as the main audience.

**Run 2:** `commercial` ✓
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: Primary emphasis is supporting external franchise partners' business operations (stock, pricing, supply chain), which is commercial/partnership stakeholder territory.

**Run 3:** `commercial` ✓
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The role's primary framing is enabling commercial decisions for franchise partners on supply chain, inventory, and pricing—defining commercial/partner operations orientation.

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The repeated emphasis on 'support' rather than 'define' or 'establish' indicates the role executes within stakeholder-defined priorities.

**Run 2:** `execution` ✓
> Quote: "Support franchise partners' decisions regarding stock, supply chain, and pricing"
> Verified: ✓ found in JD
> Reasoning: The use of support verbs throughout and framing as delivery-oriented (maintain dashboards, build systems, code logic) indicates execution of direction rather than strategic ownership.

**Run 3:** `mixed` ✗
> Quote: "build and structure analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic responsibilities (building and structuring analytics, designing dashboards) with execution-focused work (supporting partners, adapting existing tools).

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no expectation for the candidate to use or build AI tools; it is a traditional analytics and BI role.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI-assisted coding tools, GenAI applications, or AI/ML pipeline work anywhere in the JD.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tooling, AI-assisted coding, or AI-ready data infrastructure that the candidate must use or develop.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Build data marts and business layers using dbt on Databricks; Code complex business logic (royalties, taxable turnover, margins)"
> Verified: ✓ found in JD
> Reasoning: Despite coding complex financial logic, no mention of testing, data contracts, or quality frameworks appears in responsibilities or requirements.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality framework mentioned in JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: No data quality, testing frameworks, data contracts, or observability signals appear in the responsibilities or requirements sections.

**Run 3:** `absent` ✗
> Quote: "No testing practice mentioned in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD makes no reference to testing frameworks, data quality practices, observability tools, or data contracts in either responsibilities or requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: Despite the regulatory-sensitive nature of taxable turnover calculations, the JD is framed around building capabilities rather than preventing bad outcomes or compliance risks.

**Run 2:** `moderate` ✗
> Quote: "Implement row-level security"
> Verified: ✓ found in JD
> Reasoning: Security and governance concerns are present (row-level security, taxable turnover compliance) but secondary to delivery; the role emphasizes support and insights more than risk prevention as primary framing.

**Run 3:** `moderate` ✗
> Quote: "Implement row-level security"
> Verified: ✓ found in JD
> Reasoning: Row-level security implementation and complex financial logic (taxable turnover) suggest operational governance and compliance concerns, but the JD lacks explicit regulatory or stakeholder-trust framing that would elevate this to high.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'moderate']
