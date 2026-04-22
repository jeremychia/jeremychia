# Recruiter Call Prep — Senior Analytics Engineer - Finance & Operations at Pergolux LLC

**Application folder:** 2026-04-22_pergolux_senior-analytics-engineer-finance-operations
**Prepared:** 2026-04-22

---

## 1. What the recruiter is screening for

### Viability checklist
- **Expert SQL + dbt for scalable models** — Clearly covered: Vinted (end-to-end finance dbt models, production SSoT) and Tourlane (centralised dbt+Snowflake layer). Strong.
- **Finance domain depth: revenue recognition, COGS, EBITDA, logistics costs** — Clearly covered: Vinted shipping cost/revenue models, CGMA qualification, LucaNet consolidation projects. Chartered Accountant is a differentiator most candidates won't have.
- **ERP data integration experience** — Partial gap: no direct ERP (SAP/Oracle) data engineering in resume. LucaNet is EPM/consolidation-adjacent and SAP is in skills, but no "I built the ERP→warehouse pipeline" story. Prepare to address honestly.
- **Snowflake + Airbyte hands-on** — Snowflake covered via Tourlane. Airbyte is not in the resume. Be ready to bridge with experience integrating multi-source pipelines.
- **Comfort in ambiguous, fast-growing environments** — Covered: Tourlane startup experience ("developing systems"), Vinted scaling context. CGMA + Valedictorian signals structure-in-chaos capability.

### Soft skill and culture fit signals
The JD uses language like "leading", "establishing the foundation", "bringing structure", "comfort navigating uncertainty", and "align on metrics" — this signals a lean, high-autonomy team that has been operating with fragmented reporting and is now ready to do it properly. They want a confident IC who can self-direct and won't need hand-holding in an ambiguous environment. Mirror this by being decisive and specific on the call — speak in terms of "I would own X" and "I'd start by doing Y" rather than "it depends".

### Likely hard question
**"Our ERP is the primary data source — have you actually built pipelines from an ERP system before?"**
*Suggested response frame:* Be direct: "Not a full ERP ingestion pipeline end-to-end, but I've worked extensively with finance source systems — SAP at Keppel, LucaNet EPM at listed companies across APAC, Salesforce and Stripe at Tourlane. The translation challenge from messy source data into a clean, trusted financial model is exactly what I've done at Vinted. I'm confident I can ramp on the ERP-specific nuances quickly given the finance domain depth I already have."

---

## 2. Your Peak moment

> "At Vinted, I built and own the end-to-end shipping cost and revenue models in dbt and BigQuery — they're the single source of truth used by Finance Ops during month-end close, and I designed the control framework that detected carrier billing discrepancies and recovered €1.6 million in overcharges."

*Why this works:* It directly addresses Pergolux's #1 fear — fragmented, untrustworthy financial reporting — and shows you've already built exactly what they're trying to hire for, with a dramatic quantified result.

---

## 3. STAR story prompts

For each theme below, use the STAR+Spark structure: Situation/Task (20%), Action — use "I" not "we" (60%), Result with a number (20%), Learning/Spark (1 sentence).

### Theme 1: Building a Finance Single Source of Truth from scratch
**Source bullet:** "Own end-to-end finance-ready shipping cost and revenue models in dbt, BigQuery, and Looker, used as the single source of truth by Finance Ops and Group Reporting during month-end close."
**Prompt:** Prepare a story about joining a team where Finance didn't trust the data, where you identified the gaps, designed the model architecture, and drove adoption. End with what made Finance actually change their behaviour (stop using spreadsheets / start trusting the model).

### Theme 2: Navigating ambiguity and bringing structure to developing systems
**Source bullet:** "Built a centralised data transformation layer in dbt and Snowflake, integrating data from Salesforce, Stripe, Twilio, and backend systems to power finance and operational analytics."
**Prompt:** Prepare a story about arriving at a company (Tourlane) with no mature data infrastructure where you had to simultaneously figure out the requirements, build the models, and deliver business value quickly. End with how you decided what to prioritise first and what you'd do differently.

### Theme 3: Finance domain expertise driving data decisions
**Source bullet:** "Embedded a risk-based control framework into core datasets, detecting carrier billing discrepancies and recovering €1.6m in overcharges."
**Prompt:** Prepare a story about a time your accounting/finance background (not just your engineering skills) was the reason you caught something or designed something better. End with what a pure engineer would have missed and what the CA training gave you.

---

## 4. Company research findings

### Data stack and engineering culture
No public engineering or data blog found. Pergolux does not appear to have published anything about their internal data stack. The JD itself (dbt, Snowflake, Airbyte, Python) is the most concrete signal available. Their supply chain job postings reference ERP and WMS experience, confirming ERP integration is a real and active need — not aspirational.

### Data team size and structure
No public data team headcount found. Given the JD scope (Finance, Operations, and Leadership as stakeholders), and that this is the only analytics engineering role visibly open, this is most likely a small central data team or a first dedicated Finance AE hire. Expect high autonomy and broad scope from day one.

### Recent news and growth signals
Pergolux had a strong 2025: 180% year-over-year growth ([PERGOLUX press release](https://markets.financialcontent.com/wral/article/abnewswire-2025-12-31-pergolux-ends-2025-with-us-expansion-smart-pergola-launch-and-roadshow-tour)), surpassed 100,000 pergolas sold across 14 countries ([same source](https://markets.financialcontent.com/wral/article/abnewswire-2025-12-31-pergolux-ends-2025-with-us-expansion-smart-pergola-launch-and-roadshow-tour)), expanded into Southern California with a new showroom and light manufacturing facility ([October 2025](https://markets.financialcontent.com/wral/article/abnewswire-2025-12-31-pergolux-ends-2025-with-us-expansion-smart-pergola-launch-and-roadshow-tour)), and launched the S3 Series smart pergola (app/voice-controlled, best-selling US model) ([same source](https://markets.financialcontent.com/wral/article/abnewswire-2025-12-31-pergolux-ends-2025-with-us-expansion-smart-pergola-launch-and-roadshow-tour)). They are entering 2026 planning further US showroom expansion and increased manufacturing capacity ([same source](https://markets.financialcontent.com/wral/article/abnewswire-2025-12-31-pergolux-ends-2025-with-us-expansion-smart-pergola-launch-and-roadshow-tour)). This pace of growth — new geographies, new product lines, new fulfilment centres — directly explains why they need demand forecasting models and a Finance SSoT now. The data complexity is real and growing fast.

### Role-specific insight
ERP identity not publicly confirmed. Based on supply chain job postings referencing ERP/WMS experience and their operational profile (physical product, logistics, warehousing), candidates for similar roles at comparable companies typically encounter NetSuite or SAP. Worth asking directly on the call: "Which ERP are you currently running?" — this is a natural, informed question that signals you're already thinking about the integration.

### Suggested opening hook
> "I had a look at what you've been building — 180% growth last year, 100,000 pergolas across 14 countries, and now a West Coast manufacturing footprint ([PERGOLUX 2025 announcement](https://markets.financialcontent.com/wral/article/abnewswire-2025-12-31-pergolux-ends-2025-with-us-expansion-smart-pergola-launch-and-roadshow-tour)). That kind of operational scale creates exactly the kind of financial data complexity I find most interesting: COGS that spans multiple fulfilment locations, logistics costs that need to roll up cleanly into EBITDA. That's the problem I want to work on."

---

## 5. Opening and closing

### Opening (first 60 seconds)
Use the suggested hook above — it references real, specific numbers from Pergolux's own press releases.

### Closing statement
> "I'm genuinely excited about this role — building a Finance Single Source of Truth from scratch for a fast-growing operations business is exactly the kind of high-impact, end-to-end work I do best, and my Chartered Accountant background means I can engage at the finance domain level that this role clearly demands. I'm available to move forward quickly and happy to do a technical screen whenever works for the team. The thing I'd want you to take away from this call is: I've already built what you're trying to hire for."

---

## 6. Question to ask

> "If you hired the perfect person for this role and they had a great first 90 days — what would they have shipped, and what would Finance and Ops be saying about them that they can't say today?"

*Why this question works:* It forces the recruiter to visualise you succeeding in the role, and signals you are thinking about impact from day one — not just salary and perks.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story before moving on — prevents rambling and gives the recruiter time to finish their notes.
- **Use "I" not "we"** when describing achievements — recruiters need to assess your individual contribution.
- **Salary / notice period** — the range is €60k–€80k estimated. You are based in Berlin. Be ready to state your range confidently. If pushed early: "I'm flexible depending on the full package — can you share the budgeted range for the role?"
