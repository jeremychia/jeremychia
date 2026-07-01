# Trace: 2026-06-27_decathlon-digital_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Decathlon Digital FR

**Location:** Lille (Btwin Village), Nord, France; Paris, France
**Date Posted:** 2026-06-27

---

## Key Responsibilities

The role focuses on four main areas:

1. **Data Industrialization & Modeling:** Automatiser et industrialiser les pipelines de transformation de données (automating data transformation pipelines for dashboards, AI models, and analyses), including building the semantic layer for the sports domain.

2. **Strategy & Quality:** Defining technical stack strategies and ensuring la qualité, la fiabilité et la pertinence des données exposées (quality, reliability, and relevance of exposed data).

3. **Maintenance & Evolution:** Updating datasets and pipelines to support expanding use cases.

4. **Community Building:** Contributing to the internal analytics and data engineering community.

---

## Required Qualifications

- Approximately 3+ years in Analytics Engineering, Data Engineering, or comprehensive Data Analysis with data engineering experience
- Proven expertise in major cloud platforms (AWS, GCP, or Azure)
- dbt implementation and SQL et Python proficiency
- Development tools knowledge: Git, Github, CI/CD, VSCode
- Collaborative mindset suited for agile environments (Scrum/Kanban)
- Fluent English for daily communication across 60 countries

**Preferred additions:** Sports passion, Spark, Airflow, Tableau, or Modern Data Stack technologies (Polars, DuckDB)

---

## Technical Stack

- **Data Platform:** AWS, Databricks, S3
- **Code & Orchestration:** SQL, Python, Airflow
- **Modeling & Quality:** dbt, great_expectations
- **Software Delivery:** Git, GitHub, CI/CD practices

---

## Offered Benefits

- Hybrid work arrangement
- Equipment (Mac or Windows) aligned with role and sustainability commitments
- International career opportunities within global network
- Skills development and training (diverse projects, internal/external programs)
- Compensation package including employee stock options and performance bonuses

---

## Company Context

Decathlon Digital comprises 5,000+ technology experts across Paris, Lille, and Amsterdam, creating la plus vaste plateforme sportive numérique (the largest digital sports platform) through software engineering, product management, data, cloud, and cybersecurity innovation.

---

## Diversity Commitment

Decathlon emphasizes inclusion as a core value and explicitly welcomes applicants from all backgrounds, offering accessible recruitment processes and confidential accommodation requests.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 0 | 0 | 2 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | mixed | mixed | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Verified: ✓ found in JD
> Reasoning: Responsibilities explicitly emphasize quality, reliability, and relevance as core expectations with structured engineering practices (dbt, great_expectations, CI/CD), with no velocity-oriented language present.

**Run 2:** `rigour`
> Quote: "ensuring quality, reliability, and relevance of exposed data"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes data quality, reliability, and relevance as core expectations with no corresponding velocity signals like 'fast-paced' or 'rapid delivery.'

**Run 3:** `rigour`
> Quote: "Defining technical stack strategies and ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality, reliability, and relevance of exposed data with explicit strategy focus and deployment of great_expectations (quality testing), with no mention of speed, velocity, or pace-oriented delivery.

### domain_risk

**Run 1:** `moderate`
> Quote: "automating data transformation pipelines for dashboards, AI models, and analyses"
> Verified: ✓ found in JD
> Reasoning: Data serves business intelligence and decision-making across a major digital platform, but without explicit financial reporting, regulatory, audit, or compliance language indicating high-risk consequences.

**Run 2:** `moderate`
> Quote: "creating la plus vaste plateforme sportive numérique (the largest digital sports platform)"
> Verified: ✓ found in JD
> Reasoning: This is an e-commerce/sports platform where data errors affect business decisions and analytics, but the JD contains no financial reporting, regulatory, or compliance language that would elevate risk to high.

**Run 3:** `moderate`
> Quote: "ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Verified: ✓ found in JD
> Reasoning: While data quality is emphasized, the role is in sports/e-commerce without explicit financial reporting, compliance, or regulatory language, placing it in moderate risk where data errors affect business operations but not regulatory/financial consequences.

### collaboration_width

**Run 1:** `0`
> Quote: "Contributing to the internal analytics and data engineering community"
> Verified: ✓ found in JD
> Reasoning: While the JD mentions analytics and data engineering communities, these appear to be the role holder's own peer groups rather than distinct external collaboration partners.

**Run 2:** `0`
> Quote: "n/a"
> Verified: ⚠ NOT found verbatim
> Reasoning: The only collaboration mention is 'contributing to the internal analytics and data engineering community,' which describes the role holder's own data domain rather than named external partner teams.

**Run 3:** `2`
> Quote: "internal analytics and data engineering community"
> Verified: ✓ found in JD
> Reasoning: The role explicitly lists two distinct named professional functions—Analytics and Data Engineering—as communities the person collaborates with.

⚠ **LLM inconsistency**: runs gave ['0', '0', '2']

### data_team_maturity

**Run 1:** `mid`
> Quote: "building the semantic layer for the sports domain"
> Verified: ✓ found in JD
> Reasoning: Named tools deployed in responsibilities (Airflow, dbt, great_expectations) and specific domain-focused building work indicate established mid-stage infrastructure, not early-stage greenfield or mature platform governance at scale.

**Run 2:** `mid`
> Quote: "Updating datasets and pipelines to support expanding use cases"
> Verified: ✓ found in JD
> Reasoning: The JD signals growth and evolution of existing infrastructure with established tooling (dbt, Airflow, Databricks), not building from scratch or maintaining a mature stable platform.

**Run 3:** `mid`
> Quote: "Updating datasets and pipelines to support expanding use cases"
> Verified: ✓ found in JD
> Reasoning: References to maintaining existing datasets and pipelines alongside sophisticated deployed tooling (dbt, Airflow, great_expectations) indicate an established data function in scaling phase rather than early-stage or fully mature.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "building the semantic layer for the sports domain"
> Verified: ✓ found in JD
> Reasoning: Domain-specific technical context (semantic layer for sports, specific platform context) demonstrates knowledge that only comes from understanding the actual technical work, not generic boilerplate.

**Run 2:** `mixed`
> Quote: "Contributing to the internal analytics and data engineering community"
> Verified: ✓ found in JD
> Reasoning: The JD mixes technical specificity (semantic layer for sports domain, transformation pipelines for dashboards/AI models) with generic boilerplate responsibilities that could apply to any analytics role.

**Run 3:** `mixed`
> Quote: "Automatiser et industrialiser les pipelines de transformation de données (automating data transformation pipelines for dashboards, AI models, and analyses), including building the semantic layer for the sports domain"
> Verified: ✓ found in JD
> Reasoning: Contains domain-specific technical concepts (semantic layer, sports domain, specific use cases) indicating technical expertise, but overall responsibilities use somewhat generic action verbs and lack precise tool-specific application details.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Contributing to the internal analytics and data engineering community"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize building and maintaining data infrastructure (semantic layer, pipelines, quality) and serving internal analytics/data engineering consumers, not external commercial, product, or finance stakeholders.

**Run 2:** `internal_data`
> Quote: "Defining technical stack strategies and ensuring quality, reliability, and relevance of exposed data"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's core mission is building and maintaining data infrastructure and a semantic layer for internal data consumers rather than serving commercial, product, or finance stakeholders.

**Run 3:** `internal_data`
> Quote: "ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building data infrastructure, quality assurance, and platform capabilities that serve other analysts and data consumers within the data function, with no commercial, product, or finance audience emphasis.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Defining technical stack strategies and ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Verified: ✓ found in JD
> Reasoning: The role sets technical direction through strategy definition and quality ownership, but also executes in response to business priorities (updating pipelines to support expanding use cases defined by others).

**Run 2:** `mixed`
> Quote: "Defining technical stack strategies"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of technical decisions with execution-oriented responsibilities like maintaining pipelines and supporting expanding use cases.

**Run 3:** `mixed`
> Quote: "Defining technical stack strategies"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic authority (defining technical strategies) with execution responsibilities (automating, maintaining, and updating systems), making it genuinely mixed between direction-setting and delivery.

### ai_role
**Run 1:** `ai_enabler` ✓
> Quote: "building the semantic layer for the sports domain"
> Reasoning: Semantic layers are infrastructure that AI models and LLM applications consume for analytics and text-to-SQL use cases.

**Run 2:** `ai_enabler` ✓
> Quote: "building the semantic layer for the sports domain"
> Reasoning: Candidate builds semantic infrastructure that AI models and analytics consume, positioning the role as AI enabler.

**Run 3:** `ai_enabler` ✓
> Quote: "dashboards, AI models, and analyses; building the semantic layer for the sports domain"
> Reasoning: Candidate builds data infrastructure (semantic layer) that AI models consume, not using AI coding tools.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Defining technical stack strategies and ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Reasoning: Ownership verbs 'defining' and 'ensuring' paired with explicit quality and reliability responsibility.

**Run 2:** `responsibility` ✓
> Quote: "Defining technical stack strategies and ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Reasoning: Uses 'ensuring' (ownership verb) paired with quality/reliability, indicating responsibility for data quality practices.

**Run 3:** `responsibility` ✓
> Quote: "Defining technical stack strategies and ensuring la qualité, la fiabilité et la pertinence des données exposées"
> Reasoning: Candidate owns quality and reliability as core responsibility with explicit 'ensuring' language.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "la qualité, la fiabilité et la pertinence des données exposées"
> Reasoning: Emphasis on data reliability and quality as operational concern; no compliance or regulatory framing present.

**Run 2:** `moderate` ✓
> Quote: "la qualité, la fiabilité et la pertinence des données exposées; no financial/compliance/regulatory language present"
> Reasoning: Emphasis on operational reliability and data quality without regulatory framing indicates moderate loss-aversion grounded in pipeline stability.

**Run 3:** `moderate` ✓
> Quote: "la qualité, la fiabilité et la pertinence des données exposées; no financial/compliance/regulatory language present"
> Reasoning: Operational reliability framing (quality, reliability) without compliance/trust dominance, confirming moderate loss aversion.

