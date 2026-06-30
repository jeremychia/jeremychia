# Trace: 2026-06-30_van-in-sanoma_business-intelligence-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Analyst — Van In (Sanoma Learning)

**URL:** https://sanoma.wd3.myworkdayjobs.com/en-US/Sanoma_Learning/job/Wommelgem/Data-analyst_JR-1550?source=LinkedIn
**Location:** Wommelgem, Belgium / Den Bosch, Netherlands (hybrid)
**Date Posted:** 2026-06-30

---

Business Intelligence Analyst
Van In (Sanoma Learning)
Hybrid — Wommelgem / Den Bosch
Full time
Job requisition id: JR-1550
Posted 30+ Days Ago

Wil jij met data échte impact maken op het onderwijs van morgen?
Als Data Analist help je onze organisatie betere beslissingen nemen door data om te zetten in heldere inzichten. Je werkt met een moderne data stack (SQL, Power BI,…) en krijgt veel autonomie om end-to-end oplossingen uit te bouwen die ook écht gebruikt worden.

Je komt terecht in een mensgerichte organisatie waar data steeds belangrijker wordt en waar jouw werk zichtbaar bijdraagt aan maatschappelijke impact.

Jouw team

Je wordt onderdeel van het Data & Analytics team, waar je samenwerkt met één andere data-analist in België. Daarnaast heb je regelmatig contact met een groter team van data-analisten en experts in Nederland. Via kennisdeling en best practices versterk je je expertise en draag je mee bij aan de verdere uitbouw van een data gedreven organisatie. Af en toe werk je ook samen op locatie in Den Bosch.

Wat ga je doen?

Als Data Analist werk je van businessvraag tot bruikbaar inzicht. Je fungeert als brug tussen data en besluitvorming en helpt collega's data beter te begrijpen en te gebruiken.

Concreet betekent dit dat je:
- Businessvragen scherp stelt en vertaalt naar analyses en datavereisten
- Data verzamelt, transformeert en modelleert uit verschillende bronnen
- End-to-end oplossingen bouwt met SQL en Snowflake, Power BI en DBT is een mooie plus!
- Heldere, actiegerichte dashboards en rapporten ontwikkelt die effectief gebruikt worden
- Datakwaliteit, governance en betrouwbaarheid mee bewaakt
- Inzichten en aanbevelingen duidelijk communiceert naar zowel technische als niet-technische stakeholders
- Business teams ondersteunt in projecten en besluitvorming
- Meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform
- Data literacy binnen de organisatie versterkt via begeleiding, workshops of kennisdeling

Wie zoeken wij?

Je hoeft niet alles al perfect te beheersen, leergierigheid en analytisch denkvermogen zijn minstens zo belangrijk.
- Je hebt een bachelor diploma of gelijkwaardige ervaring
- Je hebt 2 tot 4 jaar ervaring in data-analyse, BI of insights
- Je werkt vlot met SQL en BI-tools
- Ervaring met dbt, Power BI en Snowflake is een sterke troef, of je wil je hierin snel verdiepen
- Kennis van Python is een plus
- Je kan complexe informatie helder uitleggen aan verschillende doelgroepen
- Je werkt gestructureerd, denkt analytisch en neemt ownership
- Je bent een teamspeler die kennis deelt en graag bijleert
- Je volgt trends in data, AI en analytics en denkt mee over toepassingen
- Je kan professioneel communiceren in het Frans of bent bereid dit verder te versterken

Wat mag je van ons verwachten?

Een mensgerichte cultuur met een DNA waarbij veel aandacht gaat naar het welzijn en werkgeluk. Een betekenisvolle job met maatschappelijke impact. Werken binnen een sterke, internationale groep (SANOMA). Ruimte om te groeien, leren en initiatief te nemen. Samenwerking met ervaren data-professionals in België en Nederland. Een competitief loon aangevuld met extralegale voordelen. Hybride werken: meerdere dagen per week thuiswerk mogelijk.

About Sanoma Learning

Sanoma Learning is a leading K12 European learning company, operating in 12 countries. With over 3000 employees, we help shape the future of education for 25+ million of students.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 1 | 0 | 1 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | mixed | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | execution | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Datakwaliteit, governance en betrouwbaarheid mee bewaakt"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality, governance, and reliability as core responsibilities with no velocity signals present.

**Run 2:** `rigour`
> Quote: "Datakwaliteit, governance en betrouwbaarheid mee bewaakt"
> Verified: ✓ found in JD
> Reasoning: Data quality, governance, and reliability are emphasized as core responsibilities without any velocity-oriented language.

**Run 3:** `rigour`
> Quote: "Datakwaliteit, governance en betrouwbaarheid mee bewaakt"
> Verified: ✓ found in JD
> Reasoning: Explicit emphasis on data quality, governance, and reliability as core responsibilities with no speed or iteration framing signals a rigour orientation.

### domain_risk

**Run 1:** `moderate`
> Quote: "Wil jij met data échte impact maken op het onderwijs van morgen?"
> Verified: ✓ found in JD
> Reasoning: Educational context carries societal impact but lacks explicit financial reporting, compliance, or regulatory risk signals typical of high-risk roles.

**Run 2:** `moderate`
> Quote: "Je fungeert als brug tussen data en besluitvorming en helpt collega's data beter te begrijpen en te gebruiken."
> Verified: ✓ found in JD
> Reasoning: The role is general business intelligence for an educational organization; there are no explicit signals of financial reporting, regulatory compliance, or audit requirements.

**Run 3:** `moderate`
> Quote: "Je fungeert als brug tussen data en besluitvorming en helpt collega's data beter te begrijpen en te gebruiken."
> Verified: ✓ found in JD
> Reasoning: Supporting business decision-making in education without explicit financial reporting, regulatory compliance, or audit requirements indicates moderate risk.

### collaboration_width

**Run 1:** `1`
> Quote: "groter team van data-analisten en experts in Nederland"
> Verified: ✓ found in JD
> Reasoning: Only one named role cohort (data analysts team) is explicitly mentioned beyond the role holder's immediate team.

**Run 2:** `0`
> Quote: ""
> Verified: ✓ found in JD
> Reasoning: No explicitly named partner functions or teams are identified; references to 'Business teams' and 'stakeholders' are generic and do not meet the threshold for counting.

**Run 3:** `1`
> Quote: "Business teams ondersteunt in projecten en besluitvorming"
> Verified: ✓ found in JD
> Reasoning: Only 'Business teams' is named as a distinct partner function; other references are either the role holder's own data team or generic stakeholders.

⚠ **LLM inconsistency**: runs gave ['1', '0', '1']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform"
> Verified: ✓ found in JD
> Reasoning: Existing data team with multiple analysts, named tools in responsibilities (SQL, Snowflake, dbt, Power BI), and active infrastructure development indicate a growing but not yet mature data function.

**Run 2:** `mid`
> Quote: "Meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform"
> Verified: ✓ found in JD
> Reasoning: Named tools (Snowflake, Power BI, dbt) appear in the responsibilities section and infrastructure is being actively improved, indicating an established but growing data function.

**Run 3:** `mid`
> Quote: "meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform"
> Verified: ✓ found in JD
> Reasoning: Multiple named tools (SQL, Snowflake, Power BI, DBT) in responsibilities with existing team structure indicates established data function in active growth phase.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "End-to-end oplossingen bouwt met SQL en Snowflake, Power BI en DBT is een mooie plus!"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific tool names in context and emphasis on actual solution usage that indicate technical specificity from someone doing the work.

**Run 2:** `mixed`
> Quote: "End-to-end oplossingen bouwt met SQL en Snowflake, Power BI en DBT is een mooie plus!"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about tools and workflows is present, but combined with generic support language ('Business teams ondersteunt'), indicating both hiring-manager and recruiter influence.

**Run 3:** `mixed`
> Quote: "End-to-end oplossingen bouwt met SQL en Snowflake, Power BI en DBT is een mooie plus!"
> Verified: ✓ found in JD
> Reasoning: Specific tool references and end-to-end context mix with generic boilerplate action verbs about collaboration and communication.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform"
> Verified: ✓ found in JD
> Reasoning: The primary emphasis is on building the data platform and analytics infrastructure to enable organizational data capability.

**Run 2:** `internal_data`
> Quote: "Meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform"
> Verified: ✓ found in JD
> Reasoning: The explicit emphasis on building the data platform, infrastructure professionalization, and strengthening data literacy positions the role as serving the data function and internal data consumers rather than specific commercial, product, or finance audiences.

**Run 3:** `internal_data`
> Quote: "meebouwt aan de verdere professionalisering van processen, data infrastructuur en het dataplatform"
> Verified: ✓ found in JD
> Reasoning: Primary mission is building data infrastructure and platform capability for organizational use, positioning platform consumers and data infrastructure as the principal audience.

### autonomy_level

**Run 1:** `mixed`
> Quote: "Je werkt met een moderne data stack (SQL, Power BI,…) en krijgt veel autonomie om end-to-end oplossingen uit te bouwen"
> Verified: ✓ found in JD
> Reasoning: The role combines explicit autonomy to define and build technical solutions with execution responsibilities to support business teams and organizational priorities.

**Run 2:** `execution`
> Quote: "Business teams ondersteunt in projecten en besluitvorming"
> Verified: ✓ found in JD
> Reasoning: The role is framed primarily as supporting and executing on business requirements, with autonomy granted in how work is implemented rather than in setting strategic direction or defining priorities.

**Run 3:** `mixed`
> Quote: "Je werkt... en krijgt veel autonomie om end-to-end oplossingen uit te bouwen"
> Verified: ⚠ NOT found verbatim
> Reasoning: Significant autonomy in executing end-to-end analytics solutions combined with supporting business team priorities reflects both strategic ownership of delivery and execution within externally-set scopes.

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'mixed']
