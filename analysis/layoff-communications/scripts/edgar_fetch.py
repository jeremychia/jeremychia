"""Download the matched filing documents listed in data/edgar/candidates_*.json as plain text.
Rate-limited to ~5 req/s (SEC limit is 10). Resumable."""
import json, glob, os, re, time, html, sys, urllib.request, threading
from concurrent.futures import ThreadPoolExecutor
UA="layoff-communications-research/0.1 jeremyjchia@gmail.com"  # SEC fair-access policy requires a declared contact; used for sec.gov only
os.makedirs('data/edgar/text',exist_ok=True)
lock=threading.Lock(); last=[0.0]
def throttle():
    with lock:
        w=0.2-(time.time()-last[0]); 
        if w>0: time.sleep(w)
        last[0]=time.time()
def clean(raw):
    raw=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',raw)
    raw=re.sub(r'(?s)<[^>]+>',' ',raw); raw=html.unescape(raw)
    return re.sub(r'\s+',' ',raw).strip()
def job(t):
    cik,adsh,f=t
    out=f'data/edgar/text/{adsh}__{f.replace("/","_")}.txt'
    if os.path.exists(out): return
    url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh.replace("-","")}/{f}'
    for i in range(3):
        try:
            throttle()
            b=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=40).read(3_000_000).decode('utf-8','ignore')
            open(out,'w').write(clean(b)[:250000]); return
        except Exception as e: time.sleep(2*(i+1))
    open(out+'.fail','w').write(url)
tasks=[]
for p in sorted(glob.glob('data/edgar/candidates_*.json')):
    for r in json.load(open(p)):
        for f in r['files']:
            if not f.lower().endswith(('.pdf','.xml','.jpg')): tasks.append((r['ciks'][0],r['adsh'],f))
print('files',len(tasks),flush=True)
with ThreadPoolExecutor(4) as ex: list(ex.map(job,tasks))
print('done',len(os.listdir('data/edgar/text')),flush=True)
