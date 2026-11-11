"""All numbers quoted in the README for corpus_v3 -> data/stats_v3.json (+ corpus_v3.csv)"""
import json, csv, collections, statistics as st
c=json.load(open('data/corpus_v3.json'))
A=[r for r in c if r['tier']=='A']
def rate(rs,f):
    v=[r.get(f) for r in rs if r.get(f) is not None]; return [sum(bool(x) for x in v),len(v)]
S={'events':len(c),'companies_note':'see build_v3.py output (first-word key, date-bounded dedupe); stats count distinct lower-cased names so may overstate',
   'by_year_tier':{y:dict(collections.Counter(r['tier'] for r in c if r['event_date'][:4]==y)) for y in sorted({r['event_date'][:4] for r in c})},
   'by_year_total':dict(sorted(collections.Counter(r['event_date'][:4] for r in c).items())),
   'by_source_pipeline':dict(collections.Counter(r['source_pipeline'] for r in c)),
   'by_sector':dict(collections.Counter(r['sector'] for r in c)),
   'text_source':dict(collections.Counter(r.get('text_source') for r in c)),
   'with_news_coverage':sum(bool(r.get('news_coverage')) for r in c),
   'news_outlets_top':collections.Counter(n['outlet'].split(' via ')[0] for r in c for n in r.get('news_coverage',[])).most_common(15),
   'tierA':len(A),'tierA_apology':rate(A,'apology'),'tierA_responsibility':rate(A,'takes_responsibility'),
   'tierA_by_year':{y:{'n':sum(r['event_date'][:4]==y for r in A),'apology':rate([r for r in A if r['event_date'][:4]==y],'apology'),'responsibility':rate([r for r in A if r['event_date'][:4]==y],'takes_responsibility'),'ai_mention':sum(bool(r.get('mentions_ai')) for r in A if r['event_date'][:4]==y)} for y in sorted({r['event_date'][:4] for r in A})},
   'ai_mention_by_year_all':{y:[sum(bool(r.get('mentions_ai')) for r in c if r['event_date'][:4]==y),sum(r['event_date'][:4]==y for r in c)] for y in sorted({r['event_date'][:4] for r in c})},
   'ai_mention_by_year_nonbio':{y:[sum(bool(r.get('mentions_ai')) for r in c if r['event_date'][:4]==y and r['sector']!='biotech_health'),sum(r['event_date'][:4]==y and r['sector']!='biotech_health' for r in c)] for y in sorted({r['event_date'][:4] for r in c})},
   'communicator':dict(collections.Counter(r['communicator'] for r in c)),
   'median_pct_by_sector':{s:st.median([r['pct_workforce'] for r in c if r['sector']==s and r['pct_workforce']]) for s in sorted({r['sector'] for r in c}) if any(r['sector']==s and r['pct_workforce'] for r in c)},
   'median_pct_all':st.median([r['pct_workforce'] for r in c if r['pct_workforce']]),
   'reasons_nonbio':collections.Counter(x for r in c if r['sector']!='biotech_health' for x in r['stated_reasons']).most_common(),
   'overhiring_by_year_nonbio':{y:[sum('overhiring' in r['stated_reasons'] for r in c if r['event_date'][:4]==y and r['sector']!='biotech_health'),sum(r['event_date'][:4]==y and r['sector']!='biotech_health' for r in c)] for y in sorted({r['event_date'][:4] for r in c})}}
json.dump(S,open('data/stats_v3.json','w'),indent=1,default=list)
cols=['company','sector','event_date','headcount_cut','pct_workforce','communicator','channel','tier','text_source','opening_line','evidence_sentence','stated_reasons','takes_responsibility','apology','mentions_ai','ai_framing','severance','confidence','notes']
with open('data/corpus_v3.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(cols+['primary_url','news_urls'])
    for r in c:
        u=next((s['url'] for s in r.get('sources',[]) if s.get('type')=='primary'),(r.get('sources') or [{}])[0].get('url','') if r.get('sources') else '')
        w.writerow([('; '.join(r.get(k)) if isinstance(r.get(k),list) else r.get(k)) for k in cols]+[u,' | '.join(n['url'] for n in r.get('news_coverage',[]))])
print(json.dumps({k:S[k] for k in ('events','by_year_total','by_year_tier','tierA','tierA_apology','tierA_responsibility','ai_mention_by_year_nonbio','overhiring_by_year_nonbio','with_news_coverage')},indent=1,default=list))
