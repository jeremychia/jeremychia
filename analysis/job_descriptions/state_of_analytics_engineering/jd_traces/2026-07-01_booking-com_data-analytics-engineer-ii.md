# Trace: 2026-07-01_booking-com_data-analytics-engineer-ii

## JD text (fed to classifier, Layer B stripped)

```
# Data Analytics Engineer II — Booking.com

**URL:** https://jobs.booking.com/booking/jobs/29172?lang=en-us&iis=Job+Board&iisn=Linkedin
**Location:** Amsterdam, Netherlands
**Date Posted:** 2026-07-01

---

Data Analytics Engineer II at Booking.com

Location: Amsterdam, Netherlands
Department: Data Engineering
Job ID: 29172

Role Description
At Booking.com, data drives our decisions. Technology is at our core and innovation is everywhere. But our company is more than just datasets, lines of code or A/B tests. We're the thrill of the first night in a new place.

B. Data Teams
The Data team's responsibilities include data platforms, warehousing, enrichment and machine learning functionality, enabling teams across the organisation to understand and manage our business performance and improve the experience of our customers. You will be responsible for delivering products that advance data excellence and innovation within your product team, and across the business, helping us shape Booking.com's data journey.

Platform Team
The Platform team is responsible for creating, developing and maintaining a robust data platform and integrations in/out of it. In conjunction with our colleagues across Booking.com, the team is embarking on an ambitious modernisation programme focusing not just on infrastructure transition to the cloud but a complete overhaul of data ingestion, quality, security and governance. Providing a platform as a service is our goal.

Data Enablement Teams
Using the ecosystem our platform team have created, our Data Enablement teams work closely with teams across the business to ensure that data is ingested, transformed and enriched into secure, high quality, well governed consumption layers. Our customers are anyone from Finance to Marketing and everyone in between.

Flights Data Enablement Team
This Data Engineering team is focused on Flights data at Booking. We are building new products for creating, maintaining, and presenting flights data using the Booking Data Exchange (BDX) platform. We enable our analysts and product teams to make data-driven decisions about product improvements, streamline their processes, and build a deeper understanding of their systems.

You Will:
- Iteratively develop next-generation scalable, reliable, flexible, high-performance data pipeline capabilities and data platforms.
- Use standardised tooling and procedures to work with business users to model and implement data pipelines which are performant, scalable, reliable, secure, well governed with required observability.
- Engage with other teams as needed to achieve business objectives.
- End-to-end ownership of data quality in our core datasets and data pipelines.
- Engage with other teams to help them identify and resolve data quality issues.
- Be responsible for maintaining data quality, security, integrity and governance by effectively following regulatory requirements, company standards, and best practices.
- Adhere to the defined principles for architecture, quality and non-functional requirements.
- Proactively help colleagues grow professionally, taking a significant role in on-boarding and mentoring new team members.
- Continuously improve services you own, making them more performant, and utilising resources in the most optimised way.
- Ensure that products/services are always kept up to date with the latest technology standards and company guidelines.
- Ensuring that service level agreements are met by implementing tests and processes.
- Perform profiling to find bottlenecks and optimise performance, and ensure that performance metrics are set up and monitored for product health.
- Be able to connect business and product goals to complex technical tasks.
- Solve issues by prioritising on customer impact and perform root cause analysis to find ways to prevent recurrence.
- Contribute to Booking.com's growth through interviewing, on-boarding and other recruitment efforts.
- Be working in an agile environment and expect to contri…[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 4 | 4 | 4 | 4 | 100% | ✓ |
| data_team_maturity | mature | mature | mature | mid | 33% | ✓ |
| jd_authorship | mixed | hiring_manager | mixed | recruiter | 0% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | strategic | execution | execution | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "End-to-end ownership of data quality in our core datasets and data pipelines."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, regulatory compliance, testing, and reliability throughout, with no speed-to-market language, establishing a clear rigour orientation.

**Run 2:** `rigour` ✓
> Quote: "End-to-end ownership of data quality in our core datasets and data pipelines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, observability, regulatory compliance, testing, and reliability as core expectations throughout, with no velocity signals dominating.

**Run 3:** `rigour` ✓
> Quote: "End-to-end ownership of data quality in our core datasets and data pipelines"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, governance, regulatory compliance, testing, and reliability as core responsibilities with no velocity language; rigour signals outnumber velocity signals 5:1.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Solve issues by prioritising on customer impact and perform root cause analysis to find ways to prevent recurrence."
> Verified: ✓ found in JD
> Reasoning: The role emphasizes operational data quality and product enablement for internal customers rather than explicit financial reporting or regulatory compliance, placing it in the moderate rather than high risk category.

**Run 2:** `moderate` ✗
> Quote: "improve the experience of our customers"
> Verified: ✓ found in JD
> Reasoning: Booking.com is an e-commerce/travel marketplace where data errors affect business decisions and customer experience but not direct financial reporting or regulatory compliance like fintech/banking/insurance.

**Run 3:** `moderate` ✗
> Quote: "Our customers are anyone from Finance to Marketing and everyone in between"
> Verified: ✓ found in JD
> Reasoning: Booking.com's data errors affect business decisions across Finance and Marketing but the JD does not emphasize financial reporting accuracy or regulatory exposure as the primary domain risk.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `4` ✓
> Quote: "Our customers are anyone from Finance to Marketing and everyone in between; enable our analysts and product teams"
> Verified: ✓ found in JD
> Reasoning: Finance, Marketing, Product teams, and Analysts are explicitly named as distinct stakeholder groups this role works with and serves.

**Run 2:** `4` ✓
> Quote: "Finance to Marketing; analysts and product teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named partners explicitly identified: Finance and Marketing as customer departments, analysts and product teams as distinct groups being served.

**Run 3:** `4` ✓
> Quote: "Our customers are anyone from Finance to Marketing; analysts and product teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named partner functions explicitly listed: Finance, Marketing, Product (product teams), and Analysts (as a distinct role cohort).

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mature` ✓
> Quote: "This Data Engineering team is focused on Flights data at Booking. We are building new products for creating, maintaining, and presenting flights data using the Booking Data Exchange (BDX) platform."
> Verified: ✓ found in JD
> Reasoning: Multiple specialized sub-teams with distinct charters (Platform team, Data Enablement teams, Flights-specific team), an established named platform (BDX), and scaled infrastructure indicate a mature data organization.

**Run 2:** `mature` ✓
> Quote: "Data Enablement Teams work closely with teams across the business to ensure that data is ingested, transformed and enriched into secure, high quality, well governed consumption layers."
> Verified: ✓ found in JD
> Reasoning: Multiple named data sub-teams with distinct charters (Platform team, Data Enablement Teams, Flights-specific team) operating an established ecosystem at scale indicates mature organizational structure.

**Run 3:** `mid` ✗
> Quote: "ambitious modernisation programme focusing not just on infrastructure transition to the cloud but a complete overhaul of data ingestion, quality, security and governance"
> Verified: ✓ found in JD
> Reasoning: Multiple specialized data teams exist with established infrastructure and platforms, but significant modernization efforts signal the function is growing and scaling rather than fully mature.

⚠ **LLM inconsistency**: runs gave ['mature', 'mature', 'mid']

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Modelling data following best practices and Data Warehousing methodologies such as Data Vault and (Kimball) Dimensional modelling."
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical methodologies (Data Vault, Kimball), named platforms (BDX), specific tools (Snowflake, Kafka, Airflow), and scale context that only come from someone actively doing the work.

**Run 2:** `mixed` ✓
> Quote: "Use standardised tooling and procedures to work with business users to model and implement data pipelines which are performant, scalable, reliable, secure, well governed with required observability."
> Verified: ✓ found in JD
> Reasoning: The responsibility contains both technical specificity (named tools, performance requirements, data governance) and generic boilerplate language (standardised procedures, work with business users) indicating mixed hiring manager and recruiter authorship.

**Run 3:** `recruiter` ✗
> Quote: "Use standardised tooling and procedures to work with business users to model and implement data pipelines which are performant, scalable, reliable, secure, well governed with required observability"
> Verified: ✓ found in JD
> Reasoning: Responsibilities are written in generic boilerplate action verbs without specific technical context, tool names, or volume details that would indicate hiring manager authorship.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Producing curated, reusable analytical data products to enable self-serve analytics for many internal customers across departments."
> Verified: ✓ found in JD
> Reasoning: The primary focus is on building data infrastructure and platforms to enable internal analysts and product teams, not on directly serving commercial, product, or finance functions as primary audiences.

**Run 2:** `internal_data` ✓
> Quote: "You will be responsible for delivering products that advance data excellence and innovation within your product team, and across the business"
> Verified: ✓ found in JD
> Reasoning: The role serves internal data consumers and the data function itself through a platform-as-service model, enabling teams across Finance, Marketing, and product to self-serve, rather than serving external or single-function stakeholders.

**Run 3:** `internal_data` ✓
> Quote: "You will be responsible for delivering products that advance data excellence and innovation within your product team, and across the business"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building and maintaining data infrastructure for internal consumption by analysts, product teams, and other business users, not serving external customers or revenue functions.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `strategic` ✗
> Quote: "End-to-end ownership of data quality in our core datasets and data pipelines."
> Verified: ✓ found in JD
> Reasoning: The role is framed around ownership and accountability for specific data domains with autonomy to continuously improve services, not execution of direction set by others.

**Run 2:** `execution` ✗
> Quote: "Adhere to the defined principles for architecture, quality and non-functional requirements"
> Verified: ✓ found in JD
> Reasoning: While the role owns specific domains (data quality, pipelines, performance), it executes within defined organizational principles and standards rather than setting direction or strategy.

**Run 3:** `execution` ✗
> Quote: "Adhere to the defined principles for architecture, quality and non-functional requirements"
> Verified: ✓ found in JD
> Reasoning: While the role has end-to-end ownership of assigned datasets, the direction and principles are pre-defined by the organization, and the role executes within those established frameworks.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['strategic', 'execution', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD mentions machine learning functionality as something the data team enables but contains no expectation that the candidate use AI tools for coding or build AI-ready data foundations.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, AI-ready data infrastructure, or AI/ML pipeline capabilities as candidate expectations.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, or building AI-ready data infrastructure; no AI skill or capability is expected of the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Ensuring that service level agreements are met by implementing tests and processes."
> Verified: ✓ found in JD
> Reasoning: Testing is framed as an owned responsibility (implementing tests) with SLA accountability, not merely as a tool listed in a skill set.

**Run 2:** `responsibility` ✗
> Quote: "End-to-end ownership of data quality in our core datasets and data pipelines"
> Verified: ✓ found in JD
> Reasoning: Data quality is explicitly framed as something the candidate owns end-to-end, establishing it as an owned responsibility rather than a tool requirement or absent concern.

**Run 3:** `responsibility` ✗
> Quote: "End-to-end ownership of data quality in our core datasets and data pipelines"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as something the candidate owns and defines through implementation of tests and processes, not as optional tooling.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Be responsible for maintaining data quality, security, integrity and governance by effectively following regulatory requirements, company standards, and best practices."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability, data quality, and regulatory compliance as core concerns, but the primary framing remains delivery of innovative data products rather than prevention of catastrophic failure.

**Run 2:** `moderate` ✗
> Quote: "maintain data quality, security, integrity and governance by effectively following regulatory requirements, company standards, and best practices"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data governance and quality are integrated responsibilities, with one mention of regulatory compliance, but the primary framing centers on building and scaling data capabilities rather than preventing catastrophic failures or compliance exposure.

**Run 3:** `moderate` ✗
> Quote: "perform root cause analysis to find ways to prevent recurrence"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability through SLAs, monitoring, and incident prevention, but lacks high loss-aversion framing around compliance risk or preventing bad data reaching stakeholders.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
