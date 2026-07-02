# Trace: 2026-07-02_bridgerpay_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — BridgerPay

**URL:** https://www.linkedin.com/jobs/view/4417929952/
**Location:** Limassol, Cyprus
**Date Posted:** 2026-07-02

---

# Senior Analytics Engineer at BridgerPay

Location: Limassol, Cyprus (Full-time, Onsite)
Salary: Not stated

## Key Responsibilities
Engineering Foundation Phase:
- Optimize batch infrastructure and establish Git version control
- Implement CI/CD practices using fully managed GCP services
- Build and scale data warehouse core and pipelines utilizing BigQuery and managed cloud services
- Prepare data ecosystem for real-time AI modeling

Analytics Engineering Phase:
- Own the semantic layer, writing production-grade LookML
- Build complex data models serving clean data to AI models, routing engines, and BI tools
- Maintain Looker and business intelligence layer with full ownership
- Introduce robust CI/CD frameworks, unit testing, and security protocols
- Ensure PCI-DSS/SOC2 compliance while optimizing costs
- Handle confidential data per organizational security policies

## Requirements
Experience:
- 5+ years in Analytics Engineering, Data Engineering, or BI Development
- Proven track record building data warehouses and semantic layers from scratch

Technical Skills:
- Expert-level SQL and Python
- Deep knowledge of API extractions, data modeling (dbt/Dataform), and Git version control
- Strong GCP experience: BigQuery, Dataform, Looker, Cloud Composer/Airflow
- Proficiency with generative AI coding assistants
- Fluent English required

Soft Skills:
- High resilience and extreme ownership focus
- Strong operational mindset regarding data SLAs and uptime
- Excellent technical communication

## Benefits (Cyprus Office)
Competitive salary, breakfast, lunch allowance, birthday day-off, private medical insurance, ESOP, career growth opportunities, modern Limassol office with pool, snacks, team events, employee referral programme, relocation support to Cyprus, flexible remote start option (3-6 months before onsite transition).

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | high | high | 100% |
| collaboration_width | 0 | 0 | 0 | 100% |
| data_team_maturity | early | mid | early | 33% |
| jd_authorship | hiring_manager | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | strategic | mixed | 33% |
| ai_role | ai_user | ai_enabler | ai_enabler | 33% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | high | high | high | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (unit testing, security protocols, CI/CD frameworks, PCI-DSS/SOC2 compliance) dominate with zero velocity language present.

**Run 2:** `rigour`
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, compliance, and operational standards throughout, with no velocity-oriented language such as 'fast-paced' or 'rapid delivery'; compliance and testing are core expectations.

**Run 3:** `rigour`
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes quality, compliance (PCI-DSS/SOC2), testing, and reliability with no velocity signals like 'fast-paced' or 'ship quickly'.

### domain_risk

**Run 1:** `high`
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Explicit PCI-DSS and SOC2 compliance requirements in a payments context indicate regulatory and financial risk with direct consequences for data accuracy.

**Run 2:** `high`
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of PCI-DSS and SOC2 compliance standards indicates data errors directly affect financial transaction processing and regulatory exposure in a fintech payment context.

**Run 3:** `high`
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: PCI-DSS and SOC2 compliance requirements indicate a fintech/payments company handling sensitive financial data with explicit regulatory obligations.

### collaboration_width

**Run 1:** `0`
> Quote: "No named partner teams or functions identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names technical outputs (AI models, routing engines, BI tools) but does not list any explicitly named business functions or partner teams.

**Run 2:** `0`
> Quote: "No named partner teams or functions identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD references AI models, routing engines, and BI tools as consumers but does not explicitly name any partner teams such as Product, Finance, Engineering, or other functional groups.

**Run 3:** `0`
> Quote: "Build complex data models serving clean data to AI models, routing engines, and BI tools"
> Verified: ✓ found in JD
> Reasoning: AI models, routing engines, and BI tools are data consumers, not named partner teams; no cross-functional team collaborators are explicitly identified.

### data_team_maturity

**Run 1:** `early`
> Quote: "Build and scale data warehouse core and pipelines utilizing BigQuery and managed cloud services"
> Verified: ✓ found in JD
> Reasoning: The structured two-phase plan (Engineering Foundation Phase, Analytics Engineering Phase) and requirement for someone with track record building 'from scratch' indicate greenfield data infrastructure.

**Run 2:** `mid`
> Quote: "Build and scale data warehouse core and pipelines utilizing BigQuery and managed cloud services"
> Verified: ✓ found in JD
> Reasoning: The JD signals both building and scaling phases with named tools already in place (BigQuery, Looker, Dataform) and existing infrastructure to enhance, indicating a team that has produced something and is growing significantly.

**Run 3:** `early`
> Quote: "Proven track record building data warehouses and semantic layers from scratch"
> Verified: ✓ found in JD
> Reasoning: The emphasis on building 'from scratch' and 'preparing data ecosystem' indicates the data function is in early-stage establishment.

⚠ **LLM inconsistency**: runs gave ['early', 'mid', 'early']

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain precise technical tool choices (Dataform, LookML, semantic layer, Cloud Composer) and specific operational context only someone hands-on in data engineering would articulate.

**Run 2:** `mixed`
> Quote: "Own the semantic layer, writing production-grade LookML; Build complex data models serving clean data to AI models, routing engines, and BI tools"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical context appears in named tools and precise responsibilities (LookML, BigQuery, Dataform, PCI-DSS compliance) alongside generic action verbs and boilerplate patterns, indicating both hiring manager and recruiter input.

**Run 3:** `mixed`
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: Specific technical knowledge (LookML, BigQuery with context) mixed with generic language ('Introduce', 'Ensure') across responsibilities indicates both hiring manager and recruiter input.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Build complex data models serving clean data to AI models, routing engines, and BI tools"
> Verified: ✓ found in JD
> Reasoning: The role is building the data platform (semantic layer, BI layer, data warehouse) that internal technical consumers depend on.

**Run 2:** `internal_data`
> Quote: "Build complex data models serving clean data to AI models, routing engines, and BI tools; Own the semantic layer; Maintain Looker and business intelligence layer"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's primary focus is building and maintaining data infrastructure, semantic layers, and BI platforms for internal technical systems and analytics consumers rather than external commercial or finance stakeholders.

**Run 3:** `internal_data`
> Quote: "Own the semantic layer"
> Verified: ✓ found in JD
> Reasoning: The role is fundamentally about building data infrastructure and semantic layers for internal platform consumption, positioning the data function itself as the primary customer.

### autonomy_level

**Run 1:** `strategic`
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: Repeated strategic verbs (Own, Build, Introduce, Ensure, Prepare) throughout indicate the role defines and establishes the data function rather than executing scoped work.

**Run 2:** `strategic`
> Quote: "Own the semantic layer; establish Git version control; Introduce robust CI/CD frameworks"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities use ownership and establishment verbs that require defining direction and standards for the analytics platform rather than executing pre-scoped work set by others.

**Run 3:** `mixed`
> Quote: "Own the semantic layer"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership (Own semantic layer, Build and scale, Introduce frameworks) with execution responsibilities (Maintain systems, Ensure compliance).

⚠ **LLM inconsistency**: runs gave ['strategic', 'strategic', 'mixed']

### ai_role

**Run 1:** `ai_user`
> Quote: "Proficiency with generative AI coding assistants"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement for proficiency with generative AI coding assistants signals the candidate is expected to use AI tools to accelerate their own development work.

**Run 2:** `ai_enabler`
> Quote: "Prepare data ecosystem for real-time AI modeling"
> Verified: ✓ found in JD
> Reasoning: While the JD lists 'Proficiency with generative AI coding assistants' as a requirement, the primary role function is building data infrastructure that AI systems consume, making the candidate an enabler of AI capabilities.

**Run 3:** `ai_enabler`
> Quote: "Prepare data ecosystem for real-time AI modeling"
> Verified: ✓ found in JD
> Reasoning: While the candidate must be proficient with generative AI coding assistants, the primary AI expectation is building data infrastructure that AI systems consume.

⚠ **LLM inconsistency**: runs gave ['ai_user', 'ai_enabler', 'ai_enabler']

### testing_framing

**Run 1:** `responsibility`
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The action verb 'Introduce' paired with 'unit testing' in responsibilities shows ownership of establishing testing and quality practices.

**Run 2:** `responsibility`
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to establish and own testing practices and CI/CD standards, using the action verb 'Introduce' which signals accountability for defining testing frameworks.

**Run 3:** `responsibility`
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The action verb 'Introduce' frames testing and CI/CD as core responsibilities the candidate owns and establishes.

### loss_aversion_framing

**Run 1:** `high`
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Regulatory compliance and data confidentiality appear as primary responsibilities in a payments context, reflecting fear of regulatory exposure and breach liability.

**Run 2:** `high`
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs; Strong operational mindset regarding data SLAs and uptime"
> Verified: ⚠ NOT found verbatim
> Reasoning: Regulatory compliance and operational reliability are core to the role framing, with explicit emphasis on preventing data failures that would create regulatory exposure or operational outages.

**Run 3:** `high`
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Regulatory compliance (PCI-DSS/SOC2) and security protocols dominate the framing, reflecting fear of regulatory exposure and financial/security breaches from data errors.
