# Trace: 2026-06-27_n26_senior-risk-data-and-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# (Senior) Risk Data & Analytics Engineer — N26

**Location:** Berlin
**Date Posted:** 2026-06-27

---

# (Senior) Risk Data & Analytics Engineer at N26

**Department:** Risk
**Location:** Berlin

## About the Opportunity

N26 seeks a technically skilled Risk Controlling professional to bridge methodology and implementation. The ICAAP Methodology & Analytics team role focuses on translating regulatory requirements into "robust, scalable, and audit-proof technical solutions." You'll implement risk methodologies in Python, enhance internal tooling, and drive automation across processes while collaborating with methodology teams and data engineers.

## Key Responsibilities

- Implement risk models (ICAAP, capital ratios) into production Python solutions
- Enhance and maintain internal risk controlling tools
- Translate regulatory requirements into automated, documented processes
- Support regulatory changes and new products
- Establish reliable data pipelines with quality assurance
- Develop automated risk reporting infrastructure
- Ensure model traceability and audit readiness
- Improve development standards within Risk Controlling (testing, versioning, documentation)
- Interface between risk, data, and technology teams

## Requirements

**Background:** Degree in Computer Science, Data Engineering, Mathematics, or equivalent; experience building data-driven Python applications; familiarity with data quality and robustness standards.

**Skills:** Strong Python proficiency; solid SQL and complex dataset experience; data pipeline design expertise; automation focus; software engineering best practices (version control, testing, CI/CD); problem-solving with attention to detail. Financial risk exposure is beneficial but not required.

**Preferred:**
- Interest in financial risk management and regulatory topics
- Prior banking, fintech, or regulatory exposure
- Understanding of risk metrics, reporting, or controls

## Benefits

Competitive personal development budget, work-from-home allowance, fitness memberships, language apps, public transit discounts, Premium N26 account access, additional annual leave per service year, and relocation support.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | high | high | 100% |
| collaboration_width | 3 | 3 | 3 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | mixed | 33% |
| stakeholder_orientation | finance | finance | finance | 100% |
| autonomy_level | execution | execution | strategic | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "robust, scalable, and audit-proof technical solutions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes correctness, quality, audit, and compliance throughout (audit-proof solutions, reliable pipelines, audit readiness, testing standards), with no velocity signals present.

**Run 2:** `rigour`
> Quote: "robust, scalable, and audit-proof technical solutions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes audit-proof solutions, reliable data pipelines, quality assurance, testing, and documentation, establishing a rigour orientation aligned with regulated finance.

**Run 3:** `rigour`
> Quote: "robust, scalable, and audit-proof technical solutions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes audit-proof infrastructure, data quality assurance, testing, CI/CD, and documentation with no language around speed, iteration, or rapid delivery.

### domain_risk

**Run 1:** `high`
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Verified: ✓ found in JD
> Reasoning: The role implements regulatory financial models (ICAAP, capital ratios) that directly affect regulatory compliance and financial reporting, placing this in the high-risk financial domain.

**Run 2:** `high`
> Quote: "Translate regulatory requirements into automated, documented processes"
> Verified: ✓ found in JD
> Reasoning: The role explicitly involves translating regulatory requirements and ensuring audit readiness in a regulated financial institution, making data errors directly consequential for compliance and financial reporting.

**Run 3:** `high`
> Quote: "Ensure model traceability and audit readiness"
> Verified: ✓ found in JD
> Reasoning: Banking/fintech sector with explicit regulatory compliance requirements (ICAAP, capital ratios, audit readiness) means data errors directly impact regulatory reporting and compliance.

### collaboration_width

**Run 1:** `3`
> Quote: "methodology teams; data engineers; technology teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct partner teams: methodology teams (mentioned in collaboration context), data engineers, and technology teams.

**Run 2:** `3`
> Quote: "collaborating with methodology teams and data engineers; Interface between risk, data, and technology teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named teams/functions are identified: methodology teams, data engineers, and technology teams.

**Run 3:** `3`
> Quote: "methodology teams; data engineers; technology teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names three distinct teams for collaboration: methodology teams and data engineers in one passage, and technology teams in the interface statement.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Enhance and maintain internal risk controlling tools"
> Verified: ✓ found in JD
> Reasoning: The presence of existing tools being actively enhanced and improved, combined with focus on upgrading development standards, indicates a function in growth mode rather than early-stage.

**Run 2:** `mid`
> Quote: "Enhance and maintain internal risk controlling tools"
> Verified: ✓ found in JD
> Reasoning: The emphasis on enhancing and maintaining existing tools indicates an established function with room for growth, rather than early-stage building or mature scale.

**Run 3:** `mid`
> Quote: "Enhance and maintain internal risk controlling tools"
> Verified: ✓ found in JD
> Reasoning: Existing tools and infrastructure are in place and require enhancement, indicating the data function has produced deliverables but is still maturing rather than building from zero.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions; Enhance and maintain internal risk controlling tools"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains specific domain knowledge (ICAAP, capital ratios, risk model traceability) suggesting hiring manager input, mixed with generic collaboration and process language typical of recruiter writing.

**Run 2:** `hiring_manager`
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Verified: ✓ found in JD
> Reasoning: The specific mention of ICAAP methodology and capital ratios, combined with references to model traceability and audit readiness, reflects domain-specific technical knowledge unlikely to come from a non-technical recruiter.

**Run 3:** `mixed`
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about regulatory methodology (ICAAP, capital ratios) and audit readiness mixed with generic collaboration verbs suggests both technical and recruiting input.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `finance`
> Quote: "Ensure model traceability and audit readiness"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is regulatory compliance, financial models (capital ratios, ICAAP), and audit readiness, directly serving finance/regulatory stakeholders.

**Run 2:** `finance`
> Quote: "Translate regulatory requirements into automated, documented processes"
> Verified: ✓ found in JD
> Reasoning: The primary mission is implementing regulatory and compliance requirements within a Risk Controlling department, ultimately serving financial reporting and regulatory audit needs.

**Run 3:** `finance`
> Quote: "Translate regulatory requirements into automated, documented processes"
> Verified: ✓ found in JD
> Reasoning: Regulatory compliance, capital ratios, and audit readiness throughout indicate the primary audience is the finance/compliance function, not product, commercial, or general data infrastructure.

### autonomy_level

**Run 1:** `execution`
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use execution-focused verbs (implement, enhance, maintain, develop, support) with direction set by regulatory requirements and existing methodology, rather than role autonomy in strategy-setting.

**Run 2:** `execution`
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Verified: ✓ found in JD
> Reasoning: The role implements and translates requirements set by others rather than defining strategic direction, indicating primarily execution-oriented work.

**Run 3:** `strategic`
> Quote: "Establish reliable data pipelines with quality assurance"
> Verified: ✓ found in JD
> Reasoning: The use of "establish," "develop," and "improve" signals direction-setting and architectural ownership rather than execution of someone else's priorities.

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'strategic']

### ai_role
**Run 1:** `none` ✓
> Quote: "Ensure model traceability and audit readiness"
> Reasoning: No AI tool usage or GenAI infrastructure mentioned; standard risk engineering work

**Run 2:** `none` ✓
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Reasoning: No AI capability signals; financial models are domain-specific regulatory tooling, not AI infrastructure or tool usage.

**Run 3:** `none` ✓
> Quote: "Implement risk models (ICAAP, capital ratios) into production Python solutions"
> Reasoning: Standard Python engineering work with no AI tooling or AI infrastructure responsibilities mentioned.


### testing_framing
**Run 1:** `absent` ✓
> Quote: "Enhance and maintain internal risk controlling tools"
> Reasoning: No explicit testing ownership or quality responsibility verbs; no testing tools listed

**Run 2:** `responsibility` ✗
> Quote: "Ensure model traceability and audit readiness"
> Reasoning: Ownership verb 'Ensure' applied to audit readiness, indicating responsibility for solution correctness and governance.

**Run 3:** `absent` ✓
> Quote: "Enhance and maintain internal risk controlling tools"
> Reasoning: Functionality and compliance focus; no testing tools, quality practice ownership, or data contract language present.

⚠ **LLM inconsistency**: runs gave ['absent', 'responsibility', 'absent']

### loss_aversion_framing
**Run 1:** `high` ✓
> Quote: "Convert regulatory requirements into audit-proof, automated processes"
> Reasoning: Regulatory compliance and audit-readiness dominate framing as primary concern

**Run 2:** `high` ✓
> Quote: "Convert regulatory requirements into audit-proof, automated processes"
> Reasoning: Regulatory compliance and audit-readiness dominate framing; trust and regulatory adherence are primary concerns, not operational SLOs.

**Run 3:** `high` ✓
> Quote: "Convert regulatory requirements into audit-proof, automated processes"
> Reasoning: Regulatory compliance and audit readiness dominate; financial risk models (ICAAP, capital ratios) reinforce regulatory risk-aversion framing.

