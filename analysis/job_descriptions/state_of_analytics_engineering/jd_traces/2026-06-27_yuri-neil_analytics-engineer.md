# Trace: 2026-06-27_yuri-neil_analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Analytics Engineer (H/F) — YURI & NEIL (client: data agency)

**Location:** Montreuil (Télétravail fréquent)
**Date Posted:** 2026-06-27
**Salary:** 48,000–55,000 EUR

---

YURI & NEIL
Analytics Engineer (H/F)

CDI
Montreuil
Télétravail fréquent
Salaire : 48 à 55 €
Expérience : > 4 ans
Éducation : Bac +5 / Master

---

Descriptif du poste

Yuri & Neil Recrutement accompagne aujourd'hui l'un de ses clients, une agence data à taille humaine spécialisée sur toute la chaîne de valeur : Web Analytics & CRO, Data Engineering, Analytics Engineering et Business Intelligence.

Cette structure en forte croissance accompagne des pure players issus de secteurs variés, avec une approche experte, pragmatique et orientée impact business.

Description du poste :

En tant que Analytics Engineer, tu interviendras sur la conception, la structuration et l'activation de stacks data complètes pour différents clients. Ton rôle sera d'accompagner la mise en place d'architectures fiables, exploitables et orientées décisionnel, depuis l'ingestion jusqu'à la valorisation des données.

Tu participeras à des projets variés mêlant engineering, analytics, gouvernance et data products, avec un fort impact sur les enjeux business des clients.

Tes missions

Construction et structuration des stacks data
Concevoir et déployer des architectures data complètes adaptées aux besoins clients.
Mettre en place les flux de collecte, transformation, consolidation et stockage des données.
Structurer les modèles de données pour garantir leur lisibilité, leur performance et leur maintenabilité.

Transformation & valorisation des données
Développer les pipelines de transformation et les modèles analytiques.
Concevoir des dashboards décisionnels clairs et actionnables.
Participer à l'activation des données pour les équipes métiers (marketing, produit, direction…).

Qualité, gouvernance & monitoring
Mettre en place des dispositifs de contrôle de qualité des données et d'alerting.
Structurer la gouvernance data : ownership, accès, documentation, règles d'usage.
Construire des semantic layers facilitant l'exploitation des données par les équipes.

Innovation & data products
Concevoir de petits produits data à forte valeur ajoutée (interfaces, outils internes, automatisations).
Participer à des projets intégrant des briques IA ou d'analyse avancée.
Proposer des améliorations techniques et méthodologiques sur les stacks clients.

---

Profil recherché

Expérience
Minimum 3 ans d'expérience (post-alternance) sur un rôle similaire.
Une alternance en data engineering / analytics engineering / BI est fortement appréciée.

Compétences techniques
Bonne maîtrise de la stack suivante :
SQL et Python
Snowflake
DBT
GitHub
Power BI
AWS

Soft skills
Esprit analytique et rigueur technique.
Capacité à vulgariser des sujets data auprès d'interlocuteurs non techniques.
Curiosité, autonomie et goût pour la résolution de problèmes complexes.
Sens du service et bon relationnel client.

Langues
Anglais : un plus.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 3 | 3 | 3 | 100% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | mixed | 33% |
| stakeholder_orientation | mixed | mixed | internal_data | 33% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Mettre en place des dispositifs de contrôle de qualité des données et d'alerting."
> Verified: ✓ found in JD
> Reasoning: Responsibilities emphasize data quality control, alerting, governance, and maintainability as core expectations rather than speed or rapid delivery.

**Run 2:** `rigour`
> Quote: "Mettre en place des dispositifs de contrôle de qualité des données et d'alerting"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize quality controls, governance structure, and reliability as core expectations with no velocity-oriented language present.

**Run 3:** `rigour`
> Quote: "Mettre en place des dispositifs de contrôle de qualité des données et d'alerting"
> Verified: ✓ found in JD
> Reasoning: The responsibilities section emphasizes data quality control, governance, and reliability as core expectations throughout, with no countervailing velocity language.

### domain_risk

**Run 1:** `moderate`
> Quote: "Cette structure en forte croissance accompagne des pure players issus de secteurs variés, avec une approche experte, pragmatique et orientée impact business."
> Verified: ✓ found in JD
> Reasoning: Work across varied sectors supporting business impact, but no explicit financial reporting, regulatory, or compliance language indicating high risk.

**Run 2:** `moderate`
> Quote: "Tu participeras à des projets variés mêlant engineering, analytics, gouvernance et data products, avec un fort impact sur les enjeux business des clients"
> Verified: ✓ found in JD
> Reasoning: While the role impacts client business decisions across varied sectors, there are no explicit signals of financial reporting, regulatory compliance, or high-risk domain exposure.

**Run 3:** `moderate`
> Quote: "accompagne des pure players issus de secteurs variés, avec une approche experte, pragmatique et orientée impact business"
> Verified: ✓ found in JD
> Reasoning: The role serves clients across varied sectors with focus on business impact rather than regulatory or financial compliance specifically.

### collaboration_width

**Run 1:** `3`
> Quote: "marketing; produit; direction"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named functions—marketing, product, and direction—are explicitly identified as stakeholder partners for data activation.

**Run 2:** `3`
> Quote: "marketing, produit, direction"
> Verified: ✓ found in JD
> Reasoning: The JD explicitly names three distinct stakeholder teams that the role will activate data for in the phrase 'équipes métiers (marketing, produit, direction…)'.

**Run 3:** `3`
> Quote: "marketing; produit; direction"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named functions are explicitly mentioned as collaboration partners for data activation in the responsibilities section.

### data_team_maturity

**Run 1:** `mid`
> Quote: "Cette structure en forte croissance accompagne des pure players issus de secteurs variés"
> Verified: ✓ found in JD
> Reasoning: Established operations serving multiple clients with multiple specializations, described as in strong growth rather than fully mature.

**Run 2:** `mid`
> Quote: "une agence data à taille humaine spécialisée sur toute la chaîne de valeur : Web Analytics & CRO, Data Engineering, Analytics Engineering et Business Intelligence"
> Verified: ✓ found in JD
> Reasoning: Multiple specialized functions exist and the agency is described as growing, but characterized as human-scaled rather than enterprise-maturity, indicating a mid-stage data organization.

**Run 3:** `mid`
> Quote: "une agence data à taille humaine spécialisée sur toute la chaîne de valeur : Web Analytics & CRO, Data Engineering, Analytics Engineering et Business Intelligence"
> Verified: ✓ found in JD
> Reasoning: The agency already operates specialized sub-functions and serves multiple clients across varied sectors, indicating an established mid-stage operation.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Structurer les modèles de données pour garantir leur lisibilité, leur performance et leur maintenabilité."
> Verified: ✓ found in JD
> Reasoning: Technical specificity about model structure, performance, and maintainability, plus governance frameworks and quality control mechanisms indicate hiring manager authorship.

**Run 2:** `hiring_manager`
> Quote: "Structurer la gouvernance data : ownership, accès, documentation, règles d'usage"
> Verified: ✓ found in JD
> Reasoning: The specific enumeration of data governance components (ownership, access, documentation, usage rules) demonstrates domain knowledge typical of someone with hands-on analytics engineering experience.

**Run 3:** `mixed`
> Quote: "Structurer les modèles de données pour garantir leur lisibilité, leur performance et leur maintenabilité"
> Verified: ✓ found in JD
> Reasoning: Technical specificity about data modeling properties and semantic layers appears alongside generic boilerplate action verbs, indicating mixed hiring manager and recruiter input.

⚠ **LLM inconsistency**: runs gave ['hiring_manager', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "Participer à l'activation des données pour les équipes métiers (marketing, produit, direction…)."
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves three distinct stakeholder categories—marketing (commercial), product (product), and direction (finance/leadership)—with roughly equal emphasis.

**Run 2:** `mixed`
> Quote: "Participer à l'activation des données pour les équipes métiers (marketing, produit, direction…)"
> Verified: ✓ found in JD
> Reasoning: The role explicitly serves marketing, product, and executive teams across multiple clients and sectors, spanning commercial, product, and finance stakeholder categories with roughly equal emphasis.

**Run 3:** `internal_data`
> Quote: "Construire des semantic layers facilitant l'exploitation des données par les équipes"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize building data infrastructure and governance to enable team access to data rather than optimizing for specific commercial or product domains.

⚠ **LLM inconsistency**: runs gave ['mixed', 'mixed', 'internal_data']

### autonomy_level

**Run 1:** `execution`
> Quote: "Tu participeras à des projets variés mêlant engineering, analytics, gouvernance et data products."
> Verified: ⚠ NOT found verbatim
> Reasoning: The use of 'participate in' indicates execution within defined client project scope rather than strategic direction-setting for the analytics practice.

**Run 2:** `execution`
> Quote: "tu participeras à des projets variés mêlant engineering, analytics, gouvernance et data products"
> Verified: ✓ found in JD
> Reasoning: The role is framed as participating in projects rather than owning or defining them, indicating execution of scope set by client needs rather than strategic direction-setting.

**Run 3:** `execution`
> Quote: "Tu participeras à l'activation des données pour les équipes métiers"
> Verified: ⚠ NOT found verbatim
> Reasoning: The consistent use of "participate in" rather than "define", "own", or "lead" indicates execution of client-scoped projects rather than strategic direction-setting.
