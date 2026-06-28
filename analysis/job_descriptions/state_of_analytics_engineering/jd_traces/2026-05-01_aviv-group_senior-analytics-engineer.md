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
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | mixed | execution | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: Testing, documentation, governance, and reliability language dominate responsibilities with no velocity signals like 'fast-paced' or 'rapid delivery'.

**Run 2:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, documentation, version control, data contracts, and governance as core expectations, with no velocity or speed-oriented language.

**Run 3:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality assurance mechanisms (testing, documentation, version control) and data governance with no mention of speed or iteration velocity.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: JD emphasizes reliability but contains no explicit financial reporting, regulatory, or compliance language to signal high-risk domain.

**Run 2:** `moderate` ✓
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: While the role emphasizes reliability, the JD contains no explicit mention of financial reporting, compliance, or regulatory requirements that would signal high domain risk.

**Run 3:** `moderate` ✓
> Quote: "Contributing to data platform architecture including "bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring""
> Verified: ✓ found in JD
> Reasoning: While data governance is mentioned, the JD contains no explicit signals of regulatory, compliance, or financial consequences that would elevate this to high risk.

### collaboration_width
**Manual:** `4`

**Run 1:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two named distinct partner teams identified (analysts and data scientists); 'business stakeholders' is too generic to count.

**Run 2:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: Only analysts and data scientists are explicitly named as distinct collaborative groups; 'business stakeholders' is too generic to count.

**Run 3:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names two distinct collaborative partner groups: analysts and data scientists.

⚠ **Disagreement**: manual=`4` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: Named tools actively in use (dbt, Snowflake) in responsibilities with technical depth indicates mid-stage team with existing infrastructure being extended, not greenfield.

**Run 2:** `mid` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: The named tools and architecture patterns (dbt, Snowflake, bronze/silver/gold, CI/CD) in the responsibilities indicate an existing data infrastructure in development, characteristic of mid-stage teams.

**Run 3:** `mid` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: References to existing named infrastructure components (bronze/silver/gold layers, CI/CD pipelines, governance) indicate an established data function scaling beyond early stage.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: Specific technical knowledge (dbt, Snowflake, data contracts, bronze/silver/gold architecture, macro development) indicates writer with hands-on experience; generic collaboration phrases are minor additions.

**Run 2:** `hiring_manager` ✗
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical concepts (data contracts, semantic models, bronze/silver/gold architecture) that indicate hands-on experience writing these systems.

**Run 3:** `hiring_manager` ✗
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical context (dbt, Snowflake, bronze/silver/gold layers, data contracts, CI/CD) that reflects hands-on domain knowledge, not generic boilerplate.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary emphasis on data platform infrastructure, governance tooling, and serving the data function rather than commercial, product, or finance teams.

**Run 2:** `internal_data` ✗
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: The core responsibilities focus on building data infrastructure and serving other data team members through reliable data platforms and contracts.

**Run 3:** `internal_data` ✗
> Quote: "Collaborating with analysts, data scientists, and business stakeholders on reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: The primary named collaborators are analysts and data scientists (data consumers); the work focuses on building data infrastructure and contracts for analytics consumption rather than external commercial, product, or finance teams.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: Strategic responsibility for defining data contracts and semantic models combined with execution responsibilities like developing/maintaining dbt models and contributing to architecture.

**Run 2:** `execution` ✗
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: While the role includes defining some elements, the overall framing emphasizes 'contributing to' and supporting an existing strategy rather than owning direction-setting.

**Run 3:** `mixed` ✗
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership in defining data contracts and metrics across domains, but operates within a platform architecture framework and collaborates with other teams rather than setting overall organizational direction.

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'mixed']
