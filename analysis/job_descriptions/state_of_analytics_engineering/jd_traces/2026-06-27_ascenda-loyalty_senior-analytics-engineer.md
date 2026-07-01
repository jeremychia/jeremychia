# Trace: 2026-06-27_ascenda-loyalty_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Ascenda Loyalty
**URL:** https://jobs.gem.com/ascenda-loyalty/am9icG9zdDofWVA0wxcjbbNzBTyR7eUG

**Location:** Singapore • Ho Chi Minh, Vietnam
**Date Posted:** 2026-06-27

---

Senior Analytics Engineer
Singapore • Ho Chi Minh, Vietnam
Engineering
Hybrid
Full-time
Great to Meet You! We are Ascenda

Ascenda powers the growth of leading financial services brands worldwide with premium rewards programs that differentiate their products, drive profitable customer behaviors, and create sustained engagement.

We are behind the world-class rewards propositions of major banks and fintechs around the globe, including brands like American Express, Capital One, Brex, Revolut, Ramp, HSBC, Bank of New Zealand, Virgin Money (Australia), Bradesco (Brazil), ANZ (Australia), HDFC (India) and many others.

We are a thriving global Loyalty as a Service company and experiencing rapid expansion. Join our dynamic finance team as one of its earliest leaders, contributing to the development of our financial planning strategies as we strive for hypergrowth. Our team spans 20 cities worldwide, with dual headquarters in Singapore and New York, totaling 250 team members.

Join us as a Senior Analytics Engineer in Singapore/Vietnam!
 
The Role
As an experienced Analytics Engineer in Ascenda's Data Team, you will act as a Data Architect and technical leader, designing, building, and governing our data medallion architecture to deliver reliable, scalable, and high-trust data products — serving both internal and external stakeholders.

You will shape how our loyalty-as-a-service business models its data, metrics, and data products for enterprise clients and partners.

You'll collaborate closely with product managers, commercial account managers, engineers, and data scientists in a modern, fast-moving environment that values autonomy, clarity, and measurable outcomes.
 
Your Impact
Architect the data foundations that enable both internal teams and global partners to turn raw data into trusted insights powering real business decisions.
Champion dimensional modelling principles, ensuring our medallion architecture scales efficiently with increasing data volume, variety, and complexity.
Design, standardise, and evolve our data modelling (dbt) frameworks to transform raw data into self-explanatory, performant, and reusable datasets for analytics and reporting.
Empower analysts, engineers, and business teams with high-quality semantic layers and data models that serve as a single source of truth across Ascenda and our partner ecosystem.
Drive excellence in our modern data stack — AWS Redshift, dbt, Airflow, Meltano, Python (Pandas, Jupyter) — ensuring performance, scalability, and maintainability.
Mentor analytics engineers, define best practices, and embed data quality, governance, and observability throughout our data stack.
Work closely with data engineers, scientists, and AI engineers to power machine learning workflows and predictive models.
 
Who You Are
5–10 years of experience in analytics engineering, data engineering, or data modelling within large-scale data environments (fintech, banking, e-commerce, telco, etc.).
Deep hands-on expertise with dbt, applying best practices in modular design, macros, reusable patterns, and unit testing.
Proven experience designing and evolving enterprise-scale data models (Kimball, Inmon, or Data Vault).
Strong SQL and Python skills, with a performance-driven mindset and production-ready practices (CI/CD, version control, monitoring).
Strong analytical and problem-solving skills, with the ability to draw insights and make data-driven recommendations.
Excellent business acumen — able to translate product and business stakeholder needs into scalable data models and semantic layers.
Outstanding communicator who can articulate architectural trade-offs and influence both technical and non-technical audiences.
Collaborative, proactive, and self-motivated, with a commitment to continuous learning and improvement.
Keeps up-to-date with emerging data and AI technologies, activel…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | high | high | moderate | 33% |
| collaboration_width | 6 | 6 | 6 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | hiring_manager | 33% |
| stakeholder_orientation | internal_data | mixed | internal_data | 33% |
| autonomy_level | strategic | strategic | strategic | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Mentor analytics engineers, define best practices, and embed data quality, governance, and observability throughout our data stack"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality, governance, observability, testing, and reliability across multiple paragraphs, vastly outweighing the single mention of a 'fast-moving environment'.

**Run 2:** `rigour`
> Quote: "designing, building, and governing our data medallion architecture to deliver reliable, scalable, and high-trust data products"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, governance, observability, testing, and standardization throughout, with no velocity signals driving the core responsibilities.

**Run 3:** `rigour`
> Quote: "design, building, and governing our data medallion architecture to deliver reliable, scalable, and high-trust data products"
> Verified: ⚠ NOT found verbatim
> Reasoning: Responsibilities emphasize reliability, governance, data quality, and observability with explicit mentions of testing practices and CI/CD—rigour signals outnumber velocity mentions by more than 2:1 despite references to a 'fast-moving environment'.

### domain_risk

**Run 1:** `high`
> Quote: "reliable, scalable, and high-trust data products — serving both internal and external stakeholders"
> Verified: ✓ found in JD
> Reasoning: The role operates in fintech serving major financial institutions (American Express, HSBC, Capital One), with explicitly stated 'high-trust data products' affecting public-facing loyalty program analytics at enterprise scale.

**Run 2:** `high`
> Quote: "We are behind the world-class rewards propositions of major banks and fintechs around the globe"
> Verified: ✓ found in JD
> Reasoning: The role operates within fintech/banking serving regulated financial institutions, where data errors directly impact financial operations and compliance.

**Run 3:** `moderate`
> Quote: "loyalty-as-a-service business models its data, metrics, and data products for enterprise clients and partners"
> Verified: ✓ found in JD
> Reasoning: While the fintech/banking sector inherently implies high financial risk, the JD uses generic data quality and architecture language rather than explicit financial reporting, regulatory, or compliance terminology.

⚠ **LLM inconsistency**: runs gave ['high', 'high', 'moderate']

### collaboration_width

**Run 1:** `6`
> Quote: "product managers; commercial account managers; engineers; data scientists; data engineers; analytics engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD names six distinct functions explicitly: Product (product managers), Commercial (commercial account managers), Engineering (engineers), Data Science (data scientists), Data Engineering (data engineers), and Analytics (analytics engineers).

**Run 2:** `6`
> Quote: "product managers; commercial account managers; engineers; data scientists; data engineers; AI engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names six distinct partner functions across product, commercial, software engineering, data, and AI domains.

**Run 3:** `6`
> Quote: "product managers; commercial account managers; engineers; data scientists; data engineers; AI engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct named teams appear across responsibilities: Product (product managers), Commercial (commercial account managers), Engineering (engineers), Data Science (data scientists), Data Engineering (data engineers), and AI/ML (AI engineers).

### data_team_maturity

**Run 1:** `mid`
> Quote: "Design, standardise, and evolve our data modelling (dbt) frameworks to transform raw data into self-explanatory, performant, and reusable datasets for analytics and reporting"
> Verified: ✓ found in JD
> Reasoning: The JD references existing infrastructure, tools, and frameworks (dbt, Redshift, Airflow, medallion architecture) being standardized and evolved, plus existing analytics engineers being mentored, indicating a growing team rather than greenfield or fully mature scale.

**Run 2:** `mid`
> Quote: "Mentor analytics engineers, define best practices, and embed data quality, governance, and observability throughout our data stack."
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (AWS Redshift, dbt, Airflow), multiple analytics engineers already present, but best practices still being defined indicates a growing team.

**Run 3:** `mid`
> Quote: "Mentor analytics engineers, define best practices, and embed data quality, governance, and observability throughout our data stack."
> Verified: ✓ found in JD
> Reasoning: The mention of an existing analytics engineering team to mentor, combined with named tools in responsibilities (dbt, Airflow, Redshift) and focus on evolving rather than building from zero, indicates mid-stage maturity with growth trajectory.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Design, standardise, and evolve our data modelling (dbt) frameworks to transform raw data into self-explanatory, performant, and reusable datasets for analytics and reporting"
> Verified: ✓ found in JD
> Reasoning: Responsibilities combine specific technical details (named tools with context: dbt, medallion architecture, dimensional modelling, Kimball/Inmon/Data Vault methodologies, CI/CD practices) alongside generic phrases like 'collaborate closely' and 'work with teams'.

**Run 2:** `hiring_manager`
> Quote: "Design, standardise, and evolve our data modelling (dbt) frameworks to transform raw data into self-explanatory, performant, and reusable datasets for analytics and reporting"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical architecture patterns (medallion, semantic layers), named tools with context (dbt frameworks, macros), and methodology references (Kimball, Inmon, Data Vault) that only come from hands-on experience.

**Run 3:** `hiring_manager`
> Quote: "Deep hands-on expertise with dbt, applying best practices in modular design, macros, reusable patterns, and unit testing."
> Verified: ✓ found in JD
> Reasoning: The JD contains technical specificity about dbt patterns, data vault methodologies, medallion architecture, and specific tool implementations that goes well beyond generic recruiter language, indicating authorship by someone with hands-on experience in this role.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Empower analysts, engineers, and business teams with high-quality semantic layers and data models that serve as a single source of truth across Ascenda and our partner ecosystem"
> Verified: ✓ found in JD
> Reasoning: The role's primary impact is enabling data team members and analytics consumers through infrastructure, platforms, and data models; external clients consume the data products these internal foundations enable.

**Run 2:** `mixed`
> Quote: "You will shape how our loyalty-as-a-service business models its data, metrics, and data products for enterprise clients and partners"
> Verified: ✓ found in JD
> Reasoning: The role serves both external commercial stakeholders (enterprise clients and partners) and internal data/engineering teams, with genuine emphasis on both.

**Run 3:** `internal_data`
> Quote: "Empower analysts, engineers, and business teams with high-quality semantic layers and data models that serve as a single source of truth across Ascenda and our partner ecosystem."
> Verified: ✓ found in JD
> Reasoning: The role's primary impact is designing and maintaining data infrastructure and models for internal and partner data consumers rather than serving a specific external business function like finance, product, or commercial teams.

⚠ **LLM inconsistency**: runs gave ['internal_data', 'mixed', 'internal_data']

### autonomy_level

**Run 1:** `strategic`
> Quote: "You will shape how our loyalty-as-a-service business models its data, metrics, and data products for enterprise clients and partners"
> Verified: ✓ found in JD
> Reasoning: The role is explicitly framed as 'technical leader' and 'Data Architect' with a mandate to define standards, mentor others, architect foundations, and champion modelling principles—all strategic verbs—rather than executing against others' priorities.

**Run 2:** `strategic`
> Quote: "act as a Data Architect and technical leader, designing, building, and governing our data medallion architecture"
> Verified: ✓ found in JD
> Reasoning: The JD positions this as a leadership role that architects, shapes, champions, and defines the data strategy rather than executing direction from others.

**Run 3:** `strategic`
> Quote: "You will shape how our loyalty-as-a-service business models its data, metrics, and data products for enterprise clients and partners."
> Verified: ✓ found in JD
> Reasoning: The explicit 'you will shape' language, combined with emphasis on defining architecture, establishing best practices, and mentoring the team, indicates the role is expected to set direction and priorities rather than execute against direction from others.

### ai_role
**Run 1:** `none` ✓
> Quote: "Design, standardise, and evolve our data modelling (dbt) frameworks"
> Reasoning: Standard data modeling work with no AI infrastructure, coding tools, or GenAI responsibilities mentioned.

**Run 2:** `none` ✓
> Quote: "Design, standardise, and evolve our data modelling (dbt) frameworks"
> Reasoning: Standard dbt/data modeling work with no signals of AI usage, GenAI, or AI-ready infrastructure.

**Run 3:** `none` ✓
> Quote: "AI engineers listed as collaborator; Empower analysts, engineers, and business teams with high-quality semantic layers"
> Reasoning: Semantic layers and AI engineers as stakeholders, but no explicit 'AI-ready', 'semantic model for AI', or 'GenAI' language in responsibilities.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "embed data quality, governance, and observability throughout our data stack"
> Reasoning: Verb 'embed' with 'data quality' establishes direct ownership of implementing quality practices.

**Run 2:** `responsibility` ✓
> Quote: "embed data quality, governance, and observability throughout our data stack"
> Reasoning: Ownership verb 'embed' combined with 'data quality' indicates candidate will establish and maintain quality practices.

**Run 3:** `responsibility` ✓
> Quote: "embed data quality, governance, and observability throughout our data stack"
> Reasoning: Embed (implement/establish) signals active ownership of quality and governance practices as core responsibility.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "embed data quality, governance, and observability throughout our data stack"
> Reasoning: Observability and reliability concerns dominate (moderate framing); governance elements hint at trust but lack explicit regulatory/compliance language.

**Run 2:** `moderate` ✓
> Quote: "embed data quality, governance, and observability throughout our data stack"
> Reasoning: Governance and observability framing reflect operational reliability and trust concerns for enterprise clients, neither compliance-driven (high) nor pure delivery-focused (none).

**Run 3:** `moderate` ✓
> Quote: "embed data quality, governance, and observability; enterprise clients and partners; scales efficiently"
> Reasoning: Governance framing and enterprise context suggest trust/operational concerns, but lack explicit regulatory/audit language.

