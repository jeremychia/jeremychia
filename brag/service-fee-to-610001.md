# service fee: from transaction to 610001 service fee revenue

**headline:** a service fee reaches 610001 by two routes. once the transaction is invoiced, the invoice line books it. at a month end where the checkout is paid but not yet invoiced, the in-transit accrual books it and reverses it on the 1st. only the accrual route has a file export to netsuite in this repo.

## route 1: invoiced service fee

| step | model | what happens |
| --- | --- | --- |
| 1 | `stg_cdc__core_invoice_lines` | invoice lines arrive from the core database through change data capture (cdc) |
| 2 | `int_invoice_lines` | deduplicates the cdc versions and reloads the last few days incrementally |
| 3 | `fct_invoice_lines` | adds invoice, invoice type, operation, revenue type (seed `revenue_type`) and eur rates |
| 4 | `int_revenue_account_assignation` | picks the revenue account from payments and transfers, for example "Adyen VintedBP_GB" or "MangoPay …" |
| 5 | `prep_invoice_lines` | joins the revenue account onto each line, with a legacy backfill for older lines |
| 6 | `mrt_invoice_lines` → `snap_invoice_lines` | a monthly snapshot freezes each closed month |
| 7 | `prep_double_entry_invoice_lines` | reads the snapshot from 2025 and live data for 2024. turns "Service fee" lines into sides: credit `service_fee_revenue`, debit `accounts_receivable` |
| 8 | `mrt_double_entry` | unions every source, unnests the sides and looks up the account number in seed `netsuite_accounts` (`service_fee_revenue` → 610001) |

**what the revenue line books:**
- **us, uk and au revenue accounts:** net fee to 610001, vat to tax payables, gross to receivables.
- **every other account:** the vat-inclusive amount to 610001 against receivables, with no vat side.
- **amount and currency:** adyen and vinted pay lines use the payment currency and amount. mangopay lines use the invoice currency.
- **scope:** only adyen, mangopay, vinted pay and "Unassigned revenue account" lines are booked.

**how it reaches netsuite:** `mrt_double_entry` is exposed as a looker explore (`double_entry`). it has no gcs export post-hook. the upload step is not visible in this repo.

## route 2: in-transit accrual at month end

| step | model | what happens |
| --- | --- | --- |
| 1 | `fct_prepared_transaction_fees`, `dim_transaction_status_times` (transactional experience sources) | the checkout's buyer protection fee (bpf) and its status dates |
| 2 | `prep_service_fee_checkout_payments` | keeps checkouts the buyer actually paid |
| 3 | `mrt_service_fee_accrual` | for each closed month, keeps checkouts not invoiced or cancelled by month end. splits bpf into net and vat by buyer country, then applies a cancellation provision by age. fully provisioned after 60 days |
| 4 | `snap_service_fee_month_end_accruals` | freezes each month end, because the cancellation rate is recomputed every month |
| 5a | `prep_double_entry_service_fee_accrual` → `mrt_double_entry` | per checkout: credit net to 610001, debit provision to 610402, debit the rest to 230011 on the month-end date. the same entry reverses on the 1st |
| 5b | `mrt_service_fee_accrual_accounting_splits` | the same three sides, summed per country, entity and currency. the post-hook `accounting_export_post_hooks("service_fee_accrual")` exports a csv to the accounting exports bucket, and accounting uploads it to netsuite by hand at close |

vat is not accrued.

## open questions
1. how does `mrt_double_entry` get into netsuite? is it a manual pull from looker, or an integration outside this repo?
2. outside us, uk and au, 610001 is credited with the vat-inclusive amount. is vat moved out of revenue somewhere else, for example in netsuite?
3. both 5a and 5b book the accrual to 610001. which one actually goes to netsuite, and does the other count as reporting only?
