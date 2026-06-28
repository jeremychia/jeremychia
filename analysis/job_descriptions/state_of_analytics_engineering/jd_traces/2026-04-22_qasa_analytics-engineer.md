# Trace: 2026-04-22_qasa_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Qasa

**URL:** https://careers.qasa.se/jobs/7452878-analytics-engineer-build-qasa-s-data-foundation
**Location:** Stockholm, Sweden (Hybrid)

---

## Key Responsibilities

- Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams
- Design and construct data models serving as the bridge between raw data and business insights
- Create self-serve analytics capabilities that empower teams to independently answer questions
- Transform complex data into compelling narratives informing product strategy and financial planning
- Partner with engineering to ensure data pipelines meet organizational needs
- Implement data governance protocols addressing GDPR compliance and access management
- Explore forecasting, modeling, and machine learning opportunities

---

## Required Qualifications

- Advanced SQL proficiency and data modeling expertise
- Demonstrated success designing and maintaining production data models
- Track record defining KPIs with consistent metric standards across organizations
- Strong analytical abilities paired with clear data communication skills
- Experience implementing BI tools (Metabase preferred)
- Cross-functional collaboration experience
- Business acumen across product, marketing, and finance domains
- Familiarity with AI-assisted development tools

---

## Preferred / Bonus Skills

- Amplitude and GA4 platform experience
- Data product deployment background
- GDPR and data governance legal knowledge

---

## Benefits

- 30 paid vacation days
- Pension contributions (ITP1 formula-based)
- Salary exchange program with 6% employer top-up
- Parental benefits (10% salary for 2-6 months)
- Annual wellness allowance: SEK 5,000
- Equipment provision (laptop, phone)
- Södermalm office location with Friday social events

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 5 | 6 | 6 | 6 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | recruiter | mixed | 33% | ✗ |
| stakeholder_orientation |  | mixed | internal_data | internal_data | 33% | ✗ |
| autonomy_level |  | strategic | strategic | execution | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, compliance, and consistency with no velocity language, establishing a rigour-focused orientation.

**Run 2:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, compliance, standardization, and data quality without any velocity or speed-focused language.

**Run 3:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance and governance implementation are explicit rigour signals that dominate the responsibilities section.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The JD touches on compliance and supports financial planning, but lacks explicit language about financial reporting or regulatory compliance at scale, indicating moderate rather than high risk.

**Run 2:** `moderate` ✓
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance is explicitly required, the role is framed as serving multiple business functions rather than as mission-critical financial reporting or regulatory operations.

**Run 3:** `moderate` ✓
> Quote: "Transform complex data into compelling narratives informing product strategy and financial planning"
> Verified: ✓ found in JD
> Reasoning: Financial planning is mentioned alongside product strategy, indicating moderate business impact without explicit regulatory or financial-reporting-critical language.

### collaboration_width
**Manual:** `5`

**Run 1:** `6` ✗
> Quote: "Product; Marketing; Finance; Support; Country Management; engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names six distinct teams: Product, Marketing, Finance, Support, Country Management, and Engineering.

**Run 2:** `6` ✗
> Quote: "Product; Marketing; Finance; Support; Country Management; engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities explicitly name six distinct teams as primary collaborators and stakeholders.

**Run 3:** `6` ✗
> Quote: "Product; Marketing; Finance; Support; Country Management teams; engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct functions are explicitly named as collaboration partners across the responsibilities section.

⚠ **Disagreement**: manual=`5` vs LLM majority=`6`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Create self-serve analytics capabilities that empower teams to independently answer questions"
> Verified: ✓ found in JD
> Reasoning: The role focuses on building and creating new capabilities rather than maintaining existing systems, and involves establishing governance and unified standards, indicating a mid-stage team expanding its capabilities.

**Run 2:** `mid` ✗
> Quote: "Demonstrated success designing and maintaining production data models"
> Verified: ✓ found in JD
> Reasoning: Production data models already exist and must be maintained, but the role emphasizes building new self-serve capabilities and establishing governance, indicating a growing function rather than mature infrastructure.

**Run 3:** `mid` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Create self-serve analytics capabilities that empower teams to independently answer questions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role focuses on establishing and creating new capabilities while maintaining production data models, indicating a growth/improvement phase rather than early-stage or fully mature specialization.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The responsibilities show specific problem understanding (fragmented KPIs and terminology) and named teams, but also some generic framing around stakeholder partnership, suggesting both hiring manager and recruiter input.

**Run 2:** `recruiter` ✓
> Quote: "Design and construct data models serving as the bridge between raw data and business insights"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use aspirational, generic language without specific implementation details, scale numbers, or technical context that would indicate hands-on domain expertise.

**Run 3:** `mixed` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Explore forecasting, modeling, and machine learning opportunities"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific organizational context (unified KPIs, GDPR governance) indicates hiring manager input, while vague exploratory language ('explore opportunities') suggests recruiter templating.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'mixed']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Transform complex data into compelling narratives informing product strategy and financial planning"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves both product strategy and financial planning with equal emphasis, and the focus on unified KPIs serves multiple business audiences, indicating mixed orientation.

**Run 2:** `internal_data` ✗
> Quote: "Create self-serve analytics capabilities that empower teams to independently answer questions"
> Verified: ✓ found in JD
> Reasoning: The majority of responsibilities emphasize building analytics infrastructure, governance, and data models—serving the internal data function—rather than primarily serving a single business team.

**Run 3:** `internal_data` ✗
> Quote: "Create self-serve analytics capabilities that empower teams to independently answer questions"
> Verified: ✓ found in JD
> Reasoning: The primary orientation is building analytics infrastructure and enabling other teams to self-serve rather than delivering insights to specific business domains.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'internal_data']

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The verb 'establish' and the responsibility to define KPIs and terminology across the organization indicates the role sets direction rather than executes direction from others.

**Run 2:** `strategic` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes establishing standards, designing governance protocols, and defining how analytics is delivered across the organization, indicating strategic direction-setting rather than execution of defined work.

**Run 3:** `execution` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Design and construct data models"
> Verified: ⚠ NOT found verbatim
> Reasoning: While responsibilities include strategic-sounding verbs, the overall framing presents these as specific deliverables to execute rather than open-ended strategic ownership of the analytics function.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`

⚠ **LLM inconsistency**: runs gave ['strategic', 'strategic', 'execution']
