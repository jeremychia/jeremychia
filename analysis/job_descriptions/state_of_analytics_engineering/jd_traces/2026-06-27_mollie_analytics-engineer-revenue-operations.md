# Trace: 2026-06-27_mollie_analytics-engineer-revenue-operations

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer - Revenue Operations — Mollie

**Location:** Amsterdam; Milan
**Date Posted:** 2026-06-27

---

Analytics Engineer - Revenue Operations
Location
Amsterdam; Milan

Employment Type
Full time

Location Type
Hybrid

Department
Engineering

Overview
Application
Analytics Engineer II - Revenue Operations

The role:

Job title: Analytics Engineer II

Location: Amsterdam or Milan

Remote/ Hybrid: Hybrid

Build with us

Since 2004, we've had one clear goal: to make payments and money management effortless for every business in Europe.

Today, more than 250,000 companies use Mollie to get paid, manage money and grow with products designed to be simple, scalable, and dependable.

With 950+ Mollies across 14+ locations, we care deeply about autonomy and craft. So we work in small teams, with real ownership, and we trust you to make the right decisions.

We're building for the long term, so we provide the tools you need, processes you can rely on, and a balanced work environment to help you do work you're proud of.

Sound like your kind of place? Let's build together.

Your impact

Revenue Operations at Mollie serves around 200 internal stakeholders across sales, customer success, marketing, and partnerships. The analytics work done here feeds directly into how commercial teams make decisions, assign leads, and manage performance. When the data is right, the whole commercial engine runs better.

This role sits inside the GTM Enablement team, a small group focused on making Mollie's go-to-market motion faster and smarter. You will be the analytics engineering support for the team's projects. At the same time you will own reporting of our GTM domains, such as Merchant Sales and CSM & Customer Growth. That means the work you produce is immediately visible and measurable within the business.

The domain is actively growing and maturing. RevOps has recently adopted a full domain model and is being rebuilt as a proper product and engineering function. There is real space here to shape how analytics is delivered to commercial stakeholders, not just execute on requests. Over time, the expectation is that the team shifts from reactive to proactive, and this role is central to making that happen.

What you'll ship

Own and maintain core dashboards for GTM domains, including CSM, and Merchant Sales, serving as the source of truth for commercial stakeholders

Own and maintain HubSpot data models

Define success metrics, set up data tracking and reporting for GTM Enablement team projects

Reduce dashboard sprawl by establishing centralised, standardised reporting in Omni

Deliver ad hoc analysis and impact scoping to support decision-making

What you'll bring

Strong SQL skills and hands-on experience building dashboards and reports in BI tools such as Looker, Tableau, or similar

Solid data visualisation skills with the ability to translate complex data into clear, actionable outputs for commercial audiences

A working understanding of data modelling concepts, with the ability to apply basic engineering best practices in your work

Experience managing stakeholders in a commercial or sales-facing environment, including the ability to prioritise, and communicate clearly with both technical and non-technical audiences

Around four or more years of experience in an analytics engineering or closely related role, with a proven level of independence to scope and drive your own work

Comfort working in a fast-moving, commercially oriented environment where priorities shift and ambiguity is part of the job


Grow your way

At Mollie, growth is personal. We believe everyone should have the chance to develop their skills, explore new challenges and shape their career on their own terms.

You'll get regular feedback and performance reviews to support your development, with fair and transparent salary reviews along the way. Many Mollies move into new roles or take on new projects to stretch themselves, and we actively hire from within to help …[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | mixed | rigour | rigour | 33% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 4 | 4 | 4 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | mixed | 33% |
| stakeholder_orientation | commercial | commercial | commercial | 100% |
| autonomy_level | mixed | strategic | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `mixed`
> Quote: "There is real space here to shape how analytics is delivered to commercial stakeholders, not just execute on requests. Over time, the expectation is that the team shifts from reactive to proactive, and this role is central to making that happen."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes both velocity signals (shift from reactive to proactive, fast-moving environment, priorities shift) and rigour signals (standardised reporting, source of truth, maintaining models), creating a genuine combination of both orientations.

**Run 2:** `rigour`
> Quote: "apply basic engineering best practices in your work"
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize standardization and best practices over speed; the single velocity signal ('fast-moving, commercially oriented environment') is outweighed by multiple rigour signals including data modelling concepts, engineering practices, and centralised reporting standards.

**Run 3:** `rigour`
> Quote: "A working understanding of data modelling concepts, with the ability to apply basic engineering best practices in your work"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize maintaining data models, establishing standardized reporting, and serving as a source of truth—core data quality and engineering best practices—while fast-paced work environment is mentioned as a comfort requirement rather than a primary orientation.

⚠ **LLM inconsistency**: runs gave ['mixed', 'rigour', 'rigour']

### domain_risk

**Run 1:** `moderate`
> Quote: "The analytics work done here feeds directly into how commercial teams make decisions, assign leads, and manage performance."
> Verified: ✓ found in JD
> Reasoning: The role impacts operational and commercial decisions without involving financial reporting, regulatory compliance, or public-facing risk, placing it at moderate risk.

**Run 2:** `moderate`
> Quote: "feeds directly into how commercial teams make decisions, assign leads, and manage performance"
> Verified: ✓ found in JD
> Reasoning: Data errors affect business and commercial operations decisions but not regulatory reporting or financial compliance; Revenue Operations serves GTM/sales outcomes rather than financial or regulatory processes.

**Run 3:** `moderate`
> Quote: "The analytics work done here feeds directly into how commercial teams make decisions, assign leads, and manage performance."
> Verified: ✓ found in JD
> Reasoning: While Mollie is a fintech company, this particular role focuses on commercial decision-making (GTM, sales, customer success) rather than financial reporting, compliance, or regulatory concerns.

### collaboration_width

**Run 1:** `4`
> Quote: "serves around 200 internal stakeholders across sales, customer success, marketing, and partnerships"
> Verified: ✓ found in JD
> Reasoning: Four distinct external collaboration partners are explicitly named: sales, customer success, marketing, and partnerships.

**Run 2:** `4`
> Quote: "across sales, customer success, marketing, and partnerships"
> Verified: ✓ found in JD
> Reasoning: Four explicitly named partner functions are listed as primary stakeholders Revenue Operations serves.

**Run 3:** `4`
> Quote: "sales, customer success, marketing, and partnerships"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names four distinct partner functions that Revenue Operations serves: sales, customer success, marketing, and partnerships.

### data_team_maturity

**Run 1:** `mid`
> Quote: "RevOps has recently adopted a full domain model and is being rebuilt as a proper product and engineering function. The domain is actively growing and maturing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The data function exists with named tools in responsibilities (HubSpot models, Omni dashboards) and is actively restructuring, indicating mid-stage maturity rather than early-stage greenfield or mature-stage stability.

**Run 2:** `mid`
> Quote: "The domain is actively growing and maturing. RevOps has recently adopted a full domain model and is being rebuilt as a proper product and engineering function."
> Verified: ✓ found in JD
> Reasoning: Infrastructure exists (HubSpot, Omni, BI tools) and is being actively scaled and restructured; the team has moved beyond early-stage but is not yet described as established at scale.

**Run 3:** `mid`
> Quote: "RevOps has recently adopted a full domain model and is being rebuilt as a proper product and engineering function."
> Verified: ✓ found in JD
> Reasoning: Named tools appear in the responsibilities section (HubSpot, Omni), and the JD indicates active growth and maturation of the RevOps function with real opportunities to shape direction.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Reduce dashboard sprawl by establishing centralised, standardised reporting in Omni"
> Verified: ✓ found in JD
> Reasoning: The precise articulation of a specific operational problem (dashboard sprawl), named solution (Omni consolidation), and domain context reflects hands-on experience with RevOps analytics work rather than generic boilerplate.

**Run 2:** `hiring_manager`
> Quote: "Own and maintain HubSpot data models"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain tool-specific context and domain expertise (HubSpot models, GTM domains, Merchant Sales, Omni) that indicates authorship by someone performing this work, not generic recruiter language.

**Run 3:** `mixed`
> Quote: "Own and maintain HubSpot data models"
> Verified: ✓ found in JD
> Reasoning: Specific tool and domain context (HubSpot, Omni, CSM, Merchant Sales) indicates hiring manager input, but generic boilerplate phrases in the requirements section suggest recruiter contributions.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `commercial`
> Quote: "feeds directly into how commercial teams make decisions, assign leads, and manage performance"
> Verified: ✓ found in JD
> Reasoning: The role's primary audience and impact is explicitly framed around commercial team decision-making, GTM enablement, and sales/customer success operations rather than product, finance, or internal platform work.

**Run 2:** `commercial`
> Quote: "Revenue Operations at Mollie serves around 200 internal stakeholders across sales, customer success, marketing, and partnerships. The analytics work done here feeds directly into how commercial teams make decisions, assign leads, and manage performance."
> Verified: ✓ found in JD
> Reasoning: Primary audience is explicitly GTM and commercial functions (sales, CSM, marketing, partnerships); role purpose is to enable commercial decision-making and pipeline management.

**Run 3:** `commercial`
> Quote: "The analytics work done here feeds directly into how commercial teams make decisions, assign leads, and manage performance."
> Verified: ✓ found in JD
> Reasoning: Revenue Operations explicitly serves sales, customer success, marketing, and partnerships to support GTM motion and commercial decision-making.

### autonomy_level

**Run 1:** `mixed`
> Quote: "There is real space here to shape how analytics is delivered to commercial stakeholders, not just execute on requests."
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership (defining how analytics is delivered, establishing standardised reporting, defining success metrics) with execution (maintain dashboards, deliver ad hoc analysis), making it genuinely mixed rather than purely strategic or execution-focused.

**Run 2:** `strategic`
> Quote: "There is real space here to shape how analytics is delivered to commercial stakeholders, not just execute on requests."
> Verified: ✓ found in JD
> Reasoning: Role is explicitly positioned to define direction and shape analytics delivery, not merely execute on assigned work; includes 'define success metrics' and ownership of domain reporting direction.

**Run 3:** `mixed`
> Quote: "There is real space here to shape how analytics is delivered to commercial stakeholders, not just execute on requests."
> Verified: ✓ found in JD
> Reasoning: The role combines strategic elements (defining success metrics, shaping analytics delivery, reducing sprawl, driving team maturation) with execution elements (maintaining dashboards and models, delivering ad hoc analysis).

⚠ **LLM inconsistency**: runs gave ['mixed', 'strategic', 'mixed']

### ai_role
**Run 1:** `none` ✓
> Quote: "feeds directly into how commercial teams make decisions, assign leads, and manage performance"
> Reasoning: No AI coding tools, infrastructure, or AI-first practices mentioned; standard analytics role.

**Run 2:** `none` ✓
> Quote: "(no AI skill phrase present)"
> Reasoning: No mentions of AI tools, AI-assisted coding, GenAI infrastructure, or AI-readiness.

**Run 3:** `none` ✓
> Quote: "No AI-related phrases detected"
> Reasoning: No mention of AI tools, GenAI infrastructure, or AI-assisted responsibilities


### testing_framing
**Run 1:** `absent` ✓
> Quote: "Reduce dashboard sprawl by establishing centralised, standardised reporting in Omni"
> Reasoning: Standards and consolidation framing without explicit testing ownership, quality practices, or data contracts.

**Run 2:** `absent` ✓
> Quote: "(no testing/quality ownership signal)"
> Reasoning: Data quality is implicit in 'source of truth' but no explicit ownership verbs (own/ensure/define/implement/establish) paired with testing/quality.

**Run 3:** `absent` ✓
> Quote: "Establishing centralised, standardised reporting"
> Reasoning: Standardization effort with no explicit testing responsibility or quality ownership verbs


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "serving as the source of truth for commercial stakeholders"
> Reasoning: Trustworthiness and reliability matter (high stakes for business decisions), but no compliance/regulatory language or operational incident framing.

**Run 2:** `moderate` ✓
> Quote: "serving as the source of truth for commercial stakeholders; feeds directly into how commercial teams make decisions, assign leads, and manage performance"
> Reasoning: Operational reliability framing around data accuracy impacting business decisions, without explicit regulatory or compliance language.

**Run 3:** `moderate` ✓
> Quote: "serving as the source of truth for commercial stakeholders; feeds directly into how commercial teams make decisions, assign leads, and manage performance"
> Reasoning: Data quality has operational consequences for business decisions, but primary framing is delivery excellence not compliance

