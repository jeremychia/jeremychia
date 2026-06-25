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
| domain_risk | high | moderate | moderate | high | 33% | ✗ |
| collaboration_width | 2 | 1 | 1 | 1 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | mixed | hiring_manager | mixed | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The emphasis on guided, multi-month implementations with complete operational handover signals a rigorous approach focused on completeness and quality rather than speed.

**Run 2:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize thorough, comprehensive implementation processes with explicit attention to quality handover rather than speed or iteration, with no velocity-related language present.

**Run 3:** `rigour` ✓
> Quote: "Guiding public sector clients through multi-month implementations of data products, from initial analysis to operational handover"
> Verified: ✓ found in JD
> Reasoning: The multi-month implementation process culminating in operational handover signals a methodology oriented toward delivering reliable, production-ready outcomes rather than rapid iteration, reinforced by the public sector context.

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: While public sector Finance carries inherent compliance risk, the JD uses generic language about developing and maintaining without explicit financial reporting, audit, or regulatory language.

**Run 2:** `moderate` ✗
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: While the public sector context and Finance domain imply high regulatory risk, the JD uses generic language about 'data products' without explicitly invoking compliance, regulatory, or financial reporting terminology.

**Run 3:** `high` ✓
> Quote: "Developing and maintaining data products across public sector domains including "Gesundheit, Finanzen oder Personal""
> Verified: ✓ found in JD
> Reasoning: Health, finance, and personnel data in the public sector are all regulatory domains where data errors directly affect compliance and public accountability.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'high']

### collaboration_width
**Manual:** `2`

**Run 1:** `1` ✗
> Quote: "customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only Customer Success is explicitly named as a collaboration partner; other references are to the role's own direct team.

**Run 2:** `1` ✗
> Quote: "customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only one explicitly named internal partner function is mentioned in the context of collaboration.

**Run 3:** `1` ✗
> Quote: "collaborating closely with customer success teams"
> Verified: ✓ found in JD
> Reasoning: Only Customer Success is explicitly named as a distinct team; clients are stakeholders served rather than named collaboration partners, and the two analytics engineers are the role holder's own team.

⚠ **Disagreement**: manual=`2` vs LLM majority=`1`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: A named team already exists with multiple roles and specific tools in use, indicating an established function growing beyond initial stage but not yet mature scale.

**Run 2:** `mid` ✓
> Quote: "Leading a team of two Analytics Engineers, providing direction and fostering their professional growth"
> Verified: ✓ found in JD
> Reasoning: The data function is established with existing team members and products being maintained, but the small team size and specific tool mentions in responsibilities indicate a growing rather than mature operation.

**Run 3:** `mid` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: Named tools appearing in the responsibilities section combined with leadership of an existing two-person team indicates an established data function with infrastructure that is scaling up, not a greenfield build.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about named tools and implementation details mixes with generic HR language like 'fostering professional growth' and 'collaborating closely.'

**Run 2:** `hiring_manager` ✗
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical tools in precise context, specific domain knowledge (public sector Finance/Health/HR), and implementation methodology that demonstrates hands-on experience with this specific role.

**Run 3:** `mixed` ✓
> Quote: "Actively coding in Python, dbt, and Airflow while coordinating project advancement"
> Verified: ✓ found in JD
> Reasoning: Specific tool naming and domain knowledge (public sector health/finance/personnel) suggest hiring manager input, but lack of technical context (what scale, what specific challenges, what methodologies) and presence of generic management language indicate recruiter shaping as well.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']
