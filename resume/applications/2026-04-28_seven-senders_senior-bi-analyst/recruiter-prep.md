# Recruiter Call Prep — Senior Business Intelligence Analyst at Seven Senders

**Application folder:** 2026-04-28_seven-senders_senior-bi-analyst
**Prepared:** 2026-05-10

---

## 1. What the recruiter is screening for

### Viability checklist

- **dbt expertise (Jinja, macros, testing)** — Clearly covered: owns Vinted shipping dbt models with Jinja macros and DRY abstractions; raised test coverage <1%→50%+ in 4 weeks; testing guide adopted by teammates.
- **Production-grade SQL at multi-billion row scale** — Clearly covered: 75% runtime reduction, 1.5TB/day query cut via incremental dbt redesign across multi-billion row shipping datasets at Vinted.
- **Looker end-to-end (backend to self-serve)** — Clearly covered: Vinted Looker for Finance Ops and Group Reporting; Tourlane dashboards saving 5 FTE days/month.
- **Discovery-to-Delivery ownership** — Clearly covered: Tourlane sole analyst owning Finance Data Products roadmap end-to-end; Vinted "owns" shipping dbt + Looker layer.
- **Junior mentoring and data culture** — Clearly covered: mentored 3 at Tourlane; ReDI School teaching with 80% progression rate; testing guide independently adopted; dbt Meetup hosted.

### Soft skill and culture fit signals

The JD language — "data culture quality", "code reviews, coaching, documentation", "translator between engineering and business" — signals a pragmatic, quality-focused team that wants someone who multiplies capability, not just ships models. "Independently lead" and "full ownership from definition to delivery" confirm they are not looking for an executor. Mirror this by being direct and concrete: name what you own, not what you contributed to.

### Likely hard question

**"You're in a specialised role at a large company like Vinted. Why move to a smaller logistics company like Seven Senders?"**
*Suggested response frame:* Scale isn't the draw — ownership is. Vinted is a great stack but the domain is narrowing. Seven Senders is a transaction-heavy, multi-carrier platform where the data problems are operationally complex. The per-parcel model means margin, carrier performance, and SLA are live business questions, not quarterly reports — that's a more direct feedback loop.

---

## 2. Your Peak moment

> "At Vinted, I redesigned our incremental dbt models across multi-billion row shipping datasets — cut runtime by 75% and removed 1.5TB of daily query volume, which reduced compute costs by 15% while maintaining our SLAs."

*Why this works:* This directly addresses the JD's explicit fear — expensive, slow queries on large datasets — with a concrete, quantified win in exactly the same domain (shipping data).

---

## 3. STAR story prompts

For each theme, use STAR+Spark: Situation/Task (20%), Action — use "I" not "we" (60%), Result with a number (20%), Learning/Spark (1 sentence).

### Theme 1: Cost-optimised dbt at scale
**Source bullet:** "75% runtime reduction on multi-billion row shipping datasets; 1.5TB/day query cut via incremental dbt redesign, reducing compute costs by 15% while maintaining SLAs."
**Prompt:** Prepare a story about inheriting a slow, expensive query layer at Vinted where you identified the root cause, redesigned the incremental dbt models, and delivered measurable cost and performance improvements. End with what you would do differently or what you learned about diagnosing query performance proactively.

### Theme 2: Discovery-to-Delivery ownership
**Source bullet:** "Owned Finance Data Products roadmap as sole analyst — end-to-end delivery from definition to OKRs."
**Prompt:** Prepare a story about taking a vague or ambiguous Finance requirement at Tourlane and owning the full cycle — stakeholder discovery, definition, build, and delivery to OKRs — without a manager directing each step. End with what you learned about scoping when requirements are still moving.

### Theme 3: Raising data culture through mentoring
**Source bullet:** "Raised dbt unit test coverage <1%→50%+ in 4 weeks; testing guide independently adopted by teammates."
**Prompt:** Prepare a story about identifying a quality gap in the team's dbt practice at Vinted, writing a testing guide, and driving adoption without formal authority. End with what you observed about what makes a technical guide actually get used versus ignored.

---

## 4. Company research findings

### Business model and unit economics

Seven Senders is a B2B cross-border parcel delivery platform: e-commerce retailers integrate once and get access to 100+ local last-mile carriers across Europe, with Seven Senders handling routing, tracking, and claims. Revenue is primarily per-parcel transaction fees, modulated by destination, carrier, service level, and add-ons. This means their core financial metrics are: margin per shipment, carrier cost by route, SLA performance by carrier/country, and claim rates. Data problems that are highest-stakes: carrier cost variance, delivery performance analytics, and claim fraud or anomaly detection — because each maps directly to margin on millions of transactions. [Source: Tech.eu Series C announcement](https://tech.eu/2021/04/15/berlin-based-parcel-delivery-platform-seven-senders-raises-e32-million-in-series-c-round/)

### Competitive position

Closest direct competitors are Parcel.One, Sendcloud, and Shippo — all multi-carrier aggregators targeting the same e-commerce cross-border segment. Indirect pressure from DHL, UPS, FedEx who offer their own label/API integrations. Seven Senders differentiates on European carrier depth (100+), single-integration simplicity, and analytics/tracking as a platform feature rather than an afterthought. They are a challenger to the big integrators and an incumbent vs. newer entrants. For the data team, this means competitive intelligence on carrier performance and cost optimisation are live concerns — not background noise. [Source: businessmodelcanvastemplate.com competitive landscape](https://businessmodelcanvastemplate.com/blogs/competitors/seven-senders-competitive-landscape)

### Data stack and engineering culture

No engineering blog or public tech writing found. The JD explicitly names dbt and Looker, confirming both are in production. The emphasis on "multi-billion row datasets" and "cost-optimised SQL" in the JD suggests they are on a columnar warehouse (BigQuery or Snowflake most likely) and have already hit performance pain. No further detail available from public sources.

### Data team size and structure

No direct headcount data found. Seven Senders has ~220–300 employees total. [Source: Apollo.io company profile](https://www.apollo.io/companies/Seven-Senders/556d215d7369641258529300) At that company size, the data team is likely 5–15 people. The JD asking for a senior IC who mentors juniors suggests a flat team without a dedicated analytics engineering manager — this role likely reports to a Head of Data or CTO equivalent and is expected to raise the bar across the team.

### Recent news and growth signals

Last confirmed funding: Series C €32M in April 2021; a later $10M Growth Equity round in August 2022. No major public announcement in 2025–2026 found. Revenue reportedly ~€100M in 2021, with 50%+ growth cited for 2023. The lack of recent funding news suggests the company is operating on existing capital and may be optimising for profitability — relevant because cost-efficient data infrastructure aligns with that mode. [Source: EU-Startups Series C coverage](https://www.eu-startups.com/2019/06/berlin-based-seven-senders-raises-e16-million-to-further-expand-its-parcel-shipping-solution-throughout-europe/)

### Role-specific insight

The JD mentions "EU-wide digital claim management" as a platform feature in Seven Senders' product suite. Claims are a direct cost line — incorrect deliveries, carrier errors, damaged parcels. A senior BI hire who can build reconciliation and anomaly detection on parcel-level data (exactly what the Vinted "€1.6m recovered via risk controls" bullet describes) is solving a real, revenue-connected problem for them. This is a direct hook from your experience.

### Suggested opening hook

> "Seven Senders processes millions of cross-border shipments on a per-parcel margin model — carrier performance and cost variance at scale are your live data problems. I built exactly that at Vinted: cost-optimised dbt on multi-billion row shipping datasets, with anomaly detection that recovered €1.6m. That's the problem I solve."

---

## 5. Opening and closing

### Opening (first 60 seconds)
Lead with the hook above. Keep it tight: one fact about their business (per-parcel model, shipping scale), one direct statement of capability. Do not spend the first 60 seconds summarising your CV — they have it. You are demonstrating that you've already connected their problem to your work.

### Closing statement

> "I've built dbt and Looker at exactly this scale, in a shipping-data context. I'm in Berlin, available on short notice, and ready to move forward. What's the next step?"

---

## 6. Questions to ask

Pick 1–2 for the call; have the others ready if the conversation opens up.

### Impact / success definition
> "The JD mentions 'data culture quality' as something this role maintains — what's the current baseline, and what would great look like at 12 months for whoever joins?"

### Team problem
> "The JD explicitly asks for cost-optimised SQL on multi-billion row datasets. Is that an active bottleneck right now — something that's causing real pain — or are you building the foundation before scale becomes a problem?"

### Business / strategy
> "Seven Senders runs on per-parcel margins across 100+ carriers in Europe. Which data questions are most high-stakes for the business right now — carrier cost variance, SLA performance, claim rates, or something else?"

### Ways of working
> "The JD says 'independently lead the Discovery-to-Delivery cycle' — in practice, when requirements come in ambiguous from the business side, who resolves that ambiguity and how much back-and-forth is normal before a project gets scoped?"

*Why specific questions work:* Generic questions ("what does success look like?") are forgettable. Questions that reference something real signal preparation, business understanding, and that you're already thinking about the role — not just trying to get it.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story — prevents rambling, gives recruiter time to finish notes.
- **Use "I" not "we"** — recruiters assess your individual contribution.
- **Salary / notice period** — state your range confidently. If pushed early: "I'm flexible depending on the full package — can you share the budgeted range for the role?"
