---
name: search-for-an-existing-implementation
description: Check the packages, then the project's own helpers, reading candidates rather than judging by filename
metadata:
  type: feedback
---

I asked twice whether an existing helper would do before accepting a new one, and the
second time I was right: a purpose-named custom test had been written when a
parameterised one doing exactly that already existed in the same directory.

**Why it is easy to miss:** a helpers directory fills up with names that read
caller-specific — `assert_<specific thing>_completeness` — so it is easy to skim the
listing, conclude nothing general is there, and add a duplicate. The genuinely reusable
ones hide among them.

**The order matters, not just the search:**

1. **The installed packages first.** I pushed back a second time — "is there a more out of
   the box implementation, do we really need a generic test?" — when I reached for the
   project's own helper where a package one fit. Most "aggregate per group" rules need no
   custom code at all; the package tests generally take group-by and row-condition
   arguments already, and group-by entries can be expressions rather than bare columns.
2. **Then the project's own helpers.**
3. **Then any shared internal package.**

**How to apply:** read the candidates rather than judging by filename — that is the step
that fails. And when adding a genuinely new one, **name it for the assertion, not the
caller**: a name derived from the first thing that used it is a name nobody finds again,
which is what created the duplicate in the first place.

Related: [[abstract-at-two-callers]] for whether to extract it once you know nothing
exists.
