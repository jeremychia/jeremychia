---
name: explain-to-a-reader-who-was-not-there
description: The shape Jeremy wants for a write-up — what went wrong, what this fixes, what was checked, what happens next — in words a non-specialist reads once
metadata:
  type: feedback
---

**Structure a write-up as what went wrong, what this fixes, what was checked, and what happens next. Explain each term the first time it appears.**

Jeremy rewrote one of my PR bodies to show the register he wants. The content was already right; the way in was not. What his version did:

- **A short labelled bullet per idea**, the label in bold and the sentence after it plain: "**the bug.**", "**the impact.**", "**why it happened.**" A reader can take the first three words of each and still know what happened.
- **Numbered list for what the change does**, one action each, in the order a reader cares about: the fix, the effect, what is protected, what is now guarded.
- **Every term explained where it appears**, not assumed. "fee estimates (accruals)". "historical snapshots are locked (frozen)". A cancelled purchase is "a user pressing buy", an attempt "is finished in seconds".
- **The headline number in the first bullet**, bolded, with the direction: booked "roughly €1.29 million too high".
- **A closing section of who does what next**, separated from the analysis, naming the team and the ticket.

**Why:** these land in front of accountants, other domains' engineers and managers, not only the reviewer. The analysis is worth nothing if the first paragraph loses them, and that is the paragraph that decides whether the rest gets read.

**How to apply:** keep the links, the tables and the evidence exactly as they are — collapse queries in `<details>` and the prose stands on its own above them. Change only the way in. Write the sentence a reader who has never seen the system would need, then the detail under it. This governs *shape*; [[plain-language-in-writeups]] governs vocabulary and [[writing-concise-and-lowercase]] governs length and casing — headings and prose stay lowercase even when copying this structure.
