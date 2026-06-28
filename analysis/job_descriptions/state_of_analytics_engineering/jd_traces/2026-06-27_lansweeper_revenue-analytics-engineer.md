# Trace: 2026-06-27_lansweeper_revenue-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Revenue Analytics Engineer — Lansweeper

**Location:** London, Greater London, United Kingdom (Hybrid) + 2 more
**Date Posted:** 2026-06-27
**Salary:** €107,000–€174,000 per year

---

Revenue Analytics Engineer
Hybrid
London, Greater London, United Kingdom•
+2 more
€107,000 - €174,000 per year
Operations
A high-impact role at the intersection of data, finance, and go-to-market strategy. The opportunity to shape how a growing SaaS company measures and steers its revenue.

About Lansweeper 

Lansweeper is a leading IT asset management company that helps organizations gain complete visibility into their IT landscape. Our technology discovers, inventories, and manages every IT asset across on-premises, cloud, and IoT environments. As we grow through new products and market expansion, revenue analytics is becoming critical to steer the business forward. 

What Success Looks Like 

C-level decisions to optimize growth are based on revenue metrics and insights, as they are highly trusted facts on the evolution of the business 

Revenue metrics are structured so they are relevant for board-level insights 

Key trends in revenue metrics are explained by linking back to sales and finance processes, ensuring the right strategic decisions for growing the company are taken 

Forecasting for key revenue metrics is in place and used to steer go-to-market actions 

The Real Challenge 

The sales organization is moving quickly and needs revenue facts to understand the success of its campaigns and to plan new sales plays 

The market is changing and so is our product — we need to allocate sales and marketing efforts where it matters most for growth 

Revenue metrics are sourced from multiple systems, have historic complexity due to acquisitions and system migrations, and data quality varies over time 

What You Will Do 

Build, maintain, and improve the revenue data models that power executive-level reporting and board-ready metrics 

Reconcile revenue data across systems of record (CRM, billing, ERP) and ensure a single source of truth for financial KPIs 

Design and deliver dashboards and reports that translate complex revenue data into clear, actionable insights for sales, finance, and leadership 

Partner with sales operations and finance to understand changing business processes and reflect them accurately in revenue analytics 

Develop and maintain forecasting models for key revenue metrics to support go-to-market planning 

Investigate and explain trends, anomalies, and shifts in revenue data, linking them back to underlying business drivers 

Proactively improve data quality and integrity across revenue-related data pipelines 

Job requirements
Required 

Experience with financial metrics reporting — you know how revenue, bookings, churn, and related KPIs are defined and measured 

Understanding of subscription sales processes — you are familiar with concepts like ARR, MRR, expansion, contraction, and renewal cycles 

Strong SQL skills — you can write, optimize, and debug complex queries against large datasets 

Experience in reconciling systems of record — you have dealt with data mismatches between CRM, billing, and finance systems and know how to resolve them 

Analytical mindset with the ability to translate data into business narratives that support decision-making 

Nice to Have 

Experience with SaaS KPI reporting (e.g., net revenue retention, LTV, CAC payback) 

Hands-on experience with Snowflake, dbt, and/or Power BI 

Familiarity with data modeling best practices (dimensional modeling, slowly changing dimensions)

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | high | high | 100% |
| collaboration_width | 4 | 4 | 2 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | mixed | finance | mixed | 33% |
| autonomy_level | mixed | execution | strategic | 0% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Reconcile revenue data across systems of record (CRM, billing, ERP) and ensure a single source of truth for financial KPIs"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reconciliation, single source of truth, and financial accuracy; the only speed references describe the sales organization's pace, not the role's orientation.

**Run 2:** `rigour`
> Quote: "Proactively improve data quality and integrity across revenue-related data pipelines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, integrity, and accurate reconciliation as core expectations, which are rigour signals.

**Run 3:** `rigour`
> Quote: "Reconcile revenue data across systems of record (CRM, billing, ERP) and ensure a single source of truth for financial KPIs"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize accuracy, reconciliation, and data integrity as core expectations, with rigour signals (single source of truth, data quality, reconciliation) substantially outweighing any velocity language.

### domain_risk

**Run 1:** `high`
> Quote: "C-level decisions to optimize growth are based on revenue metrics and insights, as they are highly trusted facts on the evolution of the business"
> Verified: ✓ found in JD
> Reasoning: Data errors directly affect C-level financial decision-making and board-level reporting, placing them at high stakes.

**Run 2:** `high`
> Quote: "C-level decisions to optimize growth are based on revenue metrics and insights, as they are highly trusted facts on the evolution of the business"
> Verified: ✓ found in JD
> Reasoning: Revenue data directly affects C-level and board decisions on company direction, indicating high financial and strategic consequence of errors.

**Run 3:** `high`
> Quote: "C-level decisions to optimize growth are based on revenue metrics and insights, as they are highly trusted facts on the evolution of the business"
> Verified: ✓ found in JD
> Reasoning: Data errors directly affect financial reporting and executive/board decision-making, with explicit language around board-ready metrics and financial KPIs.

### collaboration_width

**Run 1:** `4`
> Quote: "sales operations; finance; sales; marketing"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named functions are explicitly listed: sales operations (partnership), finance (partnership), sales (audience), and marketing (allocation decisions).

**Run 2:** `4`
> Quote: "sales operations; finance; sales; marketing"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names four distinct collaboration partners: sales operations, finance, sales, and marketing.

**Run 3:** `2`
> Quote: "Partner with sales operations and finance"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names two distinct partner functions: Sales Operations and Finance, both mentioned as key collaborators.

⚠ **LLM inconsistency**: runs gave ['4', '4', '2']

### data_team_maturity

**Run 1:** `mid`
> Quote: "revenue metrics are sourced from multiple systems, have historic complexity due to acquisitions and system migrations, and data quality varies over time"
> Verified: ✓ found in JD
> Reasoning: Multiple established systems with complex legacy data and ongoing improvement needs indicate a mid-stage function—operational but growing.

**Run 2:** `mid`
> Quote: "Build, maintain, and improve the revenue data models that power executive-level reporting and board-ready metrics"
> Verified: ✓ found in JD
> Reasoning: The combination of building, maintaining, and improving existing models indicates a mid-stage data function that has produced something but requires scaling and refinement.

**Run 3:** `mid`
> Quote: "Build, maintain, and improve the revenue data models that power executive-level reporting and board-ready metrics"
> Verified: ✓ found in JD
> Reasoning: The responsibilities show existing revenue infrastructure being improved and scaled as the company grows, not starting from zero, indicating a team in the growth/scaling phase.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Experience with subscription sales processes — you are familiar with concepts like ARR, MRR, expansion, contraction, and renewal cycles"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific SaaS metrics and subscription domain knowledge embedded throughout the requirements indicate the writer has done revenue analytics work.

**Run 2:** `hiring_manager`
> Quote: "Understanding of subscription sales processes — you are familiar with concepts like ARR, MRR, expansion, contraction, and renewal cycles"
> Verified: ✓ found in JD
> Reasoning: This level of specificity about subscription economics and SaaS-specific concepts indicates deep technical knowledge from someone who has done the role.

**Run 3:** `hiring_manager`
> Quote: "Experience with financial metrics reporting — you know how revenue, bookings, churn, and related KPIs are defined and measured"
> Verified: ✓ found in JD
> Reasoning: The JD demonstrates specific technical knowledge of SaaS metrics (ARR, MRR, expansion, churn, LTV, CAC), subscription business concepts, and specific systems (CRM, billing, ERP, Snowflake, dbt), indicating deep domain knowledge from someone who performs this work.

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "dashboards and reports that translate complex revenue data into clear, actionable insights for sales, finance, and leadership"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves finance stakeholders (C-level, board-ready metrics, financial KPIs) and commercial stakeholders (sales operations, go-to-market forecasting) with genuinely equal emphasis.

**Run 2:** `finance`
> Quote: "C-level decisions to optimize growth are based on revenue metrics and insights, as they are highly trusted facts on the evolution of the business"
> Verified: ✓ found in JD
> Reasoning: The primary success criteria emphasize building trusted revenue data for C-level and board-level decision-making, indicating finance/executive orientation.

**Run 3:** `mixed`
> Quote: "Design and deliver dashboards and reports that translate complex revenue data into clear, actionable insights for sales, finance, and leadership"
> Verified: ✓ found in JD
> Reasoning: The role is framed at the intersection of both Finance (executive/board reporting, financial KPIs) and Commercial (go-to-market strategy, sales operations), with both orientations genuinely weighted in responsibilities.

⚠ **LLM inconsistency**: runs gave ['mixed', 'finance', 'mixed']

### autonomy_level

**Run 1:** `mixed`
> Quote: "Build, maintain, and improve the revenue data models that power executive-level reporting and board-ready metrics; Partner with sales operations and finance to understand changing business processes and reflect them accurately"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role combines strategic building and designing of analytics capabilities with reactive partnership where direction comes from stakeholder business process changes.

**Run 2:** `execution`
> Quote: "Partner with sales operations and finance to understand changing business processes and reflect them accurately in revenue analytics"
> Verified: ✓ found in JD
> Reasoning: The responsibilities indicate the role responds to business processes and requirements defined by others, executing technical delivery rather than setting strategic direction.

**Run 3:** `strategic`
> Quote: "The opportunity to shape how a growing SaaS company measures and steers its revenue"
> Verified: ✓ found in JD
> Reasoning: The role is described as shaping how the company measures revenue, indicating direction-setting authority for the revenue analytics function rather than executing direction set by others.

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'strategic']
