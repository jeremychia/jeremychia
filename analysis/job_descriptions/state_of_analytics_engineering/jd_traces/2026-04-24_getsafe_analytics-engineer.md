# Trace: 2026-04-24_getsafe_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer (m/f/d) — Getsafe

**URL:** https://getsafe.jobs.personio.com/job/2612426?language=en
**Location:** Berlin, Germany (hybrid); Heidelberg, Germany (hybrid)
**Employment Type:** Full-time, Permanent employee

---

## Key Responsibilities

- Own and evolve core business metrics - from definition to tracking and operationalisation
- Develop the data and analytics components of the AI stack to support experimentation and GenAI applications
- Drive cross-functional data initiatives with stakeholders across Commercial, Operations, and Engineering
- Build and maintain scalable data pipelines and data marts using modern tooling
- Design clean, reliable, and well-documented data models as a single source of truth
- Conduct analyses to uncover insights and inform strategic decisions

---

## Required Qualifications

- 2+ years in Analytics Engineering, Data Analytics, or similar role
- Advanced SQL and data modeling expertise
- Modern transformation frameworks, especially dbt
- AI-ready data foundations: structured, governed, and discoverable data models
- Understanding of product, growth, and operational analytics
- Experience with BI tools like Metabase and self-serve environments
- Proficiency in Python or another programming language for data work
- Strong communication and narrative skills
- Attention to detail and ownership mindset

---

## Preferred / Bonus Skills

(Not separately listed — AI/GenAI stack development is called out as a key responsibility area)

---

## Benefits

- Hybrid work in Berlin or Heidelberg with remote flexibility
- Employee Stock Ownership Program (VSOPs)
- €50 monthly flex benefit budget
- Monthly Getsafe insurance voucher
- 90-day EU workation allowance
- 30 vacation days (including birthday and December 24th & 31st half-days)
- €1,000 annual development budget

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | high | high | moderate | moderate | 33% | ✗ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | mixed | hiring_manager | 33% | ✗ |
| stakeholder_orientation |  | mixed | mixed | mixed | 100% | ✗ |
| autonomy_level |  | strategic | mixed | strategic | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Design clean, reliable, and well-documented data models as a single source of truth"
> Verified: ✓ found in JD
> Reasoning: The JD consistently emphasizes reliability, documentation, governance, and data quality through phrases like 'clean', 'reliable', 'well-documented', 'structured, governed', and 'Attention to detail', while mentions of GenAI and experimentation are secondary to the infrastructure focus.

**Run 2:** `rigour` ✗
> Quote: "Design clean, reliable, and well-documented data models as a single source of truth"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, reliability, documentation standards, and governance as core expectations with no countervailing velocity language.

**Run 3:** `rigour` ✗
> Quote: "Design clean, reliable, and well-documented data models as a single source of truth"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reliability, documentation quality, and governance as core expectations with no velocity-oriented language present.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation"
> Verified: ✓ found in JD
> Reasoning: Core business metrics in an insurance company directly impact underwriting decisions, claims processing, and regulatory compliance, making data errors costly to the business and potentially to regulatory standing.

**Run 2:** `moderate` ✗
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation"
> Verified: ✓ found in JD
> Reasoning: Although Getsafe operates in the high-risk insurance sector, the JD uses generic business analytics language without explicit mention of regulatory compliance, financial reporting, or audit requirements.

**Run 3:** `moderate` ✗
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation"
> Verified: ✓ found in JD
> Reasoning: While Getsafe is an insurance company, the JD language focuses on business analytics without explicit financial reporting, compliance, or regulatory requirements.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Commercial; Operations; Engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct functions as collaboration partners in the responsibilities section.

**Run 2:** `3` ✓
> Quote: "Commercial; Operations; Engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named partner teams are explicitly listed in the collaboration mandate.

**Run 3:** `3` ✓
> Quote: "Commercial; Operations; Engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct functional teams are explicitly named as collaboration partners in the cross-functional work.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Build and maintain scalable data pipelines and data marts using modern tooling"
> Verified: ✓ found in JD
> Reasoning: The use of 'maintain' alongside 'build', combined with named tools (dbt, Metabase) deployed in responsibilities, indicates an established function with existing infrastructure that is growing and being scaled, not early-stage greenfield work.

**Run 2:** `mid` ✗
> Quote: "Build and maintain scalable data pipelines and data marts using modern tooling"
> Verified: ✓ found in JD
> Reasoning: The emphasis on maintaining existing infrastructure with modern tools (dbt, Metabase) and evolving established metrics indicates a functioning data function in a growth phase, not early-stage or fully mature.

**Run 3:** `mid` ✗
> Quote: "Build and maintain scalable data pipelines and data marts using modern tooling"
> Verified: ✓ found in JD
> Reasoning: The use of both 'build' and 'maintain' indicates established infrastructure being scaled, characteristic of a mid-stage team.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Develop the data and analytics components of the AI stack to support experimentation and GenAI applications"
> Verified: ✓ found in JD
> Reasoning: The JD blends hiring-manager specificity (AI stack context, dbt, data marts, SSOT methodology) with recruiter boilerplate ('drive cross-functional initiatives', 'conduct analyses to uncover insights').

**Run 2:** `mixed` ✗
> Quote: "Drive cross-functional data initiatives with stakeholders across Commercial, Operations, and Engineering"
> Verified: ✓ found in JD
> Reasoning: Responsibilities mix boilerplate action verbs with moderately specific technical concepts (metrics definition, data marts, AI stack integration), but more specificity appears in the requirements section than typical hiring manager authorship.

**Run 3:** `hiring_manager` ✓
> Quote: "Develop the data and analytics components of the AI stack to support experimentation and GenAI applications"
> Verified: ✓ found in JD
> Reasoning: Specific technical context (AI/GenAI stack development) shows domain knowledge beyond generic boilerplate language.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation; Develop the data and analytics components of the AI stack to support experimentation and GenAI applications"
> Verified: ⚠ NOT found verbatim
> Reasoning: The first two responsibilities equally emphasize business metric ownership and product/engineering AI enablement, with no clear primary audience across the responsibilities section.

**Run 2:** `mixed` ✗
> Quote: "Drive cross-functional data initiatives with stakeholders across Commercial, Operations, and Engineering"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple equally-weighted audiences—commercial (GTM and revenue), operations, engineering/product (GenAI stack), and broader decision-makers—without a single dominant stakeholder orientation.

**Run 3:** `mixed` ✗
> Quote: "Drive cross-functional data initiatives with stakeholders across Commercial, Operations, and Engineering"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves multiple distinct audiences (Commercial, Operations, Engineering) without a single primary focus, splitting responsibilities between product support and data infrastructure.

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation"
> Verified: ✓ found in JD
> Reasoning: The verb 'own' combined with 'from definition to tracking' indicates end-to-end ownership and the autonomy to define and shape how core metrics are structured and evolved, rather than executing direction from others.

**Run 2:** `mixed` ✗
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic responsibility for defining and evolving metrics within an established domain with execution-oriented work supporting predefined initiatives and cross-functional stakeholders.

**Run 3:** `strategic` ✗
> Quote: "Own and evolve core business metrics - from definition to tracking and operationalisation"
> Verified: ✓ found in JD
> Reasoning: The verb 'own' combined with 'from definition' indicates the role sets direction on metrics strategy and operationalization, not just executing predefined work.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'strategic']
