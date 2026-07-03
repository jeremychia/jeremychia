# LLM Classification Consistency Report

**JDs classified:** 131  
**Runs per JD:** 3  
**Model:** claude-haiku-4-5  
**Method:** claude CLI subprocess  
**Traces:** see `jd_traces/<application_id>.md` for full per-JD evidence  

---

## Inter-run agreement (LLM self-consistency)

1.00 = all three runs identical. Lower = model is uncertain on this dimension.

| Dimension | Mean | Min | Max | Fully consistent (3/3) |
|-----------|------|-----|-----|------------------------|
| velocity_vs_rigour | 0.94 | 0.33 | 1.00 | 84/93 |
| domain_risk | 0.95 | 0.33 | 1.00 | 86/93 |
| collaboration_width | 0.81 | 0.33 | 1.00 | 67/93 |
| data_team_maturity | 0.94 | 0.33 | 1.00 | 85/93 |
| jd_authorship | 0.58 | 0.00 | 1.00 | 37/93 |
| stakeholder_orientation | 0.78 | 0.00 | 1.00 | 63/93 |
| autonomy_level | 0.72 | 0.00 | 1.00 | 56/93 |

## Manual vs LLM majority-vote agreement

How often the LLM majority vote (best of 3) matches the original hand-coded classification.
High agreement → manual classifications are reproducible by the model.
Low agreement → either the codebook is ambiguous or the original call was subjective.

| Dimension | Match rate | n matched | n total |
|-----------|-----------|-----------|---------|
| velocity_vs_rigour | 34.4% | 32 | 93 |
| domain_risk | 31.2% | 29 | 93 |
| collaboration_width | 20.4% | 19 | 93 |
| data_team_maturity | 23.7% | 22 | 93 |
| jd_authorship | 29.0% | 27 | 93 |
| stakeholder_orientation | 6.5% | 6 | 93 |
| autonomy_level | 7.5% | 7 | 93 |

## Evidence quote verification

Checks whether the verbatim quote cited by the LLM actually appears in the JD text.
Failures indicate hallucinated or paraphrased evidence.

| Dimension | Run 1 pass | Run 2 pass | Run 3 pass |
|-----------|-----------|-----------|-----------|
| velocity_vs_rigour | 89/131 | 90/131 | 90/131 |
| domain_risk | 88/131 | 91/131 | 91/131 |
| collaboration_width | 44/131 | 49/131 | 45/131 |
| data_team_maturity | 86/131 | 89/131 | 87/131 |
| jd_authorship | 72/131 | 76/131 | 71/131 |
| stakeholder_orientation | 77/131 | 79/131 | 83/131 |
| autonomy_level | 85/131 | 85/131 | 83/131 |
| ai_role | — | — | — |
| testing_framing | — | — | — |
| loss_aversion_framing | — | — | — |

## Disagreements: manual vs LLM majority vote

Each disagreement is a candidate for codebook revision or reclassification.
See `jd_traces/<application_id>.md` for full reasoning on each case.

### velocity_vs_rigour (12 disagreements)

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

### domain_risk (18 disagreements)

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
| 2026-06-29_mts-globe_finance-bi-analyst | high | moderate | moderate | moderate | moderate | Collaborating closely with financial teams to support them in their reporting processes and daily operations. |
| 2026-06-29_onem-smals_senior-data-analytics-engineer | high | moderate | moderate | moderate | moderate | Conducting data validation to ensure quality and usability |
| 2026-06-30_finom_senior-analytics-engineer | high | moderate | high | moderate | moderate | Supporting data consumers (ML engineers, analysts, stakeholders) with requirements translation — partner with data consu… |
| 2026-07-01_emagine_senior-bi-analyst | high | Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases. | No AI skill signal. | Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes. | supporting inspections, audits, data validation, and the investigation of data defects | True |
| 2026-07-02_enza-zaden_senior-analytics-engineer | low | Improving data quality, reliability, performance and cost efficiency through lifecycle management | No AI skill signal. | Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI | empower self-serve BI for teams across the organization | True |
| 2026-07-02_funke-medien_analytics-engineer | moderate | kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen | No AI skill signal. | Als Expert*in im Datawarehouse kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen | Reporting und der Marketing Automation für das Zeitungsgeschäft digital und traditionell | True |

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

### data_team_maturity (22 disagreements)

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
| 2026-06-29_onem-smals_senior-data-analytics-engineer | mature | mid | mid | mid | mid | Developing stratified transformation logic with dbt, focused on maintainability, performance and profitability |
| 2026-06-30_finom_senior-analytics-engineer | early | mid | early | mid | mid | Newly formed Data Team building a Data Delivery Platform on Databricks |

### jd_authorship (17 disagreements)

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
| 2026-06-29_irium-portugal_senior-analytics-engineer | mixed | recruiter | hiring_manager | hiring_manager | hiring_manager | Cross-functional collaboration with Data Engineering and Product teams |

### stakeholder_orientation (3 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | internal_data | finance | finance | internal_data | finance | Financial services knowledge (P&L, FX, reconciliation concepts) |
| 2026-07-02_funke-medien_analytics-engineer | commercial | Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen und bringst Deine Expertise und kreativen Losungen ein, um datenbasierte Optimierungsstrategien zu entwickeln | Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft digital und traditionell | die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen | Du entwickelst und implementierst eigenständig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools | True |
| 2026-07-02_ig-group_analytics-engineer | internal_data | Deliver the migration of business-critical dashboards to Looker, rebuilding and modelling in LookML to ensure a clean, reliable transition | turn raw data into trusted, self-serve insight that business users across IG can act on | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | Build and maintain scalable, well-documented data models in dbt that enable self-serve analytics for business users across IG; Deliver the migration of business-critical dashboards to Looker, rebuilding and modelling in LookML to ensure a clean, reliable transition | True |

### autonomy_level — no disagreements ✓

### ai_role — no disagreements ✓

### testing_framing — no disagreements ✓

### loss_aversion_framing — no disagreements ✓

## LLM internal inconsistencies (runs disagree with each other)

These are cases where the same prompt produced different answers across 3 runs.
High inconsistency → borderline case or ambiguous JD language.

### velocity_vs_rigour (47 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-09_ai-futures_data-team-lead | rigour | velocity | rigour | velocity |
| 2026-04-22_distribusion_analytics-engineer | mixed | velocity | mixed | mixed |
| 2026-05-09_lightdash_analytics-engineering-advocate | mixed | rigour | mixed | velocity |
| 2026-06-23_trade-republic_analytics-engineer | mixed | rigour | rigour | mixed |
| 2026-06-25_uplearn_head-of-data | mixed | rigour | mixed |  |
| 2026-06-27_doodle_growth-analytics-engineer | rigour | velocity | rigour |  |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | mixed | rigour | rigour |  |
| 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst | rigour | velocity | rigour | rigour |
| 2026-06-29_fullenrich_analytics-engineer | rigour | mixed | mixed |  |
| 2026-07-01_airalo_analytics-engineering-manager |  | You'll own the foundations that make analytics possible at scale... you'll establish how we model data, how we govern metrics, and how we roll out self-service capabilities | Own and evolve our core dbt models and semantic layer to support key analytical use cases | mixed |
| 2026-07-01_awin_analytical-engineer |  | Establish a single source of truth for business metric definitions | establish their analytics engineering practice within the BI team | rigour |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence |  | Collaborating with Finance and Operations on reporting needs | Contributing to the ongoing design of our core data model | rigour |
| 2026-07-01_booking-com_data-analytics-engineer-ii |  | End-to-end ownership of data quality in our core datasets and data pipelines. | Data Enablement Teams work closely with teams across the business to ensure that data is ingested, transformed and enriched into secure, high quality, well governed consumption layers. | rigour |
| 2026-07-01_darwin_senior-analytics-engineer |  | Take ownership of platform architecture, data modelling standards, and engineering best practices | first dedicated Analytics Engineer within the business | rigour |
| 2026-07-01_deloitte_analytics-engineer |  | understand challenges and translate needs into data solutions that drive business impact | Develop and optimise procedures to productionize models with monitoring capabilities | rigour |
| 2026-07-01_emagine_senior-bi-analyst |  | Support the design of data migration and integration processes, ensuring data quality and availability. | Support the design of data migration and integration processes, ensuring data quality and availability. | rigour |
| 2026-07-01_entain_analytics-engineer-bi |  | Deliver ad-hoc analysis to support decision-making | Design and maintain dbt models for the analytics semantic layer | rigour |
| 2026-07-01_finanz-informatik_bi-engineer |  | Evaluate new metrics requirements collaboratively with stakeholders | The team transforms data into actionable insights by developing metrics that enable the Sparkassen group to transparently manage processes and optimise customer journeys | rigour |
| 2026-07-01_gemma-analytics_ai-analytics-engineer |  | Apply data modelling methodologies | This is a mid-level position where engineers work at the intersection of data and AI, building both traditional data pipelines and intelligent, agentic solutions | mixed |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer |  | Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting. Own data correctness and investigate quality anomalies. | Help establish organisational adoption patterns for AI-assisted engineering | mixed |
| 2026-07-01_henkel_business-intelligence-developer |  | Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department | Play a key role in development of advanced analytical tools in Power BI | rigour |
| 2026-07-01_aptrack_senior-bi-architect |  | Define BI architecture standards, principles and best practices; Define lakehouse, data warehouse, and semantic modelling structures | Define BI architecture standards, principles and best practices | rigour |
| 2026-07-01_hovione_data-analytics-engineer |  | Strong autonomy to lead analytic solutions from design to deployment; and strong foundation in analytics framework and data management | Build, standardize, and maintain reporting and self-service analytics as part of data lake and data mesh concepts | rigour |
| 2026-07-01_hse24_junior-expert-bi-analytics |  | Conceptualise and optimise BI solutions and create KPIs; Translate business requirements into analytics deliverables | Build and maintain data models with DBT and Snowflake using dimensional modelling | rigour |
| 2026-07-01_jtl-software_senior-analytics-engineer |  | Owning the data foundation for a new AI-powered BI product | Owning the data foundation for a new AI-powered BI product | rigour |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst |  | Support data governance, data modelling, data lineage, and data integration initiatives | Develop BI reports, dashboards, KPIs, and analytical solutions using Microsoft Fabric and SQL | rigour |
| 2026-07-01_retail-consult_data-analytics-engineer |  | transform business needs into scalable, reliable, and high-quality data solutions | designing data architectures, optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines | rigour |
| 2026-07-01_size-up-consulting_senior-analytics-engineer |  | Support teams in data and decision-making tool utilisation; Participate in data governance and best practice improvements | Collaborate with Product, Data Engineering, and Business teams | rigour |
| 2026-07-01_too-good-to-go_bi-developer |  | Own technical design and development of BI products and semantic models | Replace manual reporting and Google Sheets processes with scalable solutions | rigour |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert |  | work closely with the Data Team Lead, Senior Data Engineer, and business teams | work closely with the Data Team Lead, Senior Data Engineer, and business teams to build scalable data models | rigour |
| 2026-07-02_acronis_senior-business-intelligence-analyst |  | Own end-to-end BI delivery | Drive modernization and Microsoft Fabric adoption, balancing delivery speed with reliability and operational excellence | mixed |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake |  | Defining data modelling, testing, and documentation standards | Defining data modelling, testing, and documentation standards | rigour |
| 2026-07-02_asics_senior-business-intelligence-engineer |  | Define and prioritise technical requirements that align with the overall business strategy | Directing data integration and pipeline orchestration across the organization | rigour |
| 2026-07-02_bose_data-analytics-engineer |  | Follow and contribute to analytical engineering standards and best practices under the guidance of senior team members | Follow and contribute to analytical engineering standards and best practices under the guidance of senior team members | rigour |
| 2026-07-02_bridgerpay_senior-analytics-engineer |  | Own the semantic layer, writing production-grade LookML | Proven track record building data warehouses and semantic layers from scratch | rigour |
| 2026-07-02_enza-zaden_senior-analytics-engineer |  | translate complex requirements into reliable solutions on the global data platform | design, build and maintain scalable data models and analytics products that empower self-service BI for teams across the organization | rigour |
| 2026-07-02_fullenrich_analytics-engineer |  | owning the data layer end-to-end while building foundational systems for organizational growth | This is FullEnrich's inaugural dedicated data hire | mixed |
| 2026-07-02_funke-medien_analytics-engineer |  | Du entwickelst und implementierst eigenstandig Data Pipelines | Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools | mixed |
| 2026-07-02_gerolsteiner_data-analytics-engineer |  | supporting AI-driven analytics expansion | advancing existing Business Warehouse implementations | mixed |
| 2026-07-02_ig-group_analytics-engineer |  | Translate business requirements from stakeholders across functions into efficient, trusted data models | Build and maintain scalable, well-documented data models in dbt that enable self-service analytics for business users across IG | rigour |
| 2026-07-02_ijsvogel-retail_analytics-engineer |  | translating business questions into dashboards and data solutions | designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality | rigour |
| 2026-07-02_mr-marvis_senior-analytics-engineer |  | owning the analytics layer of our data platform | owning the analytics layer of our data platform and bridging data engineering with business intelligence | rigour |
| 2026-07-02_photowall_analytics-engineer |  | Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation | Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse | mixed |
| 2026-07-02_sii-poland_data-analytics-engineer |  | Partner with stakeholders, Data Engineers, and Analysts on requirements | Build and maintain core data models using dbt for critical reporting | rigour |
| 2026-07-02_sosafe_senior-analytics-engineer |  | Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company | Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions | rigour |
| 2026-07-02_xomnia_data-analytics-engineer |  | work with business stakeholders to understand analytics needs | collaborating with data engineers | mixed |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data |  | Contributing to the design, implementation, and delivery of BI solutions | Partnering with Data Engineering teams to enhance data infrastructure | rigour |

### domain_risk (45 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-09_nkg_sustainability-data-analyst | moderate | high | moderate | high |
| 2026-04-22_about-you_senior-data-engineer | moderate | high | high | high |
| 2026-04-24_getsafe_analytics-engineer | high | moderate | moderate | high |
| 2026-06-22_sumup_senior-analytics-engineer | moderate | high | high | high |
| 2026-06-25_uplearn_head-of-data | moderate | high | high |  |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | high | high | moderate |  |
| 2026-06-30_finom_senior-analytics-engineer | moderate | high | moderate | high |
| 2026-07-01_airalo_analytics-engineering-manager | Balance rigour with delivery speed — we're still building foundations while the business moves fast | No AI skill signal. | Own and evolve our core dbt models and semantic layer to support key analytical use cases: customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting | moderate |
| 2026-07-01_awin_analytical-engineer | Establish a single source of truth for business metric definitions | Exposure to data observability or AI-readiness concepts | Design data marts with self-serve usage in mind; Coach BI Developers in Analytics Engineering best practices | moderate |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence | Ensuring high data quality of the core data layer with dbt models | No AI skill signal. | Ensuring high data quality of the core data layer with dbt models | high |
| 2026-07-01_booking-com_data-analytics-engineer-ii | End-to-end ownership of data quality in our core datasets and data pipelines. | No AI skill signal. | Use standardised tooling and procedures to work with business users to model and implement data pipelines which are performant, scalable, reliable, secure, well governed with required observability. | high |
| 2026-07-01_darwin_senior-analytics-engineer | Take ownership of platform architecture, data modelling standards, and engineering best practices | No AI skill signal. | Take ownership of platform architecture, data modelling standards, and engineering best practices | moderate |
| 2026-07-01_deloitte_analytics-engineer | Design reliable, scalable, efficient data pipelines from internal and external sources | design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools | Develop and optimise procedures to productionize models with monitoring capabilities | high |
| 2026-07-01_emagine_senior-bi-analyst | Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases. | No AI skill signal. | Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes. | high |
| 2026-07-01_entain_analytics-engineer-bi | Collaborate with Data Engineering to improve data quality | No AI skill signal. | Extract and analyze large datasets from Snowflake using SQL to generate meaningful insights; Design and maintain dbt models for the analytics semantic layer | high |
| 2026-07-01_finanz-informatik_bi-engineer | Manage planning, testing, acceptance, and documentation of applications | No AI skill signal. | Evaluate new metrics requirements collaboratively with stakeholders | high |
| 2026-07-01_gemma-analytics_ai-analytics-engineer | Apply data modelling methodologies | Professional AI tool experience, ideally including coding assistants | Leverage AI tools including agentic workflows and AI coding assistants | moderate |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer | Own data correctness and investigate quality anomalies. | Develop AI-driven reporting and insight workflows. | Concrete experience structuring prompts, managing multi-agent workflows, and reviewing AI-generated outputs | moderate |
| 2026-07-01_henkel_business-intelligence-developer | Focus on detail, precision and working transparently with managing priorities independently | No AI skill signal. | Utilise and combine various data sources, master understanding of the data and underlying financial processes | high |
| 2026-07-01_aptrack_senior-bi-architect | Ensure data quality, governance, and security standards | No AI skill signal. | Translate business requirements into BI solutions and analytics outputs | moderate |
| 2026-07-01_hovione_data-analytics-engineer | Deliver projects safely, on time, and cost effectively while upholding IT governance, GMP/HSE, and compliance standards (COPs, SOPs) | No AI skill signal. | Preprocess and engineer features from structured and unstructured data, ensuring quality, lineage, and reliability | high |
| 2026-07-01_hse24_junior-expert-bi-analytics | Apply modern development standards including clean code and test-driven development | No AI skill signal. | Build and maintain data models with DBT and Snowflake using dimensional modelling; Manage code via Git with structured branching strategies and support CI/CD processes | moderate |
| 2026-07-01_jtl-software_senior-analytics-engineer | Building complex data models with high quality and availability standards | No AI skill signal. | Collaborating with development, product, and pilot customers to translate business requirements into viable data models | moderate |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst | Perform data migration, validation, reconciliation, and quality analysis | No AI skill signal. | Create data mappings, transformation rules, Data Management Plans, and technical documentation | high |
| 2026-07-01_retail-consult_data-analytics-engineer | scalable, reliable, and high-quality data solutions | No AI skill signal. | collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions | moderate |
| 2026-07-01_size-up-consulting_senior-analytics-engineer | Ensure data quality, consistency, and documentation | No AI skill signal. | Build business indicators and semantic models for activity management | moderate |
| 2026-07-01_too-good-to-go_bi-developer | Improve data governance through clear definitions and reusable logic | No AI skill signal. | Design performant LookML models, Explores and dashboards | moderate |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert | Implement testing and data validation processes within dbt | No AI skill signal. | Manage table creation, views, routines, and scheduled queries | high |
| 2026-07-02_acronis_senior-business-intelligence-analyst | Improve data quality and reliability through validation, monitoring, incident triage, and clear runbooks | AI-assisted automation for BI/data work (testing, documentation, or pipeline scripting) | Improve data quality and reliability through validation, monitoring, incident triage, and clear runbooks | moderate |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake | Improving data quality through automated testing and validation | No AI skill signal. | Designing, building, and maintaining scalable data models using dbt | moderate |
| 2026-07-02_asics_senior-business-intelligence-engineer | Establishing documentation, version control, and data privacy compliance | No AI skill signal. | Strong hands-on experience with Snowflake and DBT; Define and prioritise technical requirements that align with the overall business strategy | moderate |
| 2026-07-02_bose_data-analytics-engineer | Implement data quality tests and participate in ensuring the accuracy and reliability of data pipelines | No AI skill signal. | Implement data quality tests and participate in ensuring the accuracy and reliability of data pipelines; Assist in analyzing, cleaning, and transforming datasets | moderate |
| 2026-07-02_bridgerpay_senior-analytics-engineer | Introduce robust CI/CD frameworks, unit testing, and security protocols | Prepare data ecosystem for real-time AI modeling | Own the semantic layer, writing production-grade LookML | high |
| 2026-07-02_enza-zaden_senior-analytics-engineer | Improving data quality, reliability, performance and cost efficiency through lifecycle management | No AI skill signal. | Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI | low |
| 2026-07-02_fullenrich_analytics-engineer | Write tests and maintain documentation standards | Active use of AI tools (Cursor, Claude) for work augmentation | Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot | moderate |
| 2026-07-02_funke-medien_analytics-engineer | kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen | No AI skill signal. | Als Expert*in im Datawarehouse kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen | moderate |
| 2026-07-02_gerolsteiner_data-analytics-engineer | creating and optimizing reports, stories, and planning content | familiarity with artificial intelligence and machine learning concepts | develop analytics solutions using Azure Databricks, including Power BI reports and dashboards | moderate |
| 2026-07-02_ig-group_analytics-engineer | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | Contribute to the development of AI agents, co-pilots, and automated insights that surface data directly to users | Build and maintain scalable, well-documented data models in dbt that enable self-service analytics for business users across IG; Deliver the migration of business-critical dashboards to Looker, rebuilding and modelling in LookML to ensure a clean, reliable transition | high |
| 2026-07-02_ijsvogel-retail_analytics-engineer | monitors data quality and governance including GDPR compliance | interest in advanced analytics and AI applications | designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance including GDPR compliance | moderate |
| 2026-07-02_mr-marvis_senior-analytics-engineer | Implementing testing, monitoring, and data quality checks while partnering with data engineers | optimizing the platform for AI use cases | Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency | moderate |
| 2026-07-02_photowall_analytics-engineer | Establish monitoring and documentation protocols for data reliability | No AI skill signal. | Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation; Support A/B testing and experimentation workflows | moderate |
| 2026-07-02_sii-poland_data-analytics-engineer | Ensure data quality through testing, monitoring, and documentation | No AI skill signal. | Build and maintain core data models using dbt for critical reporting | high |
| 2026-07-02_sosafe_senior-analytics-engineer | Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle | building data infrastructure that serves AI agents, not just BI tools | Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models | moderate |
| 2026-07-02_xomnia_data-analytics-engineer | building scalable data models and pipelines | No AI skill signal. | work with business stakeholders to understand analytics needs | moderate |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data | Developing best practices in data integrity and documentation | No AI skill signal. | Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems | moderate |

### collaboration_width (64 inconsistent JDs)

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
| 2026-06-29_bip_business-intelligence-specialist | 5 | 5 | 6 |  |
| 2026-06-29_fullenrich_analytics-engineer | 4 | 5 | 5 |  |
| 2026-06-30_bitac-gmbh_business-intelligence-spezialist | 2 | 1 | 1 |  |
| 2026-06-30_louis-dreyfus-company_data-analytics-engineer-finance-systems | 3 | 4 | 4 |  |
| 2026-06-30_van-in-sanoma_business-intelligence-analyst | 1 | 0 | 1 |  |
| 2026-07-01_airalo_analytics-engineering-manager | customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting | Establish governance and standards: metric definitions, dashboard design patterns, modelling practices, testing frameworks, and documentation | self-serve platform (Lightdash) that enables teams across the business to answer their own questions | 3 |
| 2026-07-01_awin_analytical-engineer | creating a trusted semantic layer that enables self-serve analytics across the organisation | Exposure to data observability or AI-readiness concepts | Design data marts with self-serve usage in mind; Coach BI Developers in Analytics Engineering best practices; Create documentation enabling independent contributions | 3 |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence | Collaborating with Finance and Operations on reporting needs | Ensuring high data quality of the core data layer with dbt models | Enabling analysts and streamlining dashboard creation | 5 |
| 2026-07-01_booking-com_data-analytics-engineer-ii | Solve issues by prioritising on customer impact and perform root cause analysis to find ways to prevent recurrence. | Ensuring that service level agreements are met by implementing tests and processes. | You will be responsible for delivering products that advance data excellence and innovation within your product team, and across the business | 4 |
| 2026-07-01_darwin_senior-analytics-engineer | build a modern cloud-based data platform that will support the organisation's next phase of growth | No testing or data quality signal mentioned in the JD. | Build a modern cloud-based data platform that will support the organisation's next phase of growth | 1 |
| 2026-07-01_deloitte_analytics-engineer | translate needs into data solutions that drive business impact | Develop and optimise procedures to productionize models with monitoring capabilities | design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools | 1 |
| 2026-07-01_emagine_senior-bi-analyst | supporting inspections, audits, data validation, and the investigation of data defects | Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases. | Produce ad hoc analytical reports and data extracts to support inspections, audits, data validation, and the investigation of data defects. | 2 |
| 2026-07-01_entain_analytics-engineer-bi | Deliver ad-hoc analysis to support decision-making | Collaborate with Data Engineering to improve data quality | translates data into actionable insights for business stakeholders through analysis, dashboards, and reporting; Contribute to self-serve analytics capabilities | 2 |
| 2026-07-01_finanz-informatik_bi-engineer | Develop usage metrics and operational benchmarks for customers | Manage planning, testing, acceptance, and documentation of applications | develop metrics that enable the Sparkassen group to transparently manage processes and optimise customer journeys | 0 |
| 2026-07-01_gemma-analytics_ai-analytics-engineer | helps organisations become more data-driven | Work with multiple technologies across the modern data stack; Develop advanced data reporting and visualisations; Apply data modelling methodologies; Leverage AI tools including agentic workflows and AI coding assistants | building both traditional data pipelines and intelligent, agentic solutions that create real business impact | 1 |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer | Identify opportunities and risks in gameplay data. | Own data correctness and investigate quality anomalies; Help establish organisational adoption patterns for AI-assisted engineering, including review processes and quality gates. | Support product and design teams with actionable recommendations derived from complex datasets | 2 |
| 2026-07-01_henkel_business-intelligence-developer | Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department | No testing or data quality signal. | Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department | 2 |
| 2026-07-01_aptrack_senior-bi-architect | Design and deliver a modern Microsoft Fabric-based analytics platform | Ensure data quality, governance, and security standards | Create reusable data models and curated data products | 0 |
| 2026-07-01_hovione_data-analytics-engineer | Deliver projects safely, on time, and cost effectively while upholding IT governance, GMP/HSE, and compliance standards (COPs, SOPs) | set up monitoring, alerting, and lifecycle management | Build, standardize, and maintain reporting and self-service analytics as part of data lake and data mesh concepts | 0 |
| 2026-07-01_hse24_junior-expert-bi-analytics | enable data-driven decision-making | Apply modern development standards including clean code and test-driven development | Develop automated self-service BI solutions with consistent KPI definitions | 2 |
| 2026-07-01_jtl-software_senior-analytics-engineer | Owning the data foundation for a new AI-powered BI product | Improving query performance and data quality | Owning the data foundation for a new AI-powered BI product | 3 |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst | Produce ad hoc reports and data extracts for business, audit, and compliance | Data Quality, Data Validation | support delivery of a modern enterprise data platform using Microsoft Fabric, focusing on business intelligence, data analysis, migration, quality, governance, and reporting | 2 |
| 2026-07-01_retail-consult_data-analytics-engineer | collaborating with Finance, Sales, HR, and Project Management teams | high-quality data solutions | collaborating with Finance, Sales, HR, and Project Management teams | 4 |
| 2026-07-01_size-up-consulting_senior-analytics-engineer | serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data | Ensure data quality, consistency, and documentation | serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data | 3 |
| 2026-07-01_too-good-to-go_bi-developer | dashboard/reporting experience for commercial, finance, or logistics teams | No testing or observability framework mentioned. | Dashboard/reporting experience for commercial, finance, or logistics teams | 1 |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert | Design and maintain analytical data models in dbt with focus on traceability and quality | Implement testing and data validation processes within dbt | ensure consistent, actionable information organisation-wide | 2 |
| 2026-07-02_acronis_senior-business-intelligence-analyst | Define and maintain KPI/metric definitions, lineage, and reporting standards so stakeholders trust the numbers | Improve data quality and reliability through validation, monitoring, incident triage, and clear runbooks | enabling self-service dashboards and ad-hoc analysis in Power BI | 0 |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake | Designing, building, and maintaining scalable data models using dbt | Defining data modelling, testing, and documentation standards | Defining data modelling, testing, and documentation standards | 0 |
| 2026-07-02_asics_senior-business-intelligence-engineer | data privacy compliance | No testing or data quality framing identified in the JD. | Promoting BI adoption and data literacy across EMEA | 0 |
| 2026-07-02_bose_data-analytics-engineer | This work will directly inform and influence multiple divisions' strategies. | Implement data quality tests and participate in ensuring the accuracy and reliability of data pipelines | design/building of a semantic layer that helps create dashboards and models that drive insights and actions | 3 |
| 2026-07-02_bridgerpay_senior-analytics-engineer | Ensure PCI-DSS/SOC2 compliance while optimizing costs | Introduce robust CI/CD frameworks, unit testing, and security protocols | Build complex data models serving clean data to AI models, routing engines, and BI tools | 0 |
| 2026-07-02_enza-zaden_senior-analytics-engineer | Ensuring compliance with architecture, security and access standards together with IT, Architecture and Security teams | Experience with DevOps practices such as version control, testing and CI/CD for data products | empower self-service BI for teams across the organization | 4 |
| 2026-07-02_fullenrich_analytics-engineer | Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams | Write tests and maintain documentation standards | building foundational systems for organizational growth | 5 |
| 2026-07-02_funke-medien_analytics-engineer | Reporting und der Marketing Automation fur das Zeitungsgeschaft | Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools | Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft | 1 |
| 2026-07-02_gerolsteiner_data-analytics-engineer | processing IoT and market data, unifying SAP and non-SAP system data | data modeling, reporting structures | developing and maintaining data models, queries, and views in SAP environments | 0 |
| 2026-07-02_ig-group_analytics-engineer | publicly-traded FTSE250 FinTech company | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | turn raw data into trusted, self-serve insight that business users across IG can act on | 4 |
| 2026-07-02_ijsvogel-retail_analytics-engineer | monitors data quality and governance including GDPR compliance | monitors data quality and governance including GDPR compliance | translating business questions into dashboards and data solutions | 0 |
| 2026-07-02_mr-marvis_senior-analytics-engineer | Working with business teams to convert analytical needs into structured data solutions | Implementing testing, monitoring, and data quality checks while partnering with data engineers | owning the analytics layer of our data platform | 1 |
| 2026-07-02_photowall_analytics-engineer | Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels | Establish monitoring and documentation protocols for data reliability | Design and maintain dashboards for Growth, Marketing, and Product teams; Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels; Support A/B testing and experimentation workflows | 2 |
| 2026-07-02_sii-poland_data-analytics-engineer | strategic fintech project based in Copenhagen. The role involves building and scaling critical data models that support decision-making across credit, payments, and fraud/AML domains | Ensure data quality through testing, monitoring, and documentation | Contribute to the semantic layer (LookML) for consistent reporting | 3 |
| 2026-07-02_sosafe_senior-analytics-engineer | Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models | Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle | Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents | 2 |
| 2026-07-02_xomnia_data-analytics-engineer | work with business stakeholders to understand analytics needs | optimize data workflows for performance, usability, and cost efficiency | developing self-service platforms | 1 |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data | Conducting analytical deep dives and formulating recommendations for leadership | Developing best practices in data integrity and documentation | Partnering with Data Engineering teams to enhance data infrastructure | 1 |

### data_team_maturity (46 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | early | mid | early |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mid | mid | early | early |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | mature | mature | mid | early |
| 2026-05-09_lightdash_analytics-engineering-advocate | mid | mature | mature | early |
| 2026-06-22_freenow_analytics-engineer | mid | mature | mid | mature |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | mid | mature | mid | mid |
| 2026-06-27_lego-group_analytics-engineer | mid | mid | mature |  |
| 2026-06-30_finom_senior-analytics-engineer | mid | early | mid | early |
| 2026-07-01_airalo_analytics-engineering-manager | analytics teams; Data Engineering | a governed semantic layer that analytics teams trust | establish how we model data, how we govern metrics, and how we roll out self-service capabilities | mid |
| 2026-07-01_awin_analytical-engineer | Partner with Data Engineering teams; Collaborate with BI Developers and Insight Analysts | Establish a single source of truth for business metric definitions | Translate ambiguous business requirements into clear, well-documented data definitions | mid |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence | Finance and Operations; data engineering | No loss aversion framing. | assisting various teams in collecting and analyzing metrics that support growth | mid |
| 2026-07-01_booking-com_data-analytics-engineer-ii | Our customers are anyone from Finance to Marketing and everyone in between; enable our analysts and product teams | Be responsible for maintaining data quality, security, integrity and governance by effectively following regulatory requirements, company standards, and best practices. | Adhere to the defined principles for architecture, quality and non-functional requirements | mature |
| 2026-07-01_darwin_senior-analytics-engineer | Data Science or Machine Learning teams | No loss aversion framing. | Take ownership of platform architecture, data modelling standards, and engineering best practices | early |
| 2026-07-01_deloitte_analytics-engineer | None | Design reliable, scalable, efficient data pipelines from internal and external sources | This professional will design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools | mature |
| 2026-07-01_emagine_senior-bi-analyst | Collaborate with project teams; Collaborate with technical teams | supporting inspections, audits, data validation, and the investigation of data defects | Support the design of data migration and integration processes, ensuring data quality and availability. | mature |
| 2026-07-01_entain_analytics-engineer-bi | Collaborate with Data Engineering to improve data quality | Collaborate with Data Engineering to improve data quality | Deliver ad-hoc analysis to support decision-making | mid |
| 2026-07-01_finanz-informatik_bi-engineer | collaboratively with stakeholders | Manage planning, testing, acceptance, and documentation of applications | Plan and coordinate work packages for metrics development | mature |
| 2026-07-01_gemma-analytics_ai-analytics-engineer | None | engineers work at the intersection of data and AI, building both traditional data pipelines and intelligent, agentic solutions that create real business impact | Develop advanced data reporting and visualisations | mid |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer | product and design teams | Own data correctness and investigate quality anomalies; Review AI-generated code on critical paths before production deployment. | Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting | early |
| 2026-07-01_henkel_business-intelligence-developer | Product & Technology management department; financial and technical community | No loss aversion framing. | Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department | mature |
| 2026-07-01_aptrack_senior-bi-architect | Collaborate with stakeholders on requirements and insights delivery | Ensure data quality, governance, and security standards | Define BI architecture standards, principles and best practices | mature |
| 2026-07-01_hovione_data-analytics-engineer | cross functional teams | Deliver projects safely, on time, and cost effectively while upholding IT governance, GMP/HSE, and compliance standards (COPs, SOPs) | Strong autonomy to lead analytic solutions from design to deployment | mid |
| 2026-07-01_hse24_junior-expert-bi-analytics | data platform teams; business units | Apply modern development standards including clean code and test-driven development | Translate business requirements into analytics deliverables | mid |
| 2026-07-01_jtl-software_senior-analytics-engineer | development, product, and pilot customers | Building complex data models with high quality and availability standards | Collaborating with development, product, and pilot customers to translate business requirements into viable data models | early |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst | Collaborate with business and technical teams | Produce ad hoc reports and data extracts for business, audit, and compliance | Support data governance, data modelling, data lineage, and data integration initiatives | mature |
| 2026-07-01_retail-consult_data-analytics-engineer | Finance, Sales, HR, and Project Management teams | scalable, reliable, and high-quality data solutions | collaborating with Finance, Sales, HR, and Project Management teams to transform business needs | mid |
| 2026-07-01_size-up-consulting_senior-analytics-engineer | Data Engineering; Data Analytics; Product | Ensure data quality, consistency, and documentation | Design and maintain data models for analytical purposes | mature |
| 2026-07-01_too-good-to-go_bi-developer | Data Engineering teams; commercial, finance, or logistics teams | No loss aversion framing. | Own technical design and development of BI products and semantic models | mid |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert | work closely with the Data Team Lead, Senior Data Engineer, and business teams | focus on traceability and quality; Implement testing and data validation processes within dbt | focuses on designing and evolving the analytical layer | mid |
| 2026-07-02_acronis_senior-business-intelligence-analyst | None identified | ensuring data quality, operational excellence, and platform reliability through robust validation processes, monitoring, incident management | Drive modernization and Microsoft Fabric adoption | mature |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake | within a collaborative small team environment | Building reliable ELT pipelines | Defining data modelling, testing, and documentation standards | mid |
| 2026-07-02_asics_senior-business-intelligence-engineer | None | Establishing documentation, version control, and data privacy compliance | Define and prioritise technical requirements that align with the overall business strategy; Directing data integration and pipeline orchestration across the organization; Creating data models and implementing transformation/cleansing/enrichment processes | mature |
| 2026-07-02_bose_data-analytics-engineer | analysts; product; software | ensuring the accuracy and reliability of data pipelines | Follow and contribute to analytical engineering standards and best practices under the guidance of senior team members | mature |
| 2026-07-02_bridgerpay_senior-analytics-engineer | Build and scale data warehouse core and pipelines utilizing BigQuery and managed cloud services | Ensure PCI-DSS/SOC2 compliance while optimizing costs | Own the semantic layer, writing production-grade LookML | early |
| 2026-07-02_enza-zaden_senior-analytics-engineer | product owners; analytics engineers; IT specialists; IT, Architecture and Security teams | Improving data quality, reliability, performance and cost efficiency through lifecycle management | Leading complex analytics and reporting initiatives with a mid- to long-term horizon | mature |
| 2026-07-02_fullenrich_analytics-engineer | Finance, Marketing, RevOps, Sales, and Support teams | rigorous data quality standards | owning the data layer end-to-end while building foundational systems for organizational growth | early |
| 2026-07-02_funke-medien_analytics-engineer | Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen | No loss aversion framing. | Nach Deiner Einarbeitung wirst Du verantwortlich fur zwei Topics und tragst damit entscheidend zum Geschaftserfolg bei | mid |
| 2026-07-02_gerolsteiner_data-analytics-engineer | No named partner teams identified | No loss aversion framing. | supporting AI-driven analytics expansion | mid |
| 2026-07-02_ig-group_analytics-engineer | data engineers; data scientists | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | Translate business requirements from stakeholders across functions into efficient, trusted data models | mature |
| 2026-07-02_ijsvogel-retail_analytics-engineer | works with stakeholders on information needs | monitors data quality and governance including GDPR compliance; resolving pipeline issues | translating business questions into dashboards and data solutions | mid |
| 2026-07-02_mr-marvis_senior-analytics-engineer | data engineers | Enabling governed access to trusted data sources | Working with business teams to convert analytical needs into structured data solutions | mid |
| 2026-07-02_photowall_analytics-engineer | Design and maintain dashboards for Growth, Marketing, and Product teams | Establish monitoring and documentation protocols for data reliability | Own and maintain BigQuery data pipelines; Establish monitoring and documentation protocols; Support A/B testing and experimentation workflows | mid |
| 2026-07-02_sii-poland_data-analytics-engineer | Partner with stakeholders, Data Engineers, and Analysts on requirements | Comfort in high engineering/governance standard environments | Partner with stakeholders, Data Engineers, and Analysts on requirements | mid |
| 2026-07-02_sosafe_senior-analytics-engineer | Data Engineers; analytics; product | Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle | Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets | mid |
| 2026-07-02_xomnia_data-analytics-engineer | collaborating with data engineers | No loss aversion framing. | collaborating with data engineers | mid |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data | Partnering with Data Engineering teams to enhance data infrastructure | Automating reporting, audits, and other data-driven activities | Contributing to the design, implementation, and delivery of BI solutions | mature |

### jd_authorship (94 inconsistent JDs)

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
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | hiring_manager | mixed | mixed | mixed |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | hiring_manager | recruiter | recruiter |  |
| 2026-06-29_bip_business-intelligence-specialist | mixed | hiring_manager | mixed |  |
| 2026-06-29_irium-portugal_senior-analytics-engineer | recruiter | hiring_manager | hiring_manager | mixed |
| 2026-06-30_doodle_growth-analytics-engineer | recruiter | mixed | mixed |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | mixed | mixed | recruiter |  |
| 2026-06-30_finom_senior-analytics-engineer | mixed | mixed | hiring_manager | mixed |
| 2026-06-30_avalanche-studios_senior-analytics-engineer | recruiter | recruiter | mixed |  |
| 2026-06-30_louis-dreyfus-company_data-analytics-engineer-finance-systems | mixed | mixed | recruiter |  |
| 2026-06-30_plain-concepts_bi-specialist | mixed | recruiter | recruiter |  |
| 2026-06-30_van-in-sanoma_business-intelligence-analyst | hiring_manager | mixed | mixed |  |
| 2026-07-01_airalo_analytics-engineering-manager | lead and grow a team of analytics engineers (currently 2, scaling to 4 this year) | Balance rigour with delivery speed — we're still building foundations while the business moves fast | No AI skill signal. | hiring_manager |
| 2026-07-01_awin_analytical-engineer | establish their analytics engineering practice within the BI team | Establish a single source of truth for business metric definitions | No AI skill signal. | hiring_manager |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence | Contributing to the ongoing design of our core data model | Ensuring high data quality of the core data layer with dbt models | No AI skill signal. | mixed |
| 2026-07-01_booking-com_data-analytics-engineer-ii | This Data Engineering team is focused on Flights data at Booking. We are building new products for creating, maintaining, and presenting flights data using the Booking Data Exchange (BDX) platform. | End-to-end ownership of data quality in our core datasets and data pipelines | No AI skill signal. | mixed |
| 2026-07-01_darwin_senior-analytics-engineer | you'll be the first dedicated Analytics Engineer within the business | data modelling standards, and engineering best practices | No AI skill signal. | hiring_manager |
| 2026-07-01_deloitte_analytics-engineer | Develop and optimise procedures to productionize models with monitoring capabilities | Design reliable, scalable, efficient data pipelines from internal and external sources | design the pipelines and architectures of data that form the foundation for AI solutions | mixed |
| 2026-07-01_emagine_senior-bi-analyst | Analyze data across SQL and other enterprise platforms to support operational use cases. | Monitor and analyze data quality, integrity, and processing logs, identifying issues and collaborating with technical teams to resolve them. | No AI skill signal. | hiring_manager |
| 2026-07-01_entain_analytics-engineer-bi | Design and maintain dbt models for the analytics semantic layer | Collaborate with Data Engineering to improve data quality | No AI skill signal. | hiring_manager |
| 2026-07-01_finanz-informatik_bi-engineer | Conceptualise and implement new data flows | Manage planning, testing, acceptance, and documentation of applications | No AI skill signal. | recruiter |
| 2026-07-01_gemma-analytics_ai-analytics-engineer | Team of 18, growing to 24 in 2026 | Apply data modelling methodologies | building both traditional data pipelines and intelligent, agentic solutions that create real business impact | recruiter |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer | Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting. | Review AI-generated code on critical paths before production deployment | Develop AI-driven reporting and insight workflows | hiring_manager |
| 2026-07-01_henkel_business-intelligence-developer | Play a key role in development of advanced analytical tools in Power BI | Focus on detail, precision and working transparently with managing priorities independently | No AI skill signal. | mixed |
| 2026-07-01_aptrack_senior-bi-architect | Define lakehouse, data warehouse, and semantic modelling structures | Ensure data quality, governance, and security standards | No AI skill signal. | hiring_manager |
| 2026-07-01_hovione_data-analytics-engineer | Build, standardize, and maintain reporting and self-service analytics as part of data lake and data mesh concepts | Deliver projects safely, on time, and cost effectively while upholding IT governance, GMP/HSE, and compliance standards (COPs, SOPs) | No AI skill signal. | mixed |
| 2026-07-01_hse24_junior-expert-bi-analytics | Collaborate with data platform teams and business units on optimisation | Apply modern development standards including clean code and test-driven development | No AI skill signal. | hiring_manager |
| 2026-07-01_jtl-software_senior-analytics-engineer | Owning the data foundation for a new AI-powered BI product | Building complex data models with high quality and availability standards | No AI skill signal. | hiring_manager |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst | focusing on business intelligence, data analysis, migration, quality, governance, and reporting | Support data governance, data modelling, data lineage, and data integration initiatives | No AI skill signal. | mixed |
| 2026-07-01_retail-consult_data-analytics-engineer | designing data architectures, optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines | scalable, reliable, and high-quality data solutions | No AI skill signal. | recruiter |
| 2026-07-01_size-up-consulting_senior-analytics-engineer | Develop and optimise data transformations using ELT tools; Participate in data governance and best practice improvements | Ensure data quality, consistency, and documentation | No AI skill signal. | recruiter |
| 2026-07-01_too-good-to-go_bi-developer | Replace manual reporting and Google Sheets processes with scalable solutions | Improve data governance through clear definitions and reusable logic | No AI skill signal. | hiring_manager |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert | work closely with the Data Team Lead, Senior Data Engineer | Implement testing and data validation processes within dbt | No AI skill signal. | hiring_manager |
| 2026-07-02_acronis_senior-business-intelligence-analyst | Lead and develop a team of 2 direct reports | ensuring data quality, operational excellence, and platform reliability through robust validation processes, monitoring, incident management, and well-defined operational procedures | AI-assisted automation for BI/data work (testing, documentation, or pipeline scripting) | hiring_manager |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake | owning the transformation layer of a modern cloud data platform | Improving data quality through automated testing and validation | No AI skill signal. | hiring_manager |
| 2026-07-02_asics_senior-business-intelligence-engineer | Directing data integration and pipeline orchestration across the organization | Establishing documentation, version control, and data privacy compliance | No AI skill signal. | mixed |
| 2026-07-02_bose_data-analytics-engineer | Follow and contribute to analytical engineering standards and best practices under the guidance of senior team members | Implement data quality tests and participate in ensuring the accuracy and reliability of data pipelines | No AI skill signal. | hiring_manager |
| 2026-07-02_bridgerpay_senior-analytics-engineer | Introduce robust CI/CD frameworks, unit testing, and security protocols | Introduce robust CI/CD frameworks, unit testing, and security protocols | Proficiency with generative AI coding assistants | hiring_manager |
| 2026-07-02_enza-zaden_senior-analytics-engineer | Improving data quality, reliability, performance and cost efficiency through lifecycle management | Improving data quality, reliability, performance and cost efficiency through lifecycle management | No AI skill signal. | hiring_manager |
| 2026-07-02_fullenrich_analytics-engineer | This is FullEnrich's inaugural dedicated data hire | Write tests and maintain documentation standards | Active use of AI tools (Cursor, Claude) for work augmentation | hiring_manager |
| 2026-07-02_funke-medien_analytics-engineer | Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools | Sorgfaltige Arbeitsweise und hohe Eigenmotivation | No AI skill signal. | hiring_manager |
| 2026-07-02_gerolsteiner_data-analytics-engineer | advancing existing Business Warehouse implementations | developing and maintaining data models, queries, and views | familiarity with artificial intelligence and machine learning concepts | hiring_manager |
| 2026-07-02_ig-group_analytics-engineer | Business Intelligence team, which acts as the centre of excellence for analytics across IG | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | Contribute to the development of AI agents, co-pilots, and automated insights that surface data directly to users | hiring_manager |
| 2026-07-02_ijsvogel-retail_analytics-engineer | designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance | monitors data quality and governance including GDPR compliance | interest in advanced analytics and AI applications | hiring_manager |
| 2026-07-02_mr-marvis_senior-analytics-engineer | owning the analytics layer of our data platform | Implementing testing, monitoring, and data quality checks while partnering with data engineers | Openness to using AI tools for workflow improvement | hiring_manager |
| 2026-07-02_photowall_analytics-engineer | Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse | Establish monitoring and documentation protocols for data reliability | No AI skill signal. | hiring_manager |
| 2026-07-02_sii-poland_data-analytics-engineer | Support reliable data workflows using orchestration tools like Airflow | Ensure data quality through testing, monitoring, and documentation | No AI skill signal. | hiring_manager |
| 2026-07-02_sosafe_senior-analytics-engineer | Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models | Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle | an interest in building data infrastructure that serves AI agents, not just BI tools | hiring_manager |
| 2026-07-02_xomnia_data-analytics-engineer | developing self-service platforms | optimize data workflows for performance, usability, and cost efficiency | No AI skill signal. | mixed |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data | Partnering with Data Engineering teams to enhance data infrastructure | Developing best practices in data integrity and documentation | No AI skill signal. | mixed |

### stakeholder_orientation (68 inconsistent JDs)

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
| 2026-06-29_e-frontiers_analytics-engineer-data-engineer | finance | finance | internal_data | internal_data |
| 2026-06-29_chefs-culinar-west_business-intelligence-specialist | internal_data | mixed | internal_data |  |
| 2026-06-29_bip_business-intelligence-specialist | mixed | commercial | commercial |  |
| 2026-06-29_fullenrich_analytics-engineer | internal_data | internal_data | mixed |  |
| 2026-06-30_bitac-gmbh_business-intelligence-spezialist | mixed | internal_data | mixed |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | internal_data | mixed | mixed |  |
| 2026-06-30_limeflight_senior-data-analytics-engineer | internal_data | product | internal_data |  |
| 2026-07-01_airalo_analytics-engineering-manager | Own and evolve our core dbt models and semantic layer to support key analytical use cases: customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting | financial reporting | Establish governance and standards: metric definitions, dashboard design patterns, modelling practices, testing frameworks, and documentation | internal_data |
| 2026-07-01_awin_analytical-engineer | Provide business context for the mart layers of our data architecture; Partner with Data Engineering teams | creating a trusted semantic layer that enables self-serve analytics across the organisation | No testing or data quality signal in responsibilities. | internal_data |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence | Ensuring high data quality of the core data layer with dbt models; Collaborating with Finance and Operations on reporting needs | Collaborating with Finance and Operations on reporting needs | Ensuring high data quality of the core data layer with dbt models | mixed |
| 2026-07-01_booking-com_data-analytics-engineer-ii | Modelling data following best practices and Data Warehousing methodologies such as Data Vault and (Kimball) Dimensional modelling. | improve the experience of our customers | End-to-end ownership of data quality in our core datasets and data pipelines | internal_data |
| 2026-07-01_darwin_senior-analytics-engineer | Take ownership of platform architecture, data modelling standards, and engineering best practices | support the organisation's next phase of growth | No testing or data quality framework signal. | internal_data |
| 2026-07-01_deloitte_analytics-engineer | Develop and optimise procedures to productionize models with monitoring capabilities | Co-create Data Products with business stakeholders for strategic decision-making | Develop and optimise procedures to productionize models with monitoring capabilities | commercial |
| 2026-07-01_emagine_senior-bi-analyst | Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes. | Produce ad hoc analytical reports and data extracts to support inspections, audits, data validation, and the investigation of data defects. | Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases. | mixed |
| 2026-07-01_entain_analytics-engineer-bi | Design and maintain dbt models for the analytics semantic layer | Translate business questions into structured analysis | Collaborate with Data Engineering to improve data quality | internal_data |
| 2026-07-01_finanz-informatik_bi-engineer | Conceptualise and implement new data flows; Develop usage metrics and operational benchmarks for customers | Develop usage metrics and operational benchmarks for customers | Manage planning, testing, acceptance, and documentation of applications | internal_data |
| 2026-07-01_gemma-analytics_ai-analytics-engineer | Work with multiple technologies across the modern data stack | create real business impact | No testing signal. | commercial |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer | Review AI-generated code on critical paths before production deployment; Help establish organisational adoption patterns for AI-assisted engineering, including review processes and quality gates. | analytics infrastructure for a new mobile game | Own data correctness and investigate quality anomalies | product |
| 2026-07-01_henkel_business-intelligence-developer | Play a key role in development of advanced analytical tools in Power BI | Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department | No testing, data quality frameworks, or data contracts mentioned. | finance |
| 2026-07-01_aptrack_senior-bi-architect | Design and implement end-to-end BI architecture using Microsoft Fabric and Azure; Build and manage Azure Data Factory pipelines; Collaborate with stakeholders on requirements and insights delivery | Ensure data quality, governance, and security standards | Ensure data quality, governance, and security standards | internal_data |
| 2026-07-01_hovione_data-analytics-engineer | Preprocess and engineer features from structured and unstructured data, ensuring quality, lineage, and reliability | GMP/HSE, and compliance standards (COPs, SOPs) | Preprocess and engineer features from structured and unstructured data, ensuring quality, lineage, and reliability | internal_data |
| 2026-07-01_hse24_junior-expert-bi-analytics | Build and maintain data models with DBT and Snowflake using dimensional modelling; Translate business requirements into analytics deliverables | Home Shopping Europe GmbH is a leading live commerce provider in Europe, operating as a media platform offering entertainment-focused shopping | Apply modern development standards including clean code and test-driven development | internal_data |
| 2026-07-01_jtl-software_senior-analytics-engineer | Structuring raw data from JTL's inventory management into clean, documented data models | Collaborating with development, product, and pilot customers to translate business requirements into viable data models | No testing framework signal. | product |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst | Create data mappings, transformation rules, Data Management Plans, and technical documentation | Produce ad hoc reports and data extracts for business, audit, and compliance | Experience with Power BI, Data Quality, Data Validation, Data Governance, and Data Modelling | mixed |
| 2026-07-01_retail-consult_data-analytics-engineer | designing data architectures, optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines | collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions | scalable, reliable, and high-quality data solutions | mixed |
| 2026-07-01_size-up-consulting_senior-analytics-engineer | Build business indicators and semantic models for activity management; Collaborate with Product, Data Engineering, and Business teams | serving as a central bridge between Data Engineering, Data Analytics, and end users to ensure reliable, consistent, and accessible data | Ensure data quality, consistency, and documentation | internal_data |
| 2026-07-01_too-good-to-go_bi-developer | Design performant LookML models, Explores and dashboards | Dashboard/reporting experience for commercial, finance, or logistics teams | Improve data governance through clear definitions and reusable logic | internal_data |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert | Design and maintain analytical data models in dbt with focus on traceability and quality; Build and optimise complex SQL queries in BigQuery; Implement testing and data validation processes within dbt | ensure consistent, actionable information organisation-wide | Implement testing and data validation processes within dbt | internal_data |
| 2026-07-02_acronis_senior-business-intelligence-analyst | Improve data quality and reliability through validation, monitoring, incident triage, and clear runbooks | establishing trusted KPIs and developing scalable semantic models that empower self-service reporting and analytics through Power BI | Improve data quality and reliability through validation, monitoring, incident triage, and clear runbooks | internal_data |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake | Defining data modelling, testing, and documentation standards | Building reliable ELT pipelines using SQL and Python | Improving data quality through automated testing and validation | internal_data |
| 2026-07-02_asics_senior-business-intelligence-engineer | Creating data models and implementing transformation/cleansing/enrichment processes | data privacy compliance | No data quality, testing, or observability framework mentioned. | internal_data |
| 2026-07-02_bose_data-analytics-engineer | development of logical and physical data models, data wrangling and design/building of a semantic layer that helps create dashboards and models that drive insights | This work will directly inform and influence multiple divisions' strategies. | Implement data quality tests and participate in ensuring the accuracy and reliability of data pipelines | internal_data |
| 2026-07-02_bridgerpay_senior-analytics-engineer | Own the semantic layer, writing production-grade LookML | Ensure PCI-DSS/SOC2 compliance while optimizing costs | Introduce robust CI/CD frameworks, unit testing, and security protocols | internal_data |
| 2026-07-02_enza-zaden_senior-analytics-engineer | Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI | Ensuring compliance with architecture, security and access standards together with IT, Architecture and Security teams | DevOps practices such as version control, testing and CI/CD for data products | internal_data |
| 2026-07-02_fullenrich_analytics-engineer | Implement reverse ETL pipelines pushing operational data to systems like Intercom and HubSpot | Design data models ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams | Write tests and maintain documentation standards | mixed |
| 2026-07-02_funke-medien_analytics-engineer | Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen und bringst Deine Expertise und kreativen Losungen ein, um datenbasierte Optimierungsstrategien zu entwickeln | Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft digital und traditionell | die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen | commercial |
| 2026-07-02_gerolsteiner_data-analytics-engineer | integrate new data sources via Business Data Cloud and develop analytics solutions using Azure Databricks, including Power BI reports and dashboards | creating and optimizing reports, stories, and planning content within SAP Analytics Cloud | The engineer will integrate new data sources via Business Data Cloud and develop analytics solutions using Azure Databricks, including Power BI reports and dashboards. | internal_data |
| 2026-07-02_ig-group_analytics-engineer | Deliver the migration of business-critical dashboards to Looker, rebuilding and modelling in LookML to ensure a clean, reliable transition | turn raw data into trusted, self-serve insight that business users across IG can act on | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | internal_data |
| 2026-07-02_ijsvogel-retail_analytics-engineer | designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance | monitors data quality and governance including GDPR compliance | monitors data quality and governance including GDPR compliance | internal_data |
| 2026-07-02_mr-marvis_senior-analytics-engineer | Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency | Enabling governed access to trusted data sources | Implementing testing, monitoring, and data quality checks | internal_data |
| 2026-07-02_photowall_analytics-engineer | Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse | Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels | Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation; Establish monitoring and documentation protocols for data reliability | commercial |
| 2026-07-02_sii-poland_data-analytics-engineer | Contribute to the semantic layer (LookML) for consistent reporting | credit, payments, and fraud/AML domains | Ensure data quality through testing, monitoring, and documentation | internal_data |
| 2026-07-02_sosafe_senior-analytics-engineer | Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models | Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets | Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle | internal_data |
| 2026-07-02_xomnia_data-analytics-engineer | translating insights into dashboards | work with business stakeholders to understand analytics needs | No testing or data quality framework mentioned in the JD. | commercial |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data | Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems | Identifying opportunities to drive analytical reporting and business strategy | Developing best practices in data integrity and documentation | internal_data |

### autonomy_level (75 inconsistent JDs)

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
| 2026-06-30_doodle_growth-analytics-engineer | strategic | strategic | mixed |  |
| 2026-06-30_cosuno_senior-analytics-engineer | execution | mixed | execution |  |
| 2026-06-30_hilo-by-aktiia_bi-strategic-analytics-lead | strategic | mixed | mixed |  |
| 2026-06-30_limeflight_senior-data-analytics-engineer | mixed | strategic | strategic |  |
| 2026-06-30_plain-concepts_bi-specialist | mixed | execution | mixed |  |
| 2026-06-30_van-in-sanoma_business-intelligence-analyst | mixed | execution | mixed |  |
| 2026-07-01_airalo_analytics-engineering-manager | the self-service platform (Lightdash) that enables teams across the business to answer their own questions | Partner with analysts to translate their needs into scalable data assets, and with Data Engineering on pipeline reliability and data quality | Partner with Data Engineering on pipeline reliability and data quality | strategic |
| 2026-07-01_awin_analytical-engineer | creating a trusted semantic layer that enables self-serve analytics across the organisation | Partner with Data Engineering teams; Collaborate with BI Developers and Insight Analysts | No loss aversion framing. | strategic |
| 2026-07-01_bitpanda_analytics-engineer-dbt-business-intelligence | Contributing to the ongoing design of our core data model | Finance; Operations; data engineering; analysts | Ensuring high data quality of the core data layer with dbt models | mixed |
| 2026-07-01_booking-com_data-analytics-engineer-ii | Producing curated, reusable analytical data products to enable self-serve analytics for many internal customers across departments. | Finance to Marketing; analysts and product teams | maintain data quality, security, integrity and governance by effectively following regulatory requirements, company standards, and best practices | mixed |
| 2026-07-01_darwin_senior-analytics-engineer | Build a modern cloud-based data platform that will support the organisation's next phase of growth | first dedicated Analytics Engineer within the business | No loss aversion framing. | strategic |
| 2026-07-01_deloitte_analytics-engineer | design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools | No named internal partner teams explicitly identified in responsibilities | Design reliable, scalable, efficient data pipelines from internal and external sources | mixed |
| 2026-07-01_emagine_senior-bi-analyst | Develop Data Management Plans, including governance, data flows, and controls. | None identified | Produce ad hoc analytical reports and data extracts to support inspections, audits, data validation, and the investigation of data defects. | execution |
| 2026-07-01_entain_analytics-engineer-bi | translates data into actionable insights for business stakeholders through analysis, dashboards, and reporting | Data Engineering | No loss aversion framing. | mixed |
| 2026-07-01_finanz-informatik_bi-engineer | transforms data into actionable insights by developing metrics that enable the Sparkassen group to transparently manage processes | Evaluate new metrics requirements collaboratively with stakeholders | No loss aversion framing. | mixed |
| 2026-07-01_gemma-analytics_ai-analytics-engineer | Develop advanced data reporting and visualisations | None | No loss aversion signal. | mixed |
| 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer | Support product and design teams with actionable recommendations derived from complex datasets. | Support product and design teams with actionable recommendations | Review AI-generated code on critical paths before production deployment | strategic |
| 2026-07-01_henkel_business-intelligence-developer | Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department | Product & Technology management department | No loss aversion framing. | execution |
| 2026-07-01_aptrack_senior-bi-architect | Define BI architecture standards, principles and best practices; design and deliver a modern Microsoft Fabric-based analytics platform | Collaborate with stakeholders on requirements and insights delivery | Ensure data quality, governance, and security standards | strategic |
| 2026-07-01_hovione_data-analytics-engineer | Build, standardize, and maintain reporting and self-service analytics as part of data lake and data mesh concepts | Partner with stakeholders across functions as a data business partner | Deliver projects safely, on time, and cost effectively while upholding IT governance, GMP/HSE, and compliance standards (COPs, SOPs) | mixed |
| 2026-07-01_hse24_junior-expert-bi-analytics | Develop automated self-service BI solutions with consistent KPI definitions | Collaborate with data platform teams and business units on optimisation | No loss aversion framing. | mixed |
| 2026-07-01_jtl-software_senior-analytics-engineer | Owning the data foundation for a new AI-powered BI product | development, product, and pilot customers | No loss aversion framing. | strategic |
| 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst | Produce ad hoc reports and data extracts for business, audit, and compliance | No named teams identified; 'business and technical teams' are too generic to count. | Produce ad hoc reports and data extracts for business, audit, and compliance | execution |
| 2026-07-01_retail-consult_data-analytics-engineer | collaborating with Finance, Sales, HR, and Project Management teams to transform business needs | Finance, Sales, HR, and Project Management teams | No loss aversion framing. | mixed |
| 2026-07-01_size-up-consulting_senior-analytics-engineer | Design and maintain data models for analytical purposes; Build business indicators and semantic models for activity management | Product; Data Engineering; Data Analytics | ensure reliable, consistent, and accessible data | mixed |
| 2026-07-01_too-good-to-go_bi-developer | dashboard/reporting experience for commercial, finance, or logistics teams | Partner with Data Engineering teams on data optimisation; Dashboard/reporting experience for commercial, finance, or logistics teams | No loss aversion framing. | strategic |
| 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert | designing and evolving the analytical layer used across the organisation | work closely with the Data Team Lead, Senior Data Engineer, and business teams | Implement testing and data validation processes within dbt | mixed |
| 2026-07-02_acronis_senior-business-intelligence-analyst | enabling self-service dashboards and ad-hoc analysis in Power BI |  | ensuring data quality, operational excellence, and platform reliability through robust validation processes, monitoring, incident management, and well-defined operational procedures | strategic |
| 2026-07-02_archer-recruitment_senior-analytics-engineer-dbt-snowflake | owning the transformation layer of a modern cloud data platform | within a collaborative small team environment | Building reliable ELT pipelines using SQL and Python | strategic |
| 2026-07-02_asics_senior-business-intelligence-engineer | Directing data integration and pipeline orchestration across the organization | Providing technical support and training to colleagues; Promoting BI adoption and data literacy across EMEA | Establishing documentation, version control, and data privacy compliance | strategic |
| 2026-07-02_bose_data-analytics-engineer | will often serve as an internal expert about the data | analysts; product; software | Implement data quality tests and participate in ensuring the accuracy and reliability of data pipelines | execution |
| 2026-07-02_bridgerpay_senior-analytics-engineer | Build complex data models serving clean data to AI models, routing engines, and BI tools | No explicitly named partner teams identified | Ensure PCI-DSS/SOC2 compliance while optimizing costs | strategic |
| 2026-07-02_enza-zaden_senior-analytics-engineer | empower self-serve BI for teams across the organization | product owners; IT specialists; Architecture and Security teams | Improving data quality, reliability, performance and cost efficiency through lifecycle management | strategic |
| 2026-07-02_fullenrich_analytics-engineer | Conduct analytical work addressing business problems including provider cost/margin analysis, activation scoring, credit consumption pattern analysis | Finance, Marketing, RevOps, Sales, and Support teams | ensuring reliable access to the metrics across Finance, Marketing, RevOps, Sales, and Support teams | strategic |
| 2026-07-02_funke-medien_analytics-engineer | Reporting und der Marketing Automation fur das Zeitungsgeschaft | Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen | No loss aversion framing. | mixed |
| 2026-07-02_gerolsteiner_data-analytics-engineer | developing and maintaining data models, queries, and views... advancing existing Business Warehouse implementations... integrate new data sources | No named teams or functions referenced | The role encompasses developing and maintaining data models, queries, and views in SAP environments. | execution |
| 2026-07-02_ig-group_analytics-engineer | Build and maintain scalable, well-documented data models in dbt that enable self-service analytics for business users across IG | data engineers; data scientists | Safeguard data integrity through robust testing frameworks, documentation, and data quality practices | execution |
| 2026-07-02_ijsvogel-retail_analytics-engineer | translating business questions into dashboards and data solutions | works with stakeholders on information needs | monitors data quality and governance including GDPR compliance | mixed |
| 2026-07-02_mr-marvis_senior-analytics-engineer | Working with business teams to convert analytical needs into structured data solutions; Enabling governed access to trusted data sources | data engineers | Enabling governed access to trusted data sources | strategic |
| 2026-07-02_photowall_analytics-engineer | Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels | Design and maintain dashboards for Growth, Marketing, and Product teams | Establish monitoring and documentation protocols for data reliability | mixed |
| 2026-07-02_sii-poland_data-analytics-engineer | Partner with stakeholders, Data Engineers, and Analysts on requirements | Data Engineers; Analysts | Comfort in high engineering/governance standard environments | execution |
| 2026-07-02_sosafe_senior-analytics-engineer | Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents | Data Engineers; analytics; product | Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle | strategic |
| 2026-07-02_xomnia_data-analytics-engineer | developing self-service platforms | collaborating with data engineers | No loss aversion framing. | execution |
| 2026-07-02_amazon_business-intelligence-engineer-whs-data | Conducting analytical deep dives and formulating recommendations for leadership; Partnering with Data Engineering teams to enhance data infrastructure | Partnering with Data Engineering teams to enhance data infrastructure | Developing best practices in data integrity and documentation | mixed |

### ai_role — fully consistent across all JDs ✓

### testing_framing — fully consistent across all JDs ✓

### loss_aversion_framing — fully consistent across all JDs ✓
