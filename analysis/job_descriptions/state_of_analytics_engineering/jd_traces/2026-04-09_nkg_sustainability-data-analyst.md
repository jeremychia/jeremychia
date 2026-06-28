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
| domain_risk | high | moderate | high | moderate | 33% | ✗ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | recruiter | mixed | mixed | 33% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | execution | execution | execution | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly emphasizes data quality as a core requirement with no velocity signals like 'fast-paced' or 'move quickly.'

**Run 2:** `rigour` ✓
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: The emphasis on 'operate' and 'scalable' signals operational excellence and reliability-oriented work, with no velocity or speed-to-market language present.

**Run 3:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality explicitly in qualifications and throughout the framing with no velocity signals, establishing rigour as the primary orientation.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The role involves regulatory compliance (EUDR mentioned in preferred skills) but is primarily focused on analytics and reporting rather than financial reporting or direct regulatory filing.

**Run 2:** `high` ✓
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: EUDR (EU Deforestation Regulation) compliance is a direct regulatory requirement for supply chain operations, making data accuracy critical to compliance and market access.

**Run 3:** `moderate` ✗
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: While EUDR compliance appears in the job description, it is listed only as a preferred bonus skill and the core responsibilities do not emphasize regulatory or financial impact as primary drivers.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'moderate']

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "Strong cross-functional collaboration abilities"
> Verified: ✓ found in JD
> Reasoning: While collaboration is mentioned, no specific named partner teams or functions are explicitly listed in the JD.

**Run 2:** `0` ✗
> Quote: "N/A"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams, departments, or stakeholder groups are identified in the job description.

**Run 3:** `0` ✗
> Quote: "None"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD references 'the team' and generic 'cross-functional collaboration' but does not name any specific partner functions such as Finance, Product, Engineering, or Sales.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (Fabric, Power BI) and language about improving processes suggests an existing data function being scaled or enhanced rather than built from scratch.

**Run 2:** `mid` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Named technical tools in the responsibilities section (Microsoft Fabric, Power BI) indicate an existing infrastructure foundation with room to grow, characteristic of a mid-stage team.

**Run 3:** `mid` ✗
> Quote: "Improve data management processes and contribute innovative ideas to the team"
> Verified: ✓ found in JD
> Reasoning: The emphasis on improving existing processes and operating established tools (Microsoft Fabric, Power BI) indicates a team with existing infrastructure that is being enhanced, not building from zero.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `recruiter` ✓
> Quote: "Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: While specific tools are named, the responsibilities rely on generic recruiter boilerplate verbs without business context, scale, or explanation of what problems are being solved.

**Run 2:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Specific technical context (Fabric, scalable pipelines) suggests hiring manager input, but other responsibilities use generic verbs like 'contribute innovative ideas' typical of recruiter authorship.

**Run 3:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric; Create Power BI dashboards and reports for monitoring and decision-making"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD specifies technical tools and requirements (Microsoft Fabric, Power BI, DAX, SQL) but applies them with generic boilerplate action verbs lacking precise application context or scale.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'mixed']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building data infrastructure and dashboards for internal sustainability monitoring and decision-making rather than serving commercial, product, finance, or external audiences.

**Run 2:** `internal_data` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The focus on building a unified data platform and integrating sources emphasizes infrastructure serving internal data consumers rather than a specific business function.

**Run 3:** `internal_data` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources; Design and operate scalable data pipelines"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's primary focus is on building and maintaining data infrastructure itself—the platform, pipelines, and data management processes—rather than serving an explicitly named business function.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: The primary verbs (gather, create, contribute, translate) indicate responsive execution of others' requirements rather than strategic direction-setting.

**Run 2:** `execution` ✗
> Quote: "Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: The analyst executes against requirements gathered from others, implementing solutions rather than setting strategic direction for the data function.

**Run 3:** `execution` ✗
> Quote: "Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: The language explicitly frames the role as receiving requirements from others and executing solutions, with no strategic ownership language such as 'define', 'lead', 'own', or 'drive'.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`
