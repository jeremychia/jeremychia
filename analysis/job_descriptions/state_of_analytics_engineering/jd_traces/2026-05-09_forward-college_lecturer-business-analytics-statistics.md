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
| domain_risk | low | low | low | low | 100% | ✓ |
| collaboration_width | 2 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Design and grade four formative assessments"
> Verified: ✓ found in JD
> Reasoning: The emphasis on grading and assessment demonstrates a rigour-oriented approach prioritizing academic quality and evaluation over pace or iteration.

**Run 2:** `rigour` ✓
> Quote: "Demonstrate wide applicability of mathematical models while identifying their limitations and possible misuse"
> Verified: ✓ found in JD
> Reasoning: The course objectives explicitly emphasize correctness and knowing when not to apply techniques, prioritizing rigor over speed.

**Run 3:** `rigour` ✓
> Quote: "Design and grade four formative assessments"
> Verified: ✓ found in JD
> Reasoning: Assessment quality, grading, and feedback delivery are explicit rigour signals; the JD emphasizes learning outcomes and pedagogical rigor with no velocity language present.

### domain_risk
**Manual:** `low`

**Run 1:** `low` ✓
> Quote: "Teach 22 two-hour weekly seminars"
> Verified: ✓ found in JD
> Reasoning: The definition lists education as explicitly low-risk; data/content errors have pedagogical but not financial, regulatory, or mission-critical consequences.

**Run 2:** `low` ✓
> Quote: "Teach 22 two-hour weekly seminars"
> Verified: ✓ found in JD
> Reasoning: This is an educational role where analytical errors are learning opportunities within a formal assessment structure, not direct business or compliance risks.

**Run 3:** `low` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: Educational roles are explicitly classified as low domain risk in the framework; this role delivers curriculum to students rather than producing data analysis affecting business operations or compliance.

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No named cross-functional teams (Finance, Product, Engineering, Data Platform, etc.) are identified in the JD; all responsibilities are solo teaching and tutoring.

**Run 2:** `0` ✗
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material; Design and grade four formative assessments; Teach 22 two-hour weekly seminars"
> Verified: ⚠ NOT found verbatim
> Reasoning: No distinct named partner teams or organizational functions are explicitly listed as collaboration partners in the responsibilities.

**Run 3:** `0` ✗
> Quote: "N/A"
> Verified: ✓ found in JD
> Reasoning: The JD does not explicitly name any collaborative partner teams or functions (Finance, Product, Engineering, etc.); references to 'staff' and 'peers' are generic without identifying specific departments or named teams.

⚠ **Disagreement**: manual=`2` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: The program is built on established curriculum and methodology (not greenfield) with multiple pedagogical components, suggesting an established but moderately-scaled teaching infrastructure.

**Run 2:** `mid` ✗
> Quote: "Class size: ~15 students per seminar (part of a 150-student cohort)"
> Verified: ⚠ NOT found verbatim
> Reasoning: The established program structure with 150 students, formalized curriculum, and structured pedagogy indicate a mid-stage educational program with clear organization.

**Run 3:** `mid` ✗
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: Pre-existing LSE curriculum and multiple implied educator roles (Fellows, coaches) indicate an established program with existing structure and multiple roles, fitting the 'mid' maturity stage.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs (Design, deliver) but pair them with specific pedagogical methodology (flipped classroom) and curriculum context that reveal hiring-manager familiarity with the role.

**Run 2:** `hiring_manager` ✓
> Quote: "Design and deliver seminars adopting the flipped classroom approach based on London School of Economics material"
> Verified: ✓ found in JD
> Reasoning: The specific mention of flipped classroom pedagogy with LSE curriculum context and detailed pedagogical methodology throughout indicates role design by someone with teaching experience.

**Run 3:** `hiring_manager` ✓
> Quote: "Teach 22 two-hour weekly seminars"
> Verified: ✓ found in JD
> Reasoning: The specific numerical details (22 seminars, 2-hour duration, approximately 15 hours tutoring) and elaborate pedagogy section demonstrate detailed program knowledge only available from someone who has designed or manages this program.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']
