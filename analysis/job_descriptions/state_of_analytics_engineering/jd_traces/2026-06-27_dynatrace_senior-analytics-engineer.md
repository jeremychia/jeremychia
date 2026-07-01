# Trace: 2026-06-27_dynatrace_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Dynatrace

**Location:** Barcelona, Spain (Hybrid)
**Date Posted:** 2026-06-27

---

Senior Analytics Engineer - Dynatrace

Position Overview
Title: Senior Analytics Engineer
Type: Full-time, Hybrid
Location: Barcelona, Spain
Department: Business Systems
Level: Experienced and Senior
Job ID: 5288

Your Role at Dynatrace

The role involves designing and delivering data products for reporting, self-service analytics, and emerging AI use cases. Responsibilities include collaborating with stakeholders and teams while leveraging AI-assisted development tools like GitHub Copilot or Claude.

Key Responsibilities

Data Product Design & Development
- Design scalable analytical data models and curated datasets, conformed dimensions, and standardized metrics
- Translate business requirements into reliable, reusable data products
- Design data models with AI readiness in mind, including column-level descriptions
- Build structures supporting discoverability across analytics and AI/ML use cases

Standards, Quality & Governance
- Follow established SQL development and dbt modeling standards
- Support semantic layer implementation with consistent metrics
- Implement data quality checks and governance within dbt and Snowflake
- Maintain well-tested, documented models aligned with business definitions

Collaboration & Technical Contribution
- Partner with data engineers, platform teams, and stakeholders
- Collaborate through code reviews and knowledge sharing
- Contribute to cross-functional standardization initiatives
- Identify process improvement opportunities

Required Qualifications

- Bachelor's degree in Computer Science, Information Systems, Engineering, or related field
- 5–8+ years in analytics engineering or data modeling with strong SQL focus
- Strong SQL skills for complex analytical queries and optimization
- Hands-on dbt Cloud experience
- Snowflake experience with query tuning knowledge
- Understanding of dimensional modeling (Kimball) concepts
- Experience with established analytics frameworks and standards
- Ability to work independently and collaborate cross-functionally
- Strong communication skills translating technical concepts
- Data quality validation and governance experience
- Git/GitHub workflow proficiency
- Proven experience with AI-assisted development tools such as GitHub Copilot, Claude, or similar
- Power BI experience or familiarity

Preferred Qualifications
- Master's degree
- Python for automation and scripting
- Semantic layer or metric framework exposure
- AI/ML data readiness and feature engineering knowledge
- Fivetran or similar data ingestion tools
- Enterprise systems experience (Salesforce, NetSuite, SuccessFactors)

Why Join Dynatrace

Dynatrace is a leader in unified observability and security serving over 50% of Fortune 100 companies. The role offers opportunities to work at the forefront of innovation with Dynatrace Intelligence.

Benefits

Core Offerings:
- Paid time off and financial security benefits
- Retirement savings plans and health insurance
- Mental health support via Telus Health EAP
- Four designated wellness days annually
- Hybrid work model with flexible hours
- Discounted employee stock purchase plan
- Professional development and learning days
- Paid volunteer time
- Team events and multicultural environment

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Implement data quality checks and governance within dbt and Snowflake; Maintain well-tested, documented models aligned with business definitions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes data quality, governance, testing, and documentation as core expectations with no velocity-oriented language present.

**Run 2:** `rigour`
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (quality, governance, well-tested, documented, standards) with no velocity language indicates a rigour-focused role.

**Run 3:** `rigour`
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, standards, testing, and documentation with no velocity signals present.

### domain_risk

**Run 1:** `moderate`
> Quote: "The role involves designing and delivering data products for reporting, self-serve analytics, and emerging AI use cases."
> Verified: ⚠ NOT found verbatim
> Reasoning: This describes internal business analytics supporting business decisions rather than financial reporting, regulatory compliance, or revenue-critical systems.

**Run 2:** `moderate`
> Quote: "data products for reporting, self-serve analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: Internal analytics and data platform work for business systems without explicit financial reporting, compliance, or regulatory requirements indicates moderate risk.

**Run 3:** `moderate`
> Quote: "The role involves designing and delivering data products for reporting, self-service analytics, and emerging AI use cases."
> Verified: ✓ found in JD
> Reasoning: The JD focuses on business analytics and reporting without explicit financial reporting, compliance, regulatory, or mission-critical language.

### collaboration_width

**Run 1:** `2`
> Quote: "Partner with data engineers, platform teams, and stakeholders"
> Verified: ✓ found in JD
> Reasoning: Two explicitly named teams are identified: data engineers and platform teams; stakeholders is generic and does not count.

**Run 2:** `2`
> Quote: "data engineers; platform teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two explicitly named partner functions are listed in collaboration context.

**Run 3:** `2`
> Quote: "Partner with data engineers, platform teams, and stakeholders"
> Verified: ✓ found in JD
> Reasoning: Two distinct named teams are explicitly identified: data engineers and platform teams.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Follow established SQL development and dbt modeling standards; Support semantic layer implementation with consistent metrics"
> Verified: ⚠ NOT found verbatim
> Reasoning: References to established tools, standards, and frameworks indicate an existing data function with infrastructure in place and multiple team members.

**Run 2:** `mid`
> Quote: "Follow established SQL development and dbt modeling standards"
> Verified: ✓ found in JD
> Reasoning: Established standards, named tools in responsibilities (dbt, Snowflake, semantic layer), and multiple implied data roles indicate an existing function at growth stage.

**Run 3:** `mid`
> Quote: "Follow established SQL development and dbt modeling standards"
> Verified: ✓ found in JD
> Reasoning: References to established standards and named tools in responsibilities (dbt, Snowflake, semantic layer) indicate an operating data function expanding rather than building from zero.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Design scalable analytical data models and curated datasets, conformed dimensions, and standardized metrics; Implement data quality checks and governance within dbt and Snowflake"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain technical specificity (conformed dimensions, dbt, Snowflake, semantic layer) that indicates someone performing this work wrote it.

**Run 2:** `mixed`
> Quote: "Design data models with AI readiness in mind, including column-level descriptions"
> Verified: ✓ found in JD
> Reasoning: Technical specificity (AI readiness, column-level descriptions, semantic layer, conformed dimensions) is mixed with generic boilerplate language (collaborate, partner), indicating input from multiple authors.

**Run 3:** `mixed`
> Quote: "Implement data quality checks and governance within dbt and Snowflake; Design data models with AI readiness in mind, including column-level descriptions"
> Verified: ⚠ NOT found verbatim
> Reasoning: Contains technical specificity about tool stacks and concepts (semantic layer, conformed dimensions, AI readiness, column-level metadata) paired with generic collaboration boilerplate.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "designing and delivering data products for reporting, self-serve analytics, and emerging AI use cases"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's primary purpose is building analytical infrastructure and self-serve analytics platforms for internal data consumers and analysts.

**Run 2:** `internal_data`
> Quote: "designing and delivering data products for reporting, self-serve analytics, and emerging AI use cases"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role primarily serves the data function and internal analytics consumers through self-serve infrastructure and data products.

**Run 3:** `internal_data`
> Quote: "designing and delivering data products for reporting, self-service analytics, and emerging AI use cases"
> Verified: ✓ found in JD
> Reasoning: The primary emphasis is building reusable data products and infrastructure for internal analytics consumers, data engineers, and platform teams.

### autonomy_level

**Run 1:** `execution`
> Quote: "Follow established SQL development and dbt modeling standards; Support semantic layer implementation"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role operates within established frameworks and standards while supporting other teams' initiatives rather than defining overall analytics direction.

**Run 2:** `execution`
> Quote: "Follow established SQL development and dbt modeling standards"
> Verified: ✓ found in JD
> Reasoning: While the role includes design responsibilities, it operates within pre-established standards and frameworks set by the organization.

**Run 3:** `execution`
> Quote: "Translate business requirements into reliable, reusable data products"
> Verified: ✓ found in JD
> Reasoning: The role receives business requirements from stakeholders and implements them within established standards and frameworks, rather than defining analytics strategy or roadmap.

### ai_role
**Run 1:** `ai_enabler` ✓
> Quote: "Design data models with AI readiness in mind, including column-level descriptions"
> Reasoning: Candidate builds infrastructure for AI consumption through semantic-ready data models.

**Run 2:** `ai_enabler` ✓
> Quote: "Design data models with AI readiness in mind, including column-level descriptions"
> Reasoning: Candidate builds infrastructure for AI consumption via semantic metadata and AI-ready schemas.

**Run 3:** `ai_enabler` ✓
> Quote: "Design data models with AI readiness in mind, including column-level descriptions"
> Reasoning: Candidate builds semantic infrastructure (column descriptions) explicitly designed for AI consumption and text-to-SQL applications.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Reasoning: Candidate owns quality assurance and governance implementation.

**Run 2:** `responsibility` ✓
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Reasoning: Candidate owns quality implementation and governance standards, not just following them.

**Run 3:** `responsibility` ✓
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Reasoning: Explicit ownership verb 'implement' paired with quality checks shows candidate owns validation practice.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Reasoning: Governance language signals trust and compliance concerns, balanced with operational delivery framing.

**Run 2:** `moderate` ✓
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Reasoning: Framing centers on operational governance and data reliability as core responsibility, suggesting concern for stability.

**Run 3:** `moderate` ✓
> Quote: "Implement data quality checks and governance within dbt and Snowflake"
> Reasoning: Governance framing indicates operational control concerns, though lacks explicit compliance or incident-prevention language.

