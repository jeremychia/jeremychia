# Trace: 2026-06-25_adsquare_staff-data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
Staff Data Analytics Engineer (m/f/d)
Company: Adsquare GmbH
Location: Berlin
Employment Type: Full-time, Permanent
Salary: €90,000 - €100,000 annually
Start Date: ASAP
Work Model: Hybrid

About Adsquare:
Adsquare is the global audience & location intelligence company with eight international offices. They are pioneers in data-driven advertising, emphasizing innovation, reliability, and transparent client partnerships.

Core Responsibilities:
- Design horizontally scalable, cost-efficient, production-grade data solutions handling terabyte-scale datasets
- Act as principal architect for the squad, championing test-driven development practices and engineering excellence
- Cross-squad collaboration solving architectural challenges spanning multiple teams while maintaining technical alignment
- Build domain expertise in location intelligence and audience attributes
- Build data observability frameworks for multi-terabyte data streams
- Communicate complex architectural trade-offs for non-technical stakeholders

Required Qualifications:
- 7+ years in Data Engineering, Analytics Engineering, or Backend Development specializing in massive data systems
- Geo-spatial and time-series data expertise
- Advanced Python proficiency with strong object-oriented design and TDD experience
- Architectural vision for scalable data warehouses (Snowflake, Redshift, Athena)
- Mastery of SQL, dbt, Apache Spark/PySpark
- AWS cloud services (Lambda, Batch, Glue, StepFunctions)
- Leadership abilities enabling communication of complex architectural trade-offs for non-technical stakeholders

Benefits:
- €1,200 annual professional development budget
- 30 vacation days yearly
- Urban Sports Club membership
- Company pension scheme
- Flexible/remote work options
- Team and company events
- Latest hardware and equipment

Recruitment Process:
Five-stage evaluation: 30-minute take-home technical quiz, 30-minute values interview, 1.5-hour technical deep-dive, practical data challenge, and team meet-and-greet.

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
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | strategic | strategic | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Act as principal architect for the squad, championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize test-driven development, engineering excellence, production-grade quality, and observability—no velocity or shipping-speed language appears.

**Run 2:** `rigour`
> Quote: "championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes test-driven development, production-grade quality, and engineering excellence as core responsibilities, with no language about speed or rapid delivery.

**Run 3:** `rigour`
> Quote: "Act as principal architect for the squad, championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes production-grade solutions, test-driven development, engineering excellence, and data observability frameworks with no velocity signals like fast-paced or MVP delivery.

### domain_risk

**Run 1:** `moderate`
> Quote: "pioneers in data-driven advertising"
> Verified: ✓ found in JD
> Reasoning: While the company operates in advertising technology, the JD contains no explicit signals around financial reporting, compliance, regulatory, or mission-critical consequences that would elevate this to high risk.

**Run 2:** `moderate`
> Quote: "data-driven advertising"
> Verified: ✓ found in JD
> Reasoning: The advertising and data intelligence sector involves business decision impact through client relationships, but lacks financial reporting, regulatory, or compliance implications that would elevate risk to high.

**Run 3:** `moderate`
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions handling terabyte-scale datasets"
> Verified: ✓ found in JD
> Reasoning: The role supports advertising and location intelligence decisions, but lacks explicit signals of financial reporting, regulatory compliance, or audit-critical responsibilities that would elevate to high risk.

### collaboration_width

**Run 1:** `0`
> Quote: "Cross-squad collaboration solving architectural challenges spanning multiple teams"
> Verified: ✓ found in JD
> Reasoning: The JD mentions 'squad' and 'multiple teams' and 'non-technical stakeholders' but does not name any specific functions, departments, or partner teams.

**Run 2:** `0`
> Quote: "Cross-squad collaboration solving architectural challenges spanning multiple teams while maintaining technical alignment"
> Verified: ✓ found in JD
> Reasoning: While collaboration across teams is mentioned, no specific partner functions (Product, Finance, Engineering, Sales, etc.) are explicitly named in the JD.

**Run 3:** `0`
> Quote: "Cross-squad collaboration solving architectural challenges spanning multiple teams"
> Verified: ✓ found in JD
> Reasoning: The JD references squads and teams generically without naming specific partner functions like Finance, Product, Marketing, Engineering, or Data Science.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Cross-squad collaboration solving architectural challenges spanning multiple teams while maintaining technical alignment"
> Verified: ✓ found in JD
> Reasoning: The existence of multiple established squads and focus on architectural alignment indicates a data function that has moved beyond early-stage infrastructure building but lacks signals of a large, highly specialized mature org.

**Run 2:** `mid`
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, Spark, Snowflake) and established squads exist, but the emphasis on building and scaling observability infrastructure indicates a growing rather than mature data function.

**Run 3:** `mid`
> Quote: "Cross-squad collaboration solving architectural challenges spanning multiple teams while maintaining technical alignment"
> Verified: ✓ found in JD
> Reasoning: Multiple squads and teams exist with established infrastructure (dbt, Snowflake), but the organization is not described as a large, highly specialized mature establishment.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: The specific framing of observability needs at terabyte scale and understanding of the precise technical challenges involved reflects hands-on experience that a recruiter would not naturally articulate.

**Run 2:** `hiring_manager`
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions handling terabyte-scale datasets"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical context (terabyte-scale, production-grade, cost-efficiency, geo-spatial and time-series expertise) that reflects hands-on domain knowledge rather than generic recruiter language.

**Run 3:** `hiring_manager`
> Quote: "Design horizontally scalable, cost-efficient, production-grade data solutions handling terabyte-scale datasets"
> Verified: ✓ found in JD
> Reasoning: Specific technical context (terabyte-scale), domain expertise (location intelligence), and named practices (test-driven development, data observability frameworks) are too precise for generic recruiter language.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: The primary focus across responsibilities is building internal data platform capabilities—scalable solutions, observability frameworks, architectural leadership—serving data team consumers rather than commercial, product, or finance functions.

**Run 2:** `internal_data`
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Verified: ✓ found in JD
> Reasoning: Core responsibilities focus on building and scaling data infrastructure and platforms for internal data consumers, not on commercial, product, or financial audiences.

**Run 3:** `internal_data`
> Quote: "Act as principal architect for the squad, championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: Responsibilities focus on building data infrastructure, architectural capability, and technical alignment for the data function itself, not on serving commercial, product, or financial stakeholders.

### autonomy_level

**Run 1:** `strategic`
> Quote: "Act as principal architect for the squad, championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: The 'principal architect' title combined with responsibility to champion practices indicates direction-setting and standards-setting authority, not execution of work scoped by others.

**Run 2:** `strategic`
> Quote: "Act as principal architect for the squad, championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: The principal architect title combined with championing practices and building new capabilities (domain expertise, observability frameworks) indicates authority to set technical direction and shape how the data function operates.

**Run 3:** `strategic`
> Quote: "Act as principal architect for the squad, championing test-driven development practices and engineering excellence"
> Verified: ✓ found in JD
> Reasoning: The principal architect role and emphasis on championing practices and defining architectural solutions indicate strategic autonomy to shape the data function's direction and standards.

### ai_role
**Run 1:** `none` ✓
> Quote: ""
> Reasoning: No signals of AI usage, AI-first approach, or AI infrastructure building in the job description.

**Run 2:** `none` ✓
> Quote: "Mastery of SQL, dbt, Apache Spark/PySpark"
> Reasoning: No AI skill requirement; focuses on traditional data engineering tools and languages.

**Run 3:** `none` ✓
> Quote: "Mastery of SQL, dbt, Apache Spark/PySpark"
> Reasoning: No AI-specific skills or tools mentioned; standard data engineering technical stack


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "championing test-driven development practices and engineering excellence"
> Reasoning: Candidate owns and champions TDD practices, indicating direct responsibility for quality and testing culture.

**Run 2:** `responsibility` ✓
> Quote: "championing test-driven development practices and engineering excellence"
> Reasoning: Candidate owns establishment and promotion of testing practices and quality standards.

**Run 3:** `responsibility` ✓
> Quote: "championing test-driven development practices and engineering excellence"
> Reasoning: Candidate owns/champions TDD as a practice, indicating responsibility for quality standards and testing discipline


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Reasoning: Operational reliability concern through data observability infrastructure suggests moderate loss-aversion framing around pipeline stability.

**Run 2:** `moderate` ✓
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Reasoning: Operational reliability focus suggests moderate risk mitigation through pipeline stability monitoring.

**Run 3:** `moderate` ✓
> Quote: "Build data observability frameworks for multi-terabyte data streams"
> Reasoning: Focus on observability for large-scale pipelines reflects concern for operational reliability and incident prevention

