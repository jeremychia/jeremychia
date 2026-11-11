"""Turn downloaded 8-K texts into candidate layoff events with company-authored evidence.
Reads data/edgar/candidates_*.json + data/edgar/text/*.txt ; writes data/edgar/events.json.
Everything extracted is verbatim from the filing (sentences), nothing is paraphrased."""
import json, glob, os, re, collections

SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z“"(])')
WF = r'(?:workforce|work force|headcount|employees|employee base|staff|team members|positions|roles|jobs|FTEs?|full-time)'
VERB = r'(?:reduc\w+|eliminat\w+|terminat\w+|lay(?:ing|s|ed)?\s+off|layoffs?|restructur\w+|cut(?:ting|s)?|let\s+go|separat\w+|downsiz\w+)'
PCT = re.compile(r'(\d{1,2}(?:\.\d+)?)\s?(?:%|percent)\s+of\s+(?:the\s+|its\s+|our\s+|their\s+)?(?:Company[’\']s\s+|company[’\']s\s+)?(?:global\s+|current\s+|total\s+|full-time\s+|existing\s+)*' + WF, re.I)
CNT = re.compile(r'(?:approximately|about|up to|roughly|around|nearly|over|more than)?\s*(?<![\d,$])(\d{1,3}(?:,\d{3})+|(?!(?:19|20)\d\d\b)\d{2,5})\s+(?:\w+\s+){0,2}?(?:employees|positions|roles|jobs|full-time|FTEs|people|team members|workers)', re.I)
ANNOUNCE = re.compile(VERB + r'.{0,160}' + WF + r'|' + WF + r'.{0,160}' + VERB, re.I)
LETTER = re.compile(r'\b(Dear\s+(?:team|all|everyone|colleagues|employees|Stripe|[A-Z]\w+ team)|(?:Hi|Hello)\s+(?:team|all|everyone)|Team,|Everyone,|Colleagues,|Subject:|To all)', re.I)
FIRST = re.compile(r"\b(I\s+(?:wanted|want|am writing|’m writing|'m writing|have|had|know|take|made)|my\s+(?:decision|responsibility)|we\s+(?:made|have made)\s+the\s+(?:difficult|hard))", re.I)
SORRY = re.compile(r'\b(i(?:\s+am|’m|\'m)\s+(?:truly\s+|deeply\s+|so\s+|very\s+)?sorry|apologi[sz]e|sincerely sorry|we(?:’re|\'re| are) sorry)', re.I)
RESP = re.compile(r'\b((?:i|we)\s+(?:take|accept|own|am responsible|are responsible)\b[^.]{0,60}(?:responsib|accountab|this)|(?:full|sole)\s+responsibility|accountable for)', re.I)
AI = re.compile(r'\b(AI|artificial intelligence|generative AI|agentic|automation|machine learning|LLMs?)\b')
REASONS = {
 'overhiring': r'over-?hir|hired too|grew too (?:quickly|fast)|grew headcount|expanded (?:too )?(?:quickly|rapidly)',
 'macro': r'macro|economic (?:uncertaint|conditions|environment|downturn|headwind)|inflation|recession|market conditions|challenging environment',
 'interest_rates': r'interest rate',
 'revenue_decline': r'declin\w+ (?:in )?(?:revenue|sales|demand)|lower (?:revenue|demand)|decrease in (?:revenue|demand)|slower growth|growth (?:has )?slowed',
 'efficiency': r'efficien|streamlin|productiv|simplif',
 'ai_automation': r'\bAI\b|artificial intelligence|automation|agentic',
 'restructuring': r'restructur|reorganiz|realign',
 'strategic_pivot': r'strategic (?:priorit|shift|focus|pivot)|prioriti[sz]e|refocus|focus (?:our|on) (?:resources|investment)',
 'cost_cutting': r'cost (?:reduction|saving|cutting)|reduce (?:operating )?(?:costs|expenses)|operating expenses|cost structure',
 'profitability': r'profitab|path to profit|cash (?:flow|runway)|runway',
 'flatten_management': r'layers|flatten|management structure|span of control',
 'covid': r'covid|pandemic',
 'merger_integration': r'integrat\w+ (?:of|with)|synerg|acquisition of',
 'regulatory': r'regulat|tariff',
 'clinical_failure': r'clinical (?:trial|data)|discontinu\w+ (?:the )?(?:development|program|trial)|trial (?:did not|failed)',
}

def words(s, n): w = s.split(); return ' '.join(w[:n]) + (' …' if len(w) > n else '')

def analyse(texts, items):
    """texts: list[(filename, text)]. Returns dict or None if no announcement."""
    best = None
    for fn, t in texts:
        # prefer the 2.05 section of the main 8-K body when present
        m = re.search(r'Item\s*2\.05.{0,3000}', t, re.I | re.S)
        scopes = [(fn, m.group(0), '2.05')] if m else []
        scopes.append((fn, t[:60000], 'doc'))
        for fnn, scope, kind in scopes:
            for s in SENT.split(scope):
                if len(s) > 900 or not ANNOUNCE.search(s): continue
                if re.search(r'(?i)older workers|severance agreement|separation agreement|employment agreement|retention', s): continue
                p, c = PCT.search(s), CNT.search(s)
                if not (p or c): continue
                if re.search(r'(?i)\b(was|were|had been|previously|completed|since)\b.{0,40}(?:restructur|reduc)', s) and not re.search(r'(?i)will|expects?|plans?|committed|approved|announc|today|decid', s): continue
                score = (kind == '2.05') * 3 + bool(p) * 2 + bool(c) + bool(re.search(r'(?i)will|expects?|plans?|committed|approved|announc|today|decid', s))
                if not best or score > best['score']:
                    best = dict(score=score, sentence=s.strip(), file=fn, kind=kind,
                                pct=float(p.group(1)) if p else None,
                                headcount=int(c.group(1).replace(',', '')) if c else None)
    if not best: return None
    allt = ' '.join(t for _, t in texts)
    # letters: look in exhibits for greeting + first person
    letter = None
    for fn, t in texts:
        mm = LETTER.search(t[:3000]) if t else None
        if mm and re.search(r'ex-?99|exhibit', fn, re.I) and FIRST.search(t[:6000]) and ANNOUNCE.search(t[:8000]) and not re.search(r'(?i)appointed|elected to the board', t[:3000]) and len(t) < 40000:
            body = t[mm.end():mm.end() + 600].strip(' ,:-')
            letter = dict(file=fn, opening=words(body, 30))
            break
    window = (letter and ' '.join(t for fn, t in texts if fn == letter['file'])) or best['sentence']
    ctx = ' '.join(t[:12000] for _, t in texts)
    rs = [k for k, rx in REASONS.items() if re.search(rx, window if letter else best['sentence'] + ' ' + ctx[:6000], re.I)]
    sev = re.search(r'(?i)[^.]{0,120}severance[^.]{0,220}\.', allt)
    return dict(evidence_sentence=words(best['sentence'], 70), pct=best['pct'], headcount=best['headcount'],
                evidence_file=best['file'], evidence_kind=best['kind'],
                ceo_letter=bool(letter), letter_opening=letter and letter['opening'],
                apology=bool(SORRY.search(window)) if letter else None,
                responsibility=bool(RESP.search(window)) if letter else None,
                mentions_ai=bool(AI.search(window if letter else best['sentence'])),
                stated_reasons=rs, severance=sev and words(sev.group(0).strip(), 45))

def main():
    tdir = 'data/edgar/text'
    files = collections.defaultdict(list)
    for p in os.listdir(tdir):
        if p.endswith('.fail'): continue
        adsh, fn = p.split('__', 1); files[adsh].append((fn[:-4], os.path.join(tdir, p)))
    events = []
    for cp in sorted(glob.glob('data/edgar/candidates_*.json')):
        for r in json.load(open(cp)):
            fs = files.get(r['adsh'])
            if not fs: continue
            texts = [(fn, open(path).read()) for fn, path in sorted(fs)]
            a = analyse(texts, r['items'])
            if not a: continue
            formal = bool(r['items'] and '2.05' in r['items'])
            if not formal and a['pct'] is None: continue   # non-2.05 filings need an explicit % to count
            a['formal_2_05'] = formal
            name = re.sub(r'\s*\(CIK.*$', '', r['company']).strip()
            events.append(dict(company=name, cik=r['ciks'][0], adsh=r['adsh'], filing_date=r['file_date'], items=r['items'],
                               filing_url=f"https://www.sec.gov/Archives/edgar/data/{int(r['ciks'][0])}/{r['adsh'].replace('-','')}/{a['evidence_file']}", **a))
    json.dump(events, open('data/edgar/events.json', 'w'), indent=1, ensure_ascii=False)
    by = collections.Counter(e['filing_date'][:4] for e in events)
    print('events', len(events), dict(sorted(by.items())), 'ceo_letters', sum(e['ceo_letter'] for e in events))

if __name__ == '__main__': main()
