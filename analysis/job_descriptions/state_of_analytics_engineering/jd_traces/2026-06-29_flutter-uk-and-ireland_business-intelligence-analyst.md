# Trace: 2026-06-29_flutter-uk-and-ireland_business-intelligence-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Analyst — Flutter UK & Ireland

**URL:** https://careers.flutteruki.com/search-jobs/jr134770/business-intelligence-analyst/?source=LinkedIn
**Location:** Gibraltar
**Date Posted:** 2026-06-29

---

Business Intelligence Analyst

Company: Flutter UK & Ireland
Location: Gibraltar

About the role:
This role involves analyzing commercial performance data for the Gaming division's Performance and Business Intelligence team. The analyst will collaborate with Commercial, Marketing, and Acquisition teams to uncover insights from large datasets.

Key Responsibilities:
- Identifying key trends and helping form actionable insight on issues, opportunities and performance drivers using large datasets
- Conduct analysis using SQL, Excel, and data visualization tools to support Commercial, Marketing, and Acquisition teams
- Provide analytical support to our Acquisition team, including various ad-hoc performance analysis and dashboard building
- Analyze revenue impacts of product and process changes
- Collaborate with business stakeholders to identify performance trends
- Develop understanding of reporting suite and identify gaps
- Present findings with appropriate detail and effective communication
- Contribute to projects focusing on the revenue impacts of changes to products and processes

Required Skills:
- SQL proficiency
- Excel expertise
- Data analysis capabilities
- Presentation skills

Desirable Skills:
- Looker
- R programming
- Statistical modeling

About Flutter UK & Ireland:
Flutter UK & Ireland operates several major gaming brands including Sky Betting & Gaming, Paddy Power, Betfair and tombola. The organization emphasizes four core values: Customer First Always, Change The Game, Win Together, and Free To Be Me.

Benefits:
- Competitive pension scheme
- Private medical cover
- Life assurance
- Yearly wellbeing fund allowance

Flutter emphasizes inclusive hiring, stating candidates don't have to meet all the requirements listed to apply and accommodations are available upon request.

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | velocity | rigour | 33% | ✓ |
| domain_risk | high | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 3 | 3 | 3 | 3 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | recruiter | recruiter | recruiter | recruiter | 100% | ✓ |
| stakeholder_orientation | commercial | commercial | commercial | commercial | 100% | ✓ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Present findings with appropriate detail and effective communication"
> Verified: ✓ found in JD
> Reasoning: The JD lacks velocity language (fast-paced, ship, iterate) and emphasizes careful, detailed presentation of findings, indicating a rigour orientation.

**Run 2:** `velocity` ✗
> Quote: "Provide analytical support to our Acquisition team, including various ad-hoc performance analysis and dashboard building"
> Verified: ✓ found in JD
> Reasoning: The 'ad-hoc' nature of the analysis and emphasis on rapid response to business teams' analytical needs indicates a velocity-oriented role focused on quick turnaround rather than governance or testing frameworks.

**Run 3:** `rigour` ✓
> Quote: "Present findings with appropriate detail and effective communication"
> Verified: ✓ found in JD
> Reasoning: The emphasis on appropriate detail and effective communication establishes quality and rigour standards, with no corresponding velocity language in the JD.

⚠ **LLM inconsistency**: runs gave ['rigour', 'velocity', 'rigour']

### domain_risk
**Manual:** `high`

**Run 1:** `moderate` ✗
> Quote: "Analyze revenue impacts of product and process changes"
> Verified: ✓ found in JD
> Reasoning: While Flutter operates in the regulated gaming sector, the JD focuses on commercial performance and revenue analysis rather than regulatory compliance or financial reporting.

**Run 2:** `moderate` ✗
> Quote: "Analyze revenue impacts of product and process changes"
> Verified: ✓ found in JD
> Reasoning: While Flutter operates in the regulated gaming industry, the JD frames the role around analyzing revenue impacts for business teams rather than compliance or regulatory requirements, suggesting moderate rather than high domain risk.

**Run 3:** `moderate` ✗
> Quote: "Analyze revenue impacts of product and process changes"
> Verified: ✓ found in JD
> Reasoning: While the role involves financial analysis, the JD lacks explicit regulatory, compliance, or audit language that would indicate high-risk consequences.

⚠ **Disagreement**: manual=`high` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `3` ✓
> Quote: "Commercial, Marketing, and Acquisition teams"
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams are explicitly identified as primary collaboration partners.

**Run 2:** `3` ✓
> Quote: "collaborate with Commercial, Marketing, and Acquisition teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct business functions as collaboration partners.

**Run 3:** `3` ✓
> Quote: "Commercial; Marketing; Acquisition teams"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named functions are explicitly listed as collaboration partners in the responsibilities section.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Develop understanding of reporting suite and identify gaps"
> Verified: ✓ found in JD
> Reasoning: The JD references an existing reporting infrastructure that the role works with and improves, indicating a mid-stage data function rather than building from zero.

**Run 2:** `mid` ✓
> Quote: "Develop understanding of reporting suite and identify gaps"
> Verified: ✓ found in JD
> Reasoning: The existence of an established reporting suite with identifiable gaps indicates a mid-stage data team that has built foundational infrastructure but is still improving and extending it.

**Run 3:** `mid` ✓
> Quote: "Develop understanding of reporting suite and identify gaps"
> Verified: ✓ found in JD
> Reasoning: The existence of a reporting suite indicates established infrastructure, but the emphasis on understanding and identifying gaps suggests room for growth typical of mid-stage teams.

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `recruiter` ✓
> Quote: "Conduct analysis using SQL, Excel, and data visualization tools to support Commercial, Marketing, and Acquisition teams"
> Verified: ✓ found in JD
> Reasoning: Tools are listed without specific application context and responsibilities use generic BI action verbs (conduct, support, provide) without technical depth, scale, or methodology specificity.

**Run 2:** `recruiter` ✓
> Quote: "Conduct analysis using SQL, Excel, and data visualization tools to support Commercial, Marketing, and Acquisition teams"
> Verified: ✓ found in JD
> Reasoning: The generic action verbs throughout (conduct, provide, collaborate, contribute) and tools listed without specific context or application background are characteristic of recruiter-written copy.

**Run 3:** `recruiter` ✓
> Quote: "Conduct analysis using SQL, Excel, and data visualization tools to support Commercial, Marketing, and Acquisition teams"
> Verified: ✓ found in JD
> Reasoning: Tools are listed without specific application context or methodology, and the overall language uses generic boilerplate action verbs common in recruiter-written job descriptions.

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `commercial` ✓
> Quote: "collaborate with Commercial, Marketing, and Acquisition teams to uncover insights from large datasets"
> Verified: ✓ found in JD
> Reasoning: The role's primary audience is commercial functions (Acquisition, Commercial, Marketing teams) focused on revenue impacts and commercial performance.

**Run 2:** `commercial` ✓
> Quote: "collaborate with Commercial, Marketing, and Acquisition teams to uncover insights"
> Verified: ✓ found in JD
> Reasoning: The explicitly named stakeholders—Commercial, Marketing, and Acquisition teams—are all GTM and revenue-focused functions, making commercial the primary orientation.

**Run 3:** `commercial` ✓
> Quote: "support Commercial, Marketing, and Acquisition teams"
> Verified: ✓ found in JD
> Reasoning: The primary stakeholders are explicitly named as commercial functions (Commercial, Marketing, Acquisition), which are all GTM and revenue-oriented.

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "Provide analytical support to our Acquisition team, including various ad-hoc performance analysis and dashboard building"
> Verified: ✓ found in JD
> Reasoning: The role is framed as providing support and executing ad-hoc requests from business teams, with no language about defining strategy or setting direction.

**Run 2:** `execution` ✓
> Quote: "Provide analytical support to our Acquisition team, including various ad-hoc performance analysis and dashboard building"
> Verified: ✓ found in JD
> Reasoning: Consistent use of execution verbs (provide, support, contribute, assist) with no strategic ownership language indicates the role executes defined analytical tasks for business teams rather than setting its own direction.

**Run 3:** `execution` ✓
> Quote: "Provide analytical support to our Acquisition team"
> Verified: ✓ found in JD
> Reasoning: The role is framed as providing support and contributing to predefined projects rather than setting direction or defining analytics strategy.
