---
name: coding-checklist-from-team-reviews
description: Nine checks distilled from two months of a team's review comments; run them while writing a dbt change, not only in review
metadata:
  type: feedback
---

**Run these nine checks while writing the change.** They came from reading 422 review comments on 108 pull requests across a team of seven. Each one came up on several authors' pull requests.

1. **Update the description in the same commit as the sql.** A test that now allows small gaps, under a column description that still says "should be 0", makes every reader treat each gap as a problem. Ticket keys, dates and one-off measurements go in the pull request.
2. **Delete the new line and run the unit test.** Remove the new `when`, filter or `in (...)` value. If the test still passes, no mock row reaches it, so add one. Also check that no mock row lets two causes give the same output.
3. **Check what the merge builds and what a re-run of last month gives.** A model that reads a table that does not exist in production yet fails on its first build. A closed month re-run with new code must still give what was booked.
4. **No catch-all `else`.** See [[name-every-value-no-catch-all-else]].
5. **One definition for a list two models use.** Put it in a project var or macro. Drifting copies caused two real bugs. See [[abstract-at-two-callers]].
6. **No data test on what our own sql guarantees.** A `not_null` on a column built with `coalesce(..., 0)` can never fail, and it scans the table on every run. Check our own logic in a unit test. Keep data tests for inputs another team controls.
7. **Write the action into the test description.** Say what the warning means, who fixes it, and whether it clears by itself after the next run.
8. **Join on the id, not on an equal amount.** Matching a batch to a payout on amount lets two £1,000 batches share one £1,000 payout, so a missing payout passes.
9. **Multiply the scan by the number of runs.** A 3 GB model run 12 extra times a day adds about 0.8 TB a month, and up to 12 alerts when its source is down. Put a test on the snapshot that gets booked, not on a daily rebuild whose result cannot change.

**Why:** each of these was raised on several authors' pull requests. Points 7 to 9 are the ones colleagues raise on my own code, see [[what-colleagues-catch-on-my-prs]]. Catching them while writing is cheaper than a review round.

**How to apply:** go through the list before opening the pull request, and fix rather than explain. Point 2 is a command to run, not a judgement: actually delete the line. The same checks are questions in the `dbt-pr-review` skill.

Related: [[an-assertion-needs-a-test]], [[unit-test-fixtures-use-the-fewest-rows]], [[a-failing-test-should-triage-itself]], [[one-line-comments-and-docstrings]].
