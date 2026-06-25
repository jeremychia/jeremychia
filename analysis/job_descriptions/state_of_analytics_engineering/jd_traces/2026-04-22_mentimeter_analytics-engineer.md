# Trace: 2026-04-22_mentimeter_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Mentimeter

**URL:** https://job-boards.eu.greenhouse.io/mentimeter/jobs/4839752101?gh_src=3d5665c2teu

**Location:** Stockholm, Sweden (Onsite/Hybrid)

**Visa Sponsorship:** Not available

---

## Key Responsibilities

- Design, own, and evolve core data models and the modelling architecture
- Partner with business and technical stakeholders from problem framing to shipped artefacts
- Build standards, documentation, and data catalogs for the organization
- Contribute strategic input around data modeling, BI tooling, and AI-assisted analytics
- Help the organization interpret data

---

## Required Qualifications

- Roughly 4–7 years of relevant hands-on experience as an Analytics Engineer, Data Analyst, Data Scientist, BI Analyst, or similar role
- Strong SQL proficiency and sound data modeling judgment
- Experience collaborating and translating ambiguous stakeholder needs to clear, maintainable models
- Business acumen covering sales, marketing, and product analytics
- Experience with BI tools and development of BI features
- Git proficiency
- Communication in English with both technical and non-technical audiences
- Experience working with GDPR-sensitive data

---

## Preferred / Bonus Skills

- Hands-on dbt experience
- Experience with a semantic layer or metrics layer
- Experience using AI-assisted coding or coding agents in a disciplined way (reviews, tests, documentation)
- Agile environment experience

---

## Benefits

- Competitive compensation and benefits package, including pension contributions
- Professional development access
- Flexible work-life balance policies

---

## Analysis

### Layer A — Surface Extraction

| Field | Value |
|-------|-------|
| **Company slug** | mentimeter |
| **Job title slug** | analytics-engineer |
| **Experience range** | 4–7 years |
| **Team maturity signal** | Data team maturing; emphasis on standards, architecture, documentation |
| **Compliance context** | GDPR-sensitive data handling required |

---

#
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | high | moderate | 33% | ✓ |
| collaboration_width | 4 | 3 | 0 | 0 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | recruiter | mixed | hiring_manager | 0% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section prioritizes standards, documentation, catalogs, and disciplined practice (with reviews and tests noted in preferred skills) over speed or iteration, establishing a rigour-first orientation.

**Run 2:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building standards, documentation, and architecture rather than speed or iteration, with no velocity-oriented language present.

**Run 3:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize establishing governance structures, documentation, and architectural clarity rather than shipping speed or iteration pace.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: While GDPR-sensitive data handling invokes regulatory compliance, the JD's primary framing emphasizes modeling, standards, and interpretation rather than compliance reporting or financial accuracy, placing it at moderate risk.

**Run 2:** `high` ✗
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement to handle GDPR-sensitive data signals regulatory and compliance concerns material to the role.

**Run 3:** `moderate` ✓
> Quote: "GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance requires care, the role's core focus is business analytics (sales, marketing, product) rather than financial reporting or regulatory compliance that would carry high risk.

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'moderate']

### collaboration_width
**Manual:** `4`

**Run 1:** `3` ✗
> Quote: "sales, marketing, and product analytics"
> Verified: ✓ found in JD
> Reasoning: The required qualifications explicitly name three distinct business functions: sales, marketing, and product (implied by 'product analytics').

**Run 2:** `0` ✗
> Quote: "Partner with business and technical stakeholders from problem framing to shipped artefacts"
> Verified: ✓ found in JD
> Reasoning: No specific partner teams are explicitly named; collaboration is described generically as working with undefined 'stakeholders'.

**Run 3:** `0` ✗
> Quote: "Partner with business and technical stakeholders from problem framing to shipped artefacts"
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaboration but uses generic phrasing ('stakeholders') and names no specific teams, departments, or partner functions.

⚠ **Disagreement**: manual=`4` vs LLM majority=`0`

⚠ **LLM inconsistency**: runs gave ['3', '0', '0']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Building organizational standards, documentation, and catalogs is characteristic of a data function moving beyond foundational stage to professionalization and governance, but not yet operating as a specialized, scale-stage organization.

**Run 2:** `mid` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The team has existing infrastructure (models, BI tools) but is actively building governance and standards, indicating a growing mid-stage data function.

**Run 3:** `mid` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: The word 'evolve' signals existing infrastructure that requires maturation and architectural work, positioning this as a mid-stage team growing its standards and governance.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `recruiter` ✗
> Quote: "Help the organization interpret data"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section relies entirely on generic boilerplate action verbs and stakeholder collaboration language; it lacks specific tools, methodologies, technical depth, or Tuesday-morning context that would indicate hiring manager authorship.

**Run 2:** `mixed` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical depth (dbt, semantic layer, GDPR, data modeling ownership) from a hiring manager alongside generic phrasing about stakeholder collaboration and communication.

**Run 3:** `hiring_manager` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture; Build standards, documentation, and data catalogs for the organization; Contribute strategic input around data modeling, BI tooling, and AI-assisted analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities demonstrate specific technical understanding of data modeling, semantic layers (mentioned in preferred skills), and architectural work that only someone experienced in these disciplines would articulate.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`recruiter`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'hiring_manager']
