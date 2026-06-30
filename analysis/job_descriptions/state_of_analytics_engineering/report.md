# Analytics Engineering Job Market, 2026 — JD Analysis

**Prepared:** June 2026  
**Dataset:** 93 unique job descriptions from `jd_data/` (April–June 2026; European/Berlin market with UK, DACH, Nordics, and selected global roles)  
**Classification:** 41 records hand-coded (manual); 52 records classified via LLM majority vote (3 independent claude-haiku-4-5 runs per JD); full consistency study in `consistency_report.md`  
**Context source:** dbt Labs "State of Analytics Engineering" reports, 2023–2026 — used as a foil, not as the primary data

---

## 1. What this document is

This is a structured analysis of 93 analytics engineering, data engineering, and BI job postings collected during a European job search in 2026. The goal is to characterise what employers actually reveal they want through hiring language — not what practitioners report wanting in surveys.

The dbt Labs annual reports (2023–2026) are used as a reference point throughout: they are the most widely-circulated claims about the state of the profession. The core question is whether those claims show up in what employers write when they have real hiring costs at stake.

**Why this matters:** Survey responses are cheap. Writing a job description carries hiring cost. Deming and Kahn (2018) established that job postings are revealed-preference data — employers write what they actually value. This analysis holds the survey claims against that harder evidence.

**Honest scope limitations:** 93 JDs is a pilot-scale dataset. The confidence interval on any single proportion is approximately ±10pp at 95% — wide enough that individual percentages should be read as directional signals, not precise market measurements. The geographic concentration (primarily European/Berlin market) limits generalisation to North America or APAC. These limitations are stated once here and not repeated throughout; they apply to every finding in this document.

---

## 2. The dbt Labs survey — claims and constraints

The dbt Labs "State of Analytics Engineering" reports (2023–2026) are the most influential annual survey of the analytics engineering profession. Key stated findings by year:

| Year | n | Central claim |
|------|---|---------------|
| 2023 | 567 | Analytics engineering is a distinct profession; data quality is the #1 investment area |
| 2024 | 456 | Data trust is the #1 org priority; budget contraction visible; AI data management at 57% |
| 2025 | 459 | AI in daily workflows: 80% (up from 30%); budget and team growth recovering |
| 2026 | 363 | AI adoption (72% AI coding) outpacing governance (24% AI observability); trust priority: 83% |

**The self-selection constraint:** The survey is distributed through dbt's own community channels. In 2023 (the only year raw data was released), 76% of respondents already used dbt. Later years do not disclose this figure but the distribution channel is unchanged. Every finding from this survey describes the dbt community, not the analytics engineering profession broadly. This constraint is never acknowledged in the reports themselves.

**The sample decline:** n has fallen from 567 to 363 over four years — a 36% drop with no explanation. At n=363 from a non-random sample, year-on-year percentage comparisons should be read as sentiment signals, not measurements.

**The product-narrative alignment:** Each year's report aligns precisely with dbt's product priorities that year — data contracts (2024), AI assist (2025), observability and governance (2026). Whether this reflects shared market signals or editorial framing, the reports are not independent of dbt's commercial interests.

These constraints don't make the findings false. They mean the reports should be read as community sentiment documents, and validated — or not — against revealed employer behaviour.

---

## 3. The dataset

**93 unique job descriptions** collected April–June 2026. Role types:

- Analytics Engineer (AE) and senior AE: ~55%
- Data Engineer (DE) and senior DE: ~20%
- Business Intelligence Analyst/Engineer: ~15%
- Lead/Staff/Principal and Head of Data roles: ~10%

**Geographic spread:** Primarily Berlin and DACH, with meaningful representation from UK, Nordics, and a smaller share of global/remote roles (Netflix, Spotify, Wolt, etc.).

**Classification method:** 41 records were hand-coded by the author during the job search (April–May 2026). A further 52 records added in June 2026 were classified using LLM majority vote (three independent runs of claude-haiku-4-5 using the same Layer B codebook). Where manual and LLM classifications exist for the same JD, manual takes precedence.

**LLM classification quality:** Self-consistency across three runs was high for structured dimensions (velocity_vs_rigour: 0.92, domain_risk: 0.95, data_team_maturity: 0.95). It was lower for dimensions with subjective criteria (jd_authorship: 0.59, autonomy_level: 0.73). Manual–LLM match rates were 25–35% across dimensions — a codebook validity signal, not a model failure. See `consistency_report.md` for full analysis.

---

## 4. Findings

### 4.1 Work orientation: rigour dominates overwhelmingly

The `velocity_vs_rigour` dimension captures whether the JD's primary framing is about quality, correctness, and reliability (rigour) or about speed, iteration, and throughput (velocity).

| velocity_vs_rigour | n | % |
|--------------------|---|---|
| rigour | 78 | 84% |
| mixed | 13 | 14% |
| velocity | 2 | 2% |

**84% of JDs signal a rigour orientation.** Pure velocity is effectively absent — only 2 JDs across 93 signal it. This is the single clearest finding in the dataset: European analytics engineering employers in 2026 frame the role in terms of reliability and correctness, not speed.

This is broadly consistent with the dbt 2026 report's governance anxiety — but the consistency is directional. The JD data cannot distinguish "rigour because we care about engineering craft" from "rigour because we fear AI-generated errors reaching decision-makers." The dbt report's specific framing (fear of hallucinated outputs, AI governance as the driver) may or may not be what's behind employer language.

**What this looks like in practice:** JDs signal rigour through phrases like "single source of truth," "data quality standards," "you will own data reliability," CI/CD requirements, and emphasis on testing and documentation. These appear in the majority of JDs regardless of company size, seniority level, or domain.

---

### 4.2 Domain risk: moderate dominates; high-risk roles are not more rigour-focused

`domain_risk` measures the stakes of data errors in the role's primary domain (high = finance, fintech, compliance, safety; moderate = marketplace, SaaS, general commercial; low = internal tooling, education).

| domain_risk | n | % |
|-------------|---|---|
| moderate | 61 | 66% |
| high | 28 | 30% |
| low | 4 | 4% |

**Cross-tab with velocity_vs_rigour:**

| domain_risk | rigour | mixed | velocity | n |
|-------------|--------|-------|----------|---|
| moderate | 90% | 10% | 0% | 61 |
| high | 71% | 25% | 4% | 28 |
| low | 75% | 0% | 25% | 4 |

The counterintuitive finding: **moderate-risk roles are more rigour-dominant than high-risk roles.** High-risk roles (fintech, finance, compliance) show more `mixed` signals — they balance speed with rigour rather than committing entirely to rigour.

One interpretation: high-stakes businesses have more time pressure on their data work, not less. A fintech processing payments needs fast delivery alongside correctness. A general SaaS company, with less urgency, can afford to prioritise craft. The domain-risk → rigour-framing assumption in the 2026 report (that fear of bad outputs tracks with high-stakes domains) doesn't hold simply in employer language.

---

### 4.3 Data team maturity: the market skews mid-stage, and maturity reshapes everything

`data_team_maturity` estimates where the organisation's data function sits on a development arc: `early` (building the foundation, often first or second data hire), `mid` (established stack, active growth and expansion), or `mature` (sophisticated platform, federated or domain-oriented structure).

| data_team_maturity | n | % |
|--------------------|---|---|
| mid | 69 | 74% |
| early | 18 | 19% |
| mature | 6 | 6% |

**Three-quarters of the market is mid-stage.** Early-stage roles are 19% of the dataset; genuinely mature data organisations are rare (6%). This concentration at mid-stage has implications for what the role actually entails — it is neither greenfield nor optimisation work, but the messier middle of expanding coverage, increasing stakeholder count, and establishing standards that didn't exist at the start.

**Maturity × rigour cross-tab:**

| data_team_maturity | rigour | mixed | velocity | n |
|--------------------|--------|-------|----------|---|
| mid | 93% | 7% | 0% | 69 |
| mature | 100% | 0% | 0% | 6 |
| early | 44% | 44% | 11% | 18 |

The pattern is sharp: **mid and mature teams are almost exclusively rigour-oriented; early-stage teams are split evenly between rigour and mixed, with some velocity signal.** Early-stage roles are where velocity appears — these are organisations that don't yet have the infrastructure to support a rigour-first discipline, and their JDs reflect that honestly. If you want to move fast and build new things, early-stage is structurally different from the mid-stage norm.

---

### 4.4 Stakeholder orientation: internal_data dominates

`stakeholder_orientation` identifies who the AE primarily serves: `commercial` (GTM, sales, marketing, RevOps), `product` (experimentation, funnels, product analytics), `internal_data` (other data practitioners — ML, data science, platform teams), `finance`, or `mixed`.

| stakeholder_orientation | n | % |
|-------------------------|---|---|
| internal_data | 58 | 62% |
| commercial | 11 | 12% |
| finance | 11 | 12% |
| mixed | 8 | 9% |
| product | 5 | 5% |

**62% of AE roles primarily serve internal data consumers** — other analysts, data scientists, ML engineers, or the data platform itself. This is the dominant archetype in this market. Commercial-facing and finance-facing roles are each ~12% of the market; product-focused roles are the smallest segment.

**Cross-tab with rigour:**

| stakeholder_orientation | rigour | mixed | velocity | n |
|-------------------------|--------|-------|----------|---|
| internal_data | 90% | 9% | 2% | 58 |
| finance | 91% | 9% | 0% | 11 |
| commercial | 64% | 27% | 9% | 11 |
| mixed | 75% | 25% | 0% | 8 |
| product | 60% | 40% | 0% | 5 |

Finance and internal_data roles are the most rigour-dominant. Commercial roles are the most mixed — the fastest-moving stakeholders (sales, marketing) create the most pressure on delivery speed, and JD language reflects this. Product roles are split — experimentation work has its own velocity demands.

**What this means for positioning:** If you are applying for an `internal_data` role and lead with delivery speed, you are mismatched with the employer's framing. These roles want someone who makes the data more trustworthy for downstream consumers, not someone who ships faster.

---

### 4.5 Autonomy level: execution roles outnumber strategic ones, but early-stage inverts this

`autonomy_level` separates roles where the AE sets the direction (`strategic`) from roles where they execute against a direction set by others (`execution`), with `mixed` covering roles that signal both.

| autonomy_level | n | % |
|----------------|---|---|
| execution | 37 | 40% |
| strategic | 30 | 32% |
| mixed | 26 | 28% |

**Cross-tab with data_team_maturity:**

| data_team_maturity | strategic | mixed | execution | n |
|--------------------|-----------|-------|-----------|---|
| early | 44% | 17% | 39% | 18 |
| mid | 29% | 32% | 39% | 69 |
| mature | 33% | 17% | 50% | 6 |

Early-stage companies offer more strategic autonomy than mid-stage ones — the "greenfield" signal is real. But early-stage also comes with more execution-level work by necessity (someone has to build the pipelines). Mid-stage companies, despite their scale, skew toward execution — the roadmap is set, the task is to extend it.

**The "Senior AE" autonomy gap:** Senior titles in JD language frequently use ownership framing ("own the data model", "drive analytics delivery") without granting actual direction-setting power. The `autonomy_level` coding captures this gap — many JDs classified as `execution` use senior language. This is a candidate information problem: the senior title signals seniority of execution, not seniority of strategy.

The practical implication for interviews: ask explicitly what decisions this role makes autonomously in the first year. The answer separates genuine strategic roles from senior executor roles with ownership vocabulary.

---

### 4.6 JD authorship: hiring managers write most JDs, but the signal is noisy

`jd_authorship` attempts to distinguish JDs written by the actual hiring manager (technical specificity, named tools in precise context, first-person responsibility framing) from recruiter-authored JDs (generic requirements, boilerplate culture language, tool-list format).

| jd_authorship | n | % |
|---------------|---|---|
| hiring_manager | 44 | 47% |
| mixed | 35 | 38% |
| recruiter | 14 | 15% |

**This dimension has the lowest LLM self-consistency (0.59) of any dimension in the codebook.** 77 of 93 JDs showed at least one inconsistent run across three LLM classifications. The codebook decision rules for distinguishing `hiring_manager` from `mixed` were the most ambiguous in the framework — the boundary between "specificish but not clearly technical" and "clearly written by someone technical" wasn't well-defined.

This is codebook underspecification, not a model failure. The dimension still has analytical value — `recruiter` is a relatively clear classification — but `hiring_manager` vs `mixed` should be treated cautiously.

**Cross-tab with rigour:**

| jd_authorship | rigour | mixed | velocity | n |
|---------------|--------|-------|----------|---|
| hiring_manager | 80% | 18% | 2% | 44 |
| mixed | 89% | 9% | 3% | 35 |
| recruiter | 86% | 14% | 0% | 14 |

Rigour is dominant across all authorship types — this finding does not depend on who wrote the JD.

---

### 4.7 Collaboration width: mid-stage teams serve more stakeholders than early ones

`collaboration_width` is a numeric count of named stakeholder teams mentioned in the JD's responsibilities section. It is the noisiest dimension — the LLM evidence quote pass rate dropped to ~52% because many JDs describe collaboration in generic terms ("cross-functional teams") rather than naming specific teams.

| data_team_maturity | mean collaboration_width | n |
|--------------------|--------------------------|---|
| early | 2.9 | 18 |
| mid | 2.7 | 69 |
| mature | 3.8 | 6 |

The hypothesis that early-stage teams have higher collaboration width (because data ownership is ambiguous and everyone is involved) does not hold. Mature teams have the highest named-stakeholder count, early and mid teams are similar.

**Interpretation:** Collaboration width appears to be a proxy for how far data work has penetrated an organisation, not for organisational dysfunction. Mature teams have more named stakeholders because the data function has extended to more domains, not because ownership is chaotic. Early-stage teams have fewer named stakeholders because the organisation is smaller and the data function is more narrowly scoped.

**Limitation:** The generic-collaboration-language problem means this dimension may undercount early-stage teams that have broad but informally described stakeholder involvement.

---

### 4.8 dbt prevalence: real but not universal

This was not classified as a primary Layer B dimension but was noted in the manual coding phase. Of the 41 manually coded JDs, approximately 71% of AE/BI roles mentioned dbt as a required or preferred tool.

This is consistent with the dbt report's implicit claim that dbt has become the field standard — but one in three analytics engineering roles does not require it. The European market includes meaningful Databricks SQL, BigQuery-native, and Spark-first stacks. A survey distributed through dbt's community channels cannot measure this share of the market.

---

## 5. What the survey claims vs. what JDs show

| dbt 2026 claim | JD evidence | Assessment |
|----------------|-------------|------------|
| 83% prioritise data trust | 84% rigour-oriented JDs | Directionally consistent — but JD rigour ≠ fear of AI hallucination |
| 72% prioritise AI coding | Not classifiable from JD text | No structured field; anecdotal mentions in JDs are sparse |
| AI adoption outpacing governance (72% vs 24%) | Cannot test directly | Would require `has_ai_requirement` + `has_testing_culture_signal` fields |
| Fear of hallucinated outputs (71%) | Cannot isolate in JD language | Loss-aversion framing is present in some JDs but not extracted as a structured field |
| Ambiguous data ownership persists (41%) | Collaboration width does not confirm this | Mid and early teams have similar width; ownership confusion is not detectable from JD language alone |
| dbt is the field standard | 71% of AE JDs mention dbt | True for this dataset; ~30% of AE market operates without it |

**The most important gap:** The dbt 2026 report's central anxiety — AI acceleration outpacing governance — cannot be tested from current JD data. Two schema fields would unlock this: `has_ai_requirement` (does the JD mention AI as a required skill?) and `has_testing_culture_signal` (does the JD frame testing/observability as a *responsibility*, not just a tool?). If these were classified, you could directly measure whether the governance gap (AI coding without governance requirement) appears in employer language. Currently, it cannot be confirmed or denied.

---

## 6. Theoretical interpretation

The JD findings are most usefully read through three frameworks. These are interpretive lenses applied after the fact, not pre-specified hypotheses — the dataset is too small to test theories, but the theories provide vocabulary for what the patterns suggest.

**Deming & Kahn (2018) — revealed preference:** JD requirements carry hiring cost; survey responses do not. The 84% rigour finding is a revealed preference for correctness over speed. The absence of AI requirements in most JDs is also a revealed preference — employers in 2026 have not yet institutionalised AI adoption into hiring criteria, even as they reportedly use AI tools widely. The gap between 80% AI daily use (survey) and sparse AI JD requirements (revealed preference) is the most important discrepancy in the data, and it points to informal rather than normative adoption.

**DiMaggio & Powell (1983) — mimetic isomorphism:** If organisations adopt AI coding tools because peers do (mimetic), the adoption leaves no trace in hiring language — it's not a professional standard yet, just a team behaviour. If adoption becomes normative (professionalised), it would appear in JDs as a requirement. Current evidence suggests it is still mimetic. A candidate who leads on governance is differentiated in this context, because they are institutionalising what most teams have adopted informally.

**Spence (1973) — signalling:** Under information asymmetry, costly-to-fake signals carry the most weight. "Data quality focus" is cheap to claim; quantified governance outcomes ("reduced pipeline failures by 90%", "established testing standards adopted across the organisation") are costly to fabricate because they require having done the work. The 84% rigour finding suggests that what employers signal they want is people who have actually done this — not people who say they care about it.

**Rogers (2003) — diffusion:** 74% of the market is mid-stage teams. These organisations adopted the modern data stack but not necessarily the discipline that early adopters brought. Senior AE roles at mid-stage companies are implicitly asking for someone to install that discipline retrospectively. The pitch is: "I have the rigour you built fast without."

---

## 7. What JDs cannot tell you — interview questions that fill the gap

Two factors that matter most for long-term role satisfaction cannot be inferred reliably from JD text: growth ceiling and management quality. Both are partially signalled but easily faked, because JDs are marketing documents.

### Growth ceiling

**Stronger JD signals (use these to screen):**
- Explicit cross-domain rotation or architecture exposure
- Named senior technical roles the position will partner with
- `jd_authorship = hiring_manager` — a mild positive proxy for concrete thinking about the role's development path
- `data_team_maturity = mid` — the strongest structural growth signal: active expansion creates scope to acquire

**Questions to ask:**
- "What does the person who succeeds in this role do 18 months from now — deeper in this domain, or into something different?"
- "Can you tell me about someone on the team who grew significantly in the last two years — what did their growth actually look like?"
- "What's the highest-impact decision this role would make autonomously in the first year?"

**Red flags:** Vague growth language ("the sky's the limit"), growth defined only as headcount management, no concrete example of a team member who grew.

### Management quality

**Stronger JD signals:**
- `jd_authorship = hiring_manager` — the single most useful proxy. A manager who wrote the JD with specific responsibilities has usually thought clearly about how they will manage.
- Scope that is clearly defined and internally consistent — contradictory scope ("own the strategy" but "support all stakeholders") predicts a difficult first year.

**Questions to ask:**
- "How do you typically set priorities — do you set the roadmap and hand it down, or do you build it together?"
- "What would I need to do in the first three months to make you feel confident this hire was the right one?"
- "What's one thing people who've worked for you say they wished you did differently?"

**Process signals:** Disorganised interview process mirrors disorganised management. Generic interview questions indicate the manager doesn't know what they're evaluating for. No time left for your questions predicts no space for employee questions either.

---

## 8. Schema gaps — fields that would unlock the most important questions

Three fields would allow the most valuable future analyses. They would need to be backfilled across existing records.

### `ai_role` (replaces `has_ai_requirement`)
**Type:** categorical — `none`, `ai_user`, `ai_enabler`  
**Definition:**
- `none` — no AI skill expected of the candidate. Includes JDs where the *company* builds AI products but the AE role is standard modelling work. Includes stale JDs with no AI mention at all.
- `ai_user` — the role expects the candidate to use AI tools (Copilot, Claude Code, Cursor) to accelerate their own work. The AI is the candidate's tool. *"Proven active usage of AI tools in daily work with specific examples"* (Wolt); *"Experience using AI-assisted coding or coding agents in a disciplined way"* (Mentimeter).
- `ai_enabler` — the role expects the candidate to build data infrastructure that AI systems consume or run on. The AI is downstream of the candidate's work. *"Develop the data and analytics components of the AI stack to support experimentation and GenAI applications"* (Getsafe); *"Lead implementation of AI-driven analytical capabilities including text-to-SQL and semantic modelling for conversational BI"* (Leasingmarkt); *"Implement AI data agents and automation for reporting and alerting"* (Dashlane). Where a JD signals both, `ai_enabler` takes precedence.

**Why:** The dbt 2026 report claims 72% of teams use AI in coding workflows. If this has entered employer hiring language, `ai_user` and `ai_enabler` should appear in a substantial share of JDs. Anecdotal scan suggests they don't — which would mean AI adoption is informal (teams adopt it without it becoming a hiring criterion) rather than institutionalised. A `none` from a stale JD is uninterpretable, but a pattern of `none` across recently-posted JDs would confirm the gap.

**Actionable read:** `ai_user` → demonstrate workflow efficiency with AI tools. `ai_enabler` → demonstrate data products built for AI consumption. `none` → AI is not a differentiator for this role; don't over-index on it.

**Backfill note:** Requires human or LLM judgment. Regex will misclassify company-context mentions (e.g. "AI-native infrastructure") as skill requirements. Decision rule: the candidate must be expected to *do something* with AI — use it or build for it — not merely work at a company that uses it.

---

### `testing_framing` (replaces `has_testing_culture_signal`)
**Type:** categorical — `responsibility`, `tool_listed`, `absent`  
**Definition:**
- `responsibility` — testing, data contracts, observability, or data quality frameworks are framed as something the AE *owns or defines*, using action verbs. *"Own the quality, availability, and trustworthiness of data — through quality checks and data contracts"* (freenow); *"keeping domain outputs consistent, tested, and discoverable"* (SumUp); *"Ensure Data Products follow CI/CD standards, adhere to data quality frameworks; include assertion checks"* (LEGO).
- `tool_listed` — testing tools appear in the tech stack or requirements (e.g. Great Expectations, Soda, dbt tests) but without ownership framing. The employer values the tool familiarity, not the governance practice.
- `absent` — no testing or quality signal in the JD at all.

**Why:** `velocity_vs_rigour` captures *orientation* but not *accountability*. Two JDs can both be `rigour`: one because the team values engineering craft, another because the AE will be personally accountable for data trust. `testing_framing = responsibility` is the employer signal that governance has become a hiring criterion, not just a team value. This is what would confirm or deny the dbt 2026 trust gap claim at the revealed-preference level.

**Actionable read:** `responsibility` → lead the resume with governance outcomes and ownership language. `tool_listed` → mention the tool, don't over-index. `absent` → the employer hasn't operationalised quality concern into hiring criteria; pitch to delivery.

**Backfill note:** The `velocity_vs_rigour_reasoning` field in each JSON already contains interpretive notes on why the JD was coded rigour — this will surface whether it was craft-rigour or ownership-rigour, making LLM extraction tractable from existing structured data rather than re-reading raw JD text.

---

### `loss_aversion_framing`
**Type:** categorical — `none`, `moderate`, `high`  
**Definition:**
- `none` — JD is framed in delivery and capability terms. No risk register. Typical of early-stage roles and velocity-oriented JDs.
- `moderate` — operational reliability is a concern but secondary to delivery. Fear is pipeline outages or data failures, not compliance or stakeholder trust. *"First to respond to incidents and drive resolution"* (1komma5grad); *"Reliable, high-quality datasets", "SLOs", "monitoring"* (GetYourGuide).
- `high` — risk, compliance, or stakeholder trust framing dominates. Fear is bad data reaching decision-makers or regulatory exposure. *"Insurance context means data accuracy has regulatory implications"* (Getsafe); *"IFRS 15, SOX, and audit framing dominate — frame every achievement as risk reduced"* (Wolt Revenue); *"Public sector clients mean any data failure is politically visible"* (Polyteia); *"quality checks", "data contracts", "trustworthiness" repeated throughout"* (freenow).

**Why:** `velocity_vs_rigour` cannot distinguish craft-rigour from fear-rigour. The dbt report's 71% fear-of-hallucinations claim would show up in `loss_aversion_framing = high` if it had entered employer consciousness. A concentration of `moderate` instead would suggest the fear is operational (outages) not trust-based (bad outputs reaching stakeholders) — a meaningfully different employer concern.

**Actionable read:** `high` → frame every resume bullet as risk reduced, misstatement prevented, trust established. `moderate` → lead with reliability outcomes (uptime, incident response). `none` → capability and delivery framing; governance is not the pitch.

**Backfill note:** 27 newer-format JDs already have explicit Loss aversion sections that can be extracted directly. For the 67 older-format JDs, the signal lives in `domain_risk_reasoning` and `velocity_vs_rigour_reasoning` in the JSON — these routinely contain phrases like "frame achievements as risk reduction" or "regulatory implications" that map cleanly to the scale.

---

## 9. Methodological notes

### Classification approach
The Layer B framework is a structured qualitative codebook applied by judgement. It is not an automated extraction pipeline. Dimensions were assigned by reading the full JD text and applying the codebook's decision rules. For the 41 manually coded records, one analyst (the author) did all coding — this creates internal consistency but no inter-rater reliability.

The LLM consistency study (see `consistency_report.md`) addresses this partially: it establishes that the codebook produces stable automated classifications on most dimensions. But stable LLM classifications and validated human classifications are different things. Before inter-rater work, the codebook needs revision on `jd_authorship` and `autonomy_level` — the dimensions with lowest self-consistency — to close ambiguous decision rules.

### What n=93 supports
At n=93, the margin of error on a single proportion is approximately ±10pp at 95% confidence (Wilson interval). This means the 84% rigour finding is defensible as "likely between 74% and 94%" — but not as a precise market figure. Cross-tabs with cell sizes below n=10 (mature team, product stakeholder orientation) should be treated as illustrative, not evidential.

### What the geographic concentration means
This is a European job market dataset. The dbt survey skews North American (though they don't disclose exact proportions in post-2023 years). North American AE roles may have different rigour/velocity distributions — faster-growth startups, different engineering cultures, more VC pressure. The 84% European rigour figure may not hold in the US market.

---

## Appendix A: dbt Labs survey — year-by-year detail

For reference, key metrics from the dbt reports that motivated the research questions above.

### 2023 (n=567)
- 46% plan to invest more in data quality/observability
- Most time spent maintaining datasets, not building new ones
- "Cross-team alignment on data ownership" rated worst performance area (44% poor)
- 76% of respondents already use dbt

### 2024 (n=456)
- 57% cite poor data quality as predominant issue (up from 41% in 2022)
- "Increasing data trust" = #1 org focus for the first time
- 33% experienced headcount reduction from macroeconomic conditions
- 57% currently manage or plan to manage data for AI training

### 2025 (n=459)
- AI in daily workflows: 80% (up from 30%)
- Budget growth: 30% report budget growth (vs 9% prior year)
- Team growth: 40% report team growth (vs 14% prior year)
- 45% cite AI tooling as largest investment priority

### 2026 (n=363)
- 72% prioritise AI-assisted coding; 24% prioritise AI-assisted pipeline management ("trust gap")
- Trust in data as org priority: 83% (up from 66%)
- 71% cite hallucinated or incorrect outputs reaching stakeholders as top concern
- Infrastructure costs: 57% report increased warehouse/compute spend; only 36% report increased team budgets

**Persistent comparable metrics across years:**

| Theme | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|
| Poor data quality (top concern) | 41%* | 57% | 56% | not published separately |
| Ambiguous data ownership | 44% (poor rating) | ~50% (challenge) | — | 41% (obstacle) |
| Trust in data as top priority | — | #1 (qualitative) | 66% | 83% |
| Budget growth | — | contracting | 30% growth | 36% team budgets growing |

*2022 baseline from 2024 report retrospective.

Data quality concern has been essentially flat at 56–57% for two consecutive years despite being named as the #1 investment priority in 2023. Either the investment didn't resolve it, or the investment was stated preference rather than revealed preference — which is the Deming & Kahn point applied to organisations themselves.

---

## Appendix B: Academic reviewer critique and journal submission path

For a potential journal submission, the primary outlet recommendation is *Information Systems Journal* (ABS 3), positioning the paper as a critical IS discourse study with a pilot JD empirical component.

**Six issues a reviewer would raise:**

1. **No methodology section.** State plainly: structured qualitative content analysis, single coder, Layer B framework as coding instrument. Cite Krippendorff (2018). Acknowledge single-coder limitation upfront.

2. **Single-coder reliability.** Not fixable without a second coder on a 20% random sample (~19 JDs) with kappa reported per dimension. The LLM consistency study is a diagnostic for codebook revision, not a substitute for human inter-rater reliability.

3. **n=93 is pilot-scale.** For a chi-squared test across a 3×3 domain_risk × velocity_vs_rigour table to be defensible (p<0.05), need minimum expected cell frequency ≥5, which requires approximately n=150 across 9 cells. For geographic subgroup analysis, n≈300. Current findings should be labelled "directional observations from a pilot dataset."

4. **Vendor-produced primary source.** Every claim of the form "X% of analytics engineers do Y" should be rewritten as "dbt Labs' survey reports that X% of dbt community respondents say Y." The paper is a discourse study of a vendor-produced survey, not a study of analytics engineers broadly.

5. **Six theories cited, none tested.** Pick one — Abrahamson's management fashion theory is the most tractable. Derive two explicit predictions from it before presenting findings; structure the findings sections around testing those predictions.

6. **No literature review.** Three streams needed: vendor knowledge production/management fashion (Abrahamson 1996), critical IS and technology discourse (Orlikowski & Barley 2001), job postings as labour market data (Deming & Kahn 2018, Hershbein & Kahn 2018).

---

## Appendix C: Forward Data Conference proposal

**Conference:** Forward Data, Paris, 16 November 2026  
**CFP deadline:** 24 July 2026  
**Target:** Theme 01 — Data Foundations for Humans & AI → *Data Quality & Trust in the Agentic Era*  
**Format:** 25-minute Regular Talk

**Proposed title:** "363 self-selected dbt users vs. 94 revealed-preference job descriptions: what the 2026 governance panic actually shows up in employer hiring language"

**Abstract:**

Every year dbt Labs publishes a survey of the analytics engineering community. Every year it headlines a new central anxiety. In 2026 it is governance: AI adoption is outpacing trust, 71% fear hallucinated outputs, 83% now rank data trust as their top priority.

The report is widely read. Its vocabulary circulates through hiring managers and conference talks within weeks. But the sample is 363 self-selected respondents from dbt's own community channels. And surveys measure stated preferences. Job postings measure revealed ones.

I collected 94 analytics engineering job postings from April–June 2026 across Europe. I classified each on seven behavioural dimensions using a structured codebook, then ran an LLM consistency study — three independent classification passes per JD — to test whether the framework was producing stable results.

What I found: 84% of JDs signal rigour orientation, 0% signal pure velocity. The governance framing is in employer language — but not in the fear-of-AI-hallucination form the report predicts. The LLM self-consistency was 0.92; manual–LLM agreement was 0.35. That gap is the finding: a classification system that is internally stable but doesn't match its own author's classifications is not a reliability failure — it is a codebook validity signal. The dimension with the lowest consistency (`jd_authorship`) is also the one that most directly reveals whether the governance discourse has reached the people who make hiring decisions.

This talk covers what the 94 JDs show, what they can't show, and what broke in the methodology — because what broke is more interesting than what worked.

**Talk structure (25 minutes):**
- 0–3 min: What revealed-preference data is and why it's different from a survey
- 3–8 min: Four years of dbt report narrative in three slides — each year's anxiety, each year's product
- 8–16 min: What the 94 JDs show: the 84% rigour finding, the domain-risk cross-tab, the maturity split, the stakeholder distribution
- 16–21 min: What broke — the LLM consistency study, the 0.92 vs 0.35 gap, the codebook validity lesson
- 21–24 min: What this means if you're writing the JD or applying to one
- 24–25 min: The dataset is open; send me your JDs

---

## Sources

- dbt Labs, "State of Analytics Engineering" (2023–2026). Raw 2023 data: github.com/dbt-labs/analytics-engineering-survey
- Deming, D. and Kahn, L.B. (2018). "Skill Requirements across Firms and Labor Markets." *Journal of Labor Economics*, 36(S1), S337–S369. DOI: 10.1086/694106.
- Abrahamson, E. (1996). "Management Fashion." *Academy of Management Review*, 21(1), 254–285.
- DiMaggio, P.J. and Powell, W.W. (1983). "The Iron Cage Revisited." *American Sociological Review*, 48, 147–160.
- Spence, M. (1973). "Job Market Signaling." *Quarterly Journal of Economics*, 87(3), 355–374.
- Rogers, E.M. (2003). *Diffusion of Innovations* (5th ed.). Free Press.
- Collingridge, D. (1980). *The Social Control of Technology*. Frances Pinter.
- Weick, K.E. (1995). *Sensemaking in Organizations*. Sage.
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). Sage.
- Orlikowski, W.J. and Barley, S.R. (2001). "Technology and Institutions." *MIS Quarterly*, 25(2), 145–165.
- Hershbein, B. and Kahn, L.B. (2018). "Do Recessions Accelerate Routine-Biased Technological Change?" *American Economic Review*, 108(7), 1737–1772.
