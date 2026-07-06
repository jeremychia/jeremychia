# Trace: 2026-05-11_getyourguide_data-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data Engineer, Traveler Data Engineering — GetYourGuide

**URL:** https://www.linkedin.com/jobs/view/data-engineer-traveler-data-engineering-at-getyourguide-4383493346/
**Location:** Berlin, Berlin, Germany
**Seniority Level:** Associate
**Employment Type:** Full-time

---

## Key Responsibilities

- Build end-to-end data solutions independently: Deliver reliable, high-quality datasets/pipelines
- Serve as a thought partner with Product and Data teams to translate business requirements
- Apply best practices in code quality, data modeling, testing, and monitoring
- Improve what's already in production: Pragmatically refactor and simplify existing pipelines
- Contribute to team planning, code reviews, and knowledge sharing
- Maintain balance between operational responsibilities and new development using team SLOs

---

## Required Qualifications

- 3+ years in a relevant data role with hands-on data engineering experience
- Expertise in SQL & Python, building robust data pipelines and data models
- Experience operating data at scale in warehouses/lakes (Delta, Snowflake, PostgreSQL/MySQL)
- Strong dbt proficiency and Spark familiarity
- Solid understanding of data visualization tools like Looker/Tableau
- Excellent English communication skills (written and verbal)
- Ability to prioritize effectively and manage stakeholders
- Proactive ownership mindset with customer orientation

---

## Preferred / Bonus Skills

- Experience delivering data solutions for marketplace platforms
- Customer journey and metric definition expertise
- Software engineering fundamentals (Java/Scala comfort level)
- AI-first mindset: Uses modern AI tools to boost productivity

---

## Benefits

- Annual personal growth budget and mentorship programs
- Remote work flexibility (30 days annually)
- Hybrid arrangement: three in-office days (Mon, Tue, Thur), two optional remote days
- Quarterly team events and yearly company-wide gatherings
- Monthly transportation and fitness budget
- GetYourGuide activity discounts
- Language reimbursement program
- Health and wellness benefits

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 2 | 2 | 2 | 100% | ✗ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | recruiter | recruiter | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |
| ai_role |  | ai_user | ai_user | ai_user | 100% | ✗ |
| testing_framing |  | tool_listed | responsibility | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities consistently emphasize reliability, quality, testing, and monitoring with no velocity language, establishing rigour as the dominant orientation.

**Run 2:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, monitoring, code quality, and best practices as core expectations, with no velocity-related phrases like 'fast-paced' or 'move fast'.

**Run 3:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit rigour signals (testing, monitoring, best practices, reliable, high-quality) substantially outweigh the single pragmatic refactoring mention, establishing a rigour-dominated orientation.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: As a marketplace data role with no financial reporting, compliance, or regulatory signals, data errors affect business decisions but lack the high-stakes compliance consequences that would elevate risk.

**Run 2:** `moderate` ✓
> Quote: "Deliver reliable, high-quality datasets/pipelines"
> Verified: ✓ found in JD
> Reasoning: GetYourGuide is a marketplace platform with no regulatory or financial reporting language in the JD, placing it in the moderate risk category for operational decision-making.

**Run 3:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The role translates business requirements into data infrastructure without explicit mention of financial reporting, regulatory compliance, or audit impact, indicating business-decision focus rather than high-consequence regulatory work.

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "Product and Data teams"
> Verified: ✓ found in JD
> Reasoning: Only two distinct named teams are explicitly identified as collaboration partners in the responsibilities section.

**Run 2:** `2` ✗
> Quote: "Product and Data teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names two distinct partner groups: Product teams and Data teams.

**Run 3:** `2` ✗
> Quote: "Product; Data teams"
> Verified: ✓ found in JD
> Reasoning: Two distinct named teams are explicitly identified as collaboration partners: Product and Data teams.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: The role operates within established infrastructure with defined SLOs and team processes, indicating a data function beyond its initial build phase but not yet mature at scale.

**Run 2:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: The focus on improving and refactoring existing production systems indicates an established data function with infrastructure already in place, characteristic of a mid-stage team.

**Run 3:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: Existing production infrastructure, established tools (dbt, Spark, Delta, Snowflake), and multiple named data roles imply a growing but not yet fully mature function.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: While most responsibilities use generic boilerplate verbs, specific operational details like SLOs and team practices suggest some hiring manager input alongside recruiter-written generic language.

**Run 2:** `recruiter` ✗
> Quote: "Expertise in SQL & Python, building robust data pipelines and data models"
> Verified: ✓ found in JD
> Reasoning: The required qualifications list tools without specific application context or scale, using generic phrasing that could apply to any data engineer role.

**Run 3:** `recruiter` ✗
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: Responsibilities consist of generic action verbs ('deliver', 'serve as', 'apply', 'contribute to') and boilerplate phrasing with no technical specificity about actual Tuesday-morning work.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Despite partnering with Product teams, responsibilities emphasize data infrastructure quality and operational excellence rather than analytics insights or business impact.

**Run 2:** `internal_data` ✓
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus on maintaining and improving data infrastructure and team practices, with primary audience being the data function itself rather than downstream commercial, product, or finance consumers.

**Run 3:** `internal_data` ✓
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: The emphasis on maintaining operational responsibilities, production reliability (SLOs), and internal data infrastructure indicates the primary audience is the data platform and its consumers.

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Deliver reliable, high-quality datasets/pipelines"
> Verified: ✓ found in JD
> Reasoning: The role executes within scoped direction set by Product and Data teams, with independence referring to delivery approach rather than strategic direction-setting.

**Run 2:** `execution` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The role executes on requirements set by Product and Data teams rather than setting strategy or defining priorities.

**Run 3:** `execution` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: Language emphasizes supporting and assisting other teams with their requirements rather than setting strategic direction for how analytics is delivered.

### ai_role
**Manual:** ``

**Run 1:** `ai_user` ✗
> Quote: "AI-first mindset: Uses modern AI tools to boost productivity"
> Verified: ✓ found in JD
> Reasoning: The preferred skills explicitly frame AI as a personal productivity tool for the candidate to use in their own work, not as infrastructure the role builds or serves.

**Run 2:** `ai_user` ✗
> Quote: "AI-first mindset: Uses modern AI tools to boost productivity"
> Verified: ✓ found in JD
> Reasoning: The preferred skill explicitly expects the candidate to use modern AI tools to accelerate their own productivity.

**Run 3:** `ai_user` ✗
> Quote: "Uses modern AI tools to boost productivity"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use modern AI tools to accelerate their own coding and productivity work.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

### testing_framing
**Manual:** ``

**Run 1:** `tool_listed` ✗
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Testing appears as a practice to apply within best practices rather than as a domain the candidate owns or defines.

**Run 2:** `responsibility` ✗
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Testing is listed in the responsibilities section as an active practice to apply, not just a tool in the tech stack.

**Run 3:** `responsibility` ✗
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Testing appears in the responsibilities section as an active practice the candidate applies and is accountable for, not merely as a tool listed in requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'responsibility', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and SLOs are repeated concerns, but without compliance, regulatory, or data accuracy framing that would signal high loss aversion.

**Run 2:** `moderate` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: The JD mentions SLOs and operational balance, indicating operational reliability is a concern, but this is secondary to the primary framing of building and improving solutions.

**Run 3:** `moderate` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and SLOs are secondary concerns alongside delivery; there is no explicit compliance, regulatory, or stakeholder-trust framing that would indicate high loss aversion.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
