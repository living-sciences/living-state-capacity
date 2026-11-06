# Files not included, and where they came from

Everything omitted from this repository is either someone else's to distribute, behind a
registration gate, or a large raw file whose derived extracts ship here instead. Exact
URLs, vintages, byte counts, sha256 hashes and fetch dates for every omitted input are in
the shipped provenance registers, `package/PROVENANCE.md` and
`extension-assets/PROVENANCE.md` (full hash manifest: `extension-assets/sha256sums.txt`).
Re-fetch any file below and verify it against its listed sha256 to reconstruct the exact
staging the studies ran on.

## The official replication deposit (never obtained; the open human gate)

| Omitted | Why | Canonical record |
|---|---|---|
| openICPSR project 113314: `AER.dta` (36.9 KB), ReadMe PDF, `LICENSE.txt` | Registration-gated (free ICPSR account + click-through terms); never downloaded, never automated. The studies ran on the reconstruction branch with the paper's printed cells as anchors, every suspect cell tagged `pending-deposit` | doi:10.3886/E113314V1; unlock steps in `package/PROVENANCE.md` |

## Papers (pointers, not copies)

| Omitted | Why | Canonical record |
|---|---|---|
| Besley & Persson (2009), the AER article PDF | Publisher copyright; cite the journal record | doi:10.1257/aer.99.4.1218 (an open copy is on LSE Research Online, eprint 33768) |
| NBER WP 13028 (April 2007), the working-paper version read for the study 003 cross-check | NBER distribution copy; link, not re-host | https://www.nber.org/papers/w13028 |
| Besley, Dann & Persson (2021), CEPR DP16256, "Pillars of Prosperity: A Ten-Year Update" | CEPR discussion paper, author copyright; the staged copy was for internal reading only | cite as CEPR DP16256 (June 2021); https://cepr.org/publications/dp16256 |
| Munoz-Sobrado, Piolatto, Zerbini & Braccioli, BSE WP 1432 (2024) | Open working paper, staged as context, never opened in-run; link, not re-host | https://bse.eu/sites/default/files/working_paper_pdfs/1432.pdf |

## Large raws whose derived extracts ship instead

| Omitted | Size | What ships instead |
|---|---|---|
| `vdem/vdem_v16.RData` (V-Dem v16, CC BY-SA 4.0) | 34 MB | the run's extracts `followup/001-*/workspace/data/vdem_core.csv` etc. plus `extension-assets/vdem/vdem_v16_extra_lied_uds.csv`, all under the share-alike notice in `extension-assets/vdem/NOTICE.md` |
| `grd/UNUWIDERGRD_2025.xlsx` (UNU-WIDER Government Revenue Dataset 2025) | 9.7 MB | derived aggregates `followup/001-*/results/grd_main.csv` and `grd_nocaution.csv`; UNU-WIDER's own guidance is to point to wider.unu.edu for the raw file |
| `gfdd/GFDD_sept2022.xlsx` (World Bank GFDD, CC BY 4.0) | 14.4 MB | the `di01` columns inside `followup/001-*/workspace/data/outcomes.csv` and the frames |
| `wgi/wgidataset_with_sourcedata-2026.xlsx` (World Bank WGI 2026, CC BY 4.0) | 11.0 MB | the rule-of-law columns inside `outcomes.csv` and the frames |
| `doingbusiness/Historical-Data--DB04-DB20-.xlsx` (World Bank Doing Business archive) | 15.8 MB | the DB2020 extract `followup/001-*/workspace/data/db2020.csv` |
| Pillars of Prosperity datasets: `pillars/2011/Pillars.dta`, `pillars/2021/Pillars 2.dta`, the do-files and codebooks (Besley & Persson 2011; Besley, Dann & Persson 2021) | 46 MB | posted openly by the authors on the STICERD book site but with no explicit license text, so the clean posture is pointer plus citation; the derived columns the studies used (`avg_war00`, `parl_dem`, the `l_*` legal-origin dummies, `mcollective16`) ship inside the workspace frames with citation. URLs: https://sticerd.lse.ac.uk/textonly/_STICERD/publications/BOOKS/Pillars-of-Prosperity/data/2011/ and .../2021/ |

## Staged but unused, or redundant (all keyless re-fetches)

| Omitted | Why |
|---|---|
| `hanson-sigman/HansonSigman_source.dta`, `cross-sectional-table5.dta` (JOP Dataverse, CC0 1.0) | staged as the backup route; the runs used the OWID CSV route only (shipped). doi:10.7910/DVN/IFZXQX |
| 5 of the 7 WDI JSON pulls (`GC.TAX.TOTL.GD.ZS`, `GC.TAX.YPKG.RV.ZS`, `GC.TAX.INTT.RV.ZS`, `GC.TAX.GSRV.RV.ZS`, `NY.GDP.PCAP.PP.KD`) | never read by either study (fiscal outcomes came from GRD); identical keyless API recipe in `extension-assets/PROVENANCE.md` |
| `ucdp/ucdp-prio-acd-261-csv.zip` and `ucdp-prio-acd-261.pdf` (codebook) | the zip is redundant with the shipped CSV; the codebook is UCDP's to host (https://ucdp.uu.se/downloads/) |
| `vdem/codebook_v16.pdf`, `grd/User_Guide_2025.pdf`, the two Pillars codebook PDFs | reference documents consulted at staging, not opened in-run; each provider hosts its own codebook (URLs in `extension-assets/PROVENANCE.md`) |

## Run machinery that never ships

Engine internals (agent transcripts, logs, prompts, the staging byte-mirror the container
read, and grading or scoring artifacts) are not part of the paper's working directory and
are excluded as a matter of policy, not size. The studies' own code, data extracts,
results, reports and result cards are all here.
