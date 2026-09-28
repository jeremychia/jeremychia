---
name: restate-as-of-the-date-the-figure-was-struck
description: Quantifying an error in a frozen figure — gate the comparison source to the freeze date, and prove the method on a period the bug never touched
metadata:
  type: feedback
---

**To size an error in a figure that was frozen in the past, rebuild the decision from what the
sources knew on the freeze date. Then run the same method over a period the bug never touched, and
show it reproduces that period's figure.**

The failure: a month-end accrual was frozen on 2 September from a column that had silently broken.
I recomputed it against the source dimension as it read three weeks later and published the gap as
the error. It was not. It was the error plus every refund that arrived in those three weeks — real
events the original code could not have known either.

The control caught it. The same method over the previous month, which the bug never reached, moved
that month by 9.8%. A bug-free period must come back unchanged; 9.8% was pure method bias. Gating
the dimension to the freeze date brought the control to 0.4% and cut the headline number by 15%.

**Why:** a frozen figure is a point-in-time estimate. Comparing it to a later truth conflates the
defect with information that arrived afterwards, and always overstates. The number then gets
quoted in a close discussion, so being 15% out is not a rounding matter.

**How to apply:** find the timestamp that says when the comparison source last changed and only
trust rows that settled before the freeze. State the direction of whatever residual bias remains —
where the gate cannot tell, leave the original treatment in place so the figure is a floor, and say
so. Always report the control number next to the headline: "the same method reproduces the
untouched month to within 0.4%" is what makes the headline believable.

Two other things that bit in the same pass, both worth a separate check before publishing:

- **Never read a query result through `tail`.** A truncated result read as a complete one turned
  226k rows into a claim that a value "never occurs", and that claim invited someone to delete
  live code.
- **Trace the consumer to the actual output, not the plausibly named one.** Two exports differed by
  one word in the name. Only one read the broken flag. Asserting the wrong one would have pointed
  the whole investigation at an unaffected journal.

[[verify-before-asserting]] is the general rule; this is the shape it takes for a number.
