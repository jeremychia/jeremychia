# Trace: 2026-06-27_preply_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Preply

**Location:** Barcelona
**Date Posted:** 2026-06-27

---

Senior Analytics Engineer
Location
Barcelona

Employment Type
Full time

Location Type
Hybrid

Department
Data

Overview
Application
We power people's progress.
At Preply, we're all about creating life-changing learning experiences. We help people discover the magic of the perfect tutor, craft a personalised learning journey, and stay motivated to keep growing. Our approach is human-led, tech-enabled - and it's creating real impact.

We've just reached unicorn status with a $150M Series D, accelerating our vision to transform education through human-led, AI-enhanced learning. Today, 100,000+ tutors teach 90+ languages to learners in 180 countries - and we're only getting started. As a category-defining company, we're shaping what the future of learning looks like at global scale.

Every Preply lesson sparks change, fuels ambition, and drives progress that matters. Joining Preply means helping define the future of education at global scale, and building something that truly matters for millions of people, every day.

Meet the team!
At Preply, we run hundreds of A/B tests at any given time, each with unique tracking and analytical challenges. Our platform spans a diverse product ecosystem, with sophisticated tutor-learner interactions that generate a vast amount of data. This creates an exciting, high-impact environment where data engineering plays a crucial role in shaping our business decisions.

We are passionate about building a modern data infrastructure that enables our teams to extract insights, optimize experiments, and power innovation. As an Analytics Engineer, you will help shape critical data models, streamline pipelines, and optimize our analytics stack to empower decision-making across the company.

Why You'll Love This Role
Cutting-edge data stack: work with DBT, Snowflake, Airflow, Looker, Databricks, Monte Carlo, and help shape our future tech choices.

End-to-End impact: own and evolve the entire data pipeline, from ingestion to transformation and modeling, ensuring accuracy, scalability, and performance.

Cross-team collaboration: partner with data scientists, analysts, and engineers to create high-quality, actionable datasets for business insights.

Continuous learning & growth: be part of a data-driven culture where innovation, best practices, and ownership drive success.

What you will be doing
Lead the architecture, design, and evolution of complex data models ensuring clarity, accessibility, scalability, and reliability.

Develop and optimize sophisticated ETL/ELT pipelines, enhancing performance and scalability within our multi-terabyte data ecosystem.

Own and enhance our BI layer (Looker via LookML), ensuring intuitive, performant, and scalable self-service analytics.

Provide technical leadership in collaboration with data science teams to optimize analytical workflows, reduce redundancy, and enforce robust data governance.

Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring.

Drive initiatives ensuring data reliability, cleanliness, accuracy, and comprehensive documentation for critical business decision-making.

Strategically influence and drive company-wide data strategies supporting rapid product growth, sophisticated experimentation, and large-scale personalization initiatives.

What you need to succeed
5+ years of hands-on experience in analytics engineering, data engineering, or related fields.

Expert proficiency in SQL and Python, with a proven track record in designing, implementing, and optimizing data models.

Deep understanding of advanced data governance frameworks, modeling best practices, and implementation of scalable self-service analytics platforms.

Exceptional blend of technical skills, business acumen, and compelling communication skills to effectively persuade and influence stakeholders…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 3 | 3 | 3 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | hiring_manager | 33% |
| stakeholder_orientation | product | product | internal_data | 33% |
| autonomy_level | strategic | strategic | strategic | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes engineering best practices, CI/CD pipelines, and rigorous automated data quality monitoring as core responsibilities.

**Run 2:** `rigour`
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section is dominated by signals of quality, governance, best practices, and data reliability, significantly outnumbering the few passing references to fast-paced culture.

**Run 3:** `rigour`
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring."
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize engineering best practices, CI/CD, automated quality monitoring, data reliability, and governance as core expectations, with no velocity signals like 'fast-paced' or 'ship quickly' in the job responsibilities.

### domain_risk

**Run 1:** `moderate`
> Quote: "Drive initiatives ensuring data reliability, cleanliness, accuracy, and comprehensive documentation for critical business decision-making."
> Verified: ✓ found in JD
> Reasoning: The role emphasizes accuracy and documentation for critical business decisions, but without explicit financial reporting, regulatory compliance, or mission-critical operational signals typical of high-risk domains.

**Run 2:** `moderate`
> Quote: "ensuring data reliability, cleanliness, accuracy, and comprehensive documentation for critical business decision-making"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes business decision impact but lacks explicit references to financial reporting, regulatory compliance, or audit requirements typical of high-risk domains.

**Run 3:** `moderate`
> Quote: "At Preply, we run hundreds of A/B tests at any given time, each with unique tracking and analytical challenges."
> Verified: ✓ found in JD
> Reasoning: The role primarily supports experimentation and business decision-making in an ed-tech SaaS platform without explicit financial reporting, regulatory compliance, or direct revenue impact.

### collaboration_width

**Run 1:** `3`
> Quote: "partner with data scientists, analysts, and engineers to create high-quality, actionable datasets for business insights"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct partner groups: data scientists, analysts, and engineers.

**Run 2:** `3`
> Quote: "partner with data scientists, analysts, and engineers to create high-quality, actionable datasets for business insights"
> Verified: ✓ found in JD
> Reasoning: Three distinct named groups are explicitly identified as collaborators: data scientists, analysts, and engineers.

**Run 3:** `3`
> Quote: "Cross-team collaboration: partner with data scientists, analysts, and engineers to create high-quality, actionable datasets for business insights."
> Verified: ✓ found in JD
> Reasoning: Three distinct named teams are identified: data scientists, analysts, and engineers.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Own and enhance our BI layer (Looker via LookML), ensuring intuitive, performant, and scalable self-serve analytics."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD references named tools and existing infrastructure being enhanced and evolved, rather than building from zero, indicating an existing but growing data function.

**Run 2:** `mid`
> Quote: "work with DBT, Snowflake, Airflow, Looker, Databricks, Monte Carlo, and help shape our future tech choices"
> Verified: ✓ found in JD
> Reasoning: Multiple existing named tools indicate established infrastructure at scale, while 'help shape future tech choices' suggests active evolution rather than greenfield building or mature consolidation.

**Run 3:** `mid`
> Quote: "Develop and optimize sophisticated ETL/ELT pipelines, enhancing performance and scalability within our multi-terabyte data ecosystem."
> Verified: ✓ found in JD
> Reasoning: Named tools already deployed (Snowflake, DBT, Airflow, Looker, Databricks, Monte Carlo), multi-terabyte data volume, and responsibilities focused on optimization and enhancement signal an established data function at scale, not greenfield.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Develop and optimize sophisticated ETL/ELT pipelines, enhancing performance and scalability within our multi-terabyte data ecosystem."
> Verified: ✓ found in JD
> Reasoning: The context-specific details about multi-terabyte scale and named tools indicate someone familiar with the actual job and its technical constraints.

**Run 2:** `mixed`
> Quote: "Develop and optimize sophisticated ETL/ELT pipelines, enhancing performance and scalability within our multi-terabyte data ecosystem."
> Verified: ✓ found in JD
> Reasoning: Specific technical context (multi-terabyte scale, ETL/ELT work) shows hiring manager knowledge, while other responsibilities use generic action verbs, creating a mixed pattern.

**Run 3:** `hiring_manager`
> Quote: "Own and enhance our BI layer (Looker via LookML), ensuring intuitive, performant, and scalable self-serve analytics."
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific tool context (Looker via LookML) and precise application knowledge (self-serve analytics at scale) demonstrate technical specificity that only comes from someone who has done this role.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `product`
> Quote: "Strategically influence and drive company-wide data strategies supporting rapid product growth, sophisticated experimentation, and large-scale personalization initiatives."
> Verified: ✓ found in JD
> Reasoning: The role's strategic purpose is to support product growth and experimentation, indicating the primary stakeholders are product and growth teams.

**Run 2:** `product`
> Quote: "Strategically influence and drive company-wide data strategies supporting rapid product growth, sophisticated experimentation, and large-scale personalization initiatives."
> Verified: ✓ found in JD
> Reasoning: The strategic framing emphasizes product growth, A/B testing, and experimentation as the primary use case, positioning product teams as the main beneficiary of this analytics infrastructure.

**Run 3:** `internal_data`
> Quote: "Own and enhance our BI layer (Looker via LookML), ensuring intuitive, performant, and scalable self-serve analytics."
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary focus is building and maintaining analytics infrastructure and self-serve platforms for internal data consumers (analysts, data scientists), not directly serving commercial, product, or finance stakeholders.

⚠ **LLM inconsistency**: runs gave ['product', 'product', 'internal_data']

### autonomy_level

**Run 1:** `strategic`
> Quote: "Lead the architecture, design, and evolution of complex data models ensuring clarity, accessibility, scalability, and reliability."
> Verified: ✓ found in JD
> Reasoning: The role is expected to lead the design and evolution of data models and architecture, indicating decision-making authority rather than execution of direction set by others.

**Run 2:** `strategic`
> Quote: "Strategically influence and drive company-wide data strategies supporting rapid product growth, sophisticated experimentation, and large-scale personalization initiatives."
> Verified: ✓ found in JD
> Reasoning: The repeated use of action verbs like 'lead,' 'shape,' 'drive,' and 'strategically influence' indicates the role is expected to set company-wide direction rather than execute against defined priorities.

**Run 3:** `strategic`
> Quote: "Strategically influence and drive company-wide data strategies supporting rapid product growth, sophisticated experimentation, and large-scale personalization initiatives."
> Verified: ✓ found in JD
> Reasoning: The explicit expectation to 'strategically influence and drive company-wide data strategies' indicates the role sets direction for data infrastructure and priorities, not executing direction set by others.

### ai_role
**Run 1:** `none` ✓
> Quote: "Strategically influence and drive company-wide data strategies supporting rapid product growth, sophisticated experimentation, and large-scale personalization initiatives."
> Reasoning: No explicit AI skill expected; personalization context present but no signal of building AI infrastructure or using AI coding tools.

**Run 2:** `none` ✓
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring"
> Reasoning: Standard AE work with no AI tool usage, enablement, or GenAI infrastructure expectations.

**Run 3:** `none` ✓
> Quote: "Develop and optimize sophisticated ETL/ELT pipelines, enhancing performance and scalability within our multi-terabyte data ecosystem."
> Reasoning: Standard analytics engineering work with no AI skill signals or enablement responsibilities.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring."
> Reasoning: Candidate owns quality practice through 'Champion' ownership language and explicit responsibility for automated data quality monitoring.

**Run 2:** `responsibility` ✓
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring"
> Reasoning: Ownership verb 'champion' combined with 'rigorous automated data quality monitoring' signals candidate-owned testing practice.

**Run 3:** `responsibility` ✓
> Quote: "Champion engineering best practices, including advanced version control, CI/CD pipelines for analytics, and rigorous automated data quality monitoring."
> Reasoning: Ownership verbs (champion, drive, own, ensure) paired with explicit quality monitoring and testing practice signals.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Drive initiatives ensuring data reliability, cleanliness, accuracy, and comprehensive documentation for critical business decision-making."
> Reasoning: Operational reliability framing dominates (data quality, reliability, cleanliness) without explicit compliance or regulatory language.

**Run 2:** `moderate` ✓
> Quote: "Drive initiatives ensuring data reliability, cleanliness, accuracy, and comprehensive documentation for critical business decision-making"
> Reasoning: Operational reliability concern framed around impact to business decision-making, not regulatory or compliance urgency.

**Run 3:** `moderate` ✓
> Quote: "Drive initiatives ensuring data reliability, cleanliness, accuracy, and comprehensive documentation for critical business decision-making."
> Reasoning: Operational reliability and data quality impact on decision-making emphasized, but without compliance or regulatory framing.

