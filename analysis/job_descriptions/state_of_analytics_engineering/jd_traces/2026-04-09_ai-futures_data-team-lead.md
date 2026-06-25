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
| velocity_vs_rigour | velocity | rigour | velocity | velocity | 33% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 2 | 1 | 2 | 2 | 33% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | hiring_manager | mixed | mixed | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `velocity`

**Run 1:** `rigour` ✗
> Quote: "Building infrastructure that powers "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems""
> Verified: ✓ found in JD
> Reasoning: Financial decisioning and high-volume, real-time data requirements imply rigour-oriented infrastructure needs; the single "at pace" reference is subordinate to the core emphasis on building reliable infrastructure.

**Run 2:** `velocity` ✓
> Quote: "to productionise pipelines at pace"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasise shipping and building infrastructure with explicit 'at pace' language, with no rigour signals around testing, quality, or governance despite the criticality of the work.

**Run 3:** `velocity` ✓
> Quote: "productionise pipelines at pace"
> Verified: ✓ found in JD
> Reasoning: The only explicit orientation signal in the responsibilities is 'at pace', which emphasizes delivery pace; there are no explicit rigour signals like 'quality', 'testing', 'compliance', or 'governance'.

⚠ **LLM inconsistency**: runs gave ['rigour', 'velocity', 'velocity']

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ✓ found in JD
> Reasoning: Pricing and payment decisions directly impact revenue and customer financial outcomes; errors cascade through financial systems and customer trust.

**Run 2:** `high` ✓
> Quote: "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ✓ found in JD
> Reasoning: Explicit financial application (pricing, payments, financial decisioning) indicates high risk, where data errors directly affect financial systems and business decisions.

**Run 3:** `high` ✓
> Quote: "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems"
> Verified: ✓ found in JD
> Reasoning: Data errors directly affect financial transactions and automated pricing/decisioning, both of which have explicit financial consequences.

### collaboration_width
**Manual:** `2`

**Run 1:** `1` ✗
> Quote: "OEM partners"
> Verified: ✓ found in JD
> Reasoning: Only OEM partners are explicitly named as a distinct collaboration partner; the data engineering team is the role holder's own team (excluded by rule); external developers is too generic to count as a named function.

**Run 2:** `2` ✓
> Quote: "OEM partners and external developers"
> Verified: ✓ found in JD
> Reasoning: Two explicitly named collaboration partners are identified in the context of productionising pipelines.

**Run 3:** `2` ✓
> Quote: "OEM partners; external developers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct external parties are explicitly named as collaboration partners in the responsibilities.

⚠ **LLM inconsistency**: runs gave ['1', '2', '2']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: The phrasing "growing" an existing team indicates an established data function with defined roles undergoing expansion, not an early-stage startup or a mature scaled organization.

**Run 2:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: An existing data engineering team is being grown rather than built from scratch, and named tools (RapidMiner, medallion architectures) appear in responsibilities, indicating an established function expanding rather than forming.

**Run 3:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team"
> Verified: ✓ found in JD
> Reasoning: The team already exists and is growing, indicating mid-stage maturity—past the founding phase (early) but without signals of massive scale or multiple specialised sub-teams (mature).

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: The specific mention of RapidMiner by name and references to medallion architectures and Kafka/Spark context indicate technical knowledge from someone performing this work, not recruiter boilerplate.

**Run 2:** `mixed` ✓
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner; Designing and building a modern data platform for 'high-volume, real-time vehicle and transaction data'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific tools, architectural patterns (medallion architectures), and domain context (vehicle data, financial decisioning) reflect hiring-manager knowledge, but generic leadership phrasing ('growing and mentoring', 'collaborating') suggests recruiter input.

**Run 3:** `mixed` ✓
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: The JD includes specific tools, domain context, and methodology but lacks scale numbers and uses generic action verbs ('Owning', 'Building', 'Collaborating'), indicating a mix of technical specificity and recruiter-style boilerplate.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']
