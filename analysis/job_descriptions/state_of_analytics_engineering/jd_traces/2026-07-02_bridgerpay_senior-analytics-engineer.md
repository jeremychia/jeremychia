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

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 0 | 0 | 0 | 0 | 100% | ✓ |
| data_team_maturity | early | mid | early | mid | 33% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | mixed | strategic | strategic | 33% | ✓ |
| ai_role |  | ai_enabler | ai_user | ai_user | 33% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | high | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals emphasise testing, compliance (PCI-DSS/SOC2), security protocols, and production-grade work with no corresponding velocity language.

**Run 2:** `rigour` ✓
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (CI/CD, testing, security protocols, PCI-DSS/SOC2 compliance, data SLAs) dominate the responsibilities with no velocity language present.

**Run 3:** `rigour` ✓
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes compliance (PCI-DSS/SOC2), testing, CI/CD frameworks, and operational reliability over delivery speed.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Explicit regulatory compliance requirements (PCI-DSS/SOC2) signal that data errors directly affect regulatory and financial operations in a payment context.

**Run 2:** `high` ✓
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: PCI-DSS and SOC2 are regulatory compliance frameworks for payment card data and security, indicating the role directly handles regulated financial data with high regulatory stakes.

**Run 3:** `high` ✓
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Explicit compliance requirements for payment card data security (PCI-DSS) and organizational security (SOC2) indicate high financial and regulatory risk.

### collaboration_width
**Manual:** `0`

**Run 1:** `0` ✓
> Quote: "Build and scale data warehouse core and pipelines utilizing BigQuery and managed cloud services"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes technical responsibilities and deliverables without naming specific business functions or partner teams to collaborate with.

**Run 2:** `0` ✓
> Quote: "No explicitly named partner teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD references downstream consumers (AI models, routing engines, BI tools) but does not name specific functions or teams as collaboration partners.

**Run 3:** `0` ✓
> Quote: "No named partner teams explicitly identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions systems the role serves (AI models, routing engines, BI tools) but does not name specific partner functions or teams to collaborate with.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (BigQuery, Dataform, Looker) combined with foundational language (introduce, build, prepare) suggest growth from existing but not-yet-mature infrastructure.

**Run 2:** `early` ✓
> Quote: "Proven track record building data warehouses and semantic layers from scratch"
> Verified: ✓ found in JD
> Reasoning: The requirement for "building from scratch" experience combined with the "Engineering Foundation Phase" structure indicates the data function is in early-stage formation.

**Run 3:** `mid` ✗
> Quote: "Maintain Looker and business intelligence layer with full ownership"
> Verified: ✓ found in JD
> Reasoning: Named existing tools (Looker, BigQuery, Dataform) and maintenance responsibilities indicate a functioning data function being scaled and matured, not greenfield.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'early', 'mid']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about tools, techniques (production-grade LookML), and system context (routing engines, AI models) indicates hiring manager authorship.

**Run 2:** `hiring_manager` ✓
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: The specificity of technical output (production-grade LookML) paired with application context (serving AI models, routing engines, and BI tools) indicates domain knowledge from someone who performs this work.

**Run 3:** `hiring_manager` ✓
> Quote: "Implement CI/CD practices using fully managed GCP services"
> Verified: ✓ found in JD
> Reasoning: Specific technical detail about GCP services, BigQuery, LookML, and two distinct implementation phases shows domain expertise from someone who understands the specific role.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Build complex data models serving clean data to AI models, routing engines, and BI tools"
> Verified: ✓ found in JD
> Reasoning: The primary audience is internal data consumers (AI systems, routing engines, BI tools) rather than business functions like sales, product, or finance.

**Run 2:** `internal_data` ✓
> Quote: "Build complex data models serving clean data to AI models, routing engines, and BI tools"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining the data infrastructure and semantic layer that internal systems and analytics consumers depend on, rather than serving commercial, product, or finance functions.

**Run 3:** `internal_data` ✓
> Quote: "Build complex data models serving clean data to AI models, routing engines, and BI tools"
> Verified: ✓ found in JD
> Reasoning: The role is framed around building the data platform and semantic layer that serves internal systems and data consumers, not external commercial or finance stakeholders.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `mixed` ✗
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of technical domains (semantic layer, BI layer) with execution of pre-defined engineering phases.

**Run 2:** `strategic` ✓
> Quote: "Own the semantic layer, writing production-grade LookML"
> Verified: ✓ found in JD
> Reasoning: The verbs "own", "establish", and "introduce" combined with responsibility for defining CI/CD frameworks and testing standards indicate the role shapes the data architecture rather than executing assigned work.

**Run 3:** `strategic` ✓
> Quote: "full ownership"
> Verified: ✓ found in JD
> Reasoning: Repeated emphasis on ownership (semantic layer, BI layer) combined with "introduce" new frameworks and soft skills requiring "extreme ownership focus" indicates direction-setting autonomy.

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'strategic']

### ai_role
**Manual:** ``

**Run 1:** `ai_enabler` ✗
> Quote: "Prepare data ecosystem for real-time AI modeling"
> Verified: ✓ found in JD
> Reasoning: While the role requires proficiency with AI coding assistants, the primary responsibility is building data infrastructure for AI systems to consume, making this ai_enabler.

**Run 2:** `ai_user` ✗
> Quote: "Proficiency with generative AI coding assistants"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement for the candidate to be proficient with AI coding assistants indicates they are expected to use these tools to accelerate their own development and engineering work.

**Run 3:** `ai_user` ✗
> Quote: "Proficiency with generative AI coding assistants"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI coding tools like GitHub Copilot or Claude Code to accelerate their own development work.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

⚠ **LLM inconsistency**: runs gave ['ai_enabler', 'ai_user', 'ai_user']

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The ownership verb introduce for unit testing indicates the candidate will define and implement testing practices rather than just use them.

**Run 2:** `responsibility` ✗
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: The verb "introduce" paired with unit testing in the responsibilities section indicates the candidate is expected to define and establish testing standards as a core responsibility, not just apply existing tools.

**Run 3:** `responsibility` ✗
> Quote: "Introduce robust CI/CD frameworks, unit testing, and security protocols"
> Verified: ✓ found in JD
> Reasoning: Testing is framed as something the candidate owns and defines using the action verb "introduce," indicating accountability for establishing these practices.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Compliance and operational reliability are explicit concerns but secondary to the primary mission of building and scaling infrastructure.

**Run 2:** `moderate` ✗
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: While compliance and operational reliability (SLAs, uptime) are explicit concerns, the responsibilities frame them as constraints alongside delivery goals rather than as the primary risk-mitigation driver of the role.

**Run 3:** `high` ✗
> Quote: "Ensure PCI-DSS/SOC2 compliance while optimizing costs"
> Verified: ✓ found in JD
> Reasoning: Compliance and regulatory risk dominate the role framing, with additional emphasis on operational reliability through data SLAs and uptime, reflecting fear of regulatory exposure and data reliability failures.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'high']
