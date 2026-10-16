# Selected source collation — 2026-10-15

All three selected source contexts now have rendered-PDF consultation records. The supplied Payne–Sasseville PDF closes the LW40 printed-typography check; the authors’ object/RTI evidence remains distinct from project examination.

The follow-up uses user-supplied PDFs. Earlier failed network routes and web-only consultation receipts remain in `previous_consultation_record`; acquisition does not grant redistribution rights. All canonical/frozen readings and independent-review states are unchanged.

## Findings and remaining work

| Task | Source observations | Remaining work |
|---|---|---|
| LYD-LW40-HISTORICAL | Printed pp.39–40 mark the Athena restoration/translation as tentative. Littmann states that he lacked object access and drew from Bohn’s published squeeze photograph. | Keep Littmann’s tentative interpretation historical. The modern printed typography was checked in the follow-up LYD-LW40-2016; present object access and independent adjudication remain open. |
| LYD-LW40-2016 | Printed p.70 reads ẹšν̣ tasẽν̣ acνil / partaras maλiλ. Underdots are on initial e and the two word-final ν signs; the tilde belongs to ẽ, which has no underdot. The third word has no f prefix or question mark. The second line has no underdots. Printed pp.72–76 inspectable images/commentary support attribution of these conventions to the authors, including p for the B-shaped sign in partaras. Their object collation/RTI use is reported evidence, not project examination. | Printed typography check is complete for the selected transcription. Independent damaged-sign adjudication, interactive RTI access and current object/inventory verification remain open. Preserve the frozen directory text and keep syntactic analysis separate from sign evidence. |
| LYD-GUSMANI1975-LW59 | A I1 is concorded to59 and IN62.107 on p.42. The p.1 transcription and p.2 commentary retain d/v ambiguity; the following round sign is argued against f. The sign table p.50 uses the author’s b convention. | Published photograph/drawing inspected, but damaged signs and the modern b/p convention bridge are not independently adjudicated. Do not replace frozen underdots or date the fragment as an observation. |

## Consultation receipts

| Source | Modality | Inspected locus | Limits |
|---|---|---|---|
| [Roberto Gusmani (1975), Lydische Sprachdenkmäler, Sardis Monograph3, Teil A.](https://sardis-images.s3.amazonaws.com/pdf/Sardis_M3.pdf) | DIRECT_RENDERED_PDF_PAGE_IMAGES | printed p.1, A I1 transcription (PDF ordinal17); printed p.2, commentary (PDF ordinal18); printed p.42, concordance C/D (PDF ordinal58); printed p.50, sign/transcription table (PDF ordinal66); unnumbered illustration leaf, Abb.1–2 A I1 (PDF ordinal146) | Published transcription, commentary, table and photograph/drawing inspected. The scan does not support independent damaged-sign adjudication or a global modern convention crosswalk. |
| [Enno Littmann (1916), Lydian inscriptions, Part I.](https://dn790006.ca.archive.org/0/items/lydianinscriptio00littuoft/lydianinscriptio00littuoft.pdf) | DIRECT_RENDERED_PDF_PAGE_IMAGES | printed p.39, Pergamon discussion and drawing (PDF ordinal51); printed p.40, continuation (PDF ordinal52) | Publication inspection only; no project object autopsy or independent review. |
| [Annick Payne and David Sasseville (2016), Die lydische Athene: eine neue Edition von LW40, Historische Sprachforschung129,66–82.](https://www.researchgate.net/publication/311499251_Die_lydische_Athene_Eine_neue_Edition_von_LW_40) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.70, Neulesung, printed transcription, published image/drawing and n.9 (PDF ordinal5); p.72, word-divider qualifications, first-word images and sign commentary (PDF ordinal7); p.73, damage marks and second-word images/commentary (PDF ordinal8); p.74, third-word images/commentary and partaras initial p convention (PDF ordinal9); p.75, partaras and maλiλ images/commentary (PDF ordinal10); p.76, final-word commentary and grammatical analysis (PDF ordinal11) | Supplied PDF pages visually inspected. Published photographs/drawings are source evidence; no project object autopsy, interactive RTI inspection, independent review or automatic reading acceptance. |

PDF byte hashes and page-render hashes are recorded in the packet; protected PDFs and renders are not redistributed. A source-version match establishes neither reading correctness nor permission. The check is bounded to these comparisons, not a complete critical edition or exhaustive literature review.

```sh
python scripts/source_collation.py --check
python scripts/source_collation.py --case LYD-LW40-2016
python scripts/source_collation.py --verify-source SOURCE_ID /path/to/source.pdf
python -m unittest discover -s scripts -p test_source_collation.py
```
