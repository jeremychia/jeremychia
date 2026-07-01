# Trace: 2026-04-28_seven-senders_senior-bi-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Senior Business Intelligence Analyst (f/m/x) — Seven Senders

**URL:** https://www.linkedin.com/jobs/view/4406635718
**Location:** Berlin, Berlin, Germany
**Employment Type:** Full-time

---

## Key Responsibilities

- Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks
- Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets
- Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks
- Support the growth of junior analysts through code reviews, coaching, and documentation
- Explain complex technical concepts to non-technical audiences
- Own the data pipeline from architecting dbt models to enabling self-service in Looker
- Act as translator between engineering and business stakeholders
- Provide mentorship and maintain data culture quality

---

## Required Qualifications

- 4+ years of experience in Data Analytics, BI, or Data Science
- Proven experience building and maintaining scalable dbt or similar framework projects
- Deep understanding of dependency management, reusability, and runtime optimization
- Expert-Level SQL & Optimization producing efficient, production-grade SQL
- Experience in Looker (or similar tools) from backend development to storytelling
- Ability to break down ambiguous problems and take full ownership from definition to delivery

---

## Preferred / Bonus Skills

- None explicitly listed separately from requirements

---

## Benefits

- Hybrid work model with flexible remote setup and working hours
- Up to 2 months remote work annually from anywhere
- Company lunches twice monthly
- Corporate benefits platform
- German language courses
- Climate-neutral operations initiative
- Regular team events and company-wide celebrations

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 2 | 1 | 1 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | execution | execution | strategic | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes production-grade quality, performance optimization, and scaling without mentioning speed or rapid delivery.

**Run 2:** `rigour` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Emphasis on testing frameworks, advanced technical tooling, and code quality signals rigour over velocity.

**Run 3:** `rigour` ✓
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing frameworks, code reviews, and quality maintenance as core responsibilities with no velocity language present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-serve in Looker"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role supports business decision-making through analytics infrastructure but includes no language about financial reporting, compliance, or regulatory consequences.

**Run 2:** `moderate` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-serve in Looker"
> Verified: ⚠ NOT found verbatim
> Reasoning: Standard BI/analytics infrastructure work without explicit financial reporting, compliance, or regulatory language indicates moderate operational risk.

**Run 3:** `moderate` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: The role focuses on analytics infrastructure and tool enablement rather than financial reporting, compliance, or regulatory requirements, typical of moderate-risk BI roles.

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "junior analysts; engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names two distinct teams: analysts as a cohort and engineering as a named function.

**Run 2:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only 'engineering' is explicitly named as a collaboration partner; 'business stakeholders' is generic and does not count.

**Run 3:** `1` ✗
> Quote: "Act as translator between engineering and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'engineering' is explicitly named as a distinct collaboration partner; 'business stakeholders' is too vague per the decision rules to count.

⚠ **Disagreement**: manual=`3` vs LLM majority=`1`

⚠ **LLM inconsistency**: runs gave ['2', '1', '1']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: The existence of junior analysts and growth language indicates an established team in expansion phase with existing infrastructure.

**Run 2:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: Existing junior analysts and named tools (dbt, Looker) in responsibilities indicate established mid-stage team with infrastructure in place.

**Run 3:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: The presence of junior analysts and named tools in active use (dbt, Looker) indicate an established function with multiple roles, but without the scale or sub-team specialization of a mature team.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks; Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains specific technical patterns (Jinja, macros, testing frameworks, multi-billion row optimization) that indicate hiring manager domain expertise rather than generic recruiter language.

**Run 2:** `hiring_manager` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Specific technical context about dbt with Jinja, macros, testing, and multi-billion row datasets indicates hands-on domain expertise in authorship.

**Run 3:** `hiring_manager` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: The specificity about advanced Jinja, macros, and testing frameworks demonstrates hands-on technical understanding of what this role actually does day-to-day, not generic boilerplate.

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Own the data pipeline from architecting dbt models to enabling self-serve in Looker"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary focus is building data infrastructure and enabling other data consumers (junior analysts, self-serve users) rather than serving commercial, product, or finance functions.

**Run 2:** `internal_data` ✗
> Quote: "Own the data pipeline from architecting dbt models to enabling self-serve in Looker"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary emphasis on data infrastructure, self-serve analytics enablement, and serving internal data consumers indicates service to the data function.

**Run 3:** `internal_data` ✗
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building analytics infrastructure and self-serve capabilities for internal data consumers rather than serving GTM, product, or finance teams.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Verified: ✓ found in JD
> Reasoning: The role has significant autonomy over individual projects and technical domain decisions but does not set overall analytics strategy or organizational direction.

**Run 2:** `execution` ✗
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: While the role has independence within technical domains, 'deliver' frames it as executing on scoped analytical work rather than setting overall analytics strategy.

**Run 3:** `strategic` ✗
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Verified: ✓ found in JD
> Reasoning: The verbs 'independently lead' and 'own' indicate the role defines its own direction and architecture rather than executing against externally set priorities.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'strategic']

### ai_role
**Run 1:** `none` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Reasoning: No mention of AI tools, GenAI development, or AI-ready infrastructure.

**Run 2:** `none` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Reasoning: No mention of AI tools or AI infrastructure building.

**Run 3:** `none` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Reasoning: No mention of AI tools, GenAI infrastructure, or AI-assisted development; standard dbt and SQL work.


### testing_framing
**Run 1:** `tool_listed` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Reasoning: Testing frameworks mentioned as part of technical toolkit but without explicit ownership of quality practice.

**Run 2:** `tool_listed` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Reasoning: Testing frameworks mentioned as part of the toolkit but without ownership verbs like own, ensure, or define.

**Run 3:** `tool_listed` ✓
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Reasoning: Testing frameworks mentioned in the tech stack without explicit ownership verbs like 'own', 'ensure', or 'define'.


### loss_aversion_framing
**Run 1:** `none` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Reasoning: Framed around performance delivery without operational reliability (SLOs, incidents) or compliance/trust concerns.

**Run 2:** `none` ✓
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Reasoning: JD focuses on delivery and capability building with no compliance, SLO, or trust-dominance framing.

**Run 3:** `none` ✓
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Reasoning: Pure delivery framing focused on task execution and performance; no language about incidents, SLOs, compliance, or data trustworthiness.

