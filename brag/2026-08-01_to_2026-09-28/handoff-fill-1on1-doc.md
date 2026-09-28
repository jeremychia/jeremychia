# Hand-off: fill the 1:1 doc's weekly achievements table

## Task

Fill the "Last Week Achievements" column of the table on the **Weekly Achievements/Reflections** tab of the 1:1 notes doc, from the brag list already compiled. Leave every "Weekly Reflections" cell empty for Jeremy.

- **Doc:** https://docs.google.com/document/d/1xAsWxVkSAr7mVcFgMuj_mED277CEax4_hRyN6PS_Pto/edit?tab=t.8vgt5q95pls
- **Drive file id:** `1xAsWxVkSAr7mVcFgMuj_mED277CEax4_hRyN6PS_Pto`
- **Tab id:** `t.8vgt5q95pls`

## Before you start

- [ ] Confirm the **Google Docs** editor connector is loaded (search for `update_doc` / `read_doc`). If it isn't, stop and tell Jeremy. Never create a new doc instead.
- [ ] Load the `anthropic-skills:google-workspace` skill and read `references/docs.md` in full.
- [ ] Read the source material:
  - `/Users/jeremychia/Documents/Github/jeremychia/brag/2026-08-01_to_2026-09-28/brag-list.md` (the brag list, with links)
  - `.../sources/gh_prs.tsv` and `.../sources/jira_tickets.tsv` (dates, to place each item in its week)
  - `.../sources/slack_*.md` and `.../sources/confluence_slack_summary.md`
- [ ] Ask Jeremy one question before writing: **one row per week (8 rows) or one row for the whole period?** Recommend weekly, because the template is weekly.

## The table today

It has a header row (**Date | Last Week Achievements | Weekly Reflections**) and one empty row whose first cell says "Date". Replace that placeholder row. Don't add rows below it.

## What goes in each achievements cell

- **Date cell:** the week's Monday to Sunday, e.g. "3–9 Aug 2026". Weeks run from 3 Aug to 27 Sep. Put 28 Sep in the last row, or leave it for next week.
- **Achievements cell:** 3–6 bullets, each one line, biggest business number first.
  - **Shape of each bullet:** what was done, then its impact. Example: "stopped €1.29m of cost moving out of august (#2361)".
  - **Links:** link every bullet to its PR, Jira ticket, Confluence page or Slack thread. Use the full URLs from brag-list.md, and never build a Slack URL from an id you haven't seen.
  - **Flags:** add "(above and beyond)" on work outside Jeremy's remit (core billing, dbt Labs open source, systems others use). Add value tags in square brackets, e.g. [ownership].
- **Last row only:** add a closing bullet linking the full brag list, which holds the IC3/IC4 mapping:
  https://github.com/jeremychia/jeremychia/blob/main/brag/2026-08-01_to_2026-09-28/brag-list.md
- **Style:** lowercase prose, plain language, short sentences. No drafting notes in the doc.

## How to write it

1. `read_doc` on the tab, keep the `revisionId`, and find the table's cell positions. Use the skill's `docs_index.py outline`, or `fill-table` if more rows are needed.
2. Put all inserts, including the new rows, in **one** `update_doc` batch, guarded with `writeControl.requiredRevisionId`. Insert from the end of the doc backwards, so positions don't shift.
3. Add links with `updateTextStyle.link.url` on the text ranges you inserted.
4. Read the doc again and check:
   - the column order
   - the reflections cells are empty
   - every bullet has a working link
   - nothing outside the table changed
5. Tell Jeremy what was filled. Say it is the same doc with the same link.

## Facts already settled

- **Values:** Vinted Values are aim high, take ownership, co-create, care and grow. See `claude/skills/brag-list/context/vinted-values.md`.
- **Standing goals:** escrow revenue controls, and backend validation with checkout. See `claude/skills/brag-list/context/manager-format.md`.
- **Slack coverage:** 1–14 Aug and 12–20 Sep were only searched by keyword. The weekly rows for those weeks may be thinner, so say so rather than padding them.
