# Performance & career self-assessment: IC4 and PL4

**Review period:** 1 Aug – 28 Sep 2026

**Name:** Jeremy Chia, Analytics Engineer, Finance DSA

**Frameworks:** [AE Impact & Growth Framework (IC)](https://docs.google.com/spreadsheets/d/16_i3t4lxF-niI92dy_E3MbxNdIusJ4bilndOClbwL5Y/edit?gid=955252402#gid=955252402) and [DSA People Leader Impact & Growth Framework (PL)](https://docs.google.com/spreadsheets/d/1W8hRYEv_r4BKidwc8Maex2e2pvjIWHVA-yXH7lJxcHg/edit)

**Evidence window:** 8 weeks, since I rejoined on 3 Aug 2026. This is a trajectory, not a finished case; proposed checkpoint at the end of Q1 2027.

**Primary artifact:** [brag-list.md](https://github.com/jeremychia/jeremychia/blob/main/brag/2026-08-01_to_2026-09-28/brag-list.md)

---

## Summary and ask

**The pattern** *(draft)*: I find money errors at their source, often in another team's system. Then I turn the fix into a check or a schedule that runs without me.

- **The ask:** *[to write: the level you're asking for (IC4, or PL3 then PL4) and the number. Put the number in the 1:1 doc only, not in this public repo]*
- **Why it matters:** *[to write: why finance DSA needs a technical lead or a team lead, in two or three sentences. For example: the close automation and controls roadmap, the upstream-change risk, the request load]*
- **Why now:** *[to write: for example, continuous deployment is live, dbt 2.0 is coming, and Q4 close season is ahead]*
- **Next steps:** the three focus actions in Part 5. The plan is due mid-November and the delegation target is end of December. The checkpoint is the end of Q1 2027.
- **Where I am:** a strong IC3. There is partial evidence toward IC4 in standards, data mastery and collaboration. On the PL side, the evidence is strong in collaboration, process and external engagement. I have no direct reports, so half of PL4 can't be shown yet. The levels below are my own read, for António to calibrate.
- **My preferred track and why:** *[to write: which of IC4 or PL4 energises you more, shaping the data platform or growing people, and why]*
- **What I need from António:**
    1. agree the track, or how to keep both open until the checkpoint.
    2. a project with 1–2 contributors that I plan, split and deliver.
    3. a seat in finance DSA roadmap planning.
- **Feedback I'd like:**
    - does my read of the levels in Parts 3 and 4 match yours?
    - for each **Not yet**, what would you need to see to move it?
    - what does someone at IC4 or PL4 do that I don't do yet?

---

## Part 1: Impact summary

### Highlights

- **Accounting accuracy:** removed **€1.45m** of double-counted carrier cost (€712k invoiced, €741k accrued) **before** the August close. July had been corrected by hand; August didn't need to be. Found a **€1.29m** accrual timing error **after** the August close. It is fixed from September. Whether August is restated is accounting's call, and the upstream owners were warned so other consumers can check their models.
- **Systems other teams rely on:** partition monitoring across **337** tables, with **121** at-risk models flagged, so each owning team now gets its own alert. Unit tests that CI had silently skipped now run for **two** teams. VGo now rebuilds on the same dates as finance.
- **Automation:** **4** close exports and **3** manual checks now run themselves. The shipping refresh schedules itself (in review), so finance control won't need to ask us for hand-run builds. There were **3** such requests since August.
- **Fixed at the source:** a fix in core billing for **~44k** invoice lines a month filed as GB instead of UK (in review). Registration opened MA-83 to fix Spanish VAT validation, so bad numbers will be stopped where they are entered, not caught by finance later.

### What others said

| Quote | Who | About | Link |
| --- | --- | --- | --- |
| "hosted a really interesting round table… very well conducted" | António Fitas | Berlin dbt meet-up | [Slack](https://vinted.slack.com/archives/C076F6CME10/p1789104603255589) |
| "33 seconds is peanuts, thanks for the fast response!" | António Fitas | double-entry incident at close | [Slack](https://vinted.slack.com/archives/C0706RCL6CF/p1788506906115249) |
| "thanks for enabling it!! game changer" | Júlia Solé Cubilo | continuous deployment for finance | [Slack](https://vinted.slack.com/archives/C076F6CME10/p1789465411298849) |
| "the data makes a super clear case" | Júlia Solé Cubilo | self-service refresh RFC | [Slack](https://vinted.slack.com/archives/C076F6CME10/p1788771497947879) |
| "a great idea" | Oscar Ligthart | org-wide partition monitoring | [Slack](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787641108570719) |
| "a good catch" | Vedashree Patil | CDD pipeline name that never resolved | [Slack](https://vinted.slack.com/archives/C059T9KAF8X/p1787661975738699) |
| "huge huge thanks… real-mvp" | Samanta Vasilenkaitė | a detailed PR review | [Slack](https://vinted.slack.com/archives/C076F6CME10/p1790258273667139) |

### Detailed impact

| Area | What changed | Business impact | Technical impact | Evidence |
| --- | --- | --- | --- | --- |
| **Safer for the whole org** | Partition monitoring built. Unit tests that silently never ran now run. The triage bot names the failing value. | Incidents are caught before they fail downstream tasks. One earlier incident failed 20. | 121 at-risk models flagged across 337 tables; CI fixed for two teams. | [dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604), [dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220), [triage RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441/2026-08-24+-+Continuity+for+alert+triage) |
| **Money in the right month** | Carrier cost de-duplicated; accruals read the right payment status; duplicate snapshots removed; an upstream rename caught. | **Before close:** €1.45m double-counted carrier cost removed from August. **After close:** €1.29m accrual timing fixed from September; August restatement is accounting's call. **Dashboard only:** a false €1.5m jump removed from Looker; reported figures were unaffected. **Prevented:** €2.8–3.5k a month of wrong fee type, caught before the upstream change landed. | Closed months frozen; a one-snapshot-per-day test on 18 models. | [#2157](https://github.com/vinted/dataverse-finance/pull/2157), [#2361](https://github.com/vinted/dataverse-finance/pull/2361), [FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318), [#2244](https://github.com/vinted/dataverse-finance/pull/2244) |
| **Close needs fewer hands** | 4 exports and 3 manual checks automated. The shipping refresh schedules itself (in review). | Finance control stops asking us for hand-run builds; there were 3 such requests since August. The WD1 vouchers step is off the critical path. | One shared list of refresh dates for finance and VGo. | [#2178](https://github.com/vinted/dataverse-finance/pull/2178), [#2203](https://github.com/vinted/dataverse-finance/pull/2203), [#2369](https://github.com/vinted/dataverse-finance/pull/2369), [dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425) |
| **Fixed at the source** | Fixes raised in core billing (in review) and with Registration. Upstream owners warned. | ~44k invoice lines a month will stop filing the UK as a separate country. Bad VAT input is stopped where it is entered. | Fewer downstream patches to maintain. | [core#137604](https://github.com/vinted/core/pull/137604), [FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413), [MA-83 thread](https://vinted.slack.com/archives/C046D0K49C6/p1787125459869369) |
| **Cost and performance** | The Adyen fees model was rewritten after it ran out of memory. The shipping split used views, not tables. | The daily fees model completes in 17.2 slot-hours instead of failing at 156: ~139 slot-hours a day, ~50k a year. That is roughly $3k a year at BigQuery's pay-as-you-go list price (estimate; reservations show it as capacity, not billing). Views avoided storing a second 2.3 TB copy, roughly $550 a year at list price (estimate). | 1,290 → 245 query stages, and 3.34 TiB of spill → none. | [#2175](https://github.com/vinted/dataverse-finance/pull/2175), [#2222](https://github.com/vinted/dataverse-finance/pull/2222) |
| **Maintenance: dbt 2.0 readiness** | Deprecation and lint sweeps; test files moved; an open-source fix. | The upgrade will not stall finance delivery. | Mostly mechanical sweeps, with all 930 tests unchanged; the leverage is the fixes in 3 shared repos and in dbt Labs. | [FDSA-3281](https://vinted.atlassian.net/browse/FDSA-3281), [FDSA-3320](https://vinted.atlassian.net/browse/FDSA-3320), [dbt-external-tables#412](https://github.com/dbt-labs/dbt-external-tables/pull/412) |

### Systems others rely on

"Built" is IC3 evidence; "others rely on it" is IC4 evidence. Where use isn't measured yet, the scorecard in Part 5 will measure it.

| System | Who relies on it | Adoption |
| --- | --- | --- |
| Partition monitoring | every team that owns one of the 121 flagged models | alerts sent and acted on: to measure |
| Unit tests in CI | finance and dataverse-people | CI runs all tests again (in the test case, 6 instead of 2) |
| Review rules (Bugbot) | every finance PR; the rules were shared with the AE community | PRs flagged: to measure |
| Shared refresh dates | finance and VGo dbt projects | both rebuild on the same dates since 17 Sep |
| Triage bot and case log | the finance DSA on-support rotation, every day | alerts triaged: to measure |
| Continuous deployment | every finance merge | on since 9 Sep; 127 of 308 models excluded by rule |

### Judgment calls

These are the choices behind the work. They don't show up in the output.

| Decision | What I chose | What I rejected | Trade-off |
| --- | --- | --- | --- |
| Duplicate snapshots | Scanned all 18 snapshot tables and found 34 duplicates in 10 models ([FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318)) | Fixing only the 6 in the ticket | More work up front, but it found 28 duplicates the ticket missed, going back to March 2025 |
| GB filed instead of UK | Fixed it in core billing from a fork, with a staging mapping until it ships ([core#137604](https://github.com/vinted/core/pull/137604), [#2378](https://github.com/vinted/dataverse-finance/pull/2378)) | A downstream patch on its own | Two changes to keep in step until core merges, then one fewer patch for finance to maintain |
| €1.29m accrual | Froze closed months and left restating August to accounting ([#2361](https://github.com/vinted/dataverse-finance/pull/2361)) | Letting the fix rewrite a month already closed | August stays as filed until accounting decides |
| Shipping split | Views instead of tables ([#2222](https://github.com/vinted/dataverse-finance/pull/2222)) | Tables, which would have stored a second 2.3 TB copy | *[to write: what the views cost, e.g. compute on each read]* |
| Export bucket move | Held the merge until after close and warned iSAF and Pigment ([terraform-dataverse#3723](https://github.com/vinted/terraform-dataverse/pull/3723)) | Merging during close | *[to write: what the delay cost]* |
| Campaign mart cutover | Sized the change (+€17.9k InPost ES, −€8.8k SPS SK) and left the decision to Finance Control ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762/2026-08-18+-+Governed+mart+for+shipping+discount+campaigns)) | Switching over silently | The cutover waits for Finance Control's decision |

### Agreed in 1:1s

| Date | What was agreed | Owner | Status |
| --- | --- | --- | --- |
| 31 Aug | Automate the escrow revenue controls, with a September target | Me | 22 controls proposed; in review ([FDSA-3299](https://vinted.atlassian.net/browse/FDSA-3299), [#2300](https://github.com/vinted/dataverse-finance/pull/2300)) |
| 31 Aug | Propose backend validation to Checkout | Me | Core billing fix open ([core#137604](https://github.com/vinted/core/pull/137604)); a standing agreement is in Part 5 |
| 7 Sep | Keep to working hours, and leave incidents others own to them | Me | Ongoing; focus action 3 in Part 5 |
| 23 Sep | Fill in weekly achievements and reflections | Me | Started; Part 6 is the log |

### What went wrong, and what I changed

- **What happened:** my one-snapshot-per-day test ([#2232](https://github.com/vinted/dataverse-finance/pull/2232)) ran for the first time on 10 Sep, before the older duplicates had been cleaned up. Each Airflow retry rebuilt the snapshot before re-running the test. So the test fed itself: three snapshots a day on two daily models ([FDSA-3330](https://vinted.atlassian.net/browse/FDSA-3330)).
- **What I did:** ran the cleanup, deleted that day's extra snapshots, and cleared each task once. Then I changed 13 snapshot models to replace a same-day re-run instead of appending ([FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)).
- **What I learned:** clean up before you enforce. A test that sits behind a rebuild must survive retries.

### Feedback I received, and what I changed

| Feedback | From | What I changed |
| --- | --- | --- |
| Why work at 10 PM and at weekends? | António, 1:1 on 7 Sep | *[to write: what you've changed since, with an example]* |
| On incidents others own, leave it to them | António, 1:1 on 7 Sep | *[to write]* |

---

## Part 2: Two tracks at a glance

> **Both are different roles.** The IC framework says IC4 is "a fundamentally different role for which a business need must exist". People leadership likewise needs headcount and a scope. IC4 enables other AEs through technique and standards. PL4 does it through people: leading a large team or a small area, with its structure and a plan of up to 12 months.

| | IC4: technical lead | PL4: manager |
| --- | --- | --- |
| **What the level is** | Resolves challenges across the area or domain, and enables other AEs to do the same | Leads a large team or a small area; defines team structure; plans up to 12 months ahead. Includes PL3 (team lead) |
| **Where I stand** (my read) | Strong IC3; partial evidence toward IC4 in standards, data mastery, collaboration and knowledge leadership | Strong on collaboration, process, quality standards and external engagement; the people-leadership dimensions can't be shown without reports |
| **Strongest evidence** | Standards others use (review rules, linter rule C006, CI fixed for two teams); data mastery across the stack | Cross-domain collaboration with six teams; process improvements (CDD, triage bot); hosting the Berlin dbt meet-up |
| **Biggest behaviour gap** | Enable rather than do: my own output is still the main driver | Delegate and keep a sustainable pace: 454 PRs, late evenings, stepping into others' incidents (7 Sep 1:1) |
| **Biggest opportunity gap** | A teammate's project to enable, and a remit for AE standards in the domain | Direct reports: team performance and people growth can't be shown without them |
| **Shared gaps** | Delegation, pace, structured feedback, a 6–12 month plan, and written standards | *(same)* |
| **Business need** | An IC4 role in finance DSA | A PL3 team lead role first, then a larger scope for PL4 |

**One decision first:** agree with António which track to aim for, or how to keep both open. The shared behaviour gaps below are worth closing either way.

---

## Part 3: IC4 assessment (Analytics Engineer framework)

> **Framework context:** IC3 is mastery of one's own work. IC4 is a technical lead who resolves challenges across the domain and enables other AEs to do the same. The framework also says a business need must exist before an IC4 promotion is considered ([framework](https://docs.google.com/spreadsheets/d/16_i3t4lxF-niI92dy_E3MbxNdIusJ4bilndOClbwL5Y/edit?gid=955252402#gid=955252402)).

**Evidence toward IC4** is my read, for António to calibrate: **Strong** means the IC4 statement is evidenced, **Partial** means some of it is, **Not yet** means little or none. IC3 is met on every dimension except four: impact measurement, prioritisation, learning and time management.

The gaps are split in two:

- **My behaviour:** what I can close myself.
- **Needs an opportunity:** a scope, a role or a business need I can't create alone.

| Dimension | Expectation | My evidence | Evidence toward IC4 | Gap: my behaviour | Gap: needs an opportunity |
| --- | --- | --- | --- | --- | --- |
| **Theory & techniques** | Design complex architectures alone (IC3) vs. enable others to (IC4) | Gated rebuild, governed campaign mart, snapshot guard ([#2369](https://github.com/vinted/dataverse-finance/pull/2369), [RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762/2026-08-18+-+Governed+mart+for+shipping+discount+campaigns)) | **Not yet** | Package these patterns so others can reuse them. | A teammate's project where they build with them. |
| **Engineering** | Code that inspires (IC3) vs. set and guard best practices (IC4) | Refactors with identical output over 4.0bn and 13.18bn rows ([#2222](https://github.com/vinted/dataverse-finance/pull/2222), [#2209](https://github.com/vinted/dataverse-finance/pull/2209)). 156 → 17.2 slot-hours ([#2175](https://github.com/vinted/dataverse-finance/pull/2175)). Bugbot rules and linter rule C006. | **Partial** | Explain the reasoning behind the rules, not just ship them. | A mandate to own a standards area across teams. |
| **Quality standards** | Help others meet standards (IC3) vs. improve them and enable others (IC4) | Fixed CI skipping tests for two teams ([dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220)). Test-description and AI-review practices. | **Partial** | Write the practices into the repo's standards; they live in Slack threads today. | None. |
| **Data mastery** | Whole lifecycle of my area (IC3) vs. all of the data stack (IC4) | Traced core billing → CDC → tax filing ([FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413)). Audited 337 tables org-wide. | **Partial** | None. | Work that spans stacks outside finance. |
| **Impact measurement** | Own the metrics of my work (IC3) vs. enable others to (IC4) | € and row counts quoted on every fix. The refresh RFC measured a 4.6 h median wait. | **Not yet** | Keep a standing scorecard that tracks impact over time. | None. |
| **Structuring** | Iterative, systematic approach (IC3) vs. enable others to structure work (IC4) | Triage bot delivered in 4 phases. Stacked PRs. | **Not yet** | Coach structure in reviews, not only in my own work. | Someone to coach: a mentee or a project lead. |
| **Strategy & roadmap** | Bring input and facilitate (IC3) vs. strategic expert for the domain (IC4) | Both 1:1 goals delivered. Self-service refresh RFC. Policy gate proposal. | **Not yet** | Bring proposals to planning with an owner and a cost. | A seat in team or domain roadmap planning. |
| **Scope of ownership** | Resolve complex new problems end to end (IC3) vs. own the long-term quality of AEs' output (IC4) | €1.29m accrual, from detection to root cause ([#2361](https://github.com/vinted/dataverse-finance/pull/2361)). Duplicate snapshots. | **Not yet** | Delegate and review rather than do. My output is still the main driver. | A formal remit for AE output quality in the domain. |
| **Technical debt** | Identify the team's debt (IC3) vs. make sure others decide consciously (IC4) | 173 + 75 sweep PRs. dbt 2.0 blockers cleared. | **Not yet** | Start a shared debt list. | The team agreeing to prioritise from it. |
| **Business understanding** | Anticipate users' needs (IC3) vs. expert on the domain (IC4) | Added Nov and Dec close dates before anyone asked ([dbt-shared#432](https://github.com/vinted/dataverse-dbt-shared/pull/432)). Spotted that a refunded purchase is never invoiced. | **Not yet** | Turn domain rules into written guides. | Exposure to finance strategy forums. |
| **Prioritisation** | Set my own priorities and cut scope (IC3) vs. prioritise systemic problems (IC4) | Chose root-cause fixes: 13 snapshot models ([FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)). | **Not yet** | Record what I chose not to do. Fewer high-volume sweeps. | None. |
| **Time management** | Manage expectations under uncertainty (IC3) vs. accurate delivery times (IC4) | Stacked PRs waiting on review. Late-evening work (7 Sep 1:1). | **Not yet** | Keep to working hours. Give an estimate and a confidence level. Keep no more than 2 stacked PRs open. | None. |
| **Collaboration** | Drive cross-functional work (IC3) vs. drive cross-department work consistently (IC4) | VGo, Checkout, Registration, DPX, Payments, iSAF | **Partial** | Leave incidents that others own to them (7 Sep 1:1). | A standing forum with Checkout. |
| **Communication** | Persuasive to any stakeholder (IC3) vs. minimal overhead, company-level influence (IC4) | € impact up front in PRs and RFCs. Incident updates. | **Not yet** | Cut review load: 454 PRs and long threads. | A company-level forum to influence. |
| **Challenging** | Reflect critically (IC3) vs. role model for inviting challenge (IC4) | 45 review comments on other teams' RFCs | **Not yet** | Invite challenge to my own designs systematically. | None. |
| **Knowledge leadership** | Initiate sharing (IC3) vs. an environment of excellence (IC4) | Hosted the Berlin dbt meet-up for ~60 people ([recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289)). Guides shared. Open source. | **Partial** | Turn guides into written standards. | A guild session slot. |
| **Helping others** | Pull my weight beyond my deliverables | 140 PR reviews. AE hiring panel. | **Strong** | None. | A mentee. |
| **Feedback** | Give feedback systematically (IC3) vs. build a feedback culture (IC4) | 140 PR reviews and RFC comments | **Not yet** | Ask for structured feedback on my own work. | None. |
| **Learning** | Own my career path, with a circle of peers | Prepared for dbt 2.0. Filed dbt-core issues. | **Not yet** | Write a development plan toward IC4. | None. |
| **Attitude & caring** | Constructive, and responsible for the team's mood | Food bank volunteering days. Public credit to teammates. Insights Discovery suggestion. | **Not yet** | Model a sustainable pace for the team. | None. |

---

## Part 4: PL4 assessment (DSA People Leader framework)

> **What PL4 is:** "Manager". It means leading a large team with a complex scope, or a small area or domain. It means defining and evolving the team's structure, and planning up to 12 months ahead. The statements are additive, so PL4 includes everything in PL3 ("Team Lead").

### Where I stand

- **Already at PL4 or above, without reports:**
    - **cross-domain collaboration:** with VGo, Checkout, Registration, DPX, Payments and iSAF.
    - **quality standards and processes:** CDD, the triage bot, review rules, and CI fixed for two teams.
    - **external engagement:** hosted a dbt meet-up for ~60 people, and contributed to open source. 
- **The structural gap is having no direct reports.** Five dimensions assume a team: team performance, people growth, team design, part of communication, and caring for a scope. None of them can be shown fully without people to lead.
- **The biggest gap I can close myself is delegation and pace.** The framework asks a people leader to get people "working on the right things for the right amount of time … while keeping a healthy work life balance". My 454 PRs, late evenings, and stepping into incidents others own (7 Sep 1:1) are the opposite signal.
- **Planning horizon:** my work runs on 3–6 month horizons, which is PL3. PL4 asks for turning strategy into plans of up to 12 months.

| Evidence toward PL4 (my read) | Dimensions |
| --- | --- |
| **Strong** | quality standards, leading projects, decision making, risk, collaboration, procedures, external engagement |
| **Partial** | vision & strategy, theory & techniques, business understanding, communication, challenging, team design, feedback, learning, attitude, caring |
| **Not yet** | planning timespan, prioritisation & time management; team performance and people growth need reports |

| Dimension | PL3 vs. PL4 ask | My evidence | Evidence toward PL4 | Gap: my behaviour | Gap: needs an opportunity |
| --- | --- | --- | --- | --- | --- |
| **Planning timespan** | Day to day, 3–6 months (PL3) vs. turning strategy into plans under 12 months (PL4) | Work planned in 3–6 month pieces; Q4 growth actions | **Not yet** | Write a 6–12 month plan for finance AE topics, with owners | A planning cycle where I own a plan |
| **Vision & strategy** | Contribute to my organisation's vision (PL3) vs. contribute to DSA's and co-create my organisation's (PL4) | Self-service refresh RFC; policy gate for the AE roadmap; skills hierarchy and BI tooling proposals in #analytics-engineering | **Partial** | Turn proposals into a written strategy for finance data | A seat in finance DSA roadmap planning |
| **Theory & techniques** | Enough mastery to unblock my reports (same at PL3 and PL4) | Unblocked stakeholders: an over-limit Looker query, the shipping accrual logic explained step by step | **Partial** | Unblock by pointing people to the answer, not only by doing it | Reports to unblock |
| **Quality standards** | Deliverables meet standards, contribute to improving them (PL3) vs. drive improvements in the function (PL4) | CDD for finance; review rules; CI fixed for two teams; dbt 2.0 readiness | **Strong** | Write the practices into standards | None |
| **Leading projects** | Resolve complex problems in time and at quality (same at PL3 and PL4) | Shipping result chain; duplicate snapshots; the €1.29m accrual | **Strong** | Lead with others doing the parts, not alone | A project with 1–2 contributors |
| **Decision making** | Lay out arguments and rationale (PL3) vs. zoom out to the wider implications (PL4) | RFCs with options and costs; shared refresh dates across two projects | **Strong** | None | None |
| **Risk** | Conscious risk-reward trade-offs (same at PL3 and PL4) | Held the bucket merge until after close; used views to avoid doubling a 2.3 TB mart | **Strong** | None | None |
| **Business understanding** | Equal sparring partner (PL3) vs. one of the company's experts on the area (PL4) | Accrual, VAT and refund rules traced to source; anticipated the close dates | **Partial** | Write the domain rules down so others learn them | Exposure to finance leadership forums |
| **Prioritisation & time management** | People work on the right things, with delegation and a healthy work-life balance (same at PL3 and PL4) | Root-cause fixes chosen over patches, but 454 PRs, late evenings and others' incidents (7 Sep 1:1) | **Not yet** | Delegate; keep to working hours; leave others' incidents to them | A scope of people to prioritise for |
| **Communication** | Bring clarity when plans change, and talk openly with reports (PL3) vs. complex ideas adapted to each audience (PL4) | Plain-language PRs and RFCs with € up front; heads-ups to upstream teams; moderated a career panel | **Partial** | Shorter threads, less review load | Direct reports, for the report half |
| **Collaboration** | Align stakeholders and route their requests (PL3) vs. drive cross-function and cross-domain work (PL4) | Six teams; self-service refresh proposes a request route; shared dates with VGo | **Strong** | None | A standing forum with Checkout |
| **Procedures** | Improve tools and processes for collaboration (same at PL3 and PL4) | Triage bot and case log; CDD; On Support page | **Strong** | None | None |
| **Challenging** | Encourage others to challenge my ideas, safely (same at PL3 and PL4) | 45 review comments on others' RFCs | **Partial** | Invite challenge to my own designs | None |
| **Team design** | Hiring and onboarding with support (PL3) vs. adapt team structure, cross-function hiring (PL4) | AE hiring panel set-up; shadowing interviews; calibration loop; offered to lead interviews | **Partial** | Lead interviews and debriefs | A hiring loop to own; a new joiner to onboard |
| **Team performance** | High, sustainable team performance; spot underperformance (same at PL3 and PL4) | Not shown | **Not yet (needs reports)** | None | A team |
| **Feedback** | Build a feedback culture; give and seek feedback (same at PL3 and PL4) | 140 PR reviews; RFC comments | **Partial** | Ask for feedback in a structured way | None |
| **Learning** | Steer my own development (PL3) vs. spread learnings and network with other managers (PL4) | Shared with the guild and #group-applied-data; meet-up host | **Partial** | Build a network of PL3 and PL4 leads to learn from | None |
| **People growth** | Support growth plans (PL3) vs. mentor and spot career opportunities (PL4) | Guides shared; no formal mentoring | **Not yet (needs reports)** | Mentor informally now | A mentee, or reports |
| **Attitude** | Lead by example; share failures openly (same at PL3 and PL4) | Owned the "vintage" wording publicly; incident post-mortems | **Partial** | Model a sustainable pace | None |
| **Caring** | Wellbeing of the team (PL3) vs. of my scope, with processes that support it (PL4) | Insights Discovery suggestion; food bank days; public credit to teammates | **Partial** | None beyond pace | A scope of people |
| **External engagement** | Take part in community events (PL3) vs. might raise Vinted's profile (PL4) | Hosted the Berlin dbt meet-up; co-running Vilnius; open-source fix in dbt Labs | **Strong** | None | None |

---

## Part 5: Growth actions

*Three to focus on this quarter; the rest are in the backlog below. Target dates are proposals to agree with António.*

### Focus this quarter

1. **Enable and delegate, rather than do**: *IC: Scope of ownership, Structuring. PL: Prioritisation & time management, People growth*. **Behaviour · Both**
    - **Action:** turn the refresh gate, the snapshot guard and case-log upkeep into team guides. Each month, hand one piece of work to a teammate, with me as reviewer rather than doer.
    - **Done when:** a teammate ships one pattern without my help, and three pieces have shipped this way.
    - **Target:** end of December.
2. **A 6–12 month plan and the business case, with the trade-offs written down**: *IC: Prioritisation, Strategy & roadmap. PL: Planning timespan, Vision & strategy*. **Behaviour · Both**
    - **Action:** write a Q4 2026 – Q2 2027 plan for finance AE topics: close automation, controls, dbt 2.0 and self-service refresh. Give each an owner and a cost. Keep a "doing / not doing" list next to it. Use the plan to write the business case for the role.
    - **Done when:** reviewed with António, and at least one item is cut explicitly each quarter.
    - **Target:** mid-November.
3. **Sustainable pace and clear expectations**: *Acting on the 7 Sep feedback. IC: Time management, Attitude. PL: Prioritisation & time management, Attitude, Caring*. **Behaviour · Both**
    - **Action:** keep to working hours. Give each RFC an estimate and a confidence level. Keep no more than 2 stacked PRs open. Leave incidents that others own to them.
    - **Done when:** there's no late-evening work outside incidents, estimates are hit, and no overlap is flagged in 1:1s.
    - **Target:** from now.

### Backlog

- **Ask for challenge and feedback** (Both): quarterly structured feedback from 3 peers and 2 stakeholders; "what would you change?" in every RFC.
- **Write the standards down** (Both): the test-description and AI-review practices into the repo's standards, and a shared debt list.
- **Write a development plan that picks the track** (Both), after the track decision in the summary.
- **Track impact over time** (IC4): a monthly scorecard, including the adoption numbers marked "to measure" in Part 1.
- **Reduce review overhead** (IC4): fewer, batched sweep PRs; an agreed review cadence for chained PRs.
- **Coach in the open** (PL4): explain patterns in reviews; a monthly AE clinic.
- **Build a manager network** (PL4): 2–3 PL3 or PL4 leads to learn from; a people-management course; lead AE interviews.

### Opportunities to discuss with António

1. **Opportunities the team could offer**: *IC: Scope of ownership, Strategy & roadmap, Collaboration. PL: Team design, Team performance, People growth, Leading projects*. **Opportunity**
    - **Action:** discuss which of these are possible:
        - **Both:** a project with 1–2 contributors that I plan, split and deliver. Candidates are the escrow controls or self-service refresh.
        - **Both:** a seat in finance DSA roadmap planning.
        - **IC4:** a remit for AE quality standards in the domain, and a guild session slot.
        - **IC4:** ownership of a standing agreement with Checkout: a pre-release notice for changes that touch invoices.
        - **PL4:** a mentee, or onboarding buddy for the next AE hire.
        - **PL4:** ownership of the MEC support rotation design, and standing in for António at team rituals.
        - **Both:** whether a business need exists for an IC4 role, or for a PL3 team lead role.
    - **Done when:** at least two are agreed, with owners and dates written into the 1:1 doc.
    - **Target:** next 1:1.

---

## Part 6: Weekly achievement log

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
