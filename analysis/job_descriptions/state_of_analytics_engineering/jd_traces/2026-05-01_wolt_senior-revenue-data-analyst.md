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
| jd_authorship | mixed | hiring_manager | hiring_manager | hiring_manager | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The responsibility to prepare audit materials explicitly signals governance and compliance as core expectations, fundamental characteristics of rigour-oriented work.

**Run 2:** `rigour` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reconciliation, accounting accuracy, audit compliance, and IFRS 15 compliance throughout, with no velocity language; audit preparation is an explicit governance signal.

**Run 3:** `rigour` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: External audit preparation signals governance and compliance as core value, with multiple reconciliation and accuracy demands framing the role's primary orientation toward correctness rather than delivery speed.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Strong knowledge of IFRS 15/accounting principles required"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement for regulatory accounting framework knowledge (IFRS 15) indicates that data errors directly impact financial reporting accuracy and compliance outcomes.

**Run 2:** `high` ✓
> Quote: "Prepare materials for external and internal audit reviews"
> Verified: ✓ found in JD
> Reasoning: Revenue accounting errors directly affect financial reporting and regulatory compliance; audit preparation and IFRS 15 requirements indicate explicit financial/compliance risk.

**Run 3:** `high` ✓
> Quote: "Strong knowledge of IFRS 15/accounting principles required"
> Verified: ✓ found in JD
> Reasoning: IFRS 15 is a specific regulatory standard governing revenue recognition, indicating this role directly impacts financial reporting accuracy and regulatory compliance.

### collaboration_width
**Manual:** `5`

**Run 1:** `5` ✓
> Quote: "Product; Analytics; Engineering; Accounting; Finance"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names five distinct partner functions: Product, Analytics, and Engineering appear in responsibilities; Accounting in responsibilities and Finance in qualifications.

**Run 2:** `4` ✗
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names four distinct teams in collaboration context (Product, Analytics, Engineering, Accounting).

**Run 3:** `4` ✗
> Quote: "Collaborate with Product, Analytics, Engineering, and Accounting teams on revenue data requirements"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly listed as collaboration partners: Product, Analytics, Engineering, and Accounting.

⚠ **Disagreement**: manual=`5` vs LLM majority=`4`

⚠ **LLM inconsistency**: runs gave ['5', '4', '4']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: The phrasing 'continued implementation' and 'scale to the next level' indicates an established data function actively growing and improving, characteristic of mid-stage maturity.

**Run 2:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: Language indicates scaling existing infrastructure rather than building from scratch; preferred tools (Snowflake, Looker, dbt) are already deployed.

**Run 3:** `mid` ✓
> Quote: "Support the continued implementation of our revenue subledger to scale our revenue accounting to the next level"
> Verified: ✓ found in JD
> Reasoning: "Continued implementation" and "scale to the next level" indicate an established system being actively grown and improved rather than built from scratch, characteristic of mid-stage teams.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: The specific accounting terminology (flux analysis, balance sheet reconciliations, month-end close) demonstrates technical knowledge that only someone actively performing revenue accounting work would use.

**Run 2:** `hiring_manager` ✗
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: Specific accounting procedures, timing context (month-end close), and methodology names (flux analysis) reflect technical knowledge only someone performing this work would articulate with this precision.

**Run 3:** `hiring_manager` ✗
> Quote: "Prepare journal entries, balance sheet reconciliations, and flux analysis during month-end close"
> Verified: ✓ found in JD
> Reasoning: Specific accounting methodologies (flux analysis, balance sheet reconciliations) and month-end close procedures indicate someone with hands-on domain expertise wrote this, not boilerplate recruiter language.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`
