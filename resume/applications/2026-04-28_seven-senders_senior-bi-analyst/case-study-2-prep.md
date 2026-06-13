# Case Study 2: Cross-Domain Work & Knowledge Transfer
### Interview Prep — Answers + Walk-Through Guide

---

## How to Walk Through This

**Overall framing to open with:**
> "This case study is about how I navigate genuine unfamiliarity — entering a domain I don't know, with a vague ticket, and producing something production-ready. My approach has three phases: understand before building, validate before shipping, and document for the person who comes after me."

**Suggested structure for a 10–15 minute verbal walkthrough:**

| Phase | Time | What to cover |
|---|---|---|
| 1. Set up the problem | 1 min | Restate what makes this hard — vague ticket, unfamiliar domain, three tables with unknown relationships |
| 2. Walk Q1–Q3 together | 4 min | Knowledge gathering, data exploration, requirement validation — these are sequential and feed each other |
| 3. Walk Q4 | 3 min | Implementation decisions — dbt vs LookML, new vs existing models, how you'd structure the work |
| 4. Walk Q5–Q6 | 3 min | Documentation and done criteria — signal you think past the build |
| 5. Self-aware close | 1 min | Name your natural tendencies and how you'd guard against them |

**Tone:** confident but not arrogant. You're describing a reasoned process, not the one true answer. Use phrases like "my default would be..." and "I'd validate that assumption before proceeding."

---

## Q1: Knowledge Gathering

### The answer

**People first, data second.** The instinct is to open a SQL console immediately — but in an unfamiliar domain, data without context produces a confident-but-wrong model fast.

**Specific steps:**
1. **SME session (30 min, before touching data)** — book with the domain expert or ticket requester. Goal: understand vocabulary, not validate a hypothesis. Ask open questions: "How do you think about the relationship between a tariff and an actual cost?" not "It joins on route_id, right?"
2. **dbt project audit** — read existing model files, schema.yml descriptions, meta tags, and the lineage graph (dbt docs). See what's already modelled in transportation and what assumptions are baked in.
3. **LookML audit** — existing explores reveal how the business currently joins and filters these tables. This is often more informative than the raw SQL.
4. **Existing dashboards** — if the Operations team already has transportation dashboards, those are the fastest way to see which metrics are trusted and how the data is currently interpreted.
5. **Commit history** — read PRs from whoever built the transport models. Engineers document intent in ways that Confluence pages often don't.

**Relevant frameworks:**
- *Kolb's Experiential Learning Cycle*: build abstract conceptualisation (mental model) before active experimentation (writing queries)
- *Vygotsky's Zone of Proximal Development*: go further faster with a knowledgeable collaborator; seeking help is efficiency, not weakness

### Watch out for (self-aware)
Your natural move is to impose structure immediately and narrow ambiguity fast. That's the right instinct in execution — but in this phase, it can mean you go into the SME session already having decided the answer. The session then becomes confirmation, not learning. Force yourself to ask open questions and sit with the answer before responding.

---

## Q2: Data Exploration

### The answer

Systematic, not ad hoc. The goal is to understand **grain, relationships, data quality, and business logic** before writing a single model.

```sql
-- 1. Understand grain of each table
SELECT COUNT(*), COUNT(DISTINCT transport_id) FROM transport;
SELECT COUNT(*), COUNT(DISTINCT route_id) FROM route;
SELECT COUNT(*), COUNT(DISTINCT tariff_id), COUNT(DISTINCT freight_forwarder_id)
FROM freight_forwarder_tariff;

-- 2. Check join cardinality — is transport:route 1:1 or many:1?
SELECT transport_id, COUNT(DISTINCT route_id) AS route_count
FROM transport
GROUP BY 1
HAVING route_count > 1
LIMIT 10;

-- 3. Null / missing key analysis
SELECT
  COUNT(*) AS total,
  COUNT(route_id) AS has_route,
  COUNT(freight_forwarder_id) AS has_ff
FROM transport;

-- 4. Tariff coverage — does every route have a tariff estimate?
SELECT
  r.route_id,
  COUNT(fft.tariff_id) AS tariff_count
FROM route r
LEFT JOIN freight_forwarder_tariff fft ON r.route_id = fft.route_id
GROUP BY 1
ORDER BY tariff_count ASC
LIMIT 20;

-- 5. Cost distribution — understand ranges before defining "outlier"
SELECT
  PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY actual_cost) AS p25,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY actual_cost) AS median,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY actual_cost) AS p95,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY actual_cost) AS p99,
  MAX(actual_cost) AS max_cost
FROM transport;

-- 6. Date range and recency
SELECT MIN(created_at), MAX(created_at) FROM transport;
SELECT MIN(effective_date), MAX(effective_date) FROM freight_forwarder_tariff;
```

**I'm answering:** What is one row in each table? What joins are safe? Where are the gaps? What does the cost distribution look like *before* I define outliers?

**Checkpoint before moving on:** Write a short note (even just bullet points in a Notion page) summarising what you found and — critically — what you *didn't* verify. This forces honesty about gaps and prevents edge cases surfacing in production.

### Watch out for (self-aware)
You'll naturally form a strong hypothesis early and want to move. Resist closing the loop before you've explicitly checked for gaps: routes with no tariff, transports with multiple freight forwarders, currency mismatches, historical tariff versioning. These are the things that come back later.

---

## Q3: Requirement Validation

### The answer

The ticket as written has at least five unresolved ambiguities. Shipping it as-is means building something technically correct but probably not used.

**Questions to raise — written as a ticket comment, not a Slack DM** (written = shared reference):

| Question | Who to ask | Priority | Why |
|---|---|---|---|
| What does the data support — what are the possible grains, and what are the trade-offs? | Data engineer / domain SME | 🔴 Blocker | Can't write a join without knowing what the data can support. Ask this first to define the options. |
| Given the options, which grain matches what you need to analyse? | Ticket requester | 🔴 Blocker | Requester chooses between options — they can't define the options themselves. Combine with SME answer before this conversation. |
| How do we match actual costs to tariff estimates — same route, same period, same forwarder? | Data engineer / domain SME | 🔴 Blocker | Core business logic lives in the data model. SME knows whether tariffs are versioned, whether one route can have multiple forwarder tariffs. Validate intent with requester after. |
| How is "cost outlier" defined — statistical (e.g. >2 SD), business threshold, or user-defined? | Ticket requester / business stakeholder | 🟡 High priority | Business definition, not a data question. Can build the fact model without it; need it before LookML is done. |
| What date range? Rolling 90 days, full history, configurable? | Ticket requester | 🟡 High priority | Affects incremental strategy and query cost. Can default to configurable filter and confirm before shipping. |
| Who are the end users and what decision does this inform? | Check ticket context first; ask requester if unclear | 🟢 Answer yourself first | Usually inferable from who raised the ticket and what team they're on. Only ask if context is genuinely absent. |
| Is there an existing Looker explore I should align with for consistency? | Check Looker + dbt project first; ask BI owner if nothing found | 🟢 Answer yourself first | Open Looker and look before using stakeholder time. Ask only if you can't find anything after 10 minutes. |

**Framing matters.** Don't position this as "the ticket is missing the following." Position it as: *"Before I build this, I want to make sure I'm solving the right problem — a few things would help me get there."* Same information, different relationship dynamic. You're new to this domain; the requester has context you don't.

**Relevant framework:** PMBOK — Collect Requirements. The planning fallacy in reverse: underestimating the cost of building the wrong thing.

### Watch out for (self-aware)
Your directness is a strength here but can land badly. A list of five things wrong with a ticket reads as criticism of the requester's competence, even when it isn't meant that way. Especially as the person new to the domain — signal that you're asking because you want to serve the actual need, not because you're auditing their work.

---

## Q4: Implementation Approach

### The answer

**New dbt models, structured by layer. Business logic in dbt, presentation in LookML.**

**Why new models:** I'd verify first what exists in the dbt project, but given I'm new to this domain, I'd assume the staging layer is either absent or incomplete for my purposes. Building on an uncertain foundation creates hidden debt.

**Model structure:**

```
models/
  staging/
    stg_transportation__transports.sql          -- cleaned, typed, renamed
    stg_transportation__routes.sql
    stg_transportation__freight_forwarder_tariffs.sql
  intermediate/
    int_transport_costs_with_tariffs.sql        -- join actuals to tariff estimates at correct grain
  marts/
    fct_freight_forwarder_cost_comparison.sql   -- final fact table for Looker
```

**Why business logic in dbt, not LookML:**
- Version-controlled and testable
- Reusable by other models and explores
- Join logic in LookML is invisible to dbt tests and hard to audit

**LookML** sits on top of the mart: dimensions, measures, filters, and UI. Derived dimensions for cost variance (actual vs tariff); outlier flag either as a dbt-computed column or a Looker table calculation depending on how it's defined.

**Work structure (INVEST criteria — independently deliverable tickets):**
1. **Spike (timeboxed, 1 day):** data exploration + SME session → written summary of findings
2. **PR #1:** Staging models + schema.yml tests
3. **PR #2:** Intermediate + fact model
4. **PR #3:** LookML explore + UAT with requester

Each PR is independently reviewable. Small blast radius if something is wrong.

### Watch out for (self-aware)
This is your comfort zone, which is where the "over-protective of own ideas" risk is highest. When you open the PR, explicitly invite challenge on the *structure*, not just the SQL: "I've made X assumption about grain here — flag if you see it differently." This signals openness and is more likely to surface real issues before prod.

Also: your action-orientation means you may undercommunicate progress to stakeholders. A quick midpoint message — "here's what I found, here's what I'm building" — reduces the chance of a late-stage surprise, especially when you're new to the domain.

---

## Q5: Knowledge Transfer

### The answer

Documentation is a deliverable with the same priority as the model. The bar: the maintaining engineer can answer "why does this join look like this?" without asking me.

**In the dbt project:**
- `schema.yml` descriptions on every model, column, and test — including *why* a column exists, not just what it contains
- A `README.md` in `/marts` explaining: business context, grain, key assumptions, known limitations
- Inline SQL comments for non-obvious logic (e.g. "tariff matched on route_id + freight_forwarder_id + most recent effective_date ≤ transport created_at")

**In LookML:**
- Label and description fields on every dimension and measure
- Comments explaining join type choices

**In Confluence / Notion:**
- One-page summary: what the explore does, who uses it, what decisions it supports, known limitations, who to contact
- Data lineage diagram (exported from dbt docs)

**Handover session — use a teach-back, not a presentation:**
Ask the maintaining engineer to walk *you* through the model using your docs. Where they hesitate or paraphrase incorrectly is where the docs are insufficient. "Does that make sense?" always gets a yes. "Can you walk me through how the tariff join works?" doesn't.

**Relevant framework:** Curse of knowledge (Pinker) — once you understand a domain, you systematically underestimate how confusing it is to someone new. Good docs compensate for this actively.

### Watch out for (self-aware)
You show care through reliability, not emotional expression. Documentation can feel like bureaucracy when there's a logic-sound model to ship. Reframe: this is the mechanism by which your impact outlasts the ticket. It's impact at scale through someone else's capability — which is exactly what you're optimising for. That framing makes it feel less like admin.

---

## Q6: Self-Assessment — Production Readiness

### The answer

Explicit **Definition of Done** — not "I think it's done." An agreed checklist that prevents ambiguity and stops the goalposts moving.

**Functional correctness:**
- [ ] Requester has reviewed the Explore in a UAT session and confirmed numbers match expectations (or discrepancies are reconciled)
- [ ] Actuals and tariff estimates produce sensible variance figures on known routes
- [ ] Outlier logic matches the agreed definition

**Data quality:**
- [ ] dbt tests pass: not_null on keys, unique on grain, referential integrity between staging and intermediate
- [ ] accepted_values tests on any status/type fields
- [ ] No unexpected NULLs in cost columns that should always be populated

**Performance:**
- [ ] Explore loads within acceptable time for expected query patterns
- [ ] No unnecessary full-table scans

**Documentation:**
- [ ] schema.yml fully populated
- [ ] README written
- [ ] LookML descriptions present
- [ ] Confluence / Notion page exists and linked from the ticket

**Process:**
- [ ] PR reviewed by at least one peer
- [ ] Handover session completed (teach-back, not presentation)
- [ ] Ticket closed with a comment summarising what was built and any known limitations

**Known limitations are not failures.** Documenting them is professional honesty. They prevent the next engineer from spending a day wondering if a gap is a bug or a design decision.

### Watch out for (self-aware)
Two failure modes pulled in opposite directions. Your perfectionism can make the DoD a moving target — you keep finding things to tighten and delay shipping. Your pragmatism can go the other way — once the logic is sound, documentation feels like optional overhead under time pressure. The fix: treat docs as non-negotiable in the DoD from the start, not a post-ship nice-to-have.

---

## Likely Interview Questions — and How to Answer

### On knowledge gathering

**"What if the SME is unavailable or too busy to meet?"**
> "I'd work with what I have — dbt lineage, LookML, existing dashboards, commit history. I can build a reasonable hypothesis from those sources. I'd then write it down explicitly and send it as a comment on the ticket: 'Here's how I believe the data works — please correct anything I've got wrong.' That creates a forcing function for the SME to engage, and it shows I didn't block on their availability."

**"How do you balance thoroughness with moving fast?"**
> "I timebox the discovery phase. One day for the spike: SME session, data exploration, written summary. If I still have fundamental unresolved questions after that, I surface them as blockers rather than guessing. The cost of building on a wrong assumption is almost always higher than the cost of one more question."

---

### On data exploration

**"What if the data doesn't match what the SME told you?"**
> "That's actually useful information. It usually means either the data has quality issues, the SME's mental model is incomplete, or the business logic has changed since the tables were built. I'd go back with specific examples: 'You said route and tariff are always 1:1, but I'm seeing routes with three tariffs — can you help me understand why?' That conversation is more productive than the first one."

**"How would you handle missing or null data?"**
> "Depends on what's null and why. If it's structural — some routes never have tariff estimates — that's a dimension to expose in the explore, not a data quality issue. If it's unexpected — transport records with no route — that's a test to add and a question for the data owner. I'd document both cases explicitly."

---

### On requirement validation

**"The requester pushes back and says the ticket is clear enough — just build it."**
> "I'd acknowledge their view and proceed with the most defensible interpretation I can make from the data. I'd also write down my assumptions in the PR description so they're visible for review. If my interpretation is wrong, it surfaces in UAT rather than prod. The goal is to ship something reviewable quickly, not to win the argument about ticket quality."

**"How do you define a cost outlier without a clear business definition?"**
> "I'd propose two options and let the requester choose. Option A: statistical — flag costs more than 2 standard deviations from the mean per route. Option B: business threshold — flag costs exceeding X% above the tariff estimate. I can implement either in dbt or as a Looker filter. The point is to make the choice explicit rather than picking one silently."

---

### On implementation

**"Why not just build the explore in LookML and avoid the dbt work?"**
> "For simple metrics, LookML is fine. But this ticket involves join logic between three tables with unknown cardinality and business rules for matching actuals to estimates. That logic is too complex and too important to live only in LookML, where it can't be tested or reused. Putting it in dbt makes it auditable, testable, and available to any future explore or model."

**"Would you reuse existing staging models or build new ones?"**
> "I'd check first. If staging models for these tables exist and are well-maintained, I'd reuse them — that's the point of the staging layer. If they're absent, incomplete, or have assumptions baked in that don't match my use case, I'd create new ones or extend them carefully. I wouldn't silently modify an existing staging model in a way that could break downstream models."

---

### On documentation and handover

**"How much documentation is too much?"**
> "Documentation that describes *what* is usually too much. Documentation that describes *why* is usually not enough. I'd rather have three sentences explaining why a join uses the most recent tariff date than a paragraph restating what the columns are. If someone can understand the intent without reading the code, the documentation is doing its job."

**"What if the maintaining engineer doesn't read the docs?"**
> "That's a real risk. The teach-back handover session is the mitigation — it forces engagement with the docs before I'm gone. If someone skips that session, they skip the safety net by choice. Beyond that, I can't control what people read. I can make the docs good enough that referring to them is faster than guessing."

---

### On self-awareness (if they probe on the personality angle)

**"What's your biggest risk in this kind of task?"**
> "Moving too fast in the discovery phase. My instinct is to narrow ambiguity quickly — I'll form a hypothesis about the data model early and want to start building. The risk is that I stop exploring once I have *a* coherent picture, rather than a *complete* one. I manage it by explicitly writing down what I haven't verified before I open a code editor."

**"How do you handle working with people who move more slowly than you?"**
> "I try to separate pace from quality. Someone moving slower might be doing more thorough validation than I am — that's worth respecting. Where I genuinely think pace is a problem, I'd say so directly: 'I want to get this to UAT by Thursday — what do you need from me to unblock your part?' That's more useful than internal frustration."

---

## Summary: The Meta-Point

Your profile is well-suited to this type of work — logical, systematic, high standards, fast mover. The three places where technically excellent work is most likely to quietly fail:

1. **The SME conversation** — going in to confirm rather than to learn
2. **The PR review dynamic** — defending rather than genuinely considering challenges to the design
3. **The handover** — assuming good docs are sufficient without checking if they're understood

The adjustments aren't about changing your approach. They're about being deliberate at the edges where your strengths create blind spots.
