# Trace: 2026-07-01_henkel_business-intelligence-developer

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Developer — Henkel

**URL:** https://henkel.csod.com/ux/ats/careersite/1/home?c=henkel&lang=en-US#/requisition/86014&source=LinkedIn
**Location:** Bratislava, Slovakia (Hybrid)
**Date Posted:** 2026-07-01
**Salary:** 2,000–2,600 EUR

---

Business Intelligence Developer at Henkel

Locations: Bratislava, Slovakia
Job ID: 26098076
Posted: 6/30/2026

About this Position

What you'll do:
- Play a key role in development of advanced analytical tools in Power BI
- Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department
- Utilise and combine various data sources, master understanding of the data and underlying financial processes
- Identify opportunities to streamline reporting activities
- Manage your projects and collaborate with worldwide Henkel financial and technical community

What makes you a good fit:
- Strong analytical thinking and ability to translate complex business requirements into Business Intelligence solutions
- Advanced knowledge of Power BI, DAX, Power Query M formula language and MS Excel
- Experience and interest in SQL or Databricks is welcome
- Focus on detail, precision and working transparently with managing priorities independently
- Interest in combining BI acumen with finance & business understanding
- Curiosity and growth mindset, willingness to actively develop and apply new capabilities in practice

Some perks of joining Henkel:
- Flexible work scheme with flexible hours, hybrid work model and up to 30 days per year for remote work abroad
- Diverse national and international growth opportunities
- Globally applicable well-being standards, including health and preventive care programs
- Gender-neutral parental leave for a minimum of 8 weeks
- Employee Share Plan with voluntary investment and Henkel matching shares
- 13th salary, incentives
- Cafeteria benefit system, Multisport card
- Henkel shop and Henkel nursery school
- Extra paid days off for special events, referral and relocation bonus
- Salary: €2,000 – €2,600 gross per month

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 3 | 4 | 0% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | mixed | recruiter | 33% |
| stakeholder_orientation | product | mixed | finance | 0% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | absent | absent | 100% |
| loss_aversion_framing | moderate | none | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Focus on detail, precision and working transparently with managing priorities independently"
> Verified: ✓ found in JD
> Reasoning: The explicit emphasis on precision and detail as core expectations, combined with mastery of underlying financial processes, drives this classification with no velocity language present.

**Run 2:** `rigour`
> Quote: "Focus on detail, precision and working transparently with managing priorities independently"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes precision, detail, and mastery over speed or agility, with no velocity or fast-paced language present.

**Run 3:** `rigour`
> Quote: "Focus on detail, precision and working transparently with managing priorities independently"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes precision and detail over pace, with no language about speed, iteration, or rapid delivery.

### domain_risk

**Run 1:** `moderate`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: The financial KPI focus suggests business decision support for a specific department without explicit regulatory, compliance, or formal financial reporting language that would elevate to high.

**Run 2:** `moderate`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: Financial KPIs represent business-critical analysis affecting management decisions without explicit regulatory or compliance framing.

**Run 3:** `moderate`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: Financial KPIs for a major corporation carry moderate risk of impacting business decisions, but the JD lacks explicit compliance or regulatory language.

### collaboration_width

**Run 1:** `1`
> Quote: "Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named department is identified as a collaboration partner; 'worldwide Henkel financial and technical community' is too vague to count as distinct teams.

**Run 2:** `3`
> Quote: "Product & Technology management department; financial and technical community"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct collaborative functions are explicitly named: Product & Technology management, financial community, and technical community.

**Run 3:** `4`
> Quote: "Product & Technology management department; financial and technical community"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names four distinct partner functions: Product, Technology, Finance, and Technical.

⚠ **LLM inconsistency**: runs gave ['1', '3', '4']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Identify opportunities to streamline reporting activities"
> Verified: ✓ found in JD
> Reasoning: The existence of reporting activities to streamline, combined with named tools (Power BI, data sources), indicates an established function rather than early-stage greenfield.

**Run 2:** `mid`
> Quote: "Play a key role in development of advanced analytical tools in Power BI"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities and mention of advanced existing infrastructure suggests an established data function, not early-stage.

**Run 3:** `mid`
> Quote: "Play a key role in development of advanced analytical tools in Power BI"
> Verified: ✓ found in JD
> Reasoning: Power BI is established and actively used with existing multiple data sources and reporting infrastructure, but the role is about development rather than operating a mature platform.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Play a key role in development of advanced analytical tools in Power BI"
> Verified: ✓ found in JD
> Reasoning: The JD combines technical specificity (named tool Power BI, financial KPI context for a specific department) with generic action verbs and collaboration language typical of recruiter-written sections.

**Run 2:** `mixed`
> Quote: "Advanced knowledge of Power BI, DAX, Power Query M formula language and MS Excel"
> Verified: ✓ found in JD
> Reasoning: Specific tool naming and business context (financial KPIs, Product & Technology department) suggest hiring manager input, but generic responsibility verbs suggest recruiter involvement.

**Run 3:** `recruiter`
> Quote: "Identify opportunities to streamline reporting activities"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic boilerplate verbs like 'identify', 'provide', 'manage', and 'collaborate' without technical specificity about actual work context or scale.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation

**Run 1:** `product`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: The primary stakeholder explicitly named is the Product & Technology management department, making this product-oriented analytics despite the financial KPI subject matter.

**Run 2:** `mixed`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: The role serves Product (Product & Technology management) and Finance (financial KPIs) equally, making this mixed rather than primarily one or the other.

**Run 3:** `finance`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: The role explicitly centers on financial KPIs and financial processes, making financial reporting the primary work domain.

⚠ **LLM inconsistency**: runs gave ['product', 'mixed', 'finance']

### autonomy_level

**Run 1:** `execution`
> Quote: "Manage your projects and collaborate with worldwide Henkel financial and technical community"
> Verified: ✓ found in JD
> Reasoning: Action verbs emphasise project delivery, collaboration, and support rather than strategic direction-setting or defining the analytics function.

**Run 2:** `execution`
> Quote: "Provide overviews and analytical insights on various financial KPIs for the Product & Technology management department"
> Verified: ✓ found in JD
> Reasoning: The role delivers against priorities set by Product & Technology management and Finance departments rather than setting strategic direction.

**Run 3:** `execution`
> Quote: "Manage your projects and collaborate with worldwide Henkel financial and technical community"
> Verified: ✓ found in JD
> Reasoning: The role is framed as execution and collaboration rather than strategic ownership, with project-level autonomy but not direction-setting authority.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mentions of AI tools, AI-assisted coding, agentic workflows, or AI infrastructure requirements appear anywhere in the JD.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI skills, tools, or capabilities expected of the candidate.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI tooling, coding assistants, or AI infrastructure expectations.

### testing_framing

**Run 1:** `absent`
> Quote: "No testing or data quality signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of testing frameworks, data contracts, data quality practices, or observability standards.

**Run 2:** `absent`
> Quote: "No testing or data quality ownership signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of testing, data quality frameworks, observability, or data contracts.

**Run 3:** `absent`
> Quote: "No testing or data quality signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD does not mention testing frameworks, data quality practices, observability, or data contracts.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Focus on detail, precision and working transparently with managing priorities independently"
> Verified: ✓ found in JD
> Reasoning: The emphasis on precision and detail reflects concern for preventing data errors and operational quality without compliance, regulatory, or high-level risk language.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is framed in delivery and capability terms with precision presented as a work style preference, not as a risk mitigation mechanism.

**Run 3:** `moderate`
> Quote: "Focus on detail, precision and working transparently with managing priorities independently"
> Verified: ✓ found in JD
> Reasoning: Operational precision is expected in financial work, but without explicit risk, compliance, or loss-aversion language, indicating moderate rather than high risk consciousness.

⚠ **LLM inconsistency**: runs gave ['moderate', 'none', 'moderate']
