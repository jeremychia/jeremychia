# Trace: 2026-07-01_top-doctors-group_analytics-engineer-dbt-expert

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer - dbt Expert — Top Doctors Group

**URL:** https://careers.topdoctorsgroup.com/jobs/7996325-analytics-engineer
**Location:** Spain (fully remote)
**Date Posted:** 2026-07-01
**Salary:** 33,000–38,000 EUR

---

Analytics Engineer - dbt Expert at Top Doctors Group

Location: Spain (fully remote)
Salary: €33,000 - €38,000 annually

About the Company
Top Doctors Group, established in 2013, operates as a leading technology group specialising in healthcare digitalisation. The organisation serves over 1 million monthly platform users and has earned the trust of more than 10 million patients across Europe, LATAM, the United States, and the Middle East through multiple brands including Top Doctors, Top Health Tech, and others.

Role Summary
This position focuses on designing and evolving the analytical layer used across the organisation. The Analytics Engineer will work closely with the Data Team Lead, Senior Data Engineer, and business teams to build scalable data models, define reliable metrics, and ensure consistent, actionable information organisation-wide.

Key Responsibilities
- Design and maintain analytical data models in dbt with focus on traceability and quality
- Build and optimise complex SQL queries in BigQuery
- Manage table creation, views, routines, and scheduled queries
- Define, standardise, and document metrics and KPIs
- Develop dashboards in Metabase and Tableau
- Implement testing and data validation processes within dbt
- Collaborate with non-technical teams to translate business needs into scalable solutions

Requirements
- Prior experience as an Analytics Engineer or Data Analyst with strong modelling focus
- Advanced SQL proficiency with large datasets
- Solid BigQuery and modern Data Warehouse experience
- Practical dbt experience including modelling and testing
- Cloud environment knowledge (GCP or AWS)
- Dashboard development experience
- Git familiarity and software development best practices
- Fluent English for international collaboration

Benefits
- Hybrid work arrangement
- Monday-Thursday: 9:00 AM - 6:30 PM; Friday: 9:00 AM - 3:00 PM
- Birthday day off
- Flexible compensation and social benefits
- Healthcare discounts
- Collaborative, international environment

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | execution | execution | mixed | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | none | moderate | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes quality, traceability, standardization, testing, and validation throughout with no velocity-related language.

**Run 2:** `rigour` ✓
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize quality, testing, data validation, traceability, and standardization with no velocity signals present.

**Run 3:** `rigour` ✓
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality, traceability, testing, and validation with no velocity signals, establishing a rigour-focused orientation.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "define reliable metrics, and ensure consistent, actionable information organisation-wide"
> Verified: ✓ found in JD
> Reasoning: Although the company operates in regulated healthcare, the JD describes standard analytics work without explicit regulatory, compliance, or financial reporting language.

**Run 2:** `moderate` ✗
> Quote: "define reliable metrics, and ensure consistent, actionable information organisation-wide"
> Verified: ✓ found in JD
> Reasoning: Healthcare sector implies some risk, but JD language focuses on analytical reliability and metrics rather than explicit regulatory, compliance, or financial reporting concerns.

**Run 3:** `moderate` ✗
> Quote: "Develop dashboards in Metabase and Tableau"
> Verified: ✓ found in JD
> Reasoning: Although in healthcare, the JD focuses on analytical models and dashboards rather than regulatory compliance or financial reporting, making this moderate-risk business intelligence work despite the sector.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "business teams; non-technical teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: No named partner functions (Finance, Product, Marketing, etc.) are explicitly identified; only generic references to vague team groupings appear.

**Run 2:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: Data Team Lead and Senior Data Engineer are colleagues within the role holder's own team (excluded per rules); 'business teams' and 'non-technical teams' are too generic to count as distinctly named functional partners.

**Run 3:** `0` ✗
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams"
> Verified: ✓ found in JD
> Reasoning: No explicitly named cross-functional teams are listed; Data Team Lead and Senior Data Engineer are roles within the data function itself, and 'business teams' is too generic to count.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "The Analytics Engineer will work closely with the Data Team Lead, Senior Data Engineer"
> Verified: ✓ found in JD
> Reasoning: Multiple named data roles and specific named tools in responsibilities with clear application context (dbt for modelling, BigQuery for queries) indicate an established, functioning data team in growth phase.

**Run 2:** `mid` ✓
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams to build scalable data models, define reliable metrics"
> Verified: ✓ found in JD
> Reasoning: Multiple data roles already present (Team Lead, Senior Engineer) and existing named tools in responsibilities (dbt, BigQuery, Metabase, Tableau) indicate an established, growing data function rather than early-stage or mature scale.

**Run 3:** `mid` ✓
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality"
> Verified: ✓ found in JD
> Reasoning: Named tools and infrastructure (dbt, BigQuery) being maintained and optimized, plus multiple distinct data roles, signals a mid-stage team with established technical foundations.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality; Build and optimise complex SQL queries in BigQuery; Implement testing and data validation processes within dbt"
> Verified: ⚠ NOT found verbatim
> Reasoning: Responsibilities contain precise technical terminology, named tools with specific application context, and clear technical practices indicating authorship by someone with direct hands-on analytics engineering experience.

**Run 2:** `hiring_manager` ✓
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality; Build and optimise complex SQL queries in BigQuery; Implement testing and data validation processes within dbt"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical tools (dbt, BigQuery, Metabase, Tableau) with clear methodological context (model design, SQL optimization, testing implementation) demonstrates hiring manager technical depth; only one generic collaboration line.

**Run 3:** `hiring_manager` ✓
> Quote: "Manage table creation, views, routines, and scheduled queries"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about database objects (views, routines, scheduled queries) reflects hands-on experience from someone who performs this work.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "designing and evolving the analytical layer used across the organisation"
> Verified: ✓ found in JD
> Reasoning: The role centers on building data models, defining metrics, and creating dashboards as shared infrastructure for organizational data consumers, not serving a specific commercial, product, or finance function.

**Run 2:** `internal_data` ✓
> Quote: "design reliable metrics, and ensure consistent, actionable information organisation-wide"
> Verified: ⚠ NOT found verbatim
> Reasoning: Focus on building analytical data models, defining metrics, and creating the analytics infrastructure layer signals the primary audience is analytics platform consumers, not a specific business stakeholder group.

**Run 3:** `internal_data` ✓
> Quote: "ensure consistent, actionable information organisation-wide"
> Verified: ✓ found in JD
> Reasoning: The role primarily builds data infrastructure and models serving the organization's analytical needs rather than commercial, product, finance, or specific business teams.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Build and optimise complex SQL queries in BigQuery; Manage table creation, views, routines, and scheduled queries; Develop dashboards in Metabase and Tableau"
> Verified: ⚠ NOT found verbatim
> Reasoning: The dominant responsibilities use delivery-focused action verbs (build, manage, develop) indicating execution of scoped work rather than direction-setting or strategic ownership.

**Run 2:** `execution` ✗
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams to build scalable data models"
> Verified: ✓ found in JD
> Reasoning: Collaborative framing with senior-titled team members (Team Lead, Senior Engineer) indicates execution within guided direction rather than autonomous strategic ownership.

**Run 3:** `mixed` ✓
> Quote: "Design and maintain analytical data models in dbt; Define, standardise, and document metrics and KPIs"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic elements (design the analytical layer, define metrics) with execution elements (maintain models, develop dashboards).

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI coding tools, AI-assisted development, or AI/ML data infrastructure expectations for the candidate.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI tools, capabilities, or AI-related work appears anywhere in the job description.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI tools, coding assistants, agentic workflows, or AI-ready data infrastructure expectations.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Testing appears in responsibilities with an ownership verb (implement), indicating the candidate owns and defines testing practices, not just uses existing tools.

**Run 2:** `responsibility` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Action verb 'implement' indicates the candidate owns and defines testing practices as a core responsibility, not merely using existing tools.

**Run 3:** `responsibility` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: The action verb 'implement' frames testing and data validation as something the candidate owns and defines, not merely a required skill.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes delivery capabilities (design, build, develop) without mentioning compliance, regulatory risk, or preventing bad outcomes; quality is framed as a capability, not a fear response.

**Run 2:** `moderate` ✗
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality"
> Verified: ✓ found in JD
> Reasoning: Quality and traceability are primary concerns signaling moderate loss-aversion orientation toward operational data reliability, but without explicit regulatory, compliance, or stakeholder trust risk framing.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is framed around building reliable, high-quality analytics and data delivery rather than preventing risks or protecting stakeholders from bad data.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'none']
