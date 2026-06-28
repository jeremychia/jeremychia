# Trace: 2026-06-23_trade-republic_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Trade Republic

**Location:** Berlin, Germany

---

## Key Responsibilities

- Working closely with product and business stakeholders to define and build meaningful product metrics
- Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and analysis for stakeholders
- Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed, applying software engineering best practices
- Taking ownership of projects from scoping to delivery and adoption, working autonomously

---

## Required Qualifications

- At least 5 years of engineering experience with an analytical mindset
- Solid understanding of architectures, design principles and engineering best practices
- Experience across all stages of the data pipeline: ingestion, transformations, mart creation

---

## Preferred / Bonus Skills

- Experience with our tech stack is a bonus: S3/Snowflake/Airflow/Python/DBT

---

## Benefits

- Opportunity to grow career by collaborating with a team of outstanding talents and state of the art technology
- Culture that rewards ownership, excellence, and high energy
- Mission-driven: closing the pension gap and democratising wealth across 17 countries
- Commitment to DEI and equal opportunity

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | mixed | rigour | rigour | 33% | ✗ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 2 | 2 | 1 | 1 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | recruiter | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation |  | product | product | product | 100% | ✗ |
| autonomy_level |  | mixed | strategic | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed, applying software engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes both speed/cost reduction as optimization goals and software engineering best practices, showing genuinely balanced orientation toward both velocity and quality.

**Run 2:** `rigour` ✗
> Quote: "applying software engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The explicit expectation to apply engineering best practices signals rigour as the primary orientation over velocity.

**Run 3:** `rigour` ✗
> Quote: "applying software engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize architecture, design principles, and engineering best practices as core expectations, with speed mentioned only as an optimization outcome, not a primary delivery orientation.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

⚠ **LLM inconsistency**: runs gave ['mixed', 'rigour', 'rigour']

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: Although Trade Republic is fintech, the JD focuses on product analytics and dashboards rather than financial reporting or regulatory compliance, placing the role in moderate-risk territory despite the high-risk sector.

**Run 2:** `moderate` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: The focus on product metrics and self-serve analytics without explicit regulatory or financial reporting language indicates moderate risk business intelligence.

**Run 3:** `moderate` ✗
> Quote: "Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and analysis for stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role focuses on product analytics and self-serve infrastructure without explicit mention of financial reporting, regulatory compliance, or audit responsibilities.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `2` ✓
> Quote: "product and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: The JD names two distinct partner functions: product team and business stakeholders.

**Run 2:** `1` ✗
> Quote: "product and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'product' is a named function; 'business stakeholders' is too generic to count as a distinct team.

**Run 3:** `1` ✗
> Quote: "product and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'product' is explicitly named as a distinct function; 'business' is generic terminology without identifying a specific team.

⚠ **Disagreement**: manual=`2` vs LLM majority=`1`

⚠ **LLM inconsistency**: runs gave ['2', '1', '1']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed"
> Verified: ✓ found in JD
> Reasoning: The JD references existing architecture and infrastructure being improved and scaled, indicating an established data function beyond early stages but not yet mature enterprise scale.

**Run 2:** `mid` ✓
> Quote: "Improving our architecture (cloud-based and always evolving)"
> Verified: ✓ found in JD
> Reasoning: Reference to improving existing architecture indicates a data function that has been established and is growing, rather than early-stage or fully mature.

**Run 3:** `mid` ✓
> Quote: "Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed"
> Verified: ✓ found in JD
> Reasoning: The architecture already exists and is actively evolving, indicating an established data function in growth phase rather than early-stage greenfield or mature scale.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `recruiter` ✗
> Quote: "Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and analysis for stakeholders"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs and boilerplate language with no specific technical context, scale, tool application, or business problem detail that would indicate hiring manager authorship.

**Run 2:** `mixed` ✗
> Quote: "Experience across all stages of the data pipeline: ingestion, transformations, mart creation"
> Verified: ✓ found in JD
> Reasoning: Some technical specificity in requirements about pipeline stages, but responsibilities remain generic with boilerplate collaboration and ownership language.

**Run 3:** `recruiter` ✗
> Quote: "Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and analysis for stakeholders"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs and abstract categories without technical specificity—no named tools with applied context, volume numbers, or concrete problem statements.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `product` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: The primary focus on defining product metrics and enabling product/business stakeholders, combined with emphasis on analytical products, indicates this is fundamentally a product analytics role.

**Run 2:** `product` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: The explicit focus on product metrics and collaboration with product stakeholders indicates a product-facing analytics role.

**Run 3:** `product` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility explicitly establishes product teams as the main stakeholder audience, with the role focused on defining product metrics in close collaboration with them.

⚠ **Disagreement**: manual=`` vs LLM majority=`product`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Taking ownership of projects from scoping to delivery and adoption, working autonomously"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership and autonomy over project execution and metric definition, but operates within the direction and priorities set by product and business stakeholders.

**Run 2:** `strategic` ✗
> Quote: "Taking ownership of projects from scoping to delivery and adoption, working autonomously"
> Verified: ✓ found in JD
> Reasoning: Explicit language about ownership, autonomous work, and defining product metrics indicates strategic responsibility for setting analytics direction.

**Run 3:** `mixed` ✗
> Quote: "Taking ownership of projects from scoping to delivery and adoption, working autonomously"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic elements (scoping projects, defining metrics, autonomous ownership) with execution elements (delivery and adoption of analytics products).

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'mixed']
