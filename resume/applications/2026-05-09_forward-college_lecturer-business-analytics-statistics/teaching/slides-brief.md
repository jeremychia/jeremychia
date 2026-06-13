# Slides Brief — Pedagogy Presentation
## ST2187 Week 2: Univariate Data Visualisation and Descriptive Statistics
**For:** Haikel (try-out) · 10–15 minutes · ~8 slides

Each slide below includes: title, body content, visual suggestion, and speaker notes.
Design should be minimal — Forward College aesthetic leans clean and text-light.

---

## Slide 1 — Title slide

**Title:** What's wrong with this?

**Subtitle:** *(no subtitle — let the question breathe)*

**Body:**
> "You have monthly crime rates for 50 years. You compute the mean, median, and standard deviation, then build a histogram."

**Visual:** Single large quote block, centred. No other elements. Dark background or white background with one strong typographic treatment.

**Speaker notes:**
Open with this question on screen before saying a word. Let it sit for five seconds. Then: "Hold that. We'll come back to it." Move immediately — don't explain it. The audience should be slightly unsettled.

---

## Slide 2 — The design logic

**Title:** Separate exposure from application

**Body (three points, kept short):**
- Before class: targeted reading, two videos, three tutorial problems, one submitted dataset
- After the tutorial: a worked example — the full reasoning chain, annotated
- In class: interpretation, critique, peer challenge — not content delivery

**Visual:** A simple two-column split. Left column: "Before" with a clean list. Right column: "In class" with a clean list. Or a horizontal timeline: Pre-work → Quiz → Tutorial Review → Pair Work → Peer Discussion → Debrief.

**Speaker notes:**
The key point to land here: the worked example is sequenced *after* the tutorial problems, not before. Students attempt the problem first, then see the template. This is grounded in cognitive load theory — high element interactivity material (reasoning from statistics to claim to critique) exceeds working memory without a schema. The worked example builds the schema. Sweller (1994) if they ask for the reference.

---

## Slide 3 — The pre-work: worked example

**Title:** "Air quality in our city averages 48 AQI — comfortably within the WHO moderate range."

**Body:**
- Mean = 48, Median = 41, SD = 22, Min = 18, Max = 147
- The claim is technically accurate
- What is it hiding?

Then three reveal points (can animate in or just list):
1. The mean is inflated — most months are actually below 48 (median = 41)
2. SD = 22 means the spread puts some months in "unhealthy for sensitive groups" territory
3. The summary statistics lose the time dimension entirely — if the worst months were last year, that trend is invisible

**Visual:** The press release quote in a callout box styled to look like a government communication. Below it, the three statistics as a small clean table. The three "what it hides" points as a numbered list.

**Speaker notes:**
This is the worked example students read after completing the tutorial. Use it here to show the panel what the pre-work actually looks like — not just that it exists. The AQI domain is neutral, distinct from the chapter's Berlin rent example and the tutorial's salary dataset. Students who read the chapter carefully won't have seen this case before, so the cognitive surprise in Part 3 is real.

---

## Slide 4 — The retrieval quiz

**Title:** Nine questions. Two jobs.

**Body:**

| Q1–Q6 | Q7–Q9 |
|-------|-------|
| Retrieval practice | Diagnostic |
| Vocabulary and recall | Application and edge cases |
| Move on if correct | Act on splits — through pair work, not explanation |

One example from each tier:
- Q6: *"A zip code is stored as a number. Is it numerical or categorical?"* — trap question; arithmetic on a zip code is meaningless
- Q9: *"You have monthly crime rates for 50 years. You build a histogram. What's fundamentally wrong?"* — the time dimension is gone

**Visual:** The two-column table above, clean and minimal. Below it, the two example questions as pull quotes.

**Speaker notes:**
The key design point: these two types of question call for different instructor responses. Q1–Q6 splitting the room means the reading didn't land — acknowledge, clarify in 30 seconds, adjust Part 3. Q7–Q9 splitting the room is expected — don't explain the answer, let the pair work surface it. Farmus, Cribbie & Rotondi (2020) found that weekly in-class quizzes significantly moderated the flipped classroom advantage in introductory statistics. The quiz recurs every week across the full 22-week arc.

---

## Slide 5 — Tutorial review and pair work

**Title:** The analyst and the sceptic

**Body:**

**Tutorial review (15 min + buffer):**
- 2–3 volunteers present T1 solutions
- Instructor prompts, doesn't narrate: *"Does anyone want to push back on that?"*

**Pair work (25 min):**
- Each pair assigned a *classmate's* dataset — not their own
- One student: analyst (runs notebook, calls the numbers)
- Other student: sceptic (questions assumptions, pushes back on the claim)
- Roles swap at 12 minutes

**Deliverable — three things only:**
1. Histogram + summary statistics table in Jupyter
2. One plausible claim from the statistics
3. One thing that claim hides

**Visual:** A simple two-row layout — Tutorial Review on top, Pair Work below, with the three deliverables as a numbered list in a highlight box on the right.

**Speaker notes:**
The role structure is the key design decision for a Year 3 cohort. Two years of shared history means pair work can collapse into agreement — one person analyses, the other nods. Making the sceptic role explicit and requiring it to produce a counter-argument makes the interaction non-optional. The deliverable constraint (three outputs, no more) is from Lovett & Greenhouse (2000) on mental overload — tight scope preserves cognitive capacity for the interpretation work.

---

## Slide 6 — Peer discussion

**Title:** The dataset owner responds

**Body:**
- Each pair presents in ~2.5 minutes: context, claim, what it hides
- The student who *submitted* the dataset responds: did you expect this? Does the critique match what you know?
- With 40+ nationalities in the cohort, the knowledge gap is real — not manufactured

**Visual:** A simple diagram showing the asymmetry: "Analyst pair" (statistical framing) ↔ "Dataset owner" (contextual knowledge). Or just a quote from the session framing: *"Neither is complete alone. The discussion is where they integrate."*

**Speaker notes:**
This is the highest-value exchange in the session. Vygotsky's zone of proximal development: students working at the edge of their competence, supported by peers who hold complementary knowledge. The cross-national dataset constraint is what makes this work — even a cohort that knows each other well won't share the same contextual knowledge about a dataset from a country none of them is from.

---

## Slide 7 — The debrief

**Title:** Did you actually change your mind?

**Body:**

One sentence from each pair:
> *"What did we learn about how to describe a dataset — and what are the limits of that description?"*

Synthesis: descriptive statistics compress information. Compression is useful. Compression hides things. A good analyst knows both.

Then one harder question for a Year 3 cohort:
> *"Did you actually change your mind today, or did you just confirm what you already thought?"*

Leave with one unanswered question:
> *"What if your variable has a time dimension? If I gave you 65 years of monthly crime rates — would mean, median, and SD be meaningful?"*

**Visual:** The three questions stacked, each in its own typographic treatment. The last question slightly larger or bolded — it's the hook that connects back to Slide 1.

**Speaker notes:**
The "did you change your mind" question is calibrated for Berlin/Year 3 specifically. A Lisbon/Year 1 cohort needs scaffolding around giving and receiving feedback — they're still building trust norms. A Year 3 cohort has two years of shared history; the risk isn't insufficient trust, it's a cohort so fluent in each other that they stop updating. One question, handled briefly, is enough. Then close the loop: the time-series question is the answer to the question on Slide 1.

---

## Slide 8 — Why this fits Forward College

**Title:** No passive moment in 90 minutes

**Body (four lines, spare):**
- Flipped structure makes Bloom's levels 4–5 possible — you cannot do analysis and evaluation if the seminar is still delivering content
- Cross-national datasets operationalise the 40+ nationality cohort as a teaching resource
- Analyst/sceptic roles make the Year 3 peer interaction non-optional
- One unanswered question per session — not three

*(Optional closing line, can be said rather than shown:)*
"Each of those choices has a reason. That's the only version of this course I know how to teach."

**Visual:** Clean closing slide. Forward College visual identity if available. Otherwise white background, left-aligned text, no clutter.

**Speaker notes:**
Don't read this slide. Deliver the last line directly to the room, not to the screen. The presentation has been showing design choices throughout — this slide names the principle behind all of them. Close before they expect it.

---

## Timing guide

| Slide | Content | Time |
|-------|---------|------|
| 1 | Opening question | 1 min |
| 2 | Design logic | 1.5 min |
| 3 | Worked example | 2 min |
| 4 | Retrieval quiz | 2 min |
| 5 | Tutorial review + pair work | 2 min |
| 6 | Peer discussion | 1.5 min |
| 7 | Debrief | 1.5 min |
| 8 | Why Forward College | 1 min |
| **Total** | | **~12.5 min** |

---

## Design notes

- **Font:** one typeface, two weights. Headers bold, body regular.
- **Colour:** minimal — one accent colour for the quote boxes and the table header. Everything else black on white (or white on dark for Slide 1).
- **Quotes:** always in a distinct visual treatment — box, italics, or colour — so the panel can see what's student-facing language vs. instructor description.
- **No bullet soup:** maximum three points per slide. Where there are more, use a table or a two-column layout.
- **Slide 1 and Slide 7 are the bookends** — they share the same question. Make that visual echo obvious if possible (same typographic treatment for the crime rates question on both slides).
