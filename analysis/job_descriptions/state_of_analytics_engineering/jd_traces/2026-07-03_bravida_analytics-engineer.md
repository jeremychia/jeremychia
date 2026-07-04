# Trace: 2026-07-03_bravida_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Bravida

**URL:** https://web103.reachmee.com/ext/I003/475/job?site=2&lang=SE&validator=be182e4eb75429bedb0ddaafd3755823&job_id=11267
**Location:** Stockholm, Sweden
**Date Posted:** 2026-07-03

---

Analytics Engineer

Bravida Analytics Engineer role focuses on data modeling and semantic layer development.

Key Responsibilities
• Design and maintain data models using dbt on Snowflake
• Establish modeling standards and data contracts across business domains
• Construct and oversee pipelines in Dagster
• Leverage AI tools to enhance productivity and enable business self-service analytics
• Advance generative BI capabilities for natural language data querying
• Collaborate with operations, procurement, and finance teams on domain-specific modeling
• Improve data quality and reliability enterprise-wide

Requirements
• 3+ years in analytics engineering, data engineering, or analytics roles
• Production-level dbt expertise
• Snowflake or equivalent modern platform proficiency
• Dimensional modeling and semantic layer design knowledge
• Active AI tool integration in workflows

Soft skills
• Stakeholder management and influence capabilities
• Proactive problem identification and solution development
• Decision-making with incomplete information
• English fluency (Nordic languages preferred)

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 3 | 3 | 3 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | strategic | strategic | 33% |
| ai_role | ai_enabler | ai_enabler | ai_enabler | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: Standards and data contracts are core rigour signals emphasizing correctness and governance over speed.

**Run 2:** `rigour`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, standards-setting, and data contracts—signals of a rigour-oriented role focused on correctness and reliability over delivery speed.

**Run 3:** `rigour`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: The emphasis on establishing standards and data contracts reflects a rigour orientation emphasizing governance and quality.

### domain_risk

**Run 1:** `moderate`
> Quote: "Collaborate with operations, procurement, and finance teams on domain-specific modeling"
> Verified: ✓ found in JD
> Reasoning: Finance is mentioned but without regulatory, compliance, or financial reporting language that would signal high risk.

**Run 2:** `moderate`
> Quote: "Improve data quality and reliability enterprise-wide"
> Verified: ✓ found in JD
> Reasoning: Data quality affects operational decisions across business functions without explicit financial reporting or regulatory compliance requirements.

**Run 3:** `moderate`
> Quote: "Improve data quality and reliability enterprise-wide"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and data quality without explicit financial reporting, compliance, or regulatory language.

### collaboration_width

**Run 1:** `3`
> Quote: "operations; procurement; finance"
> Verified: ✓ found in JD
> Reasoning: Three distinct named business functions explicitly listed in the collaboration responsibility.

**Run 2:** `3`
> Quote: "operations; procurement; finance"
> Verified: ✓ found in JD
> Reasoning: Three distinct named business functions are explicitly listed as collaboration partners in the responsibilities.

**Run 3:** `3`
> Quote: "operations; procurement; finance"
> Verified: ✓ found in JD
> Reasoning: Three distinct named functions are explicitly identified as collaboration partners.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Design and maintain data models using dbt on Snowflake"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibility context with enterprise-wide scale signals established infrastructure being formalized with standards rather than greenfield setup.

**Run 2:** `mid`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: Named infrastructure (dbt, Snowflake, Dagster) appears in responsibilities with specific application contexts, indicating functional data systems being formalized rather than built from zero.

**Run 3:** `mid`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: The existence of named tools (dbt, Snowflake, Dagster) and responsibilities to establish standards indicates a maturing data function.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: Specific methodologies (data contracts, dimensional modeling, semantic layers) and named tools appear with precise technical context that indicates author has done this work.

**Run 2:** `hiring_manager`
> Quote: "Design and maintain data models using dbt on Snowflake"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific tool names with precise application contexts (dbt on Snowflake, Dagster pipelines, data contracts) that only someone doing this job would specify.

**Run 3:** `hiring_manager`
> Quote: "Design and maintain data models using dbt on Snowflake"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical context (named tools, methodologies like data contracts and generative BI) requiring hiring manager knowledge.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "enable business self-service analytics"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building data infrastructure and semantic layers for internal stakeholders to self-serve, not serving commercial, product, or financial reporting audiences.

**Run 2:** `internal_data`
> Quote: "enable business self-service analytics"
> Verified: ✓ found in JD
> Reasoning: The role's primary impact is enabling the organization's internal analytics capability through semantic layers and self-serve analytics infrastructure, not serving commercial, product, or finance stakeholders specifically.

**Run 3:** `internal_data`
> Quote: "enable business self-serve analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role primarily builds analytics infrastructure and enabling capability rather than serving specific external business functions.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of data modeling standards and architecture with execution in supporting operations/procurement/finance teams.

**Run 2:** `strategic`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: The use of "establish" signals the candidate is expected to set direction and define practices across domains rather than execute scoped work assigned by others.

**Run 3:** `strategic`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: The role owns technical direction (establishing organization-wide standards) rather than executing others' priorities.

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'strategic']

### ai_role

**Run 1:** `ai_enabler`
> Quote: "Advance generative BI capabilities for natural language data querying"
> Verified: ✓ found in JD
> Reasoning: The candidate must build data infrastructure that generative AI/LLM systems consume for natural language querying, making them responsible for enabling AI capabilities rather than just using AI tools.

**Run 2:** `ai_enabler`
> Quote: "Advance generative BI capabilities for natural language data querying"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that enables AI systems (generative BI for NLP queries) rather than use AI tools for personal coding productivity.

**Run 3:** `ai_enabler`
> Quote: "Advance generative BI capabilities for natural language data querying"
> Verified: ✓ found in JD
> Reasoning: The candidate must build data infrastructure for AI systems (generative BI for natural language querying), making this an enabler role.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Improve data quality and reliability enterprise-wide"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are framed as responsibilities the candidate will own and advance using action verbs, not as tools listed in a skill requirement.

**Run 2:** `responsibility`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: Data contracts are owned by the candidate as something to "establish"—an explicit responsibility for defining quality and testing practices.

**Run 3:** `responsibility`
> Quote: "Establish modeling standards and data contracts across business domains"
> Verified: ✓ found in JD
> Reasoning: Data contracts appear as an owned responsibility (establish) rather than a listed tool, indicating the candidate defines quality practices.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Improve data quality and reliability enterprise-wide"
> Verified: ✓ found in JD
> Reasoning: Operational reliability is stated as a concern but framed as an improvement initiative rather than risk-mitigation or compliance-focused.

**Run 2:** `moderate`
> Quote: "Improve data quality and reliability enterprise-wide"
> Verified: ✓ found in JD
> Reasoning: Operational reliability is a stated concern (quality, reliability, data contracts) but framed as capability improvement rather than regulatory or compliance risk mitigation.

**Run 3:** `moderate`
> Quote: "Improve data quality and reliability enterprise-wide"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are framed as operational concerns to address, but lack compliance or trust framing that would indicate high loss aversion.
