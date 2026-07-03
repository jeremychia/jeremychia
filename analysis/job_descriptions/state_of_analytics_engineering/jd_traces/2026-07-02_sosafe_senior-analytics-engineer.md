# Trace: 2026-07-02_sosafe_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — SoSafe

**URL:** https://jobs.ashbyhq.com/sosafe/86d983aa-252a-41c6-8ef1-58b40cd6f23a
**Location:** UK/Ireland/Portugal (Remote)
**Date Posted:** 2026-07-02

---

# Senior Analytics Engineer

Company: SoSafe
Location: United Kingdom Remote; Ireland Remote; London; Portugal Remote
Employment Type: Full time
Location Type: Remote
Department: Development

## About SoSafe
SoSafe has the ambition to become the leading human risk management provider in Europe. Our award-winning awareness platform triggers behavioural change by providing effective and engaging training and simulations on cybersecurity and data protection. Cybercrime is costing the world >$10 trillion annually and growing by 15% p.a.

Candidates must have work authorization in UK, Ireland, or Portugal. Office access available in London, Dublin, and Lisbon.

## Here's how you'll make a difference
- Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company
- Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets - ensuring consistent definitions across analytics, product, and AI use cases
- Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models
- Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents
- Collaborate with Data Engineers on upstream data contracts and event schemas - ensuring raw data is structured in a way that supports scalable, reliable analytics
- Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle
- Document models, metrics, and lineage clearly - enabling self-service and reducing ambiguity across teams

## What you bring
- 5+ years in analytics engineering or data engineering with a strong focus on data modeling
- Strong proficiency in dbt and SQL - building modular, well-tested models
- Solid understanding of dimensional modeling and metric design
- Experience working with cloud data warehouses (BigQuery, Snowflake, or Redshift)
- Experience with metrics / semantic layers (e.g. dbt metrics, MetricFlow, Cube)
- Strong data quality mindset (testing, validation, monitoring)
- Comfortable working with event-based data and cross-functional teams
- Able to turn ambiguous business questions into clear data models
- Strong business acumen with the ability to challenge metric definitions and ensure they reflect real business outcomes
- Fluent in English

Nice to have:
- Familiarity with how LLMs consume structured data - e.g. semantic layers, metrics registries, YAML-based context - and an interest in building data infrastructure that serves AI agents, not just BI tools
- Experience modeling product usage data (event-based or session-based)

## What we offer
Flexible hours, 33 vacation days. Access to Open Up, corporate discounts. Virtual events, collaborative team activities, local meet-ups. Tech equipment, referral bonuses, dog-friendly HQ.

## About Us
SoSafe is one of the fastest-growing security awareness scale-ups worldwide, leveraging behavioural science and data-driven learning. Backed by leading VCs like Highland Europe and Global Founders Capital, rapidly expanding across the globe.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 2 | 3 | 3 | 2 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | ai_enabler | ai_enabler | ai_enabler | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, documentation, and data quality as core expectations with explicit accountability for establishing standards.

**Run 2:** `rigour` ✓
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, documentation, data quality, and best practices with no mention of speed, iteration, or rapid delivery.

**Run 3:** `rigour` ✓
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes correctness, testing, documentation, and quality as core expectations with no velocity signals like 'fast-paced' or 'rapid delivery' present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames this as SaaS analytics work focused on product data without compliance, regulatory, or financial reporting language.

**Run 2:** `moderate` ✓
> Quote: "Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets"
> Verified: ✓ found in JD
> Reasoning: This is a SaaS business with revenue-impacting metrics but no explicit financial reporting, regulatory, or compliance language that would elevate risk to high.

**Run 3:** `moderate` ✓
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: Data errors would affect business decisions (metrics, product) but the JD does not explicitly invoke financial reporting, compliance, regulatory, or audit language that would elevate risk to high.

### collaboration_width
**Manual:** `2`

**Run 1:** `3` ✗
> Quote: "Data Engineers; analytics; product"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct partner functions: Data Engineers (collaboration on data contracts), analytics and product (requiring consistent definitions across both).

**Run 2:** `3` ✗
> Quote: "Data Engineers; analytics; product"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct teams: Data Engineers (collaboration partner), analytics (stakeholder across whom metrics must be consistent), and product (stakeholder).

**Run 3:** `2` ✓
> Quote: "Collaborate with Data Engineers on upstream data contracts and event schemas - ensuring consistent definitions across analytics, product, and AI use cases"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data Engineers and Product are explicitly named as distinct functions the role works with; Analytics may include the role holder's own team so is not counted separately.

⚠ **Disagreement**: manual=`2` vs LLM majority=`3`

⚠ **LLM inconsistency**: runs gave ['3', '3', '2']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models"
> Verified: ✓ found in JD
> Reasoning: The JD references existing dbt infrastructure and semantic layer that the role will maintain and evolve, indicating an established data function in growth phase.

**Run 2:** `mid` ✓
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions"
> Verified: ✓ found in JD
> Reasoning: The word 'evolve' rather than 'build from scratch,' the existence of Data Engineers as a distinct team, and named tools used in specific contexts indicate a data function past early stage but still growing.

**Run 3:** `mid` ✓
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers"
> Verified: ✓ found in JD
> Reasoning: The JD assumes existing infrastructure (dbt, semantic layer, Data Engineers team) and the role is to evolve and enforce practices around it rather than build from scratch.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical concepts (SaaS data modeling, Salesforce integration, fact/dimension models) and named tools with precise application context indicating hiring manager authorship.

**Run 2:** `hiring_manager` ✓
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: The specificity of technical choices (dimensional modeling, named data sources, SaaS-specific architecture, semantic layers, dbt metrics) indicates someone who has done this work, not a recruiter.

**Run 3:** `hiring_manager` ✓
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain technical specificity (transformation layer in dbt, dimensional modeling, metric design, Salesforce CRM integration, event-based data) that only comes from someone who has performed this role.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building data infrastructure and standards that internal teams and AI systems consume, rather than serving commercial or embedded product analytics teams.

**Run 2:** `internal_data` ✓
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The primary deliverables are data infrastructure components (semantic layer, metrics layer, transformation layer) that serve downstream data consumers rather than directly serving commercial, product, or finance stakeholders.

**Run 3:** `internal_data` ✓
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining data infrastructure (transformation layer, semantic layer, metrics) that serves other teams, not directly serving commercial, product, or finance functions.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company"
> Verified: ✓ found in JD
> Reasoning: The use of 'own' and 'define' with accountability for data structure and how analytics is delivered across the company indicates the role sets direction rather than executing direction from others.

**Run 2:** `strategic` ✓
> Quote: "Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets"
> Verified: ✓ found in JD
> Reasoning: The role uses ownership verbs ('own,' 'define,' 'establish') and is responsible for shaping how analytics is delivered across the organization, not executing against predefined requirements.

**Run 3:** `strategic` ✓
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes ownership ('own'), definition ('define metrics'), and establishing standards ('establish best practices'), indicating the candidate sets direction within the analytics and metrics domain.

### ai_role
**Manual:** ``

**Run 1:** `ai_enabler` ✗
> Quote: "building data infrastructure that serves AI agents, not just BI tools"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly expects the candidate to build semantic layers and metrics registries designed for LLM-based analytics agents to consume, making this an ai_enabler role.

**Run 2:** `ai_enabler` ✗
> Quote: "an interest in building data infrastructure that serves AI agents, not just BI tools"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure (semantic layers, metrics registries) that AI systems consume, not to use AI tools for their own productivity.

**Run 3:** `ai_enabler` ✗
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems consume; the nice-to-have section reinforces interest in 'building data infrastructure that serves AI agents, not just BI tools'.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_enabler`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The JD frames testing as something the candidate owns through 'establish and enforce' verbs, indicating accountability for defining and maintaining testing practices.

**Run 2:** `responsibility` ✗
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as responsibilities the role owner establishes and enforces as standards, not as tools listed in a requirements section.

**Run 3:** `responsibility` ✗
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as owned responsibilities with ownership verbs 'establish and enforce', not merely as tools to know or skills to have.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Data quality and reliability are emphasized as core responsibilities but framed in operational and process terms (standard development practice) rather than preventing regulatory, compliance, or stakeholder trust issues.

**Run 2:** `moderate` ✗
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Data quality and operational reliability are concerns but secondary to the primary mission of building metrics and semantic layer infrastructure; there is no regulatory, compliance, or stakeholder-trust-focused language.

**Run 3:** `moderate` ✗
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Reliability and data quality are central concerns, but the language emphasizes operational best practices and consistency rather than regulatory compliance or preventing catastrophic business impact.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
