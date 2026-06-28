# Trace: 2026-06-27_bolt_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Bolt
**URL:** https://bolt.eu/en/careers/positions/ccb51f9f-2c97-4ed7-9d1c-dbced6a7ccd2/

**Location:** Tallinn, Estonia
**Date Posted:** 2026-06-27

---

About Bolt

Bolt is shaping a future where cities are built for people, not cars. What started as an ambitious project of a 19-year-old in 2013 has grown into a global mobility platform used by more than 200 million customers and 4.5 million driver and courier partners across 50 countries.

From ride-hailing and food delivery to scooters, e-bikes, and car-sharing, Bolt helps people move through cities every day. Small, autonomous teams drive this work, combining the speed and ownership of a startup with the scale of a global technology company backed by more than €1bn in funding.

And we're just getting started.

Why join Bolt?

Build the future of mobility and help transform how people live and move in cities.

Tackle challenges at scale that span technology, operations, regulation, and growth.

Take real ownership early. Small, lean teams mean your decisions matter from day one, and you'll learn fast alongside some of the best people in the industry.

Join one of Europe's leading technology companies, backed by world-class investors including Sequoia.

About the role

Our whole platform lives and breathes on data. Every step of our product development is powered by robust, scalable data infrastructure — and Analytics Engineers are the people who make that possible.

As an Analytics Engineer at Bolt, you work at the intersection of data engineering and product analytics. You own everything between data producers and data consumers: building the pipelines, models, and data products that empower analysts and decision-makers across the organisation. You're a sparring partner to our Product Analysts and a force multiplier for the teams you support.

We operate across four product verticals — Ride-Hailing, Delivery (Bolt Food and Bolt Market), Rentals (e-bikes, scooters, and carsharing), and Bolt Business — plus two horizontals: Platform and Incentives.

We have multiple open roles across these teams. Once you apply, you'll go through a universal process designed to help you learn more about Analytics Engineering at Bolt — and help us find the team that best matches your skills and ambitions.

If you believe great data infrastructure is what separates fast-moving organisations from slow ones, you'll fit right in. Scroll down to find out what it looks like day-to-day!

Main tasks and responsibilities

Work closely with product analysts and adjacent stakeholders to prioritize and align analytics engineering roadmaps, ensuring that solutions meet the long-term business needs.

Build, expand and maintain reusable data models and metrics in dbt.

Set up and manage the architecture, documentation, and key data transformations for in-house and third-party data.

Improve the efficiency and impact of product analysts through data products, processes, collaboration and active knowledge-sharing.

Develop strategic data products such as segmentation feature store or enable advanced solutions such as interactive metrics trees.

Follow system design and architectural best practices and closely collaborate with cross-functional stakeholders to ensure data integrity and efficiency across all processes.

About you

You hold a Bachelor and/or Master degree in Statistics, Economics, Data Science, Computer Science, Mathematics, Information Management, Business or similar studies.

You have significant experience with data modeling, developing analytics architectures for large volumes of data and can demonstrate tangible impact in the area.

You are proficient in SQL, Python, Spark, data modelling tools such as dbt and orchestration tools such as Apache Airflow.

You possess excellent knowledge of system design and architectural best practices with a focus on reusability, maintainability, reliability, and scalability.

You are a strong cross-functional collaborator with a good business sense and excellent communication skills in verbal and written Engl…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 1 | 1 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | mixed | strategic | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Follow system design and architectural best practices and closely collaborate with cross-functional stakeholders to ensure data integrity and efficiency across all processes."
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes architectural best practices, data integrity, reliability, and system design rather than speed or rapid delivery.

**Run 2:** `rigour`
> Quote: "Follow system design and architectural best practices and closely collaborate with cross-functional stakeholders to ensure data integrity and efficiency across all processes."
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize architectural best practices, data integrity, documentation, and reliability far more than speed or shipping pace.

**Run 3:** `rigour`
> Quote: "Follow system design and architectural best practices and closely collaborate with cross-functional stakeholders to ensure data integrity and efficiency across all processes."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals (system design best practices, data integrity, architectural best practices) dominate the responsibilities without equivalent velocity language.

### domain_risk

**Run 1:** `moderate`
> Quote: "Every step of our product development is powered by robust, scalable data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Data errors would affect operational decisions and product development, but the JD contains no language about financial reporting, compliance, or regulatory risk.

**Run 2:** `moderate`
> Quote: "Every step of our product development is powered by robust, scalable data infrastructure"
> Verified: ✓ found in JD
> Reasoning: Data errors affect product development decisions and operations, but the JD contains no explicit financial reporting, regulatory, compliance, or audit language.

**Run 3:** `moderate`
> Quote: "Every step of our product development is powered by robust, scalable data infrastructure"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data infrastructure for product development and analytics support without explicit financial reporting, compliance, or regulatory language.

### collaboration_width

**Run 1:** `1`
> Quote: "You're a sparring partner to our Product Analysts"
> Verified: ✓ found in JD
> Reasoning: Product Analysts is the only explicitly named team; other references like 'adjacent stakeholders' and 'cross-functional stakeholders' are too generic to count.

**Run 2:** `1`
> Quote: "product analysts"
> Verified: ✓ found in JD
> Reasoning: Only 'product analysts' is explicitly named as a partner team; other references like 'stakeholders', 'decision-makers', and 'teams you support' are generic.

**Run 3:** `1`
> Quote: "Product Analysts"
> Verified: ✓ found in JD
> Reasoning: Only Product Analysts are explicitly named as a distinct team; other references use generic terms like 'adjacent stakeholders' and 'cross-functional'.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Build, expand and maintain reusable data models and metrics in dbt."
> Verified: ✓ found in JD
> Reasoning: The language 'expand and maintain' signals an existing data infrastructure that is growing rather than being established from scratch, with multiple AE roles being hired.

**Run 2:** `mid`
> Quote: "Build, expand and maintain reusable data models and metrics in dbt."
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (dbt, Airflow, Spark) with existing infrastructure to maintain and expand, plus multiple open roles across teams, signal a growing but established data function.

**Run 3:** `mid`
> Quote: "Build, expand and maintain reusable data models and metrics in dbt"
> Verified: ✓ found in JD
> Reasoning: The 'expand' language combined with named tools in responsibilities (dbt, Airflow) and existing Product Analysts team indicates a data function that exists and is growing, not early-stage.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Develop strategic data products such as segmentation feature store or enable advanced solutions such as interactive metrics trees."
> Verified: ✓ found in JD
> Reasoning: Specific technical concepts like segmentation feature stores and interactive metrics trees demonstrate insider knowledge of what Analytics Engineers actually build, not recruiter boilerplate.

**Run 2:** `mixed`
> Quote: "Develop strategic data products such as segmentation feature store or enable advanced solutions such as interactive metrics trees."
> Verified: ✓ found in JD
> Reasoning: Specific technical details and examples (segmentation feature store, metrics trees, system design practices) suggest hiring manager input, but generic phrases like 'collaborate with stakeholders' and 'active knowledge-sharing' indicate recruiter involvement.

**Run 3:** `mixed`
> Quote: "Develop strategic data products such as segmentation feature store or enable advanced solutions such as interactive metrics trees"
> Verified: ✓ found in JD
> Reasoning: Specific product examples suggest hiring-manager input, but generic collaboration language indicates recruiter involvement.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "You own everything between data producers and data consumers"
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the internal data ecosystem and analytics infrastructure for other analysts and data consumers, not commercial, product, or finance stakeholders.

**Run 2:** `internal_data`
> Quote: "Improve the efficiency and impact of product analysts through data products, processes, collaboration and active knowledge-sharing."
> Verified: ✓ found in JD
> Reasoning: The role primarily serves the data function itself—enabling product analysts and building infrastructure for internal data consumers rather than direct commercial, product, or finance outcomes.

**Run 3:** `internal_data`
> Quote: "You own everything between data producers and data consumers: building the pipelines, models, and data products that empower analysts and decision-makers across the organisation."
> Verified: ✓ found in JD
> Reasoning: The role is fundamentally about building analytics infrastructure and data products for internal consumption by analysts and decision-makers.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Work closely with product analysts and adjacent stakeholders to prioritize and align analytics engineering roadmaps"
> Verified: ✓ found in JD
> Reasoning: The role owns the analytics engineering domain (strategic), but roadmap priorities and business needs are shaped by product analysts and stakeholders (execution context).

**Run 2:** `mixed`
> Quote: "You own everything between data producers and data consumers: building the pipelines, models, and data products that empower analysts and decision-makers across the organisation."
> Verified: ✓ found in JD
> Reasoning: The role has strategic ownership of the technical data domain ('own everything', 'set up and manage architecture', 'develop strategic data products') but executes in service of and collaboration with product analysts and business teams.

**Run 3:** `strategic`
> Quote: "You own everything between data producers and data consumers"
> Verified: ✓ found in JD
> Reasoning: Explicit ownership language combined with 'sparring partner' positioning and involvement in prioritizing analytics engineering roadmaps indicates strategic ownership of the analytics engineering function.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'strategic']
