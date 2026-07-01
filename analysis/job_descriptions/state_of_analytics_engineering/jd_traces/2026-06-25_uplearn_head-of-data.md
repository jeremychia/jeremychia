# Trace: 2026-06-25_uplearn_head-of-data

## JD text (fed to classifier, Layer B stripped)

```
# Head of Data — Up Learn
**URL:** https://apply.workable.com/uplearn/j/E59EE2339F/

**Location:** London (Old Street) — hybrid, min 2 days/week in office
**Date:** 2026-06-25

---

About us
At Up Learn, we've built one of the world's most effective learning experiences by combining cognitive science, instructional theory, and artificial intelligence. Our mission is to give every learner the most effective path to success, and vision a world where every learner achieves more, faster, through adaptive, mastery-based learning.

We're the market-leading platform for A Levels, with seven courses on offer and 1 in 3 A Level students using Up Learn. Over the next year, we're launching GCSE Science and accelerating growth, expanding our impact to millions more students.

Our results speak for themselves: 97% of students who complete our courses achieve an A*/A, even those who started with lower grades. And a study of Up Learn in schools found usage is associated with 9 months additional progress, with grade improvements across whole year groups.

And for every paying student, we provide a full scholarship to a student in need - ensuring high-quality education is accessible to all.

About the role
The Head of Data will be a key senior leader at Up Learn, responsible for leading and overseeing the entire Data function, and reporting into the CEO. This role requires a strategic and practical individual who can level up Data at Up Learn and deliver new Data capabilities as needed to achieve the company's growth goals this year and beyond. You should be fluent in using AI and data to automate and re-engineer processes, and have the technical expertise to build data foundations in the right way to scale effectively long term. The Head of Data will set data strategy and own Data team OKRs, improve product analytics and use of KPIs across the company, improve learning metrics and impact evaluations, continue to build on our high quality data and analytics infrastructure, and lead a small high performing Data team.

What you'll do in the first 12 months
Up Learn is scaling into GCSEs and using AI to accelerate course development and product capability. As Head of Data, you'll run a high-leverage data function that helps us move faster, make better decisions, and maintain trust with schools and learners.

- Own the Data roadmap and deliver it: Set a clear quarterly plan aligned to our biggest company goals (GCSE expansion, impact evidence, responsible AI), and ship meaningful improvements every month with a small, AI-powered team.
- Strengthen use of measurement in product processes: Embed "instrumentation before shipping" so every major release launches with the right KPIs, tracking, dashboards, and alerts - enabling fast learning, quick diagnosis, and confident iteration.
- Level up our metric system and decision-making: Build on our use of KPIs so teams (and leadership) have an accurate view of performance across Product, Commercial, and Operations.
- Lead our next 'Measuring Learning' impact evaluation: Design and run a credible evaluation of learning impact, and translate findings into clear product/content priorities and school-ready evidence.
- Own responsible AI for learner data: Put in place pragmatic governance and monitoring for AI features that touch learner responses and scoring - so we can innovate and keep trust high.
- Take ownership of data privacy & school assurance: Become our day-to-day lead for data privacy and school-facing data assurance - supporting data sharing agreements and DPIAs, and ensuring our practices around children's data are robust and consistently applied.
- Improve GTM and business insight: Build clearer visibility into funnel performance and ROI (channel → conversion → retention) so we can double down on what works and stop what doesn't.
- Build a high-performance, pragmatic team: Coach and develop our data team, raise quality where it matters, and keep our warehouse/dbt/Lightdash stack reliable and scalable - without slowing the business down.

Requirements
You…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | mixed | rigour | mixed | 33% |
| domain_risk | moderate | high | high | 33% |
| collaboration_width | 4 | 3 | 3 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | hiring_manager | 33% |
| stakeholder_orientation | product | mixed | mixed | 33% |
| autonomy_level | strategic | strategic | strategic | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `mixed`
> Quote: "you value high quality, but you don't gold-plate - except where safety/privacy demands it"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes both shipping quickly ("ship meaningful improvements every month", "move faster") and rigorous governance ("pragmatic governance and monitoring", "robust and consistently applied practices"), with an explicit acknowledgment that quality matters selectively—high where safety/privacy are involved.

**Run 2:** `rigour`
> Quote: "Put in place pragmatic governance and monitoring for AI features that touch learner responses and scoring - so we can innovate and keep trust high"
> Verified: ✓ found in JD
> Reasoning: Governance, compliance, and data accuracy dominate the role's responsibilities and are explicitly non-negotiable, with compliance signals outnumbering velocity signals 2:1 despite the presence of fast-shipping language.

**Run 3:** `mixed`
> Quote: "raise quality where it matters, and keep our warehouse/dbt/Lightdash stack reliable and scalable - without slowing the business down"
> Verified: ✓ found in JD
> Reasoning: The JD balances explicit velocity signals (ship improvements monthly, fast learning, quick iteration) with equally prominent rigor signals (data privacy, DPIAs, governance, reliability) and explicitly frames this as a tradeoff to navigate.

⚠ **LLM inconsistency**: runs gave ['mixed', 'rigour', 'mixed']

### domain_risk

**Run 1:** `moderate`
> Quote: "Put in place pragmatic governance and monitoring for AI features that touch learner responses and scoring"
> Verified: ✓ found in JD
> Reasoning: While the role involves sensitive children's data and AI governance, the JD frames this as pragmatic governance and institutional trust rather than direct financial or regulatory compliance, placing it in moderate risk rather than high.

**Run 2:** `high`
> Quote: "supporting data sharing agreements and DPIAs, and ensuring our practices around children's data are robust and consistently applied"
> Verified: ✓ found in JD
> Reasoning: The role has direct responsibility for GDPR compliance (DPIAs) and children's data governance, which are regulatory requirements with material legal and reputational consequences.

**Run 3:** `high`
> Quote: "Take ownership of data privacy & school assurance: Become our day-to-day lead for data privacy and school-facing data assurance - supporting data sharing agreements and DPIAs, and ensuring our practices around children's data are robust and consistently applied."
> Verified: ✓ found in JD
> Reasoning: Operating with children's data under UK GDPR and school compliance obligations with explicit governance and privacy responsibilities creates high regulatory risk and potential harm to a vulnerable population.

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'high']

### collaboration_width

**Run 1:** `4`
> Quote: "Product, Commercial, and Operations; maintain trust with schools and learners"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three internal departments (Product, Commercial, Operations) as stakeholders and schools as an external collaboration partner for data assurance and trust.

**Run 2:** `3`
> Quote: "Build on our use of KPIs so teams (and leadership) have an accurate view of performance across Product, Commercial, and Operations"
> Verified: ✓ found in JD
> Reasoning: Three distinct named functional teams (Product, Commercial, Operations) are explicitly listed as stakeholder groups the role must serve.

**Run 3:** `3`
> Quote: "Product; Commercial; Operations"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named business functions explicitly identified as key stakeholders: Product, Commercial, and Operations.

⚠ **LLM inconsistency**: runs gave ['4', '3', '3']

### data_team_maturity

**Run 1:** `mid`
> Quote: "continue to build on our high quality data and analytics infrastructure"
> Verified: ✓ found in JD
> Reasoning: The phrase "continue to build on" signals existing infrastructure (dbt, Lightdash, warehouse) that is being improved rather than built from zero, and the role involves leading a "small" team, indicating mid-stage growth rather than established maturity.

**Run 2:** `mid`
> Quote: "continue to build on our high quality data and analytics infrastructure, and lead a small high performing Data team"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, Lightdash, warehouse) and references to existing infrastructure indicate an established function, but the small team size and "build on" language suggest mid-stage growth rather than mature scale.

**Run 3:** `mid`
> Quote: "continue to build on our high quality data and analytics infrastructure"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, Lightdash, warehouse) appear in responsibilities with operational context, and the role centers on improving and scaling existing infrastructure rather than establishing foundational capability.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Embed 'instrumentation before shipping' so every major release launches with the right KPIs, tracking, dashboards, and alerts"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD demonstrates technical specificity only someone doing this work would know—named tools (dbt/Lightdash), specific practices (instrumentation before shipping), and concrete methodologies (KPI definition, evaluation design)—far exceeding generic boilerplate.

**Run 2:** `mixed`
> Quote: "keep our warehouse/dbt/Lightdash stack reliable and scalable; Embed 'instrumentation before shipping' so every major release launches with the right KPIs, tracking, dashboards, and alerts"
> Verified: ⚠ NOT found verbatim
> Reasoning: Technical specificity about named tools and precise methodologies (instrumentation before shipping, impact evaluation) is mixed with generic team-building and stakeholder-management language, indicating both hiring manager and recruiter input.

**Run 3:** `hiring_manager`
> Quote: "Embed 'instrumentation before shipping' so every major release launches with the right KPIs, tracking, dashboards, and alerts - enabling fast learning, quick diagnosis, and confident iteration."
> Verified: ⚠ NOT found verbatim
> Reasoning: Technical specificity of methodology (instrumentation before shipping with named components: KPIs, tracking, dashboards, alerts) and precision about concrete problems to solve indicates hiring manager authorship from hands-on experience.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `product`
> Quote: "Strengthen use of measurement in product processes: Embed 'instrumentation before shipping' so every major release launches with the right KPIs, tracking, dashboards, and alerts - enabling fast learning, quick diagnosis, and confident iteration"
> Verified: ⚠ NOT found verbatim
> Reasoning: Product analytics and measurement in product development is the first responsibility in the 12-month plan, with explicit emphasis on KPIs, feature impact measurement, and embedding measurement into product processes.

**Run 2:** `mixed`
> Quote: "Build on our use of KPIs so teams (and leadership) have an accurate view of performance across Product, Commercial, and Operations"
> Verified: ✓ found in JD
> Reasoning: Responsibilities equally emphasize serving Product (measurement, instrumentation), Commercial (GTM, funnel), and Operations, indicating three co-equal stakeholder audiences with roughly balanced emphasis.

**Run 3:** `mixed`
> Quote: "Build on our use of KPIs so teams (and leadership) have an accurate view of performance across Product, Commercial, and Operations"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple stakeholder groups with roughly equal responsibility weight: Product (measurement in product processes), Commercial (GTM and funnel ROI), data function itself (infrastructure and metrics system), and the education mission (learning impact evaluation and school assurance).

⚠ **LLM inconsistency**: runs gave ['product', 'mixed', 'mixed']

### autonomy_level

**Run 1:** `strategic`
> Quote: "set data strategy and own Data team OKRs"
> Verified: ✓ found in JD
> Reasoning: The role explicitly owns strategy definition and OKRs for the data function, not execution of someone else's plan, positioning this as a leadership role that shapes direction.

**Run 2:** `strategic`
> Quote: "The Head of Data will set data strategy and own Data team OKRs"
> Verified: ✓ found in JD
> Reasoning: Direct authority to set strategy, own OKRs, and define the data roadmap indicates strategic direction-setting rather than execution of scoped work set by others.

**Run 3:** `strategic`
> Quote: "set data strategy and own Data team OKRs"
> Verified: ✓ found in JD
> Reasoning: Explicit strategic verbs (set strategy, own roadmap, define quarterly plans aligned to company goals) establish the role as responsible for defining direction and priorities for the entire data function.

### ai_role
**Run 1:** `ai_enabler` ✓
> Quote: "Put in place pragmatic governance and monitoring for AI features that touch learner responses and scoring"
> Reasoning: Candidate builds governance and monitoring infrastructure that AI systems depend on to operate safely.

**Run 2:** `ai_enabler` ✓
> Quote: "Put in place pragmatic governance and monitoring for AI features that touch learner responses and scoring"
> Reasoning: Candidate builds governance and monitoring infrastructure that AI systems depend on.

**Run 3:** `ai_enabler` ✓
> Quote: "Put in place pragmatic governance and monitoring for AI features that touch learner responses and scoring"
> Reasoning: Candidate builds governance infrastructure that AI features will consume, making them an infrastructure enabler for AI systems.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Become our day-to-day lead for data privacy and school-facing data assurance"
> Reasoning: Candidate owns data quality and assurance practices with direct leadership responsibility.

**Run 2:** `responsibility` ✓
> Quote: "Embed 'instrumentation before shipping' so every major release launches with the right KPIs, tracking, dashboards, and alerts"
> Reasoning: Role owns establishment and implementation of measurement practices as quality gates before deployment.

**Run 3:** `responsibility` ✓
> Quote: "Embed 'instrumentation before shipping' so every major release launches with the right KPIs, tracking, dashboards, and alerts - enabling fast learning, quick diagnosis, and confident iteration"
> Reasoning: Candidate owns establishing measurement and instrumentation as a quality practice responsibility, not just tools in the stack.


### loss_aversion_framing
**Run 1:** `high` ✓
> Quote: "supporting data sharing agreements and DPIAs, and ensuring our practices around children's data are robust and consistently applied"
> Reasoning: Candidate operates in highly regulated domain with children's data requiring compliance frameworks (DPIAs, data agreements).

**Run 2:** `high` ✓
> Quote: "Become our day-to-day lead for data privacy and school-facing data assurance - supporting data sharing agreements and DPIAs, and ensuring our practices around children's data are robust"
> Reasoning: Compliance, privacy regulation, and trustworthiness around sensitive data are framed as primary motivations, not operational reliability.

**Run 3:** `high` ✓
> Quote: "data privacy and school-facing data assurance - supporting data sharing agreements and DPIAs, and ensuring our practices around children's data are robust and consistently applied"
> Reasoning: Regulatory compliance (DPIA), trustworthiness, and children's data protection dominate as primary framing over operational delivery.

