# Recruiter Call Prep — Analytics Engineer at Distribusion Technologies

**Application folder:** 2026-04-22_distribusion_analytics-engineer
**Prepared:** 2026-04-24

---

## 1. What the recruiter is screening for

### Viability checklist
- **Looker dashboard development** → Clearly covered: multiple bullets at Vinted and Tourlane, calculated-field architecture, sprint delivery, finance and ops dashboards.
- **BigQuery + GCP + Kafka** → Clearly covered: Vinted bullet on tracing Kafka event streams, BigQuery ETL, Cloud Functions / Pub/Sub / Cloud Storage.
- **Apache Airflow** → Listed in skills; no dedicated story in the resume. Minor gap — prepare a sentence on any Airflow exposure (even monitoring pipelines, or awareness from Vinted's orchestration layer).
- **Python and SQL scripting** → Clearly covered: dbt/SQL at Vinted and Tourlane; Python teaching at ReDI; scripting implied by GCP automation work.
- **Git / GitLab / GCP** → Covered for GCP and Git. Resume lists GitHub; JD says GitLab specifically. Be ready to acknowledge the GitLab gap and bridge to Git fundamentals.

### Soft skill and culture fit signals
The JD uses "rapid", "tight deadlines", "single-day timeframes", "rigorous accuracy", "independently", and "anticipate future challenges" — this is a fast-moving IC role where speed and accuracy must coexist without hand-holding. The recruiter is screening for someone who acts first and escalates rarely. Mirror this tone on the call: be direct, quantify everything, avoid governance or architecture framing.

### Likely hard question
**"You come from a finance-heavy background — how quickly can you get up to speed on ground transportation data?"**
*Suggested response frame:* At Vinted I ramped independently on complex, undocumented data infrastructure — Kafka streams, carrier billing feeds, BigQuery ETL — with no documentation handoff. New domain, same problem. I trace lineage, read pipeline code, and build context fast. That's what your JD is actually asking for.

---

## 2. Your Peak moment

> "At Vinted, I owned the full analytics stack for shipping finance — built Looker dashboards delivering accurate reporting on €40m+ of financial exposure, redesigned BigQuery queries for 75% faster runtimes, and cut cloud compute costs by 15%, all while working autonomously against tight sprint deadlines."

*Why this works:* Directly addresses the top JD responsibility (rapid Looker delivery), the secondary ask (infrastructure ownership and optimisation), and the accuracy constraint — all in one answer.

---

## 3. STAR story prompts

For each theme, use STAR+Spark: Situation/Task (20%), Action — use "I" not "we" (60%), Result with a number (20%), Learning/Spark (1 sentence).

### Theme 1: Rapid dashboard delivery under tight deadlines
**Source bullet:** "Delivered Looker dashboards within tight sprint deadlines for Finance Ops and Group Reporting; built and iterated calculated-field architecture to enable rapid metric changes while maintaining 100% accuracy on €40m+ of financial exposure."
**Prompt:** Prepare a story about a moment at Vinted when a stakeholder needed a dashboard fast — walk through how you structured it for speed without sacrificing accuracy, and what the specific deadline pressure looked like. End with what you would do differently to go even faster.

### Theme 2: Independent data infrastructure navigation
**Source bullet:** "Worked independently to understand and navigate data infrastructure: traced upstream Kafka event streams and carrier billing feeds, understood BigQuery ETL dependencies, diagnosed data quality issues, and optimised queries without hand-holding."
**Prompt:** Prepare a story about joining Vinted and having to understand a complex, partially undocumented pipeline — walk through how you traced the data lineage, what tools you used, what you found, and how long it took. End with the diagnostic pattern you now apply by default.

### Theme 3: Proposing and implementing reporting enhancements
**Source bullet:** "Proposed and implemented enhancements to reporting systems: identified pipeline inefficiencies, redesigned BigQuery queries for 75% faster runtimes, and cut cloud compute costs by 15% through workload pattern optimisation."
**Prompt:** Prepare a story about identifying a reporting inefficiency that no one had asked you to fix — how you spotted it, built the case to act on it, and what the measurable outcome was. End with what this tells you about how to operate in an IC role.

---

## 4. Company research findings

### Business model and unit economics
Distribusion is a middleman between two groups: transportation companies (buses, trains, ferries) and travel websites (Google, Booking.com, Alipay, Trainline, Amadeus). Every time someone books a ticket through one of those websites, Distribusion takes a small cut. The more bookings, the more money they make. For the data team, this means tracking: how many people complete a booking (conversion rates), which carriers are performing well, and making sure commission payments are accurate.

*Technical angle:* Key revenue drivers are booking volume, the number of carriers on the platform, and retailer integrations. Every new carrier partnership adds new data sources — each with slightly different formats and quality issues — that need to be modeled and monitored. [Source: PhocusWire](https://www.phocuswire.com/b2b-ground-transportation-marketplace-distribusion-raises-80m)

### Competitive position
**Who they're up against:** Distribusion's main competitors are [Transferz](https://www.transferz.com/) (founded 2020, focuses on airport transfers), [Busbud](https://www.busbud.com) (launched B2B API offering "Busbud Business" in 2015, emphasizes bus + train), and [Bookaway](https://www.cbinsights.com/company/bookaway) (buses, trains, ferries but primarily consumer-facing). [Source: CBInsights](https://www.cbinsights.com/company/busbud/alternatives-competitors)

**Distribusion's edge:** They developed the first global B2B booking API and operate across 70 markets with coverage of all major European rail carriers (Deutsche Bahn, SNCF, Trenitalia). [Source: Tech.eu](https://tech.eu/2024/09/26/berlin-based-distribusion-secures-80m-for-global-ground-transport-accessibility/) They're the only platform covering multi-modal ground transport (buses, trains, ferries, public transport) with a single API — competitors typically specialize in one mode or focus on B2C rather than B2B. 

**Why this matters for the data team:** The data team is likely focused on proving that the API works reliably across heterogeneous carriers, demonstrating ROI to both travel retailers (Google, Booking.com) and carriers, and optimizing the booking flow to increase conversion rates and carrier adoption.

### Data stack and engineering culture
Confirmed from the JD itself: BigQuery (data warehouse), Kafka (event streaming), Airflow (orchestration), Looker and Grafana (BI / monitoring), GCP (cloud platform), GitLab (version control). Crunchbase confirms Kafka in the tech stack. No public engineering blog found. The JD signals a GCP-native setup — expect BigQuery-centred analytics with Kafka feeding real-time booking events.

### Data team size and structure
~369 employees total as of February 2026. [Source: Distribusion news/funding data] A concurrent Senior Data Engineer role is also open, suggesting a small but actively hiring data function. The JD framing — no mention of team leadership, governance, or data modeling layers — signals a lean IC team where each person owns a full domain end-to-end. Likely centralised data team serving product and commercial stakeholders.

### Recent news and growth signals
- **$80M Series C** closed September 2024 led by TQ Ventures and Lightrock, total raised $118M. Purpose: global expansion and advanced retail technology for partners. [Source: Distribusion](https://www.distribusion.com/news/distribusion-announces-$80m-series-c-led-by-tq-ventures-to-drive-global-expansion-and-to-double-down-on-advanced-retail-technology-for-its-partners)
- **Deutsche Bahn tender won** September 2024 — multi-carrier sales solution; signals major enterprise contract with a tier-1 rail operator. [Source: Distribusion news]
- **Named Top 100 Next Unicorns 2024** by Viva Technology / GP Bullhound.
- Active geographic expansion in 2025: Brazil, Indonesia (KAI), Slovakia, Italy — each new market adds carrier data sources.

### Role-specific insight
Deutsche Bahn is Germany's largest rail operator. Winning their business means Distribusion now has to build dashboards and analytics specifically for how their tickets are selling across all the travel websites. This is complex because Deutsche Bahn's data is different from other carriers (buses, ferries, etc.), and the dashboards need to be fast and accurate. As Distribusion adds more carriers (Brazil, Indonesia, Slovakia), each one has slightly different data formats and quality issues. The dashboards need to work across all of them without slowing down.

### Suggested opening hook
> "You won the Deutsche Bahn tender in September for a multi-carrier sales solution — that contract requires analytics across heterogeneous carrier data models at speed. I built exactly that at Vinted: fast, accurate dashboards on complex, multi-source BigQuery pipelines. That's the problem I solve."

---

## 5. Opening and closing

### Opening (first 60 seconds)
Use the hook above. Lead with the Deutsche Bahn fact — it shows you've done the research. Name the data problem plainly (multi-source, high-velocity, accuracy-critical). End with one concrete capability statement. Keep it under 4 sentences. Don't explain your career history unprompted — wait for them to ask.

### Closing statement
> "I've built fast, accurate Looker dashboards on BigQuery and GCP in a high-stakes, autonomous environment — that's the core of what you need. I'm in Berlin, available to start within a few weeks. What's the next step?"

---

## 6. Questions to ask

Pick 1–2 for the call; have the others ready if the conversation opens up.

### Impact / success definition
> "You won the Deutsche Bahn tender in September for a multi-carrier sales solution. In the first 6 months, is the analytics work primarily oriented around that contract — building dashboards for carrier performance, booking funnel, or SLA reporting — or is there a broader dashboard backlog this role is expected to clear?"

### Team problem
> "The JD asks candidates to independently navigate data sources and processing workflows — which suggests the infrastructure may be complex or partially undocumented. Is the hardest data challenge right now about data discovery and lineage as the carrier network scales, or more about keeping dashboard delivery fast enough to match the speed of commercial expansion?"

### Business / strategy
> "You're a B2B marketplace — revenue flows through booking volume on both sides of the network. How does the data team balance analytics priorities between the retailer side (API conversion, performance) and the carrier side (yield, inventory)? Or does this role own one side more than the other?"

### Ways of working
> "The JD says 'leverage available tools and resources to solve problems independently' — what does that look like when I hit a data quality issue that blocks a dashboard? Do I own the full resolution — investigation, fix, redelivery — or is there a data engineering team I hand off pipeline problems to?"

*Why specific questions work:* Generic questions ("what does success look like?") are forgettable. Questions that reference the Deutsche Bahn contract, the carrier data complexity, or the two-sided marketplace dynamic signal that you understand the business — and that you're already thinking about the problems, not just the job title.

---

## 7. Call mechanics

- **Stand up** if it is a phone call — opens your chest, makes your voice more energetic.
- **Wait 2 seconds** after finishing a story — prevents rambling, gives recruiter time to finish notes.
- **Use "I" not "we"** — recruiters assess your individual contribution.
- **Salary / notice period** — state your range confidently. If pushed early: "I'm flexible depending on the full package — can you share the budgeted range for the role?"
