---
name: pr-description-budget
description: The countable procedure for cutting a PR body to length, the categories to delete, and why editing an existing draft keeps all its content
metadata:
  type: feedback
---

[[writing-concise-and-lowercase]] states the rule and I keep breaking it anyway, so this
is the mechanical version. Asked for a third time after a 948-word body, with a pointer to
a plugin that pipes assistant messages through a local model to rewrite them in plain
english. The point of that link was the diagnosis, not the tool: my drafts read as
over-structured, over-evidenced and over-explained, and need a rewrite pass before they
are fit to post.

**Write short first.** Do not draft the full version and trim. Drafting long then cutting
produces a compressed essay; drafting short produces the right thing.

**Budget, countable before posting.** `sed '/^#* *Checklist/,$d' body.md | wc -w` ≤ **200**,
aiming ~150. No section over 5 lines. Summary ≤ 3 sentences. One table at most, and only
where it replaces more prose than it costs. One `<details>` block at most.

**Delete by category, not by sentence.** These all went in one 948-word body, ~6x over:

- **count tables.** A "change / count / where" table of five fix types, plus a
  before/after count table → one sentence: "13 test arguments moved under `arguments:`, 38
  properties under `config:`, 2 duplicate keys removed."
- **evidence for a claim the reviewer wasn't going to dispute.** Two source citations
  proving two settings were already the tool's defaults → "both were already defaults."
  Keep the proof for the chat reply, where it was actually asked for.
- **what I decided *not* to do, and why.** A "what is not included" section with a 7-row
  table and two paragraphs on tool false positives → one line, or nothing: it is already
  in the ticket.
- **the tool's behaviour.** Which autofix flags I passed, what it got wrong, what I
  reverted. A note for the ticket and for memory, never for the PR body.
- **validation method.** "deep diff of every node, source, exposure and macro", node-count
  inventories → the one number that means something: "930 test nodes resolve identically;
  manifests differ only in post-hook timestamps."

**Editing an existing draft is not a rewrite.** When asked to improve a PR body or make it
"more readable", keep every piece of content already in it: all the examples, the ops
notes, the cost section, the checks list. Change the order, headings, sentences and casing,
and keep the template's section headings. Do not apply the budget or the delete-by-category
list. Suggest a cut in the reply instead of making it. Once I cut three of four example
alert messages, a log-colour tip, a no-backfill note and the cost section, and got "nonon,
include all the examples. just make it more readable."

**Reword a rule only after reading the code.** Tightening a sentence about behaviour can
invert it. "alerts only if it wasn't past the threshold in the prior week" became "alerts
only if it was below the threshold at some point in the last 7 days", which is the
opposite. Check the logic before rephrasing it.

**Why:** the PR body is not the record of the work — the ticket is. It is only what a
reviewer needs in order to approve.

**How to apply:** four short sections — what changed (a sentence or two), why (one, or just
the ticket link), what was validated (one number), manual actions. Keep template sections
that don't apply and write "none." under them; never delete one. Then count the words. If
a fact feels too good to cut, put it in the ticket and link it. If the reviewer later asks
for detail you cut, put it in a follow-up comment rather than growing the body.
