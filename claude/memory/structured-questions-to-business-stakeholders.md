---
name: structured-questions-to-business-stakeholders
description: the shape for a slack message or question to finance, accounting or other non-engineers — headline number first, problem / proposed solution / numbered questions, lowercase like everything else
metadata:
  type: feedback
---

write a message that asks a business stakeholder to confirm or decide something in this shape:

1. **greeting and one opening line** naming the topic and the headline number ("11 vouchers had no provision across august and september").
2. **the problem**, as bold labels: **rule** (what was agreed, in one line), **the mismatch** (the two things that disagree, each bolded), **impact** (what happened to the numbers, each figure with its month).
3. **proposed solution**: the change in one sentence, then **financial impact** with the amounts and what does *not* change.
4. **questions for you**, as a numbered list, each answerable with yes, no or a number.

write it in lowercase, headings and labels included. mentions, country codes, currency codes and other real identifiers keep their casing. bold the key numbers and the two things being contrasted. give each figure to the precision that was measured, with its month, and say what a figure is: a rate says it is a share of value, not a count.

**Why:** asked for directly ("try to write more like this") after a paragraph-style draft. the reader is not an engineer and will act on the numbers. a labelled problem, a proposal and numbered questions let them answer point by point without rereading. the structure is what changes for this audience, not the casing: a sentence-case version was corrected with "write in lowercase". [[writing-concise-and-lowercase]] applies here too.

**How to apply:**
- fact-check every figure against its query before sending, and pair the right before and after values per month. a structured draft made it easy to copy one month's figure into the other's row.
- say which unit a count is in: distinct items vs item-months, when one item appears in two months.
- slack does not render `###` headings or nested bullets pasted from markdown. use bold lines as headings and one level of bullets.
- keep the column and table names out. say what the rule does ([[plain-language-in-writeups]]).
