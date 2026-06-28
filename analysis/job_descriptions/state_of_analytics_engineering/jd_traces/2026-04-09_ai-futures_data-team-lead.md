# Trace: 2026-04-09_ai-futures_data-team-lead

## JD text (fed to classifier, Layer B stripped)

```
# Data Team Lead — AI Futures

**URL:** https://www.linkedin.com/jobs/view/4398675612/
**Location:** Stuttgart Region (Hybrid)
**Seniority:** Mid-Senior level
**Employment Type:** Full-time

**Salary:** Base up to €130,000 + performance bonus up to 20%

---

## Key Responsibilities

- Designing and building a modern data platform for "high-volume, real-time vehicle and transaction data"
- Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner
- Building infrastructure that powers "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
- Growing and mentoring a data engineering team and contributing to hiring decisions
- Collaborating with OEM partners and external developers to productionise pipelines at pace

---

## Required Qualifications

- Proven experience building pipelines within modern data stacks such as data lakes, medallion architectures, or SQL-based platforms
- Strong Python skills across both high-code and low-code tooling
- Leadership experience or a genuine ambition to lead for the first time
- Microsoft ecosystem confidence including Power BI and Azure; Kafka or Spark experience is a strong plus
- Interest in automotive, IoT, or mobility data is highly desirable
- Professional-level German required

---

## Preferred / Bonus Skills

- Kafka or Spark experience
- Interest in automotive, IoT, or mobility data sectors
- Experience with RapidMiner or similar low-code data platforms

---

## Benefits

- Base salary: up to €130,000
- Performance bonus: up to 20%
- Equity and options package
- 30 days annual leave
- Private health insurance
- Learning & development budget
- Relocation support

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | velocity | rigour | velocity | rigour | 33% | ✗ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 2 | 0 | 2 | 2 | 33% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | hiring_manager | mixed | hiring_manager | 33% | ✗ |
| stakeholder_orientation |  | internal_data | product | internal_data | 33% | ✗ |
| autonomy_level |  | strategic | strategic | strategic | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `velocity`

**Run 1:** `rigour` ✗
> Quote: "Building infrastructure that powers 'AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Financial decisioning and high-volume real-time data handling emphasize reliability and correctness over speed.

**Run 2:** `velocity` ✓
> Quote: "Collaborating with OEM partners and external developers to productionise pipelines at pace"
> Verified: ✓ found in JD
> Reasoning: The only explicit value signal in the responsibilities section is 'productionise pipelines at pace', which emphasizes speed and delivery, with no corresponding rigour language like testing, governance, or accuracy.

**Run 3:** `rigour` ✗
> Quote: "Designing and building a modern data platform"
> Verified: ✓ found in JD
> Reasoning: The emphasis on designing a modern platform with specific architectural patterns (medallion architectures) indicates a rigour-oriented approach despite a single mention of 'at pace' in the production context.

⚠ **Disagreement**: manual=`velocity` vs LLM majority=`rigour`

⚠ **LLM inconsistency**: runs gave ['rigour', 'velocity', 'rigour']

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ✓ found in JD
> Reasoning: Explicit mention of payments and financial decisioning indicates direct financial impact of data errors.

**Run 2:** `high` ✓
> Quote: "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ✓ found in JD
> Reasoning: Data errors directly affect financial decisioning and payment processing, placing this squarely in high financial risk territory.

**Run 3:** `high` ✓
> Quote: "Building infrastructure that powers AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ⚠ NOT found verbatim
> Reasoning: Data errors directly impact pricing revenue, payments processing, and financial decisions, which carry immediate financial and potential regulatory consequences.

### collaboration_width
**Manual:** `2`

**Run 1:** `0` ✗
> Quote: "(none identified)"
> Verified: ⚠ NOT found verbatim
> Reasoning: No named internal partner functions (Finance, Product, Engineering teams, etc.) are identified; OEM partners and external developers are mentioned but do not meet the criteria of named internal teams or formally defined client/customer relationships.

**Run 2:** `2` ✓
> Quote: "OEM partners; external developers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct external collaboration partners are explicitly named in the JD.

**Run 3:** `2` ✓
> Quote: "OEM partners and external developers"
> Verified: ✓ found in JD
> Reasoning: Two distinct external partner groups are explicitly named as collaboration partners in the responsibilities.

⚠ **LLM inconsistency**: runs gave ['0', '2', '2']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: An existing team requiring growth and mentorship signals mid-stage maturity, not greenfield startup or a large established function.

**Run 2:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team"
> Verified: ✓ found in JD
> Reasoning: The existence of an already-formed team that is growing, combined with platform design/building work, indicates a mid-stage data function.

**Run 3:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: The team exists and is being expanded with specific modern architecture patterns already in place, indicating a growth phase rather than early-stage or fully mature.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Designing and building a modern data platform for 'high-volume, real-time vehicle and transaction data' using Python and low-code platforms such as RapidMiner"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical context with named tools, exact data volumes/characteristics, and use-case context indicates hands-on experience writing the role.

**Run 2:** `mixed` ✓
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: This shows technical specificity (Python, RapidMiner, ETL/ELT, connected vehicle domain), but other responsibilities like 'growing and mentoring' use generic action verbs.

**Run 3:** `hiring_manager` ✗
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: Specific tools (RapidMiner), named architecture patterns (medallion), technology stack details (Microsoft ecosystem, Kafka, Spark), and distinct collaboration context (OEM partners) indicate someone deeply familiar with the role wrote this.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Designing and building a modern data platform for 'high-volume, real-time vehicle and transaction data'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Role centers on platform and infrastructure design to serve data consumers and pipelines, rather than directly serving Finance, Product, or commercial teams.

**Run 2:** `product` ✗
> Quote: "Building infrastructure that powers AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ⚠ NOT found verbatim
> Reasoning: The infrastructure serves product and commercial decisions (pricing, payments, financial decisioning in the connected vehicle ecosystem), indicating a product-oriented audience.

**Run 3:** `internal_data` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: The primary responsibilities center on building the data platform and scaling the data engineering team itself, making the internal data function the main stakeholder rather than commercial or business functions.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

⚠ **LLM inconsistency**: runs gave ['internal_data', 'product', 'internal_data']

### autonomy_level
**Manual:** ``

**Run 1:** `strategic` ✗
> Quote: "Owning ETL and ELT pipeline development"
> Verified: ✓ found in JD
> Reasoning: The verbs 'designing', 'building', and 'owning' combined with team leadership indicate the role defines direction for the data platform domain rather than executing direction set by others.

**Run 2:** `strategic` ✗
> Quote: "Designing and building a modern data platform"
> Verified: ✓ found in JD
> Reasoning: The role is expected to design and build the data platform and lead a team, indicating strategic autonomy in defining the data function.

**Run 3:** `strategic` ✗
> Quote: "Designing and building a modern data platform for 'high-volume, real-time vehicle and transaction data'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The use of 'designing and building' combined with 'owning' ETL development indicates the role sets direction for platform strategy and architecture rather than executing work defined by others.

⚠ **Disagreement**: manual=`` vs LLM majority=`strategic`
