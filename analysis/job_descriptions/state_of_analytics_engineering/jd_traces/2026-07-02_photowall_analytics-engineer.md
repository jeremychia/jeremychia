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

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 2 | 3 | 3 | 3 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | mixed | hiring_manager | 33% | ✓ |
| stakeholder_orientation | commercial | commercial | mixed | commercial | 33% | ✓ |
| autonomy_level | mixed | execution | mixed | execution | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality validation, monitoring, and documentation for reliability without any competing velocity language.

**Run 2:** `rigour` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality validation, monitoring, and reliability as core responsibilities with no velocity language like fast-paced or rapid delivery.

**Run 3:** `rigour` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals dominate (data quality validation, monitoring, documentation, data reliability, quality assurance) with zero velocity signals like fast-paced or rapid delivery.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: The role affects marketing and product business decisions but lacks regulatory, compliance, or financial reporting language that would indicate high risk.

**Run 2:** `moderate` ✓
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: E-commerce analytics affecting marketing and growth decisions carries moderate risk to business operations but no regulatory or financial reporting exposure.

**Run 3:** `moderate` ✓
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: E-commerce role affecting marketing and business decisions without explicit financial reporting or regulatory compliance consequences.

### collaboration_width
**Manual:** `2`

**Run 1:** `3` ✗
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct partner functions that the role collaborates with.

**Run 2:** `3` ✗
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams are explicitly identified as collaboration partners: Growth, Marketing, and Product.

**Run 3:** `3` ✗
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams (Growth, Marketing, Product) are explicitly identified as collaboration partners.

⚠ **Disagreement**: manual=`2` vs LLM majority=`3`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse"
> Verified: ✓ found in JD
> Reasoning: Multiple named data sources and existing infrastructure indicate a team beyond early stage, but establishing new monitoring protocols suggests ongoing growth rather than mature scale.

**Run 2:** `mid` ✓
> Quote: "Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse"
> Verified: ✓ found in JD
> Reasoning: Named tools and platforms in responsibilities indicate established infrastructure; the role scales and maintains existing systems rather than building from zero.

**Run 3:** `mid` ✓
> Quote: "Build and maintain scalable data models serving both marketing and product use cases"
> Verified: ✓ found in JD
> Reasoning: Named tools (BigQuery, dbt/Dataform) and infrastructure exist in responsibilities with multiple established use cases, indicating mid-stage maturity.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse"
> Verified: ✓ found in JD
> Reasoning: The specific naming of data sources and systems demonstrates technical understanding of the actual data infrastructure rather than generic boilerplate.

**Run 2:** `mixed` ✗
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation; Support A/B testing and experimentation workflows"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about named tools and their contexts (BigQuery pipelines, GA4, GTM) is balanced by generic support verbs and generic action phrases.

**Run 3:** `hiring_manager` ✓
> Quote: "Integrate data from GA4, Klaviyo, marketing platforms, and backend systems into a centralized warehouse"
> Verified: ✓ found in JD
> Reasoning: Specific integration context, named data sources, technical scope, and business methodology (attribution modeling, funnel analysis) indicate someone with hands-on experience writing this.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `commercial` ✓
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: While the role supports product teams, the majority of specific responsibilities focus on marketing infrastructure and revenue operations.

**Run 2:** `mixed` ✗
> Quote: "Design and maintain dashboards for Growth, Marketing, and Product teams; Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels; Support A/B testing and experimentation workflows"
> Verified: ✓ found in JD
> Reasoning: Responsibilities split between commercial audiences (CRM, paid media, attribution) and product audiences (A/B testing, experimentation) with genuinely equal emphasis.

**Run 3:** `commercial` ✓
> Quote: "Build and maintain the data infrastructure that feeds CRM (Klaviyo) and paid media channels"
> Verified: ✓ found in JD
> Reasoning: Commercial outcomes (marketing measurement, attribution, paid media, CRM) dominate across two dedicated sections and multiple responsibilities, while product analytics is secondary.

⚠ **LLM inconsistency**: runs gave ['commercial', 'mixed', 'commercial']

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation"
> Verified: ✓ found in JD
> Reasoning: The role has ownership and some autonomy in establishing monitoring protocols, but the primary framing is maintaining and supporting existing infrastructure rather than defining strategic direction.

**Run 2:** `mixed` ✓
> Quote: "Own and maintain BigQuery data pipelines; Establish monitoring and documentation protocols; Support A/B testing and experimentation workflows"
> Verified: ✓ found in JD
> Reasoning: The role owns the data infrastructure domain and establishes protocols (strategic) but supports defined business processes like A/B testing (execution).

**Run 3:** `execution` ✗
> Quote: "Support A/B testing and experimentation workflows"
> Verified: ✓ found in JD
> Reasoning: While technical responsibilities use strategic verbs (build, own, establish), the scope, priorities, and stakeholder teams are predefined by business teams, positioning this as execution within defined domains.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI or AI-related expectations for the candidate.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, or AI-ready data infrastructure.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, AI-first mindset, AI-ready data infrastructure, or GenAI applications in the JD.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as something the candidate owns and defines, not as tools in a skill list.

**Run 2:** `responsibility` ✗
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation; Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Data quality validation and reliability are framed as responsibilities the candidate owns with action verbs, not as tools listed in a requirements section.

**Run 3:** `responsibility` ✗
> Quote: "Own and maintain BigQuery data pipelines, including scheduling, monitoring, and data quality validation"
> Verified: ✓ found in JD
> Reasoning: Data quality validation and monitoring are framed as owned responsibilities with action verb 'own', not as tools listed in requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and data quality but lacks the regulatory, compliance, or stakeholder-trust language that would indicate high loss aversion.

**Run 2:** `moderate` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality are concerns secondary to delivery responsibilities; the fear is pipeline failures, not regulatory or stakeholder trust risk.

**Run 3:** `moderate` ✗
> Quote: "Establish monitoring and documentation protocols for data reliability"
> Verified: ✓ found in JD
> Reasoning: Operational reliability is a stated concern framed as protocol establishment and maintenance, but without loss-aversion language about preventing catastrophe or regulatory risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
