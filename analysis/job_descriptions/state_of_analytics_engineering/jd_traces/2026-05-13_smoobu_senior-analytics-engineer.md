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
| collaboration_width | 3 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes robust pipelines, alerting mechanisms, and modeling principles with no velocity signals, indicating a rigour-focused orientation.

**Run 2:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: The emphasis on robust alerting mechanisms signals quality and reliability as core expectations, characteristic of rigour-focused orientation.

**Run 3:** `rigour` ✓
> Quote: "implementing robust alerting mechanisms"
> Verified: ✓ found in JD
> Reasoning: Robust alerting signals quality and correctness focus; no velocity language like fast-paced or rapid delivery appears in the JD.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: While the JD mentions GDPR compliance, it lacks explicit language about financial reporting, P&L, or mission-critical financial data, placing it in the moderate-risk SaaS analytics category.

**Run 2:** `moderate` ✓
> Quote: "data governance and GDPR practices"
> Verified: ✓ found in JD
> Reasoning: While governance and compliance are required knowledge, the SaaS vacation rental context means data errors affect operational BI and business decisions rather than direct financial reporting or regulatory compliance.

**Run 3:** `moderate` ✓
> Quote: "Create modeling principles and domain-level data models (marketing, sales)"
> Verified: ✓ found in JD
> Reasoning: Primary analytics domains are marketing and sales (business decisions), not financial reporting or compliance systems; GDPR is a compliance requirement but not the core domain risk.

### collaboration_width
**Manual:** `3`

**Run 1:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only "engineering" is an explicitly named partner function; "business teams" is too generic to count as a specific named function.

**Run 2:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only the engineering team is explicitly named; 'business teams' is too generic to count as a specific function.

**Run 3:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only engineering is explicitly named as a distinct collaborating team; business teams is too generic per the rule.

⚠ **Disagreement**: manual=`3` vs LLM majority=`1`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Create modeling principles and domain-level data models"
> Verified: ✓ found in JD
> Reasoning: The use of established tools (Airbyte, Snowplow, Airflow, dbt, Snowflake) combined with the need to establish modeling principles indicates a scaling, mid-stage team.

**Run 2:** `mid` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: Established tools (Airbyte, Snowplow, Airflow, dbt, Snowflake) being actively managed indicates mid-stage maturity with existing infrastructure requiring oversight and optimization.

**Run 3:** `mid` ✓
> Quote: "Oversee data ingestion pipelines using Airbyte and Snowplow for event tracking"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibility context show infrastructure exists and person will oversee it, indicating past early stage but no signals of massive mature scale.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "manage reverse-ETL via Hightouch"
> Verified: ✓ found in JD
> Reasoning: The specific mention of reverse-ETL and Hightouch demonstrates technical specificity about tools and methodologies that only someone actively doing this job would include.

**Run 2:** `hiring_manager` ✓
> Quote: "manage reverse-ETL via Hightouch"
> Verified: ✓ found in JD
> Reasoning: Naming a specific tool paired with its precise technical purpose (reverse-ETL) demonstrates hands-on experience that only someone who has done analytics engineering would naturally use.

**Run 3:** `hiring_manager` ✓
> Quote: "manage reverse-ETL via Hightouch"
> Verified: ✓ found in JD
> Reasoning: Reverse-ETL is a specific technical concept named with precise tool context, indicating hands-on technical knowledge from someone who does this job.
