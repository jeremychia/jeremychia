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
| jd_authorship | mixed | hiring_manager | hiring_manager | hiring_manager | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, version control, continuous integration, data validation, and monitoring—core rigour practices—with no competing velocity signals in the job description.

**Run 2:** `rigour` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, version control, continuous integration, data validation, integrity monitoring, and documentation—six+ rigour signals with zero velocity-oriented language.

**Run 3:** `rigour` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, CI/CD, data validation, and data integrity with no velocity signals present.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Take ownership of data analysis for a designated domain, collaborating closely with Product Analysts, Data Scientists, and Business Stakeholders to meet their analytical and reporting needs."
> Verified: ✓ found in JD
> Reasoning: This marketing analytics role affects business intelligence and reporting decisions but lacks explicit financial reporting, compliance, or regulatory language that would signal high risk.

**Run 2:** `moderate` ✓
> Quote: "supports self-service analytics, insightful reporting, and business intelligence across the organisation."
> Verified: ✓ found in JD
> Reasoning: A marketing analytics role supporting business intelligence decisions without financial reporting, regulatory compliance, or mission-critical system language indicates moderate risk.

**Run 3:** `moderate` ✓
> Quote: "self-service analytics, insightful reporting, and business intelligence across the organisation"
> Verified: ✓ found in JD
> Reasoning: The JD describes operational reporting and business intelligence in marketing/advertising without explicit financial reporting, compliance, or regulatory language.

### collaboration_width
**Manual:** `4`

**Run 1:** `2` ✗
> Quote: "Product Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named functions explicitly listed as collaboration partners; generic stakeholder references do not count.

**Run 2:** `2` ✗
> Quote: "Product Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Exactly two explicitly named partner teams appear in the responsibilities; 'Business Stakeholders' does not count as it is too generic per the exclusion rules.

**Run 3:** `2` ✗
> Quote: "Product Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named role cohorts are explicitly listed as collaboration partners in the responsibilities.

⚠ **Disagreement**: manual=`4` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "As a core member of our analytics team, you'll ensure our data infrastructure effectively supports self-service analytics, insightful reporting, and business intelligence across the organisation."
> Verified: ✓ found in JD
> Reasoning: Existing analytics team with named dbt tools in active use and data warehouse infrastructure already deployed suggests a growing function beyond early stage but not yet large-scale mature.

**Run 2:** `mid` ✓
> Quote: "As a core member of our analytics team, you'll ensure our data infrastructure effectively supports self-service analytics, insightful reporting, and business intelligence across the organisation."
> Verified: ✓ found in JD
> Reasoning: The language describes an established analytics team with existing infrastructure and named tools (dbt, Snowflake/BigQuery, Airflow/Dagster) in active use, but without signals of specialized sub-teams or 20+ person scale.

**Run 3:** `mid` ✓
> Quote: "As a core member of our analytics team, you'll ensure our data infrastructure effectively supports self-service analytics, insightful reporting, and business intelligence across the organisation."
> Verified: ✓ found in JD
> Reasoning: The presence of established infrastructure (dbt, cloud platforms), multiple named roles, and existing analytics team indicates a growing team past the early stage.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt. Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ⚠ NOT found verbatim
> Reasoning: This specificity about dbt models, SQL, software engineering practices, and designated domain ownership reflects hands-on technical knowledge only someone doing this work would articulate.

**Run 2:** `hiring_manager` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities demonstrate deep technical knowledge—specific tools (dbt, SQL), software engineering practices, data integrity methodology, and root cause analysis—that only comes from someone who has done the job.

**Run 3:** `hiring_manager` ✗
> Quote: "Apply software engineering practices to analytics code, including version control, testing, and continuous integration."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical practices and tool applications that indicate someone with domain expertise, not generic boilerplate language.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`
