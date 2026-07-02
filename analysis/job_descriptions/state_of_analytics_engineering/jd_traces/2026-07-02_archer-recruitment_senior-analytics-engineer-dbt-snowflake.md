# Trace: 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer (dbt & Snowflake) — Archer Recruitment (client, undisclosed)

**URL:** https://www.linkedin.com/jobs/view/4434709373/
**Location:** Dublin, Ireland
**Date Posted:** 2026-07-02
**Salary:** 80,000–95,000 EUR

---

# Senior Analytics Engineer (dbt & Snowflake)

Company: Archer Recruitment (recruiting on behalf of a client)
Location: Dublin, County Dublin, Ireland (Hybrid - 1 day per week)
Salary: EUR 80,000 - EUR 95,000/yr
Seniority Level: Mid-Senior
Employment Type: Full-time

## Key Responsibilities
The role involves owning the transformation layer of a modern cloud data platform. Specific duties include:
- Designing, building, and maintaining scalable data models using dbt
- Developing analytics-ready transformation layers in Snowflake
- Building reliable ELT pipelines using SQL and Python
- Orchestrating workflows using Airflow
- Defining data modelling, testing, and documentation standards
- Improving data quality through automated testing and validation
- Mentoring teammates and championing Analytics Engineering best practices

## Required Qualifications
- Strong commercial experience with dbt Core and/or dbt Cloud
- Excellent SQL skills
- Experience working with Snowflake
- Python experience for data engineering and automation
- Experience building dimensional models and analytics data marts
- Knowledge of modern ELT architectures
- Experience with orchestration tools such as Airflow

## Key Selling Points
The posting emphasizes real ownership over the analytics engineering function and opportunity to influence data modelling and testing practices across the organization, within a collaborative small team environment.

Contact: Brinsley Doran, Recruitment Executive at Archer Recruitment

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
| jd_authorship | mixed | hiring_manager | hiring_manager | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | mixed | strategic | 33% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Improving data quality through automated testing and validation"
> Verified: ✓ found in JD
> Reasoning: The explicit focus on testing, validation, and quality as core responsibilities demonstrates rigour orientation.

**Run 2:** `rigour`
> Quote: "Improving data quality through automated testing and validation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, validation, and data quality standards as core expectations with no countervailing velocity language.

**Run 3:** `rigour`
> Quote: "Improving data quality through automated testing and validation"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, standards, documentation, and best practices with no counterbalancing velocity signals, placing the orientation firmly on rigour.

### domain_risk

**Run 1:** `moderate`
> Quote: "Developing analytics-ready transformation layers in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The focus on analytics support without financial, compliance, or regulatory language suggests moderate domain risk typical of business intelligence operations.

**Run 2:** `moderate`
> Quote: "Developing analytics-ready transformation layers in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building data infrastructure without explicit financial reporting, compliance, or regulatory language to indicate high risk.

**Run 3:** `moderate`
> Quote: "transformation layer of a modern cloud data platform"
> Verified: ✓ found in JD
> Reasoning: No explicit financial, regulatory, or compliance language; modern data platform work typically affects business decisions without immediate regulatory consequences.

### collaboration_width

**Run 1:** `0`
> Quote: "No named partner teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities focus on analytics engineering and team mentoring without explicitly naming external partner functions such as Product, Finance, or Engineering.

**Run 2:** `0`
> Quote: "Mentoring teammates and championing Analytics Engineering best practices"
> Verified: ✓ found in JD
> Reasoning: No specific named partner teams or functions are identified in the JD; collaboration is described generically.

**Run 3:** `0`
> Quote: "No explicitly named partner teams identified in the responsibilities section"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions mentoring teammates and collaborative environment but does not explicitly name specific partner functions such as Finance, Product, Marketing, or Engineering.

### data_team_maturity

**Run 1:** `mid`
> Quote: "owning the transformation layer of a modern cloud data platform"
> Verified: ✓ found in JD
> Reasoning: The reference to an existing 'modern cloud data platform' with established infrastructure (Snowflake, Airflow, dbt) indicates a mid-stage team that has built foundational systems but is still developing practices.

**Run 2:** `mid`
> Quote: "Mentoring teammates and championing Analytics Engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The presence of mentoring responsibilities, named tools in responsibilities (dbt, Snowflake, Airflow), and the need to define standards suggest a team with existing infrastructure that is growing and formalizing practices.

**Run 3:** `mid`
> Quote: "Defining data modelling, testing, and documentation standards"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, Snowflake, Airflow) combined with standard-setting and team mentoring indicate an established team growing and formalizing practices, not building from zero.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Defining data modelling, testing, and documentation standards"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about tools (dbt Core/Cloud, Snowflake, Airflow) and methodologies (dimensional models, ELT) suggests insider knowledge, but lack of scale numbers and specific business challenges indicates recruiter involvement.

**Run 2:** `hiring_manager`
> Quote: "Designing, building, and maintaining scalable data models using dbt"
> Verified: ✓ found in JD
> Reasoning: The specificity of tool usage (dbt for transformation layer), architectural patterns (dimensional models, ELT), and context-specific descriptions indicate someone who has done this work wrote the responsibilities.

**Run 3:** `hiring_manager`
> Quote: "Building reliable ELT pipelines using SQL and Python"
> Verified: ✓ found in JD
> Reasoning: Specific technologies (dbt, Snowflake, Airflow), methodologies (ELT, dimensional models), and expected outcomes (reliable pipelines, analytics-ready layers) show technical depth only someone who has done this work would specify.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "developing analytics-ready transformation layers in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The focus on building infrastructure and models that serve downstream analytics consumers within the data team indicates internal_data stakeholder orientation.

**Run 2:** `internal_data`
> Quote: "Defining data modelling, testing, and documentation standards"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is to build data infrastructure, standards, and mentorship within the data function itself, not to serve commercial, product, or finance teams.

**Run 3:** `internal_data`
> Quote: "Mentoring teammates and championing Analytics Engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the data function itself—mentoring the team, defining standards for data engineers and analysts, and building infrastructure rather than serving product, commercial, or finance stakeholders.

### autonomy_level

**Run 1:** `strategic`
> Quote: "Defining data modelling, testing, and documentation standards"
> Verified: ✓ found in JD
> Reasoning: The responsibility for defining (not following) standards and influencing practices across the organization indicates strategic autonomy to shape the analytics engineering function's direction.

**Run 2:** `mixed`
> Quote: "Defining data modelling, testing, and documentation standards"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting (defining standards, influencing practices across the organization) with hands-on execution (designing, building, and maintaining models).

**Run 3:** `strategic`
> Quote: "real ownership over the analytics engineering function and opportunity to influence data modelling and testing practices across the organization"
> Verified: ✓ found in JD
> Reasoning: The role is expected to own the direction of analytics engineering, define standards, and shape practices across the organization rather than execute direction set by others.

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'strategic']

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no references to AI coding tools, AI-ready data infrastructure, or expected AI capabilities from the candidate.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-ready data foundations, or AI applications as expected candidate skills.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, or AI infrastructure requirements from the candidate.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Improving data quality through automated testing and validation"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as owned practices with clear action verbs showing the candidate is accountable for establishing testing standards and practices.

**Run 2:** `responsibility`
> Quote: "Improving data quality through automated testing and validation"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to own and drive data quality improvements through testing and validation, not simply use testing tools.

**Run 3:** `responsibility`
> Quote: "Defining data modelling, testing, and documentation standards"
> Verified: ✓ found in JD
> Reasoning: Testing is framed as the candidate's responsibility to define and establish standards, not merely a tool listed in requirements.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Building reliable ELT pipelines using SQL and Python"
> Verified: ✓ found in JD
> Reasoning: The emphasis on 'reliable' pipelines indicates that operational failures are a concern, suggesting moderate loss aversion focused on operational reliability rather than regulatory or compliance risk.

**Run 2:** `moderate`
> Quote: "Building reliable ELT pipelines using SQL and Python"
> Verified: ✓ found in JD
> Reasoning: Operational reliability is an explicit concern (reliable pipelines), but the JD frames this as a capability to deliver rather than a dominant risk register or compliance concern.

**Run 3:** `moderate`
> Quote: "Building reliable ELT pipelines using SQL and Python"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality are concerns (reliable pipelines, automated testing, quality improvement) but without compliance or stakeholder-trust language; the fear is pipeline failures, not regulatory exposure.
