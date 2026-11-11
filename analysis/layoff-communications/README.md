# How companies communicate layoffs

**832 layoff announcements from about 575 companies, 2021 to 11 Nov 2026**, each coded for who announced it, through which channel, the stated reasons, and (where the wording was verified) whether it apologised, took responsibility, or mentioned AI. Started from Canva's 4 Nov 2026 team update.

Open `data/corpus_v3.csv` first. `data/repeat_layoffs.csv` lists the repeat layoffers.

## How big is each year? (target: 140 per year)

| Year | Events | Target | Note |
|---|---|---|---|
| 2021 | 56 | **short** | Few layoffs happened and few are documented. I stopped rather than pad it. |
| 2022 | 149 | met | |
| 2023 | 231 | met | |
| 2024 | 154 | met | |
| 2025 | 142 | met | |
| 2026 | 100 | **short** | Year is incomplete (to 11 Nov); 10 months of data. |

## Read this first: what each tier can and can't tell you

| Tier | Events | Source | Use it for |
|---|---|---|---|
| **A** | 158 | Wording verified: quotes are exact substrings of the company's own text (53), a news reproduction of it (97), or a CEO letter filed with the SEC (8) | Apology / responsibility / AI-framing claims |
| **S** | 597 | SEC filing (8-K or 6-K): the company's own factual disclosure, extracted automatically | Who / when / how many / reasons. **Not** apology or responsibility (legal text) |
| **B** | 77 | News coverage only | Who / when / how many |

Things that would bite you:
- **The sample is 73% SEC filings, and 31% biotech.** Most S events are small public companies (many biotechs, often 30%+ cuts) announcing in dry legal language. Headline stats are computed on non-biotech events or on tier A, as labelled below. The famous CEO memos are the 136 hand-researched events.
- **Wording stats rest on 158 tier A events**, coded by research agents, not double-coded. Some fields (apology, responsibility) are blank when the text couldn't be read.
- **Event date for S events is the filing date**, which can lag the announcement by days.
- **Headcount from filings is machine-extracted.** 16 events (2.6%) are flagged `headcount_parse_uncertain` (for example, the number retained rather than cut).
- **Company text is found for only some events.** Many sites block automated fetches, and I did not circumvent that. I used plain fetches with an honest identity, the Wayback Machine, and SEC EDGAR (with a declared contact, as SEC requires). Where the company's page was unreachable, the quote comes from a news reproduction and is marked.
- **News coverage (215 events)** comes mainly from TechCrunch (91), CNBC (60), Fortune (42), Bloomberg (38), CNN (25) and Axios (13). The research tool couldn't reach Reuters, WSJ, NYT, FT, BBC, The Guardian or The Verge, so these are under-represented.
- **No S event has news coverage.**

## Do the same companies lay off again and again?

Yes, a lot of them. Of 582 companies in the corpus, **159 (27%) cut more than once**, 53 cut three or more times, and 104 had two rounds within 12 months. The median gap between rounds is about 10 months.
- **Most repeated** (counting separate announcements): Amazon 6 (Nov 2022 to Jan 2026, including its Devices unit), Meta 6, Atara Biotherapeutics 6, Blend Labs 5, Chegg 5, Unity 5, iRobot 5, Cruise 5, Microsoft 5.
- **Repeat rates by sector:** big tech 9 of 12 companies, consumer internet 14 of 32, hardware/auto 14 of 46, SaaS 33 of 114, biotech 48 of 194.
- **Blend Labs** is the clearest serial case: separate formal plans in Apr, Aug and Nov 2022, then Jan and Aug 2023.
- **I removed false repeats**: later earnings releases that merely re-describe an earlier plan (Sonos first looked like 8 cuts; it is 3).

How the later rounds are worded (20 companies with verified wording for at least two rounds):
- **Apology:** 7 companies apologised in an early round. None is coded as apologising again, though four of those later rounds couldn't be coded. Of 11 pairs coded both times, 3 went from apology to none, 1 went the other way, and 7 stayed the same.
- **Responsibility:** of 7 coded pairs, 5 dropped the explicit ownership.
- **Who speaks:** in 13 of the pairs a CEO or founder announced the first round; in 4 of those a different person (HR chief, spokesperson) announced the last. Stripe, Meta, Okta and Ford are examples.
- **AI:** 6 companies mentioned AI in the later round but not the first; only 1 did the reverse.
- **Size:** the second cut was larger than the first in 5 of 14 pairs where both are known.

## What else the larger corpus shows

1. **"We hired too fast" has gone away.** Among non-biotech events, overhiring was a stated reason in 13 of 100 events in 2022, 18 of 167 in 2023, 5 of 95 in 2024, then 1 of 101 in 2025 and 1 of 79 in 2026.
2. **AI has become the context.** Non-biotech events that mention AI: 1 of 100 in 2022, 9 of 167 in 2023, 5 of 95 in 2024, 28 of 101 in 2025, 24 of 79 in 2026. Mentioning AI is not blaming it: only some name it as the cause.
3. **The messenger gets less senior.** Excluding SEC filings, a CEO or founder announced 78% of cuts in 2022, 76% in 2023, 66% in 2024, 55% in 2025 and 57% in 2026. The rest are HR chiefs, other executives, spokespeople, earnings calls and leaks.
4. **Apology and ownership have faded, and my earlier headline was wrong.** An earlier version said responsibility was near-universal in 2022 to 2023 (16 of 17). That came from coding only the clear cases. With explicit "no" answers included it is **19 of 47** (7 of 20 in 2022, 12 of 27 in 2023). In 2025 it was **0 of 18** for both apology and responsibility. Apology by year (tier A): 7 of 23 in 2022, 10 of 46 in 2023, 5 of 21 in 2024, 0 of 18 in 2025, 1 of 7 in 2026.
5. **Apology varies by sector, but small samples.** SaaS 11 of 23, fintech/crypto 3 of 16, consumer internet 2 of 15, media/gaming 2 of 15, big tech 2 of 20 (Meta 2022 and Google 2023 are the two). 
6. **Typical cut size** (median): big tech 5%, SaaS 11%, consumer internet 13%, fintech/crypto 19.5%, biotech 34%. The all-corpus median is 16%, inflated by biotech.

## Canva (the trigger)

Canva's 4 Nov 2026 note was written by CEO Melanie Perkins and posted on its newsroom: 1,271 people (22%) affected, including role changes and relocations; "I'm deeply sorry" twice; "refounding Canva" by merging Product, Growth and Platform; slowed growth, not AI, as the reason. It is the opposite of Amazon's or Microsoft's recent wording: named owner, explicit apology, plain numbers.

## Files

- `data/corpus_v3.csv` / `.json` – the corpus (json has quotes, sources, news coverage)
- `data/repeat_layoffs.csv`, `data/repeat_stats.json` – repeat-layoff analysis
- `data/stats_v3.json` – numbers quoted here
- `data/sources/` – saved company text and reproductions used to verify quotes (research archive; quote only short excerpts)
- `data/edgar/` – SEC candidates, extracted events, SIC codes (filing text is large and can be regenerated)
- `data/corpus.json`, `data/corpus_enriched.json`, `data/raw/`, `data/raw2/`, `data/enriched/` – earlier stages
- `scripts/` – `edgar_discover.py`, `edgar_discover_6k.py`, `edgar_fetch.py`, `edgar_classify.py`, `edgar_sic.py`, `build_corpus.py`, `merge_enriched.py`, `build_v3.py`, `stats_v3.py`, `repeat_layoffs.py`
- `SCHEMA.md` – field definitions, incl. v3 addendum

## What I would do next

Add a tier A upgrade pass for the S events with well-known companies (look for the CEO letter on their site); fill 2021 and the rest of 2026; run a second coder on a sample of tier A to measure agreement; add news coverage for the S events.
