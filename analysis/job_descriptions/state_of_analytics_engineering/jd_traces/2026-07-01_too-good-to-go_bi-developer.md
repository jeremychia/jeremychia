# Trace: 2026-07-01_too-good-to-go_bi-developer

## JD text (fed to classifier, Layer B stripped)

```
# BI Developer — Too Good To Go

**URL:** https://www.linkedin.com/jobs/view/4431962529/
**Location:** Copenhagen, Denmark (Hybrid)
**Date Posted:** 2026-07-01

---

BI Developer (12 Month FTC) at Too Good To Go

Location: Copenhagen Municipality, Capital Region of Denmark, Denmark
Employment Type: Fixed-term contract (12 months)
Seniority Level: Mid-Senior level
Team: Parcels Planning

Role Summary
Too Good To Go seeks a BI Developer for their Parcels Planning team. The role focuses on designing the reporting architecture, semantic models and data foundations to enable business scaling over 18-24 months.

Main Responsibilities
- Own technical design and development of BI products and semantic models
- Design performant LookML models, Explores and dashboards
- Partner with Data Engineering teams on data optimisation
- Replace manual reporting and Google Sheets processes with scalable solutions
- Improve data governance through clear definitions and reusable logic

Key Requirements
- BI Engineering or Analytics Engineering experience with semantic modelling expertise
- Strong Looker and LookML proficiency (or equivalent BI tools)
- Dashboard/reporting experience for commercial, finance, or logistics teams
- Dimensional data modelling skills
- Experience with governed reporting environments
- Ability to translate business problems into reporting solutions

Benefits
Flexible hybrid work, enhanced parental leave, health insurance, pension plans, social events, and involvement in employee resource groups focused on diversity and inclusion.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 1 | 4 | 4 | 4 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | mixed | 33% | ✓ |
| stakeholder_orientation | internal_data | mixed | mixed | mixed | 100% | ✗ |
| autonomy_level | strategic | mixed | strategic | execution | 0% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, performance optimization, and scalable solutions without any velocity language such as 'fast-paced' or 'move quickly'.

**Run 2:** `rigour` ✓
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, clear definitions, and scalable solutions with no velocity signals present.

**Run 3:** `rigour` ✓
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, data architecture, and quality (performant models, reusable logic) with no velocity signals.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The role supports business operations and decisions across multiple teams without explicit regulatory, compliance, or financial reporting language that would indicate high risk.

**Run 2:** `moderate` ✓
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: Finance is mentioned as an audience, but the JD lacks regulatory, compliance, or P&L consequences that would indicate high financial risk.

**Run 3:** `moderate` ✓
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: Errors would affect business operations and finance decisions but there is no mention of regulatory compliance, audit, or financial reporting as core requirements.

### collaboration_width
**Manual:** `1`

**Run 1:** `4` ✗
> Quote: "Data Engineering teams; commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are identified: Data Engineering, Commercial, Finance, and Logistics.

**Run 2:** `4` ✗
> Quote: "Partner with Data Engineering teams on data optimisation; Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly mentioned: Data Engineering, Commercial, Finance, and Logistics.

**Run 3:** `4` ✗
> Quote: "Partner with Data Engineering teams on data optimisation; commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: Data Engineering teams are explicitly named as partners; Commercial, Finance, and Logistics are explicitly named as distinct functions the role serves.

⚠ **Disagreement**: manual=`1` vs LLM majority=`4`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Replace manual reporting and Google Sheets processes with scalable solutions"
> Verified: ✓ found in JD
> Reasoning: The team has existing tools (Looker) and established processes but is scaling and modernizing them, consistent with mid-stage maturity.

**Run 2:** `mid` ✓
> Quote: "Replace manual reporting and Google Sheets processes with scalable solutions"
> Verified: ✓ found in JD
> Reasoning: The JD describes modernizing existing reporting processes rather than building a data function from zero, indicating an established team in growth phase.

**Run 3:** `mid` ✓
> Quote: "Replace manual reporting and Google Sheets processes with scalable solutions"
> Verified: ✓ found in JD
> Reasoning: The data function exists with produced outputs (manual reports) but is growing and being improved, indicating a mid-stage team rather than early or mature.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design performant LookML models, Explores and dashboards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities include tool-specific application (LookML, Explores, dimensional modeling) demonstrating technical depth from someone who understands this role.

**Run 2:** `hiring_manager` ✓
> Quote: "Design performant LookML models, Explores and dashboards"
> Verified: ✓ found in JD
> Reasoning: The specific mention of LookML, Explores, and performance optimization indicates the writer understands the actual technical work.

**Run 3:** `mixed` ✗
> Quote: "Design performant LookML models, Explores and dashboards"
> Verified: ✓ found in JD
> Reasoning: Specific tool terminology (LookML, Explores) indicates technical authorship, but generic partnership language elsewhere suggests recruiter input.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `mixed` ✗
> Quote: "dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The role equally serves commercial operations, financial reporting, and logistics planning without a single dominant audience.

**Run 2:** `mixed` ✗
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The JD lists three distinct stakeholder categories with equal weight and no clear primary audience.

**Run 3:** `mixed` ✗
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The role serves commercial, finance, and logistics stakeholders equally, spanning multiple distinct functions without emphasis on one.

⚠ **Disagreement**: manual=`internal_data` vs LLM majority=`mixed`

### autonomy_level
**Manual:** `strategic`

**Run 1:** `mixed` ✗
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic technical ownership of the BI function with execution-oriented collaboration (partnering with Data Engineering) within a scoped domain.

**Run 2:** `strategic` ✓
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: The word 'own' combined with responsibility for design and defining semantic models indicates strategic direction-setting in the BI domain.

**Run 3:** `execution` ✗
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: While the role owns technical design, it executes within a scoped domain (Parcels Planning) in partnership with Data Engineering rather than setting strategy.

⚠ **Disagreement**: manual=`strategic` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, GenAI, coding agents, or AI-enabled infrastructure that would indicate candidate AI competency expectations.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no expectation of AI coding tool usage, AI infrastructure building, or AI-related candidate skills.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, coding assistants, or AI-related infrastructure in the JD.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or observability framework mentioned."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD does not reference testing practices, data quality frameworks, data contracts, or observability mechanisms in responsibilities or requirements.

**Run 2:** `absent` ✗
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: The JD mentions data governance through structure and definitions but contains no explicit reference to testing frameworks, data contracts, or observability practices.

**Run 3:** `absent` ✗
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: Governance is mentioned but no explicit testing, data contracts, or data quality frameworks are named as responsibilities or tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The role is framed in capability and delivery terms (scaling, automation, governance improvement) without risk register language around compliance, trust, or preventing bad outcomes.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed around enabling business scaling and technical improvement, with no emphasis on preventing bad outcomes, compliance, or risk mitigation.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed around design and capability building rather than preventing bad outcomes or managing risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
