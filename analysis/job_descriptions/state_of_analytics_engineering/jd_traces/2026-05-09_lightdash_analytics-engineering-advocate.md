# Trace: 2026-05-09_lightdash_analytics-engineering-advocate

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineering Advocate - Europe — Lightdash

**URL:** https://jobs.ashbyhq.com/lightdash/309706bc-1081-48b6-89dc-f769bbe17e6d
**Location:** Europe (Remote, UTC +/- 3 hours)
**Salary:** £65,000 – £100,000 annually + 0.1% – 0.3% equity

---

## About Lightdash

Lightdash is an open source BI tool that instantly turns your dbt project into a full-stack BI platform.

We're building the best BI tool for analytics engineers by letting them manage everything as code, from the comfort of their text editor and command line. Once the data team has written the metrics, then Lightdash enables self-serve for the entire business, so your data is accessible for the whole team.

We're helping data teams build data-driven companies so they can make better decisions, faster.

---

## How We Work at Lightdash

- We build in public, by default. We're an open source product, so having shared context is important so that people can contribute to Lightdash. As a team, we also think that we make the best decisions when everyone has a lot of the same information. We don't oversell and under-deliver: we want the experience of using Lightdash to be as awesome as the experience we're selling.
- We challenge problems, not people. We ask ourselves "why is this broken?" not "who is breaking this?"
- We're highly collaborative. We're a group of people that are happy working independently, but love being part of a team. We not only work on problems as a team, but we also listen to the feedback from our community and our users. We invest in tools and processes that allow us to do this, even while fully remote.
- We bias towards impact. We'd rather build something to 80% and get it in front of users so we can iterate on fast feedback than build something to 100% just to find out it's not the right thing. We spend a lot of time thinking about how our work solves real user problems. We work on the highest impact problems even if they're something a bit "out of your remit".

---

## About the Role

At Lightdash, we're obsessed with the success of our users. Our fast, empathetic, and deeply technical support is one of our superpowers. We help teams with everything from building dashboards and writing SQL to analytics engineering best practices and data modeling strategy. If you have a passion for helping teams win with data, and the technical skills to debug their toughest problems, we're looking for an Analytics Engineering Advocate to join the Lightdash team.

Our users' experience of Lightdash goes beyond product features. It includes every touchpoint and interaction they have with our community and team. In this role, you'll be the voice for our community, combining technical expertise with relationship-building to help users succeed with Lightdash and modern analytics engineering. You'll spend a significant portion of your time directly helping users in Slack and on calls — diagnosing issues, answering questions, and pair-programming through problems.

**A note on AI:** We're investing heavily in AI-powered workflows throughout Lightdash, and we expect this role to be at the forefront of that evolution. You'll use AI tools daily—for task management, technical problem-solving, analytics engineering work, and potentially contributing to our codebase. The ideal candidate is excited about the rapid pace of AI development and eager to incorporate new capabilities into their work and share that knowledge with our community.

---

## Key Responsibilities

**Obsess over user success through technical problem-solving**

Our users' wins are our wins. You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on calls to pair-program through complex issues. You'll balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process improvement. You'll leverage AI tools to work more efficiently and help users understand how to do the same.

**Be the Lightdash expert**
…[truncated]
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | velocity | mixed | mixed | velocity | 33% | ✗ |
| domain_risk | low | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 3 | 0 | 1 | 0 | 33% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | mixed | mixed | 100% | ✗ |
| stakeholder_orientation | commercial | commercial | product | commercial | 33% | ✓ |
| autonomy_level | mixed | execution | mixed | mixed | 33% | ✓ |
| ai_role |  | ai_user | ai_user | ai_user | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `velocity`

**Run 1:** `mixed` ✗
> Quote: "balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process improvement"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames the role as balancing both rapid response and delivery (velocity) with strategic, architecture-focused guidance (rigour), with both orientations equally represented.

**Run 2:** `mixed` ✗
> Quote: "You'll balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process improvement."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames the role as balancing both speed/practical solutions and strategic/thoughtful guidance, indicating genuine mixed orientation.

**Run 3:** `velocity` ✓
> Quote: "fast, practical solutions"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes shipping fast solutions with company culture framing delivery as 'bias towards impact' and iterating rapidly on user feedback, with no testing, compliance, or governance signals.

⚠ **Disagreement**: manual=`velocity` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'velocity']

### domain_risk
**Manual:** `low`

**Run 1:** `moderate` ✗
> Quote: "help teams with everything from building dashboards and writing SQL to analytics engineering best practices and data modeling strategy"
> Verified: ✓ found in JD
> Reasoning: The role supports typical BI and analytics work that affects business decisions without explicit regulatory, financial reporting, or compliance risk framing.

**Run 2:** `moderate` ✗
> Quote: "Our users' wins are our wins."
> Verified: ✓ found in JD
> Reasoning: This is a B2B SaaS support role with no explicit financial reporting, compliance, or regulatory language, placing it in moderate domain risk.

**Run 3:** `moderate` ✗
> Quote: "help teams with everything from building dashboards and writing SQL to analytics engineering best practices and data modeling strategy"
> Verified: ✓ found in JD
> Reasoning: The role operates in business analytics and BI context without any financial reporting, regulatory compliance, or mission-critical systems language.

⚠ **Disagreement**: manual=`low` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: "You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on calls to pair-program through complex issues."
> Verified: ✓ found in JD
> Reasoning: The role focuses on external user and community support without naming any internal cross-functional teams or collaboration partners.

**Run 2:** `1` ✗
> Quote: "shared customer Slack channels"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names customers as collaboration partners in Slack channels, but no specific internal functions or partner teams are identified.

**Run 3:** `0` ✗
> Quote: "No named internal teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD focuses on external users and community engagement without naming specific internal partner teams like Engineering, Product, or Finance.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

⚠ **LLM inconsistency**: runs gave ['0', '1', '0']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "using Lightdash for our own analytics and demos"
> Verified: ✓ found in JD
> Reasoning: Lightdash as an established product company demonstrates an active data operation using its own product, indicating a mid-stage operational data team.

**Run 2:** `mid` ✗
> Quote: "We're an open source product, so having shared context is important so that people can contribute to Lightdash."
> Verified: ✓ found in JD
> Reasoning: The company has an established open-source product with an active community and evolving features, but shows no signals of enterprise-scale operations or multiple specialized sub-teams.

**Run 3:** `mid` ✗
> Quote: "stay current with our latest features, including our evolving AI capabilities (using Lightdash for our own analytics and demos)"
> Verified: ✓ found in JD
> Reasoning: The established product with ongoing feature development and internal usage indicates a mid-stage data function with existing tools in active use.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "You'll stay current with our latest features, including our evolving AI capabilities (using Lightdash for our own analytics and demos), understand how they fit into broader BI and analytics engineering workflows, and share this knowledge widely."
> Verified: ✓ found in JD
> Reasoning: The responsibilities combine specific technical context (Lightdash with application examples, AI tools daily) with generic support frameworks (share knowledge, understand workflows).

**Run 2:** `mixed` ✗
> Quote: "You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on calls to pair-program through complex issues."
> Verified: ✓ found in JD
> Reasoning: The JD includes specific day-to-day context (daily Slack channels, pair-programming) suggesting hiring manager input, but also contains generic communication traits ('exceptional communication skills') suggesting recruiter involvement.

**Run 3:** `mixed` ✗
> Quote: "responding to user questions, triaging bugs, and jumping on calls to pair-program through complex issues"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical role activities (user support, debugging, pair-programming) but relies heavily on generic boilerplate language in the qualifications section.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `commercial` ✓
> Quote: "At Lightdash, we're obsessed with the success of our users."
> Verified: ✓ found in JD
> Reasoning: The role's primary accountability is to external users/customers for retention and adoption success, which aligns with customer success as a commercial function.

**Run 2:** `product` ✗
> Quote: "Ability to connect user needs to product strategy and feature development"
> Verified: ✓ found in JD
> Reasoning: The role combines identifying product champions and connecting user feedback to product development with community growth responsibilities, making product the primary stakeholder.

**Run 3:** `commercial` ✓
> Quote: "help users succeed with Lightdash and modern analytics engineering"
> Verified: ✓ found in JD
> Reasoning: The role is fundamentally oriented toward external customer success and user satisfaction, which is a commercial stakeholder orientation.

⚠ **LLM inconsistency**: runs gave ['commercial', 'product', 'commercial']

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on calls to pair-program through complex issues."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize reactive, responsive execution (responding, triaging, jumping on) rather than proactive direction-setting or strategic autonomy.

**Run 2:** `mixed` ✓
> Quote: "Develop and execute strategies to grow and engage the analytics engineering community around Lightdash."
> Verified: ✓ found in JD
> Reasoning: The role includes strategic responsibility for developing community growth strategies alongside execution-focused responsibilities for daily support, teaching, and content creation.

**Run 3:** `mixed` ✓
> Quote: "Develop and execute strategies to grow and engage the analytics engineering community"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting for community growth with execution-focused responsibilities in user support, content creation, and event representation.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'mixed']

### ai_role
**Manual:** ``

**Run 1:** `ai_user` ✗
> Quote: "You'll use AI tools daily—for task management, technical problem-solving, analytics engineering work, and potentially contributing to our codebase."
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI tools daily for personal productivity and work acceleration, not to build AI-ready data infrastructure for other systems.

**Run 2:** `ai_user` ✗
> Quote: "Proficient with AI coding assistants and productivity tools; you should be comfortable using AI to write code, debug issues, and accelerate your work"
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI tools for personal productivity, coding, and problem-solving, not to build AI infrastructure or data systems for others.

**Run 3:** `ai_user` ✗
> Quote: "You'll use AI tools daily—for task management, technical problem-solving, analytics engineering work, and potentially contributing to our codebase."
> Verified: ✓ found in JD
> Reasoning: The JD expects the candidate to use AI coding assistants and productivity tools daily to accelerate their own work and productivity.

⚠ **Disagreement**: manual=`` vs LLM majority=`ai_user`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "diagnosing issues, answering questions, and pair-programming through problems"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reactive problem-solving and debugging but contains no mention of testing frameworks, data quality ownership, data contracts, or observability practices.

**Run 2:** `absent` ✗
> Quote: "Strong hands-on experience with dbt, SQL, data modeling, and modern data stacks"
> Verified: ✓ found in JD
> Reasoning: dbt is mentioned as a required skill, but there is no mention of testing, data contracts, data quality frameworks, or observability practices.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality signals"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no references to testing frameworks, data contracts, observability, SLOs, or data reliability practices.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role in positive terms of user success and capability delivery, without language about preventing bad outcomes, compliance, regulatory risk, or data governance.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role around user success, capability delivery, and community improvement with no mention of compliance, reliability risks, pipeline stability, or preventing bad outcomes.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role entirely around user success and capability building with no emphasis on preventing failures, compliance, or risk management.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
