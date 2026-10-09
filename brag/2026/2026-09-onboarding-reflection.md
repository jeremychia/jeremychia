# Onboarding period reflection

**Jeremy Chia, Analytics Engineer, Finance DSA**

**Period:** 3 Aug – 28 Sep 2026

## 1. Impact so far

### August close and accuracy

- **Achieved:** Removed €1.45m of double-counted SPEEDX carrier cost before the August close ([#2157](https://github.com/vinted/dataverse-finance/pull/2157)). Ran my first close with Emily, with 94.1% of models on time ([MEC log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32142295207/2026-08+MEC+Issue+Request+Log)). Recovered the 4 Sep double-entry incident in about 20 minutes ([incident](https://vinted.slack.com/archives/C0706RCL6CF/p1788502006663509?thread_ts=1788500547.898079&cid=C0706RCL6CF)).
- **Missed:** An upstream change moved €1.29m of fee accruals out of August, and I found it only after the close. Fixed it from September and froze closed months, so the fix cannot rewrite a reported month ([#2361](https://github.com/vinted/dataverse-finance/pull/2361)). Accounting will decide whether to restate August.
- **Values demonstrated:** *Ownership*, *Aim High* and *Co-create* (warned the upstream owners so other teams could check their own models: [heads-up](https://vinted.slack.com/archives/C077HPXKTSN/p1790104347593269?thread_ts=1787219993.360489&cid=C077HPXKTSN)).

### Fixing problems at the source

- **Achieved:** Traced about 44k invoice lines a month that file the UK as "GB" to core billing, and wrote the fix in their code ([core#137604](https://github.com/vinted/core/pull/137604)). A wrong VAT number had blocked a seller's tax upload for months. Asked Registration how they validate it, and they opened MA-83 to fix it at the source ([thread](https://vinted.slack.com/archives/C046D0K49C6/p1787125459869369)).
- **Missed:** The core fix was still in review at the end of the period, so a temporary mapping covered the gap ([#2378](https://github.com/vinted/dataverse-finance/pull/2378)). It merged on 29 Sep ([core#137777](https://github.com/vinted/core/pull/137777)). There is no agreement yet for Checkout to warn us before releases that touch invoices.
- **Values demonstrated:** *Ownership* and *Co-create*.

### Tools other teams now use

- **Achieved:** Found 121 models across the org close to BigQuery's partition limit, and set up alerts to each owning team ([dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604)). Fixed unit tests that CI silently skipped for two teams ([dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220)). Put VGo and finance on the same rebuild dates for the shipping result ([dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425)).
- **Missed:** Adoption of these tools is not measured yet. My one-snapshot-per-day test went live before the old duplicates were cleaned up, and retries created more. Cleaned them up and changed 13 models so a re-run replaces the day's copy ([FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)).
- **Values demonstrated:** *Aim High* and *Co-create*.

## 2. Learning and feedback applied

- **Work pace (7 Sep 1:1):** António asked why I worked at 10 PM and at weekends, and asked me to leave incidents others own to them. I agree, and I have not fully closed this yet. It is a focus action for this quarter. *[add one concrete example]*
- **Learning from a mistake:** The snapshot test taught me to clean up existing data before enforcing a rule. For the €1.29m fix, I froze closed months first, so the fix could not rewrite a reported month.
- **Reviewers' feedback:** Turned 11 kinds of comment that reviewers kept leaving into automatic review rules, so every PR now gets them ([#2237](https://github.com/vinted/dataverse-finance/pull/2237)).
- **First close:** The retro showed the vouchers export was on the critical path. Automated it and three other exports ([#2178](https://github.com/vinted/dataverse-finance/pull/2178)), and turned three manual checks into tests ([#2203](https://github.com/vinted/dataverse-finance/pull/2203)).
- **1:1 goals (31 Aug):** Proposed 22 escrow revenue controls ([FDSA-3299](https://vinted.atlassian.net/browse/FDSA-3299)) and wrote the core billing fix.
- **Sharing:** Shared my unit-testing guide ([thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787824097864589?thread_ts=1787823910.491879&cid=C03JBPN0Q1W)) and a self-review practice for AI-written PRs ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788853912393169?thread_ts=1787727215.817299&cid=C076F6CME10)).

## 3. Next period

Most of my impact so far is my own output (454 PRs). Next, I want others to do more of this work, at a pace I can keep.

1. **Enable rather than do:** Write guides for the refresh schedule, the snapshot guard and the alert case log. Hand one piece of work a month to a teammate, with me as reviewer. *(Target: end of December)*
2. **Write a 6–12 month plan:** Cover close automation, controls, dbt 2.0 and [self-service data refresh](https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071/2026-09-07+-+Self-service+data+refresh+for+Finance). Give each an owner and a cost, and keep a "not doing" list. *(Target: mid-November)*
3. **Keep a sustainable pace:** Keep to working hours. Give estimates with a confidence level. Keep no more than two chained PRs open.
4. **Measure adoption:** Track how often teams act on the partition alerts, the review rules and the triage bot.

**Support needed:** a project with one or two contributors, a seat in finance DSA roadmap planning, and an agreement for Checkout to warn us before releases that touch invoices.
