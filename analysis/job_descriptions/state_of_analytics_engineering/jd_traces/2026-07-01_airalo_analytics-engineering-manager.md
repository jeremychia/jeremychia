# Trace: 2026-07-01_airalo_analytics-engineering-manager

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineering Manager — Airalo

**URL:** https://jobs.lever.co/airalo/3dd4a880-d804-4099-8d69-df0833a30838
**Location:** Remote (Spain / United Kingdom)
**Date Posted:** 2026-07-01
**Salary:** 110,000–140,000 GBP

---

Analytics Engineering Manager at Airalo

Location: Spain / United Kingdom (Remote-first)
Employment Type: Full-time / Employee
Salary: UK: £110,000 to £140,000 | Spain: €100,000 - €125,000

About Airalo
Airalo is the world's first eSIM store that helps people connect in over 200+ countries and regions across the globe. We are building the next digital service that revolutionises the telecom industry. We are a travel-tech company and an equal-opportunity environment. Our team is spread across 50+ countries and six continents.

About the Role
We're looking for an Analytics Engineering Manager to lead our self-service analytics infrastructure and data modelling practice at Airalo. You'll own the foundations that make analytics possible at scale: the semantic layer, core data models, dashboards, and the self-service platform (Lightdash) that enables teams across the business to answer their own questions. This is a building role — you'll establish how we model data, how we govern metrics, and how we roll out self-service capabilities across a 20M+ user business operating in 190+ countries.

You'll report to the Director of Data and partner closely with analytics teams and stakeholders across the business, translating their analytical needs into scalable, production-quality data models. Success looks like business users confidently answering their own questions, a governed semantic layer that analytics teams trust, and a self-service platform that replaces our patchwork of legacy reporting tools and robust data models that scale without use cases.

What you'll Do:
- Lead and grow a team of analytics engineers (currently 2, scaling to 4 this year), building a culture of craft, documentation, and user empathy
- Drive the rollout and adoption of Lightdash as our single source of truth for business reporting, based on a unified KPI framework currently in progress
- Own all dashboard development initially — from executive reporting to operational views, with support from analysts — then fully transition the ownership to analysts as self-service matures, building the templates and processes that enable this shift
- Partner with stakeholders to translate reporting needs into well-designed, maintainable data products
- Design and deliver training and enablement programs for business users across all functions
- Own and evolve our core dbt models and semantic layer to support key analytical use cases: customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting
- Establish governance and standards: metric definitions, dashboard design patterns, modelling practices, testing frameworks, and documentation
- Partner with analysts to translate their needs into scalable data assets, and with Data Engineering on pipeline reliability and data quality
- Partner with Data Engineering on pipeline reliability, data quality, and infrastructure decisions
- Balance rigour with delivery speed — we're still building foundations while the business moves fast

Must have:
- 5+ years in analytics engineering, data engineering, or technical analytics roles, with 2+ years of people management experience — ideally building or scaling a team
- You're a hands-on leader who partners with senior leadership on strategy and priorities while owning execution and day-to-day team decisions
- Deep proficiency in dbt — you've built and scaled dbt projects, not just contributed to them
- Strong SQL and experience with at least one programming language (Python preferred)
- Experience implementing or heavily using a semantic layer / metrics layer (Lightdash, Looker, MetricFlow, or similar)
- Track record of driving self-service analytics adoption — training programs, documentation, stakeholder enablement
- Familiarity …[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | mixed | mixed | mixed | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | high | 33% | ✓ |
| collaboration_width | 3 | 2 | 2 | 2 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Balance rigour with delivery speed — we're still building foundations while the business moves fast"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames both orientations with rigour signals (governance, testing frameworks, documentation) and velocity signals (building, business moving fast), making this genuinely balanced rather than dominated by either.

**Run 2:** `mixed` ✓
> Quote: "Balance rigour with delivery speed — we're still building foundations while the business moves fast"
> Verified: ✓ found in JD
> Reasoning: The responsibilities heavily emphasize governance, testing, and standards (rigour signals) while explicitly framing a required balance with delivery speed and acknowledging the business moves fast.

**Run 3:** `mixed` ✓
> Quote: "Balance rigour with delivery speed — we're still building foundations while the business moves fast"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames managing tension between both: establishing governance and testing frameworks (rigour) while moving fast to build foundations (velocity), with both framed as essential.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting"
> Verified: ✓ found in JD
> Reasoning: While financial reporting is mentioned, the B2C/marketplace context and absence of regulatory or compliance language indicate moderate risk rather than high-risk financial/compliance domains.

**Run 2:** `moderate` ✓
> Quote: "financial reporting"
> Verified: ✓ found in JD
> Reasoning: While the role mentions financial reporting as an analytical use case, the company is travel-tech (not fintech/banking/regulated), with no explicit compliance or regulatory language, placing it at moderate rather than high risk.

**Run 3:** `high` ✗
> Quote: "financial reporting"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly lists financial reporting as a core analytical use case, which carries inherent high risk of financial impact if data is incorrect.

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'high']

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "analytics teams; Data Engineering"
> Verified: ✓ found in JD
> Reasoning: Named partner functions are analytics teams and Data Engineering; other references use generic terms like 'stakeholders' which do not count.

**Run 2:** `2` ✗
> Quote: "Partner with analysts to translate their needs into scalable data assets, and with Data Engineering on pipeline reliability and data quality"
> Verified: ✓ found in JD
> Reasoning: Two distinct partner functions are explicitly named—Analysts and Data Engineering—as collaboration partners in the responsibilities.

**Run 3:** `2` ✗
> Quote: "analytics teams; Data Engineering"
> Verified: ✓ found in JD
> Reasoning: The JD names two distinct functional partners: analytics teams/analysts as a cohort, and Data Engineering as a named function.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "lead and grow a team of analytics engineers (currently 2, scaling to 4 this year)"
> Verified: ✓ found in JD
> Reasoning: The team already exists with foundation and tools in place, scaling from 2 to 4 engineers, indicating mid-stage growth rather than building from zero in a greenfield environment.

**Run 2:** `mid` ✓
> Quote: "Own and evolve our core dbt models and semantic layer to support key analytical use cases"
> Verified: ✓ found in JD
> Reasoning: The data infrastructure exists (core dbt models, semantic layer, team of 2) and is being evolved and scaled, signaling mid-maturity rather than early greenfield or established mature stage.

**Run 3:** `mid` ✓
> Quote: "Lead and grow a team of analytics engineers (currently 2, scaling to 4 this year)"
> Verified: ✓ found in JD
> Reasoning: The team exists with 2 people and is actively growing to 4, indicating a growing function with named tools in place rather than early greenfield or fully mature scale.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Own and evolve our core dbt models and semantic layer to support key analytical use cases: customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about dbt, semantic layer, and named analytical use cases indicates hiring-manager input, but this mixes with generic people-management language elsewhere suggesting recruiter involvement.

**Run 2:** `hiring_manager` ✓
> Quote: "Own and evolve our core dbt models and semantic layer to support key analytical use cases: customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting"
> Verified: ✓ found in JD
> Reasoning: The responsibilities show deep technical specificity about platform architecture (semantic layer, dbt), specific business use cases (LTV, acquisition, retention), and data infrastructure choices that only come from someone managing this function.

**Run 3:** `hiring_manager` ✓
> Quote: "Own and evolve our core dbt models and semantic layer to support key analytical use cases: customer LTV, acquisition effectiveness, retention, funnel performance, and financial reporting"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain specific technical context (named tools, specific use cases and metrics, data warehouse patterns) that only comes from direct experience, not recruiter boilerplate.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "the self-service platform (Lightdash) that enables teams across the business to answer their own questions"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building analytics infrastructure and platform capabilities that internal teams consume, not serving external commercial, product, or finance stakeholders directly.

**Run 2:** `internal_data` ✓
> Quote: "self-serve platform (Lightdash) that enables teams across the business to answer their own questions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role is primarily focused on building and maintaining the data infrastructure and platform that business users consume, rather than serving a specific business function directly.

**Run 3:** `internal_data` ✓
> Quote: "self-service analytics infrastructure and data modelling practice"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building infrastructure (semantic layer, models, self-serve platform) for internal analytics consumers to answer their own questions.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "You'll own the foundations that make analytics possible at scale... you'll establish how we model data, how we govern metrics, and how we roll out self-service capabilities"
> Verified: ⚠ NOT found verbatim
> Reasoning: Strategic ownership verbs throughout (own, establish, drive, design) indicate the manager sets direction and defines practices for the analytics engineering function.

**Run 2:** `strategic` ✓
> Quote: "establish how we model data, how we govern metrics, and how we roll out self-service capabilities"
> Verified: ✓ found in JD
> Reasoning: The role is expected to set direction and define the analytics architecture, governance, and platform strategy, rather than executing work scoped by others.

**Run 3:** `strategic` ✓
> Quote: "you'll establish how we model data, how we govern metrics, and how we roll out self-service capabilities"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly framed around establishing and defining foundational practices rather than executing pre-determined priorities, with the candidate setting direction for the analytics function.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI infrastructure development, or expected AI-related candidate skills.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no language suggesting the candidate should use AI coding tools or build AI data infrastructure; it focuses purely on traditional analytics engineering.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI infrastructure, or AI systems requiring the candidate's involvement.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Establish governance and standards: metric definitions, dashboard design patterns, modelling practices, testing frameworks, and documentation"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks are listed as something the candidate will establish and own through governance standards, indicating ownership of the testing practice rather than just tool familiarity.

**Run 2:** `responsibility` ✗
> Quote: "Establish governance and standards: metric definitions, dashboard design patterns, modelling practices, testing frameworks, and documentation"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks are explicitly listed as something the role establishes and owns as part of the governance standards, indicating ownership rather than just tool usage.

**Run 3:** `responsibility` ✗
> Quote: "Establish governance and standards: metric definitions, dashboard design patterns, modelling practices, testing frameworks, and documentation"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks are framed as something the candidate will establish (define and own standards), not merely use or have familiarity with.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "a governed semantic layer that analytics teams trust"
> Verified: ✓ found in JD
> Reasoning: Reliability and trust concerns are present (governance, robustness, reliability), but risk framing is secondary to the primary mission of building and enabling analytics capabilities.

**Run 2:** `moderate` ✗
> Quote: "Partner with Data Engineering on pipeline reliability and data quality"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role emphasizes operational reliability and data quality as partnership areas, but these are presented as secondary to the primary mission of building self-serve analytics infrastructure, indicating moderate loss aversion rather than high.

**Run 3:** `moderate` ✗
> Quote: "Balance rigour with delivery speed — we're still building foundations while the business moves fast"
> Verified: ✓ found in JD
> Reasoning: The JD indicates operational quality and reliability must be balanced with delivery, but frames this as engineering practice rather than preventing regulatory/compliance risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
