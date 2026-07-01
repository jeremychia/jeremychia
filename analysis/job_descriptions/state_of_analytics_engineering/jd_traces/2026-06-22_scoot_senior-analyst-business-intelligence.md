# Trace: 2026-06-22_scoot_senior-analyst-business-intelligence

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analyst, Business Intelligence — Scoot

**URL:** https://flyscoot.wd102.myworkdayjobs.com/ScootExternalCareers/job/Singapore-HQ/Senior-Analyst--Business-Intelligence_R0005764-1?source=LinkedIn
**Location:** Singapore HQ

---

## Key Responsibilities

- Execute dashboard implementation that meet end-user requirements.
- Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions.
- Responsible for the structure, quality, and management of large volumes of data from different sources within the business.
- Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google BigQuery.
- Distil complex data into meaningful business insights to facilitate decision-making and forward planning.

---

## Required Qualifications

- Bachelor's degree in Data Analytics / Computer Science / Information Technology / Mathematics / Statistics.
- At least 2 years of working experience in developing dashboards using Tableau (Dashboard creation, report authoring, troubleshooting, data source management).
- At least 2 years of working experience in managing relational database system and writing complex SQL queries.
- Ability to understand and explain complex data and effective working as a liaison between technical and non-technical groups.
- Willingness to show initiative and take ownership of job responsibilities.
- Ability to handle multiple tasks and support special project needs simultaneously.

---

## Preferred / Bonus Skills

None explicitly listed.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | mixed | 33% | ✗ |
| autonomy_level |  | execution | execution | execution | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business."
> Verified: ✓ found in JD
> Reasoning: Quality is explicitly named as a core responsibility with no countervailing velocity signals present in the JD.

**Run 2:** `rigour` ✓
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, structure, and management as core responsibilities with no velocity language present, indicating a rigour-oriented role.

**Run 3:** `rigour` ✓
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business."
> Verified: ✓ found in JD
> Reasoning: The responsibilities explicitly emphasize quality and structure as core expectations, with no velocity-related language present.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Distil complex data into meaningful business insights to facilitate decision-making and forward planning."
> Verified: ✓ found in JD
> Reasoning: The JD uses generic decision-support language without explicit regulatory, compliance, or financial reporting signals despite the airline industry context.

**Run 2:** `moderate` ✗
> Quote: "Distil complex data into meaningful business insights to facilitate decision-making and forward planning."
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus on operational business intelligence and decision support without explicit financial reporting, regulatory, or compliance language, indicating moderate risk.

**Run 3:** `moderate` ✗
> Quote: "Distil complex data into meaningful business insights to facilitate decision-making and forward planning."
> Verified: ✓ found in JD
> Reasoning: While airlines operate in regulated environments, the JD uses generic business intelligence language without mentioning compliance, financial reporting, or regulatory requirements.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No named teams or functions are explicitly identified; references to 'end-user requirements' and 'technical and non-technical groups' are generic stakeholder descriptions that do not count as named collaborating teams.

**Run 2:** `0` ✗
> Quote: "effective working as a liaison between technical and non-technical groups"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams, functions, or stakeholder groups are identified; collaboration language refers only to generic 'technical and non-technical groups' which do not count per the classification rules.

**Run 3:** `0` ✗
> Quote: "No named partner teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions end-users and liaison with technical and non-technical groups but does not name any specific functions or teams.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions."
> Verified: ✓ found in JD
> Reasoning: Existing BI infrastructure and tools (Tableau, BigQuery, SQL Server) are being maintained and managed, indicating an established data function rather than early-stage greenfield or a mature enterprise team.

**Run 2:** `mid` ✗
> Quote: "Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions."
> Verified: ✓ found in JD
> Reasoning: The role maintains existing BI solutions and works with established tools (SQL Server, BigQuery, Tableau), indicating a mid-stage data function with existing infrastructure already deployed.

**Run 3:** `mid` ✗
> Quote: "Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions."
> Verified: ✓ found in JD
> Reasoning: The role focuses on maintaining existing BI infrastructure with named tools already deployed (Tableau, SQL Server, BigQuery), indicating an established but growing function rather than greenfield.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google BigQuery."
> Verified: ✓ found in JD
> Reasoning: Technical specificity in naming database constructs and tools is mixed with generic responsibility language lacking business context about what these dashboards actually track.

**Run 2:** `mixed` ✗
> Quote: "Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google BigQuery."
> Verified: ✓ found in JD
> Reasoning: The JD names specific technical tools and concepts suggesting hiring manager input, but lacks precise application context and uses boilerplate action verbs like 'maintain' and 'manage' throughout, indicating mixed authorship.

**Run 3:** `mixed` ✗
> Quote: "Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google BigQuery."
> Verified: ✓ found in JD
> Reasoning: The JD combines specific technical details (stored procedures, triggers, named database platforms) with generic boilerplate verbs like execute and maintain.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Maintain, and manage advanced reporting, analyses, dashboards, and other BI solutions."
> Verified: ✓ found in JD
> Reasoning: The emphasis is on building and maintaining the BI platform infrastructure itself for internal consumption rather than serving a specific business function like Finance or Product.

**Run 2:** `internal_data` ✗
> Quote: "Execute dashboard implementation that meet end-user requirements."
> Verified: ✓ found in JD
> Reasoning: The role's primary responsibility is building and maintaining BI infrastructure (dashboards and reporting solutions) for internal stakeholder consumption, indicating internal_data platform orientation rather than serving a specific business function.

**Run 3:** `mixed` ✗
> Quote: "Distil complex data into meaningful business insights to facilitate decision-making and forward planning."
> Verified: ✓ found in JD
> Reasoning: The JD does not specify which business function (commercial, product, finance, or operations) the BI dashboards primarily serve, describing only generic decision-making.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'mixed']

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Execute dashboard implementation that meet end-user requirements."
> Verified: ✓ found in JD
> Reasoning: The use of 'execute' and the framing of meeting 'end-user requirements' indicates the role executes against direction set by others rather than defining strategic direction.

**Run 2:** `execution` ✗
> Quote: "Execute dashboard implementation that meet end-user requirements."
> Verified: ✓ found in JD
> Reasoning: The verb 'execute' combined with 'meet end-user requirements' indicates the role delivers work within constraints and priorities set by others rather than setting strategic direction independently.

**Run 3:** `execution` ✗
> Quote: "Execute dashboard implementation that meet end-user requirements."
> Verified: ✓ found in JD
> Reasoning: The core verbs emphasize execution and delivery of defined work (execute, maintain, manage) rather than setting strategic direction or defining priorities.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

### ai_role
**Run 1:** `none` ✓
> Quote: "Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google BigQuery"
> Reasoning: Technical SQL skills but no AI tooling or GenAI responsibilities mentioned

**Run 2:** `none` ✓
> Quote: "N/A"
> Reasoning: Traditional BI/analytics stack (SQL Server, BigQuery, dashboards) with no AI tool usage, AI-first framing, or GenAI infrastructure responsibilities.

**Run 3:** `none` ✓
> Quote: "Develop and utilize custom queries, stored procedures, and triggers to extract data from Microsoft SQL Server and Google BigQuery"
> Reasoning: Standard SQL/data extraction work with no AI coding tools, AI-assisted workflows, or AI infrastructure building mentioned.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business"
> Reasoning: Owns quality as a primary responsibility across data management

**Run 2:** `responsibility` ✓
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business"
> Reasoning: Candidate owns quality and data management end-to-end; no testing tool explicitly named.

**Run 3:** `responsibility` ✓
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business"
> Reasoning: Candidate owns quality practice with explicit 'responsible for' + 'quality' framing indicating ownership of data quality standards.


### loss_aversion_framing
**Run 1:** `moderate` ✗
> Quote: "Responsible for the structure, quality, and management of large volumes of data from different sources within the business"
> Reasoning: Management and quality accountability suggests operational reliability concerns without explicit regulatory framing

**Run 2:** `none` ✓
> Quote: "Distil complex data into meaningful business insights to facilitate decision-making and forward planning."
> Reasoning: Pure delivery/execution framing focused on enabling decision-making; no operational reliability or compliance risk language.

**Run 3:** `none` ✓
> Quote: "Distil complex data into meaningful business insights to facilitate decision-making and forward planning"
> Reasoning: All framing centers on delivery and insights; no operational reliability fears (SLOs, incidents) or compliance/trust dominance signals present.

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'none']
