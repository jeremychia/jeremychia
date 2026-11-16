---
name: name-every-value-no-catch-all-else
description: A case or var that sorts source values names every known value, sends the rest to an explicit other with a warn test, and never lets a catch-all else absorb a new value
metadata:
  type: feedback
---

**Name every known value in its own branch. Send the rest to an explicit `other`, keep null as null, and add a warn test on `other`.** This applies to a `case`, a `not in`, and a var that lists only the exceptions.

**Why:** a catch-all `else` is exclusive but silently exhaustive. A new value lands in a real group, and nobody notices until the numbers are wrong. This came up on five colleagues' pull requests in two months: a new country counted as europe, a new transfer type counted as a chargeback, a new payment platform booked to the default invoice, a new user group counted as "had an account", and a new payer treated as the buyer. Checking the data once showed the assumption was already wrong: 516 card payments paid fully from wallet balance had landed on the card provider.

**How to apply:**
- Before writing the case, cross-tab the inputs on prod over the business window, and say what each combination maps to.
- Key the rule on what defines the business concept, such as the amounts that show who charged the fee, not on a label that usually goes with it.
- Write a var as a mapping of every bucket to its values, not as a list of exceptions.
- Unit-test the `other` path and check that the test fails without it. The warn test is the data-side guard.

Related: [[an-assertion-needs-a-test]], [[search-for-an-existing-implementation]], [[what-colleagues-catch-on-my-prs]].
