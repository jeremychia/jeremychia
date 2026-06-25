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
| jd_authorship | recruiter | mixed | mixed | recruiter | 33% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Maintain high accuracy through rigorous verification of all outputs"
> Verified: ✓ found in JD
> Reasoning: The JD contains both velocity signals ('within tight deadlines,' 'fast-paced') and explicit rigour emphasis ('rigorous verification'), creating mixed orientation.

**Run 2:** `velocity` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: The JD repeatedly emphasizes speed and pace (tight deadlines, fast-paced environment, rapid industry growth) far more than rigour signals, establishing velocity as the primary orientation despite one mention of rigorous verification.

**Run 3:** `mixed` ✓
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: The tight deadlines signify velocity, but this is directly balanced by 'Maintain high accuracy through rigorous verification of all outputs,' creating a mixed orientation.

⚠ **LLM inconsistency**: runs gave ['mixed', 'velocity', 'mixed']

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Exposure to major clients like Booking.com and Google Maps"
> Verified: ✓ found in JD
> Reasoning: While involving major clients, the JD lacks explicit language about financial reporting, compliance, or regulatory requirements that would indicate high risk.

**Run 2:** `moderate` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: The role focuses on business reporting and dashboards without explicit signals of financial reporting, regulatory compliance, or mission-critical impact typical of high-risk domains.

**Run 3:** `moderate` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: The focus on dashboard reporting and clarity indicates operational analytics rather than financial reporting, compliance, or regulatory implications typical of high-risk domains.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "None identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: No specific named partner teams or functions are explicitly mentioned; generic references like 'collaborative international team' do not count.

**Run 2:** `0` ✗
> Quote: "None"
> Verified: ⚠ NOT found verbatim
> Reasoning: No explicitly named partner teams or functions are mentioned; generic phrases like 'collaborative team environment' do not identify specific departments or groups.

**Run 3:** `0` ✗
> Quote: "Collaborative international team environment"
> Verified: ✓ found in JD
> Reasoning: While collaboration is mentioned, no explicitly named teams, functions, or collaboration partners are identified in the JD.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Identify and propose enhancements to reporting systems for better clarity and faster creation"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure and tools (data lake, Looker, BigQuery, Kafka, Airflow) and improvement work, indicating a team past initial build but actively scaling.

**Run 2:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: References to an established data lake and reporting systems indicate infrastructure exists and is being actively used, but no mention of specialized sub-teams or platform scale suggests growth-stage rather than mature organization.

**Run 3:** `mid` ✗
> Quote: "Become proficient with the data lake, understanding data sources and processing workflows"
> Verified: ✓ found in JD
> Reasoning: The existence of a data lake, established data sources, and processing workflows indicates a data function that has moved beyond early-stage greenfield and is now operating with basic infrastructure.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines"
> Verified: ✓ found in JD
> Reasoning: Specific tool mention (Looker) and clear responsibilities show technical knowledge, but most other responsibilities use generic language without operational context or methodology details.

**Run 2:** `mixed` ✗
> Quote: "Build new Looker dashboards from scratch within tight deadlines; Maintain high accuracy through rigorous verification of all outputs"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical details (Looker, data lake, workflows) show hands-on job knowledge, but generic soft-skills language (grasp context quickly, anticipate challenges) and recruiter-style behavioral framing indicate shared authorship.

**Run 3:** `recruiter` ✓
> Quote: "Leverage available tools and resources to solve problems independently"
> Verified: ✓ found in JD
> Reasoning: This classic boilerplate language, along with generic action verbs throughout ('Identify and propose,' 'Maintain accuracy,' 'Grasp context'), suggests recruiter authorship rather than someone who has done the job.

⚠ **Disagreement**: manual=`recruiter` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'recruiter']
