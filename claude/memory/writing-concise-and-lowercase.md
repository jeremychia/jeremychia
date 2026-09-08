---
name: writing-concise-and-lowercase
description: All prose lowercase, and much shorter than feels natural — the length rule and what to delete
metadata:
  type: feedback
---

**Write all prose in lowercase** — inline comments, PR descriptions, PR comments, commit
bodies. No sentence-case capitalisation. Genuine identifiers and data literals keep their
real casing (currency codes, entity names, model and column names); lowercasing those
would misstate the data.

**Keep it much shorter than feels natural.** I have asked for this repeatedly, which is
the tell that the instinct does not correct itself: a ~600-word PR body cut to ~130, a
948-word one cut to ~180, a 10-line comment block cut to 3, a ~200-line body with four
collapsible query blocks cut to ~54.

The cut is not proportional trimming — it is **deleting whole categories**:

- **the reasoning that led to the change.** How the rule was arrived at, what was weighed,
  what was rejected. The reviewer is judging the result, not auditing the derivation.
- **before/after examples.** The diff is right there and shows all of them.
- **essays justifying the approach.** State the rule in one sentence and let the diff
  demonstrate it.
- **count tables.** A "change / count / where" table of five fix types is one sentence.
- **evidence for a claim nobody was going to dispute.** Keep the proof for the reply where
  it was actually asked for.
- **what was decided against, and the tool's behaviour.** Ticket material, never body
  material.

What survives: what changed and its scope, the rule in a sentence so a reviewer can judge
consistency, what was validated as one number, and the manual actions.

**Why:** the PR body is not the record of the work — the ticket is. The body is only what a
reviewer needs in order to approve. Anything a reviewer will not act on is noise that
hides the parts they must check.

**How to apply:** write short first; drafting long then cutting produces a compressed
essay where every sentence survives in shortened form. Count before posting rather than
eyeballing it. Keep template sections that do not apply and write "none." under them. Then
re-read and cut every sentence that explains *how you got there* rather than *what a
reviewer must check*. [[plain-language-in-writeups]] governs vocabulary at the same time —
short is not the same as readable, and both are required. [[pr-description-budget]] is the
countable version for PR bodies specifically.
