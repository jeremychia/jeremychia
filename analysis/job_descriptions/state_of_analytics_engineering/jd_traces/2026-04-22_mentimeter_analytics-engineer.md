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
| collaboration_width | 4 | 0 | 0 | 3 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | recruiter | mixed | mixed | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | mixed | 33% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | ai_user | ai_user | ai_user | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | none | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize standards, documentation, and data catalogs as core expectations, with no mention of speed, iteration, or delivery pace.

**Run 2:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Emphasis on governance, standards, and documentation with no velocity language signals a rigour-focused orientation.

**Run 3:** `rigour` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes standards, documentation, data catalogs, maintainability, and GDPR compliance over speed or iteration, framing the role around quality and governance.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: GDPR signals regulatory awareness, but the JD lacks financial reporting, compliance, or audit language that would indicate high domain risk typical of fintech or banking.

**Run 2:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is a stated requirement indicating moderate risk, but the role lacks explicit financial reporting or regulatory framing that would elevate it to high.

**Run 3:** `moderate` ✓
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: While the JD signals regulatory data sensitivity, Mentimeter is a SaaS company with data privacy concerns rather than a financial reporting or regulatory compliance context, making errors recoverable rather than mission-critical.

### collaboration_width
**Manual:** `4`

**Run 1:** `0` ✗
> Quote: "Partner with business and technical stakeholders from problem framing to shipped artefacts"
> Verified: ✓ found in JD
> Reasoning: The JD refers to stakeholders generically rather than naming specific functions like Finance, Product, Engineering, or Sales.

**Run 2:** `0` ✗
> Quote: "Partner with business and technical stakeholders from problem framing to shipped artefacts"
> Verified: ✓ found in JD
> Reasoning: Collaboration is framed generically as 'stakeholders' without naming specific partner teams like Sales, Marketing, Engineering, or Data Science.

**Run 3:** `3` ✗
> Quote: "Business acumen covering sales, marketing, and product analytics"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct business functions (Sales, Marketing, and Product) that the candidate must understand, indicating collaboration across these teams.

⚠ **Disagreement**: manual=`4` vs LLM majority=`0`

⚠ **LLM inconsistency**: runs gave ['0', '0', '3']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: The verb 'evolve' indicates existing models and infrastructure being improved, plus standards and catalogs under construction, suggesting mid-stage growth beyond greenfield.

**Run 2:** `mid` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Emphasis on formalizing standards and architecture across the organization signals a maturing data function with existing infrastructure being standardized rather than built from zero.

**Run 3:** `mid` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: The language of evolving existing models and formalizing standards suggests a data function with foundation and early tools that is now scaling and professionalizing.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `recruiter` ✗
> Quote: "Contribute strategic input around data modeling, BI tooling, and AI-assisted analytics"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic, vague action verbs without specific technical context about tools, scale, methodology, or business impact that would indicate hiring manager authorship.

**Run 2:** `mixed` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: Technical specificity in data modeling and architecture responsibilities mixed with boilerplate language like 'Partner with stakeholders' and 'Help the organization interpret data' indicates both hiring-manager and recruiter input.

**Run 3:** `mixed` ✗
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: Technical specificity appears in data modeling architecture and semantic layer requirements alongside generic collaboration language like partner with stakeholders.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['recruiter', 'mixed', 'mixed']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Primary responsibilities focus on building data infrastructure, modeling architecture, and organizational standards rather than serving commercial, product, or finance stakeholders.

**Run 2:** `internal_data` ✓
> Quote: "Build standards, documentation, and data catalogs for the organization"
> Verified: ✓ found in JD
> Reasoning: Primary responsibilities emphasize data infrastructure and platform work serving internal data consumers and the data function rather than commercial, product, or finance teams.

**Run 3:** `mixed` ✗
> Quote: "Business acumen covering sales, marketing, and product analytics"
> Verified: ✓ found in JD
> Reasoning: The qualifications equally emphasize both commercial functions (sales, marketing) and product analytics, indicating the role serves both commercial and product stakeholders.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'mixed']

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: The opening responsibility uses 'own' and 'design' in relation to core data architecture, establishing strategic ownership of this central domain.

**Run 2:** `strategic` ✓
> Quote: "Design, own, and evolve core data models and the modelling architecture"
> Verified: ✓ found in JD
> Reasoning: Strategic verbs 'Design', 'own', and 'evolve' indicate the role sets direction for data architecture and shapes organizational analytics practices rather than executing predefined work.

**Run 3:** `strategic` ✓
> Quote: "Contribute strategic input around data modeling, BI tooling, and AI-assisted analytics"
> Verified: ✓ found in JD
> Reasoning: The role owns data architecture and contributes strategic direction on tools rather than executing on priorities defined by others.

### ai_role
**Manual:** ``

**Run 1:** `ai_user` ✗
> Quote: "Experience using AI-assisted coding or coding agents in a disciplined way (reviews, tests, documentation)"
> Verified: ✓ found in JD
> Reasoning: The preferred qualifications explicitly ask candidates to demonstrate prior hands-on experience using AI coding tools to accelerate their own work.

**Run 2:** `ai_user` ✗
> Quote: "Experience using AI-assisted coding or coding agents in a disciplined way (reviews, tests, documentation)"
> Verified: ✓ found in JD
> Reasoning: Preferred skills explicitly expect candidates to have proven experience using AI coding tools and agents, positioning them as personal productivity accelerators.

**Run 3:** `ai_user` ✗
> Quote: "Experience using AI-assisted coding or coding agents in a disciplined way (reviews, tests, documentation)"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI-assisted coding tools to accelerate their own work, not to build data infrastructure that AI systems consume.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: While 'tests' appears in the context of reviewing AI-assisted code output, there are no signals about data quality frameworks, dbt tests, data contracts, or observability practices.

**Run 2:** `absent` ✗
> Quote: "No data quality, testing frameworks, or data contract signals in JD"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data quality, testing standards, observability, or data contracts are not mentioned in responsibilities; the word 'tests' appears only in the context of disciplined AI usage practices.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality framework mentioned in the JD"
> Verified: ⚠ NOT found verbatim
> Reasoning: While standards and documentation are emphasized, the JD does not explicitly mention testing frameworks, data contracts, or ownership of data quality practices.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is mentioned as a required qualification, signaling regulatory awareness and operational risk, but the role framing emphasizes design and delivery rather than prevention of bad outcomes.

**Run 2:** `moderate` ✗
> Quote: "Experience working with GDPR-sensitive data"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is acknowledged as a skill requirement indicating moderate concern for governance, but the role is primarily delivery-focused (design, own, build) with compliance secondary to capability.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed in capability and delivery terms (design, own, build, contribute) with no explicit emphasis on preventing bad outcomes or mitigating compliance risk.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`

⚠ **LLM inconsistency**: runs gave ['moderate', 'moderate', 'none']
