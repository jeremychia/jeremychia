# Hiring Manager Prep — Senior Business Intelligence Analyst at Seven Senders

**Application folder:** 2026-04-28_seven-senders_senior-bi-analyst
**Interviewer:** Mia Varis, Team Lead Business Intelligence
**Date:** Thursday, 21 May 2026, 11:00 AM CET
**Prepared:** 2026-05-21

---

## 1. Who is Mia

**Career path at Seven Senders:**
- Business Intelligence Analyst → Senior BI Analyst → Senior BI Analyst II → **Team Lead BI** (promoted Nov 2025)
- Total tenure: 5+ years (Feb 2021 – present)
- She held the exact role you are applying for before her promotion

**Background before Seven Senders:**
- Product Manager, Sales Technologies at Delivery Hero
- Senior Business Analyst, Competitive Intelligence at Wayfair (1.5 years)
- Team Lead, Supplier Merchandising at Wayfair
- Data Analyst, Merchandising at Wayfair

**Education:**
- BA Business Administration, Accounting and Finance — Berlin School of Economics and Law
- BBA European Management — Metropolia University of Applied Sciences (double degree)

**What this means:**
Mia is a business-first analyst, not an engineering-first one. Her degrees are in finance and business management. Her pre-Seven Senders roles were in competitive intelligence, merchandising analytics, and product management — not data engineering. She built technical depth through practice, not training. She will value business-outcome framing over technical elegance. When you describe dbt work, lead with the cost reduction, not the macro structure.

She was promoted six months ago. She has prior management experience (Team Lead at Wayfair, Product Manager at Delivery Hero), so she is not figuring out management for the first time — she will be direct about what she needs. The person she hires now takes over her old IC work — she needs someone she can trust to run independently, freeing her capacity for the team lead remit.

---

## 2. What Mia needs from this hire

She has just moved from IC to team lead. Her old technical ownership — dbt models, Looker, stakeholder Discovery-to-Delivery — now needs an owner. She cannot be both team lead and senior IC. The hire she makes needs to:

- Own the full analytical stack she used to maintain, without asking for direction
- Translate between data engineers and business stakeholders (she did this; she'll recognise when someone can't)
- Raise quality standards (testing, documentation, code reviews) because she no longer has time to enforce them personally
- Stay. Five-year tenure signals she values continuity — she does not want to rehire in 18 months.

**Her implicit fear:** hiring someone who needs constant management, or who treats this as a 12-month stepping stone.

---

## 3. What Mia will evaluate

### Can you do the job she used to do?
She will probe for specifics. She knows this role from the inside — vague answers will read as insufficient experience. Be concrete on: Snowflake, dbt (Jinja, macros, incremental models), Looker (LookML, explores, access control), and Discovery-to-Delivery ownership.

### Can you work without being directed?
She is a new manager and her capacity is constrained. She will look for evidence you can define your own work given a business problem, not just execute on a ticket. Have a story ready about initiating something that was not asked for, and owning it end-to-end.

### Will you stay and grow?
Her career is the proof point that longevity is rewarded here. She will ask — directly or indirectly — about your long-term intent. Be honest and specific about why Seven Senders is the right place for the next phase, not just the next job.

### Can you be the bridge?
The notes flag "translating for technical stakeholders" as a core function. Mia came from the business side — she did this translation herself. She will test whether you understand business language, not just technical correctness.

---

## 4. STAR stories — adjusted for this round

This is not a screening call. Stories need more depth. Use STAR+Spark but allocate more time to the Action — walk through your actual reasoning, not just what you did.

### Theme 1: Independent ownership without a manager directing each step
**Source bullet:** Tourlane — sole analyst, owned Finance Data Products roadmap end-to-end from definition to OKRs
**Prompt:** Describe a time you were handed an ambiguous business problem with no clear spec and no one to escalate to. Walk through how you defined the scope, decided what to build, and delivered. End with: what would you do differently now about how you handled ambiguity early in the project?
**Why this matters to Mia:** She has a full team lead remit and limited IC bandwidth. She is evaluating whether you can handle the ambiguity she used to absorb herself — not because she's uncertain about managing, but because she genuinely cannot do both.

### Theme 2: Technical quality as a culture change, not a task
**Source bullet:** Raised dbt test coverage <1% → 50%+ in 4 weeks; testing guide independently adopted by teammates
**Prompt:** Describe the moment you recognised the quality gap in the team's dbt practice, the specific way you approached writing the guide (why that format, why that scope), and how you drove adoption without formal authority. End with: what did you learn about what makes a technical guide actually get used?
**Why this matters to Mia:** She is now a team lead responsible for quality across a team. She wants to hire someone who raises the floor without being managed.

### Theme 3: Translating between data engineering and business
**Source bullet:** Bridge role at Vinted between data engineers and Finance/Group Reporting stakeholders; Tourlane — translating requirements from non-technical stakeholders
**Prompt:** Describe a specific situation where a business stakeholder had a requirement that would have been expensive, incorrect, or technically unsound if built as stated. Walk through how you challenged it, what you proposed instead, and how you got buy-in from both sides. End with: what is the skill that makes this translation work well vs. badly?
**Why this matters to Mia:** This is explicitly named in the role description and in the team context. Mia did this herself for years — she will probe it directly.

---

## 5. Questions for Mia

Pick 2 for the interview. The first two are highest signal.

### What she needs from this hire
> "You've just moved into the team lead role — what's the one area where you most need this hire to take full ownership, so you can focus on what the team lead work actually requires?"

*Why this works:* It demonstrates you've read her profile and you're already thinking about making her successful, not just getting the job. It also surfaces what she's been doing herself since the promotion.

### Data quality and engineering health
> "The JD emphasises cost-optimised SQL on multi-billion row datasets — is that an active bottleneck causing real pain right now, or are you building the foundation before scale becomes a problem?"

*Why this works:* Shows you read the JD technically and want to understand whether you'd be solving an existing fire or building preventively. The answer shapes how you'd prioritise in month one.

### Long-term team direction
> "You've been at Seven Senders five-plus years through multiple growth phases — what's the biggest change in what the data team needs to deliver now compared to when you joined?"

*Why this works:* Signals you're thinking long-term, opens up the company's evolution, and lets Mia reflect on her own career — people respond well to questions that invite them to tell their own story.

### Ways of working
> "The JD says 'independently lead the Discovery-to-Delivery cycle' — when a business stakeholder comes in with a request that's ambiguous or technically underspecified, how does that ambiguity normally get resolved? Who resolves it and how much back-and-forth is typical?"

---

## 6. Opening and closing

### Opening (first 60 seconds)
Do not summarise your CV — she has it. Lead with the connection: you have worked on the same stack (Snowflake, dbt, Looker) in the same domain (shipping data at scale). One concrete number. One direct statement of what you solve. Example:

> "Seven Senders processes millions of cross-border shipments on a per-parcel margin model — carrier performance and cost variance at scale are your live data problems. I built exactly that at Vinted: cost-optimised dbt on multi-billion row shipping datasets, with anomaly detection that recovered €1.6m. That's the problem I solve."

### Closing
> "I've built dbt and Looker at exactly this scale in a shipping-data context. I can own Discovery-to-Delivery independently. I'm in Berlin, available on short notice, and ready to move forward — what's the next step?"

---

## 7. Interview mechanics

- **Camera on, professional background** — Teams call with your direct manager, not a screen.
- **Name her work specifically** — if it is natural, reference that she moved from this role into team lead. It shows you have done your research and respect the career path she built.
- **Pause before answering** — 2–3 seconds signals confidence and prevents over-talking.
- **Use "I" not "we"** — she will be assessing individual contribution.
- **Concrete over general** — every time you are tempted to say "the team" or "we built", replace with what you specifically did and decided.
- **Salary / next steps** — if asked, state your range confidently. Do not deflect.
