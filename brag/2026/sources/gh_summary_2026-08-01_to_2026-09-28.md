# Jeremy Chia — GitHub contributions, 2026-08-01 to 2026-09-28

Source files: `gh_prs.tsv` (454 authored PRs), `gh_reviews.tsv` (140 PRs reviewed that others wrote). Every number below is quoted from the PR body. Nothing is inferred from a title.

## Totals

**454 PRs authored: 424 merged, 12 open, 18 closed.** 331 opened in August, 123 in September.

| repo | merged | open | closed |
|---|---|---|---|
| vinted/dataverse-finance | 389 | 11 | 15 |
| vinted/v-assist-registry | 10 | | |
| vinted/terraform-github | 5 | | |
| vinted/dataverse-metrics | 4 | | |
| vinted/dataverse-dbt-shared | 3 | | 1 |
| vinted/terraform-dataverse | 2 | | 2 |
| vinted/dataverse-cli | 2 | | |
| vinted/dataverse-vintedgo-dbt | 2 | | |
| vinted/dataverse-cicd, dataverse-vunit, dataverse-lookml-generator, dataverse-marketplace-intelligence, oss-platform-service, service-catalog | 1 each | | |
| vinted/core | | 1 | |
| dbt-labs/dbt-external-tables (open source) | 1 | | |

**39 PRs in 15 repos outside dataverse-finance.**

Of the 415 dataverse-finance PRs, 316 are single-file slices of 5 sweeps: 173 dbt 1.11 deprecation fixes, 75 M017 lint fixes, 51 M008 unit tests, 10 snapshot cleanups, 8 other lint fixes.

**Reviews: 140 PRs by other people** (131 merged, 3 open, 6 closed). 69 in August, 71 in September.
- by author: emily-broderick 41, juliasolee 27, Samantava 21, veda-patil 9, berendgreijnvinted 6, vinted-stutinigam 5, vanwelljanou 4, 4 bot PRs, and 15 other people with 1 to 3 each.
- by repo: dataverse-finance 103, dataverse-groupfunctions-dbt 12, v-assist-registry 6, dataverse-sustainability 5, terraform-github 3, service-catalog 2, dataverse-groupfunctions-looker 2, ae-hiring-material 2, and 1 each in terraform-dataverse, financial-forecast, dataverse-people, dataverse-custom-data-ingestion, dataverse-cli.

---

## 1. Month-end close: automation and correctness

**Headline: 2 cost-accrual errors worth about €1.3m found and fixed. 4 manual close steps now run automatically. 3 manual close checks became dbt tests.**

- **[#2361](https://github.com/vinted/dataverse-finance/pull/2361) Accrue fees on the payment status, not the checkout attempt status.** A change upstream on 27 aug meant cancelled purchases no longer showed as refunded.
  - business: "about €1.29m of cost was carried out of august that should have stayed there — august understated, september overstated." Months already closed do not move.
  - technical: picks up 972,439 fee rows whose payment changed after the attempt record froze (617,127 on june transactions). The attempt table stops updating after 2 months, so late refunds had never been seen. That lowers the figure by €9,451, from €2.83m to €2.82m. The two statuses agree 99.8% of the time.
- **[#2244](https://github.com/vinted/dataverse-finance/pull/2244) Exclude SECOND_CHARGEBACK from Adyen fee estimates.** Found before payments shipped their label split.
  - business: without it, 271 extra rows worth €2,032.50 for august, heading for about 373 rows and €2,800 over a full month. That is ~0.05% of €6.31M Adyen cost, booked to the wrong fee type and the wrong countries.
  - technical: new warn test on the set of action types, so the next upstream rename raises a warning. Costs 10.6 GiB per run.
- **[#2178](https://github.com/vinted/dataverse-finance/pull/2178) Export the voucher accrual automatically, blocked if the flooring check fails.**
  - business: two fewer manual steps on working day 1 (WD1). The file can no longer be ordered or filed wrongly. The 2026-08 accrual is 972k.
  - technical: 0 violations across all 24 snapshots in prod. A deliberately broken rule blocked the export as intended. The build billed 87 MiB.
- **[#2205](https://github.com/vinted/dataverse-finance/pull/2205) and [#2207](https://github.com/vinted/dataverse-finance/pull/2207) Export the VGO pro wallet report and both fee accruals automatically.** This removes the manual WD2 export and upload steps. #2205 was "the last Accounting Splits row in the RFC without automation".
- **[#2203](https://github.com/vinted/dataverse-finance/pull/2203) 3 month-end completeness checks for payment processing fees**, which were done by hand before.
  - business: they guard the numbers that become the NetSuite accrual journals.
  - technical: no failures across 237m Adyen, 206m Mangopay and 55m Checkout rows. The tests caught all 5 kinds of deliberately broken data. About 98 GB per run, roughly £0.50.
- **[#2302](https://github.com/vinted/dataverse-finance/pull/2302) Voucher accrual mart runs daily, and the export only formats the data.** Checks now run on the current month, weeks before close.
  - technical: the booked month is unchanged, 1,232,208 rows on each side with no differing hashes. The daily run adds 1,275,608 current-month rows. It surfaced a pre-existing gap for the IE country group.
- **[#2303](https://github.com/vinted/dataverse-finance/pull/2303) Make the fee export mapping checks able to fail.** Both checks matched "0 of 1.3bn rows" in prod, so a missing mapping could reach close unchecked. Output is identical: 500 rows on each side. About +190 GiB a month.
- **[#2194](https://github.com/vinted/dataverse-finance/pull/2194), [#2197](https://github.com/vinted/dataverse-finance/pull/2197), [#2198](https://github.com/vinted/dataverse-finance/pull/2198) Put a negative amount in the opposite debit/credit column, as a positive.** NetSuite needs both columns positive.
  - #2194: 4 of 365 rows change, the largest HUF 10,785.77. Every journal still balances.
  - adds a primary key test: 365 rows, 365 distinct keys.
- **[#2212](https://github.com/vinted/dataverse-finance/pull/2212) Correct the AU vendor on the fee accrual.** It had been booked to the wrong card. August was fixed by hand: 5 AUD rows, AUD 85,991.59.
- **[#2360](https://github.com/vinted/dataverse-finance/pull/2360) Adyen reconciliation prior-month value.** 39 rows carried a false null at the edge of the reload window. Checked cell by cell against the pre-rebuild table: 39/555 invoices change, and `amount_due_check` changes on 3.
- **[#2083](https://github.com/vinted/dataverse-finance/pull/2083) Split Adyen refund fees out of payment method fees.** Finance reported the problem.
  - business: ties to Adyen's own line on all 23 affected invoices, every difference exactly 0. It agrees to the cent in 20 of 21 groups. 47 rows reclassified.
  - technical: 11,184 join keys across all history, 0 ambiguous.
- **[#2239](https://github.com/vinted/dataverse-finance/pull/2239) Invoice total including taxes in the Adyen reconciliation**, so the monthly check no longer means opening each invoice. 46 rows on each side, 0 differing. The AU invoice ties exactly: 10% GST on AUD 38,377.49 gives 42,215.24.
- **[#2186](https://github.com/vinted/dataverse-finance/pull/2186), [#2187](https://github.com/vinted/dataverse-finance/pull/2187) Mangopay reconciliation.** A failing test now logs each wallet that is off. The movement check runs on every close day, because the view was showing the previous month during close. About 7 GB per run.
- **[#2063](https://github.com/vinted/dataverse-finance/pull/2063) Map AU VAT lines to the AU VAT scheme** from 2026-08-01, so July invoices already filed to iSAF do not change.
- **[#2227](https://github.com/vinted/dataverse-finance/pull/2227)** Adds a missing seed row after a monitoring alert, and documents what the warning means. Only the 17 known lines, tracked in ZS-293, remain flagged.

## 2. Shipping result pipeline

**Headline: the carrier cost double-count was removed in time for August close. The shipping mart went from 1,206 lines to 117 with identical output. Campaigns are moving from a manual sheet to governed seeds.**

- **[#2157](https://github.com/vinted/dataverse-finance/pull/2157) Exclude SPEEDX carrier costs from 2026-08-01.** SPEEDX costs are booked to logistics costs in the ledger, so the shipping result was double-counting them. "July had to be corrected by hand for exactly this."
  - business: August drops €712k invoiced cost, €1.30M purchase rate, €1.30M expected cost and €741k accrued carrier cost, across 377,136 rows (partial month). Every month from 2025-09 to 2026-07 is unchanged.
  - technical: 7-case unit test, checked by breaking the code to confirm it fails.
- **[#2222](https://github.com/vinted/dataverse-finance/pull/2222) Split `mrt_shipping_result` into single-purpose models.** 1,206 lines down to 117. Done as 1 PR where the RFC planned 10.
  - technical: full-row hash diff over 4,003,490,208 rows, zero differences. 85 columns identical. New grain and sign tests are clean over 1.97bn cost rows, 2.03bn revenue rows and 3.57bn transactions.
- **[#2242](https://github.com/vinted/dataverse-finance/pull/2242) `is_vgo_network` flag for planning.** Adds 492k transactions on top of August's 8.40m Vinted Go, and 233k on top of July's 8.84m, with no double count.
- **Governed campaigns, replacing a hand-kept sheet:** [#2158](https://github.com/vinted/dataverse-finance/pull/2158) adds the seeds with 26 tests. [#2171](https://github.com/vinted/dataverse-finance/pull/2171) backfills 60 campaigns and 72 windows, reconciled against the 174 live rows with 0 mismatches. It also found one missing campaign, BOXNOW SI-SI (€0.34, 655 transactions). [#2381](https://github.com/vinted/dataverse-finance/pull/2381) (open) resolves 87 windows into 283 rows. It flags 17 that produce nothing, including 5 naming carriers that do not exist upstream.
- **Shared rebuild dates for close (cross-repo, FDSA-3319):**
  - [dataverse-dbt-shared#425](https://github.com/vinted/dataverse-dbt-shared/pull/425) holds the close and actuals rebuild dates in one shared macro. [dataverse-vintedgo-dbt#9472](https://github.com/vinted/dataverse-vintedgo-dbt/pull/9472) moves VGO onto it, so the two projects cannot drift apart. [#432](https://github.com/vinted/dataverse-dbt-shared/pull/432) adds November and December. Without it, neither project would have rebuilt on those close days.
  - [terraform-github#8600](https://github.com/vinted/terraform-github/pull/8600) and [#8602](https://github.com/vinted/terraform-github/pull/8602) make the code-owner rule actually work: GitHub had been silently rejecting both teams. [dataverse-dbt-shared#427](https://github.com/vinted/dataverse-dbt-shared/pull/427) documents that trap for the next person. [terraform-github#8831](https://github.com/vinted/terraform-github/pull/8831) unblocks every PR in dataverse-dbt-shared, which a retired required check had been blocking.
  - open follow-ups: [#2369](https://github.com/vinted/dataverse-finance/pull/2369) and [#2379](https://github.com/vinted/dataverse-finance/pull/2379) move 11 shipping models to rebuild only on those dates.

## 3. Performance and refactors

- **[#2175](https://github.com/vinted/dataverse-finance/pull/2175) Fix the out-of-memory failure in `prep_adyen_payment_processing_fees`.**
  - before: failed after 1,290 stages, 3.34 TiB spilled, 156 slot-hours.
  - after: 245 stages, 0 spilled, 17.2 slot-hours, completed. That is about 9 times less compute.
  - repeated scans of `dim_accounts` fell from 90 to 6. 33 of 34 CTEs are byte-identical.
- **[#2209](https://github.com/vinted/dataverse-finance/pull/2209) Split `mrt_double_entry` into one prep model per source.** The mart drops from 837 lines to 88. Byte-level checksums over 33 months and 13,177,760,627 rows are identical. Measuring the grain found two statements in the docs that were wrong.

## 4. Data quality and monitoring

- **Duplicate snapshots:**
  - [#2232](https://github.com/vinted/dataverse-finance/pull/2232) adds a one-snapshot-per-day test on all 18 snapshot models. A re-run on 2 Sep had put a ~1.5m EUR jump into Looker.
  - [#2288](https://github.com/vinted/dataverse-finance/pull/2288)–[#2297](https://github.com/vinted/dataverse-finance/pull/2297) (10 PRs) delete the existing duplicates. In `snap_compensations` alone, 7 duplicates of 8.9m–14.2m rows each.
  - [#2308](https://github.com/vinted/dataverse-finance/pull/2308) found that the `grf_finance_cdd` pipeline was paused, with 58 merges queued and never run. [#2312](https://github.com/vinted/dataverse-finance/pull/2312) stops the test failing CI on every PR that touches a snapshot.
- **Mangopay ingestion:**
  - [#2058](https://github.com/vinted/dataverse-finance/pull/2058) adds a new generic volume test `assert_row_count_within_moving_average`. It would have caught July's wallets report at 38% below average.
  - [#2067](https://github.com/vinted/dataverse-finance/pull/2067) runs it only in the first 6 days of the month. Before, one bad month re-warned about 30 times.
  - [#2064](https://github.com/vinted/dataverse-finance/pull/2064) fixes a proactive find: the S3 listing silently stopped at 1,000 files. The bucket held 604 and grows monthly.
  - [#2065](https://github.com/vinted/dataverse-finance/pull/2065) adds a completion marker. A crashed download had left 16 parts where 100+ were expected, and it was never retried. 363 prod prefixes checked, no gaps found.
  - PRs #2068 and #2075–#2082 add an arrival timestamp to the files of 8 ingestion pipelines.
- **[#2382](https://github.com/vinted/dataverse-finance/pull/2382) (open)** adds gap checks on the AU/US invoice extras that feed the tax reconciliations, and names the owner on all 5 CDC checks. Tested against incident 6593: it finds exactly the empty 15:00 UTC hour.
- **[#2300](https://github.com/vinted/dataverse-finance/pull/2300) (open)** adds 22 controls over the invoice lines that reach the iSAF tax filing, a tier 1 asset.
- **[dataverse-metrics#604](https://github.com/vinted/dataverse-metrics/pull/604) BigQuery partition-limit monitoring for all teams.** Built after incident inc-2026-08-25. Before it there were "zero `INFORMATION_SCHEMA` reads" in the repo. It covers 337 tables and flags 121 at-risk models. [#606](https://github.com/vinted/dataverse-metrics/pull/606) fixes a bug where all 7,236 of 7,236 rows claimed a breach today.
- **[dataverse-metrics#630](https://github.com/vinted/dataverse-metrics/pull/630) Fix the org-wide hourly reliability mart (DPX-590).** It had failed every attempt, with 612 test failures, leaving the tier-1 status `upstream_failed`. It removes 804 duplicate rows out of 2,280,649, and every asset keeps exactly one row.
- **[dataverse-metrics#632](https://github.com/vinted/dataverse-metrics/pull/632)** adds lint severity to the lint mart. Finance read 62 violations where the real number was 24. Grain checked on 61,023 rows.

## 5. Test coverage and unit tests

- **M008 sweep (FDSA-3153): 51 merged PRs**, each adding an incremental unit test ahead of M008 becoming an error on 1 October. Example: [#2092](https://github.com/vinted/dataverse-finance/pull/2092). [#2143](https://github.com/vinted/dataverse-finance/pull/2143) and [#2145](https://github.com/vinted/dataverse-finance/pull/2145) exempt the 9 models that cannot be tested, and say why. [#2181](https://github.com/vinted/dataverse-finance/pull/2181) rewrites all 51 test descriptions, which had grown to 60–280 words each.
- **Found that unit tests were silently not running in CI:**
  - [dataverse-cicd#220](https://github.com/vinted/dataverse-cicd/pull/220) bumps vunit in the shared runner. Finance CI had gathered 2 tests instead of 6, and `mrt_service_fee_accrual` had never been tested in CI. The same was true in dataverse-people.
  - [#2298](https://github.com/vinted/dataverse-finance/pull/2298) moves the test files outside dbt's paths. dbt deprecation warnings go from 2 to 0.
  - [dataverse-vunit#120](https://github.com/vinted/dataverse-vunit/pull/120) fixes the vunit README, which recommended the one location that breaks.
  - [dataverse-cli#705](https://github.com/vinted/dataverse-cli/pull/705) adds new org-wide linter rule C006. It found 6 files org-wide, and ships as a warning so dataverse-people's CI is not broken. 17 new tests, 517 passing.

## 6. Linting, tech debt and dbt 2.0 readiness

- **dbt 1.11 deprecations (FDSA-3075): 172 merged single-file PRs** (e.g. [#1836](https://github.com/vinted/dataverse-finance/pull/1836)), split from a ~173-file sweep so each can be reviewed alone. [#2217](https://github.com/vinted/dataverse-finance/pull/2217) clears the ones that came back afterwards. All 930 test nodes resolve identically in the manifest diff.
- **M017 import-CTE sweep (FDSA-3071): 74 merged PRs** (e.g. [#2029](https://github.com/vinted/dataverse-finance/pull/2029)), plus 8 other lint-fix PRs.
- **[dataverse-cli#700](https://github.com/vinted/dataverse-cli/pull/700) Fix a false positive in the M017 linter**, found during the sweep. Following the warning would have broken a GDPR deletion filter. 9 new tests. Across 307 finance models, issues fell from 64 to 61, with exactly 3 false positives removed.
- **[dataverse-lookml-generator#160](https://github.com/vinted/dataverse-lookml-generator/pull/160) Read dbt meta from `config.meta`.** It unblocks every repo moving off the deprecated format. Without it, measures silently disappear: "zero measures are generated" if dbt stops copying meta across. Checked on 1,046 columns.
- **[dbt-labs/dbt-external-tables#412](https://github.com/dbt-labs/dbt-external-tables/pull/412) (open source, merged 2026-09-24).** Fixes a duplicate key in the Synapse sample file, found by `dbt-autofix`.

## 7. Continuous data deployment (CDD)

- **[#2153](https://github.com/vinted/dataverse-finance/pull/2153)** tags 127 of 308 models so they do not rebuild on merge. That covers all 23 export models, including one that would have "drop[ped] a fresh csv of austrian taxpayer pii" into the prod bucket on any build.
- **[#2154](https://github.com/vinted/dataverse-finance/pull/2154)** turns CDD on and bumps the scheduler from 1.27 to 1.34. Below 1.32 the exclusion tags are ignored.
- **[#2176](https://github.com/vinted/dataverse-finance/pull/2176)** sets the state-comparison flag Data Platform asked for, so models are not falsely selected for rebuild.

## 8. Platform migration off the legacy finance project

- **[terraform-dataverse#3723](https://github.com/vinted/terraform-dataverse/pull/3723)** creates the new export buckets, 6 across 3 environments. It keeps 10-year retention on accounting and 2-year on planning.
- **[oss-platform-service#71](https://github.com/vinted/oss-platform-service/pull/71)** moves the iSAF service to the new bucket. Found along the way: stage had been reading the prod bucket all along.
- **[#2234](https://github.com/vinted/dataverse-finance/pull/2234)** repoints the last 12 export models.
- **[#2235](https://github.com/vinted/dataverse-finance/pull/2235)** adds dbt exposures for 24 export models across 5 consuming systems: iSAF, the Austrian tax report, Sovos, NetSuite and Pigment. Until now these exports had no recorded consumers in dbt's lineage.

## 9. AI tooling others use

- **v-assist-registry, the finance alert-triage bot (10 PRs):**
  - [#675](https://github.com/vinted/v-assist-registry/pull/675) fixed "~18.5 hours of avoidable lag" in the daily SLO report. It also stopped the report scoring a VGO asset: 75% becomes the correct 100%.
  - [#677](https://github.com/vinted/v-assist-registry/pull/677) is the research doc behind the rest.
  - [#846](https://github.com/vinted/v-assist-registry/pull/846) gives the SLO report its own agent. The escalation contact had been empty, so a thumbs-down reached nobody.
  - [#851](https://github.com/vinted/v-assist-registry/pull/851) makes replies name the offending value and say whether the data or the test is at fault.
  - [#878](https://github.com/vinted/v-assist-registry/pull/878) acts on Samantava's feedback on the bot.
  - [#886](https://github.com/vinted/v-assist-registry/pull/886) adds the Alert Case Log and a nightly handover.
  - [#906](https://github.com/vinted/v-assist-registry/pull/906), [#938](https://github.com/vinted/v-assist-registry/pull/938) and [#951](https://github.com/vinted/v-assist-registry/pull/951) build a deterministic page editor and verifier, passing 54 scenario checks.
  - [#1054](https://github.com/vinted/v-assist-registry/pull/1054) pauses the handover while the page write is diagnosed.
- **Cursor Bugbot review rules:** [#1817](https://github.com/vinted/dataverse-finance/pull/1817) adds 1,040 lines across 3 scoped files, with a hard boundary against duplicating the linter. [#2237](https://github.com/vinted/dataverse-finance/pull/2237) adds 6 review classes taken from every human comment on #2176–#2235. One of them is the #2184 bug, which fixed 70 rows but "would have blanked 437,042". Enabled via [terraform-github#8079](https://github.com/vinted/terraform-github/pull/8079).
- The `/pr-description` skill: #1818 and #2238.

## 10. Other teams' repos and cross-team help

- **[vinted/core#137604](https://github.com/vinted/core/pull/137604) (open, checkout-backend).** A fix at the source in the core monolith: about 44k invoice lines a month carry VAT country `GB` instead of `UK`, split roughly 17k verification fees, 20k verification shipping and 4.7k extra services. Finance-side counterpart: [#2378](https://github.com/vinted/dataverse-finance/pull/2378) (open).
- [dataverse-marketplace-intelligence#1141](https://github.com/vinted/dataverse-marketplace-intelligence/pull/1141) gives Pigment access to the weekly targets mart.
- [terraform-dataverse#3695](https://github.com/vinted/terraform-dataverse/pull/3695) gives the VGO-finance and group-applied-data runners the central Slack token.
- **AE hiring:** [service-catalog#17023](https://github.com/vinted/service-catalog/pull/17023) creates a 21-person hiring panel team. [terraform-github#8562](https://github.com/vinted/terraform-github/pull/8562) removes the whole engineering org's read access to the interview case studies.
- [dataverse-vintedgo-dbt#9086](https://github.com/vinted/dataverse-vintedgo-dbt/pull/9086) documents purpose groups in the VGO skill file.

## Proactive finds (not asked for)

- The €1.29m accrual shift from an upstream status change (#2361).
- The SECOND_CHARGEBACK rename, caught before it landed (#2244).
- Unit tests silently not running in CI, in finance and dataverse-people (cicd#220).
- The CDD pipeline paused with 58 merges queued (#2308).
- The S3 listing capped at 1,000 files (#2064).
- Stage reading the prod iSAF bucket (oss-platform-service#71).
- The M017 linter false positive that would have broken a GDPR filter (dataverse-cli#700).
- GitHub silently dropping code owners (dbt-shared#427, terraform-github#8602).
- The org reliability mart outage (dataverse-metrics#630).
