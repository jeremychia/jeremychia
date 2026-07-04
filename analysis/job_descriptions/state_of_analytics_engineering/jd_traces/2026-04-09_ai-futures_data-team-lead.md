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
| velocity_vs_rigour | velocity | rigour | rigour | velocity | 33% | ✗ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 2 | 2 | 2 | 1 | 33% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | mixed | hiring_manager | hiring_manager | hiring_manager | 100% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | strategic | strategic | strategic | strategic | 100% | ✓ |
| ai_role |  | ai_enabler | ai_enabler | ai_enabler | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `velocity`

**Run 1:** `rigour` ✗
> Quote: "Designing and building a modern data platform for "high-volume, real-time vehicle and transaction data""
> Verified: ✓ found in JD
> Reasoning: Infrastructure language emphasizing high-volume real-time platforms implies reliability and quality orientation; only one velocity signal ("at pace") is insufficient to override this.

**Run 2:** `rigour` ✗
> Quote: "Designing and building a modern data platform for "high-volume, real-time vehicle and transaction data""
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building robust infrastructure and data architecture for financial systems over speed, with "at pace" as a single velocity modifier in an otherwise infrastructure-focused narrative focused on architecture and ownership.

**Run 3:** `velocity` ✓
> Quote: "Collaborating with OEM partners and external developers to productionise pipelines at pace"
> Verified: ✓ found in JD
> Reasoning: The explicit 'at pace' language in the responsibilities indicates velocity focus, with no corresponding rigour signals like testing, quality, compliance, or governance.

⚠ **Disagreement**: manual=`velocity` vs LLM majority=`rigour`

⚠ **LLM inconsistency**: runs gave ['rigour', 'rigour', 'velocity']

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Building infrastructure that powers "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems""
> Verified: ✓ found in JD
> Reasoning: Explicit financial outcomes (pricing, payments, financial decisioning) indicate direct business and revenue impact.

**Run 2:** `high` ✓
> Quote: "Building infrastructure that powers "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems""
> Verified: ✓ found in JD
> Reasoning: Errors in payment and financial decisioning systems have direct regulatory and financial consequences, making data quality mission-critical.

**Run 3:** `high` ✓
> Quote: "Building infrastructure that powers 'AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems'"
> Verified: ⚠ NOT found verbatim
> Reasoning: Financial decisioning directly affects financial outcomes at scale, indicating a high-risk domain with potential for significant business impact.

### collaboration_width
**Manual:** `2`

**Run 1:** `2` ✓
> Quote: "OEM partners; external developers"
> Verified: ✓ found in JD
> Reasoning: Two distinct external partner groups explicitly named as collaboration partners.

**Run 2:** `2` ✓
> Quote: "OEM partners; external developers"
> Verified: ✓ found in JD
> Reasoning: Two distinct external collaboration groups are explicitly named in the responsibilities.

**Run 3:** `1` ✗
> Quote: "OEM partners"
> Verified: ✓ found in JD
> Reasoning: OEM partners are explicitly named as a collaboration partner in the responsibilities; external developers are mentioned but not as a distinct named team or function.

⚠ **LLM inconsistency**: runs gave ['2', '2', '1']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: Existence of a team to grow and scale indicates an established data function in growth phase, not early-stage.

**Run 2:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: The data team already exists and is expanding with modern infrastructure development, indicating a function beyond early stage but not yet fully mature at enterprise scale.

**Run 3:** `mid` ✗
> Quote: "Growing and mentoring a data engineering team and contributing to hiring decisions"
> Verified: ✓ found in JD
> Reasoning: The mention of an existing team to grow suggests the data function is established but in a growth phase, indicating a mid-stage organization.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: Specific tool selections, domain knowledge (OEM partners, connected vehicle ecosystems), and precise use case context show hands-on technical experience.

**Run 2:** `hiring_manager` ✗
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: The JD includes specific technical tool knowledge (RapidMiner, medallion architectures), domain-specific use cases (payments, financial decisioning), and business model understanding (OEM partnerships, vehicle data) only an SME would include.

**Run 3:** `hiring_manager` ✗
> Quote: "Owning ETL and ELT pipeline development using Python and low-code platforms such as RapidMiner"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about named tools, methodologies (ETL/ELT), data volumes ('high-volume, real-time'), and architectural patterns (medallion architectures, data lakes) indicates hands-on engineering experience.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`hiring_manager`

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "Designing and building a modern data platform"
> Verified: ✓ found in JD
> Reasoning: Primary focus is platform and infrastructure leadership; three of five responsibilities center on internal data function and team building.

**Run 2:** `internal_data` ✓
> Quote: "Designing and building a modern data platform for "high-volume, real-time vehicle and transaction data""
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and owning data infrastructure and platform components that internal teams and downstream AI systems consume.

**Run 3:** `internal_data` ✓
> Quote: "Designing and building a modern data platform for 'high-volume, real-time vehicle and transaction data'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary focus is building the data infrastructure and platform itself rather than serving a specific external function like sales, finance operations, or product analytics.

### autonomy_level
**Manual:** `strategic`

**Run 1:** `strategic` ✓
> Quote: "Designing and building a modern data platform; Owning ETL and ELT pipeline development"
> Verified: ✓ found in JD
> Reasoning: Verbs like "designing," "building," and "owning" indicate setting direction for both technology and team priorities.

**Run 2:** `strategic` ✓
> Quote: "Owning ETL and ELT pipeline development"
> Verified: ✓ found in JD
> Reasoning: The role uses strategic verbs (designing, owning, building, growing) and includes independent decision-making on team-building, hiring, and platform architecture.

**Run 3:** `strategic` ✓
> Quote: "Owning ETL and ELT pipeline development"
> Verified: ✓ found in JD
> Reasoning: The role uses strategic action verbs (designing, building, owning, growing, mentoring) that indicate the candidate will shape and define the data function's direction.

### ai_role
**Manual:** ``

**Run 1:** `ai_enabler` ✗
> Quote: "Building infrastructure that powers "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems""
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems consume and operate on.

**Run 2:** `ai_enabler` ✗
> Quote: "Building infrastructure that powers "AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems""
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure that AI systems consume, not to use AI coding tools for personal productivity.

**Run 3:** `ai_enabler` ✗
> Quote: "Building infrastructure that powers 'AI-driven pricing, payments, and financial decisioning across connected vehicle ecosystems'"
> Verified: ⚠ NOT found verbatim
> Reasoning: The candidate is expected to build data infrastructure that AI systems consume and run on, enabling AI-driven financial decision-making.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_enabler`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: No mention of testing, data quality, data contracts, observability, or SLOs anywhere in the JD.

**Run 2:** `absent` ✗
> Quote: "No testing or data quality signal in the JD."
> Verified: ⚠ NOT found verbatim
> Reasoning: There are no mentions of testing, data quality, data contracts, observability, or reliability frameworks in the responsibilities.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality practice mentioned in the responsibilities."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of testing, data contracts, observability, data quality, or related quality/reliability practices appears in the responsibilities section.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: JD is framed around capability building and delivery rather than risk management, compliance, or preventing bad outcomes.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed in delivery and capability terms (designing, building, growing) without explicit risk mitigation, compliance, or reliability language despite the high-risk financial domain.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role in terms of building capabilities and leading the team with no emphasis on preventing bad outcomes, compliance, regulatory concerns, or stakeholder trust.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
