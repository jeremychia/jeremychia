# Trace: 2026-06-23_lovehoney-group_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Lovehoney Group

**URL:** https://jobs.eu.lever.co/lovehoneygroup/c5a8c4ee-4490-4e32-b25f-9a5d4afc70f4
**Location:** Berlin / Bath (Hybrid)

---

## Key Responsibilities

- Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems.
- Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow.
- Implement enterprise-level data quality strategies and governance frameworks across the organisation.
- Mentor other engineers while leading tool selection, technology evaluation, and architectural roadmap development.
- Represent data engineering in strategic initiatives, helping influence long-term planning and cross-functional alignment.

---

## Required Qualifications

- 5+ years of experience in data engineering or architecture, ideally in a complex, enterprise-scale environment.
- Expertise in SQL, Python, and cloud data warehouse technologies such as BigQuery.
- Strong knowledge of orchestration tools (e.g., Airflow) and data quality frameworks (e.g., Soda Core).
- A strategic mindset with experience designing scalable platforms and data governance models.
- Experience mentoring engineers and influencing technology direction at an organisational level.

---

## Preferred / Bonus Skills

None explicitly listed beyond the requirements above.

---

## Benefits

- A welcoming workplace full of drinks, snacks, friendly faces and fun team-building events.
- Access to unique discounts at high street retailers, hotels, and service providers, in addition to a 50% discount on all Lovehoney products to explore and discover new ways to have fun.
- Enjoy a hybrid work model that fosters flexibility and work-life balance, with three days per week in-office and the opportunity to work remotely for up to 4 weeks per year, alongside 25 days' holiday, plus an additional day for each year you are with Lovehoney.
- Access to customized training opportunities to support your unique learning journey, complemented by biannual feedback cycles, offering valuable insights into your performance and growth areas, enhancing your development within the company.
- Recognising the significance of physical and mental health, we proudly provide gym benefits in addition to a mental wellbeing platform, to ensure our employees thrive both professionally and personally.

---

## Interview Process

1. CV review
2. Interview with one of our Talent Acquisition Team Members
3. Hiring Manager Interview
4. Hiring Team Interview

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | mid | mid | mature | mid | 33% | ✓ |
| jd_authorship | mixed | hiring_manager | mixed | mixed | 33% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | strategic | strategic | strategic | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality strategies, governance frameworks, and enterprise-level implementation with no velocity signals present.

**Run 2:** `rigour` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes governance and data quality as core expectations with no counterbalancing velocity language like 'fast-paced', 'ship quickly', or 'iteration speed'.

**Run 3:** `rigour` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance frameworks, and enterprise-scale reliability with no velocity language like fast-paced, rapid delivery, or iteration speed.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems."
> Verified: ✓ found in JD
> Reasoning: While the role manages enterprise-scale infrastructure, there are no signals of financial reporting, regulatory compliance, or mission-critical revenue operations that would indicate high-risk domain.

**Run 2:** `moderate` ✓
> Quote: "Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems."
> Verified: ✓ found in JD
> Reasoning: While the role manages critical data infrastructure for an e-commerce retailer, the JD contains no explicit financial reporting, compliance, regulatory, or audit language that would signal high risk.

**Run 3:** `moderate` ✓
> Quote: "Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes enterprise-wide impact and data quality governance but lacks explicit financial, compliance, or regulatory language typical of high-risk domains.

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "cross-functional alignment"
> Verified: ✓ found in JD
> Reasoning: While the role involves cross-functional work, no specific partner teams or functions (Finance, Product, Marketing, Sales, etc.) are explicitly named in the JD.

**Run 2:** `0` ✗
> Quote: "Represent data engineering in strategic initiatives, helping influence long-term planning and cross-functional alignment."
> Verified: ✓ found in JD
> Reasoning: The JD mentions cross-functional work but does not explicitly name any partner teams (Finance, Product, Marketing, Operations, etc.) from the collaboration schema.

**Run 3:** `0` ✗
> Quote: "cross-functional alignment"
> Verified: ✓ found in JD
> Reasoning: The JD lacks explicitly named partner teams (Finance, Product, Marketing, etc.); only generic language like "cross-functional alignment" appears, which does not count per the rules.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow."
> Verified: ✓ found in JD
> Reasoning: The mention of platform evolution with named tools (Airflow) in specific context indicates an existing data infrastructure being improved rather than built from zero.

**Run 2:** `mature` ✗
> Quote: "orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: Airflow is named as a specific tool already deployed and used in responsibilities; combined with mentoring multiple engineers and enterprise-scale architecture focus, this indicates an established, mature data function.

**Run 3:** `mid` ✓
> Quote: "orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: Airflow is mentioned in the responsibilities section (not just requirements) and the expectation to mentor multiple engineers indicates an established but evolving data team.

⚠ **LLM inconsistency**: runs gave ['mid', 'mature', 'mid']

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow."
> Verified: ✓ found in JD
> Reasoning: The specific mention of Airflow with application context and other technical details (ETL/ELT, BigQuery, Soda Core) demonstrate technical knowledge that only someone who has performed this work would include.

**Run 2:** `mixed` ✓
> Quote: "designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: The JD includes technically specific details (Airflow, ETL/ELT pipeline design) that suggest hiring manager input, alongside generic strategic phrases ('drive platform evolution', 'cross-functional alignment') typical of recruiter language.

**Run 3:** `mixed` ✓
> Quote: "designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical language (ETL/ELT pipelines, Airflow orchestration) indicating hiring manager input, alongside generic boilerplate (governance frameworks, mentoring, strategic alignment) indicating recruiter involvement.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems."
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus entirely on building and maintaining the data infrastructure platform that serves internal organizational needs, not on serving commercial, product, or finance stakeholders directly.

**Run 2:** `internal_data` ✗
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus on building data infrastructure, governance, and quality for internal data consumers (other engineers, analytics teams) rather than serving commercial, product, finance, or external stakeholders.

**Run 3:** `internal_data` ✗
> Quote: "Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building and maintaining data infrastructure (warehouse architecture, ETL/ELT pipelines, data quality frameworks) primarily serving the data team and internal data consumers.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "leading tool selection, technology evaluation, and architectural roadmap development"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs like 'lead' and 'drive,' combined with responsibilities for defining tool selection and architectural roadmap, indicate the role is expected to set direction for the data platform rather than execute direction set by others.

**Run 2:** `strategic` ✗
> Quote: "leading tool selection, technology evaluation, and architectural roadmap development"
> Verified: ✓ found in JD
> Reasoning: The role uses strategic verbs throughout ('lead', 'drive', 'influence') and explicitly owns architecture decisions and roadmap development rather than executing pre-scoped work set by others.

**Run 3:** `strategic` ✗
> Quote: "leading tool selection, technology evaluation, and architectural roadmap development"
> Verified: ✓ found in JD
> Reasoning: The role centers on leading architectural decisions and roadmap development for the data platform rather than executing pre-determined work.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`
