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

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | mixed | rigour | rigour | rigour | 100% | ✗ |
| domain_risk | moderate | moderate | moderate | moderate | 100% | ✓ |
| collaboration_width | 1 | 3 | 0 | 0 | 33% | ✗ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | hiring_manager | mixed | hiring_manager | mixed | 33% | ✗ |
| stakeholder_orientation | commercial | commercial | commercial | commercial | 100% | ✓ |
| autonomy_level | mixed | execution | strategic | execution | 33% | ✗ |
| ai_role |  | none | none | none | 100% | ✗ |
| testing_framing |  | absent | absent | absent | 100% | ✗ |
| loss_aversion_framing |  | none | none | none | 100% | ✗ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `mixed`

**Run 1:** `rigour` ✗
> Quote: "kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen"
> Verified: ✓ found in JD
> Reasoning: Emphasis on meticulous data maintenance, model structure, and careful optimization reflects rigour orientation with no velocity signals.

**Run 2:** `rigour` ✗
> Quote: "Sorgfaltige Arbeitsweise und hohe Eigenmotivation"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes careful working style and data maintenance without any velocity language (fast-paced, rapid, MVP, etc.), placing it firmly in the rigour orientation.

**Run 3:** `rigour` ✗
> Quote: "Als Expert*in im Datawarehouse kümmerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role emphasizes data care, model structure, and warehouse maintenance, indicating a rigour orientation toward data quality and operational excellence, with no velocity language present.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`rigour`

### domain_risk
**Manual:** `moderate`

**Run 1:** `moderate` ✓
> Quote: "Reporting und der Marketing Automation fur das Zeitungsgeschaft"
> Verified: ✓ found in JD
> Reasoning: Media/subscription business focused on marketing automation and reporting without explicit financial reporting, compliance, or regulatory language places this at moderate business impact risk.

**Run 2:** `moderate` ✓
> Quote: "Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft digital und traditionell"
> Verified: ✓ found in JD
> Reasoning: The role handles reporting and marketing automation for a media/newspaper business with no explicit financial reporting, compliance, or regulatory language, making domain risk moderate rather than high.

**Run 3:** `moderate` ✓
> Quote: "Reporting und der Marketing Automation für das Zeitungsgeschäft digital und traditionell"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role serves reporting and marketing automation for a media business without explicit regulatory, compliance, or financial reporting requirements, indicating moderate business impact.

### collaboration_width
**Manual:** `1`

**Run 1:** `3` ✗
> Quote: "Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen"
> Verified: ✓ found in JD
> Reasoning: Three distinct named data functions (Data Analysts, Data Scientists, Data Engineers) are explicitly identified as collaboration partners.

**Run 2:** `0` ✗
> Quote: "Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen"
> Verified: ✓ found in JD
> Reasoning: The only collaboration mentioned is with colleagues within the same Data Subscription Team; no external partner teams or functions are explicitly named.

**Run 3:** `0` ✗
> Quote: "Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen"
> Verified: ✓ found in JD
> Reasoning: Data Analysts, Scientists, and Engineers are all part of the same Data Subscription Team (your own team), so they do not count as external partner teams.

⚠ **Disagreement**: manual=`1` vs LLM majority=`0`

⚠ **LLM inconsistency**: runs gave ['3', '0', '0']

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Established Data Subscription Team with named tools in responsibilities (dbt, SQL, GCP, GitHub) and multiple defined data roles indicates functional data organization at mid-maturity.

**Run 2:** `mid` ✓
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, SQL, GCP) appear in core responsibilities with active implementation context, and multiple data roles are implied (Analysts, Scientists, Engineers), indicating a mid-stage team.

**Run 3:** `mid` ✓
> Quote: "Du entwickelst und implementierst eigenständig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ⚠ NOT found verbatim
> Reasoning: Concrete tools are named in responsibilities (GCP, dbt, SQL) and multiple data roles exist within the team, suggesting an established mid-stage data function.

### jd_authorship
**Manual:** `hiring_manager`

**Run 1:** `mixed` ✗
> Quote: "Du arbeitest eng mit den Data Analysts/Scientists/Engineers Deines Teams zusammen und bringst Deine Expertise und kreativen Losungen ein, um datenbasierte Optimierungsstrategien zu entwickeln"
> Verified: ✓ found in JD
> Reasoning: Specific named roles and tools (dbt, SQL, GCP, data pipelines) reflect hiring manager input, but generic phrases like "bringst Deine Expertise und kreativen Losungen ein" indicate recruiter contributions.

**Run 2:** `hiring_manager` ✓
> Quote: "Als Expert*in im Datawarehouse kummerst Du Dich auch um die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen"
> Verified: ✓ found in JD
> Reasoning: The responsibilities contain specific technical expertise signals (data warehouse expert, data model structure ownership, cost optimization) that demonstrate intimate knowledge of the actual work rather than generic boilerplate.

**Run 3:** `mixed` ✗
> Quote: "Du entwickelst und implementierst eigenständig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD combines technical specificity about tools and platforms with boilerplate language about collaboration and optimization strategies.

⚠ **Disagreement**: manual=`hiring_manager` vs LLM majority=`mixed`

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation
**Manual:** `commercial`

**Run 1:** `commercial` ✓
> Quote: "Reporting und der Marketing Automation fur das Zeitungsgeschaft"
> Verified: ✓ found in JD
> Reasoning: Primary focus is supporting marketing automation for revenue-generating newspaper subscription business, making commercial optimization the primary stakeholder.

**Run 2:** `commercial` ✓
> Quote: "Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation fur das Zeitungsgeschaft"
> Verified: ✓ found in JD
> Reasoning: The role explicitly supports marketing automation and reporting for the subscription/newspaper business, with marketing automation being a core stated use case serving commercial/marketing functions.

**Run 3:** `commercial` ✓
> Quote: "Transformation von Rohdaten zur Nutzung im Reporting und der Marketing Automation für das Zeitungsgeschäft"
> Verified: ⚠ NOT found verbatim
> Reasoning: The primary framing is delivering reporting and marketing automation for the newspaper business, indicating a commercial/marketing audience.

### autonomy_level
**Manual:** `mixed`

**Run 1:** `execution` ✗
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines"
> Verified: ✓ found in JD
> Reasoning: While independent execution is expected, the verbs throughout (develop, implement, work with, take care of) are execution-focused rather than strategic direction-setting verbs like define or architect.

**Run 2:** `strategic` ✗
> Quote: "Nach Deiner Einarbeitung wirst Du verantwortlich fur zwei Topics und tragst damit entscheidend zum Geschaftserfolg bei"
> Verified: ✓ found in JD
> Reasoning: The role independently owns two topics, develops pipelines autonomously, and defines data warehouse structure and models rather than executing work assigned by others.

**Run 3:** `execution` ✗
> Quote: "Nach Deiner Einarbeitung wirst Du verantwortlich für zwei Topics und tragst damit entscheidend zum Geschäftserfolg bei"
> Verified: ⚠ NOT found verbatim
> Reasoning: The role focuses on delivering work within specific topics and executing data infrastructure, not setting strategy or direction.

⚠ **Disagreement**: manual=`mixed` vs LLM majority=`execution`

⚠ **LLM inconsistency**: runs gave ['execution', 'strategic', 'execution']

### ai_role
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI tools, ML pipelines, or AI-enabled data systems appears anywhere in the job description.

**Run 2:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: No mention of AI-assisted coding tools, agentic workflows, AI-ready data foundations, or any AI capability expectations for the candidate anywhere in the JD.

**Run 3:** `none` ✗
> Quote: "No AI skill signal."
> Verified: ✓ found in JD
> Reasoning: The JD mentions no AI tools, coding agents, or AI-related responsibilities; candidates are expected to work with standard data tools only.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`

### testing_framing
**Manual:** ``

**Run 1:** `absent` ✗
> Quote: "Du entwickelst und implementierst eigenstandig Data Pipelines in der Google Cloud Platform und nutzt dbt, SQL, Github und andere Tools"
> Verified: ✓ found in JD
> Reasoning: Data pipeline development and warehouse management responsibilities contain no testing frameworks, data quality ownership, or observability practices.

**Run 2:** `absent` ✗
> Quote: "die Datenpflege, die Struktur der Datenmodelle sowie um die Kostenoptimierungen"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data maintenance and model structure but contains no mention of testing, data quality frameworks, data contracts, or observability practices.

**Run 3:** `absent` ✗
> Quote: "No testing or data quality signal."
> Verified: ✓ found in JD
> Reasoning: The JD mentions data maintenance and model structure but contains no explicit testing, data quality frameworks, or observability responsibilities.

⚠ **Disagreement**: manual=`` vs LLM majority=`absent`

### loss_aversion_framing
**Manual:** ``

**Run 1:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: JD focuses on delivery, optimization, and capability-building with no risk, compliance, regulatory, or stakeholder-trust framing.

**Run 2:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD is framed around capability and delivery contributions rather than preventing bad outcomes, regulatory risks, or protecting stakeholder trust from data errors.

**Run 3:** `none` ✗
> Quote: "No loss aversion framing."
> Verified: ✓ found in JD
> Reasoning: The JD frames the role in delivery and capability terms with no emphasis on risk prevention, compliance, reliability, or trust.

⚠ **Disagreement**: manual=`` vs LLM majority=`none`
