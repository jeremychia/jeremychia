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

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 1 | 1 | 1 | 1 | 100% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | recruiter | recruiter | recruiter | 100% | ✗ |
| stakeholder_orientation | internal_data | mixed | internal_data | finance | 0% | ✗ |
| autonomy_level | mixed | execution | execution | execution | 100% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data integrity, documentation, and audits reflects a rigour orientation focused on quality and governance rather than speed or velocity.

**Run 2:** `rigour` ✓
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data integrity and best practices development with no velocity language, indicating a rigour orientation.

**Run 3:** `rigour` ✓
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data integrity, best practices, and conducting deep analytical work signals a rigour-oriented role without velocity language.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Conducting analytical deep dives and formulating recommendations for leadership"
> Verified: ✓ found in JD
> Reasoning: The JD uses generic analytical language without explicit financial, compliance, or regulatory signals typical of high-risk domains.

**Run 2:** `moderate` ✓
> Quote: "Identifying opportunities to drive analytical reporting and business strategy"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes general business intelligence and strategy support without explicit financial reporting, compliance, or regulatory language that would signal high domain risk.

**Run 3:** `moderate` ✓
> Quote: "Conducting analytical deep dives and formulating recommendations for leadership"
> Verified: ✓ found in JD
> Reasoning: The role supports leadership decisions on warehouse operations without explicit financial, regulatory, or compliance framing, indicating moderate domain risk.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named team (Data Engineering) is identified as a collaboration partner.

**Run 2:** `1` ✓
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Only Data Engineering is explicitly named as a collaboration partner in the responsibilities section.

**Run 3:** `1` ✓
> Quote: "Partnering with Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Only Data Engineering teams is explicitly named; other references to stakeholders and leadership are generic.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Reference to existing Data Engineering teams and infrastructure being enhanced indicates a function that is established and growing but not yet mature at scale.

**Run 2:** `mid` ✗
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The existence of named Data Engineering teams and focus on enhancing existing infrastructure signals a mid-stage data function rather than early-stage establishment or mature specialization.

**Run 3:** `mid` ✗
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The existence of Data Engineering teams and explicit reference to enhancing existing infrastructure indicates an established mid-stage function rather than early-stage build.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `recruiter` ✗
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: Boilerplate action verbs and generic responsibilities without specific tools, scale, or methodological context indicate recruiter authorship rather than hands-on domain expertise.

**Run 2:** `recruiter` ✗
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs without specific technical context about tools, workflows, or scale that would indicate hiring manager authorship.

**Run 3:** `recruiter` ✗
> Quote: "Conducting analytical deep dives and formulating recommendations for leadership"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs without specific technical context, scale metrics, or methodology names indicate recruiter boilerplate rather than hiring manager expertise.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`recruiter`

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `mixed` ✗
> Quote: "Conducting analytical deep dives and formulating recommendations for leadership; Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The role serves both executive leadership for strategic insights and the internal data function for infrastructure improvement, with roughly equal emphasis.

**Run 2:** `internal_data` ✓
> Quote: "Partnering with Data Engineering teams to enhance data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The primary named partnership is with Data Engineering, and the explicit focus on enhancing data infrastructure positions the role as serving the data function and its platform consumers.

**Run 3:** `finance` ✗
> Quote: "Identifying opportunities to drive analytical reporting and business strategy"
> Verified: ✓ found in JD
> Reasoning: The focus on business strategy and analytical recommendations for warehouse operations, which directly impacts COGS and inventory valuation, signals finance as the primary stakeholder.

⚠ **Disagreement**: manual=`internal_data` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'finance']

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Contributing to the design, implementation, and delivery of BI solutions"
> Verified: ✓ found in JD
> Reasoning: The verb 'contributing to' and focus on delivery indicate execution of priorities set by others rather than strategic ownership.

**Run 2:** `execution` ✗
> Quote: "Contributing to the design, implementation, and delivery of BI solutions"
> Verified: ✓ found in JD
> Reasoning: The primary framing uses 'contributing to' and execution-oriented verbs, suggesting the role executes on direction set by others rather than independently setting that direction.

**Run 3:** `execution` ✗
> Quote: "Contributing to the design, implementation, and delivery of BI solutions for complex and ambiguous problems"
> Verified: ✓ found in JD
> Reasoning: The verb 'contributing to' and focus on delivering solutions to defined problems indicates execution within set organizational direction rather than strategic autonomy.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no explicit or implicit expectations for AI coding tools or AI infrastructure skills from the candidate.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no explicit mention of AI tools, skills, or infrastructure that the candidate would be expected to use or enable.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI-assisted coding tools, AI pipelines, or AI skill expectations; technology references are limited to databases and visualization tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The action verb 'developing' paired with 'best practices in data integrity' indicates the candidate is expected to own or define data integrity practices.

**Run 2:** `responsibility` ✗
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The use of 'developing best practices' with an ownership verb indicates the candidate is expected to define and own data integrity standards, framing it as a responsibility rather than a listed tool.

**Run 3:** `responsibility` ✗
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: The role explicitly owns responsibility for developing data integrity best practices, indicating accountability for quality practices even without naming specific tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Automating reporting, audits, and other data-driven activities"
> Verified: ✓ found in JD
> Reasoning: The mention of audits indicates operational reliability is a concern, but overall framing emphasizes analytical delivery over risk prevention.

**Run 2:** `moderate` ✗
> Quote: "Developing best practices in data integrity and documentation"
> Verified: ✓ found in JD
> Reasoning: While data integrity is mentioned as an ownership area, there is no explicit compliance, regulatory, or risk language that would signal high loss aversion, indicating moderate operational reliability concern.

**Run 3:** `moderate` ✗
> Quote: "Automating reporting, audits, and other data-driven activities"
> Verified: ✓ found in JD
> Reasoning: Mention of audits and data integrity suggests operational reliability concerns, but lacks explicit risk, compliance, or stakeholder trust framing required for high classification.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
