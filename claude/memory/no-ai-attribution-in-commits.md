---
name: no-ai-attribution-in-commits
description: No Co-Authored-By or "generated with" attribution in commits or PR bodies
metadata:
  type: feedback
---

Do not add a `Co-Authored-By: Claude ...` trailer to commit messages, and do not add a
"Generated with Claude Code" footer to PR bodies. Asked for it to be removed once after
the fact, which needed an amend and a force-push on an already-open PR.

**Why:** the commit history in the repos I work in has no such trailers — every commit is
authored by a person only. An attribution trailer makes my commits inconsistent with
everything around them.

**How to apply:** write commit messages without the trailer from the start, even where the
harness default suggests one. Ask before adding any other bot attribution rather than
adding it by default. Commit subjects follow Conventional Commits, same as PR titles.
