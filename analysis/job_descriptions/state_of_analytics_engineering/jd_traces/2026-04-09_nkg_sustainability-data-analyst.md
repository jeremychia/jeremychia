# Trace: 2026-04-09_nkg_sustainability-data-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Sustainability Data Analyst (f/m/d) — Neumann Kaffee Gruppe (NKG)

**URL:** https://nkg.wd103.myworkdayjobs.com/en-US/nkg/job/Sustainability-Data-Analyst_JR102809-1
**Location:** Hamburg, Germany (Telecommute)
**Employment Type:** Full-time

---

## Key Responsibilities

- Develop and implement a unified sustainability data platform integrating multiple sources
- Design and operate scalable data pipelines within Microsoft Fabric
- Create Power BI dashboards and reports for monitoring and decision-making
- Gather requirements and translate them into effective reporting and analytics solutions
- Improve data management processes and contribute innovative ideas to the team

---

## Required Qualifications

- Professional experience in Business Intelligence or Data Analytics
- Power BI expertise
- DAX knowledge
- Microsoft Fabric experience
- SQL proficiency
- Data modeling capabilities
- Structured and analytical manner with emphasis on data quality
- English fluency
- Proactive, self-motivated, solution-oriented approach
- Strong cross-functional collaboration abilities

---

## Preferred / Bonus Skills

- Python and/or PySpark knowledge
- Background with sustainability-related data
- German, Spanish, or Portuguese language skills
- Experience with EUDR compliance systems (e.g., osapiens)
- Geodata validation tools experience

---

## Benefits

Not specified in the posting.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | moderate | moderate | 33% | ✗ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | execution | mixed | mixed | mixed | 100% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality as a core requirement and includes regulatory compliance (EUDR) signals, with no velocity language, placing it in rigour orientation.

**Run 2:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality and professionalism without any velocity language, indicating a rigour-focused orientation.

**Run 3:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality as a core expectation with no velocity language present, indicating a rigour orientation focused on systematic platform building rather than speed.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: EUDR is a mandatory European regulatory requirement for commodity imports; non-compliance carries legal and business penalties, placing this in high domain risk.

**Run 2:** `moderate` ✗
> Quote: "Create Power BI dashboards and reports for monitoring and decision-making"
> Verified: ✓ found in JD
> Reasoning: The role supports business decisions through sustainability data, but the JD language is generic without explicit financial reporting or compliance framing, placing it at moderate risk despite EUDR context.

**Run 3:** `moderate` ✗
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: While the company operates in a regulated compliance space (EUDR), compliance is listed as a preferred skill rather than core responsibility, and the JD frames the role around platform delivery rather than compliance risk prevention.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "No named partner teams or functions explicitly identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions cross-functional collaboration and gathering requirements but does not name specific partner teams or functions.

**Run 2:** `0` ✗
> Quote: "Strong cross-functional collaboration abilities"
> Verified: ✓ found in JD
> Reasoning: The JD expects collaboration but does not name any specific teams or functions.

**Run 3:** `0` ✗
> Quote: "Strong cross-functional collaboration abilities"
> Verified: ✓ found in JD
> Reasoning: The JD describes cross-functional collaboration as expected but names no specific teams, functions, or departments to partner with.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Named infrastructure tools in responsibilities (Microsoft Fabric, Power BI) and focus on operating and improving existing systems signals a mid-stage team.

**Run 2:** `mid` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure and tools (Microsoft Fabric, multiple data sources) while planning a major integration initiative, indicating mid-stage maturity.

**Run 3:** `mid` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Named tools (Fabric, Power BI) appear in specific responsibilities, indicating existing infrastructure, but the role emphasizes developing and scaling rather than maintaining a mature established function.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric; Create Power BI dashboards and reports for monitoring and decision-making"
> Verified: ✓ found in JD
> Reasoning: The JD combines specific technical context (Microsoft Fabric, scalable pipelines) with generic boilerplate (create dashboards, gather requirements).

**Run 2:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Specific technical tool context and skill requirements indicate hiring manager input, but generic phrases like 'improve data management processes' show recruiter contributions.

**Run 3:** `recruiter` ✓
> Quote: "Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic boilerplate action verbs without specific application context, business scale, methodology, or domain depth.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building infrastructure and platforms for internal analytics and decision-making, serving the data function itself.

**Run 2:** `internal_data` ✓
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is building the data platform and infrastructure, suggesting the role primarily serves the data function and internal analytics consumers.

**Run 3:** `internal_data` ✓
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The role is primarily about building data infrastructure and pipelines for internal sustainability management, not serving a specific GTM, product, finance, or commercial function.

### autonomy_level
**Manual:** `execution`

**Run 1:** `mixed` ✗
> Quote: "Develop and implement a unified sustainability data platform; Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic platform and pipeline design with execution of stakeholder requirements, showing both strategic ownership and support orientation.

**Run 2:** `mixed` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The role owns a major platform initiative, but also gathers requirements and translates them into solutions, combining strategic ownership with execution-oriented direction-taking.

**Run 3:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of technical systems (design, operate, develop, improve) with execution against gathered requirements, creating genuine mixed autonomy.

⚠ **Disagreement**: manual=`execution` vs LLM majority=`mixed`

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No AI coding tools, models, or infrastructure skills are mentioned as candidate expectations; Python and PySpark in preferred skills are data engineering capabilities, not AI-specific.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, agentic workflows, AI-assisted coding, or AI-enabled data infrastructure expectations.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: Python and PySpark appear in preferred skills as data processing tools but not framed as AI-assisted development, and the JD contains no mention of AI tools or AI-ready infrastructure expectations.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No explicit testing or data quality responsibility framed as role ownership"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data quality appears only as a personal characteristic requirement, not as a role responsibility, ownership verb, or named testing framework.

**Run 2:** `absent` ✗
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is valued as a professional attribute, but no testing frameworks, data contracts, or observability practices are defined as explicit responsibilities.

**Run 3:** `absent` ✗
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is valued as a candidate work style but is not framed as an owned responsibility, testing framework, or named testing tool.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: Regulatory compliance (EUDR) and data quality emphasis signal operational and regulatory risk awareness, but the overall JD is delivery-focused rather than risk-centric.

**Run 2:** `moderate` ✗
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality emphasis suggests reliability is a concern, but the overall JD framing focuses on delivery and capability rather than risk prevention or compliance, indicating moderate loss-aversion.

**Run 3:** `moderate` ✗
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: The company operates in a regulated space where data accuracy matters, and quality is valued, but the role is framed around platform delivery rather than preventing bad outcomes or managing compliance risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
