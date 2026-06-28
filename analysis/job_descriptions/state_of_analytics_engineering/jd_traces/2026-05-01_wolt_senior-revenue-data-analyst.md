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
| collaboration_width | 5 | 5 | 4 | 4 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | mixed | mixed | hiring_manager | 33% | ✓ |
| stakeholder_orientation |  | finance | finance | finance | 100% | ✗ |
| autonomy_level |  | execution | execution | execution | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The emphasis on audit compliance, reconciliation accuracy, and regulatory requirements (IFRS 15) throughout the JD signals rigour as the primary orientation.

**Run 2:** `rigour` ✓
> Quote: "Conduct accounting analysis, measurement, and reconciliations of major revenue accounts"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour-focused signals (accounting analysis, reconciliations, audit reviews, IFRS compliance) dominate the responsibilities with only secondary velocity mentions in service of accuracy.

**Run 3:** `rigour` ✓
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize accounting accuracy, reconciliation, and compliance throughout, with multiple rigour signals (reconciliations, audit, IFRS 15) that far outweigh efficiency-focused mentions.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Conduct accounting analysis, measurement, and reconciliations of major revenue accounts"
> Verified: ✓ found in JD
> Reasoning: Revenue accounting affects financial reporting and is subject to regulatory compliance (IFRS 15, SOX, audit), placing this role in a high-risk domain.

**Run 2:** `high` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: Explicit mention of audit requirements and mandatory IFRS 15 compliance indicates regulatory and financial reporting stakes where errors directly affect compliance.

**Run 3:** `high` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: External and internal audit requirements indicate that data errors in revenue accounting directly affect financial reporting validation and regulatory compliance.

### collaboration_width
**Manual:** `5`

**Run 1:** `5` ✓
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements; Cross-functional collaboration skills with Engineering, Product, and Finance teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names five distinct partner functions: Product, Analytics, Engineering, Accounting, and Finance.

**Run 2:** `4` ✗
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements"
> Verified: ✓ found in JD
> Reasoning: Four distinct named teams explicitly listed as collaboration partners in the responsibilities section.

**Run 3:** `4` ✗
> Quote: "Product; Analytics; Engineering; Accounting teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role explicitly names four distinct teams in the responsibilities section.

⚠ **Disagreement**: manual=`5` vs LLM majority=`4`

⚠ **LLM inconsistency**: runs gave ['5', '4', '4']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The language of 'continued implementation' and 'scale to the next level' indicates an existing revenue function undergoing expansion rather than greenfield build or fully mature operation.

**Run 2:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The phrase 'continued implementation' and 'scale to the next level' indicates an existing function being grown rather than early-stage greenfield or an established mature organization.

**Run 3:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The phrase 'continued implementation' and 'scale to the next level' indicate an existing but growing data infrastructure, not a greenfield setup or fully mature operation.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close; Apply problem-solving to complex, ambiguous challenges"
> Verified: ⚠ NOT found verbatim
> Reasoning: Technical accounting terminology and process specificity suggest hiring manager input, while generic verbs like 'Apply problem-solving' indicate some recruiter influence.

**Run 2:** `mixed` ✓
> Quote: "Conduct accounting analysis, measurement, and reconciliations of major revenue accounts; Apply problem-solving to complex, ambiguous challenges"
> Verified: ⚠ NOT found verbatim
> Reasoning: Technical specificity about accounting methodologies and month-end close procedures indicates hiring manager expertise, mixed with generic collaboration and problem-solving language suggesting recruiter additions.

**Run 3:** `hiring_manager` ✗
> Quote: "balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: These specific accounting terms and processes can only come from someone with hands-on revenue accounting experience.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `finance` ✗
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The primary mission is revenue accounting, reconciliation, and audit compliance, making the finance and accounting function the primary stakeholder.

**Run 2:** `finance` ✗
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: Primary responsibility is revenue accounting compliance and audit, serving finance and controllership functions rather than product, commercial, or internal data consumers.

**Run 3:** `finance` ✗
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The primary purpose of this role is to support financial compliance and audit requirements, making the finance function the primary stakeholder.

⚠ **Disagreement**: manual=`` vs LLM majority=`finance`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The 'support' verb and pre-defined initiative language indicate this role executes within a scoped direction rather than setting strategic direction.

**Run 2:** `execution` ✗
> Quote: "Support the continued implementation of our revenue subledger; Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role is framed around executing defined accounting processes and month-end close procedures under existing accounting standards rather than setting accounting strategy or direction.

**Run 3:** `execution` ✗
> Quote: "Support the continued implementation of our revenue subledger"
> Verified: ✓ found in JD
> Reasoning: The verb 'support' and work within an existing accounting framework (IFRS 15, established subledger) indicate the role executes direction set by others rather than defining strategic direction.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`
