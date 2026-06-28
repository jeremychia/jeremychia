# Trace: 2026-06-27_dashlane_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Dashlane
**URL:** https://job-boards.greenhouse.io/dashlane/jobs/7988501

**Location:** Lisbon, Portugal (Hybrid)
**Date Posted:** 2026-06-27

---

Analytics Engineer

Dashlane — Lisbon, Portugal (Hybrid)

About Dashlane

Dashlane is a credential security company serving millions of consumers and 25,000+ brands across the globe. With 300+ employees across offices in Paris, New York, and Lisbon, Dashlane's mission is to make credential security effortless for everyone.

About the Role

As an Analytics Engineer at Dashlane, you will play a pivotal role in transforming raw data into strategic business value. You'll work at the intersection of data engineering and business intelligence, owning the data models that power decision-making across the company. This is an opportunity to work on meaningful problems, partnering directly with product and go-to-market teams, and driving self-service analytics adoption across the organisation.

Responsibilities

Data Modeling: Design, build, test, and own end-to-end data models within our dbt-powered "Unified Data Model." You will ensure models are reliable, well-documented, and aligned with business logic.

Business Partnership: Act as a consultant to product and go-to-market teams, moving from reactive data support to proactive strategic insights. You will help teams understand and leverage data effectively.

Self-Service Analytics: Drive adoption of self-serve solutions in Omni while mentoring stakeholders to become more data-literate and independent in their analytics workflows.

AI & Automation: Implement AI data agents and the necessary underlying foundations to automate reporting and alerting, pushing the frontier of what analytics engineering looks like in an AI-first world.

Data Governance: Establish quality tests and governance practices while mentoring junior engineers in analytics engineering best practices.

Requirements

- 3+ years of experience in Analytics Engineering or an equivalent role
- Expert-level SQL and dbt proficiency with production experience
- Strong understanding of B2B SaaS metrics: ARR, NRR, churn, PLG
- Consultative stakeholder management abilities — you know how to translate business questions into data solutions
- You are fluent with AI coding platforms such as Claude Code
- Autonomous work style with curiosity for complex data challenges
- Fluent English (verbal and written)

Tech Stack

dbt, SQL, Python, AWS (Redshift, S3, Lambda, Kinesis, Glue), Omni, Airflow, GitLab, Claude Code

Benefits

- Flex benefits (monthly allowance to spend on what matters to you)
- Full health insurance coverage
- Extra vacation days
- Enhanced parental leave: 20 weeks fully paid for all parents
- Mental health support through Spring Health
- Donation matching for charitable contributions
- Quarterly company wellness days
- Team events and offsites

Work Arrangement

Hybrid schedule: in-office on Mondays, Tuesdays, and Thursdays. Flexible Wednesdays and Fridays for focused work.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | mixed | 33% |
| stakeholder_orientation | mixed | mixed | mixed | 100% |
| autonomy_level | mixed | mixed | strategic | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Design, build, test, and own end-to-end data models within our dbt-powered "Unified Data Model." You will ensure models are reliable, well-documented, and aligned with business logic."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (testing, reliability, documentation, quality tests, governance) with zero velocity language (no "fast-paced," "ship quickly," or "rapid") indicate rigour-focused orientation.

**Run 2:** `rigour`
> Quote: "Establish quality tests and governance practices while mentoring junior engineers in analytics engineering best practices."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, quality, governance, and best practices over speed or iteration.

**Run 3:** `rigour`
> Quote: "You will ensure models are reliable, well-documented, and aligned with business logic."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reliability, documentation, testing, and governance as core expectations, with no velocity-oriented language present.

### domain_risk

**Run 1:** `moderate`
> Quote: "Strong understanding of B2B SaaS metrics: ARR, NRR, churn, PLG"
> Verified: ✓ found in JD
> Reasoning: B2B SaaS metrics are business-critical for decision-making but lack explicit financial-reporting, compliance, or regulatory language, indicating moderate domain risk.

**Run 2:** `moderate`
> Quote: "Act as a consultant to product and go-to-market teams, moving from reactive data support to proactive strategic insights."
> Verified: ✓ found in JD
> Reasoning: Data supports business decisions for product and GTM but lacks explicit financial reporting or regulatory compliance framing despite fintech sector.

**Run 3:** `moderate`
> Quote: "Strong understanding of B2B SaaS metrics: ARR, NRR, churn, PLG"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes SaaS revenue and customer health metrics central to business intelligence rather than regulatory or financial reporting compliance.

### collaboration_width

**Run 1:** `2`
> Quote: "product and go-to-market teams"
> Verified: ✓ found in JD
> Reasoning: Two distinct named functions explicitly identified in the responsibilities section.

**Run 2:** `2`
> Quote: "product and go-to-market teams"
> Verified: ✓ found in JD
> Reasoning: Two distinct named functions identified as primary collaboration partners: Product and Go-to-market.

**Run 3:** `2`
> Quote: "partnering directly with product and go-to-market teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names product and go-to-market teams as collaboration partners, totaling two distinct named functions.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Drive adoption of self-serve solutions in Omni while mentoring stakeholders to become more data-literate and independent in their analytics workflows."
> Verified: ✓ found in JD
> Reasoning: Named existing infrastructure (Omni, dbt Unified Data Model) and mentoring others signals an established data function in growth phase.

**Run 2:** `mid`
> Quote: "dbt-powered 'Unified Data Model'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Named tools with existing infrastructure, multiple engineers implied (mentoring junior engineers), and scaling adoption efforts indicate established team in growth phase.

**Run 3:** `mid`
> Quote: "Drive adoption of self-serve solutions in Omni while mentoring junior engineers to become more data-literate and independent in their analytics workflows."
> Verified: ⚠ NOT found verbatim
> Reasoning: The presence of named tools in responsibilities (dbt, Omni), existing data models, and the need to mentor junior engineers indicate a data function that exists and is growing significantly.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Design, build, test, and own end-to-end data models within our dbt-powered "Unified Data Model." You will ensure models are reliable, well-documented, and aligned with business logic."
> Verified: ✓ found in JD
> Reasoning: Named tools with specific application context (dbt for unified model) demonstrate technical specificity only a practitioner would write, but consulting and mentoring language is generic.

**Run 2:** `hiring_manager`
> Quote: "Design, build, test, and own end-to-end data models within our dbt-powered 'Unified Data Model.'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical details (dbt, Omni, B2B SaaS metrics including ARR/NRR/churn/PLG) demonstrate hiring manager-level understanding of the role.

**Run 3:** `mixed`
> Quote: "Design, build, test, and own end-to-end data models within our dbt-powered 'Unified Data Model.'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines technical specificity about tools (dbt, Omni) and context (Unified Data Model) with generic boilerplate language about stakeholder consulting.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "Act as a consultant to product and go-to-market teams, moving from reactive data support to proactive strategic insights."
> Verified: ✓ found in JD
> Reasoning: Both product and go-to-market (commercial) teams are named as primary stakeholders with equal emphasis in responsibilities.

**Run 2:** `mixed`
> Quote: "Act as a consultant to product and go-to-market teams, moving from reactive data support to proactive strategic insights."
> Verified: ✓ found in JD
> Reasoning: Both product and commercial (GTM) teams are equally named and emphasized as primary stakeholders throughout the responsibilities.

**Run 3:** `mixed`
> Quote: "partnering directly with product and go-to-market teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names both product and go-to-market teams as primary partners with comparable emphasis, plus required B2B SaaS metrics knowledge, indicating genuinely split stakeholder orientation.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Design, build, test, and own end-to-end data models within our dbt-powered "Unified Data Model." Act as a consultant to product and go-to-market teams, moving from reactive data support to proactive strategic insights."
> Verified: ⚠ NOT found verbatim
> Reasoning: Strategic ownership of data models, governance, and analytics approach shift combined with execution through consulting to business teams indicates mixed autonomy.

**Run 2:** `mixed`
> Quote: "owning the data models that power decision-making across the company"
> Verified: ✓ found in JD
> Reasoning: Role combines strategic ownership of the data domain (own, establish, drive) with execution in service of product and GTM teams (consultant, support).

**Run 3:** `strategic`
> Quote: "owning the data models that power decision-making across the company"
> Verified: ✓ found in JD
> Reasoning: The repeated use of 'own' and 'owning' plus framing as a consultant who 'drives adoption' and 'establishes governance practices' indicates strategic direction-setting rather than execution of others' priorities.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'strategic']
