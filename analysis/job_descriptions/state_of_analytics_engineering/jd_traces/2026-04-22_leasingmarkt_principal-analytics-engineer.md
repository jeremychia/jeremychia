# Trace: 2026-04-22_leasingmarkt_principal-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Principal Analytics Engineer (m/f/d) — LeasingMarkt.de (AutoScout24 Group)

**URL:** https://www.linkedin.com/jobs/view/4404307253/
**Location:** Berlin, Germany
**Salary:** Not listed

---

## Key Responsibilities

- Define and evolve the architecture for enterprise analytical models with a strong focus on scalability, clarity and long-term robustness
- Design and maintain advanced semantic layers to unify KPIs and analytical logic across business domains
- Set technical direction and drive adoption of modern modeling practices across the organization
- Lead the definition and implementation of AI-driven analytical capabilities, including text-to-SQL, automated insights, semantic modeling for AI and conversational analytical interfaces
- Develop modeling patterns, documentation standards, and workflows for analytical efficiency
- Partner with data platform, engineering, and analytics teams on high-performance pipelines
- Optimise AWS cloud-native services (Glue, Athena, S3, MWAA) to support scalable analytical and AI workloads
- Enhance modeling patterns, performance, and development processes
- Mentor analytics engineers and analysts on modeling skills and technical standards
- Deliver high-quality semantic assets that fuel self-service analytics, reporting and AI-powered insights

---

## Required Qualifications

- 7+ years in advanced analytics engineering or data engineering roles
- Strong stakeholder influence and architectural alignment abilities
- Leadership experience on complex data initiatives
- Experience with AI-driven analytics (text-to-SQL, automated insights, semantic modeling, conversational BI)
- Extensive hands-on expertise with AWS (Glue, Athena, S3, MWAA) and familiarity with BigQuery
- Expert-level Python and PySpark skills
- Expert-level SQL and dimensional modeling mastery
- Data privacy, security, and compliance knowledge
- Large dataset optimization and performance troubleshooting capabilities

---

## Preferred Qualifications

Not explicitly listed

---

## Benefits

- International work community with 50+ nationalities represented
- Inclusive workplace culture
- Tools, training, and support for flexible work arrangements
- Learning and skill development opportunities

---

## Behavioural Insights (Hiring Manager Priorities)

### Primacy Bias
Opens with **"Define and evolve architecture for enterprise analytical models"** → they need **architectural thinking and systems design**, not operational reporting. Resume must lead with semantic layer design and multi-domain thinking.

### Repetition Signals (Fear & Desire)
| Term | Count | Type | Signal |
|------|-------|------|--------|
| "semantic layers" / "semantic assets" | 3x | Desire | Struggling with fragmented KPI logic; need unified semantic model |
| "AI-driven analytics" / "AI capabilities" | 2x | Desire | Building AI-ready analytics as competitive advantage |
| "scalability" / "performance" / "optimisation" | 3x | Fear | Past scaling pain; need performance-first thinking |
| "robustness" / "high-quality" / "governance" / "standards" | 4x | Loss aversion | Burned by bad data/reliability issues; governance > speed |
| "mentoring" / "adoption" / "leadership" | 3x | Seniority | Autonomous principal IC, not a manager; influence-driven |

### Seniority Level
Language is **directive and autonomous**: "Set technical direction", "Define and evolve", "Lead the definition", "Drive adoption". This is a **principal IC role** — someone who drives change through expertise and influence, not authority.

### Loss Aversion Framing
Multiple governance/reliability signals indicate past incidents. Frame achievements as **risk reduction and reliability wins**, not just speed. €1.6m recovery and 90% risk mitigation are the right narrative.

### What's Absent (Equally Important)
- **No dashboards/BI tools mentioned** → focus on infrastructure and modeling, not visualization
- **No cost optimization** → building new capabilities, not squeezing budgets
- **No project m…[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 4 | 3 | 3 | 3 | 100% | ✗ |
| data_team_maturity | mid | mid | mid | mature | 33% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Define and evolve the architecture for enterprise analytical models with a strong focus on scalability, clarity and long-term robustness"
> Verified: ✓ found in JD
> Reasoning: The opening responsibility emphasizes architectural rigor, scalability, clarity, and long-term robustness as core expectations, with no corresponding velocity signals throughout the JD.

**Run 2:** `rigour` ✓
> Quote: "Define and evolve the architecture for enterprise analytical models with a strong focus on scalability, clarity and long-term robustness"
> Verified: ✓ found in JD
> Reasoning: The opening responsibility emphasizes 'long-term robustness' and architectural clarity over speed, with no velocity language present throughout the JD.

**Run 3:** `rigour` ✓
> Quote: "strong focus on scalability, clarity and long-term robustness"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes architectural durability, standards, governance, and reliability over speed, with no velocity signals present.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Data privacy, security, and compliance knowledge"
> Verified: ✓ found in JD
> Reasoning: While the automotive leasing domain has regulatory considerations, the JD frames compliance generically without explicit reference to financial reporting, regulatory bodies, or mission-critical systems—characteristic of moderate-risk business intelligence roles.

**Run 2:** `moderate` ✓
> Quote: "Data privacy, security, and compliance knowledge"
> Verified: ✓ found in JD
> Reasoning: While the automotive leasing finance domain implies moderate financial risk, the JD lacks explicit regulatory or financial reporting language, making this a compliance-aware but not high-risk classification.

**Run 3:** `moderate` ✓
> Quote: "Data privacy, security, and compliance knowledge"
> Verified: ✓ found in JD
> Reasoning: While automotive leasing is a financial domain, the JD does not explicitly invoke financial reporting or regulatory drivers that would elevate it to high risk.

### collaboration_width
**Manual:** `4`

**Run 1:** `3` ✗
> Quote: "data platform; engineering; analytics"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names three partner teams in 'Partner with data platform, engineering, and analytics teams' without listing additional named functions or role cohorts.

**Run 2:** `3` ✗
> Quote: "Partner with data platform, engineering, and analytics teams on high-performance pipelines"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams are explicitly identified: data platform, engineering, and analytics.

**Run 3:** `3` ✗
> Quote: "Partner with data platform, engineering, and analytics teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named team functions are explicitly referenced: data platform, engineering, and analytics.

⚠ **Disagreement**: manual=`4` vs LLM majority=`3`

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Mentor analytics engineers and analysts on modeling skills and technical standards"
> Verified: ✓ found in JD
> Reasoning: The explicit mention of multiple analytics engineers and analysts as mentees, combined with named tools (AWS Glue, Athena, S3, MWAA) in active use, indicates an established data function with multiple roles that is growing and evolving, characteristic of a mid-stage team.

**Run 2:** `mid` ✓
> Quote: "Partner with data platform, engineering, and analytics teams on high-performance pipelines"
> Verified: ✓ found in JD
> Reasoning: Multiple established teams and roles (analytics engineers, analysts, data platform) exist with named AWS infrastructure in place, indicating growth-stage maturity rather than early-stage or fully mature.

**Run 3:** `mature` ✗
> Quote: "Partner with data platform, engineering, and analytics teams on high-performance pipelines"
> Verified: ✓ found in JD
> Reasoning: Multiple named data sub-teams with implied distinct charters, governance focus, and principal IC mentoring role indicate an established, scaled data function.

⚠ **LLM inconsistency**: runs gave ['mid', 'mid', 'mature']

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "Lead the definition and implementation of AI-driven analytical capabilities, including text-to-SQL, automated insights, semantic modeling for AI and conversational analytical interfaces"
> Verified: ✓ found in JD
> Reasoning: The specific mention of precise AI-driven capabilities—text-to-SQL, semantic modeling for AI, conversational analytical interfaces—alongside exact AWS service names (Glue, Athena, S3, MWAA) and requirements for 'Expert-level SQL and dimensional modeling mastery' reflect hands-on technical expertise only a hiring manager with direct experience in this domain would specify.

**Run 2:** `hiring_manager` ✓
> Quote: "Optimise AWS cloud-native services (Glue, Athena, S3, MWAA) to support scalable analytical and AI workloads"
> Verified: ✓ found in JD
> Reasoning: The JD demonstrates technical specificity only a hiring manager would have: exact AWS service names with contextualized usage, specific AI capability names (text-to-SQL, automated insights, conversational analytical interfaces), and architectural concepts like semantic layers for unified KPI logic.

**Run 3:** `hiring_manager` ✓
> Quote: "Optimise AWS cloud-native services (Glue, Athena, S3, MWAA) to support scalable analytical and AI workloads"
> Verified: ✓ found in JD
> Reasoning: Exact AWS service names (not generic 'AWS experience') and specific AI capabilities (text-to-SQL, automated insights, semantic modeling) indicate technical hiring manager authorship with practitioner-level knowledge.
