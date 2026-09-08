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
