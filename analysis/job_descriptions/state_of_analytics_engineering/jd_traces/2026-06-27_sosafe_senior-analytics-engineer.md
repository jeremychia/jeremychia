# Trace: 2026-06-27_sosafe_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — SoSafe

**Location:** United Kingdom Remote (also Portugal Remote, Ireland Remote, London)
**Date Posted:** 2026-04-21

---

SoSafe has the ambition to become the leading human risk management provider in Europe. Our award-winning awareness platform triggers behavioural change by providing effective and engaging training and simulations on cybersecurity and data protection. Cybercrime is costing the world >$10 trillion annually and growing by 15% p.a. - we invite you to be part of the solution!"

Location:

UK, Ireland, or Portugal (remote). Candidates must have work authorization in one of these countries. Office access available in London, Dublin, and Lisbon.


Here's how you'll make a difference:

 - Own the transformation layer in dbt- design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company.

 - Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets- ensuring consistent definitions across analytics, product, and AI use cases.

 - Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models.

 - Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents.

 - Collaborate with Data Engineers on upstream data contracts and event schemas- ensuring raw data is structured in a way that supports scalable, reliable analytics.

 - Establish and enforce best practices in testing, documentation, and data quality- making these part of the standard development lifecycle.

 - Document models, metrics, and lineage clearly- enabling self-service and reducing ambiguity across teams.



What you bring:

 - 5+ years in analytics engineering or data engineering with a strong focus on data modeling

 - Strong proficiency in dbt and SQL- building modular, well-tested models

 - Solid understanding of dimensional modeling and metric design

 - Experience working with cloud data warehouses (BigQuery, Snowflake, or Redshift)

 - Experience with metrics / semantic layers (e.g. dbt metrics, MetricFlow, Cube)

 - Strong data quality mindset (testing, validation, monitoring)

 - Comfortable working with event-based data and cross-functional teams

 - Able to turn ambiguous business questions into clear data models

 - Strong business acumen with the ability to challenge metric definitions and ensure they reflect real business outcomes

 - Fluent in English.



Nice to have:

 - Familiarity with how LLMs consume structured data- e.g. semantic layers, metrics registries, YAML-based context- and an interest in building data infrastructure that serves AI agents, not just BI tools.

 - Experience modeling product usage data (event-based or session-based).



What we offer*

 - Work/Life balance: Flexible hours, 33 vacation days

 - Wellbeing and financial support: Access to Open Up, corporate discounts

 - Connection & community: Virtual events, collaborative team activities, and opportunities for local meet-ups

 - And the list goes on: Tech equipment, referral bonuses, dog-friendly HQ

*Perks and benefits listed above are for full-time employees and may vary slightly by office location. These are just a sample- you'll learn more during the interview process.

About Us

At SoSafe, we're on a mission to make the digital world safer by addressing the human factor in cybersecurity. As one of the fastest-growing security awareness scale-ups worldwide, we leverage behavioural science and data-driven learning to empower people against cyber threats. Our Human Risk Management approach helps organisations turn their employees into their strongest line of defence.

Backed by leading VCs like Highland Europe and Global Founders Capital, we're rapidly expanding across the globe. We're looking…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | product | internal_data | internal_data | 33% |
| autonomy_level | strategic | strategic | strategic | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality- making these part of the standard development lifecycle."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, documentation, data quality, and best practices as core to the development lifecycle with no velocity language present.

**Run 2:** `rigour`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality- making these part of the standard development lifecycle."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, data quality, documentation, and reliability throughout with no counterbalancing velocity or delivery-pace language.

**Run 3:** `rigour`
> Quote: "Establish and enforce best practices in testing, documentation, and data quality- making these part of the standard development lifecycle."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, data quality, documentation, and reliability throughout without any velocity language like 'fast-paced' or 'ship quickly'.

### domain_risk

**Run 1:** `moderate`
> Quote: "Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets"
> Verified: ✓ found in JD
> Reasoning: The role focuses on product analytics metrics and SaaS data modeling without explicit regulatory, compliance, or financial reporting language.

**Run 2:** `moderate`
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models."
> Verified: ✓ found in JD
> Reasoning: The role involves operational SaaS business metrics and analytics without explicit financial reporting, regulatory, or compliance requirements.

**Run 3:** `moderate`
> Quote: "Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets"
> Verified: ✓ found in JD
> Reasoning: The role involves SaaS product analytics and business intelligence for internal decision-making rather than financial reporting or regulatory compliance.

### collaboration_width

**Run 1:** `2`
> Quote: "Collaborate with Data Engineers; product (from ensuring consistent definitions across analytics, product, and AI use cases)"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named collaborating teams are explicitly identified: Data Engineers and Product.

**Run 2:** `2`
> Quote: "Data Engineers; Product"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data Engineers are explicitly named as collaborators, and Product is named as a team requiring consistent metric definitions; Analytics is the role's own function.

**Run 3:** `2`
> Quote: "Collaborate with Data Engineers on upstream data contracts and event schemas; ensuring consistent definitions across analytics, product, and AI use cases"
> Verified: ⚠ NOT found verbatim
> Reasoning: Named partner teams are Data Engineers and Product, with AI referenced as a use case rather than a distinct collaboration partner.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Own the transformation layer in dbt- design, build, and maintain modular, well-tested data models"
> Verified: ✓ found in JD
> Reasoning: The existence of an established transformation layer in dbt and references to evolving existing infrastructure indicate a mid-stage data function with established tools and team members.

**Run 2:** `mid`
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents."
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, semantic layer, data contracts), an existing Data Engineering team, and language of evolution and scaling signal an established function in growth mode.

**Run 3:** `mid`
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers"
> Verified: ✓ found in JD
> Reasoning: The language 'evolve' and references to existing dbt infrastructure, data engineers, and multiple integrated data sources indicate an established team building upon existing capabilities rather than greenfield or mature enterprise scale.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Own the transformation layer in dbt- design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company."
> Verified: ✓ found in JD
> Reasoning: The specific technical context about dbt transformation layers, semantic layers, named tools, and product event data modeling demonstrates hands-on knowledge of the actual work.

**Run 2:** `hiring_manager`
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models."
> Verified: ✓ found in JD
> Reasoning: Specific technical context (dbt, Salesforce integration, dimensional modeling, semantic layers, data contracts, event schemas) indicates authorship by someone with hands-on experience in the role.

**Run 3:** `hiring_manager`
> Quote: "Model complex SaaS data by integrating product events, CRM (Salesforce), and support data into clean, well-defined fact and dimension models."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical details about tool usage (dbt, Salesforce), data modeling approaches (fact/dimension), and business context that would only come from someone who has performed similar work.

### stakeholder_orientation

**Run 1:** `product`
> Quote: "Define and implement core business metrics (e.g. activation, engagement, retention) as reusable, versioned data assets"
> Verified: ✓ found in JD
> Reasoning: The explicit focus on defining product-specific metrics like activation, engagement, and retention indicates this role primarily supports product analytics use cases.

**Run 2:** `internal_data`
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents."
> Verified: ✓ found in JD
> Reasoning: The primary focus is building analytics infrastructure and enabling self-service consumption by data consumers, not directly supporting commercial, product decisions, or finance.

**Run 3:** `internal_data`
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining data infrastructure (semantic layer, transformation layer) to enable self-serve analytics for other internal data consumers rather than directly serving commercial, product, or finance teams.

⚠ **LLM inconsistency**: runs gave ['product', 'internal_data', 'internal_data']

### autonomy_level

**Run 1:** `strategic`
> Quote: "Own the transformation layer in dbt- design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company."
> Verified: ✓ found in JD
> Reasoning: The role uses strategic ownership language ('own', 'define', 'establish', 'build') indicating authority to set the direction for analytics architecture and data modeling standards.

**Run 2:** `strategic`
> Quote: "Own the transformation layer in dbt- design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company."
> Verified: ✓ found in JD
> Reasoning: The role is framed around ownership and defining how analytics infrastructure is delivered across the company, not executing pre-scoped work.

**Run 3:** `strategic`
> Quote: "Own the transformation layer in dbt- design, build, and maintain modular, well-tested data models that define how data is structured and consumed across the company."
> Verified: ✓ found in JD
> Reasoning: The role uses ownership language ('own'), direction-setting verbs ('define', 'establish and enforce'), and applies these to core responsibilities that shape the data infrastructure rather than executing predefined work.

### ai_role
**Run 1:** `ai_enabler` ✓
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents."
> Reasoning: Candidate builds semantic infrastructure that downstream AI systems (LLM agents) consume.

**Run 2:** `ai_enabler` ✓
> Quote: "supports downstream consumers, including LLM-based analytics agents"
> Reasoning: Candidate builds semantic layer and data infrastructure specifically designed for AI/LLM systems to consume.

**Run 3:** `ai_enabler` ✓
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents."
> Reasoning: Candidate builds semantic infrastructure that LLM-based agents consume, enabling AI capabilities downstream.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Establish and enforce best practices in testing, documentation, and data quality- making these part of the standard development lifecycle."
> Reasoning: Candidate owns establishing and enforcing testing practices as mandatory development lifecycle requirement.

**Run 2:** `responsibility` ✓
> Quote: "Establish and enforce best practices in testing, documentation, and data quality"
> Reasoning: Candidate owns quality and testing practices as core responsibility with enforcement authority.

**Run 3:** `responsibility` ✓
> Quote: "Establish and enforce best practices in testing, documentation, and data quality- making these part of the standard development lifecycle."
> Reasoning: Candidate owns establishing and enforcing testing practices as core responsibility across the org.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents."
> Reasoning: Emphasizes operational reliability for downstream consumers and systems, with no compliance or regulatory framing.

**Run 2:** `moderate` ✓
> Quote: "reliable abstraction over our data... well-tested data models"
> Reasoning: Framing emphasizes operational reliability and testing rigor rather than compliance or trust concerns.

**Run 3:** `moderate` ✓
> Quote: "Build and evolve our semantic layer- creating a reliable abstraction over our data that enables consistent KPI definitions and supports downstream consumers, including LLM-based analytics agents."
> Reasoning: Emphasis on reliability, consistency, and reliable downstream impact framed as operational quality practice rather than regulatory compliance.

