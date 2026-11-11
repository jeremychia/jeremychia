# Enrichment brief (read fully)

Goal: for each event in your input file, (1) find the **company's own words** and save them, (2) collect **news coverage** from major outlets, (3) correct/complete the coded fields.

## Fetching rules (important)
- Use `curl -sL -m 40 -A "layoff-communications-research/0.1" URL` (honest, non-browser identity) for company pages, or the WebFetch/web-fetch tool.
- If a company page is blocked/403/404: try the Wayback Machine raw copy `https://web.archive.org/web/<YYYY>id_/<original URL>` and the availability API `https://archive.org/wayback/available?url=<URL>&timestamp=<YYYYMMDD>`.
- DO NOT spoof a browser User-Agent, rotate IPs, use reader/proxy services, or otherwise evade bot protection. If a page is still unreachable, record `blocked` in notes and move on.
- Do NOT fetch sec.gov (handled by a separate script).
- Never invent text. Quotes must be copied exactly from text you read. Save only what you actually read.

## Company's own text (priority 1)
Look in: company newsroom/blog (e.g. about.x.com/news, blog.x.com), CEO's LinkedIn/X post pages, investor-relations press releases, all-hands transcripts the company published. Save the verbatim text you retrieved to
`/Users/jeremychia/Documents/Github/jeremychia/analysis/layoff-communications/data/sources/<slug>__<YYYY-MM>/company.txt`
(slug = lowercase company name, hyphens), with the first line `URL: <url>` and second line `RETRIEVED_VIA: direct|wayback`. Then set `company_text_path` and `company_text_url`, and set `public_primary_text=true`. If you only found a reproduction on a news site, save it as `reproduction.txt` and set `reproduction_url`.
From the saved text, fill `opening_line` (<=30 words), `key_quotes` (<=3, each <=25 words), `takes_responsibility`, `apology`, `euphemisms`, `severance`, `ai_framing`, `stated_reasons` (vocabulary in SCHEMA.md). Be strict: apology=true only if an explicit sorry/apologise; responsibility=true only if explicit ownership.

## News coverage (priority 2)
Use WebSearch (pass `allowed_domains`, e.g. techcrunch.com, cnn.com, cnbc.com, reuters.com, bloomberg.com, theverge.com, nytimes.com, wsj.com, bbc.com, theguardian.com, axios.com, businessinsider.com, forbes.com, fortune.com, wired.com, geekwire.com, theinformation.com, ft.com, apnews.com, washingtonpost.com, 9to5mac / regional equivalents) to find **2-4 articles per event** from the major outlets. Only record URLs that appeared in search results or that you fetched. For each: `{outlet, url, headline, date, framing}` where `framing` is <=20 words saying how the outlet framed it (e.g. "adds AI angle company avoided", "calls out missing apology", "quotes anonymous employees").
Also record `framing_gap`: one sentence on how news framing differs from the company's own framing (or "none").

## Output
Write a JSON array to `/Users/jeremychia/Documents/Github/jeremychia/analysis/layoff-communications/data/enriched/enriched_<N>.json`, one object per input event, keyed by `company` + `event_date` exactly as in the input, containing ONLY fields you add or change plus: `news_coverage` (list), `framing_gap`, `company_text_path`, `company_text_url`, `reproduction_url`, `fetch_log` (one line: what worked/blocked). Validate it parses.
Final reply: events processed, how many got company text / news coverage, blocked sites. <=120 words.
