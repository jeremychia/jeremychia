---
name: plain-language-in-writeups
description: Write findings and PR comments so a reader who has not seen your analysis can follow them
metadata:
  type: feedback
---

**Write validation findings and PR comments in plain english, first time, without being
asked.** This has come up more than once. After one validation write-up the reply was
"can you just write in plain english, i don't understand anything you wrote in the
comment". Treat plain language as the default, not a revision pass.

The failure mode is not length — it is writing *from inside my own analysis*, so the
reader has to reconstruct the query and the code to decode the sentence. What gets
rejected:

- **internal shorthand for things the reader cannot see.** "branch 4 is effectively first"
  means nothing without the case statement open. Say what the rule *does*.
- **my query's column names used as prose.** "`reconstruction_mismatches = 0` on every
  row, so it's a like-for-like comparison" → "my version of the old logic reproduced the
  labels already in the table exactly, so the comparison is trustworthy."
- **jargon where an ordinary word exists.** predicate → condition. bucket → those rows.
  un-classifies → they end up with no label at all. "null status" → nothing at all.
- **stating the effect without the consequence.** "~400k rows sit inside the warn window" →
  "…so that test will start warning on a lot of rows."

**Never write "vintage". Write "snapshot".** Asked for twice — the second time the word had
slipped back in because this file lost the rule when it moved repos. There is no second
word needed for a snapshot taken at a different time. Say "the 2 September snapshot", "the
three snapshots from that day", "the one that was replaced" and "the one that was kept". A
word already in the codebase is not thereby allowed in prose; if it reads as wine or
finance jargon, it is jargon.

**The problem is sentence shape, not length.** Asked again with just "use claudish please",
pointing at the plugin's own rewrite prompt: *"Use short sentences and everyday words. Keep
every fact, name, number, and file path."* Short sentences is the operative half. My drafts
run 40+ words with four clauses hung off em-dashes and semicolons, and they stay hard to
read after being cut to length — a shorter document made of the same sentences reads no
better.

**It is measurable, so measure it.** Split on sentence-ending punctuation, strip code
fences and tables, and count:

- **average words per sentence** — target under 16. Two rule files I had written measured
  27.6 and 20.7.
- **share of sentences over 30 words** — target under 5%. Those two files were at 19% and
  20%.

The fix is mechanical: split every sentence at its em-dash, semicolon, or "and" joint, and
keep one idea in each. Then swap the jargon — load-bearing → needed, blast radius → what
else changes, residue → the rest, proportional trimming → cutting a bit from everywhere.
Where a paragraph lists parallel items, a table beats prose.

**Why:** these comments are read by the PR author, usually someone else. A finding nobody
can decode gets ignored, so the review value is lost regardless of how sound the analysis
was.

**How to apply:** lead with the headline as one sentence a non-author can act on ("the
change fixes 70 rows and breaks 400,000"). Then what you did, then the numbers, then the
suggested fix. Explain *why* a row changed in terms of the data ("their return fee is
cancelled out by a matching discount, so it adds up to exactly zero"), not in terms of
which condition rejected it. Keep the SQL but collapse it in `<details>`, so the prose
stands on its own and the query is there to check rather than to read.

Applies to documentation too: describe what a thing **holds**, not what it excludes, and
state a granularity as which columns are unique together and nothing else — measurements
belong in the PR. [[writing-concise-and-lowercase]] governs length and casing; both apply
at once. And [[verify-before-asserting]] — asked "is this true?" of four assertions once
and two of them were wrong.
