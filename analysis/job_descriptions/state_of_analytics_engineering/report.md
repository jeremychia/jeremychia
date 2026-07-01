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

## 4.9 Statistical relationships across dimensions

The sections above treat each dimension in isolation. This section runs exhaustive pairwise tests across all categorical and numeric fields to surface relationships that don't emerge from single-dimension inspection.

### Statistical methods

Three tests were used, selected by data type and cell size:

**Chi-squared (χ²):** Applied to all categorical × categorical pairs with expected cell frequencies ≥5. Tests whether the two variables are independent. With n=93, the minimum detectable effect (at α=0.05, 80% power) for a 2×3 table is Cramér's V ≈ 0.30 — so findings below that threshold should be read as directional only.

**Fisher's Exact:** Applied when the table is 2×2 with any expected cell frequency <5, or when any cell has fewer than 5 observations. Computationally exact rather than asymptotic; appropriate for sparse cells.

**Kruskal-Wallis (KW) / Mann-Whitney U (MWU):** Applied to numeric × categorical pairs (`collaboration_width`, `salary_min`, `salary_max`). KW is the non-parametric equivalent of one-way ANOVA (k≥3 groups); MWU is the two-group equivalent. Neither assumes normality. Salary results are treated cautiously given n=21 salary records.

**Cramér's V** is reported alongside all chi-squared tests as a standardised effect size (0 = no association, 1 = perfect association). Conventional thresholds: V≥0.10 small, V≥0.30 medium, V≥0.50 large.

**Multiple comparison note:** Running all pairwise combinations across ~20 dimensions produces many tests. No Bonferroni correction is applied — these are exploratory findings, not confirmatory hypothesis tests. Only results with p<0.05 *and* V≥0.20 (or a clear conceptual interpretation) are reported below. At n=93, p<0.05 alone is not sufficient to treat a finding as robust.

---

### Finding A: Domain risk and stakeholder orientation are structurally linked (χ², p<0.001, V=0.36)

| domain_risk | commercial | finance | internal_data | mixed | product | n |
|-------------|-----------|---------|---------------|-------|---------|---|
| high | 9% | 43% | 39% | 9% | 0% | 23 |
| moderate | 12% | 1% | 65% | 13% | 9% | 68 |

High-risk roles concentrate in finance (43%) and to a lesser extent internal_data (39%). Moderate-risk roles overwhelmingly serve internal_data (65%). Product-facing roles appear only at moderate risk — there are zero high-risk product analytics roles in this dataset.

The finance-concentration in high-risk is expected (fintech, insurance, IFRS/SOX contexts). The absence of product-risk roles is less obvious: experimentation and funnel analytics aren't classified as high-stakes in hiring language even when A/B test errors have revenue consequences. Either employers don't frame product analytics as risky, or the risk is absorbed into "moderate" by the codebook's decision rules.

**Theoretical read — DiMaggio & Powell (1983), normative isomorphism:** Normative isomorphism predicts that professional communities develop shared norms about what constitutes legitimate practice, and hiring language reflects those norms. Finance is a mature professional field with externally imposed risk classifications (regulatory bodies, audit standards, IFRS). The data-risk hierarchy in JD language therefore tracks an externally defined hierarchy, not just employer discretion. Product analytics has no equivalent external regulator defining what a "high-risk" A/B test looks like — so employers default to moderate. This is the theory *supported*: domain-risk employer language is shaped by the regulatory and professional norms of the stakeholder domain, not a free employer judgment about data stakes.

---

### Finding B: High-risk roles are more likely to require greenfield work (χ², p<0.001, V=0.29)

| domain_risk | fix_scale | greenfield | mixed | n |
|-------------|-----------|-----------|-------|---|
| high | 43% | 26% | 30% | 23 |
| moderate | 22% | 3% | 75% | 68 |

Moderate-risk roles are overwhelmingly "mixed" (existing stack, ongoing expansion). High-risk roles split more sharply between fix_scale and greenfield — employers in high-stakes domains are more likely to be either rebuilding something broken or starting from scratch, not incrementally extending. This may reflect the compliance pressure in fintech and finance to replace legacy systems rather than iterate on them.

**Theoretical read — Collingridge (1980), the control dilemma:** Collingridge's dilemma holds that technology is easiest to correct early, before dependencies lock in, and hardest to correct once it is embedded. The high-risk × fix_scale concentration suggests employers in finance and compliance have *already* hit the locked-in phase: the existing stack cannot be iteratively patched because compliance exposure is too high, so they are forced into replacement or greenfield work. Moderate-risk roles — still in the incremental "mixed" phase — haven't yet hit that ceiling. The theory predicts this pattern and the data supports it: high-stakes domains disproportionately face the costly late-stage correction that Collingridge warns about.

---

### Finding C: Early-stage teams post greenfield roles; mature teams don't (χ², p<0.001, V=0.29)

| data_team_maturity | fix_scale | greenfield | mixed | n |
|--------------------|-----------|-----------|-------|---|
| early | 0% | 60% | 40% | 5 |
| mature | 36% | 0% | 64% | 14 |
| mid | 28% | 7% | 65% | 74 |

Greenfield roles are concentrated at early-stage companies (60%) and are absent from mature teams entirely. Mid-stage teams are predominantly "mixed." Mature teams split between fix_scale and mixed — optimising and expanding, not starting fresh.

This is the structural basis for a common career advice claim ("go early-stage if you want greenfield work") — it holds in employer language. The complementary finding is less often stated: mature teams have the highest fix_scale proportion (36%), meaning they're more likely to be posting roles explicitly to address debt or replace underperforming systems.

**Theoretical read — Rogers (2003), diffusion S-curve:** Rogers' diffusion model predicts distinct phases: early adopters build infrastructure from scratch; early majority scale and expand; late majority inherit and optimise what others built. The maturity × greenfield_vs_fix distribution maps onto this almost exactly — greenfield at early, mixed at mid, fix_scale concentrated at mature. What the theory does not predict well is the mature fix_scale finding: Rogers treats late adoption as stabilisation, not remediation. The data suggests a *post-stabilisation regression* — mature teams rebuilding systems that were adequate when adopted but have since accumulated technical or compliance debt. That pattern is closer to Collingridge than Rogers, and suggests the two frameworks need to be read together to cover the full maturity arc.

---

### Finding D: Seniority predicts autonomy, but not linearly (χ², p=0.015, V=0.26)

| autonomy_level | junior | lead | manager | mid | senior | staff | n |
|----------------|--------|------|---------|-----|--------|-------|---|
| execution | 3% | 0% | 0% | 54% | 43% | 0% | 35 |
| mixed | 0% | 11% | 0% | 52% | 37% | 0% | 27 |
| strategic | 0% | 10% | 3% | 19% | 55% | 13% | 31 |

Senior roles span all three autonomy levels — 43% of execution roles are senior, and 55% of strategic roles are senior. "Senior" is not a reliable signal of strategic autonomy. The clearest contrast: mid-level roles cluster in execution (54%) but drop sharply in strategic (19%). Staff roles appear almost exclusively in strategic — a small cell (n=4) but directionally consistent with the expectation that staff engineers set direction.

Lead and manager titles show mixed patterns. Leads appear in strategic and mixed (but not execution); managers are rare in this dataset and appear inconsistently.

**Theoretical read — Spence (1973), signalling; partially contradicted:** Spence's signalling theory predicts that credentials (including job titles) serve as reliable signals of underlying quality, because they are costly to obtain. If seniority titles are good signals, "Senior AE" should reliably predict higher autonomy. The data contradicts this: "Senior" is spread almost uniformly across execution, mixed, and strategic. The signal has degraded — either because the title is cheap to award (low cost = low signal value), or because employers have disaggregated the seniority concept across multiple title ladders without standardising what it means for autonomy. The title has become a *weak* signal at best, a *misleading* one at worst. The staff title, by contrast, appears to retain signal value — its near-exclusive concentration in strategic is consistent with staff titles being genuinely more costly to award and therefore more informative. Spence's framework is supported for staff; it is contradicted for senior.

---

### Finding E: Finance roles are the most execution-oriented (χ², p=0.019, V=0.24)

| stakeholder_orientation | execution | mixed | strategic | n |
|-------------------------|-----------|-------|-----------|---|
| commercial | 20% | 50% | 30% | 10 |
| finance | 82% | 9% | 9% | 11 |
| internal_data | 40% | 29% | 31% | 55 |
| mixed | 9% | 27% | 64% | 11 |
| product | 17% | 33% | 50% | 6 |

82% of finance-facing roles are classified as execution — the highest concentration in the dataset. Finance stakeholders have defined reporting requirements, compliance frameworks, and audit cycles: the AE's job is to deliver correctly against them, not to set the direction. Commercial-facing roles are the most mixed (50%), which makes sense given the volatility of GTM priorities. "Mixed" stakeholder roles are the most strategic (64%) — these are likely platform or lead roles that serve multiple audiences and must set standards across them.

**Theoretical read — DiMaggio & Powell (1983), coercive isomorphism; supported:** Coercive isomorphism describes how external mandate — regulation, audit requirements, legal obligation — constrains organisational behaviour regardless of internal preferences. Finance-facing AE roles are shaped by coercive forces (IFRS, SOX, GDPR, insurance regulation) that define what the output must be before any internal conversation about strategy takes place. The 82% execution concentration is therefore not an employer preference — it is the shape that external coercion imposes. The contrast with commercial roles (20% execution) is precisely the contrast between coercively defined and market-defined work: commercial GTM work has no external regulator setting the deliverable, so autonomy varies with employer context. The theory fits the pattern tightly and offers a prediction: as financial regulation becomes more prescriptive (mandatory audit trails for ML-driven decisions, for instance), finance-facing AE roles should become even more execution-dominated over time.

---

### Finding F: Velocity-oriented roles cluster with streaming infrastructure (χ², p<0.001, V=0.43)

| velocity_vs_rigour | has_kafka: False | has_kafka: True | n |
|--------------------|------------------|-----------------|---|
| mixed | 86% | 14% | 7 |
| rigour | 96% | 4% | 85 |
| velocity | 0% | 100% | 1 |

The single velocity-oriented JD in the dataset requires Kafka. Among mixed-orientation roles, 14% require Kafka vs. 4% for rigour roles. This is consistent with the hypothesis that streaming infrastructure demands a different operational posture — real-time pipelines have less tolerance for the batch-correction patterns that rigour-oriented teams rely on. The cell sizes are too small to treat this as confirmatory, but the direction is clear.

Kafka also co-occurs with greenfield orientation (38% of greenfield roles require Kafka vs. 3% of mixed roles; V=0.42) and with early-stage teams (40% of early-stage vs. 4% of mid-stage; V=0.34). This forms a coherent cluster: early-stage, greenfield, streaming-infrastructure, velocity-oriented roles are the non-modal segment of the market — visible in the data, but structurally distinct from the dominant mid-stage rigour archetype.

**Theoretical read — Rogers (2003), technology clusters; Weick (1995), enacted environment; both supported:** Rogers observes that innovations rarely diffuse in isolation — adopters acquire complementary technologies together because the benefits of one depend on the presence of others. The Kafka cluster (streaming + greenfield + early-stage + velocity) is exactly this: these attributes co-occur not because of independent employer choices but because they are a coherent *technology package* that makes sense as a bundle. Adopting streaming without greenfield context, or velocity orientation without the operational infrastructure to support it, is inconsistent — and the data reflects that employers who write these JDs are selecting the whole package or none of it. Weick adds that organisations do not merely adopt technology — they enact the environment in which that technology makes sense. Velocity-oriented employers are signalling not just a tool preference but a different enacted reality about what data work is for: throughput over correctness, feedback loops over audit trails. The Kafka cluster is therefore both a technology-diffusion cluster (Rogers) and an organisational sensemaking artefact (Weick). The dominant rigour cluster is its mirror: a different enacted reality, adopted by the modal employer.

---

### Finding G: dbt authorship signals who wrote the JD (χ², p=0.012, V=0.27)

| jd_authorship | has_dbt: False | has_dbt: True | n |
|---------------|---------------|---------------|---|
| hiring_manager | 15% | 85% | 39 |
| mixed | 39% | 61% | 41 |
| recruiter | 54% | 46% | 13 |

Hiring managers who write their own JDs are significantly more likely to include dbt as a requirement (85% vs. 46% for recruiter-authored). Recruiter-authored JDs include dbt at roughly coin-flip rates. One interpretation: hiring managers who use dbt daily name it specifically; recruiters pull from generic tool-list templates that may or may not include it.

The practical implication for candidates: dbt absence in a recruiter-authored JD is weaker evidence that the team doesn't use dbt than dbt absence in a hiring-manager-authored JD. The JD authorship dimension serves as a signal-quality adjuster for the tool requirements.

**Theoretical read — Deming & Kahn (2018), revealed preference; signal degradation:** Deming and Kahn establish that JD requirements are revealed preferences — employers write what they value because posting and screening has cost. This finding introduces a second-order complication: the signal quality of a JD requirement depends on *who wrote it*. A hiring-manager-authored dbt requirement is a high-fidelity revealed preference — the manager chose to name dbt because they use it and will screen for it. A recruiter-authored dbt requirement is lower fidelity — it may reflect a template, a prior JD, or a guess about what the role needs. The Deming-Kahn framework is not wrong, but it assumes uniform signal quality across JDs. The authorship finding shows that signal quality is itself variable and measurable. The implication for the dbt prevalence finding (71% of AE JDs mention dbt): this figure is an upper bound — recruiter-authored mentions dilute the true prevalence of teams where dbt is a working daily requirement.

---

### Finding H: Autonomy level predicts salary more reliably than seniority title (KW, p=0.024, n=21)

| autonomy_level | salary_min median | salary_max median | n |
|----------------|-------------------|-------------------|---|
| execution | €48,000 | €57,500 | 7–8 |
| mixed | €65,000 | €90,000 | 5 |
| strategic | €90,000 | €100,000 | 9–10 |

The salary gradient across autonomy levels is sharper than across seniority labels (which show less separation). Strategic roles pay roughly 85% more at the floor than execution roles. This is consistent with Spence's signalling interpretation: strategic autonomy — a costly-to-fake signal — carries a salary premium that generic seniority titles don't capture.

The salary dataset is small (n=21, predominantly European) and the Kruskal-Wallis result sits at p=0.024, barely above the conventional threshold. The direction is clear; the magnitude is uncertain.

**Theoretical read — Spence (1973), signalling; supported and refined:** Spence's model predicts that signals which are costly to fake command market premiums, because they convey information that cannot be cheaply mimicked. This finding tests two competing signals: seniority title (cheap — titles are awarded by employers with minimal standardisation across firms) versus autonomy level (costly — direction-setting responsibility requires demonstrated judgment and typically longer organisational tenure to be granted). If Spence is right, autonomy level should command a larger salary premium than seniority title. The data supports this: autonomy level produces a clean monotonic salary gradient (€48k → €65k → €90k) where seniority labels produce noise. The finding does not contradict Spence so much as it identifies *which* signal has retained informational value and which has been debased. A candidate negotiating salary is better served by establishing the autonomy level of the role explicitly — it is the dimension the market is actually pricing.

---

### Finding I: Mature teams pay more and hire differently (MWU, p=0.033, n=19)

| data_team_maturity | salary_min median | n |
|--------------------|-------------------|---|
| mid | €60,600 | 16 |
| mature | €90,100 | 3 |

Mature teams pay roughly 50% higher floor salaries than mid-stage teams. With only 3 mature-team salary records, this is illustrative rather than evidential — but the direction is consistent with expectation. Mature teams also show the highest collaboration_width (median 3.5 named stakeholder groups vs. 2.0 for mid-stage) and the highest fix_scale proportion (36%). They are paying for experience and scoping the role more broadly.

**Theoretical read — Rogers (2003), late-majority adoption characteristics; partially contradicted:** Rogers predicts that late adopters (mature organisations) are more risk-averse and cost-sensitive than early adopters, and that adoption at this stage is driven by economic necessity rather than innovation appetite. If true, mature teams should pay conservatively — they adopt when they must, not because they prize capability. The salary data contradicts this prediction: mature teams pay the highest floor salaries. A better explanation comes from labour economics rather than diffusion theory: mature data functions have *more* differentiated skill requirements because they have had longer to identify which capabilities generate value. They are paying for precision, not out of innovation drive. The salary premium is better explained by skill specificity (they know exactly what they need and price for it) than by diffusion dynamics.

---

### Finding J: Loss-aversion framing predicts strategic autonomy and broader collaboration (χ², p=0.039, V=0.39)

*Based on 21 records with the new-format fields; treat as directional.*

| loss_aversion_framing | execution | mixed | strategic | n |
|-----------------------|-----------|-------|-----------|---|
| high | 17% | 0% | 83% | 6 |
| moderate | 20% | 30% | 50% | 10 |
| none | 80% | 20% | 0% | 5 |

Roles with high loss-aversion framing (dominated by compliance, regulatory exposure, or trust framing) skew heavily strategic (83%). Roles with no loss-aversion framing are overwhelmingly execution (80%). The hypothesis: when an employer fears data errors reaching decision-makers or regulators, they hire for ownership and judgment, not execution of defined tasks. Risk-consciousness and strategic autonomy are employer co-requisites.

Collaboration width shows the same gradient (KW, p=0.035): high loss-aversion roles have median 3.5 named stakeholder groups vs. 2.0 for moderate and 0 for none. Employers concerned about data risk scope the role broadly — they want the AE talking to more of the organisation, presumably to catch more failure modes before they propagate.

**Theoretical read — Kahneman & Tversky (1979), prospect theory; Weick (1995), sensemaking; both supported, with tension:** Prospect theory establishes that losses loom larger than equivalent gains in human decision-making — organisations will pay more to avoid a certain loss than to achieve an equivalent uncertain gain. If loss-aversion framing in JDs reflects an employer genuinely motivated by downside avoidance, the theory predicts they will invest more heavily in the hire: grant more autonomy (to ensure the person can act without bottlenecks when something goes wrong) and mandate broader stakeholder coverage (to catch failure modes earlier). The data supports this: high loss-aversion roles are 83% strategic and have the widest collaboration scope. However, Weick's sensemaking framework introduces a complicating read: employers with high loss-aversion framing may be *enacting* a risk narrative in their JD without that narrative accurately reflecting organisational reality. The JD is a sensemaking document — it constructs a version of what the role is for. A compliance-heavy JD may be authored by a legal team that has over-specified risk, producing strategic autonomy signals that are performative rather than operational. Distinguishing enacted risk from actual risk requires interview-stage data that JDs cannot supply. The finding is best read as: *high loss-aversion framing is a reliable signal that the employer has institutionalised their risk concern into hiring criteria* — whether that concern is proportionate to actual stakes is a separate question.

---

### Summary of significant relationships

| Relationship | Test | p | V / stat | Interpretation |
|---|---|---|---|---|
| domain_risk × stakeholder_orientation | χ² | <0.001 | 0.36 | Finance roles cluster in high-risk; product roles only at moderate |
| velocity_vs_rigour × has_kafka | χ² | <0.001 | 0.43 | Velocity/mixed orientation tracks with streaming infra |
| domain_risk × greenfield_vs_fix | χ² | <0.001 | 0.29 | High-risk domains more likely greenfield or fix_scale |
| data_team_maturity × greenfield_vs_fix | χ² | <0.001 | 0.29 | Early = greenfield; mature = fix_scale; mid = mixed |
| jd_authorship × has_dbt | χ² | 0.012 | 0.27 | Hiring managers name dbt more reliably than recruiters |
| autonomy_level × seniority | χ² | 0.015 | 0.26 | Senior ≠ strategic; execution roles are 43% senior-titled |
| stakeholder_orientation × autonomy_level | χ² | 0.019 | 0.24 | Finance = execution; mixed stakeholder = strategic |
| salary_min × autonomy_level | KW | 0.024 | — | Strategic roles pay ~85% more floor salary than execution |
| loss_aversion_framing × autonomy_level | χ² | 0.039 | 0.39 | High loss-aversion → strategic autonomy (n=21) |
| collaboration_width × stakeholder_orientation | KW | 0.015 | — | Commercial/finance roles name more stakeholder groups |

---

### 4.10 AI role: the gap between AI adoption discourse and hiring language

`ai_role` classifies whether the JD expects the candidate to *use* AI tools in their own workflow, *build* infrastructure AI systems consume, or neither.

| ai_role | n | % |
|---------|---|---|
| none | 78 | 84% |
| ai_enabler | 14 | 15% |
| ai_user | 1 | 1% |

**84% of JDs expect no AI skill from the candidate.** The dbt 2026 report claims 72% of teams use AI in coding workflows daily. If that adoption had become normative — a professional standard, not just a team behaviour — it would appear in hiring language. It does not. Almost no employers (1 of 93) name AI coding tools as a hiring criterion. The `ai_enabler` cluster (15%) is real but concentrated in roles with an explicit GenAI product context: these employers are building AI products and need AEs to supply training data, semantic models, or text-to-SQL infrastructure. That is a product-context signal, not a general market shift.

The implication for Deming & Kahn's revealed-preference framework: employers have not yet paid the hiring cost of requiring AI skills. Survey self-reports of daily AI use and revealed hiring preferences are diverging, which is consistent with DiMaggio & Powell's mimetic adoption — teams copy peers' AI tool use without it becoming a professional norm. A candidate who treats AI proficiency as a differentiator for general AE roles is pitching into a gap the employer has not opened.

**Actionable read:** `ai_enabler` roles → demonstrate data products built for AI consumption specifically. `none` → AI tool fluency is not a differentiator; don't lead with it.

---

### 4.11 Testing framing: governance accountability is now a majority hiring criterion

`testing_framing` distinguishes whether testing and data quality appear as something the candidate *owns*, as a tool listed without ownership language, or not at all.

| testing_framing | n | % |
|-----------------|---|---|
| responsibility | 53 | 57% |
| absent | 36 | 39% |
| tool_listed | 4 | 4% |

**57% of JDs frame testing as something the candidate owns** — using action verbs like own, ensure, define, implement, establish alongside quality, data contracts, or observability. This is the revealed-preference confirmation of dbt 2026's "trust gap" claim: governance accountability has entered hiring criteria in the majority of roles. It is no longer a nice-to-have or a team value — it is a stated hiring expectation.

The distinction from `velocity_vs_rigour` matters. Two JDs can both be coded `rigour`: one because the team values engineering craft, another because the AE will be personally accountable for data trust. `testing_framing = responsibility` identifies the second kind — roles where governance has been institutionalised as a personal responsibility of the hire, not delegated to team culture.

The 39% `absent` cluster is also significant. These employers have not operationalised their quality concern into hiring language, even when the role is otherwise rigour-oriented. Either the testing expectation is assumed and not stated, or it genuinely isn't a priority. Interview questions are required to distinguish the two.

**Actionable read:** `responsibility` → lead with governance outcomes and ownership language; quantify. `absent` → pitch to delivery; governance is not the differentiator here.

---

### 4.12 Loss-aversion framing: the market fears operational failure, not AI hallucinations

`loss_aversion_framing` classifies what the JD is afraid of: nothing (delivery framing only), operational failure (pipeline outages, SLOs, data freshness), or compliance and stakeholder trust failure.

| loss_aversion_framing | n | % |
|-----------------------|---|---|
| moderate | 56 | 60% |
| none | 23 | 25% |
| high | 14 | 15% |

**Three in four roles carry some fear signal, but the fear is operational, not compliance-driven.** The dbt 2026 report leads with a specific fear narrative: 71% of teams cite fear of hallucinated AI outputs reaching stakeholders. If that fear had entered employer hiring consciousness, it would appear as `high` loss-aversion in JD language. `high` is a minority at 15%. The dominant fear (60%) is `moderate` — pipeline reliability, SLO adherence, data freshness — concerns that long predate the AI discourse.

This is a meaningful divergence from the dbt framing. The market is not predominantly afraid of AI governance failures; it is afraid of the same operational failures it has always been afraid of. The survey's emphasis on AI-specific fear may reflect the concerns of dbt's community sample (more sophisticated teams with active AI deployment) rather than the broader employer market.

Finding J (section 4.9) showed that `high` loss-aversion predicts strategic autonomy (83% of high-framing roles are strategic) and wider collaboration scope — employers who fear compliance failure hire differently. The 15% `high` cluster is real and distinct, but it should not be treated as representative of the market.

**Actionable read:** `high` → frame every resume bullet as risk reduced, trust established, misstatement prevented. `moderate` → lead with reliability outcomes: uptime, incident response, SLO adherence. `none` → capability and delivery framing; fear-based pitches will read as mismatched.

---

## 5. What the survey claims vs. what JDs show

| dbt 2026 claim | JD evidence | Assessment |
|----------------|-------------|------------|
| 83% prioritise data trust | 84% rigour-oriented JDs; 57% frame testing as owned responsibility | Confirmed at the orientation level; confirmed at the accountability level |
| 72% use AI in coding workflows daily | 84% of JDs expect no AI skill; 1% name AI coding tools | Not reflected in hiring language — adoption is mimetic, not normative |
| AI adoption outpacing governance (72% vs 24%) | `ai_role` + `testing_framing` now classified across n=93 | Partially contradicted: governance accountability (57%) is *ahead* of AI hiring signal (16%) |
| Fear of hallucinated outputs (71%) | `loss_aversion_framing = high` is 15% of JDs | Not confirmed — dominant fear is operational failure, not AI trust breakdown |
| Ambiguous data ownership persists (41%) | Collaboration width does not confirm this | Ownership confusion is not detectable from JD language alone |
| dbt is the field standard | 68% of AE JDs mention dbt | Real but not universal — ~30% of AE roles run on stacks without it |

**The governance-vs-AI gap inverts the dbt narrative.** dbt 2026 frames the problem as AI adoption outrunning governance readiness. The JD data suggests the opposite pressure: governance accountability has become a majority hiring criterion (57% `testing_framing = responsibility`), while AI adoption has not entered hiring language at all (84% `ai_role = none`). Employers are hiring for governance faster than they are hiring for AI. Whether that reflects genuine institutional maturity or a lagging signal remains open — but the dbt framing of governance as the *deficit* is not what employer revealed preferences show.

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

## 8. Schema gaps — questions this dataset cannot yet answer

The current schema answers orientation questions well. It cannot answer process, trajectory, or outcome questions. Three gaps are worth naming specifically because they would change the interpretation of existing findings if filled.

### What the interview process signals about team reality

The schema captures `interview_stages` (count) but not interview *content*. A four-stage process with a case study and a technical deep-dive signals something meaningfully different from a four-stage process that is three recruiter screens and an HR check. The count is a weak proxy for selection rigour. What would be more useful: whether a technical assessment was present, whether the hiring manager conducted at least one stage, and whether a work sample was required. These would let you test whether `jd_authorship = hiring_manager` actually predicts a more evaluative process — currently assumed but not verified.

This gap matters most for the section 7 claim that a disorganised interview process mirrors disorganised management. That claim is plausible but anecdotal — the schema has no field to test it.

### Compensation coverage is too thin for salary analysis to be reliable

21 of 93 records have salary data. The 4.7 salary analysis (strategic roles pay ~85% more floor salary than execution roles) is directionally credible but statistically fragile at n=21, especially given that salary disclosure varies by country — German and Swedish employers are more likely to disclose than UK or pan-European roles. This is a structured bias: the records with salary data are not a random sample of the corpus. Any salary finding should be treated as a German-market signal with uncertain generalisability.

To make salary analysis robust: require salary extraction for all future records, and flag `salary_disclosed = false` explicitly so the absence is distinguishable from a missed extraction. Currently the field is simply null for both cases.

### Longitudinal signal is absent

Every JD in this corpus was collected between April and June 2026. The dataset is a cross-section, not a time series. Several findings would be meaningfully different if they could be tracked over time: Is `ai_role = ai_enabler` growing? Is `testing_framing = responsibility` a recent shift or a stable norm? Is `loss_aversion_framing = high` rising as AI deployment grows?

The corpus structure supports longitudinal extension — each record has a dated ID and an archived JD — but the analysis doesn't yet track change. A quarterly re-run classifying new JDs against the same codebook would allow trend detection. Without it, the 84% `none` for `ai_role` is a snapshot, not a trajectory, and the "AI adoption has not entered hiring language" finding could be either a stable state or a leading edge of change that isn't visible yet in a 3-month window.

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
- Kahneman, D. and Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263–291. DOI: 10.2307/1914185.
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). Sage.
- Orlikowski, W.J. and Barley, S.R. (2001). "Technology and Institutions." *MIS Quarterly*, 25(2), 145–165.
- Hershbein, B. and Kahn, L.B. (2018). "Do Recessions Accelerate Routine-Biased Technological Change?" *American Economic Review*, 108(7), 1737–1772.
