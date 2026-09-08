---
name: test-descriptions-state-the-invariant
description: A test description states the invariant it pins, never the fixture row that demonstrates it
metadata:
  type: feedback
---

A unit test description states **the invariant the test pins**. It never names the row that
demonstrates it. I pushed this over three rounds, ending at: "really consider if you need
to put examples in the descriptions. i think it's not necessary."

**No examples. No row ids, no dates, no literal values.** They are pointers into the
fixtures, not content — and they rot silently when a fixture moves, because nothing checks
the prose against the data. Write the assertion instead:

> `8005 sits at generation 3 against an incoming generation 2, so the guard must reject it`
> → `a row already at a higher generation is not overwritten by a lower-generation message`

Same information, and it survives a fixture edit.

Also cut: restating the variables the test sets (that is the config block two lines below),
per-row outcomes (that is the expected-output file), and row-by-row fixture provenance.

Keep, because it exists nowhere else: the mutation check ("drop that filter and it is
emitted twice"), why a column is excluded from the comparison, and one line confirming
that any personal-data values are synthetic.

**Shape:** imperative lead ("Check the run rebuilds only the reloaded partitions: …"). One
bullet per *invariant* where each is a different mechanism; prose where the assertions are
the same few behaviours every time — bullets there make cross-file repetition look like
content. Sentence case here, matching the other descriptions in a schema file; the
lowercase rule in [[writing-concise-and-lowercase]] covers code comments and PR prose, not
these.

**Why:** the fixtures are the ground truth for what the test holds. The description's only
job is the intent, which is what a reviewer needs in order to spot a missing case.

**How to apply:** say why each fixture row exists, never what the expected output already
states. Applied across 51 descriptions in one sweep it took 6,752 words to 3,853, about 73
each. The related standard when reviewing: [[an-assertion-needs-a-test]].
