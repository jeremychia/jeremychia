# Trace: 2026-04-22_qasa_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — Qasa

**URL:** https://careers.qasa.se/jobs/7452878-analytics-engineer-build-qasa-s-data-foundation
**Location:** Stockholm, Sweden (Hybrid)

---

## Key Responsibilities

- Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams
- Design and construct data models serving as the bridge between raw data and business insights
- Create self-serve analytics capabilities that empower teams to independently answer questions
- Transform complex data into compelling narratives informing product strategy and financial planning
- Partner with engineering to ensure data pipelines meet organizational needs
- Implement data governance protocols addressing GDPR compliance and access management
- Explore forecasting, modeling, and machine learning opportunities

---

## Required Qualifications

- Advanced SQL proficiency and data modeling expertise
- Demonstrated success designing and maintaining production data models
- Track record defining KPIs with consistent metric standards across organizations
- Strong analytical abilities paired with clear data communication skills
- Experience implementing BI tools (Metabase preferred)
- Cross-functional collaboration experience
- Business acumen across product, marketing, and finance domains
- Familiarity with AI-assisted development tools

---

## Preferred / Bonus Skills

- Amplitude and GA4 platform experience
- Data product deployment background
- GDPR and data governance legal knowledge

---

## Benefits

- 30 paid vacation days
- Pension contributions (ITP1 formula-based)
- Salary exchange program with 6% employer top-up
- Parental benefits (10% salary for 2-6 months)
- Annual wellness allowance: SEK 5,000
- Equipment provision (laptop, phone)
- Södermalm office location with Friday social events

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | high | high | 33% | ✗ |
| collaboration_width | 5 | 6 | 6 | 6 | 100% | ✗ |
| data_team_maturity | early | mid | early | mid | 33% | ✗ |
| jd_authorship | recruiter | hiring_manager | hiring_manager | mixed | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, compliance, and data quality through GDPR protocols and data governance, with no velocity signals like 'fast-paced' or 'ship quickly'.

**Run 2:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize governance, compliance, standardization, and data quality as core expectations, with no language around speed or iteration.

**Run 3:** `rigour` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, compliance, and standardization of KPIs and terminology across teams with no velocity signals like "fast-paced" or "move quickly."


⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Transform complex data into compelling narratives informing product strategy and financial planning"
> Verified: ✓ found in JD
> Reasoning: Data errors affect business decisions about product strategy and financial planning, but there is no explicit language about financial reporting, regulatory compliance risk, or P&L impact.

**Run 2:** `high` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly uses regulatory compliance language (GDPR), which per the classification criteria indicates a high-risk domain.

**Run 3:** `high` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance is an explicit regulatory requirement where data infrastructure failures have direct legal and financial consequences.

⚠ **Disagreement**: manual=`moderate` vs LLM majority=`high`

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'high']

### collaboration_width
**Manual:** `5`

**Run 1:** `6` ✗
> Quote: "Product; Marketing; Finance; Support; Country Management; engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct named functions are explicitly identified in the responsibilities: Product, Marketing, Finance, Support, Country Management, and Engineering.

**Run 2:** `6` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Partner with engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct named teams (Product, Marketing, Finance, Support, Country Management, and engineering) are explicitly listed as collaboration partners.

**Run 3:** `6` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams; Partner with engineering"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct named teams are explicitly identified: Product, Marketing, Finance, Support, Country Management, and Engineering.

⚠ **Disagreement**: manual=`5` vs LLM majority=`6`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The focus on establishing unified standards and building capabilities across multiple established business teams suggests a growing data function within an already-structured organization, not a greenfield build.

**Run 2:** `early` ✓
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The primary verb 'establish' signals the data function is building foundational KPIs and terminology rather than scaling or improving existing operations.

**Run 3:** `mid` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: Multiple established teams requiring KPI unification and standardization indicates existing infrastructure needing professionalization, not a from-zero build or mature specialized operation.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

⚠ **LLM inconsistency**: runs gave ['mid', 'early', 'mid']

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `hiring_manager` ✗
> Quote: "Establish unified KPIs and terminology across Product, Marketing, Finance, Support, and Country Management teams"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific organizational knowledge (named teams, specific governance requirements like GDPR, specific tool preferences like Metabase and Amplitude) that demonstrates hands-on familiarity with the role.

**Run 2:** `hiring_manager` ✗
> Quote: "Design and construct data models serving as the bridge between raw data and business insights"
> Verified: ✓ found in JD
> Reasoning: The specific technical methodology (data modeling as a bridge), clear business context, and technical depth indicate someone with analytics engineering experience wrote this rather than generic recruiter language.

**Run 3:** `mixed` ✗
> Quote: "Implement data governance protocols addressing GDPR compliance and access management"
> Verified: ✓ found in JD
> Reasoning: Specific hiring-manager knowledge (GDPR governance, Metabase tool specificity, named teams) coexists with recruiter boilerplate like "Transform complex data into compelling narratives" elsewhere in the responsibilities.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`hiring_manager`

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']
