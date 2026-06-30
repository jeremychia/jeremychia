# Trace: 2026-06-30_cosuno_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Cosuno

**URL:** https://jobs.ashbyhq.com/cosuno/b1935448-d3ea-40fb-a011-2a3a98ba3160
**Location:** Berlin/Remote
**Date Posted:** 2026-06-30
**Salary:** 80,000–100,000 EUR

---

Senior Analytics Engineer
Location
Berlin/Remote

Employment Type
Full time

Location Type
Remote

Department
Tech
Business Intelligence

Compensation
€80K – €100K

Overview

Your mission
As a member of our Data team, you'll take full ownership of the systems that turn raw data into decisions—for our product, our internal teams, our customers, and our investors. You won't just maintain dashboards; you'll own the pipeline end to end, from ingestion to the numbers people actually act on.

In your first few months, you might:

Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on.

Maintain and extend our Looker setup, and ship new dashboards and reports that customers and other stakeholders depend on.

Strengthen our data pipeline from Postgres to BigQuery, and build custom Python scripts to automate the flows that keep our warehouse fresh.

Integrate our data warehouse with external tools like Salesforce or ActiveCampaign, so the right data reaches the teams that need it.

How We Build: Our Engineering Culture
We believe in a calm, collaborative, and productive engineering environment. We trust our people and give them the autonomy to do their best work. Our approach includes:

Ownership Over Handoffs: On a small data team, you own your work from ingestion to dashboard. We trust you to make decisions and run with them.

Quality by Default: We treat our data models like production code—tested, version-controlled, and documented—so the numbers we serve are ones we can stand behind.

DevOps Mindset: We automate the boring parts. Pipelines, syncs, and checks are powered by third-party tools or GitHub Actions so the team can focus on the work that needs a human.

Collaboration & Transparency: We value open discussion, constructive reviews, and a culture where the best idea wins, regardless of who it comes from.

AI-Native by Default: We work heavily with Claude Code and other AI tools, and they're a core part of how we build—from writing models and scripts to debugging pipelines and exploring data. We expect everyone on the team to use them fluently and keep getting better at it.

Your profile
We're looking for an experienced data practitioner who likes owning the full stack of an analytics platform. You'll be a great fit if you have:

Significant professional experience building and maintaining data models with dbt and writing advanced SQL.

Solid Python skills for data syncing, automation, and general scripting.

Hands-on experience with a cloud data warehouse such as BigQuery, and comfort working with source databases like Postgres.

Experience building dashboards and serving data to non-technical stakeholders (a strong command of Looker is a big plus).

Strong, hands-on familiarity with AI coding tools—especially Claude Code—and a habit of using them as part of your daily workflow.

A pragmatic approach to problem-solving and a high sense of ownership, feeling comfortable driving projects independently.

Excellent communication skills in English.

Bonus Points For (Nice-to-Haves):
Experience with reverse ETL or integrating a data warehouse with tools like ActiveCampaign or Salesforce.

Experience building and maintaining CI/CD or automation pipelines (e.g. GitHub Actions).

Experience preparing data and reporting for external audiences such as customers or investors.

An interest in data engineering best practices, pipeline reliability, and infrastructure-as-code.

Why us?
Competitive Compensation: A competitive salary above the market average.

Work-Life Balance: Choose to work 100% remotely or from our modern office in Berlin. We offer flexible working hours to fit your life.

Top-Notch Equipment: A new MacBook Pro to ensure you have the best tools for the job…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 0 | 0 | 0 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | mixed | execution | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "We treat our data models like production code—tested, version-controlled, and documented—so the numbers we serve are ones we can stand behind."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes quality, testing, reliability, and best practices as core values, with explicit signals of governance-first culture rather than speed or iteration pace.

**Run 2:** `rigour`
> Quote: "Quality by Default: We treat our data models like production code—tested, version-controlled, and documented—so the numbers we serve are ones we can stand behind."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, quality, documentation, and reliability as core expectations throughout, with no velocity-oriented language like fast-paced or rapid delivery.

**Run 3:** `rigour`
> Quote: "We treat our data models like production code—tested, version-controlled, and documented—so the numbers we serve are ones we can stand behind."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, version control, documentation, and quality as core values, with multiple rigour signals (Quality by Default, pipeline reliability) and no velocity language.

### domain_risk

**Run 1:** `moderate`
> Quote: "Maintain and extend our Looker setup, and ship new dashboards and reports that customers and other stakeholders depend on."
> Verified: ✓ found in JD
> Reasoning: Data errors would affect business decisions but the JD lacks explicit mention of financial reporting, regulatory compliance, or P&L impact typical of high-risk domains.

**Run 2:** `moderate`
> Quote: "Maintain and extend our Looker setup, and ship new dashboards and reports that customers and other stakeholders depend on."
> Verified: ✓ found in JD
> Reasoning: The role supports business operations and customer decision-making in a SaaS construction platform without regulatory, financial reporting, or compliance requirements.

**Run 3:** `moderate`
> Quote: "for our product, our internal teams, our customers, and our investors"
> Verified: ✓ found in JD
> Reasoning: Data serves business intelligence and operational decisions for customers and stakeholders without explicit financial reporting, regulatory, or compliance language indicating high risk.

### collaboration_width

**Run 1:** `0`
> Quote: "No explicitly named partner teams or functions identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: While the role serves product, internal teams, customers, and investors, none are explicitly named as collaboration partners in the responsibilities section.

**Run 2:** `0`
> Quote: "Ownership Over Handoffs: On a small data team, you own your work from ingestion to dashboard. We trust you to make decisions and run with them."
> Verified: ✓ found in JD
> Reasoning: No named collaboration partner teams or functions are explicitly identified; the role emphasizes autonomous ownership over handoffs with no dependency on specific external teams.

**Run 3:** `0`
> Quote: "driving projects independently"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams are identified as collaboration partners; role emphasizes independent ownership of the data pipeline end-to-end.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on."
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure (dbt, BigQuery, Looker, Postgres pipeline) is operational; the focus is on improving and extending established systems rather than building from zero.

**Run 2:** `mid`
> Quote: "Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on."
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure (dbt, Looker, BigQuery, Postgres) is already deployed and operational; the role focuses on improving and extending rather than building from zero.

**Run 3:** `mid`
> Quote: "Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on."
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure with named tools (dbt, Looker, BigQuery, Postgres) and responsibilities framed as improving established systems on a small but functional data team.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Strengthen our data pipeline from Postgres to BigQuery, and build custom Python scripts to automate the flows that keep our warehouse fresh."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain technical specificity (named source/destination systems, scripting approach, specific infrastructure problem) that indicates deep operational knowledge of the actual work.

**Run 2:** `hiring_manager`
> Quote: "Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on. Maintain and extend our Looker setup, and ship new dashboards and reports that customers and other stakeholders depend on. Strengthen our data pipeline from Postgres to BigQuery, and build custom Python scripts to automate the flows that keep our warehouse fresh."
> Verified: ✓ found in JD
> Reasoning: The responsibilities detail specific technical stack choices, named tools with precise application context, and exact architectural patterns (ingestion to dashboard pipeline) that only someone with hands-on experience in this role would specify.

**Run 3:** `hiring_manager`
> Quote: "Strengthen our data pipeline from Postgres to BigQuery, and build custom Python scripts to automate the flows that keep our warehouse fresh."
> Verified: ✓ found in JD
> Reasoning: Specific technical details about database types, scripting approaches, and infrastructure tools indicate someone with hands-on data engineering experience wrote this.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "you'll own the pipeline end to end, from ingestion to the numbers people actually act on"
> Verified: ✓ found in JD
> Reasoning: While serving multiple audiences (product, customers, investors), the core mission emphasizes building and maintaining the data infrastructure itself rather than serving a specific business function.

**Run 2:** `internal_data`
> Quote: "Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building and maintaining data infrastructure, platform quality, and modeling practices rather than serving specific business functions.

**Run 3:** `internal_data`
> Quote: "Take ownership of our dbt pipeline, improving our data models so they're reliable, well-tested, and easy to build on."
> Verified: ✓ found in JD
> Reasoning: Primary focus is building and maintaining data infrastructure (dbt models, warehouse, pipelines) that serves internal data consumers and platform users.

### autonomy_level

**Run 1:** `execution`
> Quote: "You won't just maintain dashboards; you'll own the pipeline end to end, from ingestion to the numbers people actually act on."
> Verified: ✓ found in JD
> Reasoning: The role has full responsibility for delivering within a defined scope (dbt models, Looker dashboards, data pipeline, integrations) but does not set the strategic direction of the data platform.

**Run 2:** `mixed`
> Quote: "You own your work from ingestion to dashboard. We trust you to make decisions and run with them."
> Verified: ✓ found in JD
> Reasoning: The role has strategic decision-making authority over the data platform domain while executing a defined mission to serve product, internal teams, customers, and investors.

**Run 3:** `execution`
> Quote: "On a small data team, you own your work from ingestion to dashboard."
> Verified: ✓ found in JD
> Reasoning: Role owns how to execute within defined scope (improve dbt models, maintain Looker, strengthen pipelines) rather than setting data strategy direction for the organization.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']
