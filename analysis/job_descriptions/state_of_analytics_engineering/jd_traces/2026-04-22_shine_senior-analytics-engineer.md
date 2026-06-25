# Trace: 2026-04-22_shine_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Shine

**URL:** https://careers.shine.co/jobs/7556260-senior-analytics-engineer
**Location:** Berlin or Copenhagen (hybrid: 2 remote days/week possible)

---

## Key Responsibilities

- Build and maintain scalable dbt models on Snowflake for cross-entity analytics
- Enable Data Analysts to deliver insights through reliable, documented dbt models
- Establish data governance, testing, and quality frameworks
- Drive AI-assisted workflows, including GitHub Copilot integration
- Collaborate with Data Engineering and Analytics teams on pipelines and requirements
- Define SQL styling standards and peer review processes

---

## Required Qualifications

- 5+ years in Analytics Engineering or related role
- Expert SQL proficiency and hands-on dbt experience
- Strong Snowflake (or BigQuery/Redshift) knowledge
- Engineering mindset treating models as production software
- Effective communication with technical and non-technical stakeholders
- Fluent English

---

## Preferred / Bonus Skills

- Experience with data ingestion tools
- Familiarity with BI platforms like Omni or Looker
- Background in multi-product environments

---

## Tech Stack

Snowflake, dbt, Python, Omni, GitHub Copilot

---

## Benefits

- Hybrid work flexibility
- Modern centrally-located offices
- Daily lunch provided in-office
- International team environment

---

## Recruitment Process

4 stages: Screening call → Hiring manager discussion → Case study presentation → Assessment + team meetings

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 2 | 2 | 2 | 2 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | mixed | hiring_manager | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Establish data governance, testing, and quality frameworks"
> Verified: ✓ found in JD
> Reasoning: The responsibilities explicitly prioritize data governance, testing, and quality frameworks, establishing a rigour-focused orientation without any velocity-oriented language.

**Run 2:** `rigour` ✓
> Quote: "Establish data governance, testing, and quality frameworks"
> Verified: ✓ found in JD
> Reasoning: Explicit emphasis on governance, testing, and quality frameworks with no counterbalancing velocity language demonstrates a rigour-first orientation.

**Run 3:** `rigour` ✓
> Quote: "Establish data governance, testing, and quality frameworks"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, governance, and reliability throughout with no velocity or speed-oriented language present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Enable Data Analysts to deliver insights through reliable, documented dbt models"
> Verified: ✓ found in JD
> Reasoning: While Shine operates in fintech (high-risk sector), the JD emphasizes building reliable analytics infrastructure rather than explicitly stating financial reporting, regulatory compliance, or mission-critical work.

**Run 2:** `moderate` ✓
> Quote: "Enable Data Analysts to deliver insights through reliable, documented dbt models"
> Verified: ✓ found in JD
> Reasoning: Focus on enabling business insights and decision-making without mention of financial reporting, regulatory compliance, or mission-critical systems indicates moderate domain risk.

**Run 3:** `moderate` ✓
> Quote: "Enable Data Analysts to deliver insights through reliable, documented dbt models"
> Verified: ✓ found in JD
> Reasoning: This is a business intelligence and analytics support role without explicit financial reporting, compliance, or regulatory consequences mentioned.

### collaboration_width
**Manual:** `2`

**Run 1:** `2` ✓
> Quote: "Data Engineering; Analytics teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names two distinct partner teams: Data Engineering and Analytics teams.

**Run 2:** `2` ✓
> Quote: "Data Engineering; Analytics teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named partner functions (Data Engineering and Analytics teams) are explicitly listed as collaboration partners.

**Run 3:** `2` ✓
> Quote: "Data Analysts; Data Engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct teams are explicitly named: Data Analysts and Data Engineering, both listed as collaboration partners.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Collaborate with Data Engineering and Analytics teams on pipelines and requirements"
> Verified: ✓ found in JD
> Reasoning: The existence of distinct Data Engineering and Analytics teams, combined with established tool usage (Snowflake, dbt) and a senior-level position, indicates a mid-stage team with existing infrastructure.

**Run 2:** `mid` ✓
> Quote: "Build and maintain scalable dbt models on Snowflake for cross-entity analytics"
> Verified: ✓ found in JD
> Reasoning: Presence of named production tools (dbt, Snowflake) and multiple existing data roles (analysts, engineers) alongside language about establishing governance frameworks indicates a mid-stage team with existing infrastructure that needs to scale.

**Run 3:** `mid` ✓
> Quote: "Collaborate with Data Engineering and Analytics teams on pipelines and requirements"
> Verified: ✓ found in JD
> Reasoning: Multiple specialized data teams with named tools already in use (Snowflake, dbt, Omni) indicate an established but growing data function.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Build and maintain scalable dbt models on Snowflake for cross-entity analytics"
> Verified: ✓ found in JD
> Reasoning: Technically specific responsibilities naming tools with application context suggest hiring manager input, but generic boilerplate language elsewhere ('collaborate', 'establish') indicates recruiter involvement.

**Run 2:** `mixed` ✗
> Quote: "Build and maintain scalable dbt models on Snowflake for cross-entity analytics"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about tools and application context indicates hiring manager input, but this specific language is mixed throughout with generic boilerplate verbs like 'establish', 'enable', and 'collaborate'.

**Run 3:** `hiring_manager` ✓
> Quote: "Build and maintain scalable dbt models on Snowflake for cross-entity analytics"
> Verified: ✓ found in JD
> Reasoning: The specific tool contexts, named use cases, and technical practices indicate domain knowledge from someone familiar with analytics engineering rather than generic boilerplate.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']
