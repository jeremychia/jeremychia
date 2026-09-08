---
name: abstract-at-two-callers
description: Shared by two or more callers → a macro or shared function; used once → keep it in the file that owns it
metadata:
  type: feedback
---

**"If it is used across models, do as a macro. If it is just used in one model, do it in a
jinja tag."** The general form: abstract at two callers, not at one.

**Why:** an abstraction with one caller hides logic from the file that owns it, for no
reuse in return. The reader of that file now has to open a second one to understand what
it does.

**How to apply:**

- **Two or more callers → extract it.** And if a third copy of the same logic already
  exists elsewhere, switch that caller over too, so the abstraction really is shared rather
  than aspirational.
- **One caller → keep it inline.** For a parameterised repeat, a local variable holding the
  varying parts plus a loop over it reads well and compiles back to the same output — that
  is how four near-identical case branches collapse into one.
- **A shared abstraction is the right home for a contract between sibling files**: one for
  a column list, one for a struct or array type, so the siblings cannot drift.
- **Don't extract a filter only one consumer applies** — but do once a second one needs the
  same filter.

**The same expression repeated inside one file** is the smaller version of this: a date
window written twice, a threshold literal in three branches. A local variable, or a
project-level setting where one already exists, removes the chance of the copies diverging.
Check for an existing setting first — a repeated literal that already has one is a stronger
finding than a repeated expression that does not.

**One definition per concept** is the other side. Where a second file reproduces a rule
that exists, the two drift and the outputs disagree. Worse is reusing an established *name*
for a different definition — a list named for a category that includes two members where
the canonical definition includes five is not a narrower list, it is one word meaning two
things in one project. Either centralise it, or rename the local one to say what it
actually holds.

Related: [[search-for-an-existing-implementation]] — the check that comes before deciding
to write the abstraction at all.
