# Trace: 2026-05-09_forward-college_lecturer-business-analytics-statistics

## JD text (fed to classifier, Layer B stripped)

```
# Lecturer in Business Analytics and Statistics (Part-Time) — Forward College

**URL:** https://www.linkedin.com/jobs/view/4410103338/
**Location:** Berlin, Germany (Forward College Campus Berlin, Lohmühlenstraße 65, 12435 Berlin)
**Salary:** EUR 6.5 – 7.5k depending on experience
**Employment Type:** Part-time
**Start Date:** September 1, 2026 – April 30, 2027
**Application Deadline:** May 30, 2026

---

## Key Responsibilities

- Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material
- Design and grade four formative assessments
- Organise and provide 2 series of one-on-one tutoring sessions to students
- Teach 22 two-hour weekly seminars
- Provide approximately 15 hours of individual tutoring across the academic term

---

## Required Qualifications

- Experience in teaching Business Analytics and Statistics
- Demonstrated expertise in the subject matter
- Excellent level of English
- Legal right to work in Berlin/Europe (no visa sponsorship available)

---

## Preferred / Bonus Skills

- Passion for teaching and engaging students
- Curiosity about innovative pedagogical methods (including flipped classroom approach)
- Excellent interpersonal skills
- Ability to interact well with the international student body and staff

---

## Benefits

- Forward College values diversity and will prefer candidates from underrepresented groups when qualifications are equivalent

---

## Forward College Pedagogy — Key Details

**Class size:** ~15 students per seminar (part of a 150-student cohort)

**Flipped classroom in practice:**
- Students study independently 4–8 hours BEFORE each seminar (readings, videos, individual/team assignment)
- Students form study groups (2–4 students) to share difficulties and prepare a question list for the Fellow
- Seminars are NOT for content delivery — they are for tackling complex questions, debating, solving problems in teams, simulating real-life scenarios
- Students are expected to escalate the most challenging aspects of the material to the Fellow before the seminar so the Fellow can maximise class impact

**One-on-one tutorials (Oxbridge-inspired):**
- Weekly in Year 1 — Fellows review student performance on the most recent formative assessment
- Students are progressively expected to come with their own analysis of their performance (self-evaluation)
- Year 2–3: may shift to 2 students + Fellow to foster peer emulation

**Weekly formative assessments:**
- Each week: academic assessment task in exam conditions, 60–90 minutes
- Individual feedback delivered in the follow-up tutorial

**Tutored revisions:** Group sessions helping students prepare before the weekly assessment — cover methodological techniques and the most challenging course content

**Study groups:** Students regroup (2–4) to share learning before each seminar; mutual aid + completing the Fellow's pre-seminar assignment

**Personal development programme:** Annual 360° coaching sessions (cognitive, social, emotional, practical skills); students receive feedback from Fellows and peers and debrief with a personal coach

**Four intelligences — skill detail:**
- *Cognitive:* Learning agility, global challenges understanding, theoretical understanding, technical application, critical/analytical thinking, creativity, inquiry and research, written communication
- *Social:* Effective communication, connection, collaboration, influence & negotiation, visual communication, motivation and involvement, empathy, exchanging feedback
- *Emotional:* Courage & resilience, stress management & balance, mindfulness
- *Practical:* Digital skills, self-efficacy, entrepreneurship, decision making, adaptability, ethical conduct & integrity, project management, tech savviness, change management

---

## Course Content — ST2187 Business Analytics, Applied Modelling and Prediction (LSE)

**Module level:** 5 | **Credits:** 30 | **Notional study time:** 300 hours

**Summary:** Course extends and reinforces e…[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | low | low | low | moderate | 33% | ✓ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | early | mature | early | 33% | ✓ |
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |
| stakeholder_orientation | internal_data | mixed | internal_data | mixed | 33% | ✗ |
| autonomy_level | execution | execution | mixed | execution | 33% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Seminars are NOT for content delivery — they are for tackling complex questions, debating, solving problems in teams, simulating real-life scenarios"
> Verified: ✓ found in JD
> Reasoning: The JD frames the seminar approach around depth, problem-solving, and learning quality rather than information delivery speed; no velocity signals present.

**Run 2:** `rigour` ✓
> Quote: "Design and grade four formative assessments"
> Verified: ✓ found in JD
> Reasoning: The emphasis on structured assessment design, grading, and individual feedback signals a rigour-oriented approach prioritizing educational quality and accountability over speed.

**Run 3:** `rigour` ✓
> Quote: "Design and grade four formative assessments"
> Verified: ✓ found in JD
> Reasoning: The focus on structured assessments and pedagogical rigor in the assessment design indicates a quality-focused approach.

### domain_risk
**Manual:** `low`

**Run 1:** `low` ✓
> Quote: "Teach 22 two-hour weekly seminars"
> Verified: ✓ found in JD
> Reasoning: This is an educational institution with no financial reporting, regulatory, or compliance framing; consequences of poor teaching are educational, not financial or regulatory.

**Run 2:** `low` ✓
> Quote: "Experience in teaching Business Analytics and Statistics"
> Verified: ✓ found in JD
> Reasoning: The role is educational delivery in an academic setting; errors affect learner outcomes rather than financial reporting, regulatory compliance, or business decisions at scale.

**Run 3:** `moderate` ✗
> Quote: "Course extends and reinforces existing knowledge and introduces applications of modelling in management. Aimed at managers who need to be 'more inquisitive, more precise, more accurate in their statements, more selective in their use of data, more critical of advice given to them.'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role directly impacts manager decision-making through business analytics education, suggesting moderate business consequence without regulatory or compliance risk.

⚠ **LLM inconsistency**: runs gave ['low', 'low', 'moderate']

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "No named organizational teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: References to 'staff' and 'student body' are too generic; no distinct named functions like Finance, Product, or Engineering are listed as collaboration partners.

**Run 2:** `0` ✗
> Quote: "No named professional partner teams identified in JD"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names no specific departments or professional teams (Finance, Product, Engineering, etc.) that the lecturer collaborates with; interactions are confined to students and Forward College staff without department-level specificity.

**Run 3:** `0` ✗
> Quote: "No named partner teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role is a standalone teaching position with no explicit cross-functional team collaborations named in the responsibilities.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `early` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: No mention of data infrastructure, tools, or team structure; the role is purely educational delivery with no signals of organizational data capability.

**Run 2:** `mature` ✗
> Quote: "Class size: ~15 students per seminar (part of a 150-student cohort)"
> Verified: ⚠ NOT found verbatim
> Reasoning: The established curriculum, large-scale cohort, defined pedagogical infrastructure (flipped classroom, formative assessments, tutoring programs), and multiple defined roles indicate a mature educational program operating at institutional scale.

**Run 3:** `early` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: The role is establishing a distinct pedagogical approach rather than operating within an established organizational data function.

⚠ **LLM inconsistency**: runs gave ['early', 'mature', 'early']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic teaching verbs, but the detailed pedagogical approach (flipped classroom, study groups, four intelligences framework) suggests hiring manager input on teaching methodology.

**Run 2:** `hiring_manager` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: The specific pedagogical methodology (flipped classroom), reference to LSE material, exact teaching volumes (22 seminars, 15 hours tutoring, 4 assessments), and detailed institutional pedagogy demonstrate technical knowledge only available to someone deeply familiar with this role.

**Run 3:** `hiring_manager` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material; Teach 22 two-hour weekly seminars; Provide approximately 15 hours of individual tutoring across the academic term"
> Verified: ✓ found in JD
> Reasoning: The responsibilities specify a detailed, non-standard pedagogical approach (flipped classroom, specific time commitments, tutorial structure) that only comes from someone designing this specific educational program.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `mixed` ✗
> Quote: "Aimed at managers who need to be 'more inquisitive, more precise, more accurate in their statements, more selective in their use of data, more critical of advice given to them.'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The course serves managers broadly across multiple domains (commercial, product, finance, operations), not a single stakeholder function.

**Run 2:** `internal_data` ✓
> Quote: "Organise and provide 2 series of one-on-one tutoring sessions to students"
> Verified: ✓ found in JD
> Reasoning: The role exists to develop students as analytics practitioners and data-literate learners, positioning students as the primary stakeholder audience being empowered through analytical education.

**Run 3:** `mixed` ✗
> Quote: "Aimed at managers who need to be 'more inquisitive, more precise, more accurate in their statements, more selective in their use of data, more critical of advice given to them.'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role prepares managers across multiple potential functions to be more data-driven decision-makers, rather than serving a single stakeholder orientation.

⚠ **Disagreement**: manual=`internal_data` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'mixed']

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: The Fellow designs within a defined LSE curriculum and prescribed flipped classroom model; they execute pedagogical direction rather than set strategic course direction.

**Run 2:** `mixed` ✗
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic autonomy in designing assessments and seminar content with execution within a predefined pedagogical framework (LSE material, flipped classroom methodology), neither purely strategic nor purely execution-focused.

**Run 3:** `execution` ✓
> Quote: "Teach 22 two-hour weekly seminars; Provide approximately 15 hours of individual tutoring"
> Verified: ✓ found in JD
> Reasoning: The primary responsibilities are delivery and execution within Forward College's established flipped classroom and tutorial pedagogical structure.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD requires teaching expertise and interpersonal skills but contains no expectation that the candidate use or build AI tools.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, machine learning, or AI-assisted work; the Business Analytics curriculum focuses on statistical modeling, forecasting, and decision-making, not AI/ML competencies.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no expectations for AI tool usage, AI infrastructure building, or AI-related skills from the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Design and grade four formative assessments"
> Verified: ✓ found in JD
> Reasoning: Assessments mentioned are educational assessment of student learning, not data quality frameworks, testing practices, or observability tools.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal in JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD is a teaching role with no mention of data testing frameworks, data quality practices, observability, or CI/CD; formative assessments are educational evaluation tools, not data quality testing.

**Run 3:** `absent` ✗
> Quote: "Teach 22 two-hour weekly seminars; Provide approximately 15 hours of individual tutoring"
> Verified: ✓ found in JD
> Reasoning: Data quality, testing, or observability practices are not mentioned in the role's responsibilities, which focus exclusively on teaching and assessment.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD focuses on positive pedagogical outcomes, student learning development, and engagement; no risk, reliability, or compliance framing appears.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role in terms of what the lecturer will deliver (seminar design, assessment, tutoring) rather than risks to prevent or consequences of failure.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes teaching quality and learning outcomes rather than preventing bad outcomes or managing operational risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
