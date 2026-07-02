# Trace: 2026-07-01_deloitte_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Deloitte

**URL:** https://empleo.es.deloitte.com/job/Madrid-Analytics-Engineer/1275887201/
**Location:** Madrid, Spain (Hybrid)
**Date Posted:** 2026-07-01

---

Analytics Engineer at Deloitte Spain

Location: Madrid
Position Type: Profesionales con experiencia (Experienced Professionals)
Service Line: SRT (Strategy, Risk & Transactions)
Req ID: 45442

About the Company
Deloitte is committed to generating impact on society, clients, and employees. The firm works with leading international organisations across their entire value chain.

Role Summary
The Analytics Engineer role combines technical expertise with strategic vision. This professional will design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools. The role involves direct client contact to understand challenges and translate needs into data solutions that drive business impact.

Key Responsibilities
- Co-create Data Products with business stakeholders for strategic decision-making
- Design reliable, scalable, efficient data pipelines from internal and external sources
- Design data models facilitating analysis and business objectives
- Develop and optimise procedures to productionize models with monitoring capabilities
- Implement visualisation solutions for intuitive data comprehension
- Stay current with best practices for development and continuous integration

Requirements
Education & Language:
- Degree in Engineering, Mathematics, Physics, or similar
- C1 English proficiency (spoken and written)

Technical Skills:
- Experience with ETL, SQL, and Python in local, Cloud, and Big Data environments
- Knowledge of modern data processing technologies: dbt, Spark, BigQuery, Snowflake, Databricks
- Data storage knowledge (files, relational, columnar, documents, key-value)
- Machine Learning and MLOps experience
- Data visualisation with BI tools (Tableau, Power BI) or web development
- Data modelling comprehension and reporting capabilities

Soft Skills:
- Adaptable, communicative, client-oriented
- Initiative and dynamism
- Collaborative teamwork abilities
- Complex information analysis and synthesis

Work Environment
Hybrid-flexible arrangements, team-building activities, wellness programs, volunteer opportunities, continuous learning culture, and comprehensive benefits packages.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 0 | 0 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | recruiter | recruiter | 33% |
| stakeholder_orientation | internal_data | commercial | mixed | 0% |
| autonomy_level | execution | mixed | execution | 33% |
| ai_role | ai_enabler | ai_enabler | ai_enabler | 100% |
| testing_framing | tool_listed | absent | absent | 33% |
| loss_aversion_framing | none | moderate | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals—reliable, scalable, efficient, monitoring capabilities, continuous integration—dominate the responsibilities with no velocity framing present.

**Run 2:** `rigour`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: The emphasis on reliability, best practices, and continuous integration reflects a rigour-oriented approach rather than velocity-focused delivery.

**Run 3:** `rigour`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality characteristics (reliable, scalable, efficient) and best practices rather than speed or delivery pace.

### domain_risk

**Run 1:** `moderate`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: The role serves business decision-making without explicit financial reporting, regulatory, or compliance language that would signal high-risk consequences.

**Run 2:** `moderate`
> Quote: "data solutions that drive business impact"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes business impact and stakeholder decision-making without explicit financial reporting, compliance, or regulatory language.

**Run 3:** `moderate`
> Quote: "data solutions that drive business impact"
> Verified: ✓ found in JD
> Reasoning: Business-critical decisions are affected but the JD contains no explicit financial reporting, compliance, regulatory, or audit language despite the SRT context.

### collaboration_width

**Run 1:** `1`
> Quote: "direct client contact to understand challenges and translate needs into data solutions"
> Verified: ✓ found in JD
> Reasoning: Clients are explicitly named as collaboration partners; no other named functions or teams are identified in the JD.

**Run 2:** `0`
> Quote: "business stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role mentions 'business stakeholders' and 'direct client contact,' but these do not meet the counting criteria: the former is generic language, the latter refers to external clients rather than named internal partner teams.

**Run 3:** `0`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: No named functions or teams are explicitly identified; business stakeholders is generic terminology.

⚠ **LLM inconsistency**: runs gave ['1', '0', '0']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Knowledge of modern data processing technologies: dbt, Spark, BigQuery, Snowflake, Databricks"
> Verified: ✓ found in JD
> Reasoning: Established tools appear in the requirements list, indicating infrastructure exists, and the design/optimization focus suggests a team growing beyond initial build-out.

**Run 2:** `mid`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: The emphasis on designing and optimizing data pipelines using modern technologies suggests infrastructure exists and is being actively refined.

**Run 3:** `mid`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: The existence of internal and external data sources and emphasis on productionization implies infrastructure already exists and is being extended.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Develop and optimise procedures to productionize models with monitoring capabilities"
> Verified: ✓ found in JD
> Reasoning: Some technical specificity (productionize, monitoring, continuous integration) appears alongside generic consulting language (co-create, strategic decision-making, stakeholder collaboration).

**Run 2:** `recruiter`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs and boilerplate language without technical specificity about scale, challenges, or how tools are applied.

**Run 3:** `recruiter`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic boilerplate verbs (co-create, design, develop, implement) without technical specificity about what the role delivers on a Tuesday morning.

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building data infrastructure and platforms themselves rather than serving commercial, product, or finance stakeholders directly.

**Run 2:** `commercial`
> Quote: "direct client contact to understand challenges and translate needs into data solutions that drive business impact"
> Verified: ✓ found in JD
> Reasoning: As a consulting-based role with direct client engagement, the candidate serves clients' business stakeholder needs broadly.

**Run 3:** `mixed`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: The first responsibility names business stakeholders for strategic decisions, but infrastructure responsibilities (pipelines, productionization, models) constitute half the role, creating mixed orientation between client service and internal data platform.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'commercial', 'mixed']

### autonomy_level

**Run 1:** `execution`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: While the role has technical autonomy in design decisions, the overall framing of co-creation with stakeholders suggests execution within business-defined priorities rather than strategic direction-setting.

**Run 2:** `mixed`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic design of data architectures with execution in service of client-defined priorities.

**Run 3:** `execution`
> Quote: "Co-create Data Products with business stakeholders for strategic decision-making"
> Verified: ✓ found in JD
> Reasoning: Co-creation with stakeholders implies executing direction set by others rather than independently defining strategy or setting priorities.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']

### ai_role

**Run 1:** `ai_enabler`
> Quote: "design the pipelines and architectures of data that form the foundation for AI solutions"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems will consume and operate on, plus demonstrate MLOps experience—making them an enabler of AI systems rather than a user of AI coding tools.

**Run 2:** `ai_enabler`
> Quote: "design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems consume, not to use AI tools for personal productivity.

**Run 3:** `ai_enabler`
> Quote: "design the pipelines and architectures of data that form the foundation for AI solutions, advanced dashboards, and interactive tools"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems depend on, and MLOps experience is explicitly required.

### testing_framing

**Run 1:** `tool_listed`
> Quote: "monitoring capabilities"
> Verified: ✓ found in JD
> Reasoning: Monitoring is mentioned as a practice to include in productionization but without explicit ownership verbs like 'own' or 'define' that would signal responsibility.

**Run 2:** `absent`
> Quote: "No testing or data quality signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: While monitoring and continuous integration are mentioned as best practices, there is no testing responsibility, data quality framework, or data contracts outlined.

**Run 3:** `absent`
> Quote: "Develop and optimise procedures to productionize models with monitoring capabilities"
> Verified: ✓ found in JD
> Reasoning: Operational monitoring is mentioned but there is no mention of data quality testing, data contracts, or observability frameworks as owned responsibilities.

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'absent', 'absent']

### loss_aversion_framing

**Run 1:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is framed entirely in delivery and capability terms with reliability as a design quality, not in terms of preventing bad outcomes, operational incidents, or risk mitigation.

**Run 2:** `moderate`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: Reliability is emphasized as a system quality, but there is no regulatory, compliance, or stakeholder-trust framing that would elevate this to high loss-aversion.

**Run 3:** `moderate`
> Quote: "Design reliable, scalable, efficient data pipelines from internal and external sources"
> Verified: ✓ found in JD
> Reasoning: Reliability is framed as an operational quality concern but there is no explicit compliance, regulatory, or risk-prevention language.

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'moderate']
