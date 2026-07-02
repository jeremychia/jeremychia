# Trace: 2026-07-01_entain_analytics-engineer-bi

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer (BI) — Entain

**URL:** https://jobs.smartrecruiters.com/Entain/744000131097774-analytics-engineer-bi-?trid=2d92f286-613b-4daf-9dfa-6340ffbecf73
**Location:** Not stated in JD
**Date Posted:** 2026-07-01

---

Analytics Engineer (BI) at Entain

Company Description
Sports betting, gaming and interactive entertainment is changing, and we're leading that change. By putting people first. The company emphasises innovation, technology, and people-focused culture.

Role Summary
This position operates within the Data & Analytics department as a full-time role. The Analytics Engineer translates data into actionable insights for business stakeholders through analysis, dashboards, and reporting.

Key Responsibilities
- Extract and analyze large datasets from Snowflake using SQL to generate meaningful insights
- Design and maintain dbt models for the analytics semantic layer
- Build scalable dashboards and reporting solutions
- Translate business questions into structured analysis
- Deliver ad-hoc analysis to support decision-making
- Contribute to self-serve analytics capabilities
- Apply version control practices using Git
- Support team members in dbt and data modeling
- Collaborate with Data Engineering to improve data quality

Essential Requirements
- Degree in Statistics, Economics, Mathematics, Computer Science, or related discipline
- Advanced SQL skills, with the ability to query, optimise, and model large datasets in Snowflake or similar platforms
- Practical experience with dbt, Git workflows, data modeling principles
- Proficiency in Excel

Desired Qualifications
- Experience with BI tools like Looker, Tableau, or Power BI
- Background in sports, iGaming, statistical analysis, or marketing platforms such as Google Analytics

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
| stakeholder_orientation | internal_data | mixed | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | absent | absent | 100% |
| loss_aversion_framing | moderate | none | none | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize structured practices (dbt models, version control, data modeling principles) and quality improvement without any velocity-oriented language like 'fast-paced' or 'ship quickly'.

**Run 2:** `rigour`
> Quote: "Apply version control practices using Git"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes structured work and quality practices (version control, dbt models, data modeling) over speed, with no fast-paced or velocity language present.

**Run 3:** `rigour`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes structured analysis, data quality, and scalable technical infrastructure with no velocity language (no 'fast-paced', 'ship', or 'MVP' signals), placing it firmly in the rigour orientation.

### domain_risk

**Run 1:** `moderate`
> Quote: "translate data into actionable insights for business stakeholders through analysis, dashboards, and reporting"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role supports business decision-making but without explicit financial reporting, compliance, regulatory, or mission-critical language.

**Run 2:** `moderate`
> Quote: "Build scalable dashboards and reporting solutions"
> Verified: ✓ found in JD
> Reasoning: While the sports betting sector is regulated and high-risk, the JD describes generic analytics and dashboards work without explicit financial reporting, compliance, or regulatory language, so textual signals indicate moderate risk.

**Run 3:** `moderate`
> Quote: "Translate business questions into structured analysis"
> Verified: ✓ found in JD
> Reasoning: The role is general business analytics supporting stakeholder decisions without explicit financial reporting, compliance, or regulatory framing, despite the company operating in a regulated gaming sector.

### collaboration_width

**Run 1:** `1`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: Only one named partner team (Data Engineering) is explicitly identified; business stakeholders and team members are not named collaborative teams.

**Run 2:** `1`
> Quote: "Data Engineering"
> Verified: ✓ found in JD
> Reasoning: Only Data Engineering is explicitly named as a collaboration partner; 'business stakeholders' is too generic to count as a distinct named team.

**Run 3:** `1`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: Only Data Engineering is explicitly named as a collaboration partner; other references are generic ('business stakeholders', 'team members').

### data_team_maturity

**Run 1:** `mid`
> Quote: "Design and maintain dbt models for the analytics semantic layer"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, Snowflake) are already deployed and the role maintains and extends them, indicating an established data function in growth phase rather than early-stage.

**Run 2:** `mid`
> Quote: "Contribute to self-serve analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, BI platforms) are in active use with platform infrastructure being built, indicating a mid-stage team with existing tooling but not yet mature scale.

**Run 3:** `mid`
> Quote: "Design and maintain dbt models for the analytics semantic layer"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (Snowflake, dbt, dashboards, self-serve analytics) with multiple implied data professionals suggest an existing, functioning data team growing beyond early stage but not explicitly described as mature/established.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Design and maintain dbt models for the analytics semantic layer"
> Verified: ✓ found in JD
> Reasoning: Technical specificity appears in named tools and architectural concepts (dbt semantic layer, Snowflake extraction, Git version control) alongside generic support language (deliver ad-hoc analysis, support team members).

**Run 2:** `mixed`
> Quote: "Design and maintain dbt models for the analytics semantic layer"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about Snowflake, dbt, and semantic layer demonstrates hiring manager knowledge, but generic boilerplate verbs ('translate,' 'deliver') indicate recruiter involvement.

**Run 3:** `mixed`
> Quote: "Extract and analyze large datasets from Snowflake using SQL to generate meaningful insights; Support team members in dbt and data modeling"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical context (Snowflake, dbt semantic layer, version control with Git) mixes with generic collaboration language ('translate business questions', 'support decision-making'), indicating input from both practitioner and recruiter.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Contribute to self-serve analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes building analytics infrastructure (dbt models, semantic layer, self-serve dashboards, team support) for internal data consumers rather than serving external commercial, product, or finance stakeholders.

**Run 2:** `mixed`
> Quote: "translates data into actionable insights for business stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role simultaneously serves external business stakeholders (dashboards, insights, analysis) and internal data platform consumers (dbt models, self-serve capabilities, supporting team members).

**Run 3:** `internal_data`
> Quote: "Contribute to self-serve analytics capabilities"
> Verified: ✓ found in JD
> Reasoning: The emphasis on self-serve analytics and supporting team members in dbt/data modeling indicates the role primarily serves data consumers and the data function itself, not specific business functions like GTM, Product, or Finance.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'mixed', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Support team members in dbt and data modeling"
> Verified: ✓ found in JD
> Reasoning: All responsibilities use execution-oriented verbs (support, deliver, contribute, apply) without strategic direction-setting language like define, establish, or lead.

**Run 2:** `execution`
> Quote: "Translate business questions into structured analysis"
> Verified: ✓ found in JD
> Reasoning: Verbs throughout (extract, translate, deliver, support, contribute) indicate the role receives work from others and executes against defined requests rather than setting direction.

**Run 3:** `execution`
> Quote: "Deliver ad-hoc analysis to support decision-making"
> Verified: ✓ found in JD
> Reasoning: All responsibilities use execution verbs ('extract', 'deliver', 'support', 'contribute', 'maintain') with no strategic ownership language ('define', 'own', 'lead', 'architect'), indicating the role executes work scoped by others.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No AI tools, coding assistance, GenAI infrastructure, or AI literacy expectations appear anywhere in the job description.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, or AI infrastructure expectations for the candidate.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI-assisted coding, coding agents, or AI infrastructure; the company operates in gaming/betting but the JD describes standard analytics work with no AI expectation.

### testing_framing

**Run 1:** `absent`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is mentioned as a collaborative concern but no testing frameworks, data contracts, observability practices, or quality ownership are explicitly framed.

**Run 2:** `absent`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality improvement is mentioned but framed as collaborative rather than as an owned responsibility, and no testing frameworks or practices are explicitly described.

**Run 3:** `absent`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality appears as a collaborative outcome with Data Engineering rather than as an owned testing practice or methodology the candidate defines; no testing frameworks, data contracts, or observability tools are named.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Collaborate with Data Engineering to improve data quality"
> Verified: ✓ found in JD
> Reasoning: The role shows concern for operational data quality and reliability but without compliance, regulatory, or stakeholder-trust language that would indicate high loss-aversion framing.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role around analytics delivery and capabilities without language about risk management, compliance, reliability, or preventing bad outcomes.

**Run 3:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is entirely framed in terms of capability and delivery (insights, dashboards, analysis) with no regulatory, compliance, reliability, or risk-mitigation language present.

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'none']
