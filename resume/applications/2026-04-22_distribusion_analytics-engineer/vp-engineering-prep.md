# VP Engineering Interview Prep — Ilya @ Distribusion

**Format:** 45–60 min, Google Meet
**Interviewer:** Ilya, VP of Engineering (Jan 2023–present)

---

## Who is Ilya

**Career path:** Teamo.ru (Software Engineer, 2011–2013) → Badoo Moscow (Senior SWE → Team Lead, Billing Dept, 2013–2021) → OZON.ru (Engineering Manager, 2021–2023) → Distribusion VP Engineering (2023–present).

**What this means:**

- **He built billing systems at massive scale.** 8+ years at Badoo — 200+ countries, PCI DSS compliance, Apple Pay / PayPal / Adyen integrations, sharding terabyte databases, ML fraud scoring. He knows what "wrong = money lost" looks like from the inside.

- **He managed large engineering teams.** OZON.ru (one of Russia's largest marketplaces, tens of millions of users) — 4 cross-functional teams, roadmaps, architecture, hiring. He has been on the receiving end of bad data work creating toil for engineers.

- **He is a VP of Engineering, not a data person.** His question is: does this person reduce the surface area my engineering team has to cover, or expand it? He is assessing whether you operate independently, not whether you know dbt syntax.

- **He thinks about correctness as a non-negotiable.** PCI DSS, payment reconciliation, fraud scoring — his entire career has been on problems where inaccuracy has an immediate financial consequence. He will take your data quality story seriously.

**Cultural note:** Ilya, Evgeny (Director), and Dmitry (your manager) all have Russian tech backgrounds. Russian engineering culture — especially billing/payments — tends to be direct and results-focused. State results first, explain how second. Don't over-narrativise.

---

## What he will probe

| His background | What he'll actually ask |
|---|---|
| Billing system correctness | "How do you ensure the numbers you produce are right?" |
| Large-scale database work | "How do you think about query cost and table design at scale?" |
| Managed engineering teams | "How do you work with engineers — solutions or just problems?" |
| Built ML fraud scoring | "What's your thinking on the AI cost guardrails problem?" |
| Scaled platforms at OZON | "What happens when data volume doubles?" |

---

## Tailored talking points

**On data quality / correctness:**
> "I treat pipelines like instrumented systems — if there's no assertion on the output, you can't trust the reading. At Vinted I built daily reconciliation models in dbt that flagged discrepancies above a threshold. That's how I caught a €1.6m billing discrepancy before it hit the books."

This maps directly to his Badoo background. He *built* the billing system. He knows exactly what undetected discrepancies cost.

**On query cost / the AI guardrails problem (their #1 current priority, €1,000/day exposure):**
> "I've done this before — at Vinted I traced full table scans on large Kafka-derived tables back to finance dashboards and rewrote them with partition pruning and clustering. 75% faster, 15% cost reduction. The AI guardrail problem is the same pattern: identify which query shapes are expensive, materialise the right things, and put a gate on ad-hoc sprawl."

Name the problem explicitly — it's in the notes and it's real.

**On working with engineering:**
> "I bring solutions, not tickets. When I spotted the cost anomaly at Vinted I didn't file a request — I traced it, fixed it, and reported back. I want to be the person who reduces the surface area engineering has to cover for data, not expands it."

A VP of Engineering responds to this. He has been on the receiving end of the opposite.

**On self-service:**
> "I build mart tables wide and flat — no joins needed — so stakeholders answer their own questions without coming to the data team. The goal is to eliminate myself as a bottleneck, not to be indispensable."

---

## STAR stories to have ready

| Story | Lead with | Ilya's frame |
|---|---|---|
| €1.6m billing discrepancy | "I built reconciliation checks before anyone asked me to" | Correctness, initiative, instrumented systems |
| Query cost reduction (75% faster, 15% cost) | "I noticed the anomaly, traced it, fixed it without a ticket" | Cost at scale, engineering mindset, no toil created |
| Vinted onboarding with no docs | "I traced lineage manually from source to dashboard" | Independence, no handholding needed from engineers |
| Tourlane month-end close | "I asked about the decision, not the chart" | Cross-functional clarity, shortened close by 2 days |

---

## Questions to ask Ilya

1. **"From an engineering perspective, where does the data platform create the most friction for the rest of the team right now — reliability, latency, cost, or something else?"**

2. **"You've scaled billing systems at Badoo and managed large engineering departments at OZON — what does 'production-quality' mean to you for a data pipeline, versus what you'd expect in application code?"**
   *(Shows you've done your research; respects his background without being sycophantic.)*

3. **"What does the relationship between the data team and the engineering team look like here — shared CI/CD standards, shared infrastructure ownership, or mostly separate?"**
   *(Relevant because notes mention data engineers own CI/CD + Terraform.)*

---

## Mechanics

- **State results first.** He processes like an engineer — give him the output, then the method.
- **Be concrete.** Numbers, tools, scale. Avoid "I helped improve..." — say "75% faster" or "€1.6m caught."
- **He may go technical.** Be ready to explain partition pruning, dbt model structure, or how you'd design a guardrail on AI query costs.
- **He is not the hiring manager.** Dmitry owns the day-to-day. Ilya is assessing fit with the broader engineering org — does this person raise or lower the bar?
- **Don't fill silence.** State the result, stop, wait.
