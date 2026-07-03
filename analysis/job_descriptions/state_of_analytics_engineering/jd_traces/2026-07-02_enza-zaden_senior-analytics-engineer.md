# Trace: 2026-07-02_enza-zaden_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Enza Zaden

**URL:** https://enzazaden.wd103.myworkdayjobs.com/Enza-Careers/job/Enkhuizen-The-Netherlands/Analytics-Engineer_JR105077?source=LinkedIn
**Location:** Enkhuizen, Netherlands
**Date Posted:** 2026-07-02
**Salary:** 5,104–7,291 EUR

---

# Senior Analytics Engineer

Company: Enza Zaden
Location: Enkhuizen, The Netherlands
Time type: Full time
Job requisition ID: JR105077
Salary: EUR 5,103.90 - EUR 7,291.28 gross monthly, based on full-time 38-hour workweek

## Role summary
As a Senior Analytics Engineer, you make an impact by strengthening data-driven decision-making across Enza Zaden worldwide. You develop scalable data solutions and translate complex challenges into valuable insights that help teams perform better. You design, build and maintain scalable data models and analytics products that empower self-service BI for teams across the organization. Working closely with product owners, analytics engineers, IT specialists and business stakeholders, you translate complex requirements into reliable solutions on the global data platform.

## Responsibilities
- Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI
- Leading complex analytics and reporting initiatives with a mid- to long-term horizon
- Translating business needs into scalable, well-governed data solutions in collaboration with stakeholders and product owners
- Improving data quality, reliability, performance and cost efficiency through lifecycle management
- Ensuring compliance with architecture, security and access standards together with IT, Architecture and Security teams
- Coaching colleagues and contributing to knowledge sharing, user enablement and adoption of data solutions

## Requirements
- Master's degree (WO) with 6-8 years of relevant experience in analytics, reporting or data engineering
- Strong knowledge of data modelling, analytics and data transformation techniques
- Hands-on experience with Azure (DP203), Databricks, SQL, dbt, Power BI, DAX and Git
- Experience with DevOps practices such as version control, testing and CI/CD for data products
- Understanding of scalability, architecture principles and data platform lifecycle management
- Strong communication, stakeholder management and coaching skills

## Enza Zaden as employer
Enza Zaden is an international family-owned company developing innovative vegetable varieties since 1938. Together with more than 3,300 colleagues worldwide, working on vegetable seeds with better flavor, higher yields and strong resistances. Mission: 'Breeding to feed the world.' Every day, more than 480 million people eat vegetables grown from their seeds.

## Benefits
32-38 hours/week position. 8.33% vacation allowance and annual bonus program of 10% of annual salary. 25 vacation days plus purchase option and vitality day. Laptop and mobile phone provided. Accommodation contribution for long commutes. Retirement plan, commuting reimbursement, remote work allowance. Great to Grow development program, training, workshops, e-learning. Social events, free fresh fruit, healthy lunch, bike-to-work program, sports activities, mental well-being support (OpenUp).

Contact: Sandra Hoeneveld, Corporate Recruiter, s.hoeneveld-blekkink@enzazaden.nl. Response within 10 business days. This role cannot be filled on an interim basis.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | low | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 4 | 5 | 4 | 4 | 33% | ✓ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | execution | mixed | mixed | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | tool_listed | tool_listed | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Improving data quality, reliability, performance and cost efficiency through lifecycle management"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize quality, reliability, and governance with no velocity language present; compliance and architecture standards are core expectations.

**Run 2:** `rigour` ✓
> Quote: "Improving data quality, reliability, performance and cost efficiency through lifecycle management"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes quality, reliability, governance, and compliance as core expectations with no velocity or speed-oriented language present.

**Run 3:** `rigour` ✓
> Quote: "Translating business needs into scalable, well-governed data solutions"
> Verified: ✓ found in JD
> Reasoning: Governance, quality, and compliance are core responsibilities with no velocity-oriented language; 'well-governed' explicitly signals rigour priority.

### domain_risk
**Manual:** `low`

**Run 1:** `moderate` ✗
> Quote: "Ensuring compliance with architecture, security and access standards together with IT, Architecture and Security teams"
> Verified: ✓ found in JD
> Reasoning: Data errors affect internal business operations and decision-making but lack explicit financial reporting, regulatory, or audit language that would signal high risk.

**Run 2:** `moderate` ✗
> Quote: "Ensuring compliance with architecture, security and access standards together with IT, Architecture and Security teams"
> Verified: ✓ found in JD
> Reasoning: The compliance mentioned is technical and IT-focused rather than financial, regulatory, or public-safety compliance; this is a business intelligence role without explicit financial reporting or regulatory impact signals.

**Run 3:** `moderate` ✗
> Quote: "empower self-serve BI for teams across the organization"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role supports internal business decision-making and analytics without financial reporting, regulatory, or compliance-driven consequences.

⚠ **Disagreement**: manual=`low` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `5` ✗
> Quote: "product owners; analytics engineers; IT specialists; IT, Architecture and Security teams"
> Verified: ✓ found in JD
> Reasoning: Five named teams identified: Product (product owners), Analytics (analytics engineers), IT, Architecture, and Security.

**Run 2:** `4` ✓
> Quote: "product owners; IT specialists; Architecture and Security teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly mentioned: Product, IT, Architecture, and Security.

**Run 3:** `4` ✓
> Quote: "product owners; IT specialists; Architecture and Security teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly listed: Product, IT, Architecture, and Security.

⚠ **LLM inconsistency**: runs gave ['5', '4', '4']

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Improving data quality, reliability, performance and cost efficiency through lifecycle management"
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure (Databricks, dbt, Power BI) with multiple roles implies an established function scaling and improving existing systems rather than building from scratch.

**Run 2:** `mid` ✗
> Quote: "design, build and maintain scalable data models and analytics products that empower self-service BI for teams across the organization"
> Verified: ✓ found in JD
> Reasoning: Existing named tools in responsibilities (Databricks, dbt, Power BI), an established global data platform, and self-service BI infrastructure already deployed indicate a mid-stage data function with improvement focus rather than early-stage or fully mature scale.

**Run 3:** `mid` ✗
> Quote: "global data platform"
> Verified: ✓ found in JD
> Reasoning: An established global platform with multiple named roles and coaching responsibilities indicates a growing but already-operational data function.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI"
> Verified: ✓ found in JD
> Reasoning: Named tools with specific context (Databricks, dbt) in responsibilities suggests hiring manager input, but generic stakeholder management verbs ('coaching', 'knowledge sharing') indicate recruiter boilerplate.

**Run 2:** `mixed` ✗
> Quote: "Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific tool names and methodology context suggesting hands-on technical knowledge, but also include generic stakeholder collaboration and coaching language typical of recruiter-authored JDs.

**Run 3:** `mixed` ✗
> Quote: "Designing, developing and maintaining advanced data models and analytics products using tools like Databricks, dbt and Power BI"
> Verified: ✓ found in JD
> Reasoning: Specific tool applications and governance compliance details show hiring-manager input, but generic verbs like 'coaching colleagues' indicate recruiter boilerplate.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "empower self-serve BI for teams across the organization"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary framing is building and maintaining data models and analytics products for internal team consumption via self-service analytics platform.

**Run 2:** `internal_data` ✓
> Quote: "empower self-service BI for teams across the organization"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is building data infrastructure and enabling self-serve analytics for internal organizational teams rather than serving commercial, product, finance, or external audiences.

**Run 3:** `internal_data` ✓
> Quote: "empower self-serve BI for teams across the organization"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary purpose is building analytics infrastructure and data models for internal team consumption rather than commercial, product, or finance outcomes.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `execution` ✗
> Quote: "translate complex requirements into reliable solutions on the global data platform"
> Verified: ✓ found in JD
> Reasoning: Role receives scoped requirements from product owners and stakeholders and executes solutions; no strategic direction-setting or roadmap ownership language.

**Run 2:** `mixed` ✗
> Quote: "Leading complex analytics and reporting initiatives with a mid- to long-term horizon"
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership through 'leading' and 'designing' but operates within business requirements set by product owners and stakeholders, combining both strategic and execution dimensions.

**Run 3:** `mixed` ✗
> Quote: "Leading complex analytics and reporting initiatives with a mid- to long-term horizon"
> Verified: ✓ found in JD
> Reasoning: The role leads and designs initiatives (strategic) while maintaining solutions within an established governance framework and platform (execution).

⚠ **Disagreement**: manual=`strategic` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, AI-assisted coding, or AI-ready data infrastructure anywhere in the JD.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-ready data foundations, or any AI skills expected of candidates.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI coding tools, AI-assisted productivity, or AI infrastructure expectations anywhere in the JD.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `tool_listed` ✗
> Quote: "Experience with DevOps practices such as version control, testing and CI/CD for data products"
> Verified: ✓ found in JD
> Reasoning: Testing appears in requirements as a required skill area but without ownership framing; data quality is mentioned in responsibilities through 'lifecycle management' rather than testing practices.

**Run 2:** `tool_listed` ✗
> Quote: "DevOps practices such as version control, testing and CI/CD for data products"
> Verified: ✓ found in JD
> Reasoning: Testing appears as a listed skill in the requirements section without ownership verbs or responsibility framing in the responsibilities section.

**Run 3:** `responsibility` ✗
> Quote: "Improving data quality, reliability, performance and cost efficiency through lifecycle management"
> Verified: ✓ found in JD
> Reasoning: Data quality improvement is framed as a core responsibility the role owns and improves, not merely as tools listed in requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`tool_listed`

⚠ **LLM inconsistency**: runs gave ['tool_listed', 'tool_listed', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Improving data quality, reliability, performance and cost efficiency through lifecycle management"
> Verified: ✓ found in JD
> Reasoning: Reliability and quality are operational concerns but secondary to the primary delivery mission of building scalable solutions; no regulatory, compliance, or stakeholder trust risk register dominates the framing.

**Run 2:** `moderate` ✗
> Quote: "Improving data quality, reliability, performance and cost efficiency through lifecycle management"
> Verified: ✓ found in JD
> Reasoning: Reliability and compliance are stated concerns but remain secondary to the primary framing around strengthening decision-making and building scalable solutions; the fear is operational reliability rather than regulatory exposure.

**Run 3:** `moderate` ✗
> Quote: "Ensuring compliance with architecture, security and access standards"
> Verified: ✓ found in JD
> Reasoning: Compliance and operational reliability are mentioned but appear secondary to delivery; the role is not primarily framed around preventing risk or protecting stakeholders.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
