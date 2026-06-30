# Trace: 2026-06-29_e-frontiers_analytics-engineer-data-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer / Data Engineer — E-Frontiers

**URL:** https://www.aplitrak.com/?adid=YWxmb25zby5tb3JlaXJhcy5jdWVydm8uNTI4MTMuMTU1MEBlZnJvbnRpZXJzdWsuYXBsaXRyYWsuY29t
**Location:** Community of Madrid, Spain
**Date Posted:** 2026-06-29

---

Analytics Engineer / Data Engineer

E-Frontiers is recruiting an Analytics Engineer/Data Engineer for an international financial services company based in Madrid. The company is evolving its data platform to create robust, reliable data products aligned with business.

Responsibilities:
- Colaboración con negocio: Trabajar estrechamente con stakeholders para entender necesidades, definir requerimientos y traducirlos en planes técnicos accionables.
- Liderazgo end-to-end: Gestionar proyectos desde su definición hasta su entrega, incluyendo estrategia de impacto, validación y testing con negocio.
- Visión estratégica y ejecución técnica: Capacidad de alternar entre la definición de roadmaps multi-dominio y la resolución directa de problemas técnicos complejos.
- Gobernanza y fiabilidad: Monitorizar de forma proactiva los productos de datos, diseñando sistemas de alertas que permitan detectar anomalías antes de impactar al negocio.
- Modelado de datos: Desarrollar modelos de datos siguiendo buenas prácticas de ingeniería (control de versiones, testing y CI/CD).
- Trabajo en equipo: Colaborar con otros miembros del equipo para reforzar estándares de calidad y mejores prácticas en la plataforma.
- Orquestación de pipelines: Gestionar workflows de datos mediante Airflow (Cloud Composer).
- Excelencia en desarrollo: Promover buenas prácticas en desarrollo de queries, revisiones de código, documentación y testing.

Requirements:
- 4+ years in similar roles with analytics engineering expertise
- Advanced SQL for complex model optimization
- dbt experience
- Mentalidad de producto (product mindset) understanding reliability and business value
- Financial services knowledge (P&L, FX, reconciliation concepts)
- Interest in Domain-Driven Design
- High English proficiency (Spanish valued)

Offer:
- Permanent employment with client
- Hybrid model in Madrid offices (Community of Madrid, Spain)
- International, technical environment
- Strategic data project participation
- Social benefits and work flexibility

---
```

---

## Classification results

| Dimension | Manual | Run 1 | Run 2 | Run 3 | Agreement | Match? |
|-----------|--------|-------|-------|-------|-----------|--------|
| velocity_vs_rigour | rigour | rigour | rigour | rigour | 100% | ✓ |
| domain_risk | high | high | high | high | 100% | ✓ |
| collaboration_width | 0 | 0 | 0 | 0 | 100% | ✓ |
| data_team_maturity | mid | mid | mid | mid | 100% | ✓ |
| jd_authorship | mixed | hiring_manager | mixed | mixed | 33% | ✓ |
| stakeholder_orientation | internal_data | finance | finance | internal_data | 33% | ✗ |
| autonomy_level | mixed | mixed | mixed | mixed | 100% | ✓ |

---

## Evidence per dimension

### velocity_vs_rigour
**Manual:** `rigour`

**Run 1:** `rigour` ✓
> Quote: "Modelado de datos: Desarrollar modelos de datos siguiendo buenas prácticas de ingeniería (control de versiones, testing y CI/CD)."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, reliability, testing, CI/CD, code reviews, and best practices throughout, with no velocity language like 'fast-paced' or 'rapid delivery'.

**Run 2:** `rigour` ✓
> Quote: "Gobernanza y fiabilidad: Monitorizar de forma proactiva los productos de datos, diseñando sistemas de alertas que permitan detectar anomalías antes de impactar al negocio."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes governance, reliability, monitoring, and anomaly detection with explicit mentions of testing and CI/CD, establishing data quality and reliability as core expectations with no corresponding velocity language.

**Run 3:** `rigour` ✓
> Quote: "(control de versiones, testing y CI/CD)"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize testing, version control, CI/CD, governance, proactive monitoring, and code reviews with no velocity signals, establishing rigour as the dominant orientation.

### domain_risk
**Manual:** `high`

**Run 1:** `high` ✓
> Quote: "Financial services knowledge (P&L, FX, reconciliation concepts)"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement for P&L, FX, and reconciliation knowledge in a financial services company indicates data errors directly affect financial reporting and regulatory compliance.

**Run 2:** `high` ✓
> Quote: "Financial services knowledge (P&L, FX, reconciliation concepts)"
> Verified: ✓ found in JD
> Reasoning: The role operates within a financial services company and explicitly requires expertise in P&L (financial reporting), foreign exchange, and reconciliation—core financial domain concepts with regulatory and reporting impact.

**Run 3:** `high` ✓
> Quote: "Financial services knowledge (P&L, FX, reconciliation concepts)"
> Verified: ✓ found in JD
> Reasoning: P&L, FX, and reconciliation are explicitly high-risk financial operations requiring precision and compliance; the role requires specific financial services domain knowledge.

### collaboration_width
**Manual:** `0`

**Run 1:** `0` ✓
> Quote: "none identified"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mentions generic stakeholders and business partners but does not name specific functions like Finance, Product, Marketing, Engineering, or other distinct named teams.

**Run 2:** `0` ✓
> Quote: "Trabajar estrechamente con stakeholders"
> Verified: ✓ found in JD
> Reasoning: The JD references only generic terms like 'stakeholders' and 'business' without naming specific partner functions, departments, or roles.

**Run 3:** `0` ✓
> Quote: "Trabajar estrechamente con stakeholders para entender necesidades, definir requerimientos y traducirlos en planes técnicos accionables"
> Verified: ✓ found in JD
> Reasoning: No specifically named partner teams or functions are identified; 'stakeholders' and 'negocio' are too generic to count as distinct collaborators.

### data_team_maturity
**Manual:** `mid`

**Run 1:** `mid` ✓
> Quote: "Orquestación de pipelines: Gestionar workflows de datos mediante Airflow (Cloud Composer)."
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (Airflow, dbt) with specific application context, combined with references to multiple team members and an evolving platform, indicate a mid-stage team growing beyond initial setup.

**Run 2:** `mid` ✓
> Quote: "The company is evolving its data platform to create robust, reliable data products"
> Verified: ✓ found in JD
> Reasoning: The language 'evolving' indicates an existing platform being enhanced rather than built from scratch, with named infrastructure tools (Airflow/Cloud Composer) already in place.

**Run 3:** `mid` ✓
> Quote: "Orquestación de pipelines: Gestionar workflows de datos mediante Airflow (Cloud Composer)"
> Verified: ✓ found in JD
> Reasoning: Named tools (Airflow, Cloud Composer) explicitly mentioned in responsibilities indicate an established data platform undergoing evolution, not greenfield building.

### jd_authorship
**Manual:** `mixed`

**Run 1:** `hiring_manager` ✗
> Quote: "Monitorizar de forma proactiva los productos de datos, diseñando sistemas de alertas que permitan detectar anomalías antes de impactar al negocio."
> Verified: ✓ found in JD
> Reasoning: The specific technical requirements (Airflow, dbt, alert systems for anomaly detection, P&L/FX knowledge, data modeling with CI/CD) show precision about actual daily work only a hiring manager would provide.

**Run 2:** `mixed` ✓
> Quote: "Orquestación de pipelines: Gestionar workflows de datos mediante Airflow (Cloud Composer)."
> Verified: ✓ found in JD
> Reasoning: The JD mixes technical specificity (naming Airflow and Cloud Composer with orchestration context, requiring P&L/FX/reconciliation domain knowledge) with generic boilerplate verbs like 'collaborate' and 'promote best practices'.

**Run 3:** `mixed` ✓
> Quote: "Orquestación de pipelines: Gestionar workflows de datos mediante Airflow (Cloud Composer)"
> Verified: ✓ found in JD
> Reasoning: Technical specificity (Airflow/Cloud Composer, testing, CI/CD) is mixed with generic boilerplate language ('collaborate with stakeholders', 'work as a team').

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'mixed', 'mixed']

### stakeholder_orientation
**Manual:** `internal_data`

**Run 1:** `finance` ✗
> Quote: "Financial services knowledge (P&L, FX, reconciliation concepts)"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement for P&L, FX, and reconciliation knowledge in a financial services company indicates this role primarily serves finance use cases and stakeholders.

**Run 2:** `finance` ✗
> Quote: "Financial services knowledge (P&L, FX, reconciliation concepts)"
> Verified: ✓ found in JD
> Reasoning: The explicit requirement for financial services domain knowledge (P&L = financial reporting, FX = foreign exchange, reconciliation = accounting) identifies finance teams as the primary audience for the data products.

**Run 3:** `internal_data` ✓
> Quote: "Gobernanza y fiabilidad: Monitorizar de forma proactiva los productos de datos, diseñando sistemas de alertas que permitan detectar anomalías antes de impactar al negocio"
> Verified: ✓ found in JD
> Reasoning: The role emphasizes data governance, reliability monitoring, and platform infrastructure, which are internal data function responsibilities focused on serving data consumers and the platform itself.

⚠ **Disagreement**: manual=`internal_data` vs LLM majority=`finance`

⚠ **LLM inconsistency**: runs gave ['finance', 'finance', 'internal_data']

### autonomy_level
**Manual:** `mixed`

**Run 1:** `mixed` ✓
> Quote: "Visión estratégica y ejecución técnica: Capacidad de alternar entre la definición de roadmaps multi-dominio y la resolución directa de problemas técnicos complejos."
> Verified: ✓ found in JD
> Reasoning: The JD explicitly requires both defining roadmaps (strategic ownership) and solving complex technical problems (execution), indicating the role encompasses both strategic direction-setting and execution.

**Run 2:** `mixed` ✓
> Quote: "Visión estratégica y ejecución técnica: Capacidad de alternar entre la definición de roadmaps multi-dominio y la resolución directa de problemas técnicos complejos."
> Verified: ✓ found in JD
> Reasoning: The role explicitly combines strategic direction-setting (defining multi-domain roadmaps, end-to-end project leadership) with direct technical execution (solving complex problems, writing models), making it a genuine combination of both patterns.

**Run 3:** `mixed` ✓
> Quote: "Visión estratégica y ejecución técnica: Capacidad de alternar entre la definición de roadmaps multi-dominio y la resolución directa de problemas técnicos complejos"
> Verified: ✓ found in JD
> Reasoning: The role explicitly combines strategic direction-setting (defining multi-domain roadmaps, end-to-end project leadership) with hands-on technical execution (solving complex problems, managing pipelines).
