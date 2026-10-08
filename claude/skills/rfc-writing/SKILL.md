---
name: rfc-writing
description: Write, rewrite, shorten or update the status of an RFC (request for comments) or design doc on Confluence, so it reads in 2–3 minutes with the detail in collapsed sections. Use when asked to draft an RFC or design doc, cut one down, clean drafting history out of one, bring one in line with the merged code, or move its status or delivery plan forward.
---

# RFC writing

## 1. Cap the visible text

- **Keep the visible text under ~500 words**, a 2–3 minute read.
- **Put everything else in collapsed expands**: `<details><summary>…</summary>…</details>` on Confluence.
- **Title each expand for its content**, such as "Known campaigns", "How the models work", "Built against prod data", "Comparison", "Keys, lineage, cost, checks and rollout" or "Tickets and open decisions". Never title one "More" or "Details".

## 2. Open with "In short"

- **Put an info panel titled "In short" first.** Write 3–4 sentences: what changes, why, and where it stands.

## 3. Keep the space's template

- **Keep the header properties table**: Status lozenge, Created on, Author(s), Approver(s), Topic and Domain.
- **Keep the template headings**: Context, Motivation, Guiding principles, Expected Outcomes & Success Criteria, Proposal, Alternatives considered, Additional considerations and Delivery plan.
- **Show 1–3 bullets or one sentence under each heading**, then the expand.

## 4. Show only what a reader acts on

- **Show the one table of numbers that matters**, for example the impact at rollout.
- **Put decisions needed in a warning panel.** Name who decides each one.
- **Write the delivery plan as a list.** Start each step with a status lozenge: MERGED, IN REVIEW or NEXT. Link the step's pull requests and tickets.

## 5. Cut drafting history

- **Delete simulation passes, bug write-ups, "Update:" sections and earlier approaches.** Page history keeps them.
- **Delete phrases that point at an earlier draft**, such as "reinstated rather than dropped" or "now uses".

## 6. Follow the code

- **Make the RFC match the merged and open code** where the two disagree.
- **Mark a promise the code does not deliver "not built yet".** Never delete it silently.

## 7. Write plainly

- **Define each term once**, and use it the same way everywhere.
- **Prefer plain words**: "supported" or "applies", not "resolves".
- **Put every number in a table** with its context in the next column.
- **Write short sentences.** Aim under 16 words, one idea each. Split at every em-dash joint.
- **Write digits, not number words.** Expand each abbreviation on first use.
- **Use standard capitalisation** on Confluence pages.

## 8. Format safely

- **Never set text colour equal to its highlight colour.** It renders as blank blocks.
- **Avoid coloured spans** altogether.
- **Leave out wide-layout attributes inside expands.**

## 9. Update status from evidence

- **Set the Status lozenge from merged pull requests and closed tickets**, never by assumption.
- **Say what the evidence was** in the reply, for example "2 of 3 PRs merged, the last ticket is open".

## 10. Edit an existing page safely

- **Fetch the page as HTML** through the Atlassian MCP.
- **Preserve inline-comment `annotation` spans and media or figure nodes exactly.**
- **Rebuild the page in a script.** Reuse kept blocks verbatim from the fetched HTML. Never retype them.
- **Send the whole body** in the update call.
- **Re-fetch afterwards and diff it against what you sent.**
- **Check the version number went up by exactly 1.** If it went up by more, someone else edited. Report it.

## Worked case

Before, under Proposal:

> Update: after the second simulation pass we found the join double-counted refunds, so we reinstated the per-order key rather than dropping it. Originally the plan was a single wide table, but review pushed back. The new approach — two config files feed a new table, which resolves each carrier discount campaign to its orders — was rebuilt and re-run against prod, and the numbers moved by about 4%.

After:

> Two config files feed a new table that applies each carrier discount campaign to its orders.
>
> ▸ **How the models work** (collapsed: the key, the lineage and the prod run, with the 4% change in a table beside what it measures)
