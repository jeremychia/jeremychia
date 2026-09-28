# Working preferences

The short version. Each rule has a memory file under `claude/memory/` with the reasoning
and the failure cases; this file is what should be in mind by default.

## Writing

- **Lowercase prose.** Inline comments, PR descriptions, PR comments, commit bodies. Real
  identifiers and data literals keep their own casing — lowercasing those misstates the
  data.
- **Plain language, first time, without being asked.** No jargon where an ordinary word
  exists. Never use a query's own column names as prose. Lead with the headline in one
  sentence someone who has not read the analysis can act on, then the detail.
- **Never write "vintage" — write "snapshot".** Banned outright, including where the
  codebase itself uses it.
- **Short sentences.** One idea each. Split at the em-dash, the semicolon, the "and" —
  those joints are where a 40-word sentence hides four clauses. Aim under 16 words on
  average, and almost nothing over 30. This is separate from length: a short document made
  of long sentences still reads badly.
- **Never hard-wrap prose.** One paragraph is one line in PR bodies, comments, yml descriptions
  and markdown. Wrap only code and commit message bodies.
- **Lead with what went wrong, then what the change does, then what was checked, then who acts
  next.** Explain each term where it first appears. The reader is often not an engineer.
- **Short by default, and shorter than feels natural.** A PR body is ~150 words of prose,
  200 at the outside. Write short first — drafting long and trimming produces a compressed
  essay rather than a short document.
- **Cut whole categories, not sentences.** The reasoning that led to the change, the
  evidence for a claim nobody disputes, what was decided against, how the tooling behaved,
  the validation method rather than its one number. All of it belongs in the ticket.
- **Leave no drafting history in the document.** The reader is seeing it for the first time.
  No earlier passes, no self-correction, no confessing an invented detail, no "you asked."
  Keep the instruction, delete the frame. The learning goes in memory.
- **State the consequence, not just the effect.** "~400k rows fall in the warn window"
  → "…so that test will start warning on a lot of rows."
- **Collapse long SQL and query output in `<details>`** so the prose stands alone and the
  query is there to check rather than to read.
- **Build READMEs, plans, briefs and run-sheets for skimming.** A heading or bold label per
  idea, checkboxes for actions, one numbers table, what to show split from what to say.
- **Self-assessments follow four numbered parts:** impact summary, framework assessment, growth actions, weekly log. Put highlights before the tables. Split each gap into my behaviour vs. an opportunity I need. Keep links, and use standard capitalisation.
- **Write instruction files in imperatives.** Rule files, review guidance, skills, runbooks:
  lead with the verb — flag, ask, name, never. Cut any sentence that explains why a rule
  matters before saying what the rule is, and anything describing the document's own
  structure. Keep one worked case per rule, at the end.

## Comments and docs in code

- **One line wherever possible**, in any language. If a second line is needed, check
  whether it explains *why the change was made* — that part goes in the PR.
- **A comment or description carries business context only.** Why a rule exists, why an exception is booked separately. It must not narrate a prior architectural decision, a refactor's history, an incident, or plan statistics — those go stale in the file while staying true in the PR.
- **A date, a version or a "since" in a description is almost always history.** Move it to the PR. A permanent property of the data stays ("null on months snapshotted before this column existed").
- **Prose about a model belongs in its description**, not in a comment above the SQL —
  the description is what a downstream consumer actually sees.
- **Don't defend a choice against an alternative nobody proposed.**
- **Link the document that defines the business rule** rather than paraphrasing it.

## Reviewing

- **A finding names the scenario and the consequence.** Which input, and which number or
  consumer is affected. Without both it is not worth posting.
- **Assert what the repo shows; ask about what only the data knows.** Both in the same
  comment where they apply to one finding.
- **Verify every claim before writing it.** Assertions that sound right are the ones that
  turn out wrong; check rather than infer, and say when something was not verifiable.
- **Same length rules as everything else.** 1–3 short lowercase paragraphs per finding:
  what is wrong, the number that proves it, the fix.
- **A written assertion needs a test behind it.** An invariant in a description that
  nothing checks reads to everyone downstream as though it were enforced.
- **Name things for the assertion, not the caller.** A helper named for the first thing
  that used it is a helper nobody finds again.

## Engineering

- **Abstract at two callers, not one.** Shared by two or more → a macro or a shared
  function. Used once → keep it in the file that owns it, so the logic stays visible where
  it applies.
- **Look for an existing implementation before writing a new one.** Check the packages
  first, then the project's own helpers, reading candidates rather than judging by
  filename.
- **One definition per concept.** The same business rule computed in two places drifts.
  Reusing an established name for a different definition is worse than duplicating it.
- **Prefer a named CTE to a nested subquery.**

## Git

- **No AI attribution.** No `Co-Authored-By: Claude` trailer, no "Generated with" footer.
  Ask before adding any other bot attribution.
- **Conventional Commits** for commit subjects and PR titles.
- **Re-check the current branch immediately before committing.** Don't trust the branch
  name from earlier in the session.
- **Never rewrite or reset a branch someone else created** — say the stray commit is there
  and let me decide.
