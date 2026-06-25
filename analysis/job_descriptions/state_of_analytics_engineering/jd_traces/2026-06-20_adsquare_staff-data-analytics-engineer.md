# Trace: 2026-06-20_adsquare_staff-data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Staff Data Analytics Engineer (m/f/d) — Adsquare GmbH

**URL:** https://adsquare.jobs.personio.de/job/2540423
**Location:** Berlin, Germany
**Salary:** €90,000 – €100,000 per year

---

## Key Responsibilities

- Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration
- Design horizontally scalable, cost-efficient, production-grade data solutions for handling massive datasets
- Champion software engineering principles including TDD and CI/CD workflows
- Drive technical alignment across multiple teams
- Build data products leveraging location signals and audience attributes
- Mentor engineers through code reviews and pair programming
- Establish monitoring frameworks for multi-terabyte data streams

---

## Required Qualifications

- 7+ years in Data Engineering, Analytics Engineering, or Backend Development
- Hands-on experience with geo-spatial data, audience attributes, and time-series datasets
- Advanced Python proficiency with TDD, mocking, and performance profiling expertise
- Deep knowledge of scalable data architectures (Snowflake, Redshift, Athena, StarRocks, Iceberg)
- Extensive experience with Apache Spark, PySpark, and AWS EMR
- Expert-level SQL and dbt skills
- AWS cloud native architecture and Terraform (IaC) experience
- Strong leadership, communication, and organizational abilities

---

## Preferred / Bonus Skills

- Polyglot programming in compiled/strongly-typed languages (Scala, Go, Kotlin, C++, Java)
- Advanced orchestration tools (Airflow, Dagster, Prefect)

---

## Benefits

- Hybrid/remote work flexibility
- €1,200 annual professional development budget
- 30 vacation days annually
- Urban Sports Club membership
- Company pension scheme
- Team and company events
- Latest hardware and tools provided

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 3 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | recruiter | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Champion software engineering principles including TDD and CI/CD workflows"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, CI/CD, code reviews, production-grade systems, and monitoring as core expectations with no velocity-oriented language present.

**Run 2:** `rigour` ✓
> Quote: "Champion software engineering principles including TDD and CI/CD workflows"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, deployment automation, code review, and production-readiness as core practices with no language about speed, shipping, or iteration pace.

**Run 3:** `rigour` ✓
> Quote: "Champion software engineering principles including TDD and CI/CD workflows"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize TDD, CI/CD, production-grade solutions, monitoring, and code reviews—core software engineering quality practices with no velocity language present.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Build data products leveraging location signals and audience attributes"
> Verified: ✓ found in JD
> Reasoning: Adtech company context with user data, but no explicit language around compliance, regulatory, or financial reporting impact.

**Run 2:** `moderate` ✗
> Quote: "Build data products leveraging location signals and audience attributes"
> Verified: ✓ found in JD
> Reasoning: While the data infrastructure is business-critical and operates at massive scale, the JD contains no explicit mention of regulatory compliance, financial reporting, or audit concerns typical of high-risk domains.

**Run 3:** `moderate` ✗
> Quote: "Build data products leveraging location signals and audience attributes"
> Verified: ✓ found in JD
> Reasoning: The role involves business decision-making through data products but lacks explicit compliance, regulatory, or financial reporting language that would indicate high risk.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No named partner functions or teams explicitly listed; only generic references to 'squads' and 'multiple teams'.

**Run 2:** `0` ✗
> Quote: "cross-squad collaboration; multiple teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions squads and teams exist but names no specific partner functions such as Product, Finance, Marketing, Engineering, or other distinct teams.

**Run 3:** `0` ✗
> Quote: "driving cross-squad collaboration; Drive technical alignment across multiple teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions collaboration with squads and teams generically, but does not identify named functions like Finance, Product, Marketing, or other specific teams.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: Implies existing team structure and production systems already in place, but no signals of multiple specialized sub-teams or greenfield infrastructure building.

**Run 2:** `mid` ✗
> Quote: "Mentor engineers through code reviews and pair programming"
> Verified: ✓ found in JD
> Reasoning: The presence of engineers to mentor and established practices (code review, pair programming) indicates an existing, functioning team that is growing and formalizing structure, not early-stage or fully mature at scale.

**Run 3:** `mid` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: The existence of multiple squads requiring technical leadership and cross-squad alignment suggests an established data function beyond startup stage, but lacks explicit signals of large-scale mature organization.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions for handling massive datasets"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain specific technical practices (TDD, CI/CD, code reviews), domain expertise (location signals, audience attributes), and precise scale context (multi-terabyte) indicating hands-on authorship.

**Run 2:** `hiring_manager` ✓
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions for handling massive datasets"
> Verified: ✓ found in JD
> Reasoning: The specific architectural concerns (scalability, cost-efficiency, production-readiness) combined with domain-specific responsibilities and scale metrics demonstrate technical depth from someone who has done this work, not recruiter boilerplate.

**Run 3:** `recruiter` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs and concepts without specific context about what systems, tools, or metrics would be directly managed, while specific technical tools are listed separately in the requirements section.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'recruiter']
