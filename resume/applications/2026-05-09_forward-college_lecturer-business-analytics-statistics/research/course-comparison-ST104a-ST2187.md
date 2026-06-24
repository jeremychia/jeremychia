# Course Comparison: ST104a Statistics 1 vs ST2187 Business Analytics

**Purpose:** inform lesson design decisions — particularly where to pitch explanations, what prior knowledge to assume, and which topics need the most scaffolding.

---

## Overview

| | ST104a Statistics 1 | ST2187 Business Analytics |
|---|---|---|
| Level | 4 (introductory) | 5 (intermediate) |
| Credits | 15 | 30 |
| Study hours | 150 | 300 |
| Assessment | Written exam 80% + MCQ 20% | Case study 30% + written exam 70% |
| Audience | Students beginning a quantitative degree | Business/management students needing to *use* models |

---

## Syllabus comparison

### Topics in both courses

These are the statistical foundations ST2187 assumes — students who took ST104a will have seen them; others may not have:

- Data visualisation and descriptive statistics
- Probability and probability distributions
- Sampling and sampling distributions
- Confidence interval estimation
- Hypothesis testing
- Correlation and simple linear regression

### ST104a only (foundations not covered in ST2187)

These are things students may or may not know coming into ST2187, depending on their prior courses:

- Mathematics primer (summation notation, role of statistics in research)
- Contingency tables and chi-squared test
- Experimental design and survey design
- Probability theory from first principles (Venn diagrams, conditional probability, tree diagrams)

### ST2187 only (where it goes beyond ST104a)

These are the topics that make ST2187 distinct — they build on statistical foundations but extend into applied modelling:

- Decision-making under uncertainty and modelling (Week 1)
- Decision trees (Week 7)
- Regression statistical inference — beyond estimation into significance testing of coefficients (Week 12)
- Time series analysis and forecasting (Week 13)
- Optimisation models (Week 14)
- Monte Carlo simulation (Week 15)
- Tableau (Week 4 in official syllabus; moved to Block 2 Week 7 in this arc)

---

## Key differences in framing

**ST104a** is a statistics course. Its aim is literacy: students should be able to interpret tables, apply standard methods, and understand the logic of statistical inference. It is explicitly "at an elementary mathematical level." The methods are introduced for their own sake.

**ST2187** is a decision-making course that uses statistics as a toolkit. The module summary is explicit: the goal is managers who are "more inquisitive, more precise, more accurate, more selective in their use of data, more critical of advice given to them." Methods are introduced in service of a decision. Every topic has a business framing.

This distinction matters for lesson design:

- In ST104a, a question like "what is the standard deviation?" is a valid end-point.
- In ST2187, "what is the standard deviation?" is a starting point. The follow-up is always: "and what decision does knowing this enable, and what does it still not tell you?"

---

## Implications for lesson design

### 1. Do not assume statistical vocabulary

The ST2187 cohort at Forward College will have heterogeneous prior statistics exposure. Not all students will have taken ST104a or equivalent. The Mentimeter retrieval check in Weeks 1–5 should include vocabulary questions (Q1–Q6) precisely because this cannot be assumed.

### 2. Overlap topics are revision, not new material — but they still need the business framing

Weeks 2–3 (descriptive statistics, relationships between variables) and Weeks 11–13 (sampling, confidence intervals, hypothesis testing) cover territory ST104a students have seen. The risk is that students treat these as recap and disengage from the *new* content — which is the critical interpretation framing, not the mechanics.

Design implication: make explicit that "you may have computed these before; today we are asking what decision they support and what they hide." The claim/critique structure in Week 2 and the structured controversy in Week 13 are the right format for this — they demand something ST104a did not.

### 3. The genuinely new topics need more scaffolding

Decision trees (Week 10), time series (Week 16), optimisation (Week 17), and Monte Carlo (Week 18) are unlikely to appear in any prior statistics course. These weeks should budget more time for orientation and less for critique — the pair work format may need to be more guided than in Weeks 2–3.

### 4. Regression is taught twice, at different depths

ST104a introduces regression as estimation (fitting a line, interpreting slope and intercept). ST2187 Week 11 returns to this but adds statistical inference — testing whether coefficients are significant, interpreting R², identifying assumption violations. Students who took ST104a will need to shift from "this is how you fit a line" to "this is what the line's coefficients are actually claiming, and how confident we should be."

### 5. The chi-squared test and experimental design are in ST104a but not ST2187

If contingency tables or survey design come up in student datasets or case studies, the instructor cannot assume prior knowledge. These topics are not assessed in ST2187 but may surface in the practical analysis weeks (19–22) if a student's dataset contains categorical variables.

---

## What this changes in the current lesson arc

See the main lesson plan files for full detail. Key revisions flagged by this comparison:

1. **Week 2 Mentimeter Q2** (variable types) is well-targeted — nominal vs ordinal vs continuous is taught in ST104a but not always retained.
2. **Week 11 (sampling distributions)** should not assume the Central Limit Theorem has been encountered — ST104a introduces it but at an elementary level. A brief re-derivation via simulation is appropriate.
3. **Week 13 (hypothesis testing)** structured controversy is well-calibrated — the p-value misconception is specifically targeted in both courses but typically not resolved in ST104a.
4. **Weeks 16–18** (time series, optimisation, Monte Carlo) should have the most scaffolded pre-work of any block — these are genuinely new for most students.
