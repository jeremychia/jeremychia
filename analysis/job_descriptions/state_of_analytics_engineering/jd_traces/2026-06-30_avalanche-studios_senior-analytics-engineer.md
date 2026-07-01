# Trace: 2026-06-30_avalanche-studios_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Avalanche Studios Group

**URL:** https://avalanchestudios.com/jobs/557484be-0668-4a31-a06b-84a52edbdd51
**Location:** Stockholm, Sweden (hybrid)
**Date Posted:** 2026-06-30

---

Senior Analytics Engineer - Avalanche Studios Group

Company: Avalanche Studios Group
Job Title: Senior Analytics Engineer
Location: Stockholm (Södermalm office)
Salary: Not specified

Key Responsibilities

The role focuses on data architecture development. Candidates will 'extract, clean, and transform data from various sources' and collaborate with data scientists to provide reliable datasets. They must design data models capturing gaming KPIs and user profiles while ensuring 'accuracy, compliance, scalability, and long-term usability.'

Additional duties include maintaining documentation, monitoring pipelines for 'high availability and performance,' conducting code reviews, and staying current with industry trends.

Required Qualifications

Candidates need a Bachelor's or Master's degree in Computer Science or related field with 5+ years as an Analytics Engineer or similar role. Essential skills include:
- Strong SQL proficiency and experience with 'large data sets across multiple teams'
- ETL/ELT tools (DBT preferred)
- Cloud platforms (GCP preferred)
- 'Infrastructure as Code' experience

Culture Notes

The company emphasizes that underrepresented groups shouldn't hesitate to apply if they lack every requirement. Avalanche values 'drive to learn and interest in tackling challenges' over perfect credentials. The hybrid model requires office presence Mondays, Tuesdays, and Thursdays.

Application: Submit CV in English via their careers portal. No relocation assistance available.

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
| jd_authorship | recruiter | recruiter | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "ensuring 'accuracy, compliance, scalability, and long-term usability.'"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, compliance, reliability, and governance throughout, with no velocity or fast-paced language present.

**Run 2:** `rigour`
> Quote: "ensuring accuracy, compliance, scalability, and long-term usability"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities emphasize correctness, compliance, scalability, and reliability with no velocity-oriented language, indicating a rigour-focused orientation.

**Run 3:** `rigour`
> Quote: "ensuring 'accuracy, compliance, scalability, and long-term usability.'"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, compliance, scalability, and reliability with no mention of speed, iteration, or shipping velocity.

### domain_risk

**Run 1:** `moderate`
> Quote: "design data models capturing gaming KPIs and user profiles"
> Verified: ✓ found in JD
> Reasoning: The role operates in gaming analytics supporting business decisions, not regulatory, financial reporting, or compliance-critical domains.

**Run 2:** `moderate`
> Quote: "design data models capturing gaming KPIs and user profiles"
> Verified: ✓ found in JD
> Reasoning: Gaming analytics informs business decisions but does not involve financial reporting, regulatory compliance, or mission-critical systems, placing this in moderate risk.

**Run 3:** `moderate`
> Quote: "design data models capturing gaming KPIs and user profiles"
> Verified: ✓ found in JD
> Reasoning: Gaming analytics affect business decisions about player engagement and game design, but there is no explicit mention of financial reporting, regulatory compliance, or audit requirements.

### collaboration_width

**Run 1:** `1`
> Quote: "collaborate with data scientists"
> Verified: ✓ found in JD
> Reasoning: Only data scientists are explicitly named as a collaboration partner; other references like 'multiple teams' appear in requirements context, not as named collaborators.

**Run 2:** `1`
> Quote: "data scientists"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named partner function (data scientists) is identified in the JD.

**Run 3:** `1`
> Quote: "collaborate with data scientists"
> Verified: ✓ found in JD
> Reasoning: Only data scientists are explicitly named as a collaboration partner; other references are generic.

### data_team_maturity

**Run 1:** `mid`
> Quote: "maintaining documentation, monitoring pipelines for 'high availability and performance,' conducting code reviews"
> Verified: ✓ found in JD
> Reasoning: Responsibilities assume existing infrastructure, pipelines, and documentation in place, with multiple data roles present, but no signals of either greenfield establishment or mature multi-team platform scale.

**Run 2:** `mid`
> Quote: "collaborate with data scientists to provide reliable datasets"
> Verified: ✓ found in JD
> Reasoning: The existence of data scientists indicates an established data function that is expanding and hiring senior talent to develop and improve the data architecture.

**Run 3:** `mid`
> Quote: "monitoring pipelines for 'high availability and performance,'"
> Verified: ✓ found in JD
> Reasoning: The emphasis on maintaining and monitoring existing pipelines indicates established infrastructure beyond greenfield, but without explicit signals of large-scale specialization or multiple sub-teams.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "collaborate with data scientists to provide reliable datasets"
> Verified: ✓ found in JD
> Reasoning: Responsibilities are predominantly generic action-verb boilerplate typical of recruiter templates, with minimal technical specificity about tools, scale, or methodology.

**Run 2:** `recruiter`
> Quote: "maintaining documentation, monitoring pipelines for high availability and performance, conducting code reviews, and staying current with industry trends"
> Verified: ⚠ NOT found verbatim
> Reasoning: The accumulation of generic action verbs without specific application context to this role's actual work indicates recruiter authorship.

**Run 3:** `mixed`
> Quote: "design data models capturing gaming KPIs and user profiles while ensuring 'accuracy, compliance, scalability, and long-term usability.'"
> Verified: ✓ found in JD
> Reasoning: Domain specificity about gaming KPIs and scale context mix with generic quality language, suggesting both hiring manager and recruiter input.

⚠ **LLM inconsistency**: runs gave ['recruiter', 'recruiter', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "collaborate with data scientists to provide reliable datasets"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building reliable data infrastructure and supporting internal data consumers (data scientists and analytics users), not external commercial or product teams.

**Run 2:** `internal_data`
> Quote: "collaborate with data scientists to provide reliable datasets"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is serving the data function itself by building reliable datasets and data models for data scientists and analytics consumers.

**Run 3:** `internal_data`
> Quote: "collaborate with data scientists to provide reliable datasets"
> Verified: ✓ found in JD
> Reasoning: The primary audience is data scientists (other data team members), with responsibilities focused on building data infrastructure and models for internal consumption.

### autonomy_level

**Run 1:** `execution`
> Quote: "extract, clean, and transform data from various sources"
> Verified: ✓ found in JD
> Reasoning: The role is framed around delivery-focused execution tasks within defined scope rather than strategic direction-setting or defining the analytics function.

**Run 2:** `execution`
> Quote: "design data models capturing gaming KPIs and user profiles"
> Verified: ✓ found in JD
> Reasoning: While the role involves architectural design work, it executes within pre-defined business requirements (gaming KPIs) set by product and business teams.

**Run 3:** `execution`
> Quote: "design data models capturing gaming KPIs"
> Verified: ✓ found in JD
> Reasoning: The role executes against pre-defined KPI requirements rather than setting analytics strategy or defining what should be measured.

### ai_role
**Run 1:** `none` ✓
> Quote: "extract, clean, and transform data from various sources; collaborate with data scientists"
> Reasoning: Standard data engineering responsibilities with no AI tool usage signals or AI infrastructure-building responsibilities.

**Run 2:** `none` ✓
> Quote: "extract, clean, and transform data from various sources; collaborate with data scientists to provide reliable datasets"
> Reasoning: Phrases describe generic data engineering without AI tool or infrastructure signals.


### testing_framing
**Run 1:** `absent` ✓
> Quote: "collaborate with data scientists to provide reliable datasets"
> Reasoning: Quality and reliability are outcomes but no explicit testing ownership or quality practice responsibility language.

**Run 2:** `absent` ✓
> Quote: "No quality ownership verbs (own, ensure, define, implement, establish) paired with testing or data contracts"
> Reasoning: Work framed as delivery/execution with no testing responsibility or tool stack signal.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Rigour signals dominate — accuracy, compliance, scalability, high availability, monitoring"
> Reasoning: Operational reliability concerns (monitoring, high availability, SLOs) dominate; compliance framed around data usability, not regulatory/audit.

**Run 2:** `high` ✗
> Quote: "accuracy, compliance, scalability, and long-term usability; rigour signals dominate with zero velocity phrases"
> Reasoning: Compliance and regulatory trustworthiness frame the role as primary constraint, not operational reliability fear.

⚠ **LLM inconsistency**: runs gave ['moderate', 'high']
