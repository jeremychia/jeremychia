# Trace: 2026-06-29_chefs-culinar-west_business-intelligence-specialist

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Specialist (m/w/d) — CHEFS CULINAR West GmbH & Co. KG

**URL:** https://www.meine-karriere-im-handel.de/stellenangebot/6010
**Location:** Weeze, Germany
**Date Posted:** 2026-06-29

---

Business Intelligence Specialist (m/w/d) - CHEFS CULINAR West GmbH & Co. KG

Location: Weeze, Germany

Company: CHEFS CULINAR, a 100+ year old supplier to hospitality and catering sectors. CHEFS CULINAR West GmbH & Co. KG, Holtumsweg 26, 47652 Weeze.

Key Responsibilities:
- Implementing and optimising ETL/ELT processes for integrating various data sources (ETL-/ELT-Prozesse zur Integration verschiedener Datenquellen)
- Designing data models
- Developing high-performance dashboards and reports with Power BI (leistungsfähige Dashboards und Reports mit Power BI)
- Ensuring data quality and governance
- Supporting business departments (Fachbereiche) with analytics requirements
- Advancing the organisation's data architecture

Required Qualifications:
- Formal education in IT or equivalent credentials/experience in data engineering or analytics
- Practical experience in data engineering or analytics
- Understanding of ETL/ELT processes
- SQL proficiency
- Familiarity with BI tools including Power BI and IBM Cognos Analytics
- Knowledge of modern data platforms, preferably Microsoft Fabric
- Analytical thinking, structured work habits, team collaboration
- Fluency in German and English (Deutsch und Englisch)

Benefits:
- Flexible scheduling
- Remote work options (two days weekly)
- Modern equipment
- Comprehensive training
- 30 vacation days
- Fitness subsidies
- Bike leasing support
- Access to employee benefits portal
- Pension contributions
- Company restaurant access
- Complimentary water, tea, coffee and fruit (Kostenfreies Wasser, Tee, Kaffee und Obst)

Application: bewerbung-weeze@chefsculinar.de
Source: https://www.meine-karriere-im-handel.de/stellenangebot/6010

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 0 | 0 | 0 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | recruiter | recruiter | 33% |
| stakeholder_orientation | internal_data | mixed | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Ensuring data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of data quality and governance as a core responsibility directly signals a rigour orientation with no competing velocity signals present.

**Run 2:** `rigour`
> Quote: "Ensuring data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of data quality and governance as a core responsibility is a primary rigour signal with no offsetting velocity language.

**Run 3:** `rigour`
> Quote: "Ensuring data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The explicit inclusion of data quality and governance as core responsibilities demonstrates a rigour-oriented approach with no counterbalancing velocity language.

### domain_risk

**Run 1:** `moderate`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: Supporting departmental analytics without explicit mention of financial reporting, compliance, or regulatory requirements indicates moderate domain risk typical of general business intelligence.

**Run 2:** `moderate`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: The role supports operational business decisions in hospitality/catering without explicit mention of financial reporting, compliance, or regulatory requirements, indicating moderate rather than high risk.

**Run 3:** `moderate`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: This is a B2B supply company BI role with no mention of financial reporting, regulatory compliance, or mission-critical systems, placing it in the moderate-risk business intelligence domain.

### collaboration_width

**Run 1:** `0`
> Quote: "business departments (Fachbereiche)"
> Verified: ✓ found in JD
> Reasoning: The only collaboration reference is a generic mention of "business departments" without naming specific functions or teams that meet the counting criteria.

**Run 2:** `0`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: No specifically named partner teams (e.g., Finance, Product, Engineering) are mentioned; only generic reference to 'business departments.'

**Run 3:** `0`
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams, functions, or roles are identified; 'business departments' is generic and does not count as a named collaborator.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Implementing and optimising ETL/ELT processes for integrating various data sources"
> Verified: ✓ found in JD
> Reasoning: The use of "optimising" existing processes and working with named tools (Power BI, Microsoft Fabric) indicates an established data function being improved rather than built from scratch.

**Run 2:** `mid`
> Quote: "Implementing and optimising ETL/ELT processes for integrating various data sources"
> Verified: ✓ found in JD
> Reasoning: The role involves working with named tools and optimizing existing processes, indicating established infrastructure and active growth rather than early-stage setup or mature specialization.

**Run 3:** `mid`
> Quote: "Implementing and optimising ETL/ELT processes for integrating various data sources"
> Verified: ✓ found in JD
> Reasoning: The presence of named tools being actively maintained and optimized indicates an established infrastructure that is growing and improving, not building from zero.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Implementing and optimising ETL/ELT processes for integrating various data sources; Designing data models; Developing high-performance dashboards and reports with Power BI"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specific technical responsibilities with named tools and methodologies demonstrate domain knowledge indicating hiring manager input rather than generic recruiter language.

**Run 2:** `recruiter`
> Quote: "Developing high-performance dashboards and reports with Power BI"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic phrasing and standard tools without technical depth or specific context that would indicate a hiring manager's direct experience with the role.

**Run 3:** `recruiter`
> Quote: "Developing high-performance dashboards and reports with Power BI"
> Verified: ✓ found in JD
> Reasoning: The generic, boilerplate action verbs and lack of specific methodology, scale numbers, or technical context suggest recruitment language rather than technical specificity from someone who does this work.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'recruiter', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Advancing the organisation's data architecture"
> Verified: ✓ found in JD
> Reasoning: The emphasis on building data infrastructure, designing models, and optimizing ETL processes indicates primary service to the data function and analytics platform rather than a specific external business stakeholder group.

**Run 2:** `mixed`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple types of business departments (finance, operations, commercial) without explicit focus on a single stakeholder category, indicating mixed stakeholder orientation.

**Run 3:** `internal_data`
> Quote: "Advancing the organisation's data architecture"
> Verified: ✓ found in JD
> Reasoning: The majority of responsibilities focus on building and maintaining data infrastructure—ETL processes, data models, data quality, and governance—that enables other data consumers rather than serving a specific business function.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'mixed', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: The primary framing positions the role as supporting and delivering to business needs with execution-focused responsibilities rather than strategy-setting.

**Run 2:** `execution`
> Quote: "Supporting business departments (Fachbereiche) with analytics requirements"
> Verified: ✓ found in JD
> Reasoning: While the role includes technical design responsibilities, the overall framing emphasizes support and delivery to business departments rather than autonomous strategy-setting.

**Run 3:** `execution`
> Quote: "Implementing and optimising ETL/ELT processes for integrating various data sources"
> Verified: ✓ found in JD
> Reasoning: The role describes delivery of defined infrastructure tasks (implementing, optimizing) without language about setting priorities, defining strategy, or shaping organizational direction.
