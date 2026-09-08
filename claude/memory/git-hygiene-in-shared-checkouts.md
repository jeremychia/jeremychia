---
name: git-hygiene-in-shared-checkouts
description: Several sessions share one checkout — re-check the branch before every commit, branch in place, never stash
metadata:
  type: feedback
---

I run several Claude sessions against the same checkout at once. Within a single turn,
another session can commit the dirty files you saw at the start, create a branch, and move
`HEAD` — so a commit you make lands on whatever branch `HEAD` points at *then*, not the
branch you created earlier. Seen in practice: a branch created from `origin/main` for one
ticket was superseded by a parallel session's branch, and the commit landed on top of that
session's unrelated work.

**Branch in the main checkout, not a worktree.** I asked for "no worktree" — I want the
branch where my IDE is pointed. Don't reach for one by default; use it only when I ask, or
when another session is visibly mid-commit in the shared tree.

**How to apply:**

- **Re-check `git branch --show-current` immediately before every commit.** Don't trust the
  branch name or `git status` from the start of the turn.
- **Never rewrite or reset a branch another session created**, even to remove your own
  stray commit. Say it is there and let me drop it.
- **Never `git stash` here.** The stash ref is per-*repository*, not per worktree, so a
  push/pop cycle of yours reshuffles other sessions' stashes — one observed stash pushed
  another session's parked work down to `stash@{1}`. The pop restored it, but an
  interrupted turn would have left it buried. Save work with
  `git diff > <scratchpad>/x.patch` and `git apply` instead.
- One branch per ticket, named `<ISSUE-KEY>-kebab-slug` where the project uses ticket keys.

**Why:** the failure is silent. A commit on the wrong branch looks fine locally and only
surfaces when the PR shows someone else's changes in the diff.

Related: [[no-ai-attribution-in-commits]] for the message itself.
