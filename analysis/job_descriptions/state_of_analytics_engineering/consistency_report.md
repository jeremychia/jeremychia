# LLM Classification Consistency Report

**JDs classified:** 47  
**Runs per JD:** 3  
**Model:** claude-haiku-4-5  
**Method:** claude CLI subprocess  
**Traces:** see `jd_traces/<application_id>.md` for full per-JD evidence  

---

## Inter-run agreement (LLM self-consistency)

1.00 = all three runs identical. Lower = model is uncertain on this dimension.

| Dimension | Mean | Min | Max | Fully consistent (3/3) |
|-----------|------|-----|-----|------------------------|
| velocity_vs_rigour | 0.94 | 0.33 | 1.00 | 43/47 |
| domain_risk | 0.89 | 0.33 | 1.00 | 39/47 |
| collaboration_width | 0.84 | 0.00 | 1.00 | 36/47 |
| data_team_maturity | 0.89 | 0.33 | 1.00 | 39/47 |
| jd_authorship | 0.57 | 0.00 | 1.00 | 18/47 |

## Manual vs LLM majority-vote agreement

How often the LLM majority vote (best of 3) matches the original hand-coded classification.
High agreement → manual classifications are reproducible by the model.
Low agreement → either the codebook is ambiguous or the original call was subjective.

| Dimension | Match rate | n matched | n total |
|-----------|-----------|-----------|---------|
| velocity_vs_rigour | 66.0% | 31 | 47 |
| domain_risk | 63.8% | 30 | 47 |
| collaboration_width | 21.3% | 10 | 47 |
| data_team_maturity | 53.2% | 25 | 47 |
| jd_authorship | 48.9% | 23 | 47 |

## Evidence quote verification

Checks whether the verbatim quote cited by the LLM actually appears in the JD text.
Failures indicate hallucinated or paraphrased evidence.

| Dimension | Run 1 pass | Run 2 pass | Run 3 pass |
|-----------|-----------|-----------|-----------|
| velocity_vs_rigour | 47/47 | 45/47 | 46/47 |
| domain_risk | 47/47 | 45/47 | 47/47 |
| collaboration_width | 25/47 | 21/47 | 23/47 |
| data_team_maturity | 46/47 | 43/47 | 46/47 |
| jd_authorship | 42/47 | 37/47 | 42/47 |

## Disagreements: manual vs LLM majority vote

Each disagreement is a candidate for codebook revision or reclassification.
See `jd_traces/<application_id>.md` for full reasoning on each case.

### velocity_vs_rigour (16 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Establish data quality standards using tests, CI/CD, and documentation. |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement row-level security |
| 2026-04-22_about-you_senior-data-engineer | mixed | rigour | rigour | rigour | rigour | Strong software engineering fundamentals (CI/CD, testing, design patterns) |
| 2026-04-22_about-you_senior-data-engineer | mixed | rigour | rigour | rigour | rigour | Strong software engineering fundamentals (CI/CD, testing, design patterns) |
| 2026-04-22_distribusion_analytics-engineer | mixed | velocity | mixed | velocity | velocity | Build new Looker dashboards from scratch within tight deadlines |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mixed | rigour | rigour | rigour | rigour | Creating and maintaining a "Finance Single Source of Truth" covering revenue, COGS, logistics costs, and EBITDA |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mixed | rigour | rigour | rigour | rigour | establishing the foundation for all financial reporting |
| 2026-04-22_qasa_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-22_qasa_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-24_getsafe_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Design clean, reliable, and well-documented data models as a single source of truth |
| 2026-04-24_getsafe_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Design clean, reliable, and well-documented data models as a single source of truth |
| 2026-05-09_lightdash_analytics-engineering-advocate | velocity | mixed | mixed | rigour | mixed | You'll balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process impro… |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | mixed | rigour | rigour | rigour | rigour | Take full ownership of the stability of our marketing data pipelines — be the first to respond to incidents and drive re… |
| 2026-06-20_almedia_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Apply software engineering practices to analytics code, including version control, testing, and continuous integration. |
| 2026-06-20_just-dice_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data quality and validation processes to guarantee data accuracy and consistency. |
| 2026-06-23_trade-republic_analytics-engineer | mixed | rigour | rigour | rigour | rigour | applying software engineering best practices |

### domain_risk (17 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | high | moderate | moderate | moderate | moderate | customers, revenue, and operations |
| 2026-04-09_nkg_sustainability-data-analyst | high | moderate | moderate | moderate | moderate | Create Power BI dashboards and reports for monitoring and decision-making |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | moderate | high | moderate | high | high | Code complex business logic (royalties, taxable turnover, margins) |
| 2026-04-22_about-you_senior-data-engineer | high | moderate | high | moderate | moderate | the most important company reports that inform executive decisions |
| 2026-04-22_distribusion_analytics-engineer | high | moderate | moderate | moderate | moderate | Exposure to major clients like Booking.com and Google Maps |
| 2026-04-22_distribusion_analytics-engineer | high | moderate | moderate | moderate | moderate | Exposure to major clients like Booking.com and Google Maps |
| 2026-04-22_polyteia_analytics-engineering-lead | high | moderate | moderate | high | moderate | Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal" |
| 2026-04-22_qasa_analytics-engineer | moderate | moderate | high | high | high | Transform complex data into compelling narratives informing product strategy and financial planning |
| 2026-04-22_statista_analytics-engineer-reporting-platform | low | moderate | moderate | moderate | moderate | Our reporting platform is one of the key channels we use to bring data to life for the business. |
| 2026-04-22_statista_analytics-engineer-reporting-platform | low | moderate | moderate | moderate | moderate | our reporting platform is one of the key channels we use to bring data to life for the business |
| 2026-04-24_getsafe_analytics-engineer | high | moderate | high | moderate | moderate | core business metrics |
| 2026-04-24_getsafe_analytics-engineer | high | moderate | moderate | moderate | moderate | Own and evolve core business metrics - from definition to tracking and operationalisation |
| 2026-05-09_lightdash_analytics-engineering-advocate | low | moderate | moderate | moderate | moderate | Deep understanding of business intelligence and analytics engineering workflows |
| 2026-06-04_vinted_analytics-engineer-finance | high | moderate | moderate | moderate | moderate | Converting Finance requirements into technical solutions |
| 2026-06-20_adsquare_staff-data-analytics-engineer | high | moderate | moderate | moderate | moderate | Build data products leveraging location signals and audience attributes |
| 2026-06-22_scoot_senior-analyst-business-intelligence | high | moderate | moderate | moderate | moderate | Distil complex data into meaningful business insights to facilitate decision-making and forward planning. |
| 2026-06-23_trade-republic_analytics-engineer | high | moderate | moderate | moderate | moderate | Working closely with product and business stakeholders to define and build meaningful product metrics |

### collaboration_width (37 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | 8 | 9 | 6 | 5 | 9 | Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office; Shopper & Partner (D2C & B2B)… |
| 2026-04-08_riverty_data-engineering-lead | 9 | 10 | 10 | 9 | 10 | product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT team… |
| 2026-04-09_nkg_sustainability-data-analyst | 2 | 0 | 0 | 0 | 0 | Strong cross-functional collaboration abilities |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 4 | 1 | 1 | 1 | 1 | franchise partners; franchisees |
| 2026-04-22_about-you_senior-data-engineer | 3 | 0 | 0 | 0 | 0 | none |
| 2026-04-22_about-you_senior-data-engineer | 3 | 0 | 1 | 0 | 0 | other data teams |
| 2026-04-22_distribusion_analytics-engineer | 3 | 0 | 0 | 0 | 0 | Collaborative international team environment |
| 2026-04-22_distribusion_analytics-engineer | 3 | 0 | 0 | 0 | 0 | None identified |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 3 | 3 | 3 | 3 | data platform, engineering, and analytics teams |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 3 | 3 | 3 | 3 | data platform; engineering; analytics |
| 2026-04-22_mentimeter_analytics-engineer | 4 | 0 | 0 | 0 | 0 |  |
| 2026-04-22_mentimeter_analytics-engineer | 4 | 3 | 0 | 0 | 0 | sales, marketing, and product analytics |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 3 | 2 | 2 | 2 | 2 | finance, operations, and leadership teams |
| 2026-04-22_polyteia_analytics-engineering-lead | 2 | 1 | 1 | 1 | 1 | customer success teams |
| 2026-04-22_polyteia_analytics-engineering-lead | 2 | 1 | 1 | 1 | 1 | customer success teams |
| 2026-04-22_qasa_analytics-engineer | 5 | 6 | 6 | 6 | 6 | Product, Marketing, Finance, Support, and Country Management teams; engineering |
| 2026-04-22_qasa_analytics-engineer | 5 | 6 | 6 | 6 | 6 | Product; Marketing; Finance; Support; Country Management; engineering |
| 2026-04-22_statista_analytics-engineer-reporting-platform | 4 | 0 | 0 | 0 | 0 | None identified |
| 2026-04-22_statista_analytics-engineer-reporting-platform | 4 | 0 | 0 | 0 | 0 | N/A |
| 2026-04-28_seven-senders_senior-bi-analyst | 3 | 2 | 2 | 1 | 2 | Act as translator between engineering and business stakeholders; Support the growth of junior analysts |
| 2026-04-28_seven-senders_senior-bi-analyst | 3 | 1 | 1 | 1 | 1 | Act as translator between engineering and business stakeholders |
| 2026-05-01_aviv-group_senior-analytics-engineer | 4 | 2 | 2 | 2 | 2 | analysts; data scientists |
| 2026-05-01_wolt_senior-revenue-data-analyst | 5 | 5 | 4 | 4 | 4 | Product; Analytics; Engineering; Accounting; Finance |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | 2 | 0 | 0 | 0 | 0 |  |
| 2026-05-09_lightdash_analytics-engineering-advocate | 3 | 0 | 2 | 0 | 0 |  |
| 2026-05-11_getyourguide_data-engineer | 3 | 2 | 2 | 2 | 2 | Product;Data teams |
| 2026-05-13_smoobu_senior-analytics-engineer | 3 | 1 | 1 | 1 | 1 | engineering |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 5 | 4 | 4 | 4 | 4 | data analysts; engineers; software engineers; marketing teams |
| 2026-06-20_adsquare_staff-data-analytics-engineer | 3 | 0 | 0 | 0 | 0 |  |
| 2026-06-20_almedia_analytics-engineer | 4 | 2 | 2 | 2 | 2 | Product Analysts; Data Scientists |
| 2026-06-20_just-dice_analytics-engineer | 2 | 3 | 3 | 3 | 3 | our tech and product teams; our marketing and product teams |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | 3 | 0 | 0 | 0 | 0 |  |
| 2026-06-22_freenow_analytics-engineer | 4 | 3 | 3 | 3 | 3 | Engage with analysts and scientists to understand problems and translate them into data solutions; Work with developers … |
| 2026-06-22_scoot_senior-analyst-business-intelligence | 2 | 0 | 0 | 0 | 0 | N/A |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | 3 | 2 | 2 | 2 | 2 | Analytics Consulting; DWH team |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | 3 | 0 | 0 | 0 | 0 | cross-functional alignment |
| 2026-06-23_trade-republic_analytics-engineer | 2 | 1 | 1 | 1 | 1 | product and business stakeholders |

### data_team_maturity (22 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | mid | mature | mature | mid | mature | Our Commercial A&I function is recognized by the executive leadership team for spearheading the growth in analytics matu… |
| 2026-04-08_riverty_data-engineering-lead | mature | mid | mature | mid | mid | Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platfor… |
| 2026-04-08_tem_staff-analytics-engineer | early | early | mid | mid | mid | building the analytics foundation |
| 2026-04-09_ai-futures_data-team-lead | early | mid | mid | mid | mid | Growing and mentoring a data engineering team and contributing to hiring decisions |
| 2026-04-09_lovable_analytics-engineer-finance | early | mid | mid | mid | mid | Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics |
| 2026-04-09_nkg_sustainability-data-analyst | early | mid | mid | mid | mid | Develop and implement a unified sustainability data platform integrating multiple sources |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | early | mid | early | mid | mid | Build data marts and business layers using dbt on Databricks |
| 2026-04-22_distribusion_analytics-engineer | early | mid | mid | mid | mid | Become proficient with the data lake, understanding data sources and processing workflows |
| 2026-04-22_distribusion_analytics-engineer | early | mid | mid | mid | mid | Identify and propose enhancements to reporting systems for better clarity and faster creation |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | early | mid | mid | early | mid | Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting |
| 2026-04-22_qasa_analytics-engineer | early | mid | mid | mid | mid | Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams |
| 2026-04-22_qasa_analytics-engineer | early | mid | early | mid | mid | Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams |
| 2026-04-24_getsafe_analytics-engineer | early | mid | mid | mid | mid | Build and maintain scalable data pipelines and data marts using modern tooling |
| 2026-04-24_getsafe_analytics-engineer | early | mid | mid | mid | mid | Build and maintain scalable data pipelines and data marts using modern tooling |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | early | mid | mid | mid | mid | Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material |
| 2026-05-09_lightdash_analytics-engineering-advocate | early | mid | mid | mid | mid | You'll stay current with our latest features, including our evolving AI capabilities (using Lightdash for our own analyt… |
| 2026-05-11_getyourguide_data-engineer | mature | mid | mid | mid | mid | Maintain balance between operational responsibilities and new development using team SLOs |
| 2026-06-20_adsquare_staff-data-analytics-engineer | mature | mid | mid | mid | mid | Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration |
| 2026-06-20_just-dice_analytics-engineer | early | mid | mid | mid | mid | Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services. |
| 2026-06-22_freenow_analytics-engineer | mature | mid | mid | mid | mid | Provide expertise and collaborate with stakeholders to develop new data products within a Data Mesh environment |
| 2026-06-22_scoot_senior-analyst-business-intelligence | early | mid | mid | mid | mid | Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions. |
| 2026-06-22_sumup_senior-analytics-engineer | mature | mid | mid | mid | mid | Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and s… |

### jd_authorship (24 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | hiring_manager | hiring_manager | mixed | mixed | mixed | Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization. |
| 2026-04-08_tem_staff-analytics-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Design and maintain core dbt models representing business areas like customers, revenue, and operations. |
| 2026-04-09_lovable_analytics-engineer-finance | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | mixed | mixed | recruiter | mixed | Design and operate scalable data pipelines within Microsoft Fabric; Gather requirements and translate them into effectiv… |
| 2026-04-22_distribusion_analytics-engineer | recruiter | recruiter | mixed | mixed | mixed | Identify and propose enhancements to reporting systems for better clarity and faster creation |
| 2026-04-22_distribusion_analytics-engineer | recruiter | mixed | mixed | recruiter | mixed | Build new Looker dashboards from scratch within tight deadlines |
| 2026-04-22_mentimeter_analytics-engineer | hiring_manager | mixed | recruiter | mixed | mixed | Partner with business and technical stakeholders from problem framing to shipped artefacts; Contribute strategic input a… |
| 2026-04-22_mentimeter_analytics-engineer | hiring_manager | recruiter | mixed | hiring_manager | recruiter | Help the organization interpret data |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Actively coding in Python, dbt, and Airflow while coordinating project advancement |
| 2026-04-22_qasa_analytics-engineer | recruiter | hiring_manager | hiring_manager | mixed | hiring_manager | Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams |
| 2026-04-22_shine_senior-analytics-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Build and maintain scalable dbt models on Snowflake for cross-entity analytics |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | mixed | recruiter | recruiter | recruiter | Be the first point of contact for administration topics around the reporting platform, e.g. architecture questions, perm… |
| 2026-04-24_getsafe_analytics-engineer | hiring_manager | mixed | hiring_manager | recruiter | mixed | Drive cross-functional data initiatives with stakeholders across Commercial, Operations, and Engineering |
| 2026-04-24_getsafe_analytics-engineer | hiring_manager | recruiter | recruiter | recruiter | recruiter | Conduct analyses to uncover insights and inform strategic decisions |
| 2026-05-01_aviv-group_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake |
| 2026-05-01_wolt_senior-revenue-data-analyst | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close |
| 2026-05-11_getyourguide_data-engineer | hiring_manager | mixed | mixed | mixed | mixed | Serve as a thought partner with Product and Data teams to translate business requirements |
| 2026-06-20_almedia_analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt. Apply software eng… |
| 2026-06-20_just-dice_analytics-engineer | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services; Create and maintain dat… |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | hiring_manager | hiring_manager | mixed | mixed | mixed | Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagst… |
| 2026-06-22_freenow_analytics-engineer | hiring_manager | recruiter | mixed | mixed | mixed | Engage with analysts and scientists to understand problems and translate them into data solutions |
| 2026-06-22_scoot_senior-analyst-business-intelligence | recruiter | mixed | mixed | mixed | mixed | Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google… |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Build and evolve data models and marts using tools like dbt for scalable analytics |
| 2026-06-23_trade-republic_analytics-engineer | hiring_manager | mixed | recruiter | hiring_manager | mixed | Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and a… |

## LLM internal inconsistencies (runs disagree with each other)

These are cases where the same prompt produced different answers across 3 runs.
High inconsistency → borderline case or ambiguous JD language.

### velocity_vs_rigour (4 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-09_ai-futures_data-team-lead | rigour | velocity | velocity | velocity |
| 2026-04-22_distribusion_analytics-engineer | velocity | mixed | velocity | mixed |
| 2026-04-22_distribusion_analytics-engineer | mixed | velocity | mixed | mixed |
| 2026-05-09_lightdash_analytics-engineering-advocate | mixed | mixed | rigour | velocity |

### domain_risk (8 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | high | moderate | high | moderate |
| 2026-04-22_about-you_senior-data-engineer | moderate | high | moderate | high |
| 2026-04-22_mentimeter_analytics-engineer | moderate | high | moderate | moderate |
| 2026-04-22_polyteia_analytics-engineering-lead | moderate | high | high | high |
| 2026-04-22_polyteia_analytics-engineering-lead | moderate | moderate | high | high |
| 2026-04-22_qasa_analytics-engineer | moderate | high | high | moderate |
| 2026-04-24_getsafe_analytics-engineer | moderate | high | moderate | high |
| 2026-06-22_sumup_senior-analytics-engineer | high | high | moderate | high |

### collaboration_width (11 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | 9 | 6 | 5 | 8 |
| 2026-04-08_riverty_data-engineering-lead | 10 | 10 | 9 | 9 |
| 2026-04-09_ai-futures_data-team-lead | 1 | 2 | 2 | 2 |
| 2026-04-22_about-you_senior-data-engineer | 0 | 1 | 0 | 3 |
| 2026-04-22_mentimeter_analytics-engineer | 3 | 0 | 0 | 4 |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 3 | 2 | 3 | 3 |
| 2026-04-22_shine_senior-analytics-engineer | 2 | 2 | 3 | 2 |
| 2026-04-28_seven-senders_senior-bi-analyst | 2 | 2 | 1 | 3 |
| 2026-05-01_wolt_senior-revenue-data-analyst | 5 | 4 | 4 | 5 |
| 2026-05-09_lightdash_analytics-engineering-advocate | 0 | 2 | 0 | 3 |
| 2026-06-04_vinted_analytics-engineer-finance | 3 | 3 | 2 | 3 |

### data_team_maturity (8 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | mature | mature | mid | mid |
| 2026-04-08_riverty_data-engineering-lead | mid | mature | mid | mature |
| 2026-04-08_tem_staff-analytics-engineer | early | mid | mid | early |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | early | mid | early |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | mid | mid | mature | mid |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mid | mid | early | early |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | early | mid | early | early |
| 2026-04-22_qasa_analytics-engineer | mid | early | mid | early |

### jd_authorship (29 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | hiring_manager | mixed | mixed | hiring_manager |
| 2026-04-08_tem_staff-analytics-engineer | mixed | mixed | hiring_manager | hiring_manager |
| 2026-04-09_ai-futures_data-team-lead | hiring_manager | mixed | mixed | mixed |
| 2026-04-09_nkg_sustainability-data-analyst | mixed | mixed | recruiter | recruiter |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | hiring_manager | mixed | mixed |
| 2026-04-22_distribusion_analytics-engineer | recruiter | mixed | mixed | recruiter |
| 2026-04-22_distribusion_analytics-engineer | mixed | mixed | recruiter | recruiter |
| 2026-04-22_mentimeter_analytics-engineer | mixed | recruiter | mixed | hiring_manager |
| 2026-04-22_mentimeter_analytics-engineer | recruiter | mixed | hiring_manager | hiring_manager |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | hiring_manager | hiring_manager | mixed | hiring_manager |
| 2026-04-22_polyteia_analytics-engineering-lead | hiring_manager | hiring_manager | mixed | mixed |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | hiring_manager | mixed | mixed |
| 2026-04-22_qasa_analytics-engineer | recruiter | mixed | recruiter | recruiter |
| 2026-04-22_qasa_analytics-engineer | hiring_manager | hiring_manager | mixed | recruiter |
| 2026-04-22_shine_senior-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-04-22_shine_senior-analytics-engineer | mixed | mixed | hiring_manager | hiring_manager |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | recruiter | recruiter | mixed |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | mixed | hiring_manager | mixed |
| 2026-04-24_getsafe_analytics-engineer | mixed | hiring_manager | recruiter | hiring_manager |
| 2026-04-28_seven-senders_senior-bi-analyst | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-04-28_seven-senders_senior-bi-analyst | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-05-09_lightdash_analytics-engineering-advocate | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-06-04_vinted_analytics-engineer-finance | recruiter | mixed | mixed | mixed |
| 2026-06-20_adsquare_staff-data-analytics-engineer | hiring_manager | hiring_manager | recruiter | hiring_manager |
| 2026-06-20_just-dice_analytics-engineer | hiring_manager | hiring_manager | mixed | mixed |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | hiring_manager | mixed | mixed | hiring_manager |
| 2026-06-22_freenow_analytics-engineer | recruiter | mixed | mixed | hiring_manager |
| 2026-06-23_trade-republic_analytics-engineer | mixed | recruiter | hiring_manager | hiring_manager |
