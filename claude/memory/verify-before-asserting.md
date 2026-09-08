---
name: verify-before-asserting
description: Verify each claim before writing it, and separate what the code shows from what only the data knows
metadata:
  type: feedback
---

**Verify every claim before writing it.** I once asked "is this true?" of four separate
assertions in one document and two of them were wrong. Generic boilerplate that a codebase
repeats is a common source: text describing what a column holds is wrong wherever that
column actually holds something else, and it gets copied forward unchecked.

**Separate the two kinds of claim.** A repository shows you code, config, fixtures and
tests. It does not show you what is in the database. "This column is never null in
practice", "this join fans out", "every such row will warn", "this branch is unreachable"
are all statements about data you cannot read from the code.

The right shape is both halves in one comment: assert the part the code shows, ask the part
only the data knows. *"That value is a live branch at `<file>:<line>` and appears in two of
the three allowlists but not this one. If any such row has a non-null tax country, the new
test warns on every run — is that combination supported?"* That is a finding, not a hedge.

**Where a question is genuinely the right move, it has to earn it.** Three things must all
hold: the answer changes whether there is a finding; a third party could not answer it from
the diff, the surrounding files or the PR description; and I can name what goes wrong if
the answer is the bad one. "Is this intended?" is noise. Cap it at about two per review —
five questions is a request for the author to do the review themselves.

**And some things read as questions but should be asserted**, because the repo answers them:

- *is this tested?* → visible in the file. See [[an-assertion-needs-a-test]].
- *does this exist already?* → searchable. See [[search-for-an-existing-implementation]].
- *is this the convention?* → countable.

**Why:** a confident wrong claim is the most expensive thing a review can contain — it
costs the author time and it costs me the credibility that makes the next finding land.

**How to apply:** check rather than infer, and where something could not be verified, say
so explicitly. A named unchecked assumption is worth more than another small finding: a
summary that lists three minor things and stops reads as clearance for everything else.
Don't give a merge verdict — the ranked findings, the questions and the unverifiable list
are the deliverable.
