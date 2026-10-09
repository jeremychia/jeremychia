# slack and confluence evidence, 29 sep – 9 oct 2026

gathered 9 oct 2026. figures are copied exactly as stated in the source. nothing is inferred.

## coverage

**slack scope.** public and private channels only. no dms, no group dms. social channels (#etl_people, #berlin-social) appeared in search results but are left out below.

**how slack was read.** every message jeremy sent was pulled through search, sorted oldest first, and every page was walked.

| days | method | status |
| --- | --- | --- |
| tue 29 sep – thu 1 oct | `from:<@U05MT2369M1> after:2026-09-28 before:2026-10-03`, pages 1–20 | searched in full |
| fri 2 oct | same query until it hit the 20-page limit at 11:34, then `on:2026-10-02` from 11:34, pages 1–5 | searched in full |
| sat 3 – sun 4 oct | covered by the week-2 query | no messages |
| mon 5 – fri 9 oct | `from:<@U05MT2369M1> after:2026-10-02 before:2026-10-10`, pages 1–15, end of results | searched in full (9 oct up to 10:10, when the search ran) |

- no channel or thread was read in full with `slack_read_channel` or `slack_read_thread`. replies from others appear only where search returned them.
- the praise search used `-from:<@U05MT2369M1>` with the keywords "thanks" and "Jeremy", plus a mention search. it is not exhaustive. a thank-you that names nobody, or only uses an emoji, will not show up.

**confluence scope.** `contributor = currentUser() AND lastModified >= "2026-09-29"` returned 13 items. a separate creator query returned 3 pages and 2 comments created in the window.

---

## top items

1. **incident 6848, 7 oct: currency test stopped the finance daily dag.** responded at 06:44, built the physical tables, cleared `dim_active_currencies` (green 06:48), posted recovery etas, and found the root cause: a test on an upstream model read a downstream model. wrote the rfc and 5 fix prs the same day, plus linter rule m020.
2. **payment provider shares shipped, 7–8 oct.** totals match pigment exactly for may to september 2026. new mart `mrt_payment_provider_shares` and a looker dashboard. tomas radavičius: "thank you! :mvp:".
3. **voucher accrual fix before the close, 29 sep.** found 11 vouchers with no provision. set out 2 options with exact figures and recommended one under ias 37. the change went in before the close, so no restatement was needed. credited emily's live month-to-date view for catching it.
4. **adyen fee split error, 6 oct.** found €33.9k of adyen payout fees booked to 700007 instead of 700006. traced it to the kyc estimate: 70,396 checks estimated against 5,616 billed. raised a ticket to payments with the evidence.
5. **partition monitoring pipeline launched, 1 oct.** formalised the bigquery partition alerts as a pipeline. sent the first alerts by hand to the buyer and help_experience teams. yirong lo: "Thanks Jeremy! This is awesome".
6. **month-end close (wd1–wd2) support.** delivered the voucher accrual, shipping fx, extra service deferral, compensations and vgo pro wallet exports, the i.SAF export and the invoice lines snapshot. fixed the ecb rate division-by-zero, the stale trendsales views and the duplicate mangopay files.
7. **found and owned a missed adyen invoice, 2 oct.** `prep_adyen_invoice_fees` had stayed static. he caught it while checking premium splits, explained the cause, reran the chain and apologised. payouts (700006) are now split by country in the september file.
8. **rfc: self-service data refresh, updated 6 oct.** 62 refresh requests still need an engineer, with a median wait of 6.3 h. took the airflow trigger question to data platform, got their answer, and turned the proposal into tasks with no schedule (pr 2483).
9. **rfc: chargeback split accounting import file, 7 oct.** proposes a dbt journal file to replace a split that 2 teams build by hand. it shows €911,175 net for september 2026 and lists 4 decisions for accounting.
10. **mec issue and request log for 2026-09, 1–8 oct.** created the log page with júlia. it records every close issue with root cause and long-term fix. one finding: vinted inc's wd2 export has 338,588 more lines, worth usd 235,009.
11. **cost savings.** moved 10 tables to physical storage billing, which saves 80 eur / month (pr 2472). excluded shipping results tests from the daily run, because they scanned about 1.33tb on tables that do not change daily.
12. **acq-gb-vinted-fr onboarding with mangopay, 29 sep – 7 oct.** wrote the report spec for the new client, got api credentials, solved the 403 error, and flagged a row cap of 200,000 rows per 15-minute report.
13. **governance call on metrics, 7–8 oct.** pushed back on keeping psp metrics outside looker as loose queries. agreed a separate mart so fp&a's governed business metrics stay untouched. daniel arango: "That works, thanks!".
14. **hiring panel and community.** shipped ux prs for the ae hiring material, plus scorecard guidance. stuti nigam: "who needs to find time when they have Jeremy ... :mvp:". organised the 9 oct berliner tafel volunteering day. júlia notes jeremy is presenting at forward data conference in paris in november.
15. **upstream proposals.** re-opened dbt native unit testing on ctes (dbt-labs/dbt#8425) and raised apache/airflow#74336. pooled prior work on building dashboards with claude and proposed a shared skill.

---

## slack items by day

### tue 29 sep

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #fin-control_and_analytics | asked 6 numbered questions to pin down how to attribute "acquiring provider" for the psp share request | "in august 2026, 17% of completed transactions (15.3m) do not have a card acquirer"; "in FR, 2.26m of 13.0m were paid in full from a mangopay wallet"; "in PL, 11% were paid in full from vinted pay balance"; partial wallet "8% (7.3m)"; free vas "10% of august 2026 VAS orders (570k push-ups)"; "46% of VAS orders are paid fully from wallet"; "in PL, adyen_bank is 28% of transactions"; "paypal (4.0m) and ideal (2.1m) ... klarna (0.5m)"; before oct 2024 "(1.4m transactions)" | https://vinted.slack.com/archives/G01A7KGHY74/p1790665939237779?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| #finance-dsa | moved the vgo carrier invoice breakdown onto scheduled full refresh dates (pr 2379) | — | https://vinted.slack.com/archives/C076F6CME10/p1790666505504809 |
| #finance-dsa | extended cdc completeness tests to the last 2 sources (pr 2382) | "we check for completeness on 3 out of 5 sources" | https://vinted.slack.com/archives/C076F6CME10/p1790666506360869?thread_ts=1790666506.360869&cid=C076F6CME10 |
| #fin-control_and_analytics | heads-up to everyone who reads files on the google cloud bucket, with an apology for posting late | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790666611622929?thread_ts=1790666611.622929&cid=G01A7KGHY74 |
| #fin-control_and_analytics | told finance that vgo carrier invoice and shipping results now refresh on schedule, so they no longer need to ask | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790668728898329?thread_ts=1790141679.721099&cid=G01A7KGHY74 |
| #finance-dsa | wrote requirements for a new linter rule and handed it to emily as a growth task | — | https://vinted.slack.com/archives/C076F6CME10/p1790670036551719?thread_ts=1790587981.961529&cid=C076F6CME10 |
| #finance-dsa | excluded shipping results tests from the daily scheduler run (pr 2395, FDSA-3449) | "they were scanning about 1.33TB" | https://vinted.slack.com/archives/C076F6CME10/p1790671201787469?thread_ts=1790671201.787469&cid=C076F6CME10 |
| #finance-dsa-public | announced the poetry to uv migration with vedashree (prs 2397–2403) | — | https://vinted.slack.com/archives/C076P6P3L5U/p1790671893249399?thread_ts=1790671893.249399&cid=C076P6P3L5U |
| #dataverse-code-review | posted the partition-limit alert pr (dataverse-metrics#678) and later added a reviewer guide | — | https://vinted.slack.com/archives/C04KMGDQ11D/p1790677599084969?thread_ts=1787737909.584729&cid=C04KMGDQ11D |
| #ae-hiring-panel | ux prs for the interview content page (ae-hiring-material #7, #8, #9, #10) and github pages (terraform-github#8891) | — | https://vinted.slack.com/archives/C0BPJ3MQV71/p1790685817910629?thread_ts=1790685817.910629&cid=C0BPJ3MQV71 |
| #ext-vinted-mangopay-data-reporting | wrote the report format spec for new client acq-gb-vinted-fr, with a backfill request | "2026-08 (first transactions on 2026-08-05)" | https://vinted.slack.com/archives/C09JTT5NYPP/p1790686916185029?thread_ts=1790587586.485599&cid=C09JTT5NYPP |
| #fin-control_and_analytics | voucher accrual: found vouchers with no provision and asked finance which country basis to use | "11 vouchers had no provision across august and september (4 in august, 9 in september, with 2 open in both months)" | https://vinted.slack.com/archives/G01A7KGHY74/p1790687343956889?thread_ts=1790687343.956889&cid=G01A7KGHY74 |
| #fin-control_and_analytics | voucher accrual options | option 1: "other" rate "39.71% for august (today 37.95%) and 40.17% for september (today 38.36%)", "rises by €7,123 for august and €8,861 for september"; option 2: "rises by €7 for august and €2,301 for september" | https://vinted.slack.com/archives/G01A7KGHY74/p1790687441708849?thread_ts=1790687343.956889&cid=G01A7KGHY74 |
| #fin-control_and_analytics | recommended option 2, citing ias 37:36 and 37:38 | "98.9% of all voucher value"; "the 13 with no provision"; "(50 EUR face value)" | https://vinted.slack.com/archives/G01A7KGHY74/p1790688559639069?thread_ts=1790687343.956889&cid=G01A7KGHY74 |
| #fin-control_and_analytics | committed to land the change before the close, so no restatement is needed | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790689811951739?thread_ts=1790687343.956889&cid=G01A7KGHY74 |
| #fin-control_and_analytics | credited emily's live month-to-date view for catching the issue before the close | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790689923664639?thread_ts=1790687343.956889&cid=G01A7KGHY74 |
| #rududu | requested an api key for acq-gb-vinted-fr | — | https://vinted.slack.com/archives/C05V72TUWLR/p1790687924725679?thread_ts=1790331684.575449&cid=C05V72TUWLR |
| #checkout-public | chased credit notes for test-user invoices before month end | "5754440126 and 5756716970: €1.12 each"; 12 older invoices still open | https://vinted.slack.com/archives/CQTQUNDU0/p1790689039134289?thread_ts=1786359890.744179&cid=CQTQUNDU0 |
| #dataverse_finance_monitoring | triaged 7 warnings, with prs 2406, 2408 and 2410 | [7]: "it will go from 44 cases (today) to 210" | https://vinted.slack.com/archives/C0706RCL6CF/p1790690094666029?thread_ts=1790661576.304469&cid=C0706RCL6CF |
| #data-platform-support | diagnosed another team's write failure as a missing dataset grant, and linked the terraform changes behind it | — | https://vinted.slack.com/archives/C059T9KAF8X/p1790693612664399?thread_ts=1790693028.364839&cid=C059T9KAF8X |

### wed 30 sep

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #checkout-public | asked who owns qa test accounts, so leftover test transactions can be traced | — | https://vinted.slack.com/archives/CQTQUNDU0/p1790754595826949?thread_ts=1786359890.744179&cid=CQTQUNDU0 |
| #dataverse_finance_monitoring | traced a voucher threshold warning to the ds100 us referral experiment (MAT-892) and revised the limit (pr 2420) | campaigns "set up on 2026-06-29, and vouchers issued from 2026-07-22" | https://vinted.slack.com/archives/C0706RCL6CF/p1790774961693659?thread_ts=1790746978.003139&cid=C0706RCL6CF |
| #finance-dsa-public | ci change: python unit tests no longer run on dbt-only prs (pr 2421, dataverse-cicd#266) | — | https://vinted.slack.com/archives/C076P6P3L5U/p1790776940253409?thread_ts=1790671893.249399&cid=C076P6P3L5U |
| #fin-control_and_analytics | shipping campaign query: left out heavy-small parcels whose weight cannot be confirmed | "about 9.3k heavy-small parcels ... from 14-30 september"; "understated by ~13k EUR" | https://vinted.slack.com/archives/G01A7KGHY74/p1790777510882979?thread_ts=1790248880.358479&cid=G01A7KGHY74 |

### thu 1 oct (wd1)

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #dataverse_finance_monitoring | voucher accrual failed because ecb rates were not yet published; added a fallback to last month's rate (pr 2425) | "division by zero: 0 / 0" | https://vinted.slack.com/archives/C0706RCL6CF/p1790833467818989?thread_ts=1790818612.413739&cid=C0706RCL6CF |
| #dataverse_finance_monitoring | trendsales failure: the staging views were never rebuilt after the data moved; proposed making them static (pr 2426) | views "last built in oct-nov 2025" | https://vinted.slack.com/archives/C0706RCL6CF/p1790833683310029?thread_ts=1790833683.310029&cid=C0706RCL6CF |
| #dataverse_finance_monitoring | created the monthly mec issue log | — | https://vinted.slack.com/archives/C0706RCL6CF/p1790834339640359?thread_ts=1790832131.997139&cid=C0706RCL6CF |
| #fin-control_and_analytics | snapshotted invoice lines on wd1 so vinted pay de could report early, and flagged gbp growth | "GBP grew a lot - from 0.12m GBP in aug 2026 to 2.8m GBP in sep 2026" | https://vinted.slack.com/archives/G01A7KGHY74/p1790836640518689?thread_ts=1790833756.228179&cid=G01A7KGHY74 |
| #data-platform-support → #inc-2026-10-01-airflow-ui-dont-show-tasks-24994 | reported that airflow tasks were missing from the ui; it became an incident | — | https://vinted.slack.com/archives/C059T9KAF8X/p1790837103721379?thread_ts=1790837103.721379&cid=C059T9KAF8X |
| #fin-control_and_analytics | voucher accrual export ready | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790838030114899?thread_ts=1790838030.114899&cid=G01A7KGHY74 |
| #dataverse-data-scan-alerts | accepted the cost alerts, which were expected after financial_plan_2027 was added | "(5.1 TB / day)" | https://vinted.slack.com/archives/C0BVDJ8V71C/p1790839594691669 |
| #dataverse-data-scan-alerts | explained the shipping result scan alert as normal growth | "2,343 GiB on 1 sep and 2,818 GiB on 15 and 23 sep" | https://vinted.slack.com/archives/C0BVDJ8V71C/p1790839674012409?thread_ts=1790839176.562019&cid=C0BVDJ8V71C |
| #dataverse-data-scan-alerts | praised matteo and gonzalo as "the MVPs" for the data scan alerts | — | https://vinted.slack.com/archives/C0BVDJ8V71C/p1790839699669099 |
| #fin-control_and_analytics | vinted pay "unknown" transfers: explained the likely cause and added a warning test (pr 2435) | "we only have 10 'unknown' transfers which started appearing from aug 2026 onwards" | https://vinted.slack.com/archives/G01A7KGHY74/p1790842503370499?thread_ts=1790839183.540689&cid=G01A7KGHY74 |
| #hex_analytics_engineering, #dataverse-buyer-alerts | sent the first partition monitoring alerts by hand to 2 teams | help_experience: "current_partitions: 3,936", "Deadline: 2026-12-04"; buyer: "current_partitions: 3,927", "Deadline: 2026-12-16" | https://vinted.slack.com/archives/C08612B65MY/p1790843913125869?thread_ts=1790843913.125869&cid=C08612B65MY |
| #analytics-engineering | **announced the partition monitoring pipeline** (bigquery_partition_alerts) and asked teams to co-create it | "(4,000 per job, and 10,000 for the whole asset/table)" | https://vinted.slack.com/archives/C03JBPN0Q1W/p1790845548733249?thread_ts=1787641419.547139&cid=C03JBPN0Q1W |
| #dataverse-code-review | revised the partition monitoring growth rate and message (dataverse-metrics#683, #681) | — | https://vinted.slack.com/archives/C04KMGDQ11D/p1790844498602669?thread_ts=1790844498.602669&cid=C04KMGDQ11D |
| #analytics-engineering | followed up on dbt deprecation fixes across vgo and trust repos | — | https://vinted.slack.com/archives/C03JBPN0Q1W/p1790846334281909?thread_ts=1790604302.194349&cid=C03JBPN0Q1W |
| #fin-control_and_analytics | compensations with no country: proposed falling back to the receiving user's country, to match the adyen report | "(30 compensation entries)" | https://vinted.slack.com/archives/G01A7KGHY74/p1790849608688349?thread_ts=1790849608.688349&cid=G01A7KGHY74 |
| #dataverse_finance_monitoring | explained a tier-0 variance warning as the expected switch to the 2027 categories (FDSA-3288) | "'womens_maternity' (1.05m items)" | https://vinted.slack.com/archives/C0706RCL6CF/p1790849717833869?thread_ts=1790833732.673399&cid=C0706RCL6CF |
| #dataverse-data-scan-alerts | explained the adyen balance platform scan jump at the start of the month | "it replaced 32 daily partitions ... instead of the usual 3" | https://vinted.slack.com/archives/C0BVDJ8V71C/p1790853378464419?thread_ts=1790852423.632579&cid=C0BVDJ8V71C |
| #boa-finsys-dsa | told the finance systems team where to send dsa requests | — | https://vinted.slack.com/archives/C09A63VS421/p1790853536209859 |
| #penguins / #dataverse_finance_monitoring | found checkout reports missing for 2 entities and asked checkout for them (pr 2447) | "2 entities, each missing 1 of 30 days" | https://vinted.slack.com/archives/C0706RCL6CF/p1790858791822709?thread_ts=1790833732.673399&cid=C0706RCL6CF |
| #ext-vinted-mangopay-data-reporting | flagged incomplete repudiation data and a duplicate wallet fees file; got the duplicate removed from s3 | "both have the same number of rows (9,933)"; repudiation "only 1-8 sep" | https://vinted.slack.com/archives/C09JTT5NYPP/p1790860196284179?thread_ts=1790836408.551889&cid=C09JTT5NYPP |
| #dataverse_finance_monitoring | moved the mangopay checks to day 2, because files never arrive on day 1 (pr 2450) | — | https://vinted.slack.com/archives/C0706RCL6CF/p1790864247950329?thread_ts=1790833732.673399&cid=C0706RCL6CF |
| #finance-dsa | proposed reviving the move of mangopay deliveries from s3 to gcs | — | https://vinted.slack.com/archives/C076F6CME10/p1790862680725279?thread_ts=1790862680.725279&cid=C076F6CME10 |

### fri 2 oct (wd2)

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #fin-control_and_analytics | i.SAF export done, then the wd2 invoice lines snapshot | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790919683922529?thread_ts=1790917106.848299&cid=G01A7KGHY74 |
| #fin-control_and_analytics | shipping fx files generated | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790920999792409 |
| #fin-control_and_analytics | extra service revenue deferral export | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790921414081449 |
| #ext-vinted-mangopay-data-reporting | confirmed the new repudiation file is complete | "complete with 1-30 sep" | https://vinted.slack.com/archives/C09JTT5NYPP/p1790921497503479?thread_ts=1790836408.551889&cid=C09JTT5NYPP |
| #berliner-tafel-volunteering | organised the 9 oct berliner tafel volunteering day and tagged 10 colleagues | — | https://vinted.slack.com/archives/C04HC4J6X2R/p1790924596988009?thread_ts=1790924596.988009&cid=C04HC4J6X2R |
| #dataverse_finance_monitoring | triaged 4 warnings: fixed an ecb test dependency (pr 2455) and judged a mangopay row jump legitimate | "+11.3m ... EUR transfers with the ASYNC payment type, and another +2.5m in GBP" | https://vinted.slack.com/archives/C0706RCL6CF/p1790925521366679?thread_ts=1790920284.668029&cid=C0706RCL6CF |
| #fin-control_and_analytics | compensations splits export, then traced a null-country refund that had defaulted to lt/lt | "adyen paid 1.81 USD to user 3167846841 on 2026-09-17" | https://vinted.slack.com/archives/G01A7KGHY74/p1790932187783859?thread_ts=1790930834.202579&cid=G01A7KGHY74 |
| #fin-control_and_analytics | vgo pro wallet export | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790932328134539 |
| #boa-finsys-dsa | **currency completeness check**: set out 3 options to catch missing netsuite currencies before upload. antónio backed option 2 | "4 VGo UAB wallet customers were missing currency configs" | https://vinted.slack.com/archives/C09A63VS421/p1790933676957659?thread_ts=1790933676.957659&cid=C09A63VS421 |
| #finance-dsa | compensations: receiving user's country as fallback, with finance's agreement (pr 2443) | — | https://vinted.slack.com/archives/C076F6CME10/p1790934501279699?thread_ts=1790934501.279699&cid=C076F6CME10 |
| #finance-dsa | rewrote the descriptions for the custom ingestion pipelines, with a decision log (pr 2062) | — | https://vinted.slack.com/archives/C076F6CME10/p1790934940780239?thread_ts=1790934940.780239&cid=C076F6CME10 |
| #fin-control_and_analytics | split the premium amount by country for kornelija (FDSA-3530) | request: "premium amount ( -44,638.29 EUR) for Aug'26" | https://vinted.slack.com/archives/G01A7KGHY74/p1790943562861039?thread_ts=1786610159.001499&cid=G01A7KGHY74 |
| #finance-dsa | **owned a miss**: `prep_adyen_invoice_fees` stayed static after pr 2341, so one invoice was left out. caught it while checking premium splits, reran the chain, apologised | — | https://vinted.slack.com/archives/C076F6CME10/p1790947776366779?thread_ts=1790947520.071299&cid=C076F6CME10 |
| #fin-control_and_analytics | regenerated the payment processing fee files with the september vinted pay invoice | "NL202609021507 (premium -54,047.70 EUR, invoice total 629,272.70 EUR)" | https://vinted.slack.com/archives/G01A7KGHY74/p1790948130756789?thread_ts=1790924287.156649&cid=G01A7KGHY74 |
| #fin-control_and_analytics | told accounting that payouts (700006) are now split by country in the september file, so no manual split is needed | — | https://vinted.slack.com/archives/G01A7KGHY74/p1790950498218939?thread_ts=1786610159.001499&cid=G01A7KGHY74 |
| #finance-dsa | gave feedback on how leads use the career level framework (clf): evidence logs, "what qualifies" examples, an appeals route, and hand-offs between leads | — | https://vinted.slack.com/archives/C076F6CME10/p1790951945884149?thread_ts=1790951023.686409&cid=C076F6CME10 |
| #finance-dsa | clf thread: proposed an appeals mechanism for performance evaluation | — | https://vinted.slack.com/archives/C076F6CME10/p1790952482765669?thread_ts=1790951023.686409&cid=C076F6CME10 |
| #data-platform-support | welcomed a new joiner and explained the support-ticket and access process | — | https://vinted.slack.com/archives/C059T9KAF8X/p1790953280272249?thread_ts=1790952363.834369&cid=C059T9KAF8X |

### mon 5 oct

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #dataverse_finance_monitoring | added a workflow that reacts to warning messages with :mag: automatically | — | https://vinted.slack.com/archives/C0706RCL6CF/p1791183197379049?thread_ts=1791183197.379049&cid=C0706RCL6CF |
| #finance-dsa-public | answered a question on turning weekly targets into monthly ones by pointing to an existing macro | — | https://vinted.slack.com/archives/C076P6P3L5U/p1791188783826579?thread_ts=1791184855.232259&cid=C076P6P3L5U |
| #finance-dsa | added a completeness test for payment processing fees (pr 2466) | — | https://vinted.slack.com/archives/C076F6CME10/p1791196286889659?thread_ts=1791196286.889659&cid=C076F6CME10 |
| #checkout-public | us invoice: found vat on a fully discounted shipping fee and raised ZS-396 | "amount 5.68, vat_amount 0"; discount "−5.68, vat_amount +0.07"; "the shipping amounts differ by $0.99" | https://vinted.slack.com/archives/CQTQUNDU0/p1791198140941379?thread_ts=1791198115.964129&cid=CQTQUNDU0 |
| #finance-dsa | moved 10 tables to physical storage billing (pr 2472) | "saves 80 EUR / month" | https://vinted.slack.com/archives/C076F6CME10/p1791207559785659?thread_ts=1791207559.785659&cid=C076F6CME10 |
| #finance-dsa | created a dimension for shipping campaigns (pr 2381) | — | https://vinted.slack.com/archives/C076F6CME10/p1791211865375279 |
| #fin-control_and_analytics | explained why the psp accrual moved; full queries in FDSA-3541 | "US PSP fees doubled again - from 2.9m EUR to 6.0m EUR" | https://vinted.slack.com/archives/G01A7KGHY74/p1791215093692909?thread_ts=1791212113.836659&cid=G01A7KGHY74 |
| #berliner-tafel-volunteering | confirmed attendance with tafel and set up a liaison | — | https://vinted.slack.com/archives/C04HC4J6X2R/p1791200054763349?thread_ts=1790924596.988009&cid=C04HC4J6X2R |

### tue 6 oct

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #fin-control_and_analytics | explained the payout accrual drop: wallets moving to vinted pay | — | https://vinted.slack.com/archives/G01A7KGHY74/p1791267096301009?thread_ts=1791264406.708729&cid=G01A7KGHY74 |
| #fin-control_and_analytics | **found a classification error** in the adyen fee split (FDSA-3551) | "33.9k EUR of adyen payout fees which were booked to 700007 instead of 700006"; "35.6k EUR of AU payout fees" | https://vinted.slack.com/archives/G01A7KGHY74/p1791267423699489?thread_ts=1791264406.708729&cid=G01A7KGHY74 |
| #payments_dsa_public (ticket bot, his issue) | asked payments to fix the kyc estimate | "estimated 70,396 adyen identity checks ... adyen billed 5,616"; "€2.50"; "93% of the sellers in the estimate already had a vinted pay account"; "about 9,000 to 11,500 polish sellers a month"; "within 2% of adyen's bill by august"; "about 19% is still unexplained" | https://vinted.slack.com/archives/C04QY983L5C/p1791277456617379?thread_ts=1791277456.617379&cid=C04QY983L5C |
| #group-applied-data-support | handed off the dbt 1.11 deprecation clean-up with ready-made prompts (FDSA-3441) | — | https://vinted.slack.com/archives/C08DVFF5ZGB/p1791267894426509?thread_ts=1790601934.495879&cid=C08DVFF5ZGB |
| #dataverse_finance_monitoring / #finance-dsa | fixed a failed xendo job: dropped test records (pr 2479), then made the pipeline fail loudly with retries (pr 2480) | — | https://vinted.slack.com/archives/C0706RCL6CF/p1791268458397849?thread_ts=1791247823.622469&cid=C0706RCL6CF |
| #data-platform-support | proposed triggering airflow jobs from slack, linked to the self-service rfc; got data platform to agree a ticket (21 replies) | — | https://vinted.slack.com/archives/C059T9KAF8X/p1791280101885869?thread_ts=1791280101.885869&cid=C059T9KAF8X |
| #finance-dsa | raised apache/airflow#74336 on trigger form validation, and edited the mec tasks page | — | https://vinted.slack.com/archives/C076F6CME10/p1791290096761069?thread_ts=1791290029.695179&cid=C076F6CME10 |
| #fwd_data_nov26 | got a team discount from the forward data conference organisers | "FWD_VINTED_26 that gives you a 15% discount"; "automatic 20% discount for packages of 5+ tickets" | https://vinted.slack.com/archives/C0BQTP5QGCF/p1791291418414339 |
| #finance-dsa | proposed a lighter way to reshare #analytics-engineering posts in the team channel | "today we had 3" | https://vinted.slack.com/archives/C076F6CME10/p1791291700854069?thread_ts=1791291700.854069&cid=C076F6CME10 |
| #ext-vinted-mangopay-data-reporting | got credentials for acq-gb-vinted-fr and raised a 403 error with mangopay | — | https://vinted.slack.com/archives/C09JTT5NYPP/p1791295471931699?thread_ts=1791295471.931699&cid=C09JTT5NYPP |

### wed 7 oct

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #inc-2026-10-07-fx-currencies-model-error-16086 | **responded to incident 6848**: built the physical tables and cleared `dim_active_currencies` | "i am responding" 06:44; "dim_active_currencies is green now" 06:48 | https://vinted.slack.com/archives/C0C78PLMYK0/p1791348259231989 |
| #finance-dsa | gave the root cause and committed to audit for the same anti-pattern | — | https://vinted.slack.com/archives/C076F6CME10/p1791348448794769?thread_ts=1791348395.883899&cid=C076F6CME10 |
| #analytics-engineering | psa to every team doing the storage migration | — | https://vinted.slack.com/archives/C03JBPN0Q1W/p1791348882018039?thread_ts=1791202356.795119&cid=C03JBPN0Q1W |
| #finance-dsa | replaced the invoice lines test with a check against seeds (pr 2487) | — | https://vinted.slack.com/archives/C076F6CME10/p1791349937471129 |
| #dataverse-incidents | posted recovery etas for downstream teams | "int__item_transactions_incl_suspicious_base. It should finish at about 05:52 UTC" | https://vinted.slack.com/archives/C09LSRCM18W/p1791350584987609?thread_ts=1791350584.987609&cid=C09LSRCM18W |
| #dataverse-incidents | tracked a slow model through to completion | "int__sell_through_rate_base finished at 06:39 UTC after 32.1 minutes"; usual "21-26 minutes" | https://vinted.slack.com/archives/C09LSRCM18W/p1791355346727409?thread_ts=1791350584.987609&cid=C09LSRCM18W |
| #finance-dsa | added the vita-jira integration to the team's jira project for incident follow-ups | — | https://vinted.slack.com/archives/C076F6CME10/p1791357938187639?thread_ts=1791357938.187639&cid=C076F6CME10 |
| #analytics-engineering | **proposed linter rule m020**, "data tests should not read a downstream model" (dataverse-cli#735), with comments open until 16 oct | "we have 49 cases"; buildable "caused 11 tests not to run" | https://vinted.slack.com/archives/C03JBPN0Q1W/p1791361148128839?thread_ts=1791361148.128839&cid=C03JBPN0Q1W |
| #dataverse-code-review | fixed codeowners in 4 repos to match component ownership | — | https://vinted.slack.com/archives/C04KMGDQ11D/p1791362734533299?thread_ts=1791362734.533299&cid=C04KMGDQ11D |
| #finance-dsa | split transactions and vas orders by payment provider (pr 2485), 33 replies | "(+2 models, existing 2 models modified)" | https://vinted.slack.com/archives/C076F6CME10/p1791364058834239?thread_ts=1791364058.834239&cid=C076F6CME10 |
| #fin-control_and_analytics | picked up the chargeback split and added finance as rfc reviewers | — | https://vinted.slack.com/archives/G01A7KGHY74/p1791367045572619?thread_ts=1790169655.631199&cid=G01A7KGHY74 |
| #fin-control_and_analytics | **provider split ready for review** (FDSA-3392) | "the totals match pigment exactly for may to september 2026"; "UK is 75% checkout, FR/DE/ES/NL ~70% mangopay, US/PL and the nordics ~80% adyen"; "checkout went from 27% to 56% in one month"; "the US grew from 8k to 20.3m transactions a month"; "wallet balance pays 15–18% of transactions and 44–52% of vas orders"; "free vas orders (5–12% of vas orders)" | https://vinted.slack.com/archives/G01A7KGHY74/p1791379017565189?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| #ext-vinted-mangopay-data-reporting | flagged missing columns and a suspected row cap on mangopay's new reports api | "11 columns"; "exactly 200,000 rows for a 15-minute window and 850,000 for an hour" | https://vinted.slack.com/archives/C09JTT5NYPP/p1791379389568389?thread_ts=1791295471.931699&cid=C09JTT5NYPP |
| #fin-control_and_analytics | governance: disagreed with keeping the metrics outside looker, and proposed a separate model instead | — | https://vinted.slack.com/archives/G01A7KGHY74/p1791384712751429?thread_ts=1790148016.670809&cid=G01A7KGHY74 |

### thu 8 oct

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #boa-finsys-dsa | proposed a short-term fix to catch missing customers and currencies (isaf-oss-tool-service#183) | — | https://vinted.slack.com/archives/C09A63VS421/p1791439172792979?thread_ts=1790933676.957659&cid=C09A63VS421 |
| #data-platform-support | proposed task-level success messages in the scheduler (dataverse-cli#733) | — | https://vinted.slack.com/archives/C059T9KAF8X/p1791438958525039?thread_ts=1791438958.525039&cid=C059T9KAF8X |
| #finance-dsa | review: move the not_null check into the post-hook, so it stops the export, and check the seed against the chart of accounts | — | https://vinted.slack.com/archives/C076F6CME10/p1791441490135789?thread_ts=1790157470.446499&cid=C076F6CME10 |
| #fin-control_and_analytics | told daniel the metrics go to a new mart and fp&a's business metrics stay untouched | — | https://vinted.slack.com/archives/G01A7KGHY74/p1791449919427009?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| #finance-dsa | coached emily on when a change needs an rfc, and reflected that he should spot architectural patterns earlier | — | https://vinted.slack.com/archives/C076F6CME10/p1791453197014739?thread_ts=1791378662.435629&cid=C076F6CME10 |
| #finance-dsa | summarised the mart naming discussion in a pr 2485 comment | — | https://vinted.slack.com/archives/C076F6CME10/p1791456072717479?thread_ts=1791364058.834239&cid=C076F6CME10 |
| #dataverse-code-review | friction with igor over a slow codeowners review. jeremy asked how he could have phrased it better and proposed a call | — | https://vinted.slack.com/archives/C04KMGDQ11D/p1791458783587539?thread_ts=1791362734.533299&cid=C04KMGDQ11D |
| #finance-dsa | reorganised the mec tasks page after the retro, by working day and blocker | "content all remains the same - changes are only organisational" | https://vinted.slack.com/archives/C076F6CME10/p1791463236575929?thread_ts=1791463236.575929&cid=C076F6CME10 |
| #finance-dsa | added the payment provider shares dashboard (dataverse-groupfunctions-looker#2077) | — | https://vinted.slack.com/archives/C076F6CME10/p1791465580353849?thread_ts=1791465580.353849&cid=C076F6CME10 |
| #fin-control_and_analytics | **shipped `mrt_payment_provider_shares` and the looker dashboard**, and closed the request | — | https://vinted.slack.com/archives/G01A7KGHY74/p1791466380169449?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| #ae-hiring-panel | more hiring guide prs: scorecard guidance (#11), plus #13 and #14 | — | https://vinted.slack.com/archives/C0BPJ3MQV71/p1791468039871069?thread_ts=1791468039.871069&cid=C0BPJ3MQV71 |
| #science-and-analytics-guild | pooled prior work on dashboard building with claude, shared his prompts, and proposed a shared skill | — | https://vinted.slack.com/archives/C02JMNFS9GD/p1791470970290679?thread_ts=1790155270.509419&cid=C02JMNFS9GD |

### fri 9 oct (to 10:10)

| channel | summary | figures as stated | permalink |
| --- | --- | --- | --- |
| #dataverse_finance_monitoring | traced 2 vas orders that were genuinely free, and scoped the check to orders above €0 (pr 2503) | orders "61444868 and 61447750"; the warning would "repeat every day until April 2027" | https://vinted.slack.com/archives/C0706RCL6CF/p1791527453319229?thread_ts=1791525684.894619&cid=C0706RCL6CF |
| #analytics-engineering | re-opened dbt native unit testing on ctes, with community support (dbt-labs/dbt#8425) | — | https://vinted.slack.com/archives/C03JBPN0Q1W/p1791529401095519?thread_ts=1791529401.095519&cid=C03JBPN0Q1W |

---

## recognition from others

| date | who | channel | quote | permalink |
| --- | --- | --- | --- | --- |
| 29 sep | berkay koçak | #marketing_dsa_scheduler_alerts | "looks really thorough Jeremy, thanks a lot for all the effort on this :muscle:" | https://vinted.slack.com/archives/C08RJRPV4F7/p1790669377765429?thread_ts=1790574132.503559&cid=C08RJRPV4F7 |
| 29 sep | stuti nigam | #ae-hiring-panel | "I love this :smile: ... who needs to find time when they have Jeremy :joy: I must have done something right to get him on the panel.:mvp:" | https://vinted.slack.com/archives/C0BPJ3MQV71/p1790695329565529?thread_ts=1790685817.910629&cid=C0BPJ3MQV71 |
| 29 sep | matteo fiorani | #ae-hiring-panel | "Thanks Jeremy, I approved all of them." | https://vinted.slack.com/archives/C0BPJ3MQV71/p1790687407438229?thread_ts=1790686124.499519&cid=C0BPJ3MQV71 |
| 29 sep | antónio fitas | #finance-dsa | "Thanks for the suggestions Jeremy" | https://vinted.slack.com/archives/C076F6CME10/p1790670360506509?thread_ts=1790587981.961529&cid=C076F6CME10 |
| 30 sep | ieva miliauskaitė | #fin-control_and_analytics | "Thanks a lot for the solution Jeremy:v-care:" | https://vinted.slack.com/archives/G01A7KGHY74/p1790777862509409?thread_ts=1790248880.358479&cid=G01A7KGHY74 |
| 30 sep | júlia solé cubilo | #finance-dsa | "followup of your suggestion Jeremy ... thank you :thank-u:" (pr 2419) | https://vinted.slack.com/archives/C076F6CME10/p1790779995102659?thread_ts=1790157470.446499&cid=C076F6CME10 |
| 1 oct | yirong lo | #dataverse-buyer-alerts | "Thanks Jeremy! This is awesome" (partition alerts) | https://vinted.slack.com/archives/C06CS5E2AFM/p1790844380295139?thread_ts=1790843951.733179&cid=C06CS5E2AFM |
| 1 oct | tomas radavičius | #fin-control_and_analytics | "thanks for asking these questions ... I think this way we'll get much more accurate data and which will be clear to both sides" | https://vinted.slack.com/archives/G01A7KGHY74/p1790859571277059?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| 2 oct | antónio fitas | #boa-finsys-dsa | "Thanks Jeremy, option 2) aligns with the Hub ideas so I would suggest going for it + generalize the as an architecture design" | https://vinted.slack.com/archives/C09A63VS421/p1790934542164599?thread_ts=1790933676.957659&cid=C09A63VS421 |
| 2 oct | marija krištapavičiūtė | #fin-control_and_analytics | "thank you Jeremy. We will manual adjust the file." | https://vinted.slack.com/archives/G01A7KGHY74/p1790934259487099?thread_ts=1790930834.202579&cid=G01A7KGHY74 |
| 2 oct | hamid aghadadashli | #data-platform-support | "Hi Jeremy, many thanks for the clarifications :slightly_smiling_face: I will follow this going forward." | https://vinted.slack.com/archives/C059T9KAF8X/p1790953558093269?thread_ts=1790952363.834369&cid=C059T9KAF8X |
| 6 oct | agnė matačiūnaitė | #fin-control_and_analytics | "Thanks Jeremy!" (the 33.9k reclass finding) | https://vinted.slack.com/archives/G01A7KGHY74/p1791271807063369?thread_ts=1791264406.708729&cid=G01A7KGHY74 |
| 8 oct | tomas radavičius | #fin-control_and_analytics | "The results are very close, so yes, data is as expected." | https://vinted.slack.com/archives/G01A7KGHY74/p1791450605505329?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| 8 oct | daniel arango | #fin-control_and_analytics | "Jeremy That works, thanks!" | https://vinted.slack.com/archives/G01A7KGHY74/p1791451996400679?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| 8 oct | tomas radavičius | #fin-control_and_analytics | "Jeremy thank you!:pepe_thnx_sign::mvp:" | https://vinted.slack.com/archives/G01A7KGHY74/p1791466948373199?thread_ts=1790148016.670809&cid=G01A7KGHY74 |
| 8 oct | júlia solé cubilo | #finance-dsa | "we are going to a conference in Paris in November. Jeremy is presenting and in the end all of us are going!" | https://vinted.slack.com/archives/C076F6CME10/p1791462964816519?thread_ts=1791462964.816519&cid=C076F6CME10 |

**critical feedback, for growth.** igor bobić (#dataverse-code-review, 8 oct): "I don't know think this is a very nice way to communicate. Maybe you don't mean it that way, but it comes off a bit like you think this is not worth your time but is mine" — https://vinted.slack.com/archives/C04KMGDQ11D/p1791458451060299?thread_ts=1791362734.533299&cid=C04KMGDQ11D. jeremy then asked how he could have phrased it and proposed a call.

---

## confluence

### pages created in the window

| page | what he did | figures stated | url |
| --- | --- | --- | --- |
| 2026-10-07 - data tests read only the model they test and what is built before it (rfc, wip, v2) | wrote the rfc after incident 6848. it proposes one rule, 4 fix patterns and 5 prs (#2487–#2491), plus linter rule m020 (dataverse-cli #735) | "stopped the finance daily DAG for about 4 hours"; "each holds 6,803,333,003 rows"; required currencies scan "31.7 GiB → 2 small seeds"; adyen bpar "331.7 GB (dry run) → 3.1 GB"; m020 "ran over every prod manifest: 58 projects and 8,274 models. It flags 49 tests in 11 projects"; "11 of the 39 tests on `prep_invoice_lines` would then never run on schedule"; vgo pro "188,081.02 export − 190,900.00 payouts = −2,818.98 movement"; "€1.67 more revenue" | https://vinted.atlassian.net/wiki/spaces/DF/pages/32320717248 |
| 2026-10-07 - rfc chargeback split accounting import file (wip, v5) | proposed a dbt journal file to replace the manual chargeback split. sets 7 ifrs-based principles, 4 decisions and 10 questions for finance control and accounting | september 2026 net: adyen "385,185", checkout "336,330", mangopay "189,660", total "911,175" eur, "35,457 rows"; checkout funding lines "−2,361,414"; mangopay "€1,851,527 over 30,125 rows"; "within the €1,000 trivial threshold" | https://vinted.atlassian.net/wiki/spaces/DF/pages/32322650572 |
| 2026-09: mec issue & request log (live doc, co-authored with júlia) | created 1 oct. records each close issue with root cause, mitigation, long-term fix and owner. his rows: trendsales, voucher division by zero, vinted pay wd1 snapshot, netsuite regeneration, the static adyen invoice prep, the 700006/700007 split and incident 6848 | "338,588 more Vinted Inc lines ... worth USD 235,009 (VAT USD 3,298)"; august gap "387,264 lines and USD 171,925"; "NetSuite also rejected 71 of 3,030 invoices, because 4 customers were missing currencies"; "all 328,933,345 Adyen rows in the 08:54 snapshot have no invoice"; 700006 "EUR 389k in August to EUR 291k in September", "would be EUR 325.1k"; identity checks "took 79% of the EUR 60.6k EU marketplace invoice"; refund estimates "off by EUR 956k on 3 metrics" (júlia's row) | https://vinted.atlassian.net/wiki/spaces/DF/pages/32294830083 |

### pages edited in the window

| page | last edit | what changed | figures stated | url |
| --- | --- | --- | --- | --- |
| 2026-09-07 - self-service data refresh for finance (rfc, in review, v18) | 6 oct, by jeremy | "Proposal: no-schedule Airflow tasks with a success message, per DPX's answer (DPSUP-3382); first job FDSA-3556" | "median 6.3 h"; "62 refresh requests ... still need an engineer"; "Slowest tenth wait ~143 h (six days)"; "45%" raised in the first 4 working days; finance waiting "~400 h, about 0.2 FTE"; engineer time "62–83 h, or 8–10 engineer-days"; the first 3 jobs "cover 40 of the 62 requests (65%)" | https://vinted.atlassian.net/wiki/spaces/DF/pages/32174703071 |
| finance dsa — alert case log (v34) | 8 oct, by jeremy | "8 Oct curation - alert volume down 12 to 3; Adyen download SLO miss" | alert volume "down 12 to 3" | https://vinted.atlassian.net/wiki/spaces/DF/pages/32104972550 |
| 2026-08-18 - governed mart for shipping discount campaigns (rfc, in review, v47) | 6 oct, by jeremy | no version message | — | https://vinted.atlassian.net/wiki/spaces/DF/pages/32088817762 |
| 2026-08-24 - continuity for alert triage (approved, live doc) | 6 oct, by jeremy | status shows approved; "Phases 1 to 3 are merged" | — | https://vinted.atlassian.net/wiki/spaces/DF/pages/32111329441 |
| 2026-08-20 - split mrt_shipping_results into components (approved, live doc) | 7 oct, by jeremy | status shows approved; "shipped in one pull request, #2222" | "2 dimension tables, 5 preparation models and 2 shared macros" | https://vinted.atlassian.net/wiki/spaces/DF/pages/32099795441 |
| mec tasks (v632) | latest edit 8 oct by someone else | slack shows jeremy edited it on 6 oct (copy-paste config) and 8 oct (reorganised by working day and blocker, after the retro) | — | https://vinted.atlassian.net/wiki/spaces/DF/pages/29110141095 |
| how to set up access to mangopay s3 (v3) | 5 oct, by someone else | "add how to read the keys from secret manager in colab". jeremy's own edit may fall before the window | — | https://vinted.atlassian.net/wiki/spaces/DF/pages/30984568937 |
| how to fix mangopay s3 issues (v5) | 2 oct, by someone else | jeremy's own edit may fall before the window | — | https://vinted.atlassian.net/wiki/spaces/DF/pages/30418370576 |

### comments on others' pages

| date | page | comment | url |
| --- | --- | --- | --- |
| 7 oct | 2026-10-07 - financial planning prep models refactor | "is it possible to add a diagram using excalidraw?" | https://vinted.atlassian.net/wiki/spaces/DF/pages/32322552013/2026-10-07+-+Financial+planning+prep+models+refactor?focusedCommentId=32323010951 |
| 30 sep | mec tasks | "thanks!" | https://vinted.atlassian.net/wiki/spaces/DF/pages/29110141095/MEC+Tasks?focusedCommentId=32288605050 |

### vinted values page (29905420289)

**the page has not changed since the local snapshot.** version 62. lastModified `2026-09-25T05:58:42.385Z`, with no version message. this matches the local snapshot of 25 sep 05:58, assuming that time is utc.
