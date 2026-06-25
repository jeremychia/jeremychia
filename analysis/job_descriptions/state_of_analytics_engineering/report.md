# State of Analytics Engineering (dbt Labs, 2023–2026) — Research Analysis

**Prepared:** June 2026  
**Dataset:** 37 JD records from `jd_data/` (April–June 2026, primarily European/Berlin market; original manual classifications in `resume/analysis/applications_dataset.csv`)  
**Source reports:** dbt Labs annual surveys — 2023 (n=567), 2024 (n=456), 2025 (n=459), 2026 (n=363)

---

## 1. What this document is

This is a critical reading of dbt Labs' annual "State of Analytics Engineering" reports (2023–2026), cross-referenced against a dataset of real job descriptions collected during the same period. The goal is to:

1. Identify year-on-year trends in what the reports claim
2. Analyse how the tonality and framing have shifted
3. Catalogue the assertions being made — especially in 2026
4. Define research questions that can be tested against actual JD market data
5. Identify gaps in the current JD schema that would enable better validation

**Critical caveat:** The dbt Labs reports are based on self-selected surveys distributed through dbt's own community channels (Slack, newsletter, events). They are not neutral industry surveys. As confirmed from the 2023 raw data, 76% of respondents already use dbt — meaning findings describe the dbt community, not the analytics engineering profession broadly. This constraint is never acknowledged in the reports themselves.

---

## 2. Year-by-year findings

### 2023 (survey Oct–Nov 2022, n=567)

**Survey demographics:** 40% Analytics Engineer or Data Engineer titles; 20% managers/leads; 76% from dbt-using companies; 95% from North America, Europe, or APAC. Tech, Consulting, and Financial Services = 59% of respondents.

**Key findings:**
- 46% plan to invest more in data quality/observability — top investment priority
- Most time spent maintaining datasets, not building new ones
- "Cross-team alignment on data ownership" rated worst of all performance areas — 44% rate it poorly
- dbt characterised as "blurring the line" between data engineers and data analysts

**Character:** Definitional. This is the report that establishes what "analytics engineering" means — it leans heavily on category creation. The 2023 report is the only year in which the raw survey data was publicly released (GitHub repo, now archived).

---

### 2024 (survey Dec 2023–Mar 2024, n=456)

**Survey demographics:** Not fully disclosed; collection window 3+ months (Dec 22 – Mar 2, 2024).

**Key findings:**
- 57% cite poor data quality as predominant issue (up from 41% in 2022; comparable question)
- "Increasing data trust" = #1 org focus for the first time
- Ambiguous data ownership = 2nd most cited challenge, ~50% of respondents (up from 44% in 2023)
- 57% currently manage or plan to manage data for AI training
- 33% experienced headcount reduction from macroeconomic conditions; half report no change
- North America: 78% of AEs earn >$100K
- "Building data transformations" and "compute constraints" drop to bottom of concerns — technical problems largely solved; people and process problems dominate

**Character:** Cautiously sober. Post-VC winter. The first report to explicitly acknowledge budget cuts. Framing shifts from "here's what analytics engineering is" to "here are the hard unsolved problems" — and the answer is: human and organisational, not technical.

---

### 2025 (survey Oct–Dec 2024, n=459, 70% ICs / 30% managers)

**Survey demographics:** 48% analytics engineers, 36% data engineers, 16% data analysts; 70% individual contributors, 30% managers.

**Key findings:**
- AI in daily workflows: 80% — the largest single-year jump in any metric across the entire series (up from 30%)
- Of AI users: 70% for code development, 50% for documentation
- Budget growth: 30% report budget growth (vs 9% prior year; comparable question)
- Team growth: 40% report team growth (vs 14% prior year; comparable question)
- 45% cite AI tooling as largest investment priority
- 38% cite data quality/observability as investment priority
- 56% still identify poor data quality as primary challenge (stable vs 2024's 57%)
- North America ICs: 80% earn >$100K (up from 69%); managers: 49% exceed $200K (up from 32%)

**Character:** Euphoric. Directly counter-addresses AI displacement anxiety. The "80% use AI daily" headline was widely republished and serves a field-legitimacy function: practitioners needed to hear that AI makes data teams more valuable, not redundant. Budget and salary recovery stats reinforce this. The "augments, doesn't replace" framing is explicit anxiety management.

**Caution:** The 80% AI adoption stat is an extraordinary claim. "Using AI in daily workflow" likely includes GitHub Copilot autocomplete. The 70% "using AI for code development" breakdown is consistent with this low-bar interpretation.

---

### 2026 (survey Dec 2025–Feb 2026, n=363, 73% practitioners / 27% managers)

**Survey demographics:** 73% practitioners, 27% managers/executives. Smallest sample in the series — 36% smaller than the 2023 baseline, 21% smaller than 2025. No reason stated by dbt Labs.

**Key findings:**
- 72% prioritise AI-assisted coding in development workflows
- Only 24% prioritise AI-assisted pipeline management (testing, observability) — named the "trust gap"
- Trust in data as org priority: 83% (up from 66%; largest single-year jump on this metric, +17pp)
- Speed as priority: 71% (up from 50%; comparable question)
- 71% cite hallucinated or incorrect outputs reaching stakeholders as top concern
- Infrastructure costs: 57% report increased warehouse/compute spend; only 36% report increased team budgets
- Ambiguous data ownership: 41% face this as an obstacle (down from ~50% in 2024, still #2 structural blocker)
- Technical integration challenges: 27% (down from 35%; comparable question)

**Character:** Governance alarm. The tone shifts from reassurance to urgency. "AI acceleration is outpacing trust and governance" is the central claim — and it maps precisely onto dbt's product positioning around contracts, testing, and observability. The report creates the urgency; the product resolves it.

**Note on sample decline:** A 21% drop in a single year is notable. Plausible explanations: survey fatigue, dbt community contraction as Databricks-native and Python-first stacks compete for mindshare, or data role layoffs reducing the practitioner population. dbt Labs offers no explanation.

---

## 3. Persistent themes across years (comparable metrics)

The table below tracks only metrics where the same or directly comparable question was asked in multiple years.

| Theme | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|
| **Poor data quality (top concern)** | 41%* | 57% | 56% | (comparable not published separately) |
| **Ambiguous data ownership** | 44% (poor rating) | ~50% (challenge) | — | 41% (obstacle) |
| **Technical integration as challenge** | — | 35% | — | 27% |
| **Budget growth** | — | contracting | 30% growth | 36% team budgets growing |
| **Team growth** | — | 33% headcount cuts | 40% growth | — |
| **Trust in data as top priority** | — | #1 (qualitative) | 66% | 83% |
| **Speed as priority** | — | — | 50% | 71% |

*2022 baseline from 2024 report retrospective.

**Key observations from the comparable data:**

1. Data quality concern has been stable at ~56–57% for at least two years (2024–2025). Not improving despite investment. This suggests the investment announcements in 2023 didn't resolve the problem.

2. Data ownership is a persistent multi-year structural problem. It appears in every report in slightly different framing but has not improved materially. The 2026 decline from ~50% to 41% is directionally positive but may reflect question rewording.

3. The trust priority shift (66% → 83%) is the most dramatic year-on-year change in 2026. However, at n=363 from a self-selected sample, a 17pp swing should be treated as a signal rather than a precise measurement.

4. Technical integration dropping from 35% to 27% suggests tooling has genuinely improved — the modern data stack has commoditised infrastructure. This is the one structural problem the reports claim was actually solved.

---

## 4. Trend analysis

**2023→2024:** The profession pivots from defining itself to confronting its hard problems. The frame shifts from "what is analytics engineering" to "what prevents us from doing it well." The answer: human and process failures, not technical ones.

**2024→2025:** The AI wave hits. The dominant narrative becomes adoption velocity. The community is told (and believed) that AI use has tripled in twelve months. Budget and hiring rebounded from 2023's VC winter, giving the field a growth story it needed.

**2025→2026:** The wave breaks. After a year of 80% adoption claims, the 2026 report pivots to the hangover: AI is generating output faster than anyone can validate it. Trust is the new speed. Governance is the new growth. This is a predictable second-order effect of the 2025 adoption narrative — fast adoption without discipline creates quality risk.

**The pattern:** Each year's report builds on the previous year's anxiety. 2023 established the field. 2024 named the people problems. 2025 promised that AI solves the velocity problem. 2026 warns that AI creates a new governance problem. dbt's products address each: modelling discipline (2023), data contracts (2024), AI assist (2025), observability/trust (2026).

---

## 5. Tonality and framing analysis

| Year | Dominant register | Key rhetorical move |
|------|-------------------|---------------------|
| 2023 | **Aspirational / definitional** | Category creation — "analytics engineering is a profession" |
| 2024 | **Diagnostic / sober** | Problem identification — "the hard problems are human ones" |
| 2025 | **Euphoric / reassurance** | Anxiety inoculation — "AI helps, it doesn't replace" |
| 2026 | **Alarmed / prescriptive** | Urgency creation — "governance must become infrastructure" |

The 2025 report was written during AI hype peak (data collected Oct–Dec 2024). Its reassurance function is explicit: the 80% adoption stat is headlined as validation, not alarm. The 2026 report is written after the hype began to consolidate — the field has had a year of using AI and is discovering the trust failures.

**Weick's sensemaking lens (1995):** The report is not just a measurement instrument — it is a sensemaking artefact that constitutes how practitioners understand their professional moment. The 2023→2026 shift from aspiration to alarm is a collective sensemaking transition, regardless of whether the underlying data supports it at the precision implied. By providing shared vocabulary ("trust gap", "governance as infrastructure"), the report enables the community to coordinate meaning — and to feel they are part of a coherent professional narrative.

**Abrahamson's management fashion lens (Academy of Management Review, 1996):** dbt Labs functions as a fashion setter. By publishing annually and coining terms, it defines what the field should care about. The narrative must refresh each year to sustain attention. The 2026 "governance alarm" is structurally necessary — it replaces the 2025 "AI euphoria" and extends the report's agenda-setting power.

---

## 6. Methodological critique

### 6.1 Self-selection bias

The survey is distributed through dbt's community channels. In 2023, 76% of respondents already use dbt. Later years do not disclose this figure — but the distribution channel has not changed. This means every finding is a claim about *the dbt community*, not "analytics engineering professionals" broadly.

As established in survey research methodology (Lavrakas, ed., *Encyclopedia of Survey Research Methods*, Sage, 2008), self-selection creates a "digital echo" — participants share ideological and demographic characteristics. The dbt community skews: early adopter, tech-sector, North America/Europe, SQL-first, cloud-native. Conclusions about "data professionals" drawn from this sample do not generalise.

### 6.2 Shrinking sample

| Year | n | Change |
|------|---|--------|
| 2023 | 567 | — |
| 2024 | 456 | −20% |
| 2025 | 459 | stable |
| 2026 | 363 | −21% |

The 2026 sample is 36% below the 2023 baseline. At n=363 with non-random sampling, the margin of error on any percentage is roughly ±5pp at 95% confidence — even before accounting for self-selection bias. Year-on-year comparisons at this sample size should be treated as directional signals only.

### 6.3 Comparable vs non-comparable metrics

The reports frequently imply trend lines across years using statistics from different questions. In this analysis, only directly comparable questions (same construct, same framing) are tracked as trends. For example:
- Data quality as top concern: 57% (2024) → 56% (2025) — comparable, stable
- "46% plan to invest in data quality" (2023 intent) vs "57% cite it as concern" (2024 experience) — not comparable; not presented as a trend here

### 6.4 The product-market fit loop

Each year's narrative aligns with dbt's product announcements at the time of publication:
- 2024 report → dbt data contracts launch
- 2025 report → dbt Copilot / AI assist
- 2026 report → observability, governance, trust features

This alignment may be coincidental — the same market forces that shape practitioner anxiety also shape product priorities. But it creates a structural incentive to define the problem in terms dbt can solve, and the report is not independent of this.

---

## 7. 2026 assertions mapped to Layer B dimensions

The `adapt-resume` skill captures "Layer B" behavioural signals from each JD. The table below maps each 2026 report assertion to the Layer B dimension that would capture its presence (or absence) in employer language.

| 2026 Assertion | Layer B dimension | What JD evidence would look like if true |
|----------------|-------------------|------------------------------------------|
| AI adoption (72%) outpacing governance investment (24%) | **Loss aversion** | JDs frame the role in risk-reduction terms — "prevent bad data reaching stakeholders", "own data reliability" — not just "build pipelines faster" |
| Trust in data is now #1 priority (83%) | **Loss aversion** + **domain_risk** | High-domain-risk JDs (finance, fintech) should cluster on rigour + loss-aversion framing; "data accuracy" framed as business risk, not technical metric |
| Ambiguous data ownership persists (41%) | **Collaboration width** | Roles with many named stakeholder teams but early-stage data teams signal unresolved ownership — no central data authority yet |
| AI acceleration outpacing governance | **Velocity vs rigour** | If the assertion has entered employer consciousness, `rigour` should dominate JDs. `velocity` signals would indicate the governance discourse hasn't reached hiring language |
| Discipline in modelling is now a requirement, not a best practice | **JD authorship** | Hiring manager-authored JDs (vs recruiter) should include specific governance requirements — data contracts, testing mandates, observability frameworks |
| Infrastructure costs outpacing team budgets | Not captured in JD text | Cannot test from JD data; requires external budget/salary datasets |
| Agentic AI makes discipline mandatory | **Seniority signals** | Roles framing themselves as "you will define standards" or "establish governance" suggest employers are seeking someone to solve this — signals the problem is real in their org |

---

## 8. Theoretical frameworks applied

### 8.1 Collingridge Dilemma (Collingridge, 1980) — Science & Technology Studies

> "When change is easy, the need for it cannot be foreseen; when the need for change is apparent, change has become expensive, difficult, and time-consuming."

**Source:** David Collingridge, *The Social Control of Technology* (Frances Pinter, London, 1980). ISBN: 0903804727.

The 2026 report's central thesis is a textbook Collingridge instance. AI adoption was fast and cheap to enable (Copilot integration, prompt-based querying). Its governance implications were not predictable until adoption was widespread. By the time 72% of teams are coding with AI, changing the governance model is expensive — it requires re-architecting testing practices, data contracts, and observability across existing pipelines.

The report frames this as a discovered finding. The Collingridge dilemma predicts it as inevitable. The implication is not that teams failed to plan — it is that governance of fast-moving technologies is structurally late by design.

### 8.2 Diffusion of Innovations (Rogers, 1962/2003) — Rural Sociology / Communication Studies

**Source:** Everett M. Rogers, *Diffusion of Innovations* (1st ed., Free Press of Glencoe, 1962; 5th ed., Free Press, 2003).

Rogers' adoption curve maps directly onto the dbt report series:

- **2023:** Early adopter phase. The field is defining itself. Adoption is concentrated in tech-forward teams with high SQL maturity.
- **2025:** Early majority crossing. 80% AI adoption signals mass-market penetration. The community has crossed the chasm.
- **2026:** Early majority consequence. This cohort adopts tools before developing the discipline of the innovators who preceded them. Governance gaps are characteristic of this phase — not a failure of individual teams but a structural property of mass adoption.

Rogers also notes that fashion setter dynamics intensify during the early majority phase — which is precisely when Abrahamson's management fashion framework kicks in (see 8.4).

### 8.3 Institutional Isomorphism (DiMaggio & Powell, 1983) — Organisational Sociology

**Source:** Paul J. DiMaggio and Walter W. Powell, "The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality in Organizational Fields," *American Sociological Review*, Vol. 48 (1983), pp. 147–160. DOI: 10.2307/2095101.

DiMaggio & Powell identify three mechanisms by which organisations become similar: coercive (regulatory pressure), **mimetic** (copying under uncertainty), and normative (professionalisation).

The 72% AI coding / 24% governance gap is a textbook mimetic isomorphism pattern:
- Teams adopt AI coding tools because peers do — the tool is visible, fast-moving, and discussed publicly
- Governance investment is invisible and slow — no one presents "we increased test coverage by 20%" at a conference
- Under uncertainty (what does good AI data practice look like?), teams copy what is publicly celebrated rather than what is structurally sound

DiMaggio & Powell note that mimetic adoption "makes organisations more similar without necessarily making them more efficient." The dbt community adopted the same tool (AI coding) for similar reasons (peer pressure) without necessarily the same effectiveness.

**JD data connection:** If mimetic isomorphism is driving AI adoption, we would expect AI experience to appear in JDs *without* accompanying governance requirements. The proposed `has_ai_requirement` vs `has_testing_culture_signal` schema fields would test this directly.

### 8.4 Management Fashion Theory (Abrahamson, 1996) — Organisational Behaviour / Management Studies

**Source:** Eric Abrahamson, "Management Fashion," *Academy of Management Review*, Vol. 21, No. 1 (January 1996), pp. 254–285. JSTOR: 258636. DOI: 10.5465/amr.1996.9602161572.

Abrahamson defines management fashions as "transitory collective beliefs that certain management techniques are at the forefront of management progress." Fashion setters generate and sustain these beliefs through rhetoric, framing devices, and annual publication cycles.

The dbt Labs "State of Analytics Engineering" is a management fashion document by Abrahamson's definition:
- It is annual and must introduce a new central anxiety each year to sustain attention
- It uses rhetorical devices ("trust gap", "governance as infrastructure") that practitioners adopt as vocabulary
- It positions dbt's products as the resolution to the problem it names
- Its findings follow social logic (what practitioners feel) as much as technical logic (what data shows)

This does not make the findings false — it means they should be read as community sentiment reports, not objective market measurement. Abrahamson's framework would predict that "governance" becomes the dominant analytics engineering discourse in 2026–2027, regardless of whether underlying practice changes, because the fashion has been set.

### 8.5 Job Market Signalling (Spence, 1973) — Labour Economics

**Source:** Michael Spence, "Job Market Signaling," *The Quarterly Journal of Economics*, Vol. 87, Issue 3 (August 1973), pp. 355–374. DOI: 10.2307/1882010.

Spence's signalling theory establishes that under information asymmetry, observable signals proxy unobservable qualities. Employers use JD language as a signal of organisational culture and maturity to attract candidates.

Applied to this analysis: the *presence or absence* of governance language in JDs ("data contracts", "observability as a responsibility", "you will define testing standards") is an employer signal. If the 2026 report's anxiety is real and has entered organisational consciousness, it should appear in what employers ask for — not just in what practitioners report in surveys.

The absence of such language in JDs would suggest the discourse is circulating at the community/identity level (conference talks, survey responses) but has not yet translated into hiring decisions. This is the most important gap to measure.

### 8.6 Job Postings as Revealed Preference (Deming & Kahn, 2018) — Labour Economics

**Source:** David Deming and Lisa B. Kahn, "Skill Requirements across Firms and Labor Markets: Evidence from Job Postings for Professionals," *Journal of Labor Economics*, Vol. 36, No. S1 (2018), pp. S337–S369. DOI: 10.1086/694106. NBER Working Paper 23328.

Deming & Kahn establish that job postings are revealed-preference data — employers write what they actually value when faced with the cost of searching. This contrasts with survey responses, which reflect stated preferences. Within-occupation variation in JD language is substantial, meaning two "analytics engineer" JDs may be asking for fundamentally different things.

This validates the JD dataset as an analytical counterweight to the survey data. If the dbt report says "83% prioritise trust in data," the JD dataset asks: are employers *paying* for that priority by requiring it in hires? A survey respondent can state a priority at no cost; a JD requirement carries real hiring cost.

**Implied action:** Match the JD's *revealed* priority, not the survey-stated one. If a JD mentions dbt but not testing culture, the employer's actual preference is delivery — regardless of what a practitioner survey would elicit from their team. Pitch to what the JD asks for, not to the community anxiety the report describes.

---

## 8.7 What each theory implies — action synthesis

The theories are not just descriptive. Each one carries an implication for how to read JDs and how to position a candidate.

**Collingridge Dilemma → look for the early signal, not the mature practice.**
Governance requirements will not be widespread in JDs yet — the dilemma predicts governance is always structurally late. A JD that already requires testing culture or data contracts is signalling an employer ahead of the curve. These roles are worth prioritising: the employer understands the problem before most of the market does.

**Rogers' Diffusion → early-majority employers need what they skipped.**
Most of the market (mid-maturity teams, the largest segment in the JD dataset at 49%) adopted the modern data stack but not the discipline that early adopters brought with it. Senior and staff AE roles at mid-maturity companies are implicitly asking for someone to install that discipline retrospectively. The pitch is: "I have the rigour you built fast without."

**DiMaggio & Powell (Mimetic Isomorphism) → lead with what others aren't doing.**
If organisations are copying each other on AI adoption but not governance, a candidate who leads on governance is differentiated. The resume should not mirror what everyone claims (AI coding, pipeline building) — it should lead with what most people have not yet operationalised: testing standards, data contracts, reliability outcomes. That is the contrarian signal that cuts through mimetic convergence.

**Abrahamson (Management Fashion) → use the 2026 vocabulary deliberately.**
The vocabulary in the 2026 report — "trust gap", "governance as infrastructure", "discipline in modelling becomes a requirement" — will circulate through hiring managers' heads, especially those who follow the dbt community. Resume and cover letter language that mirrors this framing will read as current and self-aware. This is not cynicism; it is fashion literacy. The vocabulary was coined by someone reading the same market signals the hiring manager reads.

**Spence (Signalling) → quantified governance outcomes are costly-to-fake signals.**
Under information asymmetry, signals that are expensive to fabricate carry the most weight. Vague claims of "data quality focus" are cheap — every candidate makes them. Quantified governance outcomes ("reduced pipeline failures by 90%", "established testing standards adopted across the organisation", "cut data incident response time from days to hours") are costly to fake because they require having actually done the work. These are the signals to lead with.

**Deming & Kahn (Revealed Preference) → pitch to what the JD asks for, not what the report says teams want.**
A JD that mentions dbt but not testing culture is revealing that the employer's actual priority is delivery speed, regardless of what a survey would show. Read each JD as a revealed-preference document and pitch accordingly — the community discourse about governance may not yet have reached this particular hiring manager. The 35% of JDs classified as `mixed` on velocity vs rigour are the most ambiguous cases: they require reading which signals come first (primacy bias in the skill list, seniority language, stakeholder scope) to determine the true revealed preference.

---

## 9. Research questions and JD dataset evidence

**Dataset:** 37 records, April–June 2026, primarily European/Berlin market. Role type breakdown: 28 analytics_engineering_bi, 4 team_lead, 3 data_engineering, 2 other. Seniority in AE roles: 54% senior, 36% mid, 7% staff, 4% lead.

---

### RQ1: Is rigour the dominant market signal in 2026 JDs?

**Why this matters:** The 2026 report asserts governance/discipline has become the field's top concern. If true, JD language should reflect this — employers recruiting for analytics engineering should emphasise testing, validation, and reliability over speed.

**Result:**

| velocity_vs_rigour | All (n=37) | AE only (n=28) |
|--------------------|-----------|----------------|
| rigour | 65% (24) | 64% (18) |
| mixed | 30% (11) | 36% (10) |
| velocity | 5% (2) | 0% (0) |

**Interpretation:** Rigour dominates strongly — 65% of all JDs and 64% of AE JDs signal a rigour orientation. Notably, no pure AE role signals velocity. This is broadly consistent with the report's claim that governance and trust are now market priorities. However, this is a qualitative classification based on Layer B analysis, not a structured field measuring whether testing/governance is explicitly *required* (see RQ5 below).

---

### RQ2: Does domain risk cluster with rigour framing?

**Why this matters:** The report claims 71% fear bad data outputs reaching stakeholders — with higher stakes in high-risk domains (finance, fintech). High `domain_risk` roles should cluster on `rigour`.

**Result:**

| domain_risk | rigour | mixed | velocity | n |
|-------------|--------|-------|----------|---|
| high | 56% | 38% | 6% | 16 |
| moderate | 71% | 29% | 0% | 17 |
| low | 75% | 0% | 25% | 4 |

**Interpretation:** Counterintuitively, `moderate` domain risk roles are *more* rigour-dominant than `high` risk roles. High-risk roles (fintech, finance, marketplace) have a higher proportion of `mixed` signals — they balance speed with rigour rather than prioritising rigour exclusively. This may reflect that high-stakes businesses also have more time-pressure on their data work. The result does not straightforwardly validate the report's fear-of-bad-outputs claim as showing up in hiring language.

---

### RQ3: Does collaboration width proxy unresolved data ownership?

**Why this matters:** The report's persistent finding on ambiguous data ownership (41–50% across years) should manifest as a structural pattern — teams with many stakeholders but low maturity, where ownership questions remain open.

**Result:**

| data_team_maturity | avg collaboration_width | n |
|--------------------|------------------------|---|
| early | 2.7 | 14 |
| mid | 3.6 | 18 |
| mature | 4.6 | 5 |

**Interpretation:** Collaboration width *increases* with team maturity, not decreases. This is the opposite of the "unresolved ownership" hypothesis. Early-stage data teams have narrower stakeholder scope — they serve fewer functions because the organisation hasn't yet integrated data work broadly. As teams mature, they serve more stakeholders, not fewer. This suggests collaboration width is a proxy for organisational data penetration, not ownership confusion. The ownership problem may be orthogonal to team size.

---

### RQ4: How prevalent is dbt in JDs?

**Why this matters:** The dbt reports implicitly treat "analytics engineering" and "dbt user" as near-synonymous. JD data can test whether dbt has truly become the field standard.

**Result:**

| | All (n=37) | AE/BI only (n=28) |
|--|-----------|------------------|
| has_dbt = True | 68% (25) | 71% (20) |
| has_dbt = False | 32% (12) | 29% (8) |

**Interpretation:** 71% of AE/BI roles mention dbt — a high but not universal rate. One in three analytics engineering JDs does not require dbt. This is consistent with the sampling bias critique: a dbt-community survey would naturally show near-universal dbt familiarity, but the actual market still has significant dbt-free demand (Databricks SQL, Spark-native, BigQuery-first stacks, etc.).

**JD authorship breakdown:**

| jd_authorship | % of all |
|---------------|----------|
| hiring_manager | 54% |
| mixed | 32% |
| recruiter | 14% |

The majority of JDs in this dataset are hiring-manager authored — a signal of technical specificity rather than generic role descriptions.

---

### RQ5: Does loss aversion framing show up in JD language?

**Why this matters:** The report's 71% "fear of hallucinated outputs" finding is the most visceral claim in 2026. If employers feel this, it should appear in JD language — roles framed in terms of preventing bad data reaching stakeholders, data reliability as a risk-reduction outcome, governance as a mandatory responsibility.

**Current limitation:** This is the most important question the schema cannot currently answer. The `velocity_vs_rigour` field captures orientation but not the specific framing of *why* rigour matters. Two JDs can both be `rigour`-oriented: one because the company cares about engineering craft, and another because they fear a compliance failure or an executive making a decision on bad AI output.

**What the Layer B behavioural analysis does capture:** The `loss_aversion` field in each jd.md documents whether the JD uses risk-reduction framing. However, this is not currently extracted into a structured schema field.

**Assessment:** The JD dataset cannot test the fear-of-hallucinations claim without schema addition. See Section 10.

---

## 10. Schema extension proposals

Three new boolean/categorical fields would unlock the most important research questions. These would extend the JSON schema in `jd_data/` and require backfilling existing records.

### Field 1: `has_ai_requirement`

| Property | Value |
|----------|-------|
| Type | boolean |
| Definition | JD mentions AI, LLM, GenAI, or "AI-assisted" in required or preferred skills/responsibilities |
| Why | Tests whether employer demand has translated survey AI adoption (72–80%) into hiring requirements. If most JDs lack this despite high reported team adoption, the adoption is informal, not yet institutionalised in hiring |
| DiMaggio & Powell connection | Mimetic adoption (copying peers) leaves no trace in JDs; normative adoption (professionalisation) does |

### Field 2: `has_testing_culture_signal`

| Property | Value |
|----------|-------|
| Type | boolean |
| Definition | JD explicitly frames testing, data contracts, observability, or data quality frameworks as *responsibilities* of the role — not just named tools in a tech list |
| Why | Distinguishes tool presence (`has_soda = True`) from cultural expectation. The 2026 "trust gap" (72% AI coding vs 24% governance investment) would show up here — if governance hasn't entered employer requirements despite community anxiety, the gap is real |
| Spence connection | This is the employer signal that governance maturity is valued, not just stated |
| Note | Distinct from `has_ai_requirement` — a JD can require AI skills without requiring testing culture, and vice versa |

### Field 3: `loss_aversion_framing`

| Property | Value |
|----------|-------|
| Type | categorical: `none`, `moderate`, `high` |
| Definition | Degree to which the JD frames the role in risk-reduction, reliability, or compliance terms — "prevent bad data reaching stakeholders", "data accuracy has direct business impact", "you will be responsible for data trust" |
| Why | The most important unstructured signal currently in Layer B. Maps directly to the 2026 report's 71% fear-of-hallucinations claim. If employers feel this, it should appear in role framing. `none` = purely technical/delivery framing; `moderate` = reliability mentioned but not central; `high` = risk/compliance/trust framing dominates |
| Weick connection | This is the dimension that reveals whether sensemaking has transferred from the community discourse level into institutional hiring language |

---

## 11. Conclusions and honest caveats

### What the reports tell us (with appropriate weight)

1. **Data quality and ownership are genuinely unsolved.** Across all four years, data quality concern and ambiguous ownership appear in every report. These are real problems — not manufactured urgency. The JD data's 65% rigour orientation is broadly consistent.

2. **AI adoption happened fast, and the governance response is lagging.** The 2025 → 2026 pivot from "80% adoption" to "governance gap" follows a structurally predictable pattern (Collingridge dilemma, Rogers' early majority transition). Whether the gap is as large as claimed is unknowable from survey data alone.

3. **The trust framing has entered employer language — but not structurally.** The JD dataset shows rigour dominates (65%), which is consistent with the report's claims. But without `loss_aversion_framing` and `has_testing_culture_signal` fields, we cannot distinguish employers who want "disciplined engineers" from employers who are specifically worried about AI-generated errors reaching decision-makers.

4. **dbt is real but not universal.** 71% of AE JDs mention dbt — high but not total. One in three analytics engineering roles does not require it, pointing to the limitation of a survey conducted through the dbt community as a window onto the full market.

### What the reports do not tell us

- Whether adoption statistics reflect genuine practice change or social desirability ("yes, I use AI daily" covers everything from Copilot autocomplete to autonomous pipeline orchestration)
- Whether the reported priorities translate into hiring decisions (the Deming & Kahn distinction between stated and revealed preference)
- Whether trends are real or artefacts of question changes and self-selection shifts across years
- Why the sample is declining — potentially the most interesting untold story

### What the JD dataset adds

The JD dataset is small (n=37) and geographically concentrated (European/Berlin market). But it is revealed-preference data. The 65% rigour finding, the cross-tab showing moderate-risk roles are more rigour-dominant than high-risk ones, and the 71% dbt presence rate are all things the survey cannot capture. Together, the JD data provides a partial but useful ground truth.

The most important gap is the absence of `loss_aversion_framing` — the dimension that would most directly test whether the 2026 report's central anxiety (fear of bad AI outputs) has entered employer consciousness, or whether it remains community discourse that hasn't yet translated into what companies actually hire for.

---

---

## 12. Academic reviewer critique — action plan for journal submission

### Choose the outlet first

The right journal determines what the paper needs. Pick one lane before doing any other work — everything else follows from the framing decision.

| If you lead with… | Submit to | ABS | What this requires |
|-------------------|-----------|-----|-------------------|
| Vendor discourse / professional identity construction | *Information Systems Journal* (Wiley) | 3 | Critical discourse analysis as explicit method; JD dataset as pilot empirical counter-discourse. Most achievable at current scope. |
| Vendor discourse / professional identity construction | *Journal of Information Technology* (Palgrave) | 4 | Same angle, higher bar; needs n=200+ JDs across geographies or a second empirical study |
| Management fashion / institutional theory | *Organization Science* (INFORMS) | 4* | Abrahamson/DiMaggio as primary contribution; dbt report as the empirical case; JD data as validation |
| Labour market / job postings | *ILR Review* (Cornell/Sage) | 3 | JD dataset must be the primary data source; needs n=300+ and structured coding reliability |
| Labour market / job postings | *Journal of Labor Economics* (Chicago) | 4* | n=1,000+ JDs with geographic spread; rigorous econometric specification; not achievable from this dataset alone |

**Recommended path now:** Submit to *Information Systems Journal* (ABS 3) as a critical IS discourse paper, with the JD analysis explicitly positioned as a pilot study. This requires six concrete actions, each written below from the adversarial reviewer's position first.

---

### Failure 1 — No methodology section

**Reviewer rejection argument:** "This manuscript has no methods section. I cannot assess how the primary data were collected, how documents were selected, what analytical procedure was applied to the dbt Labs reports, or how the JD classifications were generated. The analysis appears to proceed directly from data summary to interpretation with no disclosed analytical procedure. I recommend rejection."

**Can this objection be fully answered?** Yes — but only if the methodology section is written honestly about what actually happened.

**What actually happened:** The four dbt Labs reports were read as documents. Thematic notes were taken on narrative framing, vocabulary, and year-on-year shifts. The JD classifications were assigned by hand — one analyst (the author) read each JD in full and assigned values to `velocity_vs_rigour`, `domain_risk`, `collaboration_width`, `data_team_maturity`, and `jd_authorship` by applying a structured rubric (the Layer B framework) through judgement. There was no automated parsing, no NLP pipeline, no second coder, and no kappa calculation. This is single-coder qualitative content analysis.

**What to write in the methods section:** State this plainly. Call it what it is: structured qualitative content analysis, single coder, using the Layer B framework as a coding instrument (see Action 3 for the codebook). Cite Krippendorff, K. (2018), *Content Analysis: An Introduction to Its Methodology* (4th ed., Sage) — the standard reference for this method. Acknowledge that because one person coded all 37 JDs, the classifications are internally consistent but not independently validated. This is a limitation, not a disqualification — single-coder content analysis is published routinely, provided the codebook is fully disclosed and the limitation is named upfront. Cite Fairclough's CDA for the documentary analysis of the dbt reports (different method — interpretive text analysis, not content coding).

**Done when:** A ~400 word methods section exists that names both methods (CDA for the reports, content analysis for the JDs), discloses single-coder assignment explicitly, points to the codebook in Appendix A, and names single-coder reliability as the primary limitation.

---

### Failure 2 — Single-coder classification: an objection that cannot be fully mitigated without more work

**Reviewer rejection argument:** "All JD classifications on the study's primary constructs (`velocity_vs_rigour`, `domain_risk`, etc.) were assigned by a single analyst who also authored the study. There is no inter-rater reliability statistic, no independent validation, and no disclosed decision procedure for ambiguous cases. In content analysis, the standard minimum is two independent coders with reported agreement. Without this, the core empirical contribution of the study — the JD cross-tabulations — is not reproducible and not verifiable. This is a fatal flaw."

**Can this objection be fully answered?** Not without collecting additional data. A reliability study requires a second coder. There is no reframing or prose adjustment that resolves this. It is a real gap.

**Action required — you need a second coder:** Recruit one person (a data professional or a methodologically literate colleague) to independently classify a 20% random sample of the JDs (8 records from 37) using Appendix A as the codebook. Calculate Cohen's kappa for each dimension. A kappa above 0.6 is conventionally acceptable for exploratory research; above 0.8 is good. If kappa is low on a given dimension, either revise the codebook definition or report the dimension as unreliable and exclude it from the analysis. This process takes approximately one day of work and produces the reliability statistic the reviewer requires. Without it, this paper cannot be published in a peer-reviewed journal, and the JD cross-tabulations should not be presented as findings.

**Done when:** A kappa statistic exists for each of the five dimensions, computed from an independent re-coding of an 8-record sample. These statistics are reported in the methods section alongside the codebook reference.

---

### Failure 3 — n=37 is too small for any quantitative claim. Collect more data.

**Reviewer rejection argument:** "The manuscript presents cross-tabulations with cells as small as n=4 and draws directional conclusions from them. At n=37 with no probability sampling, no inferential statistic is defensible and no percentage is meaningful beyond the sample itself. The confidence interval on the headline finding (65% rigour, ±16pp at 95%) spans 49–81% — a range so wide it is consistent with 'roughly half' or 'four-fifths' of the market. This does not tell us anything. Furthermore, the cross-tabs are presented without significance tests. The paper cannot both present quantitative cross-tabulations and decline to test them. I recommend major revision contingent on either (a) substantially expanding the dataset or (b) removing all quantitative analysis and repositioning as a purely interpretive study."

**Can this objection be fully answered without new data?** Only partially. The interpretive repositioning (option b) removes the quantitative analysis entirely — which eliminates the objection but also eliminates the paper's most novel contribution (the JD dataset). Option (a) is the right path.

**How much data you actually need:**

| Claim you want to make | Minimum n | Why |
|------------------------|-----------|-----|
| That rigour dominates (single proportion, 95% CI ±10pp) | ~100 JDs | Wilson interval: n=96 gives ±10pp at p=0.65 |
| That rigour × domain_risk cross-tab is not noise (chi-squared, 3×3 table, p<0.05) | ~150 JDs | Minimum expected cell frequency ≥5 requires n≈150 across 9 cells |
| That the pattern holds across markets (UK vs DACH vs Nordics) | ~300 JDs | ~100 per geography to permit subgroup analysis |
| That the pattern is stable over time (2024 vs 2025 vs 2026 posting dates) | ~300–500 JDs | Need roughly equal n per year within each market |

**The immediate action is:** Stop presenting cross-tabs from n=37 as findings. They are not. The 65% rigour figure, the domain_risk cross-tab, and the collaboration_width analysis should all be relabelled as "directional observations from a pilot dataset" — with an explicit note that no conclusion about the market is warranted. Then collect more JDs. The conference talk's data collection CTA (Section 13, Action 5) is not just a credibility move — it is the actual research design step that would make this paper publishable at the quantitative level.

**Done when:** Either (a) the dataset has ≥150 JDs from ≥2 geographies with a second coder's reliability statistics, at which point the cross-tabulations can be submitted; or (b) all cross-tab percentages are removed from the paper and the JD analysis is framed purely as "these patterns emerged in one analyst's pilot dataset and generated the following hypotheses for future research."

---

### Failure 4 — Primary source is vendor-produced. The paper cannot treat the dbt report findings as facts about the profession.

**Reviewer rejection argument:** "The manuscript repeatedly makes claims of the form 'X% of analytics engineers report Y' where the source is a dbt Labs annual survey distributed through dbt Slack and community events. 76% of 2023 respondents already used dbt — a figure the authors themselves cite. This is not a sample of the analytics engineering profession. It is a sample of the dbt community. Any claim extrapolated beyond that community is not supported by the data. More fundamentally, the reports are produced by an organisation with a direct commercial interest in the findings. The paper critiques this in Section 6, but then continues to use the reports' statistics as if they were neutral. The critique and the analysis are working at cross-purposes."

**Can this objection be fully answered?** Yes — but it requires a complete reframing of what the paper claims to be.

**Action required:** Rewrite every claim that reads "X% of analytics engineers do Y" to read "dbt Labs' survey reports that X% of dbt community respondents say Y." This is not a cosmetic change — it changes the epistemological status of every finding in Sections 2–5. The paper is not a study of analytics engineers. It is a study of a vendor's self-reported community survey, analysed as a discourse document. That is the legitimate contribution: understanding how dbt Labs constructs the narrative of the profession, year by year, and whether that construction has entered employer hiring language. The critique in Section 6 should move to Section 2 (immediately after introducing the reports) and should be the analytical frame for everything that follows, not an afterthought.

**Done when:** The abstract and opening paragraph position the paper as a discourse study of vendor-produced professional narratives. No sentence in Sections 2–5 makes a claim about "analytics engineers" without attributing it to dbt Labs' survey and noting the sampling constraint.

---

### Failure 5 — Six theories cited, none tested

**Reviewer rejection argument:** "The manuscript cites Collingridge, Rogers, DiMaggio & Powell, Abrahamson, Spence, and Weick. Not one of these theories is used to derive a testable prediction. Each theory is introduced, briefly described, and then applied to explain a pattern already observed in the data. This is post-hoc rationalisation, not theoretical contribution. An A+ journal publishes papers that advance theory, test theory, or develop theory. This paper does none of these things — it uses theory as rhetorical decoration. The theories should either be removed entirely or the paper should be redesigned around testing one of them."

**Can this objection be fully answered?** Only if you choose one theory and commit. Trying to defend six simultaneously will produce a reviewer report that correctly identifies this as evasion.

**The recommended commitment:** Abrahamson's management fashion theory is the most tractable given the data. The testable claim is: if dbt Labs is a fashion setter in Abrahamson's sense, then (a) each year's report vocabulary should introduce new terms that did not appear in the prior year, and (b) each year's central concern should align with dbt's product announcements that year. Both of these are verifiable from the reports themselves without a larger dataset. This repositions the paper as an empirical application of management fashion theory to a technology vendor — a publishable contribution because the domain (open-source developer tooling vendors as fashion setters) has not been studied in this literature before.

**Action required:** Pick Abrahamson as the primary theoretical frame. Derive two explicit predictions from the theory before presenting findings. Present the vocabulary shift analysis and the product-narrative alignment (already partly in Section 6) as the evidence for those predictions. The other five theories become secondary sensitising concepts, not co-equal frameworks. Reduce the theoretical frameworks section from six equal treatments to one primary theory plus a brief paragraph noting the supporting conceptual lenses.

**Done when:** The paper opens with two explicit hypotheses derived from Abrahamson's framework, and the findings sections are structured around assessing those hypotheses.

---

### Failure 6 — No literature review

**Reviewer rejection argument:** "There is no literature review. This is a desk rejection criterion at this journal. The manuscript does not cite any prior work on vendor-produced industry reports as research objects, does not engage with critical IS literature on technology discourse, and does not position itself relative to the growing body of work using job postings as labour market data. I cannot assess the paper's contribution because I do not know what it is contributing to. Reject."

**Can this objection be answered?** Yes — this is the most straightforwardly fixable failure.

**Action required:** Write a 300–400 word "Prior work" section covering three streams:

1. *Vendor knowledge production and management fashion:* Cite Abrahamson (1996) on fashion setters. Gartner Hype Cycle research (Fenn & Raskino, 2008, is a practitioner book but widely cited). State the gap: dbt Labs-style community survey reports as fashion artefacts have not been studied academically.

2. *Critical IS and technology discourse:* Cite Orlikowski & Barley (2001), "Technology and Institutions: What Can Research on Information Technology and Research on Organizations Learn from Each Other?" *MIS Quarterly*, 25(2), pp. 145–165. This is the foundational paper on how vendor framings enter organisational practice — directly relevant and peer-reviewed.

3. *Job postings as labour market data:* Cite Deming & Kahn (2018, already in the paper). Add Hershbein & Kahn (2018), "Do Recessions Accelerate Routine-Biased Technological Change?" *American Economic Review*, 108(7), pp. 1737–1772, DOI: 10.1257/aer.20161570 — a verified paper using job posting text to measure skill demand shifts. Position this paper as applying their approach to validate (or refute) an industry survey's claims.

**Done when:** A "Prior work" section of 300–400 words exists, covering all three streams, before the year-by-year analysis begins.

---

## 13. Conference reviewer critique — action plan for talk submission

### The two audiences and their tolerance

**Forward Data Conference** — independent, practitioner-critical. The critique of the dbt report's methodology is a feature, not a risk. Lead with it. The risk is sounding too academic; the mitigation is every theoretical claim earning its place with a concrete practitioner implication.

**dbt Coalesce** — dbt Labs' own event. The methodology critique needs to be reframed as "here's how the research could be extended" rather than "here's why the numbers don't hold up." The governance/trust thesis is a tailwind, not a headwind. Submit the Coalesce version after Forward Data — use audience reaction to sharpen the argument first.

---

### Action 1 — Write the one-liner thesis before anything else

Every other conference action depends on having this. Without it, the CFP abstract has no hook and the talk has no spine.

**Draft three options and pick one:**
- *"The data industry's most-cited annual report surveys 363 self-selected dbt users. Here's what 37 job descriptions tell us it got right — and where it's selling you something."* (Forward Data framing — adversarial)
- *"Four years of dbt's State of Analytics Engineering: each year's central anxiety maps to that year's product launch. Here's how to read it anyway."* (Slightly more generous — works at either venue)
- *"65% of analytics engineering JDs signal rigour. 0% signal pure velocity. The governance panic is already in the labour market — employers just aren't saying it in the ways the 2026 report predicts."* (Data-first framing — strongest for a data conference)

**Done when:** One of these (or a sharper variant) is chosen and written at the top of the CFP abstract draft. Every slide in the deck earns its place by advancing this thesis.

---

### Action 2 — Build three specific slides from existing data

No new data needed. These slides are all computable from what already exists.

**Slide A — "The rigour finding"**
Bar chart: rigour 65% / mixed 30% / velocity 5% across 37 JDs. Headline: "AE employers already want rigour. Velocity is near-absent." Subtext: "This predates the 2026 report's governance panic — or confirms it's already been absorbed." This is the data slide that earns credibility.

**Slide B — "Four years of narrative"**
Timeline with four rows (2023/2024/2025/2026), two columns: "What the report said" / "What dbt launched that year." Show the alignment. Don't editorialize — let the audience reach the product-market fit conclusion themselves. This is the slide that generates the "wait a moment" reaction.

**Slide C — "What the theories predict"**
Six boxes, one per theory, each containing a single sentence: theory name → one observable prediction → whether the JD data supports it. This is the slide that separates the talk from "data person has opinions" to "data person has a framework." Keep each box to 20 words maximum.

**Done when:** All three slides exist as drafts (even in markdown/text form) before the CFP submission deadline.

---

### Action 3 — Prepare the live JD walkthrough

This is the methodology moment that makes the talk credible and reproducible. Pick one JD from the dataset — ideally one where the Layer B analysis found a mismatch between what the employer claims to want (governance framing in the summary) and what the JD body signals (delivery-speed bullets, no testing requirements mentioned).

**The structure of the walkthrough (5 minutes on stage):**
1. Show the JD excerpt — one paragraph from the role description
2. Ask the audience: "Is this employer rigour-oriented or velocity-oriented?"
3. Take a show of hands
4. Apply the Layer B framework live — read out the signals, assign the classification
5. Show where it lands in the dataset cross-tab
6. Ask: "Does this match what the 2026 report says employers care about?"

**Done when:** One JD is selected and annotated with the Layer B signals pre-highlighted. The walkthrough script is written and can be delivered in under 5 minutes.

---

### Action 4 — Write the hiring-manager version of Section 8.7

Section 8.7 (action synthesis) is written entirely from the candidate's perspective. A conference audience includes heads of data and hiring managers who have no use for "how to position your resume." They need the mirror image.

**Write a parallel set of six bullet points, one per theory, framed for the person writing the JD:**

- *Collingridge:* If you haven't added data contract requirements to your JD yet, you're already behind — by the time it's obvious you need them, retrofitting governance into a team that was hired without it is expensive.
- *Rogers:* If your team is early-majority on AI adoption, you're probably in the governance gap right now. Hire explicitly for the discipline you skipped, not the velocity you already have.
- *DiMaggio & Powell:* Your JD looks like everyone else's because you copied a JD that looked like everyone else's. That's mimetic isomorphism. It produces a team that looks like every other team. If you want someone who governs as well as ships, write that down.
- *Abrahamson:* The vocabulary in the 2026 report ("trust gap", "governance as infrastructure") is circulating. Candidates who've read it will scan your JD for these signals. If they're absent, you're signalling you haven't read the report either.
- *Spence:* Governance requirements in a JD are costly signals — they tell a candidate you're serious enough about quality to filter for it. Their absence signals the opposite, regardless of what you say in the interview.
- *Deming & Kahn:* What you write in the JD is your revealed preference. If you write "build pipelines" but mean "build and govern pipelines", you will hire the person who builds and not the person who governs.

**Done when:** These six bullets exist as a slide or handout section titled "If you're the one writing the JD."

---

### Action 5 — Write the community data collection slide

This is the closing call-to-action. It is also the credibility move that pre-empts the "only 37 JDs" objection by converting the limitation into an invitation.

**The slide text (verbatim draft):**

> *This research is a pilot. n=37, one person's job search, Berlin, early 2026.*
>
> *To answer these questions properly I need:*
> - *500+ JDs across markets (US, UK, DACH, Nordics)*
> - *Mix of dbt and non-dbt stack requirements*
> - *Full date range: 2023–2026*
>
> *If you've applied for an AE, DE, or BI role in the last 18 months: send me the JD.*
> *[email / LinkedIn / GitHub link]*
>
> *The dataset will be open. The analysis will be public. Every JD you share makes the next finding more defensible.*

**Done when:** This slide is the second-to-last slide in the deck, before the contact/Q&A slide. The data collection mechanism (a form, an email, a GitHub issue) exists and is live before the talk.

---

### Action 6 — Write the front-loaded credibility statement

This goes on slide 2 — the second thing the audience sees, before any data.

**Draft:**

> *A note on what this is: 37 job descriptions. One person's job search. Berlin, April–June 2026.*
>
> *I'm not going to pretend that's a representative sample. It isn't.*
>
> *What it is: revealed-preference data. Employers wrote these when they had a real hiring cost. That makes them more honest than a survey.*
>
> *I'll tell you what I found. I'll tell you what I can't conclude from it. You decide what's useful.*

**Done when:** This statement is on slide 2, in the speaker's own voice, before any methodology or findings. It stays on screen for the first 60 seconds of the talk.

---

## Sources

- dbt Labs, "2023 State of Analytics Engineering" (survey Oct–Nov 2022, n=567). Raw data: github.com/dbt-labs/analytics-engineering-survey
- dbt Labs, "2024 State of Analytics Engineering" (survey Dec 2023–Mar 2024, n=456)
- dbt Labs, "2025 State of Analytics Engineering" (survey Oct–Dec 2024, n=459). PR: prnewswire.com/news-releases/ai-is-driving-a-surge-in-data-budgets-302429579.html
- dbt Labs, "2026 State of Analytics Engineering" (survey Dec 2025–Feb 2026, n=363). PR: prnewswire.com/news-releases/new-dbt-labs-report-finds-ai-driven-acceleration-is-outpacing-trust-and-governance-302741246.html
- Collingridge, David. *The Social Control of Technology*. Frances Pinter, London, 1980. ISBN: 0903804727.
- DiMaggio, Paul J. and Powell, Walter W. "The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality in Organizational Fields." *American Sociological Review*, Vol. 48 (1983), pp. 147–160. DOI: 10.2307/2095101.
- Abrahamson, Eric. "Management Fashion." *Academy of Management Review*, Vol. 21, No. 1 (January 1996), pp. 254–285. DOI: 10.5465/amr.1996.9602161572.
- Rogers, Everett M. *Diffusion of Innovations*. 1st ed., Free Press of Glencoe, 1962; 5th ed., Free Press, 2003.
- Spence, Michael. "Job Market Signaling." *The Quarterly Journal of Economics*, Vol. 87, Issue 3 (August 1973), pp. 355–374. DOI: 10.2307/1882010.
- Deming, David and Kahn, Lisa B. "Skill Requirements across Firms and Labor Markets: Evidence from Job Postings for Professionals." *Journal of Labor Economics*, Vol. 36, No. S1 (2018), pp. S337–S369. DOI: 10.1086/694106.
- Weick, Karl E. *Sensemaking in Organizations*. Sage Publications, 1995. ISBN: 9780803971776.
- Lavrakas, Paul D. (ed.). *Encyclopedia of Survey Research Methods*. Sage Publications, 2008.
