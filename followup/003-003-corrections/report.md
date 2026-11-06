# Follow-up study 003 — corrections — report

Corrective study applying the twelve bounded conformance fixes the provenance audit raised
against the two completed follow-up studies of Besley & Persson, "The Origins of State
Capacity," *AER* 99(4): 1218–1244 (2009): study **001** (`followup/001-001-living-update/`)
and study **002** (`followup/002-002-theory-update/`). Both studies passed the audit (every
spot-recomputed statistic exact; reforms/privacy/honesty clean); this study ships exactly the
twelve corrections and nothing else. **No verdict word changes.** Every old → new change is
logged in `results/card_corrections.csv`.

## Question

Apply twelve pre-specified, bounded corrections to the two prior studies, editing their files
in place: (001) fill the typo-table WP cross-check column from the now-staged NBER working
paper; fix the misattributed printed war cells and placeholder SEs in `anchors_printed.json`
and tag the two suspect war cells pending-deposit; restore a truncated identification
sentence; carry the X0-between result into the headline per the I.5 template; fix one printed
star in the summary; record the pre-1950 read route and the A4 assertion; implement and run
the R-legor pooled attenuation arm (verify non-binding); label the X2 table rows descriptive.
(002) reword a first-ness claim to absence-framing; fix the `half_label` bug that bucketed
missing-income countries into the low half and re-run the affected E2 low-half estimate with a
one-line erratum; add a `[SPEC-CHOICE]` era-boundary label to the card; add a Q3 coverage
sentence. Binding framing rules: nothing is upgraded; a code fix whose corrected value changes
a printed number ships the TRUE value with an erratum; the WP cross-check is filled from the
real PDF, never from memory.

## Approach

- **Reused unchanged from the completed studies:** both studies' working code, frames, and
  result files — I read them from disk, backed up every file I touched under
  `workspace/backups/`, and edited the studies' files in place as the instruction directs
  ("corrected files in place"). The two code reruns use the studies' own scripts.
- **Environment:** the replication venv was gone; I rebuilt a fresh `uv` venv (Python 3.12,
  pandas 3.1.1, numpy, statsmodels 0.15, pyreadstat, scipy, matplotlib, pypdf). The two
  staged PDFs (the AER paper `/workspace/inputs/paper.pdf`; the WP
  `followup_staging/shared-data/nber_w13028_2007.pdf`) were read with `pdftotext -layout` /
  `pypdf`. Foreground only, no fetches, no new estimators.
- **Two code reruns (the only computation):** (C7) added the R-legor pooled attenuation arm to
  001's `verdicts.py` and re-ran it; (002-C2) fixed `half_label` in 002's `estimate_002.py`,
  re-ran it, and regenerated the complementarity figure. Before each rerun I confirmed the
  unmodified script reproduces the existing outputs byte-for-byte (environment match).
- **Ten editorial corrections:** applied as in-place text/JSON edits, each verified against
  the source of truth (the AER PDF for printed cells, the WP PDF for the cross-check, the
  V-Dem image for the 1789 fact, the study CSVs for counts).

## Results

### Study 001

**001-C1 — WP cross-check filled (evidence, not adjudication).** Read NBER w13028 (2007)
Tables 1–2 (pp. 40–41) from the staged PDF. Crucial caveat recorded on the surface: **the WP's
tables are the regional-fixed-effects (within-region) specification** ("All specifications
include regional fixed effects"), i.e. the within cousin of the published between-region AER
tables, so coefficients are not expected to match cell-for-cell — the **star pattern** is the
cross-check. The WP corroborates the *merited* star on suspect rows 2, 3, 8 (and the printed
"none" on 1, 4); on rows 7, 11, 12 it reproduces the *printed* stars but only via a
coefficient/SE far from the AER's printed one, pointing at the AER **coefficient** (rows 7, 11)
or **SE** (row 12) as the likely misprint rather than the star; rows 5, 6, 9, 10 carry WP stars
legitimate on the WP's own numbers and so neither confirm nor overturn the AER cell. For **fn 17**
the WP (p. 26) prints the *same* "mean … 0.03 … s.d. 0.73" — the suspected `0.073` misprint
recurs in the WP and is not corrected there. All rows stay `pending-deposit`; nothing adjudicated.

**001-C2 — `anchors_printed.json` printed cells fixed** (verified against `paper.pdf`,
Tables 1–2, pp. 1237–1238):

| Cell | was | now (printed AER) |
|---|---|---|
| T1 war c3 | `[0.598, 0.241, ***]` (a Table-2 value) | `[0.029, 0.209, ""]` (ns) |
| T1 war c4 | `null` | `[0.576, 0.170, ***]` |
| T2 war c1–c4 | `c1=[0.555,·,**]`, `c2=[0.762,·,***]` (two, out of order) | `0.762(0.250)***, 0.598(0.241)***, 0.579(0.220)***, 0.555(0.162)***` |
| placeholder SEs | `0.0` | T1 parl 0.137/0.061; T2 parl 0.078/0.068; T2 war filled |
| suspect tags | untagged | T1 c2 & T2 c2 (external conflict) tagged `pending-deposit` |

**001-C3** restored the truncated note-5 identification sentence on the card ("…nothing here is
causal, **and no verdict below upgrades or downgrades the paper's causal claims, because it
made none.**"). **001-C4** carried `X0 between: weakens (3/8), reconstruction-degraded
(corr 0.61)` into the headline on the card, `findings.md`, and `report.md`, with X1 kept as the
designated headline estimate (I.5 template conformance). **001-C5** fixed the summary star:
`T2 0.555**-0.762***` → `0.555***-0.762***` (printed T2 c4 is `0.555***`). **001-C6** added a
line naming the pre-1950 read route (R `load()` of `vdem_v16.RData` via `code/extract_vdem.R`)
and the A4 result (`e_polity2` populated back to **1789**, verified from the extracted image).
**001-C8** added a `caveat` column = "descriptive (contemporaneous-war caveat)" to every X2 row
of `table1_update.csv` (84 rows) and `table2_update.csv` (56 rows), blank on X0/X1 rows, with
all numeric values preserved exactly (line-append, no re-serialization).

**001-C7 — R-legor pooled attenuation arm: implemented, run, NON-BINDING (confirmed).** Added
the pooled German+Scandinavian attenuation arm to `verdicts.py` (per the I.3 rule: when the
joint `persists` bound passes but the median standardized coefficient, pooled over both dummies
× 8 columns, is below half the paper-era pooled anchor, the verdict becomes `weakens`, worded
"persists in sign, attenuated by more than half"). Paper-era pooled anchor = **0.198**
(threshold 0.099). Computed pooled medians: X0-between 0.252, X1-between 0.258, X1-within 0.131
(all above threshold → `attenuated=False`), X0-within 0.098 (just below → `attenuated=True`,
**but non-binding**: that cell is `mixed (split: German weakens, Scandinavian persists)`, so the
joint-persists bound never passes and the attenuation clause does not fire). **All 16 scorecard
verdict words are identical to the pre-correction scorecard** — the arm changes nothing, exactly
as the audit found. See `results/fig2_001C7_legor_attenuation.png`.

### Study 002

**002-C1** reworded the comparison-table cell (and the matching summary note) from
"first era-by-era fit" to "**era-by-era fit absent from DP16256**" — absence-framing; the
battery sentence stays the only permitted first-ness claim (the `findings.md` body already used
absence-framing). **002-C3** added `[era boundaries 2000/2012: SPEC-CHOICE]` to the card's M1
value line. **002-C4** added, beside the Q3 direction-only grade (report, findings, card), that
GRD 2025's 2023 cross-section covers only **116** countries versus **169** in 2000 (both counts
already in `tradetax_march.csv`), so the shrinking raw count partly reflects a thinner
denominator — reinforcing the direction-only grade.

**002-C2 — `half_label` fix + E2 low-half re-run (true value shipped; verdict unchanged).** The
original `half_label` split countries at the median income but silently bucketed
missing-income (NaN PWT income) countries into the **low** half (a NaN fails the `>= median`
test). The fix drops those countries from both halves. Re-running `estimate_002.py` leaves the
pooled slopes, `successor_reconciliation.csv`, `tradetax_march.csv`, and `verdicts.json`'s Q1
verdict **unchanged** (only the half-sample rows move), and corrects the E2 low-half
common-sample estimate:

| Quantity (E2 low-half, common sample) | Before (contaminated) | After 002-C2 fix |
|---|---|---|
| n | 77 | 71 |
| std. slope r | 0.2151 | 0.2806 |
| HC1 p | **0.0736 (marginal)** | **0.0395 (significant)** |
| low-half r sequence E0/E1/E2 | 0.17 / 0.30 / 0.22 | 0.17 / 0.35 / 0.28 |

The Q1 slope-difference test runs on the **pooled** common sample (E2-vs-E0 diff p = 0.220,
unchanged), so **the Q1 verdict stays `stable`**. The erratum is filed in `report.md` and
`findings.md`; the complementarity figure was regenerated (the E2 low-half CI now sits above
zero), and the card's figure alt-text updated accordingly. See
`results/fig1_002C2_lowhalf_fix.png`.

## Deviations & limitations

- **Edited prior studies' files in place.** The task is a corrective study whose deliverable is
  "corrected files in place"; I therefore edited files under `001-001-living-update/` and
  `002-002-theory-update/` as instructed, keeping full backups of every touched file under this
  study's `workspace/backups/`. I did **not** touch `/workspace/eval/replication/`, `analyze/`,
  `verify/`, or `report/`.
- **No AER PDF was separately staged** for 001-C2's "verify against the staged AER PDF"; the
  AER published article is `/workspace/inputs/paper.pdf` (confirmed: VOL. 99 NO. 4, Tables 1–2
  on pp. 1237–1238), which I used as the printed-cell source of truth.
- **The WP is the regional-FE (within) spec.** 001-C1's cross-check is therefore star-pattern
  evidence, not an arithmetic replication of the between-region AER cells — stated prominently
  on the surface. Adjudication of every suspect cell remains `pending-deposit` (Branch R).
- **No verdict word changed** on any surface (001 scorecard: all 16 identical; 002 Q1/Q2/Q3
  verdicts identical). The two numeric changes that reached a printed surface (E2 low-half p;
  the corrected printed anchors) shipped as TRUE values with erratum/provenance notes.
- Scope held to the twelve items; nothing upgraded, no new analysis added.
