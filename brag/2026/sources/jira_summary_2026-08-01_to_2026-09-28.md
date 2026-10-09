# jira contributions, 2026-08-01 to 2026-09-28

source: `(assignee = currentUser() OR reporter = currentUser()) AND updated >= "2026-08-01"`, 157 tickets, all created on or after 2026-08-03. full list in `jira_tickets.tsv`. every number below is quoted from a ticket description. none is inferred from a summary line.

## totals

| status | tickets |
| --- | --- |
| done | 110 |
| to do | 20 |
| in progress | 12 |
| aborted | 7 |
| in review | 5 |
| blocked | 2 |
| won't do | 1 |
| **total** | **157** |

- **resolved in window:** 117 (110 done, 7 aborted).
- **by type:** 76 task, 45 bug/incident, 32 subtask, 2 story, 2 idea.
- **raised by jeremy himself:** 122 of 157.
- **month-end close subtasks** (created by jira automation, all done): 7 (FDSA-3217, 3218, 3219, 3222, 3223, 3224, 3226).

### stakeholder requests served (tickets with "requested by:")

20 intake tickets. 18 done, 1 to do (FDSA-3392), 1 blocked (FDSA-3410). FDSA-3315 names jeremy as requester, though ieva raised it.

| requester | domain | tickets |
| --- | --- | --- |
| ieva miliauskaitė | shipping / finance data control | 5: FDSA-3189, 3239, 3315, 3388, 3410 |
| evita mikšytė | marketplace data control (MDC) | 4: FDSA-3120, 3133, 3237, 3250 |
| martyna grigaitytė | shipping data control (SDC) | 2: FDSA-3238, 3247 |
| gabija šleiniūtė | MFDC | 2: FDSA-3135, 3275 |
| kristupas klevečka | accounting GL | 2: FDSA-3108, 3411 |
| matas jaučeras | marketplace data control | 1: FDSA-3243 |
| šarūnė lukošiūtė-kumar | accounts payable | 1: FDSA-3265 |
| uršulė sadauskaitė | FP&A | 1: FDSA-3287 |
| daniel arango | FP&A | 1: FDSA-3312 |
| salvijus jasiūnas | payments finance | 1: FDSA-3392 |

**by domain:** shipping / finance data control 7, marketplace data control 5, MFDC 2, GL 2, FP&A 2, accounts payable 1, payments finance 1.

5 were marked "1. high: critical business blocked": FDSA-3238, 3243, 3247, 3287, 3392.

some work others assigned outside the intake form: emily broderick (FDSA-3067, 3194, 3204), antónio fitas (FDSA-3047, 3090, 3370), júlia solé cubilo (FDSA-3054, 3274), samanta vasilenkaitė (FDSA-3143).

### incidents he led

- FDSA-3330: retries appended 3 snapshots per daily model on 10 sep.
- FDSA-3318 and FDSA-3302: 34 duplicate snapshots across 10 models.
- FDSA-3332: every cdd run failed at parse time.
- FDSA-3277: wrong AU vendor card in the august month-end close.
- FDSA-3067, 3123, 3124: mangopay S3 load silently skipped a month's files.
- FDSA-3206: out-of-memory failure on prep_adyen_payment_processing_fees.
- FDSA-3138: pii asset check hotfix.
- FDSA-3333: snapshot tests failing in ci.
- FDSA-3169 was a follow-up he scoped after `inc-2026-08-25-dimuseraddresses-to-many-partitions-22659`.

---

## 1. snapshot integrity (duplicate snapshots in prod)

**[FDSA-3302](https://vinted.atlassian.net/browse/FDSA-3302) guard finance snapshots against duplicate runs** (done)
- **what went wrong:** a retriggered run on 2 sep snapshotted mrt_payment_processing_fees twice. looker then showed vinted uab payment fees about €1.5m higher (jul €1,317,667.13 vs aug €2,815,521.66). reported figures were unaffected, because only one snapshot was imported downstream.
- **technical:** added a one-snapshot-per-day test on every snapshot model (PR 2232). the 13 monthly models also warn on a second snapshot in the same month.

**[FDSA-3318](https://vinted.atlassian.net/browse/FDSA-3318) delete duplicate snapshots from prod** (done)
- **what:** scanned all 18 snapshot tables. 10 models held 34 duplicate snapshots, going back to march 2025. the ticket that raised it had listed 6.
- **numbers:** in each pair, the earlier snapshot was the incomplete one. snap_payment_processing_fees on 2025-04-03 held 37,202,254 rows, then 184,227,077. snap_financial_planning_actuals on 2026-03-03 held 5.1m rows, a doubled load, against 2.6m.
- **technical:** one pr per model, so each owner could sign off separately.

**[FDSA-3330](https://vinted.atlassian.net/browse/FDSA-3330) incident: retries appended three snapshots per daily model** (done)
- **what:** the new test failed on the first run. each airflow retry then added another snapshot: 924,552 rows ×3 and 471,220 rows ×3. cleaned up 10 sep 05:52–05:55 UTC, and the run went green.

**[FDSA-3331](https://vinted.atlassian.net/browse/FDSA-3331) make snapshots replace the same-day snapshot** (done)
- **technical:** fixed the root cause. 13 snapshot models moved to insert_overwrite by day, a config change with no sql rewrite. a unit test proves a rerun replaces the day's snapshot.

**[FDSA-3333](https://vinted.atlassian.net/browse/FDSA-3333)** (done)
- **what:** fixed 18 per-day tests that failed on every pr, because ci builds snapshots twice. they now error in prod and warn elsewhere.

## 2. month-end close and accounting exports

**[FDSA-3234](https://vinted.atlassian.net/browse/FDSA-3234), [3267](https://vinted.atlassian.net/browse/FDSA-3267), [3268](https://vinted.atlassian.net/browse/FDSA-3268) automate close CSV exports** (done)
- **business impact:** vouchers accrual, vgo pro wallet and 2 payment fee accrual exports no longer need a hand export and upload. the voucher step sat on the critical path for the 9 AM CET WD1 deadline.
- **technical:** each export now reuses the shared export post-hook.

**[FDSA-3277](https://vinted.atlassian.net/browse/FDSA-3277) fix AU customer vendor in payment fees accrual** (done)
- **what went wrong:** a GL accountant (rasa) had to fix the august file by hand. 5 AUD rows, AUD 85,991.59, moved from card 494369 to 451070.
- **technical:** documented the split between wallet cards and vendor-expense cards on the seed. added unique and not_null tests.

**[FDSA-3256](https://vinted.atlassian.net/browse/FDSA-3256), [3262](https://vinted.atlassian.net/browse/FDSA-3262), [3263](https://vinted.atlassian.net/browse/FDSA-3263) debit/credit sign guards** (done)
- **what went wrong:** a group netting negative would send netsuite a negative debit or credit, which it rejects. this was real: a group netted -6 EUR in the 2025-12-02 discount coverages snapshot. extra service came close, with a smallest balancing row of GBP 4.48 and 4.5m negative rows upstream.

**[FDSA-3317](https://vinted.atlassian.net/browse/FDSA-3317) exclude SECOND_CHARGEBACK from adyen fee estimates** (done)
- **what went wrong:** a payments change would have double-counted about €2,800–3,500 a month, spread across the wrong fee groups. fixed before the payments pr merged.
- **technical:** added an accepted_values test on action_type.

**[FDSA-3189](https://vinted.atlassian.net/browse/FDSA-3189) exclude SPEEDX carrier costs** (done, ieva)
- **what:** july's shipping result double-counted SPEEDX costs, and finance had to correct them by hand. august close shipped with the fix.

**[FDSA-3260](https://vinted.atlassian.net/browse/FDSA-3260)** (done)
- **what:** replaced a manual close check on the accrual breakdown with automated assertions.

**[FDSA-3278](https://vinted.atlassian.net/browse/FDSA-3278)** (done)
- **what:** retired the flash report model, which had no queries in 90 days.

## 3. shipping result

**[FDSA-3285](https://vinted.atlassian.net/browse/FDSA-3285) split mrt_shipping_result** (done)
- **what:** broke a ~1,200-line model into 2 dims, 5 preps and 2 macros, in one pr.
- **validated:** full-row hash diff against prod.
- **technical:** the 2 cost and revenue preps are views, which avoids doubling storage on a 2.3 TB mart.

**[FDSA-3388](https://vinted.atlassian.net/browse/FDSA-3388) september actuals refresh** (done, ieva)
- **what:** checked vgo's full refresh first. all 1,361 partitions had been rewritten. the refresh picked up 14.2m more invoiced august legs (69.8m to 84.0m).

**[FDSA-3390](https://vinted.atlassian.net/browse/FDSA-3390) run shipping result daily, gated on the shared dates** (in review)
- **business impact:** removes the manual refresh request. FDSA-3388 was the third such request since august.
- **technical:** covers 11 models.

**[FDSA-3414](https://vinted.atlassian.net/browse/FDSA-3414)** (in progress)
- **what:** the same gate for the vgo carrier invoice breakdown. off days bill 0 bytes. scheduled days bill 7.1 TiB, and september already has 4 snapshots.

**[FDSA-3319](https://vinted.atlassian.net/browse/FDSA-3319)** and **[FDSA-3408](https://vinted.atlassian.net/browse/FDSA-3408)** (done)
- **what:** moved the full refresh dates into one shared macro, so finance and vgo no longer keep two lists. agreed with the vgo team.

**[FDSA-3090](https://vinted.atlassian.net/browse/FDSA-3090) shipping campaigns mart** (in progress, antónio)
- **what:** replaces a hand-edited query with a mart plus seeds. 10 subtasks.

## 4. data quality and controls

**[FDSA-3299](https://vinted.atlassian.net/browse/FDSA-3299) controls on escrow revenue** (in review)
- **headline:** the monthly review query groups august into 67,443 rows but stops at `LIMIT 500`. so the review sees under 1% of cases.
- **new tests:** tier 1 tests validated over 1.15bn lines and six months.
- **defects found:** 212 lines where the VAT amount is off by more than €10 (~€10,700). 43,389 lines coded GB rather than UK. 4,948 lines on the wrong invoice series.

**[FDSA-3413](https://vinted.atlassian.net/browse/FDSA-3413) / [3415](https://vinted.atlassian.net/browse/FDSA-3415) GB vs UK VAT country** (in progress / blocked)
- **what:** traced ~44k lines a month (against ~54m UK) to 2 code paths in core billing. these show as a separate country in the monthly iSAF review.

**[FDSA-3328](https://vinted.atlassian.net/browse/FDSA-3328) compensations with no split** (done)
- **what:** 8,103 compensations got a case but no coverage split, totalling €121,667. general ledger entries were unaffected.
- **technical:** a new invariant test holds on 14,945,083 rows.

**[FDSA-3329](https://vinted.atlassian.net/browse/FDSA-3329)** (done)
- **what:** found that the refund estimates fact strips the reporting category from 3,675,013 rows on the 2025 plan. every other model keeps it.

**[FDSA-3387](https://vinted.atlassian.net/browse/FDSA-3387) null prior_month_invoice_amount_due** (done)
- **what:** the incremental window nulled the earliest month of every series. the full refresh repaired 39 rows.
- **technical:** fix plus a unit test that fails on main.

**[FDSA-3370](https://vinted.atlassian.net/browse/FDSA-3370) payment reversal status** (done, antónio)
- **what:** cancelled transactions showed a 0.0% reversal rate after an upstream change. the true rate is ~100%. switched the source to dim_payments.

**[FDSA-3417](https://vinted.atlassian.net/browse/FDSA-3417)** (in progress)
- **what:** adds completeness tests on the 2 unmonitored AU and US CDC sources, and names the owner on all 5.

**[FDSA-3324](https://vinted.atlassian.net/browse/FDSA-3324)** (done)
- **what:** tested the declared grain of the xendo tax reconciliation: 2,847,255 combinations, no duplicates.

**[FDSA-3313](https://vinted.atlassian.net/browse/FDSA-3313)** (to do)
- **what:** measured 473 double entries out of ~896m that do not net to zero. 2 groups look like defects.

**[FDSA-3120](https://vinted.atlassian.net/browse/FDSA-3120) / [3130](https://vinted.atlassian.net/browse/FDSA-3130)** (done, evita)
- **what:** a 36-character VAT number blocked a pro seller's VMI upload for months. added a 35-character length test.

## 5. platform, migration and cost

**[FDSA-3169](https://vinted.atlassian.net/browse/FDSA-3169) partition monitoring** (done)
- **what went wrong:** after the dim_user_addresses incident (20 upstream_failed tasks), an audit found 121 models at risk of hitting partition limits. one table held 9,922 of 10,000 partitions, about 78 hours of headroom.
- **technical:** built daily monitoring with alerts routed to each owning team.
- **follow-up:** [FDSA-3203](https://vinted.atlassian.net/browse/FDSA-3203) fixed the projected breach date.

**[FDSA-3149](https://vinted.atlassian.net/browse/FDSA-3149), [3194](https://vinted.atlassian.net/browse/FDSA-3194), [3291](https://vinted.atlassian.net/browse/FDSA-3291) legacy bucket migration** (done)
- **what:** moved accounting exports to the new buckets. pointed the iSAF service (oss-platform-service) at the new bucket through a configurable env var. notified 10 active sandbox users.

**[FDSA-3306](https://vinted.atlassian.net/browse/FDSA-3306)** (done)
- **what:** added exposures for GCS exports to iSAF, the austrian tax authority, sovos, netsuite (11 models) and pigment (10). while inventorying them, found 2 exports still writing to legacy buckets.

**[FDSA-3190](https://vinted.atlassian.net/browse/FDSA-3190)** (done)
- **what:** tagged 120 of 302 models so continuous deployment (cdd) never builds them.

**[FDSA-3332](https://vinted.atlassian.net/browse/FDSA-3332)** (done)
- **what went wrong:** every cdd run failed at parse on ISO timestamps.
- **technical:** fixed with `fromisoformat`.

**[FDSA-3206](https://vinted.atlassian.net/browse/FDSA-3206)** (done)
- **what:** fixed the prep_adyen_payment_processing_fees out-of-memory failure.

**[FDSA-3067](https://vinted.atlassian.net/browse/FDSA-3067), [3123](https://vinted.atlassian.net/browse/FDSA-3123), [3124](https://vinted.atlassian.net/browse/FDSA-3124), [3128](https://vinted.atlassian.net/browse/FDSA-3128) mangopay S3** (done)
- **what went wrong:** a retry during the july close skipped that month's files.
- **technical:** fixed pagination, added a completeness comparison and an extracted_at column.

## 6. code health and dbt upgrade readiness

**[FDSA-3274](https://vinted.atlassian.net/browse/FDSA-3274)** (done, júlia)
- **what:** split mrt_double_entry into per-source prep models. output unchanged.

**[FDSA-3281](https://vinted.atlassian.net/browse/FDSA-3281)** (done)
- **what:** cleared deprecation warnings: PropertyMovedToConfig 103 → 65, missing-arguments 13 → 0.
- **validated:** all 930 test nodes are identical in the manifest.
- **related:** [FDSA-3075](https://vinted.atlassian.net/browse/FDSA-3075).

**[FDSA-3320](https://vinted.atlassian.net/browse/FDSA-3320)** (done, 3 repos)
- **what:** moved unit test yml files out of the paths dbt parses, which is a hard error in dbt 2.0.

**[FDSA-3071](https://vinted.atlassian.net/browse/FDSA-3071), [3153](https://vinted.atlassian.net/browse/FDSA-3153), [3054](https://vinted.atlassian.net/browse/FDSA-3054)** (done)
- **what:** lint sweeps. 3054 fixed 10 exposed_pii models before M003 enforcement.

**[FDSA-3326](https://vinted.atlassian.net/browse/FDSA-3326) / [3327](https://vinted.atlassian.net/browse/FDSA-3327)** (done / in progress)
- **what:** 3326 collapsed ~100 lines of struct padding. 3327 replaces 25 copies of one business rule with a macro.

**[FDSA-3334](https://vinted.atlassian.net/browse/FDSA-3334)** (in progress, now with paulius)
- **what:** found 806 mock files and 6,206 rows. 9 tests hold 2,028 of those rows. one mock has drifted from the seed.

**[FDSA-3409](https://vinted.atlassian.net/browse/FDSA-3409)** (to do)
- **what:** laptop tooling differs from the CI image on 94 of 182 packages.

## 7. ai-assisted review and alert triage

**[FDSA-3160](https://vinted.atlassian.net/browse/FDSA-3160)–[3165](https://vinted.atlassian.net/browse/FDSA-3165) alert triage bot, phases 1–4** (done; phase 5 to do)
- **what:** gave the SLO report its own agent. set an escalation target, which had been empty, so a thumbs-down reached nobody. triage now reports the offending value and whether the data or the test is at fault. it reads an alert case log instead of re-deriving, and runs a nightly handover.

**[FDSA-3307](https://vinted.atlassian.net/browse/FDSA-3307)** (done)
- **what:** reviewed human comments on prs #2176–#2235. turned 11 classes of finding into bugbot rules. one prevented case would have unlabelled 437,042 transactions.

**[FDSA-3308](https://vinted.atlassian.net/browse/FDSA-3308), [3086](https://vinted.atlassian.net/browse/FDSA-3086), [3087](https://vinted.atlassian.net/browse/FDSA-3087)** (done)
- **what:** pr-description skill, bugbot iteration and agent research.

## other

- **[FDSA-3102](https://vinted.atlassian.net/browse/FDSA-3102):** technical interview document reviews.
- **[FDSA-3047](https://vinted.atlassian.net/browse/FDSA-3047):** onboarding.
