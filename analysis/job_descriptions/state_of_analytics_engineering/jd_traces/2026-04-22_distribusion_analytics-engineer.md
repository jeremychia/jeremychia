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
| velocity_vs_rigour | mixed | mixed | velocity | mixed | 33% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 3 | 0 | 0 | 0 | 100% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | mixed | mixed | hiring_manager | 33% | ✗ |
| stakeholder_orientation |  | internal_data | internal_data | internal_data | 100% | ✗ |
| autonomy_level |  | mixed | execution | execution | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (high accuracy, rigorous verification, anticipate challenges, evaluate long-term impacts) coexist with velocity signals (tight deadlines, faster creation, fast-paced environment).

**Run 2:** `velocity` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize speed of delivery with 'tight deadlines' and 'faster creation' appearing multiple times, while rigour signals are limited to a single mention of 'rigorous verification'.

**Run 3:** `mixed` ✓
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes speed with 'tight deadlines' and 'fast-paced work environment' while also emphasizing quality with 'Maintain high accuracy through rigorous verification of all outputs', with both dimensions genuinely present.

⚠ **LLM inconsistency**: runs gave ['mixed', 'velocity', 'mixed']

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Exposure to major clients like Booking.com and Google Maps"
> Verified: ✓ found in JD
> Reasoning: Data errors affect business decisions and client relationships but no regulatory, financial reporting, or compliance language appears.

**Run 2:** `moderate` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: This is dashboard and BI work without explicit financial reporting, compliance, or regulatory language; it supports business decisions but not mission-critical financial or regulatory functions.

**Run 3:** `moderate` ✗
> Quote: "Direct ownership and measurable company impact from day one"
> Verified: ✓ found in JD
> Reasoning: The JD indicates business impact but lacks explicit language about financial reporting, compliance, regulatory requirements, or mission-critical systems that would signal high risk.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "Collaborative international team environment"
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaborative work but does not name specific departments, functions, or teams.

**Run 2:** `0` ✗
> Quote: "none"
> Verified: ⚠ NOT found verbatim
> Reasoning: No named internal partner teams or functions are mentioned in the responsibilities; external client exposure is noted but not framed as collaboration partners.

**Run 3:** `0` ✗
> Quote: "Collaborative international team environment"
> Verified: ✓ found in JD
> Reasoning: No distinct named partner teams, functions, or external collaborators are explicitly identified; generic phrases like 'collaborative team environment' do not count.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: Named existing tools (Looker, BigQuery, Kafka, Airflow, data lake) with established workflows indicate infrastructure in place with room for growth and enhancement.

**Run 2:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: The JD references established infrastructure (data lake, Kafka, Airflow, BigQuery) being enhanced and expanded, indicating a functioning data function rather than greenfield startup.

**Run 3:** `mid` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure (data lake, reporting systems, Looker, Kafka, Airflow) needing enhancement rather than building from zero, indicating a developing team with established but evolving capabilities.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: Specific tool applications (Looker, data lake, tight deadlines) suggest hiring_manager input, but generic verbs elsewhere (grasp, identify, maintain) indicate recruiter contribution.

**Run 2:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: Specific technical tool mention (Looker) and concrete constraints (tight deadlines) suggest domain expertise, but generic responsibilities like 'maintain high accuracy' and 'anticipate future challenges' indicate recruiter input.

**Run 3:** `hiring_manager` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical details (Looker dashboards, data lake, reporting systems) indicating the author understands the actual work, not generic boilerplate.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'hiring_manager']

### stakeholder_orientation
**Manual:** ``

**Run 1:** `internal_data` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: Responsibilities focus on building and improving analytics infrastructure and reporting systems that serve data consumers and the platform itself.

**Run 2:** `internal_data` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize working with data infrastructure and reporting systems, framing the role as serving the analytics platform and its consumers rather than specific business functions.

**Run 3:** `internal_data` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and improving analytics infrastructure (dashboards, data lake, reporting systems) that serves the organization's internal data consumers and capabilities.

⚠ **Disagreement**: manual=`` vs LLM majority=`internal_data`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Leverage available tools and resources to solve problems independently"
> Verified: ✓ found in JD
> Reasoning: The role includes strategic autonomy to solve independently and anticipate long-term impacts, balanced against execution responsibilities like building dashboards and maintaining accuracy.

**Run 2:** `execution` ✗
> Quote: "Leverage available tools and resources to solve problems independently"
> Verified: ✓ found in JD
> Reasoning: While there is autonomy in approach ('independently'), the role is primarily framed around executing defined deliverables (building dashboards, maintaining quality) rather than setting strategy or priorities.

**Run 3:** `execution` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: The role focuses on executing assigned work—building dashboards, learning infrastructure, improving systems—rather than setting analytics strategy or direction.

⚠ **Disagreement**: manual=`` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'execution']
