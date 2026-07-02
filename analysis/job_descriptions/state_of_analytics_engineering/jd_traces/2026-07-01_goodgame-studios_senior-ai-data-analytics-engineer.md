# Trace: 2026-07-01_goodgame-studios_senior-ai-data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior AI Data & Analytics Engineer — Goodgame Studios

**URL:** https://goodgamestudios.teamtailor.com/jobs/7936415-senior-ai-data-analytics-engineer?promotion=2077806-trackable-share-link-senior-ai-data-analytics-engineer
**Location:** Not stated in JD
**Date Posted:** 2026-07-01

---

Senior AI Data & Analytics Engineer at Goodgame Studios

Role Summary
This position focuses on building analytics infrastructure for a new mobile game using AI-native workflows. The role emphasises hands-on experience with agentic AI tools and the judgment to oversee AI-generated analytics work.

Key Responsibilities

Data Foundation: Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting. Own data correctness and investigate quality anomalies.

AI-Native Analytics: Build semantic layers translating raw data into validated concepts. Develop AI-driven reporting and insight workflows. Review AI-generated code on critical paths before production deployment.

Product Intelligence: Identify opportunities and risks in gameplay data. Support product and design teams with actionable recommendations derived from complex datasets.

Agentic Standards: Help establish organisational adoption patterns for AI-assisted engineering, including review processes and quality gates.

Required Experience
- Several years building production analytics systems, preferably gaming/mobile
- Demonstrated expertise using LLMs and agentic workflows in production
- Concrete experience structuring prompts, managing multi-agent workflows, and reviewing AI-generated outputs
- Strong Python and SQL skills with ability to verify results independently
- Experience designing scalable data architectures and pipelines
- Cloud-based data platform familiarity
- Strong analytical decomposition skills and the ability to translate ambiguous business questions into precise analytical problems
- Independent initiative ownership and excellent English communication

Nice-to-Have Skills
Gaming/mobile analytics experience, event-driven architectures, real-time telemetry systems, published work on agentic workflows.

Interview Approach
Candidates should demonstrate actual agentic workflows they've built, including specifications, failure points, and oversight mechanisms.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | early | mid | 33% |
| jd_authorship | hiring_manager | mixed | hiring_manager | 33% |
| stakeholder_orientation | internal_data | product | product | 33% |
| autonomy_level | strategic | strategic | mixed | 33% |
| ai_role | ai_enabler | ai_enabler | ai_enabler | 100% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Review AI-generated code on critical paths before production deployment"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize code review, quality gates, data correctness verification, and preventing bad outputs from reaching production—all rigour signals with no velocity language present.

**Run 2:** `rigour`
> Quote: "Own data correctness and investigate quality anomalies"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data correctness, quality investigation, and quality gates with no velocity language such as speed, iteration, or shipping pace.

**Run 3:** `rigour`
> Quote: "Own data correctness and investigate quality anomalies"
> Verified: ✓ found in JD
> Reasoning: The role explicitly prioritizes data correctness, quality investigation, and code review processes, emphasizing rigour over delivery velocity.

### domain_risk

**Run 1:** `moderate`
> Quote: "building analytics infrastructure for a new mobile game"
> Verified: ✓ found in JD
> Reasoning: Gaming analytics affects business decisions but lacks explicit financial reporting, regulatory compliance, or audit language that would signal high risk.

**Run 2:** `moderate`
> Quote: "Product Intelligence: Identify opportunities and risks in gameplay data"
> Verified: ✓ found in JD
> Reasoning: Gaming analytics affects gameplay decisions and game design but lacks financial reporting, regulatory compliance, or audit language that would indicate high risk.

**Run 3:** `moderate`
> Quote: "Identify opportunities and risks in gameplay data"
> Verified: ✓ found in JD
> Reasoning: This is business intelligence for product decisions in gaming, not financial reporting or compliance-driven analytics.

### collaboration_width

**Run 1:** `2`
> Quote: "product and design teams"
> Verified: ✓ found in JD
> Reasoning: Only two distinct named partner functions—product and design—are explicitly listed as collaboration partners in the responsibilities.

**Run 2:** `2`
> Quote: "product and design teams"
> Verified: ✓ found in JD
> Reasoning: Two explicitly named collaboration partners: Product and Design teams.

**Run 3:** `2`
> Quote: "product and design teams"
> Verified: ✓ found in JD
> Reasoning: Two distinct named teams are explicitly listed as collaborative partners: Product and Design.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Help establish organisational adoption patterns for AI-assisted engineering, including review processes and quality gates"
> Verified: ✓ found in JD
> Reasoning: The role combines building new domain-specific infrastructure with helping establish organizational adoption patterns, indicating a growing data function scaling practices beyond a single domain.

**Run 2:** `early`
> Quote: "This position focuses on building analytics infrastructure for a new mobile game using AI-native workflows"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building analytics infrastructure from scratch for a new game with no mention of existing systems to scale or improve.

**Run 3:** `mid`
> Quote: "Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting"
> Verified: ✓ found in JD
> Reasoning: The role involves designing new analytics infrastructure for a new game initiative while the company establishes AI engineering patterns, indicating growth/scaling rather than greenfield or fully mature operations.

⚠ **LLM inconsistency**: runs gave ['mid', 'early', 'mid']

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Build semantic layers translating raw data into validated concepts. Develop AI-driven reporting and insight workflows. Review AI-generated code on critical paths before production deployment."
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical methodologies—semantic layers, agentic workflows, AI-generated code oversight—that reflect deep domain knowledge of how this particular role operates.

**Run 2:** `mixed`
> Quote: "Concrete experience structuring prompts, managing multi-agent workflows, and reviewing AI-generated outputs"
> Verified: ✓ found in JD
> Reasoning: Specific technical requirements around AI and agentic workflows indicate hiring manager input, while much of the role description uses generic data analytics action verbs.

**Run 3:** `hiring_manager`
> Quote: "Concrete experience structuring prompts, managing multi-agent workflows, and reviewing AI-generated outputs"
> Verified: ✓ found in JD
> Reasoning: The JD contains highly specific technical context about agentic workflows, prompt engineering, and AI code review that reflects actual job duties, not generic boilerplate.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Help establish organisational adoption patterns for AI-assisted engineering, including review processes and quality gates"
> Verified: ✓ found in JD
> Reasoning: The majority of responsibilities focus on building data infrastructure and establishing standards for the data organization itself rather than serving commercial, product, or finance stakeholders.

**Run 2:** `product`
> Quote: "Support product and design teams with actionable recommendations derived from complex datasets"
> Verified: ✓ found in JD
> Reasoning: The primary audience and impact is the product and design teams for gameplay intelligence and game design recommendations.

**Run 3:** `product`
> Quote: "Support product and design teams with actionable recommendations derived from complex datasets"
> Verified: ✓ found in JD
> Reasoning: The primary audience for the analytics work is explicitly the product and design teams, with a section titled 'Product Intelligence' focused on their decision support.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'product', 'product']

### autonomy_level

**Run 1:** `strategic`
> Quote: "Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting. Own data correctness"
> Verified: ✓ found in JD
> Reasoning: The role uses strong directional verbs (Design, Own) and is framed around setting architecture and data standards rather than executing pre-scoped work.

**Run 2:** `strategic`
> Quote: "Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting"
> Verified: ✓ found in JD
> Reasoning: The role uses strategic verbs (design, own, build, develop, establish) that indicate the candidate defines direction and architecture.

**Run 3:** `mixed`
> Quote: "Design end-to-end gameplay analytics architecture covering tracking, storage, processing, and reporting"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of analytics architecture design and data standards with execution in service of product team priorities.

⚠ **LLM inconsistency**: runs gave ['strategic', 'strategic', 'mixed']

### ai_role

**Run 1:** `ai_enabler`
> Quote: "Build semantic layers translating raw data into validated concepts. Develop AI-driven reporting and insight workflows."
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to build data infrastructure and semantic models that AI systems consume and operate on, not merely use AI tools for personal coding acceleration.

**Run 2:** `ai_enabler`
> Quote: "Build semantic layers translating raw data into validated concepts. Develop AI-driven reporting and insight workflows."
> Verified: ✓ found in JD
> Reasoning: The candidate builds data infrastructure (semantic layers, AI-driven workflows) that AI systems consume, requiring expertise with LLMs and agentic workflows to understand what to build for.

**Run 3:** `ai_enabler`
> Quote: "Build AI-driven reporting and insight workflows"
> Verified: ⚠ NOT found verbatim
> Reasoning: The candidate is expected to build analytics infrastructure with embedded AI workflows and establish organizational adoption patterns for AI systems, not just use AI tools for personal productivity.

### testing_framing

**Run 1:** `responsibility`
> Quote: "Own data correctness and investigate quality anomalies"
> Verified: ✓ found in JD
> Reasoning: Data correctness and quality investigation are framed with the ownership verb 'own', indicating the candidate is accountable for defining and maintaining data quality practices.

**Run 2:** `responsibility`
> Quote: "Own data correctness and investigate quality anomalies"
> Verified: ✓ found in JD
> Reasoning: Data correctness and quality are framed as responsibilities the candidate owns using the verb "own", indicating accountability for quality practices.

**Run 3:** `responsibility`
> Quote: "Own data correctness and investigate quality anomalies"
> Verified: ✓ found in JD
> Reasoning: Data quality and correctness are framed as candidate's owned responsibilities requiring investigation and oversight, not as tools deployed within a testing framework.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Review AI-generated code on critical paths before production deployment"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability—preventing bad code and data anomalies in production—but frames these as delivery stability concerns rather than compliance or stakeholder trust risks.

**Run 2:** `moderate`
> Quote: "Review AI-generated code on critical paths before production deployment"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes operational reliability and quality gates to prevent bad code in production, but lacks regulatory or compliance language that would indicate high loss aversion.

**Run 3:** `moderate`
> Quote: "Review AI-generated code on critical paths before production deployment"
> Verified: ✓ found in JD
> Reasoning: Operational reliability and preventing production failures are important (code review, quality gates), but the JD lacks regulatory, compliance, or stakeholder trust framing that would indicate high loss-aversion.
