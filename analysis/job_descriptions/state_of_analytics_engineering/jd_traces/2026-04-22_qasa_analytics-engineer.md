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
| domain_risk | moderate | high | moderate | high | 33% | ✗ |
| collaboration_width | 5 | 6 | 6 | 6 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | recruiter | mixed | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | mixed | mixed | 33% | ✗ |
| autonomy_level | strategic | execution | strategic | strategic | 33% | ✓ |
| ai_role |  | ai_user | none | ai_user | 33% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, compliance, and reliability (GDPR protocols, metric standards, production data models) with no velocity-oriented language like 'fast-paced' or 'ship quickly'.

**Run 2:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: Data governance, GDPR compliance, and consistent metric standards emphasize correctness and compliance without any velocity language (rapid, MVP, fast-paced) throughout the JD.

**Run 3:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, compliance, and systematic data quality practices without any velocity-oriented language, indicating a rigour-focused orientation.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `high` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of GDPR compliance (regulatory) combined with financial planning as a stakeholder indicates data errors could have direct regulatory and financial consequences.

**Run 2:** `moderate` ✓
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance and financial planning are mentioned as concerns, but the focus is on data governance and access management rather than financial reporting accuracy or regulatory compliance as the primary role driver.

**Run 3:** `high` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly requires GDPR compliance implementation and mentions financial planning as a primary use case, establishing both regulatory and financial decision-making risk.

⚠ **Disagreement**: manual=`moderate` vs LLM majority=`high`

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'high']

### collaboration_width
**Manual:** `5`

**Run 1:** `6` ✗
> Quote: "Product, Marketing, Finance, Support, and Country Management teams; engineering"
> Verified: ✓ found in JD
> Reasoning: Six distinct named functions are identified: Product, Marketing, Finance, Support, Country Management, and Engineering.

**Run 2:** `6` ✗
> Quote: "Product; Marketing; Finance; Support; Country Management; engineering"
> Verified: ✓ found in JD
> Reasoning: Five teams explicitly named in establishing KPIs, plus engineering separately identified as a partner in ensuring data pipelines meet organizational needs.

**Run 3:** `6` ✗
> Quote: "Product, Marketing, Finance, Support, and Country Management teams; engineering"
> Verified: ✓ found in JD
> Reasoning: Six distinct named functions appear in the responsibilities: Product, Marketing, Finance, Support, Country Management, and Engineering.

⚠ **Disagreement**: manual=`5` vs LLM majority=`6`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Partner with engineering to ensure data pipelines meet organizational needs"
> Verified: ✓ found in JD
> Reasoning: The role involves implementing governance and creating self-serve capabilities on existing data infrastructure (pipelines, named tools), suggesting a team moving from early to mature but not yet fully established.

**Run 2:** `mid` ✗
> Quote: "Design and construct data models serving as the bridge between raw data and business insights"
> Verified: ✓ found in JD
> Reasoning: References to production data models and existing pipelines indicate established infrastructure, while responsibilities emphasizing implement and create suggest growth and improvement rather than greenfield build.

**Run 3:** `mid` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance; Create self-serve analytics capabilities that empower teams"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes implementing new governance and self-serve capabilities while requiring experience with 'production data models,' indicating existing infrastructure being enhanced rather than greenfield building.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Partner with engineering to ensure data pipelines meet organizational needs"
> Verified: ✓ found in JD
> Reasoning: The JD combines technical specificity (KPI standards, GDPR governance, specific tools like Metabase and Amplitude) with generic boilerplate (partnership language, empowering teams).

**Run 2:** `recruiter` ✓
> Quote: "Partner with engineering to ensure data pipelines meet organizational needs"
> Verified: ✓ found in JD
> Reasoning: Generic language about supporting teams to ensure needs are met lacks technical specificity about tools, scale, methodology, or current state that a hiring manager would provide.

**Run 3:** `mixed` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: Specific technical elements like GDPR compliance and cross-functional KPI standardization indicate hiring manager input, but generic phrases like 'transform data into narratives' suggest recruiter contributions.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'mixed']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Create self-serve analytics capabilities that empower teams to independently answer questions"
> Verified: ✓ found in JD
> Reasoning: The role is fundamentally about building data infrastructure and self-serve capabilities that serve other teams, placing the primary audience as data consumers and the platform itself.

**Run 2:** `mixed` ✗
> Quote: "Transform complex data into compelling narratives informing product strategy and financial planning"
> Verified: ✓ found in JD
> Reasoning: The JD serves Product (strategy), Finance (planning), and Internal audiences (self-serve analytics capabilities, data infrastructure) with equal emphasis across multiple responsibilities.

**Run 3:** `mixed` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple business functions (Product, Marketing, Finance, Support, Country Management) with equal emphasis through shared analytics infrastructure rather than serving one primary stakeholder.

⚠ **Disagreement**: manual=`internal_data` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['internal_data', 'mixed', 'mixed']

### autonomy_level
**Manual:** `strategic`

**Run 1:** `execution` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The role has specific, bounded responsibilities to deliver (establish KPIs, design models, implement governance) within a defined scope rather than setting overall direction for the analytics organization.

**Run 2:** `strategic` ✓
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: Strategic direction-setting verbs (establish, design, create, implement) dominate the responsibilities section, indicating the role defines how analytics is delivered rather than executing scoped work.

**Run 3:** `strategic` ✓
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use directive verbs (establish, design, construct, create, implement) that emphasize defining direction and building capabilities rather than executing pre-defined work.

⚠ **LLM inconsistency**: runs gave ['execution', 'strategic', 'strategic']

### ai_role
**Manual:** ``

**Run 1:** `ai_user` ✗
> Quote: "Familiarity with AI-assisted development tools"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to have familiarity with AI-assisted development tools (like GitHub Copilot or Claude Code) to accelerate their own coding and development work.

**Run 2:** `none` ✗
> Quote: "Familiarity with AI-assisted development tools"
> Verified: ✓ found in JD
> Reasoning: Familiarity is too vague to count as a skill expectation (requires proven usage or proficiency), and the ML mention is exploratory rather than a core responsibility.

**Run 3:** `ai_user` ✗
> Quote: "Familiarity with AI-assisted development tools"
> Verified: ✓ found in JD
> Reasoning: The required qualifications expect candidates to be familiar with AI-assisted development tools, indicating the role expects candidates to use AI tools to accelerate their own coding and analytical productivity.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

⚠ **LLM inconsistency**: runs gave ['ai_user', 'none', 'ai_user']

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: The JD does not mention testing frameworks, data quality practices, data contracts, or observability as either a responsibility or a tool.

**Run 2:** `absent` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: Governance language focuses on GDPR compliance and access management, not on testing, data contracts, data quality frameworks, or observability.

**Run 3:** `absent` ✗
> Quote: "No testing, data quality, data contracts, or observability practices mentioned in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no references to testing frameworks, data quality standards, data contracts, or observability tooling in either the responsibilities or requirements sections.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance and governance are mentioned as concerns, but the role's primary framing is capability-building (KPIs, self-serve analytics, modeling) rather than preventing catastrophic risk or regulatory exposure.

**Run 2:** `moderate` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance indicates regulatory risk awareness, but the role is framed primarily around analytics delivery and capability building rather than preventing failures or stakeholder trust as the dominant concern.

**Run 3:** `moderate` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: Compliance and governance are explicit responsibilities, but the primary framing emphasizes capability building and analytics delivery rather than preventing bad data outcomes or regulatory exposure.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
