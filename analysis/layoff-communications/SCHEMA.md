# Record schema (one JSON object per layoff *event*; a company can have several)

Batch files: data/raw/batch_<letter>.json = JSON array of records.

| field | type | notes |
|---|---|---|
| company | str | |
| sector | str | big_tech / saas / fintech_crypto / consumer_internet / media_gaming / traditional / hardware_auto / consulting_finance / international_startup |
| event_date | str | YYYY-MM-DD (announcement date) |
| headcount_cut | int/null | people |
| pct_workforce | float/null | |
| communicator | str | ceo / founder / cpo_hr / exec_other / spokesperson / earnings_call / sec_filing / media_leak / podcast_interview |
| communicator_name | str | |
| channel | list[str] | internal_email, public_blog, linkedin, x_post, all_hands, zoom, earnings_call, 8k_filing, press_release, podcast, personal_email_to_laid_off |
| public_primary_text | bool | is the CEO/company wording itself publicly available? |
| opening_line | str/null | verbatim, <=30 words, only if verified from a primary or quoted source |
| key_quotes | list[str] | verbatim, each <=25 words, max 3, only if verified |
| stated_reasons | list[str] | from: overhiring, macro, interest_rates, revenue_decline, efficiency, ai_automation, restructuring, strategic_pivot, cost_cutting, flatten_management, performance, covid, merger_integration, regulatory, profitability, other |
| takes_responsibility | bool/null | explicit "I/we am/are responsible/accountable" |
| apology | bool/null | explicit "sorry"/"apologize" |
| mentions_ai | bool | |
| ai_framing | str/null | none / cause / reallocation / "not about AI" / future_context |
| euphemisms | list[str] | e.g. "reduce workforce", "let go", "restructure", "rightsizing", "role elimination" |
| severance | str/null | terms as announced |
| notice_style | str | advance_notice / same_day / pre_leak / locked_out_first / unknown |
| ceo_voice | str | 1-sentence characterisation of tone (human, corporate, defiant, contrite, clinical...) |
| sources | list[{url,title,type}] | type = primary / news / analysis |
| confidence | str | high / medium / low |
| notes | str | caveats, anything unverified |

Rules: NEVER invent a quote. If you only have a paraphrase, leave quote fields empty and say so in notes.
Quotes must be short (<=25 words) - this is a research corpus, not a republication of memos.
