# Trace: 2026-07-02_asics_senior-business-intelligence-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Business Intelligence Engineer — ASICS

**URL:** https://career5.successfactors.eu/career?career_ns=job_listing&company=S003910448P&navBarLevel=JOB_SEARCH&rcm_site_locale=en_GB&career_job_req_id=76188&source=LinkedIn
**Location:** Hoofddorp, Netherlands
**Date Posted:** 2026-07-02

---

# Senior Business Intelligence Engineer

Company: ASICS
Requisition ID: 76188
Location: Hoofddorp, near Amsterdam (EMEA headquarters)
Employment Type: Permanent, Full Time
Salary: Not stated

## Key Responsibilities
- Define and prioritise technical requirements that align with the overall business strategy
- Directing data integration and pipeline orchestration across the organization
- Creating data models and implementing transformation/cleansing/enrichment processes
- Enhancing database platform performance and cost-effectiveness
- Establishing documentation, version control, and data privacy compliance
- Providing technical support and training to colleagues
- Promoting BI adoption and data literacy across EMEA

## Required Qualifications
- Extensive SQL and relational database experience
- Strong hands-on experience with Snowflake and DBT
- Bachelor's degree in Computer Science, IT, or related field
- CI/CD standards experience for data engineering
- Proven success leading ETL and database initiatives

## Preferred Qualifications
- Experience with complementary ETL solutions like Azure Data Factory

Interview Process & Team Structure: Not specified in the job posting.

Benefits: Gym access, 50% ASICS gear discount, Calm app access, wellness programs, hybrid work flexibility, and annual working abroad allowance.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 0 | 0 | 0 | 0 | 100% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | recruiter | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | mixed | mixed | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Establishing documentation, version control, and data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, compliance, and documentation without any velocity-oriented language.

**Run 2:** `rigour` ✓
> Quote: "Establishing documentation, version control, and data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance practices (documentation, version control, compliance) and CI/CD standards as core expectations rather than speed or delivery pace.

**Run 3:** `rigour` ✓
> Quote: "Establishing documentation, version control, and data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: Rigour signals (documentation, version control, compliance) dominate the responsibilities with no velocity language present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: While data privacy is mentioned as a regulatory concern, the company is retail/apparel and the JD frames the role as operational platform management rather than financial reporting or high-stakes compliance work.

**Run 2:** `moderate` ✓
> Quote: "data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: While compliance is mentioned, the JD lacks financial reporting, regulatory reporting, or audit language; ASICS retail/sportswear context also suggests moderate rather than high risk.

**Run 3:** `moderate` ✓
> Quote: "Enhancing database platform performance and cost-effectiveness"
> Verified: ✓ found in JD
> Reasoning: The role is framed as internal infrastructure and platform work with no explicit financial reporting, regulatory, or compliance-critical framing.

### collaboration_width
**Manual:** `0`

**Run 1:** `0` ✓
> Quote: "None"
> Verified: ✓ found in JD
> Reasoning: No named teams like Finance, Product, Marketing, Data Science, or Engineering are explicitly identified; the JD uses generic language like 'colleagues' and 'the organization' without naming specific partner functions.

**Run 2:** `0` ✓
> Quote: "Providing technical support and training to colleagues; Promoting BI adoption and data literacy across EMEA"
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaboration scope but names no distinct partner functions like Finance, Product, Marketing, or Engineering; 'colleagues' and geographic region do not count as named teams.

**Run 3:** `0` ✓
> Quote: "Providing technical support and training to colleagues"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner teams (Finance, Product, Data Science, Engineering, etc.) are identified; mentions are generic.

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Directing data integration and pipeline orchestration across the organization"
> Verified: ✓ found in JD
> Reasoning: The organization has existing infrastructure being actively directed and scaled, with training and adoption initiatives underway, but governance practices are still being established rather than mature.

**Run 2:** `mid` ✗
> Quote: "Directing data integration and pipeline orchestration across the organization"
> Verified: ✓ found in JD
> Reasoning: The verb 'directing' implies existing infrastructure at scale, and paired with named tools (Snowflake, DBT) suggests a growing function with established operations but not yet mature specialization.

**Run 3:** `mid` ✗
> Quote: "Directing data integration and pipeline orchestration across the organization"
> Verified: ✓ found in JD
> Reasoning: Responsibilities reference existing infrastructure, named tools (Snowflake, DBT), and enhancement work rather than greenfield build.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `recruiter` ✗
> Quote: "Creating data models and implementing transformation/cleansing/enrichment processes"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic action verbs without technical specificity, scale, methodology, or context that would indicate authorship by someone doing this work.

**Run 2:** `mixed` ✓
> Quote: "Strong hands-on experience with Snowflake and DBT; Define and prioritise technical requirements that align with the overall business strategy"
> Verified: ✓ found in JD
> Reasoning: The JD combines technical specificity (named tools, platform knowledge) with generic boilerplate action verbs ('Define and prioritise', 'Providing technical support', 'Promoting BI adoption') that lack operational context.

**Run 3:** `recruiter` ✗
> Quote: "Providing technical support and training to colleagues"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic boilerplate verbs without technical specificity about implementation context, scale, methodology, or how tools are applied.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Directing data integration and pipeline orchestration across the organization"
> Verified: ✓ found in JD
> Reasoning: The primary responsibilities focus on building and maintaining the data platform itself and enabling internal data consumers rather than serving commercial, product, or finance stakeholders.

**Run 2:** `internal_data` ✓
> Quote: "Promoting BI adoption and data literacy across EMEA"
> Verified: ✓ found in JD
> Reasoning: The entire role focuses on building data infrastructure, enabling internal BI users, and training colleagues—not serving commercial, product, or finance stakeholders.

**Run 3:** `internal_data` ✓
> Quote: "Promoting BI adoption and data literacy across EMEA"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves internal data consumers and analytics teams, with emphasis on data platform, infrastructure, and adoption.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Define and prioritise technical requirements that align with the overall business strategy"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly expected to define and prioritize technical direction across the organization, establishing governance and shaping how data delivery works.

**Run 2:** `mixed` ✗
> Quote: "Define and prioritise technical requirements that align with the overall business strategy; Directing data integration and pipeline orchestration across the organization; Creating data models and implementing transformation/cleansing/enrichment processes"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting verbs (Define, Directing, Establishing) with execution responsibilities (Creating, Implementing, Providing support), equally present in the responsibilities section.

**Run 3:** `mixed` ✗
> Quote: "Define and prioritise technical requirements that align with the overall business strategy"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs like 'define' and 'directing' coexist with execution responsibilities like 'providing technical support' and 'creating data models.'

⚠ **Disagreement**: manual=`strategic` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['strategic', 'mixed', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, AI infrastructure, or any AI-related skill expectations.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mentions of AI coding tools (Copilot, Claude Code, Cursor), AI infrastructure, or AI-assisted development that the candidate should demonstrate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, GenAI applications, or AI-related candidate expectations.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or data quality framing identified in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: There is no mention of testing frameworks, data contracts, observability, data quality ownership, or quality assurance practices anywhere in the JD.

**Run 2:** `absent` ✗
> Quote: "No data quality, testing, or observability framework mentioned."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes documentation and compliance but does not mention testing, data quality frameworks, data contracts, observability practices, or quality ownership.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: No testing frameworks, data contracts, observability, or data quality practices appear in responsibilities; CI/CD is listed as a requirement but not framed as testing ownership.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Establishing documentation, version control, and data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: Data privacy compliance is mentioned as a concern, signaling operational and regulatory risk awareness, but the overall JD framing emphasizes capability delivery and adoption rather than preventing bad outcomes.

**Run 2:** `moderate` ✗
> Quote: "Establishing documentation, version control, and data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: Compliance is explicitly listed as a responsibility to establish, signaling organizational concern, but it is framed as infrastructure setup rather than prevention of bad outcomes to decision-makers or regulatory exposure.

**Run 3:** `moderate` ✗
> Quote: "Establishing documentation, version control, and data privacy compliance"
> Verified: ✓ found in JD
> Reasoning: Compliance is mentioned as a secondary concern, but overall framing emphasizes delivery and capability, not risk prevention or regulatory exposure.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
