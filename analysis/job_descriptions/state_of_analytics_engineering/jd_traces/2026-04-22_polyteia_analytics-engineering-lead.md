# Trace: 2026-04-22_polyteia_analytics-engineering-lead

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineering Lead — Polyteia

**URL:** https://polyteia.jobs.personio.de/job/2478119?display=de&language=de&pid=19b90fa3-5f5f-4cd2-8758-eeb8d18cef2b&it=56Pd1f2QPc9dcLiyVWCwTQ&_ghcid=71e67ea4-f328-4404-ad0c-95e7b0e31743

**Location:** Berlin

**Employment Type:** Full-time, Permanent

**Salary:** €80,000–€90,000 annually

---

## Key Responsibilities

- Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover
- Serving as the primary technical and domain expert for complex client questions, collaborating closely with customer success teams
- Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal"
- Leading a team of two Analytics Engineers, providing direction and fostering their professional growth
- Actively coding in Python, dbt, and Airflow while coordinating project advancement

---

## Required Qualifications

- Multiple years implementing data projects with proven ability to guide stakeholders through complex implementations
- Strong technical foundation: SQL and Python proficiency; familiarity with dbt and Airflow
- Domain expertise mindset; ability to understand data context and communicate with subject matter experts
- Fluent German (C2 level) and secure English communication

---

## Preferred Skills

- Prior experience in public administration or GovTech sectors

---

## Benefits

- Influence over platform strategy and technical direction
- Modern technology stack with development freedom
- 29 vacation days
- Hybrid arrangement: three office days weekly in Berlin Kreuzberg
- Urban Sports Club membership and additional benefits
- Inclusive workplace culture emphasizing professional development

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 2 | 2 | 1 | 2 | 33% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | mixed | mixed | hiring_manager | 33% | ✓ |
| stakeholder_orientation |  | commercial | commercial | commercial | 100% | ✗ |
| autonomy_level |  | mixed | mixed | mixed | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The structured progression from initial analysis through operational handover emphasizes methodical, quality-focused delivery without velocity signals.

**Run 2:** `rigour` ✓
> Quote: "multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The emphasis on multi-month timelines and complete operational handover indicates a rigour-oriented approach focused on thoroughness and completeness rather than speed.

**Run 3:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: Multi-month implementation timelines, emphasis on complete handover phases, and domain expertise-driven work indicate rigorous, deliberate project delivery rather than velocity-focused iteration.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: Public sector finance and health data inherently carry regulatory and compliance risks that create high consequences for errors.

**Run 2:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: Public sector work, particularly in finance, carries inherent regulatory and compliance risk due to government accountability and budget oversight requirements.

**Run 3:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including 'Gesundheit, Finanzen oder Personal'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Public sector finance and personnel data carry regulatory compliance and audit requirements, creating high consequences for data errors.

### collaboration_width
**Manual:** `2`

**Run 1:** `2` ✓
> Quote: "public sector clients; customer success teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named collaboration partners identified: customer success teams (internal function) and public sector clients (external parties explicitly named for collaboration).

**Run 2:** `1` ✗
> Quote: "collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named partner team is identified in the responsibilities section.

**Run 3:** `2` ✓
> Quote: "customer success teams; public sector clients"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct partner groups explicitly named: customer success teams as internal collaborators and public sector clients as external partners in implementations.

⚠ **LLM inconsistency**: runs gave ['2', '1', '2']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: An established team structure already exists with named tools in operational responsibilities, indicating beyond-early stage but a team of two suggests growing rather than fully mature.

**Run 2:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers"
> Verified: ✓ found in JD
> Reasoning: An established team with named tools (dbt, Airflow) and existing data products indicates mid-stage maturity rather than greenfield build.

**Run 3:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: A small but established team exists with named tools in active use (dbt, Airflow in responsibilities); not early-stage infrastructure-building, but too small to be mature.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: Specific tool application and project context indicates hiring manager input, balanced against generic phrases like "serving as primary technical expert" typical of recruiter writing.

**Run 2:** `mixed` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: Specific technical details (named tools with context, domain areas, team size) are present alongside generic collaboration language.

**Run 3:** `hiring_manager` ✗
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: Specific tools with application context, explicit team size, and concrete implementation methodology reflect someone who has performed this role, not generic boilerplate language.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `commercial` ✗
> Quote: "Serving as the primary technical and domain expert for complex client questions, collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: Primary responsibilities center on client-facing implementation delivery and customer success partnership, establishing commercial GTM orientation.

**Run 2:** `commercial` ✗
> Quote: "Serving as the primary technical and domain expert for complex client questions, collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: The role's primary responsibilities center on serving external clients and supporting customer success teams, which is commercial stakeholder orientation.

**Run 3:** `commercial` ✗
> Quote: "collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is client delivery and implementation success, with explicit customer success team collaboration indicating customer-facing, commercial orientation.

⚠ **Disagreement**: manual=`` vs LLM majority=`commercial`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth; Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role genuinely combines strategic team leadership and direction-setting with hands-on execution and project delivery work.

**Run 2:** `mixed` ✗
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The role explicitly combines strategic leadership (leading team, providing direction, guiding clients) with hands-on execution (actively coding), indicating mixed autonomy.

**Run 3:** `mixed` ✗
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The role has strategic leadership responsibilities (directing the team's priorities and development) combined with execution responsibilities (guiding client implementations, hands-on coding).

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

### ai_role
**Run 1:** `none` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Reasoning: No AI tools, frameworks, or infrastructure mentioned; standard analytics engineering stack only.

**Run 2:** `none` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Reasoning: No AI tools (Copilot, Claude Code, Cursor) or AI-enablement (GenAI, text-to-SQL) mentioned; standard data engineering stack only.

**Run 3:** `none` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Reasoning: Traditional analytics engineering stack with no AI tools, AI-first mindset, or GenAI infrastructure signals.


### testing_framing
**Run 1:** `absent` ✓
> Quote: "N/A"
> Reasoning: No testing ownership, quality practices, or data contracts mentioned.

**Run 2:** `absent` ✓
> Quote: "Developing and maintaining data products"
> Reasoning: No ownership language (own, ensure, define, implement, establish) paired with testing, quality, or data contracts.

**Run 3:** `absent` ✓
> Quote: "Developing and maintaining data products"
> Reasoning: No testing ownership verbs (ensure, define, implement, establish) and no testing tools explicitly listed.


### loss_aversion_framing
**Run 1:** `none` ✓
> Quote: "Developing and maintaining data products"
> Reasoning: Framing centers on delivery and team leadership without compliance, regulatory, or risk mitigation language.

**Run 2:** `moderate` ✗
> Quote: "Developing and maintaining data products across public sector domains"
> Reasoning: Public sector context implicitly signals compliance and regulatory concerns as operational baseline, though not framed as primary trust/audit focus.

**Run 3:** `none` ✓
> Quote: "Serving as the primary technical and domain expert for complex client questions, collaborating closely with customer success teams"
> Reasoning: Delivery and customer success framing; no compliance, regulatory, reliability, or trustworthiness risk language.

⚠ **LLM inconsistency**: runs gave ['none', 'moderate', 'none']
