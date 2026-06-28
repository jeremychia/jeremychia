# Trace: 2026-06-27_sisu-group_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Sisu Group

**Location:** Tallinn
**Date Posted:** 2026-06-27

---

Sisu Group is a fast-growing iGaming startup with 170+ employees across Tallinn and Malaga offices. The organization launched ReSpin.com and Epicbet.com in 2024 and has secured €21M in funding. The company is on a mission to redefine the future of iGaming and sports betting by building cutting-edge technology.

Hiring for: Senior Analytics Engineer
Department: Revenues
Location: Tallinn

## Key Responsibilities

- Design and build clear, compelling visualizations, dashboards, and reports using BI tools like Power BI, Tableau, etc.
- Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform
- Configure critical data connections to ensure smooth information flow across platforms
- Implement validation processes to guarantee data accuracy and reliability
- Work with product and development teams to enhance data structures
- Stay current with industry trends and emerging technologies

## Required Qualifications

- Minimum 3+ years of hands-on experience in data analysis and engineering
- Expert-level SQL skills, with a strong grasp of performance optimization and data transformation logic
- Experience designing scalable analytical datasets and dimensional data modeling
- Proficiency with BI tools like Power BI or Tableau
- Strong pipeline orchestration experience using Airflow, Dataform, or DBT
- Basic Python skills for integrations and scripting
- Excellent English communication and presentation abilities
- Demonstrated collaboration experience with Marketing, Finance, and Product teams

## Culture & Benefits

- Competitive compensation and stock options
- Generous paid time off
- Collaborative, non-corporate workplace culture
- Values: collaboration, open communication, treating all team members as equals
- Encourages proactive ownership and professional growth

Contact: Ginta Baranauskaite, TA & People Specialist

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 4 | 4 | 4 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | mixed | recruiter | 33% |
| stakeholder_orientation | internal_data | commercial | finance | 0% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Implement validation processes to guarantee data accuracy and reliability"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly emphasizes validation, guarantees, and reliability across multiple responsibility items, with no velocity signals like rapid iteration or shipping pace.

**Run 2:** `rigour`
> Quote: "Implement validation processes to guarantee data accuracy and reliability"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data accuracy, reliability, and validation—core rigour concerns—without corresponding velocity language.

**Run 3:** `rigour`
> Quote: "Implement validation processes to guarantee data accuracy and reliability"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize accuracy, validation, and reliability as core expectations with no counterbalancing velocity language like shipping, iteration, or speed.

### domain_risk

**Run 1:** `moderate`
> Quote: "Implement validation processes to guarantee data accuracy and reliability"
> Verified: ✓ found in JD
> Reasoning: While iGaming is a regulated sector, the JD emphasizes data quality without explicitly referencing financial reporting, compliance, or regulatory requirements.

**Run 2:** `moderate`
> Quote: "Department: Revenues"
> Verified: ✓ found in JD
> Reasoning: The revenue operations context suggests business-critical data decisions, but the JD contains no explicit regulatory, compliance, or financial reporting language.

**Run 3:** `moderate`
> Quote: "Department: Revenues"
> Verified: ✓ found in JD
> Reasoning: The Revenues department has financial implications, but the JD lacks explicit regulatory, compliance, or financial reporting language that would elevate this to high risk.

### collaboration_width

**Run 1:** `4`
> Quote: "product; development; Marketing; Finance"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct teams are explicitly named in collaboration contexts: product, development, Marketing, and Finance.

**Run 2:** `4`
> Quote: "product and development teams; Marketing, Finance, and Product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct teams are explicitly named: Product, Development, Marketing, and Finance.

**Run 3:** `4`
> Quote: "Work with product and development teams to enhance data structures; Demonstrated collaboration experience with Marketing, Finance, and Product teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions are identified: Product, Development, Marketing, and Finance.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities with build/maintain language indicates an established data function that is evolving, not greenfield or highly specialized.

**Run 2:** `mid`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in responsibility context (not just requirements), suggesting an existing data infrastructure that the role maintains and enhances rather than building from zero.

**Run 3:** `mid`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform"
> Verified: ✓ found in JD
> Reasoning: The existence of established infrastructure (warehouse, pipelines, BI tools) being maintained and extended indicates a mid-stage data function rather than early-stage greenfield or large mature organization.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform; Expert-level SQL skills, with a strong grasp of performance optimization and data transformation logic"
> Verified: ⚠ NOT found verbatim
> Reasoning: Combines specific technical methodology names (dimensional modeling, performance optimization) and named tools with generic responsibility phrasing (collaborate, work with teams).

**Run 2:** `mixed`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about named tools and methodologies is balanced by generic collaborative language and limited business application depth.

**Run 3:** `recruiter`
> Quote: "Design and build clear, compelling visualizations, dashboards, and reports using BI tools like Power BI, Tableau, etc.; Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities use generic action verbs and list tools without specific context, methodology, scale numbers, or technical challenges that would indicate hands-on hiring manager authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines"
> Verified: ✓ found in JD
> Reasoning: Core responsibilities emphasize building and maintaining analytical infrastructure rather than serving a specific business function directly.

**Run 2:** `commercial`
> Quote: "Demonstrated collaboration experience with Marketing, Finance, and Product teams"
> Verified: ✓ found in JD
> Reasoning: The role sits in the Revenues department and explicitly collaborates with Marketing, Finance, and Product teams in a commercial/revenue-operations context.

**Run 3:** `finance`
> Quote: "Demonstrated collaboration experience with Marketing, Finance, and Product teams"
> Verified: ✓ found in JD
> Reasoning: The Revenues department placement combined with explicit Finance team collaboration indicates the primary audience is financial reporting and revenue analysis.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'commercial', 'finance']

### autonomy_level

**Run 1:** `execution`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize execution tasks (build, maintain, configure, implement) with no language about defining strategy or shaping analytical direction.

**Run 2:** `execution`
> Quote: "Build and maintain robust data warehouse solutions and transformation pipelines using tools like Airflow or Dataform"
> Verified: ✓ found in JD
> Reasoning: Responsibilities focus on building and maintaining technical systems within a defined scope rather than shaping analytics strategy or direction.

**Run 3:** `execution`
> Quote: "Work with product and development teams to enhance data structures"
> Verified: ✓ found in JD
> Reasoning: The language emphasizes enhancing and supporting existing structures and team needs rather than defining strategy or establishing new directions.
