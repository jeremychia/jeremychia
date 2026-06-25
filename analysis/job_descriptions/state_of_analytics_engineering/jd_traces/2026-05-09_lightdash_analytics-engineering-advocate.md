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
| velocity_vs_rigour | velocity | mixed | mixed | rigour | 33% | ✗ |
| domain_risk | low | moderate | moderate | moderate | 100% | ✗ |
| collaboration_width | 3 | 0 | 2 | 0 | 33% | ✗ |
| data_team_maturity | early | mid | mid | mid | 100% | ✗ |
| jd_authorship | hiring_manager | mixed | hiring_manager | hiring_manager | 33% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `velocity`

**Run 1:** `mixed` ✗
> Quote: "You'll balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process improvement."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames the role as balancing speed with strategic depth, and the company values emphasize shipping at 80% while the role emphasizes teaching and best practices.

**Run 2:** `mixed` ✗
> Quote: "balance fast, practical solutions with thoughtful, strategic guidance on analytics architecture and process improvement"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly frames the role as balancing speed and strategic rigor, with velocity signals (fast, accelerate) appearing alongside rigorous language (thoughtful, best practices, maintain quality).

**Run 3:** `rigour` ✗
> Quote: "thoughtful, strategic guidance on analytics architecture and process improvement"
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals emphasize quality, expertise, and strategic thinking (world-class tutorials, best practices, process improvement, authenticity) far outweigh the single velocity signal of fast, practical solutions.

⚠ **Disagreement**: manual=`velocity` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'rigour']

### domain_risk
**Manual:** `low`

**Run 1:** `moderate` ✗
> Quote: "Deep understanding of business intelligence and analytics engineering workflows"
> Verified: ✓ found in JD
> Reasoning: The role is in the BI/analytics domain affecting business decisions but lacks explicit financial, compliance, or regulatory risk signals that would indicate high risk.

**Run 2:** `moderate` ✗
> Quote: "helping teams win with data"
> Verified: ✓ found in JD
> Reasoning: This is a SaaS BI tool company supporting analytics work, not directly responsible for financial reporting, compliance, or regulatory requirements, placing it in the moderate risk category.

**Run 3:** `moderate` ✗
> Quote: "help teams with everything from building dashboards and writing SQL to analytics engineering best practices and data modeling strategy"
> Verified: ✓ found in JD
> Reasoning: The role supports general business intelligence and decision-making without explicit mention of financial reporting, regulatory compliance, or other high-risk domains.

⚠ **Disagreement**: manual=`low` vs LLM majority=`moderate`

### collaboration_width
**Manual:** `3`

**Run 1:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: The JD mentions collaborating with users and community but does not explicitly name any internal partner teams or functions.

**Run 2:** `2` ✗
> Quote: "shared customer Slack channels; cultivating relationships with community members"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct collaboration partners are explicitly named: customers and community members.

**Run 3:** `0` ✗
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No named internal teams or functions are explicitly identified as collaboration partners in the role responsibilities.

⚠ **Disagreement**: manual=`3` vs LLM majority=`0`

⚠ **LLM inconsistency**: runs gave ['0', '2', '0']

### data_team_maturity
**Manual:** `early`

**Run 1:** `mid` ✗
> Quote: "You'll stay current with our latest features, including our evolving AI capabilities (using Lightdash for our own analytics and demos)"
> Verified: ✓ found in JD
> Reasoning: Lightdash has established internal analytics using their own product, suggesting a mid-stage data function that exists and is producing something but is not yet a large, highly specialized organization.

**Run 2:** `mid` ✗
> Quote: "using Lightdash for our own analytics and demos"
> Verified: ✓ found in JD
> Reasoning: The company has an established internal analytics function using their product, indicating a data team that exists and is operational but without signals of enterprise-scale maturity.

**Run 3:** `mid` ✗
> Quote: "You'll stay current with our latest features, including our evolving AI capabilities (using Lightdash for our own analytics and demos)"
> Verified: ✓ found in JD
> Reasoning: The company uses its own product internally for analytics and actively develops new features, indicating an established team beyond early stage but without evidence of multiple specialized sub-teams.

⚠ **Disagreement**: manual=`early` vs LLM majority=`mid`

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "You'll spend a significant portion of your time directly helping users in Slack and on calls — diagnosing issues, answering questions, and pair-programming through problems."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific details about day-to-day work (Slack support, pair-programming, dbt expertise) showing hiring manager insight, mixed with some generic community/growth language.

**Run 2:** `hiring_manager` ✓
> Quote: "You'll be active daily in shared customer Slack channels, responding to user questions, triaging bugs, and jumping on calls to pair-program through problems."
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain specific technical practices and concrete daily activities that demonstrate intimate familiarity with what this job entails, rather than generic boilerplate language.

**Run 3:** `hiring_manager` ✓
> Quote: "You'll spend a significant portion of your time directly helping users in Slack and on calls — diagnosing issues, answering questions, and pair-programming through problems."
> Verified: ✓ found in JD
> Reasoning: The responsibilities show specific understanding of actual daily work activities and concrete technical practices (pair programming, debugging, triaging) that indicate someone with direct experience in the role wrote this, rather than generic recruiter language.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']
