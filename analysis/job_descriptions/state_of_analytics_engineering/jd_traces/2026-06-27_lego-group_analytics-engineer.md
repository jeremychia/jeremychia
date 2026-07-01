# Trace: 2026-06-27_lego-group_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — The LEGO Group

**Location:** Billund, Denmark; London, United Kingdom
**Date Posted:** 2026-06-27

---

Analytics Engineer

Management Level: Lead Professional

Job ID: 0000035262

Category: Data & Analytics

Locations:
- Billund, Denmark
- London, United Kingdom

Are you interested in being a key contributor in enabling our Markets & Channels organisation to understand its commercial impact deeply and expand data transparency to drive data driven decisions that always put the shopper first?

Bring your understanding of data platforms together with your retail knowledge and natural curiosity into play in this role to be part of a pioneering data and analytics team bringing digital transformation to life in our commercial areas!

Core Responsibilities

- Build data pipeline engineering, orchestration, and monitoring to deliver high-quality data products centred around one of our three Commercial Domain pillars.

- Ensure Data Products follow CI/CD best practice, adhere to data quality frameworks; include assertion checks and have performance & cost optimisation applied.

- Build and maintain semantic layer infrastructure including metric view pipelines, materialisation and optimisation

- Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment

- Collaborate closely with the Analytics Interface, Commercial Analytics and business teams to turn business requirements into productionised AI-enabling data products.

- Enable Markets & Channels specific data understanding and champion data literacy via guidelines, training, drop-in sessions, documentation, and knowledge sharing.

- Partner with the Analytics Innovation & Automation and Data Office Product teams to prototype & deliver cutting edge features across the Data Platform; ensure platforms, tools & processes meet business needs

- Collaborate with Shopper & Partner (D2C & B2B) digital product teams to ensure high-quality data is collected and published to LEGO Data Platform (Databricks) to a standard fit for purpose for downstream delivery of data products.

- Consistently champion best practices in data product development within the team, across Markets & Channels and with the broader analytics community, helping ensure data integrity, -quality, and -scalability of overall data products on the LEGO Data Platform.

Play your part in our team succeeding!

The overall department's key focus is to enable self-service data products for Markets & Channels (Commercial) data consumers and decision makers; helping shape data-driven actions both for operational optimisation purposes and tactical and strategical decision recommendations. Within this mandate, the Analytics Engineering team's responsibility is to build an AI-enabled data foundation the entire company can rely on.

The key stakeholders of this role will be focused on our A&I and broader Commercial organisation but have potential to expand to be multifunctional in areas such as Data Science, Marketing, Finance, Operations, etc.

This role is essential as we strive to build a world-class analytics organization, capable of delivering scalable data products, AI-driven insights and real decision intelligence.

Do you have what it takes?

- Analytics Engineer, Data Solutions, Data Engineering and/or Data Specialist experience.

- Strong SQL and/or Python skills or similar experience in manipulating large structured and unstructured datasets.

- Working knowledge of CI/CD pipelines, Git and data transformation best practices.

- Ability to translate technical constraints / trade-offs to people within non-technical roles.

- Thorough and detail-oriented, strong adaptability and focus to deliver results.

- Self-driven, with the ability to deliver towards large initiatives as part of a cross-functional squad.

- Strong collaborative personality with a #OneTeam mindset.

- Positive can-do attitude, with natural curiosity and…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 5 | 5 | 9 | 33% |
| data_team_maturity | mid | mid | mature | 33% |
| jd_authorship | mixed | hiring_manager | mixed | 33% |
| stakeholder_orientation | commercial | commercial | internal_data | 33% |
| autonomy_level | mixed | execution | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Ensure Data Products follow CI/CD best practice, adhere to data quality frameworks; include assertion checks and have performance & cost optimisation applied."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality frameworks, assertion checks, governance, compliance, and best practices as core expectations, with no countervailing velocity language.

**Run 2:** `rigour`
> Quote: "Ensure Data Products follow CI/CD best practice, adhere to data quality frameworks; include assertion checks and have performance & cost optimisation applied."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes quality frameworks, CI/CD best practices, assertion checks, and data integrity with no velocity language, indicating a rigour-focused orientation.

**Run 3:** `rigour`
> Quote: "Ensure Data Products follow CI/CD best practice, adhere to data quality frameworks; include assertion checks and have performance & cost optimisation applied."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, CI/CD best practices, assertion checks, and governance as core expectations with no velocity language present.

### domain_risk

**Run 1:** `moderate`
> Quote: "Markets & Channels organisation to understand its commercial impact deeply and expand data transparency to drive data driven decisions"
> Verified: ✓ found in JD
> Reasoning: The role supports commercial and operational decision-making without explicit financial reporting, regulatory, or compliance language that would elevate risk to high.

**Run 2:** `moderate`
> Quote: "The overall department's key focus is to enable self-service data products for Markets & Channels (Commercial) data consumers and decision makers; helping shape data-driven actions both for operational optimisation purposes and tactical and strategical decision recommendations."
> Verified: ✓ found in JD
> Reasoning: The role affects commercial business decisions without explicit regulatory, compliance, or financial reporting consequences, placing it at moderate risk.

**Run 3:** `moderate`
> Quote: "enable self-service data products for Markets & Channels (Commercial) data consumers and decision makers"
> Verified: ✓ found in JD
> Reasoning: The role serves business decision-making in a commercial context without explicit financial reporting, regulatory, or compliance language that would elevate risk to high.

### collaboration_width

**Run 1:** `5`
> Quote: "Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office Product teams; Shopper & Partner (D2C & B2B) digital product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Five distinct named teams are explicitly listed as collaboration partners across the responsibility section.

**Run 2:** `5`
> Quote: "Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office Product teams; Shopper & Partner (D2C & B2B) digital product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Five distinct named partner teams are explicitly identified across the responsibilities section.

**Run 3:** `9`
> Quote: "Analytics Interface; Commercial Analytics; Analytics Innovation & Automation; Data Office Product teams; Shopper & Partner (D2C & B2B) digital product teams; Data Science; Marketing; Finance; Operations"
> Verified: ⚠ NOT found verbatim
> Reasoning: Nine distinct named teams or functions are explicitly listed as collaboration partners, spanning current analytics sub-teams, data office product teams, digital product teams, and stated potential functional partners.

⚠ **LLM inconsistency**: runs gave ['5', '5', '9']

### data_team_maturity

**Run 1:** `mid`
> Quote: "build an AI-enabled data foundation the entire company can rely on"
> Verified: ✓ found in JD
> Reasoning: The JD references established infrastructure (Databricks, Unity Catalog, semantic layers) and multiple specialized sub-teams while framing the role around building and transformation, indicating active growth rather than early establishment or mature scale operation.

**Run 2:** `mid`
> Quote: "Build and maintain semantic layer infrastructure including metric view pipelines, materialisation and optimisation"
> Verified: ✓ found in JD
> Reasoning: Named tools used in responsibilities (Databricks, Unity Catalog, semantic layer pipelines) and multiple defined analytics sub-teams indicate an established data function in growth mode.

**Run 3:** `mature`
> Quote: "Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment"
> Verified: ✓ found in JD
> Reasoning: The presence of governance and platform tooling deployed at scale (Unity Catalog with structured governance and control mechanisms) indicates an established, specialized data operation.

⚠ **LLM inconsistency**: runs gave ['mid', 'mid', 'mature']

### jd_authorship

**Run 1:** `mixed`
> Quote: "Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical context (Unity Catalog, metric view pipelines, assertion checks) that only comes from domain knowledge, alongside generic collaboration verbs like 'collaborate closely' and 'champion,' indicating input from both technical and recruiting perspectives.

**Run 2:** `hiring_manager`
> Quote: "Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment; Build and maintain semantic layer infrastructure including metric view pipelines, materialisation and optimisation"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specificity about Unity Catalog governance, semantic layer infrastructure, metric view pipelines, and materialization practices indicates technical knowledge from someone who has performed this work.

**Run 3:** `mixed`
> Quote: "Build and maintain semantic layer infrastructure including metric view pipelines, materialisation and optimisation; Drive Unity Catalog governance (schemas, access, metadata tagging)"
> Verified: ⚠ NOT found verbatim
> Reasoning: Technical specificity in tool application and methodology (semantic layer, metric views, Unity Catalog governance) is mixed with generic collaboration language and process-oriented responsibilities elsewhere.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `commercial`
> Quote: "enable self-service data products for Markets & Channels (Commercial) data consumers and decision makers"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly framed as serving the Commercial organization (Markets & Channels) as the primary audience, with supporting product and internal data components.

**Run 2:** `commercial`
> Quote: "Build data pipeline engineering, orchestration, and monitoring to deliver high-quality data products centred around one of our three Commercial Domain pillars."
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves Markets & Channels commercial teams and is scoped to commercial domain pillars for delivering data products that drive commercial decision-making.

**Run 3:** `internal_data`
> Quote: "Within this mandate, the Analytics Engineering team's responsibility is to build an AI-enabled data foundation the entire company can rely on."
> Verified: ✓ found in JD
> Reasoning: The role's primary responsibility is to build data foundation and infrastructure for internal company use, with commercial/Markets & Channels impact as the framed end goal of that infrastructure.

⚠ **LLM inconsistency**: runs gave ['commercial', 'commercial', 'internal_data']

### autonomy_level

**Run 1:** `mixed`
> Quote: "Drive Unity Catalog governance (schemas, access, metadata tagging)"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting verbs ('Drive,' 'champion,' 'shape') with execution within an already-defined departmental mandate to build data products and governance.

**Run 2:** `execution`
> Quote: "Collaborate closely with the Analytics Interface, Commercial Analytics and business teams to turn business requirements into productionised AI-enabling data products."
> Verified: ✓ found in JD
> Reasoning: The primary responsibility framing emphasizes translating business requirements set by commercial partners into delivered products, indicating execution of priorities defined by others.

**Run 3:** `mixed`
> Quote: "Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment; Collaborate closely with the Analytics Interface, Commercial Analytics and business teams to turn business requirements into productionised AI-enabling data products."
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic responsibility for data governance and platform building with execution in service of business requirements set by other stakeholders.

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'mixed']

### ai_role
**Run 1:** `none` ✓
> Quote: "Build data pipeline engineering, orchestration, and monitoring"
> Reasoning: Standard data engineering and pipeline work with no AI skill expectations or infrastructure for AI consumption.

**Run 2:** `none` ✓
> Quote: "Build data pipeline engineering, orchestration, and monitoring to deliver high-quality data products"
> Reasoning: No AI-specific skills or tools mentioned; focuses on traditional data engineering.

**Run 3:** `none` ✓
> Quote: "no explicit AI signals in phrases"
> Reasoning: Standard data engineering and analytics work; no AI tool usage or AI infrastructure requirements mentioned


### testing_framing
**Run 1:** `tool_listed` ✗
> Quote: "adhere to data quality frameworks; include assertion checks"
> Reasoning: Testing techniques (assertions) are mentioned as requirements to include, but without ownership verbs (own/ensure/define/implement/establish).

**Run 2:** `responsibility` ✓
> Quote: "adhere to data quality frameworks; include assertion checks and have performance & cost optimisation applied"
> Reasoning: Candidate expected to implement and own quality assurance practices including assertion checks.

**Run 3:** `responsibility` ✓
> Quote: "include assertion checks and have performance & cost optimisation applied"
> Reasoning: Candidate owns implementing data quality frameworks and assertion checks as part of their work

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'responsibility', 'responsibility']

### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "adhere to data quality frameworks; include assertion checks and have performance & cost optimisation applied"
> Reasoning: Operational reliability concerns present through quality frameworks, assertions, and monitoring, but without explicit SLO, incidents, or compliance/regulatory dominance.

**Run 2:** `moderate` ✓
> Quote: "Drive Unity Catalog governance (schemas, access, metadata tagging) to improve data accessibility in highly controlled compliant environment"
> Reasoning: Governance and compliance emphasis signals loss aversion around regulatory/operational controls, but not the dominant role framing.

**Run 3:** `high` ✗
> Quote: "highly controlled compliant environment; Drive Unity Catalog governance"
> Reasoning: Compliance and governance framing dominates (explicit 'compliant', regulatory alignment, data trustworthiness) alongside operational reliability concerns

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'high']
