---
name: readme-built-for-skimming
description: The shape Jeremy wants for a README, project doc, plan, brief, talk run-sheet or data model description — one heading or bold label per idea, checkboxes for actions, one numbers table, what-to-show split from what-to-say
metadata:
  type: feedback
---

**Build a README so a reader can skim it. Every idea gets its own heading or bold label, and every command gets its own block.**

Jeremy shared a rewritten README as the model to follow. The content was the same as mine. The shape was not:

- **A sub-heading per idea, numbered when they are parallel.** "design decisions" became `### 1. the data fits in memory`, `### 2. …`, not four dense bullets under one heading.
- **Bold-labelled bullets** for lists of files, docs or limitations: "**validation only warns.**" then the plain sentence. The label alone should tell the story.
- **Split install from run.** Each gets its own `###` and code block. Each command gets a `#` comment above it, not a trailing comment on the same line.
- **Asides go in a `> **tip:**` blockquote**, kept out of the main flow.
- **The headline claim goes in bold near the top of its section**: "it **does not use dbt, SQL or a database.** here is why."
- **Short paragraphs under each heading.** Two to four sentences, one idea each.

Don't copy that example's defects. It used Title Case headings, tracking parameters (`utm_source=…`), and relative links rewritten as search-engine URLs. It also changed a stated threshold ("a few thousand" became "tens of thousands"). Keep links relative and keep facts exactly as they were.

**The same holds for plans, briefs and talk run-sheets.** Jeremy supplied a rewritten talk plan as the model. It said the same things as mine in half the reading time:

- **Sections named for their job, in a fixed order:** overview, to-confirm, key facts, audience, rules, structure, per-part detail, reference numbers, actions.
- **Actions as `- [ ]` checkboxes**, not paragraphs about what still needs checking.
- **Per slide, "on screen" and "say" as separate blocks.** Delivery notes go in their own checklist.
- **Every number in one reference table**, bolded where it is the point, with n and p in one format.
- **A small text diagram for the structure**: a timeline for the talk, a three-box flow for the argument.
- **Current state only.** No "the earlier draft said", no reviewer panel, no "this was wrong" — per [[no-drafting-history-in-the-output]].
- **Coaching cut to one line.** My version spent paragraphs on why each beat works; his kept the instruction and dropped the argument.

That example also had defects: jargon ("structural data drift", "ingestion boundary"), a code snippet showing patterns that weren't the real ones, and "highest globally" for "highest in this corpus". Take the structure, not the wording, and re-check every quoted figure and snippet against the source.

**The same holds for a data model's description.** Jeremy rewrote two model descriptions as the model to follow. Each was a wrapped block under four labels, with several rules run together in one paragraph:

- **One labelled paragraph per idea**, each on one line, with a blank line between. The line starts with the label and a colon.
- **`Summary:` first**, one or two sentences on what the table holds.
- **Then one label per rule**, named for the rule: `Threshold:`, `Precedence:`, `Batches:`, `Tests:`, `Refresh:`.
- **`Granularity:` and `Filter:` get their own lines too.** Keep any keywords a linter requires, word for word.
- **Short sentences, standard capitalisation after the label**, and never hard-wrapped.
- **Only what the table holds and how it is built.** Leave out what tests check, why each exclusion exists and how to rebuild it. Those belong on the test, the column or the README. Asked to cut, a 2,500-character description came down to about 1,500 by dropping a tests paragraph and the reasons behind each filter. Aim for under ~1,500 characters.

That example had defects too. Five of its claims were wrong against the code. It said the table held "every" record when it held only the ones the model could resolve. It left out one exclusion. It called an append a rebuild. It said a warning always fires when a match on other keys can hide it. It said "grouped by" where the model emits one row per month. Take the structure and re-derive every claim from the SQL.

**Why:** a README is opened by someone looking for one thing, like how to run it, or why there's no database. Dense bullets that each wrap to five lines hide that one thing. Headings and labels let a reader jump straight to it.

A model description is read by someone deciding whether a table fits their question, so each rule has to be findable by its label.

A plan is opened by someone about to act — rehearse, build slides, check a fact — and reasoning prose makes them dig for the instruction.

**How to apply:** when writing or tidying a README, plan, brief, run-sheet or model description, restructure first. Put in headings, labels and separate blocks, then tighten the sentences per [[writing-concise-and-lowercase]] and [[plain-language-in-writeups]]. Never hard-wrap per [[no-hard-wrapped-prose]]. Before restyling, check every path and number against the repo per [[verify-before-asserting]].
