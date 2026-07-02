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

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 1 | 2 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | hiring_manager | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | mixed | strategic | 33% |
| ai_role | ai_enabler | ai_enabler | ai_enabler | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, monitoring, and data quality implementation as core practices with no counterbalancing velocity language, indicating a rigour-focused orientation.

**Run 2:** `rigour`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities explicitly frame data quality and testing as core expectations, a clear rigour signal with no offsetting velocity language.

**Run 3:** `rigour`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, and reliability with no velocity language, making rigour the clear primary orientation.

### domain_risk

**Run 1:** `moderate`
> Quote: "converting analytical needs into structured data solutions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role affects business decision-making infrastructure but contains no signals of financial reporting, regulatory compliance, or audit that would elevate it to high risk.

**Run 2:** `moderate`
> Quote: "converting analytical needs into structured data solutions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities focus on business decision support without explicit financial reporting, compliance, or regulatory language characteristic of high-risk domains.

**Run 3:** `moderate`
> Quote: "Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: Data errors would affect business decisions and analytics reliability but lack explicit financial reporting, regulatory, or compliance language that would indicate high risk.

### collaboration_width

**Run 1:** `2`
> Quote: "bridging data engineering with business intelligence; partnering with data engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role explicitly names data engineering and business intelligence as distinct partner functions.

**Run 2:** `1`
> Quote: "partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: Only "data engineers" is explicitly named as a collaboration partner; other references like "business teams" are too generic to count as distinct named functions.

**Run 3:** `2`
> Quote: "business teams; data engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names two distinct partner teams: business teams and data engineers.

⚠ **LLM inconsistency**: runs gave ['2', '1', '2']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: Named tool (dbt) appears in responsibilities with specific application context, indicating established infrastructure beyond early stage, but team structure and scale suggest not yet fully mature.

**Run 2:** `mid`
> Quote: "owning the analytics layer of our data platform and bridging data engineering with business intelligence"
> Verified: ✓ found in JD
> Reasoning: The platform and analytics infrastructure already exist with named tools (dbt, BI tools) and governance frameworks, positioning this as a mid-stage data team that is scaling and improving existing systems.

**Run 3:** `mid`
> Quote: "owning the analytics layer of our data platform and bridging data engineering with business intelligence"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure (dbt, data platform, BI tools) and implies a functioning data engineering team, but the hire is to strengthen and own the analytics layer.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical detail (dbt with performance and cost optimization) alongside generic stakeholder collaboration language, indicating mixed hiring manager and recruiter input.

**Run 2:** `hiring_manager`
> Quote: "Data modeling expertise (facts, dimensions, grains, marts, testing)"
> Verified: ✓ found in JD
> Reasoning: The requirements list uses specialized technical terminology (facts, dimensions, grains, marts) that only someone deeply familiar with analytics engineering would specify, indicating hiring manager authorship.

**Run 3:** `hiring_manager`
> Quote: "Building robust dbt models that translate business logic into scalable solutions while optimizing for performance and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical knowledge—named tools (dbt) with precise context, data modeling methodology (facts, dimensions, grains, marts), and explicit performance/cost optimization focus—that indicates hiring manager authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Enabling governed access to trusted data sources and optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: The role's primary framing emphasizes building and optimizing infrastructure for internal data consumers rather than serving commercial, product, or finance functions.

**Run 2:** `internal_data`
> Quote: "Enabling governed access to trusted data sources and optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: The core responsibilities center on building and maintaining data infrastructure for internal consumption, not directly serving commercial, product, or finance functions.

**Run 3:** `internal_data`
> Quote: "Enabling governed access to trusted data sources and optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: The primary audience is internal data consumers and the data platform itself, with business teams as secondary stakeholders whose needs are translated into platform solutions.

### autonomy_level

**Run 1:** `mixed`
> Quote: "owning the analytics layer of our data platform and bridging data engineering with business intelligence"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership of the analytics layer but operates as a bridge within existing infrastructure and in service of business team needs, combining direction-setting with execution.

**Run 2:** `mixed`
> Quote: "owning the analytics layer of our data platform and bridging data engineering with business intelligence"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of the analytics layer and metric definitions with execution-focused implementation of business-driven analytical needs, reflecting both direction-setting and delivery accountability.

**Run 3:** `strategic`
> Quote: "owning the analytics layer of our data platform"
> Verified: ✓ found in JD
> Reasoning: The use of 'owning' combined with design, modeling, establishing, and implementing verbs indicates the role is expected to define direction and shape the analytics function.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'strategic']

### ai_role

**Run 1:** `ai_enabler`
> Quote: "optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: While the JD mentions openness to using AI tools, the primary AI framing in responsibilities is building data infrastructure that AI systems consume.

**Run 2:** `ai_enabler`
> Quote: "optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: While the JD mentions openness to AI tools, the primary AI signal is building data infrastructure for AI systems, making this an ai_enabler role.

**Run 3:** `ai_enabler`
> Quote: "optimizing the platform for AI use cases"
> Verified: ✓ found in JD
> Reasoning: While the candidate is expected to use AI tools for workflow improvement, the primary AI expectation is building data infrastructure that AI systems can consume, making ai_enabler the dominant classification.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality checks are framed as owned responsibilities using the action verb "implementing," indicating the candidate is accountable for these practices.

**Run 2:** `responsibility`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: Data quality and testing are framed as owned responsibilities with action verbs ("implementing"), indicating the candidate is accountable for establishing these practices.

**Run 3:** `responsibility`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as owned responsibilities with the action verb 'implementing', not listed as a required skill.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Implementing testing, monitoring, and data quality checks"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are framed as operational responsibilities rather than risk prevention, with no compliance or stakeholder-trust language to elevate this to high loss aversion.

**Run 2:** `moderate`
> Quote: "Enabling governed access to trusted data sources"
> Verified: ✓ found in JD
> Reasoning: While governance and data quality are priorities, the JD frames them as operational practices rather than risk or compliance mitigation, reflecting moderate rather than high loss aversion.

**Run 3:** `moderate`
> Quote: "Implementing testing, monitoring, and data quality checks while partnering with data engineers"
> Verified: ✓ found in JD
> Reasoning: Operational reliability through testing and monitoring is a concern, but the JD lacks the regulatory, compliance, or stakeholder trust language that would indicate high loss aversion framing.
