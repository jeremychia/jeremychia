# Trace: 2026-06-25_dashlane_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Dashlane
**URL:** https://job-boards.greenhouse.io/dashlane/jobs/7988501

**Company:** Dashlane
**Location:** Lisbon, Portugal (Hybrid) — in-office Mondays, Tuesdays, Thursdays; remote Wednesdays and Fridays
**Salary:** Not stated
**ATS:** greenhouse
**Job ID:** 7988501

---

## Full JD

Analytics Engineer
Company: Dashlane
Location: Lisbon, Portugal (Hybrid) — in-office Mondays, Tuesdays, Thursdays; remote Wednesdays and Fridays

About Dashlane:
Dashlane focuses on credential security for businesses and employees. The organization serves millions of consumers and over 25,000 brands globally, including Michelin, Air France, and Forrester. Founded in Paris, the company operates offices in New York and Lisbon with more than 300 employees worldwide.

Role Overview:
This position involves joining the Data & Analytics team as a strategic partner between technical modeling and business decisions. The Analytics Engineer will shift the team from reactive support toward proactive strategy, addressing complex data architecture while enabling organizational self-service capabilities.

Key Responsibilities:
- Design, build, test, and maintain end-to-end data models within dbt-powered systems
- Transform messy datasets into clean, intuitive models serving as single sources of truth
- Partner consultatively with Product, Go-to-Market, and business teams on data-driven insights
- Guide stakeholders toward scalable self-serve solutions rather than ad-hoc requests
- Implement AI data agents and automation for reporting and alerting systems
- Establish data governance, quality testing, and mentoring for junior team members

Requirements:
- 3+ years in Analytics Engineering or equivalent roles
- Expert-level SQL and dbt proficiency with production experience
- Strong B2B SaaS business knowledge (ARR, NRR, churn, product-led growth)
- Consultative stakeholder management abilities
- Fluent with AI coding platforms such as Claude Code
- Autonomous working style with curiosity for complex data challenges
- Fluent English (verbal and written)

Tech Stack:
dbt, SQL, Python, AWS (Redshift, S3, Lambda, Kinesis, Glue), Omni, Airflow, GitLab, Claude Code

Benefits:
- Flex Benefits allocation
- Health insurance coverage
- 5 additional vacation days annually plus birthday off
- Quarterly well-being days
- Up to 20 weeks paid parental leave
- Mental health services through Spring Health
- Team events and social activities

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
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | mixed | internal_data | internal_data | 33% |
| autonomy_level | mixed | mixed | mixed | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Establish data governance, quality testing, and mentoring for junior team members"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, governance, and quality as core expectations rather than speed or iteration pace.

**Run 2:** `rigour`
> Quote: "Establish data governance, quality testing, and mentoring for junior team members"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, quality testing, and reliability as core expectations with no counterbalancing velocity signals present.

**Run 3:** `rigour`
> Quote: "Establish data governance, quality testing, and mentoring for junior team members"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly emphasizes data governance and quality testing as core responsibilities with zero velocity signals, indicating a rigour-first approach.

### domain_risk

**Run 1:** `moderate`
> Quote: "Strong B2B SaaS business knowledge (ARR, NRR, churn, product-led growth)"
> Verified: ✓ found in JD
> Reasoning: The role supports business decision-making through SaaS metrics without explicit regulatory, compliance, or financial reporting language.

**Run 2:** `moderate`
> Quote: "Partner consultatively with Product, Go-to-Market, and business teams on data-driven insights"
> Verified: ✓ found in JD
> Reasoning: The primary audience is business teams making operational decisions rather than financial reporting or regulatory compliance stakeholders.

**Run 3:** `moderate`
> Quote: "Partner consultatively with Product, Go-to-Market, and business teams on data-driven insights"
> Verified: ✓ found in JD
> Reasoning: This is a B2B SaaS analytics role supporting business intelligence and GTM decisions without explicit financial reporting, compliance, or regulatory language.

### collaboration_width

**Run 1:** `2`
> Quote: "Product, Go-to-Market"
> Verified: ✓ found in JD
> Reasoning: Two named functions are explicitly listed: Product and Go-to-Market; 'business teams' is too generic to count as a distinct named team.

**Run 2:** `2`
> Quote: "Product; Go-to-Market"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two named functions explicitly mentioned as collaboration partners; 'business teams' is generic and does not count.

**Run 3:** `2`
> Quote: "Product; Go-to-Market"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names Product and Go-to-Market as distinct partnership functions; 'business teams' is generic and does not count as a named function.

### data_team_maturity

**Run 1:** `mid`
> Quote: "shift the team from reactive support toward proactive strategy, addressing complex data architecture while enabling organizational self-serve capabilities"
> Verified: ⚠ NOT found verbatim
> Reasoning: The team has established infrastructure (dbt, named tools) and existing work but is evolving from reactive to proactive, with junior members to mentor.

**Run 2:** `mid`
> Quote: "Transform messy datasets into clean, intuitive models serving as single sources of truth"
> Verified: ✓ found in JD
> Reasoning: References to existing messy data and established dbt infrastructure indicate a data function that exists with some scale but requires improvement, not greenfield nor mature at scale.

**Run 3:** `mid`
> Quote: "shift the team from reactive support toward proactive strategy"
> Verified: ✓ found in JD
> Reasoning: The organization has existing infrastructure and team structure with junior members to mentor, but is actively evolving its analytics approach, indicating mid-stage maturity.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Design, build, test, and maintain end-to-end data models within dbt-powered systems"
> Verified: ✓ found in JD
> Reasoning: The technical specificity—named tool (dbt) with production context, detailed tech stack (AWS Redshift, S3, Lambda, Kinesis, Glue, Omni, Airflow)—indicates hands-on expertise.

**Run 2:** `hiring_manager`
> Quote: "Design, build, test, and maintain end-to-end data models within dbt-powered systems"
> Verified: ✓ found in JD
> Reasoning: The specific tool application context (dbt for end-to-end models) and concrete problem statement reflect technical depth only someone performing the job would articulate.

**Run 3:** `hiring_manager`
> Quote: "Design, build, test, and maintain end-to-end data models within dbt-powered systems"
> Verified: ✓ found in JD
> Reasoning: This shows technical specificity (dbt context, end-to-end lifecycle) and hands-on understanding of the work that only comes from someone familiar with the actual role.

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "Partner consultatively with Product, Go-to-Market, and business teams on data-driven insights"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves Product (product stakeholder) and Go-to-Market (commercial stakeholder), plus enables self-serve for the data team (internal_data stakeholder).

**Run 2:** `internal_data`
> Quote: "enabling organizational self-service capabilities"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building and improving the analytics data platform for internal self-serve consumption, with Product and Go-to-Market as downstream consumers of that infrastructure.

**Run 3:** `internal_data`
> Quote: "Guide stakeholders toward scalable self-serve solutions rather than ad-hoc requests"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building self-serve analytics infrastructure and data governance to enable internal data platform consumers, reducing ad-hoc dependency.

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'internal_data']

### autonomy_level

**Run 1:** `mixed`
> Quote: "shift the team from reactive support toward proactive strategy, addressing complex data architecture while enabling organizational self-serve capabilities"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic direction-setting ('shift toward proactive strategy', 'establish governance') with execution-focused responsibilities (design, build, maintain models).

**Run 2:** `mixed`
> Quote: "shift the team from reactive support toward proactive strategy, addressing complex data architecture while enabling organizational self-service capabilities"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting (shifting team orientation, designing architecture) with execution on technical delivery (building models, implementing automation, maintaining systems).

**Run 3:** `mixed`
> Quote: "shift the team from reactive support toward proactive strategy"
> Verified: ✓ found in JD
> Reasoning: The role is responsible for driving strategic organizational change in analytics delivery while also executing core technical work (design, build, maintain, implement).
