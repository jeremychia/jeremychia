# LLM Classification Consistency Report

**JDs classified:** 132  
**Runs per JD:** 3  
**Model:** claude-haiku-4-5  
**Method:** claude CLI subprocess  
**Traces:** see `jd_traces/<application_id>.md` for full per-JD evidence  

---

## Inter-run agreement (LLM self-consistency)

1.00 = all three runs identical. Lower = model is uncertain on this dimension.

| Dimension | Mean | Min | Max | Fully consistent (3/3) |
|-----------|------|-----|-----|------------------------|
| velocity_vs_rigour | 0.92 | 0.00 | 1.00 | 117/132 |
| domain_risk | 0.95 | 0.33 | 1.00 | 123/132 |
| collaboration_width | 0.82 | 0.33 | 1.00 | 97/132 |
| data_team_maturity | 0.95 | 0.33 | 1.00 | 122/132 |
| jd_authorship | 0.59 | 0.00 | 1.00 | 55/132 |
| stakeholder_orientation | 0.78 | 0.00 | 1.00 | 88/132 |
| autonomy_level | 0.73 | 0.00 | 1.00 | 81/132 |

## Manual vs LLM majority-vote agreement

How often the LLM majority vote (best of 3) matches the original hand-coded classification.
High agreement → manual classifications are reproducible by the model.
Low agreement → either the codebook is ambiguous or the original call was subjective.

| Dimension | Match rate | n matched | n total |
|-----------|-----------|-----------|---------|
| velocity_vs_rigour | 34.8% | 46 | 132 |
| domain_risk | 27.3% | 36 | 132 |
| collaboration_width | 25.8% | 34 | 132 |
| data_team_maturity | 25.0% | 33 | 132 |
| jd_authorship | 28.8% | 38 | 132 |
| stakeholder_orientation | 14.4% | 19 | 132 |
| autonomy_level | 15.9% | 21 | 132 |

## Evidence quote verification

Checks whether the verbatim quote cited by the LLM actually appears in the JD text.
Failures indicate hallucinated or paraphrased evidence.

| Dimension | Run 1 pass | Run 2 pass | Run 3 pass |
|-----------|-----------|-----------|-----------|
| velocity_vs_rigour | 128/132 | 128/132 | 129/132 |
| domain_risk | 126/132 | 129/132 | 128/132 |
| collaboration_width | 67/132 | 76/132 | 68/132 |
| data_team_maturity | 124/132 | 126/132 | 126/132 |
| jd_authorship | 101/132 | 108/132 | 105/132 |
| stakeholder_orientation | 114/132 | 115/132 | 118/132 |
| autonomy_level | 123/132 | 122/132 | 120/132 |

## Disagreements: manual vs LLM majority vote

Each disagreement is a candidate for codebook revision or reclassification.
See `jd_traces/<application_id>.md` for full reasoning on each case.

### velocity_vs_rigour (13 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Establish data quality standards using tests, CI/CD, and documentation. |
| 2026-04-09_ai-futures_data-team-lead | velocity | rigour | velocity | rigour | rigour | Building infrastructure that powers 'AI-driven pricing, payments, and financial decisioning across connected vehicle eco… |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Code complex business logic (royalties, taxable turnover, margins) |
| 2026-04-22_about-you_senior-data-engineer | mixed | rigour | rigour | rigour | rigour | Strong software engineering fundamentals (CI/CD, testing, design patterns) |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mixed | rigour | rigour | rigour | rigour | Creating and maintaining a 'Finance Single Source of Truth' covering revenue, COGS, logistics costs, and EBITDA |
| 2026-04-22_qasa_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-24_getsafe_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Design clean, reliable, and well-documented data models as a single source of truth |
| 2026-05-09_lightdash_analytics-engineering-advocate | velocity | mixed | rigour | mixed | mixed | You'll balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process impro… |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | mixed | rigour | rigour | rigour | rigour | Take full ownership of the stability of our marketing data pipelines — be the first to respond to incidents and drive re… |
| 2026-06-20_almedia_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Apply software engineering practices to analytics code, including version control, testing, and continuous integration. |
| 2026-06-20_just-dice_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data quality and validation processes to guarantee data accuracy and consistency. |
| 2026-06-23_trade-republic_analytics-engineer | mixed | mixed | rigour | rigour | rigour | Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and … |
| 2026-06-29_fullenrich_analytics-engineer | mixed | rigour | rigour | velocity | rigour | les fondations sont ultra-propres, documentées et testées |

### domain_risk (23 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | high | moderate | moderate | moderate | moderate | Design and maintain core dbt models representing business areas like customers, revenue, and operations. |
| 2026-04-09_nkg_sustainability-data-analyst | high | moderate | high | moderate | moderate | Develop and implement a unified sustainability data platform integrating multiple sources |
| 2026-04-22_distribusion_analytics-engineer | high | moderate | moderate | moderate | moderate | Exposure to major clients like Booking.com and Google Maps |
| 2026-04-22_statista_analytics-engineer-reporting-platform | low | moderate | moderate | moderate | moderate | Support documentation and governance efforts to improve maintainability and trust in reporting assets |
| 2026-04-24_getsafe_analytics-engineer | high | high | moderate | moderate | moderate | Own and evolve core business metrics - from definition to tracking and operationalisation |
| 2026-05-09_lightdash_analytics-engineering-advocate | low | moderate | moderate | moderate | moderate | help teams with everything from building dashboards and writing SQL to analytics engineering best practices and data mod… |
| 2026-06-04_vinted_analytics-engineer-finance | high | moderate | moderate | moderate | moderate | Converting Finance requirements into technical solutions through requirements gathering |
| 2026-06-20_adsquare_staff-data-analytics-engineer | high | moderate | moderate | moderate | moderate | Build data products leveraging location signals and audience attributes |
| 2026-06-22_scoot_senior-analyst-business-intelligence | high | moderate | moderate | moderate | moderate | Distil complex data into meaningful business insights to facilitate decision-making and forward planning. |
| 2026-05-11_helmes_team-lead | low | moderate | moderate | moderate | moderate | Manage finances (billing, reporting) |
| 2026-06-23_trade-republic_analytics-engineer | high | moderate | moderate | moderate | moderate | Working closely with product and business stakeholders to define and build meaningful product metrics |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | high | moderate | moderate | moderate | moderate | Analyze revenue impacts of product and process changes |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | high | moderate | moderate | moderate | moderate | Analyze revenue impacts of product and process changes |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | high | moderate | moderate | moderate | moderate | Analyze revenue impacts of product and process changes |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | high | moderate | moderate | moderate | moderate | Analyze revenue impacts of product and process changes |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | high | moderate | moderate | moderate | moderate | Analyze revenue impacts of product and process changes |
| 2026-06-29_mts-globe_finance-bi-analyst | high | moderate | moderate | moderate | moderate | Collaborating closely with financial teams to support them in their reporting processes and daily operations. |
| 2026-06-29_mts-globe_finance-bi-analyst | high | moderate | moderate | moderate | moderate | Collaborating closely with financial teams to support them in their reporting processes and daily operations. |
| 2026-06-29_mts-globe_finance-bi-analyst | high | moderate | moderate | moderate | moderate | Collaborating closely with financial teams to support them in their reporting processes and daily operations. |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | high | moderate | moderate | moderate | moderate | public social security institution managing unemployment, career interruption, and time credit services |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | high | moderate | moderate | moderate | moderate | public social security institution managing unemployment, career interruption, and time credit services in Belgium |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | high | moderate | moderate | moderate | moderate | Conducting data validation to ensure quality and usability |
| 2026-06-30_finom_senior-analytics-engineer | high | moderate | high | moderate | moderate | Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation — partner with data consu… |

### collaboration_width (25 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | 8 | 6 | 5 | 5 | 5 | Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office; Shopper & Partner (D2C & B2B)… |
| 2026-04-09_nkg_sustainability-data-analyst | 2 | 0 | 0 | 0 | 0 | Strong cross-functional collaboration abilities |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 4 | 0 | 1 | 1 | 1 | Design and maintain dashboards for franchisees and internal teams |
| 2026-04-22_about-you_senior-data-engineer | 3 | 0 | 1 | 0 | 0 | other data teams; other departments |
| 2026-04-22_distribusion_analytics-engineer | 3 | 0 | 0 | 0 | 0 | Collaborative international team environment |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 3 | 3 | 3 | 3 | Partner with data platform, engineering, and analytics teams on high-performance pipelines |
| 2026-04-22_mentimeter_analytics-engineer | 4 | 3 | 3 | 0 | 3 | Business acumen covering sales, marketing, and product analytics |
| 2026-04-22_qasa_analytics-engineer | 5 | 6 | 6 | 6 | 6 | Product; Marketing; Finance; Support; Country Management; engineering |
| 2026-04-22_statista_analytics-engineer-reporting-platform | 4 | 0 | 0 | 0 | 0 | Be the first point of contact for administration topics around the reporting platform, e.g. architecture questions, perm… |
| 2026-04-28_seven-senders_senior-bi-analyst | 3 | 2 | 1 | 1 | 1 | junior analysts; engineering |
| 2026-05-01_aviv-group_senior-analytics-engineer | 4 | 2 | 2 | 2 | 2 | analysts; data scientists |
| 2026-05-01_wolt_senior-revenue-data-analyst | 5 | 5 | 4 | 4 | 4 | Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements; Cross-functional co… |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | 2 | 0 | 0 | 0 | 0 | No named partner teams identified in the responsibilities section |
| 2026-05-09_lightdash_analytics-engineering-advocate | 3 | 0 | 0 | 0 | 0 | None identified |
| 2026-05-11_getyourguide_data-engineer | 3 | 2 | 2 | 1 | 2 | Product and Data teams |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 5 | 4 | 4 | 4 | 4 | data analysts; engineers; software engineers; marketing teams |
| 2026-06-20_adsquare_staff-data-analytics-engineer | 3 | 0 | 0 | 0 | 0 | driving cross-squad collaboration |
| 2026-06-20_almedia_analytics-engineer | 4 | 2 | 2 | 2 | 2 | Product Analysts; Data Scientists |
| 2026-06-20_just-dice_analytics-engineer | 2 | 3 | 3 | 3 | 3 | tech and product teams; marketing and product teams |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | 3 | 0 | 0 | 0 | 0 |  |
| 2026-06-22_freenow_analytics-engineer | 4 | 3 | 3 | 3 | 3 | Engage with analysts and scientists to understand problems and translate them into data solutions; Work with developers … |
| 2026-06-22_scoot_senior-analyst-business-intelligence | 2 | 0 | 0 | 0 | 0 |  |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | 3 | 2 | 2 | 2 | 2 | Analytics Consulting; DWH team |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | 3 | 0 | 0 | 0 | 0 | cross-functional alignment |
| 2026-06-23_trade-republic_analytics-engineer | 2 | 2 | 1 | 1 | 1 | product and business stakeholders |

### data_team_maturity (26 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_riverty_data-engineering-lead | mature | mid | mid | mid | mid | Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platfor… |
| 2026-04-08_tem_staff-analytics-engineer | early | mid | mid | mid | mid | This hands-on, individual contributor position focuses on building the analytics foundation. |
| 2026-04-09_ai-futures_data-team-lead | early | mid | mid | mid | mid | Growing and mentoring a data engineering team and contributing to hiring decisions |
| 2026-04-09_lovable_analytics-engineer-finance | early | mid | mid | mid | mid | Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics |
| 2026-04-09_nkg_sustainability-data-analyst | early | mid | mid | mid | mid | Design and operate scalable data pipelines within Microsoft Fabric |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | early | mid | early | mid | mid | Early-stage opportunity to build and structure analytics capabilities |
| 2026-04-22_distribusion_analytics-engineer | early | mid | mid | mid | mid | Become proficient with the data lake, understanding data sources and processing workflows |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | early | mid | mid | early | mid | Comfort navigating uncertainty and bringing structure to developing systems |
| 2026-04-22_qasa_analytics-engineer | early | mid | mid | mid | mid | Create self-serve analytics capabilities that empower teams to independently answer questions |
| 2026-04-24_getsafe_analytics-engineer | early | mid | mid | mid | mid | Build and maintain scalable data pipelines and data marts using modern tooling |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | early | mature | mature | mid | mature | Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material |
| 2026-05-09_lightdash_analytics-engineering-advocate | early | mid | mature | mature | mature | using Lightdash for our own analytics and demos |
| 2026-05-11_getyourguide_data-engineer | mature | mid | mid | mid | mid | Improve what's already in production: Pragmatically refactor and simplify existing pipelines |
| 2026-06-20_adsquare_staff-data-analytics-engineer | mature | mid | mid | mid | mid | Establish monitoring frameworks for multi-terabyte data streams |
| 2026-06-20_just-dice_analytics-engineer | early | mid | mid | mid | mid | Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services. |
| 2026-06-22_freenow_analytics-engineer | mature | mid | mature | mid | mid | develop new data products within a Data Mesh environment |
| 2026-06-22_scoot_senior-analyst-business-intelligence | early | mid | mid | mid | mid | Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions. |
| 2026-06-22_sumup_senior-analytics-engineer | mature | mid | mid | mid | mid | helping establish durable ownership, consistent definitions, and a shared catalogue of data products |
| 2026-05-11_helmes_team-lead | early | mid | mid | mid | mid | Lead software development teams and projects |
| 2026-06-29_mts-globe_finance-bi-analyst | early | mid | mid | mid | mid | Provide trainings and support to the business community to ensure a good adoption and usage of our tools. |
| 2026-06-29_mts-globe_finance-bi-analyst | early | mid | mid | mid | mid | Provide trainings and support to the business community to ensure a good adoption and usage of our tools. |
| 2026-06-29_mts-globe_finance-bi-analyst | early | mid | mid | mid | mid | Provide trainings and support to the business community to ensure a good adoption and usage of our tools. |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | mature | mid | mid | mid | mid | Developing stratified transformation logic with dbt, focused on maintainability, performance and profitability |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | mature | mid | mid | mid | mid | Implementing data orchestration via Dagster for reliable delivery |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | mature | mid | mid | mid | mid | Developing stratified transformation logic with dbt, focused on maintainability, performance and profitability |
| 2026-06-30_finom_senior-analytics-engineer | early | mid | early | mid | mid | Newly formed Data Team building a Data Delivery Platform on Databricks |

### jd_authorship (21 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-09_ai-futures_data-team-lead | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Designing and building a modern data platform for 'high-volume, real-time vehicle and transaction data' using Python and… |
| 2026-04-09_lovable_analytics-engineer-finance | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | recruiter | mixed | mixed | mixed | Gather requirements and translate them into effective reporting and analytics solutions |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | mixed | hiring_manager | hiring_manager | hiring_manager | Build data marts and business layers using dbt on Databricks; Code complex business logic (royalties, taxable turnover, … |
| 2026-04-22_distribusion_analytics-engineer | recruiter | mixed | mixed | hiring_manager | mixed | Build new Looker dashboards from scratch within tight deadlines |
| 2026-04-22_mentimeter_analytics-engineer | hiring_manager | mixed | mixed | recruiter | mixed | Experience using AI-assisted coding or coding agents in a disciplined way (reviews, tests, documentation) |
| 2026-04-22_qasa_analytics-engineer | recruiter | mixed | recruiter | mixed | mixed | Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams |
| 2026-04-24_getsafe_analytics-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Develop the data and analytics components of the AI stack to support experimentation and GenAI applications |
| 2026-05-01_aviv-group_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake |
| 2026-05-09_lightdash_analytics-engineering-advocate | hiring_manager | mixed | mixed | hiring_manager | mixed | You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on ca… |
| 2026-06-20_almedia_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Design, build, and maintain clean, scalable, and performance-optimised data models using SQL and dbt. |
| 2026-06-20_just-dice_analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services; Create and maintain dat… |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | hiring_manager | mixed | hiring_manager | mixed | mixed | Design and implement complex data pipelines with dependency control and orchestration |
| 2026-06-22_freenow_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Own the quality, availability, and trustworthiness of data — through quality checks and data contracts |
| 2026-06-22_scoot_senior-analyst-business-intelligence | recruiter | mixed | mixed | mixed | mixed | Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google… |
| 2026-06-23_trade-republic_analytics-engineer | hiring_manager | recruiter | mixed | recruiter | recruiter | Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and a… |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Orquestación de pipelines: Gestionar workflows de datos mediante Airflow (Cloud Composer); Modelado de datos: Desarrolla… |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | recruiter | mixed | recruiter | hiring_manager | mixed | Analyse complex data using SQL and Python; Partner with stakeholders to understand business problems |
| 2026-06-29_fullenrich_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed | mixed | calcul de l'économie unitaire/marges par fournisseur de données, scoring d'activation produit, prédiction du churn |
| 2026-06-29_irium-portugal_senior-analytics-engineer | mixed | hiring_manager | recruiter | mixed | hiring_manager | Build and optimize ELT pipelines and quality tests |
| 2026-06-29_irium-portugal_senior-analytics-engineer | mixed | recruiter | hiring_manager | hiring_manager | hiring_manager | Cross-functional collaboration with Data Engineering and Product teams |

### stakeholder_orientation (3 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | internal_data | finance | internal_data | finance | finance | Financial services knowledge (P&L, FX, reconciliation concepts) |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | internal_data | finance | finance | internal_data | finance | Financial services knowledge (P&L, FX, reconciliation concepts) |
| 2026-06-29_fullenrich_analytics-engineer | commercial | internal_data | internal_data | mixed | internal_data | Structurer les couches de données, pousser plus loin les modèles dbt et automatiser pour que chaque équipe (Sales, Marke… |

### autonomy_level (1 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | mixed | strategic | mixed | strategic | strategic | Visión estratégica y ejecución técnica: Capacidad de alternar entre la definición de roadmaps multi-dominio y la resoluc… |

## LLM internal inconsistencies (runs disagree with each other)

These are cases where the same prompt produced different answers across 3 runs.
High inconsistency → borderline case or ambiguous JD language.

### velocity_vs_rigour (15 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-09_ai-futures_data-team-lead | rigour | velocity | rigour | velocity |
| 2026-04-22_distribusion_analytics-engineer | mixed | velocity | mixed | mixed |
| 2026-05-09_lightdash_analytics-engineering-advocate | mixed | rigour | mixed | velocity |
| 2026-06-23_trade-republic_analytics-engineer | mixed | rigour | rigour | mixed |
| 2026-06-25_uplearn_head-of-data | mixed | rigour | mixed |  |
| 2026-06-27_doodle_growth-analytics-engineer | rigour | velocity | rigour |  |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | mixed | rigour | rigour |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | velocity | rigour | rigour |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | velocity | rigour | rigour |  |
| 2026-06-29_fullenrich_analytics-engineer | rigour | rigour | velocity | mixed |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | rigour | velocity | rigour |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | rigour | velocity | rigour |  |
| 2026-06-29_fullenrich_analytics-engineer | rigour | mixed | mixed | mixed |
| 2026-06-30_doodle_growth-analytics-engineer | rigour | mixed | velocity |  |
| 2026-06-30_doodle_growth-analytics-engineer | rigour | velocity | rigour |  |

### domain_risk (9 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-09_nkg_sustainability-data-analyst | moderate | high | moderate | high |
| 2026-04-22_about-you_senior-data-engineer | moderate | high | high | high |
| 2026-04-24_getsafe_analytics-engineer | high | moderate | moderate | high |
| 2026-06-22_sumup_senior-analytics-engineer | moderate | high | high | high |
| 2026-06-25_uplearn_head-of-data | moderate | high | high |  |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | high | high | moderate |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | moderate | high | moderate |  |
| 2026-06-30_finom_senior-analytics-engineer | high | moderate | moderate |  |
| 2026-06-30_finom_senior-analytics-engineer | moderate | high | moderate |  |

### collaboration_width (35 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | 6 | 5 | 5 | 8 |
| 2026-04-08_riverty_data-engineering-lead | 9 | 10 | 9 | 9 |
| 2026-04-09_ai-futures_data-team-lead | 0 | 2 | 2 | 2 |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 0 | 1 | 1 | 4 |
| 2026-04-22_about-you_senior-data-engineer | 0 | 1 | 0 | 3 |
| 2026-04-22_mentimeter_analytics-engineer | 3 | 3 | 0 | 4 |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 3 | 3 | 2 | 3 |
| 2026-04-22_polyteia_analytics-engineering-lead | 2 | 1 | 2 | 2 |
| 2026-04-22_shine_senior-analytics-engineer | 3 | 2 | 2 | 2 |
| 2026-04-28_seven-senders_senior-bi-analyst | 2 | 1 | 1 | 3 |
| 2026-05-01_wolt_senior-revenue-data-analyst | 5 | 4 | 4 | 5 |
| 2026-05-11_getyourguide_data-engineer | 2 | 2 | 1 | 3 |
| 2026-06-23_trade-republic_analytics-engineer | 2 | 1 | 1 | 2 |
| 2026-06-25_uplearn_head-of-data | 4 | 3 | 3 |  |
| 2026-06-27_decathlon-digital_senior-analytics-engineer | 0 | 0 | 2 |  |
| 2026-06-27_lansweeper_revenue-analytics-engineer | 4 | 4 | 2 |  |
| 2026-06-27_lego-group_analytics-engineer | 5 | 5 | 9 |  |
| 2026-06-27_m13h_lead-analytics-engineer | 3 | 2 | 3 |  |
| 2026-06-27_netflix_analytics-engineer-l5-localization | 5 | 4 | 4 |  |
| 2026-06-27_protolabs_senior-analytics-engineer | 1 | 0 | 1 |  |
| 2026-06-27_vestas_analytics-engineer | 3 | 3 | 4 |  |
| 2026-06-29_bip_business-intelligence-specialist | 6 | 6 | 5 |  |
| 2026-06-29_bip_business-intelligence-specialist | 5 | 5 | 6 |  |
| 2026-06-29_fullenrich_analytics-engineer | 5 | 5 | 4 | 5 |
| 2026-06-29_fullenrich_analytics-engineer | 4 | 5 | 5 | 5 |
| 2026-06-30_doodle_growth-analytics-engineer | 1 | 0 | 0 |  |
| 2026-06-30_cosuno_senior-analytics-engineer | 2 | 0 | 0 |  |
| 2026-06-30_bitac-gmbh_business-intelligence-spezialist | 1 | 1 | 2 |  |
| 2026-06-30_bitac-gmbh_business-intelligence-spezialist | 2 | 1 | 1 |  |
| 2026-06-30_cosuno_senior-analytics-engineer | 0 | 1 | 0 |  |
| 2026-06-30_doodle_growth-analytics-engineer | 0 | 0 | 2 |  |
| 2026-06-30_doodle_growth-analytics-engineer | 0 | 0 | 2 |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | 5 | 6 | 6 |  |
| 2026-06-30_louis-dreyfus-company_data-analytics-engineer-finance-systems | 3 | 4 | 4 |  |
| 2026-06-30_van-in-sanoma_business-intelligence-analyst | 1 | 0 | 1 |  |

### data_team_maturity (10 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | early | mid | early |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mid | mid | early | early |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | mature | mature | mid | early |
| 2026-05-09_lightdash_analytics-engineering-advocate | mid | mature | mature | early |
| 2026-06-22_freenow_analytics-engineer | mid | mature | mid | mature |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | mid | mature | mid | mid |
| 2026-06-27_lego-group_analytics-engineer | mid | mid | mature |  |
| 2026-06-29_fullenrich_analytics-engineer | mid | early | early | early |
| 2026-06-29_irium-portugal_senior-analytics-engineer | mid | mature | mid | mid |
| 2026-06-30_finom_senior-analytics-engineer | mid | early | mid |  |

### jd_authorship (77 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_riverty_data-engineering-lead | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-04-09_ai-futures_data-team-lead | hiring_manager | mixed | hiring_manager | mixed |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | mixed | mixed | recruiter |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | hiring_manager | hiring_manager | mixed |
| 2026-04-22_distribusion_analytics-engineer | mixed | mixed | hiring_manager | recruiter |
| 2026-04-22_mentimeter_analytics-engineer | mixed | mixed | recruiter | hiring_manager |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | mixed | hiring_manager | mixed |
| 2026-04-22_qasa_analytics-engineer | mixed | recruiter | mixed | recruiter |
| 2026-04-22_shine_senior-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | recruiter | mixed | mixed |
| 2026-04-24_getsafe_analytics-engineer | mixed | mixed | hiring_manager | hiring_manager |
| 2026-05-01_wolt_senior-revenue-data-analyst | mixed | mixed | hiring_manager | mixed |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | hiring_manager | mixed | recruiter | hiring_manager |
| 2026-05-09_lightdash_analytics-engineering-advocate | mixed | mixed | hiring_manager | hiring_manager |
| 2026-05-11_getyourguide_data-engineer | hiring_manager | mixed | recruiter | hiring_manager |
| 2026-06-04_vinted_analytics-engineer-finance | mixed | recruiter | hiring_manager | mixed |
| 2026-06-20_adsquare_staff-data-analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-06-20_almedia_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | mixed | hiring_manager | mixed | hiring_manager |
| 2026-06-22_sumup_senior-analytics-engineer | hiring_manager | hiring_manager | mixed | hiring_manager |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | mixed | recruiter | mixed | mixed |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | hiring_manager | mixed | mixed | mixed |
| 2026-06-23_trade-republic_analytics-engineer | recruiter | mixed | recruiter | hiring_manager |
| 2026-06-25_egnyte_analytics-engineer | mixed | mixed | recruiter |  |
| 2026-06-25_marie-stella-maris_data-integration-engineer | hiring_manager | mixed | hiring_manager |  |
| 2026-06-25_uplearn_head-of-data | hiring_manager | mixed | hiring_manager |  |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | mixed | hiring_manager | hiring_manager |  |
| 2026-06-27_bolt_senior-analytics-engineer | hiring_manager | mixed | mixed |  |
| 2026-06-27_dashlane_analytics-engineer | mixed | hiring_manager | mixed |  |
| 2026-06-27_datenna_senior-analytics-engineer | hiring_manager | mixed | mixed |  |
| 2026-06-27_decathlon-digital_senior-analytics-engineer | hiring_manager | mixed | mixed |  |
| 2026-06-27_doodle_growth-analytics-engineer | recruiter | hiring_manager | recruiter |  |
| 2026-06-27_dynatrace_senior-analytics-engineer | hiring_manager | mixed | mixed |  |
| 2026-06-27_eraneos_analytics-engineer | hiring_manager | hiring_manager | mixed |  |
| 2026-06-27_lego-group_analytics-engineer | mixed | hiring_manager | mixed |  |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | hiring_manager | hiring_manager | mixed |  |
| 2026-06-27_mr-marvis_senior-analytics-engineer | mixed | mixed | hiring_manager |  |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | mixed | hiring_manager | mixed |  |
| 2026-06-27_preply_senior-analytics-engineer | hiring_manager | mixed | hiring_manager |  |
| 2026-06-27_sisu-group_senior-analytics-engineer | mixed | mixed | recruiter |  |
| 2026-06-27_spotify_analytics-engineer-ii | mixed | hiring_manager | mixed |  |
| 2026-06-27_vestas_analytics-engineer | recruiter | mixed | mixed |  |
| 2026-06-27_vinted_area-lead-analytics-engineer | mixed | mixed | recruiter |  |
| 2026-06-27_welcome-to-the-jungle_senior-analytics-engineer | hiring_manager | recruiter | mixed |  |
| 2026-06-27_yuri-neil_analytics-engineer | hiring_manager | hiring_manager | mixed |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | hiring_manager | recruiter | recruiter |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | hiring_manager | hiring_manager | mixed |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | mixed | mixed | hiring_manager |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | hiring_manager | hiring_manager | mixed |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | recruiter | mixed | mixed |  |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | recruiter | mixed | recruiter |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | recruiter | recruiter | mixed |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | mixed | hiring_manager | mixed |  |
| 2026-06-29_bip_business-intelligence-specialist | mixed | mixed | hiring_manager |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | mixed | recruiter | hiring_manager |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | recruiter | recruiter | mixed |  |
| 2026-06-29_bip_business-intelligence-specialist | mixed | hiring_manager | mixed |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | mixed | recruiter | hiring_manager |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | hiring_manager | mixed | mixed |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | recruiter | recruiter | mixed |  |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | hiring_manager | recruiter | recruiter |  |
| 2026-06-29_fullenrich_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | hiring_manager | recruiter | recruiter |  |
| 2026-06-29_irium-portugal_senior-analytics-engineer | mixed | mixed | hiring_manager | mixed |
| 2026-06-29_irium-portugal_senior-analytics-engineer | hiring_manager | recruiter | mixed | mixed |
| 2026-06-29_irium-portugal_senior-analytics-engineer | recruiter | hiring_manager | hiring_manager | mixed |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-06-30_doodle_growth-analytics-engineer | recruiter | recruiter | mixed |  |
| 2026-06-30_doodle_growth-analytics-engineer | recruiter | hiring_manager | recruiter |  |
| 2026-06-30_doodle_growth-analytics-engineer | recruiter | mixed | mixed |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | mixed | mixed | recruiter |  |
| 2026-06-30_finom_senior-analytics-engineer | mixed | hiring_manager | mixed |  |
| 2026-06-30_finom_senior-analytics-engineer | mixed | mixed | hiring_manager |  |
| 2026-06-30_avalanche-studios_senior-analytics-engineer | recruiter | recruiter | mixed |  |
| 2026-06-30_louis-dreyfus-company_data-analytics-engineer-finance-systems | mixed | mixed | recruiter |  |
| 2026-06-30_plain-concepts_bi-specialist | mixed | recruiter | recruiter |  |
| 2026-06-30_van-in-sanoma_business-intelligence-analyst | hiring_manager | mixed | mixed |  |

### stakeholder_orientation (44 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | internal_data | commercial | commercial |  |
| 2026-04-09_ai-futures_data-team-lead | internal_data | product | internal_data |  |
| 2026-04-22_about-you_senior-data-engineer | internal_data | internal_data | mixed |  |
| 2026-04-22_qasa_analytics-engineer | mixed | internal_data | internal_data |  |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | internal_data | mixed | internal_data |  |
| 2026-05-09_lightdash_analytics-engineering-advocate | internal_data | commercial | commercial |  |
| 2026-05-11_getyourguide_data-engineer | internal_data | internal_data | product |  |
| 2026-05-13_smoobu_senior-analytics-engineer | internal_data | internal_data | mixed |  |
| 2026-06-20_just-dice_analytics-engineer | product | mixed | product |  |
| 2026-06-22_scoot_senior-analyst-business-intelligence | internal_data | internal_data | mixed |  |
| 2026-06-25_dashlane_analytics-engineer | mixed | internal_data | internal_data |  |
| 2026-06-25_uplearn_head-of-data | product | mixed | mixed |  |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | internal_data | mixed | internal_data |  |
| 2026-06-27_blue-orange-digital_analytics-engineer-power-bi-specialist | finance | finance | mixed |  |
| 2026-06-27_lansweeper_revenue-analytics-engineer | mixed | finance | mixed |  |
| 2026-06-27_lego-group_analytics-engineer | commercial | commercial | internal_data |  |
| 2026-06-27_netflix_analytics-engineer-l5-localization | mixed | product | product |  |
| 2026-06-27_preply_senior-analytics-engineer | product | product | internal_data |  |
| 2026-06-27_sisu-group_senior-analytics-engineer | internal_data | commercial | finance |  |
| 2026-06-27_sosafe_senior-analytics-engineer | product | internal_data | internal_data |  |
| 2026-06-27_spotify_analytics-engineer-ii | product | internal_data | internal_data |  |
| 2026-06-27_vestas_analytics-engineer | finance | finance | internal_data |  |
| 2026-06-27_yuri-neil_analytics-engineer | mixed | mixed | internal_data |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | internal_data | mixed | internal_data |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | finance | finance | internal_data |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | internal_data | finance | finance |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | internal_data | internal_data | finance |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | internal_data | internal_data | finance |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | internal_data | mixed | internal_data |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | finance | internal_data | finance |  |
| 2026-06-29_bip_business-intelligence-specialist | commercial | commercial | internal_data |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | internal_data | internal_data | finance |  |
| 2026-06-29_bip_business-intelligence-specialist | mixed | commercial | commercial |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | finance | finance | internal_data |  |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | internal_data | mixed | internal_data |  |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | internal_data | mixed | internal_data |  |
| 2026-06-29_fullenrich_analytics-engineer | internal_data | internal_data | mixed | commercial |
| 2026-06-29_fullenrich_analytics-engineer | internal_data | internal_data | mixed | commercial |
| 2026-06-30_doodle_growth-analytics-engineer | mixed | mixed | commercial |  |
| 2026-06-30_cosuno_senior-analytics-engineer | internal_data | mixed | internal_data |  |
| 2026-06-30_bitac-gmbh_business-intelligence-spezialist | mixed | internal_data | mixed |  |
| 2026-06-30_cosuno_senior-analytics-engineer | mixed | mixed | internal_data |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | internal_data | mixed | mixed |  |
| 2026-06-30_limeflight_senior-data-analytics-engineer | internal_data | product | internal_data |  |

### autonomy_level (51 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | strategic | strategic | execution |  |
| 2026-04-08_tem_staff-analytics-engineer | mixed | strategic | strategic |  |
| 2026-04-09_lovable_analytics-engineer-finance | execution | execution | mixed |  |
| 2026-04-22_distribusion_analytics-engineer | mixed | execution | execution |  |
| 2026-04-22_qasa_analytics-engineer | strategic | strategic | execution |  |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | mixed | execution |  |
| 2026-04-24_getsafe_analytics-engineer | strategic | mixed | strategic |  |
| 2026-04-28_seven-senders_senior-bi-analyst | execution | execution | strategic |  |
| 2026-05-01_aviv-group_senior-analytics-engineer | mixed | execution | mixed |  |
| 2026-05-09_lightdash_analytics-engineering-advocate | execution | mixed | mixed |  |
| 2026-05-11_getyourguide_data-engineer | execution | mixed | execution |  |
| 2026-05-13_smoobu_senior-analytics-engineer | mixed | strategic | strategic |  |
| 2026-06-04_vinted_analytics-engineer-finance | execution | mixed | execution |  |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | execution | execution | mixed |  |
| 2026-05-11_helmes_team-lead | mixed | strategic | execution |  |
| 2026-06-23_trade-republic_analytics-engineer | mixed | strategic | mixed |  |
| 2026-06-25_blue-orange-digital_analytics-engineer-power-bi-specialist | execution | mixed | strategic |  |
| 2026-06-25_telavox_analytics-engineer | strategic | mixed | strategic |  |
| 2026-06-27_blue-orange-digital_analytics-engineer-power-bi-specialist | execution | mixed | execution |  |
| 2026-06-27_bolt_senior-analytics-engineer | mixed | mixed | strategic |  |
| 2026-06-27_dashlane_analytics-engineer | mixed | mixed | strategic |  |
| 2026-06-27_doodle_growth-analytics-engineer | mixed | strategic | strategic |  |
| 2026-06-27_lansweeper_revenue-analytics-engineer | mixed | execution | strategic |  |
| 2026-06-27_lego-group_analytics-engineer | mixed | execution | mixed |  |
| 2026-06-27_m13h_lead-analytics-engineer | mixed | execution | mixed |  |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | mixed | strategic | mixed |  |
| 2026-06-27_mr-marvis_senior-analytics-engineer | mixed | strategic | mixed |  |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | execution | execution | strategic |  |
| 2026-06-27_perk_analytics-engineer | mixed | execution | execution |  |
| 2026-06-27_vinted_area-lead-analytics-engineer | strategic | strategic | mixed |  |
| 2026-06-27_welcome-to-the-jungle_senior-analytics-engineer | strategic | mixed | mixed |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | mixed | strategic | mixed |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | strategic | mixed | mixed |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | mixed | strategic | mixed |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | strategic | mixed | mixed |  |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | execution | mixed | execution |  |
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | strategic | mixed | strategic |  |
| 2026-06-29_experis-uk_analytics-engineer-data-analyst | execution | execution | strategic |  |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | execution | mixed | execution |  |
| 2026-06-29_irium-portugal_senior-analytics-engineer | mixed | execution | execution | execution |
| 2026-06-30_doodle_growth-analytics-engineer | mixed | mixed | strategic |  |
| 2026-06-30_cosuno_senior-analytics-engineer | execution | mixed | strategic |  |
| 2026-06-30_cosuno_senior-analytics-engineer | mixed | strategic | strategic |  |
| 2026-06-30_cosuno_senior-analytics-engineer | execution | mixed | execution |  |
| 2026-06-30_doodle_growth-analytics-engineer | strategic | strategic | mixed |  |
| 2026-06-30_doodle_growth-analytics-engineer | strategic | strategic | mixed |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | strategic | mixed | mixed |  |
| 2026-06-30_finom_senior-analytics-engineer | strategic | mixed | mixed |  |
| 2026-06-30_limeflight_senior-data-analytics-engineer | mixed | strategic | strategic |  |
| 2026-06-30_plain-concepts_bi-specialist | mixed | execution | mixed |  |
| 2026-06-30_van-in-sanoma_business-intelligence-analyst | mixed | execution | mixed |  |
