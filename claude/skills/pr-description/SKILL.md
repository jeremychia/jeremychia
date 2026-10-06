---
name: pr-description
description: Write a pull request description for the current branch using the repo's live pull request template. Use when asked for a PR description, PR body, PR write-up, to "fill out the PR template", or to open/update a PR for the current branch.
---

# PR description

Produce a filled-in PR body for the current branch that matches the repo's template
exactly, states only what the diff and the author actually support, and asks for the facts
that cannot be read out of the code.

## The budget — apply it while drafting, not after

**Write short first.** Drafting the full version and cutting it produces a compressed
essay — every sentence survives in shortened form.

| Measure | Limit |
| --- | --- |
| Prose words, checklist excluded | **≤ 300**, aim ~200 |
| Any one section | ≤ 6 lines |
| Summary | ≤ 3 sentences, plus a list if the change has parts |
| Tables | 1 at most, and only where it replaces more prose than it costs |
| `<details>` blocks | 1 at most |

**Plain english beats the word count.** Where the two conflict, go over the limit. The limit
exists to stop waffle, and there are two ways to hit it: cut the waffle, or compress the
vocabulary. The second is a trap. "A narrowed case arm that leaves rows with no label" is
nine words and unreadable to anyone who has not just read the code. "Someone tightens one
rule in a chain of if/then labels, and the rows that no longer match end up with no label at
all" is twenty-four words and needs no explaining. Write the second and go over.

Order of operations: write it plainly, cut what is genuinely redundant, stop. Never buy
words back with jargon. And note `wc -w` over-counts — it counts table cells and list items
as prose, so judge the prose and use the number as a hint.

**Lowercase prose throughout** — body, section text, bullets. Real identifiers and data
literals keep their own casing; lowercasing those misstates the data. Plain, declarative,
no build-up.

**The ticket is the record of the work; the body is only what a reviewer needs in order to
approve it.** When a fact feels too good to cut, put it in the ticket and link it.

## 1. Load the live template — never a remembered copy

Templates change. Read it at run time:

```bash
cat .github/pull_request_template.md
```

- If missing, try `.github/PULL_REQUEST_TEMPLATE.md`,
  `.github/PULL_REQUEST_TEMPLATE/*.md`, `docs/pull_request_template.md`.
- If the working tree modifies the template, also check
  `git show origin/HEAD:.github/pull_request_template.md` and use the **working-tree**
  version — that is the template the repo is moving to — mentioning the difference.
- If none exists, say so and fall back to: Summary (What / Why), Validation, Manual
  Actions, Cost, Checklist.

Reproduce the structure verbatim: same headings, same order, same heading levels, same
checklist wording and links, and keep any trailing note block. Replace italic `_hint text_`
with real content. **Do not delete sections that turn out to be N/A** — templates commonly
say so explicitly; keep the heading and write `N/A` or `none.` plus a one-line reason. That
is the one place the word budget loses.

## 2. Gather the diff context

Resolve the base branch first (`main` unless the repo says otherwise), then:

```bash
git branch --show-current
git log --oneline "$BASE"...HEAD
git diff "$BASE"...HEAD --stat
git diff "$BASE"...HEAD
git status --short          # uncommitted work is NOT part of the PR
```

Read the changed files where the diff alone is not self-explanatory.

- Describe **only** what is committed on the branch. If the working tree holds unrelated
  uncommitted changes, exclude them and say so.
- If the branch name carries a ticket key, reference it in the Summary and offer the
  tracker link. **Never invent a ticket number.**
- Derive a Conventional Commits title (`feat:`, `fix:`, `docs:`, `chore:`, …) and offer it
  alongside the body.

## 3. Fill what the diff supports

| Section | Derive from |
| --- | --- |
| What | The files touched, grouped by intent — not a file list |
| Why | Ticket key, commit messages, the defect or gap the change closes |
| Validation | New or changed tests in the diff — assertions, fixtures, test files |
| Manual Actions | Migrations, backfills, changed keys or partitioning, renamed or dropped fields, new reference data, anything whose historical rows the normal run will not rebuild |
| Cost | Whether the change adds work at runtime (new sources, wider windows, full rebuilds) or is metadata-only |
| Checklist | Tick only what the diff or the author's answers justify |

Metadata-only changes legitimately give `N/A` for Validation, Manual Actions and Cost — say
why in one line each. A diff touching only tests is a test-only PR: say so rather than
reporting Validation as `N/A`. If you find no tests, leave the box unticked and ask (§4)
rather than assuming they were skipped.

### Links the Summary has to carry

Most templates ask for these in the Summary hint in as many words ("add any relevant links
that help contextualise — Slack, RFCs, designs"), so a Summary with no links has not filled
the section. Gather:

| Link | Where to find it | If you cannot |
| --- | --- | --- |
| **Ticket** | the branch name's key, or a commit message | ask (§4) — never guess a number |
| **Thread** that asked for the change or agreed the approach | the user, a chat URL in a commit or code comment | ask |
| **Design doc, RFC or wiki page** defining the business rule | a link already in the code or a neighbouring file | ask |
| **Related PRs** — the one this stacks on, the follow-up, the cross-repo half | `git log`, `gh pr list` | search before asking |
| **Consuming code** for a new export or interface | the consumer repo, line-anchored | ask which repo |

Two rules on how they appear:

- **Anchor the link on the thing, not on bare punctuation.** `[TICKET-123](url)` and
  "agreed in [this thread](url)", not a trailing "(see: url)".
- **Say what the reader gets from each one** in the same clause — "the RFC that defines the
  cutover date", not "see the RFC". A bare link makes the reviewer open it to find out
  whether they needed it.

For a chat thread, **name the channel and what was decided there**, not just the link — a
link alone rots for any reader without channel access. Links are cheap against the budget
and are the first thing a reviewer follows, so they survive the cut in §5.

### How to word it

The reader has not opened the files you just edited. That is the whole rule, and the one
most often broken — a body written in the vocabulary of the diff reads as complete to its
author and as noise to everyone else.

**The test: could someone on another team read this and say what goes wrong?** Two things
fail it every time:

- **Words that only mean something inside the change** — *case arm, invariant, caller,
  fires, grain, exposure, predicate, assertion.* Say what the thing does. "A shared test
  that many models use" beats "caller".
- **Section numbers, rule codes and file paths standing in for content.** Those are places
  to look, not information. Say what the check catches, then cite the code if the reader
  needs to find it.

Then the rest:

- No jargon where an ordinary word exists. predicate → condition. bucket → those rows.
- **Never use your own query's column names as prose.** A reader has not seen your query.
- No internal shorthand for things the reader cannot see — say what the rule *does*.
- **Lead with the headline in one sentence a non-author can act on**, then the detail.
- State the consequence, not just the effect: "~400k rows fall in the warn window" →
  "…so that test will start warning on a lot of rows."
- Explain *why* something changed in terms of the data, not in terms of which condition
  rejected it.
- Keep SQL, but collapse it in `<details>` so the prose stands alone.

### Write standard english sentences

Short, lowercase and jargon-free is not enough on its own. Read each sentence alone and
check it has a plain subject, a plain verb, and numbers as numerals.

- **Open the Summary with "this pr adds / fixes / introduces …"**, then the ticket link.
- **Name the key change in the Summary's first 2 sentences**: the one piece of logic the
  reviewer must check, in plain words, plus the fault it fixes. Never give only the outcome.
  "a payment charged back twice no longer gets each chargeback paired with the other one's
  settlement line" → "this pr fixes chargebacks being paired with the wrong settlement line.
  a payment's chargebacks are now put in order by value date instead of by transaction id."
- **Start table rows and bullets with a third-person verb:** "ensures every checkout ends as
  one outcome", "counts only fee lines", "does not rebuild final months". Never a bare rule
  with an implied *must*.
- **Start Validation bullets with a bold label, then what was done:** "**data accuracy:**
  the total matches the snapshot to the cent. this confirms …".
- **Give each decision a bold lead-in that states it**, then one sentence on why.
- **Name the mechanism; never use a metaphor-verb or aphorism.** "borrows the rate" →
  "carries over the latest available rate". "bites when loosened" → "fails when the
  threshold is lowered". "the part that holds today" → "the rules that remain valid today".
  "the model holds one month" → "the model contains data for one month only". "once the
  data lands" → "once the data arrives".
- **Never make an object the actor.** "the entity invoices shipping and nothing else" →
  "the entity invoices only for shipping".
- **Write numbers as numerals:** "12 checks", "more than 10%", "27.9 million".
- **Split em-dash and semicolon chains** into one sentence per fact.
- **Expand an abbreviation the first time** — "a service level agreement (SLA)".
- **Drop intensifiers:** genuinely, simply, just, critical, proper.
- **Mirror What in Why when What has parts.** Number the Why items in the same order, one
  per What bullet, each with a bold lead-in naming the fault: "**a day could go missing:**".
- **Give the exact values the code uses**, in backticks: "`429`, `500`, `502`, `503` and
  `504`", never "5xx" when the code lists four of them.

### Take structure, not text, from a pasted rewrite

When another tool's rewrite is pasted back, keep its layout and redo the wording.

- **Keep:** a numbered or bold-labelled layout that makes sections line up, backticks on
  literals, any sentence split that reads better.
- **Reject:** capitalised prose and title-case labels ("Proper Upload Error Handling"),
  noun-phrase bullets, intensifiers, its preamble ("here is a cleaned-up version") and any
  "what was refined" section after the body.
- **Restore the template:** its hint lines and checklist wording, verbatim, even where the
  rewrite dropped or reworded them.
- **Re-check every fact against the diff.** A rewrite generalises: "5xx" for four status
  codes. It also introduces ambiguous terms: "pre-commit code" reads as the pre-commit hook.

Worked case: a rewrite of a three-fix body turned Why into three numbered, bolded items
matching the three What bullets. That layout was taken. Its capitals, "critical", dropped
template hint line and "what was refined" footer were not.

## 4. Ask about what the diff cannot tell you

Batch up to 4 questions in one call. Skip anything the diff clearly answers — do not ask
for confirmation of something visible in the code. Ask when:

- **Why** is unclear — no ticket, terse commits, no obvious defect.
- **Validation** — was a comparison run? Ask for the link or query; offer "no validation
  performed" and "tests only" as options.
- **Manual Actions** — the diff suggests a migration or backfill: confirm it, and whether
  it runs before or after merge.
- **Cost** — was an analysis done, and what was the outcome?
- **Downstream consumers** — a shared interface or contract changed: who was notified, and
  where?

**Always ask for any link from §3 that is not in the diff or in the conversation.** These
are the questions most often skipped, because a body reads complete without them — and the
ones that cannot be recovered later, since only the author knows which thread the decision
happened in. Ask, in one batched call:

- **The ticket**, where the branch name carries no key. Offer "no ticket"; never construct
  a plausible key from the change.
- **The chat thread or channel** where this was asked for, decided, or reported. Ask for
  both the link and one line on what was decided there. Offer "not discussed".
- **The design doc, RFC or wiki page** defining the business rule, whenever the change
  implements a named process. Accept "no page exists" and say so in the body rather than
  linking something that does not answer it.
- **The consuming repo or service** for a new export, interface, or contract change, and
  who supports it.

Always include an escape hatch ("Not applicable", "Leave as TODO"). If the author declines,
write `TODO: <what is needed>` rather than inventing a plausible-sounding validation, cost
figure, or notification.

**Never fabricate** links, ticket ids, threads or channel names, wiki pages, reviewer
names, row counts, byte counts, or claims that tests or notifications happened. A guessed
URL is worse than an admitted gap: it looks checkable, so nobody checks it. Write
`TODO: link to <the thing>` and flag it in the handover.

## 5. Read it back, then cut by category

**First, read it as someone who has not seen the diff.** Every word that only makes sense
with the files open is a rewrite, not a cut. Do this before counting: the count tempts you
to fix length by compressing vocabulary, which makes it worse.

Then count, rather than eyeballing it:

```bash
sed '/^#* *Checklist/,$d' <path> | wc -w      # hint, not a limit: aim ~200, cap ~300
```

This over-counts — table cells and list items are not prose. If the number is high and the
prose is plain and non-repetitive, leave it.

Then re-read once and cut every sentence that explains **how you got there** rather than
**what a reviewer must check**.

**Cut by category, not by sentence** — proportional trimming does not get you there. These
go wholesale:

- the reasoning that led to the change — the reviewer is judging the result, not auditing
  the derivation
- count tables — usually one sentence
- evidence for a claim nobody was going to dispute — keep the proof for the reply, where it
  was actually asked for
- what you decided *not* to do, and why — ticket material
- the tool's behaviour: which flags you passed, what it got wrong, what you reverted
- the validation method, as opposed to its one meaningful number
- before/after examples — the diff shows all of them
- essays justifying the approach — state the rule in one sentence

What survives: what changed and its scope, the rule in a sentence, what was validated as
one number, the manual actions, and **every link from §3**. Never cut a link to save
words — they cost a handful of words each, the template asks for them, and they are the
first thing a reviewer follows. "Evidence for a claim" above means a restated proof in
prose, not the link to where the decision was made.

Still over? Drop the largest table or `<details>` block and see whether anything is lost,
then move the residue to the ticket and link it. Reduce a section to one line rather than
deleting it.

## 6. Deliver

1. Show the finished body in chat as a fenced markdown block.
2. Write it to a scratch file so it can be reused.
3. State the suggested title, the word count you measured, the assumptions made, and
   anything left as `TODO`.
4. Offer — do not run unprompted — the command to apply it:

```bash
gh pr create  --title "<title>" --body-file <path>   # new PR
gh pr edit    --body-file <path>                     # existing PR
```

Check `gh pr view --json number,title` first: if a PR exists for the branch, `edit` is the
right verb, and mention that it overwrites the current body. Add no AI attribution footer.

If detail you cut is later asked for, put it in a **follow-up PR comment** or the ticket
rather than growing the body.
