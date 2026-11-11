"""Which companies lay off again and again? Reads data/corpus_v3.json -> data/repeat_layoffs.csv, data/repeat_stats.json"""
import json, re, csv, collections, statistics as st
from datetime import date
SUF=r'\b(inc|incorporated|corp|corporation|co|company|ltd|limited|plc|llc|holdings?|group|technologies|technology|the|sa|ag|nv|se|lp|therapeutics|pharmaceuticals|biosciences|bio)\b'
ALIAS={'alphabet':'google','x':'twitter','facebook':'meta','square':'block','activision':'microsoft','xbox':'microsoft','linkedin':'microsoft','github':'microsoft','twitch':'amazon','cruise':'gm','general':'gm'}
def k(name):
    n=re.sub(r'\(.*?\)','',name.lower()); n=re.sub(r'[^a-z0-9 ]',' ',n); n=re.sub(SUF,' ',n).split()
    kk=n[0] if n else name.lower(); return ALIAS.get(kk,kk)
def d(s): y,m,dd=(int(x) for x in s[:10].split('-')); return date(y,m,dd)
c=json.load(open('data/corpus_v3.json'))
g=collections.defaultdict(list)
for r in c: g[k(r['company'])+('|bio' if r['sector']=='biotech_health' else '')].append(r)   # first-word key + bio split avoids Unity/Unity Biotechnology style collisions
rows=[]
for key,v in g.items():
    v.sort(key=lambda r:r['event_date'])
    if len(v)<2: continue
    gaps=[(d(b['event_date'])-d(a['event_date'])).days/30.4 for a,b in zip(v,v[1:])]
    rows.append(dict(company=v[0]['company'].split(' (')[0],sector=collections.Counter(r['sector'] for r in v).most_common(1)[0][0],events=len(v),
        first=v[0]['event_date'][:7],last=v[-1]['event_date'][:7],min_gap_months=round(min(gaps),1),median_gap_months=round(st.median(gaps),1),
        within_12m=sum(g_<=12 for g_ in gaps),pcts=';'.join(str(r['pct_workforce']) for r in v),
        communicators=';'.join(r['communicator'] for r in v),mentions_ai=';'.join(str(int(bool(r.get('mentions_ai')))) for r in v),
        tiers=''.join(r['tier'] for r in v)))
rows.sort(key=lambda r:(-r['events'],r['median_gap_months']))
with open('data/repeat_layoffs.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
S={'companies':len(g),'repeaters':len(rows),'share_repeaters':round(len(rows)/len(g),3),'three_plus':sum(r['events']>=3 for r in rows),
   'within_12m_pairs':sum(r['within_12m'] for r in rows),'companies_with_back_to_back_within_12m':sum(r['within_12m']>0 for r in rows),
   'median_gap_months':st.median([r['median_gap_months'] for r in rows]),'by_sector':{}}
for sec in sorted({r['sector'] for r in rows}):
    tot=sum(1 for v in g.values() if collections.Counter(x['sector'] for x in v).most_common(1)[0][0]==sec)
    S['by_sector'][sec]=(sum(r['sector']==sec for r in rows),tot)
# second-round wording drift among repeaters with 2+ tier-A (wording-verified) events
drift=[]
for key,v in g.items():
    A=[r for r in v if r['tier']=='A']
    if len(A)>=2:
        f,l=A[0],A[-1]
        drift.append(dict(company=v[0]['company'],first=f['event_date'][:7],last=l['event_date'][:7],
            apology=(f.get('apology'),l.get('apology')),responsibility=(f.get('takes_responsibility'),l.get('takes_responsibility')),
            ai=(bool(f.get('mentions_ai')),bool(l.get('mentions_ai'))),pct=(f.get('pct_workforce'),l.get('pct_workforce')),comm=(f['communicator'],l['communicator'])))
S['wording_drift_pairs']=drift
json.dump(S,open('data/repeat_stats.json','w'),indent=1,default=list)
print({k_:v for k_,v in S.items() if k_!='wording_drift_pairs'}); print('top:'); [print(' ',r['company'],r['events'],r['first'],'->',r['last'],'median gap',r['median_gap_months'],'m') for r in rows[:15]]
print('drift pairs',len(drift))
