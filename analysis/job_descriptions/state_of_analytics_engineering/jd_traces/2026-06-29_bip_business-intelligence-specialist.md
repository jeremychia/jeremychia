# Trace: 2026-06-29_bip_business-intelligence-specialist

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Specialist — BIP (Business Integration Partners)

**URL:** https://fa-etjb-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1326
**Location:** Milano, Lombardia, Italy
**Date Posted:** 2026-06-29

---

Business Intelligence Specialist - Google
Milano, Lombardia, Italy

Job Description
Entra nel nostro mondo.

Trasforma insieme a noi.

Business Intelligence Specialist

Quale sarà la tua sfida?

In qualità di Business Intelligence Specialist, svolgerai un ruolo fondamentale nella fornitura di soluzioni tecniche e application-based nei progetti di Business Intelligence. Ciò comporta l'analisi e lo sviluppo di soluzioni di visualizzazione dei dati per iniziative basate su progetti o come servizio per i clienti. Ti impegnerai nella raccolta e nella valutazione dei requisiti aziendali, garantendone l'accuratezza e la pertinenza. Le tue responsabilità includono l'analisi dell'origine dei dati, la modellazione dei dati e l'implementazione di servizi di progettazione dei dati con competenza metodica.
Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP. Questi strumenti ti aiuteranno a creare rappresentazioni dei dati di grande impatto, fornendo metriche che consentono un processo decisionale aziendale solido e basato sui dati. Inoltre, potresti essere incaricato di riassumere analisi complesse condotte da altri esperti, tra cui Data Scientist, esperti di Data Governance, Data Architect e Project Manager.
In base alla tua esperienza, potrai anche dimostrare e costruire relazioni con i clienti, collaborare con vendor e partner tecnologici e comunicare i tuoi risultati in modo efficace a colleghi e clienti. Inoltre, potrai guidare e coordinare junior analyst all'interno dei team di progetto.

Sarai tu ad entrare nel nostro Team?

Requisiti Indispensabili:

Laurea Specialistica in Ingegneria Informatica, Ingegneria Matematica, Ingegneria delle Telecomunicazioni, Informatica, Statistica, Ingegneria Gestionale o discipline affini (STEM)
Competenza in almeno una tecnologia di visualizzazione dei dati (ad esempio, Looker, Tableau, PowerBI, QlikSense) ed esperienza nell'estrazione, pulizia, modellazione e analisi dei dati utilizzando strumenti come MS Excel, SQL, SAS e Python
Ottima conoscenza e competenza in ambito SQL e capacità funzionale di data analysis IT-based
Conoscenza fluente di italiano e inglese

Plus:

Capacità di realizzare stored procedure, SQL function e conoscenza delle funzionalità di BigQuery
MS Excel avanzato (VBA programming)
Familiarità con Python, R, Java, C++, Javascript/HTML, PHP
Esperienza in progetti che utilizzano modelli di AI (Gemini, OpenAI, altro) che servono a generare insights dei dati

Soft Skills:

Standing consulenziale con ottime doti relazionali e comunicative
Orientamento al cliente e al raggiungimento degli obiettivi
Buona attitudine a lavorare in team e grande attenzione al dettaglio
Precisione e stress tolerance nel rispetto delle scadenze
Disponibilità per trasferte in Italia e all'estero

Perchè Bip?

Crescita e Formazione
Più di 300 corsi su tecnologie e business emergenti, programmi di sviluppo personalizzati e iniziative di training e people care per supportare la tua crescita professionale e personale.

Flessibilità e Work-Life Integration
Lavoro agile con possibilità di programmare le giornate da remoto e in ufficio con il proprio responsabile e in base alle esigenze di progetto, Banca Ore Solidale per usufruire o mettere a disposizione ore di permesso a colleghi e colleghe che vivono momenti di difficoltà e una cultura che favorisce l'equilibrio tra vita e lavoro.

Salute & Benefits
Assicurazione sanitaria, check-up agevolati, piattaforme per il benessere psicofisico e un piano welfare integrativo. Ticket restaurant e altri benefit dedicati.

Famiglia e Genitorialità
Supporto concreto a neogenitori: integrazione al 100% per i primi 3 mesi del congedo parenta…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | moderate | moderate | 100% |
| collaboration_width | 5 | 5 | 6 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | mixed | hiring_manager | mixed | 33% |
| stakeholder_orientation | mixed | commercial | commercial | 33% |
| autonomy_level | execution | execution | execution | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "implementazione di servizi di progettazione dei dati con competenza metodica"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize methodical, precise implementation and data accuracy with no signals of speed, MVP delivery, or iteration velocity.

**Run 2:** `rigour`
> Quote: "garantendone l'accuratezza e la pertinenza"
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes accuracy, precision, methodical competence, and attention to detail across multiple sections, with no velocity-oriented language like 'fast-paced' or 'rapid delivery'.

**Run 3:** `rigour`
> Quote: "garantendone l'accuratezza e la pertinenza"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize accuracy, relevance, methodical competence, and attention to detail, with no velocity or speed-oriented language present.

### domain_risk

**Run 1:** `moderate`
> Quote: "soluzioni di visualizzazione dei dati per iniziative basate su progetti o come servizio per i clienti"
> Verified: ✓ found in JD
> Reasoning: The role creates BI solutions for clients' business decisions but without explicit financial reporting, regulatory, or compliance context that would indicate high risk.

**Run 2:** `moderate`
> Quote: "fornitura di soluzioni tecniche e application-based nei progetti di Business Intelligence"
> Verified: ✓ found in JD
> Reasoning: The JD describes delivering BI solutions to clients without explicit financial reporting, compliance, or regulatory language typical of high-risk domains.

**Run 3:** `moderate`
> Quote: "fornendo metriche che consentono un processo decisionale aziendale solido e basato sui dati"
> Verified: ✓ found in JD
> Reasoning: The role supports business intelligence and business decision-making but contains no financial reporting, regulatory, or compliance language that would signal high-risk domain impact.

### collaboration_width

**Run 1:** `5`
> Quote: "Data Scientist, esperti di Data Governance, Data Architect e Project Manager; clienti"
> Verified: ⚠ NOT found verbatim
> Reasoning: Five named partner teams identified: Data Scientist, Data Governance experts, Data Architect, Project Manager, and clients as explicit collaboration partners.

**Run 2:** `5`
> Quote: "Data Scientist; esperti di Data Governance; Data Architect; Project Manager; clienti"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD explicitly names five distinct collaboration partners: Data Scientists, Data Governance experts, Data Architects, Project Managers, and clients.

**Run 3:** `6`
> Quote: "Data Scientist, esperti di Data Governance, Data Architect e Project Manager; clienti; vendor e partner tecnologici"
> Verified: ⚠ NOT found verbatim
> Reasoning: Six distinct named teams/functions are explicitly identified as collaboration partners: Data Scientists, Data Governance experts, Data Architects, Project Managers, clients, and technology vendors/partners.

⚠ **LLM inconsistency**: runs gave ['5', '5', '6']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP"
> Verified: ✓ found in JD
> Reasoning: Named tools already deployed with specific application context, plus conditional leadership of junior analysts, indicates existing infrastructure and team growth rather than greenfield build.

**Run 2:** `mid`
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP"
> Verified: ✓ found in JD
> Reasoning: The mention of established deployment tools (Looker and GCP) and the ability to coordinate junior analysts indicates a data function that exists with infrastructure and is growing, not early-stage or mature at scale.

**Run 3:** `mid`
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP"
> Verified: ✓ found in JD
> Reasoning: Named tools appear in responsibilities with specific context (Looker, GCP), multiple established data roles are referenced, and the mention of junior analysts to coordinate indicates an organized team structure beyond greenfield stage.

### jd_authorship

**Run 1:** `mixed`
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP; comunicare i tuoi risultati in modo efficace a colleghi e clienti"
> Verified: ⚠ NOT found verbatim
> Reasoning: Specific technical responsibilities with named tools and methodologies suggest hiring manager input, but generic relationship-building language indicates recruiter scaffolding.

**Run 2:** `hiring_manager`
> Quote: "analisi dell'origine dei dati, la modellazione dei dati e l'implementazione di servizi di progettazione dei dati"
> Verified: ✓ found in JD
> Reasoning: The JD contains specific technical responsibilities (data source analysis, data modeling, data design services) with named tools (Looker, GCP) applied to concrete deliverables, demonstrating knowledge of actual job work rather than generic competencies.

**Run 3:** `mixed`
> Quote: "svolgerai un ruolo fondamentale nella fornitura di soluzioni tecniche e application-based; Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP"
> Verified: ⚠ NOT found verbatim
> Reasoning: The JD mixes generic language (delivering technical solutions) with specific technical knowledge (Looker, GCP named tools), suggesting input from both HR/recruiting and someone with direct BI project experience.

⚠ **LLM inconsistency**: runs gave ['mixed', 'hiring_manager', 'mixed']

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "metriche che consentono un processo decisionale aziendale solido e basato sui dati"
> Verified: ✓ found in JD
> Reasoning: The role creates general business analytics for clients across their organization without emphasis on a specific stakeholder function (commercial, product, finance, or internal data).

**Run 2:** `commercial`
> Quote: "costruire relazioni con i clienti, collaborare con vendor e partner tecnologici"
> Verified: ✓ found in JD
> Reasoning: The role explicitly prioritizes building client relationships and working with external technology partners, positioning external clients as the primary audience for delivered BI solutions.

**Run 3:** `commercial`
> Quote: "dimostrare e costruire relazioni con i clienti"
> Verified: ✓ found in JD
> Reasoning: The role explicitly emphasizes client relationships, consulting standing, and customer orientation in a consulting firm context, positioning the commercial stakeholder (clients) as the primary audience.

⚠ **LLM inconsistency**: runs gave ['mixed', 'commercial', 'commercial']

### autonomy_level

**Run 1:** `execution`
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici"
> Verified: ✓ found in JD
> Reasoning: Core responsibilities are delivery-focused implementation of BI solutions with client requirements defining the scope, while strategic elements like leading junior analysts are secondary and conditional.

**Run 2:** `execution`
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici"
> Verified: ✓ found in JD
> Reasoning: The responsibilities emphasize delivering and implementing specific BI systems based on collected business requirements, rather than defining analytics strategy or shaping how analytics is organized.

**Run 3:** `execution`
> Quote: "Ti impegnerai nella raccolta e nella valutazione dei requisiti aziendali"
> Verified: ✓ found in JD
> Reasoning: The core responsibilities involve gathering requirements set by others, implementing solutions to specifications, and delivering against scoped work rather than defining analytical strategy or direction.

### ai_role
**Run 1:** `none` ✓
> Quote: "Looker, Google GCP, BigQuery, stored procedures"
> Reasoning: No AI coding tools or GenAI infrastructure mentioned; traditional BI and analytics stack only.

**Run 2:** `none` ✓
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici utilizzando gli strumenti Looker e Google GCP"
> Reasoning: Role focuses on data visualization and analytics tools without AI/ML or AI-assisted coding responsibilities.

**Run 3:** `none` ✓
> Quote: ""
> Reasoning: No AI tools (Copilot, Claude Code, Cursor) or GenAI infrastructure capabilities mentioned; listed tools are Looker, GCP, BigQuery—standard analytics platforms.


### testing_framing
**Run 1:** `absent` ✓
> Quote: "garantendone l'accuratezza e la pertinenza"
> Reasoning: Individual precision and accuracy emphasized, but no ownership of testing practices, quality frameworks, or data contracts.

**Run 2:** `absent` ✓
> Quote: "Svilupperai sistemi di analisi delle performance, report interattivi e dashboard analitici"
> Reasoning: Focus on analysis and visualization delivery; no testing ownership, practices, or tools mentioned.

**Run 3:** `absent` ✓
> Quote: "garantendone l'accuratezza e la pertinenza"
> Reasoning: Quality required via accuracy and precision in deliverables but no testing ownership responsibility or framework implementation evident.


### loss_aversion_framing
**Run 1:** `none` ✓
> Quote: "No loss aversion framing detected"
> Reasoning: Delivery and project outcome focus with no compliance, regulatory, or operational reliability risk language.

**Run 2:** `none` ✓
> Quote: "precisione e stress tolerance nel rispetto delle scadenze; garantendone l'accuratezza e la pertinenza"
> Reasoning: JD emphasizes delivery accuracy and deadline management without compliance, regulatory, or trustworthiness dominance.

**Run 3:** `none` ✓
> Quote: "BIP is a consulting firm; the JD contains no explicit financial/regulatory/compliance language"
> Reasoning: Role prioritizes precision and deadline delivery over compliance, audit, or data trustworthiness framing; no loss-aversion signals present.

