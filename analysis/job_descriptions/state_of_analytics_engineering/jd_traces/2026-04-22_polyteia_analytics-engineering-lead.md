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
| collaboration_width | 2 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | hiring_manager | hiring_manager | hiring_manager | 100% | ✗ |
| stakeholder_orientation | commercial | commercial | commercial | commercial | 100% | ✓ |
| autonomy_level | mixed | mixed | mixed | mixed | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Serving as the primary technical and domain expert for complex client questions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasises domain expertise and complex problem-solving as core expectations, with no velocity-oriented language.

**Run 2:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The emphasis on multi-month implementations and comprehensive lifecycle guidance suggests a rigour-oriented approach focused on deliberate execution rather than rapid iteration or shipping.

**Run 3:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The emphasis on multi-month engagements and 'operational handover' signals focus on ensuring systems work reliably and completely rather than rapid iteration or speed-to-market.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: The role explicitly covers Finance and Health domains in the public sector, both of which carry regulatory and compliance requirements that make data errors costly.

**Run 2:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: The explicit mention of Finance (Finanzen) as a core domain for public sector data products indicates high regulatory and compliance risk inherent to financial data work.

**Run 3:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including 'Gesundheit, Finanzen oder Personal'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Explicit mention of Finance (Finanzen) and Health (Gesundheit) data in public sector contexts are inherently high-risk domains with regulatory and compliance implications.

### collaboration_width
**Manual:** `2`

**Run 1:** `1` ✗
> Quote: "collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only Customer Success is explicitly named as a distinct team the role collaborates with.

**Run 2:** `1` ✗
> Quote: "collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only Customer Success is explicitly named as a collaboration partner; other references like stakeholders and subject matter experts are too generic to count as distinct named teams.

**Run 3:** `1` ✗
> Quote: "collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only one named internal team partner is explicitly identified in the responsibilities section.

⚠ **Disagreement**: manual=`2` vs LLM majority=`1`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The team exists with multiple members and is established enough to have formal team structures and succession planning, but is not described as a large, specialised, mature organisation.

**Run 2:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The existence of an established team with existing data products and named tools in active responsibilities (Python, dbt, Airflow) indicates a mid-stage function with growth, not early-stage or highly mature.

**Run 3:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The team has defined structure with multiple named roles and explicit tools (dbt, Airflow) used in responsibilities, indicating established infrastructure beyond first-hire stage.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: The JD specifies tools with precise application context (actively coding while coordinating), specific team size, and domain-specific responsibilities that only someone doing this job would describe.

**Run 2:** `hiring_manager` ✗
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: The specific mention of named tools in an active working context, combined with domain-specific details about public sector implementations and team size, suggests someone with direct experience of this role wrote the responsibilities.

**Run 3:** `hiring_manager` ✗
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: The specific tool context (dbt/Airflow for public sector implementations), domain specificity (Gesundheit, Finanzen, Personal), and precise team size suggest technical knowledge from someone who has done this work.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `commercial` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The primary mission is serving public sector clients through implementation delivery and technical expertise, with collaboration from customer success teams, making this a client-facing commercial role.

**Run 2:** `commercial` ✓
> Quote: "Serving as the primary technical and domain expert for complex client questions, collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: The role is primarily oriented toward external public sector clients and their customer success managers, making this client/customer-facing rather than internal data infrastructure or product analytics.

**Run 3:** `commercial` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The primary audience is external clients served through customer success partnerships, making this a commercial-facing role.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic team leadership and direction-setting with hands-on technical execution and client delivery.

**Run 2:** `mixed` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic elements (leading team, providing direction, domain expertise) with execution responsibilities (actively coding, project coordination), creating genuinely mixed autonomy.

**Run 3:** `mixed` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: The role genuinely combines strategic responsibilities (leading team, guiding clients, coordinating projects) with hands-on execution (actively coding), shown as parallel not sequential.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: There are no references to AI skills, tools, or applications expected of the candidate anywhere in the JD.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no reference to AI coding tools, AI-ready infrastructure, or expectation that the candidate demonstrate AI proficiency.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI-assisted coding, AI tools, or AI-enabled data infrastructure expected of the candidate.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or data quality signal in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: There are no responsibilities, tool requirements, or mentions related to data quality, testing, or observability.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal found in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: Testing, data contracts, and quality assurance are not mentioned in responsibilities, requirements, or elsewhere in the JD.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality language appears in the responsibilities section."
> Verified: ⚠ NOT found verbatim
> Reasoning: There is no mention of data quality frameworks, testing practices, observability, or data contracts anywhere in the JD.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "operational handover"
> Verified: ✓ found in JD
> Reasoning: The framing of client implementation through operational handover suggests responsibility for stable, reliable systems, but without explicit risk, compliance, or loss-prevention language.

**Run 2:** `moderate` ✗
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The mention of operational handover and public sector context imply operational reliability concerns, though compliance or trust is not explicitly emphasized as primary framing.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed around delivery capability (guiding implementations, developing products, leading teams) with no explicit risk, compliance, or stakeholder-trust language despite the regulated domain context.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'none']
