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
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | mixed | recruiter | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The explicit emphasis on data quality is a core rigour signal with no counterbalancing velocity language present in the JD.

**Run 2:** `rigour` ✓
> Quote: "Structured and analytical manner with emphasis on data quality"
> Verified: ✓ found in JD
> Reasoning: The single explicit signal in the JD is emphasis on data quality in the qualifications; no velocity, speed, or iteration language appears anywhere in the posting.

**Run 3:** `rigour` ✓
> Quote: "Improve data management processes"
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus on process improvement and operational stability with no velocity or speed-oriented language, indicating a rigour-focused role.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Create Power BI dashboards and reports for monitoring and decision-making"
> Verified: ✓ found in JD
> Reasoning: The role focuses on internal analytics and reporting for business decision-making without explicit financial reporting or regulatory compliance as core responsibilities, despite EUDR compliance appearing only as a bonus skill.

**Run 2:** `moderate` ✗
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: While regulatory compliance language appears via EUDR (EU Deforestation Regulation), it is relegated to preferred skills rather than core responsibilities, and the main responsibilities emphasize reporting and dashboards for decision-making rather than compliance-critical work.

**Run 3:** `moderate` ✗
> Quote: "Experience with EUDR compliance systems (e.g., osapiens)"
> Verified: ✓ found in JD
> Reasoning: While EUDR compliance is mentioned in preferred skills indicating regulatory awareness, the core responsibilities focus on infrastructure building rather than direct regulatory reporting or compliance outcomes.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "Strong cross-functional collaboration abilities"
> Verified: ✓ found in JD
> Reasoning: The JD expects collaboration but does not name any specific partner teams or functions; only generic cross-functional language is used.

**Run 2:** `0` ✗
> Quote: "None identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: No named partner teams or functions (Finance, Product, Marketing, Engineering, etc.) appear in the JD; only generic references to 'cross-functional collaboration' and 'the team'.

**Run 3:** `0` ✗
> Quote: "Strong cross-functional collaboration abilities"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams or functions such as Finance, Product, Engineering, or specific team names are identified in the JD.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Develop and implement a unified sustainability data platform integrating multiple sources"
> Verified: ✓ found in JD
> Reasoning: The emphasis on developing and implementing a unified platform while operating within established tools (Microsoft Fabric, Power BI) signals an existing data function with infrastructure that is growing and scaling.

**Run 2:** `mid` ✗
> Quote: "Improve data management processes and contribute innovative ideas to the team"
> Verified: ✓ found in JD
> Reasoning: Language about improving existing processes, combined with named tools embedded in responsibilities (Microsoft Fabric, Power BI) rather than just requirements, indicates an established data function that is growing and scaling rather than building from zero or fully mature at enterprise scale.

**Run 3:** `mid` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (Microsoft Fabric, Power BI) combined with both development and operational language indicates an existing data function being actively scaled and improved.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric; Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines technical specificity about platforms (Microsoft Fabric) with generic recruiter-style action verbs (gather requirements, translate solutions), indicating mixed authorship.

**Run 2:** `mixed` ✗
> Quote: "Design and operate scalable data pipelines within Microsoft Fabric"
> Verified: ✓ found in JD
> Reasoning: Some responsibilities contain technical tool specificity (Microsoft Fabric, Power BI with named application contexts) suggesting hiring manager input, but multiple generic phrases ('translate them into effective reporting and analytics solutions', 'contribute innovative ideas') indicate recruiter template text as well.

**Run 3:** `recruiter` ✓
> Quote: "Gather requirements and translate them into effective reporting and analytics solutions"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs and lack of specific methodology or operational context despite mentioning tools indicates recruiter authorship.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']
