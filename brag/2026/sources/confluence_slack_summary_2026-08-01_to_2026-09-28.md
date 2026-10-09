# Jeremy Chia — Confluence and Slack contributions, 2026-08-01 to 2026-09-28

Jeremy rejoined Vinted as an analytics engineer in Finance DSA on 3 Aug 2026. In eight weeks he wrote four RFCs and a live case log that the triage bot reads every morning. He co-ran his first month-end close and hosted the Berlin dbt meet-up (~60 guests). He also reviewed RFCs across Finance DSA and Dataverse.

## Confluence — pages he wrote

| Page | Created | Who it is for | What it is, and what it created |
| --- | --- | --- | --- |
| [2026-08-18 — Governed mart for shipping discount campaigns](https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762/2026-08-18+-+Governed+mart+for+shipping+discount+campaigns) (RFC, FDSA-3090) | 18 Aug, updated to 25 Sep | Finance DSA (António), Finance Control requester (Ieva), the person running the manual process (Samanta) | Replaces a monthly hand-edited SQL query and Google Sheet with two reviewed seeds (campaign rules and windows). These feed `dim_shipping_campaign_definitions` and `prep_shipping_campaign_application`. It covers flat, cap, percentage, floor, ceiling and gated campaigns. It was the third ticket asking for this. It found the likely cause of a campaign giving two answers a month apart: two runs pinned different snapshots. Seeds merged (#2158, #2171) and both models built in #2381: 87 windows resolve to 224 rows against prod. It sizes the change at cutover (+€17.9k InPost ES, −€8.8k SPS SK stacking) and names two decisions for Finance Control. It also covers the first price-cap campaign (InPost ES/PT, Sep 2026, FDSA-3410). |
| [2026-08-20 — Split mrt_shipping_results into components](https://vinted.atlassian.net/wiki/spaces/DF/pages/32099795441/2026-08-20+-+Split+mrt_shipping_results+into+components) (RFC, FDSA-3285) | 20 Aug, updated to 14 Sep | Finance DSA engineers, Finance Control FYI | Splits the 1,157-line shipping P&L model into 2 dims, 5 preps and 2 shared macros. The mart went from 1,206 lines to 117. It shipped in one PR, #2222. A full-row hash diff over 4,003,490,208 rows found zero differences. The page records what shipped against what was proposed, and why (views not tables on a 2.3 TB mart, to avoid doubling storage). It adds tests that enforce the grain assumptions, and flags an open VAT-branch question rather than changing logic silently. |
| [2026-08-24 — Continuity for alert triage](https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441/2026-08-24+-+Continuity+for+alert+triage) (RFC) | 24 Aug | Finance DSA on-support rotation | Improves the v-assist triage bot that answers `#dataverse_finance_monitoring` alerts. Phases 1 and 2 are merged (v-assist-registry #846, #851). The SLO report got its own agent, which fixed a gate that let the report suppress itself. Replies now name the failing value rather than a count, and say whether the data or the test is at fault. Phase 3 is the Alert Case Log below. Along the way it fixed two bugs in the stored-failures lookup, cut always-loaded prompt context by 20%, and found that v-assist write access to dataverse-finance was never checked. He ran the team review session and logged the feedback as page comments. |
| [Finance DSA — Alert Case Log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32104972550/Finance+DSA+Alert+Case+Log) | Aug, curated to 23 Sep | Whoever is on support; read by the triage bot before every reply | One row per recurring warning, sorted into four groups: needs attention, known and lived with, nobody looking, sorted out. For each it gives what is normal, where it is being chased, and when it should stop. People fill in two cells per new case, and the bot works out the rest. It has already paid off. `ITX-NULL-QUOTE-ID` read as abnormal only because the normal count was written down, which got it escalated to backend on 24 Aug. It also surfaces risks before month-end: an untracked shipping-result boundary issue, a US tax load that needed 7 attempts, and a case that returned. |
| [2026-09-07 — Self-service data refresh for Finance](https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071/2026-09-07+-+Self-service+data+refresh+for+Finance) (RFC) | 7 Sep | Finance DSA lead, DPX (Airflow access, Slack app), finance stakeholders | Proposes a `/trigger` Slack command. Finance picks a named business process from a dropdown, and a bot runs it and marks the thread done. It is based on analysis of all 1,255 FDSA tickets. 78 were ad-hoc refresh requests plus 103 checklist items, with a 4.6 h median wait and a ~4-day p90. Three people and three pipelines make up 71% of requests. It estimates ~500 h a year of finance time unblocked and 9–11 engineer-days saved. Safety is designed around the 2 Sep duplicate snapshot: jobs are marked unsafe to re-run, a pre-flight snapshot count runs first, and a failed run tells people not to retry. |
| [2026-08: MEC Issue & Request Log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32142295207/2026-08+MEC+Issue+Request+Log) (co-author with Emily Broderick) | 1 Sep | Finance Control and Finance DSA — the MEC retrospective | His first month-end close. He wrote up the shipping result discount allocation (€27.72 from late return-label orders), the VGo Pro wallet reconciliation, and the negative credit amounts in payment processing fees. For the last, he fixed the model (#2194) and proactively fixed two more at the same risk (#2197, #2198). António's retro post credited Jeremy (first MEC) and Emily, with 94.1% of expected models delivered on time. |

## Confluence — pages he edited

- **[MEC Tasks](https://vinted.atlassian.net/wiki/spaces/DF/pages/29110141095/MEC+Tasks)** — the runbook. He asked clarifying questions (10 Aug) and updated it after merges (7 Sep).
- **[On Support](https://vinted.atlassian.net/wiki/spaces/DF/pages/30046224455/On+Support)** — the support rotation page. He edited it, and linked it from the case log and triage RFC.
- **[2026-04-23 — Model Schedule Alignment](https://vinted.atlassian.net/wiki/spaces/DF/pages/31621906495/2026-04-23+-+Model+Schedule+Alignment)** — his progress report on the accounting-export rows assigned to him. `mrt_vouchers_accounting_accrual` moved to daily in PR #2302. He also posted a self-correction about `mrt_payment_processing_fees` being declared static (9 Sep).
- Also contributed to: Double Entry, 2026-08-26 Tier 0 P&L scope RFC, Outside-dbt Integrations, the 2026-07 MEC log, and his own onboarding page. He also flagged outdated GitHub setup pages in the DSA space.

## Confluence — review comments on others' RFCs (45 comments)

- **[2026 Q3 — Tier 1 Reliability Review](https://vinted.atlassian.net/wiki/spaces/DF/pages/32046055735/2026+Q3+-+Tier+1+Reliability+Review)** (10 Aug). He argued for "shift left" testing. He proposed that only primary-key tests stay as errors. He said finance data should be less tolerant of soft dependencies than product data, and challenged how a "last refreshed" signal would be read.
- **[2026-08-24 — Suspicious User Impact & Unified Looker Table](https://vinted.atlassian.net/wiki/spaces/DF/pages/32110877019/2026-08-24-+Suspicious+User+Impact+Unified+Looker+Table)** (24 Aug). He asked which suspicious-user flag and window is used, and suggested linking the definition and putting the 21-day rule up front.
- **[2026-08-26 — Increasing Tier 0 Scope to P&L Financial Metrics](https://vinted.atlassian.net/wiki/spaces/DF/pages/32120244315/2026-08-26+Increasing+Tier+0+Scope+to+P+L+Financial+Metrics)** (26 Aug). He tested whether financial and non-financial metrics need separate models, and asked whether the P&L list is complete. He asked whether auditors really see all Tier 0 metrics, and suggested cutting the motivation to "minimise metric drift".
- **[2026 Q3 — Tier 0 Data Assets — what it means for your team](https://vinted.atlassian.net/wiki/spaces/DF/pages/32202654020/2026+Q3+-+Tier+0+Data+Assets+-+what+it+means+for+your+team)** (22 Sep). He proposed adding a policy gate (P002) for Tier 0 changes as an analytics-engineering roadmap item.
- **[2026-09-22 — Recovering consecutive failed DAG runs](https://vinted.atlassian.net/wiki/spaces/DPV2/pages/32026985454/2026-09-22+Recovering+consecutive+failed+DAG+runs)** (Dataverse/DPX, 22 Sep). He asked for a minimum lookback rather than a default, and pointed out a 2-vs-3-day inconsistency. He asked who "on-call" refers to, and proposed a required "Recovery" keyword in model descriptions.
- **Self-service refresh RFC and triage RFC** — he captured reviewer feedback from the team sessions as comments on his own RFCs.

## Slack — highlights (public and private channels only)

**Coverage note:** the full week-by-week walk of his messages was delegated in four date slices, but those results had not come back when this file was written. The items below come from the recognition searches and a direct walk of 5–7, 13–14 and 20–21 Aug. The rest of the window is not covered here.

### Proposals and ideas
- **v-assist agent and skill roadmap** (7 Aug, #finance-dsa). He built on Júlia's first bot and surveyed what other domains run. He proposed new agents and skills in README.md and RESEARCH.md (v-assist-registry #677), and cross-posted to #analytics-engineering for opinions. [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1786112051113869)
- **BUGBOT review instructions** (6–7 Aug). He wrote review rules for the finance repo (#1817, then #1834) and compared notes with the marketplace team. He shared what the bot does well in #analytics-engineering, and later co-started a BUGBOT feedback study with Julien in #dsa-ae-bugbot-review ("awesome initiative" — David Lopez Mejia, 3 Sep). [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1786029423431619)
- **Two shipping RFCs posted for comment** (20 Aug, #finance-dsa): the campaigns mart and the `mrt_shipping_result` split. [link](https://vinted.slack.com/archives/C076F6CME10/p1787240435286499)
- **First-responder timing and scope fix** for the SLO report (v-assist-registry #675, 7 Aug). [link](https://vinted.slack.com/archives/C076F6CME10/p1786088722381089)

### Platform and code-health work announced for review
- dbt 1.10–1.11 deprecation fixes (#1830) and linter M017/M014 fixes (#1826), 6 Aug. [link](https://vinted.slack.com/archives/C076F6CME10/p1786022959183149)
- Lint drive: he reported the Looker lint-violation trend improving and asked for reviews on the M008/M014/M017 PRs (21 Aug). [link](https://vinted.slack.com/archives/C076F6CME10/p1787302209748429)
- Mangopay S3 pipeline: a pagination fix (#2064) and a `_SUCCESS` completeness marker (#2065), 14 Aug. He also slimmed the pipeline READMEs (#2062). [link](https://vinted.slack.com/archives/C076F6CME10/p1786720717469669)
- **Continuous data deployment (CDD) switched on** for finance (PR #2154, ~10 Sep). He worked with DPX to fix the three blockers first. Júlia: "thanks for enabling it!! game changer". [link](https://vinted.slack.com/archives/C076F6CME10/p1789465411298849)
- Central record of where each export gets its data, kept in the dbt project (#2235), 8 Sep. António had asked for this, and Jeremy already had the PR. [link](https://vinted.slack.com/archives/C076F6CME10/p1788868318312719)

### Help to finance stakeholders and other teams
- AU VAT scheme fix for Evita (#2063). He checked the 10 August and 27 May cases and asked whether past records needed correcting (14 Aug). [link](https://vinted.slack.com/archives/C076F6CME10/p1786698203412179)
- Bucket migration with Egidijus (21 Aug, #finance-dsa-public). He agreed to prepare now and merge after month-end, to protect the close. [link](https://vinted.slack.com/archives/C076P6P3L5U/p1787301812631449)
- Payments data migration: Skirmantė approved his change to the payment-attempts schema (24 Aug). [link](https://vinted.slack.com/archives/C077HPXKTSN/p1787574590641709)
- Group applied data and Dataverse reviews. He explained PR approval rights through the terraform-github config (7 Aug), and reviewed PRs for Janou van Well, Berend Greijn (twice) and Anna Pöhlmann. [link](https://vinted.slack.com/archives/C08DVFF5ZGB/p1786086748831719)
- VGo: he asked for the agenda of the revenue/cost reporting ownership meeting so Finance DSA could follow the decision (2 Sep). [link](https://vinted.slack.com/archives/C077RK49JP2/p1788357320741439)
- Detailed PR reviews for teammates. Samanta: "huge huge thanks… real-mvp" on the suspicious-users P&L PR (24 Sep). Júlia thanked him for reviews of #2376 and the vunit linter change (dataverse-cli #689). [link](https://vinted.slack.com/archives/C076F6CME10/p1790258273667139)

### Incidents and month-end close
- **First MEC, co-run with Emily.** He resolved the shipping result allocation failure on WD1 and the payment processing fee sign issue. Retro: 94.1% of models on time. He recovered the double-entry build on 4 Sep, 33 seconds past the 09:00 deadline. António: "33 seconds is peanuts, thanks for the fast response!" [retro](https://vinted.slack.com/archives/G01A7KGHY74/p1788944254889679) · [4 Sep](https://vinted.slack.com/archives/C0706RCL6CF/p1788506906115249)
- Daily triage in #dataverse_finance_monitoring. For example, on 21 Aug he steered the bot with Emily's context across seven checks. [link](https://vinted.slack.com/archives/C0706RCL6CF/p1787290078172049)

### Hiring, community and onboarding
- **AE hiring panel.** He was onboarded to the new technical interview and gave feedback on the material, which Stuti took on. He described the monthly calibration loop to António (3 Sep). [link](https://vinted.slack.com/archives/C076F6CME10/p1788425500516319)
- **Berlin dbt meet-up host** (10 Sep, ~60 guests). Talks came from dbt Labs and Blacklane, and he moderated a career panel. He used the event to promote open AE roles, coordinated with Georgi. António: "hosted a really interesting round table… very well conducted". [recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289) · [António](https://vinted.slack.com/archives/C076F6CME10/p1789111312538369) · [roles](https://vinted.slack.com/archives/C04L74YS12R/p1788768881613059)
- He restarted the Berlin AE lunches ("Jeremy is back, AE lunches are back"). He also stepped in for an AE hiring panel slot on 31 Aug.

### Recognition received
- Welcome back to Vinted from António in #dsa, 3 Aug. [link](https://vinted.slack.com/archives/C02K4DJRZH8/p1785738336232599)
- MEC retro shout-out: "1st MEC!!!!… great job and prompt resolutions" — António, 9 Sep.
- "game changer" for CDD — Júlia, 15 Sep.
- "real-mvp" for his review — Samanta, 24 Sep.
- "thanks for the suggestions" from Berend on the centralised v-assist agent (v-assist-registry #1249), 22 Sep. [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1790084257398219)
- Samanta liked the incident timeline he wrote on 23 Sep. [link](https://vinted.slack.com/archives/C076F6CME10/p1790144676513819)
- A colleague mentioned him being cheered at the dbt Summit community keynote as meetup and community organiser of the year (15 Sep). This is not verified. [link](https://vinted.slack.com/archives/C05L8F2HVGF/p1789472017254199)

## Slack — full walk, 12–28 Sep (added after the first hand-back)

Almost all messages in this slice fall on 22–25 Sep. There were only 3 between 12 and 21 Sep, which suggests he was away that week.

### Incidents and heads-ups
- **PSP cost accrual misstatement, €1.29m** (23 Sep, #finance-dsa). He wrote a post-mortem timeline (FDSA-3370) and a fix (PR #2361). It adds a test that alerts if the refund rate on cancelled transactions drops below 90%. Samanta praised the timeline. [link](https://vinted.slack.com/archives/C076F6CME10/p1790141400999119)
- **Heads-up to Payments** on the upstream status-logic change behind that misstatement (22 Sep). He asked them to announce future changes like it in #finance-dsa-public. [link](https://vinted.slack.com/archives/C077HPXKTSN/p1790104347593269) · [cross-post](https://vinted.slack.com/archives/C04QY983L5C/p1790104380975359)
- **GB vs UK VAT country bug** (24–25 Sep). About 44k invoice lines a month skip the iSAF zero-rate checks. He diagnosed it and opened a fix in core (#137604, from a fork), then gave Evita an impact analysis. [#checkout-public](https://vinted.slack.com/archives/CQTQUNDU0/p1790260587175519) · [impact](https://vinted.slack.com/archives/G01A7KGHY74/p1790328825861349)
- **Payments' planned dim_payins change** (22 Sep). He checked the grain with Ansel before the change landed. [link](https://vinted.slack.com/archives/C076P6P3L5U/p1790070740956749)

### Proposals
- **Three-tier PR review model** (24 Sep, #finance-dsa). Tier 3 auto-merges, tier 2 gets a standard review, and tier 1 needs a short RFC. It answers PR fatigue from 370+ lint PRs and is set for discussion at the offsite. [link](https://vinted.slack.com/archives/C076F6CME10/p1790255685823279)
- **Tag tests by accounting assertion** (ISA 315) so audit walkthroughs are traceable. António linked it to the future controls inventory. [link](https://vinted.slack.com/archives/C076F6CME10/p1790264617378129)
- **Life after Looker** (23 Sep, #analytics-engineering, 26 replies). He argued that the yml definitions make a move easier. Inga suggested discovery in Q2–Q3 2027, and he volunteered to join. [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1790155483401789)
- **Shared AI skills in two tiers** (22 Sep): generic rules shared, domain rules kept local. He also proposed one standard AI disclaimer. [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1790077325066109)
- **Hourly source-completeness test.** He assessed it and found daily checks are enough for finance's change-data sources (PR #2382). [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1790348624431869)

### Process and tooling
- He unblocked dataverse-dbt-shared merges by removing a stale required check (terraform-github #8831). DPX then opened a ticket to centralise its CI. [link](https://vinted.slack.com/archives/C059T9KAF8X/p1790244865378719)
- **Shared MEC and actuals dates for group finance and VGo** (dbt-shared #432). He applied them in #2369 (shipping results) and #2379 (VGo invoice breakdown). [link](https://vinted.slack.com/archives/C077RK49JP2/p1790229604185959)
- He replaced a personal reminder with a team Workflow Builder "Pre-MEC Reminder". [link](https://vinted.slack.com/archives/G01A7KGHY74/p1790252429468759)
- **Other PRs:**
  - #2300: escrow revenue controls, part 1. [link](https://vinted.slack.com/archives/C076F6CME10/p1790263091639779)
  - #2360: fix for missing prior-month values in the Adyen invoice reconciliation.
  - #2359: "vintage" replaced with "snapshot" across the repo.

### Help, hiring and recognition
- **Mangopay reconciliation** (25 Sep). He found the missing client ID and the extra VintedPay pay-ins. [link](https://vinted.slack.com/archives/C076P6P3L5U/p1790345596101039)
- **Requests from finance:**
  - Carrier base-rate snapshot query. [link](https://vinted.slack.com/archives/G01A7KGHY74/p1790335041395829)
  - "Invoice Total Including Taxes" field for Gabija. [link](https://vinted.slack.com/archives/G01A7KGHY74/p1790094292274729)
- **Teammate PRs:** reviews, a merge-conflict fix, and an offer to carry Samanta's PR to merge while she is on holiday. [link](https://vinted.slack.com/archives/C076F6CME10/p1790154288457109)
- **AE hiring panel:** offered to lead interviews and suggested wording for the interview instructions. [link](https://vinted.slack.com/archives/C0BPJ3MQV71/p1790268505951699)
- **Recognition:** Živilė suggested showcasing his scheduled full refresh at the AE meeting. He deferred to Justina's demo. [link](https://vinted.slack.com/archives/C077RK49JP2/p1790243669319419)
- **Not verified:** whether #2300, #2360, #2369, #2379 and #2382 have merged, and whether Checkout has replied on core #137604.

## Slack — full walk, 1–14 Aug (added after the first hand-back)

### Proposals
- **M008 lint rule: warning first** (12 Aug, #analytics-engineering). Mats proposed making it an error straight away. Jeremy argued for a one-month grace period, and the rule becomes an error on 1 Oct. [link](https://vinted.slack.com/archives/C03JBPN0Q1W/p1786526393519909?thread_ts=1786526348.115389&cid=C03JBPN0Q1W)
- **Source-file completeness test** (PR #2058, 13 Aug). A proof of concept on Mangopay, agreed with António. [link](https://vinted.slack.com/archives/C076F6CME10/p1786604884692809)
- **A skill for documenting pipelines**, with the Mangopay README (#2051), 11 Aug. [link](https://vinted.slack.com/archives/C076F6CME10/p1786428661678739?thread_ts=1786428658.944239&cid=C076F6CME10)

### Process and tooling
- **Code review bot:** enabled Cursor bugbot on the team repos (terraform-github #8079, 5 Aug). [link](https://vinted.slack.com/archives/C076F6CME10/p1785917101209399)
- **Jira:** added two FDSA automations that move tickets when a PR opens and when it merges (10 Aug). [link](https://vinted.slack.com/archives/C076F6CME10/p1786353495412019)
- **Monitoring:** set up alerts from Python Docker jobs to the monitoring channel (terraform-dataverse #3695, 12 Aug). [link](https://vinted.slack.com/archives/C04KMGDQ11D/p1786530822301549)
- **Deprecation clean-up:** after António asked for smaller PRs, he split it into one PR per model (#1836–#2049). He shared a review rota across António, Emily and Samanta: 40 reviewed, ~174 to go. [link](https://vinted.slack.com/archives/C076F6CME10/p1786438104562599?thread_ts=1786022959.183149&cid=C076F6CME10)
- **LookML generator:** fixed it for the new dbt 1.10 `config.meta` layout (dataverse-lookml-generator #160). Other teams depend on it. [link](https://vinted.slack.com/archives/C04KMGDQ11D/p1786435219952209)
- **Other PRs:**
  - #1818: PR template and PR-description skill.
  - #1822: `data_tests` rename.
  - #1810: upstream-model docs.

### Help given
- **Adyen chargeback fees** for Radvilė and Gabija (11–12 Aug). He queried the raw Adyen data and found only USD carries second-chargeback markups. [link](https://vinted.slack.com/archives/C076P6P3L5U/p1786462379421769?thread_ts=1786461807.281829&cid=C076P6P3L5U)
- **AU VAT fix** for Evita. He limited it to invoices from 1 Aug, because earlier ones were already uploaded to iSAF.
- **Access advice** for Kristupas on which groups to request. [link](https://vinted.slack.com/archives/G01A7KGHY74/p1786529310433019?thread_ts=1786529121.767869&cid=G01A7KGHY74)

### Hiring and community
- **AE hiring panel:** volunteered on 13 Aug. [link](https://vinted.slack.com/archives/C0BPJ3MQV71/p1786620864844169?thread_ts=1786620655.134169&cid=C0BPJ3MQV71)
- **Berlin dbt meet-up:** started organising it and asked for presenters on 3 Aug. [link](https://vinted.slack.com/archives/C05L8F2HVGF/p1785741071289669)
