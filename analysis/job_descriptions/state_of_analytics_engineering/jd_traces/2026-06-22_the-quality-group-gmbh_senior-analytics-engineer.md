# Trace: 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# (Senior) Analytics Engineer (gn) — The Quality Group GmbH

**URL:** https://job-boards.eu.greenhouse.io/thequalitygroupgmbh1/jobs/4858130101?gh_src=58d2bdf2teu
**Location:** Hamburg (hybrid)

---

## Key Responsibilities

- Build and evolve data models and marts using tools like dbt for scalable analytics
- Translate business requirements into clean, reusable data structures
- Implement and maintain KPI logic in collaboration with Analytics Consulting
- Ensure data quality through testing, validation, and monitoring
- Define and enforce modeling standards and best practices
- Transform DWH data into business-ready datasets
- Support ad-hoc analytical requests requiring data modeling
- Serve as interface between stakeholders, Analytics Consulting, and the DWH team

---

## Required Qualifications

- 2+ years in analytics engineering, data analytics, or similar role
- Strong SQL skills and experience with modern transformation tools (dbt)
- Solid understanding of data modeling and data warehouse concepts
- Experience implementing business logic and KPIs in data models
- Familiarity with version control (Git) and collaborative workflows
- Ability to translate business needs into scalable technical solutions
- Structured, independent, solution-oriented work approach
- Strong ownership mindset and focus on quality
- Clear communication with technical and non-technical stakeholders
- Excellent German and very good English skills

---

## Preferred / Bonus Skills

- Experience with BI tools such as Tableau or Databricks

---

## Benefits

- Flexible working hours and remote work options
- 50% employee discount on products
- E-gym Wellpass subsidy
- Workation opportunities
- 28 days vacation annually
- Corporate benefits (Germany only)

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 2 | 2 | 2 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | mixed | recruiter | mixed | 33% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | execution | execution | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes quality, testing, validation, and monitoring with no velocity-oriented language present.

**Run 2:** `rigour` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, validation, monitoring, and enforcing standards with no velocity, shipping, or speed language present.

**Run 3:** `rigour` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, validation, monitoring, standards, and best practices with no velocity language present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Transform DWH data into business-ready datasets"
> Verified: ✓ found in JD
> Reasoning: The JD describes business analytics and BI work without explicit financial reporting, compliance, or regulatory language that would signal high risk.

**Run 2:** `moderate` ✓
> Quote: "Translate business requirements into clean, reusable data structures"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes supporting business analytics and decision-making without explicit financial reporting, compliance, or regulatory consequences language.

**Run 3:** `moderate` ✓
> Quote: "Transform DWH data into business-ready datasets"
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus on operational analytics and business intelligence rather than financial reporting, regulatory compliance, or mission-critical systems.

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "Analytics Consulting; DWH team"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two named partner teams are explicitly mentioned as collaboration points in the responsibilities.

**Run 2:** `2` ✗
> Quote: "Analytics Consulting; DWH team"
> Verified: ⚠ NOT found verbatim
> Reasoning: Only two explicitly named teams are identified in the responsibilities and role description.

**Run 3:** `2` ✗
> Quote: "Analytics Consulting; DWH team"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named teams are explicitly mentioned as collaboration partners in the responsibilities.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities with existing infrastructure and language around growth and evolution indicate a mid-stage team.

**Run 2:** `mid` ✓
> Quote: "Build and evolve data models and marts using tools like dbt"
> Verified: ✓ found in JD
> Reasoning: Named tool in responsibilities paired with language of evolving existing systems indicates a growing data function with established foundational infrastructure.

**Run 3:** `mid` ✓
> Quote: "Serve as interface between stakeholders, Analytics Consulting, and the DWH team"
> Verified: ✓ found in JD
> Reasoning: Multiple established data functions exist with specific roles and charters, and the position involves defining standards, indicating growth beyond early stage but not yet mature.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics"
> Verified: ✓ found in JD
> Reasoning: Specific technical details like dbt with application context are mixed with generic action verbs like support and serve.

**Run 2:** `recruiter` ✗
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics"
> Verified: ✓ found in JD
> Reasoning: The JD mentions dbt without specific application context, scale, volume, or methodology details that would indicate hiring manager domain expertise.

**Run 3:** `mixed` ✓
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics; Ensure data quality through testing, validation, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD includes specific technical context (dbt, KPI logic, modeling standards) alongside generic collaboration language.

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'mixed']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Transform DWH data into business-ready datasets"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the analytics function and data consumers through infrastructure and data modeling work.

**Run 2:** `internal_data` ✗
> Quote: "Serve as interface between stakeholders, Analytics Consulting, and the DWH team"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is serving as part of the internal analytics infrastructure and data function rather than directly driving commercial, product, or finance outcomes.

**Run 3:** `internal_data` ✗
> Quote: "Transform DWH data into business-ready datasets"
> Verified: ✓ found in JD
> Reasoning: The role is focused on building the modeling layer and analytics infrastructure to serve internal Analytics Consulting and data consumers, not external commercial or specific business functions.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Support ad-hoc analytical requests requiring data modeling"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize executing defined work and supporting assigned requests rather than setting strategic direction for analytics.

**Run 2:** `execution` ✗
> Quote: "Translate business requirements into clean, reusable data structures"
> Verified: ✓ found in JD
> Reasoning: The emphasis on translating externally-set requirements and supporting ad-hoc requests indicates executing direction set by others rather than setting strategic direction.

**Run 3:** `mixed` ✗
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics; Define and enforce modeling standards and best practices; Support ad-hoc analytical requests requiring data modeling"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic ownership of the modeling domain and governance with execution of support requests and interface responsibilities.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'mixed']

### ai_role
**Run 1:** `none` ✓
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics"
> Reasoning: dbt is a standard data transformation tool, not an AI coding or infrastructure tool; no GenAI responsibilities mentioned.

**Run 2:** `none` ✓
> Quote: "Build and evolve data models and marts using tools like dbt for scalable analytics"
> Reasoning: No AI coding tools, GenAI responsibilities, or AI-ready infrastructure signals; dbt is traditional analytics tooling.

**Run 3:** `none` ✓
> Quote: "No explicit AI signals in stack or responsibilities"
> Reasoning: Role describes standard analytics engineering work (dbt, data modeling, KPI logic) with no mention of AI coding tools, GenAI infrastructure, or AI-first approaches.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Reasoning: Uses ownership verb 'ensure' paired with testing and validation responsibilities, indicating quality practice ownership.

**Run 2:** `responsibility` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Reasoning: Ownership verb 'Ensure' paired with 'testing, validation, monitoring' indicates responsibility for quality practice.

**Run 3:** `responsibility` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Reasoning: Candidate owns quality practice with direct ownership verb (ensure) applied to testing and validation.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Reasoning: Operational reliability framing centered on preventing data quality issues and incidents, not compliance or regulatory dominance.

**Run 2:** `moderate` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Reasoning: Operational reliability signal in data quality monitoring and validation focus, but lacks compliance/audit/regulatory framing.

**Run 3:** `moderate` ✓
> Quote: "Ensure data quality through testing, validation, and monitoring"
> Reasoning: Loss aversion centers on operational reliability (monitoring, data quality) rather than regulatory compliance or trust/governance dominance.

