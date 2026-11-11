"""Foreign private issuers file 6-K, not 8-K. Same discovery as edgar_discover.py but forms=6-K -> data/edgar/candidates_6k_<year>.json"""
import json, sys, time, urllib.parse, importlib.util
spec=importlib.util.spec_from_file_location('ed','scripts/edgar_discover.py'); ed=importlib.util.module_from_spec(spec); spec.loader.exec_module(ed)
Q=['"workforce reduction"','"reduction in force"','"reduce its workforce"','"reduce our workforce"','layoffs employees','"reduction of approximately" "employees"','"restructuring" "headcount"','"eliminate" "positions" employees']
def run(year):
    out={}
    for q in Q:
        for frm in range(0,1000,100):
            u="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode({'q':q,'forms':'6-K','dateRange':'custom','startdt':f'{year}-01-01','enddt':f'{year}-12-31','from':frm})
            d=ed.get(u); time.sleep(0.25)
            if not d: break
            hits=d['hits']['hits']
            for h in hits:
                s=h['_source']; row=out.setdefault(s['adsh'],{'adsh':s['adsh'],'company':s['display_names'][0],'ciks':s['ciks'],'file_date':s['file_date'],'items':s.get('items'),'files':set(),'queries':set()})
                row['files'].add(h['_id'].split(':')[1]); row['queries'].add(q)
            if len(hits)<100: break
    rows=[{**r,'files':sorted(r['files']),'queries':sorted(r['queries'])} for r in out.values()]
    json.dump(rows,open(f'data/edgar/candidates_6k_{year}.json','w'),indent=1)
    print(year,'6-K filings',len(rows),'companies',len({r['ciks'][0] for r in rows}))
for y in sys.argv[1:]: run(y)
