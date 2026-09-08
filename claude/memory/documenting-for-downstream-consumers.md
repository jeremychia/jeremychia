---
name: documenting-for-downstream-consumers
description: Docs about a downstream consumer need the consuming code linked, a support channel and the real owning team — and none of the sourcing
metadata:
  type: feedback
---

Reviewing a set of descriptions for data exports consumed by other teams, I asked the same
things of every one. Prose that merely *describes* a consumer is not done; each claim needs
a way to act on it:

1. **Link the code that consumes it.** Not "service X reads this bucket" but the variable
   or constant name, the repo, and a file link with line numbers.
2. **Name the support channel**, per consumer. Verify it first — and note a Slack channel
   search only covers *public* channels, so "no such channel exists" can be wrong. The same
   trap applies to code search: a repo-wide code search missed the consuming repository
   entirely.
3. **Make every storage path a clickable link**, alongside the raw URI — a reader cannot
   paste a `gs://` or `s3://` URI into a browser. Use the resource's own project, and drop
   the session junk a copied console URL carries.
4. **Name the real owning team, never an invented one.** I wrote a plausible-sounding team
   name and was asked to look it up. Where team ownership lives in an
   infrastructure-as-code repo, GitHub team slugs are often the only identity there — so a
   group email address written in that shape may simply not exist. Don't invent one.
5. **Do not write the sourcing into the file.** "you don't need to state the basis for your
   assertion in the document. say this in-chat, but no need to write it down here." An
   earlier "did you assume this or is there a basis for this somewhere?" was a question *to
   me*, not a request to document the answer — so verify it, put the evidence in the PR
   reply, and let the file state the fact plainly. Hedges, code-search dates and quoted
   justification are all noise in the artifact.

**Why:** the person reading this is usually mid-incident. They need where to look and who
to ask. The provenance of the sentence only matters to the reviewer deciding whether to
trust it, and that conversation belongs in the PR.

**How to apply:** fix one comment per commit, reply naming the sha, then resolve the
thread — this is how I asked for it twice. Where a claim really is uncertain, state the
fact plainly in the file and put the caveat in the reply.
[[one-line-comments-and-docstrings]] and [[plain-language-in-writeups]] govern how long it
is and how it reads; [[verify-before-asserting]] covers the checking.
