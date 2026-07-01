# Trace: 2026-05-11_helmes_team-lead

## JD text (fed to classifier, Layer B stripped)

```
# Team Lead — Helmes

**Location:** Estonia (offices in Tallinn and Tartu)
**Application Deadline:** 22.05.2026

---

## Key Responsibilities

- Lead software development teams and projects
- Inspire and develop team members
- Provide resources (technology, skills, capacity) for success
- Monitor performance and continuously improve work methods
- Manage finances (billing, reporting)
- Serve as primary contact for both clients and team
- Develop client relationships and seek new opportunities
- Support sales and client acquisition
- Contribute to process and tool development

---

## Required Qualifications

- Minimum 3 years of project management experience in software development
- Experience managing teams, including ability to motivate people
- Good communication skills
- Willingness to take responsibility and follow through on obligations
- Experience with financial and budget management at unit level
- Very good Estonian and English language skills both in speech and writing
- Knowledge and ability to manage Scrum processes

---

## Preferred / Bonus Skills

None listed.

---

## Benefits

- Caring work environment, where you can grow, take responsibility and have real impact
- Supportive mentor for professional development
- Freedom, trust, and responsibility in work
- Flexible hybrid work and work-life balance
- Modern offices in Tallinn and Tartu
- Additional health insurance and sports activity support
- Caring culture with regular team events and community activities

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | low | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 2 | 2 | 2 | 2 | 100% | ✓ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | recruiter | recruiter | recruiter | recruiter | 100% | ✓ |
| stakeholder_orientation |  | commercial | commercial | commercial | 100% | ✗ |
| autonomy_level |  | mixed | strategic | execution | 0% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Monitor performance and continuously improve work methods"
> Verified: ✓ found in JD
> Reasoning: Emphasis on continuous improvement and performance monitoring suggests focus on operational excellence and quality rather than speed or rapid delivery.

**Run 2:** `rigour` ✓
> Quote: "Monitor performance and continuously improve work methods"
> Verified: ✓ found in JD
> Reasoning: The emphasis on monitoring and continuous process improvement signals a quality and process orientation rather than speed or velocity.

**Run 3:** `rigour` ✓
> Quote: "Monitor performance and continuously improve work methods"
> Verified: ✓ found in JD
> Reasoning: The emphasis on monitoring performance and continuous improvement of work methods signals a focus on process quality and discipline rather than speed or velocity.

### domain_risk
**Manual:** `low`

**Run 1:** `moderate` ✗
> Quote: "Manage finances (billing, reporting)"
> Verified: ✓ found in JD
> Reasoning: Financial and billing management at team level creates business impact but lacks high-stakes regulatory or compliance risk.

**Run 2:** `moderate` ✗
> Quote: "Manage finances (billing, reporting)"
> Verified: ✓ found in JD
> Reasoning: Financial management is operational (billing, reporting) rather than regulatory or strategic, indicating moderate business impact without high-risk domain signals.

**Run 3:** `moderate` ✗
> Quote: "Lead software development teams and projects"
> Verified: ✓ found in JD
> Reasoning: The JD provides no explicit domain risk signals such as financial reporting, regulatory compliance, or mission-critical systems; generic software development carries moderate business risk by default.

⚠ **Disagreement**: manual=`low` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `2`

**Run 1:** `2` ✓
> Quote: "Support sales and client acquisition; Serve as primary contact for both clients and team"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two named collaborating functions identified: sales (explicit function) and clients (explicitly named as primary collaboration partners).

**Run 2:** `2` ✓
> Quote: "clients; sales"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names clients as collaboration partners ('Serve as primary contact for both clients') and sales as a distinct function ('Support sales and client acquisition').

**Run 3:** `2` ✓
> Quote: "clients; sales"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct partner functions are explicitly named: clients (primary contact and relationship focus) and sales team (to support).

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "Lead software development teams and projects"
> Verified: ✓ found in JD
> Reasoning: JD implies existing established teams requiring management and improvement rather than greenfield setup or early-stage building.

**Run 2:** `mid` ✗
> Quote: "Contribute to process and tool development"
> Verified: ✓ found in JD
> Reasoning: Implies existing processes and tools while also suggesting ongoing development and improvement, characteristic of mid-stage team maturity.

**Run 3:** `mid` ✗
> Quote: "Caring work environment, where you can grow, take responsibility and have real impact"
> Verified: ✓ found in JD
> Reasoning: Language describes an established organization with organizational structure and formal benefits, but no signals of greenfield setup or large-scale specialized team infrastructure.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `recruiter`

**Run 1:** `recruiter` ✓
> Quote: "Inspire and develop team members"
> Verified: ✓ found in JD
> Reasoning: All responsibilities use generic boilerplate action verbs without technical specificity, named tools, or context that would indicate hiring-manager authorship.

**Run 2:** `recruiter` ✓
> Quote: "Lead software development teams and projects; Inspire and develop team members; Serve as primary contact for both clients and team"
> Verified: ⚠ NOT found verbatim
> Reasoning: Generic boilerplate management verbs with no technical specificity, named tools with context, or scale metrics that would indicate hiring manager authorship.

**Run 3:** `recruiter` ✓
> Quote: "Lead software development teams and projects; Inspire and develop team members; Provide resources (technology, skills, capacity) for success"
> Verified: ⚠ NOT found verbatim
> Reasoning: Responsibilities consist entirely of generic, boilerplate action verbs with no technical specificity, scale context, or methodology detail that would indicate hands-on hiring manager authorship.

### stakeholder_orientation
**Manual:** ``

**Run 1:** `commercial` ✗
> Quote: "Develop client relationships and seek new opportunities"
> Verified: ✓ found in JD
> Reasoning: Primary responsibilities emphasize client relationship development and supporting GTM/sales activities.

**Run 2:** `commercial` ✗
> Quote: "Develop client relationships and seek new opportunities; Support sales and client acquisition"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary emphasis on client-facing activities and sales support as distinguishing responsibilities indicates commercial stakeholder orientation.

**Run 3:** `commercial` ✗
> Quote: "Develop client relationships and seek new opportunities; Support sales and client acquisition"
> Verified: ⚠ NOT found verbatim
> Reasoning: Primary emphasis in responsibilities centers on client relations, business development, and GTM support, indicating commercial/revenue-focused stakeholder orientation.

⚠ **Disagreement**: manual=`` vs LLM majority=`commercial`

### autonomy_level
**Manual:** ``

**Run 1:** `mixed` ✗
> Quote: "Lead software development teams and projects; Support sales and client acquisition"
> Verified: ⚠ NOT found verbatim
> Reasoning: Role combines strategic leadership of team direction (lead, develop) with execution support for business-set objectives (support sales).

**Run 2:** `strategic` ✗
> Quote: "Lead software development teams and projects; Develop client relationships and seek new opportunities"
> Verified: ⚠ NOT found verbatim
> Reasoning: Direction-setting verbs 'Lead' and 'Develop' applied to core responsibilities indicate the role is expected to set direction for teams and client relationships rather than execute direction from others.

**Run 3:** `execution` ✗
> Quote: "Support sales and client acquisition"
> Verified: ✓ found in JD
> Reasoning: The role supports and executes strategic priorities set by others rather than defining overall direction; responsibilities frame the position as delivery-oriented within organizational strategy.

⚠ **Disagreement**: manual=`` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'execution']

### ai_role
**Run 1:** `none` ✓
> Quote: "Lead software development teams and projects"
> Reasoning: The role focuses on team leadership and project management without mention of AI tools or infrastructure

**Run 2:** `none` ✓
> Quote: "Lead software development teams and projects"
> Reasoning: Leadership and sales responsibilities with no AI tool usage or infrastructure building mentioned.

**Run 3:** `none` ✓
> Quote: "Lead software development teams and projects"
> Reasoning: No mention of AI tools, AI-first mindset, or GenAI-related infrastructure.


### testing_framing
**Run 1:** `absent` ✓
> Quote: "Monitor performance and continuously improve work methods"
> Reasoning: Performance and methods are mentioned but no explicit ownership of testing or quality practices

**Run 2:** `absent` ✓
> Quote: "Monitor performance and continuously improve work methods"
> Reasoning: Performance monitoring present but no explicit testing, quality ownership, or data-contract responsibility.

**Run 3:** `absent` ✓
> Quote: "Serve as primary contact for both clients and team"
> Reasoning: No explicit testing/quality responsibility ownership, tool mentions, or quality process signals.


### loss_aversion_framing
**Run 1:** `none` ✓
> Quote: "Lead software development teams and projects; Support sales and client acquisition"
> Reasoning: Responsibilities emphasize delivery and growth with no compliance, reliability, or risk-mitigation framing

**Run 2:** `none` ✓
> Quote: "Monitor performance and continuously improve work methods"
> Reasoning: Delivery and process-improvement framing with no operational reliability or compliance risk drivers.

**Run 3:** `none` ✓
> Quote: "Lead software development teams and projects; Inspire and develop team members; Provide resources (technology, skills, capacity) for success"
> Reasoning: Positive delivery framing centered on team success and capability-building, not risk mitigation or compliance concerns.

