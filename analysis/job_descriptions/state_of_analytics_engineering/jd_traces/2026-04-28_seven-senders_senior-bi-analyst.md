# Trace: 2026-04-28_seven-senders_senior-bi-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Senior Business Intelligence Analyst (f/m/x) — Seven Senders

**URL:** https://www.linkedin.com/jobs/view/4406635718
**Location:** Berlin, Berlin, Germany
**Employment Type:** Full-time

---

## Key Responsibilities

- Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks
- Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets
- Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks
- Support the growth of junior analysts through code reviews, coaching, and documentation
- Explain complex technical concepts to non-technical audiences
- Own the data pipeline from architecting dbt models to enabling self-service in Looker
- Act as translator between engineering and business stakeholders
- Provide mentorship and maintain data culture quality

---

## Required Qualifications

- 4+ years of experience in Data Analytics, BI, or Data Science
- Proven experience building and maintaining scalable dbt or similar framework projects
- Deep understanding of dependency management, reusability, and runtime optimization
- Expert-Level SQL & Optimization producing efficient, production-grade SQL
- Experience in Looker (or similar tools) from backend development to storytelling
- Ability to break down ambiguous problems and take full ownership from definition to delivery

---

## Preferred / Bonus Skills

- None explicitly listed separately from requirements

---

## Benefits

- Hybrid work model with flexible remote setup and working hours
- Up to 2 months remote work annually from anywhere
- Company lunches twice monthly
- Corporate benefits platform
- German language courses
- Climate-neutral operations initiative
- Regular team events and company-wide celebrations

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks are explicitly mentioned as a core responsibility with no velocity-related language present; the JD emphasizes correctness, optimization, and quality over speed.

**Run 2:** `rigour` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes cost optimization, production-grade quality, and testing frameworks with no velocity language, indicating rigour-first orientation.

**Run 3:** `rigour` ✓
> Quote: "high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes quality, optimization, testing frameworks, and mentorship with zero velocity language, establishing a rigour-focused orientation.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: The JD describes internal business intelligence and self-service analytics work with no mention of financial reporting, compliance, or regulatory requirements, indicating operational rather than high financial/regulatory risk.

**Run 2:** `moderate` ✓
> Quote: "Act as translator between engineering and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role supports business decisions without explicit financial reporting, compliance, or regulatory language that would signal high-risk consequences.

**Run 3:** `moderate` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: This is a BI/analytics role at a logistics company with no mention of financial reporting, regulatory compliance, or mission-critical systems, indicating moderate business-decision impact.

### collaboration_width
**Manual:** `3`

**Run 1:** `1` ✗
> Quote: "Act as translator between engineering and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'engineering' counts as an explicitly named partner function; 'business stakeholders' is excluded per the rule that 'the business' does not count.

**Run 2:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only Engineering is explicitly named as a distinct collaboration partner; 'business stakeholders' is generic language that does not count.

**Run 3:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Only one named partner function (Engineering) is explicitly mentioned as a collaboration point in the responsibilities.

⚠ **Disagreement**: manual=`3` vs LLM majority=`1`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: The presence of junior analysts, mentorship responsibilities, and existing tools (dbt, Looker) in active use indicates an established data function that is growing and scaling, not a greenfield build.

**Run 2:** `mid` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: The JD assumes existing data infrastructure (dbt, Looker) that must be owned and maintained, plus references junior analysts, indicating an established function scaling.

**Run 3:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: The existence of junior analysts and active mentorship responsibilities indicate an established data function that is actively scaling beyond its founding phase.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Highly specific technical details (dbt, Jinja, macros, testing frameworks, multi-billion row datasets) suggest hiring manager authorship, but generic boilerplate phrases like 'act as translator between engineering and business stakeholders' indicate recruiter involvement or additions.

**Run 2:** `hiring_manager` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about dbt patterns and advanced methodology reflects hands-on experience that only someone performing this work would articulate.

**Run 3:** `hiring_manager` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical depth about dbt internals (Jinja, macros, testing) and multi-billion row optimization that only someone actively performing this work would know to include.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']
