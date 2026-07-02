# Trace: 2026-07-01_finanz-informatik_bi-engineer

## JD text (fed to classifier, Layer B stripped)

```
# BI Engineer — Finanz Informatik

**URL:** https://www.f-i.de/karriere/offene-stellen/muenster/bi-engineer-m-w-d
**Location:** Hannover, Münster, or Frankfurt, Germany
**Date Posted:** 2026-07-01

---

BI Engineer (m/w/d) at Finanz Informatik

Location: Hannover, Münster, or Frankfurt
Organisational Unit: BI-Kennzahlen (BI Metrics)
Reference Number: 417/B

About the Company
Finanz Informatik is one of Europe's largest banking IT service providers and digitalisation partners operating within the Sparkassen financial group. The company employs over 5,000 staff across 3 locations and offers diverse roles spanning app development, network technologies, consulting, and support.

Role Summary
The team transforms data into actionable insights by developing metrics that enable the Sparkassen group to transparently manage processes and optimise customer journeys.

Key Responsibilities
- Conceptualise and implement new data flows
- Develop usage metrics and operational benchmarks for customers
- Evaluate new metrics requirements collaboratively with stakeholders
- Plan and coordinate work packages for metrics development
- Manage planning, testing, acceptance, and documentation of applications

Requirements
- Completed relevant degree or equivalent professional training
- 2-3 years of relevant professional experience
- Strong analytical capabilities
- Background in data engineering or process/data analysis
- Database management system knowledge and/or programming skills (e.g., Python)
- Ideally project planning and coordination experience
- Enjoyment working with numbers and data evaluation

Benefits
Flexible work hours, subsidised transit passes, remote work options, professional development, cafeteria services, retirement provisions, family services, and fitness support.

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
| jd_authorship | recruiter | recruiter | mixed | 33% |
| stakeholder_orientation | internal_data | commercial | internal_data | 33% |
| autonomy_level | execution | execution | strategic | 33% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | none | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: Testing, acceptance, and documentation are explicitly framed as core responsibilities, signaling a rigour-oriented approach rather than velocity.

**Run 2:** `rigour`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of testing, acceptance, and documentation as managed responsibilities signals a rigour-oriented approach to delivering reliable metrics.

**Run 3:** `rigour`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: Testing, acceptance, and documentation are explicitly named as responsibilities with no velocity signals present in the JD.

### domain_risk

**Run 1:** `moderate`
> Quote: "Develop usage metrics and operational benchmarks for customers"
> Verified: ✓ found in JD
> Reasoning: While operating in banking, the JD emphasizes operational metrics and customer journey optimization rather than financial reporting or regulatory compliance, indicating moderate rather than high risk.

**Run 2:** `moderate`
> Quote: "Develop usage metrics and operational benchmarks for customers"
> Verified: ✓ found in JD
> Reasoning: While Finanz Informatik operates in banking (typically high-risk), the JD emphasizes operational metrics without explicit financial reporting, compliance, or regulatory language that would elevate to high risk.

**Run 3:** `moderate`
> Quote: "The team transforms data into actionable insights by developing metrics that enable the Sparkassen group to transparently manage processes and optimise customer journeys."
> Verified: ✓ found in JD
> Reasoning: While the company operates in banking (high-risk sector), the JD language emphasizes metrics and operational benchmarks without explicit financial reporting, regulatory, or compliance language.

### collaboration_width

**Run 1:** `0`
> Quote: "collaboratively with stakeholders"
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaboration but does not name specific functions like Finance, Product, Engineering, or BI teams.

**Run 2:** `0`
> Quote: "Evaluate new metrics requirements collaboratively with stakeholders"
> Verified: ✓ found in JD
> Reasoning: No distinct named partner teams are identified; 'stakeholders' and 'customers' are mentioned but lack the specificity to count as named collaborative partners.

**Run 3:** `0`
> Quote: "Evaluate new metrics requirements collaboratively with stakeholders"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams or functions are identified; 'stakeholders' is generic and does not count per classification rules.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Plan and coordinate work packages for metrics development"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of coordinating work packages suggests a structured, existing function rather than greenfield startup, with processes already in place.

**Run 2:** `mid`
> Quote: "Plan and coordinate work packages for metrics development"
> Verified: ✓ found in JD
> Reasoning: The explicit coordination and planning responsibilities within a named organizational unit of a large established company suggest a team that exists and has structure beyond early stage.

**Run 3:** `mid`
> Quote: "Conceptualise and implement new data flows"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building new data capabilities within an established company structure, suggesting a mid-stage data function expanding its reach.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "Develop usage metrics and operational benchmarks for customers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs without specific tool names, scale context, or technical methodology details that would indicate hiring manager authorship.

**Run 2:** `recruiter`
> Quote: "Develop usage metrics and operational benchmarks for customers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs without technical specificity, named tools with context, scale numbers, or methodology details that would indicate hiring manager authorship.

**Run 3:** `mixed`
> Quote: "Develop usage metrics and operational benchmarks for customers"
> Verified: ✓ found in JD
> Reasoning: Responsibilities show specific business context understanding (customer-facing metrics, operational benchmarks) but also generic project management language and no specific tool mentions.

⚠ **LLM inconsistency**: runs gave ['recruiter', 'recruiter', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "enable the Sparkassen group to transparently manage processes and optimise customer journeys"
> Verified: ✓ found in JD
> Reasoning: The role is framed as building metrics for internal organizational management and operational optimization, not serving commercial, product, or finance teams specifically.

**Run 2:** `commercial`
> Quote: "optimise customer journeys"
> Verified: ✓ found in JD
> Reasoning: The explicit focus on optimizing customer journeys aligns with customer success and customer operations, which are commercial functions.

**Run 3:** `internal_data`
> Quote: "The team transforms data into actionable insights by developing metrics that enable the Sparkassen group to transparently manage processes and optimise customer journeys."
> Verified: ✓ found in JD
> Reasoning: The role builds metrics and data flows as infrastructure for internal business teams to consume, not for revenue/sales, product experimentation, or FP&A reporting.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'commercial', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Evaluate new metrics requirements collaboratively with stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role is framed around evaluating and executing on requirements set by stakeholders rather than defining strategy or owning direction.

**Run 2:** `execution`
> Quote: "Plan and coordinate work packages for metrics development"
> Verified: ✓ found in JD
> Reasoning: The focus on planning and coordinating predefined work packages, rather than defining direction or strategy, indicates execution-oriented autonomy.

**Run 3:** `strategic`
> Quote: "Conceptualise and implement new data flows"
> Verified: ✓ found in JD
> Reasoning: Verbs like 'conceptualise', 'develop', and 'plan' indicate the role defines what gets built rather than executes direction set by others.

⚠ **LLM inconsistency**: runs gave ['execution', 'execution', 'strategic']

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no reference to AI skills, tools, or practices for the candidate to use or enable.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no references to AI capabilities, tooling, or workflows that the candidate would be expected to deploy or build.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI tools, machine learning, GenAI applications, or AI-enabling data infrastructure.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: The candidate is responsible for managing testing as a core delivery activity, indicating ownership of the testing process rather than just tool familiarity.

**Run 2:** `responsibility`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: Testing is framed as a managed responsibility of the role in delivering applications, indicating the candidate is accountable for testing practices.

**Run 3:** `responsibility`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: 'Manage testing' shows the role is accountable for testing practices as a primary responsibility, not merely listing a testing tool.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: The emphasis on testing, acceptance, and documentation signals operational reliability as a concern, but without explicit compliance or regulatory framing this is moderate rather than high loss-aversion.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role in delivery and optimization terms without explicit risk, compliance, or reliability concerns that would indicate loss-aversion motivation.

**Run 3:** `moderate`
> Quote: "Manage planning, testing, acceptance, and documentation of applications"
> Verified: ✓ found in JD
> Reasoning: Testing and acceptance language suggests concern with operational reliability and data quality, but without explicit risk, compliance, or regulatory framing.

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'moderate']
