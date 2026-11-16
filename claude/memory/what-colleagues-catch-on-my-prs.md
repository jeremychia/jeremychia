---
name: what-colleagues-catch-on-my-prs
description: The four things colleagues keep raising on my own pull requests; check them in self-review before asking for review
metadata:
  type: feedback
---

**Before asking for review, check the four things colleagues raise most on my pull requests.** These came from reading every review comment others left on my pull requests over two months.

1. **Say what to do when it fires.** Every test and job description names the action, who acts, and whether the warning clears by itself after the next run. A test with an empty description tells the person on watch nothing. A readme sentence such as "moves on" was read as "yesterday is skipped".
2. **Ask what happens when two rows could match.** Two campaigns on one route with different service types. Two batches of £1,000 passing against a single £1,000 payout, because the test matched on amount and not on which batch owns the payout. A tax amount that doubles if the vendor repeats it on a second row. Add one mock row for each case.
3. **Count the cost and the alerts of each extra run.** Twelve runs a day means up to twelve alerts when the source is down, and about 0.8 TB a month of rebuilds. Daily tests on a table whose result only changes at the next booking cost about 36 GB a day for nothing. Put the test on the snapshot that gets booked.
4. **Check what the merge and side effects do.** Adding a `ref` to a model with a post-hook export means a `+` selector can now send that file by accident. A post-hook runs inside the model build, so a test cannot stop the file.

**Why:** these are the gaps my own review lens misses on my own code. I check grain, descriptions and tests on other people's work, but colleagues look at operations: alerts, run cost and overlapping rules.

**How to apply:** run these four as a checklist after the usual self-review, and write the answer to the first one into each new test's description. The same four are questions in the `dbt-pr-review` skill.

Related: [[a-failing-test-should-triage-itself]], [[name-every-value-no-catch-all-else]], [[an-assertion-needs-a-test]].
