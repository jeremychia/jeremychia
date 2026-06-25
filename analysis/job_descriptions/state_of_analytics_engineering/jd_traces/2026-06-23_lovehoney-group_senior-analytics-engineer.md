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
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | mixed | mixed | mixed | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality and governance frameworks with no velocity signals like shipping speed or iteration pace.

**Run 2:** `rigour` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, governance, and enterprise standards with no mention of speed, iteration, or fast-paced delivery.

**Run 3:** `rigour` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, governance, and architecture with no velocity language, establishing rigour as the primary work orientation.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems"
> Verified: ✓ found in JD
> Reasoning: While data warehouse operations are critical to business decisions, the JD contains no explicit financial reporting, compliance, or regulatory language to indicate high-risk domain impact.

**Run 2:** `moderate` ✓
> Quote: "Lead enterprise-wide data warehouse architecture and implement high-performance data processing systems"
> Verified: ✓ found in JD
> Reasoning: While the data infrastructure is critical to business operations, the JD contains no explicit regulatory, compliance, or financial reporting language that would elevate risk to high.

**Run 3:** `moderate` ✓
> Quote: "Implement enterprise-level data quality strategies and governance frameworks across the organisation."
> Verified: ✓ found in JD
> Reasoning: The JD focuses on data quality and governance but contains no explicit financial reporting, compliance, regulatory, or audit language, indicating moderate business impact rather than high regulatory risk.

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "cross-functional alignment"
> Verified: ✓ found in JD
> Reasoning: The JD mentions cross-functional work but does not explicitly name any partner functions such as Finance, Product, Marketing, Data Science, or Operations.

**Run 2:** `0` ✗
> Quote: "No named partner teams or functions explicitly identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: Although the role involves mentoring engineers and cross-functional alignment, no distinct named teams (Finance, Product, Marketing, etc.) are explicitly mentioned as collaboration partners.

**Run 3:** `0` ✗
> Quote: "Represent data engineering in strategic initiatives, helping influence long-term planning and cross-functional alignment."
> Verified: ✓ found in JD
> Reasoning: No named partner teams or functions (Finance, Product, Marketing, etc.) are explicitly identified; phrases like 'cross-functional alignment' are generic terms that do not count as named collaborators.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: The phrase 'platform evolution' indicates an existing data platform being improved and extended, not built from scratch, with mentoring responsibilities suggesting a growing established team.

**Run 2:** `mid` ✓
> Quote: "Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of Airflow as a current tool used in operations and language focused on platform evolution rather than platform construction indicates an existing, established data function that is growing.

**Run 3:** `mid` ✓
> Quote: "Drive platform evolution by designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow."
> Verified: ✓ found in JD
> Reasoning: The mention of Airflow in the specific context of orchestrating existing pipelines, combined with the requirement to mentor other engineers, indicates a team and platform already in place and being evolved.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: The JD includes specific tool references (Airflow, Soda Core) with precise application context suggesting hiring manager input, but also contains generic recruiter phrases like 'mentor other engineers' and 'cross-functional alignment.'

**Run 2:** `mixed` ✓
> Quote: "designing sophisticated ETL/ELT pipelines and orchestrating them via Airflow"
> Verified: ✓ found in JD
> Reasoning: The JD mixes specific technical details (Airflow for pipeline orchestration) with generic senior-leader boilerplate (mentoring, governance, strategic alignment, cross-functional initiatives), indicating both technical input and recruiter-template language.

**Run 3:** `mixed` ✓
> Quote: "Mentor other engineers while leading tool selection, technology evaluation, and architectural roadmap development."
> Verified: ✓ found in JD
> Reasoning: The JD contains specific tool mentions (Airflow, Soda Core, BigQuery) suggesting hiring manager familiarity, but responsibilities use generic action verbs ('mentor', 'lead', 'drive') without concrete context, indicating recruiter template contributions.
