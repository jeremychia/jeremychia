---
name: one-line-comments-and-docstrings
description: Code comments and docstrings are one line where possible; the reasoning goes in the PR
metadata:
  type: feedback
---

Keep code comments and docstrings to **one line** wherever possible, in any language. The
feedback that produced this was "are some of the function descriptions too verbose?"
followed by "everything is too verbose. keep comments not so verbose please".

What was too much, and what replaced it:

- a 4-line docstring explaining why a qualified table reference isn't a local reference →
  2 lines
- a 12-line docstring with a worked example → 4 lines, no example
- a 3-line comment above a CTE → 1 line
- an extra 15-line `Good:` example added to a rule docstring → deleted; the one-line rule
  text carries it

**Comments in production code are business context only.** A comment may explain a
*business* decision — why one fee is booked separately, why a charge carries a particular
tax treatment. It must **not** narrate a prior architectural decision or the history of a
refactor. Headers like "split out of X because the engine re-plans a CTE once per
reference … 1290 stages, 3.7tb spilled" were rejected: "the comments should only contain
context of a business decision, but doesn't need to explain a prior architectural
decision". Refactor rationale, plan statistics and before/after numbers belong in the PR
body.

Two more, from reviewing a set of new models:

- **prose describing the model belongs in its description**, not in a comment above the
  SQL. Where descriptions are published to the warehouse, the description is what a
  consumer sees and the comment reaches nobody.
- **don't explain your design decisions**, and don't defend a choice against an
  alternative nobody proposed.

**Why:** long rationale bloats the file and the review surface, and duplicates what belongs
in a ticket. Architectural history also goes stale in the file while staying accurate in
the PR.

**How to apply:** write the one-line version first. If it needs a second line, ask whether
the sentence is explaining *why the change was made* — that part goes in the PR. Keep only
what a future reader needs while editing the code. When splitting a file, add no header
comment explaining the split: the description carries what the thing is, the PR carries
why it exists. Link the document that defines a business rule rather than paraphrasing it —
a comment that still leaves a reader needing that page should carry the link.

Same instinct as [[writing-concise-and-lowercase]] and [[plain-language-in-writeups]], but
about comments in code rather than prose written for a person.
