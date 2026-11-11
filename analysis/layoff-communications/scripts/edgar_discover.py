"""Discover layoff-related 8-K filings via SEC EDGAR full-text search (public, rate-limited, honest UA).
Output: data/edgar/candidates_<year>.json  (one row per filing, deduped by accession)."""
import json, time, sys, urllib.request, urllib.parse, os
UA="layoff-communications-research/0.1 (personal research script)"
QUERIES=['"reduction in force"','"workforce reduction"','"reduce its workforce"','"reduce our workforce"','"reduction of approximately" "workforce"','layoffs "employees" restructuring plan','"reduce headcount"','"eliminate approximately" "positions"']
def get(url):
    for i in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=40))
        except Exception as e: time.sleep(2*(i+1)); err=e
    print('fail',url[:120],err,file=sys.stderr); return None
def run(year):
    out={}
    for q in QUERIES:
        for frm in range(0,1000,100):
            u="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode({'q':q,'forms':'8-K','dateRange':'custom','startdt':f'{year}-01-01','enddt':f'{year}-12-31','from':frm})
            d=get(u); time.sleep(0.25)
            if not d: break
            hits=d['hits']['hits']
            for h in hits:
                s=h['_source']; adsh=s['adsh']
                row=out.setdefault(adsh,{'adsh':adsh,'company':s['display_names'][0],'ciks':s['ciks'],'file_date':s['file_date'],'items':s.get('items'),'files':set(),'queries':set()})
                row['files'].add(h['_id'].split(':')[1]); row['queries'].add(q)
            if len(hits)<100: break
    rows=[{**r,'files':sorted(r['files']),'queries':sorted(r['queries'])} for r in out.values()]
    os.makedirs('data/edgar',exist_ok=True)
    json.dump(rows,open(f'data/edgar/candidates_{year}.json','w'),indent=1)
    i205=sum(1 for r in rows if r['items'] and '2.05' in r['items'])
    print(year,'filings',len(rows),'with item 2.05',i205,'companies',len({r['ciks'][0] for r in rows}))
if __name__=='__main__':
    for y in (sys.argv[1:] or ['2021','2022','2023','2024','2025','2026']): run(y)
