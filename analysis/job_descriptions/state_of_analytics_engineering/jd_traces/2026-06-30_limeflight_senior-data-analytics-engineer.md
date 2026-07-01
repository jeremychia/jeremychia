# Trace: 2026-06-30_limeflight_senior-data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Data & Analytics Engineer — LimeFlight

**URL:** https://career.limeflight.com/o/senior-data-analytics-engineer-europe-100-remote
**Location:** Europe, 100% remote
**Date Posted:** 2026-06-30

---

LimeFlight Senior Data & Analytics Engineer Position

Company: LimeFlight
Job Title: Senior Data & Analytics Engineer (Europe, 100% remote)
Locations: Multiple European cities including Vienna, Brussels, Sofia, Helsinki, Berlin, Dublin, Madrid, Stockholm, Zürich, and 19+ additional locations
Salary: Not specified in posting

Role Overview
LimeFlight seeks a Senior Data & Analytics Engineer to 'take end-to-end ownership of our data platform and BI layer.' The company focuses on sustainable inflight service management, headquartered in Zurich with teams across 11 countries.

Key Responsibilities

Platform & Architecture:
- Own end-to-end data platform using Databricks and Microsoft Fabric
- 'Design and operate scalable pipelines and lakehouse architecture'
- Build ETL/ELT workflows managing batch and near real-time processing
- Ensure data quality, reliability, observability, and performance

Data Modeling:
- Own Power BI semantic models and KPIs
- Build dimensional models using star schema
- Maintain DAX performance and dataset refresh consistency

Customer-Facing Analytics:
- Build and maintain customer dashboards and embedded analytics
- Enable self-service analytics with governance
- Maintain customer-facing exports

Platform Quality & Operations:
- Implement validation scripts, unit tests, data quality checks
- Build CI/CD, testing, and versioning for pipelines
- Support multi-tenant architecture and security governance

Migration Focus:
- Reverse-engineer vendor-built BI solution
- Reduce technical debt and rebuild toward clean architecture

Requirements

Experience:
- '5+ years in data engineering / analytics engineering for customer-facing BI products'
- SaaS or product-driven environment background
- Proven scalable data platform and analytics experience

Technical Skills:
- Databricks (Spark, PySpark, Delta Lake)
- Microsoft Fabric or Azure data stack
- Power BI data modeling and DAX
- Advanced SQL and dimensional modeling
- Lakehouse architecture and ETL/ELT design
- Multi-tenant data models and embedded analytics
- CI/CD, Git, monitoring, and data quality practices

Nice-to-Have:
- Azure infrastructure knowledge
- Data quality frameworks like Great Expectations

Mindset:
Candidates should demonstrate 'strong ownership and autonomy,' impact-driven thinking, product orientation, proactive problem-solving, business acumen, pragmatism, and clear cross-functional communication.

Additional Details

Language: Minimum English C1 level
Travel: Two annual one-week team events
Work Authorization: Must be legally eligible to work full-time in Europe under employment contract (no freelance/B2B)
Company Tech Stack: C#/.NET 8-10, ASP.NET Core, SQL Server, Azure services, Docker, Databricks, Azure Fabric
Hiring Process: Four stages including recruiter screen, manager interview, technical assessment, and founder/peer discussion

---
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
| stakeholder_orientation | internal_data | product | internal_data | 33% |
| autonomy_level | mixed | strategic | strategic | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Ensure data quality, reliability, observability, and performance"
> Verified: ✓ found in JD
> Reasoning: The core responsibilities emphasize data quality, reliability, observability, and governance—foundational rigour principles—with no velocity-oriented language.

**Run 2:** `rigour`
> Quote: "Implement validation scripts, unit tests, data quality checks"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, testing, validation, CI/CD, and governance throughout, with no mention of speed or velocity priorities.

**Run 3:** `rigour`
> Quote: "Ensure data quality, reliability, observability, and performance"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize data quality, testing, CI/CD, and reliability as core work characteristics with no counterbalancing velocity signals.

### domain_risk

**Run 1:** `moderate`
> Quote: "customer-facing BI products"
> Verified: ✓ found in JD
> Reasoning: While customer-facing, the role lacks signals of financial reporting, regulatory compliance, or direct revenue impact that would indicate high domain risk.

**Run 2:** `moderate`
> Quote: "Build and maintain customer dashboards and embedded analytics"
> Verified: ✓ found in JD
> Reasoning: The role delivers customer-facing analytics in a SaaS product environment, affecting business decisions without financial reporting or regulatory compliance consequences.

**Run 3:** `moderate`
> Quote: "5+ years in data engineering / analytics engineering for customer-facing BI products"
> Verified: ✓ found in JD
> Reasoning: Customer-facing analytics product but with no explicit signals about financial reporting, regulatory compliance, or mission-critical systems.

### collaboration_width

**Run 1:** `0`
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes technical ownership and platform work without naming specific cross-functional teams or departments as collaboration partners.

**Run 2:** `0`
> Quote: "take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: No distinct named partner functions (Finance, Product, Marketing, Engineering, etc.) are explicitly mentioned; the role emphasizes end-to-end platform ownership.

**Run 3:** `0`
> Quote: "Take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: No named internal teams or functions are identified as collaboration partners; role framing emphasizes end-to-end solo ownership.

### data_team_maturity

**Run 1:** `mid`
> Quote: "take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: The platform already exists and is customer-facing, but requires significant ownership and modernization work—characteristic of a mid-stage team.

**Run 2:** `mid`
> Quote: "Reverse-engineer vendor-built BI solution"
> Verified: ✓ found in JD
> Reasoning: The role addresses modernizing existing infrastructure rather than building from zero, indicating a maturing team with established but legacy systems requiring architectural rebuild.

**Run 3:** `mid`
> Quote: "Reverse-engineer vendor-built BI solution"
> Verified: ✓ found in JD
> Reasoning: Existing customer-facing infrastructure and named tools in use, but significant rebuilding required indicates growing mid-stage maturity rather than early or established teams.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Maintain DAX performance and dataset refresh consistency"
> Verified: ✓ found in JD
> Reasoning: Knowledge of DAX optimization and Power BI refresh mechanics indicates a hiring manager who has worked in this technical domain.

**Run 2:** `hiring_manager`
> Quote: "Design and operate scalable pipelines and lakehouse architecture"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain precise technical methodology (lakehouse architecture, star schema, DAX, multi-tenant models) and specific business context that only comes from someone who has performed this work.

**Run 3:** `hiring_manager`
> Quote: "Reverse-engineer vendor-built BI solution; Reduce technical debt and rebuild toward clean architecture"
> Verified: ⚠ NOT found verbatim
> Reasoning: Responsibilities contain company-specific context and precise technical scope (star schema, lakehouse, DAX, semantic models) that only comes from someone doing this work.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: The role's core responsibility is owning the data platform and infrastructure that happens to power customer-facing analytics.

**Run 2:** `product`
> Quote: "Build and maintain customer dashboards and embedded analytics"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly framed around delivering customer-facing BI products in a SaaS environment, positioning customers as the primary audience for the analytics delivered.

**Run 3:** `internal_data`
> Quote: "Enable self-serve analytics with governance"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary responsibility is building and operating the data platform and self-service analytics infrastructure rather than serving product, commercial, or finance teams.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'product', 'internal_data']

### autonomy_level

**Run 1:** `mixed`
> Quote: "take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of platform architecture and design with hands-on execution of technical implementations.

**Run 2:** `strategic`
> Quote: "take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: The role is positioned to set direction for the data platform and BI layer with verbs like 'own', 'design', and 'architect', combined with the explicit mindset requirement for 'strong ownership and autonomy'.

**Run 3:** `strategic`
> Quote: "take end-to-end ownership of our data platform and BI layer"
> Verified: ✓ found in JD
> Reasoning: End-to-end ownership with responsibility for defining architecture and reducing technical debt indicates strategic autonomy to shape the platform direction rather than executing scoped work.

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'strategic']

### ai_role
**Run 1:** `none` ✓
> Quote: "Own end-to-end data platform using Databricks and Microsoft Fabric"
> Reasoning: Data platform infrastructure role with named tools but no AI capabilities (coding assistants, GenAI, semantic models) in scope.

**Run 2:** `none` ✓
> Quote: "Own end-to-end data platform using Databricks and Microsoft Fabric"
> Reasoning: No AI tooling (Copilot, Claude Code) or GenAI infrastructure mentioned; stack is traditional data tools.

**Run 3:** `none` ✓
> Quote: "Own end-to-end data platform using Databricks and Microsoft Fabric"
> Reasoning: No AI coding tools, AI-ready infrastructure, or GenAI responsibilities mentioned.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Build CI/CD, testing, and versioning for pipelines"
> Reasoning: Candidate owns testing implementation with explicit ownership verb ('Build') for CI/CD and testing practices.

**Run 2:** `responsibility` ✓
> Quote: "Build CI/CD, testing, and versioning for pipelines"
> Reasoning: Ownership verb 'build' applied to testing and quality; testing is core deliverable not just tooling.

**Run 3:** `responsibility` ✓
> Quote: "Build CI/CD, testing, and versioning for pipelines"
> Reasoning: Candidate explicitly owns CI/CD, testing, and versioning responsibilities.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Ensure data quality, reliability, observability, and performance"
> Reasoning: Operational reliability concerns (reliability, observability, performance) dominate without regulatory or compliance framing.

**Run 2:** `moderate` ✓
> Quote: "Ensure data quality, reliability, observability, and performance"
> Reasoning: Operational reliability concerns (quality, observability, consistency) dominate; customer-facing BI adds business-decision risk but no regulatory/compliance language detected.

**Run 3:** `none` ✗
> Quote: "Ensure data quality, reliability, observability, and performance"
> Reasoning: Responsibilities focus on delivery and operations without regulatory compliance or trustworthiness as primary framing.

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'none']
