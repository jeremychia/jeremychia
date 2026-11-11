"""corpus_enriched.json + raw2/year_*.json + edgar/events.json -> data/corpus_v3.json / corpus_v3.csv
tiers:  A = wording verified in company text or news reproduction (wording stats use only A)
        S = SEC filing, company-authored factual disclosure (auto-extracted; used for who/when/how-many/channel/reasons, NOT apology/responsibility)
        B = news-only"""
import json, glob, re, os, csv, collections
from datetime import date
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ')).strip().lower()
def readp(p):
    if not p: return None
    p=p if os.path.isabs(p) else os.path.join(os.getcwd(),p)
    return norm(open(p,errors='ignore').read()) if os.path.exists(p) else None
SUF=r'\b(inc|incorporated|corp|corporation|co|company|ltd|limited|plc|llc|holdings?|group|technologies|technology|the|sa|ag|nv|se|lp|therapeutics|pharmaceuticals|biosciences|bio)\b'
def key(name):
    n=re.sub(r'\(.*?\)','',name.lower()); n=re.sub(r'[^a-z0-9 ]',' ',n); n=re.sub(SUF,' ',n); n=n.split()
    n=[w for w in n if w]; return n[0] if n else name.lower()
ALIAS={'alphabet':'google','twitter':'twitter','x':'twitter','meta':'meta','facebook':'meta','square':'block','block':'block','activision':'microsoft','xbox':'microsoft','linkedin':'microsoft','github':'microsoft','twitch':'amazon','amazon':'amazon','cruise':'gm','general':'gm'}
def k(name): kk=key(name); return ALIAS.get(kk,kk)
def d(s): y,m,dd=(int(x) for x in s[:10].split('-')); return date(y,m,dd)
def sector(sic):
    try: s=int(sic)
    except: return 'other'
    if s in(2833,2834,2835,2836,3841,3842,3843,3844,3845,3826,8731,8071,8082,8090,8093) or 8000<=s<=8099 or s in(5122,3851): return 'biotech_health'
    if 7370<=s<=7379 or s in(7389,3577,3571,3572,3575): return 'saas'
    if s in(3674,3672,3661,3663,3669,3670,3679,3576,3578,3669) or 3550<=s<=3569 or 3711<=s<=3799 or 3600<=s<=3699: return 'hardware_auto'
    if 6000<=s<=6799: return 'finance_realestate'
    if s in(4833,4841,7812,7819,7822,7829,7830,7841,7900,7990,7997,2711,2721,2731,2741,4832,7372): return 'media_gaming'
    if s==5961 or s in(5731,5734,5735,5945,5990): return 'consumer_internet'
    return 'traditional'
base=json.load(open('data/corpus_enriched.json'))
for r in base: r.setdefault('source_pipeline','research_agent')
# ---- raw2 (year gap fill)
added=collections.Counter(); out=list(base)
def dup(r,pool,days=45):
    kk=k(r['company'])
    return next((p for p in pool if k(p['company'])==kk and abs((d(p['event_date'])-d(r['event_date'])).days)<=days),None)
for f in sorted(glob.glob('data/raw2/year_*.json')):
    for r in json.load(open(f)):
        if not r.get('event_date') or len(r['event_date'])<10: added['bad_date']+=1; continue
        if dup(r,out): added['dup_raw2']+=1; continue
        text=readp(r.get('company_text_path')) or readp(r.get('reproduction_path'))
        ctext=readp(r.get('company_text_path'))
        kq=[q for q in (r.get('key_quotes') or []) if text and norm(q) in text]
        r['key_quotes']=kq
        if r.get('opening_line') and not (text and norm(r['opening_line']).rstrip('… .') in text): r['opening_line']=None
        r['text_source']='company' if ctext else ('reproduction' if text else 'news_only')
        r['public_primary_text']=bool(ctext); r['tier']='A' if (text and kq) else 'B'; r['source_pipeline']='year_gapfill'
        for fld,default in (('stated_reasons',[]),('euphemisms',[]),('channel',[]),('sources',[]),('mentions_ai',False)): r.setdefault(fld,default)
        out.append(r); added['raw2_'+r['tier']]+=1
# ---- EDGAR
sic=json.load(open('data/edgar/sic.json')); ev=json.load(open('data/edgar/events.json'))
ev.sort(key=lambda e:e['filing_date'])   # chronological: earliest filing = the announcement
PAST=re.compile(r'(?i)\b(previously|as previously|had announced|included|initiated on|was implemented|were implemented|completed|in connection with the (?:\d{4}|prior|previous))\b|\bthe (?:\d{4}|prior|previous) (?:restructuring|reduction)')
RETAIN=re.compile(r'(?i)retain|remain\w*|will have approximately|workforce of approximately|result in (?:a )?(?:total )?(?:workforce|headcount) of')
edgar_rows=[]
for e in ev:
    name=re.sub(r'\s*\(.*$','',e['company']).strip()
    s=sic.get(e['cik'],{})
    hc=e['headcount']; flag=None
    if hc and RETAIN.search(e['evidence_sentence']): hc=None; flag='headcount_parse_uncertain'
    if hc and hc<10 and not e['pct']: hc=None; flag='headcount_parse_uncertain'
    r=dict(company=name,sector=sector(s.get('sic')),sic=s.get('sic'),sic_desc=s.get('sic_desc'),tickers=s.get('tickers'),event_date=e['filing_date'],
        headcount_cut=hc,pct_workforce=e['pct'],communicator='ceo' if e['ceo_letter'] else 'sec_filing',communicator_name=None,
        channel=['8k_filing']+(['internal_email'] if e['ceo_letter'] else []),public_primary_text=True,opening_line=e['letter_opening'],
        key_quotes=[],evidence_sentence=e['evidence_sentence'],stated_reasons=e['stated_reasons'],takes_responsibility=e['responsibility'],apology=e['apology'],
        mentions_ai=e['mentions_ai'],ai_framing=None,euphemisms=[],severance=e['severance'],notice_style='unknown',confidence='medium',
        sources=[{'url':e['filing_url'],'title':'SEC 8-K '+e['filing_date'],'type':'primary'}],notes=flag or '',text_source='sec_filing',tier='A' if e['ceo_letter'] else 'S',
        source_pipeline='edgar',edgar_items=e['items'],cik=e['cik'],adsh=e['adsh'])
    formal=bool(e['formal_2_05'])
    prior=[x for x in edgar_rows if x['cik']==r['cik']]
    if not formal and PAST.search(e['evidence_sentence']): added['stale_restatement']+=1; continue
    if any((x['pct_workforce'] is not None and x['pct_workforce']==r['pct_workforce']) or (x['headcount_cut'] and x['headcount_cut']==r['headcount_cut']) for x in prior if 0<=(d(r['event_date'])-d(x['event_date'])).days<=548) and not formal: added['restated_values']+=1; continue
    if any(x['pct_workforce']==r['pct_workforce'] and x['headcount_cut']==r['headcount_cut'] for x in prior if 0<=(d(r['event_date'])-d(x['event_date'])).days<=120): added['amendment_dup']+=1; continue
    if dup(r,out,60) or any(x['cik']==r['cik'] and abs((d(x['event_date'])-d(r['event_date'])).days)<=45 for x in edgar_rows): added['dup_edgar']+=1; continue
    edgar_rows.append(r); added['edgar_'+r['tier']]+=1
out+=edgar_rows
out=[r for r in out if r['event_date']>='2021-01-01' or r.get('keep_pre2021')]
out.sort(key=lambda r:r['event_date'])
json.dump(out,open('data/corpus_v3.json','w'),indent=1,ensure_ascii=False)
print(dict(added)); print('events',len(out),'companies',len({k(r['company']) for r in out}))
by=collections.defaultdict(collections.Counter)
for r in out: by[r['event_date'][:4]][r['tier']]+=1
for y in sorted(by): print(y,sum(by[y].values()),dict(by[y]))
print('sector',collections.Counter(r['sector'] for r in out).most_common())
