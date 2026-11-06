# Living paper: The Origins of State Capacity (Besley and Persson 2009)

This repository holds the working files behind the living-paper page
**https://livingscience.ai/econ/living-state-capacity**: two extension studies that
re-estimate the paper's cross-country tables on 2000-2024 outcomes measured with the
successor data of each original source, plus a corrections study that applied the fixes a
provenance audit raised.

**Paper.** Besley, Timothy, and Torsten Persson. 2009. "The Origins of State Capacity:
Property Rights, Taxation, and Politics." *American Economic Review* 99(4): 1218-1244.
doi:10.1257/aer.99.4.1218. The earlier working-paper version is NBER WP 13028 (April
2007), https://www.nber.org/papers/w13028; the two versions differ in the empirical
specification (the WP tables carry regional fixed effects, the AER tables do not), which
matters below. Neither PDF ships here; see `LARGE_FILES_OMITTED.md`.

## No replication has run yet, by design

This paper went extension-first. The official replication deposit (openICPSR project
113314, doi:10.3886/E113314V1: one 37 KB `AER.dta` plus a ReadMe) sits behind a
registration gate, a free ICPSR login and a click-through license that must be a human
act, so it was never downloaded and no Phase 1 replication has run. The unlock steps, two
minutes of human time, are documented in `package/PROVENANCE.md`.

The extension studies therefore ran on their pre-registered reconstruction branch
(Branch R): the baseline "original" side of every comparison is the paper's printed
coefficient cells (Tables 1-2, pp. 1237-1238), hand-transcribed and disclosed, and every
printed cell whose stars are arithmetically impossible given its own printed coefficient
and standard error is tagged `pending-deposit`. The specs pre-register a deposit branch:
when the deposit is obtained, the per-cell adjudication (typo versus replication
divergence) runs against the re-estimated `AER.dta` values, and the tagged cells resolve.
Until then no printed cell is called an error anywhere in these files.

## Headline outcomes

- **The war correlation persists between regions, undiminished.** On outcomes measured
  2000-2024 with the paper's own 1816-2000 war history, external-war incidence keeps the
  paper's positive sign at p < 0.05 in all 8 successor outcome columns, with a median
  standardized coefficient of 0.237 against a paper-era reconstruction anchor of 0.194.
  Within regions (the WP's own robustness cut) it weakens, significant in 3 of 8.
  Parliamentary democracy weakens; German and Scandinavian legal origin is the most
  durable correlate; and plain democracy, a null in the paper, turns into a significant
  positive predictor out of sample. (Study 001, `results/scorecard.csv`.)
- **The legal-fiscal complementarity is stable by era.** The paper's core observable
  proposition, income taxation rising with private credit, is positive and significant
  in all three eras 1975-2000, 2000-2012, 2012-2024 (common-sample correlations 0.50,
  0.64, 0.52), and the pre-declared era slope-difference test does not reject equality
  (p = 0.22). (Study 002, Q1.)
- **The trade-tax march continues, graded direction-only.** Countries with trade taxes
  above 40 percent of total taxes fall 27 (2000) to 15 (2010) to 6 (2023) on GRD 2025.
  The 2010 count does not reconcile with the 7 printed in the authors' 2021 update
  (CEPR DP16256) within the pre-declared tolerance, a dataset-vintage mismatch, so the
  claim is graded direction-only rather than reproduced. (Study 002, Q3.)
- **Twelve printed cells carry stars-versus-implied-t tensions.** Rule-enumerated from
  the published tables and cross-checked against the working paper: in each cell at
  least one of the coefficient, the standard error, or the stars must be misprinted, but
  which one is a deposit question. All twelve (plus one footnote statistic) are tagged
  `pending-deposit` and their printed stars are never used as evidence. (Study 001
  `results/findings.md`, refined by study 003.)

## What is in the repository

| Path | What it is |
|---|---|
| `briefing.md` | The feasibility briefing: why this theory-heavy AER paper gets a short replication target list, the printed-table anomalies, the openICPSR gate, and the extension landscape. |
| `followup/001-001-living-update/` | Study 001: re-estimates Tables 1-2 on 2000-2024 successor outcomes with pre-declared succession gates (G1-G5), grades each determinant persists / weakens / reverses / mixed, updates Figure 1, reruns the income regression, and enumerates the suspect-cell set. |
| `followup/002-002-theory-update/` | Study 002: the complementarity by era (Q1), the determinants against the successor composite capacity measures (Q2), and the trade-tax march through 2023 (Q3). |
| `followup/003-003-corrections/` | Study 003: the twelve bounded audit corrections, applied to the two studies' files in place with backups under `workspace/backups/`; every old-to-new change is in `results/card_corrections.csv`. No verdict word changed. |
| `specs/` | The studies' registered designs, written and gated before the studies ran. Each study's `instruction.md` is the copy it executed under. |
| `recency-research.md` | The research note that scoped the studies: the 2009-2026 data landscape, the authors' own successor work (Pillars of Prosperity 2011 and the 2021 update), and every endpoint verified live with dates. |
| `package/PROVENANCE.md` | The deposit record: what openICPSR 113314 contains, the human unlock steps, and the open raw sources behind each paper variable. |
| `extension-assets/` | The staged input data the studies read, included where the license allows, with `PROVENANCE.md` recording every URL, vintage, sha256 and fetch date, and `sha256sums.txt` as the full manifest (57 files, including the omitted ones). |
| `LARGE_FILES_OMITTED.md` | Everything left out (the gated deposit, the paper PDFs, and large raws whose derived extracts ship instead), each with its re-fetch route. |

## Reproducing

The studies are small cross-section studies: data assembly plus OLS with HC1 robust
standard errors, well under one core-hour each, in Python 3.12 (pandas, numpy,
statsmodels, pyreadstat, openpyxl, scipy, matplotlib) with one R step (reading the V-Dem
RData). The study code is under `followup/*/workspace/code/` and reads a container
staging mirror at `/workspace/eval/followup_staging/shared-data/`, laid out exactly like
`extension-assets/` plus `literature/` and the `nber_w13028_2007.pdf` working paper. To
re-run: place the shipped `extension-assets/` folders at that layout, re-fetch the
omitted files per the URLs and sha256 hashes in `extension-assets/PROVENANCE.md` and
`LARGE_FILES_OMITTED.md`, and run study 001's code (gates first, then
`extract_vdem.R`, the three build scripts, `estimate.py`, `verdicts.py`, `figures.py`),
then study 002's, which reuses 001's `results/frame_update.csv` read-only. Both studies
verify the staged files against `sha256sums.txt` at start and touched no live endpoint
in-run (`001/results/fetch_log.json`). Study 003 edits the two studies' files in place;
its reruns use the studies' own scripts.

## Data

Everything the studies read is inventoried, with URL, vintage, sha256 and fetch date, in
`extension-assets/PROVENANCE.md`, and audited row-by-row against the code that used it.
What ships follows each source's license:

- **V-Dem v16** (CC BY-SA 4.0): the raw RData is omitted for size; the derived extracts
  ship under the share-alike notice in `extension-assets/vdem/NOTICE.md`.
- **UCDP/PRIO Armed Conflict Dataset v26.1** (CC BY 4.0): shipped; cite Davies et al.
  and Gleditsch et al.
- **Correlates of War** Inter-State and Extra-State War v4.0 (free academic use):
  shipped; cite Sarkees and Wayman (2010).
- **UNU-WIDER Government Revenue Dataset 2025**: derived aggregates ship
  (`grd_main.csv`, `grd_nocaution.csv`); the raw workbook is pointed to at
  wider.unu.edu per the provider's guidance.
- **World Bank** GFDD (Sept 2022), WGI (2026), WDI API pulls, and the Doing Business
  historical archive (CC BY 4.0 and World Bank archive terms): the two WDI JSONs the
  studies read ship; the three large workbooks are omitted for size with their derived
  columns shipped in the study frames.
- **Hanson-Sigman State Capacity Dataset v1** via the Our World in Data CSV (CC BY):
  shipped; cite Hanson and Sigman (*JOP* 2021, doi:10.1086/715066) and OWID as
  redistributor.
- **QoG Standard cross-section, Jan 2021** (free use with citation): shipped; cite
  Teorell et al. and La Porta et al. for `lp_legor`.
- **Bjornskov-Rode integrated regime dataset v7.1** (posted openly by the authors, free
  academic use with citation): shipped.
- **Penn World Table 11.0** (CC BY 4.0): shipped.
- **Pillars of Prosperity datasets** (Besley and Persson 2011; Besley, Dann and Persson
  2021): posted openly by the authors on the STICERD book site but with no explicit
  license text, so the raw `.dta` files are pointed to rather than re-hosted; the
  derived columns the studies used ship inside the workspace frames with citation.
- **CEPR DP16256** (Besley, Dann and Persson 2021): cited and engaged throughout; the
  PDF is the authors' and CEPR's to distribute, so it is linked, not shipped. The one
  hand-coded fact taken from it (the 2010 trade-tax count of 7) is disclosed in study
  002's findings.

Files derived from the authors' materials (the Pillars-derived columns, the printed AER
cells transcribed as anchors) remain under the authors' and publishers' terms. Each
shipped dataset remains under its own provider's license, cited above. The study code
and documentation in this repository may be reused with attribution to the living-paper
page.
