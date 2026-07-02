# Trace: 2026-07-02_photowall_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Photowall

**URL:** https://career.photowall.com/jobs/7750533-analytics-engineer
**Location:** Stockholm, Hybrid
**Date Posted:** 2026-07-02

---

# Analytics Engineer - Photowall

Company: Photowall
Location: Stockholm, Hybrid (3 days office, 2 days remote)
Salary: Not stated

## Responsibilities
Data Infrastructure & Pipelines
- Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation
- Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse
- Build and maintain scalable data models serving both marketing and product use cases
- Establish monitoring and documentation protocols for data reliability

Analytics & Dashboards
- Design and maintain dashboards for Growth, Marketing, and Product teams
- Conduct ad-hoc analysis and executive reporting
- Support A/B testing and experimentation workflows

Event Tracking & Digital Analytics
- Implement event tracking via Google Tag Manager (GTM) and GA4
- Manage funnel analysis and cross-web tracking quality assurance

First-Party Data & Marketing Measurement
- Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels
- Support attribution modeling and channel performance analysis

## Requirements
- 4-6 years in data analytics, analytics engineering, or hybrid role in e-commerce
- Strong SQL and BigQuery expertise; experience with dbt, Dataform, or similar transformation tools
- Proficiency with Looker (or a similar BI tool) and Funnel
- Strong communication skills - comfortable explaining technical concepts to non-technical stakeholders
- Fluent English

Nice to have: GA4, GTM experience; CRM and paid media platform familiarity

Interview Process & Team Structure: Not specified in posting

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
| jd_authorship | hiring_manager | hiring_manager | mixed | 33% |
| stakeholder_orientation | mixed | mixed | commercial | 33% |
| autonomy_level | execution | mixed | execution | 33% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality validation, monitoring, and reliability as core expectations with no counterbalancing velocity signals.

**Run 2:** `rigour`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality validation, monitoring, and reliability throughout with no counterbalancing velocity language.

**Run 3:** `rigour`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality validation, monitoring, documentation, and reliability as core expectations, with no velocity-oriented language about speed or iteration.

### domain_risk

**Run 1:** `moderate`
> Quote: "Build and maintain scalable data models serving both marketing and product use cases"
> Verified: ✓ found in JD
> Reasoning: E-commerce context with business decision support focus but no financial reporting, compliance, or regulatory language, typical of moderate-risk roles.

**Run 2:** `moderate`
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: E-commerce marketing analytics where data errors affect revenue operations and customer decisions, but without explicit financial reporting, compliance, or regulatory risk language.

**Run 3:** `moderate`
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: The role supports marketing and product decisions in an e-commerce context without explicit financial reporting, regulatory, or compliance language, placing it at typical e-commerce/SaaS risk level.

### collaboration_width

**Run 1:** `3`
> Quote: "Growth; Marketing; Product"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct teams explicitly named in responsibilities: Growth, Marketing, and Product teams.

**Run 2:** `3`
> Quote: "Growth; Marketing; Product"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct teams as collaboration partners for analytics delivery and dashboards.

**Run 3:** `3`
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct partner teams: Growth, Marketing, and Product.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build and maintain scalable data models serving both marketing and product use cases"
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure and named tools in responsibilities (BigQuery, GA4, Klaviyo, GTM) indicate an operational data function growing and scaling, not early-stage or mature enterprise.

**Run 2:** `mid`
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation"
> Verified: ✓ found in JD
> Reasoning: The role involves maintaining existing infrastructure (BigQuery, GA4, dbt) and scaling it rather than establishing from zero or joining a fully mature established organization.

**Run 3:** `mid`
> Quote: "Build and maintain scalable data models serving both marketing and product use cases"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (BigQuery, dbt/Dataform, Looker) combined with existing infrastructure and multiple named use cases indicate an established data function in growth phase.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: Technical specificity around how tools are applied (Klaviyo CRM integration, paid media measurement) and methodologies (attribution modeling, funnel analysis) indicates someone who does this work.

**Run 2:** `hiring_manager`
> Quote: "Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse"
> Verified: ✓ found in JD
> Reasoning: The precise naming of specific tools with their integration context and the specific transformation targets indicates technical specificity that comes from hands-on experience.

**Run 3:** `mixed`
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation"
> Verified: ✓ found in JD
> Reasoning: The JD combines specific technical context (BigQuery, GA4, Klaviyo, GTM, Looker with precise applications) with generic support verbs (support, conduct, design) typical of recruiter-drafted text.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams"
> Verified: ✓ found in JD
> Reasoning: The explicitly named teams span both commercial (Growth, Marketing) and product (Product), with additional commercial infrastructure work (CRM, paid media measurement) creating genuinely mixed emphasis.

**Run 2:** `mixed`
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams; Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role serves Product teams with A/B testing and experimentation support and Commercial teams with attribution modeling and CRM infrastructure with comparable emphasis.

**Run 3:** `commercial`
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: The prominent 'First-Party Data & Marketing Measurement' section and explicit focus on CRM, paid media, attribution modeling, and channel performance indicate commercial/marketing stakeholders are primary.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'commercial']

### autonomy_level

**Run 1:** `execution`
> Quote: "Support A/B testing and experimentation workflows"
> Verified: ✓ found in JD
> Reasoning: While the role includes ownership of technical domains (pipelines, dashboards), the strategic direction is set by pre-defined business stakeholder needs rather than by the role holder.

**Run 2:** `mixed`
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation; Support A/B testing and experimentation workflows"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic ownership of data infrastructure (own, build, establish) with execution support for business teams' analytical workflows.

**Run 3:** `execution`
> Quote: "Support A/B testing and experimentation workflows"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs (own, establish) are limited to technical sub-domains while business priorities are framed with support language, indicating the role executes against direction set by others.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI coding tools, generative AI, machine learning, or AI-related capabilities expected of the candidate throughout the JD.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mentions of AI/ML skills, AI-assisted coding tools, or AI data infrastructure expectations.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No AI skill, tool, or framework is mentioned anywhere in the JD; all requirements are traditional data analytics and engineering skills.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation"
> Verified: ✓ found in JD
> Reasoning: Data quality validation is framed as a core responsibility the candidate owns, not merely a tool or framework to use.

**Run 2:** `responsibility`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The ownership verb 'establish' frames data reliability practices as something the analyst owns and defines, rather than tools in a tech stack.

**Run 3:** `responsibility`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Data quality validation and reliability are framed as responsibilities the role owns and establishes, not as tools listed in a requirements checklist.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality are ongoing concerns, but without compliance, audit, or high-stakes trust framing that would indicate high loss aversion.

**Run 2:** `moderate`
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Data reliability and quality are named concerns with dedicated operational responsibilities, but the JD frames them as capability delivery rather than preventing bad outcomes or managing compliance risk.

**Run 3:** `moderate`
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation"
> Verified: ✓ found in JD
> Reasoning: The JD reflects concern for operational reliability and preventing data failures through monitoring and quality validation, but lacks compliance or stakeholder trust language associated with high loss-aversion.
