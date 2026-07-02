# Trace: 2026-07-02_amazon_business-intelligence-engineer-whs-data

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Engineer, WHS Data — Amazon EU Sarl

**URL:** https://www.amazon.jobs/en/jobs/10463343/business-intelligence-engineer-whs-data?cmpid=SPLICX0248M&ss=paid
**Location:** Luxembourg
**Date Posted:** 2026-07-02

---

# Business Intelligence Engineer, WHS Data

Company: Amazon EU Sarl
Job ID: 10463343
Location: Luxembourg (LUX)
Salary: Not stated

## Key Responsibilities
- Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems
- Conducting analytical deep dives and formulating recommendations for leadership
- Identifying opportunities to drive analytical reporting and business strategy
- Creating written insights for stakeholders on metric development
- Automating reporting, audits, and other data-driven activities
- Partnering with Data Engineering teams to enhance data infrastructure
- Developing best practices in data integrity and documentation
- Learning new technologies to support innovation

## Requirements
Basic Qualifications:
- Bachelor's degree in BI, finance, engineering, statistics, computer science, mathematics, or equivalent quantitative field
- 3+ years analyzing/interpreting data with Redshift, Oracle, NoSQL
- Data modeling, warehousing, and ETL pipeline experience
- Data visualization experience (Tableau, Quicksight, or similar)

Preferred Qualifications:
- Master's degree in related quantitative field
- 5+ years data analysis experience
- AWS solutions expertise (EC2, DynamoDB, S3, Redshift)
- Data mining experience with large-scale, complex datasets

Team & Culture: The team emphasizes work-life balance, inclusive culture, and mentorship with career growth opportunities.

Interview Process & Tools: Not specified in posting.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 1 | 1 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | recruiter | mixed | recruiter | 33% |
| stakeholder_orientation | internal_data | internal_data | mixed | 33% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | responsibility | responsibility | 33% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, best practices, and documentation without any velocity signals like shipping, fast-paced work, or iteration speed.

**Run 2:** `rigour`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data integrity, audits, and best practices without any velocity-oriented language like 'fast-paced' or 'move quickly', indicating a rigour-focused orientation.

**Run 3:** `rigour`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: Rigour signals (data integrity, best practices, documentation, audits) significantly outnumber velocity signals in the responsibilities section.

### domain_risk

**Run 1:** `moderate`
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: Warehouse operations data affects business decisions but lacks explicit regulatory, compliance, or financial reporting language that would elevate this to high risk.

**Run 2:** `moderate`
> Quote: "Identifying opportunities to drive analytical reporting and business strategy"
> Verified: ✓ found in JD
> Reasoning: The role supports business strategy and operational decisions but the JD uses no language about financial reporting, regulatory compliance, or audit-critical impacts that would indicate high risk.

**Run 3:** `moderate`
> Quote: "identifying opportunities to drive analytical reporting and business strategy"
> Verified: ✓ found in JD
> Reasoning: Data errors affect warehouse/logistics business decisions without explicit regulatory, compliance, or financial reporting framing, indicating moderate operational risk rather than high.

### collaboration_width

**Run 1:** `1`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Only one named team is explicitly identified in the JD; other references like 'leadership' and 'stakeholders' are too generic to count as distinct partner functions.

**Run 2:** `1`
> Quote: "Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named partner function (Data Engineering teams) is mentioned; 'leadership' and 'stakeholders' are generic role references, not distinct collaborating teams.

**Run 3:** `1`
> Quote: "Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Only one named partner function (Data Engineering) is explicitly identified; 'stakeholders' and 'leadership' are too generic to count.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Multiple data roles (Data Engineering teams exist alongside this BI Engineer) and named infrastructure tools (Redshift, Tableau) indicate a growing but not yet mature data organization.

**Run 2:** `mid`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The plural 'teams' and verb 'enhance' indicate infrastructure and multiple data roles already exist; the focus is on improving rather than building from zero.

**Run 3:** `mid`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The plural 'teams' and expectation to enhance existing infrastructure indicate a multi-person data function in growth phase, not early-stage or fully mature.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs and absence of technical specificity about how tools are applied to warehouse operations suggest recruiter authorship rather than hiring manager insight.

**Run 2:** `mixed`
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic boilerplate language ('contributing', 'delivering') typical of recruiter writing, while the requirements section shows technical specificity (Redshift, Tableau, AWS services) suggesting hiring manager involvement.

**Run 3:** `recruiter`
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs ('contributing', 'formulating', 'identifying opportunities') and vague problem framing lack the technical specificity and context that hiring managers provide.

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The explicit partnership with Data Engineering and focus on building data infrastructure position this role as serving the data platform and analytics function, not a specific commercial, product, or finance stakeholder.

**Run 2:** `internal_data`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes developing analytics infrastructure, working with data teams, and establishing best practices rather than serving commercial, product, or finance-specific audiences.

**Run 3:** `mixed`
> Quote: "formulating recommendations for leadership; Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role balances business stakeholder service (leadership strategy recommendations) equally with data platform/infrastructure work, creating dual audience orientation.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'mixed']

### autonomy_level

**Run 1:** `execution`
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: The use of 'contributing to' rather than 'owning' or 'defining' indicates the role executes within a team framework rather than independently setting analytical direction.

**Run 2:** `execution`
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The role 'contributes to' and 'partners with' rather than 'leads', 'owns', or 'defines', indicating the candidate executes within existing frameworks rather than setting strategic direction.

**Run 3:** `execution`
> Quote: "Contributing to the design, implementation, and delivery of BI solutions"
> Verified: ✓ found in JD
> Reasoning: The verb 'contributing' and emphasis on delivery rather than defining direction indicate the role executes scoped work rather than setting analytics strategy.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI tools, machine learning, LLMs, or AI-assisted coding expected of the candidate.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no explicit AI skill expectations; 'learning new technologies' is too vague to indicate a specific AI requirement.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI skills, tools, GenAI applications, or agentic workflows expected of the candidate.

### testing_framing

**Run 1:** `absent`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: Data integrity is mentioned but testing practices, data contracts, or observability frameworks are not explicitly named or framed as a responsibility.

**Run 2:** `responsibility`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The verb 'developing' frames data integrity and quality as something the candidate will establish and own through best practices, not merely use existing tools.

**Run 3:** `responsibility`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The action verb 'Developing' indicates the role owns and defines data integrity practices rather than using pre-existing tools.

⚠ **LLM inconsistency**: runs gave ['absent', 'responsibility', 'responsibility']

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Automating reporting, audits, and other data-driven activities"
> Verified: ✓ found in JD
> Reasoning: Audits and data integrity practices suggest concern with operational reliability but lack regulatory or compliance language that would indicate high loss aversion.

**Run 2:** `moderate`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are concerns (audits, integrity), but the JD emphasizes operational best practices rather than regulatory risk, compliance, or preventing bad data from reaching stakeholders.

**Run 3:** `moderate`
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: Data integrity concerns are present and suggest operational reliability matters, but the framing emphasizes building practices rather than preventing compliance violations or critical stakeholder trust failure.
