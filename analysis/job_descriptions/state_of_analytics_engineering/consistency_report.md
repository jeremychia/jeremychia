# LLM Classification Consistency Report

**JDs classified:** 33  
**Runs per JD:** 3  
**Model:** claude-haiku-4-5  
**Method:** claude CLI subprocess  
**Traces:** see `jd_traces/<application_id>.md` for full per-JD evidence  

---

## Inter-run agreement (LLM self-consistency)

1.00 = all three runs identical. Lower = model is uncertain on this dimension.

| Dimension | Mean | Min | Max | Fully consistent (3/3) |
|-----------|------|-----|-----|------------------------|
| velocity_vs_rigour | 0.92 | 0.33 | 1.00 | 29/33 |
| domain_risk | 0.86 | 0.33 | 1.00 | 26/33 |
| collaboration_width | 0.73 | 0.00 | 1.00 | 20/33 |
| data_team_maturity | 0.96 | 0.33 | 1.00 | 31/33 |
| jd_authorship | 0.62 | 0.33 | 1.00 | 14/33 |
| stakeholder_orientation | 0.80 | 0.33 | 1.00 | 23/33 |
| autonomy_level | 0.72 | 0.00 | 1.00 | 20/33 |
| ai_role | 0.94 | 0.33 | 1.00 | 30/33 |
| testing_framing | 0.96 | 0.33 | 1.00 | 31/33 |
| loss_aversion_framing | 0.74 | 0.33 | 1.00 | 20/33 |

## Manual vs LLM majority-vote agreement

How often the LLM majority vote (best of 3) matches the original hand-coded classification.
High agreement → manual classifications are reproducible by the model.
Low agreement → either the codebook is ambiguous or the original call was subjective.

| Dimension | Match rate | n matched | n total |
|-----------|-----------|-----------|---------|
| velocity_vs_rigour | 54.5% | 18 | 33 |
| domain_risk | 60.6% | 20 | 33 |
| collaboration_width | 27.3% | 9 | 33 |
| data_team_maturity | 51.5% | 17 | 33 |
| jd_authorship | 42.4% | 14 | 33 |
| stakeholder_orientation | 87.9% | 29 | 33 |
| autonomy_level | 72.7% | 24 | 33 |
| ai_role | 0.0% | 0 | 33 |
| testing_framing | 0.0% | 0 | 33 |
| loss_aversion_framing | 0.0% | 0 | 33 |

## Evidence quote verification

Checks whether the verbatim quote cited by the LLM actually appears in the JD text.
Failures indicate hallucinated or paraphrased evidence.

| Dimension | Run 1 pass | Run 2 pass | Run 3 pass |
|-----------|-----------|-----------|-----------|
| velocity_vs_rigour | 32/33 | 33/33 | 33/33 |
| domain_risk | 31/33 | 30/33 | 31/33 |
| collaboration_width | 31/33 | 29/33 | 32/33 |
| data_team_maturity | 31/33 | 33/33 | 33/33 |
| jd_authorship | 31/33 | 31/33 | 32/33 |
| stakeholder_orientation | 30/33 | 28/33 | 31/33 |
| autonomy_level | 32/33 | 33/33 | 33/33 |
| ai_role | 33/33 | 33/33 | 32/33 |
| testing_framing | 25/33 | 22/33 | 25/33 |
| loss_aversion_framing | 31/33 | 33/33 | 32/33 |

## Disagreements: manual vs LLM majority vote

Each disagreement is a candidate for codebook revision or reclassification.
See `jd_traces/<application_id>.md` for full reasoning on each case.

### velocity_vs_rigour (15 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | mixed | rigour | rigour | mixed | rigour | Establish data quality standards using tests, CI/CD, and documentation. |
| 2026-04-08_tem_staff-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Establish data quality standards using tests, CI/CD, and documentation. |
| 2026-04-09_ai-futures_data-team-lead | velocity | rigour | rigour | velocity | rigour | Designing and building a modern data platform for "high-volume, real-time vehicle and transaction data" |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Document KPI definitions and business rules |
| 2026-04-22_about-you_senior-data-engineer | mixed | rigour | rigour | rigour | rigour | Strong software engineering fundamentals (CI/CD, testing, design patterns) |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Code complex business logic (royalties, taxable turnover, margins) |
| 2026-04-22_about-you_senior-data-engineer | mixed | rigour | rigour | rigour | rigour | Strong software engineering fundamentals (CI/CD, testing, design patterns) |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mixed | rigour | rigour | rigour | rigour | establishing the foundation for all financial reporting |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mixed | rigour | rigour | rigour | rigour | building scalable, well-structured models |
| 2026-04-22_qasa_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-22_qasa_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-24_getsafe_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Design clean, reliable, and well-documented data models as a single source of truth |
| 2026-07-02_fullenrich_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Comfort with ambiguity and rigorous data quality standards |
| 2026-07-03_riskpoint-group_business-intelligence-bi-developer | mixed | rigour | rigour | rigour | rigour | Ensuring data quality and integrity across platforms |
| 2026-07-02_funke-medien_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Sorgfältige Arbeitsweise und hohe Eigenmotivation |

### domain_risk (13 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | high | moderate | moderate | moderate | moderate | Design and maintain core dbt models representing business areas like customers, revenue, and operations. |
| 2026-04-08_tem_staff-analytics-engineer | high | moderate | moderate | moderate | moderate | Design and maintain core dbt models representing business areas like customers, revenue, and operations. |
| 2026-04-09_nkg_sustainability-data-analyst | high | moderate | moderate | moderate | moderate | Experience with EUDR compliance systems (e.g., osapiens) |
| 2026-04-09_nkg_sustainability-data-analyst | high | high | moderate | moderate | moderate | Experience with EUDR compliance systems (e.g., osapiens) |
| 2026-04-22_distribusion_analytics-engineer | high | moderate | moderate | moderate | moderate | Exposure to major clients like Booking.com and Google Maps |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | moderate | high | high | moderate | high | Code complex business logic (royalties, taxable turnover, margins) |
| 2026-04-22_about-you_senior-data-engineer | high | high | moderate | moderate | moderate | Own the most important company reports that inform executive decisions |
| 2026-04-22_distribusion_analytics-engineer | high | moderate | moderate | moderate | moderate | Exposure to major clients like Booking.com and Google Maps |
| 2026-04-22_polyteia_analytics-engineering-lead | high | moderate | moderate | high | moderate | Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal" |
| 2026-04-22_qasa_analytics-engineer | moderate | high | high | moderate | high | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-22_statista_analytics-engineer-reporting-platform | low | moderate | moderate | moderate | moderate | Increase transparency around data sources, KPI definitions, and report ownership. |
| 2026-04-22_qasa_analytics-engineer | moderate | high | moderate | high | high | Implement data governance protocols addressing GDPR compliance and access management |
| 2026-04-24_getsafe_analytics-engineer | high | moderate | moderate | moderate | moderate | Own and evolve core business metrics - from definition to tracking and operationalisation |

### collaboration_width (24 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | 8 | 10 | 5 | 6 | 10 | Analytics Interface; Commercial Analytics; Markets & Channels; Analytics Innovation & Automation; Data Office product te… |
| 2026-04-08_lego_senior-analytics-engineer | 8 | 6 | 5 | 5 | 5 | Analytics Interface; Commercial Analytics; Markets & Channels; Analytics Innovation & Automation; Data Office; Shopper &… |
| 2026-04-09_nkg_sustainability-data-analyst | 2 | 0 | 0 | 0 | 0 | Strong cross-functional collaboration abilities |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 4 | 1 | 0 | 1 | 1 | franchisees |
| 2026-04-22_about-you_senior-data-engineer | 3 | 1 | 0 | 0 | 0 | creating foundational tools and monitoring systems for other data teams |
| 2026-04-09_nkg_sustainability-data-analyst | 2 | 0 | 0 | 0 | 0 | No named partner teams or functions explicitly identified |
| 2026-04-22_distribusion_analytics-engineer | 3 | 0 | 0 | 0 | 0 | Collaborative international team environment |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 4 | 1 | 1 | 1 | 1 | franchisees |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 4 | 3 | 3 | 3 | Partner with data platform, engineering, and analytics teams; Mentor analytics engineers and analysts |
| 2026-04-22_about-you_senior-data-engineer | 3 | 1 | 0 | 1 | 1 | other data teams |
| 2026-04-22_mentimeter_analytics-engineer | 4 | 0 | 0 | 0 | 0 | business and technical stakeholders |
| 2026-04-22_distribusion_analytics-engineer | 3 | 0 | 0 | 0 | 0 | Collaborative international team environment |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 3 | 2 | 2 | 3 | 2 | finance, operations |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 3 | 3 | 3 | 3 | data platform, engineering, and analytics teams |
| 2026-04-22_mentimeter_analytics-engineer | 4 | 0 | 0 | 3 | 0 | Partner with business and technical stakeholders from problem framing to shipped artefacts |
| 2026-04-22_polyteia_analytics-engineering-lead | 2 | 1 | 1 | 2 | 1 | customer success teams |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 3 | 3 | 2 | 2 | 2 | finance; operations; leadership teams |
| 2026-04-22_qasa_analytics-engineer | 5 | 6 | 6 | 6 | 6 | Product; Marketing; Finance; Support; Country Management; engineering |
| 2026-04-22_polyteia_analytics-engineering-lead | 2 | 1 | 1 | 1 | 1 | collaborating closely with customer success teams |
| 2026-04-22_statista_analytics-engineer-reporting-platform | 4 | 0 | 0 | 0 | 0 | No named partner teams explicitly identified in responsibilities |
| 2026-04-22_qasa_analytics-engineer | 5 | 6 | 6 | 6 | 6 | Product, Marketing, Finance, Support, and Country Management teams; engineering |
| 2026-07-03_riskpoint-group_business-intelligence-bi-developer | 2 | 1 | 1 | 1 | 1 | analysts |
| 2026-07-02_funke-medien_analytics-engineer | 1 | 0 | 0 | 0 | 0 | Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen |
| 2026-07-03_telenet_analytics-engineer | 3 | 4 | 3 | 4 | 4 | Data Product Managers; Data Architects; Tech Leads; Data Engineers |

### data_team_maturity (16 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_tem_staff-analytics-engineer | early | mid | mid | mid | mid | This hands-on, individual contributor position focuses on building the analytics foundation. |
| 2026-04-08_tem_staff-analytics-engineer | early | mid | mid | mid | mid | Design and maintain core dbt models representing business areas like customers, revenue, and operations. |
| 2026-04-09_lovable_analytics-engineer-finance | early | mid | mid | mid | mid | Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics |
| 2026-04-09_nkg_sustainability-data-analyst | early | mid | mid | mid | mid | Develop and implement a unified sustainability data platform integrating multiple sources |
| 2026-04-09_ai-futures_data-team-lead | early | mid | mid | mid | mid | Growing and mentoring a data engineering team and contributing to hiring decisions |
| 2026-04-09_lovable_analytics-engineer-finance | early | mid | mid | mid | mid | Establish foundational tables for monthly/annual recurring revenue, churn analysis, and revenue patterns |
| 2026-04-09_nkg_sustainability-data-analyst | early | mid | mid | mid | mid | Design and operate scalable data pipelines within Microsoft Fabric |
| 2026-04-22_distribusion_analytics-engineer | early | mid | mid | mid | mid | Become proficient with the data lake, understanding data sources and processing workflows |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | early | mid | mid | early | mid | Early-stage opportunity to build and structure analytics capabilities |
| 2026-04-22_distribusion_analytics-engineer | early | mid | mid | mid | mid | Become proficient with the data lake, understanding data sources and processing workflows |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | early | mid | mid | mid | mid | Leading ERP data integration into the data warehouse and establishing the foundation for all financial reporting |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | early | mid | mid | mid | mid | proven experience with dbt building scalable, well-structured models |
| 2026-04-22_qasa_analytics-engineer | early | mid | mid | mid | mid | Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams |
| 2026-04-22_qasa_analytics-engineer | early | mid | mid | mid | mid | Partner with engineering to ensure data pipelines meet organizational needs |
| 2026-04-24_getsafe_analytics-engineer | early | mid | mid | mid | mid | Build and maintain scalable data pipelines and data marts using modern tooling |
| 2026-07-03_riskpoint-group_business-intelligence-bi-developer | early | mid | mid | mid | mid | Business Intelligence team, which currently has three members across Europe |

### jd_authorship (19 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization. Driv… |
| 2026-04-08_lego_senior-analytics-engineer | hiring_manager | hiring_manager | mixed | mixed | mixed | Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization |
| 2026-04-09_lovable_analytics-engineer-finance | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Document business logic for financial metrics including revenue recognition and deferred income |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | recruiter | mixed | mixed | mixed | Gather requirements and translate them into effective reporting and analytics solutions |
| 2026-04-09_ai-futures_data-team-lead | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner |
| 2026-04-09_lovable_analytics-engineer-finance | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Develop and sustain dimensional models using SQLMesh for revenue recognition and subscription metrics |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | mixed | mixed | recruiter | mixed | Design and operate scalable data pipelines within Microsoft Fabric; Create Power BI dashboards and reports for monitorin… |
| 2026-04-22_distribusion_analytics-engineer | recruiter | recruiter | mixed | mixed | mixed | Grasp project context quickly to identify critical needs and gaps |
| 2026-04-22_mentimeter_analytics-engineer | hiring_manager | mixed | recruiter | recruiter | recruiter | Design, own, and evolve core data models and the modelling architecture |
| 2026-04-22_distribusion_analytics-engineer | recruiter | mixed | mixed | mixed | mixed | Build new Looker dashboards from scratch within tight deadlines |
| 2026-04-22_mentimeter_analytics-engineer | hiring_manager | recruiter | mixed | mixed | mixed | Contribute strategic input around data modeling, BI tooling, and AI-assisted analytics |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | mixed | hiring_manager | hiring_manager | hiring_manager | Actively coding in Python, dbt, and Airflow while coordinating project advancement |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Actively coding in Python, dbt, and Airflow while coordinating project advancement |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | recruiter | mixed | recruiter | recruiter | Support documentation and governance efforts to improve maintainability and trust in reporting assets. |
| 2026-04-22_qasa_analytics-engineer | recruiter | mixed | recruiter | mixed | mixed | Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Partne… |
| 2026-04-24_getsafe_analytics-engineer | hiring_manager | mixed | recruiter | mixed | mixed | Develop the data and analytics components of the AI stack to support experimentation and GenAI applications |
| 2026-07-03_relyzit_analytics-engineer-freelance | recruiter | mixed | mixed | hiring_manager | mixed | Conducting automated data quality checks using tools such as Great Expectations; Designing and implementing robust data … |
| 2026-07-02_funke-medien_analytics-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Du entwickelst und implementierst eigenständig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github un… |
| 2026-07-03_telenet_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Perform Source-to-target analyses (S2T), identify gaps in source data and document required transformations using Agenti… |

### stakeholder_orientation (4 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-22_qasa_analytics-engineer | internal_data | internal_data | mixed | mixed | mixed | Create self-serve analytics capabilities that empower teams to independently answer questions |
| 2026-04-24_getsafe_analytics-engineer | mixed | internal_data | mixed | internal_data | internal_data | Design clean, reliable, and well-documented data models as a single source of truth |
| 2026-07-02_fullenrich_analytics-engineer | mixed | commercial | commercial | commercial | commercial | reporting directly to Simon (RevOps) |
| 2026-07-02_funke-medien_analytics-engineer | commercial | commercial | internal_data | internal_data | internal_data | Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation für das Zeitungsgeschäft |

### autonomy_level (9 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-08_lego_senior-analytics-engineer | strategic | execution | mixed | mixed | mixed | Build data pipeline engineering, orchestration, and monitoring to deliver high-quality data products centered around Ret… |
| 2026-04-08_lego_senior-analytics-engineer | strategic | execution | mixed | mixed | mixed | Collaborate closely with the Analytics Interface, Commercial Analytics and business teams to turn business requirements … |
| 2026-04-22_about-you_senior-data-engineer | strategic | execution | mixed | strategic | execution | drive the transition to our new DataPlatform (Dagster, dbt, AWS ECS, and GCP BigQuery) |
| 2026-04-09_nkg_sustainability-data-analyst | execution | mixed | mixed | mixed | mixed | Develop and implement a unified sustainability data platform; Gather requirements and translate them into effective repo… |
| 2026-04-22_distribusion_analytics-engineer | execution | strategic | execution | mixed | strategic | Direct ownership and measurable company impact from day one |
| 2026-04-22_statista_analytics-engineer-reporting-platform | mixed | execution | execution | execution | execution | Support the ongoing modernization of the BI stack |
| 2026-04-24_getsafe_analytics-engineer | strategic | mixed | mixed | mixed | mixed | Own and evolve core business metrics - from definition to tracking and operationalisation |
| 2026-07-02_funke-medien_analytics-engineer | mixed | execution | execution | execution | execution | Nach Deiner Einarbeitung wirst Du verantwortlich für zwei Topics |
| 2026-07-03_telenet_analytics-engineer | strategic | execution | mixed | mixed | mixed | You translate data requirements into robust and scalable solution designs and data models, and guide external Data Engin… |

### ai_role — no disagreements ✓

### testing_framing — no disagreements ✓

### loss_aversion_framing — no disagreements ✓

## LLM internal inconsistencies (runs disagree with each other)

These are cases where the same prompt produced different answers across 3 runs.
High inconsistency → borderline case or ambiguous JD language.

### velocity_vs_rigour (4 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_tem_staff-analytics-engineer | rigour | rigour | mixed | mixed |
| 2026-04-09_ai-futures_data-team-lead | rigour | rigour | velocity | velocity |
| 2026-04-22_distribusion_analytics-engineer | mixed | velocity | mixed | mixed |
| 2026-04-22_distribusion_analytics-engineer | rigour | mixed | mixed | mixed |

### domain_risk (7 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-22_about-you_senior-data-engineer | moderate | high | high | high |
| 2026-04-09_nkg_sustainability-data-analyst | high | moderate | moderate | high |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | high | high | moderate | moderate |
| 2026-04-22_about-you_senior-data-engineer | high | moderate | moderate | high |
| 2026-04-22_polyteia_analytics-engineering-lead | moderate | moderate | high | high |
| 2026-04-22_qasa_analytics-engineer | high | high | moderate | moderate |
| 2026-04-22_qasa_analytics-engineer | high | moderate | high | moderate |

### collaboration_width (13 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | 10 | 5 | 6 | 8 |
| 2026-04-08_lego_senior-analytics-engineer | 6 | 5 | 5 | 8 |
| 2026-04-09_ai-futures_data-team-lead | 2 | 2 | 1 | 2 |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 1 | 0 | 1 | 4 |
| 2026-04-22_about-you_senior-data-engineer | 1 | 0 | 0 | 3 |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 3 | 3 | 4 |
| 2026-04-22_about-you_senior-data-engineer | 1 | 0 | 1 | 3 |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 2 | 2 | 3 | 3 |
| 2026-04-22_mentimeter_analytics-engineer | 0 | 0 | 3 | 4 |
| 2026-04-22_polyteia_analytics-engineering-lead | 1 | 1 | 2 | 2 |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | 3 | 2 | 2 | 3 |
| 2026-04-22_shine_senior-analytics-engineer | 2 | 2 | 3 | 2 |
| 2026-07-03_telenet_analytics-engineer | 4 | 3 | 4 | 3 |

### data_team_maturity (2 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | early | early | early |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | mid | early | early |

### jd_authorship (19 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | mixed | mixed | hiring_manager | hiring_manager |
| 2026-04-08_lego_senior-analytics-engineer | hiring_manager | mixed | mixed | hiring_manager |
| 2026-04-08_tem_staff-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-04-08_tem_staff-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | mixed | mixed | recruiter |
| 2026-04-09_nkg_sustainability-data-analyst | mixed | mixed | recruiter | recruiter |
| 2026-04-22_distribusion_analytics-engineer | recruiter | mixed | mixed | recruiter |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | hiring_manager | mixed | mixed |
| 2026-04-22_mentimeter_analytics-engineer | mixed | recruiter | recruiter | hiring_manager |
| 2026-04-22_mentimeter_analytics-engineer | recruiter | mixed | mixed | hiring_manager |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | hiring_manager | hiring_manager | mixed |
| 2026-04-22_qasa_analytics-engineer | recruiter | mixed | recruiter | recruiter |
| 2026-04-22_shine_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-04-22_statista_analytics-engineer-reporting-platform | recruiter | mixed | recruiter | mixed |
| 2026-04-22_qasa_analytics-engineer | mixed | recruiter | mixed | recruiter |
| 2026-04-24_getsafe_analytics-engineer | mixed | recruiter | mixed | hiring_manager |
| 2026-07-02_fullenrich_analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-07-03_relyzit_analytics-engineer-freelance | mixed | mixed | hiring_manager | recruiter |
| 2026-07-02_funke-medien_analytics-engineer | mixed | mixed | hiring_manager | hiring_manager |

### stakeholder_orientation (10 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | internal_data | commercial | commercial | commercial |
| 2026-04-08_lego_senior-analytics-engineer | commercial | commercial | internal_data | commercial |
| 2026-04-22_about-you_senior-data-engineer | mixed | internal_data | internal_data | internal_data |
| 2026-04-22_distribusion_analytics-engineer | mixed | internal_data | internal_data | internal_data |
| 2026-04-22_mentimeter_analytics-engineer | internal_data | internal_data | mixed | internal_data |
| 2026-04-22_polyteia_analytics-engineering-lead | mixed | commercial | commercial | commercial |
| 2026-04-22_qasa_analytics-engineer | internal_data | internal_data | mixed | internal_data |
| 2026-04-22_qasa_analytics-engineer | internal_data | mixed | mixed | internal_data |
| 2026-04-24_getsafe_analytics-engineer | internal_data | mixed | internal_data | mixed |
| 2026-07-02_funke-medien_analytics-engineer | commercial | internal_data | internal_data | commercial |

### autonomy_level (13 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | execution | mixed | mixed | strategic |
| 2026-04-08_lego_senior-analytics-engineer | execution | mixed | mixed | strategic |
| 2026-04-09_nkg_sustainability-data-analyst | execution | execution | mixed | execution |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | execution | execution | execution |
| 2026-04-09_lovable_analytics-engineer-finance | mixed | execution | execution | execution |
| 2026-04-22_about-you_senior-data-engineer | execution | mixed | strategic | strategic |
| 2026-04-22_distribusion_analytics-engineer | execution | execution | mixed | execution |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | execution | execution | mixed | execution |
| 2026-04-22_distribusion_analytics-engineer | strategic | execution | mixed | execution |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | strategic | strategic | mixed | strategic |
| 2026-04-22_qasa_analytics-engineer | strategic | mixed | strategic | strategic |
| 2026-04-22_qasa_analytics-engineer | execution | strategic | strategic | strategic |
| 2026-07-03_telenet_analytics-engineer | execution | mixed | mixed | strategic |

### ai_role (3 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | ai_user | ai_enabler | ai_enabler |  |
| 2026-04-08_lego_senior-analytics-engineer | ai_enabler | none | ai_enabler |  |
| 2026-04-22_qasa_analytics-engineer | ai_user | none | ai_user |  |

### testing_framing (2 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-22_about-you_senior-data-engineer | tool_listed | tool_listed | responsibility |  |
| 2026-04-22_mentimeter_analytics-engineer | absent | absent | tool_listed |  |

### loss_aversion_framing (13 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_tem_staff-analytics-engineer | moderate | none | none |  |
| 2026-04-09_lovable_analytics-engineer-finance | moderate | high | high |  |
| 2026-04-09_nkg_sustainability-data-analyst | none | none | moderate |  |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | moderate | none | none |  |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | none | moderate | moderate |  |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | high | moderate | moderate |  |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | moderate | none | none |  |
| 2026-04-22_mentimeter_analytics-engineer | moderate | moderate | none |  |
| 2026-04-22_polyteia_analytics-engineering-lead | none | moderate | none |  |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | moderate | none | none |  |
| 2026-04-22_polyteia_analytics-engineering-lead | moderate | moderate | none |  |
| 2026-04-24_getsafe_analytics-engineer | moderate | none | moderate |  |
| 2026-07-02_funke-medien_analytics-engineer | none | none | moderate |  |
