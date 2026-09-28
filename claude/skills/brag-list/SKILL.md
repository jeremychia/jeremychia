---
name: brag-list
description: Compile my achievements and reflections for a 1:1 with my manager, or a longer-period brag doc, from my work in Jira, Confluence, GitHub and Slack, mapped to the company values and the IC3/IC4 framework. Use when asked for a brag list, a brag doc, weekly achievements, a 1on1 update, what I did last week or since a date, or how my work maps to my level.
---

# Brag list

Read the three context files first:

- [context/manager-format.md](context/manager-format.md): the 1:1 doc, its template, the standing goals from past 1:1s, and the ids to search with.
- [context/vinted-values.md](context/vinted-values.md): the five values, and when to tag each one.
- [context/ic-framework-analytics-engineer.md](context/ic-framework-analytics-engineer.md): IC3 and IC4 statements per dimension.

[prompt.md](prompt.md) holds the original asks verbatim.

## 1. Set the window

- Default to the previous Monday to Sunday.
- Use the window the user names. "Since 1 august" means through today.
- State the dates at the top.

## 2. Gather from every source

- **Jira:** `(assignee = currentUser() OR reporter = currentUser()) AND updated >= "<start>"`. Page with `nextPageToken`. Results over the size limit land in a file, so read them with jq. Classify each ticket as a stakeholder request ("Requested by:" in the description), a self-raised ticket or an incident.
- **Confluence:** pages I created, pages I edited (`contributor = currentUser()`), and my comments on other people's RFCs.
- **GitHub:** `gh search prs --author=@me` and `--reviewed-by=@me` across every org, split by date range to get past the 200-result cap. Read the bodies of every PR outside the main repo, and of the ~25 biggest inside it.
- **Slack:** my messages in public and private channels only. Never read DMs, group DMs or social channels. Walk week by week and read every page.
- **Delegate:** for a window over two weeks, run one background agent per source, and split Slack by fortnight. Save their summaries under `sources/`.
- **Never infer impact from a title.** Quote the figure the body, ticket or page states.

## 3. Write each achievement

- **Headline:** one bold sentence with the business number, then the state (merged, open or in review) and the links.
- **what:** one or two sentences.
- **business:** the money, the deadline, who stops waiting, which report is now right.
- **technical:** code standards, tech debt cleared, readiness for an upgrade, manual runs removed.
- **above and beyond:** flag work outside my remit. Examples: a fix in another team's codebase, an open-source PR, a system others now use, a proposal that changes how another team works, a problem found before anyone reported it.
- **values:** tag each item only where the evidence shows the value.

## 4. Link everything

- **Internal links are required**, so every claim can be checked. Use the full URL: `https://github.com/<org>/<repo>/pull/<n>`, `https://vinted.atlassian.net/browse/<KEY>`, the Confluence page URL, and the Slack permalink.
- **Never build a Slack URL from an id you have not seen in a permalink.** User-group ids (`S…`) are not channels.

## 5. Map to the framework

- **Table:** one row per framework dimension, with three columns: dimension, IC3 evidence (my own work), IC4 evidence (enabling others, or beyond my scope).
- **Gaps:** add an honest gaps list against IC4. IC4 means enabling other AEs, not producing more output.
- **Standing goals:** tie items back to the goals in manager-format.md.

## 6. Output

- **Weekly:** one row for the 1:1 table (Date | Last week achievements | Weekly reflections).
- **Longer window:** write `brag/<start>_to_<end>/brag-list.md`. Include the headline, a numbers table, sections by theme, the IC table, the gaps and draft reflections. Put a "how this was compiled" note in a `<details>` block, naming any source days not read in full.
- **Evidence:** keep the raw lists and agent summaries in `brag/<start>_to_<end>/sources/`.
- **Reflections:** draft them from evidence (blocked reviews, upstream breakages, repeated requests) and mark them as a draft.
- **Style:** follow my writing rules. Plain language, short sentences, headline first.

## Worked case

> **€1.29m of cost was carried out of August that should have stayed in it.** Fixed, merged ([#2361](https://github.com/vinted/dataverse-finance/pull/2361), [FDSA-3370](https://vinted.atlassian.net/browse/FDSA-3370)).
> - **what:** an upstream change stopped cancelled purchases showing as refunded, so the accrual rule moved their fees into September. The status now comes from the payments table, closed months stay frozen, and a daily test guards it.
> - **above and beyond:** I traced the upstream change and warned its owners so other consumers can check their models.
> - **values:** [ownership] [aim high] [co-create]
