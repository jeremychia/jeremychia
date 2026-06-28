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
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | strategic | strategic | strategic | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Champion software engineering principles including TDD and CI/CD workflows"
> Verified: ✓ found in JD
> Reasoning: Explicit emphasis on test-driven development and continuous integration/deployment as core work principles, with no velocity signals present.

**Run 2:** `rigour` ✓
> Quote: "Champion software engineering principles including TDD and CI/CD workflows"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize engineering rigor through TDD, CI/CD, monitoring frameworks, and production-grade systems, with no corresponding velocity signals present.

**Run 3:** `rigour` ✓
> Quote: "Champion software engineering principles including TDD and CI/CD workflows"
> Verified: ✓ found in JD
> Reasoning: Multiple rigorous signals (TDD, CI/CD, production-grade, monitoring frameworks, code reviews) with no explicit velocity language demonstrates a rigour-focused orientation.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Build data products leveraging location signals and audience attributes"
> Verified: ✓ found in JD
> Reasoning: Ad tech marketing data affects targeting accuracy and business decisions without explicit financial reporting, regulatory compliance, or audit-level risk signals.

**Run 2:** `moderate` ✗
> Quote: "Build data products leveraging location signals and audience attributes"
> Verified: ✓ found in JD
> Reasoning: While the role involves adtech and large-scale data, the JD focuses on technical delivery rather than financial reporting or regulatory compliance, placing it at business-decision risk rather than high regulatory/financial risk.

**Run 3:** `moderate` ✗
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions for handling massive datasets"
> Verified: ✓ found in JD
> Reasoning: Production-grade systems at scale indicate high impact, but the absence of financial reporting, compliance, or regulatory language keeps this at moderate risk.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: References to teams and collaboration are generic and unnamed; no distinct partner functions like Finance, Product, Marketing, or Data Science are explicitly identified.

**Run 2:** `0` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: No named partner functions or teams are explicitly identified; 'squad' and 'multiple teams' are mentioned generically without specific department or function names.

**Run 3:** `0` ✗
> Quote: "Drive technical alignment across multiple teams"
> Verified: ✓ found in JD
> Reasoning: The JD references multiple teams but does not explicitly name specific partner functions or teams.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Establish monitoring frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: Operating at significant scale with multiple engineers and specific tooling, but still actively establishing infrastructure components rather than maintaining mature, fully-built systems.

**Run 2:** `mid` ✗
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions for handling massive datasets"
> Verified: ✓ found in JD
> Reasoning: The JD shows established infrastructure with production systems and multiple squads, but lacks explicit evidence of multiple specialized sub-teams or team size 20+ that would indicate mature-stage maturity.

**Run 3:** `mid` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: Multiple squads exist with established tools (Snowflake, dbt, Spark) and infrastructure suggesting a growing data organization beyond early stage.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Build data products leveraging location signals and audience attributes"
> Verified: ✓ found in JD
> Reasoning: Domain-specific technical application and scale context (location signals, geo-spatial data, multi-terabyte streams) paired with generic leadership verbs (mentor, drive alignment, champion) indicates both hiring manager and recruiter input.

**Run 2:** `hiring_manager` ✓
> Quote: "Establish monitoring frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific scale/volume descriptors ('multi-terabyte data streams', 'massive datasets') and technical methodology names (TDD, CI/CD) that suggest hands-on domain expertise rather than generic boilerplate.

**Run 3:** `hiring_manager` ✓
> Quote: "Establish monitoring frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: The technical specificity around multi-terabyte scale, domain context (geo-spatial, audience attributes), and concrete tools (dbt, Spark, Snowflake) indicates hiring manager authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: Role is framed around technical leadership, mentoring engineers, and architectural governance of the data function itself rather than serving external commercial, product, or finance stakeholders.

**Run 2:** `internal_data` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: The role's primary framing is technical leadership within the data function, with emphasis on establishing data infrastructure and mentoring engineers, serving the data team itself.

**Run 3:** `internal_data` ✗
> Quote: "Establish monitoring frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: The emphasis on technical leadership, architectural decisions, and data infrastructure (monitoring, scalable solutions) prioritizes serving the data function itself over external commercial or product stakeholders.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: Decision-making authority, architectural ownership, and explicit direction-setting verbs (make, drive, establish, champion) position this as a strategic role that defines technical direction rather than executing scoped work.

**Run 2:** `strategic` ✗
> Quote: "making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly expected to make architectural decisions, champion engineering principles, establish monitoring frameworks, and drive technical alignment—all strategic direction-setting verbs.

**Run 3:** `strategic` ✗
> Quote: "Act as technical lead for a squad, making architectural decisions and driving cross-squad collaboration"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes technical leadership, architectural decision-making, and establishing standards rather than executing work defined by others.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`
