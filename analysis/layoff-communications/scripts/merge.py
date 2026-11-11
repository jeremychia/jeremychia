import json, glob, collections
recs=[]
for f in sorted(glob.glob('data/raw/batch_*.json')):
    b=f.split('_')[-1][0]
    for r in json.load(open(f)):
        r['batch']=b; recs.append(r)
keys=collections.Counter(k for r in recs for k in r)
print('records',len(recs),'companies',len({r['company'].strip().lower() for r in recs}))
print({k:v for k,v in keys.items() if v<len(recs)})
for fld in ['sector','communicator','confidence','public_primary_text','takes_responsibility','apology','mentions_ai','ai_framing','notice_style']:
    print(fld,dict(collections.Counter(str(r.get(fld)) for r in recs)))
print('channels',collections.Counter(c for r in recs for c in (r.get('channel') or [])).most_common(12))
print('reasons',collections.Counter(c for r in recs for c in (r.get('stated_reasons') or [])).most_common(20))
seen=collections.Counter((r['company'].lower(),r.get('event_date','')[:7]) for r in recs)
print('dupes',[k for k,v in seen.items() if v>1])
print('years',sorted(collections.Counter((r.get('event_date') or '????')[:4] for r in recs).items()))
