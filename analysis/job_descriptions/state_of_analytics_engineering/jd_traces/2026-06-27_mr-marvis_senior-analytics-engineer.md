# Trace: 2026-06-27_mr-marvis_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — MR MARVIS

**Location:** Amsterdam HQ Office
**Date Posted:** 2026-06-27

---

"Own the analytics layer at MR MARVIS. Build trusted data products that power smarter decisions, self-serve insights and future AI use cases"

### What You'll Do

**Design & Modeling**
- Build robust data pipelines translating complex business logic into scalable dbt models
- Optimize models for performance, cost efficiency, and long-term maintainability

**Stakeholder Collaboration**
- Work with business stakeholders to translate analytical needs into structured data solutions
- Drive alignment around consistent metric definitions and reporting standards

**Self-Serve Enablement**
- Enable governed self-serve analytics by simplifying access to trusted data sources
- Support business users in adopting best practices for data exploration
- Optimize our data platform - especially the analytics layer - for AI use cases

**Data Quality & Infrastructure**
- Implement testing, monitoring, and data quality checks
- Partner with data engineers on clean ingestion and upstream design
- Optimize warehouse usage through partitioning, clustering, and incremental modeling

### Requirements

**Essential:**
- Significant Analytics Engineering or BI Engineering experience
- Strong SQL and production dbt experience
- Strong data modelling understanding (facts, dimensions, grain, reuse, testing)
- BI tool experience (Looker Studio, Tableau, Omni, Power BI or similar)
- Strong stakeholder communication skills
- Curious about using AI tools to improve coding, documentation, testing and workflow efficiency
- End-to-end cross-functional ownership capability

**Nice-to-Haves:**
- Warehouse optimization exposure
- Semantic layer or metric governance experience
- Omni experience
- Python or R experience
- Retail, ecommerce, DTC, marketplace, or consumer brand background

### Benefits

25 vacation days, 5-year sabbatical option, hybrid Amsterdam office (~3 days/week), monthly wellness budget, free coaching/psychology access, meditation app, personal development, team events, international team, mobility allowance, pension scheme, 20% employee discount, equipment provision, free office lunch, B-Corp status.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 1 | 1 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | mixed | hiring_manager | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | strategic | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Implement testing, monitoring, and data quality checks"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit quality, testing, and governance signals dominate the responsibilities section with no velocity language present.

**Run 2:** `rigour`
> Quote: "Implement testing, monitoring, and data quality checks"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes quality, testing, governance, and data accuracy throughout, with no velocity language present.

**Run 3:** `rigour`
> Quote: "Implement testing, monitoring, and data quality checks"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, monitoring, data quality, and robust/maintainable design with no counterbalancing velocity language.

### domain_risk

**Run 1:** `moderate`
> Quote: "Build trusted data products that power smarter decisions, self-serve insights and future AI use cases"
> Verified: ✓ found in JD
> Reasoning: This is business intelligence and operational reporting (moderate risk) with no explicit financial reporting, compliance, or regulatory language.

**Run 2:** `moderate`
> Quote: "Build trusted data products that power smarter decisions"
> Verified: ✓ found in JD
> Reasoning: The JD frames data as supporting business decisions without explicit financial, regulatory, or compliance language.

**Run 3:** `moderate`
> Quote: "Retail, ecommerce, DTC, marketplace, or consumer brand background"
> Verified: ✓ found in JD
> Reasoning: The domain is retail/ecommerce focused, affecting business decisions but lacking explicit financial reporting, compliance, or regulatory language.

### collaboration_width

**Run 1:** `1`
> Quote: "Partner with data engineers on clean ingestion and upstream design"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named team function (data engineers) appears; generic references like 'business stakeholders' and 'business users' do not count.

**Run 2:** `1`
> Quote: "data engineers"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named partner team (data engineers) appears in the JD; other references use generic terms like stakeholders.

**Run 3:** `1`
> Quote: "Partner with data engineers on clean ingestion and upstream design"
> Verified: ✓ found in JD
> Reasoning: Data engineers is the only explicitly named team or function; 'business stakeholders' and 'business users' are too generic to count.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Optimize our data platform - especially the analytics layer - for AI use cases"
> Verified: ✓ found in JD
> Reasoning: References to optimizing existing infrastructure, named tools in responsibilities (dbt, BI platforms), and clear role delineation with data engineers indicate a functioning team growing from an existing base rather than building from zero or operating at scale.

**Run 2:** `mid`
> Quote: "Optimize our data platform - especially the analytics layer - for AI use cases"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure (platform, warehouse, BI tools) being optimized, indicating a data function that exists and is growing.

**Run 3:** `mid`
> Quote: "Partner with data engineers on clean ingestion and upstream design"
> Verified: ✓ found in JD
> Reasoning: The existence of a data engineering team and references to 'our data platform' and optimize suggest an established function in growth phase rather than early build or mature scale.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Optimize warehouse usage through partitioning, clustering, and incremental modeling"
> Verified: ✓ found in JD
> Reasoning: Technical specificity (partitioning, clustering, incremental modeling, facts/dimensions/grain) is mixed with generic collaboration boilerplate (stakeholder alignment, user support).

**Run 2:** `mixed`
> Quote: "Optimize warehouse usage through partitioning, clustering, and incremental modeling"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical methodology details alongside generic stakeholder collaboration language.

**Run 3:** `hiring_manager`
> Quote: "Optimize warehouse usage through partitioning, clustering, and incremental modeling"
> Verified: ✓ found in JD
> Reasoning: The JD contains technical specificity (warehouse optimization techniques, specific dbt modeling approaches, data modeling concepts) that reflects hands-on experience.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Enable governed self-serve analytics by simplifying access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: The primary framing emphasizes building platform infrastructure and data consumer enablement, not serving external GTM, product teams, or finance functions.

**Run 2:** `internal_data`
> Quote: "Enable governed self-serve analytics by simplifying access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: The primary audience is internal data consumers and the data platform function itself, not commercial, product, or finance teams.

**Run 3:** `internal_data`
> Quote: "Enable governed self-serve analytics by simplifying access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building and optimizing the analytics platform for internal data consumers rather than serving commercial, product, or finance stakeholders.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Own the analytics layer at MR MARVIS"
> Verified: ✓ found in JD
> Reasoning: Strategic ownership of the analytics domain is combined with execution responsibilities supporting business stakeholders and partnering with data engineers.

**Run 2:** `strategic`
> Quote: "Drive alignment around consistent metric definitions and reporting standards"
> Verified: ✓ found in JD
> Reasoning: The role is framed as owning and defining the analytics layer, with direction-setting responsibilities rather than execution against externally set priorities.

**Run 3:** `mixed`
> Quote: "Own the analytics layer at MR MARVIS"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership of the analytics platform but responsibilities are framed around executing business requirements and supporting platform users.

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'mixed']
