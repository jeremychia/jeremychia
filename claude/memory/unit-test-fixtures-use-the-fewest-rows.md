---
name: unit-test-fixtures-use-the-fewest-rows
description: A new unit test uses the fewest fixture rows that still prove its rule, and reuses the shape of the tests already in the file
metadata:
  type: feedback
---

A unit test uses the fewest fixture rows that still prove its rule. It reuses what the file already has before adding anything new.

- **Shrink the threshold to shrink the rows.** If a threshold of 1 proves the filter, don't use a threshold of 2 with three rows. One row that the filter must exclude plus one it must keep is usually enough.
- **Copy the nearest existing test.** Use the same ids, entity names, currency and expected columns as the test it sits beside. Then the new test differs from its neighbour only in what it tests.
- **Drop a new test when an existing expected output already makes its assertion.** One example: a test that "carries a column through" is redundant when another new test already expects that column's value. Say in the remaining test's description that it covers both.
- **Prove the smaller fixture still catches the fault.** Switch off the logic under test and confirm the test fails before calling it done.

**Why:** I asked for this on a pull request whose new tests copied a three-row fixture and added a test another one already covered. Extra rows make a reviewer work out which row matters. A redundant test is one more fixture to update when the schema changes.

**How to apply:** before writing a new fixture, read the tests in the same file and start from the closest one. Then remove rows until removing one more would stop the test from proving the rule. Keep one behaviour per test. Reusing a fixture's shape is not the same as merging two behaviours into one test. Related: [[test-descriptions-state-the-invariant]], [[an-assertion-needs-a-test]].
