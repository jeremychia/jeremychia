# Trace: 2026-06-27_perk_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Perk

**Location:** London; Barcelona
**Date Posted:** 2026-06-27

---

Analytics Engineer
Location
London; Barcelona

Address
London

Employment Type
Full time

Department
Data

Overview
Application
About Us

Perk (formerly TravelPerk) is the intelligent platform for travel and spend management. Built to tackle the time-consuming, manual work that gets in the way of real work, our tools automate everything from travel bookings to expenses, invoice processing, and more. By eliminating this shadow work that wastes hours, erodes morale, and saps innovation, we're on a mission to power real work, with real impact.

We're trusted by more than 10,000 companies worldwide, including Wise, On Running, Breitling, and Fabletics, and we're tackling the 7 hours of lost productivity per employee each week, a $1.7 trillion problem.

Founded in 2015, Perk has grown into a global company of more than 1,800 people across 12 offices globally, with headquarters in London and Boston. We combine innovation, control, and simplicity to transform how businesses work and how people feel at work.

At Perk, we're driven by our values, like being an owner, delivering a 7-star experience, and working as one team. We value curiosity, purpose, and mindset, not just knowledge, to unlock the power in your potential. Our talent team brings together leading minds from the travel and SaaS industries, representing over 70 countries. If you're excited about having a real impact and shaping how millions of people experience work, we'd love you on the team.

Visit www.perk.com to learn more.


Overview

This critical role sits at the intersection of Data Engineering and Data Analytics, focusing on transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users. The ideal candidate will possess a strong background in SQL, dbt, data modelling, ETL/ELT principles and experience with modern cloud data platforms.

Core Responsibilities

Develop and Maintain Transformation best practices in ELT Pipelines: Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models.

Data Modelling: Implement best-practice data modelling and software engineering techniques to ensure data structures are optimised for performance, accuracy, and ease of use in reporting and analytical applications (e.g. CI/CD, testing, lineage).

Data Quality and Testing: Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets. Establish and maintain documentation for all data transformations and models.

Collaboration: Work closely with Data Analysts and business users to understand their reporting needs and optimise data models to support their analytical use cases. Collaborate with Data Engineers on data ingestion strategies and platform optimisation.

Performance Optimisation: Tune and optimise SQL queries and data models to reduce latency and improve the performance of our data warehouse and downstream applications.

Tool Adoption: Champion the adoption of modern data stack tools and practices (e.g. Git, CI/CD).

Build scalable, compelling data visualisations in Looker that can be used by large teams.

Required Qualifications

Experience: 3+ years of experience in a data-focused role (e.g., Analytics Engineer, Data Analyst, BI Developer).

SQL Mastery: Expert-level proficiency in writing and optimising complex SQL queries.

Data Transformation Tooling: Hands-on experience with dbt (Data Build Tool) or similar data transformation frameworks is essential.

Data Warehousing: Experience working with cloud-based data warehouses such as Snowflake, Google BigQuery, or Amazon Redshift.

Data modelling: Solid understanding of data warehousing concepts, ETL/ELT principles, and dimensional modelling techniques.

…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | execution | execution | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, documentation, CI/CD, lineage, and reliability as core expectations throughout the responsibilities section, with no language about speed or rapid delivery.

**Run 2:** `rigour`
> Quote: "Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, testing, best practices, documentation, accuracy, and reliability with no velocity language (fast-paced, ship quickly, rapid delivery), making this unmistakably rigour-oriented.

**Run 3:** `rigour`
> Quote: "Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, testing, accuracy, and best practices as core expectations, with no velocity-oriented language present.

### domain_risk

**Run 1:** `moderate`
> Quote: "transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users"
> Verified: ✓ found in JD
> Reasoning: While Perk handles financial data (expenses, spend management), the JD frames this role as building analytics infrastructure for internal stakeholders rather than direct financial reporting, regulatory compliance, or audit requirements.

**Run 2:** `moderate`
> Quote: "transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users"
> Verified: ✓ found in JD
> Reasoning: This is a B2B SaaS platform for travel and expense management with no explicit regulatory, compliance, or financial reporting signals, indicating moderate business intelligence risk rather than high-risk financial/regulated domains.

**Run 3:** `moderate`
> Quote: "transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users"
> Verified: ✓ found in JD
> Reasoning: While Perk handles financial data through its expense and invoice platform, the JD frames this as an analytics role focused on business intelligence rather than regulatory compliance or financial reporting.

### collaboration_width

**Run 1:** `2`
> Quote: "Data Analysts; Data Engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names two distinct partner teams with whom the role collaborates: Data Analysts and Data Engineers.

**Run 2:** `2`
> Quote: "Data Analysts; Data Engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names two distinct teams as collaboration partners: Data Analysts and Data Engineers.

**Run 3:** `2`
> Quote: "Data Analysts; Data Engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names Data Analysts and Data Engineers as distinct collaboration partners.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Collaborate with Data Engineers on data ingestion strategies and platform optimisation."
> Verified: ✓ found in JD
> Reasoning: References to an established Snowflake data warehouse, existing Data Engineers and Data Analysts teams, and downstream applications indicate a mid-stage function with infrastructure and team structure already in place.

**Run 2:** `mid`
> Quote: "Collaborate with Data Engineers on data ingestion strategies and platform optimisation."
> Verified: ✓ found in JD
> Reasoning: Multiple specialized roles (Data Analysts, Data Engineers, BI users) already exist, infrastructure is in place (Snowflake, dbt, Looker), and responsibilities focus on scaling and improving practices rather than building from zero.

**Run 3:** `mid`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: The JD references existing named tools in active use within responsibilities (dbt, Snowflake) and implies multiple data roles, indicating a data function that has matured beyond early stage.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical details about tool application (dbt with Snowflake), methodologies (dimensional modelling, CI/CD, testing, lineage), and concrete problem-solving context that only someone doing this work would write.

**Run 2:** `hiring_manager`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: Specific technical context is provided (dbt for transformation, Snowflake as warehouse, dimensional modelling, CI/CD practices) that reflects hands-on knowledge of what the role actually entails.

**Run 3:** `hiring_manager`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific tool applications (dbt→Snowflake, Looker) and technical methodology references that indicate hands-on authorship by someone familiar with the actual role.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is to build infrastructure and data assets for internal data analysts, engineers, and other analytics consumers, not for commercial, product, or finance external stakeholders.

**Run 2:** `internal_data`
> Quote: "Collaborate with Data Engineers on data ingestion strategies and platform optimisation."
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining data infrastructure (dbt models, data warehouse optimization, data quality infrastructure) for other data consumers rather than serving commercial, product, or finance functions.

**Run 3:** `internal_data`
> Quote: "transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users"
> Verified: ✓ found in JD
> Reasoning: The primary purpose is to create data infrastructure and models for internal data consumers (Data Analysts, business users) rather than serve commercial, product, or finance functions directly.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: The role exhibits strategic ownership of the transformation domain's design and standards while execution is guided by responsiveness to priorities and use cases defined by Data Analysts and business users.

**Run 2:** `execution`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: The role is scoped to developing and maintaining data infrastructure within defined technical parameters rather than setting direction, with priorities and reporting needs provided by Data Analysts and business users.

**Run 3:** `execution`
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize delivery and maintenance of data models within an established technical stack, rather than defining the overall analytics strategy or direction.

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'execution']

### ai_role
**Run 1:** `none` ✓
> Quote: "Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into our data warehouse (Snowflake) into clean, ready-to-use data models"
> Reasoning: No AI coding tools, GenAI responsibilities, or text-to-SQL infrastructure mentioned; standard dbt transformation work.

**Run 2:** `none` ✓
> Quote: "(no AI signal)"
> Reasoning: No mentions of AI tools, GenAI, or AI-adjacent responsibilities; purely traditional data transformation.

**Run 3:** `none` ✓
> Quote: "No AI-specific skill mentions across phrases"
> Reasoning: Standard data transformation and modeling work with no AI coding tools, GenAI responsibilities, or AI infrastructure signals.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets"
> Reasoning: Candidate owns quality practice with explicit ownership verbs (write, ensure) applied to testing and monitoring outcomes.

**Run 2:** `responsibility` ✓
> Quote: "Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets."
> Reasoning: Candidate owns quality practice with explicit responsibility verbs (write, ensure) on testing and monitoring.

**Run 3:** `responsibility` ✓
> Quote: "Write comprehensive data quality checks, tests, and monitoring scripts to ensure the accuracy, completeness, and reliability of all transformed data assets."
> Reasoning: Candidate explicitly owns quality practice through write/ensure verbs paired with testing, monitoring, and data quality accountability.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "focusing on transforming raw data into high-quality, trustworthy, and easily consumable datasets and visualisations for business users"
> Reasoning: Reliability and trustworthiness framed as operational quality concerns, not compliance or regulatory drivers.

**Run 2:** `moderate` ✓
> Quote: "ensure the accuracy, completeness, and reliability of all transformed data assets"
> Reasoning: Operational reliability framing around accuracy and preventing pipeline failures; no regulatory or compliance language.

**Run 3:** `moderate` ✓
> Quote: "ensure the accuracy, completeness, and reliability; high-quality, trustworthy, and easily consumable datasets for business users"
> Reasoning: Operational reliability and trustworthiness frame the work without explicit regulatory/compliance language; emphasis on preventing data issues reaching stakeholders.

