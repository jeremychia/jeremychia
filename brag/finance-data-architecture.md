# finance data architecture: building data for accountants

**headline:** accountants don't really run on kpis. they run on the month-end close. the data is "good" when the close finishes on time, every number ties back to a source, and a closed month never changes.

## 1. what accountants measure

these are the numbers an accounting team watches. most of them describe the close, not the business.

| what they track | what it means for the data team |
| --- | --- |
| days to close | your data must be ready by a fixed working day (for example wd1 or wd3, the 1st or 3rd working day of the month) |
| reconciliation breaks | your totals must match the bank, the payment provider and the invoices |
| manual journals | every hand-made booking is a gap your pipeline could fill |
| restatements | a closed month that changes is a failure, even if the new number is "more correct" |
| audit findings | the auditor must be able to trace any booked number back to source records |
| unreconciled balances | money sitting in clearing or suspense accounts that nobody has explained |

**materiality** decides how much any of this matters. it is the amount below which an error does not change anyone's decision. ask for your company's threshold early. it is the right basis for test thresholds.

## 2. what changes in the data stack

### the output is a journal entry, not a dashboard
- **write entries as balanced rows.** one row per side of an entry: date, entity, account, currency, amount. the sides of one event sum to zero.
- **keep debit and credit as two unsigned columns** if the ledger expects that. a negative debit is a classic import bug.
- **test that every entry balances.** list the few legitimate exceptions by name, for example a side booked by hand in the ledger.

### closed months must not move
- **snapshot each month at close.** reports and bookings read the snapshot, not the live table.
- **guard against duplicate snapshots.** a retry that writes the same month twice doubles the books.
- **book corrections as adjustments in the current month.** rewriting history breaks the audit trail.
- **watch incremental models.** a reload window that reaches into a closed month silently changes it.

### build on the close calendar
- **rebuild accounting outputs on the agreed close dates,** not every day. a daily rebuild produces numbers nobody has agreed to.
- **keep an override** so finance can ask for an off-schedule run.
- **know your cut-off.** data that arrives after the export (late invoices, other time zones) belongs to a defined month by rule, not by accident.

### mappings are business rules
- **keep mapping tables in version control:** chart of accounts, customer and vendor codes, vat rates, entity per country. finance owns the content, and the data team owns the pipeline that applies it.
- **name every known value and send the rest to an explicit "other" or "unmapped" bucket.** test its share, so a new product or country shows up as a warning instead of vanishing.

### controls are tests
- **completeness:** invoice lines sum to the invoice total. no day is missing. row counts are in line with recent weeks.
- **reconciliation:** your totals match an outside source (bank, payment provider statement, the ledger itself).
- **mapping coverage:** every row got an account.
- **set thresholds from materiality.** error where someone must act before the close. warn where it can wait.
- **check your own sql logic with unit tests.** a data test that re-runs the same logic will always pass.

### exports to the ledger
- **write one file per period,** and make a re-run replace it cleanly.
- **refuse to export an empty result.** an empty file that overwrites a good one is worse than a failed run.
- **carry source ids on every line** so a booked amount can be traced back.

### currencies
- **ask which rate each booking uses:** daily, monthly average or month-end closing. different reports often need different ones.
- **store the transaction currency and the converted amount side by side,** plus the rate and its date.

## 3. accruals and deferrals, briefly
- **accrual:** book a cost or revenue in the month it was earned, before the invoice arrives. it usually reverses on the 1st of the next month, when the real invoice gets booked.
- **deferral:** money received now for something delivered later. it is released to revenue over time.
- these are often the hardest models. they estimate a number at month end and then get compared with what was actually invoiced.

## 4. on oracle fah
my understanding is that fah turns source transactions into journal entries using accounting rules configured inside fah. if so, your job is mostly the quality and completeness of the transactions and their attributes, and the rules sit with the accountants. worth confirming with your team:
- who owns the accounting rules, and how a rule change is tested?
- what happens to a transaction fah cannot account for? where do the errors land?
- how do you reconcile what you sent with what fah booked?

## 5. questions to ask your accountants
1. what is the close calendar, and on which working day do you need each output?
2. what is the materiality threshold?
3. which reconciliations take the most manual time today?
4. which manual journals happen every month?
5. what does the auditor ask for, and how do you answer today?
6. when a past month is wrong, do you restate it or adjust in the current month?

## 6. glossary
- **general ledger (gl):** the main set of accounts the financial statements are built from.
- **subledger:** a detailed record (invoices, payments) that rolls up into the gl.
- **chart of accounts:** the list of gl accounts.
- **journal entry:** a booking of debits and credits that balance.
- **entity / subsidiary:** a legal company in the group. each one keeps its own books.
- **ar / ap:** accounts receivable (owed to you) and accounts payable (owed by you).
- **credit note:** a negative invoice that cancels or reduces an earlier one.
- **intercompany:** transactions between two entities of the same group. they must cancel out in the group view.
- **cut-off:** the rule that decides which month a transaction belongs to.
- **clearing / suspense account:** a temporary account that should go to zero once everything is matched.
