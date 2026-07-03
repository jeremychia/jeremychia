# Trace: 2026-07-02_ijsvogel-retail_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer — IJsvogel Retail (Pets Place Boerenbond)

**URL:** https://werkenbij.ijsvogelretail.nl/vacature-hoofdkantoor/analytics-engineer
**Location:** Ede, Netherlands
**Date Posted:** 2026-07-02
**Salary:** 3,800–6,200 EUR

---

# Analytics Engineer

Company: Pets Place Boerenbond (part of IJsvogel Retail)
Job Title: Analytics Engineer
Location: Netherlands (headquarters in Ede)
Salary: EUR 3800 - EUR 6200 per month (fulltime basis)

## Key Responsibilities
The role involves translating business questions into dashboards and data solutions. The engineer designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance including GDPR compliance. The position also includes resolving pipeline issues and promoting data-driven culture across the organization.

## Requirements
Candidates need HBO+ education level and 3-5 years in similar roles. Essential skills include cloud platform experience (Google Cloud Platform/BigQuery preferred), SQL and Python programming, dbt expertise, and BI tools knowledge (preferably Looker). Understanding data architecture, governance, privacy regulations, and retail processes is required, plus interest in advanced analytics and AI applications.

## Additional Information
Contact: Stef van Hoek, Lead Data (06-42997509)
Benefits: 25 vacation days, remote work options (minimum 3 office days), travel reimbursement, 15% employee discount, and Alleo app access
Note: Acquisition approaches discouraged

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 0 | 0 | 0 | 0 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | mixed | recruiter | 33% | ✗ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | mixed | execution | execution | execution | 100% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality, governance, and compliance as core expectations rather than speed or delivery pace.

**Run 2:** `rigour` ✓
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The responsibilities explicitly emphasise data quality, governance, and compliance as core expectations with no corresponding velocity language.

**Run 3:** `rigour` ✓
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data governance, quality monitoring, and regulatory compliance as core responsibilities with no counterbalancing velocity language.

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: GDPR compliance indicates regulatory awareness, but the role is primarily analytics-focused without emphasis on financial reporting or compliance-critical risk.

**Run 2:** `moderate` ✓
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: While GDPR compliance is mentioned, the primary framing is business analytics (dashboards and data solutions) for a retail company, which typically carries moderate business risk rather than high regulatory or financial consequences.

**Run 3:** `moderate` ✓
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: While GDPR and governance matter, this retail company role is primarily framed around translating business questions into dashboards without direct financial reporting or compliance-driven consequences.

### collaboration_width
**Manual:** `0`

**Run 1:** `0` ✓
> Quote: "works with stakeholders on information needs"
> Verified: ✓ found in JD
> Reasoning: No named teams or functions are explicitly identified; stakeholders are referenced generically without specification.

**Run 2:** `0` ✓
> Quote: "works with stakeholders on information needs"
> Verified: ✓ found in JD
> Reasoning: The JD uses generic terms like 'stakeholders' and 'business' without naming specific teams or functions.

**Run 3:** `0` ✓
> Quote: "works with stakeholders on information needs"
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner functions or teams are identified in the JD; 'stakeholders' is too generic to count as a specific collaboration partner.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: The role uses named existing tools (dbt, BigQuery) and works with established pipelines, indicating an existing but growing data function.

**Run 2:** `mid` ✓
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in responsibilities with specific context (dbt models, BigQuery, existing pipelines), indicating an established but still-growing data function.

**Run 3:** `mid` ✓
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: Named tools and established governance practices appear in the responsibilities section, indicating a developing data function beyond early-stage but without signals of multiple specialized sub-teams.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance"
> Verified: ✓ found in JD
> Reasoning: Combines technical specificity (named tools, GDPR compliance) with generic boilerplate verbs like 'works with stakeholders' and 'promoting data-driven culture'.

**Run 2:** `mixed` ✗
> Quote: "designs datamodels in dbt and BigQuery, works with stakeholders on information needs, and monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: Some responsibilities show technical specificity (named tools, compliance context) while others are generic boilerplate, indicating both hiring manager and recruiter input.

**Run 3:** `recruiter` ✗
> Quote: "translating business questions into dashboards and data solutions. The engineer designs datamodels in dbt and BigQuery, works with stakeholders on information needs"
> Verified: ✓ found in JD
> Reasoning: The responsibilities use generic boilerplate action verbs and collaboration language typical of recruiter templates, with tool names but limited contextual depth about problems solved.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The role focuses on providing analytics infrastructure and dashboards to internal business stakeholders seeking answers, rather than serving a specific commercial, product, or finance function.

**Run 2:** `internal_data` ✓
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The primary function is providing self-serve analytics (dashboards) to business stakeholders seeking to answer their own questions, which aligns with internal_data stakeholder orientation.

**Run 3:** `internal_data` ✓
> Quote: "promoting data-driven culture across the organization"
> Verified: ✓ found in JD
> Reasoning: The emphasis on governance, quality monitoring, and cultural adoption suggests the role primarily serves the analytics function itself and internal platform consumers.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The verb 'translating' and overall framing indicate the role implements solutions to defined business questions rather than setting strategic direction.

**Run 2:** `execution` ✗
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The primary responsibility is translating given business questions into solutions, which frames the role as executing against questions defined by stakeholders rather than setting direction.

**Run 3:** `execution` ✗
> Quote: "translating business questions into dashboards and data solutions"
> Verified: ✓ found in JD
> Reasoning: The responsibilities frame the role as delivering solutions in response to others' needs rather than setting strategic direction or defining how analytics is delivered.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "interest in advanced analytics and AI applications"
> Verified: ✓ found in JD
> Reasoning: This is vague interest language without specific AI skill expectations for the candidate; interest is not equivalent to required proficiency or demonstrated application.

**Run 2:** `none` ✗
> Quote: "interest in advanced analytics and AI applications"
> Verified: ✓ found in JD
> Reasoning: 'Interest in AI' is explicitly vague framing per the classification rules and does not demonstrate a concrete AI skill requirement.

**Run 3:** `none` ✗
> Quote: "interest in advanced analytics and AI applications"
> Verified: ✓ found in JD
> Reasoning: The JD mentions interest in AI but provides no specific AI skill requirement for the candidate; vague interest phrases do not constitute a skill expectation.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as an explicit responsibility the candidate monitors and is accountable for.

**Run 2:** `responsibility` ✗
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly accountable for data quality monitoring, which establishes ownership of the data quality practice even without specifying particular tools.

**Run 3:** `responsibility` ✗
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: Data quality monitoring is framed as a core responsibility the engineer is accountable for, indicating ownership of this practice.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "monitors data quality and governance including GDPR compliance; resolving pipeline issues"
> Verified: ✓ found in JD
> Reasoning: While compliance and operational reliability are mentioned, they are secondary to the primary delivery focus on translating business questions into dashboards.

**Run 2:** `moderate` ✗
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: The JD includes operational reliability and compliance concerns, indicating moderate risk awareness, though they are secondary to the primary delivery responsibilities.

**Run 3:** `moderate` ✗
> Quote: "monitors data quality and governance including GDPR compliance"
> Verified: ✓ found in JD
> Reasoning: Compliance and governance signal operational risk management concerns, but the role is primarily framed around delivering dashboards, making risk secondary to delivery.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
