# Trace: 2026-06-20_almedia_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Almedia

**URL:** https://jobs.ashbyhq.com/almedia/8d28d1b5-1508-473b-a599-55e133fba45b
**Location:** Berlin, Germany (On-site)
**Compensation:** €70K – €140K • Offers Equity • Offers Bonus

---

## Overview

This isn't your regular job. Almedia is a place where those who want to push harder can accelerate their careers faster than anywhere else. We're aiming to become Germany's second bootstrapped unicorn. Almedia is already Europe's #3 fastest-growing company in 2025 (FT1000).

We are building the future of marketing by rewarding our community of over 70 million users for engaging with our advertisers' products. We are offering a new way to acquire users for the biggest companies in the world.

Join our team as an Analytics Engineer, where you'll ensure our data is clean, accessible, and ready for analysis. As a core member of our analytics team, you'll ensure our data infrastructure effectively supports self-service analytics, insightful reporting, and business intelligence across the organisation.

---

## Key Responsibilities

- Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt.
- Apply software engineering practices to analytics code, including version control, testing, and continuous integration.
- Automate and streamline data validation, testing, and reporting processes.
- Take ownership of data analysis for a designated domain, collaborating closely with Product Analysts, Data Scientists, and Business Stakeholders to meet their analytical and reporting needs.
- Proactively monitor data integrity, identify issues, and perform root cause analysis.
- Maintain comprehensive data documentation and definitions for easy reference and understanding.
- Train business users on utilising the data platform and data visualisation tools effectively.

---

## Required Qualifications

- 2-4 years of experience as an Analytics Engineer, Data Analyst, or similar role.
- Experience in marketing analytics, with proficiency in SQL and Python.
- Understanding of data warehousing concepts, data modelling, and performance optimization.
- Knowledge of data validation, testing frameworks, and version control best practices (Git).
- Familiarity with modern data stacks (dbt, Snowflake/BigQuery/Redshift, Dagster/Airflow) and cloud data platforms (GCP, AWS).
- Ability to communicate complex analytical findings clearly and concisely to diverse audiences, influencing data-driven decisions.

---

## Preferred / Bonus Skills

- Passionate about transforming data into actionable insights.
- A detail-oriented problem-solver who excels in a collaborative environment.
- Eager to innovate and continuously improve data processes.

---

## Benefits

- Own Our Growth: All Berlin-based employees receive equity in Almedia.
- Scale With Almedia: Grow alongside a startup that has been profitable from day one.
- Central Berlin Office: Work from a fully-stocked modern office built for collaboration, accessible from all around Berlin.
- Other Benefits: Transport subsidy, breakfasts and lunches, language learning, Urban Sports Club, and more.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 4 | 2 | 2 | 2 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | hiring_manager | mixed | hiring_manager | 33% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | execution | execution | execution | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (testing, CI/CD, version control) with zero velocity signals dominate the responsibilities section.

**Run 2:** `rigour` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, CI/CD, and data validation practices as core expectations, with no countervailing velocity signals.

**Run 3:** `rigour` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, version control, continuous integration, data integrity, and data validation as core expectations.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Take ownership of data analysis for a designated domain, collaborating closely with Product Analysts, Data Scientists, and Business Stakeholders to meet their analytical and reporting needs."
> Verified: ✓ found in JD
> Reasoning: The JD describes business intelligence and operational reporting context without explicit financial reporting, compliance, or regulatory language.

**Run 2:** `moderate` ✓
> Quote: "Join our team as an Analytics Engineer, where you'll ensure our data is clean, accessible, and ready for analysis."
> Verified: ✓ found in JD
> Reasoning: The role supports marketing analytics and user acquisition without explicit mention of financial reporting, compliance, or regulatory risk.

**Run 3:** `moderate` ✓
> Quote: "ensure our data is clean, accessible, and ready for analysis"
> Verified: ✓ found in JD
> Reasoning: The role supports business intelligence and analytical decision-making but lacks explicit financial reporting, compliance, or regulatory language indicating high-risk consequences.

### collaboration_width
**Manual:** `4`

**Run 1:** `2` ✗
> Quote: "Product Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named functions are explicitly listed as collaboration partners in the responsibilities section.

**Run 2:** `2` ✗
> Quote: "Product Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named teams are identified as collaboration partners; 'Business Stakeholders' is too generic to count.

**Run 3:** `2` ✗
> Quote: "Product Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named role cohorts are explicitly identified as primary collaboration partners in the responsibilities.

⚠ **Disagreement**: manual=`4` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt."
> Verified: ✓ found in JD
> Reasoning: Named tool (dbt) in responsibilities indicates existing infrastructure, not greenfield, with multiple data roles implied.

**Run 2:** `mid` ✓
> Quote: "Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt."
> Verified: ✓ found in JD
> Reasoning: Named tools in active operational use (dbt) combined with reference to existing self-serve analytics infrastructure indicates an established data function beyond greenfield stage.

**Run 3:** `mid` ✓
> Quote: "ensure our data infrastructure effectively supports self-serve analytics, insightful reporting, and business intelligence across the organisation"
> Verified: ⚠ NOT found verbatim
> Reasoning: The existence of established data infrastructure (self-serve analytics platform) and named tools in responsibilities (dbt) indicates a data function that is scaling beyond initial launch.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt."
> Verified: ✓ found in JD
> Reasoning: Named tools with specific application context (dbt for data models) and domain scoping demonstrate technical knowledge of the actual work.

**Run 2:** `mixed` ✓
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: Generic action verbs combined with specific technical practices and named tool usage (dbt, domain ownership) indicates both recruiter and hiring_manager input.

**Run 3:** `hiring_manager` ✗
> Quote: "Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt."
> Verified: ✓ found in JD
> Reasoning: The specific technical tools (SQL, dbt), software engineering practices (version control, testing, CI), and concrete methodologies demonstrate hands-on knowledge of the role only someone performing it would have.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "ensure our data infrastructure effectively supports self-serve analytics, insightful reporting, and business intelligence across the organisation"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary mission is building and maintaining data infrastructure for internal analytical consumption, not serving commercial, product, or finance specifically.

**Run 2:** `internal_data` ✗
> Quote: "ensure our data infrastructure effectively supports self-service analytics, insightful reporting, and business intelligence across the organisation."
> Verified: ✓ found in JD
> Reasoning: The primary mission is building and maintaining the data platform and self-serve analytics infrastructure, positioning the data team and its analytics consumers as the core audience.

**Run 3:** `internal_data` ✗
> Quote: "Take ownership of data analysis for a designated domain, collaborating closely with Product Analysts, Data Scientists, and Business Stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role serves data analytics consumers (Product Analysts, Data Scientists) and internal stakeholders through building and maintaining data infrastructure.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "collaborating closely with Product Analysts, Data Scientists, and Business Stakeholders to meet their analytical and reporting needs"
> Verified: ✓ found in JD
> Reasoning: The role is framed around meeting defined needs of others rather than setting direction or defining analytics strategy.

**Run 2:** `execution` ✗
> Quote: "Take ownership of data analysis for a designated domain"
> Verified: ✓ found in JD
> Reasoning: The domain is explicitly 'designated' (pre-assigned) and responsibilities focus on executing others' analytical priorities rather than setting strategic direction.

**Run 3:** `execution` ✗
> Quote: "Take ownership of data analysis for a designated domain"
> Verified: ✓ found in JD
> Reasoning: The role receives a pre-scoped domain and executes against analytical and reporting needs defined by collaborative stakeholders rather than setting strategic direction.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

### ai_role
**Run 1:** `none` ✓
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Reasoning: Lists software engineering practices without mentioning AI tools or infrastructure requirements.

**Run 2:** `none` ✓
> Quote: "No AI signal across phrases"
> Reasoning: Standard analytics engineering work (data modeling, SQL/dbt, infrastructure) with no mention of AI coding tools, AI-first mindset, or AI-enabled infrastructure.

**Run 3:** `none` ✓
> Quote: ""
> Reasoning: No AI tools (Copilot, Claude Code, Cursor) or AI infrastructure responsibilities mentioned in the JD.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Reasoning: Candidate owns testing as explicit software engineering practice.

**Run 2:** `responsibility` ✓
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Reasoning: Candidate expected to apply testing practices as part of software engineering responsibility for analytics code.

**Run 3:** `tool_listed` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Reasoning: Testing is mentioned as part of SE practices to apply, but without explicit ownership verbs (own/ensure/define/implement/establish).

⚠ **LLM inconsistency**: runs gave ['responsibility', 'responsibility', 'tool_listed']

### loss_aversion_framing
**Run 1:** `moderate` ✗
> Quote: "ensuring our data is clean, accessible, and ready for analysis"
> Reasoning: Protective framing around data quality indicates operational reliability concern.

**Run 2:** `none` ✓
> Quote: "ensuring our data is clean, accessible, and ready for analysis; ensure data infrastructure effectively supports analytics"
> Reasoning: Framing emphasizes data quality and usability to enable good analysis, not operational risk avoidance or compliance concerns.

**Run 3:** `none` ✓
> Quote: "ensuring our data is clean, accessible, and ready for analysis"
> Reasoning: Data quality framed as enablement and readiness for analysis, not as risk prevention or compliance imperative.

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'none']
