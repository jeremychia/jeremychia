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
| collaboration_width | 3 | 1 | 0 | 3 | 0% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | mixed | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize operational reliability, governance, and regulatory compliance (GDPR) with no speed or iteration language.

**Run 2:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes robust system design and governance; no velocity language like fast-paced or shipping appears.

**Run 3:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (robust systems, data governance, GDPR practices) with zero velocity language throughout the JD.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Knowledge of data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: The marketplace context and GDPR requirement indicate data protection compliance concerns, but no explicit financial reporting or revenue attribution risk.

**Run 2:** `moderate` ✓
> Quote: "Knowledge of data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is explicitly required, positioning the role in a regulated context, but the primary framing is technical platform work rather than financial reporting or compliance enforcement.

**Run 3:** `moderate` ✓
> Quote: "Knowledge of data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is mentioned but the company is a marketplace (not high-risk sector) and the role emphasizes operational data infrastructure rather than financial reporting or regulatory protection.

### collaboration_width
**Manual:** `3`

**Run 1:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only 'engineering' is explicitly named as a distinct collaboration function; 'business teams' is too generic per the exclusion rules.

**Run 2:** `0` ✗
> Quote: "None"
> Verified: ✓ found in JD
> Reasoning: The JD mentions 'engineering and business teams' generically and lists 'marketing, sales' as data modeling domains, but does not explicitly name specific teams or functions as collaboration partners.

**Run 3:** `3` ✓
> Quote: "Connect engineering and business teams; domain-level data models (marketing, sales)"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams explicitly referenced: engineering, marketing, and sales.

⚠ **Disagreement**: manual=`3` vs LLM majority=`1`

⚠ **LLM inconsistency**: runs gave ['1', '0', '3']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Create modeling principles and domain-level data models"
> Verified: ✓ found in JD
> Reasoning: The team has established infrastructure with named tools in responsibilities but is still establishing governance principles, indicating a growth phase.

**Run 2:** `mid` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking; Design and maintain complex DAGs"
> Verified: ✓ found in JD
> Reasoning: Multiple named tools in responsibilities (Airbyte, Snowplow, Airflow, dbt, Snowflake, Hightouch) indicate an established data function with infrastructure in place, but no evidence of specialized sub-teams.

**Run 3:** `mid` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: Multiple named tools in responsibilities signal established infrastructure; the emphasis on creating modeling principles indicates growth-stage standardization work.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design and maintain complex DAGs, implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical methodology (DAGs, alerting mechanisms) that reflects hands-on domain knowledge rather than generic action verbs.

**Run 2:** `hiring_manager` ✓
> Quote: "Design and maintain complex DAGs, implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about DAG design and alerting strategies with precise tool context indicates hands-on experience rather than generic template.

**Run 3:** `hiring_manager` ✓
> Quote: "manage reverse-ETL via Hightouch"
> Verified: ✓ found in JD
> Reasoning: Specific tool-application context (Hightouch for reverse-ETL) reveals someone who does this work; the stack (Airbyte, Snowplow, Airflow, dbt, Snowflake, Hightouch) shows precise technical knowledge.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building and maintaining data infrastructure for internal consumption rather than serving commercial, product, or finance stakeholders directly.

**Run 2:** `internal_data` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking; Design and maintain complex DAGs"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize building and maintaining the data platform infrastructure (pipelines, DAGs, models) as the primary mission.

**Run 3:** `internal_data` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: Primary responsibilities center on building and maintaining data infrastructure (pipelines, DAGs, alerting, principles) rather than delivering insights to commercial, product, or financial stakeholders.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Create modeling principles and domain-level data models"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to set direction through establishing modeling principles and governance, not execute scoped work defined by others.

**Run 2:** `strategic` ✓
> Quote: "Create modeling principles and domain-level data models"
> Verified: ✓ found in JD
> Reasoning: The role is expected to create (define) modeling principles and standards, coupled with explicit requirement of 'high autonomy and accountability'.

**Run 3:** `mixed` ✗
> Quote: "Create modeling principles and domain-level data models"
> Verified: ✓ found in JD
> Reasoning: Strategic ownership of data modeling standards combined with execution/operational responsibilities (oversee, maintain, manage) creates a dual responsibility pattern.

⚠ **LLM inconsistency**: runs gave ['strategic', 'strategic', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The preferred mention of 'interest in AI agents' is too vague and listed as bonus-level; no concrete AI-user or AI-enabler skills are required.

**Run 2:** `none` ✗
> Quote: "Interest in AI agents within modern data analytics"
> Verified: ✓ found in JD
> Reasoning: The AI reference is vague and relegated to preferred/bonus skills, not a core expected competency.

**Run 3:** `none` ✗
> Quote: "Interest in AI agents within modern data analytics"
> Verified: ✓ found in JD
> Reasoning: The preference for interest in AI agents is vague, bonus-only, and does not indicate expected ai_user or ai_enabler skills.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: While alerting reflects reliability concerns, there is no explicit testing framework, data quality ownership, or named testing tools in the JD.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of testing, data quality frameworks, data contracts, or observability as a named practice or responsibility.

**Run 3:** `absent` ✗
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: No mention of testing frameworks, data contracts, or data quality ownership; alerting signals operational reliability but not testing or quality assurance responsibility.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The emphasis on operational reliability and GDPR compliance indicates moderate concern for preventing failures, but the overall framing is capability-delivery rather than risk-prevention focused.

**Run 2:** `moderate` ✗
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: Operational reliability through alerting is a concern, with GDPR governance required, but the role is primarily framed around technical delivery and platform building.

**Run 3:** `moderate` ✗
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and governance requirements are present but secondary to infrastructure delivery; fear is pipeline/data failures, not regulatory or stakeholder-trust catastrophe.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
