# Trace: 2026-07-02_xomnia_data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data Analytics Engineer — Xomnia

**URL:** https://careers.xomnia.com/o/data-analytics-engineer
**Location:** Amsterdam, Netherlands
**Date Posted:** 2026-07-02
**Salary:** 3,800–6,200 EUR

---

# Data Analytics Engineer at Xomnia

Location: Amsterdam, Noord-Holland, Netherlands (Hybrid)
Salary: EUR 3,800 - EUR 6,200 per month (40 hours, excluding vacation allowance)

## Key Responsibilities
The role involves building scalable data models and pipelines. Professionals will optimize data workflows for performance, usability, and cost efficiency and work with business stakeholders to understand analytics needs. Additional duties include developing self-service platforms, collaborating with data engineers, translating insights into dashboards, and contributing to internal knowledge sharing.

## Required Qualifications
Candidates need 3+ years of experience in a similar role plus a Bachelor's or Master's degree with strong IT/ICT components. Essential skills include SQL, Python/Spark proficiency, and hands-on experience with DBT and cloud data warehouses (e.g. Snowflake, BigQuery, Databricks).

Additional requirements: strong data modeling expertise, direct client communication abilities, fluent in Dutch and English (required for this role), and collaborative mindset.

## Tech Stack & Tools
DBT, Databricks, Snowflake, BigQuery, Azure Data Factory, Power BI, Tableau

## Benefits
EUR 5,000 annual development budget, 25 vacation days, flexible working arrangements, pension, company trips, and Stock Appreciation Rights opportunities.

Contact: ezra.lammers@xomnia.com

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 1 | 1 | 1 | 1 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | recruiter | recruiter | mixed | 33% | ✗ |
| stakeholder_orientation | commercial | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "building scalable data models and pipelines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize architectural quality, scalability, and optimization over speed or iteration, with no velocity language present.

**Run 2:** `rigour` ✗
> Quote: "optimize data workflows for performance, usability, and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes optimization for performance and cost efficiency, signaling operational excellence and quality rather than velocity.

**Run 3:** `rigour` ✗
> Quote: "building scalable data models and pipelines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize scalability and optimization for performance and cost efficiency, with no velocity-oriented language like 'fast-paced' or 'ship quickly'.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "work with business stakeholders to understand analytics needs"
> Verified: ✓ found in JD
> Reasoning: The role supports business decision-making without explicit financial reporting, compliance, or regulatory language that would signal high risk.

**Run 2:** `moderate` ✓
> Quote: "work with business stakeholders to understand analytics needs"
> Verified: ✓ found in JD
> Reasoning: The JD describes generic analytics and data modeling work for business stakeholders without financial reporting, regulatory, or compliance language, indicating moderate domain risk.

**Run 3:** `moderate` ✓
> Quote: "translating insights into dashboards"
> Verified: ✓ found in JD
> Reasoning: The focus on operational dashboards and business analytics indicates standard business intelligence work where errors affect decisions but not financial reporting or compliance.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "collaborating with data engineers"
> Verified: ✓ found in JD
> Reasoning: Only one named partner team (data engineers) is explicitly identified; business stakeholders is generic and does not count.

**Run 2:** `1` ✓
> Quote: "collaborating with data engineers"
> Verified: ✓ found in JD
> Reasoning: Only one distinct named partner team (data engineers) is explicitly identified in the responsibilities section.

**Run 3:** `1` ✓
> Quote: "collaborating with data engineers"
> Verified: ✓ found in JD
> Reasoning: Only 'data engineers' is an explicitly named partner team; 'business stakeholders' is too generic per the classification rules.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "developing self-service platforms"
> Verified: ✓ found in JD
> Reasoning: The role builds on existing data infrastructure with enhancement work (self-serve platforms) rather than establishing foundational infrastructure from zero.

**Run 2:** `mid` ✓
> Quote: "collaborating with data engineers"
> Verified: ✓ found in JD
> Reasoning: The JD references existing data engineers and implies a data function building self-serve infrastructure, suggesting a team at growth/mid stage rather than early-stage greenfield.

**Run 3:** `mid` ✓
> Quote: "developing self-service platforms"
> Verified: ✓ found in JD
> Reasoning: The presence of established tools (DBT, Snowflake, Databricks) and platform-building work suggests a team beyond early stage but not yet large-scale maturity.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `recruiter` ✗
> Quote: "translating insights into dashboards"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs and boilerplate phrasing without specific technical context, scale, or methodological depth that would indicate hiring manager authorship.

**Run 2:** `recruiter` ✗
> Quote: "work with business stakeholders to understand analytics needs"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section consists entirely of generic, boilerplate action verbs without technical specificity, scale context, or methodology that would indicate a hiring manager's input.

**Run 3:** `mixed` ✓
> Quote: "hands-on experience with DBT and cloud data warehouses (e.g. Snowflake, BigQuery, Databricks)"
> Verified: ✓ found in JD
> Reasoning: Some technical specificity about tools appears in requirements, but responsibilities rely heavily on generic boilerplate like 'work with business stakeholders' and 'collaborating with data engineers'.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'recruiter', 'mixed']

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `internal_data` ✗
> Quote: "developing self-service platforms"
> Verified: ✓ found in JD
> Reasoning: The role primarily builds internal analytics infrastructure and platforms for data consumers, with business stakeholder interaction as a supportive mechanism rather than primary audience.

**Run 2:** `internal_data` ✗
> Quote: "developing self-service platforms"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building data infrastructure and self-serve analytics platforms for analytics consumers, while business stakeholder engagement is instrumental to that mission.

**Run 3:** `internal_data` ✗
> Quote: "developing self-service platforms"
> Verified: ✓ found in JD
> Reasoning: The emphasis on building analytics infrastructure and platforms indicates the role serves data consumers and the analytics function, not commercial or financial stakeholders.

⚠ **Disagreement**: manual=`commercial` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "work with business stakeholders to understand analytics needs"
> Verified: ✓ found in JD
> Reasoning: The role receives direction from business stakeholders' needs rather than setting strategic direction independently.

**Run 2:** `execution` ✓
> Quote: "collaborating with data engineers"
> Verified: ✓ found in JD
> Reasoning: Verbs like 'work with' and 'collaborating' indicate support and execution orientation rather than strategic direction-setting.

**Run 3:** `execution` ✓
> Quote: "work with business stakeholders to understand analytics needs"
> Verified: ✓ found in JD
> Reasoning: The responsibilities frame this as supporting stakeholders' existing needs rather than defining analytics strategy, direction, or priorities.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no explicit AI skill expectations for the candidate, whether as a personal productivity tool or infrastructure builder.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted development, or AI data infrastructure that would require candidate AI skills.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI infrastructure building, or any AI-related capabilities expected of the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "optimize data workflows for performance, usability, and cost efficiency"
> Verified: ✓ found in JD
> Reasoning: While usability is mentioned as an optimization goal, there is no explicit reference to testing frameworks, data quality practices, observability, or data contracts.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality framework mentioned in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of testing, data quality frameworks, data contracts, or observability practices.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: The JD makes no mention of testing, data quality, observability, or data reliability practices.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role entirely around capability delivery and optimization without risk, compliance, reliability, or stakeholder trust language.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed entirely in delivery and capability terms without mention of regulatory risk, reliability concerns, or preventing bad outcomes.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role around building and optimizing platforms with no mention of risk, compliance, reliability, or preventing negative outcomes.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
