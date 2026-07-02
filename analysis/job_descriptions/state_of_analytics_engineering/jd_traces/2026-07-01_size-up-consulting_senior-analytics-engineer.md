# Trace: 2026-07-01_size-up-consulting_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Size Up Consulting

**URL:** https://www.linkedin.com/jobs/view/4431933660/
**Location:** Paris, Île-de-France, France
**Date Posted:** 2026-07-01

---

Senior Analytics Engineer at Size Up Consulting

Location: Paris, Île-de-France, France
Seniority Level: Mid-Senior level
Employment Type: Full-time
Job Function: Production, Distribution, and Engineering
Industries: Software Development and IT Services and IT Consulting

About Size Up Consulting
Size Up Consulting, est plus qu'une simple société de conseil — the company positions itself as a partner committed to client and employee success, guided by four core values: proximity, excellence, fulfilment, and commitment. The firm specialises in data, DevOps, and user support, with 200 IT experts and an average employee tenure of 5 years.

Role Overview
The position seeks an Analytics Engineer to structure, model, and leverage data used by business teams, serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data.

Key Responsibilities
- Design and maintain data models for analytical purposes
- Develop and optimise data transformations using ELT tools
- Ensure data quality, consistency, and documentation
- Build business indicators and semantic models for activity management
- Collaborate with Product, Data Engineering, and Business teams
- Optimise data model and analytical query performance
- Participate in data governance and best practice improvements
- Support teams in data and decision-making tool utilisation

Technical Environment
SQL, dbt, Snowflake, BigQuery, Databricks, Python, Looker, Tableau, Power BI, Git, Airflow, Docker, AWS, Azure, or GCP

Required Profile
- Minimum 4 years in Analytics Engineering, Business Intelligence, or Data Engineering
- Strong SQL and data modelling expertise
- Experience with dbt or equivalent ELT tool
- Understanding of business and analytical challenges
- Ability to work in agile environments collaborating with technical and functional teams

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | mixed | 33% | ✓ |
| autonomy_level | mixed | execution | mixed | mixed | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, consistency, and governance without any counterbalancing velocity or speed framing.

**Run 2:** `rigour` ✓
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reliability, consistency, quality, and governance with no velocity signals like fast-paced delivery or iteration speed.

**Run 3:** `rigour` ✓
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes quality, consistency, governance, and reliability with no mention of velocity, speed, delivery pace, or iteration.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The role serves business decision-making but lacks explicit financial reporting, regulatory, or compliance language that would indicate high risk.

**Run 2:** `moderate` ✓
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The role supports business decision-making and operational analytics in a consulting context, without financial reporting, regulatory, or compliance signals.

**Run 3:** `moderate` ✓
> Quote: "structure, model, and leverage data used by business teams"
> Verified: ✓ found in JD
> Reasoning: The role supports business analytics without explicit financial reporting, compliance, or regulatory language, indicating standard business intelligence risk.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Data Engineering; Data Analytics; Product"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct teams as collaboration partners: Data Engineering and Data Analytics from the bridge statement, and Product from the collaboration list.

**Run 2:** `3` ✓
> Quote: "Product; Data Engineering; Data Analytics"
> Verified: ✓ found in JD
> Reasoning: Three distinct named functions are explicitly listed: Product and Data Engineering in the collaboration statement, and Data Analytics in the role overview.

**Run 3:** `3` ✓
> Quote: "Product; Data Engineering; Data Analytics"
> Verified: ✓ found in JD
> Reasoning: Named partner functions are Product, Data Engineering, and Data Analytics from the opening role description; Business teams is too generic to count separately.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Develop and optimise data transformations using ELT tools; Participate in data governance and best practice improvements"
> Verified: ✓ found in JD
> Reasoning: The role works with named tools (ELT/dbt) in a governance context, indicating an established data function that is growing and improving.

**Run 2:** `mid` ✗
> Quote: "Collaborate with Product, Data Engineering, and Business teams"
> Verified: ✓ found in JD
> Reasoning: The JD implies existing infrastructure with multiple named data and product roles already established, indicating a growing but not yet mature data organization.

**Run 3:** `mid` ✗
> Quote: "Develop and optimise data transformations using ELT tools"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, Snowflake, Databricks) and language about optimizing existing infrastructure indicate an established team scaling rather than building from zero.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Build business indicators and semantic models for activity management; Collaborate with Product, Data Engineering, and Business teams"
> Verified: ✓ found in JD
> Reasoning: The JD contains some technical specificity (semantic models, ELT tools, activity management context) alongside boilerplate collaboration language.

**Run 2:** `mixed` ✗
> Quote: "Build business indicators and semantic models for activity management"
> Verified: ✓ found in JD
> Reasoning: The JD combines technical specificity like semantic models and activity management with generic boilerplate responsibilities like collaboration and data governance.

**Run 3:** `recruiter` ✓
> Quote: "Design and maintain data models for analytical purposes"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic boilerplate action verbs without technical specificity such as scale, volume, domain methodology, or business context.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Design and maintain data models for analytical purposes; Build business indicators and semantic models for activity management"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building the data modelling and semantic layer for internal consumption, rather than directly serving product, finance, or commercial functions.

**Run 2:** `internal_data` ✓
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The role is positioned as enabling data consumption and self-serve analytics for business end users, with emphasis on accessible, reliable data infrastructure.

**Run 3:** `mixed` ✗
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users"
> Verified: ✓ found in JD
> Reasoning: The role bridges multiple stakeholder groups equally—internal data teams (internal_data orientation) and business end users (general business analytics).

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'mixed']

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Support teams in data and decision-making tool utilisation; Participate in data governance and best practice improvements"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes support and participation in others' initiatives rather than defining direction, strategy, or owning outcomes.

**Run 2:** `mixed` ✓
> Quote: "Design and maintain data models for analytical purposes"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic technical ownership over data model design and quality with an overall framing as a supporting bridge collaborating with and supporting other teams.

**Run 3:** `mixed` ✓
> Quote: "Design and maintain data models for analytical purposes; Build business indicators and semantic models for activity management"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs like design, build, and optimize suggest ownership of technical direction, but collaborate and support language indicates execution of priorities set by others.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no requirements or expectations for the candidate to use, build, or enable AI tools or systems.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, or AI-ready data infrastructure as candidate skills or job expectations.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI-assisted coding tools, agentic workflows, or AI-ready data infrastructure for the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The role explicitly owns data quality using the action verb 'ensure,' framing it as a primary responsibility.

**Run 2:** `responsibility` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as an owned responsibility in the key responsibilities section, not as a tool requirement or incidental concern.

**Run 3:** `responsibility` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as a core responsibility with an ownership verb (Ensure) in the responsibilities section, not merely listed as a tool or requirement.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality concerns are present but secondary to design and delivery responsibilities; the framing focuses on maintaining quality rather than preventing failures or regulatory exposure.

**Run 2:** `moderate` ✗
> Quote: "ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and quality without compliance, regulatory, or stakeholder-trust risk framing.

**Run 3:** `moderate` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and governance are emphasized but no compliance, regulatory, or stakeholder trust language appears, indicating moderate risk focus on pipeline stability.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
