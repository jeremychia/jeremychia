# Trace: 2026-05-01_aviv-group_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — AVIV Group

**URL:** https://www.linkedin.com/jobs/view/4378126108/
**Location:** Berlin, Germany
**Salary:** Extremely competitive comp + equity

---

## Key Responsibilities

- Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake
- Defining data contracts, metrics, and semantic models across business domains
- Collaborating with analysts, data scientists, and business stakeholders on reliable data delivery
- Applying testing, documentation, and version control best practices
- Contributing to data platform architecture including "bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"

---

## Required Qualifications

- 5+ years in analytics engineering, data modeling, or advanced analytics
- Strong SQL and dbt skills including "modeling, testing, and macro development"
- Hands-on experience with Snowflake or comparable cloud data warehouse
- Understanding of data modeling principles, ELT workflows, and modern data stack tools
- Strong communication and collaboration abilities across teams

---

## Preferred / Bonus Skills

- Data contracts and semantic modeling expertise
- Bronze/silver/gold layer architecture
- CI/CD pipeline design for data workflows
- Data governance and monitoring practices
- Modern data stack tools and integrations

---

## Additional Information

**Seniority Level:** Mid-Senior
**Employment Type:** Full-time
**Posted:** 10 hours ago with 68 applicants
**Recruiter Contact:** Ben Johnson, Principal Talent Partner

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 4 | 2 | 2 | 2 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | hiring_manager | hiring_manager | hiring_manager | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit rigour signals (testing, data contracts, governance, monitoring, reliable delivery) with no velocity language present.

**Run 2:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, documentation, and version control practices alongside multiple rigour signals (data contracts, governance, monitoring) with no velocity-oriented language.

**Run 3:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: Seven rigour signals present (testing, documentation, version control, data contracts, reliable delivery, governance, monitoring) with zero velocity indicators.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Collaborating with analysts, data scientists, and business stakeholders on reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: Emphasis on reliable data delivery to business stakeholders indicates business-critical decisions depend on the data, but no explicit financial, regulatory, or compliance language.

**Run 2:** `moderate` ✓
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: While the role emphasizes reliability and governance, there are no explicit signals of financial reporting, regulatory compliance, or regulatory requirements that would indicate high-risk domain.

**Run 3:** `moderate` ✓
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: Emphasizes operational reliability and data governance without explicit financial reporting, compliance, regulatory, or public-facing product language.

### collaboration_width
**Manual:** `4`

**Run 1:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two named role cohorts explicitly listed as collaboration partners; business stakeholders is generic and does not count.

**Run 2:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct role cohorts (analysts and data scientists) are explicitly named as collaboration partners.

**Run 3:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named functions—analysts and data scientists—explicitly listed as collaboration partners; 'business stakeholders' is too generic to count.

⚠ **Disagreement**: manual=`4` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: References to existing named tools, architecture patterns, and multiple governance mechanisms indicate an established data function in growth mode, not early-stage.

**Run 2:** `mid` ✓
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The JD assumes existing dbt and Snowflake infrastructure with named tools deployed in responsibilities, indicating a mid-stage team with established foundations but lacking mature-scale specialization signals.

**Run 3:** `mid` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: Multiple named tools and infrastructure components in place (dbt, Snowflake, CI/CD, governance) indicate existing platform, but 'defining' data contracts and semantic models suggests active growth rather than fully mature operations.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: Specific technical context about named tools, their precise application (dbt transformation workflows), and technology stack indicates someone with hands-on experience writing this.

**Run 2:** `hiring_manager` ✗
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: The responsibilities demonstrate specific methodology knowledge (data contracts, semantic models, bronze/silver/gold architecture) that indicates hands-on experience, not generic boilerplate language.

**Run 3:** `hiring_manager` ✗
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: Specific technical details about exact tools, data workflow direction, and desired outputs demonstrate insider knowledge only a hiring manager would possess.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`
