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

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | recruiter | recruiter | 33% | ✗ |
| stakeholder_orientation | product | product | internal_data | product | 33% | ✓ |
| autonomy_level | strategic | mixed | execution | mixed | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | responsibility | 33% | ✗ |
| loss_aversion_framing |  | moderate | none | moderate | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes quality, documentation, and availability standards repeatedly with no velocity language present.

**Run 2:** `rigour` ✓
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: The repeated emphasis on data quality, documentation, and standards in responsibilities signals rigour as the primary orientation, with no velocity language like 'fast-paced' or 'rapid delivery' present.

**Run 3:** `rigour` ✓
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: Quality, documentation, and availability standards are framed as core responsibilities throughout rather than speed or iteration pace.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: E-commerce SaaS context affects business decisions but carries no regulatory, compliance, or financial reporting consequences typical of high-risk domains.

**Run 2:** `moderate` ✓
> Quote: "Collaborating with development, product, and pilot customers to translate business requirements into viable data models"
> Verified: ✓ found in JD
> Reasoning: This is a B2B SaaS BI product context serving customers with no explicit financial reporting or regulatory language, placing it in moderate operational risk rather than high compliance risk.

**Run 3:** `moderate` ✓
> Quote: "leading e-commerce software provider in German-speaking regions, operating with approximately 450 employees across the group and serving over 50,000 customers"
> Verified: ✓ found in JD
> Reasoning: E-commerce SaaS serving business customers implies business intelligence and operational decision-making, not financial reporting or regulatory compliance.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "development, product, and pilot customers"
> Verified: ✓ found in JD
> Reasoning: Three distinct named partners explicitly listed as collaboration targets in the responsibilities section.

**Run 2:** `3` ✓
> Quote: "development, product, and pilot customers"
> Verified: ✓ found in JD
> Reasoning: The responsibilities explicitly name three distinct collaboration partners: development team, product team, and pilot customers as external partners.

**Run 3:** `3` ✓
> Quote: "development; product; pilot customers"
> Verified: ✓ found in JD
> Reasoning: Development team, product team, and pilot customers are explicitly named as distinct collaboration partners in the responsibilities.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The organization is established (450 employees, 50,000+ customers, existing ERP infrastructure) but launching a new BI product initiative suggests growth and expansion rather than early-stage build.

**Run 2:** `mid` ✗
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The company has existing data infrastructure from inventory management but is building a new analytics product, signaling growth of the data function rather than early-stage or mature scale.

**Run 3:** `mid` ✗
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role involves establishing infrastructure for a new product component, but the parent company and existing data infrastructure are already established.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Structuring raw data from JTL's inventory management into clean, documented data models"
> Verified: ✓ found in JD
> Reasoning: Specific context about JTL's inventory systems and multi-tenant architecture suggests domain knowledge, but responsibilities also contain generic collaboration verbs typical of recruiter writing.

**Run 2:** `recruiter` ✗
> Quote: "Collaborating with development, product, and pilot customers to translate business requirements into viable data models"
> Verified: ✓ found in JD
> Reasoning: The generic action verbs and lack of specific technical context or named tools in the responsibilities section signals recruiter authorship rather than hiring manager specificity.

**Run 3:** `recruiter` ✗
> Quote: "Collaborating with development, product, and pilot customers to translate business requirements into viable data models"
> Verified: ✓ found in JD
> Reasoning: Boilerplate collaboration and translation language without specific technical detail about data models, scale, or methodology suggests recruiter authorship.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['mixed', 'recruiter', 'recruiter']

### stakeholder_orientation
**Manual:** `product`

**Run 1:** `product` ✓
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is to support a product initiative (BI product) with product and pilot customers as key collaboration partners.

**Run 2:** `internal_data` ✗
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is establishing the data platform and analytics infrastructure that will serve decision-makers, making internal data infrastructure the primary stakeholder orientation.

**Run 3:** `product` ✓
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The role exists to build data infrastructure for a new BI product serving the internal product team.

⚠ **LLM inconsistency**: runs gave ['product', 'internal_data', 'product']

### autonomy_level
**Manual:** `strategic`

**Run 1:** `mixed` ✗
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: The candidate owns the data foundation strategy (strategic) but executes against product team requirements and customer feedback (execution).

**Run 2:** `execution` ✗
> Quote: "Collaborating with development, product, and pilot customers to translate business requirements into viable data models"
> Verified: ✓ found in JD
> Reasoning: While the role includes 'owning' the data foundation, the bulk of responsibilities frame execution of a scoped technical initiative (translating requirements into data models) rather than setting direction or strategy.

**Run 3:** `mixed` ✗
> Quote: "Owning the data foundation for a new AI-powered BI product"
> Verified: ✓ found in JD
> Reasoning: Ownership implies strategic autonomy over the data domain, while collaboration with product and customers on requirements suggests execution in service of business needs.

⚠ **Disagreement**: manual=`strategic` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The company builds an AI-powered BI product but no AI skill, tool usage, or AI infrastructure capability is expected of the candidate.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: While the product is AI-powered, the candidate's responsibilities focus on data modeling and quality, with only 'basic' ML understanding listed as preferred, not as a core expectation for the role.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The company's product is AI-powered, but the candidate's role is standard data modelling without explicit AI infrastructure, coding tool usage, or AI-ready data expectations.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Improving query performance and data quality"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as an outcome to achieve, not as a testing responsibility or framework to own or define; no testing tools or observability practices are mentioned.

**Run 2:** `absent` ✗
> Quote: "No testing framework signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions data quality and high standards as requirements but does not reference testing frameworks, data contracts, or ownership of quality practices.

**Run 3:** `responsibility` ✗
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: The candidate is accountable for building and maintaining quality and availability standards as core responsibilities, not just using testing tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

⚠ **LLM inconsistency**: runs gave ['absent', 'absent', 'responsibility']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Building complex data models with high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and quality standards are core concerns, but there is no compliance, regulatory, or stakeholder trust framing that would indicate high loss aversion.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes quality and availability standards as delivery requirements, not as safeguards against regulatory, compliance, or stakeholder trust risks.

**Run 3:** `moderate` ✗
> Quote: "high quality and availability standards"
> Verified: ✓ found in JD
> Reasoning: Availability standards signal operational reliability concerns, but lack regulatory, compliance, or stakeholder-trust framing typical of high loss aversion.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'moderate']
