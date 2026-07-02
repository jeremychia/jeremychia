# Trace: 2026-07-01_jtl-software_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — JTL Software

**URL:** https://jtl-software-gmbh.jobs.personio.de/job/2684130
**Location:** Remote (Germany)
**Date Posted:** 2026-07-01

---

Senior Analytics Engineer (w/m/d) at JTL Software

Mobil, Vollzeit, Festanstellung (Mobile, Full-time, Permanent)

About JTL
JTL stands as a leading e-commerce software provider in German-speaking regions, operating with approximately 450 employees across the group and serving over 50,000 customers. The organisation develops scalable solutions for online commerce, spanning from ERP systems to shop and marketplace integrations.

Your Responsibilities
- Structuring raw data from JTL's inventory management into clean, documented data models
- Owning the data foundation for a new AI-powered BI product
- Improving query performance and data quality
- Collaborating with development, product, and pilot customers to translate business requirements into viable data models
- Building complex data models with high quality and availability standards

Required Qualifications
- Several years of practical data experience with proficiency in SQL and Python
- BI/analytics background
- Ability to communicate technical concepts with diverse stakeholders
- Du kommunizierst fließend auf Deutsch und sicher auf Englisch (Fluent German and secure English communication required)

Preferred Skills
- dbt framework knowledge
- Basic data science and machine learning understanding
- ERP system data experience
- Azure cloud infrastructure familiarity
- Multi-tenant architecture understanding

Benefits
- Remote-first within Germany with up to 180 days annual remote work eligibility
- Food allowance up to €115 net monthly
- Ergonomic workspace stipend for home office setup
- Team events, company offsites, and seasonal celebrations
- EGYM Wellpass and Job Rad subsidies
- Financial benefits including capital formation payments and occupational pension provisions

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 3 | 3 | 3 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | recruiter | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | product | 33% |
| autonomy_level | mixed | mixed | mixed | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | absent | absent | 33% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals emphasize quality, documentation, and standards with no velocity language present.

**Run 2:** `rigour`
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize high quality and availability standards as core expectations with no countervailing speed or velocity language.

**Run 3:** `rigour`
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality, documentation, and standards throughout rather than speed or iteration pace.

### domain_risk

**Run 1:** `moderate`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: E-commerce/SaaS context focused on business intelligence and operational analytics with no financial reporting, compliance, or regulatory language.

**Run 2:** `moderate`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: This is a business intelligence and analytics role for an e-commerce SaaS company, without regulatory, compliance, or financial reporting language typical of high-risk domains.

**Run 3:** `moderate`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: E-commerce and software sector with business intelligence focus affects business decisions without explicit financial reporting or regulatory compliance drivers.

### collaboration_width

**Run 1:** `3`
> Quote: "Collaborating with development, product, and pilot customers"
> Verified: ✓ found in JD
> Reasoning: Three named partner functions explicitly listed: development team, product team, and pilot customers.

**Run 2:** `3`
> Quote: "development; product; pilot customers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three distinct partner teams in the collaboration statement: development team, product team, and pilot customers as external collaborators.

**Run 3:** `3`
> Quote: "development; product; pilot customers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named partner teams explicitly listed: development team, product team, and pilot customers as external collaboration partners.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: New product initiative within an established company (450 employees, 50,000 customers) with existing development and product teams, suggesting growing infrastructure rather than greenfield startup.

**Run 2:** `mid`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The focus on owning a data foundation for a new product indicates the data function is expanding within an established company, characteristic of a mid-stage data team.

**Run 3:** `mid`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: An established 450-person company with 50,000 customers scaling into a new product area signals mid-stage growth rather than establishing the data function from zero.

### jd_authorship

**Run 1:** `recruiter`
> Quote: "Structuring raw data from JTL's inventory management into clean, documented data models"
> Verified: ✓ found in JD
> Reasoning: Generic action verbs and templated structure; no named tools in responsibilities, no scale numbers, no technical methodology specificity typical of hiring manager authorship.

**Run 2:** `mixed`
> Quote: "Structuring raw data from JTL's inventory management into clean, documented data models"
> Verified: ✓ found in JD
> Reasoning: Some responsibilities show domain-specific technical knowledge (ERP inventory data context) while others use generic collaboration language, indicating mixed authorship.

**Run 3:** `mixed`
> Quote: "Structuring raw data from JTL's inventory management into clean, documented data models"
> Verified: ✓ found in JD
> Reasoning: Specific context about JTL's inventory data and product requirements indicates hiring manager input, while collaboration language remains generic.

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: Primary responsibility is building and owning the data infrastructure layer itself, not serving commercial, product, or finance teams directly.

**Run 2:** `internal_data`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The central responsibility is building the data platform and foundation that other teams will consume, rather than providing analytics insights or serving commercial stakeholders directly.

**Run 3:** `product`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role is primarily focused on building data infrastructure that powers a new product offering, serving product teams and pilot customers.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'product']

### autonomy_level

**Run 1:** `mixed`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: Role has strategic ownership of the data foundation but operates within constraints of translating business requirements from product and development teams.

**Run 2:** `mixed`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of the data platform architecture with execution in collaborating with product and customers to translate their requirements into models.

**Run 3:** `mixed`
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of the data foundation with execution within a scoped product initiative defined by development and product teams.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: Company builds AI BI products but no AI skill is explicitly required of the candidate; basic ML understanding listed as preferred but is vague and not about candidate AI tool usage or enablement work.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: While the company builds an AI-powered BI product, the JD contains no explicit expectations for the candidate to use AI tools or build AI-ready data infrastructure.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The company builds AI products, but the job description does not require candidates to demonstrate AI tool usage or skills; basic ML knowledge in preferred skills is domain knowledge, not AI capability.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Improving query performance and data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as a responsibility the candidate actively improves, using an action verb in the responsibilities section.

**Run 2:** `absent`
> Quote: "Improving query performance and data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is mentioned as a general concern but without a named testing framework, data contracts, or ownership responsibility; no testing tools appear in the requirements list.

**Run 3:** `absent`
> Quote: "Improving query performance and data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is mentioned as a general goal but no testing frameworks, data contracts, or quality practices are specified or framed as owned responsibilities.

⚠ **LLM inconsistency**: runs gave ['responsibility', 'absent', 'absent']

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: Quality and availability standards signal concern about operational reliability, though this is secondary to the primary capability-building and delivery mission.

**Run 2:** `moderate`
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and quality standards but frames them as attributes of good systems design rather than preventing compliance risk or stakeholder trust failures.

**Run 3:** `moderate`
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: Operational reliability through quality and availability standards is explicitly required but secondary to the primary goal of building a new product.
