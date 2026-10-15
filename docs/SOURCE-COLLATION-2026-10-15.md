# Selected source collation — 2026-10-15

Three selected comparisons. Littmann’s tentative historical interpretation and Gusmani’s d/v ambiguity, conventions and published figure context are directly page-checked. Payne–Sasseville2016 was freshly inspected as author-posted web text only; exact PDF typography and RTI remain open after403 responses.

Scope: selected source-located tasks. This is a fresh, bounded publication check with a separate consultation state for every source. It is not a complete critical edition, exhaustive literature search, independent expert review or project examination of an ancient object.

## Findings and remaining work

| Task | Source observations | Remaining work |
|---|---|---|
| LYD-LW40-HISTORICAL | Printed pp.39–40 mark the Athena restoration/translation as tentative. Littmann states that he lacked object access and drew from Bohn’s published squeeze photograph. | Do not convert a historical interpretation into a secure sign string. Exact modern typography and present object access remain open. |
| LYD-LW40-2016 | The p.70 author-posted text locates the newer verb reading in the third word; the authors’2015 object collation and2016 RTI work are reported evidence, not project examination. | Both ordinary PDF routes returned403. Exact diacritics and complete first-line typography remain pending; extracted web glyphs must not be normalized into a fresh diplomatic line. |
| LYD-GUSMANI1975-LW59 | A I1 is concorded to59 and IN62.107 on p.42. The p.1 transcription and p.2 commentary retain d/v ambiguity; the following round sign is argued against f. The sign table p.50 uses the author’s b convention. | Published photograph/drawing inspected, but damaged signs and the modern b/p convention bridge are not independently adjudicated. Do not replace frozen underdots or date the fragment as an observation. |

## Consultation receipts

| Source | Modality | Inspected locus | Limits |
|---|---|---|---|
| [Roberto Gusmani (1975), Lydische Sprachdenkmäler, Sardis Monograph3, Teil A.](https://sardis-images.s3.amazonaws.com/pdf/Sardis_M3.pdf) | DIRECT_RENDERED_PDF_PAGE_IMAGES | printed p.1, A I1 transcription (PDF ordinal17); printed p.2, commentary (PDF ordinal18); printed p.42, concordance C/D (PDF ordinal58); printed p.50, sign/transcription table (PDF ordinal66); unnumbered illustration leaf, Abb.1–2 A I1 (PDF ordinal146) | Published transcription, commentary, table and photograph/drawing inspected. The scan does not support independent damaged-sign adjudication or a global modern convention crosswalk. |
| [Enno Littmann (1916), Lydian inscriptions, Part I.](https://dn790006.ca.archive.org/0/items/lydianinscriptio00littuoft/lydianinscriptio00littuoft.pdf) | DIRECT_RENDERED_PDF_PAGE_IMAGES | printed p.39, Pergamon discussion and drawing (PDF ordinal51); printed p.40, continuation (PDF ordinal52) | Publication inspection only; no project object autopsy or independent review. |
| [Annick Payne and David Sasseville (2016), Die lydische Athene: eine neue Edition von LW40, Historische Sprachforschung129,66–82.](https://www.researchgate.net/publication/311499251_Die_lydische_Athene_Eine_neue_Edition_von_LW_40) | DIRECT_AUTHOR_POSTED_WEB_TEXT_PAGE_MARKERS | p.70, Neulesung, numbered transcription and n.9; pp.66,69–70, attribution and earlier edition history | Fresh author-posted article text inspected at the p.70 Neulesung section. Both author-PDF and publisher-PDF downloads returned403. Exact PDF diacritics, photographs and RTI remain uninspected this pass. |

The JSON packet retains bibliographic identities, exact native comparison/check pointers, PDF byte hashes where acquired, and page-render hashes for inspected pages. PDF files, rendered page images and full protected editions are not redistributed. A web-text consultation has no PDF byte hash and cannot certify diacritics or figure details. Access failures are route-specific observations, not proof that lawful copies do not exist.

## Reproduce the integrity checks

```sh
python scripts/source_collation.py --check
python scripts/source_collation.py --case 'LYD-LW40-HISTORICAL'
python -m unittest discover -s scripts -p test_source_collation.py
```

Researchers with a lawfully obtained copy can match it to an inspected PDF receipt using `python scripts/source_collation.py --verify-source SOURCE_ID /path/to/source.pdf`. A byte match establishes source version, not scholarly correctness or permission to redistribute it.

Canonical/frozen readings are unchanged. A correction to project source-attribution notation does not accept a reading. See `research/source-collation-2026-10-15.json` for case-specific source voices, uncertainty carriers and remaining work.
