"""Fetch SIC code/description + ticker for each CIK in data/edgar/events.json -> data/edgar/sic.json (resumable)."""
import json, os, time, urllib.request
UA="layoff-communications-research/0.1 jeremyjchia@gmail.com"   # SEC requires declared contact; sec.gov only
ev=json.load(open('data/edgar/events.json'))
out=json.load(open('data/edgar/sic.json')) if os.path.exists('data/edgar/sic.json') else {}
for cik in sorted({e['cik'] for e in ev}):
    if cik in out: continue
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json',headers={'User-Agent':UA}),timeout=30))
        out[cik]={'sic':d.get('sic'),'sic_desc':d.get('sicDescription'),'tickers':d.get('tickers'),'state':(d.get('addresses',{}).get('business',{}) or {}).get('stateOrCountry'),'name':d.get('name')}
    except Exception as ex: out[cik]={'error':str(ex)}
    time.sleep(0.2)
json.dump(out,open('data/edgar/sic.json','w'),indent=1); print(len(out),'ciks',sum('error' in v for v in out.values()),'errors')
