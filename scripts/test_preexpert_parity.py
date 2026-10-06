#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
req=["data/reference/records.json","research/source-lineage-register.json","research/disagreement-register.json","research/rights-source-matrix.json","research/residual-blocker-ledger.json","research/browser-sources.json","scripts/research_api.py","scripts/export_research_layer.py","review/handoff-manifest.json"]
missing=[p for p in req if not (R/p).exists()];assert not missing,missing
rows=json.loads((R/"data/reference/records.json").read_text());status=json.loads((R/"analysis/current-status.json").read_text())
assert len(rows)==118,(len(rows),118)
assert status["acquired_document_ids"]==118 and status["nonempty_source_lines"]==471
assert status["verified_primary_edition_readings"]==0 and status["verified_physical_objects"]==0 and status["independent_review"] is False
print(json.dumps({"status":"PASS","reference_records":118,"source_lines":471,"primary_verified":0,"objects_verified":0,"controls":len(req),"boundary":"Method parity does not equal an independently collated critical edition."}))
