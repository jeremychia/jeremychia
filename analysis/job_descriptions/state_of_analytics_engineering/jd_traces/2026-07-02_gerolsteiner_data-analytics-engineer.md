# Trace: 2026-07-02_gerolsteiner_data-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Data & Analytics Engineer (m/w/d) — Gerolsteiner Brunnen GmbH & Co. KG

**URL:** https://gerolsteiner.softgarden.io/job/65116063/Data-Analytics-Engineer-m-w-d-?jobDbPVId=274846393&l=de
**Location:** Gerolstein, Germany
**Date Posted:** 2026-07-02

---

# Data & Analytics Engineer (m/w/d)

Company: Gerolsteiner Brunnen GmbH & Co. KG
Location: Gerolstein, Eifel region (Vulkanring 54567 Gerolstein), Germany
Salary: Not stated

## Responsibilities
The role encompasses developing and maintaining data models, queries, and views in SAP environments. Key duties include creating and optimizing reports, stories, and planning content within SAP Analytics Cloud and advancing existing Business Warehouse implementations. The engineer will integrate new data sources via Business Data Cloud and develop analytics solutions using Azure Databricks, including Power BI reports and dashboards. Additional responsibilities involve processing IoT and market data, unifying SAP and non-SAP system data, and supporting AI-driven analytics expansion.

## Requirements
Candidates need a completed IT degree or equivalent qualification with minimum two years' experience supporting SAP modules in manufacturing settings. Required expertise includes SAP Analytics covering modules like BW, BW/4HANA, SAC, or Datasphere. Additional prerequisites include proficiency with data modeling, reporting structures, and familiarity with artificial intelligence and machine learning concepts. Preferred qualifications involve prior exposure to SAP Business Data Cloud and programming skills in ABAP or Python. The ideal candidate demonstrates structured work habits, analytical thinking, teamwork capacity, and fluency in German and English.

## Benefits
The company offers hybrid flexible work arrangements, competitive compensation with social benefits, appreciative workplace culture, team events, professional development opportunities, and complimentary beverages at the office and for home use.

Contact: Ann-Kathrin Lux (ann-kathrin.lux@gerolsteiner.com)

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 0 | 0 | 0 | 0 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | hiring_manager | 100% | ✓ |
| stakeholder_orientation | internal_data | internal_data | internal_data | internal_data | 100% | ✓ |
| autonomy_level | execution | execution | execution | execution | 100% | ✓ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "creating and optimizing reports, stories, and planning content"
> Verified: ✓ found in JD
> Reasoning: The emphasis on 'optimizing' and 'maintaining' work products, combined with complete absence of velocity language, signals a focus on quality and precision rather than speed.

**Run 2:** `rigour` ✗
> Quote: "developing and maintaining data models, queries, and views"
> Verified: ✓ found in JD
> Reasoning: Emphasis on maintenance and optimization signals focus on correctness and stability over delivery speed.

**Run 3:** `rigour` ✗
> Quote: "creating and optimizing reports, stories, and planning content within SAP Analytics Cloud"
> Verified: ✓ found in JD
> Reasoning: The focus on optimization within an established SAP/manufacturing environment implies quality and stability rather than delivery speed.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "processing IoT and market data, unifying SAP and non-SAP system data"
> Verified: ✓ found in JD
> Reasoning: This operational analytics work in manufacturing affects business decisions but lacks explicit financial reporting, compliance, or regulatory signals that would elevate it to high risk.

**Run 2:** `moderate` ✓
> Quote: "creating and optimizing reports, stories, and planning content within SAP Analytics Cloud"
> Verified: ✓ found in JD
> Reasoning: BI and reporting work for a manufacturing company with no financial reporting, compliance, or regulatory language present.

**Run 3:** `moderate` ✓
> Quote: "developing and maintaining data models, queries, and views in SAP environments"
> Verified: ✓ found in JD
> Reasoning: Manufacturing context with SAP implies operational importance but lacks explicit financial, regulatory, or compliance language that signals high risk.

### collaboration_width
**Manual:** `0`

**Run 1:** `0` ✓
> Quote: "No named partner teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD describes work without naming specific partner functions; 'supporting AI-driven analytics expansion' is generic language without identifying Finance, Product, Operations, or other discrete teams.

**Run 2:** `0` ✓
> Quote: "No named teams or functions referenced"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities describe specific tools and data work without naming any partner teams or functions the role collaborates with.

**Run 3:** `0` ✓
> Quote: "No named partner teams explicitly identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role description lists technical responsibilities without naming specific partner teams or functions to collaborate with.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "advancing existing Business Warehouse implementations"
> Verified: ✓ found in JD
> Reasoning: Existing SAP infrastructure with multiple named tools in active use signal an established data function being extended and improved, rather than built from zero or operating at enterprise-wide scale.

**Run 2:** `mid` ✓
> Quote: "advancing existing Business Warehouse implementations"
> Verified: ✓ found in JD
> Reasoning: Multiple named tools in responsibilities combined with framing of improving existing infrastructure indicate an established mid-stage data function.

**Run 3:** `mid` ✓
> Quote: "advancing existing Business Warehouse implementations"
> Verified: ✓ found in JD
> Reasoning: Named established tools (SAP BW, Databricks, Power BI) being expanded and advanced indicate a mid-stage data function with existing infrastructure.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `hiring_manager` ✓
> Quote: "integrate new data sources via Business Data Cloud and develop analytics solutions using Azure Databricks, including Power BI reports and dashboards"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific SAP ecosystem terminology (Business Data Cloud, Databricks integration, BW/4HANA modules) with precise application context that only someone doing this work would articulate.

**Run 2:** `hiring_manager` ✓
> Quote: "develop analytics solutions using Azure Databricks, including Power BI reports and dashboards"
> Verified: ✓ found in JD
> Reasoning: Specific tool combinations (Azure Databricks with Power BI) and precise technical context indicate detail from someone actively doing this work.

**Run 3:** `hiring_manager` ✓
> Quote: "creating and optimizing reports, stories, and planning content within SAP Analytics Cloud and advancing existing Business Warehouse implementations"
> Verified: ✓ found in JD
> Reasoning: Specific named tools with precise context (SAP Analytics Cloud stories/planning features, Business Warehouse modules, ABAP/Python requirements) show technical knowledge only a hiring manager would possess.

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `internal_data` ✓
> Quote: "developing and maintaining data models, queries, and views... advancing existing Business Warehouse implementations... integrate new data sources"
> Verified: ⚠ NOT found verbatim
> Reasoning: The emphasis is on building and maintaining analytics infrastructure and data pipelines serving the data function itself, rather than commercial, product, or finance stakeholders.

**Run 2:** `internal_data` ✓
> Quote: "developing and maintaining data models, queries, and views in SAP environments"
> Verified: ✓ found in JD
> Reasoning: The focus is on data infrastructure and platform work (models, data integration, unification) serving the data function itself, not external commercial, product, or finance stakeholders.

**Run 3:** `internal_data` ✓
> Quote: "unifying SAP and non-SAP system data"
> Verified: ✓ found in JD
> Reasoning: The emphasis on data infrastructure, system integration, warehouse advancement, and data source consolidation indicates the role serves the data platform and its consumers rather than specific business functions.

### autonomy_level
**Manual:** `execution`

**Run 1:** `execution` ✓
> Quote: "supporting AI-driven analytics expansion"
> Verified: ✓ found in JD
> Reasoning: The verb 'supporting' indicates the role executes direction set elsewhere rather than defining strategy or owning the direction of initiatives.

**Run 2:** `execution` ✓
> Quote: "supporting AI-driven analytics expansion"
> Verified: ✓ found in JD
> Reasoning: All responsibilities use execution verbs (develop, maintain, integrate, create, advance) with no strategic framing of defining priorities, setting roadmaps, or owning direction.

**Run 3:** `execution` ✓
> Quote: "supporting AI-driven analytics expansion"
> Verified: ✓ found in JD
> Reasoning: The framing of "supporting" expansion and "advancing existing" systems rather than defining strategy indicates the role executes direction set by others.

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "familiarity with artificial intelligence and machine learning concepts"
> Verified: ✓ found in JD
> Reasoning: 'Familiarity with concepts' is too vague to establish that the candidate must use AI tools for coding or build AI-ready data infrastructure.

**Run 2:** `none` ✗
> Quote: "familiarity with artificial intelligence and machine learning concepts"
> Verified: ✓ found in JD
> Reasoning: The vague mention of familiarity with concepts does not indicate expected use of AI coding tools, coding agents, or building AI-specific data infrastructure.

**Run 3:** `none` ✗
> Quote: "familiarity with artificial intelligence and machine learning concepts"
> Verified: ✓ found in JD
> Reasoning: The vague phrase "familiarity with concepts" lacks specific expectations for AI coding tools (ai_user) or building AI data infrastructure (ai_enabler).

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "data modeling, reporting structures"
> Verified: ✓ found in JD
> Reasoning: Requirements list these skills but no testing frameworks, data quality practices, or observability tools are mentioned anywhere in the JD.

**Run 2:** `absent` ✗
> Quote: "The engineer will integrate new data sources via Business Data Cloud and develop analytics solutions using Azure Databricks, including Power BI reports and dashboards."
> Verified: ✓ found in JD
> Reasoning: Data model and infrastructure work is described without any mention of testing frameworks, data quality practices, or observability standards in responsibilities or requirements.

**Run 3:** `absent` ✗
> Quote: "The role encompasses developing and maintaining data models, queries, and views in SAP environments"
> Verified: ✓ found in JD
> Reasoning: No mention of testing practices, data quality frameworks, data contracts, or quality assurance appears in the responsibilities or requirements.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed entirely in capability and delivery terms with no mention of compliance, regulatory exposure, audit, or preventing bad data outcomes.

**Run 2:** `none` ✗
> Quote: "The role encompasses developing and maintaining data models, queries, and views in SAP environments."
> Verified: ✓ found in JD
> Reasoning: The JD is entirely framed in capability and delivery terms with no language around risk, compliance, regulatory requirements, or data accuracy as a trust concern.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The role is framed in technical capability and delivery terms without emphasizing risk prevention, reliability guarantees, compliance, or stakeholder trust.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
