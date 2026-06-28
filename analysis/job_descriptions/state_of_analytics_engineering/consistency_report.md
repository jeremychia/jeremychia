# LLM Classification Consistency Report

**JDs classified:** 35  
**Runs per JD:** 3 (all runs identical prompt, temperature not controllable via CLI)  
**Model:** claude-haiku-4-5  
**Method:** CLI subprocess (authenticated session)  

## Inter-run agreement (LLM self-consistency across 3 runs)

1.00 = all three runs produced the same classification. Lower = the LLM is uncertain on this JD/dimension.

| Dimension | Mean agreement | Min | Max | # fully consistent (1.0) |
|-----------|---------------|-----|-----|--------------------------|
| velocity_vs_rigour | 0.92 | 0.33 | 1.00 | 31/35 |
| domain_risk | 0.87 | 0.33 | 1.00 | 28/35 |
| collaboration_width | 0.90 | 0.33 | 1.00 | 30/35 |
| data_team_maturity | 0.89 | 0.33 | 1.00 | 29/35 |
| jd_authorship | 0.58 | 0.33 | 1.00 | 13/35 |

## Manual vs LLM majority-vote agreement

How often the LLM majority vote (best of 3) matches the original hand-coded classification.
This is the key validity check: high agreement means the manual classifications are reproducible.
Low agreement on a dimension means either the codebook is ambiguous or the original call was subjective.

| Dimension | Match rate | n matched | n total |
|-----------|-----------|-----------|---------|
| velocity_vs_rigour | 0.74 | 26 | 35 |
| domain_risk | 0.77 | 27 | 35 |
| collaboration_width | 0.23 | 8 | 35 |
| data_team_maturity | 0.54 | 19 | 35 |
| jd_authorship | 0.51 | 18 | 35 |

## Disagreements: manual vs LLM majority vote

Each disagreement is a case where the human analyst and LLM reached a different conclusion.
These are candidates for codebook revision or reclassification.

### velocity_vs_rigour (9 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 reasoning |
|----------------|--------|------|------|------|----------|----------------|
| 2026-04-09_ai-futures_data-team-lead | velocity | mixed | mixed | mixed | mixed | The JD emphasizes infrastructure building and team leadership (rigour-oriented), |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | rigour | rigour | rigour | rigour | Multiple signals emphasise governance and quality: "Document KPI definitions and |
| 2026-04-22_about-you_senior-data-engineer | mixed | rigour | rigour | rigour | rigour | The JD emphasizes 'maintaining source system performance', 'monitoring systems', |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | mixed | rigour | rigour | rigour | rigour | JD emphasizes 'establishing the foundation for all financial reporting' and crea |
| 2026-04-22_qasa_analytics-engineer | mixed | rigour | rigour | rigour | rigour | The JD emphasizes 'Implement data governance protocols addressing GDPR complianc |
| 2026-04-24_getsafe_analytics-engineer | mixed | rigour | rigour | rigour | rigour | JD emphasizes 'clean, reliable, and well-documented data models as a single sour |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | mixed | rigour | rigour | mixed | rigour | Emphasis on pipeline stability, incident response ('be the first to respond to i |
| 2026-06-20_almedia_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Core responsibilities emphasize 'Apply software engineering practices to analyti |
| 2026-06-20_just-dice_analytics-engineer | mixed | rigour | rigour | rigour | rigour | JD emphasizes 'Implement data quality and validation processes to guarantee data |

### domain_risk (8 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 reasoning |
|----------------|--------|------|------|------|----------|----------------|
| 2026-04-09_nkg_sustainability-data-analyst | high | moderate | moderate | moderate | moderate | The core responsibilities focus on 'unified sustainability data platform' and 'd |
| 2026-04-22_distribusion_analytics-engineer | high | moderate | moderate | moderate | moderate | JD focuses on reporting systems and dashboards without mentioning financial repo |
| 2026-04-22_qasa_analytics-engineer | moderate | high | high | moderate | high | The JD explicitly uses regulatory language ('GDPR compliance') and mentions 'fin |
| 2026-04-22_statista_analytics-engineer-reporting-platform | low | moderate | moderate | moderate | moderate | While Statista is a data company, the JD is for internal reporting platform admi |
| 2026-06-04_vinted_analytics-engineer-finance | high | moderate | moderate | high | moderate | The role focuses on 'Converting Finance requirements into technical solutions',  |
| 2026-06-20_adsquare_staff-data-analytics-engineer | high | moderate | moderate | moderate | moderate | Ad-tech role focused on location signals and audience attributes for business op |
| 2026-06-22_scoot_senior-analyst-business-intelligence | high | moderate | moderate | moderate | moderate | JD focuses on 'business insights to facilitate decision-making and forward plann |
| 2026-06-23_trade-republic_analytics-engineer | high | moderate | moderate | moderate | moderate | Trade Republic is fintech (sector defaults to high risk), but JD language is gen |

### collaboration_width (27 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 reasoning |
|----------------|--------|------|------|------|----------|----------------|
| 2026-04-08_lego_senior-analytics-engineer | 8 | 5 | 6 | 5 | 5 | Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Da |
| 2026-04-08_riverty_data-engineering-lead | 9 | 10 | 9 | 10 | 10 | Product Owners; BI; Data Analysis; Data Science; Data Platform; Tech teams; Plat |
| 2026-04-09_ai-futures_data-team-lead | 2 | 0 | 0 | 0 | 0 | Only external stakeholders are named (OEM partners, external developers); no int |
| 2026-04-09_nkg_sustainability-data-analyst | 2 | 0 | 0 | 0 | 0 | No distinct named teams or functions are explicitly identified; 'cross-functiona |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | 4 | 0 | 0 | 0 | 0 | No explicitly named internal teams identified; 'internal teams' mentioned but no |
| 2026-04-22_about-you_senior-data-engineer | 3 | 0 | 0 | 0 | 0 | The JD mentions 'other data teams' and 'other departments' but provides no speci |
| 2026-04-22_distribusion_analytics-engineer | 3 | 0 | 0 | 0 | 0 | No named internal teams or functions are explicitly identified; only vague refer |
| 2026-04-22_leasingmarkt_principal-analytics-engineer | 4 | 3 | 3 | 3 | 3 | data platform team; engineering team; analytics teams |
| 2026-04-22_mentimeter_analytics-engineer | 4 | 0 | 0 | 0 | 0 | No explicitly named partner teams are identified; 'business and technical stakeh |
| 2026-04-22_polyteia_analytics-engineering-lead | 2 | 1 | 1 | 1 | 1 | Only 'customer success teams' is explicitly named as a partner team; other funct |
| 2026-04-22_qasa_analytics-engineer | 5 | 6 | 6 | 6 | 6 | Product; Marketing; Finance; Support; Country Management; Engineering |
| 2026-04-22_statista_analytics-engineer-reporting-platform | 4 | 0 | 0 | 0 | 0 | No explicitly named partner teams (Finance, Product, Engineering, Data Science,  |
| 2026-04-28_seven-senders_senior-bi-analyst | 3 | 1 | 1 | 1 | 1 | Engineering |
| 2026-05-01_aviv-group_senior-analytics-engineer | 4 | 2 | 2 | 2 | 2 | analysts; data scientists |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | 2 | 0 | 0 | 0 | 0 | No named partner teams or functions are identified; 'staff' and 'Fellows' are me |
| 2026-05-11_getyourguide_data-engineer | 3 | 2 | 2 | 2 | 2 | Product; Data teams |
| 2026-06-04_vinted_analytics-engineer-finance | 3 | 2 | 2 | 2 | 2 | Finance (explicitly stated in 'Converting Finance requirements into technical so |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 5 | 4 | 4 | 3 | 4 | data analysts; engineers (data engineers); software engineers; marketing teams |
| 2026-06-20_adsquare_staff-data-analytics-engineer | 3 | 0 | 0 | 0 | 0 | No explicitly named partner teams or functions identified; all references use ge |
| 2026-06-20_almedia_analytics-engineer | 4 | 2 | 2 | 2 | 2 | Product Analysts; Data Scientists |
| 2026-06-20_just-dice_analytics-engineer | 2 | 3 | 3 | 3 | 3 | Product team; Tech/Engineering team; Marketing team |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | 3 | 0 | 0 | 0 | 0 | No named partner teams (Finance, Product, Engineering, Operations, etc.) are exp |
| 2026-06-22_freenow_analytics-engineer | 4 | 3 | 3 | 3 | 3 | Analysts; Data Scientists; Developers |
| 2026-06-22_scoot_senior-analyst-business-intelligence | 2 | 0 | 0 | 0 | 0 | No named teams are explicitly mentioned; phrases like 'liaison between technical |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | 3 | 2 | 2 | 2 | 2 | Analytics Consulting; DWH team |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | 3 | 0 | 0 | 0 | 0 | The JD uses generic phrases like 'cross-functional alignment' and 'strategic ini |
| 2026-06-23_trade-republic_analytics-engineer | 2 | 1 | 2 | 1 | 1 | Only 'product' is explicitly named as a partner team; 'business stakeholders' is |

### data_team_maturity (16 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 reasoning |
|----------------|--------|------|------|------|----------|----------------|
| 2026-04-08_riverty_data-engineering-lead | mature | mid | mid | mid | mid | The JD references 'build and scale', multiple sub-teams ('agile data product tea |
| 2026-04-08_tem_staff-analytics-engineer | early | mid | mid | early | mid | The JD frames the role as 'building the analytics foundation' while already spec |
| 2026-04-09_ai-futures_data-team-lead | early | mid | mid | mid | mid | The JD emphasizes "Designing and building a modern data platform" paired with "G |
| 2026-04-09_lovable_analytics-engineer-finance | early | mid | mid | mid | mid | JD references existing infrastructure (SQLMesh, cloud warehouses, BI platforms)  |
| 2026-04-09_nkg_sustainability-data-analyst | early | mid | mid | mid | mid | Responsibilities include 'develop and implement a unified sustainability data pl |
| 2026-04-22_distribusion_analytics-engineer | early | mid | mid | mid | mid | Established data infrastructure (data lake, BigQuery, Kafka, Airflow) already ex |
| 2026-04-22_pergolux_senior-analytics-engineer-finance-operations | early | mid | mid | early | mid | JD states 'establishing the foundation for all financial reporting' and 'leading |
| 2026-04-22_qasa_analytics-engineer | early | mid | mid | mid | mid | The JD emphasizes foundational activities ('Establish unified KPIs', 'Design and |
| 2026-04-24_getsafe_analytics-engineer | early | mid | mid | mid | mid | JD describes 'evolving core business metrics' and developing 'AI-ready data foun |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | early | mid | mid | mid | mid | The program is based on established LSE curriculum with a 150-student cohort, st |
| 2026-05-11_getyourguide_data-engineer | mature | mid | mid | mid | mid | JD mentions 'improve what's already in production' and 'operational responsibili |
| 2026-06-20_adsquare_staff-data-analytics-engineer | mature | mid | mid | mature | mid | Multiple squads, established data warehouse/lake tools (Snowflake, Redshift, Ath |
| 2026-06-20_just-dice_analytics-engineer | early | mid | mid | mid | mid | JD mentions maintaining established tools (dbt, AWS, Tableau) and tasks to 'enha |
| 2026-06-22_freenow_analytics-engineer | mature | mid | mature | mid | mid | The organisation operates 'within a Data Mesh environment' with established infr |
| 2026-06-22_scoot_senior-analyst-business-intelligence | early | mid | mid | mid | mid | JD states the role will 'Maintain and manage advanced reporting, analyses, dashb |
| 2026-06-22_sumup_senior-analytics-engineer | mature | mid | mid | mid | mid | JD describes scaling existing infrastructure ('incremental processing strategies |

### jd_authorship (17 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 reasoning |
|----------------|--------|------|------|------|----------|----------------|
| 2026-04-08_lego_senior-analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Responsibilities section contains precise technical context ('Unity Catalog gove |
| 2026-04-09_ai-futures_data-team-lead | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Technical specificity is evident throughout: named architectural patterns (medal |
| 2026-04-09_lovable_analytics-engineer-finance | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Technical specificity about 'SQLMesh for revenue recognition and subscription me |
| 2026-04-09_nkg_sustainability-data-analyst | recruiter | mixed | mixed | mixed | mixed | Specific tools are named (Microsoft Fabric, Power BI, DAX, SQL) but without prec |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Specific technical depth throughout: "dbt on Databricks", "LODs, parameters, com |
| 2026-04-22_distribusion_analytics-engineer | recruiter | mixed | mixed | mixed | mixed | Specific tools named (BigQuery, Kafka, Airflow, Looker) with technical requireme |
| 2026-04-22_mentimeter_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Responsibilities are somewhat generic ('Design, own, and evolve core data models |
| 2026-04-22_qasa_analytics-engineer | recruiter | mixed | hiring_manager | mixed | mixed | The responsibilities section shows technical precision (GDPR governance protocol |
| 2026-04-24_getsafe_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Responsibilities section demonstrates technical domain knowledge (metrics owners |
| 2026-05-01_aviv-group_senior-analytics-engineer | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Responsibilities contain specific technical methodology (data contracts, semanti |
| 2026-05-01_wolt_senior-revenue-data-analyst | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Specific mention of "Leverage AI tools like Claude Code and Cursor to accelerate |
| 2026-05-11_getyourguide_data-engineer | hiring_manager | mixed | mixed | mixed | mixed | Responsibilities mix generic language ('best practices', 'thought partner') with |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | hiring_manager | hiring_manager | mixed | mixed | mixed | Responsibilities demonstrate deep domain specificity ('you know them by heart an |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | hiring_manager | hiring_manager | mixed | mixed | mixed | 'Design and implement complex data pipelines with dependency control and orchest |
| 2026-06-22_freenow_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | The responsibilities section demonstrates technical domain knowledge (Data Mesh, |
| 2026-06-22_scoot_senior-analyst-business-intelligence | recruiter | mixed | mixed | mixed | mixed | JD includes some technical specificity in requirements ('Tableau (Dashboard crea |
| 2026-06-23_trade-republic_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Responsibilities use generic analytics engineering language ('develop analytical |

## Skipped

- 2026-05-09_lightdash_analytics-engineering-advocate — one or more runs failed
- 2026-05-11_helmes_team-lead — one or more runs failed
- 2026-06-23_octopus-energy-germany_analytics-engineer — not in CSV