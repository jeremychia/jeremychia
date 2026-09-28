# Brag list: 1 Aug – 28 Sep 2026

**Jeremy Chia, Analytics Engineer, Finance DSA.** Written for António Fitas, for our 1:1s.

**Headline:** in eight weeks I kept about €2.7m of cost from being booked in the wrong place (€1.29m of accruals and €1.45m of double-counted carrier cost). I moved four close exports, three manual checks and the shipping refresh into the pipeline. I also built systems other teams now use: org-wide partition monitoring, the finance triage bot's memory, and review rules. And I took fixes upstream myself, into core billing and into an open-source dbt package.

| measure | count |
| --- | --- |
| PRs authored | 454 (424 merged, 12 open) |
| repos I merged into | 15, including [dbt-labs/dbt-external-tables](https://github.com/dbt-labs/dbt-external-tables/pull/412); a 16th, [vinted/core](https://github.com/vinted/core/pull/137604), is open |
| PRs reviewed for others | 140, in 13 repos |
| Jira tickets | 157 updated, 117 closed, 122 raised by me |
| stakeholder requests served | 20 (18 done), 5 of them marked "critical business blocked" |
| RFCs written | 4, plus the alert case log and the August MEC log |
| Confluence review comments | 45 |

Values key: **[aim high] [ownership] [co-create] [care] [grow]**, from [Vinted Values](https://vinted.atlassian.net/wiki/spaces/EKP/pages/29905420289/Vinted+Values). IC levels are from the [Impact & Growth Framework](https://docs.google.com/spreadsheets/d/16_i3t4lxF-niI92dy_E3MbxNdIusJ4bilndOClbwL5Y/edit?gid=955252402#gid=955252402).

---

## 1. Month-end close is right, and less manual

**€1.29m of cost was carried out of August that should have stayed in it.** Fixed, merged ([#2361](https://github.com/vinted/dataverse-finance/pull/2361), [FDSA-3370](https://vinted.atlassian.net/browse/FDSA-3370)).
- **what:** an upstream change stopped cancelled purchases showing as refunded, so the accrual rule moved their fees into September. The status now comes from the payments table. Months already closed stay frozen, and a daily test guards the rule.
- **business:** August and September cost sit in the right month. The fix also picks up 972,439 fee rows a frozen status had missed.
- **above and beyond:** I traced the timeline of the upstream change. I warned its owners in [#payments_dataverse_migration](https://vinted.slack.com/archives/C077HPXKTSN/p1790104347593269?thread_ts=1787219993.360489&cid=C077HPXKTSN) so other consumers can check their own models.
- **values:** [ownership] [aim high] [co-create]

**SPEEDX carrier cost was double-counted against the ledger.** Fixed before the August close ([#2157](https://github.com/vinted/dataverse-finance/pull/2157), [FDSA-3189](https://vinted.atlassian.net/browse/FDSA-3189)).
- **business:** it removes €712k invoiced and €741k accrued carrier cost from August. July had been corrected by hand. Earlier months are unchanged.
- **values:** [aim high]

**Wrong fees stopped before they reached the books.**
- **Adyen rename:** a SECOND_CHARGEBACK rename upstream would have booked about €2,800–3,500 a month as the wrong fee type. I caught it before it merged ([#2244](https://github.com/vinted/dataverse-finance/pull/2244), [FDSA-3317](https://vinted.atlassian.net/browse/FDSA-3317)).
- **AU vendor card:** an accountant had fixed AUD 85,991.59 of fee accrual by hand. I fixed the mapping at source ([#2212](https://github.com/vinted/dataverse-finance/pull/2212), [FDSA-3277](https://vinted.atlassian.net/browse/FDSA-3277)).
- **Negative amounts:** NetSuite rejects negative amounts. I fixed the model the problem was reported on ([#2194](https://github.com/vinted/dataverse-finance/pull/2194)). Then, unasked, I fixed two more models with the same risk ([#2197](https://github.com/vinted/dataverse-finance/pull/2197), [#2198](https://github.com/vinted/dataverse-finance/pull/2198); [FDSA-3256](https://vinted.atlassian.net/browse/FDSA-3256), [FDSA-3262](https://vinted.atlassian.net/browse/FDSA-3262), [FDSA-3263](https://vinted.atlassian.net/browse/FDSA-3263)).
- **values:** [aim high] [ownership]

**Four close exports no longer need a person to run them.**
- **what:** the vouchers accrual, VGo pro wallet and two fee accrual files now export automatically ([#2178](https://github.com/vinted/dataverse-finance/pull/2178), [#2205](https://github.com/vinted/dataverse-finance/pull/2205), [#2207](https://github.com/vinted/dataverse-finance/pull/2207); [FDSA-3234](https://vinted.atlassian.net/browse/FDSA-3234), [FDSA-3267](https://vinted.atlassian.net/browse/FDSA-3267), [FDSA-3268](https://vinted.atlassian.net/browse/FDSA-3268)).
- **manual checks now tests:** three manual fee completeness checks are now dbt tests ([#2203](https://github.com/vinted/dataverse-finance/pull/2203), [FDSA-3260](https://vinted.atlassian.net/browse/FDSA-3260)). They are clean over 237m Adyen, 206m Mangopay and 55m Checkout rows, and they caught all 5 kinds of deliberately broken data.
- **business:** the vouchers step was on the critical path for the 9 AM CET WD1 deadline.
- **values:** [aim high]

**First month-end close, run with Emily.** 94.1% of models were on time ([retro](https://vinted.slack.com/archives/G01A7KGHY74/p1788944254889679), [MEC log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32142295207/2026-08+MEC+Issue+Request+Log)).
- **incident:** I led [the 4 Sep double-entry incident](https://vinted.slack.com/archives/C0706RCL6CF/p1788502006663509?thread_ts=1788500547.898079&cid=C0706RCL6CF) and recovered it in about 20 minutes. It landed 33 seconds past the 09:00 deadline. António: "33 seconds is peanuts, thanks for the fast response" ([4 Sep](https://vinted.slack.com/archives/C0706RCL6CF/p1788506906115249)).
- **values:** [ownership] [co-create]

## 2. Shipping result: one agreed schedule, no hand-run refreshes

**The shipping result now rebuilds itself on the agreed close and actuals dates.** In review: [#2369](https://github.com/vinted/dataverse-finance/pull/2369) and [#2379](https://github.com/vinted/dataverse-finance/pull/2379), [FDSA-3390](https://vinted.atlassian.net/browse/FDSA-3390) and [FDSA-3414](https://vinted.atlassian.net/browse/FDSA-3414).
- **what:** 11 models run daily but only rebuild on the dates in one shared list. On other days they cost 0 bytes.
- **one shared list:** I proposed the list to VGo ([thread](https://vinted.slack.com/archives/C077RK49JP2/p1788938610010669)) and built it across four repos: [dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425), [#432](https://github.com/vinted/dataverse-dbt-shared/pull/432), [vintedgo-dbt#9472](https://github.com/vinted/dataverse-vintedgo-dbt/pull/9472), [terraform-github#8600](https://github.com/vinted/terraform-github/pull/8600), [#8602](https://github.com/vinted/terraform-github/pull/8602) and [#8831](https://github.com/vinted/terraform-github/pull/8831) ([FDSA-3319](https://vinted.atlassian.net/browse/FDSA-3319), [FDSA-3408](https://vinted.atlassian.net/browse/FDSA-3408)).
- **business:** finance control stops asking us for hand-run builds. [FDSA-3388](https://vinted.atlassian.net/browse/FDSA-3388) was the third request since August. Finance and VGo numbers are now built on the same days.
- **technical:** without #432, neither project would have rebuilt on the November and December close days. #8831 unblocked every PR in dataverse-dbt-shared.
- **above and beyond:** this is a cross-team system, agreed with VGo and built in their repos as well as ours.
- **values:** [co-create] [aim high]

**A 1,206-line model became 117 lines, with identical output.** Merged ([#2222](https://github.com/vinted/dataverse-finance/pull/2222), [FDSA-3285](https://vinted.atlassian.net/browse/FDSA-3285), [RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32099795441/2026-08-20+-+Split+mrt_shipping_results+into+components)).
- **what:** split into 2 dimensions, 5 prep models and 2 macros. A full-row hash diff over 4.0bn rows found zero differences.
- **technical:** I used views rather than tables, so the 2.3 TB mart's storage did not double.
- **values:** [aim high]

**Shipping discount campaigns get a governed source, replacing a hand-edited query and sheet.** RFC in review ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762/2026-08-18+-+Governed+mart+for+shipping+discount+campaigns), [FDSA-3090](https://vinted.atlassian.net/browse/FDSA-3090)). Seeds are merged ([#2158](https://github.com/vinted/dataverse-finance/pull/2158), [#2171](https://github.com/vinted/dataverse-finance/pull/2171)) and the models are open ([#2381](https://github.com/vinted/dataverse-finance/pull/2381)).
- **business:** it reconciles to 174 live rows with 0 mismatches, and it found one campaign missing from the manual list. It also explains why one campaign gave two answers a month apart. It sizes the change at cutover (+€17.9k InPost ES, −€8.8k SPS SK) for Finance Control to decide.
- **values:** [aim high] [co-create]

## 3. Controls and data quality: problems found before anyone reported them

**The escrow revenue review only saw under 1% of cases.** In review ([FDSA-3299](https://vinted.atlassian.net/browse/FDSA-3299), [#2300](https://github.com/vinted/dataverse-finance/pull/2300)). This is the 31 Aug 1:1 goal.
- **what:** the monthly review query groups August into 67,443 rows but stops at 500. I proposed 22 controls on the invoice lines that reach the iSAF tax filing, validated over 1.15bn lines.
- **defects found:** 212 lines with VAT off by more than €10 (about €10,700 in total), 43,389 lines coded GB instead of UK, and 4,948 lines on the wrong invoice series.
- **values:** [aim high]

**About 44k invoice lines a month file the UK as a separate country.** I wrote the backend fix myself ([core#137604](https://github.com/vinted/core/pull/137604), open; [FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413), ZS-370).
- **what:** I traced it to three code paths in core billing and opened the fix from a fork, because I have no write access to core. I raised it in #checkout-public. A staging mapping ([#2378](https://github.com/vinted/dataverse-finance/pull/2378)) covers the gap until the fix ships.
- **above and beyond:** this is a fix in another team's Ruby codebase. It is the backend-validation goal from our 31 Aug 1:1, done in practice.
- **values:** [ownership] [co-create]

**A wrong VAT number reached the Lithuanian tax authority.** Fixed at the source ([17 Aug](https://vinted.slack.com/archives/G01A7KGHY74/p1786972417599199?thread_ts=1786690608.841269&cid=G01A7KGHY74), [FDSA-3120](https://vinted.atlassian.net/browse/FDSA-3120), [FDSA-3130](https://vinted.atlassian.net/browse/FDSA-3130)).
- **what:** a 36-character value had blocked a pro seller's tax upload for months. I added a 35-character warning test.
- **above and beyond:** I asked Registration whether they validate the input ([thread](https://vinted.slack.com/archives/C046D0K49C6/p1787125459869369)). They confirmed a regex bug and opened MA-83 to fix Spanish VAT validation at the source.
- **values:** [ownership] [co-create]

**Smaller finds, each with a test behind it.**
- **Compensations:** 8,103 compensations (€121,667) had a case but no coverage split ([FDSA-3328](https://vinted.atlassian.net/browse/FDSA-3328)).
- **Reporting category:** 3,675,013 rows lost their reporting category in one model ([FDSA-3329](https://vinted.atlassian.net/browse/FDSA-3329)).
- **Adyen reconciliation:** the reload window left 39 values null. I found it by comparing the table with its earlier version cell by cell ([#2360](https://github.com/vinted/dataverse-finance/pull/2360), [FDSA-3387](https://vinted.atlassian.net/browse/FDSA-3387)).
- **Double entry:** 473 of about 896m double-entry rows do not net to zero. The three real defects are ticketed ([FDSA-3313](https://vinted.atlassian.net/browse/FDSA-3313)).
- **CDC gaps:** added gap checks to the AU and US invoice extras. The checks name the owner and find exactly the empty hour of incident 6593 ([#2382](https://github.com/vinted/dataverse-finance/pull/2382), [FDSA-3417](https://vinted.atlassian.net/browse/FDSA-3417)).
- **values:** [aim high]

## 4. Incidents I led and cleaned up at the root

**A duplicate snapshot put a €1.5m jump into Looker.** Fixed at the root ([FDSA-3302](https://vinted.atlassian.net/browse/FDSA-3302), [FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318), [FDSA-3330](https://vinted.atlassian.net/browse/FDSA-3330), [FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)).
- **what:** a re-run on 2 Sep made Vinted UAB payment fees look €1.5m too high. Reported figures were unaffected. The first ticket listed 6 duplicates. I scanned all 18 snapshot tables and found 34 in 10 models, going back to March 2025.
- **fix:** I cleaned them up ([#2288–#2297](https://github.com/vinted/dataverse-finance/pull/2288)) and added a one-snapshot-per-day test ([#2232](https://github.com/vinted/dataverse-finance/pull/2232)). 13 models now replace a same-day re-run instead of adding a copy.
- **values:** [ownership] [aim high]

**Other incidents.**
- **Mangopay:** the S3 listing silently stopped at 1,000 files, so a July close retry skipped the month's files ([#2064](https://github.com/vinted/dataverse-finance/pull/2064), [#2065](https://github.com/vinted/dataverse-finance/pull/2065), [FDSA-3067](https://vinted.atlassian.net/browse/FDSA-3067)).
- **Adyen fees:** the fees model failed on memory at 156 slot-hours with 3.34 TiB spilled. It now runs in 17.2 slot-hours with no spill ([#2175](https://github.com/vinted/dataverse-finance/pull/2175), [FDSA-3206](https://vinted.atlassian.net/browse/FDSA-3206)).
- **CDD queue:** I found the CDD pipeline paused with 58 merges queued and never run ([#2308](https://github.com/vinted/dataverse-finance/pull/2308), [FDSA-3332](https://vinted.atlassian.net/browse/FDSA-3332)).
- **values:** [ownership]

## 5. Systems other teams now use

**Partition-limit monitoring for every team.** Merged ([dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604), [#606](https://github.com/vinted/dataverse-metrics/pull/606), [FDSA-3169](https://vinted.atlassian.net/browse/FDSA-3169)).
- **what:** an incident elsewhere failed 20 downstream tasks. I checked every table and found 121 at-risk models org-wide. One table had about 78 hours of headroom. Alerts now go to each owning team.
- **recognition:** Oscar Ligthart called it "a great idea" ([#analytics-engineering](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787641108570719)).
- **values:** [aim high] [co-create]

**The finance alert-triage bot.** Phases 1–4 are done ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441/2026-08-24+-+Continuity+for+alert+triage), [case log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32104972550/Finance+DSA+Alert+Case+Log), [FDSA-3160](https://vinted.atlassian.net/browse/FDSA-3160)–[3165](https://vinted.atlassian.net/browse/FDSA-3165)). Ten v-assist-registry PRs, including [#846](https://github.com/vinted/v-assist-registry/pull/846), [#851](https://github.com/vinted/v-assist-registry/pull/851), [#886](https://github.com/vinted/v-assist-registry/pull/886) and [#951](https://github.com/vinted/v-assist-registry/pull/951).
- **what:** replies now name the failing value and say whether the data or the test is at fault. The bot reads a case log the team curates, and it posts a nightly handover. About 18.5 hours of lag are gone from the daily report.
- **above and beyond:** I shared the lessons with [#group-applied-data](https://vinted.slack.com/archives/C082FD8K05B/p1787812514645189?thread_ts=1787757309.592049&cid=C082FD8K05B).
- **values:** [aim high] [co-create]

**Review rules taken from real review comments.** ([#1817](https://github.com/vinted/dataverse-finance/pull/1817), [#2237](https://github.com/vinted/dataverse-finance/pull/2237), [FDSA-3307](https://vinted.atlassian.net/browse/FDSA-3307))
- **what:** 11 kinds of human review comment became Bugbot rules. One of the cases behind them would have blanked 437,042 rows.
- **above and beyond:** I co-started [#dsa-ae-bugbot-review](https://vinted.slack.com/archives/C0BUP5UA8G2/p1788420922343509) with Julien Varin to scale it across Dataverse.
- **values:** [co-create] [grow]

**Self-service data refresh for Finance.** RFC ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071/2026-09-07+-+Self-service+data+refresh+for+Finance), [thread](https://vinted.slack.com/archives/C076F6CME10/p1788771497947879))
- **what:** I analysed all 1,255 FDSA tickets. There were 78 ad-hoc refresh requests, with a 4.6 h median wait and a p90 of about 4 days. The RFC proposes a Slack `/trigger` for named finance jobs.
- **business:** it estimates about 500 finance hours a year unblocked and 9–11 engineer-days saved. Júlia: "the data makes a super clear case".
- **values:** [aim high] [co-create]

## 6. Code standards and dbt 2.0 readiness

**Deprecation and lint sweeps.** 173 dbt deprecation PRs and 75 M017 lint PRs, with all 930 tests resolving identically before and after ([FDSA-3281](https://vinted.atlassian.net/browse/FDSA-3281), [#2217](https://github.com/vinted/dataverse-finance/pull/2217), [lint drive](https://vinted.slack.com/archives/C076F6CME10/p1787583981544379)).
- **technical:** one warning type went from 103 to 65 and another from 13 to 0.
- **values:** [aim high]

**51 unit-test PRs.** They landed before the M008 rule becomes an error on 1 October ([FDSA-3153](https://vinted.atlassian.net/browse/FDSA-3153)).
- **found:** unit tests were silently not running in CI, in finance and in dataverse-people. CI gathered 2 tests instead of 6.
- **fixed:** [dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220), [dataverse-vunit#120](https://github.com/vinted/dataverse-vunit/pull/120) and [#2298](https://github.com/vinted/dataverse-finance/pull/2298). I added a new org-wide linter rule, C006 ([dataverse-cli#705](https://github.com/vinted/dataverse-cli/pull/705)).
- **values:** [aim high]

**dbt 2.0 blockers cleared across repos.**
- **unit test files:** the custom unit-test key is a hard error in dbt 2.0, so I moved the test files out of dbt's parse path in 3 repos ([FDSA-3320](https://vinted.atlassian.net/browse/FDSA-3320), [thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1788515249278649?thread_ts=1787823910.491879&cid=C03JBPN0Q1W)).
- **Looker measures:** they would have silently disappeared under the new meta format ([lookml-generator#160](https://github.com/vinted/dataverse-lookml-generator/pull/160)).
- **linter:** following one linter false positive would have broken a GDPR deletion filter ([dataverse-cli#700](https://github.com/vinted/dataverse-cli/pull/700)).
- **dbt-core:** I filed issues #16179 and #16180 after diagnosing the dbt 1.12 CI break ([thread](https://vinted.slack.com/archives/C059T9KAF8X/p1788423995537369)).
- **values:** [aim high] [co-create]

**An open-source contribution to dbt Labs.** Merged 24 Sep ([dbt-labs/dbt-external-tables#412](https://github.com/dbt-labs/dbt-external-tables/pull/412)).
- **what:** dbt-autofix flagged a duplicate YAML key in the package's Synapse sample. I split the example into its own table so both examples stay valid.
- **above and beyond:** this is an upstream fix to a package the whole dbt community uses, on the path to dbt 2.0.
- **values:** [co-create] [grow]

**Tech debt paid down.**
- **refactors:** `mrt_double_entry` went from 837 lines to 88, byte-identical over 13.18bn rows ([#2209](https://github.com/vinted/dataverse-finance/pull/2209), [FDSA-3274](https://vinted.atlassian.net/browse/FDSA-3274)).
- **retired:** a model with no queries in 90 days ([#2213](https://github.com/vinted/dataverse-finance/pull/2213), [FDSA-3278](https://vinted.atlassian.net/browse/FDSA-3278)).
- **scoped:** laptop tooling differs from CI on 94 of 182 packages ([FDSA-3409](https://vinted.atlassian.net/browse/FDSA-3409)).
- **values:** [aim high]

## 7. Platform and migration

**Continuous deployment turned on for finance** ([#2153](https://github.com/vinted/dataverse-finance/pull/2153), [#2154](https://github.com/vinted/dataverse-finance/pull/2154), [#2176](https://github.com/vinted/dataverse-finance/pull/2176), [FDSA-3190](https://vinted.atlassian.net/browse/FDSA-3190)).
- **what:** I cleared three blockers with DPX. 127 of 308 models are excluded from rebuilding on merge. One of them would have written Austrian taxpayer personal data to the prod bucket on any build.
- **recognition:** Júlia called it a "game changer" ([thread](https://vinted.slack.com/archives/C076F6CME10/p1789465411298849)).
- **values:** [aim high] [co-create]

**Export buckets moved off the legacy project** ([terraform-dataverse#3723](https://github.com/vinted/terraform-dataverse/pull/3723), [oss-platform-service#71](https://github.com/vinted/oss-platform-service/pull/71), [#2234](https://github.com/vinted/dataverse-finance/pull/2234), [FDSA-3149](https://vinted.atlassian.net/browse/FDSA-3149), [FDSA-3194](https://vinted.atlassian.net/browse/FDSA-3194), [FDSA-3291](https://vinted.atlassian.net/browse/FDSA-3291)).
- **found:** stage had been reading the prod iSAF bucket.
- **communication:** I warned [#isaf](https://vinted.slack.com/archives/C02A97Z59L2/p1788768336716279) and [#pigment_support](https://vinted.slack.com/archives/C08QS2MLS2U/p1788860282653919). I held the merge until after the close, and notified 10 sandbox users.
- **lineage:** 24 export models now show their consumers across iSAF, Austrian tax, Sovos, NetSuite and Pigment ([#2235](https://github.com/vinted/dataverse-finance/pull/2235), [FDSA-3306](https://vinted.atlassian.net/browse/FDSA-3306)).
- **values:** [ownership] [co-create]

## 8. Team, community and hiring

- **Berlin dbt meet-up:** I hosted it on 10 Sep, for about 60 guests. I moderated the AE career panel and promoted our open roles. António: the round table was "very well conducted" ([recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289), [António](https://vinted.slack.com/archives/C076F6CME10/p1789104603255589)). I am co-organising a Vilnius meet-up for mid-October ([thread](https://vinted.slack.com/archives/C076F6CME10/p1787561169076779?thread_ts=1786355397.086789&cid=C076F6CME10)). **[co-create] [grow]**
- **AE hiring panel:** I set up the group and its access ([service-catalog#17023](https://github.com/vinted/service-catalog/pull/17023), [terraform-github#8562](https://github.com/vinted/terraform-github/pull/8562)). I shadow interviews, join the calibration loop, and offered to lead interviews ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788425573475809?thread_ts=1788425500.516319&cid=C076F6CME10)). **[co-create] [grow]**
- **Reviews:** I reviewed 140 PRs, 103 of them in finance (Emily 41, Júlia 27, Samanta 21). Samanta called a detailed review "real-mvp". **[co-create]**
- **Shared practices:** I shared the unit-testing guide ([thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787824097864589?thread_ts=1787823910.491879&cid=C03JBPN0Q1W)) and a self-review practice for AI-written PRs ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788853912393169?thread_ts=1787727215.817299&cid=C076F6CME10)). I proposed that test descriptions state the rule and what to do on failure ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788770645634999?thread_ts=1788769943.200799&cid=C076F6CME10)). **[co-create] [grow]**
- **Care:** I organised Berliner Tafel food bank volunteering days ([thread](https://vinted.slack.com/archives/C04HC4J6X2R/p1786958374428139)). I credited Emily's export automation in public ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788364525194939)), and suggested an Insights Discovery retake before the offsite. **[care]**

## 9. Strategy and influence beyond finance

- **RFC reviews:** I left 45 review comments. They include the [Tier 1 Reliability Review](https://vinted.atlassian.net/wiki/spaces/DF/pages/32046055735/2026+Q3+-+Tier+1+Reliability+Review) (shift testing left) and [Tier 0 P&L scope](https://vinted.atlassian.net/wiki/spaces/DF/pages/32120244315/2026-08-26+Increasing+Tier+0+Scope+to+P+L+Financial+Metrics). On [Tier 0 Data Assets](https://vinted.atlassian.net/wiki/spaces/DF/pages/32202654020/2026+Q3+-+Tier+0+Data+Assets+-+what+it+means+for+your+team) I proposed a policy gate as an AE roadmap item. On [Recovering failed DAG runs](https://vinted.atlassian.net/wiki/spaces/DPV2/pages/32026985454/2026-09-22+Recovering+consecutive+failed+DAG+runs) I asked for a minimum lookback rather than a default.
- **CDD for the org:** I asked for CDD to cover SQL changes only, to allow a per-PR opt-out, and to show a plan first ([thread](https://vinted.slack.com/archives/C02JMNFS9GD/p1787656910916349?thread_ts=1787653801.646929&cid=C02JMNFS9GD)).
- **Ownership of cross-domain changes:** I argued that a team making one should own the downstream PRs ([thread](https://vinted.slack.com/archives/C076F6CME10/p1787738141452099?thread_ts=1787736956.482569&cid=C076F6CME10)).
- **BI tooling:** I opened a discussion on moving off Looker, now that our measures live in yml. I volunteered for the 2027 BI discovery and POC.
- **Audit:** I proposed tagging tests by accounting assertion, so audit walkthroughs can see what each test proves (ISA 315).
- **values:** [co-create] [aim high]

---

## How this maps to IC3 and IC4

The framework is additive: IC4 is a technical lead who resolves challenges at the level of the area or domain, and enables other AEs to do the same. IC3 is craft mastery on my own work.

| dimension | IC3: my own work | IC4: enabling others, beyond my scope |
| --- | --- | --- |
| **Theory & techniques** | designed the shipping split, the gated rebuild and the campaign mart myself (sections 1–2) | the shared refresh-date pattern is used by VGo too; the unit-test and dbt 2.0 moves span 3 repos |
| **Engineering** | three refactors with zero output change (1,206→117, 837→88, 4.0bn and 13.18bn rows); a slot-hours fix from query plans (156→17.2) | Bugbot rules and new linter rule C006 set standards for others; linter and lookml-generator fixes protect every repo |
| **Quality standards** | every fix ships with a test; 51 unit-test PRs | found CI silently skipping tests for two teams and fixed it for all; test-description and AI-review practices shared |
| **Data mastery** | traced defects from core billing Ruby, through CDC, to the tax filing (GB/UK, VAT length, payment status) | partition-risk audit across all 337 tables org-wide |
| **Impact measurement** | quote the € and row effect on every fix; the refresh RFC measured wait time from 1,255 tickets | lint severity metric ([metrics#632](https://github.com/vinted/dataverse-metrics/pull/632)); fixed the org reliability mart ([#630](https://github.com/vinted/dataverse-metrics/pull/630)) |
| **Structuring** | stacked PRs, phased RFCs (the triage bot in 4 phases) | split sweeps into ~11 PRs per reviewer so the team could share the review load |
| **Strategy & roadmap** | escrow controls and backend validation goals delivered | policy gate on the AE roadmap; CDD and BI-tool proposals to the guild |
| **Scope of ownership** | the €1.29m fix and the duplicate snapshots, from detection to root cause | owned a fix in core, and built monitoring that pages other teams |
| **Technical debt** | 173 deprecation and 75 lint PRs; FDSA-3409 tooling drift | dbt 2.0 blockers cleared in shared repos and upstream in dbt Labs |
| **Business understanding** | knew a refunded purchase is never invoiced, which exposed the €1.29m shift | anticipated November and December close dates for two projects |
| **Collaboration** | 20 stakeholder requests; the close with Emily | cross-team work with VGo, checkout, Registration, DPX, Payments and iSAF |
| **Communication** | plain-language PRs and RFCs with € impact up front | led incident comms and upstream heads-ups; hosted a 60-person meet-up |
| **Knowledge leadership** | MEC log, case log, runbooks | meet-up host; lessons shared with the guild and #group-applied-data |
| **Helping others** | 140 PR reviews; AE hiring panel | set up the hiring panel's infrastructure |

**Honest gaps against IC4:**
- **enabling, not doing:** most of the impact is still my own output (454 PRs). IC4 asks me to *enable* other AEs to do this work. The next step is to turn patterns (the refresh gate, snapshot guards, the case log) into skills or guides that teammates apply without me.
- **prioritisation:** the lint and unit-test sweeps were high volume. IC4 asks me to prioritise the most systemic problems. I can show that by cutting scope explicitly, and by saying what I chose not to do.
- **working hours:** from the 7 Sep 1:1. Some of this landed late in the evening. A sustainable pace is part of the "attitude" and "caring" rows too.

## Reflections (draft for me to finish)

- **went well:** the biggest finds came from checking my own work (a table compared with its earlier version, a snapshot scan), not from alerts.
- **issue:** other teams' upstream changes caused most of the breakage: the payment status change, GB from core, the Adyen rename and the partition limits. Each cost days after the fact. Could finance get into those teams' release process earlier?
- **issue:** my PRs stack up waiting for review (#2369 blocks #2379 and #2381). Could we agree a review cadence for chained PRs?
- **thought:** the AE community is converging on shared skills and standards. Finance can shape them instead of adopting what others decide.

---

<details>
<summary>How this was compiled</summary>

- **GitHub:** `gh search prs --author=@me` and `--reviewed-by=@me`, created 2026-08-01..2026-09-28, split by date to get past the 200-result cap. The raw lists are in [sources/gh_prs.tsv](sources/gh_prs.tsv) and [sources/gh_reviews.tsv](sources/gh_reviews.tsv).
- **Jira:** `(assignee = currentUser() OR reporter = currentUser()) AND updated >= "2026-08-01"`. The raw list is in [sources/jira_tickets.tsv](sources/jira_tickets.tsv).
- **Confluence:** created and edited pages, plus comments. See [sources/confluence_slack_summary.md](sources/confluence_slack_summary.md).
- **Slack:** public and private channels only, never DMs. 15 Aug – 11 Sep and 21–28 Sep were read in full ([15–28 Aug](sources/slack_2026-08-15_to_2026-08-28.md), [29 Aug – 11 Sep](sources/slack_2026-08-29_to_2026-09-11.md)). 1–14 Aug and 12–20 Sep came only from targeted searches.
- **Figures:** every figure is quoted from a PR body, ticket description or page, never inferred from a title.

</details>
