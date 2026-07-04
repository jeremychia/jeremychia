# Trace: 2026-05-01_wolt_senior-revenue-data-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Senior Revenue Data Analyst — Wolt

**URL:** https://job-boards.greenhouse.io/wolt/jobs/7735284
**Location:** Berlin, Germany; Budapest, Hungary

---

## Key Responsibilities

- Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level
- Conduct accounting analysis, measurement, and reconciliations of major revenue accounts
- Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close
- Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements
- Apply problem-solving to complex, ambiguous challenges
- Leverage AI tools like Claude Code and Cursor to accelerate analysis and automate reconciliation tasks
- Identify and resolve data issues and reconciliation gaps
- Contribute to process improvement and automation across revenue operations
- Prepare materials for external and internal audit reviews

---

## Required Qualifications

- Degree in Accounting, Business, Data Science, or related field
- 5-7 years of experience in revenue accounting/finance, data analytics, and/or related field
- Cross-functional collaboration skills with Engineering, Product, and Finance teams
- Strong knowledge of IFRS 15/accounting principles required
- Intermediate to advanced SQL proficiency with large transactional datasets
- Proven active usage of AI tools in daily work with specific examples
- EU work eligibility

---

## Preferred / Bonus Skills

- US GAAP and SOX knowledge
- Experience with NetSuite, Snowflake, Looker, and dbt
- Background in gig economy or marketplace companies
- English fluency as working language

---

## Benefits

Not specified in posting

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 5 | 4 | 5 | 4 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | hiring_manager | mixed | hiring_manager | 33% | ✗ |
| stakeholder_orientation | finance | finance | finance | finance | 100% | ✓ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |
| ai_role |  | ai_user | ai_user | ai_user | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | high | high | moderate | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize accounting accuracy, reconciliations, audit compliance, and IFRS 15 principles throughout, with acceleration language only in service of automating reconciliation tasks.

**Run 2:** `rigour` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The role centers on accounting reconciliation and audit-ready materials rather than rapid iteration or shipping.

**Run 3:** `rigour` ✓
> Quote: "Conduct accounting analysis, measurement, and reconciliations of major revenue accounts"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize accounting accuracy, reconciliations, and compliance rather than velocity, with rigour signals (reconciliation, measurement, audit) substantially outweighing velocity signals.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: Data errors directly affect financial reporting, regulatory compliance (IFRS 15, SOX), and audit outcomes in a fintech/marketplace context.

**Run 2:** `high` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: Revenue accounting directly affects financial reporting accuracy and is subject to external audit, making data errors have immediate compliance consequences.

**Run 3:** `high` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: External audit requirements and explicit financial reporting context (revenue accounting, IFRS 15, SOX) signal high regulatory and financial reporting risk where data errors have direct compliance consequences.

### collaboration_width
**Manual:** `5`

**Run 1:** `4` ✗
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements"
> Verified: ✓ found in JD
> Reasoning: Four distinct named teams are explicitly listed as collaboration partners: Product, Analytics, Engineering, and Accounting.

**Run 2:** `5` ✓
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams; Cross-functional collaboration skills with Engineering, Product, and Finance teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names five distinct partner functions: Product, Analytics, Engineering, Accounting, and Finance.

**Run 3:** `4` ✗
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements"
> Verified: ✓ found in JD
> Reasoning: Four distinct named partner teams are explicitly identified as collaboration stakeholders in responsibilities.

⚠ **Disagreement**: manual=`5` vs LLM majority=`4`

⚠ **LLM inconsistency**: runs gave ['4', '5', '4']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The revenue subledger already exists and is being scaled, indicating an established data function growing rather than building from scratch or operating at mature scale.

**Run 2:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The role involves scaling an existing revenue infrastructure with named tools (NetSuite, dbt, Snowflake) rather than building from zero, indicating a mid-stage data function.

**Run 3:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The language 'continued implementation' and 'scale' indicates an existing data function being expanded rather than built from scratch.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: Specific accounting methodologies (flux analysis, balance sheet reconciliations), regulatory frameworks (IFRS 15), and named tools (Claude Code, Cursor) demonstrate technical depth only someone doing this work would include.

**Run 2:** `mixed` ✓
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close; Leverage AI tools like Claude Code and Cursor to accelerate analysis and automate reconciliation tasks"
> Verified: ✓ found in JD
> Reasoning: The role includes specific accounting procedures and tools with clear application context alongside generic collaboration language.

**Run 3:** `hiring_manager` ✗
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: Specific accounting methodologies (flux analysis, balance sheet reconciliations, month-end close cycle) indicate domain expertise from someone doing this work daily.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** `finance`

**Run 1:** `finance` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The role's primary impact is on accounting accuracy, audit readiness, and financial reporting, with finance, controllership, and audit as the core audiences.

**Run 2:** `finance` ✓
> Quote: "Conduct accounting analysis, measurement, and reconciliations of major revenue accounts; Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The role's core responsibilities center on financial accounting accuracy and audit compliance, making Finance/FP&A the primary stakeholder.

**Run 3:** `finance` ✓
> Quote: "Conduct accounting analysis, measurement, and reconciliations of major revenue accounts"
> Verified: ✓ found in JD
> Reasoning: The role's responsibilities center on revenue accounting and reconciliations supporting financial reporting and audit compliance, making finance the primary stakeholder.

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Support the continued implementation of our revenue subledger"
> Verified: ✓ found in JD
> Reasoning: All responsibilities use execution verbs (support, conduct, prepare, contribute) with no strategic ownership of direction-setting or priority definition.

**Run 2:** `execution` ✓
> Quote: "Support the continued implementation of our revenue subledger"
> Verified: ✓ found in JD
> Reasoning: The core verb is 'support' and the role receives scoped deliverables (reconciliations, journal entries, audit materials) rather than defining how analytics is delivered.

**Run 3:** `execution` ✓
> Quote: "Support the continued implementation of our revenue subledger"
> Verified: ✓ found in JD
> Reasoning: The verb 'support' and framing around 'continued implementation' indicate execution of a pre-defined scope set by existing processes rather than strategic direction-setting.

### ai_role
**Manual:** ``

**Run 1:** `ai_user` ✗
> Quote: "Leverage AI tools like Claude Code and Cursor to accelerate analysis and automate reconciliation tasks"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to actively use AI coding tools to accelerate their own analytical and reconciliation work.

**Run 2:** `ai_user` ✗
> Quote: "Leverage AI tools like Claude Code and Cursor to accelerate analysis and automate reconciliation tasks"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI coding tools to accelerate their own analysis and automation work, not to build data infrastructure for AI systems.

**Run 3:** `ai_user` ✗
> Quote: "Leverage AI tools like Claude Code and Cursor to accelerate analysis and automate reconciliation tasks"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI coding tools to accelerate their own analysis and automate reconciliation tasks as personal productivity tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Identify and resolve data issues and reconciliation gaps"
> Verified: ✓ found in JD
> Reasoning: While the role involves data reconciliation and issue resolution, there is no explicit mention of data quality frameworks, testing practices, data contracts, or observability tooling.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no reference to testing, data quality frameworks, or observability practices.

**Run 3:** `absent` ✗
> Quote: "Identify and resolve data issues and reconciliation gaps"
> Verified: ✓ found in JD
> Reasoning: While reconciliation and issue resolution are implicit quality activities, the JD does not frame testing, data contracts, or data quality frameworks as explicit responsibilities or mention any testing tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `high` ✗
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The JD frames the role around regulatory compliance (IFRS 15, SOX, audit readiness), reflecting high fear of compliance failure and regulatory exposure.

**Run 2:** `high` ✗
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The role includes audit material preparation and mandatory IFRS 15 knowledge, indicating the fear is regulatory and compliance consequences from inaccurate financial data.

**Run 3:** `moderate` ✗
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: Audit compliance and regulatory requirements (IFRS 15, SOX) are explicitly present but framed as baseline operational requirements within the close process rather than as a primary risk-mitigation or stakeholder-trust mandate.

⚠ **Disagreement**: manual=`` vs LLM majority=`high`

⚠ **LLM inconsistency**: runs gave ['high', 'high', 'moderate']
