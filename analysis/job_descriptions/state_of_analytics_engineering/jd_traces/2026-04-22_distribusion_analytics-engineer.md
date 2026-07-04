# Trace: 2026-04-22_distribusion_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer @ Distribusion

**URL:** https://careers.distribusion.com/o/analytics-engineer-all-genders-4

## Key Responsibilities
- Build new Looker dashboards from scratch within tight deadlines
- Become proficient with the data lake, understanding data sources and processing workflows
- Identify and propose enhancements to reporting systems for better clarity and faster creation
- Grasp project context quickly to identify critical needs and gaps
- Maintain high accuracy through rigorous verification of all outputs
- Anticipate future challenges and evaluate long-term impacts of decisions
- Leverage available tools and resources to solve problems independently

## Required Skills & Qualifications
- Strong proficiency in Python and SQL with solid scripting capabilities
- Experience with data visualization platforms, especially Looker, Grafana, and various visualisation libraries
- Familiarity with big data technologies including BigQuery, Kafka, and Airflow
- Project management tool competency (Jira) with reliable timeline estimation ability
- Version control expertise using git/GitLab in cloud environments like Google Cloud Platform

## Behavioural Profile
- Fast-paced work environment with rapid industry growth
- Direct ownership and measurable company impact from day one
- Exposure to major clients like Booking.com and Google Maps
- Collaborative international team environment
- Flexible remote and relocation options

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | mixed | mixed | 33% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 3 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation | internal_data | mixed | internal_data | internal_data | 33% | ✓ |
| autonomy_level | execution | strategic | execution | mixed | 0% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | responsibility | responsibility | responsibility | 100% | ✗ |
| loss_aversion_framing |  | moderate | moderate | moderate | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: Rigour signals (rigorous verification, high accuracy, anticipate challenges, long-term impacts) substantially outnumber velocity signals (tight deadlines, faster creation), making rigour the dominant orientation.

**Run 2:** `mixed` ✓
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: Rigour signals (accuracy, verification) are balanced by multiple velocity signals (tight deadlines, faster creation) throughout responsibilities.

**Run 3:** `mixed` ✓
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: The JD balances velocity signals ("within tight deadlines", "fast-paced work environment") with rigour signals ("maintain high accuracy", "rigorous verification", "anticipate future challenges"), with neither dominating sufficiently for a 2:1 classification.

⚠ **LLM inconsistency**: runs gave ['rigour', 'mixed', 'mixed']

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Exposure to major clients like Booking.com and Google Maps"
> Verified: ✓ found in JD
> Reasoning: While the company operates at scale with major clients, there is no language about financial reporting, compliance, or regulatory concerns, indicating moderate rather than high risk.

**Run 2:** `moderate` ✗
> Quote: "Exposure to major clients like Booking.com and Google Maps"
> Verified: ✓ found in JD
> Reasoning: The role supports critical business clients but lacks explicit financial reporting, compliance, regulatory, or mission-critical risk language.

**Run 3:** `moderate` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: The JD describes analytics and reporting work without financial, compliance, or regulatory language, typical of moderate-risk SaaS/marketplace roles where data errors affect business intelligence but not regulatory exposure.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "Collaborative international team environment"
> Verified: ✓ found in JD
> Reasoning: The JD references collaboration generically without naming any specific partner teams, functions, or distinct stakeholder groups.

**Run 2:** `0` ✗
> Quote: "Collaborative international team environment"
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaboration but names no specific business functions or partner teams in responsibilities or structure.

**Run 3:** `0` ✗
> Quote: "Leverage available tools and resources to solve problems independently"
> Verified: ✓ found in JD
> Reasoning: The JD does not name specific partner teams, functions, or stakeholder groups; instead emphasizes independent problem-solving within the analytics domain.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: The JD signals existing infrastructure (data lake, Kafka, Airflow, BigQuery) with a focus on growth and enhancement rather than greenfield construction, indicating a mid-stage team.

**Run 2:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure and tools (data lake, BigQuery, Kafka, Airflow, Looker) are in place; the role focuses on learning and enhancement rather than operating specialized sub-teams.

**Run 3:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: The presence of named infrastructure (data lake, Kafka, Airflow, BigQuery) in responsibilities and focus on improving existing systems indicates a growing, established data function rather than early-stage or mature-scale.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about tools and context (Looker dashboards, data lake, timeline constraints) is mixed with generic boilerplate phrases like collaborative team environment and solving problems independently.

**Run 2:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: Technical specificity (Looker, data lake, named tools and workflows) mixes with generic competency language (grasp context, maintain accuracy, anticipate challenges).

**Run 3:** `mixed` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical detail (named tools like Looker, data lake, Kafka, Airflow) indicating hiring-manager input, but also generic responsibilities ("grasp project context", "anticipate future challenges") suggesting recruiter contributions.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch"
> Verified: ✓ found in JD
> Reasoning: The role builds dashboards and reporting systems without explicit signals for commercial, product, finance, or internal_data audiences, suggesting service to multiple business functions without clear emphasis.

**Run 2:** `internal_data` ✓
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize building and improving data infrastructure and reporting systems for internal analytics consumption rather than serving commercial, product, or finance teams.

**Run 3:** `internal_data` ✓
> Quote: "Build new Looker dashboards from scratch"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building and improving reporting infrastructure and dashboards without specifying commercial, product, or finance stakeholder audiences, indicating the role primarily serves the data function itself.

⚠ **LLM inconsistency**: runs gave ['mixed', 'internal_data', 'internal_data']

### autonomy_level
**Manual:** `execution`

**Run 1:** `strategic` ✗
> Quote: "Direct ownership and measurable company impact from day one"
> Verified: ✓ found in JD
> Reasoning: Direct ownership, autonomy to identify and propose enhancements, and expectation to anticipate challenges signal the role is empowered to shape analytics direction rather than execute handed-down priorities.

**Run 2:** `execution` ✓
> Quote: "Leverage available tools and resources to solve problems independently"
> Verified: ✓ found in JD
> Reasoning: The role is framed around independently executing delivery of dashboards and data work within defined parameters rather than setting strategic direction or owning analytics strategy.

**Run 3:** `mixed` ✗
> Quote: "Leverage available tools and resources to solve problems independently"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic initiative ("identify critical needs", "propose enhancements", "anticipate future challenges") within a technical domain alongside execution responsibility (build dashboards), rather than setting function-wide direction.

⚠ **Disagreement**: manual=`execution` vs LLM majority=`strategic`

⚠ **LLM inconsistency**: runs gave ['strategic', 'execution', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no signals about AI coding tools, AI-assisted development, or AI infrastructure; mentions of Python and SQL are standard development skills without AI context.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI coding tools, AI-ready data infrastructure, or AI skills expected of the candidate.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD contains no mention of AI tools (Copilot, Claude Code), AI infrastructure (GenAI applications, AI-ready data), or AI skill requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `responsibility` ✗
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: The responsibility for verification is explicitly owned by the candidate using an action verb ('maintain'), not listed as a tool requirement, indicating an owned quality responsibility.

**Run 2:** `responsibility` ✗
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: Data accuracy and verification are framed as owned responsibilities using active ownership language, not as listed tools or absent practices.

**Run 3:** `responsibility` ✗
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: The candidate is accountable for maintaining accuracy through rigorous verification processes, framing data quality as an owned responsibility rather than a listed tool or absent concern.

⚠ **Disagreement**: manual=`` vs LLM majority=`responsibility`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `moderate` ✗
> Quote: "Anticipate future challenges and evaluate long-term impacts of decisions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and quality (avoiding errors through verification and anticipation) but lacks compliance, regulatory, or stakeholder trust language that would indicate high loss aversion.

**Run 2:** `moderate` ✗
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: Data accuracy and operational reliability are concerns, but without explicit regulatory, compliance, or stakeholder-trust risk framing characteristic of high loss aversion.

**Run 3:** `moderate` ✗
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and accuracy are concerns, but the JD emphasizes delivery within tight deadlines and problem-solving rather than compliance, regulatory, or stakeholder-trust risk registers.

⚠ **Disagreement**: manual=`` vs LLM majority=`moderate`
