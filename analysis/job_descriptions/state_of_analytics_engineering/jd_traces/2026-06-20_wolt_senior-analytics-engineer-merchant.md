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
| jd_authorship | hiring_manager | hiring_manager | mixed | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The lead responsibility explicitly prioritizes quality and understanding business needs rather than speed or iteration, with no signal phrases around fast-paced delivery or rapid velocity.

**Run 2:** `rigour` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality, dependency control, orchestration, and governance throughout, with no velocity-focused language present.

**Run 3:** `rigour` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The opening responsibility emphasizes quality as the primary value, with no counterbalancing velocity language like fast-paced, iteration, or rapid delivery.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Working on centrally maintained data integrations and data pipelines"
> Verified: ✓ found in JD
> Reasoning: Merchant analytics affects business operations and revenue relationships but contains no explicit financial reporting, compliance, or regulatory language that would indicate high risk.

**Run 2:** `moderate` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: The role focuses on operational reporting and business intelligence without explicit mention of financial reporting, regulatory compliance, or other high-risk consequences.

**Run 3:** `moderate` ✓
> Quote: "Enhancing reporting and metrics quality as a whole, from understanding the needs of the business to providing easily understandable and actionable data"
> Verified: ✓ found in JD
> Reasoning: This is business intelligence analytics for a marketplace's merchant domain, not financial reporting or regulatory compliance, placing it in the moderate risk tier typical of e-commerce platforms.

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: The JD references generic 'the business' and 'the domain' without naming specific partner teams or functions such as Finance, Product, Engineering, or Sales.

**Run 2:** `0` ✗
> Quote: "None identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: No named partner teams or functions are explicitly mentioned in the JD.

**Run 3:** `0` ✗
> Quote: "Collaborative team environment with mentorship opportunities"
> Verified: ✓ found in JD
> Reasoning: No specific named partner teams (Finance, Product, Engineering, etc.) are mentioned; the JD refers only generically to 'the business' and collaboration broadly.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Working on centrally maintained data integrations and data pipelines"
> Verified: ✓ found in JD
> Reasoning: The existence of centrally maintained infrastructure and the requirement to mentor junior team members indicates an established, growing data function rather than early-stage or fully mature.

**Run 2:** `mid` ✓
> Quote: "Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagster, GitHub)"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure and named tools in responsibilities, plus multiple team members to mentor, suggesting an established but growing data function.

**Run 3:** `mid` ✓
> Quote: "Develop a self-service data modelling strategy"
> Verified: ✓ found in JD
> Reasoning: The team has established tooling (Snowflake, Airflow, dbt, Looker) and is actively evolving it; mentoring junior members implies growth beyond early stage but not yet multiple specialized sub-teams.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Managing data integrations, pipelines, models, and dashboards using modern tools (Snowflake, SQL, Looker, Airflow, Dagster, GitHub)"
> Verified: ✓ found in JD
> Reasoning: The specific enumeration of tools paired with technical concepts like 'dependency control and orchestration' demonstrates hands-on knowledge of the actual role rather than generic boilerplate language.

**Run 2:** `mixed` ✗
> Quote: "Design and implement complex data pipelines with dependency control and orchestration"
> Verified: ✓ found in JD
> Reasoning: The specific technical language around 'dependency control and orchestration' suggests hiring manager input, but generic responsibility framing indicates recruiter involvement.

**Run 3:** `mixed` ✗
> Quote: "Design and implement complex data pipelines with dependency control and orchestration"
> Verified: ✓ found in JD
> Reasoning: Technical specificity around pipeline architecture and orchestration indicates hiring manager input, but other responsibilities use generic boilerplate verbs like 'enhancing quality' and 'increase data literacy' typical of recruiter writing.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']
