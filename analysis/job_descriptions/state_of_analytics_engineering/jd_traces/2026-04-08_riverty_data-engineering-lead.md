# Trace: 2026-04-08_riverty_data-engineering-lead

## JD text (fed to classifier, Layer B stripped)

```
# Data Engineering Lead (m/w/d) — Riverty

**URL:** https://jobsearch.createyourowncareer.com/Riverty/job/Berlin-Data-Engineering-Lead-%28mwd%29-BE-10623/284720-de_DE/
**Location:** Berlin, Verl, Baden-Baden or Oslo (hybrid)
**Employment Type:** Full-time, unlimited
**Job ID:** 284720

---

## About Riverty

Riverty is a FinTech company and part of the Bertelsmann Group. Mission: "Mit Empathie, moderner Technologie und datengestützten Erkenntnissen dafür zu sorgen, dass Menschen und Unternehmen im Fluss bleiben." (Using empathy, modern technology, and data-driven insights to keep people and businesses flowing.) Over 4,000 people from almost 80 nations in 11 countries, across 30 hybrid work environments. Operates in payments, dunning, invoicing, and collections.

---

## The Role

The Data Engineering Lead leads the design, development, and delivery of high-quality data pipelines and data products that power analytics, BI, and AI across the fintech ecosystem in payments, dunning, invoicing, and collections. This leader will build and scale a high-performing data engineering team focused on transforming raw data into trusted, accessible, and reusable assets — ensuring that the broader organization can make faster and smarter decisions.

Working in an agile, cross-functional data product model, this role is accountable for the results and contributions of the data engineering discipline — ensuring that the data engineers deliver trusted, timely, and high-quality data to enable business and analytical outcomes.

---

## Key Responsibilities

### Strategic Leadership
- Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy.
- Establish and continuously improve the operating model for data engineers within agile data product teams, ensuring clear accountability for delivery outcomes (timeliness, quality, completeness, compliance).
- Champion the adoption of modern data engineering and agile delivery practices, fostering close collaboration with product owners, BI, data analysis, data science, data platform, and tech teams.

### Data Pipelines & Modeling
- Oversee the development of robust ETL/ELT pipelines to ingest and transform data from multiple internal and external sources.
- Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting.
- Drive excellence in data modeling and pipeline design, ensuring solutions are efficient, maintainable, and well-documented.

### Data Quality & Reliability
- Implement data quality frameworks and automation across pipelines owned by agile teams.
- Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability.
- Promote proactive data reliability engineering, enabling teams to detect and resolve issues early.

### Collaboration & Stakeholder Management
- Collaborate closely with Data Product Owners to prioritize and deliver data engineering work in alignment with business priorities.
- Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platform.
- Collaborate with the Business IT teams to create reliable and robust interfaces to the source systems.
- Work hand-in-hand with Data Governance and Data Architecture to ensure alignment on metadata, lineage, and data ownership.

### Team Leadership & Development
- Lead, mentor, and grow a high-performing team of data engineers working across multiple agile data product teams.
- Ensure consistent technical standards, delivery practices, and performance management across the discipline, even within decentralized team setups.
- Cultivate a culture of ownership, accountability, and collaboration within and across agile data product teams.

### Process & Operational Excellence
- Promote automation, CI/CD for data, and observability across all data engineering workstreams…[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 9 | 9 | 10 | 9 | 33% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | strategic | strategic | strategic | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Promote proactive data reliability engineering, enabling teams to detect and resolve issues early."
> Verified: ✓ found in JD
> Reasoning: The role emphasizes data quality frameworks, SLAs/SLOs, reliability engineering, and documentation as core responsibilities, establishing rigour as the primary work orientation.

**Run 2:** `rigour` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality frameworks, reliability engineering, SLAs/SLOs, observability, and accuracy as core expectations, with no velocity signals like 'fast-paced' or 'rapid delivery.'

**Run 3:** `rigour` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The role emphasizes data quality frameworks, SLAs/SLOs, reliability engineering, and robustness throughout, with no mention of speed or velocity.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: Fintech company with explicit mention of regulatory reporting as a data model requirement indicates financial/regulatory compliance risk inherent to the role.

**Run 2:** `high` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: Riverty is a fintech company operating in payments and collections, and the explicit requirement to support regulatory reporting means data errors would directly expose the organization to compliance and financial reporting risk.

**Run 3:** `high` ✓
> Quote: "regulatory reporting"
> Verified: ✓ found in JD
> Reasoning: Fintech company operating in payments, invoicing, and collections with explicit mention of regulatory reporting requirements signals high-risk financial services domain.

### collaboration_width
**Manual:** `9`

**Run 1:** `9` ✓
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role explicitly lists partnerships with nine distinct named teams across product, analytics, data science, engineering, operations, and data governance functions, indicating very wide cross-functional collaboration requirements.

**Run 2:** `10` ✗
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names ten distinct functions/teams as collaboration partners: product owners, BI, data analysis, data science, data platform, tech teams, Platform Engineering, Business IT, Data Governance, and Data Architecture.

**Run 3:** `9` ✓
> Quote: "product owners; BI; data analysis; data science; data platform; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: Nine distinct named functions explicitly listed as collaboration partners across the responsibilities section.

⚠ **LLM inconsistency**: runs gave ['9', '10', '9']

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platform."
> Verified: ✓ found in JD
> Reasoning: The role presupposes a shared core data platform and existing data pipelines with multiple specialized teams, indicating an established data function scaling or improving its operations rather than building from zero.

**Run 2:** `mid` ✗
> Quote: "build and scale a high-performing data engineering team focused on transforming raw data into trusted, accessible, and reusable assets"
> Verified: ✓ found in JD
> Reasoning: The use of 'scale' combined with multiple named agile data product teams and established governance/architecture functions suggests an existing data function growing significantly, rather than a greenfield build.

**Run 3:** `mid` ✗
> Quote: "Establish and continuously improve the operating model for data engineers within agile data product teams, ensuring clear accountability for delivery outcomes (timeliness, quality, completeness, compliance)."
> Verified: ✓ found in JD
> Reasoning: The JD references existing named tools (dbt, Airflow, Spark), multiple data sub-teams, and team size >10, but uses language about establishing and improving the operating model rather than maintaining a fully mature system.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Define and continuously improve the operating model for data engineers within agile data product teams, ensuring clear accountability for delivery outcomes (timeliness, quality, completeness, compliance)."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines specific technical concepts (agile data product teams, quality and compliance metrics, data product thinking) with generic leadership language (define, improve, accountability), indicating mixed hiring manager and recruiter authorship.

**Run 2:** `hiring_manager` ✓
> Quote: "Promote automation, CI/CD for data, and observability across all data engineering workstreams"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical practices (CI/CD for data, observability, SLAs/SLOs, data quality frameworks, Medallion architecture) that demonstrate hands-on data engineering experience, not generic recruiter language.

**Run 3:** `hiring_manager` ✓
> Quote: "Promote automation, CI/CD for data, and observability across all data engineering workstreams, including AI-based productivity increases."
> Verified: ✓ found in JD
> Reasoning: The phrase 'CI/CD for data' demonstrates specific technical knowledge of modern data engineering practices that only a hiring manager familiar with the role would articulate.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: The role's primary responsibilities focus on building data infrastructure and models consumed by analytics, BI, and data science teams (internal_data audiences), with regulatory reporting as a secondary technical requirement.

**Run 2:** `internal_data` ✗
> Quote: "transforming raw data into trusted, accessible, and reusable assets"
> Verified: ✓ found in JD
> Reasoning: The role's core mission is building data pipelines, frameworks, and products that serve internal data consumers—analysts, data scientists, platform teams—with emphasis on data-as-a-product and self-serve infrastructure.

**Run 3:** `internal_data` ✗
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: The primary audience is internal data consumers (analytics, BI, AI/data science teams) receiving data models and infrastructure, though regulatory reporting adds a compliance dimension.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy."
> Verified: ✓ found in JD
> Reasoning: The role's foundational responsibility is to define the vision and roadmap for the data engineering function, indicating strategic ownership of the technical direction and organizational shape.

**Run 2:** `strategic` ✗
> Quote: "Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy."
> Verified: ✓ found in JD
> Reasoning: The role is framed around setting direction, establishing operating models, championing practices, and shaping the data engineering discipline—not executing scope defined by others.

**Run 3:** `strategic` ✗
> Quote: "Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy."
> Verified: ✓ found in JD
> Reasoning: The role is framed around setting direction for the data engineering discipline, establishing operating models, and championing practices rather than executing defined work.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`

### ai_role
**Run 1:** `none`
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Reasoning: AI mentioned as a consumer of data models, not as infrastructure being built or AI tools used by the candidate.

### testing_framing
**Run 1:** `responsibility`
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Reasoning: Clear ownership verbs (define, monitor, ensure) paired with quality practices and establishing operating standards.

### loss_aversion_framing
**Run 1:** `moderate`
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Reasoning: Emphasis on operational reliability metrics (SLAs/SLOs) and proactive issue detection rather than regulatory compliance or trust dominance.
