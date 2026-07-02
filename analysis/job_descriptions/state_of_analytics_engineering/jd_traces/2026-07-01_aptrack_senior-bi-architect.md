# Trace: 2026-07-01_aptrack_senior-bi-architect

## JD text (fed to classifier, Layer B stripped)

```
# Senior BI Architect — Aptrack (client undisclosed)

**URL:** https://www.aptrack.co/uap/AAAGoQAPZp8B8uZs/
**Location:** Dublin 8, Ireland (Hybrid)
**Date Posted:** 2026-07-01

---

Senior Business Intelligence Architect (EBT8141) via Aptrack

Location: Dublin 8, Ireland
Employment Type: 12-month rolling contract
Work Model: Hybrid (3 days onsite per week)
Sector: IT

Role Summary
The organisation seeks an experienced professional to design and deliver a modern Microsoft Fabric-based analytics platform. This role encompasses comprehensive BI architecture covering data ingestion, modelling, storage, and reporting on Azure infrastructure.

Key Responsibilities
- Design and implement end-to-end BI architecture using Microsoft Fabric and Azure
- Define lakehouse, data warehouse, and semantic modelling structures
- Build and manage Azure Data Factory pipelines and ETL/ELT processes
- Develop Power BI datasets, dashboards, and reporting solutions
- Create reusable data models and curated data products
- Ensure data quality, governance, and security standards
- Translate business requirements into BI solutions and analytics outputs
- Define BI architecture standards, principles and best practices
- Ensure scalability, performance and enterprise alignment
- Collaborate with stakeholders on requirements and insights delivery

Required Experience
- 7+ years in BI, Data Architecture, or Analytics roles
- Strong Azure data platform and Microsoft Fabric experience
- Data warehousing, data lakes, and enterprise data modelling expertise
- Hands-on Power BI, Azure Data Factory, and SQL proficiency
- PySpark or Fabric notebooks experience
- Data governance and quality practices knowledge
- Stakeholder collaboration experience

Key Skills
Microsoft Fabric/Azure Synapse, Azure Data Factory, Azure Data Lake, Power BI, SQL, PySpark, data modelling, ETL/ELT, Azure DevOps, data governance and security.

Work Authorization
Candidates must possess appropriate Irish work rights or valid long-term work visa documentation.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 0 | 0 | 0 | 0 | 100% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | recruiter | hiring_manager | 0% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | mixed | strategic | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, quality, and standards across multiple bullet points with no velocity-oriented language like 'fast-paced' or 'rapid delivery'.

**Run 2:** `rigour` ✓
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize governance, standards, quality, and enterprise alignment without any delivery speed or iteration pace language.

**Run 3:** `rigour` ✓
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize architecture standards, governance, quality, and enterprise alignment with no delivery velocity language, placing this firmly in the rigour category.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Design and deliver a modern Microsoft Fabric-based analytics platform"
> Verified: ✓ found in JD
> Reasoning: The JD describes a general enterprise BI platform without explicit financial reporting, compliance, or regulatory language typical of high-risk domains.

**Run 2:** `moderate` ✓
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: The role builds data infrastructure and platforms without explicit financial reporting, regulatory compliance, or audit framing that would signal high-risk domain.

**Run 3:** `moderate` ✓
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: The role involves enterprise analytics infrastructure but lacks explicit financial reporting, regulatory, or compliance language that would elevate it to high risk.

### collaboration_width
**Manual:** `0`

**Run 1:** `0` ✓
> Quote: "Collaborate with stakeholders on requirements and insights delivery"
> Verified: ✓ found in JD
> Reasoning: The only collaboration reference uses generic 'stakeholders' language, which per the rules does not count as a named team or function.

**Run 2:** `0` ✓
> Quote: "Collaborate with stakeholders on requirements and insights delivery"
> Verified: ✓ found in JD
> Reasoning: No distinctly named teams, functions, or partner groups are explicitly identified; only generic 'stakeholders' are mentioned.

**Run 3:** `0` ✓
> Quote: "Collaborate with stakeholders on requirements and insights delivery"
> Verified: ✓ found in JD
> Reasoning: No named partner teams or functions are specified; 'stakeholders' is generic language excluded from counting per the rules.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Define lakehouse, data warehouse, and semantic modelling structures"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize defining and building technical structures for a modern platform, indicating an established organization in a platform modernization phase rather than greenfield or mature operating-at-scale.

**Run 2:** `mid` ✗
> Quote: "Define BI architecture standards, principles and best practices"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in responsibilities and the role involves modernizing/defining architecture, suggesting an established function being scaled and standardized rather than built from zero.

**Run 3:** `mid` ✗
> Quote: "Design and implement end-to-end BI architecture using Microsoft Fabric and Azure"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in responsibilities with emphasis on designing and implementing (not maintaining) a platform, indicating an emerging/growing analytics function beyond early stage.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Design and implement end-to-end BI architecture using Microsoft Fabric and Azure; Build and manage Azure Data Factory pipelines; Collaborate with stakeholders on requirements and insights delivery"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about named tools and architectural approaches (Microsoft Fabric, Azure Data Factory, lakehouse structures) is mixed with generic boilerplate verbs ('Collaborate', 'Translate business requirements').

**Run 2:** `recruiter` ✗
> Quote: "Translate business requirements into BI solutions and analytics outputs"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic boilerplate action verbs without specific business context, scale, named technical challenges, or details about what a Tuesday morning actually looks like.

**Run 3:** `hiring_manager` ✓
> Quote: "Design and implement end-to-end BI architecture using Microsoft Fabric and Azure; Build and manage Azure Data Factory pipelines and ETL/ELT processes; Develop Power BI datasets, dashboards, and reporting solutions"
> Verified: ✓ found in JD
> Reasoning: Technical specificity throughout—named tools with precise architectural context (Microsoft Fabric platform design, ADF pipelines, Power BI reporting, semantic modelling)—indicates a hiring manager wrote this, with only minor generic additions.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Define BI architecture standards, principles and best practices; design and deliver a modern Microsoft Fabric-based analytics platform"
> Verified: ✓ found in JD
> Reasoning: The role is framed as architecting and governing the analytics platform infrastructure itself, primarily serving the data function and analytics consumers rather than a specific business department.

**Run 2:** `internal_data` ✓
> Quote: "Create reusable data models and curated data products"
> Verified: ✓ found in JD
> Reasoning: The role is primarily accountable for building platform infrastructure and data products for internal data consumers, not for a specific business function.

**Run 3:** `internal_data` ✓
> Quote: "Create reusable data models and curated data products"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building analytics infrastructure, defining data models, and creating products for internal data consumers rather than serving commercial, product, or finance teams.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Define BI architecture standards, principles and best practices; Define lakehouse, data warehouse, and semantic modelling structures"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize defining and designing the architecture, standards, and technical structures, indicating the role sets direction for the BI platform rather than executing existing direction.

**Run 2:** `mixed` ✗
> Quote: "Define BI architecture standards, principles and best practices"
> Verified: ✓ found in JD
> Reasoning: The role genuinely combines strategic definition ('define standards', 'design architecture') with execution ('develop dashboards', 'build pipelines').

**Run 3:** `strategic` ✓
> Quote: "Define BI architecture standards, principles and best practices"
> Verified: ✓ found in JD
> Reasoning: Multiple ownership verbs—define, design, establish—indicate the role sets direction for the analytics platform and architecture rather than executing predefined work.

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'strategic']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI infrastructure requirements, or AI product enablement.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI skills, coding tools, agentic workflows, or data-for-AI infrastructure expected of the candidate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, or AI data infrastructure requirements for the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: Data quality and governance are framed as a key responsibility to 'ensure' rather than listed as tools or skills to learn, indicating the candidate owns these practices.

**Run 2:** `responsibility` ✗
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as a primary responsibility the candidate is accountable for ensuring, indicating ownership of quality and governance practices.

**Run 3:** `responsibility` ✗
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: The action verb 'ensure' in Key Responsibilities indicates the candidate owns data quality outcomes, framing it as an accountability rather than a listed tool.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability through data quality and governance rather than regulatory compliance or stakeholder trust breaches, reflecting moderate loss aversion.

**Run 2:** `moderate` ✗
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and data quality are concerns, but without high-risk regulatory, compliance, or stakeholder-trust-failure framing.

**Run 3:** `moderate` ✗
> Quote: "Ensure data quality, governance, and security standards"
> Verified: ✓ found in JD
> Reasoning: Governance and standards language signal operational risk awareness, but the absence of compliance, regulatory, or 'prevent bad data' language prevents a high classification.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
