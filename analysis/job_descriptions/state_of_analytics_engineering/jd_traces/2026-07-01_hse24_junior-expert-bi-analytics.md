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

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 1 | 1 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | mixed | mixed | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | none | none | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes test-driven development, CI/CD processes, structured branching strategies, and clean code—core quality and governance signals with no velocity language present.

**Run 2:** `rigour`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize development practices (clean code, test-driven development), structured process (Git branching strategies, CI/CD), and consistency (KPI definitions) rather than speed or delivery pace.

**Run 3:** `rigour`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, code quality, CI/CD processes, and structured governance (branching strategies) with zero velocity signals, making rigour the dominant orientation.

### domain_risk

**Run 1:** `moderate`
> Quote: "designing, developing, and optimising modern BI and analytics solutions to enable data-driven decision-making"
> Verified: ✓ found in JD
> Reasoning: The role supports business decision-making in a live commerce context without explicit financial reporting, compliance, or regulatory language, placing it in moderate risk.

**Run 2:** `moderate`
> Quote: "designing, developing, and optimising modern BI and analytics solutions to enable data-driven decision-making"
> Verified: ✓ found in JD
> Reasoning: This is e-commerce/retail media analytics without explicit financial reporting, compliance, or regulatory language; data errors affect business decisions but lack the high-risk framing of fintech or regulated sectors.

**Run 3:** `moderate`
> Quote: "enable data-driven decision-making"
> Verified: ✓ found in JD
> Reasoning: Live commerce (e-commerce) role with no financial reporting, compliance, or regulatory language; data errors affect business decisions but not regulatory or financial risk.

### collaboration_width

**Run 1:** `1`
> Quote: "data platform teams"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named team—data platform teams—is mentioned as a collaboration partner; business units is generic.

**Run 2:** `1`
> Quote: "data platform teams"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named team function is listed; 'business units' is too generic to count as a named partner team.

**Run 3:** `1`
> Quote: "data platform teams"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named team ('data platform teams') is identified as a collaboration partner; 'business units' is too generic to count as a named function.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in responsibilities (DBT, Snowflake) with specific context (dimensional modelling), and the existence of a separate data platform team implies an established but still-growing data function.

**Run 2:** `mid`
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: Named tools (DBT, Snowflake) appear in responsibilities with specific context, collaboration with data platform teams implies existing multi-role structure, and the focus is on scaling and optimizing existing capabilities rather than building from zero.

**Run 3:** `mid`
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, Snowflake) appear in responsibilities alongside established practices (dimensional modelling, self-serve solutions) and an existing data platform team, indicating a growing established function rather than greenfield startup.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: The JD shows technical specificity (DBT, Snowflake, dimensional modelling, TDD, Git branching) alongside generic action verbs (conceptualise, optimise, translate), indicating both hiring manager and recruiter input.

**Run 2:** `mixed`
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling; Translate business requirements into analytics deliverables"
> Verified: ⚠ NOT found verbatim
> Reasoning: Some responsibilities show technical specificity (DBT, Snowflake, dimensional modelling, Git strategies, CI/CD) while others use generic action verbs (translate, collaborate, support) typical of recruiter boilerplate.

**Run 3:** `mixed`
> Quote: "Build and maintain data models with DBT and Snowflake using dimensional modelling"
> Verified: ✓ found in JD
> Reasoning: Technical specificity around dbt, Snowflake, and dimensional modelling indicates hiring manager input, but generic collaboration and translation language suggests recruiter contributions.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Develop automated self-service BI solutions with consistent KPI definitions"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building self-serve analytics infrastructure and semantic models for the data platform, targeting data consumers and the analytics function.

**Run 2:** `internal_data`
> Quote: "Develop automated self-service BI solutions with consistent KPI definitions"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is building self-service analytics infrastructure for internal data consumers and supporting the data platform team, not serving GTM, product experimentation, or financial reporting stakeholders.

**Run 3:** `internal_data`
> Quote: "Develop automated self-service BI solutions with consistent KPI definitions"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building data models and self-service analytics infrastructure for internal consumption rather than serving commercial, product, or finance stakeholders directly.

### autonomy_level

**Run 1:** `execution`
> Quote: "Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: The role centers on executing delivered business requirements and maintaining existing models rather than setting analytics strategy or defining the roadmap.

**Run 2:** `execution`
> Quote: "Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: The role is framed around receiving business requirements and delivering solutions within established frameworks (applying standards, using specified tools) rather than defining direction or setting strategy.

**Run 3:** `execution`
> Quote: "Translate business requirements into analytics deliverables"
> Verified: ✓ found in JD
> Reasoning: The role receives business requirements and delivers against them; autonomy is limited to execution tactics within a given scope rather than defining analytics strategy or priorities.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD lists traditional BI and data tools (Power BI, Tableau, DBT, Snowflake, SQL, Python) with no expectation of AI coding tools, AI data infrastructure, or GenAI application skills.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted workflows, or AI data infrastructure expectations for the candidate.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI tools, AI-assisted coding, or AI-related responsibilities anywhere in the JD.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development is listed as a key responsibility the candidate will apply, not merely as a tool in a skills list.

**Run 2:** `responsibility`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development is framed as an active practice the candidate applies in their work, not merely listed as a tool requirement.

**Run 3:** `responsibility`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Test-driven development is framed as a responsibility the candidate applies rather than a tool listed in requirements, indicating ownership of testing practice in their work.

### loss_aversion_framing

**Run 1:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role around enabling decisions and optimizing solutions, with no emphasis on compliance risk, data reliability concerns, or preventing bad outcomes.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is framed entirely around delivery and capability building (optimize, develop, create) with no risk, compliance, or data-trust language that would signal loss aversion.

**Run 3:** `moderate`
> Quote: "Apply modern development standards including clean code and test-driven development"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and quality are embedded through best practices (TDD, clean code, CI/CD) but without explicit risk, compliance, or stakeholder trust language, indicating reliability is valued without fear-based framing.

⚠ **LLM inconsistency**: runs gave ['none', 'none', 'moderate']
