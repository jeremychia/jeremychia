# Onboarding period reflection

**Jeremy Chia, Analytics Engineer, Finance DSA**

**Period:** 3 Aug – 30 Sep 2026

## 1. Impact so far

Most of finance's data errors in this period started at a boundary with another team's system. I worked on them at three levels. First, fix the number before it reaches the books. Second, add a control that catches the whole class of error. Third, move the fix to the team that owns the source. I chose which problems to take on by how systemic they were, not by the order they were reported.

### Close accuracy: controlling how the numbers are produced

- **Achieved:** Removed €1.45m of double-counted SPEEDX carrier cost before the August close ([#2157](https://github.com/vinted/dataverse-finance/pull/2157)). Fixed blank voucher provisions before the September close ([#2408](https://github.com/vinted/dataverse-finance/pull/2408)). Gave finance two options with their impact on each month, and recommended the one that left August as filed ([options](https://vinted.slack.com/archives/G01A7KGHY74/p1790687441708849?thread_ts=1790687343.956889&cid=G01A7KGHY74)). Scanned all 18 snapshot tables, not just the 6 duplicates in the ticket, and found 34 in 10 models ([FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318)). Built 25 checks on the invoice lines that reach the iSAF tax filing, the escrow revenue goal from our 31 Aug 1:1. The monthly review they back had seen under 1% of cases, because its query stopped at 500 of 67,443 rows. Each check is grouped by the audit assertion it tests, so auditors can see what it proves ([#2300](https://github.com/vinted/dataverse-finance/pull/2300), merged 7 Oct).
- **Missed:** An upstream change moved €1.29m of fee accruals out of August, and I found it only after the close. Fixed it from September and froze closed months, so no fix can rewrite a reported month ([#2361](https://github.com/vinted/dataverse-finance/pull/2361)). Accounting will decide whether to restate August.
- **Values demonstrated:** *Aim High* and *Ownership*. I credited Emily's live month-to-date view for catching the voucher gap (*Co-create*: [thread](https://vinted.slack.com/archives/G01A7KGHY74/p1790689923664639?thread_ts=1790687343.956889&cid=G01A7KGHY74)).

### The boundary with upstream teams

- **Achieved:** Traced about 44k invoice lines a month that file the UK as "GB" to core billing. Wrote the fix in their code, and it merged on 29 Sep ([core#137777](https://github.com/vinted/core/pull/137777)). Asked Registration how they validate VAT numbers after a wrong one blocked a seller's tax upload, and they opened MA-83 to fix it at the source ([thread](https://vinted.slack.com/archives/C046D0K49C6/p1787125459869369)). Caught an Adyen rename before it booked €2.8–3.5k a month as the wrong fee type ([#2244](https://github.com/vinted/dataverse-finance/pull/2244)). Made every CDC completeness check name its owning team and where to ask ([#2382](https://github.com/vinted/dataverse-finance/pull/2382)). Stopped two privacy risks before they shipped: a model that would have written Austrian taxpayers' personal data to the prod bucket ([#2153](https://github.com/vinted/dataverse-finance/pull/2153)), and a linter change that would have broken a GDPR deletion filter ([dataverse-cli#700](https://github.com/vinted/dataverse-cli/pull/700)). Across the period, I drove this work with checkout, Registration, payments, VGo, DPX and iSAF.
- **Missed:** Each of these was found after the upstream change had shipped. There is still no agreement for Checkout to warn finance before releases that touch invoices. The system is safer, but it still reacts.
- **Values demonstrated:** *Ownership* and *Co-create* (warned the payments owners about the €1.29m change, so other consumers could check their models: [heads-up](https://vinted.slack.com/archives/C077HPXKTSN/p1790104347593269?thread_ts=1787219993.360489&cid=C077HPXKTSN)).

### Standards and tools that work without me

- **Achieved:** Found 121 models across the org close to BigQuery's partition limit. From 30 Sep, each owning team gets its own alert ([dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604), [#678](https://github.com/vinted/dataverse-metrics/pull/678)). Fixed unit tests that CI silently skipped for two teams, and added a linter rule for every dataverse repo ([dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220), [dataverse-cli#705](https://github.com/vinted/dataverse-cli/pull/705)). Turned 11 kinds of review comment into automatic review rules, so the team's standards are checked on every PR ([#2237](https://github.com/vinted/dataverse-finance/pull/2237)). Put VGo and finance on one shared list of rebuild dates ([dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425)). Turned on continuous deployment for finance with DPX, so every merge now builds itself ([#2154](https://github.com/vinted/dataverse-finance/pull/2154)). Gave the on-support rotation a triage bot that names the failing value and reads a case log the team keeps ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441/2026-08-24+-+Continuity+for+alert+triage)). Measured the cost of hand-run refreshes from all 1,255 FDSA tickets, and proposed a self-service route ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071/2026-09-07+-+Self-service+data+refresh+for+Finance)).
- **Missed:** Adoption is not measured yet. I reviewed 140 PRs for others, but most of this is still my own output, over 450 PRs. The next step is for other analytics engineers to apply these patterns without me. My one-snapshot-per-day test also went live before the old duplicates were cleaned up, and retries created more. I cleaned them up and changed 13 models so a re-run replaces the day's copy ([FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)).
- **Values demonstrated:** *Aim High* and *Co-create*. Júlia on the self-service RFC: "the data makes a super clear case" ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788771497947879)).

### Also on record

- **Code quality:** Split the two largest finance models into parts others can read and test (1,206 → 117 and 837 → 88 lines), with identical output over 4.0bn and 13.18bn rows ([#2222](https://github.com/vinted/dataverse-finance/pull/2222), [#2209](https://github.com/vinted/dataverse-finance/pull/2209)).
- **Shared tooling:** Stopped Looker measures disappearing in every repo under dbt's new format ([lookml-generator#160](https://github.com/vinted/dataverse-lookml-generator/pull/160)). Fixed a dbt Labs package on the path to dbt 2.0 ([dbt-external-tables#412](https://github.com/dbt-labs/dbt-external-tables/pull/412)).
- **Cost:** Rewrote the Adyen fees model after it ran out of memory, from 156 to 17.2 slot-hours a day ([#2175](https://github.com/vinted/dataverse-finance/pull/2175)).
- **Influence beyond finance:** Reviewed other teams' RFCs, including the [Tier 0 P&L scope](https://vinted.atlassian.net/wiki/spaces/DF/pages/32120244315/2026-08-26+Increasing+Tier+0+Scope+to+P+L+Financial+Metrics) and the [Tier 1 reliability review](https://vinted.atlassian.net/wiki/spaces/DF/pages/32046055735/2026+Q3+-+Tier+1+Reliability+Review). Proposed a policy gate for the AE roadmap.

## 2. Learning and feedback applied

- **Work pace (7 Sep 1:1):** António asked why I worked at 10 PM and at weekends, and asked me to leave incidents others own to them. The pace I keep sets the pace others think is expected, so I want to model a sustainable one. I have not fully closed this yet, and it is a focus action for this quarter. *[add one concrete example]*
- **Sharing a failure:** The snapshot test taught me to clean up existing data before enforcing a rule. I recorded the cause and the fix in the tickets ([FDSA-3330](https://vinted.atlassian.net/browse/FDSA-3330), [FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)), and I include it here for the same reason. For the €1.29m fix, I froze closed months first, so the fix could not rewrite a reported month.
- **Feedback into the system:** Reviewers kept leaving the same 11 kinds of comment. I turned them into rules, so every PR now gets that feedback, and I co-started a channel to bring the approach to the rest of Dataverse ([#dsa-ae-bugbot-review](https://vinted.slack.com/archives/C0BUP5UA8G2/p1788420922343509)).
- **First close:** The retro with Emily showed the vouchers export was on the critical path for the 9 AM deadline. I automated it and three other exports ([#2178](https://github.com/vinted/dataverse-finance/pull/2178)), and turned three manual checks into tests ([#2203](https://github.com/vinted/dataverse-finance/pull/2203)).
- **1:1 goals (31 Aug):** I turned both goals into delivered work: the escrow controls and the core billing fix.
- **Knowledge leadership:** Shared my unit-testing guide with the AE community ([thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787824097864589?thread_ts=1787823910.491879&cid=C03JBPN0Q1W)) and a self-review practice for AI-written PRs ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788853912393169?thread_ts=1787727215.817299&cid=C076F6CME10)). Hosted the Berlin dbt meet-up for about 60 guests and moderated its AE career panel, which raised Vinted's profile with the data community ([recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289)).

## 3. Next period

In this period I mostly delivered the work myself. Next, I want to own the long-term quality of finance's analytics engineering: others deliver more of it, I plan further ahead, and I keep a pace the team can copy.

1. **Enable rather than do:** Write guides for the refresh schedule, the snapshot guard and the alert case log. Hand one piece of work a month to a teammate, with me as reviewer. *(Target: end of December)*
2. **Write a plan for the next 12 months:** Turn the domain's direction into a plan for close automation, controls, dbt 2.0 and self-service refresh. Give each item an owner and a cost, and keep a "not doing" list so trade-offs on debt are made on purpose. *(Target: mid-November)*
3. **Move finance earlier into upstream releases:** Agree with Checkout that finance hears about invoice changes before they ship. This turns the boundary work in section 1 from reacting to preventing. *(Target: end of Q4)*
4. **Keep a sustainable pace:** Keep to working hours. Give delivery estimates with a confidence level. Keep no more than two chained PRs open.
5. **Measure adoption:** Track how often teams act on the partition alerts, the review rules and the triage bot, so the impact of each system is visible.

**Support needed:**
- a project with one or two contributors that I plan and split
- a seat in finance DSA roadmap planning
- a sponsor for the Checkout release agreement
