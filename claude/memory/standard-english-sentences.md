---
name: standard-english-sentences
description: Write each sentence the way an ordinary professional writer would — plain subject and verb, numerals, no aphorisms or metaphor-verbs; still lowercase
metadata:
  type: feedback
---

**Write each sentence in standard english.** This is a third axis, separate from length ([[writing-concise-and-lowercase]]) and vocabulary ([[plain-language-in-writeups]]). A sentence can be short, lowercase and jargon-free and still read as a compressed riddle. I have asked for it four times, each time by pasting a rewrite as the target.

**Characteristics to follow:**

- **plain subject, plain verb.** "the control compares the accrued amount against the invoiced fee." Not "accrued vs invoiced, per month".
- **verb-first, third person in bullets and table rows.** "ensures every checkout ends as one outcome", "counts only fee lines", "does not rebuild final months". Never a bare rule with an implied *must*.
- **headline sentence first.** "this pr adds / fixes / introduces …", then the link that defines the rule.
- **bold label, then the fact.** Validation bullets lead with "**data accuracy:**", "**independent reconciliation:**". Each decision leads with a bold statement of the decision, then one sentence on why.
- **past tense for what was done.** "simulated the close", "verified that", "added 7 unit tests".
- **numerals, never words.** "12 checks", "more than 10%", "277 million" rather than "277m".
- **expand an abbreviation the first time it appears.** "a service level agreement (SLA)".
- **one fact per sentence.** Split at the em-dash and the semicolon.
- **name the consequence in full.** "flagging earlier would produce a false positive for every month."
- **name the referent instead of "it", "they", "this" or "that".** Repeat the noun, even if it reads as repetitive. "update it to match the fix above" → "update this sentence to match the fix in the comment on `variance_eur`". "add it to the grain" → "add `reporting_company_name` to the grain". "above" and "below" are vague too, because review comments do not stay in order, so name the comment.

**Words to avoid, and what to write instead:**

| avoid | write instead |
| --- | --- |
| metaphor-verbs: "borrows the rate", "bites when loosened" | "carries over the latest available rate", "fails when the threshold is lowered" |
| aphorisms: "the part that holds today" | "the rules that remain valid today" |
| objects as actors: "the entity invoices shipping and nothing else" | "the entity invoices only for shipping" |
| "gets a second reader" | "now has a second downstream consumer" |
| "off by 0.18%" | "shows a 0.18% variance" |
| "the 2% is a proposal. X to confirm." | "the 2% threshold is a proposal and awaits confirmation from X." |
| "that warning is the cue to re-size it" | "a warning means the limit needs re-sizing" |
| data as a container or traveller: "the model holds one month", "the month held in X", "once the data lands" | "the model contains data for one month only", "the same month as the data in X", "once the data arrives" |
| "half rows" | "incomplete rows" |
| intensifiers: genuinely, simply, just | nothing — delete them |

**Keep my own rules when a rewrite comes from another tool.** The pasted targets come back title-cased, longer, with the template's checklist reworded and units added. Take the sentence construction only. Keep lowercase (asked for explicitly: "just keep it in lowercase as well"), keep the template's checklist and note text verbatim, and re-check every figure. One target added a currency symbol to a three-way split whose parts summed to more than the total it was meant to reconcile, so the unit was a guess.

**Why:** compressed sentences read as a style tic, and the reader has to decode them. A document that passes the length and vocabulary checks can still fail this one.

**How to apply:** after drafting, read each sentence alone. Ask whether it has a plain subject, a plain verb and its numbers as numerals. If a clause sounds like a maxim, rewrite it as the mechanical fact it stands in for. On a structured PR with headings and a table, the result can run past the word budget, and that is accepted ([[pr-description-budget]]).
