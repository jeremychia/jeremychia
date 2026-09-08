---
name: write-rules-as-imperatives
description: Rule files, review guidance and skills lead with the verb — flag, ask, name, never — not with framing or explanation
metadata:
  type: feedback
---

**Write instruction files in imperatives.** Rule files, review guidelines, skills, runbooks —
anything whose job is to tell someone what to do. Lead with the verb: *flag*, *ask*, *name*,
*check*, *never*, *require*, *drop*.

The feedback was one line — "write in imperatives" — with a link to
`github.com/gvzdv/claudish-to-english`, a plugin that pipes assistant messages through a
local model to rewrite them in plain English. The point of the link is the diagnosis, not
the tool: my drafts read as *claudish* — dense, over-structured, over-evidenced,
over-explained.

What that looks like in practice, from one rule file:

- a section opened with **31 lines of setup** before its first instruction
- another spent **four paragraphs** explaining why its category was difficult to get right
- one paragraph explained **the document's own structure** — self-referential scaffolding
- bullets ran **122–140 words** against the file's own 32-word median

The rewrite: state the instruction, then the mechanism in a clause, then the worked case
last if it earns a place.

> The highest-value finding available here, and the one most likely to pass every test.
> Several models label rows by walking an ordered case chain. When a diff narrows one arm…

becomes

> **When a diff narrows one arm of a labelling `case` chain, trace where the rejected rows
> go.** They fall through to the arms below. If none accepts them, the column comes out NULL
> and nothing fails.

**Why:** an instruction buried under its own justification does not get followed. The
framing is written for the author, who has just worked it out; the reader wants to know
what to do. It is also a length problem — the explanation is usually most of the words.

**How to apply:** write the verb first, then check three things. Cut any sentence that
explains why the rule matters *before* saying what the rule is. Cut anything describing the
document's own organisation. Where a list sits under a `Flag:` lead-in, noun phrases are
already imperative — match the file's existing pattern rather than converting them, but hold
their bodies to the file's median length. Keep one worked case per rule, at the end, and
name it as an example rather than deriving the rule from it.

Same instinct as [[writing-concise-and-lowercase]] and [[plain-language-in-writeups]],
applied to documents that instruct rather than report.
