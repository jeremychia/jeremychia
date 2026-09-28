---
name: no-hard-wrapped-prose
description: Never hard-wrap prose in markdown that renders — one paragraph is one line; wrapping belongs only in code and code comments
metadata:
  type: feedback
---

**Do not break prose lines at a column width in anything that renders as markdown.** A paragraph is one line. A bullet is one line, however long.

This covers PR descriptions, PR and ticket comments, model descriptions in yml, and markdown documents. Asked for directly: "don't do unnatural line breaks please".

The habit comes from source code, where an 80 or 100 column limit is real. In markdown it is not: the renderer reflows anyway, so the breaks show up only where they hurt — a diff where one added word rewraps six lines, an edit box with ragged lines, and a raw view where sentences stop mid-clause.

Where wrapping still applies: SQL and code inside fences, inline code comments, and commit message bodies, which are read in a terminal that does not reflow.

**Why:** the line breaks are invisible when it renders and ugly everywhere else, and they make a one-word edit look like a rewritten paragraph in review.

**How to apply:** write the paragraph, do not wrap it, and let the tool reflow. If a long line is uncomfortable to write, that is a sign the sentence is too long — split the sentence, not the line. See [[writing-concise-and-lowercase]], which wants sentences under about 16 words in any case.
