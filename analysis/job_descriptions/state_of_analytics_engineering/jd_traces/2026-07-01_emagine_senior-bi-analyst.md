# Trace: 2026-07-01_emagine_senior-bi-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Senior BI Analyst — emagine

**URL:** https://portal.emagine.org/jobs/178078/senior-bi-analyst
**Location:** Not stated in JD
**Date Posted:** 2026-07-01

---

Senior BI Analyst at emagine

Department: Data & Analytics
Sector: Government
Job ID: #316289
Start date: 02.11.2026
Duration: > 12 months
Language: English/Full professional
Seniority: Senior

About emagine
emagine is a dynamic, fast-growing international consulting and technology company, founded on real-world experience, focused on custom-fit solutions. We have the proven people and expertise to complete complex projects, while delivering lasting knowledge-transfer benefits to empower our partners for the next challenge.

Key Responsibilities as BI Analyst:
- Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases.
- Monitor and analyze data quality, integrity, and processing logs, identifying issues and collaborating with technical teams to resolve them.
- Produce ad hoc analytical reports and data extracts to support inspections, audits, data validation, and the investigation of data defects.
- Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes.
- Collaborate with project teams to deliver business and technical documentation, including data mapping and transformation rules.
- Support the design of data migration and integration processes, ensuring data quality and availability.
- Analyze data across SQL and other enterprise platforms to support operational use cases.
- Develop Data Management Plans, including governance, data flows, and controls.
- Contribute to the design and documentation of logical and physical data models.

Key Requirements:
- Proven experience in data analysis, quality assessment, validation, reconciliation, and anomaly detection.
- Experience in supporting or coordinating data testing and validation processes.
- Ability to analyze data processing outputs to identify issues and trends.
- Experience in producing ad hoc reports and data extracts for operational requirements.
- Skilled in interpreting data and presenting findings to stakeholders.
- Experience in developing technical documentation, including data mappings and transformation logic.
- Understanding logical and physical data models and documenting them appropriately.
- Experience querying and analyzing data using SQL.
- Strong analytical and problem-solving skills with attention to detail.

Nice to Have:
- Familiarity with data governance frameworks.
- Experience in integrating data from multiple sources.
- Knowledge of data lineage and process mappings.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | moderate | moderate | 33% |
| collaboration_width | 0 | 0 | 0 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | recruiter | recruiter | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | high | moderate | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Monitor and analyze data quality, integrity, and processing logs, identifying issues and collaborating with technical teams to resolve them."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data validation, testing, audits, quality monitoring, and governance as core expectations, with no signals of speed or rapid delivery.

**Run 2:** `rigour`
> Quote: "Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases."
> Verified: ✓ found in JD
> Reasoning: The opening responsibility establishes testing and validation as the core orientation, with no speed or iteration language present throughout the JD.

**Run 3:** `rigour`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, quality, testing, and controls throughout with no velocity signals.

### domain_risk

**Run 1:** `high`
> Quote: "to support inspections, audits, data validation, and the investigation of data defects"
> Verified: ✓ found in JD
> Reasoning: Government sector combined with explicit language around audits, inspections, and data integrity indicates regulatory compliance and risk exposure.

**Run 2:** `moderate`
> Quote: "to support inspections, audits, data validation, and the investigation of data defects"
> Verified: ✓ found in JD
> Reasoning: While audits and government sector suggest compliance concern, the JD frames work around operational data quality and testing rather than financial reporting or regulatory compliance.

**Run 3:** `moderate`
> Quote: "supporting inspections, audits, data validation, and the investigation of data defects"
> Verified: ⚠ NOT found verbatim
> Reasoning: Government sector and audit references indicate regulatory concern, but explicit compliance or financial-reporting language is absent from the JD.

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']

### collaboration_width

**Run 1:** `0`
> Quote: "No named partner teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: Only generic terms like 'technical teams', 'project teams', and 'stakeholders' appear; no specific named functions or departments are listed.

**Run 2:** `0`
> Quote: "None"
> Verified: ⚠ NOT found verbatim
> Reasoning: References to 'project teams' and 'technical teams' are generic descriptors, not named functions like Finance, Product, or Engineering.

**Run 3:** `0`
> Quote: "Collaborate with project teams to deliver business and technical documentation"
> Verified: ✓ found in JD
> Reasoning: Collaboration references are generic ('project teams', 'technical teams', 'stakeholders') and do not name specific partner functions like Finance, Product, or Engineering.

### data_team_maturity

**Run 1:** `mid`
> Quote: "supporting migration and ongoing data pipeline releases"
> Verified: ✓ found in JD
> Reasoning: The role supports established pipelines and data governance work rather than building from zero, but language like 'supporting migration' suggests significant evolution underway.

**Run 2:** `mid`
> Quote: "Monitor and analyze data quality, integrity, and processing logs, identifying issues and collaborating with technical teams to resolve them."
> Verified: ✓ found in JD
> Reasoning: The JD describes supporting and monitoring existing infrastructure, data pipelines, and processes, indicating an established data function requiring operational support.

**Run 3:** `mid`
> Quote: "supporting migration and ongoing data pipeline releases"
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure and pipelines are mentioned, indicating the data function already exists and is being scaled or enhanced through migration.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls"
> Verified: ✓ found in JD
> Reasoning: Some responsibilities show governance and modeling specificity, but generic action verbs like 'assist', 'support', and 'contribute' dominate; no named tools or technical context provided.

**Run 2:** `recruiter`
> Quote: "Produce ad hoc analytical reports and data extracts to support inspections, audits, data validation, and the investigation of data defects."
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs without technical specificity—no named tools, scale metrics, or methodologies that would indicate hiring manager authorship.

**Run 3:** `recruiter`
> Quote: "Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes."
> Verified: ✓ found in JD
> Reasoning: Generic action verbs and absence of specific technical context—no named tools, scale numbers, or methodology details—indicate recruiter authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls"
> Verified: ✓ found in JD
> Reasoning: The role is focused on data platform governance, quality assurance, and data infrastructure rather than serving commercial, product, or finance stakeholders.

**Run 2:** `internal_data`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls."
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the data function itself through data management, quality governance, and supporting internal operations rather than external commercial or product audiences.

**Run 3:** `internal_data`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls."
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the data function itself through quality assurance, governance, and data architecture rather than external business stakeholders.

### autonomy_level

**Run 1:** `execution`
> Quote: "Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize 'assist', 'support', 'contribute', and 'collaborate' rather than 'define', 'own', or 'lead', indicating delivery against scope set by others.

**Run 2:** `execution`
> Quote: "Assist in identifying, analyzing, and investigating data issues, and contribute to testing and resolution processes."
> Verified: ✓ found in JD
> Reasoning: The responsibility verbs—assist, contribute, support, coordinate—indicate execution within defined scopes rather than strategic direction-setting.

**Run 3:** `execution`
> Quote: "Support the design of data migration and integration processes, ensuring data quality and availability."
> Verified: ✓ found in JD
> Reasoning: The 'support' framing and focus on executing within a defined migration scope indicate delivery of others' direction rather than independent strategy-setting.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-enabled infrastructure, or AI skill expectations from the candidate.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI-assisted coding tools, GenAI, text-to-SQL, or AI/ML infrastructure expectations anywhere in the JD.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no expectations for AI-assisted coding, AI-ready data infrastructure, or GenAI applications.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Coordinate and execute data validation and acceptance testing activities"
> Verified: ✓ found in JD
> Reasoning: Data validation and testing are framed as activities the candidate coordinates and executes, indicating owned rather than just tool-listed practices.

**Run 2:** `responsibility`
> Quote: "Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases."
> Verified: ✓ found in JD
> Reasoning: Testing and validation are the opening responsibility with explicit coordination and execution verbs, establishing testing as an owned accountability even if not full strategic definition.

**Run 3:** `responsibility`
> Quote: "Coordinate and execute data validation and acceptance testing activities, supporting migration and ongoing data pipeline releases."
> Verified: ✓ found in JD
> Reasoning: Testing and quality assurance are framed as owned responsibilities with action verbs (coordinate, execute, monitor), not as tool usage.

### loss_aversion_framing

**Run 1:** `high`
> Quote: "to support inspections, audits, data validation, and the investigation of data defects"
> Verified: ✓ found in JD
> Reasoning: Government sector combined with prominent emphasis on audits, inspections, data integrity, and governance indicates regulatory compliance and risk mitigation are primary concerns.

**Run 2:** `moderate`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls."
> Verified: ✓ found in JD
> Reasoning: Governance and control language, plus audit mention, signal operational risk management, but without high-risk regulatory or compliance framing.

**Run 3:** `moderate`
> Quote: "Develop Data Management Plans, including governance, data flows, and controls."
> Verified: ✓ found in JD
> Reasoning: Governance and controls language, combined with audit references, reflect operational reliability and data quality risk consciousness rather than compliance or stakeholder-trust catastrophe.

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']
