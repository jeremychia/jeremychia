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

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 2 | 3 | 0% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | strategic | strategic | strategic | 100% |
| ai_role | ai_enabler | ai_enabler | ai_enabler | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize testing, data quality frameworks, documentation, and best practices as core expectations, with no velocity or speed-to-ship language.

**Run 2:** `rigour`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes testing, documentation, data quality, and reliability as core practices throughout, with no velocity or speed-oriented language.

**Run 3:** `rigour`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize correctness, testing, quality, reliability, and documentation as core expectations throughout, with no countervailing velocity or iteration speed signals.

### domain_risk

**Run 1:** `moderate`
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: This is a SaaS analytics engineering role with no financial reporting, regulatory, or compliance language; data errors affect business decisions but not immediate regulatory or financial reporting consequences.

**Run 2:** `moderate`
> Quote: "Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets"
> Verified: ✓ found in JD
> Reasoning: The role involves SaaS analytics and operational reporting without explicit financial reporting, regulatory compliance, or public-facing product exposure.

**Run 3:** `moderate`
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: The role affects business intelligence and product decisions but does not involve financial reporting, regulatory compliance, or audit-level risk that would elevate it to high domain risk.

### collaboration_width

**Run 1:** `1`
> Quote: "Collaborate with Data Engineers on upstream data contracts and event schemas"
> Verified: ✓ found in JD
> Reasoning: Only Data Engineers are explicitly named as a collaboration partner; other functions like product and analytics are named as downstream consumers or stakeholder groups, not as active collaboration partners.

**Run 2:** `2`
> Quote: "Data Engineers; product"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data Engineers and Product are explicitly named as distinct collaboration partners in the responsibilities section.

**Run 3:** `3`
> Quote: "Collaborate with Data Engineers on upstream data contracts; ensuring consistent definitions across analytics, product, and AI use cases"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named teams are explicitly mentioned as collaborators or stakeholders: Data Engineers (explicit partner), Product (named stakeholder), and Analytics (named stakeholder).

⚠ **LLM inconsistency**: runs gave ['1', '2', '3']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: Dbt, data engineers, and semantic layer infrastructure already exist and are being used; the role is to evolve and scale these, indicating a team past greenfield but not yet fully mature at scale.

**Run 2:** `mid`
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers"
> Verified: ✓ found in JD
> Reasoning: The JD describes evolving existing infrastructure (dbt transformation layer, semantic layer, data integration pipelines) with an established data engineering team rather than building from scratch.

**Run 3:** `mid`
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models"
> Verified: ✓ found in JD
> Reasoning: The role involves maintaining and extending existing named tools (dbt, semantic layers) rather than building from scratch, suggesting a data function beyond greenfield but still actively growing its capabilities.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain technical specificity about SaaS integration patterns, named tool contexts (Salesforce), dimensional modeling, metrics naming (activation, engagement, retention), and semantic layer design that only comes from someone with hands-on analytics engineering experience.

**Run 2:** `hiring_manager`
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical details (dbt, dimensional modeling, data contracts, specific cloud DWs, MetricFlow, Cube, semantic layers) that indicate hands-on experience rather than recruiter boilerplate.

**Run 3:** `hiring_manager`
> Quote: "Collaborate with Data Engineers on upstream data contracts and event schemas - ensuring raw data is structured in a way that supports scalable, reliable analytics"
> Verified: ✓ found in JD
> Reasoning: The responsibilities demonstrate technical specificity (data contracts, event schemas, dimensional modeling patterns, dimensional models) that only someone actively doing this work would include.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the data function itself—building data infrastructure, semantic layers, and metrics for analytics teams, data engineers, and AI agents to consume.

**Run 2:** `internal_data`
> Quote: "supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The primary framing is building reliable data infrastructure and semantic layers that serve the data function itself and its consumers, not directly serving product, commercial, or finance teams.

**Run 3:** `internal_data`
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The primary emphasis is on building and owning data infrastructure (semantic layer, transformation layer, self-serve documentation) that serves multiple downstream consumers, rather than serving a single business function.

### autonomy_level

**Run 1:** `strategic`
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company"
> Verified: ✓ found in JD
> Reasoning: The role is expected to own, design, and define the transformation strategy, not execute scoped work set by others—these are direction-setting responsibilities.

**Run 2:** `strategic`
> Quote: "Own the transformation layer in dbt"
> Verified: ✓ found in JD
> Reasoning: The role uses ownership and direction-setting verbs (Own, Define, Build, Establish) throughout, establishing standards and shaping how data is structured and metrics are defined.

**Run 3:** `strategic`
> Quote: "Own the transformation layer in dbt - design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company"
> Verified: ✓ found in JD
> Reasoning: The role uses repeated ownership and definition verbs (own, define, establish, build, evolve) that frame the candidate as setting direction for major components of data infrastructure.

### ai_role

**Run 1:** `ai_enabler`
> Quote: "Build and evolve our semantic layer - creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The candidate is explicitly expected to build data infrastructure that LLM-based analytics agents consume and understand how to structure data for AI system consumption.

**Run 2:** `ai_enabler`
> Quote: "supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that LLMs consume, explicitly mentioned in responsibilities and reinforced by the nice-to-have section on semantic layers for AI agents.

**Run 3:** `ai_enabler`
> Quote: "building data infrastructure that serves AI agents, not just BI tools"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to understand how LLMs consume structured data and to build semantic layers and data infrastructure specifically to enable AI agent consumption.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as owned responsibilities with action verbs 'establish and enforce,' indicating the candidate is accountable for defining and institutionalizing these practices.

**Run 2:** `responsibility`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as something the candidate owns and establishes as a standard practice, not as tools they use.

**Run 3:** `responsibility`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The action verbs 'establish and enforce' indicate the candidate owns the creation and enforcement of testing and quality practices as a core responsibility.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and consistency are stated concerns throughout (reliable, consistent, well-tested, best practices), but there is no compliance, regulatory, or stakeholder trust framing—the fear is operational data quality issues, not catastrophic risk.

**Run 2:** `moderate`
> Quote: "strong data quality mindset (testing, validation, monitoring)"
> Verified: ✓ found in JD
> Reasoning: Reliability and quality are emphasized as operational standards rather than as risk mitigation against compliance, regulatory, or stakeholder-trust failure.

**Run 3:** `moderate`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality - making these part of the standard development lifecycle"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and data quality as ongoing organizational concerns, but frames them as standard practices and excellence rather than regulatory, compliance, or stakeholder-trust risks.
