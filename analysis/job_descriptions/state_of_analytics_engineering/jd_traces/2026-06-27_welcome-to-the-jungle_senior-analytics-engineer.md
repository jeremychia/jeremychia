# Trace: 2026-06-27_welcome-to-the-jungle_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Welcome to the Jungle

**Location:** Paris (Hybrid)
**Date Posted:** 2026-06-27
**Salary:** €58,000 – €72,000 EUR

---

Senior Analytics Engineer
Permanent contract
Paris
Data
Hybrid
Salary: €58,000 – €72,000

The job


Application

Job details for Senior Analytics Engineer at Welcome to the Jungle

The role
The Senior Analytics Engineer (AE) at Welcome to the Jungle plays a crucial role at building up our data assets and consolidating existing ones. It's pivotal in the definition of setting up standards and guidelines for other data practitioners as well as applying the first levels of governance and participating at setting up the architecture direction.

This role is central in the data space of the company, allowing to work directly with the likes of Data Engineers (DE), Data Analyst (DA) or Data Scientists (DS). It also works closely to the different business functions.

Additionally, as a senior member of the team, they play a key role in developing more junior team members and implementing best practices.

The Analytics Engineer will work as part of the Data Platform team, regrouping both DE and AE specialists.

Our data stack
Overall, our stack is aligned with the standards of the modern data stack:

Snowflake as our Data Warehouse

dbt as our modeling tool

Airflow to manage our workflows

Rivery for our ingestions

Omni and Metabase for the Dashboarding and reporting needs

And some ad-hoc Python script

Key responsibilities
Bring-in your experience as a seasoned data specialist

Build-up our Data Warehouse by developing robust and efficient data pipelines and data models

Make our data ready to use by our end-users by setting up proper models in our BI tools and AI assistants

Interact with your data peers to advocate good practices among the practitioners

Ensure our data is well documented and well govern

Keep up to speed with the novelty of the sector

Support the use of our data by third party products (CRM, website, AI assistant…)

The ideal profile
You have at least 5 years of experience working in data and at least one previous experience as an Analytics Engineer (or other data modeling role)

You have a good understanding of the concepts of data warehouse modeling

You have a deep proficiency in SQL, including architecting scalable transformations and frameworks to handle enterprise-scale datasets

You have used dbt in a previous context

You have an experience with cloud-based data warehouses (Snowflake experience would be nice)

You have some experience using at least one BI tools such as Omni, Looker, Tableau, Power BI…

Experience using Python is a nice addition but not a requirement

Some experience working with AI in the context of a data team is a plus but not a hard requirement

Perks & benefits
4-day work week after your first month

5 weeks of paid vacation + 2 additional days

Flexible remote work (hybrid)

75% refund of Navigo Pass OR 20€ monthly allowance if you come to the office by any other means of transport (bike, on foot, etc.)"

Hiring steps
TA Interview

Case + Job Skills Interview

2 set of values interview

Best of luck !

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
| jd_authorship | hiring_manager | recruiter | mixed | 0% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | mixed | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "setting up standards and guidelines for other data practitioners as well as applying the first levels of governance and participating at setting up the architecture direction"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, standards, documentation, and best practices throughout with zero velocity-oriented language, signaling a rigour-focused orientation.

**Run 2:** `rigour`
> Quote: "Ensure our data is well documented and well govern"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes governance, documentation, standards-setting, and quality infrastructure over delivery speed or iteration pace.

**Run 3:** `rigour`
> Quote: "Ensure our data is well documented and well govern"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, documentation, standards, and best practices throughout with no velocity or speed language present.

### domain_risk

**Run 1:** `moderate`
> Quote: "Make our data ready to use by our end-users by setting up proper models in our BI tools and AI assistants"
> Verified: ✓ found in JD
> Reasoning: The role serves a SaaS job board platform's internal analytics needs without explicit financial reporting or compliance requirements, making data errors moderate business risks.

**Run 2:** `moderate`
> Quote: "Make our data ready to use by our end-users by setting up proper models in our BI tools and AI assistants"
> Verified: ✓ found in JD
> Reasoning: The role focuses on business intelligence and operational reporting without explicit financial reporting, compliance, or regulatory obligations.

**Run 3:** `moderate`
> Quote: "Make our data ready to use by our end-users by setting up proper models in our BI tools and AI assistants"
> Verified: ✓ found in JD
> Reasoning: The role serves business intelligence and AI systems but shows no indicators of financial reporting, compliance, or regulatory consequences.

### collaboration_width

**Run 1:** `3`
> Quote: "Data Engineers (DE), Data Analyst (DA) or Data Scientists (DS)"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct data functions—Data Engineers, Data Analysts, and Data Scientists—as direct collaboration partners.

**Run 2:** `3`
> Quote: "work directly with the likes of Data Engineers (DE), Data Analyst (DA) or Data Scientists (DS)"
> Verified: ✓ found in JD
> Reasoning: Three named partner functions are explicitly identified: Data Engineers, Data Analysts, and Data Scientists.

**Run 3:** `3`
> Quote: "Data Engineers (DE); Data Analyst (DA); Data Scientists (DS)"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named partner functions explicitly listed in the responsibilities section.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build-up our Data Warehouse by developing robust and efficient data pipelines and data models"
> Verified: ✓ found in JD
> Reasoning: The team has deployed a modern stack (Snowflake, dbt, Airflow) with multiple specialized roles, but is actively building and consolidating assets, indicating growth-stage mid-maturity.

**Run 2:** `mid`
> Quote: "building up our data assets and consolidating existing ones"
> Verified: ✓ found in JD
> Reasoning: The phrase indicates existing infrastructure requires consolidation while new capability is being built, characteristic of a scaling team with established but growing infrastructure.

**Run 3:** `mid`
> Quote: "building up our data assets and consolidating existing ones"
> Verified: ✓ found in JD
> Reasoning: The team has deployed existing infrastructure with named tools but is still in growth and improvement phase with emerging governance.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "deep proficiency in SQL, including architecting scalable transformations and frameworks to handle enterprise-scale datasets"
> Verified: ✓ found in JD
> Reasoning: The JD specifies named tools in applied context (dbt modeling, Snowflake, Airflow), enterprise-scale architectural requirements, and specific methodologies that signal authorship by someone actively doing this work.

**Run 2:** `recruiter`
> Quote: "Build-up our Data Warehouse by developing robust and efficient data pipelines and data models"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs without specific scale, volume, tooling context, or methodology that would indicate someone who performs this job wrote them.

**Run 3:** `mixed`
> Quote: "participating at setting up the architecture direction"
> Verified: ✓ found in JD
> Reasoning: Responsibilities show some domain specificity (governance, architecture, standards) but lack granular technical details and include generic collaborative language like 'advocate good practices'.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'recruiter', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "It's pivotal in the definition of setting up standards and guidelines for other data practitioners as well as applying the first levels of governance"
> Verified: ✓ found in JD
> Reasoning: The primary emphasis is on setting standards and governance for data practitioners within the team and advancing the data platform, making the data function itself the core audience.

**Run 2:** `internal_data`
> Quote: "setting up standards and guidelines for other data practitioners as well as applying the first levels of governance"
> Verified: ✓ found in JD
> Reasoning: The primary emphasis is on data infrastructure, governance frameworks, and enabling other data practitioners rather than serving commercial, product, or finance stakeholders.

**Run 3:** `internal_data`
> Quote: "setting up standards and guidelines for other data practitioners"
> Verified: ✓ found in JD
> Reasoning: The primary audience is the data function itself—other data practitioners and the data platform infrastructure—not commercial, product, or finance functions.

### autonomy_level

**Run 1:** `strategic`
> Quote: "participating at setting up the architecture direction"
> Verified: ✓ found in JD
> Reasoning: The role is framed as 'pivotal' in defining standards, setting architecture direction, and developing team members, indicating clear strategic ownership and direction-setting expectations.

**Run 2:** `mixed`
> Quote: "setting up standards and guidelines for other data practitioners as well as applying the first levels of governance and participating at setting up the architecture direction"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic responsibilities (defining standards, establishing governance, architecture participation, mentoring junior team members) with execution responsibilities (building pipelines and models).

**Run 3:** `mixed`
> Quote: "participating at setting up the architecture direction"
> Verified: ✓ found in JD
> Reasoning: The role genuinely combines setting direction (standards, architecture, mentorship) with hands-on execution (building pipelines, models, documentation).

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'mixed']

### ai_role
**Run 1:** `none` ✓
> Quote: "developing robust and efficient data pipelines and data models"
> Reasoning: All phrases describe standard data engineering work with no mention of AI coding tools, GenAI infrastructure, or AI-assisted development.

**Run 2:** `none` ✓
> Quote: "developing robust and efficient data pipelines and data models"
> Reasoning: No mention of AI tools, AI-first mindset, or AI infrastructure building.

**Run 3:** `none` ✓
> Quote: "developing robust and efficient data pipelines and data models"
> Reasoning: Standard data engineering work with no AI tooling, infrastructure building, or AI-first mindset mentioned.


### testing_framing
**Run 1:** `absent` ✗
> Quote: "It's pivotal in the definition of setting up standards and guidelines for other data practitioners as well as applying the first levels of governance"
> Reasoning: Standards and governance mentioned but no explicit testing responsibility verb or testing tools listed.

**Run 2:** `responsibility` ✓
> Quote: "It's pivotal in the definition of setting up standards and guidelines for other data practitioners as well as applying the first levels of governance"
> Reasoning: Candidate owns establishing quality standards and governance practices across the team.

**Run 3:** `responsibility` ✓
> Quote: "It's pivotal in the definition of setting up standards and guidelines for other data practitioners as well as applying the first levels of governance"
> Reasoning: Candidate owns quality and governance practice by establishing standards and applying governance across the data team.

⚠ **LLM inconsistency**: runs gave ['absent', 'responsibility', 'responsibility']

### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "developing robust and efficient data pipelines; applying the first levels of governance"
> Reasoning: Emphasis on 'robust' pipelines and operational governance indicates reliability concerns, though without explicit incident/SLO/stability language.

**Run 2:** `moderate` ✓
> Quote: "developing robust and efficient data pipelines and data models"
> Reasoning: Emphasis on robust and efficient systems reflects operational reliability concerns without compliance or regulatory dominance.

**Run 3:** `moderate` ✓
> Quote: "It's pivotal in the definition of setting up standards and guidelines for other data practitioners as well as applying the first levels of governance"
> Reasoning: Operational governance and data standards matter for trustworthiness, framed around reliability and proper practices rather than explicit compliance.

