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
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | mixed | strategic | strategic | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (data quality, tests, CI/CD, documentation) significantly outnumber velocity signals, establishing clear prioritization of correctness and governance.

**Run 2:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasises data quality standards, testing, CI/CD, and documentation as core expectations, which are rigour signals that significantly outnumber the velocity references.

**Run 3:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (data quality, tests, CI/CD, documentation) substantially outnumber the single velocity signal appearing in requirements.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: While revenue is involved, the JD lacks explicit regulatory, compliance, or financial reporting language; focus is analytics infrastructure rather than financial controls.

**Run 2:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: Though the sector is financial (energy transactions), the JD language focuses on business analytics and self-serve analytics infrastructure rather than compliance, audit, or regulatory reporting.

**Run 3:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: While the energy-transactions sector carries inherent risk, the JD emphasizes business analytics without regulatory, compliance, or explicit financial reporting language.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `4` ✓
> Quote: "partnering with Marketing, Finance, Operations, and Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named functions are explicitly listed as collaboration partners.

**Run 2:** `4` ✓
> Quote: "Marketing, Finance, Operations, and Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named teams are explicitly mentioned as collaboration partners in the role description.

**Run 3:** `4` ✓
> Quote: "Marketing; Finance; Operations; Data Engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four distinct named teams explicitly listed as collaboration partners in the role description.

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "This hands-on, individual contributor position focuses on building the analytics foundation."
> Verified: ✓ found in JD
> Reasoning: The analytics layer is newly being built on top of existing infrastructure (dbt, Omni, established Data Engineering team), indicating mid-stage maturity.

**Run 2:** `mid` ✗
> Quote: "building the analytics foundation"
> Verified: ✓ found in JD
> Reasoning: The role involves building the analytics layer, but with existing infrastructure (dbt, Omni, Data Engineering team) already in place and operating at scale.

**Run 3:** `mid` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: Existing named tools (dbt, Omni) are already deployed and referenced in responsibilities, indicating past infrastructure work; this IC hire is scaling/formalizing an established foundation.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture."
> Verified: ✓ found in JD
> Reasoning: Specific technical details like ~1B rows daily scale, incremental models, and custom macros indicate direct hiring manager authorship.

**Run 2:** `hiring_manager` ✓
> Quote: "Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture."
> Verified: ✓ found in JD
> Reasoning: The requirements contain highly specific technical details and scale metrics that only come from someone who performs this work; a recruiter would not specify incremental models at 1B rows daily.

**Run 3:** `hiring_manager` ✓
> Quote: "Production dbt experience including incremental models at scale (~1B rows daily), custom macros, optimization, and architecture."
> Verified: ✓ found in JD
> Reasoning: Specific scale metrics, tool-specific technical depth (incremental models, custom macros, architecture decisions), and domain context indicate hands-on technical authorship.

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Define and implement company metrics in Omni for self-serve analytics."
> Verified: ✓ found in JD
> Reasoning: The primary responsibility centers on enabling self-serve analytics for internal data consumers, positioning the role as analytics platform enabler rather than serving commercial or finance teams.

**Run 2:** `internal_data` ✗
> Quote: "Define and implement company metrics in Omni for self-serve analytics."
> Verified: ✓ found in JD
> Reasoning: The role explicitly emphasises self-serve analytics and building analytics infrastructure; while it partners with other teams, the primary mission is enabling internal analytics consumers.

**Run 3:** `internal_data` ✗
> Quote: "Define and implement company metrics in Omni for self-serve analytics."
> Verified: ✓ found in JD
> Reasoning: The primary mission is building analytics infrastructure and enabling self-serve access for internal consumers, not serving commercial, product, or finance functions directly.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Define and implement company metrics in Omni for self-serve analytics."
> Verified: ✓ found in JD
> Reasoning: This responsibility demonstrates both strategic direction-setting (define metrics and standards) and hands-on execution, reinforced by 'hands-on, individual contributor' combined with 'set direction for analytics patterns' expectations.

**Run 2:** `strategic` ✗
> Quote: "Ability to set direction for analytics patterns, standards, and strategy."
> Verified: ✓ found in JD
> Reasoning: The requirements explicitly demand the ability to set direction for patterns, standards, and strategy, indicating the role is expected to shape how analytics is delivered rather than execute assigned work.

**Run 3:** `strategic` ✗
> Quote: "Ability to set direction for analytics patterns, standards, and strategy."
> Verified: ✓ found in JD
> Reasoning: Requirements explicitly expect the role to set direction and establish standards, with strategic verbs (define, establish, lead, build) driving the responsibilities.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'strategic']

### ai_role
**Run 1:** `none` ✓
> Quote: "No mentions across all phrases"
> Reasoning: No AI tools, enablement responsibilities, or infrastructure readiness signals.

**Run 2:** `none` ✓
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations"
> Reasoning: No AI tool usage or infrastructure signals; standard dbt-based analytics engineering work

**Run 3:** `none` ✓
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Reasoning: No AI skills or infrastructure responsibilities mentioned; standard analytics engineering work.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Establish data quality standards using tests, CI/CD, and documentation"
> Reasoning: Candidate owns quality standards establishment with tests as core practice.

**Run 2:** `responsibility` ✓
> Quote: "Establish data quality standards using tests, CI/CD, and documentation"
> Reasoning: Candidate owns quality practice by establishing standards, implementing tests, and CI/CD processes

**Run 3:** `responsibility` ✓
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Reasoning: Candidate owns data quality practice through establishing standards, tests, and CI/CD implementation.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Partner with Data Engineering to diagnose issues and optimize warehouse performance"
> Reasoning: Operational reliability concern (issue diagnosis, performance tuning) without regulatory or compliance framing.

**Run 2:** `moderate` ✓
> Quote: "Partner with Data Engineering to diagnose issues and optimize warehouse performance"
> Reasoning: Operational reliability concern signaled through problem diagnosis and performance optimization

**Run 3:** `moderate` ✓
> Quote: "Partner with Data Engineering to diagnose issues and optimize warehouse performance."
> Reasoning: Framing emphasizes operational reliability and performance concerns rather than compliance or regulatory risk.

