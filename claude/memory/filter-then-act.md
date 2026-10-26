---
name: filter-then-act
description: a loop that skips items with a chain of if-continue guards keeps only the deciding condition; move the exclusions into a named generator or filter
metadata:
  type: feedback
---

When a loop decides whether to act on an item, keep only the deciding condition in it. Move the guards that say which items to consider into a named generator, such as `_tests_to_check`, and the decision into a named predicate, such as `_runs_in_a_task`. The body then reads as one line: act when the predicate says so.

**Why:** a reviewer asked on a linter rule pr: "would it be possible to exclude of if: continue statements and move more directly into if: issues.append, or can we only get to what to include by excluding other situations?" Five `continue` guards mixed scope (which tests) with verdict (is it lost), so the rule's actual condition was hard to find.

**How to apply:** split each guard into scope or verdict. Scope goes in the generator, each with its one-line reason. The verdict becomes the single condition in the loop or comprehension. Run the old and new code over the same inputs and compare the results. Related: [[full-word-names-in-code]], [[pass-only-what-the-code-reads]].
