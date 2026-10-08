# My Claude Code working system

How I want Claude to work: my writing standards, review standards, and engineering
preferences, in the form Claude Code actually reads.

This is the portable half of my setup. It holds **preferences only** — how I want things
written and reviewed. Anything specific to an employer's codebase (model names, project
ids, ticket keys, internal links) stays in that project's own local memory directory and
is deliberately not here.

## Layout

```
claude/
  CLAUDE.md              always-loaded instructions — the short version of everything
  memory/
    MEMORY.md            the index Claude loads each session, one line per memory
    *.md                 one preference per file
  skills/
    pr-description/      write a PR body against the repo's live template
    memory-keeping/      how to add to and maintain this system
    data-test-review/    write and review dbt tests: placement, keys, windows, limits
    dbt-pr-review/       the questions dataverse reviewers ask most on dbt PRs
```

## Install

```bash
make install-claude      # symlinks claude/CLAUDE.md and claude/skills into ~/.claude
```

That makes the preferences global, so they apply in every repo rather than only where
they were first learned. `make uninstall-claude` removes the symlinks. Neither touches
per-project memory.

Symlinks rather than copies, so editing a file here takes effect immediately and the repo
stays the single source of truth.

## How the two halves fit together

| | Lives in | Loaded |
| --- | --- | --- |
| Preferences — writing, review, engineering taste | this repo, symlinked to `~/.claude` | every session, every repo |
| Project facts — a codebase's internals, tickets, prod behaviour | `~/.claude/projects/<project>/memory/` | only in that project |

The split is the point: a preference is about me and travels; a project fact is about a
codebase, goes stale, and belongs next to it. When something learned in a project turns
out to be a general preference, it moves here and the project copy is deleted rather than
kept in both.

## Maintaining it

Use the `memory-keeping` skill. In short: one fact per file, `feedback` memories say
**why** and **how to apply**, link related ones with `[[name]]`, and add exactly one line
to `MEMORY.md`. Prefer updating an existing file to adding a near-duplicate, and delete
what turns out to be wrong.
