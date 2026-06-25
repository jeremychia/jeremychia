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
| jd_authorship | hiring_manager | mixed | mixed | mixed | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize code quality, testing, monitoring, and reliable delivery as primary expectations, with no velocity-oriented language present.

**Run 2:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes reliability, quality, testing, monitoring, and best practices throughout, with no language emphasizing speed, iteration, or fast-paced delivery.

**Run 3:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize best practices, testing, and monitoring rather than speed or delivery pace.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: This describes data infrastructure for product and business operations in a marketplace domain, not financial reporting, compliance, or other high-risk systems.

**Run 2:** `moderate` ✓
> Quote: "Build end-to-end data solutions independently: Deliver reliable, high-quality datasets/pipelines"
> Verified: ✓ found in JD
> Reasoning: As a marketplace platform data role focused on operational pipelines with no explicit financial reporting, compliance, or regulatory language, data errors affect business decisions and operations (moderate) rather than financial reporting or regulatory compliance (high).

**Run 3:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The role supports business decision-making in a marketplace context without explicit financial reporting or regulatory compliance requirements.

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "Product;Data teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Product and Data teams are the only explicitly named partner functions mentioned in the responsibilities section.

**Run 2:** `2` ✗
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: Two distinct named teams are explicitly listed as collaboration partners: Product and Data teams.

**Run 3:** `2` ✗
> Quote: "Product; Data teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Product is a distinct function, and Data teams (plural) represents collaboration with other teams within the data organization.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: The team operates with established SLOs and manages both operational and development work, indicating a maturing data function beyond early-stage infrastructure.

**Run 2:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: The reference to existing production systems, operational responsibilities, and team SLOs indicates an established team managing mature infrastructure rather than building greenfield systems, but without language suggesting massive scale or multiple specialized sub-teams.

**Run 3:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: Existing production infrastructure requiring optimization, operational processes via SLOs, and sub-team specialization (Traveler Data Engineering) indicate mid-stage maturity.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: Some responsibilities show specific technical understanding (data modeling, pipeline refactoring, SLOs), but generic recruiter phrases like 'thought partner' and 'translate requirements' indicate recruiter input alongside hiring manager authorship.

**Run 2:** `mixed` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: The JD contains technical specificity (SLOs, named warehouse platforms, dbt/Spark) indicative of hiring manager input mixed with generic boilerplate phrases like 'thought partner' and 'translate business requirements,' typical of large companies with split authorship.

**Run 3:** `mixed` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: Specific knowledge of team SLOs and operational tensions indicates hiring manager input, though boilerplate language elsewhere (thought partner, apply best practices) suggests recruiter involvement.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`
