# Trace: 2026-07-02_mr-marvis_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — MR MARVIS

**URL:** https://careers.mrmarvis.com/jobs/7670021-senior-analytics-engineer
**Location:** Amsterdam, Netherlands
**Date Posted:** 2026-07-02

---

# Senior Analytics Engineer at MR MARVIS

Location: Amsterdam HQ Office (Hybrid)
Department: PEDX
Salary: Not stated

## Key Responsibilities
The role involves owning the analytics layer of our data platform and bridging data engineering with business intelligence.

Design & Modeling: Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency

Stakeholder Collaboration: Working with business teams to convert analytical needs into structured data solutions and establishing consistent metric definitions

Self-Serve Analytics: Enabling governed access to trusted data sources and optimizing the platform for AI use cases

Data Quality: Implementing testing, monitoring, and data quality checks while partnering with data engineers

## Essential Requirements
- Significant Analytics Engineering or similar technical data role experience
- Strong SQL and production dbt proficiency
- Data modeling expertise (facts, dimensions, grains, marts, testing)
- BI tool experience (Looker Studio, Tableau, Omni, Power BI, or similar)
- Strong stakeholder communication skills
- Openness to using AI tools for workflow improvement
- Ability to own cross-functional analytics problems end-to-end

## Nice-to-Have Skills
Warehouse optimization knowledge, semantic layer/metric governance experience, Omni familiarity, Python/R skills, and retail/ecommerce/DTC industry background

## Benefits Highlights
25 vacation days plus 5-year sabbatical, hybrid work (~3 days weekly in Amsterdam), monthly wellness budget, free coaching platform and meditation app access, daily office lunch, equipment provided, 20% employee discount on products

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 1 | 1 | 1 | 2 | 33% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | mixed | hiring_manager | 33% | ✓ |
| stakeholder_orientation | internal_data | mixed | internal_data | internal_data | 33% | ✓ |
| autonomy_level | strategic | mixed | execution | strategic | 0% | ✗ |
| ai_role |  | ai_enabler | ai_user | ai_enabler | 33% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, governance, and quality through explicit testing and monitoring language with no velocity or speed signals present.

**Run 2:** `rigour` ✓
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, testing, and monitoring throughout with no countervailing velocity language.

**Run 3:** `rigour` ✓
> Quote: "Data Quality: Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, monitoring, data quality checks, and robust modeling over speed or iteration pace.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Working with business teams to convert analytical needs into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: The role supports business intelligence and operational decision-making without explicit financial reporting, compliance, or regulatory language.

**Run 2:** `moderate` ✓
> Quote: "Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: Data quality and governance are emphasized, indicating business decisions depend on data accuracy, but without explicit financial reporting or regulatory language.

**Run 3:** `moderate` ✓
> Quote: "retail/ecommerce/DTC industry background"
> Verified: ✓ found in JD
> Reasoning: The JD lacks explicit financial reporting, regulatory, or compliance language typical of high-risk domains, and the sector hints (retail/ecommerce) imply business decision-making without immediate regulatory consequences.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "data engineers"
> Verified: ✓ found in JD
> Reasoning: Only 'data engineers' is explicitly named as a distinct partner team; 'business teams' is too generic to count as a specific named function.

**Run 2:** `1` ✓
> Quote: "data engineers"
> Verified: ✓ found in JD
> Reasoning: Only data engineers are explicitly named as a collaboration partner; 'business teams' is generic and does not count as a named function.

**Run 3:** `2` ✗
> Quote: "business teams; data engineers"
> Verified: ✓ found in JD
> Reasoning: Two distinct named functions are explicitly mentioned: business teams and data engineers.

⚠ **LLM inconsistency**: runs gave ['1', '1', '2']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "owning the analytics layer of our data platform"
> Verified: ✓ found in JD
> Reasoning: The JD references an existing data platform with established tooling (dbt) and multiple data roles already in place, indicating a function with infrastructure that is scaling.

**Run 2:** `mid` ✓
> Quote: "owning the analytics layer of our data platform and bridging data engineering with business intelligence"
> Verified: ✓ found in JD
> Reasoning: Named dbt tools appear in responsibilities and multiple data functions are implied, indicating an established platform being scaled rather than early-stage.

**Run 3:** `mid` ✓
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt) appear in responsibilities with specific technical context, and multiple data roles are implied (data engineers, business teams), indicating an established but still-growing function.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain technical specificity about dbt application context, data modeling terminology (facts, dimensions, grains, marts), and platform optimization concerns that only come from someone who has done this role.

**Run 2:** `mixed` ✗
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: Specific tool names and technical concerns (dbt, cost optimization, metric definitions) are mixed with generic collaboration language.

**Run 3:** `hiring_manager` ✓
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: The specific technical knowledge about how dbt engineers translate business logic and optimize for performance demonstrates hands-on expertise from someone who has done this job.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `mixed` ✗
> Quote: "Working with business teams to convert analytical needs into structured data solutions; Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize both serving business BI needs and building internal data platform infrastructure with roughly equal weight.

**Run 2:** `internal_data` ✓
> Quote: "owning the analytics layer of our data platform"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is to the analytics data platform itself with emphasis on self-serve analytics and data quality, even though business collaboration is part of execution.

**Run 3:** `internal_data` ✓
> Quote: "owning the analytics layer of our data platform and bridging data engineering with business intelligence"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is platform ownership and infrastructure, with business collaboration framed as understanding their needs rather than serving revenue, product, or finance functions.

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'internal_data']

### autonomy_level
**Manual:** `strategic`

**Run 1:** `mixed` ✗
> Quote: "owning the analytics layer of our data platform"
> Verified: ✓ found in JD
> Reasoning: The role is framed around ownership of the analytics layer but the enumerated responsibilities are primarily execution-oriented (building, implementing, enabling) rather than strategic direction-setting.

**Run 2:** `execution` ✗
> Quote: "Working with business teams to convert analytical needs into structured data solutions"
> Verified: ✓ found in JD
> Reasoning: The role executes on analytical needs defined by business teams within the analytics layer domain rather than setting company analytics strategy.

**Run 3:** `strategic` ✓
> Quote: "owning the analytics layer of our data platform"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to own the analytics platform and establish metric definitions, setting direction rather than executing work assigned by others.

⚠ **Disagreement**: manual=`strategic` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'strategic']

### ai_role
**Manual:** ``

**Run 1:** `ai_enabler` ✗
> Quote: "optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure optimized for AI system consumption, with secondary signal of openness to using AI tools for personal workflow improvement.

**Run 2:** `ai_user` ✗
> Quote: "Openness to using AI tools for workflow improvement"
> Verified: ✓ found in JD
> Reasoning: The requirement indicates the candidate should use AI coding or productivity tools to accelerate their own work.

**Run 3:** `ai_enabler` ✗
> Quote: "optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems consume, as indicated by optimizing the platform for AI use cases.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_enabler`

⚠ **LLM inconsistency**: runs gave ['ai_enabler', 'ai_user', 'ai_enabler']

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as practices the candidate owns and implements through action verbs, not merely listed as skills or tools.

**Run 2:** `responsibility` ✗
> Quote: "Implementing testing, monitoring, and data quality checks"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as something the candidate implements and owns, not merely a tool or skill they possess.

**Run 3:** `responsibility` ✗
> Quote: "Implementing testing, monitoring, and data quality checks"
> Verified: ✓ found in JD
> Reasoning: Testing is listed as a core responsibility with the ownership verb 'implementing', not merely as a tool in a requirements list.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: Operational reliability through governance and trust is clearly a concern, but without explicit compliance, regulatory, or stakeholder-trust-crisis framing typical of high loss-aversion roles.

**Run 2:** `moderate` ✗
> Quote: "Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: Governance and trustworthiness indicate operational reliability matters, but without regulatory, compliance, or decision-protection language, this is moderate rather than high risk aversion.

**Run 3:** `moderate` ✗
> Quote: "Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes trust and reliability in data infrastructure, but without compliance, regulatory, or business-impact risk language that would indicate high loss aversion.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
