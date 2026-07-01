# Trace: 2026-06-27_spotify_analytics-engineer-ii

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer II — Spotify

**Location:** Stockholm / London
**Date Posted:** 2026-06-27

---

Analytics Engineer II
Stockholm / LondonData and Analytics – Platform /Permanent /Hybrid
The Platform team creates the technology that enables Spotify to learn quickly and scale easily, enabling rapid growth in our users and our business around the globe. Spanning many disciplines, we work to make the business work; creating the infrastructure, tooling, frameworks, and capabilities needed to welcome a billion customers.

We're looking for an Analytics Engineer II to join Spotify's Platform Central Data (PCD) squad, a cross-functional Data Engineering and Analytics Engineering team within the Platform Mission. You'll help build and maintain trusted analytical models, metrics, and data products that power developer productivity, platform health, and leadership decision-making. Working closely with Data Engineers, Product, Engineering, and Platform partners, you'll translate platform signals into reliable, well-modeled data assets that help Spotify ship faster and safer.

What You'll Do
Build and maintain analytical data models using dbt (or similar SQL-based transformation frameworks) in BigQuery for a broad set of stakeholders
Build and operate reliable data pipelines using SQL, with a focus on testing, observability, and CI/CD
Help define and evolve key metrics for platform health, developer productivity, and ML/AI platform adoption
Partner with Data Engineers on upstream pipelines and collaborate with Product, Engineering, and Data Science to scope and deliver insights
Improve data quality, performance, and cost efficiency across pipelines and models, including troubleshooting and backfills
Contribute to dashboards and self-serve data products that enable better decision-making across teams
Follow and contribute to data quality, testing, and documentation practices across the analytics layer
Participate in a fair support rotation for key datasets, pipelines, and analytical products
Who You Are
You have 2+ years of experience in analytics engineering, data engineering, or a related field
You have strong SQL skills and experience with data modelling
You are experienced with dbt (or similar SQL-based transformation frameworks) and a cloud data warehouse such as BigQuery, Snowflake, Redshift, or Databricks SQL
You are familiar with workflow orchestration tools such as Airflow, Dagster, Prefect, or Flyte
You care about data quality, reliability, and testability
You are comfortable working with BI/visualisation tools such as Looker or Tableau
You communicate clearly with both technical and non-technical partners
You are able to prioritize and deliver in a fast-moving environment
You have experience with platform or developer productivity data, experimentation, or ML/AI metrics
Where You'll Be
This role is based in London or Stockholm.

We offer you the flexibility to work where you work best! There will be some in person meetings, but still allows for flexibility to work from home.
Spotify is an equal opportunity employer. You are welcome at Spotify for who you are, no matter where you come from, what you look like, or what's playing in your headphones. Our platform is for everyone, and so is our workplace. The more voices we have represented and amplified in our business, the more we will all thrive, contribute, and be forward-thinking! So bring us your personal experience, your perspectives, and your background. It's in our differences that we will find the power to keep revolutionizing the way the world listens.

At Spotify, we are passionate about inclusivity and making sure our entire recruitment process is accessible to everyone. We have ways to request reasonable accommodations during the interview process and help assist in what you need. If you need accommodations at any stage of the application or interview process, please let us know - we're here to support you in any way we can.

We may use artificial intelligence (AI) …[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 4 | 4 | 4 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | mixed | 33% |
| stakeholder_orientation | product | internal_data | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Build and operate reliable data pipelines using SQL, with a focus on testing, observability, and CI/CD"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, observability, CI/CD, data quality, reliability, and testability as core expectations, with only two velocity signals present.

**Run 2:** `rigour`
> Quote: "Build and operate reliable data pipelines using SQL, with a focus on testing, observability, and CI/CD"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, observability, CI/CD, data quality, reliability, and documentation as core expectations with 6+ rigour signals versus only 2 velocity signals.

**Run 3:** `rigour`
> Quote: "Build and operate reliable data pipelines using SQL, with a focus on testing, observability, and CI/CD"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reliability, testing, and observability as core expectations, with no language prioritizing speed or rapid delivery.

### domain_risk

**Run 1:** `moderate`
> Quote: "leadership decision-making"
> Verified: ✓ found in JD
> Reasoning: The role supports internal platform metrics and leadership decisions but lacks explicit financial reporting, regulatory compliance, or P&L accountability.

**Run 2:** `moderate`
> Quote: "You'll help build and maintain trusted analytical models, metrics, and data products that power developer productivity, platform health, and leadership decision-making."
> Verified: ✓ found in JD
> Reasoning: The role affects internal operational and strategic decisions about platform health and developer productivity without explicit regulatory, financial reporting, or compliance requirements.

**Run 3:** `moderate`
> Quote: "Help define and evolve key metrics for platform health, developer productivity, and ML/AI platform adoption"
> Verified: ✓ found in JD
> Reasoning: The role serves internal platform operations and business decisions without explicit financial reporting, regulatory, or compliance language.

### collaboration_width

**Run 1:** `4`
> Quote: "Partner with Data Engineers on upstream pipelines and collaborate with Product, Engineering, and Data Science to scope and deliver insights"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names four distinct partner functions: Data Engineers, Product, Engineering, and Data Science.

**Run 2:** `4`
> Quote: "Partner with Data Engineers on upstream pipelines and collaborate with Product, Engineering, and Data Science to scope and deliver insights"
> Verified: ✓ found in JD
> Reasoning: The JD names four distinct partner functions: Data Engineers, Product, Engineering, and Data Science.

**Run 3:** `4`
> Quote: "Data Engineers; Product; Engineering; Data Science"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions are explicitly listed as collaboration partners throughout the responsibilities section.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build and maintain analytical data models using dbt (or similar SQL-based transformation frameworks) in BigQuery"
> Verified: ✓ found in JD
> Reasoning: The team has established infrastructure with named tools actively used in responsibilities and multiple data roles collaborating, indicating a mid-stage data function.

**Run 2:** `mid`
> Quote: "join Spotify's Platform Central Data (PCD) squad, a cross-functional Data Engineering and Analytics Engineering team within the Platform Mission"
> Verified: ✓ found in JD
> Reasoning: The existence of a named squad with distinct Data Engineering and Analytics Engineering roles, plus named production tools (dbt, BigQuery, Airflow) in responsibilities, indicates mid-stage maturity.

**Run 3:** `mid`
> Quote: "Participate in a fair support rotation for key datasets, pipelines, and analytical products"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, BigQuery, orchestration) and the support rotation structure indicate an established team with infrastructure and operational maturity but not yet multi-sub-team scale.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Build and operate reliable data pipelines using SQL, with a focus on testing, observability, and CI/CD"
> Verified: ✓ found in JD
> Reasoning: The responsibilities include specific technical methodologies and tools (dbt, BigQuery, testing, observability, CI/CD, troubleshooting, backfills) alongside generic action verbs.

**Run 2:** `hiring_manager`
> Quote: "Build and maintain analytical data models using dbt (or similar SQL-based transformation frameworks) in BigQuery for a broad set of stakeholders"
> Verified: ✓ found in JD
> Reasoning: The JD contains technical specificity about tools, data domains (platform health, developer productivity, ML/AI metrics), and practices (testing, CI/CD) that reflects domain expertise, not boilerplate.

**Run 3:** `mixed`
> Quote: "Build and operate reliable data pipelines using SQL, with a focus on testing, observability, and CI/CD"
> Verified: ✓ found in JD
> Reasoning: Technical specificity in pipeline and tool descriptions (dbt, SQL, testing, CI/CD) indicates hiring manager input, though some collaboration language is boilerplate.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `product`
> Quote: "Help define and evolve key metrics for platform health, developer productivity, and ML/AI platform adoption"
> Verified: ✓ found in JD
> Reasoning: The primary focus is on metrics and data assets that support Product and Engineering teams' decisions on platform health, developer productivity, and ML/AI adoption.

**Run 2:** `internal_data`
> Quote: "You'll help build and maintain trusted analytical models, metrics, and data products that power developer productivity, platform health, and leadership decision-making."
> Verified: ✓ found in JD
> Reasoning: The primary audience is internal platform engineering and product teams who consume metrics and data products; this is infrastructure and data platform work, not revenue/product experimentation/finance-facing.

**Run 3:** `internal_data`
> Quote: "Contribute to dashboards and self-serve data products that enable better decision-making across teams"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building analytics infrastructure and self-serve capabilities for internal data consumers rather than serving commercial, product, or finance functions.

⚠ **LLM inconsistency**: runs gave ['product', 'internal_data', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Partner with Data Engineers on upstream pipelines and collaborate with Product, Engineering, and Data Science to scope and deliver insights"
> Verified: ✓ found in JD
> Reasoning: The role is framed around partnering with and supporting other teams to deliver on their priorities, with limited independent strategic direction-setting.

**Run 2:** `execution`
> Quote: "Follow and contribute to data quality, testing, and documentation practices across the analytics layer"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes collaboration with other teams to scope work, following established practices, and contributing to collective standards rather than setting strategic direction.

**Run 3:** `execution`
> Quote: "Partner with Data Engineers on upstream pipelines and collaborate with Product, Engineering, and Data Science to scope and deliver insights"
> Verified: ✓ found in JD
> Reasoning: The role is positioned as partnering and collaborating to deliver scoped work rather than setting overall direction or defining the analytics strategy.

### ai_role
**Run 1:** `none` ✓
> Quote: "key metrics for platform health, developer productivity, and ML/AI platform adoption"
> Reasoning: Mentions ML/AI platform adoption but focuses on metrics and tracking rather than building AI infrastructure or using AI coding tools.

**Run 2:** `none` ✓
> Quote: "Help define and evolve key metrics for platform health, developer productivity, and ML/AI platform adoption"
> Reasoning: Role tracks ML/AI platform adoption metrics but shows no signal of building AI-ready infrastructure or using AI coding tools.

**Run 3:** `none` ✓
> Quote: "key metrics for platform health, developer productivity, and ML/AI platform adoption"
> Reasoning: Company has ML/AI platform but AE performs standard analytics work without building AI-specific infrastructure.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "with a focus on testing, observability, and CI/CD"
> Reasoning: Focus on testing indicates ownership of quality practices and testing discipline.

**Run 2:** `absent` ✗
> Quote: "with a focus on testing, observability, and CI/CD"
> Reasoning: Testing is mentioned as a focus area but lacks ownership verbs (own/ensure/define/implement/establish) and no specific testing tools listed.

**Run 3:** `responsibility` ✓
> Quote: "with a focus on testing, observability, and CI/CD"
> Reasoning: Focus on testing indicates core responsibility for quality practices and testing strategy.

⚠ **LLM inconsistency**: runs gave ['responsibility', 'absent', 'responsibility']

### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "support rotation for key datasets, pipelines, and analytical products"
> Reasoning: Support rotation signals operational reliability concerns and incident-response responsibilities rather than compliance/regulatory risk.

**Run 2:** `moderate` ✓
> Quote: "support rotation for key datasets, pipelines, and analytical products; Help define and evolve key metrics for platform health"
> Reasoning: Framing centers on operational reliability and platform stability concerns, but no regulatory or compliance signals present.

**Run 3:** `moderate` ✓
> Quote: "support rotation for key datasets, pipelines, and analytical products"
> Reasoning: Support rotation and on-call responsibilities signal operational reliability and incident response concerns.

