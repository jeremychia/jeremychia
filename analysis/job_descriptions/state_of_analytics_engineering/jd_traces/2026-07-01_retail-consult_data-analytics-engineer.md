# Trace: 2026-07-01_retail-consult_data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data & Analytics Engineer — Retail Consult

**URL:** https://www.linkedin.com/jobs/view/4435147982/
**Location:** Maia, Porto, Portugal
**Date Posted:** 2026-07-01

---

Data & Analytics Engineer (PostgreSQL & Power BI) at Retail Consult

Location: Maia, Porto, Portugal
Seniority Level: Mid-Senior
Employment Type: Full-time

Key Responsibilities
The role involves collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions. Core duties include designing data architectures, optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines.

Requirements
- Experience with Data Lakes and Data Warehouses
- Strong SQL expertise
- Proficiency in Power BI dashboard development
- General understanding of cloud fundamentals, including compute, storage, networking, and identity/access management
- Fluent English is mandatory

Benefits
Health insurance, mobile allowance, flexible working hours, extra days off, and a wellbeing program. Professional development includes Training and Mentoring/Talent Development programs.

Application: Submit CV at www.retail-consult.com/en/work-with-us/ or jobs@retail-consult.com

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 4 | 4 | 4 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | recruiter | recruiter | recruiter | 100% |
| stakeholder_orientation | mixed | mixed | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | absent | absent | 100% |
| loss_aversion_framing | none | moderate | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reliability and quality as core expectations with no language about speed, iteration, or fast-paced delivery.

**Run 2:** `rigour`
> Quote: "scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reliability and high-quality as core expectations without any velocity language like fast-paced or rapid delivery.

**Run 3:** `rigour`
> Quote: "transform business needs into scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reliability and high-quality standards as core values with no velocity or speed-to-market language.

### domain_risk

**Run 1:** `moderate`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: While Finance is a named stakeholder, the JD contains no language about financial reporting, compliance, regulatory requirements, or audit that would elevate to high risk.

**Run 2:** `moderate`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: Finance is mentioned but the JD lacks explicit financial reporting, regulatory, or compliance language that would signal high risk.

**Run 3:** `moderate`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple business functions including Finance but contains no mention of financial reporting, compliance, or regulatory requirements that would indicate high risk.

### collaboration_width

**Run 1:** `4`
> Quote: "Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct business functions are explicitly named as collaboration partners.

**Run 2:** `4`
> Quote: "Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly listed as collaboration partners in the responsibilities.

**Run 3:** `4`
> Quote: "Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named stakeholder teams are explicitly listed in the responsibilities section.

### data_team_maturity

**Run 1:** `mid`
> Quote: "optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines"
> Verified: ✓ found in JD
> Reasoning: Named tools and frameworks in responsibilities with optimization and management context indicates an established data function growing beyond initial setup.

**Run 2:** `mid`
> Quote: "optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines"
> Verified: ✓ found in JD
> Reasoning: Named tools and systems in responsibilities suggest an established data function being optimized and extended rather than built from scratch.

**Run 3:** `mid`
> Quote: "optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines"
> Verified: ✓ found in JD
> Reasoning: Named tools are present in actual role responsibilities indicating existing infrastructure, but no mention of scaling or established sub-teams suggests mid-stage maturity.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "designing data architectures, optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs with tool names but no specific technical context, scale, methodology, or domain problem that would signal hands-on authorship.

**Run 2:** `recruiter`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs like collaborating and transform business needs without specific methodological detail, scale context, or technical depth suggest recruiter authorship.

**Run 3:** `recruiter`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities rely on generic, boilerplate phrasing ('transform business needs', 'scalable solutions') without the technical context or day-to-day detail that would come from someone doing the job.

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple distinct stakeholder categories (finance, commercial, internal operations) with equal apparent weight and no primary audience emphasis.

**Run 2:** `mixed`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams"
> Verified: ✓ found in JD
> Reasoning: Multiple distinct stakeholder groups are listed with equal emphasis and no indication of which is the primary audience.

**Run 3:** `internal_data`
> Quote: "designing data architectures, optimising PostgreSQL databases, developing Power BI dashboards, and managing ETL/ELT pipelines"
> Verified: ✓ found in JD
> Reasoning: Core responsibilities focus on data infrastructure and platform work that serves multiple teams' data consumption needs rather than a specific business function.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: The role is framed as receiving and fulfilling stakeholder needs rather than defining direction, strategy, or roadmap.

**Run 2:** `execution`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams to transform business needs"
> Verified: ✓ found in JD
> Reasoning: The framing of collaborating to transform business needs suggests the role executes against requirements defined by others rather than setting strategic direction independently.

**Run 3:** `execution`
> Quote: "collaborating with Finance, Sales, HR, and Project Management teams to transform business needs into scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: The role frame emphasizes collaborating with stakeholders to transform their stated needs rather than defining strategic direction independently.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no requirement, expectation, or mention of any AI tool, AI-assisted coding, or AI infrastructure capability.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-ready data infrastructure, or AI skills expected of the candidate.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI tools, AI-assisted coding, or AI infrastructure expectations for the candidate.

### testing_framing

**Run 1:** `absent`
> Quote: "No testing or data quality signal explicitly framed as a practice."
> Verified: ⚠ NOT found verbatim
> Reasoning: While 'high-quality' appears as an outcome goal, no testing practice, data quality framework, or observability requirement is explicitly stated as a responsibility.

**Run 2:** `absent`
> Quote: "high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: Quality is mentioned as a value but there is no reference to testing practices, data quality frameworks, observability tools, or testing ownership.

**Run 3:** `absent`
> Quote: "No testing or data quality signal anywhere in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: While 'reliable' and 'high-quality' appear as desired solution attributes, there is no mention of testing frameworks, data quality practices, or tools that the candidate would own.

### loss_aversion_framing

**Run 1:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is framed entirely around capabilities and delivery (designing, optimising, managing) with no emphasis on preventing negative outcomes, compliance risk, or stakeholder trust.

**Run 2:** `moderate`
> Quote: "reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: Reliability is mentioned as a capability to achieve but without explicit risk language around compliance, audit, or preventing bad data reaching stakeholders.

**Run 3:** `moderate`
> Quote: "scalable, reliable, and high-quality data solutions"
> Verified: ✓ found in JD
> Reasoning: Operational reliability is a concern in the language but there is no framing around preventing compliance failures or regulatory risk, typical of moderate risk aversion.

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'moderate']
