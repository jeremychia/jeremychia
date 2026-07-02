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
| jd_authorship | recruiter | recruiter | recruiter | recruiter | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | execution | execution | execution | 100% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | absent | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Ensure data quality, consistency, and documentation; Participate in data governance and best practice improvements"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities emphasize quality, consistency, documentation, and governance without any velocity-oriented language like fast-paced or rapid delivery.

**Run 2:** `rigour` ✓
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasise data quality, consistency, documentation, and governance as core expectations with no velocity or speed-focused language.

**Run 3:** `rigour` ✓
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, and best practices with no velocity signals such as fast-paced delivery or iteration speed present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "structure, model, and leverage data used by business teams"
> Verified: ✓ found in JD
> Reasoning: The role supports business intelligence and decision-making at a consulting firm with no explicit financial reporting, compliance, or regulatory language present.

**Run 2:** `moderate` ✓
> Quote: "structure, model, and leverage data used by business teams"
> Verified: ✓ found in JD
> Reasoning: The role serves generic business teams without explicit financial reporting, regulatory, compliance, or audit framing.

**Run 3:** `moderate` ✓
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes data reliability for business teams in a consulting context with no explicit financial reporting, compliance, or regulatory language.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Product, Data Engineering, and Business teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named functions are explicitly listed as collaboration partners in the responsibilities section.

**Run 2:** `3` ✓
> Quote: "Collaborate with Product, Data Engineering, and Business teams; serving as a central bridge between Data Engineering, Data Analytics, and end users"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named teams: Product, Data Engineering, and Data Analytics are explicitly referenced as collaboration partners.

**Run 3:** `3` ✓
> Quote: "Collaborate with Product, Data Engineering, and Business teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named partner teams are explicitly listed in the collaboration responsibility.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Develop and optimise data transformations using ELT tools; Participate in data governance and best practice improvements"
> Verified: ⚠ NOT found verbatim
> Reasoning: Named tools (dbt, Snowflake, BigQuery) are deployed and operational, suggesting an established function in growth phase rather than greenfield or fully mature.

**Run 2:** `mid` ✗
> Quote: "Participate in data governance and best practice improvements"
> Verified: ✓ found in JD
> Reasoning: Multiple existing data teams and tools are referenced with responsibilities focused on improving and optimising existing infrastructure rather than building from zero or operating at massive scale.

**Run 3:** `mid` ✗
> Quote: "Develop and optimise data transformations using ELT tools"
> Verified: ✓ found in JD
> Reasoning: Named tools already in use and multiple data roles (Data Engineering, Data Analytics) indicate an established data function beyond early-stage.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `recruiter` ✓
> Quote: "Collaborate with Product, Data Engineering, and Business teams; Optimise data model and analytical query performance; Support teams in data and decision-making tool utilisation"
> Verified: ⚠ NOT found verbatim
> Reasoning: Responsibilities are generic boilerplate verbs without specific technical context, scale numbers, or methodology detail that would indicate hands-on authorship.

**Run 2:** `recruiter` ✓
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic boilerplate action verbs typical of recruiter-written JDs, with no specific problems, scale numbers, or technical context unique to this role.

**Run 3:** `recruiter` ✓
> Quote: "Collaborate with Product, Data Engineering, and Business teams"
> Verified: ✓ found in JD
> Reasoning: Responsibilities rely heavily on generic collaboration and support language without technical specificity about scale, methodology, or tool application context.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly framed as an infrastructure bridge supporting data consumers across the organization rather than serving commercial, product, or finance directly.

**Run 2:** `internal_data` ✓
> Quote: "serve as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role is framed around serving the data platform infrastructure and internal data consumers rather than commercial, product, or finance teams.

**Run 3:** `internal_data` ✓
> Quote: "serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The primary framing emphasizes making data reliable and accessible to data consumers and infrastructure users rather than serving commercial, product, or finance teams directly.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Design and maintain data models for analytical purposes; Develop and optimise data transformations"
> Verified: ⚠ NOT found verbatim
> Reasoning: Responsibilities use execution verbs (develop, optimise, maintain, support) without strategic direction-setting language like 'define strategy' or 'shape delivery'.

**Run 2:** `execution` ✗
> Quote: "Support teams in data and decision-making tool utilisation"
> Verified: ✓ found in JD
> Reasoning: The role emphasises supporting, collaborating, and participating in others' priorities rather than defining strategy or setting data direction.

**Run 3:** `execution` ✗
> Quote: "Support teams in data and decision-making tool utilisation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use execution-oriented verbs (support, develop, ensure, optimize) indicating the role delivers scoped work rather than sets strategic direction.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI coding tools, AI-assisted workflows, or AI data infrastructure expected of the candidate anywhere in the JD.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI skills, coding tools, or AI-related infrastructure anywhere in the JD.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI-related tools, skills, or responsibilities either for candidate use or for building AI infrastructure.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as a core responsibility the candidate owns rather than listed as a tool or absent from the role.

**Run 2:** `absent` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality is a responsibility but there is no mention of testing frameworks, tools, data contracts, or specific quality practices.

**Run 3:** `responsibility` ✗
> Quote: "Ensure data quality, consistency, and documentation"
> Verified: ✓ found in JD
> Reasoning: The verb 'ensure' combined with 'Participate in data governance and best practice improvements' indicates the role owns data quality practices rather than simply using tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

⚠ **LLM inconsistency**: runs gave ['responsibility', 'absent', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "reliable, consistent, and accessible data; Ensure data quality, consistency, and documentation"
> Verified: ⚠ NOT found verbatim
> Reasoning: The framing emphasizes operational reliability and data quality concerns without compliance, regulatory, or stakeholder-trust language typical of high loss-aversion roles.

**Run 2:** `moderate` ✗
> Quote: "ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasises operational reliability and data quality but lacks the compliance, regulatory, or high-stakes risk language that would indicate high loss-aversion framing.

**Run 3:** `moderate` ✗
> Quote: "ensure reliable, consistent, and accessible data"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data consistency are emphasized as core concerns, but without explicit framing of regulatory risk or stakeholder trust as primary drivers.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
