# Trace: 2026-07-01_darwin_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Darwin (via Aplitrak)

**URL:** https://www.aplitrak.com/?adid=R2VvZmZyZXkuS25hcHAuNDgwNjIuMTU1MEBkYXJ3aW4uYXBsaXRyYWsuY29t
**Location:** Amsterdam, Netherlands (Hybrid)
**Date Posted:** 2026-07-01
**Salary:** 6,500–7,250 EUR

---

Senior Analytics Engineer - Amsterdam International Organisation (via Darwin/Aplitrak)

Position Overview
The role involves leading the design and build of a brand-new analytics platform for an Amsterdam-based international organization. This is a rare greenfield opportunity where you'll be the first dedicated Analytics Engineer within the business.

Key Responsibilities
- Take ownership of platform architecture, data modelling standards, and engineering best practices
- Build a modern cloud-based data platform that will support the organisation's next phase of growth
- Design and build from scratch rather than maintaining existing systems

Required Qualifications
- Commercial experience designing and building modern analytics or data platforms
- Strong experience with Databricks and/or Snowflake
- Excellent SQL and Python skills
- Experience with cloud-based data platforms (Azure experience beneficial)
- Knowledge of modern data modelling and semantic layer design
- Exposure to BI tools such as Tableau or Power BI
- Advantageous: experience working with Data Science or Machine Learning teams
- Proactive approach with confidence to influence technical decisions

Compensation & Benefits
- Salary: €6,500–€7,250 gross per month
- Annual bonus opportunity
- 27 days annual leave plus holiday allowance
- Pension contribution
- Hybrid working arrangement
- Long-term growth opportunities within a collaborative, people-first culture

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 0 | 0 | 1 | 33% |
| data_team_maturity | early | early | early | 100% |
| jd_authorship | mixed | recruiter | hiring_manager | 0% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | strategic | strategic | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | absent | absent | 100% |
| loss_aversion_framing | none | none | none | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize architecture, standards, and best practices rather than speed or iteration, with no velocity language present.

**Run 2:** `rigour`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The emphasis on standards and best practices signals a rigour orientation focused on correctness and engineering excellence.

**Run 3:** `rigour`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, standards, and best practices over speed or iteration, with no velocity signals present.

### domain_risk

**Run 1:** `moderate`
> Quote: "Build a modern cloud-based data platform that will support the organisation's next phase of growth"
> Verified: ✓ found in JD
> Reasoning: The role builds general business analytics infrastructure to support organizational growth, which carries moderate risk of impacting business decisions without explicit regulatory or financial consequences.

**Run 2:** `moderate`
> Quote: "Amsterdam-based international organization"
> Verified: ✓ found in JD
> Reasoning: Without explicit financial, compliance, or regulatory language, and absent sector context in the JD, domain risk defaults to moderate for a business organization building analytics.

**Run 3:** `moderate`
> Quote: "Build a modern cloud-based data platform that will support the organisation's next phase of growth"
> Verified: ✓ found in JD
> Reasoning: The JD describes strategic platform infrastructure without explicit financial reporting, compliance, or regulatory language that would signal high risk.

### collaboration_width

**Run 1:** `0`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes individual ownership with no named partner teams identified in core responsibilities.

**Run 2:** `0`
> Quote: "None identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities section contains no explicitly named partner teams or functions.

**Run 3:** `1`
> Quote: "experience working with Data Science or Machine Learning teams"
> Verified: ✓ found in JD
> Reasoning: Data Science/Machine Learning teams are explicitly named as a relevant collaboration domain in the qualifications section.

⚠ **LLM inconsistency**: runs gave ['0', '0', '1']

### data_team_maturity

**Run 1:** `early`
> Quote: "This is a rare greenfield opportunity where you'll be the first dedicated Analytics Engineer within the business."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly states this is a greenfield platform build with no existing infrastructure, and the candidate is the first dedicated analytics hire.

**Run 2:** `early`
> Quote: "first dedicated Analytics Engineer within the business"
> Verified: ✓ found in JD
> Reasoning: The explicit description of being the first dedicated analytics hire clearly signals an early-stage data function.

**Run 3:** `early`
> Quote: "This is a rare greenfield opportunity where you'll be the first dedicated Analytics Engineer within the business"
> Verified: ✓ found in JD
> Reasoning: The explicit statement of being the first analytics engineer and greenfield opportunity clearly signals an early-stage data function being established.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical domains (platform architecture, data modelling standards) mixed with generic action verbs (take ownership).

**Run 2:** `recruiter`
> Quote: "Strong experience with Databricks and/or Snowflake"
> Verified: ✓ found in JD
> Reasoning: Tools are listed without specific context about application, scale, or methodology, which is typical of recruiter-written JDs lacking hands-on experience.

**Run 3:** `hiring_manager`
> Quote: "Strong experience with Databricks and/or Snowflake; Knowledge of modern data modelling and semantic layer design"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain specific technical methodology names and platform tools with precise context that only someone performing this work would specify.

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Build a modern cloud-based data platform"
> Verified: ✓ found in JD
> Reasoning: The role focuses on infrastructure and platform building for internal analytics consumption rather than serving commercial, product, finance, or other specific business functions.

**Run 2:** `internal_data`
> Quote: "Build a modern cloud-based data platform that will support the organisation's next phase of growth"
> Verified: ✓ found in JD
> Reasoning: The role is framed around building data infrastructure and platform foundations rather than serving a specific business function.

**Run 3:** `internal_data`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The emphasis on building platform architecture and semantic layer design indicates the role is establishing analytics infrastructure for internal data consumers rather than serving a specific business function.

### autonomy_level

**Run 1:** `strategic`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The use of ownership and design verbs, combined with the greenfield context, positions the role as setting the direction for analytics infrastructure rather than executing defined work.

**Run 2:** `strategic`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The ownership framing and responsibility for defining architecture and standards signals strategic autonomy in shaping the analytics platform.

**Run 3:** `strategic`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices; Design and build from scratch"
> Verified: ⚠ NOT found verbatim
> Reasoning: The language of 'take ownership' combined with 'design and build from scratch' indicates authority to define direction and shape the analytics platform strategy.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no expectation for the candidate to use AI coding tools or build AI-ready data infrastructure.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: While Data Science team collaboration is mentioned as advantageous, there is no expectation for the candidate to use AI tools or build AI infrastructure.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no references to AI coding tools, AI-ready data infrastructure, or AI system enablement; it mentions ML teams only as advantageous prior experience.

### testing_framing

**Run 1:** `absent`
> Quote: "No testing or data quality signal found in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD makes no mention of testing, data contracts, data quality frameworks, or observability practices.

**Run 2:** `absent`
> Quote: "data modelling standards"
> Verified: ✓ found in JD
> Reasoning: While data modelling standards are mentioned, there is no explicit signal about testing, data quality frameworks, or observability ownership.

**Run 3:** `absent`
> Quote: "Take ownership of platform architecture, data modelling standards, and engineering best practices"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize engineering standards and best practices but contain no explicit mention of data quality frameworks, testing, or observability practices.

### loss_aversion_framing

**Run 1:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role around building capability and supporting organizational growth rather than preventing bad outcomes or managing risk.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role around capability and growth delivery with no language around risk, compliance, or preventing bad outcomes.

**Run 3:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role entirely around building new analytics platform capabilities and supporting organizational growth with no emphasis on risk, compliance, reliability, or preventing bad outcomes.
