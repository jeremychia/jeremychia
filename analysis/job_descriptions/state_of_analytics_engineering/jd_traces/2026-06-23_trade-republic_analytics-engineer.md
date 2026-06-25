# Trace: 2026-06-23_trade-republic_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Trade Republic

**URL:** https://traderepublic.com/en-de/about?gh_jid=6589276003&gh_src=632be8e43us&jobId=6589276003
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
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 2 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | recruiter | hiring_manager | 0% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "applying software engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The JD consistently emphasizes software engineering fundamentals, architecture, and best practices as the primary work orientation, with no velocity language.

**Run 2:** `rigour` ✗
> Quote: "applying software engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes software engineering best practices, design principles, and building meaningful products with deliberate ownership through delivery and adoption, establishing rigour as the primary orientation despite a single mention of speed in an optimization context.

**Run 3:** `rigour` ✗
> Quote: "applying software engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes software engineering best practices and architecture design as core expectations, with only a single passing reference to speed nested within cost-reduction language.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: While Trade Republic is fintech (high-risk sector), the JD language lacks explicit financial reporting, compliance, or regulatory signals, suggesting this role's data work impacts operational decisions rather than direct financial/regulatory consequences.

**Run 2:** `moderate` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: While Trade Republic is fintech (which defaults to high risk), the JD uses generic language about product metrics and stakeholder enablement without explicit signals of financial reporting, regulatory compliance, or audit concerns.

**Run 3:** `moderate` ✗
> Quote: "Working closely with product and business stakeholders to define and build meaningful product metrics"
> Verified: ✓ found in JD
> Reasoning: While Trade Republic operates in fintech, the JD focuses on product metrics and self-serve analytics without explicitly invoking financial reporting, regulatory compliance, or audit language.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `1` ✗
> Quote: "product and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'Product' is an explicitly named team function; 'business stakeholders' is too generic to count per the rules.

**Run 2:** `1` ✗
> Quote: "product"
> Verified: ✓ found in JD
> Reasoning: Only the Product team is explicitly named as a distinct collaboration partner; business stakeholders is generic phrasing and does not count as a named function.

**Run 3:** `1` ✗
> Quote: "product and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'Product' qualifies as a named distinct function; 'business stakeholders' is generic and does not count per classification rules.

⚠ **Disagreement**: manual=`2` vs LLM majority=`1`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed"
> Verified: ✓ found in JD
> Reasoning: The JD references an existing cloud-based architecture and specific tools/processes, indicating an established data function that is scaling and improving rather than building from zero.

**Run 2:** `mid` ✓
> Quote: "Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed"
> Verified: ✓ found in JD
> Reasoning: The language signals an existing, evolving architecture and established data pipeline stages rather than greenfield building, indicating a growing but not fully mature data organization.

**Run 3:** `mid` ✓
> Quote: "Improving our architecture (cloud-based and always evolving) based on what brings the most impact to cost reduction and speed"
> Verified: ✓ found in JD
> Reasoning: The JD describes improving and evolving an existing architecture, indicating a data function with established infrastructure growing in capability rather than building from zero.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and analysis for stakeholders"
> Verified: ✓ found in JD
> Reasoning: The JD includes some technical specificity (named product types, data pipeline stages) alongside generic boilerplate action verbs, without scale, tool context, or methodology detail.

**Run 2:** `recruiter` ✗
> Quote: "Developing analytical products such as data models, dashboards, reports and tooling to enable self-serve reporting and analysis for stakeholders"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use boilerplate action verbs and generic analytical deliverables without specific technical context, scale numbers, or methodology names that would indicate hiring manager authorship.

**Run 3:** `hiring_manager` ✓
> Quote: "Experience across all stages of the data pipeline: ingestion, transformations, mart creation"
> Verified: ✓ found in JD
> Reasoning: The specific enumeration of pipeline stages and technical framing of architecture optimization decisions indicate hands-on familiarity with the actual role, despite some generic stakeholder collaboration language.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'hiring_manager']
