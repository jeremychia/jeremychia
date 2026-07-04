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
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | execution | strategic | strategic | strategic | 100% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | tool_listed | tool_listed | 33% | ✗ |
| loss_aversion_framing |  | none | moderate | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks, performance optimization, cost-efficiency, and complex problem-solving are emphasized throughout with no velocity signals like 'fast-paced' or 'ship quickly'.

**Run 2:** `rigour` ✓
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing frameworks, production-grade SQL, and data quality culture with no velocity or shipping language, establishing rigour as the primary work orientation.

**Run 3:** `rigour` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks, code reviews, optimization, and quality maintenance are central responsibilities with no velocity language like fast-paced or rapid delivery.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: The role is business intelligence analytics without explicit financial reporting, compliance, or regulatory language, indicating operational decision support rather than high-risk financial contexts.

**Run 2:** `moderate` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: The role focuses on operational analytics and self-serve intelligence for a logistics platform with no financial reporting, compliance, or regulatory signals, indicating moderate business intelligence risk.

**Run 3:** `moderate` ✓
> Quote: "Act as translator between engineering and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role supports operational business decision-making without explicit financial reporting, compliance, or regulatory framing.

### collaboration_width
**Manual:** `3`

**Run 1:** `1` ✗
> Quote: "Act as translator between engineering and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'engineering' is a named specific function; 'business stakeholders' is too vague and junior analysts are part of the role holder's own team.

**Run 2:** `1` ✗
> Quote: "Act as translator between engineering and business stakeholders"
> Verified: ✓ found in JD
> Reasoning: Only 'engineering' counts as a named function; 'business stakeholders' is too vague per the rules, and junior analysts are part of the role holder's own team.

**Run 3:** `1` ✗
> Quote: "engineering"
> Verified: ✓ found in JD
> Reasoning: Engineering is the only explicitly named partner function; business stakeholders is a generic term that does not count.

⚠ **Disagreement**: manual=`3` vs LLM majority=`1`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: Multiple junior analysts exist, dbt and Looker infrastructure are established and active, and data culture is defined—indicating an existing function with scale and growth, not early-stage or fully mature.

**Run 2:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: Multiple analysts exist on the team with established dbt infrastructure and Looker platforms in place, indicating an established function that is actively growing.

**Run 3:** `mid` ✓
> Quote: "Support the growth of junior analysts through code reviews, coaching, and documentation"
> Verified: ✓ found in JD
> Reasoning: The presence of junior analysts to mentor indicates an established and growing data team beyond the early stage.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about dbt implementation details and SQL scale coexist with generic responsibilities like mentorship and translator roles that any analytics recruiter might write.

**Run 2:** `hiring_manager` ✓
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: The specific mention of Jinja, macros, testing frameworks, multi-billion row datasets, and Looker backend-to-storytelling workflows indicates technical depth only a practitioner would write.

**Run 3:** `hiring_manager` ✓
> Quote: "Deliver high-performance, cost-optimized SQL queries designed for multi-billion row datasets"
> Verified: ✓ found in JD
> Reasoning: The specific scale metric (multi-billion rows) and performance context indicate hiring manager familiarity with the actual work scope.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-serve in Looker"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary responsibilities center on building and maintaining analytics infrastructure and supporting the data team, with business stakeholder engagement framed as a translator/support role.

**Run 2:** `internal_data` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: The primary responsibilities focus on building data infrastructure and self-serve analytics platforms, with mentoring junior analysts, indicating the role primarily serves internal analytics consumers and the data function.

**Run 3:** `internal_data` ✓
> Quote: "Own the data pipeline from architecting dbt models to enabling self-service in Looker"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is building data infrastructure for internal consumption and analyst self-service, not serving external business domains.

### autonomy_level
**Manual:** `execution`

**Run 1:** `strategic` ✗
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs ('independently lead', 'own', 'design', 'architect') are applied to the entire problem-solving and pipeline ownership, not narrow technical sub-problems.

**Run 2:** `strategic` ✗
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Verified: ✓ found in JD
> Reasoning: The requirement to independently lead from requirements discovery through delivery, plus ownership of the data pipeline and mentoring, indicates the candidate sets direction for projects and shapes how analytical work is executed.

**Run 3:** `strategic` ✗
> Quote: "Independently lead the Discovery-to-Delivery cycle for medium to highly complex tasks"
> Verified: ✓ found in JD
> Reasoning: The role has primary responsibility for setting direction and owning the discovery-to-delivery cycle, not executing work defined by others.

⚠ **Disagreement**: manual=`execution` vs LLM majority=`strategic`

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI coding tools, agentic workflows, AI infrastructure, or AI-related candidate skills anywhere in the JD.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted workflows, or AI data infrastructure requirements for the candidate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools, coding agents, or AI-related expectations for the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Design, build, and maintain dbt models, utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks are embedded as core to building and maintaining dbt models, indicating the candidate owns testing practices as an integral responsibility, not a separate tool requirement.

**Run 2:** `tool_listed` ✗
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks are listed as tools used in dbt model design without explicit ownership verbs like 'own' or 'define', making this tool_listed rather than responsibility.

**Run 3:** `tool_listed` ✗
> Quote: "utilizing advanced Jinja, macros, and testing frameworks"
> Verified: ✓ found in JD
> Reasoning: Testing frameworks appear as part of the dbt toolkit the candidate uses without explicit ownership verbs like own, define, or implement.

⚠ **Disagreement**: manual=`` vs LLM majority=`tool_listed`

⚠ **LLM inconsistency**: runs gave ['responsibility', 'tool_listed', 'tool_listed']

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes capability and quality culture in positive terms, without loss-aversion language around compliance, incidents, or preventing bad data reaching stakeholders.

**Run 2:** `moderate` ✗
> Quote: "maintain data culture quality"
> Verified: ✓ found in JD
> Reasoning: Some concern with production reliability and quality standards appears in 'production-grade SQL' and quality culture maintenance, but risk prevention is secondary to delivery and capability framing.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed around delivery capability and quality output, not around preventing bad outcomes, reliability concerns, or risk mitigation.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'none']
