# Trace: 2026-06-27_datenna_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Datenna BV

**Location:** Hybrid, Eindhoven, Noord-Brabant, Netherlands
**Date Posted:** 2026-06-27

---

Senior Analytics Engineer at Datenna BV

Position: Senior Analytics Engineer
Location: Hybrid, Eindhoven, Noord-Brabant, Netherlands
Department: Engineering

About the Company

Datenna is a fast-growing tech scale-up combining cutting-edge OSINT and AI technologies focused on providing governments with insights into China's technological and economic landscape.

Key Responsibilities

- Design efficient data models using techniques like star schema and snowflake schema
- Develop and maintain data transformation pipelines using dbt, SQL, and Python
- Implement data quality checks and governance practices
- Collaborate with stakeholders to understand data requirements and implement solutions
- Maintain data documentation and catalogs to improve data discoverability
- Apply software engineering best practices to analytics code
- Optimize data models and pipelines for performance

Required Qualifications

- Bachelor's degree in Computer Science, Engineering, or related field
- 5+ years of experience in analytics engineering, or data engineering with focus on data modelling
- Strong SQL skills and experience with data modeling techniques
- Proficiency in dbt, Databricks and Python for data transformation
- Strong problem-solving and communication skills
- Experience with version control systems like Git
- Experience with CI/CD practices for data pipelines
- Experience with orchestrations frameworks, such as Dagster or Airflow

Preferred Skills

- Experience with AI coding assistants (like Claude Code or Codex) is advantageous
- AI is part of how we build — candidates are expected to use AI tools responsibly in daily work

Why Join Datenna

- Impactful geopolitical intelligence work
- OSINT and AI innovation opportunities
- Competitive compensation
- International team environment
- Growth prospects in a scaling company

Application Process

Four stages: recruiter screening call, behavioral interview, system design interview, and skill assessment.

Note: Candidates must already reside in the Netherlands.

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
| jd_authorship | hiring_manager | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Implement data quality checks and governance practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasises data quality, governance, and software engineering best practices rather than speed or iteration—hallmark rigour signals.

**Run 2:** `rigour`
> Quote: "Implement data quality checks and governance practices"
> Verified: ✓ found in JD
> Reasoning: Explicit data quality and governance signals (data quality checks, governance, documentation, best practices) dominate responsibilities with no velocity language present.

**Run 3:** `rigour`
> Quote: "Implement data quality checks and governance practices"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals present (data quality, governance, software engineering best practices, CI/CD, version control, optimization) with no velocity language in the responsibilities section.

### domain_risk

**Run 1:** `moderate`
> Quote: "Impactful geopolitical intelligence work"
> Verified: ✓ found in JD
> Reasoning: While the work is described as impactful, the JD does not explicitly invoke financial reporting, regulatory, or compliance risk language that would classify as high risk.

**Run 2:** `moderate`
> Quote: "Datenna is a fast-growing tech scale-up combining cutting-edge OSINT and AI technologies focused on providing governments with insights into China's technological and economic landscape."
> Verified: ✓ found in JD
> Reasoning: Government intelligence work suggests high risk, but the JD lacks explicit regulatory, compliance, or financial terminology that would trigger the high-risk classification.

**Run 3:** `moderate`
> Quote: "Implement data quality checks and governance practices"
> Verified: ✓ found in JD
> Reasoning: Government intelligence work has high stakes for decision-making, but the JD lacks explicit regulatory, compliance, or financial reporting language that would trigger the high classification.

### collaboration_width

**Run 1:** `0`
> Quote: "Collaborate with stakeholders to understand data requirements and implement solutions"
> Verified: ✓ found in JD
> Reasoning: The JD mentions generic stakeholder collaboration but does not name specific functions like Product, Finance, Data Science, Engineering, or other discrete partner teams.

**Run 2:** `0`
> Quote: "Collaborate with stakeholders to understand data requirements and implement solutions"
> Verified: ✓ found in JD
> Reasoning: Only generic 'stakeholders' mentioned with no named functions, teams, or partner groups explicitly identified.

**Run 3:** `0`
> Quote: "Collaborate with stakeholders to understand data requirements and implement solutions"
> Verified: ✓ found in JD
> Reasoning: Only collaboration mention uses the generic term "stakeholders" with no named partner teams or distinct functions identified.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Develop and maintain data transformation pipelines using dbt, SQL, and Python"
> Verified: ✓ found in JD
> Reasoning: The use of specific named tools (dbt, Databricks) in responsibilities and emphasis on maintaining and optimizing existing pipelines indicates an established data function with infrastructure already in place.

**Run 2:** `mid`
> Quote: "Develop and maintain data transformation pipelines using dbt, SQL, and Python"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities with maintain/optimize focus indicates existing infrastructure and tooling at the growth stage, not greenfield or early phase.

**Run 3:** `mid`
> Quote: "Develop and maintain data transformation pipelines using dbt, SQL, and Python"
> Verified: ✓ found in JD
> Reasoning: Named tools appearing in responsibilities and emphasis on maintaining existing infrastructure indicates an established data function that is growing, not greenfield.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Design efficient data models using techniques like star schema and snowflake schema"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain technical specificity about data modeling methods, named tools, and practices that only someone performing this work would articulate, beyond boilerplate action verbs.

**Run 2:** `mixed`
> Quote: "Design efficient data models using techniques like star schema and snowflake schema; Develop and maintain data transformation pipelines using dbt, SQL, and Python"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical content including schema techniques and named tools appears alongside generic phrases like 'collaborate with stakeholders' and 'apply software engineering best practices'.

**Run 3:** `mixed`
> Quote: "Design efficient data models using techniques like star schema and snowflake schema"
> Verified: ✓ found in JD
> Reasoning: Responsibilities mix specific technical content (schema types, named tools like dbt and Databricks) with generic boilerplate verbs (collaborate, apply best practices).

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Maintain data documentation and catalogs to improve data discoverability"
> Verified: ✓ found in JD
> Reasoning: The role is focused on building and maintaining analytics infrastructure, documentation, and discoverability—serving internal data consumers rather than commercial, product, or finance teams.

**Run 2:** `internal_data`
> Quote: "Maintain data documentation and catalogs to improve data discoverability"
> Verified: ✓ found in JD
> Reasoning: Focus on data infrastructure, documentation, and discoverability directly serves data consumers and internal data platform users, not GTM, product, or finance audiences.

**Run 3:** `internal_data`
> Quote: "Develop and maintain data transformation pipelines using dbt, SQL, and Python"
> Verified: ✓ found in JD
> Reasoning: Role focuses on building data infrastructure and modeling for internal consumption by the analytics team, not directly supporting commercial, product, or finance stakeholders.

### autonomy_level

**Run 1:** `execution`
> Quote: "Collaborate with stakeholders to understand data requirements and implement solutions"
> Verified: ✓ found in JD
> Reasoning: The role receives scoped requirements from stakeholders and executes implementation; verbs are execution-focused (develop, maintain, implement, optimize) rather than strategic (define, establish, shape).

**Run 2:** `execution`
> Quote: "Collaborate with stakeholders to understand data requirements and implement solutions"
> Verified: ✓ found in JD
> Reasoning: Role receives requirements from stakeholders and implements solutions against those requirements rather than setting overall direction or defining strategy.

**Run 3:** `execution`
> Quote: "Collaborate with stakeholders to understand data requirements and implement solutions"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize understanding externally-set requirements and delivering solutions within defined technical scope, not setting analytics strategy or priorities.
