---
name: an-assertion-needs-a-test
description: My most-repeated review comment — an invariant written into a description with nothing checking it
metadata:
  type: feedback
---

**"Are you testing this assertion?"** I asked this six times on a single PR, which makes it
the thing I most reliably look for when reviewing. A description states an invariant,
nothing checks it, and from then on everyone downstream reads it as though it were
enforced.

What counts as an assertion: a stated granularity ("one row per shipment leg"), a
uniqueness claim ("campaign ids are unique"), a range claim ("amounts are always
positive"), a nullability claim ("never null for completed rows"). Each is a testable
statement someone wrote and nobody wired up.

**It applies at every layer**, including intermediate and preparation models — not just the
consumer-facing ones. Where the model is a *view*, a test on it re-runs the whole upstream
chain per run, and the right answer is the same test on the first materialised consumer,
filtered to the relevant rows. Say which of the two you are asking for; that is a real
cost difference, not a detail.

**The inverse is a finding too, and is easier to miss:** a description that no longer
matches the tests in the same file. A granularity naming three columns next to a
uniqueness test on two of them means one of them is wrong, and the diff does not say
which.

**Why:** a grain claim that is false is a fan-out, and a fan-out multiplies money
downstream. That is what makes this worth a comment rather than a tidiness note.

**How to apply:** name the specific claim, name the test that would check it, and say what
goes wrong if it is false. One comment per file, not one per line.

**Assert it, don't ask it.** Whether a test exists is visible in the file in front of me,
so "the description says one row per campaign and no test here checks it" is the comment.
"Are you testing this?" is the same finding phrased as though the repo were unreadable —
and it puts the work back on the author. This is the one thing to fix about how I phrase
it. See [[verify-before-asserting]] for the general form and
[[test-descriptions-state-the-invariant]] for what the test's own description should say.
