# Trace: 2026-06-27_m13h_lead-analytics-engineer

## JD text (fed to classifier, Layer B stripped)

```
# Lead Analytics Engineer (H/F) — M13h

**Location:** Lyon, France
**Date Posted:** 2026-06-27
**Salary:** 60,000–70,000 EUR

---

En tant qu'Analytics Engineer, basé dans notre bureau de Lyon, tu interviens sur des problématiques à la croisée de la data science, de la data analyse et de la data ingénierie et ton rôle est de mettre en place pour nos clients ou nos besoins internes des datasets pertinents : bien modélisés, documentés, fiables en termes de qualité et de disponibilité, répondant aux besoins des usages ultérieurs.

En tant que lead, tu portes une expertise et la fait rayonner au sein du cabinet et à l'extérieur et participe à la formalisation d'offres sur la base de ton expertise.

Pour cela, tu interviens à différents stades des projets :

Analyse des besoins d'accès aux données, en collaboration avec les utilisateurs business, data analysts et dataviz engineers

Mise en place des flux et modèles de données, en se basant sur des stacks data modernes (SQL, DBT, outils ELTs, GCP/Azure/AWS/Snowflake, …)

Exposition des données dans les outils BI & visualisation

Maintenance des pipelines et mise en place d'alertes & tests de qualité de données

Quelques exemples de missions à titre d'illustration :

Construction d'une Customer Data Platform pour un grand retailer (8 marques / 30+ pays)

Migration d'une large infrastructure de dashboards basés sur un stack Supermetrics vers un stack Adverity+BigQuery

Mise en place d'outils de pilotage de bout en bout pour plusieurs startups en forte croissance

Packaging d'outils internes sur l'attribution custom

Polyvalent·e, tu as à cœur de comprendre les besoins de tes interlocuteurs pour les traduire en structures de données exploitables et de bonne qualité. Tu sais travailler en autonomie sur tes missions et tu as le souhait d'accompagner et faire progresser des consultant·e·s plus jeunes sur ton expertise et sur les stacks data modernes.

**Profil recherché**

Issu·e d'une grande école de commerce, d'ingénieurs ou équivalent, tu disposes d'au moins 5 années d'expérience professionnelle.

Tu maîtrises les technologies/outils/environnements suivants:

- GCP / Microsoft Azure / AWS
- Snowflake
- Python & SQL
- Airflow / DBT
- Git

Tu as de bonnes capacités d'analyse et sais gérer un projet analytique de bout en bout en faisant preuve d'autonomie et de rigueur. Tu as déjà été amené à travailler/ tu souhaites travailler sur des problématiques de data marketing et tu as déjà eu des expériences/ tu souhaites travailler dans le monde du conseil.

Langues parlées: Français/Anglais

**Informations supplémentaires**

Processus de recrutement en 3 étapes incluant une étude de cas

Le groupe Cosmo5 inscrit la diversité et la mixité durant tout son processus de recrutement afin de garantir un environnement de travail accessible à toutes et tous.

---
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 3 | 2 | 3 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | internal_data | internal_data | internal_data | 100% |
| autonomy_level | mixed | execution | mixed | 33% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes documentation, reliability, quality, and availability as core dataset properties, with no mention of speed, iteration, or rapid delivery.

**Run 2:** `rigour`
> Quote: "bien modélisés, documentés, fiables en termes de qualité et de disponibilité, répondant aux besoins des usages ultérieurs"
> Verified: ✓ found in JD
> Reasoning: The role is framed around creating well-structured, reliable, documented datasets with explicit quality and availability guarantees, with no mention of speed or rapid iteration.

**Run 3:** `rigour`
> Quote: "mise en place d'alertes & tests de qualité de données"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize data quality testing, documentation, and reliability as core expectations, with no velocity-oriented language present.

### domain_risk

**Run 1:** `moderate`
> Quote: "Construction d'une Customer Data Platform pour un grand retailer (8 marques / 30+ pays)"
> Verified: ✓ found in JD
> Reasoning: The mission examples cover general business analytics and SaaS work for retail and startups without explicit financial reporting, regulatory compliance, or mission-critical language.

**Run 2:** `moderate`
> Quote: "datasets pertinents : bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Verified: ✓ found in JD
> Reasoning: While data quality is emphasized, the JD lacks explicit financial reporting, compliance, or regulatory language that would signal high domain risk in a consulting context.

**Run 3:** `moderate`
> Quote: "Construction d'une Customer Data Platform pour un grand retailer (8 marques / 30+ pays)"
> Verified: ✓ found in JD
> Reasoning: The work affects business decisions across multiple markets and functions but lacks explicit financial, compliance, or regulatory language that would indicate high risk.

### collaboration_width

**Run 1:** `3`
> Quote: "les utilisateurs business, data analysts et dataviz engineers"
> Verified: ✓ found in JD
> Reasoning: Three distinct named collaborating teams are identified: business users, data analysts, and dataviz engineers.

**Run 2:** `2`
> Quote: "data analysts; dataviz engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Two distinct named functions are explicitly listed as collaboration partners in the main responsibilities section.

**Run 3:** `3`
> Quote: "utilisateurs business; data analysts; dataviz engineers"
> Verified: ⚠ NOT found verbatim
> Reasoning: Three distinct named partner functions are explicitly listed in the collaboration requirements.

⚠ **LLM inconsistency**: runs gave ['3', '2', '3']

### data_team_maturity

**Run 1:** `mid`
> Quote: "mise en place des flux et modèles de données, en se basant sur des stacks data modernes (SQL, DBT, outils ELTs, GCP/Azure/AWS/Snowflake, …)"
> Verified: ✓ found in JD
> Reasoning: Modern data tools are embedded in current responsibilities and the lead role mentoring junior consultants suggests an established but growing consulting practice.

**Run 2:** `mid`
> Quote: "Mise en place des flux et modèles de données, en se basant sur des stacks data modernes (SQL, DBT, outils ELTs, GCP/Azure/AWS/Snowflake, …)"
> Verified: ✓ found in JD
> Reasoning: Multiple named data tools are mentioned in operational contexts (responsibilities, not just requirements), indicating an established function with operational maturity.

**Run 3:** `mid`
> Quote: "tu as le souhait d'accompagner et faire progresser des consultant·e·s plus jeunes sur ton expertise et sur les stacks data modernes"
> Verified: ✓ found in JD
> Reasoning: The presence of junior consultants to mentor and established tooling (DBT, Snowflake, GCP/Azure/AWS, Airflow) indicates a growing data function with defined practices.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Construction d'une Customer Data Platform pour un grand retailer (8 marques / 30+ pays)"
> Verified: ✓ found in JD
> Reasoning: Mission examples contain specific tool stacks, business scale details, and real technical challenges that indicate authorship by someone with hands-on technical experience.

**Run 2:** `hiring_manager`
> Quote: "Construction d'une Customer Data Platform pour un grand retailer (8 marques / 30+ pays); Migration d'une large infrastructure de dashboards basés sur un stack Supermetrics vers un stack Adverity+BigQuery"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific project examples with scale and tool context (Supermetrics, Adverity, BigQuery) reflect hands-on experience rather than generic recruiter language.

**Run 3:** `hiring_manager`
> Quote: "Migration d'une large infrastructure de dashboards basés sur un stack Supermetrics vers un stack Adverity+BigQuery"
> Verified: ✓ found in JD
> Reasoning: Specific tool applications in concrete project contexts and detailed technical examples indicate authorship by someone with hands-on data engineering experience.

### stakeholder_orientation

**Run 1:** `internal_data`
> Quote: "ton rôle est de mettre en place pour nos clients ou nos besoins internes des datasets pertinents : bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is building reliable, well-documented datasets and data infrastructure that serve data consumers and other analytics practitioners.

**Run 2:** `internal_data`
> Quote: "ton rôle est de mettre en place pour nos clients ou nos besoins internes des datasets pertinents : bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Verified: ✓ found in JD
> Reasoning: The primary focus is creating and maintaining high-quality data infrastructure and datasets that serve the data ecosystem, not a specific business function.

**Run 3:** `internal_data`
> Quote: "mettre en place pour nos clients ou nos besoins internes des datasets pertinents"
> Verified: ✓ found in JD
> Reasoning: The role's primary purpose is to build and maintain data infrastructure and datasets for consumption by other analysts, BI engineers, and platform consumers.

### autonomy_level

**Run 1:** `mixed`
> Quote: "tu portes une expertise et la fait rayonner au sein du cabinet et à l'extérieur et participe à la formalisation d'offres sur la base de ton expertise"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic leadership (defining offerings, establishing expertise) with execution across specific scoped projects and client engagements.

**Run 2:** `execution`
> Quote: "tu interviens à différents stades des projets"
> Verified: ✓ found in JD
> Reasoning: The role is primarily framed around implementing and maintaining solutions within scoped projects, with autonomy within those projects rather than defining the firm's overall analytics direction.

**Run 3:** `mixed`
> Quote: "tu portes une expertise et la fait rayonner au sein du cabinet et à l'extérieur et participe à la formalisation d'offres sur la base de ton expertise"
> Verified: ✓ found in JD
> Reasoning: The role combines strategic elements (thought leadership, offer development, mentoring junior consultants) with core execution responsibilities (implementing datasets, maintaining pipelines).

⚠ **LLM inconsistency**: runs gave ['mixed', 'execution', 'mixed']

### ai_role
**Run 1:** `none` ✓
> Quote: "No AI-related phrases in JD"
> Reasoning: No mention of AI tools, GenAI, text-to-SQL, semantic models, or AI-assisted coding; standard analytics engineering work

**Run 2:** `none` ✓
> Quote: "Migration d'une large infrastructure de dashboards basés sur un stack Supermetrics vers un stack Adverity+BigQuery"
> Reasoning: Traditional data infrastructure migration with no AI tooling, building, or enablement mentioned.

**Run 3:** `none` ✓
> Quote: "Migration d'une large infrastructure de dashboards basés sur un stack Supermetrics vers un stack Adverity+BigQuery"
> Reasoning: Infrastructure modernization with no AI tools, enablement, or AI-first responsibilities mentioned.


### testing_framing
**Run 1:** `responsibility` ✓
> Quote: "ton rôle est de mettre en place pour nos clients ou nos besoins internes des datasets pertinents : bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Reasoning: Candidate owns implementing datasets with explicit quality and reliability standards

**Run 2:** `responsibility` ✓
> Quote: "ton rôle est de mettre en place pour nos clients ou nos besoins internes des datasets pertinents : bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Reasoning: Candidate owns designing, modeling, documenting, and ensuring quality/reliability of datasets.

**Run 3:** `absent` ✗
> Quote: "bien modélisés, documentés, fiables en termes de qualité et de disponibilité"
> Reasoning: Quality/availability as dataset outcome requirement without explicit testing practice ownership or tool mention.

⚠ **LLM inconsistency**: runs gave ['responsibility', 'responsibility', 'absent']

### loss_aversion_framing
**Run 1:** `moderate` ✓
> Quote: "fiables en termes de qualité et de disponibilité"
> Reasoning: Operational reliability framing (availability, quality) without regulatory or compliance language

**Run 2:** `moderate` ✓
> Quote: "fiables en termes de qualité et de disponibilité"
> Reasoning: Emphasis on reliability and availability signals operational concerns about data stability rather than purely delivery-focused or compliance-driven framing.

**Run 3:** `moderate` ✓
> Quote: "fiables en termes de qualité et de disponibilité"
> Reasoning: Operational reliability framing (quality and availability) without compliance or regulatory dominance.

