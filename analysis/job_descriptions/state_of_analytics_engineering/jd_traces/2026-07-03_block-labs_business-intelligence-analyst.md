# Trace: 2026-07-03_block-labs_business-intelligence-analyst

## JD text (fed to classifier, Layer B stripped)

```
# Business Intelligence Analyst — Block Labs

**URL:** https://jobs.ashbyhq.com/block-labs/06e721f0-df84-4eab-a4f3-be0c1614d458/application
**Location:** Remote
**Date Posted:** 2026-07-03

---

Business Intelligence Analyst

Block Labs is a premier technology studio operating at the bleeding edge of Web3, Artificial Intelligence, and iGaming. We don't just ship features; we engineer high-scale, production-grade platforms that power the next generation of digital products.

About The Role
We're looking for a data-obsessed BI Analyst to turn blockchain and product data into crisp insights that drive growth, retention, and risk controls across our crypto-enabled iGaming products. You'll own the end-to-end analytics stack for wallet funnels, wagering behavior, lifecycle marketing, and compliance—using SQL, DBT, Python, Amplitude and Tableau as your primary tools.

Key Responsibilities
• Drive the business forward through proactive analytics - spot anomalies, frame the right question yourself, and bring actionable recommendations to Product / CRM / Risk before they have to ask.
• Build, maintain, and iterate dashboards surfacing KPIs (GGR/NGR, ARPU, LTV, churn, deposit→wager conversion, fraud loss rate).
• Write production-grade SQL (CTEs, window functions, incremental models) to model clean datasets from Clickhouse and on-chain tables.
• Build and maintain AI-agent workflows that automate recurring analytics - anomaly investigation, root-cause loops etc.
• Use Python (pandas, seaborn, sklearn, scipy) for analysis, data quality checks, lightweight ETL/backfills, API pulls (e.g., blockchain providers), and automation.
• Work with on-chain data: parse EVM logs, token transfers (ERC-20/721), join labeled address datasets, analyze exchange/bridge flows, gas/fee dynamics, and wallet clustering.
• Partner with Product, Marketing/CRM, Risk/Compliance, and Engineering to define event schemas and tracking plans; ensure data quality, lineage, and documentation.
• Design and analyze experiments, cohort analyses, and attribution within iGaming and regional compliance constraints.
• Investigate anomalies (bonus abuse, botting, arbitrage, suspicious wallet rings) and recommend mitigations.
• Automate recurring reporting and alerting for KPI movements.

Must-haves
• 2+ years in BI or Data Analytics; crypto or iGaming exposure preferred.
• Ambitions about building great analytics infrastructure.
• Good SQL: complex joins, window functions, query optimization, and dimensional modeling.
• Solid AI-collaboration craft — prompt & context engineering, spec-driven task framing, and eval-driven iteration.
• BI Versatility: Expert knowledge of Tableau (LODs, parameters, performance tuning) combined with strong interest or experience in modern, open-source BI tools like Metabase or Apache Superset.
• Proficient Python for analytics & data engineering: pandas, modular scripts/notebooks, API integrations, scheduling small jobs, and writing maintainable code.
• Solid statistics and probability fundamentals for experimentation - hypothesis testing, sample size and power, confidence intervals, and the discipline to distinguish real signal from noise.
• Practical understanding of crypto wallets and transaction flows.

Nice-to-haves
• dbt, Great Expectations/Monte Carlo for data quality; orchestration with Airflow/Prefect.
• Built or contributed to production AI agents for analytics — ReAct loops, RAG over a knowledge base , MCP servers for data sources, multi-agent orchestration.
• Ability to produce on-chain analytics (Dune/Flipside/Goldsky/Nansen tables or self-indexed data; contract ABIs; entity labeling).
• Warehouse ecosystems knowledge Clickhouse, AWS, S3 buckets.
• Data governance & privacy (GDPR, data minimization, retention policies).
• Understanding of iGaming economics & KPIs: deposits, wagers, hold, GGR/NGR, RTP, bonus efficiency, RG metrics, and common fraud/AML patterns.
• Experience with product analytics services like Amplitude, Mixpanel, Google…[truncated]
```

---

## Classification results

| Dimension | Run 1 | Run 2 | Run 3 | Agreement |
|-----------|-------|-------|-------|-----------|
| velocity_vs_rigour | rigour | rigour | rigour | 100% |
| domain_risk | moderate | high | moderate | 33% |
| collaboration_width | 6 | 4 | 4 | 33% |
| data_team_maturity | mid | mid | mid | 100% |
| jd_authorship | hiring_manager | hiring_manager | hiring_manager | 100% |
| stakeholder_orientation | mixed | mixed | mixed | 100% |
| autonomy_level | execution | mixed | strategic | 0% |
| ai_role | ai_enabler | ai_enabler | ai_user | 33% |
| testing_framing | responsibility | responsibility | responsibility | 100% |
| loss_aversion_framing | moderate | moderate | moderate | 100% |

---

## Evidence per dimension

### velocity_vs_rigour

**Run 1:** `rigour`
> Quote: "Write production-grade SQL (CTEs, window functions, incremental models) to model clean datasets from Clickhouse and on-chain tables."
> Verified: ✓ found in JD
> Reasoning: Multiple rigour signals dominate the responsibilities section: production-grade emphasis, ensure data quality/lineage/documentation, and discipline to distinguish signal from noise; no velocity signals present.

**Run 2:** `rigour`
> Quote: "Write production-grade SQL (CTEs, window functions, incremental models) to model clean datasets from Clickhouse and on-chain tables."
> Verified: ✓ found in JD
> Reasoning: Multiple explicit quality and correctness signals (production-grade, clean datasets, precise SQL techniques, data quality checks, ensure lineage and documentation) with no velocity or shipping-speed emphasis.

**Run 3:** `rigour`
> Quote: "Write production-grade SQL (CTEs, window functions, incremental models) to model clean datasets from Clickhouse and on-chain tables."
> Verified: ✓ found in JD
> Reasoning: The JD emphasizes production-grade quality, rigorous methodology, data quality ownership, statistical discipline, and compliance constraints, with no emphasis on speed or rapid iteration.

### domain_risk

**Run 1:** `moderate`
> Quote: "Investigate anomalies (bonus abuse, botting, arbitrage, suspicious wallet rings) and recommend mitigations."
> Verified: ✓ found in JD
> Reasoning: Risk framing focuses on operational fraud/abuse detection rather than financial reporting, regulatory compliance, or audit exposure, placing this in moderate rather than high risk category.

**Run 2:** `high`
> Quote: "Investigate anomalies (bonus abuse, botting, arbitrage, suspicious wallet rings) and recommend mitigations."
> Verified: ✓ found in JD
> Reasoning: Explicit fraud investigation and financial loss impact (fraud loss rate as a key KPI) combined with regulatory compliance constraints in a regulated iGaming/crypto domain.

**Run 3:** `moderate`
> Quote: "Design and analyze experiments, cohort analyses, and attribution within iGaming and regional compliance constraints."
> Verified: ✓ found in JD
> Reasoning: While iGaming involves regulated activities and financial transactions (GGR/NGR, fraud detection, AML patterns), the JD frames the role around insights and growth delivery rather than pure compliance or regulatory risk management.

⚠ **LLM inconsistency**: runs gave ['moderate', 'high', 'moderate']

### collaboration_width

**Run 1:** `6`
> Quote: "Product; Marketing; CRM; Risk; Compliance; Engineering"
> Verified: ✓ found in JD
> Reasoning: Six distinct named partner functions explicitly listed across the JD: Product and CRM and Risk are mentioned in partnership statements; Marketing, Risk, Compliance, and Engineering are named in collaboration language.

**Run 2:** `4`
> Quote: "Product; Marketing/CRM; Risk/Compliance; Engineering"
> Verified: ✓ found in JD
> Reasoning: Four distinct named partner functions explicitly listed in the collaboration requirement.

**Run 3:** `4`
> Quote: "Product; Marketing/CRM; Risk/Compliance; Engineering"
> Verified: ✓ found in JD
> Reasoning: Four distinct named partner teams are explicitly listed in the responsibilities section.

⚠ **LLM inconsistency**: runs gave ['6', '4', '4']

### data_team_maturity

**Run 1:** `mid`
> Quote: "Write production-grade SQL (CTEs, window functions, incremental models) to model clean datasets from Clickhouse and on-chain tables."
> Verified: ✓ found in JD
> Reasoning: Named tools (Clickhouse, dbt, Amplitude, Tableau) in active use with specific responsibilities to maintain/iterate suggest established infrastructure beyond early-stage, but no indication of large specialized sub-teams or mature-scale governance.

**Run 2:** `mid`
> Quote: "Write production-grade SQL (CTEs, window functions, incremental models) to model clean datasets from Clickhouse and on-chain tables."
> Verified: ✓ found in JD
> Reasoning: Existing infrastructure (Clickhouse, on-chain data systems) with production-grade expectations and named tools (DBT, Tableau, Amplitude) in use indicates established but growing data function.

**Run 3:** `mid`
> Quote: "Build, maintain, and iterate dashboards surfacing KPIs (GGR/NGR, ARPU, LTV, churn, deposit→wager conversion, fraud loss rate)."
> Verified: ✓ found in JD
> Reasoning: Named tools in responsibilities (Clickhouse, DBT, Tableau, Amplitude) indicate existing infrastructure beyond early stage, but no signals of a large, specialized, multi-team organization.

### jd_authorship

**Run 1:** `hiring_manager`
> Quote: "Work with on-chain data: parse EVM logs, token transfers (ERC-20/721), join labeled address datasets, analyze exchange/bridge flows, gas/fee dynamics, and wallet clustering."
> Verified: ✓ found in JD
> Reasoning: Technical specificity about on-chain data parsing, ERC standards, and domain-specific methodologies reflects deep product knowledge only someone doing this work would possess.

**Run 2:** `hiring_manager`
> Quote: "Use Python (pandas, seaborn, sklearn, scipy) for analysis, data quality checks, lightweight ETL/backfills, API pulls (e.g., blockchain providers), and automation."
> Verified: ✓ found in JD
> Reasoning: Exact Python library names, specific use cases, and technical depth (blockchain provider APIs, specific protocols) indicate authorship by someone who performs this work.

**Run 3:** `hiring_manager`
> Quote: "parse EVM logs, token transfers (ERC-20/721), join labeled address datasets, analyze exchange/bridge flows, gas/fee dynamics, and wallet clustering"
> Verified: ✓ found in JD
> Reasoning: Highly specific on-chain technical detail (EVM logs, token standards, wallet clustering, exchange flows) and domain-specific KPIs that only someone with hands-on experience in this role could have written.

### stakeholder_orientation

**Run 1:** `mixed`
> Quote: "bring actionable recommendations to Product / CRM / Risk before they have to ask."
> Verified: ✓ found in JD
> Reasoning: Role explicitly serves three distinct audiences (Product for growth/experiments, CRM for lifecycle/revenue metrics, Risk for fraud/compliance) with genuinely split responsibilities across all three.

**Run 2:** `mixed`
> Quote: "bring actionable recommendations to Product / CRM / Risk before they have to ask."
> Verified: ✓ found in JD
> Reasoning: Role explicitly serves three distinct audiences with equal emphasis: Product (experiments, funnels), Commercial/CRM (lifecycle marketing, churn, LTV), and Risk (compliance, fraud investigation).

**Run 3:** `mixed`
> Quote: "bring actionable recommendations to Product / CRM / Risk before they have to ask"
> Verified: ✓ found in JD
> Reasoning: The role serves multiple primary audiences with equal weight: Product (experimentation, cohort analysis), CRM (lifecycle marketing), and Risk (fraud/compliance), rather than emphasizing one.

### autonomy_level

**Run 1:** `execution`
> Quote: "Build, maintain, and iterate dashboards surfacing KPIs (GGR/NGR, ARPU, LTV, churn, deposit→wager conversion, fraud loss rate)."
> Verified: ✓ found in JD
> Reasoning: Primary framing is delivery-oriented (build dashboards, write SQL, automate reporting); while the role has autonomy in problem-framing (frame questions yourself), direction is ultimately set by partnerships with Product/CRM/Risk.

**Run 2:** `mixed`
> Quote: "own the end-to-end analytics stack for wallet funnels, wagering behavior, lifecycle marketing, and compliance"
> Verified: ✓ found in JD
> Reasoning: Strategic ownership of the full analytics function combined with hands-on execution responsibilities (writing SQL, building dashboards, investigating anomalies).

**Run 3:** `strategic`
> Quote: "own the end-to-end analytics stack for wallet funnels, wagering behavior, lifecycle marketing, and compliance"
> Verified: ✓ found in JD
> Reasoning: The role explicitly owns and shapes the analytics infrastructure and event schema definitions, setting direction for how analytics is delivered rather than executing scoped work.

⚠ **LLM inconsistency**: runs gave ['execution', 'mixed', 'strategic']

### ai_role

**Run 1:** `ai_enabler`
> Quote: "Build and maintain AI-agent workflows that automate recurring analytics - anomaly investigation, root-cause loops etc"
> Verified: ✓ found in JD
> Reasoning: Candidate is expected to build data infrastructure and automation platforms that AI agents consume and run on, not just use AI tools for personal coding productivity.

**Run 2:** `ai_enabler`
> Quote: "Build and maintain AI-agent workflows that automate recurring analytics - anomaly investigation, root-cause loops etc."
> Verified: ✓ found in JD
> Reasoning: Candidate is expected to build and maintain AI agent systems (with ReAct loops, RAG, MCP servers mentioned in nice-to-haves) for analytics automation, not just use AI tools.

**Run 3:** `ai_user`
> Quote: "Solid AI-collaboration craft — prompt & context engineering, spec-driven task framing, and eval-driven iteration."
> Verified: ✓ found in JD
> Reasoning: The candidate is expected to use AI agents effectively (via prompt engineering and evaluation techniques) to automate their own analytics workflows and investigations, not to build data infrastructure for AI systems.

⚠ **LLM inconsistency**: runs gave ['ai_enabler', 'ai_enabler', 'ai_user']

### testing_framing

**Run 1:** `responsibility`
> Quote: "ensure data quality, lineage, and documentation."
> Verified: ✓ found in JD
> Reasoning: Ownership verb 'ensure' frames data quality as an explicit responsibility the candidate owns, not a tool listed in requirements.

**Run 2:** `responsibility`
> Quote: "ensure data quality, lineage, and documentation."
> Verified: ✓ found in JD
> Reasoning: Action verb 'ensure' in responsibilities section indicates the candidate owns data quality outcomes, not just uses tools.

**Run 3:** `responsibility`
> Quote: "ensure data quality, lineage, and documentation"
> Verified: ✓ found in JD
> Reasoning: Data quality is framed as an owned responsibility the candidate must ensure, using an active verb, not merely listed as a tool skill.

### loss_aversion_framing

**Run 1:** `moderate`
> Quote: "Investigate anomalies (bonus abuse, botting, arbitrage, suspicious wallet rings) and recommend mitigations."
> Verified: ✓ found in JD
> Reasoning: Primary fear is operational risk (fraud, abuse, anomalies) and data accuracy in business decisions; regulatory/compliance concerns are present but secondary to operational reliability focus.

**Run 2:** `moderate`
> Quote: "Investigate anomalies (bonus abuse, botting, arbitrage, suspicious wallet rings) and recommend mitigations."
> Verified: ✓ found in JD
> Reasoning: Explicit fraud investigation and mitigation are significant responsibilities, but risk/compliance is one of four equally-weighted domains rather than the dominant framing.

**Run 3:** `moderate`
> Quote: "Investigate anomalies (bonus abuse, botting, arbitrage, suspicious wallet rings) and recommend mitigations."
> Verified: ✓ found in JD
> Reasoning: Fraud prevention, AML pattern recognition, and loss investigation are significant concerns reflecting moderate risk aversion, but balanced equally with growth and retention objectives rather than dominating the role framing.
