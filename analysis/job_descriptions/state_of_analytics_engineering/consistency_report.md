# LLM Classification Consistency Report

**JDs classified:** 102  
**Runs per JD:** 3  
**Model:** claude-haiku-4-5  
**Method:** claude CLI subprocess  
**Traces:** see `jd_traces/<application_id>.md` for full per-JD evidence  

---

## Inter-run agreement (LLM self-consistency)

1.00 = all three runs identical. Lower = model is uncertain on this dimension.

| Dimension | Mean | Min | Max | Fully consistent (3/3) |
|-----------|------|-----|-----|------------------------|
| velocity_vs_rigour | 0.92 | 0.00 | 1.00 | 91/102 |
| domain_risk | 0.91 | 0.33 | 1.00 | 89/102 |
| collaboration_width | 0.76 | 0.00 | 1.00 | 68/102 |
| data_team_maturity | 0.95 | 0.33 | 1.00 | 95/102 |
| jd_authorship | 0.59 | 0.00 | 1.00 | 41/102 |
| stakeholder_orientation | 0.82 | 0.33 | 1.00 | 75/102 |
| autonomy_level | 0.68 | 0.00 | 1.00 | 54/102 |
| ai_role | 0.93 | 0.33 | 1.00 | 91/102 |
| testing_framing | 0.91 | 0.33 | 1.00 | 89/102 |
| loss_aversion_framing | 0.82 | 0.33 | 1.00 | 75/102 |

## Manual vs LLM majority-vote agreement

How often the LLM majority vote (best of 3) matches the original hand-coded classification.
High agreement → manual classifications are reproducible by the model.
Low agreement → either the codebook is ambiguous or the original call was subjective.

| Dimension | Match rate | n matched | n total |
|-----------|-----------|-----------|---------|
| velocity_vs_rigour | 73.5% | 75 | 102 |
| domain_risk | 76.5% | 78 | 102 |
| collaboration_width | 38.2% | 39 | 102 |
| data_team_maturity | 62.7% | 64 | 102 |
| jd_authorship | 50.0% | 51 | 102 |
| stakeholder_orientation | 88.2% | 90 | 102 |
| autonomy_level | 70.6% | 72 | 102 |
| ai_role | 0.0% | 0 | 102 |
| testing_framing | 0.0% | 0 | 102 |
| loss_aversion_framing | 0.0% | 0 | 102 |

## Evidence quote verification

Checks whether the verbatim quote cited by the LLM actually appears in the JD text.
Failures indicate hallucinated or paraphrased evidence.

| Dimension | Run 1 pass | Run 2 pass | Run 3 pass |
|-----------|-----------|-----------|-----------|
| velocity_vs_rigour | 100/102 | 100/102 | 102/102 |
| domain_risk | 99/102 | 95/102 | 98/102 |
| collaboration_width | 96/102 | 94/102 | 97/102 |
| data_team_maturity | 96/102 | 97/102 | 101/102 |
| jd_authorship | 98/102 | 98/102 | 100/102 |
| stakeholder_orientation | 91/102 | 91/102 | 94/102 |
| autonomy_level | 100/102 | 101/102 | 101/102 |
| ai_role | 101/102 | 100/102 | 99/102 |
| testing_framing | 86/102 | 83/102 | 83/102 |
| loss_aversion_framing | 99/102 | 98/102 | 101/102 |

## Disagreements: manual vs LLM majority vote

Each disagreement is a candidate for codebook revision or reclassification.
See `jd_traces/<application_id>.md` for full reasoning on each case.

### velocity_vs_rigour (27 disagreements)

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
| 2026-07-02_photowall_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Establish monitoring and documentation protocols for data reliability |
| 2026-07-02_xomnia_data-analytics-engineer | mixed | rigour | rigour | rigour | rigour | optimize data workflows for performance, usability, and cost efficiency |
| 2026-05-09_lightdash_analytics-engineering-advocate | velocity | mixed | mixed | velocity | mixed | balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process improvement |
| 2026-05-11_helmes_team-lead | rigour | velocity | velocity | rigour | velocity | Develop client relationships and seek new opportunities; Support sales and client acquisition |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | mixed | rigour | rigour | rigour | rigour | be the first to respond to incidents and drive resolution |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | mixed | rigour | rigour | rigour | rigour | Take full ownership of the stability of our marketing data pipelines — be the first to respond to incidents and drive re… |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | mixed | rigour | rigour | rigour | rigour | Take full ownership of the stability of our marketing data pipelines — be the first to respond to incidents and drive re… |
| 2026-06-20_just-dice_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Implement data quality and validation processes to guarantee data accuracy and consistency. |
| 2026-06-23_trade-republic_analytics-engineer | mixed | mixed | rigour | rigour | rigour | Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and … |
| 2026-06-20_almedia_analytics-engineer | mixed | rigour | rigour | rigour | rigour | Apply software engineering practices to analytics code, including version control, testing, and continuous integration. |
| 2026-06-27_doodle_growth-analytics-engineer | mixed | rigour | rigour | mixed | rigour | Build reusable datasets and reporting models eliminating manual work while improving data accessibility and reliability |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | rigour | velocity | rigour | mixed | velocity | Comfort working in a fast-moving, commercially oriented environment where priorities shift and ambiguity is part of the … |

### domain_risk (24 disagreements)

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
| 2026-05-09_lightdash_analytics-engineering-advocate | low | moderate | moderate | moderate | moderate | help teams with everything from building dashboards and writing SQL to analytics engineering best practices and data mod… |
| 2026-07-03_block-labs_business-intelligence-analyst | high | moderate | moderate | high | moderate | risk controls across our crypto-enabled iGaming products |
| 2026-05-11_helmes_team-lead | low | moderate | moderate | low | moderate | Manage finances (billing, reporting) |
| 2026-06-04_vinted_analytics-engineer-finance | high | moderate | moderate | high | moderate | Converting Finance requirements into technical solutions through requirements gathering |
| 2026-06-04_vinted_analytics-engineer-finance | high | moderate | moderate | moderate | moderate | Converting Finance requirements into technical solutions through requirements gathering |
| 2026-06-20_adsquare_staff-data-analytics-engineer | high | moderate | moderate | moderate | moderate | Build data products leveraging location signals and audience attributes |
| 2026-06-22_scoot_senior-analyst-business-intelligence | high | moderate | moderate | moderate | moderate | Distil complex data into meaningful business insights to facilitate decision-making and forward planning. |
| 2026-06-22_sumup_senior-analytics-engineer | high | moderate | moderate | moderate | moderate | Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring |
| 2026-06-23_trade-republic_analytics-engineer | high | moderate | moderate | moderate | moderate | Working closely with product and business stakeholders to define and build meaningful product metrics |
| 2026-06-25_uplearn_head-of-data | moderate | moderate | high | high | high | Take ownership of data privacy & school assurance: Become our day-to-day lead for data privacy and school-facing data as… |
| 2026-06-27_mentimeter_analytics-engineer | moderate | moderate | high | high | high | Experience working with GDPR-sensitive data and collaborating with legal experts on compliance |

### collaboration_width (63 disagreements)

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
| 2026-04-28_seven-senders_senior-bi-analyst | 3 | 1 | 1 | 1 | 1 | Act as translator between engineering and business stakeholders |
| 2026-05-01_aviv-group_senior-analytics-engineer | 4 | 2 | 2 | 2 | 2 | Collaborating with analysts, data scientists, and business stakeholders |
| 2026-07-02_photowall_analytics-engineer | 2 | 3 | 3 | 3 | 3 | Growth; Marketing; Product teams |
| 2026-05-01_wolt_senior-revenue-data-analyst | 5 | 4 | 5 | 4 | 4 | Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements |
| 2026-07-02_sii-poland_data-analytics-engineer | 3 | 2 | 2 | 2 | 2 | Data Engineers; Analysts |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | 2 | 0 | 0 | 0 | 0 | No named organizational teams identified |
| 2026-05-09_lightdash_analytics-engineering-advocate | 3 | 0 | 1 | 0 | 0 | You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on ca… |
| 2026-05-11_getyourguide_data-engineer | 3 | 2 | 2 | 2 | 2 | Product and Data teams |
| 2026-07-03_block-labs_business-intelligence-analyst | 3 | 6 | 4 | 4 | 4 | Product / CRM / Risk; Product, Marketing/CRM, Risk/Compliance, and Engineering |
| 2026-07-03_decathlon-digital_senior-bi-analytics-engineer-circularity | 1 | 0 | 0 | 0 | 0 | None - generic 'business teams' mentioned without named functions |
| 2026-05-13_smoobu_senior-analytics-engineer | 3 | 1 | 0 | 3 | 1 | engineering |
| 2026-07-03_enza-zaden_senior-analytics-engineer | 2 | 4 | 4 | 4 | 4 | product owners; IT; Architecture; Security teams |
| 2026-07-03_eraneos_analytics-engineer | 2 | 1 | 1 | 1 | 1 | analysts |
| 2026-04-08_riverty_data-engineering-lead | 9 | 8 | 8 | 9 | 8 | product owners; BI; data analysis; data science; Platform Engineering teams; Business IT teams; Data Governance; Data Ar… |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 5 | 4 | 4 | 4 | 4 | Work with data analysts, engineers, software engineers, and marketing teams |
| 2026-04-08_riverty_data-engineering-lead | 9 | 9 | 10 | 10 | 10 | product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT team… |
| 2026-07-03_fp-markets_senior-analytics-engineer | 4 | 5 | 5 | 5 | 5 | Finance, Risk, Operations, Product, Business Development |
| 2026-06-04_vinted_analytics-engineer-finance | 3 | 2 | 2 | 2 | 2 | Finance; Data Science |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 5 | 3 | 3 | 4 | 3 | Work with data analysts, engineers, software engineers, and marketing teams |
| 2026-06-20_adsquare_staff-data-analytics-engineer | 3 | 0 | 0 | 0 | 0 | Drive technical alignment across multiple teams |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 5 | 4 | 2 | 4 | 4 | Work with data analysts, engineers, software engineers, and marketing teams |
| 2026-06-20_just-dice_analytics-engineer | 2 | 3 | 3 | 3 | 3 | tech and product teams; marketing and product teams |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | 3 | 0 | 0 | 0 | 0 | No named partner teams identified |
| 2026-06-22_freenow_analytics-engineer | 4 | 3 | 3 | 3 | 3 | analysts; scientists; developers |
| 2026-06-22_scoot_senior-analyst-business-intelligence | 2 | 0 | 0 | 0 | 0 | Ability to understand and explain complex data and effective working as a liaison between technical and non-technical gr… |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | 3 | 2 | 2 | 2 | 2 | Analytics Consulting; DWH team |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | 3 | 0 | 0 | 0 | 0 | Represent data engineering in strategic initiatives, helping influence long-term planning and cross-functional alignment… |
| 2026-06-23_trade-republic_analytics-engineer | 2 | 1 | 1 | 2 | 1 | product and business stakeholders |
| 2026-06-25_uplearn_head-of-data | 3 | 3 | 4 | 4 | 4 | Product, Commercial, and Operations |
| 2026-06-20_almedia_analytics-engineer | 4 | 2 | 2 | 2 | 2 | Product Analysts; Data Scientists |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | 6 | 7 | 8 | 5 | 7 | product managers, commercial account managers, engineers, and data scientists; analysts; data engineers; AI engineers |
| 2026-06-27_decathlon-digital_senior-analytics-engineer | 1 | 0 | 0 | 0 | 0 | Contributing to the internal analytics and data engineering community |
| 2026-06-27_lansweeper_revenue-analytics-engineer | 4 | 3 | 3 | 2 | 3 | Partner with sales operations and finance; dashboards and reports that translate complex revenue data into clear, action… |
| 2026-06-27_lego-group_analytics-engineer | 9 | 5 | 5 | 5 | 5 | Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office Product teams; Shopper & Partn… |
| 2026-06-27_lexroom_analytics-engineer | 4 | 5 | 5 | 5 | 5 | Collaborate with engineers to improve event tracking and data contracts at the source; Create and curate dashboards and … |
| 2026-06-27_m13h_lead-analytics-engineer | 3 | 2 | 2 | 2 | 2 | data analysts et dataviz engineers |
| 2026-06-27_m13h_lead-analytics-engineer | 3 | 2 | 3 | 2 | 2 | data analysts et dataviz engineers |
| 2026-06-27_mentimeter_analytics-engineer | 4 | 1 | 1 | 4 | 1 | collaborating with legal experts on compliance |
| 2026-06-27_mentimeter_analytics-engineer | 4 | 3 | 4 | 0 | 3 | Strong business acumen with an understanding of sales, marketing, and product analytics |

### data_team_maturity (38 disagreements)

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
| 2026-05-09_lightdash_analytics-engineering-advocate | early | mid | mid | mid | mid | using Lightdash for our own analytics and demos |
| 2026-05-11_getyourguide_data-engineer | mature | mid | mid | mid | mid | Improve what's already in production: Pragmatically refactor and simplify existing pipelines |
| 2026-07-03_block-labs_business-intelligence-analyst | early | mid | mid | mid | mid | Build and maintain AI-agent workflows that automate recurring analytics - anomaly investigation, root-cause loops etc. |
| 2026-05-11_helmes_team-lead | early | mid | mature | mid | mid | Lead software development teams and projects |
| 2026-07-03_enza-zaden_senior-analytics-engineer | mature | mid | mid | mid | mid | Design, develop and maintain advanced data models and analytics products using tools like Databricks, dbt and Power BI |
| 2026-04-08_riverty_data-engineering-lead | mature | mid | mid | mature | mid | Lead, mentor, and grow a high-performing team of data engineers working across multiple agile data product teams. |
| 2026-04-08_riverty_data-engineering-lead | mature | mid | mid | mid | mid | build and scale a high-performing team of data engineers working across multiple agile data product teams |
| 2026-07-03_fp-markets_senior-analytics-engineer | early | mid | mid | mid | mid | building and scaling our new data platform from the ground up |
| 2026-06-20_adsquare_staff-data-analytics-engineer | mature | mid | mid | mid | mid | Establish monitoring frameworks for multi-terabyte data streams |
| 2026-06-20_just-dice_analytics-engineer | early | mid | mid | mid | mid | Create and maintain data architecture and data models for various business domains. Design, construct, and enhance data … |
| 2026-06-22_freenow_analytics-engineer | mature | mid | mid | mid | mid | within a Data Mesh environment |
| 2026-06-22_scoot_senior-analyst-business-intelligence | early | mid | mid | mid | mid | Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions. |
| 2026-06-22_sumup_senior-analytics-engineer | mature | mid | mid | mid | mid | maintaining staging pipelines, applying modelling conventions, and keeping domain outputs consistent, tested, and discov… |
| 2026-06-25_adsquare_staff-data-analytics-engineer | mature | mid | mid | mid | mid | Build data observability frameworks for multi-terabyte data streams |
| 2026-06-27_bolt_senior-analytics-engineer | mature | mid | mid | mid | mid | Build, expand and maintain reusable data models and metrics in dbt. |
| 2026-06-27_decathlon-digital_senior-analytics-engineer | mature | mid | mid | mid | mid | Automatiser et industrialiser les pipelines de transformation de données (automating data transformation pipelines for d… |
| 2026-06-27_dynatrace_senior-analytics-engineer | mature | mid | mid | mid | mid | Follow established SQL development and dbt modeling standards |
| 2026-06-27_lego-group_analytics-engineer | mature | mid | mid | mid | mid | the Analytics Engineering team's responsibility is to build an AI-enabled data foundation the entire company can rely on |
| 2026-06-27_mentimeter_analytics-engineer | mature | mid | mid | mid | mid | Design, own, and evolve core data models and the modelling architecture |
| 2026-06-27_mentimeter_analytics-engineer | mature | mid | mid | mid | mid | Develop, own and maintain data modeling standards and the data development experience |
| 2026-06-27_netflix_analytics-engineer-l5-localization | mature | mid | mid | mid | mid | improve foundational data models and accelerate productization of data insights |
| 2026-06-27_netflix_analytics-engineer-l5-localization | mature | mid | mid | mid | mid | join our growing EMEA team |

### jd_authorship (51 disagreements)

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
| 2026-05-01_aviv-group_senior-analytics-engineer | mixed | mixed | hiring_manager | hiring_manager | hiring_manager | Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake |
| 2026-07-02_photowall_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed | mixed | Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation |
| 2026-05-01_wolt_senior-revenue-data-analyst | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close |
| 2026-07-02_sii-poland_data-analytics-engineer | hiring_manager | mixed | hiring_manager | mixed | mixed | Build and maintain core data models using dbt for critical reporting; Contribute to the semantic layer (LookML) for cons… |
| 2026-07-02_xomnia_data-analytics-engineer | mixed | recruiter | recruiter | recruiter | recruiter | translating insights into dashboards, and contributing to internal knowledge sharing |
| 2026-05-09_lightdash_analytics-engineering-advocate | hiring_manager | mixed | mixed | mixed | mixed | You'll stay current with our latest features, including our evolving AI capabilities (using Lightdash for our own analyt… |
| 2026-05-11_getyourguide_data-engineer | hiring_manager | mixed | recruiter | recruiter | recruiter | Maintain balance between operational responsibilities and new development using team SLOs |
| 2026-07-03_decathlon-digital_senior-bi-analytics-engineer-circularity | hiring_manager | mixed | mixed | mixed | mixed | Monitor production data integrity and resolve incidents; Create documentation to help users work independently |
| 2026-07-03_enza-zaden_senior-analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Design, develop and maintain advanced data models and analytics products using tools like Databricks, dbt and Power BI |
| 2026-07-03_eraneos_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed | mixed | Develop dimensional models (Kimball Star Schema, Snowflake Schema, DataVault 2.0) |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | hiring_manager | hiring_manager | mixed | mixed | mixed | Maintain expertise across marketing tech stack including ad platforms, Airbyte, Zoho CRM, GTM, and web analytics |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | hiring_manager | hiring_manager | mixed | mixed | mixed | Maintain expertise across marketing tech stack including ad platforms, Airbyte, Zoho CRM, GTM, and web analytics |
| 2026-06-20_just-dice_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services. Create and maintain dat… |
| 2026-06-22_freenow_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed | mixed | Own the quality, availability, and trustworthiness of data — through quality checks and data contracts |
| 2026-06-22_scoot_senior-analyst-business-intelligence | recruiter | mixed | mixed | mixed | mixed | Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google… |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | mixed | hiring_manager | mixed | recruiter | hiring_manager | Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow. |
| 2026-06-23_trade-republic_analytics-engineer | hiring_manager | recruiter | recruiter | recruiter | recruiter | Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and a… |
| 2026-06-25_blue-orange-digital_analytics-engineer-power-bi-specialist | mixed | mixed | hiring_manager | hiring_manager | hiring_manager | Optimize DirectQuery and Import performance for financial datasets; Engage directly with stakeholders to translate requi… |
| 2026-06-25_marie-stella-maris_data-integration-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Build integrations using APIs and Celigo middleware |
| 2026-06-25_uplearn_head-of-data | hiring_manager | mixed | hiring_manager | mixed | mixed | warehouse/dbt/Lightdash stack reliable and scalable |
| 2026-06-27_datenna_senior-analytics-engineer | recruiter | mixed | mixed | mixed | mixed | Design efficient data models using techniques like star schema and snowflake schema |
| 2026-06-27_dynatrace_senior-analytics-engineer | mixed | hiring_manager | mixed | hiring_manager | hiring_manager | Design scalable analytical data models and curated datasets, conformed dimensions, and standardized metrics |
| 2026-06-27_eraneos_analytics-engineer | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Entwicklung dimensionaler Datenmodelle (Star Schema, Snowflake Schema, Data Vault) |
| 2026-06-27_lansweeper_revenue-analytics-engineer | mixed | hiring_manager | recruiter | mixed | hiring_manager | Reconcile revenue data across systems of record (CRM, billing, ERP) and ensure a single source of truth for financial KP… |
| 2026-06-27_lego-group_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed | mixed | Build and maintain semantic layer infrastructure including metric view pipelines, materialisation and optimisation |
| 2026-06-27_m13h_lead-analytics-engineer | mixed | mixed | hiring_manager | hiring_manager | hiring_manager | Mise en place des flux et modèles de données, en se basant sur des stacks data modernes (SQL, DBT, outils ELTs, GCP/Azur… |
| 2026-06-27_mentimeter_analytics-engineer | hiring_manager | mixed | mixed | hiring_manager | mixed | Strong SQL and sound judgment in data modelling (grain, reusability, naming, and how metrics should behave) |
| 2026-06-27_mentimeter_analytics-engineer | hiring_manager | mixed | mixed | mixed | mixed | Design, own, and evolve core data models and the modelling architecture |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Reduce dashboard sprawl by establishing centralised, standardised reporting in Omni |
| 2026-06-27_mr-marvis_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | mixed | hiring_manager | Build robust data pipelines translating complex business logic into scalable dbt models |
| 2026-06-27_mr-marvis_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Optimize warehouse usage through partitioning, clustering, and incremental modeling |
| 2026-06-27_perk_analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager | hiring_manager | Design, develop, and maintain efficient and scalable workflows using tools like dbt to transform raw data loaded into ou… |

### stakeholder_orientation (12 disagreements)

| application_id | manual | run1 | run2 | run3 | majority | run1 evidence quote |
|----------------|--------|------|------|------|----------|---------------------|
| 2026-04-22_qasa_analytics-engineer | internal_data | internal_data | mixed | mixed | mixed | Create self-serve analytics capabilities that empower teams to independently answer questions |
| 2026-04-24_getsafe_analytics-engineer | mixed | internal_data | mixed | internal_data | internal_data | Design clean, reliable, and well-documented data models as a single source of truth |
| 2026-07-02_fullenrich_analytics-engineer | mixed | commercial | commercial | commercial | commercial | reporting directly to Simon (RevOps) |
| 2026-07-02_funke-medien_analytics-engineer | commercial | commercial | internal_data | internal_data | internal_data | Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation für das Zeitungsgeschäft |
| 2026-07-02_photowall_analytics-engineer | commercial | mixed | product | mixed | mixed | Design and maintain dashboards for Growth, Marketing, and Product teams; Build and maintain the data infrastructure that… |
| 2026-07-02_sii-poland_data-analytics-engineer | internal_data | finance | internal_data | finance | finance | critical data models that support decision-making across credit, payments, and fraud/AML domains |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | internal_data | mixed | internal_data | mixed | mixed | Aimed at managers who need to be 'more inquisitive, more precise, more accurate in their statements, more selective in t… |
| 2026-07-02_xomnia_data-analytics-engineer | commercial | internal_data | internal_data | internal_data | internal_data | developing self-serve platforms |
| 2026-07-03_fp-markets_senior-analytics-engineer | finance | mixed | mixed | mixed | mixed | Collect requirements directly from business stakeholders — Finance, Risk, Operations, Product, Business Development |
| 2026-06-20_just-dice_analytics-engineer | product | mixed | mixed | mixed | mixed | Plan, execute, and evaluate experiments with our marketing and product teams; Establish the KPIs and metrics that will b… |
| 2026-06-25_dashlane_analytics-engineer | internal_data | mixed | mixed | mixed | mixed | Partner consultatively with Product, Go-to-Market, and business teams on data-driven insights |
| 2026-06-27_lansweeper_revenue-analytics-engineer | mixed | finance | finance | mixed | finance | Build, maintain, and improve the revenue data models that power executive-level reporting and board-ready metrics |

### autonomy_level (30 disagreements)

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
| 2026-04-28_seven-senders_senior-bi-analyst | execution | strategic | strategic | strategic | strategic | Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks |
| 2026-07-02_mr-marvis_senior-analytics-engineer | strategic | strategic | mixed | mixed | mixed | owning the analytics layer of our data platform |
| 2026-07-02_photowall_analytics-engineer | mixed | strategic | execution | mixed | strategic | Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation |
| 2026-07-02_sosafe_senior-analytics-engineer | strategic | strategic | mixed | mixed | mixed | Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models |
| 2026-05-11_helmes_team-lead | mixed | mixed | strategic | strategic | strategic | Lead software development teams and projects; Monitor performance and continuously improve work methods; Develop client … |
| 2026-07-03_decathlon-digital_senior-bi-analytics-engineer-circularity | execution | mixed | mixed | mixed | mixed | Design optimized datasets; Define KPIs; Lead proof-of-concept projects |
| 2026-07-03_fp-markets_senior-analytics-engineer | strategic | mixed | strategic | mixed | mixed | you still have the authority and ownership to shape the analytics foundation |
| 2026-06-20_just-dice_analytics-engineer | mixed | strategic | mixed | strategic | strategic | Design, construct, and enhance data pipelines; Create and maintain data architecture; Establish and implement data requi… |
| 2026-06-22_sumup_senior-analytics-engineer | execution | mixed | execution | mixed | mixed | Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelli… |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | execution | mixed | mixed | mixed | mixed | Define and enforce modeling standards and best practices |
| 2026-06-23_octopus-energy-germany_analytics-engineer | mixed | strategic | strategic | strategic | strategic | Du treibst die Weiterentwicklung unserer Datenarchitektur voran und etablierst Best Practices im Bereich Analytics Engin… |
| 2026-06-23_trade-republic_analytics-engineer | mixed | mixed | strategic | strategic | strategic | Taking ownership of projects from scoping to delivery and adoption, working autonomously |
| 2026-06-25_dashlane_analytics-engineer | mixed | strategic | strategic | strategic | strategic | shift the team from reactive support toward proactive strategy |
| 2026-06-25_egnyte_analytics-engineer | execution | mixed | mixed | execution | mixed | Design and build data transformation pipelines |
| 2026-06-25_marie-stella-maris_data-integration-engineer | mixed | execution | execution | mixed | execution | Translate business requirements into technical solutions |
| 2026-06-25_telavox_analytics-engineer | strategic | mixed | execution | mixed | mixed | Own the dbt project |
| 2026-06-27_bolt_senior-analytics-engineer | mixed | mixed | strategic | strategic | strategic | You own everything between data producers and data consumers: building the pipelines, models, and data products that emp… |
| 2026-06-27_dashlane_analytics-engineer | mixed | strategic | strategic | strategic | strategic | owning the data models that power decision-making across the company |
| 2026-06-27_lego-group_analytics-engineer | mixed | strategic | strategic | mixed | strategic | Build data pipeline engineering, orchestration, and monitoring to deliver high-quality data products |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | mixed | strategic | strategic | strategic | strategic | There is real space here to shape how analytics is delivered to commercial stakeholders, not just execute on requests. O… |
| 2026-06-27_mr-marvis_senior-analytics-engineer | mixed | strategic | mixed | strategic | strategic | Own the analytics layer at MR MARVIS. Build trusted data products that power smarter decisions |

### ai_role — no disagreements ✓

### testing_framing — no disagreements ✓

### loss_aversion_framing — no disagreements ✓

## LLM internal inconsistencies (runs disagree with each other)

These are cases where the same prompt produced different answers across 3 runs.
High inconsistency → borderline case or ambiguous JD language.

### velocity_vs_rigour (11 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_tem_staff-analytics-engineer | rigour | rigour | mixed | mixed |
| 2026-04-09_ai-futures_data-team-lead | rigour | rigour | velocity | velocity |
| 2026-04-22_distribusion_analytics-engineer | mixed | velocity | mixed | mixed |
| 2026-04-22_distribusion_analytics-engineer | rigour | mixed | mixed | mixed |
| 2026-05-09_lightdash_analytics-engineering-advocate | mixed | mixed | velocity | velocity |
| 2026-05-11_helmes_team-lead | velocity | velocity | rigour | rigour |
| 2026-06-23_trade-republic_analytics-engineer | mixed | rigour | rigour | mixed |
| 2026-06-27_doodle_growth-analytics-engineer | rigour | rigour | mixed | mixed |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | velocity | rigour | mixed | rigour |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | rigour | velocity | rigour | rigour |
| 2026-06-27_netflix_analytics-engineer-l5-localization | rigour | rigour | velocity | rigour |

### domain_risk (13 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-22_about-you_senior-data-engineer | moderate | high | high | high |
| 2026-04-09_nkg_sustainability-data-analyst | high | moderate | moderate | high |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | high | high | moderate | moderate |
| 2026-04-22_about-you_senior-data-engineer | high | moderate | moderate | high |
| 2026-04-22_polyteia_analytics-engineering-lead | moderate | moderate | high | high |
| 2026-04-22_qasa_analytics-engineer | high | high | moderate | moderate |
| 2026-04-22_qasa_analytics-engineer | high | moderate | high | moderate |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | low | low | moderate | low |
| 2026-07-03_block-labs_business-intelligence-analyst | moderate | moderate | high | high |
| 2026-05-11_helmes_team-lead | moderate | moderate | low | low |
| 2026-06-04_vinted_analytics-engineer-finance | moderate | moderate | high | high |
| 2026-06-25_uplearn_head-of-data | moderate | high | high | moderate |
| 2026-06-27_mentimeter_analytics-engineer | moderate | high | high | moderate |

### collaboration_width (34 inconsistent JDs)

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
| 2026-05-01_wolt_senior-revenue-data-analyst | 4 | 5 | 4 | 5 |
| 2026-07-02_sosafe_senior-analytics-engineer | 2 | 2 | 3 | 2 |
| 2026-05-09_lightdash_analytics-engineering-advocate | 0 | 1 | 0 | 3 |
| 2026-07-03_block-labs_business-intelligence-analyst | 6 | 4 | 4 | 3 |
| 2026-05-13_smoobu_senior-analytics-engineer | 1 | 0 | 3 | 3 |
| 2026-06-04_vinted_analytics-engineer-finance | 2 | 3 | 3 | 3 |
| 2026-04-08_riverty_data-engineering-lead | 8 | 8 | 9 | 9 |
| 2026-04-08_riverty_data-engineering-lead | 9 | 10 | 10 | 9 |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 3 | 3 | 4 | 5 |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | 4 | 2 | 4 | 5 |
| 2026-06-23_trade-republic_analytics-engineer | 1 | 1 | 2 | 2 |
| 2026-06-25_uplearn_head-of-data | 3 | 4 | 4 | 3 |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | 7 | 8 | 5 | 6 |
| 2026-06-27_lansweeper_revenue-analytics-engineer | 3 | 3 | 2 | 4 |
| 2026-06-27_m13h_lead-analytics-engineer | 2 | 3 | 2 | 3 |
| 2026-06-27_mentimeter_analytics-engineer | 1 | 1 | 4 | 4 |
| 2026-06-27_mentimeter_analytics-engineer | 3 | 4 | 0 | 4 |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | 4 | 4 | 5 | 4 |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | 2 | 3 | 3 | 3 |
| 2026-06-27_netflix_analytics-engineer-l5-localization | 5 | 4 | 4 | 4 |
| 2026-06-27_perk_analytics-engineer | 2 | 2 | 3 | 2 |

### data_team_maturity (7 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | early | early | early |
| 2026-04-10_decathlon_senior-data-analyst-analytics-engineer | mid | mid | early | early |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | early | mature | early | early |
| 2026-05-11_helmes_team-lead | mid | mature | mid | early |
| 2026-04-08_riverty_data-engineering-lead | mid | mid | mature | mature |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | mid | mature | mid | mid |
| 2026-06-27_m13h_lead-analytics-engineer | mature | mid | mid | mid |

### jd_authorship (61 inconsistent JDs)

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
| 2026-04-28_seven-senders_senior-bi-analyst | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-07-02_mr-marvis_senior-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-05-01_aviv-group_senior-analytics-engineer | mixed | hiring_manager | hiring_manager | mixed |
| 2026-07-02_photowall_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager |
| 2026-05-01_wolt_senior-revenue-data-analyst | hiring_manager | mixed | hiring_manager | mixed |
| 2026-07-02_sii-poland_data-analytics-engineer | mixed | hiring_manager | mixed | hiring_manager |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-05-11_getyourguide_data-engineer | mixed | recruiter | recruiter | hiring_manager |
| 2026-07-03_bravida_analytics-engineer | hiring_manager | hiring_manager | mixed | hiring_manager |
| 2026-07-03_eraneos_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager |
| 2026-04-08_riverty_data-engineering-lead | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | hiring_manager | hiring_manager | mixed | hiring_manager |
| 2026-06-04_vinted_analytics-engineer-finance | mixed | hiring_manager | recruiter | mixed |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | hiring_manager | mixed | mixed | hiring_manager |
| 2026-06-20_adsquare_staff-data-analytics-engineer | hiring_manager | mixed | hiring_manager | hiring_manager |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | hiring_manager | mixed | mixed | hiring_manager |
| 2026-06-20_just-dice_analytics-engineer | hiring_manager | mixed | hiring_manager | mixed |
| 2026-06-22_freenow_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager |
| 2026-06-22_the-quality-group-gmbh_senior-analytics-engineer | mixed | hiring_manager | mixed | mixed |
| 2026-06-23_lovehoney-group_senior-analytics-engineer | hiring_manager | mixed | recruiter | mixed |
| 2026-06-25_adsquare_staff-data-analytics-engineer | hiring_manager | hiring_manager | mixed | hiring_manager |
| 2026-06-25_blue-orange-digital_analytics-engineer-power-bi-specialist | mixed | hiring_manager | hiring_manager | mixed |
| 2026-06-25_egnyte_analytics-engineer | mixed | mixed | recruiter | mixed |
| 2026-06-25_marie-stella-maris_data-integration-engineer | mixed | mixed | hiring_manager | hiring_manager |
| 2026-06-25_uplearn_head-of-data | mixed | hiring_manager | mixed | hiring_manager |
| 2026-06-20_almedia_analytics-engineer | hiring_manager | mixed | mixed | mixed |
| 2026-06-27_dashlane_analytics-engineer | mixed | hiring_manager | hiring_manager | hiring_manager |
| 2026-06-27_decathlon-digital_senior-analytics-engineer | hiring_manager | recruiter | mixed | hiring_manager |
| 2026-06-27_doodle_growth-analytics-engineer | recruiter | mixed | mixed | mixed |
| 2026-06-27_dynatrace_senior-analytics-engineer | hiring_manager | mixed | hiring_manager | mixed |
| 2026-06-27_eraneos_analytics-engineer | hiring_manager | hiring_manager | mixed | mixed |
| 2026-06-27_lansweeper_revenue-analytics-engineer | hiring_manager | recruiter | mixed | mixed |
| 2026-06-27_lego-group_analytics-engineer | mixed | hiring_manager | mixed | hiring_manager |
| 2026-06-27_m13h_lead-analytics-engineer | hiring_manager | mixed | mixed | mixed |
| 2026-06-27_m13h_lead-analytics-engineer | mixed | hiring_manager | hiring_manager | mixed |
| 2026-06-27_mentimeter_analytics-engineer | mixed | mixed | hiring_manager | hiring_manager |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | hiring_manager | hiring_manager | mixed | mixed |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | hiring_manager | mixed | mixed | mixed |
| 2026-06-27_mr-marvis_senior-analytics-engineer | hiring_manager | hiring_manager | mixed | mixed |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | mixed | mixed | hiring_manager | mixed |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | mixed | hiring_manager | mixed | mixed |
| 2026-06-27_netflix_analytics-engineer-l5-localization | recruiter | mixed | mixed | mixed |

### stakeholder_orientation (27 inconsistent JDs)

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
| 2026-07-02_photowall_analytics-engineer | mixed | product | mixed | commercial |
| 2026-07-02_sii-poland_data-analytics-engineer | finance | internal_data | finance | internal_data |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | mixed | internal_data | mixed | internal_data |
| 2026-05-09_lightdash_analytics-engineering-advocate | commercial | product | commercial | commercial |
| 2026-07-03_block-labs_business-intelligence-analyst | mixed | mixed | commercial | mixed |
| 2026-05-11_helmes_team-lead | mixed | commercial | commercial | commercial |
| 2026-06-04_vinted_analytics-engineer-finance | internal_data | finance | finance | finance |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | commercial | commercial | mixed | commercial |
| 2026-06-23_trade-republic_analytics-engineer | product | mixed | product | product |
| 2026-06-25_uplearn_head-of-data | mixed | product | mixed | mixed |
| 2026-06-27_bolt_senior-analytics-engineer | product | internal_data | internal_data | internal_data |
| 2026-06-27_doodle_growth-analytics-engineer | commercial | mixed | mixed | mixed |
| 2026-06-27_lansweeper_revenue-analytics-engineer | finance | finance | mixed | mixed |
| 2026-06-27_lego-group_analytics-engineer | commercial | commercial | internal_data | commercial |
| 2026-06-27_lexroom_analytics-engineer | product | product | internal_data | product |
| 2026-06-27_m13h_lead-analytics-engineer | internal_data | commercial | internal_data | internal_data |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | finance | internal_data | finance | finance |

### autonomy_level (48 inconsistent JDs)

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
| 2026-07-02_mr-marvis_senior-analytics-engineer | strategic | mixed | mixed | strategic |
| 2026-07-02_photowall_analytics-engineer | strategic | execution | mixed | mixed |
| 2026-05-09_forward-college_lecturer-business-analytics-statistics | execution | mixed | execution | execution |
| 2026-07-02_sosafe_senior-analytics-engineer | strategic | mixed | mixed | strategic |
| 2026-05-09_lightdash_analytics-engineering-advocate | execution | mixed | mixed | mixed |
| 2026-07-03_block-labs_business-intelligence-analyst | strategic | mixed | strategic | strategic |
| 2026-05-11_helmes_team-lead | mixed | strategic | strategic | mixed |
| 2026-05-13_smoobu_senior-analytics-engineer | strategic | strategic | mixed | strategic |
| 2026-07-03_enza-zaden_senior-analytics-engineer | strategic | execution | strategic | strategic |
| 2026-06-04_vinted_analytics-engineer-finance | execution | execution | mixed | execution |
| 2026-07-03_fp-markets_senior-analytics-engineer | mixed | strategic | mixed | strategic |
| 2026-06-04_vinted_analytics-engineer-finance | execution | execution | mixed | execution |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | strategic | strategic | mixed | strategic |
| 2026-06-20_just-dice_analytics-engineer | strategic | mixed | strategic | mixed |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | mixed | mixed | strategic | mixed |
| 2026-06-22_sumup_senior-analytics-engineer | mixed | execution | mixed | execution |
| 2026-06-23_trade-republic_analytics-engineer | mixed | strategic | strategic | mixed |
| 2026-06-25_blue-orange-digital_analytics-engineer-power-bi-specialist | execution | mixed | execution | execution |
| 2026-06-25_egnyte_analytics-engineer | mixed | mixed | execution | execution |
| 2026-06-25_marie-stella-maris_data-integration-engineer | execution | execution | mixed | mixed |
| 2026-06-25_telavox_analytics-engineer | mixed | execution | mixed | strategic |
| 2026-06-20_almedia_analytics-engineer | execution | strategic | execution | execution |
| 2026-06-27_blue-orange-digital_analytics-engineer-power-bi-specialist | execution | execution | strategic | execution |
| 2026-06-27_bolt_senior-analytics-engineer | mixed | strategic | strategic | mixed |
| 2026-06-27_decathlon-digital_senior-analytics-engineer | strategic | mixed | mixed | mixed |
| 2026-06-27_eraneos_analytics-engineer | execution | execution | mixed | execution |
| 2026-06-27_lansweeper_revenue-analytics-engineer | mixed | mixed | execution | mixed |
| 2026-06-27_lego-group_analytics-engineer | strategic | strategic | mixed | mixed |
| 2026-06-27_lexroom_analytics-engineer | strategic | mixed | strategic | strategic |
| 2026-06-27_m13h_lead-analytics-engineer | mixed | execution | mixed | mixed |
| 2026-06-27_mentimeter_analytics-engineer | strategic | mixed | strategic | strategic |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | strategic | mixed | mixed | mixed |
| 2026-06-27_mr-marvis_senior-analytics-engineer | strategic | mixed | mixed | mixed |
| 2026-06-27_mr-marvis_senior-analytics-engineer | strategic | mixed | strategic | mixed |
| 2026-06-27_n26_senior-risk-data-and-analytics-engineer | execution | execution | mixed | execution |

### ai_role (11 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-08_lego_senior-analytics-engineer | ai_user | ai_enabler | ai_enabler |  |
| 2026-04-08_lego_senior-analytics-engineer | ai_enabler | none | ai_enabler |  |
| 2026-04-22_qasa_analytics-engineer | ai_user | none | ai_user |  |
| 2026-07-02_mr-marvis_senior-analytics-engineer | ai_enabler | ai_enabler | ai_user |  |
| 2026-07-02_sosafe_senior-analytics-engineer | ai_enabler | ai_enabler | none |  |
| 2026-07-03_block-labs_business-intelligence-analyst | ai_enabler | ai_user | ai_enabler |  |
| 2026-04-08_riverty_data-engineering-lead | none | ai_enabler | none |  |
| 2026-06-25_telavox_analytics-engineer | none | ai_enabler | ai_enabler |  |
| 2026-06-27_lexroom_analytics-engineer | ai_enabler | none | none |  |
| 2026-06-27_mr-marvis_senior-analytics-engineer | ai_user | ai_user | ai_enabler |  |
| 2026-06-27_mr-marvis_senior-analytics-engineer | ai_user | ai_enabler | ai_user |  |

### testing_framing (13 inconsistent JDs)

| application_id | run1 | run2 | run3 | manual |
|----------------|------|------|------|--------|
| 2026-04-22_about-you_senior-data-engineer | tool_listed | tool_listed | responsibility |  |
| 2026-04-22_mentimeter_analytics-engineer | absent | absent | tool_listed |  |
| 2026-04-28_seven-senders_senior-bi-analyst | responsibility | tool_listed | tool_listed |  |
| 2026-05-11_getyourguide_data-engineer | tool_listed | responsibility | responsibility |  |
| 2026-07-03_enza-zaden_senior-analytics-engineer | tool_listed | responsibility | responsibility |  |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | tool_listed | tool_listed | absent |  |
| 2026-06-20_1komma5grad_senior-analytics-engineer-growth | tool_listed | absent | tool_listed |  |
| 2026-06-22_scoot_senior-analyst-business-intelligence | absent | absent | responsibility |  |
| 2026-06-22_sumup_senior-analytics-engineer | responsibility | tool_listed | responsibility |  |
| 2026-06-23_octopus-energy-germany_analytics-engineer | responsibility | tool_listed | responsibility |  |
| 2026-06-25_blue-orange-digital_analytics-engineer-power-bi-specialist | tool_listed | absent | absent |  |
| 2026-06-27_netflix_analytics-engineer-l5-localization | absent | absent | responsibility |  |
| 2026-06-27_netflix_analytics-engineer-l5-localization | responsibility | absent | absent |  |

### loss_aversion_framing (27 inconsistent JDs)

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
| 2026-04-28_seven-senders_senior-bi-analyst | none | moderate | none |  |
| 2026-05-01_wolt_senior-revenue-data-analyst | high | high | moderate |  |
| 2026-07-02_sii-poland_data-analytics-engineer | high | high | moderate |  |
| 2026-07-03_bravida_analytics-engineer | moderate | moderate | none |  |
| 2026-04-08_riverty_data-engineering-lead | high | high | moderate |  |
| 2026-06-20_wolt_senior-analytics-engineer-merchant | moderate | none | moderate |  |
| 2026-06-22_scoot_senior-analyst-business-intelligence | none | moderate | moderate |  |
| 2026-06-25_telavox_analytics-engineer | high | moderate | moderate |  |
| 2026-06-25_uplearn_head-of-data | moderate | high | high |  |
| 2026-06-27_ascenda-loyalty_senior-analytics-engineer | high | moderate | moderate |  |
| 2026-06-27_blue-orange-digital_analytics-engineer-power-bi-specialist | none | moderate | moderate |  |
| 2026-06-27_lexroom_analytics-engineer | moderate | high | high |  |
| 2026-06-27_mollie_analytics-engineer-revenue-operations | none | moderate | moderate |  |
| 2026-06-27_mr-marvis_senior-analytics-engineer | high | moderate | moderate |  |
