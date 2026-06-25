# Trace: 2026-04-22_statista_analytics-engineer-reporting-platform

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer - Reporting Platform (m/f/d) — Statista

**URL:** https://jobs.ashbyhq.com/statista/daa5811c-c67e-4fdc-abf9-e96b68a5269d
**Location:** Hamburg or Berlin, Germany
**Employment Type:** Full-Time
**Workplace Type:** Hybrid (Work from abroad up to 30 calendar days per year)

---

## Key Responsibilities

- Be the first point of contact for administration topics around the reporting platform, e.g. architecture questions, permission management and specific reporting issues.
- Analyze reporting usage and help identify opportunities for optimization and cleanup.
- Increase transparency around data sources, KPI definitions, and report ownership.
- Support documentation and governance efforts to improve maintainability and trust in reporting assets.
- Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools.
- Improve consistency and usability of reports through establishing shared standards, templates, and best practices.
- Design, develop, and deploy reports and dashboards powered by our Data Warehouse.

---

## Required Qualifications

- 3+ years of relevant experience in analytics, BI, or analytics engineering.
- Hands-on experience with Power BI (or comparable BI tools).
- Solid SQL skills, understanding of data modeling concepts and experience working with a data warehouse (e.g. Snowflake, Redshift, …).
- A structured, quality-focused mindset and genuine interest in standards and data governance topics.
- Curiosity and openness to learning new tools and modern analytics approaches.
- Excellent communication skills in English (written and spoken).

---

## Preferred / Bonus Skills

- Experience with migrating BI tools is a plus.
- German proficiency is a plus.

---

## Benefits

- Work from abroad up to 30 calendar days a year
- Hybrid work and flex-time
- International team and social events
- Subsidized urban mobility and access to fitness and wellness options
- Free access to Langdock and all its amazing functionalities
- Career & training opportunities
- Attractive locations and modern offices
- Mental health support with OpenUp

---

## Company Description

At Statista, we're all about facts and data, for we are the world's leading business data platform. By providing reliable and easy-to-use data as well as various data analytics products and services, we empower people worldwide to make fact-based decisions. Founded in Hamburg in 2007, we have quickly grown into a global company with offices in major cities such as London, New York, Berlin and Tokyo.

Statista's central Data team is building the foundation for a truly data-driven organization. Our reporting platform is one of the key channels we use to bring data to life for the business. While our current solution is based on Power BI, we are reassessing our BI stack and evaluating different modern analytics and visualization solutions for the future.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | low | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 4 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | mixed | mixed | hiring_manager | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Multiple signals emphasize governance, documentation, maintainability, and trust as core expectations with no counterbalancing velocity language present.

**Run 2:** `rigour` ✓
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, documentation, standards, and trust as core expectations with no corresponding velocity or speed-focused language present.

**Run 3:** `rigour` ✓
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: The emphasis on governance, documentation, trust, and standards are core rigour signals with no offsetting velocity language.

### domain_risk
**Manual:** `low`

**Run 1:** `moderate` ✗
> Quote: "our reporting platform is one of the key channels we use to bring data to life for the business"
> Verified: ✓ found in JD
> Reasoning: Language indicates internal business intelligence and reporting without explicit financial reporting, regulatory compliance, or audit signals, suggesting moderate risk where errors affect decisions but lack immediate regulatory consequences.

**Run 2:** `moderate` ✗
> Quote: "Increase transparency around data sources, KPI definitions, and report ownership."
> Verified: ✓ found in JD
> Reasoning: The role supports business stakeholder decision-making but lacks explicit financial reporting, compliance, or regulatory language that would signal high risk.

**Run 3:** `moderate` ✗
> Quote: "Our reporting platform is one of the key channels we use to bring data to life for the business."
> Verified: ✓ found in JD
> Reasoning: Internal business reporting affects decisions but lacks explicit financial reporting, compliance, or regulatory language indicating high risk.

⚠ **Disagreement**: manual=`low` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `0` ✗
> Quote: "N/A"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams, functions, or role cohorts appear in the responsibilities; generic references like 'the business' are excluded by definition.

**Run 2:** `0` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: No distinct named teams, functions, or roles (Finance, Product, Engineering, etc.) are explicitly identified as collaboration partners in the responsibilities.

**Run 3:** `0` ✗
> Quote: "Be the first point of contact for administration topics around the reporting platform, e.g. architecture questions, permission management and specific reporting issues."
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams or functions (Finance, Product, Engineering, etc.) are listed in the JD.

⚠ **Disagreement**: manual=`4` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "While our current solution is based on Power BI, we are reassessing our BI stack and evaluating different modern analytics and visualization solutions for the future."
> Verified: ✓ found in JD
> Reasoning: Presence of an established, named BI solution actively undergoing modernization indicates a mid-stage team with proven infrastructure expanding its capabilities, not early greenfield or mature scaled operations.

**Run 2:** `mid` ✓
> Quote: "While our current solution is based on Power BI, we are reassessing our BI stack and evaluating different modern analytics and visualization solutions for the future."
> Verified: ✓ found in JD
> Reasoning: Named tools (Power BI, Data Warehouse) appear in responsibilities with active modernization underway, indicating an established function evolving beyond greenfield but not yet at mature/scaled governance.

**Run 3:** `mid` ✓
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: The existence of established infrastructure (Power BI, Data Warehouse) undergoing modernization indicates a data function that exists but is actively improving.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: This responsibility demonstrates specific contextual knowledge of an actual modernization project a hiring manager would know, balanced against generic governance and stakeholder language that appears recruiter-authored throughout.

**Run 2:** `mixed` ✓
> Quote: "Be the first point of contact for administration topics around the reporting platform, e.g. architecture questions, permission management and specific reporting issues."
> Verified: ✓ found in JD
> Reasoning: This responsibility shows hiring-manager-level specificity (administration, permission management, architecture), but other responsibilities rely heavily on generic boilerplate (establish standards, improve consistency, best practices).

**Run 3:** `hiring_manager` ✗
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: The specific context about their BI stack situation, Power BI usage, and modernization efforts shows technical knowledge only a hiring manager would possess.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']
