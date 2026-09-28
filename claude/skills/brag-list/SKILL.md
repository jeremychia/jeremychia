---
name: brag-list
description: Compile my weekly achievements and reflections for a 1:1 with my manager from my work in the issue tracker, wiki, code host and chat. Use when asked for a brag list, a brag doc, weekly achievements, a 1on1 update, or what I did last week.
---

# Brag list

## 1. Set the window

- Default to the previous Monday to Sunday. State the dates at the top.
- Use the window the user names when they name one.

## 2. Gather from every source

- **Issue tracker:** tickets assigned to or reported by me, updated in the window. Read the descriptions for figures.
- **Wiki:** pages and comments I created or edited in the window (`contributor = currentUser()`).
- **Code host:** PRs I authored and PRs I reviewed. Include other teams' repos and open-source repos — `gh search prs --author=@me` and `--reviewed-by=@me` cover every org.
- **Chat:** messages I sent in work channels. Skip DMs and social channels.
- Read the PR and ticket bodies. Never infer impact from a title.

## 3. Fill the manager's format

One table row: **Date | Last week achievements | Weekly reflections.**

- **Achievements:** the problems I solved, documents I wrote, important meetings, contributions that had impact.
- **Reflections:** what went well, what issues I ran into, and thoughts about the company, the team and the domain.

## 4. Write each achievement

- **What was done:** one sentence. Say whether it is merged, open or blocked.
- **Business impact:** the money, the deadline, who stops waiting, which report is now right. Use the number from the ticket.
- **Technical impact:** code standards, tech debt cleared, readiness for an upgrade, manual runs removed, fewer places to edit.
- **Above and beyond:** flag work outside my remit. Examples: a fix written in another team's codebase, an upstream open-source PR, a system or tool others now use, a proposal that changes how another team works, a problem found before anyone reported it.
- **Values:** tag each item with the company values it shows. Read the company values page on the wiki first; project memory has the link. Tag a value only where the evidence shows it.

## 5. Rules

- Group by theme, not by source. Lead each group with its biggest business number.
- Link each item to its PR, ticket or page.
- Draft the reflections from evidence — blocked reviews, upstream breakages, repeated requests — and mark them as a draft. They are mine to finish.
- Leave out DMs, gossip and social chat.
- Keep my writing rules: plain language, short sentences, no jargon.

## Worked case

> **accrual moved into the wrong month (merged).** a status column changed meaning upstream, so a seven-figure fee accrual left the closing month. read the status from the right source, froze closed months, added a test. *business:* month-end close is right again. *technical:* removed wildcard imports. *above and beyond:* traced the upstream change and told its owners. *values:* take ownership, aim high.
