# Trace: 2026-04-08_tem_staff-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Staff Analytics Engineer — tem

**URL:** https://jobs.ashbyhq.com/tem/66b06873-4d08-4347-9d16-dc5c24ae481c  
**Location:** United Kingdom (Remote)  
**Employment Type:** Full-time  
**Salary:** £100,500/year

---

## About tem

tem is rebuilding energy transactions to be transparent and fair. The company has developed AI-native transaction infrastructure for buying, selling, and pricing electricity. After closing a $75 million Series B in late 2025, tem is positioned for global expansion.

---

## The Role

This hands-on, individual contributor position focuses on building the analytics foundation. You'll work end-to-end on the analytics layer, using dbt for transformations and Omni as the semantic layer. The role involves partnering with Marketing, Finance, Operations, and Data Engineering teams.

---

## Key Responsibilities

- Design and maintain core dbt models representing business areas like customers, revenue, and operations.
- Define and implement company metrics in Omni for self-serve analytics.
- Lead cross-domain analytics projects spanning multiple teams.
- Balance speed, accuracy, and maintainability in data modeling decisions.
- Establish data quality standards using tests, CI/CD, and documentation.
- Partner with Data Engineering to diagnose issues and optimize warehouse performance.

---

## Must-Have Requirements

- Strong analytics engineering experience in fast-moving environments.
- Ability to set direction for analytics patterns, standards, and strategy.
- Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture.
- Excellent SQL and data modeling fundamentals.
- Semantic layer/BI tool experience (Omni, Looker, or similar).
- Experience defining metrics with business stakeholders.
- Comfort operating with ambiguity.

---

## Nice-to-Haves

- Marketing and Finance data experience.
- Early-stage analytics stack building.
- Experimentation, funnel analysis, or unit economics familiarity.

---

## Benefits

- Stock options for team ownership.
- 25 days holiday plus public holidays (customizable); birthday day off.
- Fully remote, distributed across Europe.
- £1,200/€1,200 annual home office budget.
- £150/€150 monthly wellbeing budget.
- Twice-yearly salary reviews using market data.

---

## Interview Process

Approximately 2–3 weeks total:
1. Talent team call (30 mins)
2. Behaviour interview with Data Manager (60 mins)
3. Technical interview with team (90 mins)
4. Culture-add interview with stakeholders (45 mins)

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 4 | 4 | 4 | 4 | 100% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | mixed | hiring_manager | 33% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality standards, testing, and CI/CD pipelines as core expectations, outweighing the single mention of fast-paced environments.

**Run 2:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality standards, testing, CI/CD, and documentation with explicit ownership language; speed is mentioned but balanced against accuracy and maintainability.

**Run 3:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize correctness through testing, CI/CD, documentation, and structured data modeling far more than delivery speed.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: Revenue data is core to the role, affecting business decisions, but there is no explicit regulatory, compliance, or financial reporting language to elevate this to high risk.

**Run 2:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: While the company operates in energy transactions, the JD uses generic analytics engineering language without explicit financial reporting, compliance, or regulatory framing.

**Run 3:** `moderate` ✗
> Quote: "representing business areas like customers, revenue, and operations"
> Verified: ✓ found in JD
> Reasoning: While energy transactions operate in a regulated sector, the JD language focuses on analytics infrastructure rather than explicitly invoking compliance, regulatory, or financial reporting concerns.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `4` ✓
> Quote: "Marketing; Finance; Operations; Data Engineering"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names four distinct partner teams in the opening description.

**Run 2:** `4` ✓
> Quote: "partnering with Marketing, Finance, Operations, and Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions (Marketing, Finance, Operations, Data Engineering) are explicitly identified as collaboration partners.

**Run 3:** `4` ✓
> Quote: "partnering with Marketing, Finance, Operations, and Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Four named functions are explicitly identified as collaboration partners in the role summary.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: Named tools and specific business area models in responsibilities, plus existing warehouse and data engineering team, indicate a data function building and scaling existing infrastructure rather than starting from zero.

**Run 2:** `mid` ✗
> Quote: "This hands-on, individual contributor position focuses on building the analytics foundation."
> Verified: ✓ found in JD
> Reasoning: Named tools in production use (dbt at ~1B rows daily, Omni) and scale signals indicate an established team growing and expanding, not an early-stage greenfield build.

**Run 3:** `mid` ✗
> Quote: "building the analytics foundation"
> Verified: ✓ found in JD
> Reasoning: The role establishes analytics standards and metrics in a company with existing Data Engineering and production-scale infrastructure (~1B rows daily), indicating mid-stage data maturity.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture."
> Verified: ✓ found in JD
> Reasoning: The specificity of dbt requirements at 1B-row scale with custom macros, combined with named tools and precise context, indicates this was written by someone with hands-on analytics engineering experience.

**Run 2:** `mixed` ✗
> Quote: "Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture."
> Verified: ✓ found in JD
> Reasoning: Requirements contain technical specificity (named tools with scale context and optimization details), while responsibilities mix specific tool mentions with generic action verbs like 'design', 'define', and 'establish'.

**Run 3:** `hiring_manager` ✓
> Quote: "Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture."
> Verified: ✓ found in JD
> Reasoning: The specific volume numbers, named technical patterns (incremental models, custom macros), and tool-specific context indicate technical authorship from someone who has performed this work.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Define and implement company metrics in Omni for self-serve analytics."
> Verified: ✓ found in JD
> Reasoning: The primary focus is building the analytics foundation and self-serve analytics layer that internal teams will consume, making this fundamentally an internal data platform role.

**Run 2:** `internal_data` ✓
> Quote: "Define and implement company metrics in Omni for self-serve analytics."
> Verified: ✓ found in JD
> Reasoning: The primary mission is building the analytics infrastructure (dbt models, semantic layer, metrics) for internal consumption, establishing patterns and standards for other data consumers.

**Run 3:** `internal_data` ✓
> Quote: "define and implement company metrics in Omni for self-serve analytics"
> Verified: ✓ found in JD
> Reasoning: Self-serve analytics and semantic layer implementation are internal data infrastructure activities designed to serve other data consumers, not external GTM or product teams.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Ability to set direction for analytics patterns, standards, and strategy."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly requires the candidate to set direction for analytics patterns and strategy, supported by responsibilities using strategic verbs like design, define, lead, and establish.

**Run 2:** `strategic` ✓
> Quote: "Ability to set direction for analytics patterns, standards, and strategy."
> Verified: ✓ found in JD
> Reasoning: The requirements explicitly expect the candidate to set direction for analytics patterns and strategy, indicating ownership of direction-setting rather than execution of defined work.

**Run 3:** `strategic` ✓
> Quote: "Ability to set direction for analytics patterns, standards, and strategy."
> Verified: ✓ found in JD
> Reasoning: The role is explicitly expected to set direction and establish standards (define, design, lead), indicating strategic ownership rather than execution against pre-set priorities.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: While the company builds AI-native infrastructure, the JD contains no expectation for the candidate to use AI tools, build AI-ready data foundations, or work with AI/ML pipelines.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The company builds AI-native products, but the JD contains no expectations for the candidate to use AI coding tools or build AI-supporting data infrastructure.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The company description mentions AI-native infrastructure, but the JD contains no requirement for the candidate to use AI tools or build AI-enabling data infrastructure.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Testing and data quality standards are framed as a responsibility the candidate owns and establishes, not merely as a tool to use.

**Run 2:** `responsibility` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Testing and data quality are framed as something the candidate owns and establishes (verb 'establish'), indicating accountability for the practice rather than just familiarity with tools.

**Run 3:** `responsibility` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The verb 'establish' indicates the candidate owns defining and implementing data quality and testing practices, not just using existing tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Balance speed, accuracy, and maintainability in data modeling decisions."
> Verified: ✓ found in JD
> Reasoning: Accuracy is mentioned as a concern balanced against speed, indicating operational reliability matters, but the overall framing emphasizes capability-building rather than risk prevention.

**Run 2:** `moderate` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Data quality and operational reliability are clearly important concerns, but the role is primarily framed around building and delivering analytics capability rather than preventing bad outcomes or managing risk.

**Run 3:** `moderate` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Data quality and accuracy are core concerns framed as operational standards and reliability practices, but without explicit regulatory, compliance, or stakeholder-trust risk language.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
