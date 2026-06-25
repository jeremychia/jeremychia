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
| collaboration_width | 9 | 10 | 10 | 9 | 33% | ✗ |
| data_team_maturity | mature | mid | mature | mid | 33% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implement data quality frameworks and automation across pipelines owned by agile teams."
> Verified: ✓ found in JD
> Reasoning: The responsibilities repeatedly emphasize data quality, SLAs/SLOs, reliability engineering, compliance, and governance rather than speed or shipping velocity.

**Run 2:** `rigour` ✓
> Quote: "Implement data quality frameworks and automation across pipelines owned by agile teams. Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes data quality, reliability, standards, and SLAs/SLOs throughout with no velocity language, clearly prioritizing rigour.

**Run 3:** `rigour` ✓
> Quote: "ensuring that the data engineers deliver trusted, timely, and high-quality data to enable business and analytical outcomes"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality frameworks, SLAs/SLOs, data reliability engineering, CI/CD, and observability as core responsibilities, with no competing velocity language like 'move fast' or 'rapid delivery'.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: Explicit regulatory reporting requirement in a fintech organization operating in payments, invoicing, and collections indicates high financial and compliance risk.

**Run 2:** `high` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly mentions regulatory reporting, and Riverty operates in fintech payments/collections, making data errors high-consequence.

**Run 3:** `high` ✓
> Quote: "Ensure that agile data product teams deliver fit-for-purpose data models that meet the needs of analytics, AI, and regulatory reporting."
> Verified: ✓ found in JD
> Reasoning: Explicit mention of regulatory reporting in a fintech context (payments, dunning, invoicing, collections) directly signals high regulatory and compliance risk.

### collaboration_width
**Manual:** `9`

**Run 1:** `10` ✗
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: Ten distinct named partner functions are explicitly listed across the responsibilities section.

**Run 2:** `10` ✗
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: Ten distinct named teams/functions are explicitly listed throughout the JD in collaboration and responsibility sections.

**Run 3:** `9` ✓
> Quote: "product owners; BI; data analysis; data science; data platform; tech teams; Platform Engineering teams; Business IT teams; Data Governance; Data Architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: Nine distinct named partner teams/functions are explicitly mentioned across Strategic Leadership and Collaboration sections, including product, analytics, data science, engineering, governance, and architecture functions.

⚠ **Disagreement**: manual=`9` vs LLM majority=`10`

⚠ **LLM inconsistency**: runs gave ['10', '10', '9']

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platform."
> Verified: ✓ found in JD
> Reasoning: The reference to an existing shared core data platform, multiple agile data product teams, and operational pipelines indicates established infrastructure being improved rather than built from zero.

**Run 2:** `mature` ✓
> Quote: "Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platform."
> Verified: ✓ found in JD
> Reasoning: The JD references established specialized teams, a shared core platform infrastructure, and mature methodologies (agile data product model), indicating a mature data organization.

**Run 3:** `mid` ✗
> Quote: "Partner with Platform Engineering teams to ensure smooth operation of data pipelines within the shared core data platform."
> Verified: ✓ found in JD
> Reasoning: The reference to an existing shared core data platform and established governance structures (SLAs, SLOs, metadata/lineage) indicates a developed function, while the team size >10 and lack of multiple specialized sub-teams suggests mid-stage rather than mature scale.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'mature', 'mid']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Promote proactive data reliability engineering, enabling teams to detect and resolve issues early."
> Verified: ✓ found in JD
> Reasoning: The specific use of 'data reliability engineering' as a discipline demonstrates technical knowledge only someone actively practicing this role would include.

**Run 2:** `hiring_manager` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The responsibilities include specific technical metrics (SLAs, SLOs, CI/CD for data) and practices applied in context, showing hands-on data engineering experience rather than generic recruiter language.

**Run 3:** `hiring_manager` ✓
> Quote: "Define and monitor data SLAs and SLOs, ensuring that product teams deliver data that meets business needs in terms of timeliness, accuracy, and availability."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain technical specificity (SLAs/SLOs, data reliability engineering, CI/CD for data, observability, metadata/lineage) that only someone doing this job would write; generic boilerplate phrases are minimal and scattered rather than dominant.
