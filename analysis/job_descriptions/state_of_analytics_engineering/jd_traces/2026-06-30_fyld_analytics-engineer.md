# Trace: 2026-06-30_fyld_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Fyld

**URL:** https://www.linkedin.com/jobs/view/4431082635/
**Location:** Lisbon Metropolitan Area, Portugal
**Date Posted:** 2026-06-30

---

Analytics Engineer at Fyld

Company: Fyld
Position: Analytics Engineer
Location: Lisbon Metropolitan Area
Employment Type: Full-time
Seniority Level: Mid-Senior
Posted: 22 hours ago

Job Description

Fyld is a Portuguese consulting company specializing in IT services that brings professionals into various tech domains. The organization follows sports management principles to foster peak performance among consultants, emphasizing training and excellence.

Key Requirements

Education & Experience:
- Bachelor's degree in Computer Science, IT, Engineering, or related field
- 3+ years in Analytics Engineering, Data Engineering, or BI roles

Technical Skills:
- Advanced SQL proficiency including CTEs, window functions, and query optimization
- Data modeling expertise with dimensional schemas, star schemas, and SCD patterns
- Hands-on experience with Spark and Delta Lake for transformations
- Microsoft Fabric including Lakehouse and Warehouse optimization
- Power BI semantic model knowledge
- Data quality, validation, monitoring, and observability skills
- Secure data access patterns including Row-Level Security
- Azure Data Factory or Microsoft Fabric pipelines
- Python for scripting and automation
- Git and CI/CD pipeline experience
- dbt familiarity is advantageous
- Fluent English (mandatory)

What They Offer
- Continuous learning opportunities
- Access to modern technology projects
- Collaborative team environment

Application: Candidates should send CVs to: sofia.neves@fyld.pt

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
| jd_authorship | recruiter | recruiter | recruiter | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Data quality, validation, monitoring, and observability skills"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, validation, monitoring, and observability as core technical expectations with no velocity-oriented language present.

**Run 2:** `rigour`
> Quote: "Data quality, validation, monitoring, and observability skills"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data quality, validation, monitoring, and observability signals a rigour orientation focused on correctness and reliability rather than speed or iteration.

**Run 3:** `rigour`
> Quote: "Data quality, validation, monitoring, and observability skills"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data quality, validation, monitoring, and observability indicates a rigour-oriented approach prioritizing correctness and reliability over speed.

### domain_risk

**Run 1:** `moderate`
> Quote: "Portuguese consulting company specializing in IT services"
> Verified: ✓ found in JD
> Reasoning: Without explicit mention of financial reporting, compliance, or regulatory impact, and as a staffing/IT services consulting firm, the role carries moderate risk typical of most business analytics work.

**Run 2:** `moderate`
> Quote: "Portuguese consulting company specializing in IT services that brings professionals into various tech domains"
> Verified: ✓ found in JD
> Reasoning: The generic consulting nature with no mention of financial reporting, compliance, or regulatory requirements suggests moderate risk typical of business analytics work rather than high-stakes financial or regulated domains.

**Run 3:** `moderate`
> Quote: "Power BI semantic model knowledge"
> Verified: ✓ found in JD
> Reasoning: Tools like Power BI and Microsoft Fabric are typically used for business intelligence supporting operational decisions without explicit regulatory or financial consequences.

### collaboration_width

**Run 1:** `0`
> Quote: "No named teams identified in JD"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no explicit references to named partner functions or teams; 'Collaborative team environment' is generic boilerplate that does not count.

**Run 2:** `0`
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: The JD mentions 'collaborative team environment' generically but does not explicitly name any specific partner teams or functions to collaborate with.

**Run 3:** `0`
> Quote: "Collaborative team environment"
> Verified: ✓ found in JD
> Reasoning: While collaboration is mentioned, the JD names no specific partner teams or functions to collaborate with.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Hands-on experience with Spark and Delta Lake for transformations"
> Verified: ✓ found in JD
> Reasoning: The deployed modern tech stack (Spark, Delta Lake, Microsoft Fabric, Azure Data Factory) indicates an established data function rather than early-stage, but absence of multiple specialized sub-teams suggests not yet mature.

**Run 2:** `mid`
> Quote: "Hands-on experience with Spark and Delta Lake for transformations"
> Verified: ✓ found in JD
> Reasoning: The presence of multiple specific named tools with application context (Spark, Delta Lake, Microsoft Fabric, ADF, Power BI) indicates existing infrastructure is deployed rather than early-stage greenfield.

**Run 3:** `mid`
> Quote: "The organization follows sports management principles to foster peak performance among consultants, emphasizing training and excellence."
> Verified: ✓ found in JD
> Reasoning: The established training and development infrastructure of the consulting organization suggests a mid-stage team with some organizational maturity.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "Continuous learning opportunities; Access to modern technology projects; Collaborative team environment"
> Verified: ⚠ NOT found verbatim
> Reasoning: The complete absence of a responsibilities section describing actual work and reliance on generic boilerplate benefits language indicates recruiter authorship.

**Run 2:** `recruiter`
> Quote: "Continuous learning opportunities; Access to modern technology projects; Collaborative team environment"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD entirely lacks a dedicated responsibilities section and contains only generic benefit statements and a technical checklist without context for what the person will actually do.

**Run 3:** `recruiter`
> Quote: "Hands-on experience with Spark and Delta Lake for transformations; Microsoft Fabric including Lakehouse and Warehouse optimization; Power BI semantic model knowledge"
> Verified: ⚠ NOT found verbatim
> Reasoning: A technical skills checklist without any description of actual work, problems solved, or measurable impact is typical of recruiter-written job descriptions.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Data quality, validation, monitoring, and observability skills; Secure data access patterns including Row-Level Security"
> Verified: ⚠ NOT found verbatim
> Reasoning: The emphasis on data infrastructure, platform governance, and data consumer enablement points to internal_data orientation rather than serving commercial, product, or finance stakeholders.

**Run 2:** `internal_data`
> Quote: "Data modeling expertise with dimensional schemas, star schemas, and SCD patterns"
> Verified: ✓ found in JD
> Reasoning: The infrastructure and platform-focused technical emphasis without naming external business stakeholders (sales, product, finance, customers) suggests orientation toward supporting the data team and analytics consumers.

**Run 3:** `internal_data`
> Quote: "Data quality, validation, monitoring, and observability skills"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data infrastructure, quality, and observability rather than business outcomes or stakeholder-facing work indicates the role primarily serves the analytics/data function itself.

### autonomy_level

**Run 1:** `execution`
> Quote: "Hands-on experience with Spark and Delta Lake for transformations"
> Verified: ✓ found in JD
> Reasoning: The skills-focused requirements with no strategic direction-setting language indicate the role is primarily technical execution rather than defining analytics direction.

**Run 2:** `execution`
> Quote: "Seniority Level: Mid-Senior"
> Verified: ✓ found in JD
> Reasoning: Mid-Senior level roles typically execute on scoped work and specific technical deliverables rather than establishing strategic direction or defining how analytics should be delivered.

**Run 3:** `execution`
> Quote: "Hands-on experience with Spark and Delta Lake for transformations"
> Verified: ✓ found in JD
> Reasoning: The 'hands-on' language and technical skill requirements emphasize executing defined data engineering work rather than setting strategic direction.
