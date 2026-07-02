# Trace: 2026-07-02_funke-medien_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer (m/w/d) — FUNKE Mediengruppe

**URL:** https://jobs.funkemedien.de/job/Berlin-Analytics-Engineer-%28mwd%29/1359070355/
**Location:** Berlin/Hamburg, Germany
**Date Posted:** 2026-07-02

---

# Analytics Engineer (m/w/d)

Company: FUNKE Mediengruppe
Standort: Berlin, DE / Hamburg, DE

## Uber FUNKE
FUNKE gehort zu den fuhrenden Arbeitgebern der Medienbranche. Von Online-Portalen uber Zeitungen und Zeitschriften bis hin zu Radio und Podcast - die Vielfalt der Titel, Marken und Genres ist einzigartig in der deutschen Medienlandschaft. Rund 1.700 Journalist*innen und 2.800 Medienmacher*innen gestalten jeden Tag in ganz Deutschland die Zukunft der Medien mit.

Als Analytics Engineer (m/w/d) tragst Du massgeblich zur Gestaltung datengetriebener Projekte bei und spielst eine Schlusselrolle im Team. Zur Verstarkung des Teams in Berlin oder Hamburg wird ein Analytics Engineer gesucht.

## Deine Aufgaben
- Als Mitglied des Data Subscription Teams bist Du verantwortlich fur alles rund um das Thema Analytics Engineering: Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft digital und traditionell
- Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen und bringst Deine Expertise und kreativen Losungen ein, um datenbasierte Optimierungsstrategien zu entwickeln
- Nach Deiner Einarbeitung wirst Du verantwortlich fur zwei Topics und tragst damit entscheidend zum Geschaftserfolg bei
- Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools
- Als Expert*in im Datawarehouse kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen

## Dein Profil
- Leidenschaft fur Daten und Interesse am Vertriebsgeschaft regionaler Tageszeitungen
- Erfahrung als Analytics Engineer/Data Analyst sowie fortgeschrittene Kenntnisse in SQL, idealerweise Kenntnisse in Python oder weiteren Programmiersprachen
- Begeisterung fur technische Innovationen und Fahigkeit, sich zugig und effektiv in neue technologische Systeme und Tools einzuarbeiten
- Verantwortungsbewusstsein und Ownership
- Fliessendes Deutsch, Offenheit, Kommunikationsstarke und Teamfahigkeit
- Sorgfaltige Arbeitsweise und hohe Eigenmotivation

## Deine Benefits
Innovation trifft Tradition: Mitgestaltung der digitalen Transformation der Mediengruppe. Entwicklung durch FUNKE Akademie (Coachings, Workshops, Online-Trainings). Hybrides Arbeitsmodell fur Work-Life-Balance. Dynamisches Team, offene Feedbackkultur, kurze Kommunikationswege. Corporate Benefits Portal mit Rabatten und Abos. Kooperationen mit Fitnessstudios und individuelle Beratung fur mentale und korperliche Gesundheit.

Bewerbung an Steffen Flach.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 0 | 0 | 0 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | hiring_manager | 33% |
| stakeholder_orientation | internal_data | commercial | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |
| ai_role | none | none | none | 100% |
| testing_framing | absent | absent | absent | 100% |
| loss_aversion_framing | none | none | moderate | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Sorgfaltige Arbeitsweise und hohe Eigenmotivation"
> Verified: ✓ found in JD
> Reasoning: The profile requirements emphasize careful, meticulous working style as a core expectation, with no velocity or speed language present anywhere in the JD.

**Run 2:** `rigour`
> Quote: "Sorgfaltige Arbeitsweise und hohe Eigenmotivation"
> Verified: ✓ found in JD
> Reasoning: The profile section emphasizes careful, meticulous work as a core requirement with no velocity-oriented language, establishing rigor as the primary orientation.

**Run 3:** `rigour`
> Quote: "Sorgfaltige Arbeitsweise und hohe Eigenmotivation"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes careful, meticulous work and data maintenance with no velocity or speed-focused language.

### domain_risk

**Run 1:** `moderate`
> Quote: "Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft digital und traditionell"
> Verified: ✓ found in JD
> Reasoning: The role affects business intelligence and marketing operations in the newspaper publishing sector, but does not involve regulatory compliance, financial reporting, or direct financial risk.

**Run 2:** `moderate`
> Quote: "Reporting und der Marketing Automation fur das Zeitungsgeschaft digital und traditionell"
> Verified: ✓ found in JD
> Reasoning: The role focuses on operational reporting and marketing automation for a media/subscription business rather than financial reporting or regulatory compliance, placing it in the moderate risk category.

**Run 3:** `moderate`
> Quote: "Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft"
> Verified: ✓ found in JD
> Reasoning: Data errors affect business reporting and marketing decisions for newspaper operations but involve no regulatory, compliance, or direct financial reporting risks.

### collaboration_width

**Run 1:** `0`
> Quote: "No named external teams identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions working with Data Analysts/Scientists/Engineers in the same Data Subscription Team, which does not count per rules; no other named teams (Finance, Product, Marketing, Operations, etc.) are explicitly listed as collaboration partners.

**Run 2:** `0`
> Quote: "No named partner teams identified in the JD"
> Verified: ⚠ NOT found verbatim
> Reasoning: While the role works with Data Analysts/Scientists/Engineers, these are colleagues within the same Data Subscription Team rather than distinct named partner functions; no external collaborating teams are explicitly mentioned.

**Run 3:** `0`
> Quote: "Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen"
> Verified: ✓ found in JD
> Reasoning: The JD names only team members within the role holder's own data team, which does not count as external collaboration per definition.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in the responsibilities section with specific context, and the existence of multiple data roles (Analysts, Scientists, Engineers) indicates an established function with infrastructure in place.

**Run 2:** `mid`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Named tools appearing in responsibilities (GCP, dbt, SQL, Github) and references to existing data warehouse expertise indicate established infrastructure; the team is scaling rather than building from zero.

**Run 3:** `mid`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Named tools (GCP, dbt, SQL) appear in responsibilities indicating established infrastructure; multiple data roles are implied, and the role owns specific topics within existing structure.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about GCP, dbt, and pipeline development suggests hiring manager input, but adjacent responsibilities use generic recruiter language like 'bringst Deine Expertise und kreativen Losungen ein' without concrete detail.

**Run 2:** `hiring_manager`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools; Als Expert*in im Datawarehouse kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen"
> Verified: ⚠ NOT found verbatim
> Reasoning: The responsibilities contain specific technical context (GCP, dbt, data warehouse expertise, cost optimization) that reflects hands-on understanding rather than generic boilerplate language.

**Run 3:** `hiring_manager`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Responsibilities contain precise technical context—specific tools, business domain (newspaper sales reporting), and technical concerns (data maintenance, model structure)—reflecting hands-on experience.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'hiring_manager']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Analytics Engineering: Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation"
> Verified: ✓ found in JD
> Reasoning: The primary focus is building and maintaining data infrastructure (warehouse, models, pipelines) that serves downstream functions, characteristic of internal_data orientation rather than GTM, product, or finance.

**Run 2:** `commercial`
> Quote: "Reporting und der Marketing Automation fur das Zeitungsgeschaft"
> Verified: ✓ found in JD
> Reasoning: The primary focus on reporting and marketing automation for a subscription business indicates the role primarily serves commercial/GTM stakeholders.

**Run 3:** `internal_data`
> Quote: "Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building analytics infrastructure (data transformation and pipelines) for internal stakeholders (reporting and marketing automation teams).

⚠ **LLM inconsistency**: runs gave ['internal_data', 'commercial', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Nach Deiner Einarbeitung wirst Du verantwortlich fur zwei Topics und tragst damit entscheidend zum Geschaftserfolg bei"
> Verified: ✓ found in JD
> Reasoning: The role receives scoped, defined domains (two topics) to own and execute, but does not set overall analytics strategy or define priorities.

**Run 2:** `execution`
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines"
> Verified: ✓ found in JD
> Reasoning: While the role has autonomy over technical implementation, the scope is defined by assigned topics post-onboarding rather than self-directed strategic ownership.

**Run 3:** `execution`
> Quote: "Nach Deiner Einarbeitung wirst Du verantwortlich fur zwei Topics"
> Verified: ✓ found in JD
> Reasoning: While implementation is autonomous, ownership is scoped to two defined topics after onboarding, indicating execution within set boundaries rather than strategic direction-setting.

### ai_role

**Run 1:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted work, or building AI-ready data infrastructure.

**Run 2:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI coding tools, AI-assisted development, or AI infrastructure expectations for the candidate.

**Run 3:** `none`
> Quote: "No AI skill signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD contains no mention of AI, LLMs, coding agents, or AI tools expected of the candidate.

### testing_framing

**Run 1:** `absent`
> Quote: "kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen"
> Verified: ✓ found in JD
> Reasoning: Data maintenance is mentioned but no testing frameworks, data quality practices, data contracts, or observability approaches are explicitly addressed.

**Run 2:** `absent`
> Quote: "No testing or data quality signal."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD emphasizes careful work and data maintenance but does not explicitly mention testing frameworks, data quality practices, data contracts, or observability.

**Run 3:** `absent`
> Quote: "um die Datenpflege, die Struktur der Datenmodelle"
> Verified: ✓ found in JD
> Reasoning: While data maintenance is mentioned, no testing practices, data contracts, observability frameworks, or data quality standards are explicitly referenced.

### loss_aversion_framing

**Run 1:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role around delivering value and contributing to business success, with no risk, compliance, reliability, or prevention-of-bad-outcomes language.

**Run 2:** `none`
> Quote: "No loss aversion framing."
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD frames the role in terms of capability and optimization with no explicit risk, compliance, or failure-prevention language in the responsibilities.

**Run 3:** `moderate`
> Quote: "um die Datenpflege, die Struktur der Datenmodelle"
> Verified: ✓ found in JD
> Reasoning: Data maintenance and structure are emphasized as core responsibilities, reflecting operational reliability concerns, though not framed as risk mitigation or compliance-driven.

⚠ **LLM inconsistency**: runs gave ['none', 'none', 'moderate']
