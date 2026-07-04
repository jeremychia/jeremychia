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
| jd_authorship | mixed | recruiter | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | execution | execution | execution | 100% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "A structured, quality-focused mindset and genuine interest in standards and data governance topics."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, standards, trust, and quality throughout with no velocity language (fast-paced, ship quickly, iteration speed), making rigour the clear orientation.

**Run 2:** `rigour` ✓
> Quote: "A structured, quality-focused mindset and genuine interest in standards and data governance topics."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data governance, standards, transparency, trust, and maintainability throughout, with no velocity or shipping-oriented language.

**Run 3:** `rigour` ✓
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Multiple governance, standards, consistency, and trust signals dominate the responsibilities with no velocity language present.

### domain_risk
**Manual:** `low`

**Run 1:** `moderate` ✗
> Quote: "Increase transparency around data sources, KPI definitions, and report ownership."
> Verified: ✓ found in JD
> Reasoning: This is an internal BI role affecting business decisions and reporting accuracy, but without financial reporting, regulatory compliance, or customer-facing product responsibilities.

**Run 2:** `moderate` ✗
> Quote: "Increase transparency around data sources, KPI definitions, and report ownership."
> Verified: ✓ found in JD
> Reasoning: This is a business intelligence role focused on reporting platform administration where errors affect business decisions but not regulatory compliance or financial reporting.

**Run 3:** `moderate` ✗
> Quote: "Improve consistency and usability of reports through establishing shared standards, templates, and best practices."
> Verified: ✓ found in JD
> Reasoning: Role focuses on internal reporting operations without financial reporting, compliance, or regulatory language.

⚠ **Disagreement**: manual=`low` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `0` ✗
> Quote: "No named partner teams explicitly identified in responsibilities"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities describe collaboration (first point of contact, supporting governance) but do not name specific partner teams or business functions.

**Run 2:** `0` ✗
> Quote: "No explicitly named partner teams identified in the responsibilities or qualifications sections."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD describes the role's technical scope and deliverables but does not explicitly name which teams or functions this role collaborates with.

**Run 3:** `0` ✗
> Quote: "None"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams or functions appear in the responsibilities or requirements sections.

⚠ **Disagreement**: manual=`4` vs LLM majority=`0`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: Named tools (Power BI, Snowflake, Redshift) and modernization efforts indicate an existing data function with infrastructure being improved, not early-stage or fully mature.

**Run 2:** `mid` ✓
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: The JD references an existing Power BI-based platform and established Data Warehouse, with ongoing evolution and tool evaluation characteristic of a maturing team.

**Run 3:** `mid` ✓
> Quote: "Statista's central Data team is building the foundation for a truly data-driven organization. Our reporting platform is one of the key channels we use to bring data to life for the business."
> Verified: ✓ found in JD
> Reasoning: Established data infrastructure exists (Power BI, Data Warehouse) and role supports modernization of an existing platform, indicating mid-stage maturity.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `recruiter` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Generic action verbs (support, improve, increase, establish) lack technical specificity about what the candidate actually does on a Tuesday morning; no hiring-manager detail.

**Run 2:** `mixed` ✓
> Quote: "Hands-on experience with Power BI (or comparable BI tools). Solid SQL skills, understanding of data modeling concepts and experience working with a data warehouse (e.g. Snowflake, Redshift, …)."
> Verified: ⚠ NOT found verbatim
> Reasoning: The requirements list specific tools (Power BI, Snowflake, Redshift) indicating hiring manager input, but the responsibilities themselves contain generic boilerplate language about administration and support.

**Run 3:** `recruiter` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic governance and administrative language without technical specificity about actual day-to-day work or scale.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: The role focuses on platform administration, governance, and infrastructure modernization serving the data function and reporting platform consumers, not commercial, product, or finance stakeholders.

**Run 2:** `internal_data` ✓
> Quote: "Support the ongoing modernization of the BI stack, including evaluating and testing alternative analytics and visualization tools."
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is on reporting platform governance, standards, modernization, and infrastructure serving internal analytics consumers rather than specific business functions.

**Run 3:** `internal_data` ✓
> Quote: "Be the first point of contact for administration topics around the reporting platform, e.g. architecture questions, permission management and specific reporting issues."
> Verified: ✓ found in JD
> Reasoning: Role serves the reporting platform and its internal users, not commercial, product, or finance teams.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Support the ongoing modernization of the BI stack"
> Verified: ✓ found in JD
> Reasoning: The 'support' verb indicates executing a direction (BI stack modernization) set by others rather than defining strategy or owning priorities independently.

**Run 2:** `execution` ✗
> Quote: "Support the ongoing modernization of the BI stack"
> Verified: ✓ found in JD
> Reasoning: The repeated use of 'support' indicates execution within a modernization strategy set by others, with tactical input on standards but not strategic direction-setting.

**Run 3:** `execution` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Role is framed around supporting existing initiatives and improving current state rather than defining strategy or direction.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No candidate AI skills are required in responsibilities or qualifications; Langdock is offered as a benefits perk but not as a required competency.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, or AI-related capabilities expected of the candidate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, coding agents, or AI-ready data foundations; generic learning openness is not AI-specific.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No mention of testing, data quality, or observability frameworks."
> Verified: ⚠ NOT found verbatim
> Reasoning: Testing tools, data quality practices, or observability frameworks do not appear as candidate responsibilities, required skills, or technical knowledge areas.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality framework mentioned."
> Verified: ⚠ NOT found verbatim
> Reasoning: While quality and governance are valued as mindset requirements, the JD does not mention testing practices, data quality frameworks, or testing tools as responsibilities or requirements.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality ownership framing appears in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of testing, data contracts, observability, or data quality frameworks in responsibilities or requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Trust, transparency, and governance language indicate concern for preventing data failures and operational reliability, but absence of regulatory, compliance, or audit language keeps this moderate rather than high.

**Run 2:** `moderate` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes trust in reporting assets and governance concerns, indicating risk aversion toward bad data reaching stakeholders, but lacks regulatory or compliance framing.

**Run 3:** `moderate` ✗
> Quote: "Support documentation and governance efforts to improve maintainability and trust in reporting assets."
> Verified: ✓ found in JD
> Reasoning: Trust and governance are present but framed as practices to establish and maintain, not as risk prevention or compliance requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
