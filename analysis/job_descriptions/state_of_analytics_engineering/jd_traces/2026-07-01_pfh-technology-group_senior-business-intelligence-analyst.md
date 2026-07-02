# Trace: 2026-07-01_pfh-technology-group_senior-business-intelligence-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Senior Business Intelligence Analyst — PFH Technology Group

**URL:** https://www.linkedin.com/jobs/view/4434967351/
**Location:** Dublin, County Dublin, Ireland (Hybrid)
**Date Posted:** 2026-07-01

---

Senior Business Intelligence Analyst at PFH Technology Group

Location: Dublin, County Dublin, Ireland (Hybrid)
Contract Type: Day Rate Contract (1-year Contract)
Start Date: ASAP
Seniority Level: Mid-Senior level
Employment Type: Contract
Job Function: Information Technology
Industry: Government Administration

Overview
PFH Technology is partnering with a Dublin-based client seeking an experienced Senior BI Analyst to support delivery of a modern enterprise data platform using Microsoft Fabric, focusing on business intelligence, data analysis, migration, quality, governance, and reporting.

Key Responsibilities
- Develop BI reports, dashboards, KPIs, and analytical solutions using Microsoft Fabric and SQL
- Perform data migration, validation, reconciliation, and quality analysis
- Analyze enterprise data to identify trends, anomalies, and data quality issues
- Produce ad hoc reports and data extracts for business, audit, and compliance
- Create data mappings, transformation rules, Data Management Plans, and technical documentation
- Support data governance, data modelling, data lineage, and data integration initiatives
- Collaborate with business and technical teams to deliver scalable, high-quality data solutions

Must-Have Skills & Experience
- 8+ years in Business Intelligence, Data Analysis, or Data Migration
- Hands-on Microsoft Fabric experience
- Strong SQL skills (SQL Server or relational databases)
- Experience with Power BI, Data Quality, Data Validation, Data Governance, and Data Modelling
- Excellent analytical, problem-solving, and stakeholder engagement skills
- Bachelor's degree in Computer Science, IT, or related discipline (preferred)
- Microsoft Fabric, Azure Data, Power BI, or Data Analytics certifications (desirable)

Additional Notes
No visa sponsorship available for this role. Referrals increase interview chances by 2x.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 2 | 0 | 0 | 2 | 33% | ✗ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | mixed | hiring_manager | mixed | 33% | ✓ |
| stakeholder_orientation | mixed | mixed | internal_data | mixed | 33% | ✓ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | tool_listed | tool_listed | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Perform data migration, validation, reconciliation, and quality analysis"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, quality, validation, and governance throughout, with no velocity or iteration language present.

**Run 2:** `rigour` ✓
> Quote: "Support data governance, data modelling, data lineage, and data integration initiatives"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, validation, reconciliation, quality analysis, and documentation with no velocity language; rigour signals dominate throughout.

**Run 3:** `rigour` ✓
> Quote: "Perform data migration, validation, reconciliation, and quality analysis"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize validation, reconciliation, data quality analysis, governance, and modelling without any velocity signals like speed, iteration, or rapid delivery.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Audit and compliance are explicitly named as primary report audiences, combined with the Government Administration sector which carries inherent regulatory requirements.

**Run 2:** `high` ✓
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Government Administration sector combined with explicit audit and compliance stakeholders signals high-risk data that directly serves regulatory and financial control functions.

**Run 3:** `high` ✓
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Government administration sector combined with explicit audit and compliance reporting requirements indicates data errors directly impact regulatory and compliance outcomes.

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "Collaborate with business and technical teams"
> Verified: ✓ found in JD
> Reasoning: No distinct named functions or teams are identified; 'business and technical teams' are generic descriptors, not named team cohorts.

**Run 2:** `0` ✗
> Quote: "No named teams identified; 'business and technical teams' are too generic to count."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions generic 'business and technical teams' without naming specific functions like Finance, Product, or named data sub-teams.

**Run 3:** `2` ✓
> Quote: "audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Audit and compliance are explicitly named stakeholder/partner functions that the role produces reports for.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

⚠ **LLM inconsistency**: runs gave ['0', '0', '2']

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "focusing on business intelligence, data analysis, migration, quality, governance, and reporting"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data migration and governance support, combined with adoption of Microsoft Fabric, suggests an actively growing data function, not yet fully mature.

**Run 2:** `mid` ✗
> Quote: "Develop BI reports, dashboards, KPIs, and analytical solutions using Microsoft Fabric and SQL"
> Verified: ✓ found in JD
> Reasoning: Named tools (Microsoft Fabric, SQL, Power BI) appear as action verbs in responsibilities, indicating an existing platform being developed on rather than infrastructure built from zero.

**Run 3:** `mid` ✗
> Quote: "Support data governance, data modelling, data lineage, and data integration initiatives"
> Verified: ✓ found in JD
> Reasoning: Multiple established data practices (governance, lineage, integration) with named initiatives indicate mid-stage maturity with existing infrastructure.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Create data mappings, transformation rules, Data Management Plans, and technical documentation"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical artifacts (Data Management Plans, data lineage) and workflows, but lacks the deep contextual specificity and scale details typical of a hiring manager.

**Run 2:** `hiring_manager` ✗
> Quote: "Create data mappings, transformation rules, Data Management Plans, and technical documentation"
> Verified: ✓ found in JD
> Reasoning: The specificity of named methodology components (data mappings, transformation rules, Data Management Plans) indicates authorship by someone with hands-on experience in this work.

**Run 3:** `mixed` ✓
> Quote: "Create data mappings, transformation rules, Data Management Plans, and technical documentation"
> Verified: ✓ found in JD
> Reasoning: Mix of technically specific deliverables (data mappings, Data Management Plans) and generic boilerplate language (collaborate, stakeholder engagement) indicates mixed authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: The role genuinely serves both finance/audit/compliance audiences and internal data platform consumers through governance and infrastructure initiatives, without clear dominance of either.

**Run 2:** `internal_data` ✗
> Quote: "support delivery of a modern enterprise data platform using Microsoft Fabric, focusing on business intelligence, data analysis, migration, quality, governance, and reporting"
> Verified: ✓ found in JD
> Reasoning: The primary mission frames the role as building and supporting data platform infrastructure; governance, data lineage, and data modelling are internal data team responsibilities.

**Run 3:** `mixed` ✓
> Quote: "Develop BI reports, dashboards, KPIs, and analytical solutions; Support data governance, data modelling, data lineage, and data integration initiatives"
> Verified: ✓ found in JD
> Reasoning: The role combines reporting work serving finance/business stakeholders with infrastructure work serving the data function, with approximately equal emphasis on both.

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'mixed']

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Support data governance, data modelling, data lineage, and data integration initiatives"
> Verified: ✓ found in JD
> Reasoning: The use of 'support' and the framing of work around delivering defined BI solutions, migrations, and executing governance initiatives set by others indicates execution rather than strategic ownership.

**Run 2:** `execution` ✓
> Quote: "Support data governance, data modelling, data lineage, and data integration initiatives"
> Verified: ✓ found in JD
> Reasoning: The verb 'support' frames the role as executing initiatives and technical work defined by others, not setting strategic direction or defining priorities.

**Run 3:** `execution` ✓
> Quote: "Develop BI reports, dashboards, KPIs, and analytical solutions"
> Verified: ✓ found in JD
> Reasoning: Action verbs throughout (develop, perform, produce, support) are all execution-oriented without strategic framing of defining direction or shaping priorities.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, machine learning, generative AI applications, or AI-assisted coding practices.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, or AI-ready data infrastructure that the candidate must demonstrate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, AI-assisted coding, or GenAI capabilities throughout the job description.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `tool_listed` ✗
> Quote: "Data Quality, Data Validation"
> Verified: ✓ found in JD
> Reasoning: Data quality and validation appear in the required skills list without an ownership framing verb like 'own', 'define', or 'establish', indicating they are expected competencies rather than responsibilities the candidate will own.

**Run 2:** `tool_listed` ✗
> Quote: "Experience with Power BI, Data Quality, Data Validation, Data Governance, and Data Modelling"
> Verified: ✓ found in JD
> Reasoning: Data quality and validation appear as required skills in the requirements section without ownership verbs or accountability framing in the responsibilities.

**Run 3:** `responsibility` ✗
> Quote: "Perform data migration, validation, reconciliation, and quality analysis"
> Verified: ✓ found in JD
> Reasoning: The action verb 'perform' paired with explicit quality analysis responsibility indicates the candidate owns quality work throughout the engagement.

⚠ **Disagreement**: manual=`` vs LLM majority=`tool_listed`

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'tool_listed', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Compliance and audit are named concerns reflecting regulatory risk in the government sector, but the primary role framing emphasizes BI delivery and analytics development rather than risk prevention.

**Run 2:** `moderate` ✗
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Audit and compliance are named stakeholders and governance is a responsibility, indicating operational reliability concerns; however, the overall framing emphasizes platform delivery rather than preventing regulatory failure or trust breakdown.

**Run 3:** `moderate` ✗
> Quote: "Produce ad hoc reports and data extracts for business, audit, and compliance"
> Verified: ✓ found in JD
> Reasoning: Explicit audit and compliance reporting indicates moderate risk awareness focused on operational compliance and regulatory reporting rather than high-stakes framing.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
