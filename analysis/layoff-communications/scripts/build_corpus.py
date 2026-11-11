"""Merge data/raw/batch_*.json -> data/corpus.json, corpus.csv, excluded.json, stats.json"""
import json, glob, csv, collections, statistics as st
R={'high':3,'medium':2,'low':1}
EXCLUDE={ # (company, month): reason
 ('nestle','2025-10'):'recorded from memory, never verified',
 ('warner bros. discovery','2023-11'):'retrospective interview, not a layoff announcement',
 ('klarna','2024-12'):'attrition/AI claim, not a layoff memo',
 ('klarna','2024-08'):'attrition/hiring freeze, not a layoff memo',
 ('duolingo','2025-04'):'contractor phase-out, not an employee layoff',
 ('qualcomm','2023-10'):'WARN filing only; no CEO communication',
 ('igniteTech'.lower(),'2025-08'):'no contemporaneous memo; dated from later interview',
 ('stripe','2025-01'):'search title only; fields are guesses',
}
recs=[]
for f in sorted(glob.glob('data/raw/batch_*.json')):
    for r in json.load(open(f)): r['batch']=f.split('_')[-1][0]; recs.append(r)
def score(r): return (R[r['confidence']], bool(r['key_quotes']), bool(r['public_primary_text']), sum(v is not None for v in r.values()))
best={}; excluded=[]
for r in recs:
    k=(r['company'].strip().lower(), r['event_date'][:7])
    if k in EXCLUDE: r['excluded_reason']=EXCLUDE[k]; excluded.append(r); continue
    if k not in best or score(r)>score(best[k]): best[k]=r
corpus=list(best.values())
# Normalise pct_workforce: some batches stored fractions (0.3 = 30%). Amazon/IBM values <2 are true percents of total workforce.
KEEP_SMALL={'amazon','ibm'}
for r in corpus:
    v=r['pct_workforce']
    if v is not None and v<1 and r['company'].lower() not in KEEP_SMALL: r['pct_workforce']=round(v*100,2)
for r in corpus:
    r['tier']='A' if (r['public_primary_text'] and r['key_quotes'] and r['confidence'] in('high','medium')) else 'B'
corpus.sort(key=lambda r:r['event_date'])
json.dump(corpus,open('data/corpus.json','w'),indent=1,ensure_ascii=False)
json.dump(excluded,open('data/excluded.json','w'),indent=1,ensure_ascii=False)
cols=['company','sector','event_date','headcount_cut','pct_workforce','communicator','communicator_name','channel','tier','confidence','opening_line','stated_reasons','takes_responsibility','apology','mentions_ai','ai_framing','euphemisms','severance','notice_style','ceo_voice']
with open('data/corpus.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(cols+['primary_url'])
    for r in corpus:
        u=next((s['url'] for s in r['sources'] if s.get('type')=='primary'),(r['sources'] or [{}])[0].get('url',''))
        w.writerow([ '; '.join(r[c]) if isinstance(r[c],list) else r[c] for c in cols]+[u])
A=[r for r in corpus if r['tier']=='A']
def rate(rs,f):
    v=[r[f] for r in rs if r[f] is not None]; return (sum(v),len(v)) if v else (0,0)
S={'n_events':len(corpus),'n_companies':len({r['company'].lower() for r in corpus}),'n_excluded':len(excluded),'tierA':len(A),'tierB':len(corpus)-len(A)}
S['communicator']=collections.Counter(r['communicator'] for r in corpus)
S['communicator_ceo_or_founder_share']=round(sum(r['communicator'] in('ceo','founder') for r in corpus)/len(corpus),3)
S['by_year']=dict(sorted(collections.Counter(r['event_date'][:4] for r in corpus).items()))
S['apology_tierA']=rate(A,'apology'); S['responsibility_tierA']=rate(A,'takes_responsibility')
S['ai_mention_by_year']={y:(sum(r['mentions_ai'] for r in corpus if r['event_date'][:4]==y),sum(1 for r in corpus if r['event_date'][:4]==y)) for y in sorted({r['event_date'][:4] for r in corpus})}
S['ai_framing_2025plus']=collections.Counter(r['ai_framing'] for r in corpus if r['event_date']>='2025')
S['reasons']=collections.Counter(x for r in corpus for x in r['stated_reasons']).most_common()
S['reasons_tierA']=collections.Counter(x for r in A for x in r['stated_reasons']).most_common()
S['median_pct']=st.median([r['pct_workforce'] for r in corpus if r['pct_workforce']])
S['channel']=collections.Counter(x for r in corpus for x in r['channel']).most_common()
S['notice']=collections.Counter(r['notice_style'] for r in corpus)
S['euphemisms']=collections.Counter(x.lower() for r in A for x in (r['euphemisms'] or [])).most_common(15)
for sec in sorted({r['sector'] for r in corpus}):
    rs=[r for r in A if r['sector']==sec]; S.setdefault('apology_by_sector',{})[sec]=(rate(rs,'apology'),len(rs))
def era(r):
    y=r['event_date'][:4]; return '2020-21' if y<'2022' else y
S['communicator_by_year']={y:dict(collections.Counter(r['communicator'] for r in corpus if era(r)==y)) for y in sorted({era(r) for r in corpus})}
S['overhiring_by_year']={y:(sum('overhiring' in r['stated_reasons'] for r in corpus if era(r)==y),sum(1 for r in corpus if era(r)==y)) for y in sorted({era(r) for r in corpus})}
S['ai_cause_reason_by_year']={y:sum('ai_automation' in r['stated_reasons'] for r in corpus if era(r)==y) for y in sorted({era(r) for r in corpus})}
S['responsibility_by_year_tierA']={y:rate([r for r in A if era(r)==y],'takes_responsibility') for y in sorted({era(r) for r in A})}
S['apology_by_year_tierA']={y:rate([r for r in A if era(r)==y],'apology') for y in sorted({era(r) for r in A})}
S['median_pct_by_sector']={s:st.median([r['pct_workforce'] for r in corpus if r['sector']==s and r['pct_workforce']]) for s in sorted({r['sector'] for r in corpus}) if any(r['sector']==s and r['pct_workforce'] for r in corpus)}
S['pct_known']=sum(1 for r in corpus if r['pct_workforce'])
S['notice_by_comm_ceo']=dict(collections.Counter(r['notice_style'] for r in corpus if r['communicator'] in('ceo','founder')))
json.dump(S,open('data/stats.json','w'),indent=1,default=list)
print(json.dumps(S,indent=1,default=list))
