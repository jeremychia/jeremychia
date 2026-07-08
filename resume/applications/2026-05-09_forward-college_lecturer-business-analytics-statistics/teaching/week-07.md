# Flipped Classroom Lesson Plan
## ST2187 Business Analytics — Week 7: Tableau — Orientation and Dashboard Design
**Format:** 90-minute in-person seminar, 12–15 students

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Connect** a CSV or Excel data source to Tableau and correctly classify fields as dimensions or measures, understanding the analytical consequences of each classification (Bloom's: Understand / Apply).
2. **Construct** a three-chart Tableau dashboard using bar chart, line chart, and scatter plot, applying preattentive attributes (colour, position, size) and the Tufte data-ink ratio principle to minimise chart junk (Bloom's: Apply / Create).
3. **Evaluate** a peer's dashboard by identifying the implicit argument it makes, what it reveals, and what it conceals — using a structured critique protocol (Bloom's: Evaluate).
4. **Justify** chart-type selection for a given analytical question, distinguishing when to use comparison, trend, relationship, and geographic charts (Bloom's: Analyse / Evaluate).

---

## Before Class (Student Pre-Work)

**Environment check / install:**

Students must install Tableau Desktop (14-day free trial) or Tableau Public (free, permanent, but saves are public). Forward College should request Tableau for Teaching licences — the instructor should follow up with IT before Week 5.

- Tableau Desktop: https://www.tableau.com/products/trial
- Tableau Public: https://public.tableau.com/en-us/s/download

Minimum: Tableau version 2022.x or later. Students on Linux: Tableau does not run on Linux natively; use a Windows virtual machine or pair with another student.

**Reading:**

- Albright & Winston, Chapter 3, §3-4 (pp. 95–108): scatter plots and correlation — the bivariate visual material behind Chart 3. (Tableau's text tables with dimensions on rows are the pivot tables of §3-5, for those who skimmed it in Week 3.)
- Albright & Winston, Chapter 2, §2-4d (pp. 45–54): charts for numerical variables; and §2-5 (pp. 54–61): time series data — the logic behind Chart 2's line chart.
- Albright & Winston, Chapter 17, §17-2b and §17-2d (pp. 901–904 and 911–912): OLAP and visualization software — the textbook's own discussion of dashboard/BI tools of exactly this week's kind.
- Optional but strongly recommended: Knaflic, C. N. (2015), *Storytelling with Data*, Chapter 2: "Choosing an Effective Visual" (PDF excerpt on LMS, 18 pages).

**Pre-work task:**

Download the shared dataset posted to the LMS: `berlin_air_quality_monthly_2022.csv`. This dataset contains monthly average PM2.5, PM10, NO2, and O3 readings across 12 Berlin monitoring stations for calendar year 2022 (sourced from daten.berlin.de).

Open Tableau and complete the following before class:

1. Connect to the CSV file (Data menu → Connect to Data → Text file).
2. Go to a new worksheet. Drag `Month` to Columns and `PM25_avg` to Rows. What type of chart appears?
3. Write one sentence: "The default chart Tableau produced was [X]. I think it chose this because [Y]."

The pre-work is designed to produce a partially wrong or confusing result (Tableau may default to a table or an unexpected aggregation). Bring your confusion to class — it is the starting point for Part 2.

---

## In-Class Session (90 minutes)

### Part 1 — Live Tool Challenge (10 minutes)

**Challenge:** "Open Tableau, connect to the shared CSV, make one bar chart showing average PM2.5 by monitoring station. You have 5 minutes. Go."

The instructor posts the CSV file link to Slack/Teams at the start of class (not before — prevents pre-solving). Students work individually. No guidance is given.

After 5 minutes, the instructor asks three students to project their charts briefly. Common divergences to surface:

- Some students produce a bar chart showing the SUM of PM2.5 rather than the AVG (Tableau's default aggregation is SUM for measures)
- Some students have `Station_name` on the wrong axis — bars run horizontally instead of vertically (or vice versa)
- Some students accidentally produce a text table instead of a bar chart because they dropped the field on the wrong shelf
- Some students get the correct chart but with station names cut off because the axis is too narrow

The instructor writes the divergences on the whiteboard: "SUM vs AVG — we'll fix this. Wrong axis — we'll fix this. Text table — we'll fix this." These become the diagnostic agenda for Part 2.

This challenge reveals the core novice mistake in Tableau: dragging fields without thinking about aggregation. Students who produce AVG immediately are likely to be more fluent with tool logic; those who produce SUM are not wrong to be confused — SUM is the default and it IS displayed, but it is almost never what an analyst means when they visualise air quality.

---

### Part 2 — Live Coding / Instructor Demo (30 minutes)

The instructor builds from scratch in Tableau, projected on screen. Students follow on their own machines. The narrative is: "I'm going to build the same dashboard in front of you, and I'm going to make decisions out loud."

**Step 1: Connecting to data and understanding field types (5 minutes)**

Open Tableau → Connect → Text File → `berlin_air_quality_monthly_2022.csv`.

In the Data Source pane, point out:
- Blue pills = **discrete** fields (create headers); green pills = **continuous** fields (create axes). Dimensions are *usually* discrete and measures *usually* continuous — but the colour encodes discrete vs continuous, not dimension vs measure: Step 3's continuous date is a green *dimension*
- Whether a field is a dimension or a measure is shown by which pane it sits in — and that classification is Tableau's interpretation, not absolute truth: `Month` may be imported as a number (1–12) rather than a date — show how to change it (right-click → Change Data Type → Date)

Key teaching moment: "If Month is a number and I drag it to Columns, Tableau will SUM it. January through December becomes 78. That is technically correct and completely meaningless."

**Step 2: Chart 1 — Bar chart (comparison) (7 minutes)**

```
New worksheet.
Drag: Station_name → Columns
Drag: PM25_avg → Rows
Right-click PM25_avg pill → Measure → Average (change from SUM to AVG)
Sort: Click the sort descending button on the axis
Color: Drag PM25_avg → Color on Marks shelf (this encodes value in both position AND colour)
```

Ask the class: "I just encoded PM2.5 in two places — position (bar height) and colour. Is that redundant? Or does it add information?"

Expected answers will vary. Instructor frames: redundant encoding can help readers who are colour-blind and reinforces the most important variable. But it can also look like you are hiding a less important variable by not giving it colour. Analytical choice, not aesthetic one.

Remove gridlines: Format → Lines → set Grid Lines to None. "This is Tufte's data-ink ratio in practice. Every ink mark should carry information. Gridlines rarely do."

**Step 3: Chart 2 — Line chart (time series) (7 minutes)**

```
New worksheet.
Drag: Month → Columns (ensure it is treated as continuous Date, not integer)
Drag: PM25_avg → Rows (Measure → Average)
Drag: Station_name → Color on Marks shelf
```

This produces a multi-line chart with one line per station. 12 lines, 12 colours.

Ask: "Is this a good chart? What is wrong with it?"

Expected: too many lines, too many colours, impossible to distinguish. The colour channel is overloaded.

Fix option 1: Filter to 3 stations. Drag `Station_name` → Filters shelf → select 3 stations.
Fix option 2: Use a highlight action on the dashboard (preview — we will add this in Step 5).

Key insight: "When you put 12 series on a line chart, you are not communicating 12 pieces of information — you are producing visual noise. The limit of distinguishable colours for most humans is 6–8 (Ware, 2004). Exceeding that is a design failure."

**Step 4: Chart 3 — Scatter plot (relationship) (6 minutes)**

```
New worksheet.
Drag: PM25_avg → Columns (Measure → Average)
Drag: NO2_avg → Rows (Measure → Average)
Drag: Station_name → Detail on Marks shelf (one dot per station — 12 marks)
Drag: Month → Color (watch the mark count jump from 12 to 144: adding a dimension to any Marks slot changes the level of aggregation, not just the styling — each station splits into 12 month-marks, which is what reveals the seasonal pattern)
Add trend line: Analytics pane → Drag Trend Line → Linear
```

Ask: "What relationship does this chart suggest between PM2.5 and NO2? Is that a causal claim?"

Expected: positive correlation visible; causation cannot be inferred from a cross-sectional scatter plot. Both pollutants may respond to a common cause (traffic density, weather).

Note the tooltip: hover over a point — Tableau shows Station name, PM25_avg, NO2_avg. Tooltips are free data-ink. Use them.

**Step 5: Building the dashboard (5 minutes)**

```
New Dashboard → Set size: 1366 × 768 (Desktop standard)
Drag Sheet 1 (bar) → top left quadrant
Drag Sheet 2 (line) → top right quadrant
Drag Sheet 3 (scatter) → bottom
Add Filter Action: Dashboard → Actions → Add Action → Filter
  Source Sheet: bar chart
  Target Sheet: line chart and scatter
  Run action on: Select
```

This creates an interactive filter: clicking a station in the bar chart filters the line and scatter to that station.

"A dashboard is not three charts that happen to be on the same page. It is a system of linked views where the user's question drives the navigation."

---

### Part 3 — Guided Practice (25 minutes)

Students now build their own three-chart dashboard using the same Berlin air quality dataset (or a dataset of their choice from the open data portals). The instructor posts the task list to Slack/Teams.

**Task list:**

```
Task 1. Build the bar chart from the demo in your own Tableau workbook.
        Change: sort by PM10_avg instead of PM25_avg. Does the ranking change?
        Write in a text box on your dashboard: "The station with the highest PM10
        is [X] but with the highest PM25 it is [Y]. This might be because [Z]."

Task 2. Build the line chart. Limit to 4 stations of your choice.
        Add a reference line: Analytics pane → Average Line → Entire Table.
        Which months exceed the annual average?

Task 3. Build the scatter plot. Change: use O3_avg on one axis.
        Add station labels: Marks shelf → Label → Show Mark Labels.
        Is the label clutter better or worse than tooltips only?

Task 4. Assemble the dashboard at 1366x768.
        Add one interactive filter action (your choice of which charts it connects).
        Add a title text box: "Berlin Air Quality 2022 — [Your name]"

Task 5 (stretch). Add a calculated field:
        Calculated Fields → Create → Name: "PM_ratio" → Formula: [PM25_avg]/[PM10_avg]
        Add this ratio as a colour encoding on the bar chart.
        What does a PM_ratio close to 1.0 indicate?

Task 6 (stretch). Duplicate the bar chart. Change the chart type to a packed bubble chart
        (Show Me panel). Is this more or less readable than the bar chart?
        What does it add? What does it lose?
```

**Common errors to watch for (instructor circulates):**

| Error | Cause | Fix |
|---|---|---|
| Bars show SUM not AVG | Default aggregation | Right-click pill → Measure → Average |
| Line chart shows disconnected points | Month is integer not Date | Right-click field → Change Data Type → Date |
| Dashboard charts are the wrong size | Fixed size not set | Dashboard → Size → Fixed Size → 1366x768 |
| Filter action filters the wrong direction | Source/Target swapped | Dashboard → Actions → Edit → swap Source and Target |
| Calculated field returns null | Division by zero (PM10 = 0 in some rows) | Wrap formula: IF [PM10_avg] != 0 THEN [PM25_avg]/[PM10_avg] END |
| Scatter plot shows one aggregate point | Station_name not on Detail shelf | Drag Station_name to Detail on Marks shelf |

Students who finish Task 4 before time is called should move to Tasks 5 or 6, or experiment with the Show Me panel to explore chart types they have not used.

---

### Part 4 — Build-and-Critique / Peer Review (15 minutes)

Students pair up (instructor assigns — mix of open-data sources if some students used their own data). Each student shows their dashboard on their screen. The structured critique protocol runs for 5 minutes each direction, then 5 minutes of open discussion.

**Critique questions (same structure as Week 6, adapted for dashboard design):**

1. **What argument is this dashboard making?** (State it in one sentence without the author's help. If you cannot, the dashboard has failed its communication goal.)
2. **What design choice would you challenge?** (Pick one: a chart type, a colour choice, an aggregation, a filter. Say what you would change and why.)
3. **What question does this dashboard NOT answer?** (What would a stakeholder ask after seeing this that cannot be answered from these three charts?)

The instructor listens to two or three pairs. Specific conflicts to surface for the whole group:

- "You used a packed bubble chart for Task 6 — why? The areas are hard to compare accurately. Bar charts are almost always better for comparison."
- "Your bar chart is sorted alphabetically, not by value. That means the reader has to search for patterns instead of reading them. Sorting by value is almost always correct for comparison charts."
- "You used 12 different colours for 12 stations in the line chart. I can't read it. What would you do differently?"

Instructor closes Part 4 with the session's core argument: "Every design choice is an argument. The sort order, the colour scheme, the chart type, the aggregation — each one makes a claim about what matters in your data. If you cannot articulate why you made each choice, you have not yet made an analytical decision. You have accepted a default."

---

### Part 5 — Debrief (10 minutes)

**Closing the tool decision framework:**

Return to the whiteboard note from Part 1 (the divergent charts from the tool challenge). Resolve each:

- SUM vs AVG → right-click → Measure → this is the most common Tableau error and the first thing to check on any unfamiliar viz
- Wrong axis → swap Rows and Columns with the swap button (top toolbar)
- Text table → drag the field off the Row/Column shelf and put it on Detail instead

Post a one-slide summary on screen: "When to use which chart type"

| Question type | Chart type | Why |
|---|---|---|
| Comparison across categories | Bar chart (sorted) | Position is the most accurate perceptual channel |
| Change over time | Line chart | Connects sequential values, implies continuity |
| Relationship between two variables | Scatter plot | Simultaneously encodes two numeric variables |
| Part of a whole | Pie chart (≤5 slices) or stacked bar | Use sparingly; angle is a weak perceptual channel |
| Geographic distribution | Map | Only when geography IS the question, not a decoration |

**Bridge question (last 3 minutes):**

"Next week we write SQL queries to pull the data that would feed a dashboard like this. The air quality data we used today was already clean and pre-aggregated. What problems might a SQL analyst encounter before the data is clean enough for Tableau?"

Expected answers: nulls in station readings, date formats inconsistent across months, duplicate rows from data pipeline errors, column names with spaces that break queries. These are precisely the issues Week 8 SQL will address.

---

## After Class (~20 minutes)

**Dashboard completion and export:**

Finalize your three-chart dashboard. Export it as an image (Dashboard → Export → Image) and as a Tableau Packaged Workbook (.twbx) file.

Upload both files to the shared class folder (link on LMS) using the naming convention: `W07_[your_initials]_[dataset_name].twbx` and `W07_[your_initials]_[dataset_name].png`.

Write a short reflection in a Tableau text box (visible on the dashboard itself): "The most important analytical claim this dashboard makes is [X]. The biggest limitation of this dashboard — what it cannot show — is [Y]." This text box is part of the submission, not a separate document.

No LMS reflection post required. The dashboard IS the reflection.

---

## Design Rationale

| Design choice | Pedagogical grounding |
|---|---|
| Live tool challenge produces systematically wrong output (SUM not AVG) | Bjork (1994) desirable difficulties: the default Tableau aggregation error is a productive failure — students who produce SUM and then learn to fix it are more likely to remember the correction than students who are simply told "always check the aggregation." |
| Instructor makes design decisions out loud during demo | Lovett & Greenhouse (2000) cognitive load: narrating the decision process (not just the outcome) reduces the gap between expert tacit knowledge and novice awareness. Students learn that experts do not see "the right chart" immediately — they evaluate options. |
| Pre-work designed to produce confusion (month as integer) | Ausubel (1968) assimilation theory: confusion created by the pre-work activates a question that the in-class instruction answers. Students who arrive with "I tried it and got a weird number" retain the correction more deeply than students who arrive having never tried. |
| Structured three-question critique protocol | Black & Wiliam (1998) formative assessment: the three questions operationalise Bloom's Evaluate level in a peer context. "What argument is this making?" is harder than "Is it good?" and produces more generative feedback. |
| Chart type decision table in debrief | Kalyuga et al. (2003) expertise reversal: for novices, an explicit reference table reduces cognitive load more than asking them to derive the principle. The table is a scaffold, not a shortcut — students are expected to be able to justify selections from it. |
| Bridge question connecting to SQL | Roediger & Karpicke (2006) testing effect: asking students to predict SQL problems from a Tableau context is a form of forward transfer testing — it activates the upcoming week's content before instruction, improving retrieval. |
| Dashboard reflection embedded in the artefact itself | Vygotsky (1978) ZPD: requiring the analytical claim to be stated on the dashboard closes the loop between design and communication — the student cannot separate "making the chart" from "knowing what it argues." |

---

## Timing Summary

| Activity | Time | Notes |
|---|---|---|
| Part 1 — Live Tool Challenge | 10 min | Students connect and build independently; instructor notes divergences on whiteboard for Part 2 |
| Part 2 — Live Demo | 30 min | 5 steps; instructor narrates decisions; students follow in Tableau; questions embedded throughout |
| Part 3 — Guided Practice | 25 min | 6 tasks; instructor circulates; common error table posted; stretch tasks for fast finishers |
| Part 4 — Build-and-Critique | 15 min | 3-question structured peer critique; instructor surfaces 2-3 productive conflicts |
| Part 5 — Debrief | 10 min | Resolve Part 1 divergences; chart type reference table; bridge to SQL in Week 8 |
| **Total** | **90 min** | |

---

## Pedagogical Design Challenges

**1. The drag-and-drop abstraction problem**

Tableau's greatest pedagogical liability is also its greatest strength: it hides the computation. When a student drags a measure to Rows, Tableau automatically aggregates it — but the aggregation function (SUM, AVG, COUNT) is displayed only in the pill label, which novices rarely notice. The result is a chart that looks correct but computes something different from what the analyst intended. This is harder to catch in Tableau than in Python, where the function call is explicit. The instructor must repeatedly ask "what is this number?" and "how was it computed?" — not just "does the chart look right?" The SUM-vs-AVG error in the tool challenge is specifically designed to create this awareness early.

**2. Aesthetic judgement vs. analytical judgement**

Students from design-adjacent backgrounds (marketing, UX, visual arts) frequently produce dashboards that are visually polished but analytically weak — good colours, poor sort order, wrong chart type, no filter logic. Students from quantitative backgrounds frequently produce dashboards that are analytically sound but visually cluttered — correct aggregations, illegible labels, 12-colour line charts. The peer critique protocol is designed to surface both failure modes, but the instructor must be prepared to validate quantitative rigour over aesthetic finish explicitly. The rubric for Block 2 assessment should weight "correctness of analytical claim" above "visual design quality."

**3. Interactivity as analysis vs. interactivity as performance**

Tableau's filter actions and dashboard interactions can create the impression of analytical depth without requiring analytical thought. A dashboard that lets you filter by station and month feels sophisticated, but if the user cannot state what question those interactions are answering, the interactivity is decorative. The three-question critique protocol forces students to articulate the dashboard's argument before evaluating its design, which prevents interactivity from substituting for analysis. The instructor should flag this explicitly during Part 4: "A dashboard that lets you explore everything is not the same as a dashboard that answers a specific question well."

**4. The Tableau Public saving problem**

Students using the free Tableau Public version cannot save locally — their workbooks are published to the public internet. This raises a data governance issue if students use datasets containing personal or sensitive information, and a practical issue if the class VPN or network restricts access to Tableau's servers. The instructor should confirm before class that Tableau Public saving is accessible from the campus network, and brief students that anything saved to Tableau Public is publicly viewable. Students who have loaded personal data (e.g., their own financial data for an earlier exercise) should not use it in Tableau Public. The Berlin air quality dataset is fully public and safe.

---

## References

Albright, S. C., & Winston, W. L. (2019). *Business analytics: Data analysis and decision making* (6th ed.). Cengage Learning.

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's educational objectives*. Longman.

Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart and Winston.

Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. https://doi.org/10.1080/0969595980050102

Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. https://doi.org/10.1207/S15326985EP3801_4

Knaflic, C. N. (2015). *Storytelling with data: A data visualization guide for business professionals*. Wiley.

Lovett, M. C., & Greenhouse, J. B. (2000). Applying cognitive theory to statistics instruction. *The American Statistician, 54*(3), 196–206. https://doi.org/10.1080/00031305.2000.10474545

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x

Tufte, E. R. (2001). *The visual display of quantitative information* (2nd ed.). Graphics Press.

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

Ware, C. (2004). *Information visualization: Perception for design* (2nd ed.). Morgan Kaufmann.

---

# Supplement (2026-07-06): Textbook Cross-Reference, Extended Exercises, Alternative Activities, Critique

## 1. Textbook Cross-Reference — Albright & Winston, 6th ed.

**Both assigned references are wrong, and the chapter that actually covers this week's topic is unused.**

- "Chapter 3 pp. 75–95" — Chapter 3 begins at p. 79, and scatterplots/correlation sit at **pp. 95–108 (3-4)**. As cited, students would read the crosstab material they already covered in Week 3 and stop just before the scatterplot section this session uses.
- "Chapter 2 pp. 58–68: 'Data Exploration'" — no section of that name exists in Chapter 2. The visualisation material is **2-4d Charts for Numerical Variables (pp. 45–54)** and **2-5 Time Series Data (pp. 54–61)**, which covers the line-chart-for-time-series logic of Chart 2.
- **The real textbook anchor for this week is Chapter 17, §17-2 "Data Exploration and Visualization" (pp. 900–912)** — including 17-2b OLAP (the slice/filter mental model behind dashboard actions) and **17-2d Visualization Software (p. 911), where A&W explicitly discuss Tableau-class tools.** Assign 17-2b + 17-2d (~6 pages): it gives the session textbook legitimacy and pre-loads vocabulary (drill-down, slicing) that Week 8's SQL GROUP BY will formalise.
- **Close the Week 3 promissory note.** Week 3 deferred A&W §3-5 (Pivot Tables, pp. 108–131) "to Block 2 (Tableau and Excel practical sessions)". This is that week — yet pivot tables never appear. One sentence in Part 2 ("what Tableau calls a text table with dimensions on rows *is* the pivot table from §3-5") plus an optional skim reference discharges the promise; otherwise the deferral was a quiet drop.

## 2. Extended Exercise Bank (with answers)

**E1 — When is SUM actually right?** For each, say whether the default SUM aggregation is correct or a bug: (i) monthly PM2.5 readings by station; (ii) transaction revenue by store; (iii) satisfaction scores (1–5) by branch; (iv) population by district on a choropleth.
**Answer:** (i) bug — averaging (or a proper time-weighted mean) is meant; summing monthly averages is meaningless. (ii) correct — revenue is additive. (iii) bug — scores aren't additive; AVG (with caveats about ordinal data, per Week 3's Q11). (iv) correct — population is additive over districts. The rule: *SUM is right only when the quantity is additive over the dimension shown.*

**E2 — Blue vs green pills.** True or false: "Blue pills are dimensions, green pills are measures."
**Answer:** **False — and the demo's own Step 3 proves it.** Blue = **discrete** (creates headers), green = **continuous** (creates axes). Dimensions are *usually* discrete and measures *usually* continuous, but Month treated as a continuous date is a **green dimension** (that's exactly what Step 3 requires for an unbroken line), and a binned/discrete measure shows blue. Teaching pill colour as dimension/measure creates a misconception that breaks the first time a student needs a continuous date axis. (See critique point 1.)

**E3 — Chart selection drill.** Choose a chart type and defend it in one sentence: (i) market share of 4 competitors today; (ii) market share of 4 competitors over 10 years; (iii) delivery time vs distance for 300 orders; (iv) sales by 16 German states; (v) survey responses on a 5-point scale across 3 cohorts.
**Answer:** (i) sorted bar (or pie at only 4 slices — defensible, weak angle encoding); (ii) line chart, one line per competitor — trend question; (iii) scatter plot — relationship between two numerics; (iv) map only if geography is the question, otherwise sorted bar — "geographic data" ≠ "geographic question"; (v) stacked or grouped bar (diverging stacked bar for Likert if taught) — distribution comparison across groups.

**E4 — Aggregation granularity.** A scatter has AVG(PM25) vs AVG(NO2) and nothing on Detail. How many marks appear? What changes when Station goes on Detail? When Month is *also* added to Colour?
**Answer:** One mark (grand averages); 12 marks (one per station); **144 marks** (station × month) — adding any dimension to any Marks card slot changes the level of aggregation, not just the styling. This is the invisible-computation trap of Design Challenge 1 in concrete form.

**E5 — Calculated field.** `PM_ratio = [PM25_avg]/[PM10_avg]`. What range must this ratio physically lie in, and what does a value near 1.0 vs near 0.3 indicate?
**Answer:** PM2.5 is a subset of PM10, so 0 < ratio ≤ 1 (a value > 1 signals a data error — worth telling students to *check for*). Near 1.0: particulate load dominated by fine combustion particles (traffic, heating); near 0.3: coarse particles dominate (dust, construction). A domain-meaningful derived metric — and a built-in data-quality assertion.

**E6 — Data-ink audit.** List four default chart elements that usually fail Tufte's data-ink test, and one case where gridlines earn their ink.
**Answer:** Gridlines, chart borders, redundant axis titles ("PM25_avg" when the chart title says it), legend boxes duplicating direct labels. Gridlines earn their keep when readers must *read values off* the chart (reference use) rather than compare shapes (analytic use) — the test is the reader's task, not aesthetics.

## 3. Alternative In-Class Activities (additional options)

**A. Same data, opposite stories (25 min, Part 3 alternative).** Half the room builds a dashboard arguing "Berlin's air quality is a serious problem"; the other half argues "Berlin's air is fine and improving" — same CSV, no fabrication allowed. Gallery review: identify each dashboard's rhetorical moves (axis ranges, station selection, month windows, colour temperature). The "every design choice is an argument" thesis, experienced from the inside. Pairs naturally with the post-work limitation statement.

**B. Cleveland–McGill mini-replication (10 min, opener).** Show the same four values encoded as bar lengths, pie angles, bubble areas, and colour intensities; students estimate the ratio between two marked values in each; collect estimates via Mentimeter and plot error by encoding. The class *generates* the perceptual-channel ranking the debrief table asserts. Ten minutes, and the chart-type table stops being folklore.

**C. Redesign a real dashboard (15 min, Part 4 alternative).** Project a screenshot of a genuinely cluttered public dashboard (many government COVID or air-quality dashboards qualify). Pairs list three specific changes with justifications tied to today's vocabulary (aggregation, channel overload, sort order). Critique skills sharpen faster on strangers' work than on classmates' — no politeness tax.

**D. Dashboard speed-dating (15 min, Part 4 alternative).** Dashboards open on every screen; students rotate seats every 3 minutes and leave a sticky note answering critique question 1 only ("the argument this makes is ___"). Authors return to 4–5 independent readings of their dashboard — the fastest possible test of whether the intended argument survives contact with readers.

**E. Show Me forensics (10 min, stretch replacement for Task 6).** Students pick any Show Me chart type they've never used, build it, then answer: what did Tableau put on which shelf, and what level of aggregation resulted? Reverse-engineering Show Me converts the "magic button" into an inspection exercise — the drag-and-drop abstraction problem (Design Challenge 1) turned into practice.

## 4. Critique of the Lesson Plan

**What works (keep):** the SUM-vs-AVG productive failure in Part 1 (the single most important Tableau lesson, correctly placed first); decisions narrated aloud in the demo; the argument-first critique protocol; the reflection embedded in the artefact; the honest Tableau Public data-governance note.

**Problems, reasons, and fixes:**

1. **The blue/green pill explanation is factually wrong.** Blue/green encodes **discrete vs continuous**, not dimension vs measure — and Step 3's own instruction ("ensure Month is treated as continuous Date") produces a green *dimension*, contradicting the rule taught 15 minutes earlier. *Reason it matters:* this is the misconception most Tableau-experienced interviewers and students will catch, and the wrong rule fails precisely at the week's central demo moment. *Fix:* teach "blue = discrete (headers), green = continuous (axis); dimension/measure is a separate property shown by which pane the field lives in."
2. **Both reading references are broken and the right chapter is missing (see §1).** Fix pages; add 17-2b/17-2d; close the §3-5 pivot-table promise from Week 3.
3. **Step 4 contradicts itself on granularity.** "Drag Station_name → Detail (one dot per station)" followed by "Drag Month → Color (to show seasonal pattern)" yields **144 marks**, not 12 — adding a dimension to Colour changes the aggregation level. As written, the instructor will narrate "one dot per station" while the screen shows twelve dots per station. *Fix:* either present the 12-dot version (drop Month) and add Month-colour as a deliberate "watch the granularity change" moment, or fix the narration. Done intentionally, it's the perfect demonstration of E4/Design Challenge 1.
4. **The 14-day trial creates a timing bomb.** Installed at Week 6–7 as instructed, Tableau Desktop trials expire around Week 9 — before the full-analysis weeks (19–22) where students may want dashboards for their final presentations. *Fix:* confirm Tableau for Teaching licences (1-year) before the course starts, not "before Week 5"; make Tableau Public the explicit default otherwise, with the governance caveat already noted.
5. **Design Challenge 2 references a "rubric for Block 2 assessment" that doesn't exist anywhere in the materials.** Same gap as Week 6's notebook (see that supplement, point 3). *Fix:* one shared Block 2 rubric covering both artefacts (notebook, dashboard): analytical correctness of the claim > justification of design choices > reproducibility/labelling > visual polish, in that order — publishing the weighting is itself the pedagogy.
6. **No categorical-encoding guidance despite a 12-category dataset.** The demo diagnoses the 12-line/12-colour failure but the only sanctioned fixes are filtering to 3–4 stations or dashboard actions. Add the third standard fix: grey-out-and-highlight (all stations in light grey, one or two focal stations in colour) — it preserves context without channel overload, is two clicks in Tableau, and is the pattern students will need for their final presentations.
7. **Pre-work asks Forward College to sort licensing "before Week 5" inside a Week 7 document.** Logistics instructions to the institution shouldn't live inside student-facing pre-work; move to an instructor-notes block (several weeks mix audience voices — a full-set editing pass should separate student text from instructor text, the same pass that splits answer keys out).
