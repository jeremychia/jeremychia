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
| collaboration_width | 1 | 1 | 4 | 4 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | mixed | mixed | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | commercial | 33% | ✓ |
| autonomy_level | strategic | strategic | mixed | strategic | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | moderate | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data governance, clear definitions, and reusable logic as core responsibilities with no velocity or speed signals present.

**Run 2:** `rigour` ✓
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize governance, clear definitions, and reusable logic as core expectations with no velocity signals like 'fast-paced' or 'ship quickly'.

**Run 3:** `rigour` ✓
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, clear definitions, reusable logic, and performant design with no velocity or iteration language present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The role involves operational reporting and BI infrastructure for business teams without explicit financial reporting, compliance, or regulatory language.

**Run 2:** `moderate` ✓
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: Finance is named as an audience but the JD frames this as reporting and dashboards without signals of financial reporting, regulatory compliance, or mission-critical impact.

**Run 3:** `moderate` ✓
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The role serves finance and commercial teams but contains no regulatory, compliance, or financial reporting language typical of high-risk domains.

### collaboration_width
**Manual:** `1`

**Run 1:** `1` ✓
> Quote: "Partner with Data Engineering teams on data optimisation"
> Verified: ✓ found in JD
> Reasoning: Only one named team (Data Engineering) is explicitly listed as a collaboration partner in the responsibilities.

**Run 2:** `4` ✗
> Quote: "Partner with Data Engineering teams on data optimisation; commercial, finance, or logistics teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct functions explicitly named: Data Engineering (collaboration partner), Commercial, Finance, and Logistics (named audiences).

**Run 3:** `4` ✗
> Quote: "Data Engineering teams; commercial, finance, or logistics teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names four distinct functions: Data Engineering, Commercial, Finance, and Logistics teams.

⚠ **Disagreement**: manual=`1` vs LLM majority=`4`

⚠ **LLM inconsistency**: runs gave ['1', '4', '4']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "designing the reporting architecture, semantic models and data foundations to enable business scaling over 18-24 months"
> Verified: ✓ found in JD
> Reasoning: The JD indicates modernization of existing processes (Google Sheets replacement) and partnership with existing data engineering teams, suggesting a maturing function rather than greenfield startup.

**Run 2:** `mid` ✓
> Quote: "Replace manual reporting and Google Sheets processes with scalable solutions"
> Verified: ✓ found in JD
> Reasoning: Existing Data Engineering teams and manual reporting processes indicate an established function needing scaling and improvement, not a greenfield build.

**Run 3:** `mid` ✓
> Quote: "Replace manual reporting and Google Sheets processes with scalable solutions"
> Verified: ✓ found in JD
> Reasoning: The role addresses existing manual processes and partners with established Data Engineering teams, indicating a mid-stage function scaling beyond early setup.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Design performant LookML models, Explores and dashboards"
> Verified: ✓ found in JD
> Reasoning: Specific naming of Looker tools (LookML, Explores) and mention of replacing Google Sheets processes indicates someone with hands-on BI experience wrote this.

**Run 2:** `mixed` ✗
> Quote: "Design performant LookML models, Explores and dashboards"
> Verified: ✓ found in JD
> Reasoning: Specific LookML and Looker tool knowledge (Explores is a Looker-specific feature) suggests hiring manager input, but generic collaboration phrases like 'Partner with Data Engineering teams' suggest recruiter involvement.

**Run 3:** `mixed` ✗
> Quote: "Design performant LookML models, Explores and dashboards"
> Verified: ✓ found in JD
> Reasoning: The JD includes specific BI tool knowledge (LookML, Explores) alongside generic verbs like 'Own technical design,' indicating both hiring-manager and recruiter contributions.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "designing the reporting architecture, semantic models and data foundations to enable business scaling over 18-24 months"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building data infrastructure and semantic models as its primary mission, with commercial and finance teams as secondary consumers.

**Run 2:** `internal_data` ✓
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: The primary framing is building data foundations and semantic models for platform consumers (commercial, finance, logistics teams) rather than serving product or commercial teams directly.

**Run 3:** `commercial` ✗
> Quote: "Dashboard/reporting experience for commercial, finance, or logistics teams"
> Verified: ✓ found in JD
> Reasoning: The Parcels Planning team's focus on reporting architecture primarily enables commercial operations and GTM functions, with finance as secondary.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'commercial']

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: The role is framed around owning and designing the technical architecture for BI/reporting, not executing direction set by others.

**Run 2:** `mixed` ✗
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of BI platform architecture design with execution responsibility for building dashboards and models in service of business teams.

**Run 3:** `strategic` ✓
> Quote: "Own technical design and development of BI products and semantic models"
> Verified: ✓ found in JD
> Reasoning: The 'Own' verb for technical design and architecture indicates strategic responsibility for shaping the BI direction rather than executing existing plans.

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'strategic']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no references to AI skills, coding tools, or AI-ready data infrastructure.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, GenAI applications, or AI-related data infrastructure expectations.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, or AI infrastructure expectations for the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: Data governance is mentioned but no testing frameworks, data quality ownership, or observability practices are described.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: While data governance is mentioned as an area to improve, no testing practices, data quality frameworks, observability, or data contracts are explicitly named.

**Run 3:** `absent` ✗
> Quote: "No testing signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: While data governance is mentioned, there is no explicit reference to testing frameworks, data contracts, observability, or quality assurance practices.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is framed around building better reporting infrastructure and scaling capabilities with no emphasis on risk, compliance, or preventing bad outcomes.

**Run 2:** `moderate` ✗
> Quote: "Improve data governance through clear definitions and reusable logic"
> Verified: ✓ found in JD
> Reasoning: Governance suggests concern for operational reliability and data trust, but this is secondary to the primary framing of enabling business scaling rather than preventing compliance failures.

**Run 3:** `none` ✗
> Quote: "Role focuses on designing the reporting architecture, semantic models and data foundations to enable business scaling over 18-24 months"
> Verified: ✓ found in JD
> Reasoning: The primary framing emphasizes delivery and scaling capabilities rather than risk prevention, compliance, or operational reliability concerns.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'none']
