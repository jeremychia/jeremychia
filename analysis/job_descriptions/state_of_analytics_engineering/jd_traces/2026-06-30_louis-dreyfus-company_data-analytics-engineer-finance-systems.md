# Trace: 2026-06-30_louis-dreyfus-company_data-analytics-engineer-finance-systems

## JD text (fed to classifier, Layer B stripped)

```
# Data & Analytics Engineer - Finance Systems — Louis Dreyfus Company

**URL:** https://www.ldc.com/careers/join-ldc/job-details/?id=ef073889-b345-48c9-afcc-b596cdeafbfa&trid=2d92f286-613b-4daf-9dfa-6340ffbecf73
**Location:** Sofia, Bulgaria
**Date Posted:** 2026-06-30

---

Data & Analytics Engineer - Finance Systems
Sofia, Bulgaria
Job Reference JR0096116
Professional Areas: Information Technology
Function: Information Technology
Contract Type: Permanent
Years of Work Experience: 0-3
Start date: 2026-06-01

Company Description
Louis Dreyfus Company is a leading merchant and processor of agricultural goods. Our activities span the entire value chain from farm to fork, across a broad range of business lines, we leverage our global reach and extensive asset network to serve our customers and consumers around the world. Structured as a matrix organization of six geographical regions and ten platforms, Louis Dreyfus Company is active in over 100 countries and employs approximately 18,000 people globally.

This role will have an impactful contribution to supporting and enhancing Louis Dreyfus Company's OneStream Enterprise Performance Management (EPM) platform, contributing to the delivery of accurate, reliable, and scalable financial planning, reporting, and performance management processes. Partnering with Finance, Data & Analytics teams, Business Process Owners, and external implementation partners, you will develop expertise in Enterprise Performance Management technologies while contributing to platform performance, data quality, governance, and operational stability.

Job Description
Brief:
Support LDC's OneStream-based Enterprise Performance Management platform from Sofia as a core technical engineer, delivering deep configuration, performance optimization, rule development, troubleshooting, and technical platform stability.
This role contributes directly to building the Enterprise Performance Management Center of Excellence, enabling scalable operations, technical autonomy, and long-term value creation across Daily P&L, Actuals, Forecasting, Group Reporting and future Enterprise performance management roadmap components.

The resource will join at a key moment (platform ramp-up and CoE build), work closely with experienced internal and external experts, and quickly take ownership of meaningful technical components that directly impact Finance performance and operational efficiency.

Main Responsibilities:
- Develop and enhance business rules, calculations, workflows, and data transformation processes.
- Support financial reporting, forecasting, planning, and performance management solutions.
- Troubleshoot platform issues and investigate data quality or integration challenges.
- Work with Finance teams to understand business requirements and translate them into technical solutions.
- Optimize system performance and improve reliability of financial processes.
- Participate in testing, releases, and deployments across development and production environments.
- Create technical documentation, support guides, and reusable development standards.
- Collaborate with global stakeholders, implementation partners, and internal technology teams.
- Contribute to the growth of the Enterprise Performance Management Center of Excellence and help build future best practices.

What Makes This Opportunity Different
- Join a newly established Center of Excellence and help shape its future.
- Gain expertise in a highly specialized and sought-after technology domain.
- Work directly with international Finance and Data teams.
- Receive mentorship from experienced OneStream consultants and platform experts.
- Exposure to large-scale global financial processes and enterprise systems.
- Opportunity to grow into senior engineering, architecture, or product ownership roles.

Experience
What We're Looking For

Education
Bachelor's or Master's degree in Computer Science, Information Systems, Engineering, Mathematics, Economics, Finance Technology, or …[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | high | high | 100% |
| collaboration_width | 3 | 4 | 4 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | mixed | recruiter | 33% |
| stakeholder_orientation | finance | finance | finance | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "delivering accurate, reliable, and scalable financial planning, reporting, and performance management processes"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes accuracy, reliability, quality, and stability as core values, with explicit signals around testing, data quality, documentation, and platform stability throughout the responsibilities.

**Run 2:** `rigour`
> Quote: "data quality, governance, and operational stability"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes correctness, reliability, governance, and testing as core expectations throughout, with no velocity or speed-related language.

**Run 3:** `rigour`
> Quote: "data quality, governance, and operational stability"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reliability, data quality, governance, testing, and operational stability throughout with no velocity signals like fast-paced or rapid delivery.

### domain_risk

**Run 1:** `high`
> Quote: "Daily P&L, Actuals, Forecasting, Group Reporting"
> Verified: ✓ found in JD
> Reasoning: P&L and financial reporting are explicitly named as core responsibility areas, indicating direct impact on financial reporting and regulatory compliance—the defining signal of high-risk domains.

**Run 2:** `high`
> Quote: "Daily P&L, Actuals, Forecasting, Group Reporting"
> Verified: ✓ found in JD
> Reasoning: Errors in P&L, actuals, and financial group reporting directly impact financial reporting and regulatory compliance.

**Run 3:** `high`
> Quote: "accurate, reliable, and scalable financial planning, reporting, and performance management processes"
> Verified: ✓ found in JD
> Reasoning: The role directly supports financial reporting, P&L, forecasting, and group reporting—core financial processes where data errors have immediate regulatory and audit impact.

### collaboration_width

**Run 1:** `3`
> Quote: "Finance; Data & Analytics teams; Business Process Owners"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named collaboration partners are explicitly identified: Finance (function), Data & Analytics teams (function), and Business Process Owners (role cohort).

**Run 2:** `4`
> Quote: "Partnering with Finance, Data & Analytics teams, Business Process Owners, and external implementation partners"
> Verified: ✓ found in JD
> Reasoning: Four distinct named partner groups are explicitly listed: Finance, Data & Analytics teams, Business Process Owners, and external implementation partners.

**Run 3:** `4`
> Quote: "Finance; Data & Analytics teams; Business Process Owners; external implementation partners"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions explicitly listed as collaboration partners in the role introduction.

⚠ **LLM inconsistency**: runs gave ['3', '4', '4']

### data_team_maturity

**Run 1:** `mid`
> Quote: "join at a key moment (platform ramp-up and CoE build)"
> Verified: ✓ found in JD
> Reasoning: The OneStream platform already exists with named components and operations, but the team is actively ramping up and building a new Center of Excellence, indicating growth from an existing foundation rather than greenfield or fully mature state.

**Run 2:** `mid`
> Quote: "join at a key moment (platform ramp-up and CoE build)"
> Verified: ✓ found in JD
> Reasoning: The EPM platform and Finance/Data teams already exist with experienced mentorship available, but the Center of Excellence is newly established and ramping up, indicating mid-stage growth rather than greenfield or mature operations.

**Run 3:** `mid`
> Quote: "join at a key moment (platform ramp-up and CoE build)"
> Verified: ✓ found in JD
> Reasoning: The OneStream platform already operates but the Center of Excellence is newly established, indicating active scaling rather than greenfield build or established steady state.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Support financial reporting, forecasting, planning, and performance management solutions"
> Verified: ✓ found in JD
> Reasoning: The brief section shows technical specificity (OneStream platform, named financial processes, specific technical activities), but the main responsibilities rely on generic action verbs ('support', 'develop', 'optimize') without deep technical context, indicating both hiring manager and recruiter input.

**Run 2:** `mixed`
> Quote: "Develop and enhance business rules, calculations, workflows, and data transformation processes"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about EPM components and rule development is mixed with generic responsibilities like 'Work with Finance teams to understand business requirements' and boilerplate collaboration language.

**Run 3:** `recruiter`
> Quote: "Work with Finance teams to understand business requirements and translate them into technical solutions."
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic recruiter boilerplate verbs—support, work with, collaborate, participate, troubleshoot—without technical depth about the actual platform components or methodologies.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation

**Run 1:** `finance`
> Quote: "Work with Finance teams to understand business requirements and translate them into technical solutions"
> Verified: ✓ found in JD
> Reasoning: Finance teams are explicitly named as the primary audience multiple times, with all major responsibilities centered on supporting financial reporting, P&L systems, and Finance operational performance.

**Run 2:** `finance`
> Quote: "Support financial reporting, forecasting, planning, and performance management solutions"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is delivering financial reporting, P&L, forecasting, and performance management solutions directly to Finance teams.

**Run 3:** `finance`
> Quote: "accurate, reliable, and scalable financial planning, reporting, and performance management processes"
> Verified: ✓ found in JD
> Reasoning: The role's core mission is delivering accurate financial reporting, forecasting, and P&L outcomes to the Finance function, not building data infrastructure for data consumers.

### autonomy_level

**Run 1:** `execution`
> Quote: "Work with Finance teams to understand business requirements and translate them into technical solutions"
> Verified: ✓ found in JD
> Reasoning: The role is framed as receiving requirements from Finance and delivering solutions within an existing platform structure, rather than setting direction or defining analytics strategy—characteristics of execution-oriented work.

**Run 2:** `execution`
> Quote: "Support LDC's OneStream-based Enterprise Performance Management platform from Sofia as a core technical engineer"
> Verified: ✓ found in JD
> Reasoning: While the role involves technical ownership of EPM components, the primary framing is support-oriented with strategic direction set by Finance requirements and established EPM strategy.

**Run 3:** `execution`
> Quote: "Work with Finance teams to understand business requirements and translate them into technical solutions."
> Verified: ✓ found in JD
> Reasoning: The primary responsibilities emphasize receiving and executing against requirements set by Finance teams and external experts, not setting direction or strategy for the platform.
