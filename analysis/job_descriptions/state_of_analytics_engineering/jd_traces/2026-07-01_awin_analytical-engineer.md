# Trace: 2026-07-01_awin_analytical-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytical Engineer — Awin

**URL:** https://job-boards.greenhouse.io/awin/jobs/7785591003?gh_src=e8316d393us
**Location:** Iași, Romania or Warsaw, Poland (Hybrid)
**Date Posted:** 2026-07-01

---

Analytical Engineer at Awin

Role Overview
Awin seeks an Analytical Engineer to establish their analytics engineering practice within the BI team. The position bridges Data Engineering and Business Intelligence, focusing on creating a trusted semantic layer that enables self-serve analytics across the organisation.

Primary Responsibilities
- Provide business context for the mart layers of our data architecture
- Establish a single source of truth for business metric definitions
- Partner with Data Engineering teams
- Collaborate with BI Developers and Insight Analysts
- Design data marts with self-serve usage in mind
- Coach BI Developers in Analytics Engineering best practices
- Create documentation enabling independent contributions
- Translate ambiguous business requirements into clear, well-documented data definitions

Required Qualifications
- Strong SQL proficiency
- Production experience with dbt
- Familiarity with cloud data warehouses
- Understanding of data modelling concepts like dimensional modelling and star schemas
- Experience working within BI teams
- Ability to translate ambiguous business requirements into clear, well-documented data definitions
- Strong communication abilities

Preferred Experience
- Tableau or Power BI experience
- Databricks knowledge
- Semantic layer tooling familiarity
- Mentoring experience
- Exposure to data observability or AI-readiness concepts

Location & Benefits
- Positions available in Iași, Romania and Warsaw, Poland
- Flexible four-day work weeks at full pay
- Hybrid work options
- Development programs through Awin Academy
- Remote working allowances

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | mixed | execution | strategic | 0% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | moderate | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes accurate metrics, documentation, best practices, and trusted infrastructure with no velocity signals.

**Run 2:** `rigour` ✓
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes establishing foundational practices with clear documentation and best practices rather than delivery speed or iteration pace.

**Run 3:** `rigour` ✓
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize establishing trusted metrics, best practices, and well-documented definitions without any velocity language like fast-paced iteration or rapid delivery.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "creating a trusted semantic layer that enables self-serve analytics across the organisation"
> Verified: ✓ found in JD
> Reasoning: Supports business decisions across the organization without financial reporting or regulatory signals.

**Run 2:** `moderate` ✓
> Quote: "creating a trusted semantic layer that enables self-serve analytics across the organisation"
> Verified: ✓ found in JD
> Reasoning: Data errors would affect business decisions through self-serve analytics, but lacks explicit financial, regulatory, or compliance language indicating high risk.

**Run 3:** `moderate` ✓
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: The role focuses on analytics infrastructure for business decision-making rather than financial reporting, compliance, or regulatory concerns.

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Partner with Data Engineering teams; Collaborate with BI Developers and Insight Analysts"
> Verified: ✓ found in JD
> Reasoning: Three distinct named partner functions: Data Engineering, BI Developers, and Insight Analysts.

**Run 2:** `3` ✓
> Quote: "Partner with Data Engineering teams; Collaborate with BI Developers and Insight Analysts"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams/roles are explicitly identified as collaboration partners across the responsibilities.

**Run 3:** `3` ✓
> Quote: "Partner with Data Engineering teams; Collaborate with BI Developers and Insight Analysts"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct teams: Data Engineering, BI Developers, and Insight Analysts.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "establish their analytics engineering practice within the BI team"
> Verified: ✓ found in JD
> Reasoning: Data function exists with multiple roles (Data Engineering, BI teams) but the analytics engineering practice specifically needs establishment and growth.

**Run 2:** `mid` ✓
> Quote: "establish their analytics engineering practice within the BI team"
> Verified: ✓ found in JD
> Reasoning: Analytics engineering is being newly established but within an already-existing BI and Data Engineering infrastructure with multiple roles implied, indicating mid-stage maturity.

**Run 3:** `mid` ✓
> Quote: "establish their analytics engineering practice within the BI team"
> Verified: ✓ found in JD
> Reasoning: Multiple data functions already exist (Data Engineering, BI, Analysts) but the analytics engineering practice is newly being established and scaled.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Provide business context for the mart layers of our data architecture; Partner with Data Engineering teams"
> Verified: ✓ found in JD
> Reasoning: Specific technical concepts (mart layers, semantic layers, dimensional modelling) mixed with generic collaboration language.

**Run 2:** `mixed` ✗
> Quote: "Design data marts with self-serve usage in mind; Coach BI Developers in Analytics Engineering best practices"
> Verified: ✓ found in JD
> Reasoning: Technical specificity in semantic layer focus and coaching responsibilities suggests hiring manager input, but generic collaboration verbs and lack of scale/context indicate recruiter contribution.

**Run 3:** `mixed` ✗
> Quote: "Design data marts with self-serve usage in mind; Coach BI Developers in Analytics Engineering best practices"
> Verified: ✓ found in JD
> Reasoning: Specific technical architecture concepts (data marts, semantic layer, dimensional modeling) mix with generic collaboration and coaching verbs.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "creating a trusted semantic layer that enables self-serve analytics across the organisation"
> Verified: ✓ found in JD
> Reasoning: Role builds data infrastructure for internal consumers to use independently rather than serving commercial, product, or finance functions.

**Run 2:** `internal_data` ✓
> Quote: "Design data marts with self-serve usage in mind; Coach BI Developers in Analytics Engineering best practices; Create documentation enabling independent contributions"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is enabling other data professionals and analytics consumers through infrastructure, coaching, and documentation rather than serving external stakeholders.

**Run 3:** `internal_data` ✓
> Quote: "Design data marts with self-serve usage in mind"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is building analytics infrastructure and enabling self-serve data consumption for internal data consumers.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `mixed` ✗
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: Strategic ownership of analytics engineering practice and metric standards combined with execution supporting other teams' analytics needs.

**Run 2:** `execution` ✗
> Quote: "Translate ambiguous business requirements into clear, well-documented data definitions"
> Verified: ✓ found in JD
> Reasoning: While the role includes design responsibility for marts and metric definitions, it primarily executes direction set by business requirements and operates within an existing BI team structure.

**Run 3:** `strategic` ✓
> Quote: "establish their analytics engineering practice within the BI team"
> Verified: ✓ found in JD
> Reasoning: The role is tasked with establishing and shaping how analytics engineering practices are delivered, designing the architecture, and coaching others in best practices.

⚠ **Disagreement**: manual=`strategic` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'strategic']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "Exposure to data observability or AI-readiness concepts"
> Verified: ✓ found in JD
> Reasoning: Only vague preference for exposure to concepts in preferred experience; no concrete AI skill requirement for the candidate.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No expected AI skill is articulated; the vague reference to 'AI-readiness concepts' in preferred experience does not constitute a clear expectation for the candidate to use or enable AI.

**Run 3:** `none` ✗
> Quote: "Exposure to data observability or AI-readiness concepts"
> Verified: ✓ found in JD
> Reasoning: The only AI mention is vague preferred exposure rather than a required skill expectation for using or building with AI tools.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Exposure to data observability or AI-readiness concepts"
> Verified: ✓ found in JD
> Reasoning: No testing frameworks, data quality ownership, or observability responsibilities defined; observability mentioned only as marginal preferred skill.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal in responsibilities."
> Verified: ⚠ NOT found verbatim
> Reasoning: Testing, data quality frameworks, and data contracts are absent from core responsibilities; observability only appears as optional preferred experience without ownership framing.

**Run 3:** `absent` ✗
> Quote: "Exposure to data observability or AI-readiness concepts"
> Verified: ✓ found in JD
> Reasoning: No explicit testing, data quality frameworks, or data contracts are mentioned in the responsibilities; the single data observability reference is too vague and peripheral.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: JD framed around building capabilities and establishing best practices, not preventing bad outcomes or managing risk.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The role is framed around establishing analytics engineering practices and enabling self-serve analytics as a capability-building effort, not around preventing bad outcomes or managing organizational risk.

**Run 3:** `moderate` ✗
> Quote: "Establish a single source of truth for business metric definitions"
> Verified: ✓ found in JD
> Reasoning: The framing implies concern about preventing metric confusion and unreliable data affecting business decisions, but lacks regulatory or compliance risk language.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

⚠ **LLM inconsistency**: runs gave ['none', 'none', 'moderate']
