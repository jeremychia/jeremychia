---
name: links-carry-where-it-was-said
description: Every link and every quoted phrase names where it came from — the channel, the file and line, the ticket field — so the reader can judge it without asking
metadata:
  type: feedback
---

**Attach a source to every link and every characterisation. Say where it was said, by whom, and
when — not just that it exists.**

A bare link makes the reader open it to find out whether it supports the claim. Worse is a
characterisation with no link at all: writing that a column is now "attempt-only" when that phrase
appears nowhere, and the actual wording is a sentence in a yml description added by one pull
request. The reader cannot tell whether that is quoted, paraphrased or invented.

What a sourced reference looks like:

- a slack message — the channel name and the permalink to that message, not the channel
- a code claim — a permalink pinned to the commit, with the line number
- a quoted phrase — quotation marks and the artifact it came from, and if it is your own wording
  for something, say so and link what it summarises
- a ticket field — which field, since a description and a comment carry different weight
- a tool or bot output — a link to that comment, because "CI flagged it" is unverifiable otherwise

**Why:** the reader is deciding whether to act on the claim. Provenance is what lets them, and a
write-up that cannot be checked gets treated as opinion. It also protects the writer: sourcing a
claim is what exposes the ones that turn out to be wrong.

**How to apply:** before posting, go through every link and every phrase in quotation marks and ask
where it came from. Where a claim rests on a search, name the search — the terms, the window, the
scope — and say what the search could not cover. See [[verify-before-asserting]] for checking the
claim itself; this rule is about letting someone else check it.
