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
| autonomy_level | mixed | execution | mixed | execution | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, data validation, quality, traceability, and reliable metrics—core rigour signals—with no velocity-oriented language present.

**Run 2:** `rigour` ✓
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Testing and data validation are explicit core responsibilities, indicating quality and reliability as primary values over shipping speed.

**Run 3:** `rigour` ✓
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality, testing, and standardization with no velocity language; testing and data validation appear prominently as core expectations.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality"
> Verified: ✓ found in JD
> Reasoning: Healthcare sector implies inherent risk, but the JD uses generic BI/analytics language without explicit regulatory, compliance, or financial-reporting framers.

**Run 2:** `moderate` ✗
> Quote: "ensure consistent, actionable information organisation-wide"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes analytical reliability and business decision-support, which carries moderate risk without explicit financial reporting or regulatory compliance framing typical of high-risk domains.

**Run 3:** `moderate` ✗
> Quote: "serves over 1 million monthly platform users and has earned the trust of more than 10 million patients across Europe, LATAM, the United States, and the Middle East"
> Verified: ✓ found in JD
> Reasoning: While healthcare sector and patient scale imply inherent risk, the JD language is generic about analytics without explicit regulatory, compliance, or financial reporting framing.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams"
> Verified: ✓ found in JD
> Reasoning: No distinct external named partner functions are explicitly identified; data team members are internal collaborators and business teams is generic.

**Run 2:** `0` ✗
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams"
> Verified: ✓ found in JD
> Reasoning: Mentioned collaborators are members of the data team itself (which does not count per rules) and 'business teams' is too generic; no named distinct functions are identified.

**Run 3:** `0` ✗
> Quote: "No explicitly named partner functions identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: References to 'business teams' and 'non-technical teams' are too vague; no named functions like Finance, Product, or Engineering appear in the JD.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "work closely with the Data Team Lead, Senior Data Engineer"
> Verified: ✓ found in JD
> Reasoning: Multiple named data roles and established tools (dbt, BigQuery, Metabase, Tableau) used in responsibilities indicate an existing data function being scaled/improved rather than built from zero.

**Run 2:** `mid` ✓
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams to build scalable data models"
> Verified: ✓ found in JD
> Reasoning: Multiple named data roles and existing named tools (dbt, BigQuery, Metabase) deployed in production indicate an established data function that is scaling and evolving.

**Run 3:** `mid` ✓
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality"
> Verified: ✓ found in JD
> Reasoning: Named tools deployed in responsibilities and multiple data roles (Team Lead, Senior Data Engineer) imply an established team, but no signals of enterprise-scale maturity like multiple specialized sub-teams or large team size.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design and maintain analytical data models in dbt with focus on traceability and quality; Build and optimise complex SQL queries in BigQuery; Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Specific technical responsibilities with named tools and methodologies (dbt modelling, BigQuery optimization, testing frameworks) enable understanding of actual Tuesday work; generic collaboration statement is minor.

**Run 2:** `hiring_manager` ✓
> Quote: "Manage table creation, views, routines, and scheduled queries"
> Verified: ✓ found in JD
> Reasoning: The specificity of technical tasks (views, routines, scheduled queries) and precise tool application contexts (dbt testing, BigQuery optimization) demonstrates hands-on domain expertise.

**Run 3:** `hiring_manager` ✓
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Specific tool names with precise methodology context throughout responsibilities (dbt models, BigQuery queries, Metabase dashboards) indicate hands-on domain knowledge in the author.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "designing and evolving the analytical layer used across the organisation"
> Verified: ✓ found in JD
> Reasoning: The role is framed around building/maintaining analytics infrastructure and defining standards for data consumers, not serving commercial, product, or finance functions directly.

**Run 2:** `internal_data` ✓
> Quote: "ensure consistent, actionable information organisation-wide"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building reliable analytical infrastructure (models, metrics, dashboards) that serves the entire organization's data needs, not a specific business function.

**Run 3:** `internal_data` ✓
> Quote: "designing and evolving the analytical layer used across the organisation"
> Verified: ✓ found in JD
> Reasoning: The role is focused on building and maintaining the shared analytical infrastructure that enables internal analytics consumers, not serving a specific business function.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "work closely with the Data Team Lead, Senior Data Engineer, and business teams"
> Verified: ✓ found in JD
> Reasoning: The role is scoped to build and maintain the analytical layer through collaboration with leadership rather than setting strategic direction independently.

**Run 2:** `mixed` ✓
> Quote: "focuses on designing and evolving the analytical layer"
> Verified: ✓ found in JD
> Reasoning: The role balances strategic ownership (designing models, defining metrics standards) with execution of specific projects (building dashboards, implementing testing frameworks).

**Run 3:** `execution` ✗
> Quote: "Collaborate with non-technical teams to translate business needs into scalable solutions"
> Verified: ✓ found in JD
> Reasoning: The role is positioned as executing technical solutions within an established team structure with leadership already in place, not strategically driving analytics direction.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI coding tools, AI-enabler data infrastructure, or AI/ML pipelines anywhere in the JD.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-powered infrastructure, or AI-related capabilities required of the candidate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI skills, tools, or methodologies expected of the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Testing and data validation are framed as an owned responsibility (Implement) rather than a listed tool requirement or absent entirely.

**Run 2:** `responsibility` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: The action verb 'implement' frames testing and data validation as an owned responsibility the candidate is accountable for establishing.

**Run 3:** `responsibility` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: The verb 'implement' frames testing and data validation as something the candidate owns and is accountable for, not merely a tool to use.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "focus on traceability and quality; Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Reliability and data accuracy are emphasized through testing and quality focus, indicating operational reliability is a concern, but without explicit compliance or regulatory risk framing.

**Run 2:** `moderate` ✗
> Quote: "Implement testing and data validation processes within dbt"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are operational priorities (testing, validation, consistency), indicating concern for analytics stability rather than compliance or catastrophic-risk prevention.

**Run 3:** `moderate` ✗
> Quote: "ensure consistent, actionable information organisation-wide"
> Verified: ✓ found in JD
> Reasoning: Reliability and consistency are mentioned as important characteristics but secondary to delivery focus, without framing around preventing regulatory or stakeholder-trust risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
