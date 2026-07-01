# Trace: 2026-06-25_egnyte_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Egnyte
**URL:** https://jobs.jobvite.com/egnyte/job/oNOlzfwf

**Location:** Poznań, Poland (Remote option available)
**Date:** 2026-06-25

---

Analytics Engineer
Company: Egnyte
Location: Poznań, Poland (Remote option available)
Department: Data Analytics

About the Company:
Egnyte is "the secure multi-cloud platform for content security and governance" established in 2008, serving over 22,000 organizations. The company emphasizes organizational values including invested relationships, fiscal prudence, and candid conversations.

Key Responsibilities:
- Design and build data transformation pipelines
- Develop dbt semantic layer architecture
- Collaborate across departments on data strategy
- Manage CI/CD processes
- Create test cases for data accuracy
- Document data models
- Address data quality issues

Required Qualifications:
- Deep dbt expertise
- Extensive SQL proficiency
- BigQuery experience
- 3+ years in data-related roles
- Test automation tools experience
- Git proficiency
- Agile team collaboration
- Familiarity with Terraform and visualization platforms like Tableau or Power BI

Benefits:
- Competitive salary
- 50TB lifetime Egnyte cloud storage access
- Monthly wellness choices (MultiSport cards or gift cards)
- Private healthcare
- In-house English instruction

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
| jd_authorship | mixed | mixed | recruiter | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Create test cases for data accuracy"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, CI/CD management, documentation, and data quality—core rigour signals with no velocity language present.

**Run 2:** `rigour`
> Quote: "Create test cases for data accuracy"
> Verified: ✓ found in JD
> Reasoning: The explicit emphasis on testing, CI/CD management, and data quality signals a rigour-focused orientation with no competing velocity language.

**Run 3:** `rigour`
> Quote: "Create test cases for data accuracy"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, CI/CD processes, data documentation, and quality, with no signals of speed or iteration velocity.

### domain_risk

**Run 1:** `moderate`
> Quote: "Address data quality issues"
> Verified: ✓ found in JD
> Reasoning: As a SaaS analytics role without explicit financial or regulatory context, data errors affect business decisions and operations rather than compliance or P&L.

**Run 2:** `moderate`
> Quote: "Address data quality issues"
> Verified: ✓ found in JD
> Reasoning: While Egnyte operates in a regulated security sector, the JD focuses on internal analytics infrastructure without explicit financial reporting, compliance, or regulatory language.

**Run 3:** `moderate`
> Quote: "Address data quality issues"
> Verified: ✓ found in JD
> Reasoning: The JD indicates data accuracy matters for business operations but does not reference financial reporting, compliance, or regulatory stakes that would elevate it to high-risk.

### collaboration_width

**Run 1:** `0`
> Quote: "Collaborate across departments on data strategy"
> Verified: ✓ found in JD
> Reasoning: The JD mentions cross-functional collaboration generically but does not name specific teams, functions, or partner groups.

**Run 2:** `0`
> Quote: "Collaborate across departments on data strategy"
> Verified: ✓ found in JD
> Reasoning: Departments are mentioned generically without naming specific functions, teams, or partner groups.

**Run 3:** `0`
> Quote: "Collaborate across departments on data strategy"
> Verified: ✓ found in JD
> Reasoning: The JD mentions cross-departmental collaboration but does not name any specific functions, teams, or roles.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Develop dbt semantic layer architecture"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt) and CI/CD management indicate an established data function that is growing and evolving its analytics capabilities.

**Run 2:** `mid`
> Quote: "Develop dbt semantic layer architecture"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, BigQuery, CI/CD) indicate an established data function with existing infrastructure being developed and extended.

**Run 3:** `mid`
> Quote: "Develop dbt semantic layer architecture"
> Verified: ✓ found in JD
> Reasoning: The JD assumes existing tools and infrastructure (dbt, BigQuery, CI/CD) are already in place, with the role focused on developing and improving them rather than building from zero or managing a large established structure.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Develop dbt semantic layer architecture; Collaborate across departments on data strategy"
> Verified: ⚠ NOT found verbatim
> Reasoning: Some responsibilities are technically specific (dbt semantic layer, BigQuery, Terraform), while others use generic boilerplate (collaborate, document, address issues).

**Run 2:** `mixed`
> Quote: "Develop dbt semantic layer architecture; Collaborate across departments on data strategy"
> Verified: ⚠ NOT found verbatim
> Reasoning: The semantic layer architecture responsibility shows technical specificity, while most other responsibilities use generic boilerplate verbs indicating dual authorship.

**Run 3:** `recruiter`
> Quote: "Collaborate across departments on data strategy"
> Verified: ✓ found in JD
> Reasoning: The responsibilities rely on generic boilerplate verbs (collaborate, manage, create, document, address) without specific technical context, scale, or methodology details that would indicate hiring manager authorship.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Develop dbt semantic layer architecture"
> Verified: ✓ found in JD
> Reasoning: The bulk of responsibilities focus on building data infrastructure and semantic layers for consumption by other data consumers rather than external business or GTM stakeholders.

**Run 2:** `internal_data`
> Quote: "Develop dbt semantic layer architecture"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining data infrastructure and the semantic layer that serves internal analytics consumers.

**Run 3:** `internal_data`
> Quote: "Develop dbt semantic layer architecture"
> Verified: ✓ found in JD
> Reasoning: The emphasis on dbt semantic layer development and data model documentation indicates the primary audience is internal data consumers enabling self-serve analytics rather than commercial, product, or finance stakeholders.

### autonomy_level

**Run 1:** `execution`
> Quote: "Create test cases for data accuracy"
> Verified: ✓ found in JD
> Reasoning: The responsibilities are focused on delivering specific technical outputs and managing defined processes within scope rather than setting overall direction or strategy.

**Run 2:** `execution`
> Quote: "Manage CI/CD processes"
> Verified: ✓ found in JD
> Reasoning: Most responsibilities are execution-oriented (managing processes, creating tests, documenting) with design responsibilities narrowly scoped to technical components rather than broader strategy.

**Run 3:** `execution`
> Quote: "Collaborate across departments on data strategy"
> Verified: ✓ found in JD
> Reasoning: The phrasing 'collaborate on' rather than 'define' or 'own' strategy, combined with execution-focused tasks (manage, create, document, address), indicates the role executes work scoped by others rather than setting direction.

### ai_role
**Run 1:** `ai_enabler` ✓
> Quote: "Develop dbt semantic layer architecture"
> Reasoning: Semantic layer infrastructure enables AI consumption (text-to-SQL, GenAI patterns).

**Run 2:** `ai_enabler` ✓
> Quote: "Develop dbt semantic layer architecture"
> Reasoning: Semantic layer architecture provides AI-ready infrastructure for GenAI and analytics consumption.

**Run 3:** `ai_enabler` ✓
> Quote: "Develop dbt semantic layer architecture"
> Reasoning: Semantic layer is infrastructure AI consumes for natural language to SQL translation.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Create test cases for data accuracy"
> Reasoning: Candidate owns quality practice through explicit test case creation.

**Run 2:** `responsibility` ✓
> Quote: "Create test cases for data accuracy"
> Reasoning: Candidate owns test creation, demonstrating responsibility for quality and data accuracy practices.

**Run 3:** `responsibility` ✓
> Quote: "Create test cases for data accuracy"
> Reasoning: Candidate owns test case creation as quality practice responsibility.


### loss_aversion_framing
**Run 1:** `high` ✓
> Quote: "secure multi-cloud platform for content security and governance"
> Reasoning: Governance and security dominance signals compliance/trust-driven framing over operational reliability.

**Run 2:** `high` ✓
> Quote: "secure multi-cloud platform for content security and governance"
> Reasoning: Governance and compliance framing indicates high loss aversion centered on trustworthiness and regulatory concerns.

**Run 3:** `high` ✓
> Quote: "secure multi-cloud platform for content security and governance"
> Reasoning: Compliance and governance responsibilities indicate loss aversion centered on trust and regulatory concerns.

