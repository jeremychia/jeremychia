# Trace: 2026-06-27_eraneos_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer (all genders) — Eraneos

**Location:** Hamburg, München, Düsseldorf, remote
**Date Posted:** 2026-06-27

---

Eraneos ist ein technisches, umsetzungsorientiertes Spin-Off einer global agierenden Managementberatung. Wir begleiten unsere Kunden – vorwiegend DAX- und Fortune-500-Unternehmen – auf ihrem Weg der analytischen und KI-gestützten Transformation. Im Mittelpunkt steht dabei die Umsetzung: von der Strategie über die Architektur bis zur Implementierung.

**Responsibilities:**

- Konzeption und Implementierung von Datenmodellen in modernen Data Warehouses und Lakehouses
- Aufbau und Pflege von Datentransformations-Pipelines mit dbt
- Entwicklung dimensionaler Datenmodelle (Star Schema, Snowflake Schema, Data Vault)
- Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden
- Implementierung von Datenqualitätsprüfungen und -tests
- Optimierung der Datenbankperformance durch den Einsatz moderner Tabellenformate (z. B. Iceberg, Delta)
- Enge Zusammenarbeit mit Analytics- und Data-Science-Teams
- Übernahme von Projektverantwortung und Steuerung von Teilprojekten
- Kommunikation und Abstimmung mit Stakeholdern auf verschiedenen Ebenen

**Requirements:**

- Fundierte Erfahrung in der Datenmodellierung in Data-Platform-Umgebungen
- Praktische dbt-Erfahrung (mindestens 6 Monate)
- Kenntnisse in dimensionalen Datenmodellierungsansätzen (Star Schema, Snowflake Schema, Data Vault)
- Solide SQL-Kenntnisse und idealerweise Python-Programmierkenntnisse
- Erfahrung mit Data Lakehouses wie Snowflake oder Databricks
- Idealerweise Erfahrung mit Data-Quality-Tools (z. B. Great Expectations, Soda)
- Deutschkenntnisse auf mindestens B1-Niveau und sehr gute Englischkenntnisse
- Reisebereitschaft (gelegentlich)
- Teamfähigkeit und strukturierte Arbeitsweise

**Benefits:**

- Flexible Arbeitszeiten und Home-Office-Möglichkeiten
- Flache Hierarchien und kurze Entscheidungswege
- Trainings- und Weiterbildungsmöglichkeiten
- JobRad (Company Bike Program)
- EGYM Wellpass (Fitness-Mitgliedschaft)
- Zentrale Bürolagen mit guter Verkehrsanbindung
- Täglich frisches Obst, Kaffee, Snacks und Getränke

Contact: Ekaterina Korolkova – career.de@eraneos.com – +49 40 809 081-172

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 2 | 2 | 2 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | mixed | 33% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes reliability and performance of analytical data as core responsibilities, which are rigour-oriented signals, with no mention of velocity, iteration speed, or shipping pace.

**Run 2:** `rigour`
> Quote: "Implementierung von Datenqualitätsprüfungen und -tests"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes data quality checks, testing, and reliable delivery with no corresponding speed or iteration language.

**Run 3:** `rigour`
> Quote: "Implementierung von Datenqualitätsprüfungen und -tests"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality checks, testing, and reliable delivery as core expectations, with no velocity-oriented language about speed or iteration.

### domain_risk

**Run 1:** `moderate`
> Quote: "vorwiegend DAX- und Fortune-500-Unternehmen"
> Verified: ✓ found in JD
> Reasoning: The role serves large enterprises where data quality matters significantly, but the JD lacks explicit financial reporting, compliance, or regulatory language indicating high risk.

**Run 2:** `moderate`
> Quote: "Konzeption und Implementierung von Datenmodellen in modernen Data Warehouses und Lakehouses"
> Verified: ✓ found in JD
> Reasoning: The role describes generic data engineering work without explicit financial, regulatory, or compliance language despite the company's Fortune-500 client base.

**Run 3:** `moderate`
> Quote: "Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden"
> Verified: ✓ found in JD
> Reasoning: While serving large enterprises (DAX/Fortune 500), the JD emphasizes reliable analytical data delivery without explicit mention of financial reporting, compliance, or regulatory requirements.

### collaboration_width

**Run 1:** `2`
> Quote: "Analytics- und Data-Science-Teams"
> Verified: ✓ found in JD
> Reasoning: Two distinct named teams are explicitly mentioned as collaboration partners: Analytics teams and Data Science teams.

**Run 2:** `2`
> Quote: "Analytics- und Data-Science-Teams"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names two distinct partner functions: Analytics teams and Data Science teams.

**Run 3:** `2`
> Quote: "Analytics- und Data-Science-Teams"
> Verified: ✓ found in JD
> Reasoning: Two distinct internal teams are explicitly named: Analytics team (1) and Data Science team (1).

### data_team_maturity

**Run 1:** `mid`
> Quote: "Aufbau und Pflege von Datentransformations-Pipelines mit dbt"
> Verified: ✓ found in JD
> Reasoning: The JD names specific tools (dbt) in responsibilities with implementation context, indicating established data infrastructure being built and extended rather than greenfield setup.

**Run 2:** `mid`
> Quote: "Aufbau und Pflege von Datentransformations-Pipelines mit dbt"
> Verified: ✓ found in JD
> Reasoning: The JD references existing tools (dbt, Snowflake, Databricks) and multiple established data roles (Analytics and Data Science teams), indicating infrastructure at the scaling stage rather than greenfield.

**Run 3:** `mid`
> Quote: "Aufbau und Pflege von Datentransformations-Pipelines mit dbt"
> Verified: ✓ found in JD
> Reasoning: Named tools (dbt, Snowflake, Databricks) appear in responsibilities combined with references to multiple data roles, indicating an existing but growing data function rather than greenfield startup.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Optimierung der Datenbankperformance durch den Einsatz moderner Tabellenformate (z. B. Iceberg, Delta)"
> Verified: ✓ found in JD
> Reasoning: This phrase demonstrates technical specificity about performance optimization with concrete technology examples that only someone who has done this work would write.

**Run 2:** `hiring_manager`
> Quote: "Entwicklung dimensionaler Datenmodelle (Star Schema, Snowflake Schema, Data Vault)"
> Verified: ✓ found in JD
> Reasoning: The specific naming of dimensional modeling patterns and optimization techniques (Iceberg, Delta) demonstrates technical depth that only someone with hands-on experience would include.

**Run 3:** `mixed`
> Quote: "Entwicklung dimensionaler Datenmodelle (Star Schema, Snowflake Schema, Data Vault)"
> Verified: ✓ found in JD
> Reasoning: Technical specificity in named methodologies (Star Schema, Snowflake Schema, Data Vault) and tool-specific responsibilities indicate hiring manager input, though generic project and collaboration language is also present.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "Enge Zusammenarbeit mit Analytics- und Data-Science-Teams"
> Verified: ✓ found in JD
> Reasoning: The primary collaboration and audience described in the JD is other data and analytics teams within the organization, indicating the role serves the internal data function.

**Run 2:** `internal_data`
> Quote: "Enge Zusammenarbeit mit Analytics- und Data-Science-Teams"
> Verified: ✓ found in JD
> Reasoning: The primary collaborators are internal Analytics and Data Science teams, and the role exists to provide reliable analytical data to support the data function itself.

**Run 3:** `internal_data`
> Quote: "Enge Zusammenarbeit mit Analytics- und Data-Science-Teams"
> Verified: ✓ found in JD
> Reasoning: The role's primary mission is building data infrastructure and transformation pipelines for internal analytics and data science teams.

### autonomy_level

**Run 1:** `execution`
> Quote: "Übernahme von Projektverantwortung und Steuerung von Teilprojekten"
> Verified: ✓ found in JD
> Reasoning: The role assumes responsibility for executing projects and sub-projects, indicating the role delivers against defined project scopes rather than setting overall analytics direction.

**Run 2:** `execution`
> Quote: "Aufbau und Pflege von Datentransformations-Pipelines mit dbt"
> Verified: ✓ found in JD
> Reasoning: The responsibilities focus on building, maintaining, and implementing systems within a defined technical scope rather than setting strategic direction for the analytics function.

**Run 3:** `execution`
> Quote: "Aufbau und Pflege von Datentransformations-Pipelines mit dbt"
> Verified: ✓ found in JD
> Reasoning: Responsibilities focus on implementing and delivering data solutions (building, maintaining, implementing) rather than defining the overall analytics strategy or direction.

### ai_role
**Run 1:** `none` ✓
> Quote: "begleiten unsere Kunden – vorwiegend DAX- und Fortune-500-Unternehmen – auf ihrem Weg der analytischen und KI-gestützten Transformation"
> Reasoning: Company context is AI-first transformation, but no signal the candidate builds AI infra or uses AI coding tools.

**Run 2:** `none` ✓
> Quote: "begleiten unsere Kunden... auf ihrem Weg der analytischen und KI-gestützten Transformation"
> Reasoning: Company context includes AI transformation, but AE responsibilities are standard data engineering (dbt pipelines, dimensional models).

**Run 3:** `ai_enabler` ✗
> Quote: "Enge Zusammenarbeit mit Analytics- und Data-Science-Teams"
> Reasoning: Builds data models and pipelines that Data Science teams consume as infrastructure for AI work.

⚠ **LLM inconsistency**: runs gave ['none', 'none', 'ai_enabler']

### testing_framing
**Run 1:** `absent` ✓
> Quote: "Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden"
> Reasoning: Reliability and performance expectations stated, but no explicit testing responsibility or tool signals.

**Run 2:** `absent` ✓
> Quote: "No explicit testing signal or ownership phrase in these responsibilities"
> Reasoning: Data reliability mentioned but without testing tool listing or quality practice ownership verb.

**Run 3:** `absent` ✓
> Quote: ""
> Reasoning: No testing ownership verbs (own/ensure/define/implement) or testing tools mentioned.


### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden"
> Reasoning: Operational reliability concerns (reliable data delivery, performance) signal SLO/pipeline stability focus without regulatory/compliance framing.

**Run 2:** `moderate` ✓
> Quote: "Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden"
> Reasoning: Operational reliability and performance of data delivery is primary framing concern (no compliance/audit/trust signals).

**Run 3:** `moderate` ✓
> Quote: "Sicherstellung, dass analytische Daten zuverlässig und performant bereitgestellt werden"
> Reasoning: Operational reliability and performance optimization signal SLO/pipeline stability concerns.

