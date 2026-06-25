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
| data_team_maturity | early | early | mid | mid | 33% | ✗ |
| jd_authorship | hiring_manager | mixed | mixed | hiring_manager | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality standards, testing infrastructure, and documentation as core professional expectations, with accuracy and maintainability repeated as explicit priorities.

**Run 2:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes quality practices (tests, CI/CD, documentation) and data standards, with no velocity language like 'move fast' or 'ship quickly' — this is rigour-oriented.

**Run 3:** `rigour` ✗
> Quote: "Establish data quality standards using tests, CI/CD, and documentation."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, testing, and CI/CD as core expectations, with speed mentioned only as one factor to balance alongside accuracy and maintainability.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "customers, revenue, and operations"
> Verified: ✓ found in JD
> Reasoning: Revenue is mentioned as a core analytics domain within an energy-trading sector, but the JD lacks explicit financial reporting, compliance, or regulatory language despite the high-risk industry context.

**Run 2:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: Revenue is financially important but the JD frames this as analytics engineering work without explicit regulatory, compliance, or financial reporting language that would signal high risk.

**Run 3:** `moderate` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: While revenue data is involved, the JD uses generic business language without explicit financial reporting, compliance, or regulatory requirements typical of high-risk domains.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `4`

**Run 1:** `4` ✓
> Quote: "partnering with Marketing, Finance, Operations, and Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Four distinct named teams are explicitly listed as collaboration partners in the role description.

**Run 2:** `4` ✓
> Quote: "Marketing, Finance, Operations, and Data Engineering"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names four distinct partner teams in the responsibilities section.

**Run 3:** `4` ✓
> Quote: "Marketing; Finance; Operations; Data Engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Four explicitly named teams listed as collaboration partners in the partnership statement.

### data_team_maturity
**Manual:** `early`

**Run 1:** `early` ✓
> Quote: "building the analytics foundation"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is explicitly to establish the analytics foundation, which directly signals early-stage team status focused on foundational work.

**Run 2:** `mid` ✗
> Quote: "Partner with Data Engineering to diagnose issues and optimize warehouse performance."
> Verified: ✓ found in JD
> Reasoning: Established Data Engineering team, named tools in active use (dbt, Omni), and optimization work indicate a maturing function with infrastructure in place, not greenfield startup.

**Run 3:** `mid` ✗
> Quote: "building the analytics foundation"
> Verified: ✓ found in JD
> Reasoning: The analytics layer is being built with existing infrastructure at scale (1B rows daily, separate Data Engineering team present), indicating growth phase rather than greenfield or fully mature stage.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['early', 'mid', 'mid']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: The responsibilities include specific technical context (named tools, business domains) suggesting hiring manager input, but also generic phrasing and boilerplate verbs (design, maintain, lead) indicating recruiter involvement.

**Run 2:** `mixed` ✗
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: Tool-specific responsibilities (dbt models, Omni metrics, tests/CI/CD) show hiring manager input, but generic boilerplate like 'lead cross-domain analytics projects spanning multiple teams' indicates recruiter contribution.

**Run 3:** `hiring_manager` ✓
> Quote: "Design and maintain core dbt models representing business areas like customers, revenue, and operations."
> Verified: ✓ found in JD
> Reasoning: The specific tools (dbt, Omni), named business areas, production scale context, and technical approaches (tests, CI/CD, warehouse optimization) indicate hiring manager authored this with deep technical knowledge.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']
