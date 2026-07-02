# Trace: 2026-07-02_sii-poland_data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data Analytics Engineer (f/m/x) — Sii Poland

**URL:** https://sii.pl/en/job-ads/id/37337/?sii_source=10#apply-contact-form
**Location:** Poland (Remote/Hybrid/Office)
**Date Posted:** 2026-07-02

---

# Data Analytics Engineer (f/m/x) - Senior Level

Company: Sii Poland
Location: Multiple locations in Poland (Remote, Hybrid, or Office options available)
Salary: Not stated

## Overview
Sii is recruiting an Analytics Engineer for a strategic fintech project based in Copenhagen. The role involves building and scaling critical data models that support decision-making across credit, payments, and fraud/AML domains.

## Key Responsibilities
- Build and maintain core data models using dbt for critical reporting
- Partner with stakeholders, Data Engineers, and Analysts on requirements
- Work collaboratively across technical and non-technical teams
- Contribute to the semantic layer (LookML) for consistent reporting
- Ensure data quality through testing, monitoring, and documentation
- Support reliable data workflows using orchestration tools like Airflow
- Uphold analytics engineering practices including code reviews
- Balance work across multiple data domains with adaptability

## Requirements
Must-Have:
- Min. 5 years of hands-on experience with dbt and modern cloud data warehouses (BigQuery)
- SQL proficiency and experience with layered model architecture
- Ability to translate unclear business requirements into clean solutions
- Git-based workflows and CI/CD familiarity
- Strong ownership mindset for business-critical data
- Comfort in high engineering/governance standard environments
- English language proficiency
- Fluent Polish required and residence in Poland mandatory

Nice-to-Have:
- Apache Airflow experience
- AML domain knowledge

## Tech Stack
Required: dbt, SQL, Git, BigQuery, LookML, Looker, Data Governance, Data Modeling
Optional: Apache Airflow, AML

Job no. JOB-22E63

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | high | high | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | hiring_manager | 33% |
| stakeholder_orientation | finance | internal_data | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | high | moderate | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (testing, data quality, documentation, code reviews, governance standards) with no velocity language present.

**Run 2:** `rigour`
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, testing, monitoring, governance standards, and code reviews with no velocity or shipping language, marking this as clearly rigour-oriented.

**Run 3:** `rigour`
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, testing, monitoring, documentation, CI/CD, and governance as core expectations with no countervailing speed or delivery-focused signals.

### domain_risk

**Run 1:** `high`
> Quote: "strategic fintech project based in Copenhagen. The role involves building and scaling critical data models that support decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: Explicit fintech sector and fraud/AML regulatory domain directly indicate financial and compliance risk.

**Run 2:** `high`
> Quote: "critical data models that support decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: The fintech sector combined with credit, payments, and fraud/AML domains—all regulated financial and compliance areas—creates high financial and regulatory risk from data errors.

**Run 3:** `high`
> Quote: "critical data models that support decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: Fintech with explicit regulatory domains (AML is regulated compliance, payments and credit are financial) means data errors directly expose the organization to regulatory and financial consequences.

### collaboration_width

**Run 1:** `2`
> Quote: "Data Engineers, and Analysts"
> Verified: ✓ found in JD
> Reasoning: Two explicitly named partner functions (Data Engineers and Analysts) identified as collaboration partners.

**Run 2:** `2`
> Quote: "Data Engineers; Analysts"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two named partner teams are identified: Data Engineers and Analysts, both explicitly listed as collaboration partners in the responsibilities section.

**Run 3:** `2`
> Quote: "Partner with stakeholders, Data Engineers, and Analysts on requirements"
> Verified: ✓ found in JD
> Reasoning: Two distinct named teams are explicitly identified as collaboration partners: Data Engineers and Analysts.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Uphold analytics engineering practices including code reviews"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, LookML, Airflow) and established practices like code reviews indicate a functioning team with infrastructure, but no evidence of multiple specialized sub-teams.

**Run 2:** `mid`
> Quote: "Build and maintain core data models using dbt for critical reporting"
> Verified: ✓ found in JD
> Reasoning: Multiple named tools in responsibilities (dbt, LookML, Airflow) with specific application context indicate an established data function with infrastructure in place, not a greenfield build.

**Run 3:** `mid`
> Quote: "Build and maintain core data models using dbt for critical reporting"
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, LookML, Airflow) combined with multiple team mentions indicate an established function growing and scaling, not greenfield or highly mature.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Build and maintain core data models using dbt for critical reporting"
> Verified: ✓ found in JD
> Reasoning: Specific technical context (dbt models, LookML, credit/payments/fraud/AML domains, semantic layer, code reviews) demonstrates hands-on understanding of the actual work.

**Run 2:** `mixed`
> Quote: "Build and maintain core data models using dbt for critical reporting; Ensure data quality through testing, monitoring, and documentation"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains specific technical context (named tools with application domains: credit/payments/fraud-AML, data quality frameworks) alongside generic phrases like 'work collaboratively across technical and non-technical teams', indicating mixed hiring manager and recruiter input.

**Run 3:** `hiring_manager`
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting; Support reliable data workflows using orchestration tools like Airflow"
> Verified: ⚠ NOT found verbatim
> Reasoning: The specific technical context (LookML semantic layer architecture, Airflow orchestration, layered model architecture, BigQuery) reflects hands-on knowledge that only comes from someone who has done this role.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `finance`
> Quote: "support decision-making across credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: The domains served (credit, payments, fraud/AML) are all finance and risk functions, indicating the primary business audience is finance and risk decision-makers.

**Run 2:** `internal_data`
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: The immediate partners are Data Engineers and Analysts, and the core work is building and maintaining the modelling layer and semantic infrastructure, making the primary audience the data function itself.

**Run 3:** `internal_data`
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves internal data consumers and the data platform itself—building models and infrastructure that downstream analytics teams use—not external business functions.

⚠ **LLM inconsistency**: runs gave ['finance', 'internal_data', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: The verbs 'contribute to' and 'support' indicate the role executes on systems and priorities defined by stakeholders rather than setting strategic direction.

**Run 2:** `execution`
> Quote: "Contribute to the semantic layer (LookML) for consistent reporting"
> Verified: ✓ found in JD
> Reasoning: The verbs are 'contribute', 'partner', 'support', and 'maintain'—all reactive/execution-oriented—with no strategic direction-setting or ownership framing, indicating the role executes against established priorities.

**Run 3:** `execution`
> Quote: "Support reliable data workflows using orchestration tools like Airflow"
> Verified: ✓ found in JD
> Reasoning: Responsibilities are dominated by execution verbs (partner, contribute, support, uphold) rather than strategic direction-setting verbs, indicating the role delivers within established practices and defined domains.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI tools, skills, or capabilities expected of the candidate anywhere in the JD.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD does not mention AI coding tools, agentic workflows, or any expectation for AI-assisted work; the candidate is not expected to demonstrate AI skills.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: No mention of AI coding tools, GenAI, AI-assisted workflows, or AI data infrastructure anywhere in the JD.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The action verb 'Ensure' indicates the candidate owns and is accountable for testing and data quality practices, not just using tools.

**Run 2:** `responsibility`
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The phrase uses the ownership verb 'Ensure' with data quality as the outcome, framing testing as the candidate's responsibility for maintaining quality, not just a tool in the tech stack.

**Run 3:** `responsibility`
> Quote: "Ensure data quality through testing, monitoring, and documentation"
> Verified: ✓ found in JD
> Reasoning: The ownership verb 'Ensure' combined with explicit testing and data quality practices makes this a responsibility the candidate owns, not a tool listed in requirements.

### loss_aversion_framing

**Run 1:** `high`
> Quote: "Strong ownership mindset for business-critical data; Comfort in high engineering/governance standard environments"
> Verified: ⚠ NOT found verbatim
> Reasoning: Repeated emphasis on business-critical data, fraud/AML regulatory domain, and governance standards indicate the role is framed around preventing serious data errors and compliance failures.

**Run 2:** `moderate`
> Quote: "Strong ownership mindset for business-critical data; Comfort in high engineering/governance standard environments"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role emphasizes business-criticality and governance standards reflecting concern for reliability and engineering practices, but the primary framing remains delivery-oriented ('Build and maintain', 'Support') rather than compliance or regulatory-risk dominated.

**Run 3:** `moderate`
> Quote: "credit, payments, and fraud/AML domains"
> Verified: ✓ found in JD
> Reasoning: While the fintech sector and explicit AML (regulated) domain imply high consequences for failure, the JD frames the role around engineering excellence and data quality standards rather than regulatory compliance or risk prevention.

⚠ **LLM inconsistency**: runs gave ['high', 'moderate', 'moderate']
