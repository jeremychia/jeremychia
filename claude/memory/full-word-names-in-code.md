---
name: full-word-names-in-code
description: name loop and comprehension variables with full words (parent, task_model), never single letters or abbreviations (p, task_id for a model)
metadata:
  type: feedback
---

Name every variable with a full word, including in comprehensions and short loops: `parent for parent in parents`, never `p for p in parent_ids`. Drop an `_id` suffix when every value of that kind is an id anyway.

**Why:** a reviewer flagged `p` and `task_id` on a linter rule pr as a readability nit: "lets use `parent for parent in parents_ids` instead of the abbreviations". A one-letter name forces the reader to look back at the iterable to know what it holds.

**How to apply:** rename in the same commit across the module and its tests, then check nothing else changed. Related: [[pass-only-what-the-code-reads]], [[filter-then-act]].
