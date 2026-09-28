---
name: a-failing-test-should-triage-itself
description: A data test's failing row carries what the bad column holds, the money at stake and example ids, so the responder does not have to write a query to start
metadata:
  type: feedback
---

**Make a failing data test emit what the responder needs to diagnose it, not just the metric that failed.** Asked for directly: "could you log some of the results? the goal is that i want faster triaging."

My first version returned the row count, the count that passed, and the percentage. All that tells anyone is that something broke. The first thing they then do is open a console and ask what the column is actually holding — so the test should have told them.

What earns a column in the output:

- **what the suspect column actually contains** — the top few values with counts. `created (62849033), settled (817296), <null> (1517)` names the cause on sight. `approx_top_count` does this in one pass.
- **a discriminator between the likely causes.** The share of nulls separates "the join broke" from "the values changed meaning". Pick the one measure that splits your top two hypotheses.
- **the size of the problem in the unit the business cares about** — money, not rows.
- **two or three example ids** to look up, so the first investigation needs no query at all.

Then map them in the header comment, in reading order: "read pct_null_status first: high means the join broke, low means the column changed meaning again." A responder should be able to work top to bottom.

**Weigh the extra bytes against how often the test runs.** The diagnostic columns nearly doubled one test, 12 GB to 23 GB, because the scan had to read the fee amount and the id as well. Fine on a monthly model, not on a daily one — so check the schedule before deciding, and say the trade in the PR's cost section.

**Why:** the gap between the alert firing and someone understanding it is most of the time to fix. A test that already answers the first three questions closes that gap, and it is nearly free to write while the context is fresh.

**How to apply:** after writing the assertion, ask what you would query next if it fired, and select that instead. Then run it against production and read the row as if you had been paged — if it does not tell you what to do, it is not finished. One mechanical note: sqlfmt strips hanging indentation inside SQL comments, so keep each comment line self-contained rather than aligning continuations, and run it twice to confirm the format is stable.

Related: [[test-descriptions-state-the-invariant]] covers what a unit test's description says; this is about what a data test *returns*.
