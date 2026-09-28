# Performance & career self-assessment

**Review period:** 1 Aug – 28 Sep 2026

**Name:** Jeremy Chia, Analytics Engineer, Finance DSA

**Primary artifact:** [brag-list.md](https://github.com/jeremychia/jeremychia/blob/main/brag/2026-08-01_to_2026-09-28/brag-list.md)

---

## Part 1: Impact summary

### Highlights

- **Financial integrity:** kept **~€2.7m** of cost out of the wrong accounting period: **€1.29m** of accruals and **€1.45m** of double-counted carrier cost.
- **Reporting accuracy:** removed a false **€1.5m** jump from Looker. Stopped **€2.8k–3.5k a month** of fees being booked as the wrong type.
- **Process automation:** automated **4** close exports and **3** manual checks. The shipping refresh now schedules itself, so finance control no longer asks us for hand-run builds.
- **Fixed at the source:** raised a fix in core billing for **~44k invoice lines a month** filed as GB instead of UK (still in review). Got Registration to fix invalid VAT input where it is entered.

### Detailed impact

| Area | What changed | Business impact | Technical impact | Evidence |
| --- | --- | --- | --- | --- |
| **Money in the right month** | Accruals read the correct payment status. Double-counted carrier cost removed. Duplicate snapshots cleaned up. | Kept ~€2.7m of cost out of the wrong period. Removed a false €1.5m jump in Looker. Stopped €2.8–3.5k a month of wrong fees. | Closed months are frozen. A one-snapshot-per-day test now covers 18 models. | [#2361](https://github.com/vinted/dataverse-finance/pull/2361), [#2157](https://github.com/vinted/dataverse-finance/pull/2157), [FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318), [#2244](https://github.com/vinted/dataverse-finance/pull/2244) |
| **Close needs fewer hands** | 4 exports and 3 manual checks automated. The shipping refresh schedules itself. | Finance control stops asking us for hand-run builds; there were 3 such requests since August. The WD1 vouchers step is off the critical path. | One shared list of refresh dates for finance and VGo. | [#2178](https://github.com/vinted/dataverse-finance/pull/2178), [#2203](https://github.com/vinted/dataverse-finance/pull/2203), [#2369](https://github.com/vinted/dataverse-finance/pull/2369), [dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425) |
| **Fixed at the source** | Fixes raised in core billing and with Registration. Upstream owners warned about their changes. | ~44k invoice lines a month will stop filing the UK as a separate country. Bad VAT input is stopped where it is entered. | Fewer downstream patches to maintain. | [core#137604](https://github.com/vinted/core/pull/137604), [FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413), [MA-83 thread](https://vinted.slack.com/archives/C046D0K49C6/p1787125459869369) |
| **Safer for the whole org** | Partition monitoring built. Unit tests that silently never ran now run. The triage bot names the failing value. | Incidents are caught before they fail downstream tasks. One earlier incident failed 20. | 121 models at risk of the partition limit, flagged across 337 tables. CI fixed for two teams. | [dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604), [dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220), [triage RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441/2026-08-24+-+Continuity+for+alert+triage) |
| **Ready for dbt 2.0** | Deprecation and lint sweeps done. Test files moved out of dbt's path. An open-source fix contributed. | The upgrade will not stall finance delivery. | 173 deprecation and 75 lint PRs, with all 930 tests unchanged. Fixes in 3 repos and in dbt Labs. | [FDSA-3281](https://vinted.atlassian.net/browse/FDSA-3281), [FDSA-3320](https://vinted.atlassian.net/browse/FDSA-3320), [dbt-external-tables#412](https://github.com/dbt-labs/dbt-external-tables/pull/412) |

---

## Part 2: Growth assessment against the career level framework

> **Framework context:** IC3 is mastery of one's own work. IC4 is a technical lead who resolves challenges across the domain and enables other AEs to do the same. The framework also says a business need must exist before an IC4 promotion is considered ([framework](https://docs.google.com/spreadsheets/d/16_i3t4lxF-niI92dy_E3MbxNdIusJ4bilndOClbwL5Y/edit?gid=955252402#gid=955252402)).

The gaps are split in two:
- **My behaviour:** what I can close myself.
- **Needs an opportunity:** a scope, a role or a business need I can't create alone.

| Dimension | Expectation | My evidence | Current level | Gap: my behaviour | Gap: needs an opportunity |
| --- | --- | --- | --- | --- | --- |
| **Theory & techniques** | Design complex architectures alone (IC3) vs. enable others to (IC4) | Gated rebuild, governed campaign mart, snapshot guard ([#2369](https://github.com/vinted/dataverse-finance/pull/2369), [RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762/2026-08-18+-+Governed+mart+for+shipping+discount+campaigns)) | **IC3** | Package these patterns so others can reuse them. | A teammate's project where they build with them. |
| **Engineering** | Code that inspires (IC3) vs. set and guard best practices (IC4) | Refactors with identical output over 4.0bn and 13.18bn rows ([#2222](https://github.com/vinted/dataverse-finance/pull/2222), [#2209](https://github.com/vinted/dataverse-finance/pull/2209)). 156 → 17.2 slot-hours ([#2175](https://github.com/vinted/dataverse-finance/pull/2175)). Bugbot rules and linter rule C006. | **IC3 (IC4 in part)** | Explain the reasoning behind the rules, not just ship them. | A mandate to own a standards area across teams. |
| **Quality standards** | Help others meet standards (IC3) vs. improve them and enable others (IC4) | Fixed CI skipping tests for two teams ([dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220)). Test-description and AI-review practices. | **IC4 in part** | Write the practices into the repo's standards; they live in Slack threads today. | None. |
| **Data mastery** | Whole lifecycle of my area (IC3) vs. all of the data stack (IC4) | Traced core billing → CDC → tax filing ([FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413)). Audited 337 tables org-wide. | **IC3 (IC4 in part)** | None. | Work that spans stacks outside finance. |
| **Impact measurement** | Own the metrics of my work (IC3) vs. enable others to (IC4) | € and row counts quoted on every fix. The refresh RFC measured a 4.6 h median wait. | **IC3 in part** | Keep a standing scorecard that tracks impact over time. | None. |
| **Structuring** | Iterative, systematic approach (IC3) vs. enable others to structure work (IC4) | Triage bot delivered in 4 phases. Stacked PRs. | **IC3** | Coach structure in reviews, not only in my own work. | Someone to coach: a mentee or a project lead. |
| **Strategy & roadmap** | Bring input and facilitate (IC3) vs. strategic expert for the domain (IC4) | Both 1:1 goals delivered. Self-service refresh RFC. Policy gate proposal. | **IC3** | Bring proposals to planning with an owner and a cost. | A seat in team or domain roadmap planning. |
| **Scope of ownership** | Resolve complex new problems end to end (IC3) vs. own the long-term quality of AEs' output (IC4) | €1.29m accrual, from detection to root cause ([#2361](https://github.com/vinted/dataverse-finance/pull/2361)). Duplicate snapshots. | **IC3** | Delegate and review rather than do. My output is still the main driver. | A formal remit for AE output quality in the domain. |
| **Technical debt** | Identify the team's debt (IC3) vs. make sure others decide consciously (IC4) | 173 + 75 sweep PRs. dbt 2.0 blockers cleared. | **IC3** | Start a shared debt list. | The team agreeing to prioritise from it. |
| **Business understanding** | Anticipate users' needs (IC3) vs. expert on the domain (IC4) | Added Nov and Dec close dates before anyone asked ([dbt-shared#432](https://github.com/vinted/dataverse-dbt-shared/pull/432)). Spotted that a refunded purchase is never invoiced. | **IC3** | Turn domain rules into written guides. | Exposure to finance strategy forums. |
| **Prioritisation** | Set my own priorities and cut scope (IC3) vs. prioritise systemic problems (IC4) | Chose root-cause fixes: 13 snapshot models ([FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)). | **IC3 in part** | Record what I chose not to do. Fewer high-volume sweeps. | None. |
| **Time management** | Manage expectations under uncertainty (IC3) vs. accurate delivery times (IC4) | Stacked PRs waiting on review. Late-evening work (7 Sep 1:1). | **Gap** | Keep to working hours. Give an estimate and a confidence level. Keep no more than 2 stacked PRs open. | None. |
| **Collaboration** | Drive cross-functional work (IC3) vs. drive cross-department work consistently (IC4) | VGo, Checkout, Registration, DPX, Payments, iSAF | **IC4 in part** | Leave incidents that others own to them (7 Sep 1:1). | A standing forum with Checkout. |
| **Communication** | Persuasive to any stakeholder (IC3) vs. minimal overhead, company-level influence (IC4) | € impact up front in PRs and RFCs. Incident updates. | **IC3** | Cut review load: 454 PRs and long threads. | A company-level forum to influence. |
| **Challenging** | Reflect critically (IC3) vs. role model for inviting challenge (IC4) | 45 review comments on other teams' RFCs | **IC3** | Invite challenge to my own designs systematically. | None. |
| **Knowledge leadership** | Initiate sharing (IC3) vs. an environment of excellence (IC4) | Hosted the Berlin dbt meet-up for ~60 people ([recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289)). Guides shared. Open source. | **IC3 (IC4 in part)** | Turn guides into written standards. | A guild session slot. |
| **Helping others** | Pull my weight beyond my deliverables | 140 PR reviews. AE hiring panel. | **Met** | None. | A mentee. |
| **Feedback** | Give feedback systematically (IC3) vs. build a feedback culture (IC4) | 140 PR reviews and RFC comments | **IC3** | Ask for structured feedback on my own work. | None. |
| **Learning** | Own my career path, with a circle of peers | Prepared for dbt 2.0. Filed dbt-core issues. | **IC3 in part** | Write a development plan toward IC4. | None. |
| **Attitude & caring** | Constructive, and responsible for the team's mood | Food bank volunteering days. Public credit to teammates. Insights Discovery suggestion. | **IC3** | Model a sustainable pace for the team. | None. |

---

## Part 3: Growth actions (path to IC4)

*Ordered by how much each closes the gap to IC4. Target dates are proposals to agree with António.*

1. **Enable, rather than do**: *Scope of ownership, Structuring, Theory & techniques*. **Behaviour**
    - **Action:** turn the refresh gate, the snapshot guard and case-log upkeep into three team skills or guides.
    - **Done when:** a teammate ships one of these patterns without my help.
    - **Target:** end of October.
2. **Track impact over time**: *Impact measurement*. **Behaviour**
    - **Action:** publish a scorecard of manual close steps left, ad-hoc refresh requests a month, MEC on-time % and alert false positives. Baseline it from the 1,255-ticket analysis.
    - **Done when:** it is reviewed monthly in the 1:1.
    - **Target:** baseline by mid-October, then monthly.
3. **Record the trade-offs**: *Prioritisation*. **Behaviour**
    - **Action:** keep a quarterly "doing / not doing" list, with the opportunity cost of each item.
    - **Done when:** at least one item is cut or deferred each quarter, agreed with António.
    - **Target:** Q4 planning.
4. **Pace and expectations**: *Time management, Attitude*. **Behaviour**
    - **Action:** keep to agreed working hours. Give each RFC a delivery estimate and a confidence level. Keep no more than 2 stacked PRs open.
    - **Done when:** no late-evening work outside incidents, and estimates are hit.
    - **Target:** from now.
5. **Reduce review overhead**: *Communication*. **Behaviour**
    - **Action:** batch sweeps into fewer PRs where it is safe. Agree a review cadence for chained PRs. Post a short monthly stakeholder update.
    - **Done when:** my share of the team's review queue stays under an agreed number.
    - **Target:** end of October.
6. **Respect incident ownership**: *Collaboration, Caring*. **Behaviour**
    - **Action:** on incidents that others own, offer help and wait to be asked.
    - **Done when:** no overlap is flagged in 1:1s.
    - **Target:** from now.
7. **Ask for challenge and feedback**: *Feedback, Challenging*. **Behaviour**
    - **Action:** ask Ieva, Evita and Emily for structured feedback. Add a "what would you change?" section to every RFC I write.
    - **Done when:** the feedback themes are reviewed with António.
    - **Target:** mid-October.
8. **Write the standards down**: *Quality standards, Knowledge leadership*. **Behaviour**
    - **Action:** write the test-description and AI-review practices into the repo's standards, and start a shared debt list.
    - **Done when:** both are merged.
    - **Target:** end of November.
9. **Write an IC4 development plan**: *Learning, Strategy & roadmap*. **Behaviour**
    - **Action:** draft the plan with António. Join the *Ontology Pipeline* book club, and co-run the Vilnius dbt meet-up.
    - **Done when:** the plan is agreed and reviewed quarterly.
    - **Target:** next 1:1.
10. **Opportunities to discuss with António**: *Scope of ownership, Structuring, Strategy & roadmap, Collaboration, Knowledge leadership, Helping others*. **Opportunity**
    - **Action:** discuss which of these the team can offer:
        - a mentee, or a teammate's project to support.
        - a seat in team or domain roadmap planning.
        - a remit for AE quality standards in the domain.
        - ownership of a standing agreement with Checkout: a pre-release notice for changes that touch invoices.
        - a guild session slot.
        - whether a business need for an IC4 role exists, or could exist.
    - **Done when:** at least two are agreed, with owners.
    - **Target:** next 1:1.

---

## Part 4: Weekly achievement log

### 3–9 Aug 2026

- Rejoined Finance DSA and started organising the Berlin dbt meet-up ([thread](https://vinted.slack.com/archives/C05L8F2HVGF/p1785741071289669)). `[Co-create]`
- Turned PR review comments into Bugbot review rules ([#1817](https://github.com/vinted/dataverse-finance/pull/1817)). `[Aim High / Above & beyond]`
- Fixed 10 models that exposed personal data, before the linter rule was enforced ([FDSA-3054](https://vinted.atlassian.net/browse/FDSA-3054)). `[Ownership]`
- Proposed the V-Assist agent roadmap for finance ([v-assist-registry#677](https://github.com/vinted/v-assist-registry/pull/677)). `[Co-create]`
- Started the dbt deprecation and lint sweeps that prepare us for dbt 2.0 ([FDSA-3070](https://vinted.atlassian.net/browse/FDSA-3070)). `[Aim High]`

### 10–16 Aug 2026

- Fixed Looker measures that would have silently disappeared under the new meta format ([lookml-generator#160](https://github.com/vinted/dataverse-lookml-generator/pull/160)). `[Aim High / Above & beyond]`
- Found that the Mangopay S3 load stopped at 1,000 files, so a July close retry skipped files ([FDSA-3067](https://vinted.atlassian.net/browse/FDSA-3067)). `[Ownership]`
- Documented the Mangopay API and S3 pipeline ([FDSA-3101](https://vinted.atlassian.net/browse/FDSA-3101)). `[Co-create]`
- Gave feedback on the new AE technical interview material ([FDSA-3102](https://vinted.atlassian.net/browse/FDSA-3102)). `[Grow]`
- Merged 162 finance PRs from the lint and deprecation sweeps across 3–16 Aug ([FDSA-3281](https://vinted.atlassian.net/browse/FDSA-3281)). `[Aim High]`

### 17–23 Aug 2026

- Traced a wrong VAT number that reached the Lithuanian tax authority and added a 35-character test ([FDSA-3120](https://vinted.atlassian.net/browse/FDSA-3120)). Registration then fixed Spanish VAT validation at the source, in MA-83 ([thread](https://vinted.slack.com/archives/C046D0K49C6/p1787125459869369)). `[Ownership / Co-create / Above & beyond]`
- Wrote two RFCs: the [governed shipping campaigns mart](https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762/2026-08-18+-+Governed+mart+for+shipping+discount+campaigns) and the [shipping result split](https://vinted.atlassian.net/wiki/spaces/DF/pages/32099795441/2026-08-20+-+Split+mrt_shipping_results+into+components). `[Co-create]`
- Split out Adyen refund fees for Gabija. They reconcile to Adyen on all 23 invoices ([#2083](https://github.com/vinted/dataverse-finance/pull/2083)). `[Aim High]`
- Gave FP&A Pigment access to weekly targets ([marketplace-intelligence#1141](https://github.com/vinted/dataverse-marketplace-intelligence/pull/1141)). `[Co-create]`
- Started the export bucket move, and held the merge until after close ([terraform-dataverse#3723](https://github.com/vinted/terraform-dataverse/pull/3723)). `[Ownership]`
- Organised Berliner Tafel food bank volunteering days ([thread](https://vinted.slack.com/archives/C04HC4J6X2R/p1786958374428139)). `[Care]`

### 24–30 Aug 2026

- Removed double-counted SPEEDX carrier cost from August before close: €712k invoiced and €741k accrued ([#2157](https://github.com/vinted/dataverse-finance/pull/2157)). `[Aim High]`
- Found 121 models across the org at risk of BigQuery's partition limit, and built monitoring that alerts each owning team ([dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604), [FDSA-3169](https://vinted.atlassian.net/browse/FDSA-3169)). `[Aim High / Co-create / Above & beyond]`
- Delivered the RFC and phases 1–2 of the finance alert-triage bot ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441/2026-08-24+-+Continuity+for+alert+triage), [v-assist-registry#846](https://github.com/vinted/v-assist-registry/pull/846)). `[Aim High]`
- Fixed an out-of-memory failure on the Adyen fees model, from 156 to 17.2 slot-hours ([#2175](https://github.com/vinted/dataverse-finance/pull/2175)). `[Aim High]`
- Added seeds for the governed campaign mart ([#2158](https://github.com/vinted/dataverse-finance/pull/2158)) and CDD exclusion rules ([#2153](https://github.com/vinted/dataverse-finance/pull/2153)). `[Aim High]`
- Shared my unit-testing guide with the AE community ([thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787824097864589?thread_ts=1787823910.491879&cid=C03JBPN0Q1W)). `[Co-create / Grow]`

### 31 Aug – 6 Sep 2026

- Ran my first month-end close with Emily, with 94.1% of models on time ([retro](https://vinted.slack.com/archives/G01A7KGHY74/p1788944254889679), [MEC log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32142295207/2026-08+MEC+Issue+Request+Log)). `[Ownership / Co-create]`
- Automated 4 close exports ([#2178](https://github.com/vinted/dataverse-finance/pull/2178), [#2205](https://github.com/vinted/dataverse-finance/pull/2205), [#2207](https://github.com/vinted/dataverse-finance/pull/2207)), and turned 3 manual fee checks into tests ([#2203](https://github.com/vinted/dataverse-finance/pull/2203)). `[Aim High]`
- Fixed the negative amounts NetSuite rejects ([#2194](https://github.com/vinted/dataverse-finance/pull/2194)). Also fixed, unasked, two more models with the same risk ([#2197](https://github.com/vinted/dataverse-finance/pull/2197), [#2198](https://github.com/vinted/dataverse-finance/pull/2198)). `[Ownership]`
- Fixed the AU vendor mapping on AUD 85,991.59 of fee accrual that an accountant had corrected by hand ([#2212](https://github.com/vinted/dataverse-finance/pull/2212)). `[Ownership]`
- Led the 4 Sep double-entry incident and recovered it in about 20 minutes ([incident](https://vinted.slack.com/archives/C0706RCL6CF/p1788502006663509?thread_ts=1788500547.898079&cid=C0706RCL6CF)). `[Ownership]`
- Set up the AE hiring panel group and its access ([service-catalog#17023](https://github.com/vinted/service-catalog/pull/17023)). `[Grow]`

### 7–13 Sep 2026

- Found 34 duplicate snapshots in 10 models, behind a false €1.5m jump in Looker. Cleaned them up and added a one-per-day test ([#2232](https://github.com/vinted/dataverse-finance/pull/2232), [FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318)). `[Ownership]`
- Caught an upstream Adyen rename that would have booked €2.8–3.5k a month as the wrong fee type ([#2244](https://github.com/vinted/dataverse-finance/pull/2244)). `[Aim High]`
- Wrote the self-service data refresh RFC from all 1,255 FDSA tickets. It estimates ~500 finance hours a year unblocked ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071/2026-09-07+-+Self-service+data+refresh+for+Finance)). `[Aim High / Co-create]`
- Refactored the shipping result (1,206 → 117 lines) and double entry (837 → 88 lines), with identical output ([#2222](https://github.com/vinted/dataverse-finance/pull/2222), [#2209](https://github.com/vinted/dataverse-finance/pull/2209)). `[Aim High]`
- Found unit tests silently not running in CI for two teams, and fixed it ([dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220), [dataverse-cli#705](https://github.com/vinted/dataverse-cli/pull/705)). `[Aim High / Above & beyond]`
- Turned on continuous deployment for finance ([#2154](https://github.com/vinted/dataverse-finance/pull/2154)). Proposed one shared refresh-date list with VGo ([dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425)). `[Co-create]`
- Hosted the Berlin dbt meet-up for ~60 guests and moderated the AE career panel ([recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289)). `[Co-create / Grow]`

### 14–20 Sep 2026

- Changed 13 snapshot models to replace a same-day re-run instead of adding a copy ([FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)). `[Ownership]`
- Put the shared refresh dates live in both the finance and VGo projects ([FDSA-3319](https://vinted.atlassian.net/browse/FDSA-3319), [vintedgo-dbt#9472](https://github.com/vinted/dataverse-vintedgo-dbt/pull/9472)). `[Co-create]`
- Opened the investigation into the payment status change behind the €1.29m accrual shift ([FDSA-3370](https://vinted.atlassian.net/browse/FDSA-3370)). `[Aim High]`

### 21–27 Sep 2026

- Stopped €1.29m of cost moving out of August: fixed the accrual source, froze closed months and warned the upstream owners ([#2361](https://github.com/vinted/dataverse-finance/pull/2361), [heads-up](https://vinted.slack.com/archives/C077HPXKTSN/p1790104347593269?thread_ts=1787219993.360489&cid=C077HPXKTSN)). `[Ownership / Aim High / Co-create]`
- Wrote a fix in core billing for ~44k invoice lines a month filed as GB instead of UK; it is in review ([core#137604](https://github.com/vinted/core/pull/137604), [FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413)). `[Ownership / Co-create / Above & beyond]`
- Merged an open-source fix into dbt Labs' dbt-external-tables ([dbt-external-tables#412](https://github.com/dbt-labs/dbt-external-tables/pull/412)). `[Co-create / Grow / Above & beyond]`
- Made the shipping result rebuild itself on the agreed close and actuals dates ([#2369](https://github.com/vinted/dataverse-finance/pull/2369), [#2379](https://github.com/vinted/dataverse-finance/pull/2379)). Added the Nov and Dec dates, and unblocked every dataverse-dbt-shared PR ([dbt-shared#432](https://github.com/vinted/dataverse-dbt-shared/pull/432), [terraform-github#8831](https://github.com/vinted/terraform-github/pull/8831)). `[Aim High]`
- Found 39 wrong values in the Adyen reconciliation by comparing the table with its earlier version ([#2360](https://github.com/vinted/dataverse-finance/pull/2360)). `[Aim High]`
- Added CDC gap checks that name the owner ([#2382](https://github.com/vinted/dataverse-finance/pull/2382)). Created the [alert case log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32104972550/Finance+DSA+Alert+Case+Log) that the triage bot reads. `[Co-create]`

<details>
<summary>How this was compiled</summary>

- **Sources:** GitHub, Jira, Confluence and Slack, from 1 Aug to 28 Sep 2026. The raw lists and summaries are in [sources/](sources/).
- **Slack:** public and private channels only. 15 Aug – 11 Sep and 21–28 Sep were read in full. 1–14 Aug and 12–20 Sep came only from targeted searches.
- **Figures:** every figure is quoted from a PR body, ticket description or page.

</details>
