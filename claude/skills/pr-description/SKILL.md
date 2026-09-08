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
| Prose words, checklist excluded | **≤ 200**, aim ~150 |
| Any one section | ≤ 5 lines |
| Summary | ≤ 3 sentences |
| Tables | 1 at most, and only where it replaces more prose than it costs |
| `<details>` blocks | 1 at most |

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

### How to word it

Write to the budget as you go — a section that wants more than 5 lines is a signal that
most of what you are about to write belongs in the ticket. Short is not the same as
readable, and both are required: the body is read by someone who has not seen your
analysis.

- No jargon where an ordinary word exists. predicate → condition. bucket → those rows.
- **Never use your own query's column names as prose.** A reader has not seen your query.
- No internal shorthand for things the reader cannot see — say what the rule *does*.
- **Lead with the headline in one sentence a non-author can act on**, then the detail.
- State the consequence, not just the effect: "~400k rows fall in the warn window" →
  "…so that test will start warning on a lot of rows."
- Explain *why* something changed in terms of the data, not in terms of which condition
  rejected it.
- Keep SQL, but collapse it in `<details>` so the prose stands alone.

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

Always include an escape hatch ("Not applicable", "Leave as TODO"). If the author declines,
write `TODO: <what is needed>` rather than inventing a plausible-sounding validation, cost
figure, or notification.

**Never fabricate:** links, ticket ids, threads, reviewer names, row counts, byte counts,
or claims that tests or notifications happened.

## 5. Count it, then cut by category

Run the count rather than eyeballing it — a draft that is twice the limit still reads as
appropriately short from the inside:

```bash
sed '/^#* *Checklist/,$d' <path> | wc -w      # target ≤ 200
```

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
one number, and the manual actions.

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
