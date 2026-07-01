# Trace: 2026-06-20_wolt_senior-analytics-engineer-merchant

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer, Merchant — Wolt

**URL:** https://job-boards.greenhouse.io/wolt/jobs/8006892
**Location:** Berlin, Germany; Helsinki, Finland; Stockholm, Sweden
**Salary:** Not listed

---

## Key Responsibilities

- Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data
- Working on centrally maintained data integrations and data pipelines
- Design and implement complex data pipelines with dependency control and orchestration
- Develop a self-service data modelling strategy
- Increase data literacy across the domain through training and documentation
- Lead, mentor, and guide more junior team members
- Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagster, GitHub)

---

## Required Qualifications

- 5+ years of experience as an Analytics Engineer or BI Developer
- Strong hands-on experience with data integrations, data pipelines, data models, metric development, and dashboards
- Proficiency in Snowflake, SQL, Airflow, DBT, and visualization tools (Looker, Tableau, or Power BI)
- Advanced SQL skills and ability to write optimized queries for large data sets
- Strong business acumen and product-oriented thinking

---

## Preferred / Bonus Skills

- Experience with orchestration tools (Airflow, Dagster)
- Familiarity with in-house ETL systems
- Exposure to complex geolocational and temporal data challenges

---

## Benefits

- Hybrid, at the office, or remote within the location (Berlin, Helsinki, or Stockholm)
- Exposure to complex geolocational and temporal data challenges
- Opportunity to create significant impact
- Collaborative team environment with mentorship opportunities
- Inclusive company culture emphasising ownership and continuous learning

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | hiring_manager | mixed | 33% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | mixed | mixed | mixed | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The first responsibility explicitly prioritizes quality enhancement with no speed or iteration language present throughout the JD.

**Run 2:** `rigour` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasise data quality, clarity, training, documentation, and orchestration control—core rigour signals—with no velocity language present.

**Run 3:** `rigour` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes quality, accessibility, and understanding stakeholder needs as primary responsibilities with no mention of speed, shipping, or iteration velocity.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Working on centrally maintained data integrations and data pipelines"
> Verified: ✓ found in JD
> Reasoning: Wolt is a marketplace/SaaS platform without explicit financial reporting, compliance, or regulatory language in the JD, placing it in the moderate risk tier.

**Run 2:** `moderate` ✓
> Quote: "from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The role supports merchant business decisions but lacks explicit financial reporting, regulatory, or compliance language that would elevate risk to high.

**Run 3:** `moderate` ✓
> Quote: "Managing data integrations, pipelines, models, and dashboards using modern tools"
> Verified: ✓ found in JD
> Reasoning: This is standard SaaS/marketplace business intelligence work affecting business decisions but not financial reporting, regulatory compliance, or mission-critical public-facing products.

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams or functions (Finance, Product, Engineering, etc.) are identified in the responsibilities.

**Run 2:** `0` ✗
> Quote: "Collaborative team environment with mentorship opportunities"
> Verified: ✓ found in JD
> Reasoning: The JD references 'the business' and internal mentorship but does not name any distinct partner functions such as Finance, Product, Engineering, or Sales.

**Run 3:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: While the JD implies cross-functional work (understanding business needs, increasing data literacy), no specific teams like Finance, Product, Engineering, or other named functions are explicitly identified.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Working on centrally maintained data integrations and data pipelines"
> Verified: ✓ found in JD
> Reasoning: The phrase 'centrally maintained' indicates existing infrastructure beyond startup phase, reinforced by multiple named tools (Snowflake, Airflow, Dagster, dbt) used in specific contexts.

**Run 2:** `mid` ✓
> Quote: "Develop a self-serve data modelling strategy"
> Verified: ⚠ NOT found verbatim
> Reasoning: The emphasis on developing and extending an existing self-serve capability, managing established tools (Snowflake, Airflow, dbt), and mentoring junior staff indicates a team with infrastructure and multiple members but still scaling.

**Run 3:** `mid` ✓
> Quote: "Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagster, GitHub)"
> Verified: ✓ found in JD
> Reasoning: Named tools with specific application context in responsibilities, a team structure with seniors mentoring juniors, and references to centrally maintained systems signal a growing mid-stage data function.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Design and implement complex data pipelines with dependency control and orchestration"
> Verified: ✓ found in JD
> Reasoning: Specific technical methodology and precise tool stack mixed with generic narrative language about understanding business needs.

**Run 2:** `hiring_manager` ✓
> Quote: "Design and implement complex data pipelines with dependency control and orchestration"
> Verified: ✓ found in JD
> Reasoning: The specific technical methodology (dependency control, orchestration) and named tools with context signal someone who has done this work, not generic action verbs.

**Run 3:** `mixed` ✗
> Quote: "Design and implement complex data pipelines with dependency control and orchestration"
> Verified: ✓ found in JD
> Reasoning: Some technically specific concerns (dependency control, orchestration) and named tools demonstrate hiring manager input, but generic phrases like mentorship and business acumen suggest recruiter involvement.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Develop a self-service data modelling strategy"
> Verified: ✓ found in JD
> Reasoning: The role's core mission—building self-serve infrastructure, increasing data literacy, and managing the analytics stack—serves data consumers and the data function itself.

**Run 2:** `internal_data` ✗
> Quote: "Develop a self-serve data modelling strategy"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities prioritise building platform infrastructure, strategy, data literacy, and team development—serving analytics consumers and the data function—over serving external commercial or product teams directly.

**Run 3:** `internal_data` ✗
> Quote: "Develop a self-service data modelling strategy"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is building analytics infrastructure and data accessibility for internal data consumers rather than serving commercial, product, or finance teams.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Lead, mentor, and guide more junior team members"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting (develop strategy, mentor, increase literacy) with execution responsibilities (design, implement, manage pipelines).

**Run 2:** `mixed` ✗
> Quote: "Develop a self-serve data modelling strategy"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role genuinely combines strategic direction-setting (developing strategy, mentoring junior staff, increasing data literacy) with execution of pipelines and tool management.

**Run 3:** `mixed` ✗
> Quote: "Develop a self-service data modelling strategy"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic responsibilities (developing strategy, leading and mentoring junior team members) with execution responsibilities (implementing pipelines, managing systems).

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

### ai_role
**Run 1:** `none` ✓
> Quote: "Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagster, GitHub)"
> Reasoning: Tech stack consists entirely of traditional data tools with no AI-specific capabilities or tools mentioned.

**Run 2:** `none` ✓
> Quote: "None identified"
> Reasoning: No AI tools, coding assistants, or AI infrastructure building mentioned in role requirements.

**Run 3:** `none` ✓
> Quote: "Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagster, GitHub)"
> Reasoning: Standard data engineering tech stack with no AI tools or infrastructure requirements.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Enhancing reporting and metrics quality as a whole"
> Reasoning: Direct ownership framing with 'enhancing' action verb paired with explicit quality accountability.

**Run 2:** `responsibility` ✓
> Quote: "Enhancing reporting and metrics quality as a whole"
> Reasoning: Candidate owns quality practice through active enhancement of reporting and metrics across the organization.

**Run 3:** `absent` ✗
> Quote: "None identified"
> Reasoning: No testing responsibility verbs, testing tools, or quality ownership language present.

⚠ **LLM inconsistency**: runs gave ['responsibility', 'responsibility', 'absent']

### loss_aversion_framing
**Run 1:** `none` ✓
> Quote: "Understanding the needs of the business to providing easily understandable and actionable data"
> Reasoning: Positive value-delivery framing with no compliance, regulatory, or incident-prevention language.

**Run 2:** `none` ✓
> Quote: "Understanding the needs of the business to providing easily understandable and actionable data"
> Reasoning: Role framed around delivery of business value and clarity, not operational reliability fears or compliance constraints.

**Run 3:** `none` ✓
> Quote: "Understanding the needs of the business to providing easily understandable and actionable data"
> Reasoning: Framed around delivery and business value with no compliance, reliability, or risk-mitigation signals.

