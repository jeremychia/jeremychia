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
| collaboration_width | 9 | 9 | 10 | 10 | 33% | ✗ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | none | ai_enabler | none | 33% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | high | high | moderate | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality frameworks, reliability engineering, compliance, and observability throughout with no velocity language like 'fast-paced', 'ship quickly', or 'iteration speed'.

**Run 2:** `rigour` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section is dominated by quality, reliability, governance, and compliance signals (data quality frameworks, SLAs/SLOs, compliance, observability) with no velocity-oriented language.

**Run 3:** `rigour` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section is dominated by quality, compliance, reliability, and governance language (SLAs/SLOs, data quality frameworks, data reliability engineering, compliance) with minimal velocity framing.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "ensuring clear accountability for delivery outcomes (timeliness, quality, completeness, compliance)"
> Verified: ✓ found in JD
> Reasoning: Fintech domain combined with explicit compliance accountability and regulatory reporting signals high financial/regulatory risk.

**Run 2:** `high` ✓
> Quote: "ensure that the data engineers deliver trusted, timely, and high-quality data to enable business and analytical outcomes"
> Verified: ⚠ NOT found verbatim
> Reasoning: FinTech sector with explicit regulatory reporting requirement and fintech-specific domains (payments, invoicing, collections) create high financial and regulatory risk.

**Run 3:** `high` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: Fintech sector combined with explicit regulatory reporting and compliance accountability means data errors have direct regulatory and financial consequences.

### collaboration_width
**Manual:** `9`

**Run 1:** `9` ✓
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ✓ found in JD
> Reasoning: The JD names nine distinct partner functions explicitly across responsibilities and collaboration sections (combining 'tech teams' and 'Platform Engineering' as overlapping engineering functions).

**Run 2:** `10` ✗
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ✓ found in JD
> Reasoning: Ten distinct named teams/functions explicitly appear across the collaboration and stakeholder management sections.

**Run 3:** `10` ✗
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ✓ found in JD
> Reasoning: Ten distinct named teams/functions explicitly listed across responsibilities section.

⚠ **Disagreement**: manual=`9` vs LLM majority=`10`

⚠ **LLM inconsistency**: runs gave ['9', '10', '10']

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "build and scale a high-performing team of data engineers working across multiple agile data product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Existing infrastructure and tools (dbt, Airflow, Spark, Databricks, Azure) are named in requirements, multiple data teams already operate, and the role is about scaling and improving rather than building from zero.

**Run 2:** `mid` ✗
> Quote: "build and scale a high-performing data engineering team focused on transforming raw data into trusted, accessible, and reusable assets"
> Verified: ✓ found in JD
> Reasoning: Organization has multiple established agile data product teams, governance, and platform functions in place, but is in active growth and process-improvement phase rather than mature steady-state.

**Run 3:** `mid` ✗
> Quote: "This leader will build and scale a high-performing data engineering team focused on transforming raw data into trusted, accessible, and reusable assets"
> Verified: ✓ found in JD
> Reasoning: Language of 'build and scale' combined with existing infrastructure (shared core data platform, multiple agile data product teams, established tools) indicates a data function that exists but is growing.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting. Drive excellence in data modeling and pipeline design, ensuring solutions are efficient, maintainable, and well-documented."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains specific technical concepts (ETL/ELT, Medallion architecture, data SLAs/SLOs, data-as-a-product) and named tools with precise application context that only come from someone who has done this work.

**Run 2:** `hiring_manager` ✓
> Quote: "Implement data quality frameworks and automation across pipelines owned by agile teams; Define and monitor data SLAs and SLOs; Promote proactive data reliability engineering"
> Verified: ✓ found in JD
> Reasoning: Specific operational frameworks (SLAs/SLOs, CI/CD for data, Medallion architecture, dbt/Airflow), organizational models (agile data product teams), and technical methodologies indicate hands-on hiring manager input.

**Run 3:** `hiring_manager` ✓
> Quote: "Establish and continuously improve the operating model for data engineers within agile data product teams, ensuring clear accountability for delivery outcomes (timeliness, quality, completeness, compliance)."
> Verified: ✓ found in JD
> Reasoning: Technical specificity about the agile data product team operating model and granular accountability criteria (timeliness, quality, completeness, compliance) shows this was written by someone who has done this work.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Contribute to the evolution of our data-as-a-product approach, ensuring data products are discoverable, well-documented, and reusable."
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining the data infrastructure and function itself as a product, serving internal data consumers (analysts, data scientists, product teams) rather than commercial or finance stakeholders.

**Run 2:** `internal_data` ✓
> Quote: "transforming raw data into trusted, accessible, and reusable assets — ensuring that the broader organization can make faster and smarter decisions"
> Verified: ✓ found in JD
> Reasoning: Primary responsibility is building and scaling the data engineering function and infrastructure that BI, analytics, and data science teams consume internally.

**Run 3:** `internal_data` ✓
> Quote: "This leader will build and scale a high-performing data engineering team focused on transforming raw data into trusted, accessible, and reusable assets — ensuring that the broader organization can make faster and smarter decisions."
> Verified: ✓ found in JD
> Reasoning: The primary audience is the analytics, BI, and data science functions that consume data products; the role builds infrastructure for data professionals rather than serving commercial, product, or finance teams directly.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy."
> Verified: ✓ found in JD
> Reasoning: The role is framed around defining vision, establishing practices, championing adoption, and driving strategic decisions across the data engineering function, not executing scoped work set by others.

**Run 2:** `strategic` ✓
> Quote: "Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy."
> Verified: ✓ found in JD
> Reasoning: The role is framed around defining direction, establishing operating models, driving practices, and leading the data engineering discipline, not executing direction set by others.

**Run 3:** `strategic` ✓
> Quote: "Define and execute the data engineering vision and roadmap aligned with the overall Data, AI & Analytics strategy."
> Verified: ✓ found in JD
> Reasoning: The leader is expected to define vision, roadmap, operating model, standards, and practices—clear strategic ownership of direction rather than execution of direction set by others.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD mentions AI as something the role supports (AI pipelines as a consumer) but does not require the candidate to demonstrate AI coding skills or AI-specific technical expertise.

**Run 2:** `ai_enabler` ✗
> Quote: "meet the needs of analytics, AI, and regulatory reporting"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure and pipelines that support AI systems and analytics, not to use AI tools for personal coding productivity.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: While the company uses AI and mentions 'AI-based productivity increases,' there is no explicit requirement that the candidate demonstrate AI tool usage or AI skill.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['none', 'ai_enabler', 'none']

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Implement data quality frameworks and automation across pipelines owned by agile teams."
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are explicitly owned responsibilities with action verbs ('Implement', 'Define', 'Promote'), not just listed as tool requirements.

**Run 2:** `responsibility` ✗
> Quote: "Implement data quality frameworks and automation across pipelines owned by agile teams."
> Verified: ✓ found in JD
> Reasoning: Data quality and testing are framed as owned responsibilities with action verbs (Implement, Define, Monitor, Promote), not as tools to learn from a requirements list.

**Run 3:** `responsibility` ✗
> Quote: "Implement data quality frameworks and automation across pipelines owned by agile teams."
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are framed as owned responsibilities with action verbs (implement, define, promote) rather than listed as tools or skills in a requirements section.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `high` ✗
> Quote: "transforming raw data into trusted, accessible, and reusable assets — ensuring that the broader organization can make faster and smarter decisions."
> Verified: ✓ found in JD
> Reasoning: Compliance, regulatory reporting, and 'trusted' data are framed as core mission in a fintech domain, with emphasis on preventing bad data from reaching stakeholders, signaling high loss aversion beyond operational reliability.

**Run 2:** `high` ✗
> Quote: "ensure that the data engineers deliver trusted, timely, and high-quality data to enable business and analytical outcomes"
> Verified: ⚠ NOT found verbatim
> Reasoning: FinTech sector with regulatory reporting requirement, repeated quality/reliability emphasis, and 'trusted data' as central to the role framing reflect high concern with preventing bad data and compliance failures.

**Run 3:** `moderate` ✗
> Quote: "ensuring clear accountability for delivery outcomes (timeliness, quality, completeness, compliance)"
> Verified: ✓ found in JD
> Reasoning: Regulatory reporting requirement in fintech creates genuine reliability and compliance concerns, but the JD frames these operationally (SLAs, frameworks, standards) rather than as risk mitigation or fear of regulatory exposure.

⚠ **Disagreement**: manual=`` vs LLM majority=`high`

⚠ **LLM inconsistency**: runs gave ['high', 'high', 'moderate']
