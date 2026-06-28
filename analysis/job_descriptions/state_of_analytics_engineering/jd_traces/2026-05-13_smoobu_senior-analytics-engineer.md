# Trace: 2026-05-13_smoobu_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Smoobu (HomeToGo Group)

**URL:** https://smoobu.jobs.personio.com/job/2614929?pc=2633709
**Location:** Berlin
**Employment Type:** Full-time, Permanent

---

## Key Responsibilities

- Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking
- Design and maintain complex DAGs, implementing robust alerting mechanisms
- Create modeling principles and domain-level data models (marketing, sales)
- Connect engineering and business teams; manage reverse-ETL via Hightouch

---

## Required Qualifications

- 5+ years in Data Engineering or Analytics Engineering
- Expertise with Airbyte, Snowplow, Airflow, dbt, Snowflake, Hightouch
- Advanced SQL and data modeling skills
- Experience optimizing warehouse costs and queries
- Knowledge of data governance and GDPR practices
- High autonomy and accountability
- Fluent in English, both written and spoken

---

## Preferred / Bonus Skills

- Interest in AI agents within modern data analytics

---

## Benefits

- Remote work up to 50% annually; 63 working days abroad permitted
- 27 vacation days plus tenure bonuses (up to 32 days)
- Deutschland-Ticket subsidy and bike leasing
- Mentorship, German classes, professional development
- Team events, dog-friendly office, mental health support, Wellhub access
- Corporate discounts through FutureBens

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | mixed | 33% | ✗ |
| autonomy_level |  | mixed | strategic | strategic | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Design and maintain complex DAGs, implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes robust systems and modeling principles as core responsibilities, with no velocity-focused language present.

**Run 2:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The emphasis on 'robust' and alerting mechanisms signals reliability and correctness as core values, not delivery speed.

**Run 3:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The emphasis on robust alerting and required expertise in data governance and GDPR practices signals a focus on correctness, reliability, and compliance over speed.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Create modeling principles and domain-level data models (marketing, sales)"
> Verified: ✓ found in JD
> Reasoning: The role supports business decisions in marketing and sales but does not involve financial reporting, regulatory compliance, or P&L attribution.

**Run 2:** `moderate` ✓
> Quote: "Knowledge of data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance is mentioned, the JD does not emphasize financial reporting, regulatory compliance consequences, or mission-critical impact that would indicate high domain risk.

**Run 3:** `moderate` ✓
> Quote: "Knowledge of data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: GDPR and data governance are explicitly required, indicating regulatory compliance concerns, but the role focuses on data infrastructure rather than financial reporting or regulatory filings.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "engineering; marketing; sales"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct functions are explicitly named: engineering (in 'Connect engineering and business teams'), marketing and sales (in 'domain-level data models').

**Run 2:** `3` ✓
> Quote: "Connect engineering and business teams; Create modeling principles and domain-level data models (marketing, sales)"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three named partner functions are explicitly identified as collaborators: engineering, marketing, and sales.

**Run 3:** `3` ✓
> Quote: "engineering and business teams; domain-level data models (marketing, sales)"
> Verified: ⚠ NOT found verbatim
> Reasoning: Engineering is explicitly named as a collaboration partner, while marketing and sales are explicitly listed as domains served by the data models.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking; Design and maintain complex DAGs"
> Verified: ⚠ NOT found verbatim
> Reasoning: Multiple named tools in responsibilities indicate established infrastructure, while emphasis on creating modeling principles suggests a growing data function.

**Run 2:** `mid` ✓
> Quote: "Create modeling principles and domain-level data models (marketing, sales)"
> Verified: ✓ found in JD
> Reasoning: The role involves scaling and extending existing data infrastructure with new principles and domain models, indicating a maturing data function beyond early-stage.

**Run 3:** `mid` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking; Design and maintain complex DAGs"
> Verified: ⚠ NOT found verbatim
> Reasoning: The presence of existing named tools in active use combined with responsibilities to design and improve systems indicates a mid-stage team with established infrastructure.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking; Design and maintain complex DAGs, implementing robust alerting mechanisms; manage reverse-ETL via Hightouch"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical details including tools with use-case context (Airbyte/Snowplow for event tracking, Hightouch for reverse-ETL, DAG alerting) demonstrate hands-on technical knowledge.

**Run 2:** `hiring_manager` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: All responsibilities include specific tool names with precise application context (Airbyte and Snowplow for event tracking, Hightouch for reverse-ETL) that only someone doing this work would write.

**Run 3:** `hiring_manager` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking; Design and maintain complex DAGs, implementing robust alerting mechanisms; manage reverse-ETL via Hightouch"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specificity of named tools with precise applications (Snowplow for event tracking, reverse-ETL via Hightouch, alerting mechanisms in DAGs) indicates technical knowledge from direct experience with this stack.

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Create modeling principles and domain-level data models (marketing, sales); manage reverse-ETL via Hightouch"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role builds data infrastructure and a modeling layer that downstream consumers and systems depend on, emphasizing platform and enablement over direct business delivery.

**Run 2:** `internal_data` ✗
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: The primary function is building and maintaining data infrastructure and platforms that internal teams consume, even though marketing and sales are mentioned as domain examples.

**Run 3:** `mixed` ✗
> Quote: "Create modeling principles and domain-level data models (marketing, sales); Oversee data ingestion pipelines using Airbyte and Snowplow"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role genuinely balances internal data infrastructure responsibilities serving engineering teams with commercial domain modeling and reverse-ETL activation serving marketing and sales teams.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'mixed']

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Create modeling principles and domain-level data models"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership through modeling principles and standards while executing maintenance and operational responsibilities for pipelines and DAGs.

**Run 2:** `strategic` ✗
> Quote: "Create modeling principles and domain-level data models (marketing, sales)"
> Verified: ✓ found in JD
> Reasoning: The use of 'create' for principles and the explicit requirement for 'high autonomy and accountability' indicates the role is expected to define direction and shape how analytics is delivered.

**Run 3:** `strategic` ✗
> Quote: "Create modeling principles"
> Verified: ✓ found in JD
> Reasoning: Creating modeling principles indicates the role is expected to establish methodological standards and shape how data architecture is designed rather than execute predefined work.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'strategic']
