# Trace: 2026-06-30_plain-concepts_bi-specialist

## JD text (fed to classifier, Layer B stripped)

```
# BI Specialist — Plain Concepts

**URL:** https://www.linkedin.com/jobs/view/4431592813/
**Location:** Portugal (remote/hybrid not specified)
**Date Posted:** 2026-06-30

---

BI Specialist at Plain Concepts

Company: Plain Concepts
Position: BI Specialist
Location: Portugal
Employment Type: Full-time
Seniority Level: Mid-Senior
Posted: 1 hour ago

Job Overview

Plain Concepts seeks a professional who understands 'data as a product' rather than simply building reports. The role focuses on designing analytical layers where 'metrics depend on well-modeled, reliable data.'

Key Responsibilities

- Design and maintain BI solutions including reports, dashboards, and data models for decision-making
- Convert business needs into scalable data models and visualizations
- Build and optimize ETL/ELT processes for data availability
- Collaborate with Data Engineers on quality and performance
- Define KPIs with business stakeholders
- Enhance reporting solutions focusing on usability and performance
- Support data governance and documentation

Requirements

- Bachelor's degree in Computer Science, Information Systems, or related field
- 3+ years as BI Developer, Data Analyst, or Analytics Engineer
- Strong SQL and relational database skills
- Dashboard experience with Power BI, Tableau, or Looker
- Data modeling knowledge (star schema, snowflake schema)
- ETL/ELT pipeline design experience
- Cloud platform familiarity (Azure, AWS, Google Cloud) preferred
- Data warehousing principles knowledge
- Git version control experience valued
- Agile environment experience preferred
- Fluent English (written and spoken)

Industry: IT Services and IT Consulting

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 1 | 1 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | recruiter | recruiter | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | execution | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "metrics depend on well-modeled, reliable data"
> Verified: ✓ found in JD
> Reasoning: The job overview explicitly frames the role around data reliability and modeling quality rather than delivery speed, with emphasis on data governance and quality.

**Run 2:** `rigour`
> Quote: "metrics depend on well-modeled, reliable data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data reliability, quality, governance, and documentation as core values rather than speed or rapid iteration.

**Run 3:** `rigour`
> Quote: "metrics depend on well-modeled, reliable data"
> Verified: ✓ found in JD
> Reasoning: The job explicitly emphasizes data quality, reliability, and modeling rigor as core to its mission, with no velocity or speed-focused language.

### domain_risk

**Run 1:** `moderate`
> Quote: "reports, dashboards, and data models for decision-making"
> Verified: ✓ found in JD
> Reasoning: The role supports operational business decisions but lacks explicit mention of financial reporting, compliance, or regulatory requirements that would elevate risk.

**Run 2:** `moderate`
> Quote: "data models for decision-making"
> Verified: ✓ found in JD
> Reasoning: The role supports business decisions without explicit regulatory, financial reporting, or compliance language, indicating moderate rather than high risk.

**Run 3:** `moderate`
> Quote: "Design and maintain BI solutions including reports, dashboards, and data models for decision-making"
> Verified: ✓ found in JD
> Reasoning: This is internal business intelligence work supporting decision-making without explicit regulatory, compliance, or financial reporting requirements that would elevate risk.

### collaboration_width

**Run 1:** `1`
> Quote: "Data Engineers"
> Verified: ✓ found in JD
> Reasoning: Only Data Engineers is explicitly named as a partner function; business stakeholders is generic language per classification rules.

**Run 2:** `1`
> Quote: "Data Engineers"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named team (Data Engineers) is identified as a collaboration partner; 'business stakeholders' is too generic to count as a distinct named function.

**Run 3:** `1`
> Quote: "Data Engineers"
> Verified: ✓ found in JD
> Reasoning: Only 'Data Engineers' is explicitly named as a collaboration partner; other references like 'business stakeholders' are generic and do not count.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Collaborate with Data Engineers on quality and performance"
> Verified: ✓ found in JD
> Reasoning: Reference to an existing Data Engineers function indicates the data capability has matured beyond early stage but is not described as a large, multi-specialized organization.

**Run 2:** `mid`
> Quote: "Collaborate with Data Engineers on quality and performance"
> Verified: ✓ found in JD
> Reasoning: Shows an established but specialized data function with a distinct Data Engineer team rather than early-stage greenfield building or mature multi-team scale.

**Run 3:** `mid`
> Quote: "Enhance reporting solutions focusing on usability and performance"
> Verified: ✓ found in JD
> Reasoning: The emphasis on enhancing existing solutions and optimizing processes suggests an established team improving capabilities rather than building from zero.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Build and optimize ETL/ELT processes for data availability"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical concepts (ETL/ELT, data models, star schema) but lacks granular details like tool names or scale metrics that would indicate hiring manager authorship alone.

**Run 2:** `recruiter`
> Quote: "Design and maintain BI solutions including reports, dashboards, and data models for decision-making; Collaborate with Data Engineers on quality and performance; Define KPIs with business stakeholders"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities section uses generic action verbs that could apply to any BI role without specific technical context about what this person actually does.

**Run 3:** `recruiter`
> Quote: "Design and maintain BI solutions including reports, dashboards, and data models; Enhance reporting solutions focusing on usability and performance"
> Verified: ⚠ NOT found verbatim
> Reasoning: Generic action verbs and responsibilities without specific company context, existing challenges, scale, or tool-specific application indicate recruiter authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "metrics depend on well-modeled, reliable data"
> Verified: ✓ found in JD
> Reasoning: While serving business stakeholders with reports and dashboards, the role's defining emphasis on reliable, well-modeled data and its responsibilities for ETL and governance align with serving the data function's mission.

**Run 2:** `internal_data`
> Quote: "understands 'data as a product' rather than simply building reports"
> Verified: ✓ found in JD
> Reasoning: The framing emphasizes building data infrastructure and modeling layers as a service to data consumers, characteristic of internal_data platform orientation.

**Run 3:** `internal_data`
> Quote: "understands 'data as a product' rather than simply building reports"
> Verified: ✓ found in JD
> Reasoning: The role is framed around building analytical infrastructure and treating data as a product for internal use, positioning it as serving the data function's needs.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Define KPIs with business stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting (designing solutions, defining KPIs) with execution-oriented responsibilities (support governance, enhance solutions), indicating mixed autonomy.

**Run 2:** `execution`
> Quote: "Convert business needs into scalable data models and visualizations"
> Verified: ✓ found in JD
> Reasoning: The phrase indicates the role receives business direction and executes solutions rather than setting strategic direction for the analytics function.

**Run 3:** `mixed`
> Quote: "Define KPIs with business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs like 'define' and 'design' suggest ownership, but execution occurs collaboratively with external stakeholders rather than independently.

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'mixed']

### ai_role
**Run 1:** `none` ✓
> Quote: "Build and optimize ETL/ELT processes for data availability"
> Reasoning: Standard data engineering and BI work with no AI tool usage or GenAI-enabling infrastructure responsibilities.

**Run 2:** `none` ✓
> Quote: "Collaborate with Data Engineers on quality and performance; data as a product"
> Reasoning: No mention of AI coding tools, GenAI capabilities, or AI-ready infrastructure; focuses on traditional data modeling and governance.

**Run 3:** `none` ✓
> Quote: "No explicit AI signal"
> Reasoning: No mentions of AI coding tools, AI-first mindset, or GenAI infrastructure in provided phrases.


### testing_framing
**Run 1:** `absent` ✓
> Quote: "Collaborate with Data Engineers on quality and performance"
> Reasoning: Quality mentioned in collaborative context only; no ownership verb (own/ensure/define/implement) paired with testing or quality responsibility.

**Run 2:** `absent` ✓
> Quote: "Collaborate with Data Engineers on quality and performance; Support data governance and documentation"
> Reasoning: Quality mentioned but as collaborative effort without ownership verbs (own/ensure/define/implement); no testing tools or explicit data contracts specified.

**Run 3:** `absent` ✓
> Quote: "Collaborate with Data Engineers on quality and performance"
> Reasoning: Quality mentioned as collaborative effort, not as owned responsibility with defining/implementing/ensuring verbs.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "metrics depend on well-modeled, reliable data; data governance and documentation"
> Reasoning: Hiring driven by operational reliability concerns (governance, quality, data stability) but no compliance or regulatory framing; moderate loss aversion rather than high trust/audit-driven.

**Run 2:** `moderate` ✓
> Quote: "metrics depend on well-modeled, reliable data; Rigour signals dominate — reliable data, data governance, quality and performance"
> Reasoning: Operational reliability and data quality emphasized throughout; errors affect business decisions without regulatory/compliance/audit language.

**Run 3:** `moderate` ✓
> Quote: "errors affect business decisions without regulatory consequence"
> Reasoning: Operational reliability framing centered on business impact, not compliance or regulatory constraints.

