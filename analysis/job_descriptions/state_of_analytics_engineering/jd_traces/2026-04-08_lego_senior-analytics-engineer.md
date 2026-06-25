# Trace: 2026-04-08_lego_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — The LEGO Group

**URL:** https://www.lego.com/de-de/careers/job/senior-analytics-engineer-a3245e08168b1000dbc6187d0c820000  
**Location:** Billund, Denmark or Boston, Massachusetts, United States  
**Date Posted:** April 6, 2026  
**Valid Through:** May 6, 2026  
**Job ID:** 0000032938  
**Category:** Data & Analytics  
**Salary:** $107,885–$161,827 (based on responsibilities, market benchmarks, and organizational constraints)

---

## Job Description

Are you ready to join an energetic, pioneering data and analytics enablement team, as part of a company wide digital transformation and entering into a new era of Analytics & Insights?

Our Commercial A&I function is recognized by the executive leadership team for spearheading the growth in analytics maturity at the LEGO Group, and driving quantifiable commercial value through data and insights!

---

## Core Responsibilities

- Build data pipeline engineering, orchestration, and monitoring to deliver high-quality data products centered around Retail Execution Commercial pillar.
- Ensure Data Products follow CI/CD standards, adhere to data quality frameworks; include assertion checks and have performance & cost optimization applied.
- Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization.
- Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment.
- Collaborate closely with the Analytics Interface, Commercial Analytics and business teams to turn business requirements into productionised AI-enabling data products.
- Enable Markets & Channels specific data understanding and champion data literacy via guidelines, training, drop-in sessions, documentation, and knowledge sharing.
- Partner with the Analytics Innovation & Automation and Data Office product teams to prototype & deliver innovative features across the Data Platform; ensure platforms, tools & processes meet business needs.
- Collaborate with Shopper & Partner (D2C & B2B) digital product teams to ensure high quality data is collected and published to LEGO Data Platform (Databricks) to a standard fit for purpose for downstream delivery of data products.
- Consistently champion best practices in data product development within the team, across Markets & Channels and with the broader analytics community, helping ensure data integrity, quality, and scalability of overall data products on the LEGO Data Platform.

---

## Play Your Part in Our Team Succeeding

The overall department's key focus is to enable self-service data products for Markets & Channels (Commercial) data consumers and decision makers; helping shape data-driven actions both for operational optimization purposes and tactical and strategical decision recommendations. Within this mandate, the Analytics Engineering team's responsibility is to build an AI-enabled data foundation the entire company can rely on.

The key partners of this role will be focused on our A&I and broader Commercial organization but have potential to expand to be multifunctional in areas such as Data Science, Marketing, Finance, Operations, etc.

This role is essential as we strive to build a world-class analytics organization, capable of delivering scalable data products, AI-driven insights and real decision intelligence.

---

## Do You Have What It Takes?

### Required Qualifications

- Analytics Engineer, Data Solutions, Data Engineering and/or Data Specialist experience.
- Strong skills in SQL and/or Python or similar experience in manipulating large structured and unstructured datasets.
- Experience working with CI/CD pipelines, Git and knowledge of data transformation best practices.
- Can provide technical context and direction, translating technical constraints / trade-offs to people within non-technical roles, including senior leadership.
- Thorough and meticulous, strong adaptability and focus to deliver resul…[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 8 | 9 | 6 | 5 | 0% | ✗ |
| data_team_maturity | mid | mature | mature | mid | 33% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | mixed | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Ensure Data Products follow CI/CD standards, adhere to data quality frameworks; include assertion checks and have performance & cost optimization applied."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality frameworks, assertion checks, CI/CD standards, and compliance as core expectations rather than speed or iteration pace.

**Run 2:** `rigour` ✓
> Quote: "Ensure Data Products follow CI/CD standards, adhere to data quality frameworks; include assertion checks and have performance & cost optimization applied."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality frameworks, CI/CD standards, assertion checks, governance, best practices, and data integrity throughout, with no velocity or speed-focused language present.

**Run 3:** `rigour` ✓
> Quote: "Ensure Data Products follow CI/CD standards, adhere to data quality frameworks; include assertion checks and have performance & cost optimization applied."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, CI/CD standards, assertion checks, governance, and data integrity rather than speed or iteration pace.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "the Analytics Engineering team's responsibility is to build an AI-enabled data foundation the entire company can rely on"
> Verified: ✓ found in JD
> Reasoning: While the data foundation is critical to business operations, LEGO is a retail/consumer company without the financial reporting or regulatory compliance risk of banking, fintech, or healthcare sectors.

**Run 2:** `moderate` ✓
> Quote: "turn business requirements into productionised AI-enabling data products"
> Verified: ✓ found in JD
> Reasoning: The role drives commercial and operational decision-making at a consumer goods company without explicit financial reporting, regulatory, or compliance risk signals.

**Run 3:** `moderate` ✓
> Quote: "highly controlled compliant environment"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance and compliance for retail/commercial analytics without explicit financial reporting, regulatory, or audit language typical of high-risk financial or compliance roles.

### collaboration_width
**Manual:** `8`

**Run 1:** `9` ✗
> Quote: "Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office; Shopper & Partner (D2C & B2B) digital product teams; Data Science; Marketing; Finance; Operations"
> Verified: ⚠ NOT found verbatim
> Reasoning: Nine distinct named partner teams or functions are explicitly listed: four analytics sub-teams in the responsibilities section plus five cross-functional areas mentioned in the partnership expansion section.

**Run 2:** `6` ✗
> Quote: "Analytics Interface; Commercial Analytics; Markets & Channels; Analytics Innovation & Automation; Data Office product teams; Shopper & Partner (D2C & B2B) digital product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct named teams or functions are explicitly listed in the responsibilities section as direct collaboration partners.

**Run 3:** `5` ✗
> Quote: "Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office; Shopper & Partner (D2C & B2B) digital product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Five distinct named teams are explicitly listed as collaboration partners across the responsibilities section.

⚠ **Disagreement**: manual=`8` vs LLM majority=`9`

⚠ **LLM inconsistency**: runs gave ['9', '6', '5']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mature` ✗
> Quote: "Our Commercial A&I function is recognized by the executive leadership team for spearheading the growth in analytics maturity at the LEGO Group, and driving quantifiable commercial value through data and insights!"
> Verified: ✓ found in JD
> Reasoning: The function is established and recognized at executive level with multiple named sub-teams, existing platforms (Databricks), and governance structures (Unity Catalog) already in place.

**Run 2:** `mature` ✗
> Quote: "Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment; Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization"
> Verified: ⚠ NOT found verbatim
> Reasoning: Multiple named data sub-teams with specialized charters, established platforms (Databricks, Unity Catalog), and governance infrastructure at scale indicate a mature, established data organization.

**Run 3:** `mid` ✓
> Quote: "spearheading the growth in analytics maturity at the LEGO Group"
> Verified: ✓ found in JD
> Reasoning: Multiple established teams and named tools (Databricks, Unity Catalog, semantic layer) exist, with the focus on scaling and growth rather than greenfield build or fully mature operations.

⚠ **Disagreement**: manual=`mid` vs LLM majority=`mature`

⚠ **LLM inconsistency**: runs gave ['mature', 'mature', 'mid']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical terminology and methodologies (semantic layer, metric view pipelines, materialization, Unity Catalog governance) that demonstrate knowledge of the work from someone who does it.

**Run 2:** `mixed` ✗
> Quote: "Build and maintain semantic layer infrastructure including metric view pipelines, materialization and optimization"
> Verified: ✓ found in JD
> Reasoning: Specific technical terms (semantic layer, metric views, materialization, Unity Catalog, CI/CD, assertion checks) indicate domain expertise, but these are mixed throughout with generic collaboration boilerplate ("collaborate closely with", "champion best practices") typical of recruiter involvement.

**Run 3:** `mixed` ✗
> Quote: "Ensure Data Products follow CI/CD standards, adhere to data quality frameworks; include assertion checks and have performance & cost optimization applied."
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical language (CI/CD, data quality frameworks, assertion checks, semantic layer infrastructure, Unity Catalog) and tool context alongside generic boilerplate phrases (collaborate closely, champion best practices, prototype & deliver).

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']
