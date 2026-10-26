---
name: pass-only-what-the-code-reads
description: give an object the slice of data its callers read, built once and shared; keep the existing central class where it is, so the change touches no other code
metadata:
  type: feedback
---

Give an object only the data its consumers read. When a rule needs a project's lineage, attach a small typed field holding parents, children, names and the few flags the rule checks, built once and shared by every object. Never attach the whole parent structure, such as a full manifest. Keep the class that owns the parent structure central: do not move it into a new module or pass it around, because every file that imports it then changes too.

**Why:** a reviewer asked "why will every model carry the full manifest" and "would refrain from creating this and passing it around" on a linter rule pr. The full manifest hid which fields the rule depended on. Moving its class into its own module changed an import in five other rules' tests and a shared helper, so a pr for one new rule touched code it had nothing to do with. The lean field showed the rule's real inputs, and keeping the class central put the diff back to the new rule plus the two files that build the field.

**How to apply:** list the fields the new code reads, then build exactly those in the one place that already owns the parent structure. Keep the existing class where it is. Before pushing, check `git diff --stat origin/main...HEAD`: every file outside the new feature needs a reason, and an import-only change in another module means something central moved. Prove the refactor is output-neutral by running the old and new code over real inputs and comparing every result. Related: [[abstract-at-two-callers]], [[full-word-names-in-code]], [[filter-then-act]].
