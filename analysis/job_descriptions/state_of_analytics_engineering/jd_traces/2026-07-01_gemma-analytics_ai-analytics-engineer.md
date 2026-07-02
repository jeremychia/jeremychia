# Trace: 2026-07-01_gemma-analytics_ai-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# AI & Analytics Engineer — Gemma Analytics

**URL:** https://gemma.jobs.personio.de/job/2649089?display=en&language=en&pid=fa3a7aa6-8e14-4a4a-bd96-762640840138&it=26JtXR2RD2OVFVc5EDmXOw&_ghcid=71e67ea4-f328-4404-ad0c-95e7b0e31743
**Location:** Berlin, Germany
**Date Posted:** 2026-07-01
**Salary:** 56,700–69,300 EUR

---

AI & Analytics Engineer at Gemma Analytics

About the Company
Gemma Analytics is a Berlin-based firm founded in 2020 that helps organisations become more data-driven. The company has served over 50 clients and operates profitably without VC backing. Team of 18, growing to 24 in 2026.

Role Summary
This is a mid-level position where engineers work at the intersection of data and AI, building both traditional data pipelines and intelligent, agentic solutions that create real business impact.

Key Responsibilities
- Work with multiple technologies across the modern data stack
- Develop advanced data reporting and visualisations
- Apply data modelling methodologies
- Leverage AI tools including agentic workflows and AI coding assistants

Requirements
Essential:
- SQL and relational database experience
- Native or C2 fluency in German and English
- Understanding of data modelling techniques and data warehousing
- Professional AI tool experience, ideally including coding assistants

Optional:
- Python or other programming languages
- Stakeholder/client management experience

Compensation & Benefits
- €56,700 - €69,300 annually
- Flexible office attendance (2-5 days weekly)
- Profit sharing (minimum 20%)
- Berlin location near Nordbahnhof
- Full-time, permanent employee in Berlin

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 0 | 0 | 1 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | recruiter | recruiter | 33% |
| stakeholder_orientation | internal_data | commercial | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | ai_user | ai_enabler | ai_user | 33% |
| testing_framing | absent | absent | absent | 100% |
| loss_aversion_framing | none | none | none | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Apply data modelling methodologies"
> Verified: ✓ found in JD
> Reasoning: The emphasis on 'methodologies' and 'advanced' reporting signals a systematic, quality-focused approach with no velocity language present.

**Run 2:** `rigour`
> Quote: "Apply data modelling methodologies"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize established methodologies and process-oriented work with no velocity language present, defaulting to rigour when neither orientation dominates.

**Run 3:** `rigour`
> Quote: "Apply data modelling methodologies"
> Verified: ✓ found in JD
> Reasoning: The emphasis on applying established methodologies signals a structured, methodical approach rather than velocity-driven delivery.

### domain_risk

**Run 1:** `moderate`
> Quote: "helps organisations become more data-driven"
> Verified: ✓ found in JD
> Reasoning: The role involves standard business intelligence and data analytics work for client organizations without explicit financial reporting, compliance, or regulatory language.

**Run 2:** `moderate`
> Quote: "helps organisations become more data-driven"
> Verified: ✓ found in JD
> Reasoning: The consulting context serves business decision-making without explicit financial reporting, regulatory, or compliance requirements, placing it in the moderate risk category.

**Run 3:** `moderate`
> Quote: "helps organisations become more data-driven"
> Verified: ✓ found in JD
> Reasoning: As a consulting firm serving various clients without explicit financial, regulatory, or compliance mandates, data errors affect business decisions without immediate legal or financial reporting consequences.

### collaboration_width

**Run 1:** `0`
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No named partner teams or functions are explicitly identified in the responsibilities section.

**Run 2:** `0`
> Quote: "N/A - no named partner teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: No specific named functions (Finance, Product, Engineering, etc.) or teams are explicitly listed as collaboration partners in the responsibilities.

**Run 3:** `1`
> Quote: "Stakeholder/client management experience"
> Verified: ✓ found in JD
> Reasoning: Only clients are explicitly named as a collaboration partner; no internal team functions are specified.

⚠ **LLM inconsistency**: runs gave ['0', '0', '1']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Team of 18, growing to 24 in 2026"
> Verified: ✓ found in JD
> Reasoning: The company is an established, profitable organization with an existing data service offering and client base, but no signals of specialized sub-teams or large-scale specialization.

**Run 2:** `mid`
> Quote: "Team of 18, growing to 24 in 2026"
> Verified: ✓ found in JD
> Reasoning: The established consulting firm with existing client base and planned growth implies a functioning but still-scaling data function, not early-stage or highly specialized.

**Run 3:** `mid`
> Quote: "building both traditional data pipelines and intelligent, agentic solutions"
> Verified: ✓ found in JD
> Reasoning: An established 18-person team serving 50+ clients with varied work across both traditional and advanced analytics indicates a mid-stage data function.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Leverage AI tools including agentic workflows and AI coding assistants"
> Verified: ✓ found in JD
> Reasoning: Specific technical knowledge about AI tools and agentic workflows combined with generic boilerplate language like 'Work with multiple technologies' indicates mixed authorship.

**Run 2:** `recruiter`
> Quote: "Work with multiple technologies across the modern data stack"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs and boilerplate language with no technical specificity about tools, scale, or domain-specific methodology details only a hiring manager would know.

**Run 3:** `recruiter`
> Quote: "Work with multiple technologies across the modern data stack"
> Verified: ✓ found in JD
> Reasoning: Generic phrasing without specific context about tools, scale, or domain problems signals recruiter-written boilerplate rather than hiring manager experience.

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'recruiter']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "building both traditional data pipelines and intelligent, agentic solutions"
> Verified: ✓ found in JD
> Reasoning: The role is primarily focused on building data infrastructure and analytics platforms that serve the data function itself within client organizations.

**Run 2:** `commercial`
> Quote: "building both traditional data pipelines and intelligent, agentic solutions that create real business impact"
> Verified: ✓ found in JD
> Reasoning: The consulting context frames the role as building data solutions that serve client business needs, positioning external commercial stakeholders as the primary audience.

**Run 3:** `internal_data`
> Quote: "building both traditional data pipelines and intelligent, agentic solutions"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes building data infrastructure and methodologies that serve internal data consumers rather than a specific business function.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'commercial', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Work with multiple technologies across the modern data stack"
> Verified: ✓ found in JD
> Reasoning: The action verb 'work with' and mid-level positioning indicate the engineer executes against a defined technology stack rather than setting strategic direction.

**Run 2:** `execution`
> Quote: "Apply data modelling methodologies"
> Verified: ✓ found in JD
> Reasoning: The role is framed to work within and apply existing methodologies and technology choices rather than define or shape how analytics is delivered.

**Run 3:** `execution`
> Quote: "Apply data modelling methodologies"
> Verified: ✓ found in JD
> Reasoning: The instruction to apply existing methodologies indicates execution of established practices rather than strategic direction-setting.

### ai_role

**Run 1:** `ai_user`
> Quote: "Professional AI tool experience, ideally including coding assistants"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to have hands-on experience using AI tools like coding assistants to accelerate their own engineering work.

**Run 2:** `ai_enabler`
> Quote: "building both traditional data pipelines and intelligent, agentic solutions that create real business impact"
> Verified: ✓ found in JD
> Reasoning: The role explicitly builds agentic solutions and applies agentic workflows, expecting the candidate to construct data infrastructure and intelligent systems that enable AI.

**Run 3:** `ai_user`
> Quote: "Leverage AI tools including agentic workflows and AI coding assistants"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use (leverage) AI tools and coding assistants as personal productivity tools to accelerate their own work.

⚠ **LLM inconsistency**: runs gave ['ai_user', 'ai_enabler', 'ai_user']

### testing_framing

**Run 1:** `absent`
> Quote: "No testing signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities and requirements sections contain no mention of testing, data contracts, data quality frameworks, or observability practices.

**Run 2:** `absent`
> Quote: "No testing or data quality framework mentioned."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no language about testing, data quality, data contracts, observability, or reliability as either a responsibility or a required tool.

**Run 3:** `absent`
> Quote: "No testing signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of testing frameworks, data quality standards, data contracts, or observability practices.

### loss_aversion_framing

**Run 1:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The role is framed in capability and delivery terms ('create real business impact') with no language about risk, compliance, regulatory exposure, or preventing bad outcomes.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The role is framed entirely around capability building and business impact delivery with no mention of risk, compliance, reliability, incident response, or preventing bad outcomes.

**Run 3:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes building capabilities and creating business impact without mention of compliance, reliability, risk prevention, or stakeholder trust concerns.
