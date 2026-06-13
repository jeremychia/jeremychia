# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 2: Univariate Data Visualisation and Descriptive Statistics
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:
- Compute and interpret descriptive statistics (mean, median, standard deviation, min, max) for a real dataset
- Identify what descriptive statistics reveal — and what they hide
- Critique a claim made from summary statistics, recognising the limitations of single-variable analysis

These map directly to the ST2187 course outcome: *"identifying limitations and possible misuse"* of quantitative models, and the employability skill of being *"more critical of advice given to them."*

These objectives operate at the **analysis and evaluation** levels of Bloom's Taxonomy (Anderson & Krathwohl, 2001) — moving beyond recall of formulas toward critical interpretation of statistical output.

---

## Before Class (Student Pre-Work)

**Reading:** Albright & Winston, *Business Analytics*, Chapter 2 — read the following sections only:
- §2.1 Types of data (pp. 19–27)
- §2.3 Describing numerical variables — central tendency, spread, shape (pp. 35–58)
- §2.4 Charts for numerical variables — histograms and box plots (pp. 58–68)

The time series section (§2.5, pp. 68–75) and missing data section (§2.6) are optional this week. §2.5 is surfaced at the end of the seminar as an unanswered question; you will encounter it properly in Week 13.

*Rationale:* the full chapter is 61 pages. The sections above cover everything needed for Parts 1–4 of this seminar. Reading the full chapter in addition to completing the tutorial problems and worked example below would exceed what is useful preparation time for a 90-minute session (Fischer et al., 2023 — see pedagogical critique).

**Videos (~20 minutes total):**
- [Descriptive Statistics — Simply Explained](https://www.youtube.com/watch?v=FzujIYo9GYo)
- [Descriptive Statistics: Full Tutorial — Mean, Median, Mode, Variance & SD](https://www.youtube.com/watch?v=SplCk-t1BeA)

**Worked example (attempt T1–T3 first, then read this):**

This walks through the reasoning chain you will use in Part 3. Read it *after* you have written your T1–T3 answers — not before. If you read it first, it will not help you; it will help you feel like you understand something you haven't yet had to do.

> **Dataset:** Monthly average air quality index (AQI) for a mid-sized European city, 24 months of data.
> Mean AQI = 48, Median AQI = 41, SD = 22, Min = 18, Max = 147.
>
> **Step 1 — What do the numbers say?**
> The mean (48) is noticeably higher than the median (41). That gap — 7 points — tells us the distribution is right-skewed: a small number of months with very high pollution are pulling the mean up. The median is more representative of a "typical" month.
>
> **Step 2 — Construct a plausible claim.**
> A city government press release states: "Air quality in our city averages 48 AQI — comfortably within the WHO moderate range." This is technically accurate.
>
> **Step 3 — What is the claim hiding?**
> Three things. First, the mean is inflated by outlier months — most months are actually better than 48 (the median is 41). Second, the SD of 22 means a wide spread: applying the empirical rule (even roughly), many months fall between 26 and 70 AQI. A month at 70 is in the "unhealthy for sensitive groups" category — the mean tells you nothing about how often that happens. Third, and most importantly: AQI has a time dimension. The summary statistics compress 24 months into three numbers and lose the sequence entirely. If the worst months were all in the past year, that trend is invisible in the mean.
>
> **What you are looking for in your own dataset:** the gap between what a number says and what a reasonable person could misread from it. The AQI example has three gaps. Your dataset may have one, or two, or a different kind entirely.

*This worked example is marked optional for students who already feel confident after completing T1(a)–(e) and T2. If the tutorial problems felt straightforward, the example will not add much. If they felt difficult, read it carefully — it shows the reasoning behind the kind of question Part 3 asks.* (On the expertise reversal effect in pre-work design, see Kalyuga, Ayres, Chandler & Sweller, 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4).)

**Tutorial problems (submitted before class, reviewed in Part 2):**

These sit between the reading and the seminar. They confirm mechanical competence — the prerequisite for the higher-order work in Parts 3 and 4. Students bring written answers; two or three will present.

The tutorial runs three questions at different levels:

*T1 — Straightforward computation (no ambiguity):*
> The following are weekly salaries (in €) for 10 employees at a small company: 1200, 1400, 1350, 1250, 1300, 1450, 1200, 1380, 4800, 1290.
>
> (a) Calculate the mean and median. Show your working.
> (b) Which is the better summary of "typical" salary here? Explain in one sentence why.
> (c) What is the mode? Is it a useful summary here?
> (d) Calculate Q1, Q3, and the IQR.
> (e) Calculate the standard deviation (you may use Excel). What does it tell you about spread?
> (f) The empirical rule says ~68% of values fall within 1 SD of the mean. Apply this rule to the salary data. Does the interval make sense? Why or why not?
> (g) One employee earning €4,800 is the CEO. A new analyst suggests removing this value to "clean up" the data before reporting. What would you say to them?

Parts (a)–(e) are mechanical — students either know how or they don't, and the in-class review will surface who struggled. Part (f) is where the computation becomes conceptual: the lower bound goes negative, which is impossible for a salary, and the 68% rule clearly doesn't hold. Part (g) is the ethical question. The right answer is not "never remove outliers" — it's "run both analyses and report both, with an explanation of why the CEO's salary was treated separately." Students who write "remove it because it skews the data" haven't read the chapter carefully enough.

*T2 — Interpretation, not just computation:*
> A supermarket chain reports: "The average customer spends €42 per visit." You are given data showing mean = €42, median = €28, SD = €35.
> (a) Sketch what you'd expect the histogram to look like based on these three numbers alone.
> (b) The marketing team wants to use the mean to set a "typical customer" benchmark for a loyalty programme. What's the problem with that?
> (c) What would you report instead, and why?

This one has no single right answer. It requires the student to reason from summary measures to shape, then from shape to a decision. The sketch in (a) is intentional — it forces students to visualise before they compute.

*T3 — Edge case that requires genuine thought:*
> A dataset of monthly temperatures for a city over 30 years has mean = 14°C, SD = 8°C, and skewness ≈ 0.
> (a) A colleague applies the empirical rules and says: "About 95% of months have temperatures between −2°C and 30°C." Is this a reasonable claim? Under what assumption?
> (b) Now suppose instead of monthly temperatures, this dataset contains monthly average *house prices* in the same city over 30 years, with the same mean, SD, and near-zero skewness. Would you trust the empirical rules here? Why or why not?

The point of T3 is that near-zero skewness does not guarantee normality — and for time series data, the mean and SD of the *raw values* may be meaningless regardless of shape (house prices trend; temperatures cycle). Students who grasp this are ready for Part 4. Students who don't will be brought there by the discussion.

**Pre-class submission (on the course portal):**

Students find a dataset with at least one numerical column from an open data source (e.g. [data.gov.sg](https://data.gov.sg), [Berlin Open Data](https://daten.berlin.de), [Paris Data](https://opendata.paris.fr), [dados.gov.pt](https://dados.gov.pt)) and submit answers to three questions:

**Choose a dataset from a country other than your own.** With 40+ nationalities in the cohort, the dataset owner will have contextual knowledge the analyst pair won't — that gap is part of what the in-class discussion is designed to surface.

1. What is this dataset, and what does it measure?
2. Before computing anything — what do you expect the distribution to look like, and why?
3. What result in the data would genuinely surprise you?

The prediction in Q2–Q3 is intentional: it primes students to notice whether their intuition held up during the in-class analysis. This activates prior knowledge and creates a cognitive hook for new information — consistent with Ausubel's (1968) assimilation theory, which holds that learning is most durable when new material is anchored to existing mental structures. The cross-national dataset constraint sharpens the Vygotskian dynamic in Part 4: the knowledge gap between analyst and dataset owner is not just statistical but cultural.

---

## In-Class Session (90 minutes)

### Part 1 — Retrieval Check (10 minutes)

**Mini-quiz via Mentimeter (5 minutes, 9 questions)**

Questions run from straightforward to genuinely difficult. The easy ones confirm vocabulary and build momentum; the hard ones find where understanding stops. Run all six — Mentimeter is fast. The spread of results across the difficulty gradient is more informative than any single question.

**Easy — vocabulary and recall:**

- Q1: What does the median represent?
  *(a) The most frequent value  (b) The arithmetic average  (c) The middle value when sorted  (d) The value one standard deviation from the mean)*

- Q2: A variable records whether a customer owns a home: Yes or No. What type of variable is this?
  *(a) Continuous numerical  (b) Discrete numerical  (c) Ordinal categorical  (d) Nominal categorical)*

- Q3: Which Excel function calculates the average of a range?
  *(a) MEDIAN  (b) AVERAGE  (c) MODE  (d) STDEV)*

- Q4: The values 3, 7, 7, 9, 14 have a mode of:
  *(a) 7  (b) 8  (c) 9  (d) There is no mode)*

- Q5: Which measure of variability is defined as Q3 minus Q1?
  *(a) Range  (b) Standard deviation  (c) Interquartile range  (d) Variance)*

- Q6: A zip code is stored as a number. Is it numerical or categorical?
  *(a) Numerical — it is stored as a number  (b) Categorical — arithmetic on zip codes is meaningless  (c) It depends on the country  (d) It depends on how many digits it has)*

Q6 here is the trap question. The chapter explicitly flags zip codes as one of three examples of numbers that look numerical but are categorical. Students who read carefully will get it; students who skimmed will guess numerical. If the room splits on this, it's a useful 30-second clarification: the test is not "is it stored as a number" but "does arithmetic on it produce a meaningful result."

**Medium — application:**

- Q7: A dataset of salaries has mean = $120,000 and median = $65,000. What does this gap most likely indicate?
  *(a) A data entry error  (b) Right skew — a few very high salaries pulling the mean up  (c) Left skew — a few very low salaries pulling the mean down  (d) The data is normally distributed)*

- Q8: Two manufacturing suppliers both produce parts with a target diameter of 100mm. Supplier A has SD = 1mm; Supplier B has SD = 12mm. Both have the same mean. Which supplier would you choose?
  *(a) Supplier A — lower variability means more consistent quality  (b) Supplier B — higher variability suggests a wider range of capabilities  (c) Neither — mean is all that matters for quality control  (d) It depends on the target, not the SD)*

**Hard — conceptual, requires the chapter's final insight:**

- Q9: You have monthly crime rates for 50 years. You want to understand how crime changed over time. You compute the mean, median, and standard deviation, then create a histogram. What is fundamentally wrong with this approach?
  *(a) Crime data is categorical, not numerical  (b) 50 years is not enough data for summary measures  (c) The histogram and summary measures destroy the time dimension — you lose the sequence entirely  (d) Nothing is wrong — this is a valid approach)*

Q9 is the sharpest question in the set. The answer — that summary measures and histograms lose the time dimension — is counterintuitive for students who've just learned that histograms give "the complete picture." The complete picture of *what* is the lesson. A histogram of monthly crime rates tells you the distribution of values; it tells you nothing about when they occurred or in what order. That distinction is the chapter's final move, and most students miss it.

**Instructor acts on results (5 minutes)**

The quiz is doing two distinct jobs and they call for different responses:

**Q1–Q6 are retrieval practice.** Their purpose is to strengthen retention by forcing recall — not to diagnose gaps. If most students answer correctly, move on immediately. Extended discussion of questions everyone got right wastes the retrieval benefit and signals that the quiz is a teaching moment rather than a practice one. If Q1–Q6 are *failing badly* (more than a third wrong on vocabulary questions), that signals the reading did not happen — acknowledge it, give a 60-second clarification, and adjust Part 3 accordingly (simpler dataset, more scaffolded pair prompt).

**Q7–Q9 are diagnostic.** Splitting the room here is expected and is where the session's value lies. But the right response to a split on Q9 (the time-series question) is *not* a mini-lecture — it is to let Part 3 surface the answer through the pair work, then name it explicitly in the debrief. Students who get there through their own analysis will retain it longer than students who are told the answer.

*This is not a compliance check. It tells us where to spend the next 80 minutes — and how.*

This is formative assessment in action — the quiz result drives real-time instructional adjustment, consistent with Black & Wiliam's (1998) evidence that formative feedback loops are among the highest-leverage interventions in learning. The quiz format (recurring weekly, Mentimeter) is also specifically supported by evidence from introductory statistics courses: Farmus, Cribbie & Rotondi (2020) found that the presence of weekly in-class quizzes significantly moderated the flipped classroom advantage (Hedge's g = 0.43, DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475)). The quiz should run every week of the 22-week arc, not only in theory weeks.

---

### Part 2 — Tutorial Review (15 minutes + 10 minutes buffer)

Two or three volunteers present their solutions to T1 and T2. Others ask questions. T3 is held back — it surfaces naturally in Part 3 if pairs encounter time-structured data, and is used as the bridge forward in Part 5 if it doesn't.

The instructor's role here is to prompt, not narrate: *"Does anyone want to push back on that?"*, *"What would change if the dataset were larger?"*

The 10-minute buffer is explicit and named. It is not filled with additional content. It absorbs: slow starts, extended debate on T1(g) (the outlier ethics question), or re-covering Q1–Q6 if the quiz revealed the reading hadn't landed. If none of these apply, the buffer compresses and Part 3 starts early.

**If the quiz showed Q7–Q9 splitting the room:** spend the buffer there rather than on T1–T3 mechanics. The conceptual questions are where the session's value is.

Students are doing retrieval practice on the mechanics so that the pair-work can focus on interpretation, not computation. Peer presentation activates the **testing effect** (Roediger & Karpicke, 2006): retrieving and articulating learned material strengthens long-term retention more than re-reading or passive review.

---

### Part 3 — Pair Work (25 minutes)

Each pair is assigned a classmate's submitted dataset (not their own).

**Deliverable — three things, no more:**
1. A histogram and a summary statistics table (mean, median, SD, min, max) in Jupyter Notebook
2. One claim someone could plausibly make from these statistics (e.g. a government press release, a company report, a news headline)
3. One thing that claim would be hiding — what does the summary statistic obscure?

**Example to frame the task — but do not use this one:**

The Berlin rent example (mean = €1,200, median = €950, SD = €800) is the closing example in the chapter reading. Students who did the work will recognise it immediately. Using it as the worked example kills the cognitive surprise — the thing you want students to feel when their own dataset produces the same gap. Instead, frame the task directly:

> *"Look at your summary stats. Find the biggest gap between what the numbers say and what someone could reasonably misread from them. That's your claim. Now find what the claim hides."*

If students are stuck, the instructor can offer a prompt from a different domain — not housing:

The goal is not to make a recommendation — the data doesn't support one yet. The goal is to read a claim critically and identify what a single descriptive statistic cannot tell you.

**One additional prompt for pairs:** If you found a value that looked impossible — a number that seemed like an error — what did you do with it? Why? There's no right answer here, but there's a wrong one: deleting it because it made the analysis messier. The chapter's position on this is clear: run the analysis twice, with and without the outlier, and report both. If pairs didn't encounter anything unusual in their data, the instructor can ask the room: did anyone find something strange? Outliers in real data are not an edge case — they are what real data looks like.

The constrained deliverable (three outputs, no more) is deliberate. Lovett & Greenhouse (2000) identify mental overload as a direct inhibitor of learning efficiency; an open-ended task in 25 minutes would produce anxiety, not analysis. Tight scope frees cognitive capacity for the higher-order critique work.

---

### Part 4 — Peer Discussion (20 minutes)

Each pair presents in ~2.5 minutes:
- Their dataset (one sentence of context)
- The claim they constructed
- What that claim hides

The student who *submitted* the dataset then responds: did they expect this? Does the critique match what they know about the context?

This is the highest-value exchange in the session. The dataset owner has real-world context the analyst pair doesn't — that asymmetry is the point.

This structure draws on Vygotsky's (1978) **zone of proximal development**: students are working at the edge of their competence, supported not by the instructor but by peers who hold complementary knowledge. The dataset owner's contextual knowledge and the analyst pair's statistical framing are both incomplete alone — the discussion is where they integrate.

---

### Part 5 — Instructor Debrief (10 minutes)

**Close the loop on this session first:**

*"What did we learn today about how to describe a dataset — and what are the limits of that description?"*

One sentence from each pair. Synthesise into: descriptive statistics compress information. Compression is useful. Compression also hides things. A good analyst knows both.

Then one more question — addressed to the room, not requiring a full answer, just a moment of reflection:

*"Did you actually change your mind today, or did you just confirm what you already thought?"*

This is not statistical. It's about noticing the limits of your own perspective — a harder question for Year 3 than Year 1, precisely because the cohort knows each other well and may have stopped updating on new evidence. One exchange here, handled briefly, signals that the class is paying attention to the whole analyst, not just the output.

This consolidation step is grounded in **constructivist learning theory** (Piaget, 1952; Lawson, 2002): knowledge is not transmitted but built. The instructor's role at this stage is to help students assemble what they discovered into a transferable mental model, not to re-deliver the content. The reflective question connects to Forward College's Year 3 leadership curriculum — specifically the focus on accountability, wise decision-making, and noticing the limits of your own framing. ([forward-college.eu/certificates/personal-development](https://forward-college.eu/certificates/personal-development/))

**Then one question to leave them with — don't answer it today:**

> *"What if your variable has a time dimension? If I gave you 65 years of monthly crime rates and asked you to summarise them — mean, median, SD — would that be meaningful?"*

The answer is no, and it's not obvious why until you think about it. A mean of 60 years of Dow Jones prices tells you nothing useful about where the market is now or where it's going. But the percentage change from month to month — that distribution is stable, interpretable, and follows the empirical rules. This plants the question for Week 13 (time series and forecasting), where it returns properly.

One question. Not three. Working memory is depleted at the end of a 90-minute session — opening multiple threads produces noise, not retention. The time-series question is the sharpest and most counterintuitive; it is the one that will still be turning over in students' heads when they leave.

---

## After Class (Student Post-Work, ~30 minutes)

Students write a short reflection — posted to the LMS (e.g. Moodle or Canvas), formatted as though it were a public social media post — about one dataset from the session:
- What did the statistics show?
- What did they hide?
- What would you need to know before making a decision from this data?

**Format constraint:** write it as if posting to LinkedIn or a data science community — not a formal essay and not a private journal. One to three paragraphs, a headline, something a stranger could engage with. This is deliberate: the discipline of writing for a non-specialist public audience forces clarity of argument, strips jargon, and requires the student to stand behind a claim. It also mirrors the professional communication skill Forward College explicitly targets.

The audience is the cohort, not the internet. Other students are expected to leave at least one comment — a pushback, a follow-up question, or a connection to their own dataset. That's the consolidation mechanism, not the act of writing alone. Forward College frames relationships as "the necessary fuel for deep learning" — a comment that forces you to articulate *why* a colleague's claim is incomplete is more cognitively demanding than writing the original post.

**Trade-off:** public-format writing creates performance pressure that private journalling does not. Some students will optimise for sounding credible rather than being honest about what confused them. The instructor should model this in the debrief — naming something that was genuinely unclear — before the post-class task is set. This signals that intellectual honesty is the norm, not polish.

Optional further reading: [Critical Thinking Tutorial: Statistical Misrepresentation](https://libguides.usask.ca/CriticalThinkingTutorial/HowReasoningFails/StatisticalMisrepresentation)

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Student-chosen datasets from another country | Ausubel (1968): self-relevance anchors learning; cross-national constraint sharpens the cultural knowledge gap exploited in Part 4 |
| Structured prediction in pre-submission | Activates prior knowledge before exposure; prediction errors create memorable cognitive events (Bjork, 1994 — desirable difficulties) |
| Pre-work reading scoped to specific sections, not full chapter | Fischer et al. (2023) recommend capping pre-work at ~1.5× in-class time and using targeted readings over full chapters; DOI: [10.1186/s12909-023-04325-x](https://doi.org/10.1186/s12909-023-04325-x) |
| Worked example added to pre-work, attempted after T1–T3 | Sweller (1994): high element interactivity material (reasoning from statistics to claim to critique) requires a cognitive template for novices; Rosenshine (2012) Principle 4: provide models of expert reasoning; ERIC EJ971753. Marked optional to mitigate expertise reversal (Kalyuga et al., 2003, DOI: [10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)) |
| Quiz runs easy → hard across 9 questions; runs every week | Q1–Q6 are retrieval practice; Q7–Q9 are diagnostic — different instructor responses. Weekly quiz format specifically supported by Farmus, Cribbie & Rotondi (2020): weekly in-class quizzes significantly moderated flipped classroom advantage in introductory statistics (g = 0.43); DOI: [10.1080/10691898.2020.1834475](https://doi.org/10.1080/10691898.2020.1834475) |
| Tutorial T1–T3 scaffold from computation to edge case | T1 (a)–(e) are mechanical filters; T1 (f) turns computation into a conceptual test of the empirical rules; T1 (g) is the outlier ethics question; T2 requires reasoning from statistics to decisions; T3 introduces the limits of empirical rules and the time series problem |
| Quiz acts on results; split on Q7–Q9 resolved through pair work not mini-lecture | Black & Wiliam (1998): formative assessment with feedback loops is among the highest-leverage learning interventions; students who reach the answer through their own analysis retain it longer than students who are told |
| Peer presentation of tutorial solutions | Roediger & Karpicke (2006): testing effect — retrieval strengthens retention more than re-study |
| Pair works on someone else's data | Vygotsky (1978): ZPD — complementary knowledge between pairs produces learning neither could achieve alone; cultural gap deepens the asymmetry |
| Worked example in pre-work uses AQI dataset, distinct from Berlin rent and salary datasets | Berlin rent closes the chapter reading — students who read carefully recognise it; salary is T1. A third distinct domain (AQI) is needed so the cognitive surprise in Part 3 is real |
| Outlier prompt added to pair work | Real data has unusual values; the right response (run analysis twice, report both) is non-obvious and worth surfacing before students develop the habit of deleting inconvenient observations |
| Critique framing, not recommendation | Bloom's Taxonomy levels 4–5 (analysis, evaluation); honest about what the data can support at this stage |
| Constrained deliverable (3 outputs) | Lovett & Greenhouse (2000): mental overload inhibits learning; tight scope preserves cognitive capacity for interpretation |
| Reflective debrief question on instinct and blind spots | Forward College Year 3 leadership curriculum: accountability, wise decision-making, noticing limits of own framing (forward-college.eu/certificates/personal-development) |
| Single bridge-forward question; two threads dropped | Working memory is depleted at end of 90 minutes; one counterintuitive unanswered question plants a more durable hook than three connections made when students are cognitively spent |
| Three-touchpoint structure | Cepeda et al. (2006): spacing effect — distributed practice improves long-term retention over massed practice |
| Reflection posted to LMS, social-media format | Constructivist consolidation (Piaget, 1952); public-format writing forces clarity and commitment to a claim; peer comments replace passive reading with active critique. Trade-off: performance pressure may produce polish over honesty; mitigated by instructor modelling intellectual uncertainty in the debrief |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Mini-quiz + instructor addresses results | 10 min | Act only on contested questions |
| Tutorial review | 15 min | T1–T2 only; T3 held for bridge |
| Buffer (explicit) | 10 min | Absorbs slow starts, extended debate, or re-covering basics if quiz showed gaps |
| Pair work | 25 min | Analyst/sceptic roles; swap at 12 min |
| Peer discussion | 20 min | ~2.5 min per pair; dataset owner responds |
| Instructor debrief | 10 min | Close the loop, bridge forward, leave one unanswered question |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

This section documents live tensions in the lesson design — choices that could have gone differently, and the reasoning behind what was chosen.

---

### 1. Berlin is Year 3. Trust is not an assumption — it's a resource.

This session is in Berlin, which means the cohort has two years of shared history: Lisbon (social intelligence, belonging) and Paris (resilience, adaptation). They have lived together, been assessed together, received 360-degree feedback on each other, and navigated two cities as a unit.

This changes the stakes of Part 4 considerably.

In Year 1 (Lisbon), peer presentation of tutorial work carries real social risk — students don't yet know how their cohort handles disagreement, and the Personal Development Programme is still building the norms for giving and receiving feedback. A facilitator would need to be more scaffolded: structured sentence stems, roles, visible ground rules.

In Year 3 (Berlin), the risk runs the other way. The cohort may be so fluent in their own dynamics — including informal hierarchies, recurring roles, and established opinions about each other's work — that Part 4 becomes a performance of disagreement rather than genuine critique. Students who have heard each other's views for two years may stop updating on new evidence.

**Trade-off:** the depth of cohort trust in Year 3 makes the peer discussion more substantive (less anxiety, more content). It also makes it easier for students to coast on rapport rather than engage with what's actually in the data. The cross-national dataset constraint is the structural counterweight: even a cohort that knows each other well won't all share the same contextual knowledge about a dataset from a country none of them is from. The knowledge asymmetry in Part 4 is real, not manufactured.

**Design implication:** the debrief question — *"Where did your partner notice something you'd missed?"* — should be framed carefully in Year 3. The more honest version: *"Did you actually change your mind today, or did you just confirm what you already thought?"* That's a harder question, and Year 3 students are ready for it.

---

### 2. The flipped classroom assumes the reading was done.

The entire session design rests on students having completed the Albright & Winston chapter and the pre-class videos before arriving. The quiz and the tutorial review are diagnostic — they assume prior exposure. If a significant portion of the class hasn't done the reading, Parts 3 and 4 lose their foundation.

**The standard defence** is that Forward College students are self-selected for preparation — the pre-class submission (dataset + answers) creates an accountability mechanism. Students who haven't submitted have a visible gap before the session begins.

**The challenge:** the pre-submission confirms that students completed the questions, not that they understood the material. A student who copied answers from a classmate passes the filter. A student who genuinely struggled but submitted partial work is harder to identify than one who submitted nothing.

**Alternative: just-in-time teaching (JiTT).** Students submit one question and one confusion point 24 hours before class (not a full tutorial). The instructor reads responses that evening and opens the session by addressing the three most common confusions — naming them, not attributing them. This makes the gap between what students understood and what the session covers explicit at the start.

**Trade-off:** JiTT is lower stakes for students (less pre-work) and gives the instructor richer diagnostic data. But it reduces the volume of retrieval practice before class, which is where T1–T3 do their work. For a statistics module where mechanical fluency is a genuine prerequisite, that's a real cost. The current design accepts higher pre-work burden in exchange for stronger preparation going into the analysis phase.

---

### 3. Pair work produces unequal contribution by design — is that a problem?

Part 3 pairs each student with a classmate's dataset. The goal is interaction — the pair relationship is the learning mechanism, not just a vehicle for getting analysis done. Forward College's cohort model treats peer exchange as "the necessary fuel for deep learning," and pair work here operationalises that: two students with different contextual knowledge, looking at the same data, must negotiate what it means.

In practice: one student will often drive the Jupyter notebook while the other shapes the narrative. This is not always failure — it can be legitimate division of labour. But in a 25-minute window, it can become one student doing analysis while the other nods. When that happens, the interaction — the actual purpose — has collapsed into observation.

**The fix is not to go individual-first.** That would recover technical contribution at the cost of the interaction itself, which is precisely what this design is for.

**The fix is to make the interaction structurally non-optional.** Two levers:

1. *Assign roles explicitly.* One student is the analyst (runs the notebook, calls the numbers). The other is the sceptic (questions every assumption, proposes alternative interpretations, pushes back on the claim). Roles swap at the 12-minute mark. The sceptic role cannot be discharged by nodding — it requires producing a counter-argument. This is also closer to how analytical work functions in professional contexts, where challenge is a job function, not an optional contribution.

2. *The deliverable requires two voices, not one.* The claim and the critique must come from different people — the pair attributes them explicitly in their Part 4 presentation ("I argued X; my partner argued Y"). If the outputs are indistinguishable, the roles weren't being held.

**Trade-off:** assigned roles create artificial structure that some Year 3 students will find patronising — they've spent two years learning to collaborate and may resist being told who speaks when. The instructor should frame it as a professional simulation, not a scaffold: "In a real analysis review, someone is always the challenger. Today that role is explicit." For a cohort in Berlin, that framing lands differently than it would in Lisbon Year 1.

---

### 4. The Mentimeter quiz is formative but not anonymous enough.

In a cohort of 12–15 students, even aggregated Mentimeter results partially reveal individual answers — especially on the trap question (Q6) or the contested conceptual questions (Q9). If 11 students answer correctly and 3 get Q6 wrong, those 3 students know roughly who they are, and so does everyone else.

**Design implication:** the instructor should name the wrong answer as a *plausible reading of the chapter*, not as a mistake. The zip codes question (Q6) is genuinely ambiguous if you haven't read carefully — most real-world data pipelines store zip codes as integers. Validating the wrong reasoning before correcting it reduces the social cost of having been wrong in front of your Year 3 cohort.

**Alternative: no quiz, cold-call Socratic opening.** The instructor opens by presenting one of the tutorial problems and cold-calling a student for an answer. Discussion follows from there. No technology, no aggregation, just a direct question and a conversation.

**Trade-off:** Socratic opening is faster to set up and removes the quiz's pseudo-anonymity problem. But it also concentrates participation risk on whoever gets cold-called, and it provides no diagnostic data about the rest of the room. Mentimeter's aggregate view is more informative precisely because it reveals where *the class* stands, not just one student. The current design accepts the partial de-anonymisation in exchange for room-level diagnostics.

---

### 5. 90 minutes may be the wrong unit.

The session is structured as a single 90-minute block. The timing summary shows five sequential activities with no scheduled breaks. In practice, the transition from Part 2 (tutorial review) to Part 3 (pair work) is the moment most likely to lose pace — students are shifting from listening to doing, and getting Jupyter notebooks open and datasets loaded takes 3–5 minutes that isn't budgeted.

The 25-minute Tutorial Review block contains 10 minutes of intentional buffer. That buffer should be named as such in the instructor's working notes — otherwise the temptation is to fill it with more content, which defeats the purpose.

**Design implication:** the buffer in Part 2 is most usefully spent on Q7–Q9 from the quiz, not on re-covering T1–T3 mechanics. If the quiz revealed that most students are confident on computation but split on the time-series question (Q9), that's where the 10 minutes goes. If students are still shaky on Q1–Q6, the buffer absorbs that — but it signals the pre-work didn't land and Part 3 should be simplified accordingly.

---

---

## Supplementary Practical Session — Descriptive Statistics in Python and SQL
**Format:** 90-minute lab, same cohort, scheduled the week of or immediately after the seminar above
**Prerequisites:** students have completed the seminar; they have Python (Jupyter) and database access set up

The seminar above develops critical interpretation. This session develops mechanical fluency in the tools students will use for the rest of the course. The two sessions are deliberately separate: mixing tool instruction into a seminar built around debate kills both.

---

### Learning Objectives

By the end of this session, students will be able to:
- Compute all descriptive statistics from the seminar (mean, median, SD, quartiles, skewness) in Python using `pandas`
- Produce a histogram and box plot in Python using `matplotlib` or `seaborn`
- Run equivalent queries in SQL using window functions and aggregates
- Identify when Python vs. SQL is the right tool for a given task

---

### Before Class

**Install check (done in advance, not in the lab):** Python 3, Jupyter, `pandas`, `matplotlib`, `seaborn`, and access to a SQL environment (PostgreSQL via pgAdmin, or SQLite via DB Browser — specify based on course setup). Students confirm their environment works by running one cell: `import pandas as pd; print(pd.__version__)`.

**Reading:** none new. The chapter content from the seminar is the conceptual foundation. This session translates it into code.

---

### Session Structure

#### Part 1 — Live Coding: Descriptive Statistics in Python (30 minutes)

Instructor codes from scratch in a shared Jupyter notebook, projected live. Students follow along on their own machines. Pace is set by the slowest student — if three hands go up with the same error, stop and fix it together.

**Dataset:** the same salary dataset from T1 in the seminar pre-work. Students already know the answers — the point is to reproduce them in code, not to discover them.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

salaries = pd.Series([1200, 1400, 1350, 1250, 1300, 1450, 1200, 1380, 4800, 1290])

# Central tendency
print(salaries.mean())
print(salaries.median())
print(salaries.mode())

# Spread
print(salaries.std())
print(salaries.var())
print(salaries.quantile([0.25, 0.75]))
print(salaries.quantile(0.75) - salaries.quantile(0.25))  # IQR

# Shape
print(salaries.skew())
print(salaries.kurt())

# Full summary
print(salaries.describe())
```

**Key teaching moment:** `describe()` gives most of this in one call — but students should know what each line does before they use the shortcut. Run the full version first, then show `describe()` as the production equivalent.

**Histogram:**

```python
salaries.hist(bins=5)
plt.xlabel('Weekly salary (€)')
plt.title('Distribution of salaries')
plt.show()
```

Vary `bins` from 3 to 10. Ask: at what point does the shape become misleading? This is the computational version of the same judgement the seminar asked them to make.

**Box plot:**

```python
sns.boxplot(y=salaries)
plt.title('Salary box plot')
plt.show()
```

Ask: where does the CEO's salary appear? What does that tell you that the histogram doesn't immediately show?

---

#### Part 2 — Live Coding: Equivalent Queries in SQL (25 minutes)

Switch to the SQL environment. Use the same salary data loaded into a table called `employees`.

```sql
-- Central tendency
SELECT
    AVG(salary)    AS mean_salary,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
FROM employees;

-- Spread
SELECT
    STDDEV_SAMP(salary)  AS std_dev,
    VAR_SAMP(salary)     AS variance,
    MAX(salary) - MIN(salary) AS range_salary,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary)
      - PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS iqr
FROM employees;

-- Full profile
SELECT
    COUNT(salary)  AS n,
    MIN(salary)    AS min,
    MAX(salary)    AS max,
    AVG(salary)    AS mean,
    PERCENTILE_CONT(0.5)  WITHIN GROUP (ORDER BY salary) AS median,
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3,
    STDDEV_SAMP(salary)   AS std_dev
FROM employees;
```

**Key teaching moment:** SQL cannot produce a histogram natively — it returns aggregated numbers, not plots. This is the practical version of the conceptual distinction: SQL is for extracting and summarising structured data; Python is for exploration and visualisation. In practice you do both — query in SQL, plot in Python.

**Outlier flagging in SQL:**

```sql
-- Flag values more than 2 SDs from the mean
WITH stats AS (
    SELECT AVG(salary) AS mean, STDDEV_SAMP(salary) AS sd
    FROM employees
)
SELECT
    salary,
    CASE
        WHEN ABS(salary - stats.mean) > 2 * stats.sd THEN 'outlier'
        ELSE 'normal'
    END AS flag
FROM employees, stats;
```

This bridges back to T1(g) from the seminar: the CEO's €4,800 salary is flagged here automatically. Ask: does flagging it mean removing it?

---

#### Part 3 — Independent Practice (25 minutes)

Students work individually on their own submitted dataset from the seminar pre-work — the one they picked from an open data source.

**Task:**
1. Load the dataset into a `pandas` DataFrame
2. Run `describe()` on the numerical column(s)
3. Produce a histogram and a box plot
4. Write two SQL queries: one for central tendency, one for spread
5. In one sentence: does anything look different in code than it did in your pre-seminar written answers?

The last question is the payoff: some students will find discrepancies (rounding, different quartile methods, missing values handled differently). Those discrepancies are worth surfacing — they're not errors to fix, they're reasons to understand what the tool is actually computing.

**Instructor circulates.** Common issues to anticipate:
- `KeyError` from mistyped column names — check `df.columns` first
- `PERCENTILE_CONT` not available in SQLite — use a workaround or switch to PostgreSQL
- Missing values causing unexpected NaN output — introduce `df.dropna()` vs `df.fillna()` briefly if it comes up, don't pre-empt it

---

#### Part 4 — Debrief (10 minutes)

Two students share one thing that surprised them — a discrepancy, an unexpected output, or something they now understand differently.

Instructor closes with the tool decision framework:

> **Use SQL when:** the data is already in a database, you need a single aggregate number, or you're filtering before analysis.
> **Use Python when:** you're exploring, visualising, or the analysis requires more than one step.
> **In practice:** SQL to extract, Python to analyse. They're not alternatives — they're a pipeline.

---

### Timing Summary

| Activity | Time |
|---|---|
| Live coding: Python | 30 min |
| Live coding: SQL | 25 min |
| Independent practice | 25 min |
| Debrief | 10 min |
| **Total** | **90 min** |

---

## Provisional Course Arc — 22 Weeks

**Source:** ST2187 Business Analytics, Applied Modelling and Prediction (University of London, 2025–26). 15 syllabus topics + 7 additional weeks for practical labs, integration, and full analysis.

**Structure:** 5 theory → 4 practical → 6 theory → 7 practical

The outer structure (flipped classroom: pre-work → active seminar → LMS reflection) holds across all 22 weeks. What varies is the *seminar format* — the nature of the active work in the room. Retrieval checks (Mentimeter) run in theory weeks where new concepts need diagnosing; they are replaced by live tool challenges or standing questions in practical weeks. LMS reflection posts run in ~15 of 22 weeks — dropped in lab-heavy sessions where the output *is* the reflection.

---

### Block 1 — Theory: Foundations (Weeks 1–5)

*Syllabus topics covered:* 1, 2, 3, 5, 6
*What this block builds:* the statistical vocabulary and conceptual foundations everything else depends on. Students should leave Block 1 able to describe any dataset, interpret a chart critically, reason about probability, and identify which distribution is appropriate for a given situation.
*Seminar format:* dataset exploration, structured critique, error autopsy.
*Retrieval check:* Mentimeter every week — diagnostic value is highest here because concepts are new and the exam tests them directly.

| Week | Syllabus topic | Seminar format | Core tension to surface |
|------|---------------|----------------|------------------------|
| 1 | Decision-making under uncertainty and modelling | Scenario sorting: students categorise real business decisions by how much uncertainty is involved and what model would help | What does "modelling" actually mean — and what does a model give up in order to be useful? |
| 2 | Univariate data visualisation and descriptive statistics *(this lesson plan)* | Dataset exploration + claim/critique (pair work, analyst/sceptic roles) | What do summary statistics compress — and what do they hide? |
| 3 | Exploring relationships between variables | Spurious correlation gallery — students argue for and against causal claims from scatter plots and correlation coefficients | Correlation is not causation, but what *is* the threshold for suspicion? |
| 4 | Probability and probability distributions | Structured controversy: two defensible positions on the same probability claim (e.g. base rate neglect in medical testing) | What does a probability of 0.05 actually mean — and what doesn't it mean? |
| 5 | Common probability distributions in business applications | Error autopsy: published business decisions that assumed the wrong distribution | When should you trust a distribution assumption — and how do you check it? |

**Note on Week 4 (Tableau) in the syllabus:** the official syllabus lists Tableau as Week 4. In this arc it is moved to Block 2 (Week 7) where it sits alongside the other practical tool sessions. Weeks 1–5 are theory-only to let the statistical concepts land before students are asked to operate software. This is a deliberate departure from the default syllabus sequence.

---

### Block 2 — Practical: Visualisation and Tools (Weeks 6–9)

*Syllabus topics covered:* 4 (Tableau), plus Python and SQL which are not in the official syllabus but are essential for the practical weeks in Block 4.
*What this block builds:* tool fluency. Students should leave Block 2 able to query structured data in SQL, explore and visualise a dataset in Python, and build a multi-chart Tableau dashboard.
*Seminar format:* live coding labs, build-and-critique, dashboard peer review.
*Retrieval check:* replaced by a live tool challenge at the start of each session — "reproduce this output in 5 minutes."

| Week | Topic | Seminar format | Core tension to surface |
|------|-------|---------------|------------------------|
| 6 | Python: descriptive statistics and visualisation *(supplementary session above)* | Live coding from scratch on the Week 2 salary dataset — reproduce what they computed by hand | When does code give a different answer than your manual calculation — and why? |
| 7 | Tableau: orientation and dashboard design | Build a 3-chart dashboard on a shared business dataset; pairs critique each other's chart choices | Every design choice is an argument — what is this dashboard claiming, and what is it hiding? |
| 8 | SQL: querying, filtering, aggregating | Query challenge — reproduce a specified output from a messy raw table with nulls and duplicates | SQL forces you to be explicit about what you're asking; ambiguity in the question becomes an error in the query |
| 9 | SQL + Python pipeline: from query to visualisation | End-to-end lab: query a database in SQL, load into pandas, produce a chart | Where does the pipeline break — and what does that tell you about the data? |

---

### Block 3 — Theory: Inference and Modelling (Weeks 10–15)

*Syllabus topics covered:* 7, 8, 9, 10, 11, 12
*What this block builds:* the conceptual leap from description to inference, and from inference to modelling. Students should leave Block 3 able to construct and interpret a confidence interval, run and critique a hypothesis test, build a regression model, and identify when its assumptions are violated.
*Seminar format:* structured controversy, case study with a decision, error autopsy, prediction games.
*Retrieval check:* returns here — inference concepts are non-obvious, stack on each other, and the exam tests them heavily.

| Week | Syllabus topic | Seminar format | Core tension to surface |
|------|---------------|----------------|------------------------|
| 10 | Decision-making under uncertainty using decision trees | Decision tree construction on a real business case — students build the tree, then challenge each other's probability estimates | The tree is only as good as the numbers you put in it; where do those numbers come from? |
| 11 | Sampling and sampling distributions | Simulation: students draw repeated samples from the same dataset and observe the sampling distribution of the mean | Why does the mean of means behave so much more predictably than the raw data? |
| 12 | Confidence interval estimation | Case study: interpret a real CI from a published study or news report — what can and can't you conclude? | A 95% CI does not mean there is a 95% probability the true value is inside it |
| 13 | Hypothesis testing | Structured controversy: two students argue opposing conclusions from the same p-value on a real dataset | What does p < 0.05 actually license you to claim — and what doesn't it? |
| 14 | Regression analysis — estimating relationships | Prediction game: students estimate the regression line by eye before fitting it, then compare | What does R² actually tell you — and what does a high R² not guarantee? |
| 15 | Regression analysis — statistical inference | Confound hunt: students add variables one at a time and observe coefficient changes | Adding a variable can flip the sign of another coefficient — why, and what does that mean for the model? |

---

### Block 4 — Practical: Programming and Full Analysis (Weeks 16–22)

*Syllabus topics covered:* 13 (time series), 14 (optimisation), 15 (Monte Carlo), plus full integration weeks.
*What this block builds:* the ability to go from raw data to a defensible conclusion, using the right tool for each step. Weeks 16–18 cover the remaining syllabus topics in applied lab format. Weeks 19–22 are full analysis cycles — students own the problem, the tools, and the argument.
*Seminar format:* applied labs for weeks 16–18; full analysis cycle for weeks 19–22.
*No retrieval check:* replaced by a standing opening question — "what did you find that you didn't expect?"

| Week | Topic | Seminar format | Core tension to surface |
|------|-------|---------------|------------------------|
| 16 | Time series analysis and forecasting | Live coding: decompose a real time series (trend, seasonality, noise), build a simple forecast, critique it | A forecast is a claim about the future based on patterns from the past — what has to stay true for it to hold? |
| 17 | Optimisation models | Build-and-break: students construct a linear programme for a simple resource allocation problem, then their partner finds an assumption that breaks it | Every optimisation model has a feasibility assumption — what happens when it's violated? |
| 18 | Monte Carlo simulation models | Live coding: simulate a simple business risk model; vary the input distributions and observe output sensitivity | The output distribution is only as good as the input distributions you chose — where did those come from? |
| 19 | Full analysis 1 — describe and question | Groups choose a real dataset and present: what it contains, what it shows, and one question the description alone cannot answer | A description is not a conclusion — what would you need to make a defensible claim? |
| 20 | Full analysis 2 — model and infer | Same groups return with a model or hypothesis test applied to their Week 19 question | What assumption did you have to make — and is it defensible given this data? |
| 21 | Full analysis 3 — challenge and revise | Other groups challenge the analysis; presenting group defends or revises their claim in real time | The analyst's job is not to be right — it's to know what would make them wrong |
| 22 | Full analysis 4 — final presentation | Formal 10-minute presentation + Q&A from the room and instructor | What would you do differently with more time, more data, or a different model? |

---

### Instructional Format Summary

| Format | Weeks | Why this content demands this format |
|--------|-------|--------------------------------------|
| Scenario sorting / classification | 1 | Decision-making is intuitive before it's formal — surface the intuition first |
| Dataset exploration + claim/critique | 2, 3 | Descriptive concepts need concrete data to become real |
| Structured controversy | 4, 13 | Probability and hypothesis testing have genuinely contested interpretations that debate surfaces better than explanation |
| Error autopsy | 5, 10 | Distribution assumptions and decision trees fail in characteristic ways — studying failure is more memorable than studying correct examples |
| Live coding lab | 6, 9, 16–18 | Tool fluency requires doing; watching a demo is not the same skill |
| Build-and-critique | 7–8, 17 | Design and modelling choices are arguments; peer critique surfaces assumptions the builder couldn't see |
| Simulation | 11, 18 | Sampling distributions and Monte Carlo are both counterintuitive until you see them run — explanation alone doesn't land |
| Case study with a decision | 12, 14–15 | Inference only matters when something is at stake; abstract problems produce abstract reasoning |
| Full analysis cycle | 19–22 | Integration: students own the whole pipeline from question to conclusion |

**LMS reflection posts:** Weeks 1–5, 10–15 (11 of 22). Dropped in Block 2 (tool labs — the output is the reflection) and Block 4 Weeks 16–18 (same reason). Weeks 19–22 replace the post with a group log entry: one paragraph on what changed between sessions and why.

---

## References
- Ausubel, D.P. (1968). *Educational Psychology: A Cognitive View.* Holt, Rinehart & Winston.
- Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education*, 5(1), 7–74.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
- Chi, M.T.H., de Leeuw, N., Chiu, M.H. & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439–477.
- Lawson, A.E. (2002). Using the learning cycle to teach biology concepts and reasoning patterns. *Journal of Biological Education*, 35(4).
- Lovett, M. & Greenhouse, J. (2000). Applying cognitive theory to statistics instruction. *The American Statistician*, 54(3), 196–206.
- Piaget, J. (1952). *The Origins of Intelligence in Children.* International Universities Press.
- Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press.
