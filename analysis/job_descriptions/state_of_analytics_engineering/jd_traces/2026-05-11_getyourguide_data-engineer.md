# Trace: 2026-05-11_getyourguide_data-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data Engineer, Traveler Data Engineering — GetYourGuide

**URL:** https://www.linkedin.com/jobs/view/data-engineer-traveler-data-engineering-at-getyourguide-4383493346/
**Location:** Berlin, Berlin, Germany
**Seniority Level:** Associate
**Employment Type:** Full-time

---

## Key Responsibilities

- Build end-to-end data solutions independently: Deliver reliable, high-quality datasets/pipelines
- Serve as a thought partner with Product and Data teams to translate business requirements
- Apply best practices in code quality, data modeling, testing, and monitoring
- Improve what's already in production: Pragmatically refactor and simplify existing pipelines
- Contribute to team planning, code reviews, and knowledge sharing
- Maintain balance between operational responsibilities and new development using team SLOs

---

## Required Qualifications

- 3+ years in a relevant data role with hands-on data engineering experience
- Expertise in SQL & Python, building robust data pipelines and data models
- Experience operating data at scale in warehouses/lakes (Delta, Snowflake, PostgreSQL/MySQL)
- Strong dbt proficiency and Spark familiarity
- Solid understanding of data visualization tools like Looker/Tableau
- Excellent English communication skills (written and verbal)
- Ability to prioritize effectively and manage stakeholders
- Proactive ownership mindset with customer orientation

---

## Preferred / Bonus Skills

- Experience delivering data solutions for marketplace platforms
- Customer journey and metric definition expertise
- Software engineering fundamentals (Java/Scala comfort level)
- AI-first mindset: Uses modern AI tools to boost productivity

---

## Benefits

- Annual personal growth budget and mentorship programs
- Remote work flexibility (30 days annually)
- Hybrid arrangement: three in-office days (Mon, Tue, Thur), two optional remote days
- Quarterly team events and yearly company-wide gatherings
- Monthly transportation and fitness budget
- GetYourGuide activity discounts
- Language reimbursement program
- Health and wellness benefits

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 3 | 2 | 2 | 1 | 33% | ✗ |
| data_team_maturity | mature | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | hiring_manager | mixed | recruiter | 0% | ✓ |
| stakeholder_orientation |  | internal_data | internal_data | product | 33% | ✗ |
| autonomy_level |  | execution | mixed | execution | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality standards, testing, monitoring, and best practices as core expectations, with no counterbalancing velocity or iteration signals.

**Run 2:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Multiple explicit rigour signals (testing, monitoring, code quality, best practices) with zero velocity language.

**Run 3:** `rigour` ✓
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: The responsibilities heavily emphasize correctness, quality, testing, and monitoring with no counterbalancing velocity language like fast-paced or rapid delivery.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: As a marketplace platform, data errors affect operational business decisions and Product priorities, but not regulatory compliance or financial reporting.

**Run 2:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: Marketplace platform role informs business decisions but lacks financial, compliance, or regulatory language indicating high-risk context.

**Run 3:** `moderate` ✓
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The role supports business decision-making in a marketplace platform context without explicit financial reporting, compliance, or regulatory requirements.

### collaboration_width
**Manual:** `3`

**Run 1:** `2` ✗
> Quote: "Product and Data teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names Product and Data teams as distinct collaborative partners.

**Run 2:** `2` ✗
> Quote: "Product and Data teams"
> Verified: ✓ found in JD
> Reasoning: Two named teams (Product, Data) explicitly listed as collaboration partners in responsibilities.

**Run 3:** `1` ✗
> Quote: "Product"
> Verified: ✓ found in JD
> Reasoning: Only Product is explicitly named as an external partner team; Data teams refers to the role holder's own function.

⚠ **Disagreement**: manual=`3` vs LLM majority=`2`

⚠ **LLM inconsistency**: runs gave ['2', '2', '1']

### data_team_maturity
**Manual:** `mature`

**Run 1:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: Existing production systems and operational responsibilities (SLOs) indicate an established data function beyond early stage, but the role focuses on a specialized sub-team rather than massive scale.

**Run 2:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: Explicitly references existing production infrastructure with ongoing improvement needs, characteristic of mid-stage teams with runway.

**Run 3:** `mid` ✗
> Quote: "Improve what's already in production: Pragmatically refactor and simplify existing pipelines"
> Verified: ✓ found in JD
> Reasoning: The existence of production pipelines and mature operational practices indicates an established data function, not early-stage greenfield work.

⚠ **Disagreement**: manual=`mature` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: Reference to SLOs and the balance between operational stability and new development shows specific operational knowledge only someone actively performing this role would include.

**Run 2:** `mixed` ✗
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Verified: ✓ found in JD
> Reasoning: Combines specific operational knowledge (SLOs, responsibility balance) with generic boilerplate like 'thought partner'.

**Run 3:** `recruiter` ✗
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Responsibilities use generic, boilerplate action verbs and best-practice language without technical specificity about tools, scale, or methodology.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Build end-to-end data solutions independently: Deliver reliable, high-quality datasets/pipelines"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building and maintaining data infrastructure and pipelines that internal consumers rely on, rather than directly serving business decisions or revenue functions.

**Run 2:** `internal_data` ✗
> Quote: "Apply best practices in code quality, data modeling, testing, and monitoring"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize data platform engineering and infrastructure quality over product analytics, commercial, or finance outcomes.

**Run 3:** `product` ✗
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The primary framing is translating and serving Product team requirements into data solutions, making Product the primary stakeholder.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

⚠ **LLM inconsistency**: runs gave ['internal_data', 'internal_data', 'product']

### autonomy_level
**Manual:** ``

**Run 1:** `execution` ✗
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The role receives and translates business requirements from Product, then executes solutions, rather than setting strategic direction for the analytics function.

**Run 2:** `mixed` ✗
> Quote: "Build end-to-end data solutions independently"
> Verified: ✓ found in JD
> Reasoning: Signals strategic domain ownership and independent decision-making, but constrained by team SLOs and business requirements established elsewhere.

**Run 3:** `execution` ✗
> Quote: "Serve as a thought partner with Product and Data teams to translate business requirements"
> Verified: ✓ found in JD
> Reasoning: The role executes on requirements defined externally by Product teams rather than setting strategic direction for the data function.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'execution']

### ai_role
**Run 1:** `none` ✓
> Quote: ""
> Reasoning: No mention of AI tools, AI-first mindset, or AI infrastructure responsibilities.

**Run 2:** `none` ✓
> Quote: ""
> Reasoning: No AI tools, GenAI responsibilities, or AI-ready infrastructure mentioned.

**Run 3:** `none` ✓
> Quote: ""
> Reasoning: No AI tools or GenAI responsibilities mentioned; standard data engineering work.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "best practices in code quality, data modeling, testing, and monitoring; Deliver reliable, high-quality datasets/pipelines"
> Reasoning: Testing and quality ownership implied through 'best practices' language and 'deliver reliable, high-quality' expectations; candidate owns solution quality.

**Run 2:** `responsibility` ✓
> Quote: "best practices in code quality, data modeling, testing, and monitoring; Deliver reliable, high-quality datasets/pipelines"
> Reasoning: Testing explicitly mentioned as best practice; delivery framed around high-quality outcomes showing ownership.

**Run 3:** `responsibility` ✓
> Quote: "best practices in code quality, data modeling, testing, and monitoring"
> Reasoning: Candidate owns testing and quality practices explicitly.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Reasoning: SLOs signal operational reliability and incident prevention concerns, but lack compliance/regulatory or data-trust framing.

**Run 2:** `moderate` ✓
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Reasoning: SLO-based framing indicates concern for operational reliability and incident prevention without compliance focus.

**Run 3:** `moderate` ✓
> Quote: "Maintain balance between operational responsibilities and new development using team SLOs"
> Reasoning: Operational reliability framing with SLO emphasis; pipeline stability concerns.

