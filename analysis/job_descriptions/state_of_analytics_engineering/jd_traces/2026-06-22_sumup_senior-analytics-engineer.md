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
| domain_risk | high | moderate | high | high | 33% | ✓ |
| collaboration_width | 4 | 4 | 4 | 4 | 100% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | mixed | 33% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | execution | execution | execution | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, consistency, and data quality throughout, with no velocity-oriented language present.

**Run 2:** `rigour` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, consistency, discoverability, and quality assurance throughout (tested outputs, quality-assured data products, deep care for data quality, testing and documentation), with no velocity signals present.

**Run 3:** `rigour` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit quality, testing, and governance signals dominate the responsibilities with no velocity language.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "risk scoring"
> Verified: ✓ found in JD
> Reasoning: While SumUp is a fintech company and risk scoring is mentioned, the JD does not explicitly use regulatory, compliance, or financial reporting language that would elevate this to high risk.

**Run 2:** `high` ✓
> Quote: "merchant activity, product adoption, lifecycle events, and risk scoring"
> Verified: ✓ found in JD
> Reasoning: SumUp is fintech; errors in merchant activity modeling and risk scoring directly affect financial operations and regulatory compliance.

**Run 3:** `high` ✓
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring"
> Verified: ✓ found in JD
> Reasoning: Risk scoring in a fintech company carries direct regulatory and financial implications for merchant approval decisions.

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'high']

### collaboration_width
**Manual:** `4`

**Run 1:** `4` ✓
> Quote: "Product Managers, Engineers, Analysts, and Data Scientists"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names four distinct functions as collaboration partners: Product (Managers), Engineering, Analytics, and Data Science.

**Run 2:** `4` ✓
> Quote: "Comfort working across squads with Product Managers, Engineers, Analysts, and Data Scientists"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly listed as collaboration partners: Product Managers, Engineers, Analysts, and Data Scientists.

**Run 3:** `4` ✓
> Quote: "Product Managers; Engineers; Analysts; Data Scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions/teams are explicitly listed as collaboration partners.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "helping establish durable ownership, consistent definitions, and a shared catalogue of data products"
> Verified: ✓ found in JD
> Reasoning: The mention of 'helping establish' durable ownership and governance indicates an evolving team still building its organizational structure, rather than an early-stage greenfield or mature, fully-formed operation.

**Run 2:** `mid` ✗
> Quote: "Contribute to SumUp's broader data domain strategy, helping establish durable ownership, consistent definitions, and a shared catalogue of data products"
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure is implied (Snowflake, dbt, staging pipelines, governed domains) and the role involves scaling governance and establishing shared standards across multiple business domains.

**Run 3:** `mid` ✗
> Quote: "Implement technical improvements including incremental processing strategies, performance optimisations, and scalable data architecture"
> Verified: ✓ found in JD
> Reasoning: Focus on optimizing and scaling existing infrastructure indicates functional systems and tools already in place, not greenfield building.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities demonstrate technical specificity (data contracts, staging pipelines, modelling conventions, domain-driven design) and named business domains that only someone doing this job would articulate.

**Run 2:** `hiring_manager` ✓
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: The specific analytical constructs (KPI models, funnels, cohorts, segmentations), architectural terminology (insights layer, governed domains), and technical methodology (incremental processing strategies, modelling conventions) demonstrate direct experience from someone actively doing this work.

**Run 3:** `mixed` ✗
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring, building well-documented, quality-assured data products"
> Verified: ✓ found in JD
> Reasoning: Named business domains and specific technical outputs show domain knowledge, but generic phrases like 'quality-assured data products' and 'well-documented' indicate recruiter involvement.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is building data infrastructure and reusable analytics tools that serve other data consumers and analysts, not directly serving commercial, product, or finance stakeholders.

**Run 2:** `internal_data` ✗
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes building infrastructure, shared catalogues, and reusable data products for internal data consumers rather than serving a specific business function like finance or commercial teams.

**Run 3:** `internal_data` ✗
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building data infrastructure and governance for platform consumers rather than directly serving product, commercial, or finance teams.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize partnership, maintenance, and application of established patterns, framing the role as executing on defined work rather than independently setting direction.

**Run 2:** `execution` ✗
> Quote: "Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions, and keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: The primary work verbs (maintain, apply, keep, model, build) are execution-focused; while event design involves collaboration, scope is determined by existing domain structures, business domains, and squad needs rather than self-directed strategic direction-setting.

**Run 3:** `execution` ✗
> Quote: "Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions, and keeping domain outputs consistent, tested, and discoverable"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize maintaining existing systems, supporting squads, and applying established conventions, with direction set by partners rather than by the role.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

### ai_role
**Run 1:** `none` ✓
> Quote: ""
> Reasoning: No AI tools, infrastructure, or GenAI responsibilities mentioned; standard analytics engineering and domain modeling work.

**Run 2:** `none` ✓
> Quote: "Model key business domains, including merchant activity, product adoption, lifecycle events, and risk scoring, building well-documented, quality-assured data products"
> Reasoning: Standard analytics engineering work with no AI tooling, AI-first mindset, or GenAI infrastructure signals.

**Run 3:** `none` ✓
> Quote: "Build and maintain the insights layer on top of governed domains, producing reusable KPI models, funnels, cohorts, and segmentations"
> Reasoning: Standard analytics engineering work without AI tool or infrastructure expectations


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "building well-documented, quality-assured data products"
> Reasoning: Candidate owns building and quality assurance of data products, with explicit ownership verb paired with quality expectation.

**Run 2:** `responsibility` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Reasoning: Candidate owns quality practice through direct mention of testing and consistency as deliverable responsibilities.

**Run 3:** `responsibility` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Reasoning: Candidate owns testing and quality assurance responsibilities explicitly


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "keeping domain outputs consistent, tested, and discoverable"
> Reasoning: Emphasis on operational consistency and discoverability suggests reliability and pipeline maintenance concerns rather than compliance/audit-primary framing.

**Run 2:** `moderate` ✓
> Quote: "Partner with squads across the tribe on event design and data contracts, maintaining staging pipelines, applying modelling conventions"
> Reasoning: Operational reliability emphasized through data contracts and pipeline stability, but no regulatory or compliance framing.

**Run 3:** `moderate` ✓
> Quote: "governed domains"
> Reasoning: Data governance and quality concerns drive the role, but no explicit compliance or regulatory framing

