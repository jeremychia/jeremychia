# Trace: 2026-06-27_protolabs_senior-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Senior Analytics Engineer — Protolabs

**Location:** Amsterdam
**Date Posted:** 2026-06-27

---

Protolabs - Analytics Engineer

Analytics Engineer
Amsterdam
Technology – Software Engineering / Full-time / Hybrid

Be yourself at Protolabs

Studies have shown that women and people of color are less likely to apply to jobs unless they meet every single qualification. We are an equal opportunity employer, and we are committed to building a diverse team that feels they are valued in the workplace. So do you feel you do not meet every single requirement but still intrigued? We encourage you to still apply! You can help make our company even better. We do not discriminate based on race, color, national origin, sexual orientation, gender, age, mental or physical ability, or any way you represent yourself. We strongly believe diversity makes for more successful teams.

Why Protolabs?

We are the leaders in digital manufacturing. We hire doers, makers, and creative thinkers who tackle our roles with an entrepreneurial spirit. Our culture is centered around meaningful work that brings new and innovative products to market at unprecedented speeds. We are a diverse team that comes from all walks of life and take pride in our team who is smart, genuine, humble, and passionate about what we do. It's our people who fuel our creativity and make our culture feel like home.

We are looking for a Senior Analytics Engineer to join our team! This is a hybrid role, and we are accepting applications from candidates based in the Netherlands.

The Senior Analytics Engineer plays a critical role in shaping and scaling the data foundations that support analytics and decision‑making across the organization. This role transforms complex, raw data into reliable, well‑structured data products that analysts and business partners can confidently use to drive insights. Sitting at the intersection of data engineering and business analytics, the Senior Analytics Engineer brings deep technical expertise—particularly in dbt and large‑scale transformation design—to guide the evolution of the analytics platform. Working closely with the Principal Analytics Engineer, this role accelerates the migration from legacy DOMO pipelines to a modern data stack, establishes robust modeling and testing standards, and helps elevate technical best practices across the Analytics Engineering team.

What you'll do

Design, build, and maintain complex, scalable dbt models and projects in large, multi domain environments
Act as the team's dbt expert, including refactoring complex transformations, resolving performance issues, and exploring, evaluating, and introducing advanced dbt features where they add clear value
Accelerate the migration from legacy DOMO pipelines to the modern data platform in close collaboration with the Principal Analytics Engineer
Help shape and refine shared approaches to data modeling, documentation, dbt project structure, and overall transformation practices as the platform scales
Support the team in using AI powered IDEs, coding assistants, agents, and automation tools to improve development workflows and productivity
Guide and support the growth of other Analytics Engineers, helping them strengthen dbt, SQL, modeling, and problem solving skills
Collaborate with business stakeholders to understand workflows and metrics, translating real world logic into clear, reliable data models
Provide Analytics Engineering coverage during EU business hours, partnering closely with EU based stakeholders.

What you'll bring

Education and Experience:
Bachelor's Degree in Computer Science, Software Engineering, Mathematics, Data Engineering, or a related field
Minimum of 5 years of experience in analytics engineering, data modeling, or data transformation
Extensive hands on experience with dbt (or similar transformation tools such as SQLMesh), ideally in large, complex, multi project environments
Advanced SQL skills, with the ability to refactor complex queries, simplify…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 0 | 1 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | mixed | mixed | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "establishes robust modeling and testing standards, and helps elevate technical best practices across the Analytics Engineering team"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing standards, robust practices, and technical excellence as core expectations, with no emphasis on speed or shipping pace.

**Run 2:** `rigour`
> Quote: "establishes robust modeling and testing standards"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes testing, quality, standards, and robust practices as core expectations, with no velocity language like 'fast-paced' or 'rapid delivery.'

**Run 3:** `rigour`
> Quote: "establish robust modeling and testing standards, and helps elevate technical best practices across the Analytics Engineering team"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes testing, standards, reliability, and technical excellence (6+ rigour signals) far more than speed or delivery pace (2-3 velocity signals).

### domain_risk

**Run 1:** `moderate`
> Quote: "transforms complex, raw data into reliable, well‑structured data products that analysts and business partners can confidently use to drive insights"
> Verified: ✓ found in JD
> Reasoning: The data supports business analytics and decision-making but the JD contains no mention of financial reporting, regulatory compliance, or direct revenue impact.

**Run 2:** `moderate`
> Quote: "transforms complex, raw data into reliable, well‑structured data products that analysts and business partners can confidently use to drive insights"
> Verified: ✓ found in JD
> Reasoning: Business intelligence and operational reporting influence decision-making but lack explicit regulatory, compliance, or financial reporting requirements.

**Run 3:** `moderate`
> Quote: "This role transforms complex, raw data into reliable, well‑structured data products that analysts and business partners can confidently use to drive insights."
> Verified: ✓ found in JD
> Reasoning: Data errors affect business decision-making, but the JD contains no financial reporting, compliance, regulatory, or audit language that would indicate high risk.

### collaboration_width

**Run 1:** `1`
> Quote: "Principal Analytics Engineer"
> Verified: ✓ found in JD
> Reasoning: Only the Principal Analytics Engineer is explicitly named as a distinct collaborating role; other stakeholders referenced generically as 'business stakeholders' rather than named functions.

**Run 2:** `0`
> Quote: "Collaborate with business stakeholders to understand workflows and metrics"
> Verified: ✓ found in JD
> Reasoning: The JD references only generic 'business stakeholders' without naming specific partner teams like Finance, Product, or Marketing.

**Run 3:** `1`
> Quote: "analysts"
> Verified: ✓ found in JD
> Reasoning: Only 'analysts' counts as a named role cohort; 'business partners' and 'business stakeholders' are generic terms that fall into the do-not-count category.

⚠ **LLM inconsistency**: runs gave ['1', '0', '1']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Guide and support the growth of other Analytics Engineers, helping them strengthen dbt, SQL, modeling, and problem solving skills"
> Verified: ✓ found in JD
> Reasoning: The presence of multiple Analytics Engineers and an established Principal Analytics Engineer role, combined with active growth initiatives and tool scaling, indicates a maturing data function beyond early stage.

**Run 2:** `mid`
> Quote: "Working closely with the Principal Analytics Engineer, this role accelerates the migration from legacy DOMO pipelines to a modern data stack"
> Verified: ✓ found in JD
> Reasoning: Multiple data roles, existing infrastructure being migrated, and platform scaling indicate an established data function in growth phase.

**Run 3:** `mid`
> Quote: "Working closely with the Principal Analytics Engineer, this role accelerates the migration from legacy DOMO pipelines to a modern data stack"
> Verified: ✓ found in JD
> Reasoning: The presence of a Principal Analytics Engineer, multiple Analytics Engineers, and existing legacy infrastructure indicates an established team modernizing rather than early-stage building.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Act as the team's dbt expert, including refactoring complex transformations, resolving performance issues, and exploring, evaluating, and introducing advanced dbt features where they add clear value"
> Verified: ✓ found in JD
> Reasoning: The specific technical depth about dbt optimization, performance troubleshooting, and feature evaluation can only come from someone who has done this work hands-on.

**Run 2:** `hiring_manager`
> Quote: "Act as the team's dbt expert, including refactoring complex transformations, resolving performance issues, and exploring, evaluating, and introducing advanced dbt features where they add clear value"
> Verified: ✓ found in JD
> Reasoning: Specific technical details about dbt work, transformation challenges, and advanced features indicate authorship by someone with hands-on experience in this role.

**Run 3:** `hiring_manager`
> Quote: "Act as the team's dbt expert, including refactoring complex transformations, resolving performance issues, and exploring, evaluating, and introducing advanced dbt features where they add clear value"
> Verified: ✓ found in JD
> Reasoning: The specific technical detail about dbt expertise, transformation refactoring, and performance optimization can only come from someone with hands-on experience in this role.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "transforms complex, raw data into reliable, well‑structured data products that analysts and business partners can confidently use to drive insights"
> Verified: ✓ found in JD
> Reasoning: The primary mission is building reliable data infrastructure and products for internal analytics consumers rather than external commercial, product, or financial stakeholders.

**Run 2:** `internal_data`
> Quote: "transforms complex, raw data into reliable, well‑structured data products that analysts and business partners can confidently use to drive insights"
> Verified: ✓ found in JD
> Reasoning: The role primarily builds data infrastructure and products for internal use by analysts and data platform consumers rather than external commercial, product, or finance stakeholders.

**Run 3:** `internal_data`
> Quote: "establishes robust modeling and testing standards, and helps elevate technical best practices across the Analytics Engineering team"
> Verified: ✓ found in JD
> Reasoning: The role's primary focus is building analytics engineering infrastructure and standards for the data function itself, even though it engages with business users to inform requirements.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Help shape and refine shared approaches to data modeling, documentation, dbt project structure, and overall transformation practices as the platform scales"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic direction-setting over analytics engineering standards and practices with significant hands-on execution of complex modeling and transformation work.

**Run 2:** `mixed`
> Quote: "Help shape and refine shared approaches to data modeling, documentation, dbt project structure, and overall transformation practices"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of analytics engineering practices (shaping approaches, mentoring) with execution on the migration project directed by the Principal Analytics Engineer.

**Run 3:** `mixed`
> Quote: "Help shape and refine shared approaches to data modeling, documentation, dbt project structure, and overall transformation practices as the platform scales"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic ownership of technical domain practices (shaping standards, guiding team growth) with execution of technical work (designing and maintaining models, supporting teams).
