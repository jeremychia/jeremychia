# Trace: 2026-07-01_hse24_junior-expert-bi-analytics

## JD text (fed to classifier, Layer B stripped)

```
# Junior Expert BI & Analytics — HSE24

**URL:** https://karriere-hse24-portal.rexx-systems.com/Junior-Expert-BI-Analytics-mwd-de-j3667.html?sid=724ab8567cdcfb9bb38652d88b99105f
**Location:** Munich, Germany (Hybrid, 2 days on-site)
**Date Posted:** 2026-07-01

---

Junior Expert BI & Analytics (m/w/d) at HSE24 / Home Shopping Europe GmbH

About the Company
Home Shopping Europe GmbH is a leading live commerce provider in Europe, operating as a media platform offering entertainment-focused shopping. They feature curated products across fashion, jewellery, beauty, wellness, household, and home & living categories, engaging audiences through TV, online shop, and social media channels.

Role Summary
The position involves designing, developing, and optimising modern BI and analytics solutions to enable data-driven decision-making.

Key Responsibilities
- Conceptualise and optimise BI solutions and create KPIs, semantic models, reports, and dashboards
- Translate business requirements into analytics deliverables
- Develop automated self-service BI solutions with consistent KPI definitions
- Build and maintain data models with DBT and Snowflake using dimensional modelling
- Apply modern development standards including clean code and test-driven development
- Manage code via Git with structured branching strategies and support CI/CD processes
- Collaborate with data platform teams and business units on optimisation

Required Qualifications
- Relevant degree or comparable qualification with multi-year BI/Analytics experience
- Strong expertise with tools like Power BI, Tableau, or Google Looker Studio
- Very good SQL knowledge, solid Python skills and practical experience with DBT
- Data modelling and reporting technology expertise
- Fluent English; German language skills preferred
- Willingness to work two days weekly on-site at their campus

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 2 | 2 | 1 | 1 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | mixed | execution | execution | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | tool_listed | responsibility | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | none | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize test-driven development, clean code, CI/CD, and structured branching strategies as core expectations, with no velocity-oriented language.

**Run 2:** `rigour` ✓
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development, clean code, CI/CD processes, and structured Git branching are core responsibilities with no countervailing velocity signals.

**Run 3:** `rigour` ✓
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize structured development practices, testing discipline, and code quality management with no mention of speed, iteration, or rapid delivery.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "enable data-driven decision-making"
> Verified: ✓ found in JD
> Reasoning: A live commerce platform's data errors affect business decisions but not financial reporting, regulatory compliance, or public-facing product safety.

**Run 2:** `moderate` ✓
> Quote: "Home Shopping Europe GmbH is a leading live commerce provider in Europe, operating as a media platform offering entertainment-focused shopping"
> Verified: ✓ found in JD
> Reasoning: E-commerce and retail operations involve business decision-making but lack regulatory, compliance, or financial reporting signals that would indicate high domain risk.

**Run 3:** `moderate` ✓
> Quote: "enable data-driven decision-making"
> Verified: ✓ found in JD
> Reasoning: The role supports business intelligence and internal decision-making in a retail/commerce platform with no signals of financial reporting, compliance, or regulatory exposure.

### collaboration_width
**Manual:** `2`

**Run 1:** `2` ✓
> Quote: "data platform teams; business units"
> Verified: ✓ found in JD
> Reasoning: Two distinct named partner groups are explicitly listed in the collaboration responsibility.

**Run 2:** `1` ✗
> Quote: "Collaborate with data platform teams and business units on optimisation"
> Verified: ✓ found in JD
> Reasoning: Only 'data platform teams' qualifies as a named function; 'business units' is too generic to count.

**Run 3:** `1` ✗
> Quote: "Collaborate with data platform teams and business units on optimisation"
> Verified: ✓ found in JD
> Reasoning: Only 'data platform teams' counts as a named team function; 'business units' is a generic reference and does not count per classification rules.

⚠ **Disagreement**: manual=`2` vs LLM majority=`1`

⚠ **LLM inconsistency**: runs gave ['2', '1', '1']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Collaborate with data platform teams and business units on optimisation"
> Verified: ✓ found in JD
> Reasoning: The existence of a named data platform team and the responsibility to optimize existing tools (DBT, Snowflake) indicates an established function beyond early stage.

**Run 2:** `mid` ✓
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: Named tools (DBT, Snowflake) appear in responsibilities with specific technical methodology context, and the existence of dedicated data platform teams indicates an established function scaling.

**Run 3:** `mid` ✓
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: Named tools (DBT, Snowflake) appear in responsibilities with specific methodology context, and a separate data platform team exists, indicating infrastructure is established but not at massive scale.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling; Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: Specific technical details (DBT, Snowflake, dimensional modelling) suggest hiring manager input, but generic collaboration language (translate requirements) indicates recruiter involvement.

**Run 2:** `mixed` ✗
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling; Manage code via Git with structured branching strategies and support CI/CD processes"
> Verified: ✓ found in JD
> Reasoning: Specific tool and methodology references (DBT, Snowflake, dimensional modelling, Git CI/CD) are mixed with generic boilerplate verbs like 'Translate business requirements' and 'Collaborate'.

**Run 3:** `mixed` ✗
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling; Manage code via Git with structured branching strategies and support CI/CD processes"
> Verified: ✓ found in JD
> Reasoning: Technical specificity appears in tool selection and process details (DBT, Snowflake, Git, CI/CD, dimensional modelling) alongside boilerplate phrasing (translate requirements, collaborate with stakeholders).

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Develop automated self-service BI solutions with consistent KPI definitions"
> Verified: ✓ found in JD
> Reasoning: The emphasis on self-serve analytics and collaboration with the data platform team indicates the primary audience is data consumers and the data function itself.

**Run 2:** `internal_data` ✓
> Quote: "Develop automated self-service BI solutions with consistent KPI definitions"
> Verified: ✓ found in JD
> Reasoning: The primary deliverables (dashboards, KPIs, semantic models, self-serve BI infrastructure) serve internal analytics consumers and the data platform function rather than commercial, product, or finance-specific stakeholders.

**Run 3:** `internal_data` ✓
> Quote: "Develop automated self-serve BI solutions with consistent KPI definitions"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary focus is building analytics infrastructure and self-service tooling for internal data consumers, not commercial, product, or finance-specific objectives.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Conceptualise and optimise BI solutions and create KPIs; Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: Strategic language (conceptualise, optimise, create KPIs) coexists with execution framing (translate business requirements), indicating both direction-setting and delivery roles.

**Run 2:** `execution` ✗
> Quote: "Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: The role receives scoped direction (business requirements) and executes delivery against those priorities, with no strategic direction-setting or ownership language.

**Run 3:** `execution` ✗
> Quote: "Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes delivering against defined requirements and collaborating on direction set by others, with no signals of strategic ownership or agenda-setting.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, AI-assisted coding, or AI-ready infrastructure anywhere in the job description.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, or AI-enabled data infrastructure expectations.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, coding assistants, generative AI capabilities, or AI-enablement responsibilities.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `tool_listed` ✗
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development is mentioned as a practice to apply rather than as a testing framework or standard the candidate owns or defines.

**Run 2:** `responsibility` ✗
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development is framed as an applied responsibility the candidate owns, not merely a tool in a requirements list.

**Run 3:** `responsibility` ✗
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development is explicitly listed as a responsibility the candidate should implement, not merely as a tool in a requirements list.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'responsibility', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Quality and reliability are concerns (through TDD and CI/CD) but secondary to delivery, with no explicit risk language around compliance, bad data reaching stakeholders, or regulatory exposure.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed entirely around building and optimising analytics capabilities without mention of risk, compliance, data accuracy concerns, or preventing bad outcomes.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed entirely in terms of capability delivery and optimization with no language around risk, compliance, prevention, or stakeholder trust.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'none']
