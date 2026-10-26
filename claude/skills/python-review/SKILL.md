---
name: python-review
description: Write or review Python so a reviewer can see what each object depends on and why each item is kept or skipped. Use when writing or reviewing Python in a PR (linter rules, CLI code, ingestion jobs), when adding data to an existing class, when a loop has several `if …: continue` guards, or when answering Python review comments.
---

# Python review

Run these checks on every Python change before asking for review.

## 1. Pass only what the code reads

- **List the fields the new code reads** from any shared structure it is given.
- **Attach a lean, typed field holding exactly those fields** to the object that needs them. Build it once, in the place that already owns the parent structure, and share the one instance.
- **Never attach a whole parent structure**, such as a full manifest or config, to every object.
- **Keep the class that owns the shared structure central.** Do not move it into a new module or pass it around, because every file that imports it changes too.
- **Check `git diff --stat origin/main...HEAD` before pushing.** Every file outside the new feature needs a reason. An import-only change in another module means something central moved.

## 2. Use full words for every name

- **Spell out loop and comprehension variables:** `parent for parent in parents`, never `p for p in parent_ids`.
- **Drop an `_id` suffix** when every value of that kind is an id.
- **Rename across the module and its tests in one commit,** and change nothing else in it.

## 3. Filter, then act

- **Sort each `if …: continue` guard** into scope (which items the code looks at) or verdict (whether to act on an item).
- **Move the scope guards into a named generator,** each guard with a one-line comment giving its reason.
- **Make the verdict one named predicate,** so the loop or comprehension keeps a single condition.

## 4. Prove a refactor changes nothing

- **Run the old and new code over the same real inputs,** and compare every output, not a count.
- **Quote the comparison in the reply,** for example "identical on all 58 inputs".

## 5. Answer review comments

- **Make one commit per review comment.** One change can answer several comments on the same point; name that commit in each of their threads.
- **Reply in each thread with the commit link** and one or two sentences on what changed.
- **Move or delete your own review notes that the change made outdated.** Edit the note in place, rather than repost it, when other people have replied under it.

## Worked cases

**Rule 1.** A linter rule needed each model's tests and lineage, so every model carried the whole manifest, and the manifest class moved into a new module. A reviewer asked why every model carried the full manifest. The fix was a frozen `relations` field holding parents, children, names, two test fields and the set of scheduled models. It was built once from the manifest's nodes, and the manifest class went back where it was. The diff then dropped five other rules' tests and a shared helper, which had only changed an import.

**Rule 2.** `any(p.startswith("source.") for p in parent_ids)` became `any(parent.startswith("source.") for parent in parents)`, and `task_id` became `task_model`, in a commit that only renamed names.

**Rule 3.** A `check()` loop had five `continue` guards before `issues.append`. Four were scope: a unit test, a test another model owns, a test that reads a source, a test that reads no scheduled model. They moved into `_tests_to_check()`. The fifth, "a task can run it", became `_runs_in_a_task()`, and `check()` became one comprehension: `for test in _tests_to_check(...) if not _runs_in_a_task(...)`.

**Rule 4.** All three refactor commits ran over the same 58 project manifests and gave identical results: 441 flagged tests with the same messages.
