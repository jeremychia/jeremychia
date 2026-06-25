# Trace: 2026-06-22_sumup_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer - Run & Grow — SumUp

**URL:** https://www.sumup.com/careers/positions/berlin-germany/data-analytics/senior-analytics-engineer-run-grow/8529484002/?gh_jid=8529484002&gh_src=1e0ad71d2
**Location:** Berlin, Germany

---

## Key Responsibilities

- Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions, and keeping domain outputs consistent, tested, and discoverable
- Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring, building well-documented, quality-assured data products
- Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations
- Implement technical improvements including incremental processing strategies, performance optimisations, and scalable data architecture
- Contribute to SumUp's broader data domain strategy, helping establish durable ownership, consistent definitions, and a shared catalogue of data products

---

## Required Qualifications

- Strong, proven experience in analytics engineering or data engineering, with a track record of building and maintaining production data systems
- Expert-level SQL skills for complex transformations and query optimisation, with hands-on experience building layered data models in a modern data warehouse or lakehouse
- Ability to think in terms of business domains, not just tables, translating complex business logic into clean, durable, and reusable data models
- Comfort working across squads with Product Managers, Engineers, Analysts, and Data Scientists
- Deep care for data quality, trust, and discoverability, building models others can rely on
- Proficiency with dbt including testing, documentation, and modelling conventions
- Experience with platforms like Snowflake, Iceberg

---

## Preferred / Bonus Skills

Not explicitly listed — technical requirements folded into required qualifications.

---

## Benefits

- Virtual Stock Option programme
- €2000 annual L&D budget
- Pension scheme matching up to 20%
- 28 days paid leave plus public holidays
- Urban Sports Club subsidy
- Kita placement assistance
- Subsidised office lunches
- 1-month sabbatical after 3 years service
- Referral bonus programme

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | moderate | 33% | ✓ |
| collaboration_width | 4 | 4 | 4 | 4 | 100% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit rigour signals (data quality, testing, consistency, governed domains, data contracts) with zero velocity language throughout the responsibilities section.

**Run 2:** `rigour` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, governance, and reliability throughout—'data contracts', 'quality-assured', 'tested', 'deep care for data quality, trust, and discoverability'—with no velocity or speed signals present.

**Run 3:** `rigour` ✓
> Quote: "Deep care for data quality, trust, and discoverability, building models others can rely on"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, documentation, and governance throughout, with no velocity-focused language present.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring"
> Verified: ✓ found in JD
> Reasoning: Fintech sector inherently high-risk, and JD explicitly mentions risk scoring and merchant activity with direct financial transaction implications.

**Run 2:** `high` ✓
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring"
> Verified: ✓ found in JD
> Reasoning: SumUp is fintech, and the explicit mention of 'risk scoring' indicates modeling of financial/credit risk decisions that directly affect business outcomes with regulatory and financial consequences.

**Run 3:** `moderate` ✗
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring"
> Verified: ✓ found in JD
> Reasoning: While SumUp operates in fintech where risk is inherent, the JD uses generic operational language (KPI models, funnels, cohorts) rather than explicit financial reporting or compliance terminology.

⚠ **LLM inconsistency**: runs gave ['high', 'high', 'moderate']

### collaboration_width
**Manual:** `4`

**Run 1:** `4` ✓
> Quote: "Product Managers; Engineers; Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions explicitly identified as collaboration partners in the required qualifications section.

**Run 2:** `4` ✓
> Quote: "Product Managers; Engineers; Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names four distinct partner functions in the required qualifications section.

**Run 3:** `4` ✓
> Quote: "Product Managers; Engineers; Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions are explicitly listed as collaboration partners in the qualifications section.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: Existing governance infrastructure, multiple established business domains, and reusable data products indicate a function beyond early stage that is scaling, not a mature multi-team operation.

**Run 2:** `mid` ✗
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: References to maintaining existing 'governed domains', named tools already in use (dbt, Snowflake, Iceberg), and staging pipelines indicate an established data function extending existing infrastructure rather than building from zero.

**Run 3:** `mid` ✗
> Quote: "maintaining staging pipelines, applying modelling conventions, and keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure and tools (staging pipelines, dbt), indicating an established data function beyond greenfield stage.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions, and keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: Specific technical terminology (data contracts, staging pipelines, modelling conventions, incremental processing strategies) demonstrating practitioner-level domain expertise rather than generic boilerplate.

**Run 2:** `hiring_manager` ✓
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring, building well-documented, quality-assured data products"
> Verified: ✓ found in JD
> Reasoning: The JD specifies exact domains (merchant activity, lifecycle events, risk scoring) and outputs (KPI models, funnels, cohorts, segmentations) that only someone performing this work daily would itemize, not generic boilerplate.

**Run 3:** `hiring_manager` ✓
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical concepts (governed domains, insights layer architecture, specific analytics artifacts) that suggest hands-on experience, not generic recruiter language.
