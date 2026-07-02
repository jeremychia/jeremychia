# Trace: 2026-07-02_ijsvogel-retail_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — IJsvogel Retail (Pets Place Boerenbond)

**URL:** https://werkenbij.ijsvogelretail.nl/vacature-hoofdkantoor/analytics-engineer
**Location:** Ede, Netherlands
**Date Posted:** 2026-07-02
**Salary:** 3,800–6,200 EUR

---

# Analytics Engineer

Company: Pets Place Boerenbond (part of IJsvogel Retail)
Job Title: Analytics Engineer
Location: Netherlands (headquarters in Ede)
Salary: EUR 3800 - EUR 6200 per month (fulltime basis)

## Key Responsibilities
The role involves translating business questions into dashboards and data solutions. The engineer designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance including GDPR compliance. The position also includes resolving pipeline issues and promoting data-driven culture across the organization.

## Requirements
Candidates need HBO+ education level and 3-5 years in similar roles. Essential skills include cloud platform experience (Google Cloud Platform/BigQuery preferred), SQL and Python programming, dbt expertise, and BI tools knowledge (preferably Looker). Understanding data architecture, governance, privacy regulations, and retail processes is required, plus interest in advanced analytics and AI applications.

## Additional Information
Contact: Stef van Hoek, Lead Data (06-42997509)
Benefits: 25 vacation days, remote work options (minimum 3 office days), travel reimbursement, 15% employee discount, and Alleo app access
Note: Acquisition approaches discouraged

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
| jd_authorship | recruiter | recruiter | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | responsibility | responsibility | 33% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, and regulatory compliance with no velocity language like 'fast-paced' or 'rapid delivery'.

**Run 2:** `rigour`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, and compliance as core expectations without any velocity or speed-oriented framing.

**Run 3:** `rigour`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, and compliance with no velocity language, making rigour the dominant orientation.

### domain_risk

**Run 1:** `moderate`
> Quote: "GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance is mentioned, the JD lacks explicit financial reporting, audit, or regulatory emphasis typical of high-risk domains, making this a moderate-risk operational retail role.

**Run 2:** `moderate`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance is mentioned, the role is focused on internal analytics in a retail context without explicit financial reporting or regulatory compliance responsibilities that would indicate high risk.

**Run 3:** `moderate`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: This is a retail role with operational reporting needs and standard EU GDPR compliance requirements, not financial reporting or regulatory audit exposure.

### collaboration_width

**Run 1:** `0`
> Quote: "No named teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD uses generic language like 'stakeholders' and 'organization' but does not explicitly name specific functions or partner teams.

**Run 2:** `0`
> Quote: "works with stakeholders on information needs"
> Verified: ✓ found in JD
> Reasoning: While the role works cross-functionally, no specific named teams or functions are explicitly identified in the JD text.

**Run 3:** `0`
> Quote: "No named partner teams explicitly listed"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions 'stakeholders' generically but does not name specific functions like Finance, Product, Marketing, or other discrete teams.

### data_team_maturity

**Run 1:** `mid`
> Quote: "designs datamodels in dbt and BigQuery"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, BigQuery) in the responsibilities section indicate an established data function with existing infrastructure, characteristic of a mid-stage team.

**Run 2:** `mid`
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The JD names specific production tools (dbt, BigQuery) in responsibilities and mentions maintaining existing infrastructure (resolving pipeline issues), indicating an established but growing data function.

**Run 3:** `mid`
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The JD references existing, named tools in active use and implies established processes, but shows no signals of a large specialized team or multiple sub-teams.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "translating business questions into dashboards and data solutions. The engineer designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs and boilerplate language without specific technical context, methodology names, or scale details that would indicate a hiring manager wrote this.

**Run 2:** `recruiter`
> Quote: "translating business questions into dashboards and data solutions; works with stakeholders on information needs"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities use generic boilerplate action verbs and lack technical specificity about actual work context, scale, or methodology that would indicate hiring manager authorship.

**Run 3:** `mixed`
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The JD combines specific technical responsibilities with named tools against generic boilerplate language like 'works with stakeholders' and 'promoting data-driven culture'.

⚠ **LLM inconsistency**: runs gave ['recruiter', 'recruiter', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data model design, governance, and infrastructure work indicates the primary focus is serving the data platform and internal data team rather than a specific commercial, product, or finance stakeholder.

**Run 2:** `internal_data`
> Quote: "translating business questions into dashboards and data solutions; monitors data quality and governance"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role focuses on building and maintaining data infrastructure and analytics solutions for organizational consumption rather than serving a specific business function.

**Run 3:** `internal_data`
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The role's core mission emphasizes building and maintaining data infrastructure (models, governance, pipelines) that serves data consumers and the platform itself.

### autonomy_level

**Run 1:** `execution`
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is to execute on stakeholder requirements and translate questions into solutions, indicating an execution-focused role without strategic ownership.

**Run 2:** `execution`
> Quote: "works with stakeholders on information needs, and monitors data quality"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize supporting stakeholder needs and maintaining existing systems rather than defining priorities or setting direction.

**Run 3:** `execution`
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The role is framed around translating and delivering against business requirements set by others, with no strategic direction-setting verbs like 'define' or 'establish'.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions 'interest in advanced analytics and AI applications' which is too vague to indicate expected AI skill, and there are no specific AI coding tools or AI infrastructure responsibilities mentioned.

**Run 2:** `none`
> Quote: "interest in advanced analytics and AI applications"
> Verified: ✓ found in JD
> Reasoning: The JD mentions AI as an area of interest but does not expect the candidate to demonstrate concrete AI skills, use AI tools, or build AI-specific data infrastructure.

**Run 3:** `none`
> Quote: "interest in advanced analytics and AI applications"
> Verified: ✓ found in JD
> Reasoning: The mention of AI is vague ('interest in') rather than a specific skill expectation for the candidate to demonstrate.

### testing_framing

**Run 1:** `absent`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: Data quality is mentioned as a monitoring responsibility rather than owning or defining testing standards, and no testing tools or frameworks are named.

**Run 2:** `responsibility`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as a core responsibility the candidate will have, even though framed as oversight (monitoring) rather than strategic ownership.

**Run 3:** `responsibility`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The candidate is accountable for monitoring data quality and governance, framing quality as an owned responsibility rather than a tool in a tech stack.

⚠ **LLM inconsistency**: runs gave ['absent', 'responsibility', 'responsibility']

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance and data quality are mentioned as operational concerns, but the overall JD framing emphasizes delivery and capability rather than risk or compliance as primary drivers.

**Run 2:** `moderate`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: While data quality and regulatory compliance are mentioned, the role framing emphasizes analytics delivery rather than risk prevention or trust, indicating moderate rather than high loss aversion.

**Run 3:** `moderate`
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The JD signals operational concerns (pipeline issues, GDPR compliance, data quality) as secondary to primary delivery responsibilities, indicating moderate risk awareness.
