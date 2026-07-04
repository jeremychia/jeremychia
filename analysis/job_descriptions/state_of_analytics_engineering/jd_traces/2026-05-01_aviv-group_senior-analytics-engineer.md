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
| jd_authorship | mixed | mixed | hiring_manager | hiring_manager | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | mixed | mixed | mixed | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals dominate (data contracts, testing, CI/CD, data governance, monitoring, reliable delivery) with no velocity language present.

**Run 2:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, documentation, data governance, and monitoring as core expectations, with no velocity-oriented language like fast-paced, shipping quickly, or iteration speed.

**Run 3:** `rigour` ✓
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes correctness, governance, and operational best practices with explicit testing and CI/CD signals throughout, with no velocity or speed-to-ship language.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reliability and governance but lacks explicit financial reporting, compliance, or regulatory language that would indicate high risk.

**Run 2:** `moderate` ✓
> Quote: "transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The role focuses on analytics infrastructure and BI, with no explicit financial reporting, compliance, regulatory, or mission-critical language that would indicate high domain risk.

**Run 3:** `moderate` ✓
> Quote: "Collaborating with analysts, data scientists, and business stakeholders on reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple internal business consumers but lacks explicit financial reporting, compliance, regulatory, or mission-critical language that would elevate risk to high.

### collaboration_width
**Manual:** `4`

**Run 1:** `2` ✗
> Quote: "Collaborating with analysts, data scientists, and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Two distinct named functions (analysts and data scientists) are identified as collaboration partners; business stakeholders is generic and does not count.

**Run 2:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ✓ found in JD
> Reasoning: Named function cohorts are 'analysts' and 'data scientists' from the statement 'Collaborating with analysts, data scientists, and business stakeholders'; 'business stakeholders' is generic stakeholder language, not a named team.

**Run 3:** `2` ✗
> Quote: "analysts; data scientists"
> Verified: ✓ found in JD
> Reasoning: Two named role cohorts are identified in the collaboration statement; 'business stakeholders' does not count as a specific named function.

⚠ **Disagreement**: manual=`4` vs LLM majority=`2`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: Infrastructure exists with named tools (dbt, Snowflake, CI/CD) and multiple data roles present; the role contributes to rather than builds the foundational platform.

**Run 2:** `mid` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: The data team already has established tooling (dbt, Snowflake, CI/CD), multiple roles (analysts, data scientists), and complex infrastructure patterns, indicating mid-stage maturity with growth and standardization.

**Run 3:** `mid` ✓
> Quote: "Contributing to data platform architecture including "bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring""
> Verified: ✓ found in JD
> Reasoning: Named tools and architecture patterns appear in responsibilities rather than requirements alone, and multiple data roles (analysts, data scientists, data engineers) are implied as already existing.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: Specific tools and application context (dbt models, Snowflake, bronze/silver/gold, data contracts) mix with generic action verbs (applying best practices, collaborating).

**Run 2:** `hiring_manager` ✗
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain precise technical context—named tools (dbt, Snowflake) with specific use cases, architectural patterns (bronze/silver/gold), and methodology (data contracts, semantic models)—that only someone who does analytics engineering daily would specify.

**Run 3:** `hiring_manager` ✗
> Quote: "Developing and maintaining dbt models transforming raw data into analytics-ready datasets in Snowflake"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain specific technical context (tool names paired with application, specific architecture patterns) that reflects hands-on experience rather than generic boilerplate.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Contributing to data platform architecture including bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role primarily serves internal data consumers (analysts, data scientists) through platform infrastructure and reliable data delivery rather than external commercial or finance stakeholders.

**Run 2:** `internal_data` ✓
> Quote: "Collaborating with analysts, data scientists, and business stakeholders on reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: The primary audience is the data function itself—serving analysts and data scientists with reliable analytics infrastructure, semantic models, and data contracts.

**Run 3:** `internal_data` ✓
> Quote: "Contributing to data platform architecture including "bronze/silver/gold layers, CI/CD pipelines, data governance, and monitoring""
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building and maintaining data infrastructure that serves data consumers (analysts, data scientists) within the organization.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: Defining standards across domains shows strategic ownership, but overall role framing (maintaining models, contributing to architecture, collaborating) is execution-oriented.

**Run 2:** `mixed` ✓
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership of the semantic and metrics layer across business domains while executing on dbt development and platform maintenance.

**Run 3:** `mixed` ✓
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of data standards and platform direction with execution-focused responsibilities like maintaining models and applying best practices.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, GenAI applications, coding agents, or AI infrastructure in the JD.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, GenAI applications, or AI-ready infrastructure; this is a traditional analytics engineering role.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI data infrastructure, or GenAI applications; this is standard data engineering work.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: Testing appears in responsibilities as a practice the candidate will actively apply and implement, not merely a listed skill requirement.

**Run 2:** `responsibility` ✗
> Quote: "Defining data contracts, metrics, and semantic models across business domains"
> Verified: ✓ found in JD
> Reasoning: Data contracts are explicitly named as something the candidate will define and own, indicating accountability for this quality and reliability practice.

**Run 3:** `responsibility` ✗
> Quote: "Applying testing, documentation, and version control best practices"
> Verified: ✓ found in JD
> Reasoning: Testing is framed as an owned responsibility through the action verb 'Applying' rather than listed as a tool or skill requirement.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and governance are concerns but the framing focuses on delivery and platform stability rather than compliance, regulatory, or stakeholder trust risks.

**Run 2:** `moderate` ✗
> Quote: "reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and monitoring are concerns, but the framing is infrastructure-focused, not compliance or risk-focused.

**Run 3:** `moderate` ✗
> Quote: "Collaborating with analysts, data scientists, and business stakeholders on reliable data delivery"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and governance are concerns but the JD lacks compliance, audit, or existential risk language; fear is pipeline stability rather than regulatory exposure.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
