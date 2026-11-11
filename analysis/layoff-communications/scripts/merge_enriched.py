"""corpus.json + data/enriched/enriched_*.json -> data/corpus_enriched.json
Quotes/opening lines are kept ONLY if they occur verbatim in the saved company/reproduction text."""
import json, glob, re, os, collections
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ')).strip().lower()
base=json.load(open('data/corpus.json'))
idx={(r['company'],r['event_date']):r for r in base}
enr=[r for f in sorted(glob.glob('data/enriched/enriched_*.json')) for r in json.load(open(f))]
log=collections.Counter(); out=[]; moved=[]
def readp(p):
    if not p: return None
    p=p if os.path.isabs(p) else os.path.join(os.getcwd(),p)
    return norm(open(p,errors='ignore').read()) if os.path.exists(p) else None
for e in enr:
    r=idx.get((e['company'],e['event_date']))
    if not r: log['unmatched']+=1; continue
    ctext=readp(e.get('company_text_path')); rtext=readp(e.get('reproduction_path'))
    text=ctext or rtext
    for k,v in e.items():
        if k in('company','event_date','fetch_log','event_date_corrected','event_date_note','headcount_cut_note','company_text_path','reproduction_path','key_quotes','opening_line','confidence','public_primary_text') or v in(None,[],''): continue
        r[k]=v
    r['company_text_path']=e.get('company_text_path'); r['reproduction_path']=e.get('reproduction_path'); r['fetch_log']=e.get('fetch_log')
    if e.get('event_date_corrected'): r['event_date_original']=r['event_date']; r['event_date']=e['event_date_corrected']; log['date_corrected']+=1
    if text:
        kq=[q for q in (e.get('key_quotes') or []) if norm(q) in text]; log['quotes_dropped']+=len(e.get('key_quotes') or [])-len(kq)
        if kq: r['key_quotes']=kq
        ol=e.get('opening_line')
        if ol and norm(ol).rstrip('… .') in text: r['opening_line']=ol
        elif ol: log['opening_dropped']+=1; r['opening_line']=None
        r['text_source']='company' if ctext else 'reproduction'
    else:
        r['text_source']='news_only'
        if e.get('key_quotes'): r['key_quotes_unverified']=e['key_quotes']; r['key_quotes']=[]
        if e.get('opening_line'): r['opening_line']=None
    r['public_primary_text']=bool(ctext)
    r['tier']='A' if (r['text_source'] in('company','reproduction') and r['key_quotes']) else 'B'
    log['tier_'+r['tier']]+=1; log['src_'+r['text_source']]+=1
final=[]
for r in base:
    if r['company']=='Rappi' and r['event_date'].startswith('2020'): moved.append(r); continue
    if r['event_date']<'2021-01-01' and r['company']!='Airbnb': pass
    final.append(r)
final.sort(key=lambda r:r['event_date'])
json.dump(final,open('data/corpus_enriched.json','w'),indent=1,ensure_ascii=False)
print(dict(log),'| events',len(final),'| news_coverage>=2:',sum(len(r.get('news_coverage',[]))>=2 for r in final),'| any news:',sum(bool(r.get('news_coverage')) for r in final))
print('outlets',collections.Counter(n['outlet'].split(' via ')[0] for r in final for n in r.get('news_coverage',[])).most_common(25))
