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
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 4 | 3 | 3 | 0 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | strategic | strategic | strategic | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit rigour signals (standards, documentation, catalogs, sound data modeling judgment, clear maintainable models, disciplined methodology) with zero velocity language establish a clear rigour orientation.

**Run 2:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building standards, documentation, and data catalogs—core indicators of a rigour-focused role—with no countervailing velocity language.

**Run 3:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, quality, and organizational structure through standards and documentation, with no velocity or shipping language present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance requirement indicates regulatory responsibility, but absence of financial reporting, audit, or regulatory language prevents classification as high risk.

**Run 2:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance is mentioned, the role is fundamentally product/business analytics for a SaaS company, not financial reporting or regulatory compliance reporting.

**Run 3:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is mentioned but refers to data privacy handling rather than financial reporting or regulatory risk; the role is analytics for a SaaS product, not financial/compliance reporting.

### collaboration_width
**Manual:** `4`

**Run 1:** `3` ✗
> Quote: "Business acumen covering sales, marketing, and product analytics"
> Verified: ✓ found in JD
> Reasoning: Sales, Marketing, and Product are three distinct business functions explicitly named in the business acumen requirement.

**Run 2:** `3` ✗
> Quote: "Business acumen covering sales, marketing, and product analytics"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names Sales, Marketing, and Product as distinct business functions the role engages with.

**Run 3:** `0` ✗
> Quote: "Partner with business and technical stakeholders from problem framing to shipped artefacts"
> Verified: ✓ found in JD
> Reasoning: No named teams or functions are explicitly listed as collaboration partners; all stakeholder references use generic language.

⚠ **Disagreement**: manual=`4` vs LLM majority=`3`

⚠ **LLM inconsistency**: runs gave ['3', '3', '0']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Emphasis on building organizational standards and catalogs indicates a data function that has moved beyond early stage but is still establishing governance infrastructure.

**Run 2:** `mid` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: The use of 'evolve' and 'core data models' signals existing infrastructure, while the emphasis on building standards indicates a team scaling its practices rather than establishing from zero.

**Run 3:** `mid` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The focus on formalizing standards, documentation, and governance indicates an established data function actively scaling and professionalizing, not building from zero.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Experience using AI-assisted coding or coding agents in a disciplined way (reviews, tests, documentation)"
> Verified: ✓ found in JD
> Reasoning: Specific technical requirements (dbt, semantic layer, disciplined AI methodology) indicate hiring manager input, while generic collaboration verbs throughout suggest recruiter involvement.

**Run 2:** `mixed` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture; Partner with business and technical stakeholders from problem framing to shipped artefacts"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines technical specificity about modeling and architecture (hiring-manager-level) with generic stakeholder collaboration language (recruiter-level).

**Run 3:** `recruiter` ✗
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic action verbs without specific tool context, implementation details, scale numbers, or problem-domain specificity that would indicate hands-on technical authorship.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Primary focus on building data infrastructure and organizational standards indicates the role primarily serves the data function and its consumers rather than external business stakeholders.

**Run 2:** `internal_data` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture; Build standards, documentation, and data catalogs for the organization"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role's primary impact is building data infrastructure and standards that serve analytics consumers and the data function, not directly driving commercial or product decisions.

**Run 3:** `internal_data` ✗
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The primary mission is establishing data infrastructure and enablement for analytics consumers rather than serving a specific business function like commercial, product, or finance.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: Responsibility to design and own data architecture indicates strategic autonomy to define technical direction rather than execute direction set by others.

**Run 2:** `strategic` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture; Contribute strategic input around data modeling, BI tooling, and AI-assisted analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: Multiple strategic verbs (design, own, build, contribute strategic input) indicate the role is expected to define direction and shape data strategy, not execute pre-scoped work.

**Run 3:** `strategic` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: Multiple strategic verbs (design, own, evolve) and explicit mention of contributing strategic input indicate the role is expected to set direction and shape analytics delivery, not execute others' priorities.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`
