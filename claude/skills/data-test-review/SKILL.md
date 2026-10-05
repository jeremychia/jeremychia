---
name: data-test-review
description: Write or review dbt data tests and unit tests so they test the risky rows, sit where the risk enters, and fire only when someone has to act. Use when adding or reviewing tests in a PR, setting severity, warn_if or error_if, choosing a test's where window, deciding whether a check should be a data test or a unit test, or writing a test's description.
---

# Data test review

Run these checks on every test a PR adds or changes. Each rule names what to check, what to change, and how to prove it. Worked cases are at the end.

## 1. Classify each check as logic or data

- **Grep for `as <column>`** on every column in the assertion. If the model's own SQL computes the column, the check is logic. Move it to a unit test.
- **Keep a data test only when the rule depends on what arrives**: a source, a join, a mapping or a seed.
- **Delete a data test that other checks already imply.** Work out what the column is built from. If upstream tests already cover every input over the same window, the check cannot fail on its own.

## 2. Shift left

- **Put each check on the earliest model where the risk enters.** Test a join key on the table being joined, not on the output.
- **Find what each model can actually stop.** A model that writes a file in a post-hook has already written it before its tests run. Its tests can only report.
- **Never claim a warning holds anything back.** A `warn` never skips a downstream model. Only `error` does, and only in the same invocation.

## 3. Find the true key, then what readers assume

- **Measure the declared key over the whole table**: row count, distinct count and nulls. Then check whether a smaller key also holds. If the id alone repeats, the type column belongs in the key.
- **List every reader**, in the repo and in other projects' manifests, plus any service that reads an export.
- **For each reader, note how it uses the table**: joined on the key, summed after a join, or protected by `distinct`, `min()` or an existence check.
- **Flag every reader that sums after a join.** That is where a duplicate becomes a wrong number.
- **Check whether an external consumer enforces uniqueness.** One that deletes a day and reinserts the file passes a duplicate straight through.

## 4. Test every join that can fan out a row

- **List every left join in the model**, and test each join key on the joined table.
- **Skip a key its owner already tests**, and say so in the PR.
- **Use `error` only for fan-out.** Keep every other check at `warn`.
- **Set the limits from materiality:** `warn_if: ">0"`, and `error_if` at the duplicate count that could pass the clearly trivial threshold. That count is the threshold divided by the 99th percentile of what one duplicate adds, measured on prod. Put the percentiles in the PR, not in the description.

## 5. Make the window cover what the run rewrites

- **Read the model's reload window from its config.** For day partitions, the run rewrites the N days ending on the run date. For month partitions, it rewrites the current month and the N−1 before it. Look for start-of-month extensions in the jinja.
- **Start the test at whichever is earlier:** the business window or the reload window. Use `least()` of the two constants, so partitions still prune.
- **Cover what an export uploads**, not what the model holds. A run that rewrites 46 days of files needs a 46-day check.
- **Add one extra period at the start of a test that uses `lag()`.** The where clause filters before the window function, so the first period has nothing to compare with.
- **Run uniqueness checks up to the run date.** Only a completeness check needs a lag at the end, for data that is still settling.
- **Check the worst run date, the 1st of the month**, as well as today.

## 6. Test the risky rows, with one filter rule

- **Filter to the population the rule is about**, for example the lines that are filed.
- **Drop filters that another flag already implies.** Check for nulls in the flag first.
- **Use one filter for each purpose:** one for checks on the filing and one for model-wide rules. Mixed filters across one model are a review finding.

## 7. Set limits from known cases

- **Before raising a limit, read the team's alert case log** and the test's run history.
- **For a known case**, raise `warn_if` to its settled level. Add a one-line comment naming the case id and linking the log.
- **For a case not in the log**, leave the limit and report the rows.
- **Check whether a window change caused a firing**, and whether it will fire again on a later run date.

## 8. Prove each test catches a fault

- **Break the model the way the test guards against**, for example remove a fallback or flip an operator. Run the test, and expect it to fail. Restore the model.
- **Make fixture rows differ in the column the rule chooses between.** A fallback test whose two sources hold the same value passes either way.
- **Write one unit test per behaviour**, and name it for that behaviour.

## 9. Write the description as rule, cause, action

- **State the rule and why a breach matters** in plain words.
- **Give the usual cause.** It must be one the test's window can see.
- **End on an imperative and an owner:** "<team> needs to fix it. <Verb> …, and tell <full name> in <team> …".
- **Look up every contact** from the table's labels or its owning repo. Use full names throughout.
- **Make every claim match the code.** Check that "this stops the upload" matches the severity, and that "this watches closed months" matches the date logic.
- **Move evidence, dates and rationale to the PR.** That includes thresholds' measurements, incident examples, and arguments against alternatives nobody proposed.

## 10. Run everything against prod before reporting

- **Compile with dev, rewrite references to prod, and run `count(*)` over each test.** Compare each count with that test's own `warn_if` and `error_if`.
- **Report every test that fires**, with the rows behind it and whether it is a known case.
- **Leave a PR review note on every new data test.** Say it ran against prod for today and for the 1st of the month. Give the rows found, the cost, and the limit in words. Recommend whether it is safe to add. Collapse the compiled prod query in `<details>`.
- **Leave a PR review note on every test removed from main.** Name the test that now covers it, say why the removed one could not fail alone, and link the SQL.
- **Leave no note for a check that never reached main.** Dropping it removes nothing from production, and the diff against main shows nothing to explain.

## Worked cases

- **Logic.** A check that gross equals net plus VAT re-added two numbers the model had just added. It cost 23 GB a run and could never fail. A unit test with a rate that forces rounding proved more.
- **Shift left.** An export's duplicate check passed, but the risk was a user listed twice in a joined source. A uniqueness test on that source names the record to fix and costs almost nothing.
- **True key.** The declared pair held over billions of rows, but the id alone repeated on millions. So both columns belong in the key, and every reader that filtered on the type before joining was safe.
- **Materiality.** One line adds about €9 at the 99th percentile, so 100 duplicated lines stay under €1,000. One business seller adds about €600 a month, so 2 duplicates pass it.
- **Window.** The merge rewrote 35 days, but the check started at the start of last month. On the 1st it missed 4 days, and readers that sum history would have counted a duplicate there twice.
- **Known case.** A country check fired daily on a case the log already tracked. Its limit went to the settled level, with a comment linking the case. A sign check that was not in the log kept its limit.
- **Bites.** A date-fallback test still passed with the fallback deleted, because the two candidate dates were the same day. Moving one date fixed it.
- **Claim.** A description said a check "holds the upload back", but its severity was `warn`. The sentence went.
