# Year gap-fill brief (read fully)

Project: corpus on HOW companies communicate layoffs. Schema: /Users/jeremychia/Documents/Github/jeremychia/analysis/layoff-communications/SCHEMA.md . Already-covered events: data/raw2/existing_events.txt (skip those company-months).
Goal for YOUR YEAR: find **up to 40 additional layoff events announced in that calendar year** that are NOT already covered, favouring (a) well-known companies, (b) events where the company published its own words (CEO memo/blog/post/press release/LinkedIn), (c) a mix of sectors and countries. Skip companies that are only small biotechs (a separate SEC pipeline covers those). Quality over quantity: 25 good records beat 40 weak ones.

## Budget warning
Earlier agents ran out of WebSearch budget. Be frugal: find events via LIST pages first (WebFetch/curl: TechCrunch's yearly "comprehensive list of tech layoffs" article for the year, Wikipedia "Layoffs" / "List of ... layoffs" pages, Crunchbase News tracker, company-specific Wikipedia pages), then spend searches only on verifying specific events and finding news coverage.

## Fetching rules
- `curl -sL -m 40 -A "layoff-communications-research/0.1" URL` or WebFetch / web-fetch agent. For a blocked company page try Wayback raw copy `https://web.archive.org/web/<YYYY>id_/<URL>` (go gently: ~1 request/second; archive.org returns 429 if hammered).
- DO NOT spoof a browser User-Agent, use proxy/reader services, or otherwise evade bot protection. If blocked, note `blocked` and move on. Do not fetch sec.gov.
- Never invent text, quotes, numbers or URLs. Quotes must be copied exactly from text you read.

## Per event
Fill the SCHEMA.md fields. Save the company's own text (or news reproduction) you actually read to
`/Users/jeremychia/Documents/Github/jeremychia/analysis/layoff-communications/data/sources/<slug>__<YYYY-MM>/company.txt` (or `reproduction.txt`), first line `URL: <url>`, second `RETRIEVED_VIA: direct|wayback`. Set `company_text_path` / `reproduction_path` to that file. Quotes (<=25 words each, max 3) and opening_line (<=30 words) must be exact substrings of that file; otherwise leave them empty. Add `news_coverage`: 2-3 items `{outlet,url,headline,date,framing}` from major outlets (TechCrunch, CNN, CNBC, Bloomberg, Fortune, Axios, Forbes, GeekWire, Wired, The Information ...) using only URLs you saw. Add `framing_gap` (one sentence, or "none").
Set `year_batch` to your year. event_date must be the real announcement date (YYYY-MM-DD).

## Output
Valid JSON array at `/Users/jeremychia/Documents/Github/jeremychia/analysis/layoff-communications/data/raw2/year_<YEAR>.json`. Write it incrementally (save after every ~8 events) so a budget cut-off does not lose work. Final reply (<=100 words): records written, how many with company text, how many with news coverage, blocked sites.
