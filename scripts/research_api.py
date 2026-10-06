#!/usr/bin/env python3
import argparse,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
FILES={"records":"data/reference/records.json","lineage":"research/source-lineage-register.json","disagreements":"research/disagreement-register.json","sources":"research/source-register.json","frontier":"research/source-frontier.json"}
def rows(k):
 v=json.loads((R/FILES[k]).read_text(encoding="utf-8"))
 if isinstance(v,list): return v
 for key in ("records","items","sources","entries","lineages"):
  if isinstance(v.get(key),list): return v[key]
 return [v]
p=argparse.ArgumentParser();p.add_argument("resource",choices=FILES);p.add_argument("--text",default="");p.add_argument("--limit",type=int,default=50);a=p.parse_args();q=a.text.casefold();x=[r for r in rows(a.resource) if not q or q in json.dumps(r,ensure_ascii=False).casefold()][:a.limit];print(json.dumps({"resource":a.resource,"records":x,"boundary":"Attributed digital evidence; source lineage, uncertainty and component rights remain controlling."},ensure_ascii=False,indent=2))
