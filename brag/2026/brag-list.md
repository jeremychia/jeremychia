# Brag list: 2026

**Jeremy Chia, Analytics Engineer, Finance DSA.** Written for António Fitas, for our 1:1s. Newest period first.

Values key: **[aim high] [ownership] [co-create] [care] [grow]**, from [Vinted Values](https://vinted.atlassian.net/wiki/spaces/EKP/pages/29905420289/Vinted+Values). IC levels are from the [Impact & Growth Framework](https://docs.google.com/spreadsheets/d/16_i3t4lxF-niI92dy_E3MbxNdIusJ4bilndOClbwL5Y/edit?gid=955252402#gid=955252402).

---

## 29 Sep – 9 Oct 2026

**Headline:** the September close ran with three money errors caught in the data. I fixed voucher provisions before the close, so August needed no restatement. I found €33.9k of Adyen payout fees booked to the wrong account. The partition alerts now reach every owning team. Financial planning has a payment provider split that matches Pigment exactly. The escrow controls from our 31 Aug 1:1 merged, and so did the core billing fix.

| measure | count |
| --- | --- |
| PRs authored | 78 (43 merged, 22 open), plus 15 older PRs merged in the window |
| repos | 15, including an open PR to [apache/airflow](https://github.com/apache/airflow/pull/74338) |
| PRs reviewed for others | 40 (Júlia 16, Vedashree 9, Emily 5, Paulius 5) |
| Jira tickets | 147 updated |
| RFCs written or updated | 3 |


---

### 1. September close

**Voucher provisions came out blank in August and September.** Fixed before the close ([#2408](https://github.com/vinted/dataverse-finance/pull/2408), [FDSA-3459](https://vinted.atlassian.net/browse/FDSA-3459)).
- **what:** the accrual took the rate group and the 500-voucher count from two different countries. Both now use the country the voucher is booked under.
- **business:** I gave finance two options. Option 1 added €7,123 to August and €8,861 to September. Option 2 added €7 and €2,301. I recommended option 2, and finance did not need to restate August ([options](https://vinted.slack.com/archives/G01A7KGHY74/p1790687441708849?thread_ts=1790687343.956889&cid=G01A7KGHY74)).
- **credit:** Emily's live month-to-date view caught it, and I said so in the thread ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1790689923664639?thread_ts=1790687343.956889&cid=G01A7KGHY74)).
- **values:** [aim high] [co-create]

**€33.9k of Adyen payout fees were booked to 700007 instead of 700006.** Found, and the fix is in review ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1791267423699489?thread_ts=1791264406.708729&cid=G01A7KGHY74), [FDSA-3542](https://vinted.atlassian.net/browse/FDSA-3542)).
- **what:** I traced it to the identity-check estimate. It estimated 70,396 checks, and Adyen billed 5,616. 93% of those sellers were already on Vinted Pay.
- **above and beyond:** I raised it with payments, since the estimate is theirs ([ticket thread](https://vinted.slack.com/archives/C04QY983L5C/p1791277456617379?thread_ts=1791277456.617379&cid=C04QY983L5C)).
- **values:** [aim high] [co-create]

**Accounting no longer splits Adyen payouts by country by hand.** From the September file, the payout fees (700006) are split by country ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1790950498218939?thread_ts=1786610159.001499&cid=G01A7KGHY74)).
- **values:** [aim high]

**A miss I owned: the September Adyen fee snapshot had every fee unscaled.** Fixed the same day ([#2464](https://github.com/vinted/dataverse-finance/pull/2464)).
- **what:** an earlier change moved three Adyen fee models to the daily run but missed the fourth. It still held August invoices, so none of the 328,933,345 September rows matched an invoice. I deleted the bad snapshot, scheduled the model daily and reran the close chain.
- **ownership:** I explained the cause in the team channel and apologised ([thread](https://vinted.slack.com/archives/C076F6CME10/p1790947776366779?thread_ts=1790947520.071299&cid=C076F6CME10)).
- **values:** [ownership]

**Other close fixes.**
- **Exchange rates:** on the 1st of the month, before the ECB publishes, EUR had no rate. 14 models read that table. EUR now gets a rate of 1 for the open month, and the vouchers accrual carries the last rate forward ([#2444](https://github.com/vinted/dataverse-finance/pull/2444), [#2425](https://github.com/vinted/dataverse-finance/pull/2425)).
- **Vinted Pay:** money moved by hand on 29 Sep showed as 5 "unknown" rows in Looker. They now book as manual transfers, and any new unknown movement warns ([#2435](https://github.com/vinted/dataverse-finance/pull/2435)).
- **Vinted Go point of sale:** Portugal went live on 26 Sep. Its first invoice would have entered the Adyen reconciliation. Every point-of-sale account is now handled without a code change ([#2410](https://github.com/vinted/dataverse-finance/pull/2410)).
- **Invoice lines:** Vinted Pay closes on WD1, but invoice lines were snapshotted on WD2 only. Double entry now gets a WD1 snapshot ([#2498](https://github.com/vinted/dataverse-finance/pull/2498)).
- **NetSuite currencies:** NetSuite rejected 71 of 3,030 invoices on WD2 because customers lacked a currency. I set out three options, António backed option 2, and the check is open ([thread](https://vinted.slack.com/archives/C09A63VS421/p1790933676957659?thread_ts=1790933676.957659&cid=C09A63VS421), [isaf-oss-tool-service#183](https://github.com/vinted/isaf-oss-tool-service/pull/183)).
- **MEC log:** co-wrote the September issue log with Júlia ([MEC log](https://vinted.atlassian.net/wiki/spaces/DF/pages/32294830083)).
- **values:** [aim high] [ownership] [co-create]

### 2. Standing goals from our 1:1s

**The escrow revenue controls merged** (31 Aug goal) ([#2300](https://github.com/vinted/dataverse-finance/pull/2300), [FDSA-3299](https://vinted.atlassian.net/browse/FDSA-3299)).
- **what:** 25 new checks on the invoice lines that reach the iSAF tax filing. The six that catch a duplicated line fail the build once duplicates could pass the €1,000 clearly trivial threshold. The rest warn.
- **business:** many of these replace fields Evita checks by hand in her monthly Looker review.
- **values:** [aim high]

**The core billing fix for GB instead of UK merged** (31 Aug goal) ([core#137777](https://github.com/vinted/core/pull/137777), [FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413)).
- **business:** about 44k invoice lines a month stop filing the UK as a separate country.
- **above and beyond:** a fix in checkout's Ruby codebase.
- **values:** [ownership] [co-create]

### 3. New data for finance

**Financial planning can see each payment provider's share of transactions.** Merged ([#2485](https://github.com/vinted/dataverse-finance/pull/2485), [groupfunctions-looker#2077](https://github.com/vinted/dataverse-groupfunctions-looker/pull/2077), [FDSA-3392](https://vinted.atlassian.net/browse/FDSA-3392)).
- **what:** a new mart and Looker dashboard split transactions and paid-feature orders by provider, per seller country.
- **business:** financial planning uses the shares to forecast payment processing cost. The totals match Pigment exactly for May to September 2026. The card-provider shares match their sheet for all 27 countries in August ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1791466380169449?thread_ts=1790148016.670809&cid=G01A7KGHY74)).
- **governance:** I kept the new metrics in their own mart, so FP&A's governed metrics stay untouched. Daniel Arango: "That works, thanks!" ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1791451996400679?thread_ts=1790148016.670809&cid=G01A7KGHY74)).
- **recognition:** Tomas Radavičius: "thank you! :mvp:" ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1791466948373199?thread_ts=1790148016.670809&cid=G01A7KGHY74)).
- **values:** [aim high] [co-create]

**The shipping campaign definitions merged.** The campaign application and the switch from the sheet are open ([#2381](https://github.com/vinted/dataverse-finance/pull/2381), [#2471](https://github.com/vinted/dataverse-finance/pull/2471), [#2496](https://github.com/vinted/dataverse-finance/pull/2496), [FDSA-3176](https://vinted.atlassian.net/browse/FDSA-3176)).
- **values:** [aim high]

**US tax reconciliation: the Xendo feed stopped breaking.** Merged ([#2479](https://github.com/vinted/dataverse-finance/pull/2479), [#2480](https://github.com/vinted/dataverse-finance/pull/2480), [#2481](https://github.com/vinted/dataverse-finance/pull/2481), [FDSA-3543](https://vinted.atlassian.net/browse/FDSA-3543)).
- **what:** on 5 Oct, Xendo sent 102 test records and stopped both reconciliation marts. Test records are now dropped and other bad ids warn. The download job also could lose a day of data without failing. It now fails loudly, retries and logs each step.
- **business:** a repeated invoice line would have doubled its tax in the Sovos export. A new test now fails the mart on one.
- **values:** [ownership] [aim high]

### 4. Incidents

**Incident 6848: a currency test stopped the finance daily DAG** ([incident](https://vinted.slack.com/archives/C0C78PLMYK0/p1791348259231989), [root cause](https://vinted.slack.com/archives/C076F6CME10/p1791348448794769?thread_ts=1791348395.883899&cid=C076F6CME10)).
- **what:** I had the failing model green four minutes after responding, and posted recovery times for other teams. The cause was a test on an upstream model that read a downstream one ([#2487](https://github.com/vinted/dataverse-finance/pull/2487)).
- **fix at the root:** the same day, I wrote an [RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32320717248) and a new linter rule, M020 ([dataverse-cli#735](https://github.com/vinted/dataverse-cli/pull/735), open). It ran over all 8,274 models in 58 projects, and it flags 49 tests in 11 projects.
- **above and beyond:** I proposed M020 to the whole AE community ([thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1791361148128839?thread_ts=1791361148.128839&cid=C03JBPN0Q1W)).
- **values:** [ownership] [aim high] [co-create]

### 5. Systems other teams use

**Partition alerts now go to every owning team.** Merged ([dataverse-metrics#678](https://github.com/vinted/dataverse-metrics/pull/678), [#683](https://github.com/vinted/dataverse-metrics/pull/683), [launch](https://vinted.slack.com/archives/C03JBPN0Q1W/p1790845548733249?thread_ts=1787641419.547139&cid=C03JBPN0Q1W)).
- **what:** in September, two marketing models failed at the 4,000-partition limit while the mart already flagged them. Now each team gets a message. A backfill on 30 Sep made the monitor project a 16-year cap at 74 days, so I made the growth rate ignore one-day spikes. The next PR tells teams what to do ([#681](https://github.com/vinted/dataverse-metrics/pull/681), open).
- **recognition:** Yirong Lo: "Thanks Jeremy! This is awesome" ([thread](https://vinted.slack.com/archives/C06CS5E2AFM/p1790844380295139?thread_ts=1790843951.733179&cid=C06CS5E2AFM)).
- **values:** [aim high] [co-create]

**Self-service data refresh: data platform agreed a ticket.** RFC updated ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071), [thread](https://vinted.slack.com/archives/C059T9KAF8X/p1791280101885869?thread_ts=1791280101.885869&cid=C059T9KAF8X)).
- **business:** 62 refresh requests still need an engineer. The median wait is 6.3 hours, and the slowest tenth wait about 143 hours. Finance waits about 400 hours a year in total.
- **next:** monthly manual jobs move to their own DAG, each with its own success message ([#2483](https://github.com/vinted/dataverse-finance/pull/2483), [dataverse-cli#733](https://github.com/vinted/dataverse-cli/pull/733), both open).
- **values:** [co-create]

**Chargeback split RFC** ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32322650572)).
- **what:** proposes a dbt journal file to replace a split that two teams build by hand. September's net is €911,175 over 35,457 rows. It sets 7 principles and 4 decisions for accounting.
- **values:** [aim high] [co-create]

### 6. Cost, CI and standards

- **Storage:** moved 10 finance tables to physical storage billing, saving about €80 a month ([#2472](https://github.com/vinted/dataverse-finance/pull/2472)).
- **Scan cost:** adding a third financial plan raised seven models' daily scan by about 50%. Clustering cut the one-version reads from 38.9 to 13.0 GiB and from 84.9 to 26.0 GiB, with identical results ([#2432](https://github.com/vinted/dataverse-finance/pull/2432)). Shipping result tests no longer scan about 1.33 TB a day on tables that don't change daily ([#2395](https://github.com/vinted/dataverse-finance/pull/2395)).
- **CI:** a PR now runs only the Python suites it changes, and each suite gets its own coverage comment ([#2421](https://github.com/vinted/dataverse-finance/pull/2421), [dataverse-cicd#266](https://github.com/vinted/dataverse-cicd/pull/266)). A shared stale-branch clean-up is open for finance and Looker, which hold 80 and 316 stale branches ([dataverse-cicd#280](https://github.com/vinted/dataverse-cicd/pull/280)).
- **Docs:** every one of the 11 ingestion jobs now has a README that says who uses the feed ([#2062](https://github.com/vinted/dataverse-finance/pull/2062)).
- **dbt 2.0:** cleared dbt 1.11 deprecations in 7 group functions domains, another team's project ([groupfunctions-dbt#1118](https://github.com/vinted/dataverse-groupfunctions-dbt/pull/1118)). Wrote down what blocks a move from vunit to native dbt unit tests ([dataverse-vunit#127](https://github.com/vinted/dataverse-vunit/pull/127), open), and re-opened [dbt-labs/dbt#8425](https://vinted.slack.com/archives/C03JBPN0Q1W/p1791529401095519?thread_ts=1791529401.095519&cid=C03JBPN0Q1W) on testing CTEs.
- **Open source:** opened [apache/airflow#74338](https://github.com/apache/airflow/pull/74338). It stops someone triggering a DAG with the end date before the start date. **[above and beyond]**
- **values:** [aim high] [co-create]

### 7. Team, hiring and community

- **AE hiring material:** reorganised the interviewer guide, and opened scoring guidance and a locked-down candidate doc ([ae-hiring-material#7](https://github.com/vinted/ae-hiring-material/pull/7), [#11](https://github.com/vinted/ae-hiring-material/pull/11), [#12](https://github.com/vinted/ae-hiring-material/pull/12)). Stuti Nigam: "who needs to find time when they have Jeremy ... :mvp:" ([thread](https://vinted.slack.com/archives/C0BPJ3MQV71/p1790695329565529?thread_ts=1790685817.910629&cid=C0BPJ3MQV71)). **[grow] [co-create]**
- **Career framework:** gave feedback on how leads use the level framework, including an appeals route ([thread](https://vinted.slack.com/archives/C076F6CME10/p1790952482765669?thread_ts=1790951023.686409&cid=C076F6CME10)). **[grow]**
- **Paris conference:** I am presenting in November ([thread](https://vinted.slack.com/archives/C076F6CME10/p1791462964816519?thread_ts=1791462964.816519&cid=C076F6CME10)). **[grow]**
- **Berliner Tafel:** organised the 9 Oct volunteering day ([thread](https://vinted.slack.com/archives/C04HC4J6X2R/p1790924596988009?thread_ts=1790924596.988009&cid=C04HC4J6X2R)). **[care]**

### Feedback I received

| feedback | from | what I changed |
| --- | --- | --- |
| My tone on a slow review "comes off a bit like you think this is not worth your time but is mine". I asked how to phrase it better and offered a call ([thread](https://vinted.slack.com/archives/C04KMGDQ11D/p1791458451060299?thread_ts=1791362734.533299&cid=C04KMGDQ11D)). | Igor Bobić, 8 Oct | *[to write]* |

---

### Weekly log

#### 29 Sep – 5 Oct 2026

- Fixed blank voucher provisions before the close, so August needed no restatement ([#2408](https://github.com/vinted/dataverse-finance/pull/2408)). `[Aim High / Co-create]`
- Sent partition alerts to every owning team, and fixed a false 74-day projection ([dataverse-metrics#678](https://github.com/vinted/dataverse-metrics/pull/678), [#683](https://github.com/vinted/dataverse-metrics/pull/683)). `[Aim High / Co-create / Above & beyond]`
- Gave EUR a rate for the open month, used by 14 models ([#2444](https://github.com/vinted/dataverse-finance/pull/2444)). `[Aim High]`
- Booked Vinted Pay's hand-moved refunds as manual transfers ([#2435](https://github.com/vinted/dataverse-finance/pull/2435)). `[Co-create]`
- Caught and fixed the unscaled September Adyen snapshot, and reran the close chain ([#2464](https://github.com/vinted/dataverse-finance/pull/2464)). `[Ownership]`
- Proposed a NetSuite currency check after 71 invoices were rejected ([thread](https://vinted.slack.com/archives/C09A63VS421/p1790933676957659?thread_ts=1790933676.957659&cid=C09A63VS421)). `[Aim High]`
- Saw the core billing fix for GB instead of UK merge ([core#137777](https://github.com/vinted/core/pull/137777)). `[Ownership / Above & beyond]`

#### 6–9 Oct 2026

- Found €33.9k of Adyen payout fees on the wrong account, and raised the cause with payments ([thread](https://vinted.slack.com/archives/G01A7KGHY74/p1791267423699489?thread_ts=1791264406.708729&cid=G01A7KGHY74)). `[Aim High / Co-create]`
- Shipped the payment provider shares mart and dashboard, matching Pigment exactly ([#2485](https://github.com/vinted/dataverse-finance/pull/2485), [groupfunctions-looker#2077](https://github.com/vinted/dataverse-groupfunctions-looker/pull/2077)). `[Aim High / Co-create]`
- Led incident 6848 and proposed linter rule M020, which flags 49 tests in 11 projects ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32320717248), [dataverse-cli#735](https://github.com/vinted/dataverse-cli/pull/735)). `[Ownership / Above & beyond]`
- Merged the 25 escrow revenue controls from our 31 Aug 1:1 ([#2300](https://github.com/vinted/dataverse-finance/pull/2300)). `[Aim High]`
- Made the Xendo US tax feed fail loudly and drop test records ([#2479](https://github.com/vinted/dataverse-finance/pull/2479), [#2480](https://github.com/vinted/dataverse-finance/pull/2480)). `[Ownership]`
- Wrote the chargeback split RFC ([RFC](https://vinted.atlassian.net/wiki/spaces/DF/pages/32322650572)). Updated the self-service refresh RFC, and data platform agreed a ticket ([thread](https://vinted.slack.com/archives/C059T9KAF8X/p1791280101885869?thread_ts=1791280101.885869&cid=C059T9KAF8X)). `[Co-create]`
- Moved 10 tables to cheaper storage billing, saving about €80 a month ([#2472](https://github.com/vinted/dataverse-finance/pull/2472)). `[Aim High]`
- Opened an Airflow PR that validates trigger dates ([apache/airflow#74338](https://github.com/apache/airflow/pull/74338)). `[Co-create / Above & beyond]`
- Organised the Berliner Tafel volunteering day ([thread](https://vinted.slack.com/archives/C04HC4J6X2R/p1790924596988009?thread_ts=1790924596.988009&cid=C04HC4J6X2R)). `[Care]`

### 1:1 row

| Date | Last week achievements | Weekly reflections |
| --- | --- | --- |
| 29 Sep – 9 Oct 2026 | Fixed blank voucher provisions before close, so August needed no restatement. Found €33.9k of Adyen payout fees on the wrong account. Shipped payment provider shares, matching Pigment. Merged the escrow controls and the core GB/UK fix (31 Aug goals). Led incident 6848 and proposed linter rule M020. Partition alerts now reach every team. | *[to write]* |

---

## 1 Aug – 28 Sep 2026

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


---

### 1. Month-end close is right, and less manual

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

### 2. Shipping result: one agreed schedule, no hand-run refreshes

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

### 3. Controls and data quality: problems found before anyone reported them

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

### 4. Incidents I led and cleaned up at the root

**A duplicate snapshot put a €1.5m jump into Looker.** Fixed at the root ([FDSA-3302](https://vinted.atlassian.net/browse/FDSA-3302), [FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318), [FDSA-3330](https://vinted.atlassian.net/browse/FDSA-3330), [FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331)).
- **what:** a re-run on 2 Sep made Vinted UAB payment fees look €1.5m too high. Reported figures were unaffected. The first ticket listed 6 duplicates. I scanned all 18 snapshot tables and found 34 in 10 models, going back to March 2025.
- **fix:** I cleaned them up ([#2288–#2297](https://github.com/vinted/dataverse-finance/pull/2288)) and added a one-snapshot-per-day test ([#2232](https://github.com/vinted/dataverse-finance/pull/2232)). 13 models now replace a same-day re-run instead of adding a copy.
- **values:** [ownership] [aim high]

**Other incidents.**
- **Mangopay:** the S3 listing silently stopped at 1,000 files, so a July close retry skipped the month's files ([#2064](https://github.com/vinted/dataverse-finance/pull/2064), [#2065](https://github.com/vinted/dataverse-finance/pull/2065), [FDSA-3067](https://vinted.atlassian.net/browse/FDSA-3067)).
- **Adyen fees:** the fees model failed on memory at 156 slot-hours with 3.34 TiB spilled. It now runs in 17.2 slot-hours with no spill ([#2175](https://github.com/vinted/dataverse-finance/pull/2175), [FDSA-3206](https://vinted.atlassian.net/browse/FDSA-3206)).
- **CDD queue:** I found the CDD pipeline paused with 58 merges queued and never run ([#2308](https://github.com/vinted/dataverse-finance/pull/2308), [FDSA-3332](https://vinted.atlassian.net/browse/FDSA-3332)).
- **values:** [ownership]

### 5. Systems other teams now use

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

### 6. Code standards and dbt 2.0 readiness

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

### 7. Platform and migration

**Continuous deployment turned on for finance** ([#2153](https://github.com/vinted/dataverse-finance/pull/2153), [#2154](https://github.com/vinted/dataverse-finance/pull/2154), [#2176](https://github.com/vinted/dataverse-finance/pull/2176), [FDSA-3190](https://vinted.atlassian.net/browse/FDSA-3190)).
- **what:** I cleared three blockers with DPX. 127 of 308 models are excluded from rebuilding on merge. One of them would have written Austrian taxpayer personal data to the prod bucket on any build.
- **recognition:** Júlia called it a "game changer" ([thread](https://vinted.slack.com/archives/C076F6CME10/p1789465411298849)).
- **values:** [aim high] [co-create]

**Export buckets moved off the legacy project** ([terraform-dataverse#3723](https://github.com/vinted/terraform-dataverse/pull/3723), [oss-platform-service#71](https://github.com/vinted/oss-platform-service/pull/71), [#2234](https://github.com/vinted/dataverse-finance/pull/2234), [FDSA-3149](https://vinted.atlassian.net/browse/FDSA-3149), [FDSA-3194](https://vinted.atlassian.net/browse/FDSA-3194), [FDSA-3291](https://vinted.atlassian.net/browse/FDSA-3291)).
- **found:** stage had been reading the prod iSAF bucket.
- **communication:** I warned [#isaf](https://vinted.slack.com/archives/C02A97Z59L2/p1788768336716279) and [#pigment_support](https://vinted.slack.com/archives/C08QS2MLS2U/p1788860282653919). I held the merge until after the close, and notified 10 sandbox users.
- **lineage:** 24 export models now show their consumers across iSAF, Austrian tax, Sovos, NetSuite and Pigment ([#2235](https://github.com/vinted/dataverse-finance/pull/2235), [FDSA-3306](https://vinted.atlassian.net/browse/FDSA-3306)).
- **values:** [ownership] [co-create]

### 8. Team, community and hiring

- **Berlin dbt meet-up:** I hosted it on 10 Sep, for about 60 guests. I moderated the AE career panel and promoted our open roles. António: the round table was "very well conducted" ([recap](https://vinted.slack.com/archives/C02K4DJRZH8/p1789104601271289), [António](https://vinted.slack.com/archives/C076F6CME10/p1789104603255589)). I am co-organising a Vilnius meet-up for mid-October ([thread](https://vinted.slack.com/archives/C076F6CME10/p1787561169076779?thread_ts=1786355397.086789&cid=C076F6CME10)). **[co-create] [grow]**
- **AE hiring panel:** I set up the group and its access ([service-catalog#17023](https://github.com/vinted/service-catalog/pull/17023), [terraform-github#8562](https://github.com/vinted/terraform-github/pull/8562)). I shadow interviews, join the calibration loop, and offered to lead interviews ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788425573475809?thread_ts=1788425500.516319&cid=C076F6CME10)). **[co-create] [grow]**
- **Reviews:** I reviewed 140 PRs, 103 of them in finance (Emily 41, Júlia 27, Samanta 21). Samanta called a detailed review "real-mvp". **[co-create]**
- **Shared practices:** I shared the unit-testing guide ([thread](https://vinted.slack.com/archives/C03JBPN0Q1W/p1787824097864589?thread_ts=1787823910.491879&cid=C03JBPN0Q1W)) and a self-review practice for AI-written PRs ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788853912393169?thread_ts=1787727215.817299&cid=C076F6CME10)). I proposed that test descriptions state the rule and what to do on failure ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788770645634999?thread_ts=1788769943.200799&cid=C076F6CME10)). **[co-create] [grow]**
- **Care:** I organised Berliner Tafel food bank volunteering days ([thread](https://vinted.slack.com/archives/C04HC4J6X2R/p1786958374428139)). I credited Emily's export automation in public ([thread](https://vinted.slack.com/archives/C076F6CME10/p1788364525194939)), and suggested an Insights Discovery retake before the offsite. **[care]**

### 9. Strategy and influence beyond finance

- **RFC reviews:** I left 45 review comments. They include the [Tier 1 Reliability Review](https://vinted.atlassian.net/wiki/spaces/DF/pages/32046055735/2026+Q3+-+Tier+1+Reliability+Review) (shift testing left) and [Tier 0 P&L scope](https://vinted.atlassian.net/wiki/spaces/DF/pages/32120244315/2026-08-26+Increasing+Tier+0+Scope+to+P+L+Financial+Metrics). On [Tier 0 Data Assets](https://vinted.atlassian.net/wiki/spaces/DF/pages/32202654020/2026+Q3+-+Tier+0+Data+Assets+-+what+it+means+for+your+team) I proposed a policy gate as an AE roadmap item. On [Recovering failed DAG runs](https://vinted.atlassian.net/wiki/spaces/DPV2/pages/32026985454/2026-09-22+Recovering+consecutive+failed+DAG+runs) I asked for a minimum lookback rather than a default.
- **CDD for the org:** I asked for CDD to cover SQL changes only, to allow a per-PR opt-out, and to show a plan first ([thread](https://vinted.slack.com/archives/C02JMNFS9GD/p1787656910916349?thread_ts=1787653801.646929&cid=C02JMNFS9GD)).
- **Ownership of cross-domain changes:** I argued that a team making one should own the downstream PRs ([thread](https://vinted.slack.com/archives/C076F6CME10/p1787738141452099?thread_ts=1787736956.482569&cid=C076F6CME10)).
- **BI tooling:** I opened a discussion on moving off Looker, now that our measures live in yml. I volunteered for the 2027 BI discovery and POC.
- **Audit:** I proposed tagging tests by accounting assertion, so audit walkthroughs can see what each test proves (ISA 315).
- **values:** [co-create] [aim high]

---

### How this maps to IC3 and IC4

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

### Reflections (draft for me to finish)

- **went well:** the biggest finds came from checking my own work (a table compared with its earlier version, a snapshot scan), not from alerts.
- **issue:** other teams' upstream changes caused most of the breakage: the payment status change, GB from core, the Adyen rename and the partition limits. Each cost days after the fact. Could finance get into those teams' release process earlier?
- **issue:** my PRs stack up waiting for review (#2369 blocks #2379 and #2381). Could we agree a review cadence for chained PRs?
- **thought:** the AE community is converging on shared skills and standards. Finance can shape them instead of adopting what others decide.

---

<details>
<summary>How this was compiled</summary>

**29 Sep – 9 Oct 2026**

- **GitHub:** PRs authored and reviewed, created or merged 29 Sep – 9 Oct. The raw lists are in [sources/gh_prs_2026-09-29_to_2026-10-09.tsv](sources/gh_prs_2026-09-29_to_2026-10-09.tsv) and [sources/gh_reviews_2026-09-29_to_2026-10-09.tsv](sources/gh_reviews_2026-09-29_to_2026-10-09.tsv). PR bodies are in [sources/pr_bodies_2026-09-29_to_2026-10-09.md](sources/pr_bodies_2026-09-29_to_2026-10-09.md).
- **Jira:** `(assignee = currentUser() OR reporter = currentUser()) AND updated >= "2026-09-29"`.
- **Slack and Confluence:** see [sources/slack_confluence_summary_2026-09-29_to_2026-10-09.md](sources/slack_confluence_summary_2026-09-29_to_2026-10-09.md). Every message was searched, and no channel was read in full. 9 Oct is covered up to 10:10. The praise search found only messages that name Jeremy.
- **Figures:** quoted from a PR body, ticket, page or message, never inferred from a title.

**1 Aug – 28 Sep 2026**

- **GitHub:** `gh search prs --author=@me` and `--reviewed-by=@me`, created 2026-08-01..2026-09-28, split by date to get past the 200-result cap. The raw lists are in [sources/gh_prs_2026-08-01_to_2026-09-28.tsv](sources/gh_prs_2026-08-01_to_2026-09-28.tsv) and [sources/gh_reviews_2026-08-01_to_2026-09-28.tsv](sources/gh_reviews_2026-08-01_to_2026-09-28.tsv).
- **Jira:** `(assignee = currentUser() OR reporter = currentUser()) AND updated >= "2026-08-01"`. The raw list is in [sources/jira_tickets_2026-08-01_to_2026-09-28.tsv](sources/jira_tickets_2026-08-01_to_2026-09-28.tsv).
- **Confluence:** created and edited pages, plus comments. See [sources/confluence_slack_summary_2026-08-01_to_2026-09-28.md](sources/confluence_slack_summary_2026-08-01_to_2026-09-28.md).
- **Slack:** public and private channels only, never DMs. 15 Aug – 11 Sep and 21–28 Sep were read in full ([15–28 Aug](sources/slack_2026-08-15_to_2026-08-28.md), [29 Aug – 11 Sep](sources/slack_2026-08-29_to_2026-09-11.md)). 1–14 Aug and 12–20 Sep came only from targeted searches.
- **Figures:** every figure is quoted from a PR body, ticket description or page, never inferred from a title.

</details>
