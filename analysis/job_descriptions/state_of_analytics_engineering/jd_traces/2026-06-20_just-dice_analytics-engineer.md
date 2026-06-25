# Trace: 2026-06-20_just-dice_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer (f/m/d) — justDice

**URL:** https://jobs.ashbyhq.com/justDice/07c63836-8e46-4408-95bb-fcc9c30c51be
**Location:** Hamburg, Germany (Hybrid — 3 core office days)

---

## Key Responsibilities

**Data Engineering**

- Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services.
- Create and maintain data architecture and data models for various business domains.
- Implement data quality and validation processes to guarantee data accuracy and consistency.
- Automate and streamline data integration, ETL, and ELT processes to improve efficiency.

**Analytics**

- Establish and implement data requirements and analytics solutions with our tech and product teams.
- Plan, execute, and evaluate experiments with our marketing and product teams.
- Establish the KPIs and metrics that will be used by the business. Develop appropriate monitoring tools for these indicators.
- Convey the message using visualization tools (Tableau)

---

## Required Qualifications

- Bachelor's degree in STEM fields or previous experience in related jobs or projects.
- Minimum 3 years of experience in data science, engineering, analytics, or a related field.
- Strong SQL, Python programming skills.
- Knowledge of dbt
- Proficient in data modeling, data architecture, and data engineering principles.
- Knowledge of GitLab or similar git-based version control systems.
- Ability to validate hypotheses through data visualization.
- Strong analytical skills.
- Autonomy and ability to work independently.
- Strong problem-solving skills.
- Growth mindset and eagerness to learn new technologies and methodologies.
- Is able to communicate in a pragmatic and professional manner.

---

## Preferred / Bonus Skills

None explicitly listed.

---

## Benefits

- **Invest in Your Future:** Regular feedback and our development program support your growth, helping you expand your skill set and achieve your career goals.
- **Easy Arrival to justDice:** From signing to settling in Hamburg, we've got you covered. Need a visa? No problem. Ready to build your new life and career at justDice in Hamburg? We support every ambition—from learning German to a relocation bonus that helps you settle in and make Hamburg feel like home.
- **Live Your Best Life, at Work and Beyond:** We work in a hybrid setup with 3 core office days, plus flexible working hours. Enjoy 30 vacation days, 3 weeks of remote work per year, and free access to an in-house gym with lots of different fitness classes and mental health support through our Employee Assistance Program (EAP).
- **Thrive Where You Work:** Enjoy the Alster lake view from our central office with top notch equipment, fun open spaces, and a large variety of snacks and drinks.
- **Join the Community!** Participate in regular team and company events, including hackathons and social gatherings. We work together, and we celebrate together, too.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 2 | 3 | 3 | 3 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | hiring_manager | hiring_manager | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Implement data quality and validation processes to guarantee data accuracy and consistency."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data accuracy, consistency, and validation as core expectations, with no language signaling speed or iteration velocity.

**Run 2:** `rigour` ✗
> Quote: "Implement data quality and validation processes to guarantee data accuracy and consistency."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, accuracy, and validation as core expectations with no velocity or speed-focused language present.

**Run 3:** `rigour` ✗
> Quote: "Implement data quality and validation processes to guarantee data accuracy and consistency"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes correctness and accuracy as core expectations with no velocity signals present.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Establish the KPIs and metrics that will be used by the business."
> Verified: ✓ found in JD
> Reasoning: The JD focuses on business analytics and operational reporting without explicit financial reporting, regulatory, or compliance language typical of high-risk domains.

**Run 2:** `moderate` ✓
> Quote: "Plan, execute, and evaluate experiments with our marketing and product teams. Establish the KPIs and metrics that will be used by the business."
> Verified: ⚠ NOT found verbatim
> Reasoning: The role supports business-critical decisions through experiments and KPI establishment, but the JD contains no language about regulatory compliance, financial reporting, or mission-critical systems.

**Run 3:** `moderate` ✓
> Quote: "Establish the KPIs and metrics that will be used by the business"
> Verified: ✓ found in JD
> Reasoning: The JD frames the role around business intelligence and operational analytics without explicit financial reporting, regulatory compliance, or mission-critical language.

### collaboration_width
**Manual:** `2`

**Run 1:** `3` ✗
> Quote: "our tech and product teams; our marketing and product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named teams are explicitly mentioned as collaboration partners: tech/engineering, product, and marketing.

**Run 2:** `3` ✗
> Quote: "with our tech and product teams; with our marketing and product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named functions are identified as collaboration partners: tech teams, product teams, and marketing teams.

**Run 3:** `3` ✗
> Quote: "tech and product teams; marketing and product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct partner functions: Tech, Product, and Marketing.

⚠ **Disagreement**: manual=`2` vs LLM majority=`3`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services."
> Verified: ✓ found in JD
> Reasoning: Named tools deployed in the responsibilities (dbt, AWS services) indicate an existing data function with infrastructure in a growth and enhancement phase, not a greenfield build.

**Run 2:** `mid` ✗
> Quote: "Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services; Create and maintain data architecture and data models for various business domains."
> Verified: ⚠ NOT found verbatim
> Reasoning: The presence of specific established tools (dbt, AWS) and responsibility to maintain existing infrastructure indicates an established data function, while foundational work (establishing KPIs) suggests ongoing growth rather than full maturity.

**Run 3:** `mid` ✗
> Quote: "Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities and language of 'enhance' and 'maintain' indicate existing infrastructure requiring growth rather than greenfield setup.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services; Create and maintain data architecture and data models for various business domains."
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain specific technical tools, methodologies (ETL/ELT, data modeling), and precise application context that only someone with hands-on data engineering experience would articulate.

**Run 2:** `hiring_manager` ✗
> Quote: "Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services; Create and maintain data architecture and data models; Implement data quality and validation processes to guarantee data accuracy and consistency."
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities specify particular tools (dbt, Python, AWS), explicit methodologies (data modeling, data architecture, ETL/ELT), and concrete business context (experiments, KPIs) that only someone with hands-on experience in the role would describe.

**Run 3:** `mixed` ✓
> Quote: "Design, construct, and enhance data pipelines utilizing SQL, Python, dbt, git, and AWS services; Establish and implement data requirements and analytics solutions with our tech and product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data engineering section contains technical specificity with named tools and concepts, while analytics collaboration sections use generic stakeholder language.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']
