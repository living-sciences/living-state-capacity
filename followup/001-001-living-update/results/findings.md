# Follow-up study 001 — living-update — findings

**Paper.** Besley & Persson, "The Origins of State Capacity: Property Rights, Taxation,
and Politics," *AER* 99(4): 1218–1244, 2009. Cells cited by table/page: Table 1 p. 1237,
Table 2 p. 1238, Figure 1 p. 1220, Section IV pp. 1235–1239, fns 17–24 pp. 1236–1238.

**Branch.** This study ran on **Branch R (reconstruction; deposit pending)**. The Phase-1
replication on disk (`/workspace/eval/replication/`) is an extension-first scaffold: the
openICPSR 113314 deposit (`AER.dta`) was never unlocked (human gate) and **no Phase-1
reconstruction estimate file exists** on disk. Per the Branch-R rule, paper-era anchors are
the **printed** AER cells, every cell in the rule-defined suspect set carries the tag
`pending-deposit`, no study text asserts which printed cells are typos, and the printed
**stars** of suspect cells are never used as evidence in prose (signs may be).

## Method

For each history determinant we re-estimate the paper's cross-section specification with the
outcome windows rolled from the paper's "1975–early-2000s averages" to **2000–2024** on the
successor instruments, and optionally extend the history variables through 2024 behind the
pre-declared succession gates (§Gates). Specification (AER T1/T2 notes, pp. 1237–1238): OLS
with **HC1 robust SEs**, regressors = external-war incidence + democracy incidence +
parliamentary-democracy incidence + four legal-origin dummies (French excluded; legal
origins from Pillars 2 `l_*`, cross-checked against QoG `lp_legor`). Two first-class
variants per column: **V-between** (the paper's published spec, no regional controls) and
**V-within** (plus World Bank regional dummies — the paper's own fn-20 robustness, which it
reports weakens the war correlation). Three history generations: **X0** (the paper's,
history ≤1975, reconstructed from COW v4 + V-Dem `e_polity2` + Pillars-2 `parl_dem`), **X1**
(extended/headline: `avg_war00` 1816–2000, democracy to 2024, parliamentary via the G1
chain to 2024), and **X2** (war spliced with UCDP type 1+2 to 2024, *descriptive
(contemporaneous-war caveat)* — never enters a verdict). Magnitudes use standardized
coefficients (X and Y z-scored on the estimation sample).

**Pre-1950 history read route (A4).** The pre-1950 democracy/parliamentary history is read
from V-Dem's native R image: `code/extract_vdem.R` does an R `load()` of
`shared-data/vdem/vdem_v16.RData` and writes `workspace/data/vdem_core.csv`. The A4
pre-1950 assertion passes — `e_polity2` is populated back to **1789** (earliest non-missing
year; full image year range 1789–2025) — so the X0 democracy-incidence share from 1800 (or
independence) to 1975 is built on genuine pre-1950 coverage, not back-extrapolation.

**Identification caveat (verbatim).** These are conditional cross-country correlations,
exactly as the paper itself labels its evidence (pp. 1235, 1241); nothing here is causal,
and no verdict below upgrades or downgrades the paper's causal claims, because it made none.

**No outcome regression was run at spec time.**

## Prior art and novelty (novelty-scope bound)

This is **the first re-estimation of the AER 2009 Tables 1–2 specification (external-war
incidence 1816–1975 + democracy and parliamentary-democracy incidence to 1975 + legal
origins, on the paper's outcome battery or its successors) on any post-publication data, and
the first grading of those patterns out of sample.** Verification basis: checked against the
update's published do-files and dataset; literature search 2026-11-05. The two closest prior
works: (a) **Besley–Dann–Persson, CEPR DP16256 (2021)** re-created the *book's* charts on a
2010 cross-section with the book's battery (`avg_war00` + executive constraints + gamma +
ethnic fractionalization) and re-examined the Figure-1 legal–fiscal correlation on 2010
ICTD/Fraser data, finding it "still holds up"; it never re-estimated these AER tables. (b)
**Cárdenas & Tuzemen (Brookings WP, 2011)** is a panel re-examination of the BP
cross-section claims on pre-modern data — the closest early re-estimation. Adjacent work
exists; only the narrow battery claim above is asserted.

## Succession gates (results/gates.json)

All five gates **pass**. Labels travel verbatim from the spec.

| Gate | Computed (2026-11-06, staged files) | Threshold | Pass |
|---|---|---|---|
| **G1 parliamentary chain** | agree 0.9983 / κ 0.9943 (n=8,710, polity leg); agree 0.9942 / κ 0.9804 (n=8,724, LIED leg) | ≥0.99 & κ≥0.97; ≥0.985 & κ≥0.96 `[PREVIEW-CALIBRATED: 0.9982/κ0.9942 (n=8,355); 0.9939/κ0.9802 (n=8,369)]` | ✅ → parliamentary X1 extends to 2024 |
| **G2 democracy chain** | agree 0.9245 / κ 0.8493 (n=9,533) | ≥0.90 & κ≥0.80 `[PREVIEW-CALIBRATED: 0.9245/κ0.8493 (n=9,533)]` | ✅ → democracy X1 extends to 2024 |
| **G3 war splice** | agree 0.9765 (n=14,518) | ≥0.95 `[SPEC-DECLARED, no preview. Reference note, not a preview: the Pillars-2 codebook's reported 0.984 is the CIVIL-war dummy's vintage-update agreement (old Pillars vintage vs its UCDP-19.1 recreation, internal conflict) — a same-source-family reference on a different conflict type, not an external-war COW-vs-UCDP cross-source quantity]` | ✅ → X2 built (descriptive) |
| **G4 credit splice** | corr 0.9295 (n=3,489) | ≥0.90 `[SPEC-DECLARED, no preview]` | ✅ → Y1 GFDD leg confirmed |
| **G5 frame sanity** | per-column N (within legal-origin frame): Y1 177, Y4 197, Y5 167, Y6 158, Y7 176, Y8 174, Y9 179, Y10 181 | N≥80; expected ≈150–190 | ✅ (no column `not separable (coverage)`) |

G2's preview-calibrated value reproduces **exactly** (0.9245/κ0.8493, n=9,533). Branch R: the
G5 "X0 vs Phase-1 X agreement = exact on Branch D" clause is N/A (no Phase-1 estimate file).

## Per-row verdicts (results/scorecard.csv)

Grid: 8 verdict columns {Y1 private credit, Y4 WGI rule-of-law, Y5 V-Dem property, Y6
Hanson–Sigman, Y7 1−trade share, Y8 1−(trade+indirect), Y9 income-tax/GDP, Y10 tax/GDP} ×
{V-between, V-within} × {X0, X1}. Y2/Y3 are bridge columns outside the verdict count.

### R-war (headline) — **persists between regions, weakens within**
With the paper's own 1816–2000 war history (X1), the war correlation **persists** between
regions — the paper's positive sign in all 8 columns and **p<0.05 in all 8** (4 legal-capacity,
4 fiscal) — and the median standardized coefficient **0.237** is *not* attenuated (it exceeds
the paper-era reconstruction anchor of 0.194). **V-within** the same X1 history **weakens**:
positive sign in all 8 but p<0.05 in only 3. On the paper's own ≤1975 reconstruction,
**X0 between: weakens (3/8), reconstruction-degraded (corr 0.61)** — i.e. the X0 war share
correlates only 0.61 with the authors' frozen `avg_war00`, which is exactly why **X1
(`avg_war00` 1816–2000) is the designated headline estimate** — and X0 within also weakens
(2/8; all-positive sign). "Persists between regions, absent within" is a pre-named,
first-class outcome — the paper itself flags this fn-20 within-region weakening.

| Generation | Variant | Verdict | sign&p<.05 (legal, fiscal) | median std β | paper-era anchor |
|---|---|---|---|---|---|
| X0 | between | weakens | 3/8 (0,3) | 0.190 | 0.194 |
| X0 | within | weakens | 2/8 (0,2) | 0.040 | 0.194 |
| **X1** | **between** | **persists** | **8/8 (4,4)** | **0.237** | 0.194 |
| X1 | within | weakens | 3/8 (1,2) | 0.093 | 0.194 |
| X2 *(descriptive, contemporaneous-war caveat)* | between | — | 6/8 positive&sig | — | — |

### R-parl (parliamentary democracy) — **weakens**
Paper-sign (positive) in all 8 columns in every cell of the grid, but significance short of
`persists` throughout: X1 between 4/8 (2 legal, 2 fiscal), X1 within 3/8, X0 between 0/8, X0
within 2/8. The paper's significant columns (investor protection, ICRG, income-tax/GDP,
tax/GDP) survive only patchily on the successors (Y1 private credit, Y4 WGI, Y9 income-tax,
Y10 tax under X1 between). Verdict: **weakens** in all four (variant × generation) cells.

### R-legor (German + Scandinavian, joint row) — **persists**
German and Scandinavian legal origin **persist** out of sample: X1 between — German 7/8,
Scandinavian 8/8 positive & significant; X1 within — German 4/8, Scandinavian 6/8; X0
between — German 6/8, Scandinavian 8/8. The one non-`persists` cell is **X0 within**, reported
per-origin: `mixed (split: German weakens, Scandinavian persists)`. This is the most durable
of the paper's correlates on the successor battery.

### R-dem (democracy) — **new out-of-sample pattern**
The paper's own democracy row is null-to-weak. Out of sample, democracy incidence becomes a
**new, significant positive** predictor of capacity: X0 between 7/8, X1 between 6/8, X1 within
5/8 newly positive & significant (X0 within stays null, 8/8 insignificant → "persists (stays
null-to-weak)"). Reported as a **new out-of-sample pattern**, not as a paper error.

## C4 rerun — log income per capita (Section IV D, p. 1239)

DV = log income per capita, mean 2000–2023 (PWT 11.0 `rgdpe`/pop; WDI `NY.GDP.PCAP.KD`
sensitivity). The paper's qualitative claim is "very similar patterns of sign and
significance" (war + legal origins significant, same signs). On 2000–2024 data the war and
legal-origin coefficients carry the paper's positive signs and are jointly significant in the
between-region X1 spec (see `results/income_rerun.csv`): verdict **holds** (qualitative).

## Figure 1 update (C1, descriptive)

`results/fig1_update.png` / `.csv`: private credit/GDP (2000–2021) vs income-tax/GDP
(2000–2023), split at median income per capita. The legal–fiscal correlation is present
(overall corr 0.57; high-income half 0.50, low-income half 0.26) — the complementarity
pattern is visible descriptively. **Grading of the complementarity trajectory belongs to
study 002**; nothing here is double-graded.

## Typo-adjudication surface (Branch R — every row `pending-deposit`)

Rule: a printed cell is *suspect* when its printed stars are impossible given its printed
coefficient and SE at the rounding extremes (two-sided 10/5/1; normal c.v. 1.645/1.960/2.576;
verdicts unchanged under t(N−k)). The enumerated set below is the rule-defined suspect set;
the |t| intervals were **independently re-verified in this run** (e.g. T1c1 [16.008,16.299],
T1c4 [0.268,0.304], T2c4-Soc [3.762,3.918], T2c3-Ger [16.238,18.053] — all reproduce). On
Branch R **no resolution is claimed**; each row awaits the deposit. The WP cross-check column
is now **filled from the staged working paper** (NBER w13028, 2007,
`shared-data/nber_w13028_2007.pdf`, Tables 1–2 pp. 40–41, read 2026-11-06 — study 003-C1).
**Caveat on reading it:** the WP's Tables 1–2 report the *regional-fixed-effects* specification
("All specifications include regional fixed effects (for eight regions)"), i.e. the WP is the
*within-region* cousin of the published *between-region* AER tables, so its coefficients are
not expected to match the AER cell-for-cell; it is the **star pattern** that is the cross-check
evidence here (does the WP corroborate the *merited* reading or the *printed* reading?).
This is **evidence, not adjudication** — resolution stays pending-deposit.

WP cross-check column reads **WP coef (SE) stars → agreement**; "agrees-merited" = WP stars
match the merited reading, "agrees-printed" = WP stars match the printed reading, "differs" =
neither. WP is the regional-FE (within) spec (see caveat above).

| # | Cell (page) | Regressor | Printed coef (SE) stars | \|t\| at rounding extremes | Stars merited | Stars printed | WP cross-check (w13028, regional-FE spec) | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | T1 c1 (p.1237) | democracy | 0.953 (0.059), none | [16.008, 16.299] | *** | none | 0.102 (0.079) none → agrees-printed (ns); WP coef 0.102 ≠ 0.953 ⇒ supports a coef/SE misprint, not a missing star | pending-deposit |
| 2 | T1 c2 (p.1237) | external conflict | 0.647 (0.191) ** | [3.376, 3.399] | *** | ** | 0.676 (0.191) *** → agrees-merited (SE identical, coef close); WP supports *** | pending-deposit |
| 3 | T1 c4 (p.1237) | Socialist LO | 0.010 (0.035) *** | [0.268, 0.304] | none | *** | 0.008 (0.066) none → agrees-merited (coef ≈0.008, ns); WP supports "none" | pending-deposit |
| 4 | T2 c1 (p.1238) | democracy | 0.143 (0.077), none | [1.839, 1.876] | * | none | 0.005 (0.085) none → agrees-printed (ns); WP coef ≈0 ⇒ no support for a * | pending-deposit |
| 5 | T2 c2 (p.1238) | external conflict | 0.598 (0.241) *** | [2.474, 2.489] | ** | *** | 0.683 (0.201) *** (|t|≈3.4) → agrees-printed stars on WP's own numbers; AER printed *** vs merited ** is an in-cell arithmetic gap | pending-deposit |
| 6 | T2 c2 (p.1238) | German LO | 0.196 (0.090) *** | [2.160, 2.196] | ** | *** | 0.290 (0.093) *** (|t|≈3.1) → agrees-printed *** on WP's own larger coef | pending-deposit |
| 7 | T2 c2 (p.1238) | Scandinavian LO | 0.068 (0.084) ** | [0.799, 0.820] | none | ** | 0.195 (0.078) ** → agrees-printed ** but via coef 0.195 (≫0.068) ⇒ supports the 0.068 coef being the misprint | pending-deposit |
| 8 | T2 c3 (p.1238) | German LO | 0.171 (0.010) * | [16.238, 18.053] | *** | * | 0.295 (0.084) *** → agrees-merited ***; printed * (or SE 0.010) is the misprint | pending-deposit |
| 9 | T2 c3 (p.1238) | Socialist LO | −0.109 (0.065) *** | [1.656, 1.698] | * (under t(95): none-to-*) | *** | −0.155 (0.065) ** (|t|≈2.38) → between merited * and printed ***; WP via a larger coef | pending-deposit |
| 10 | T2 c3 (p.1238) | Scandinavian LO | 0.258 (0.134) ** | [1.914, 1.936] | * | ** | 0.364 (0.141) ** (|t|≈2.58) → agrees-printed ** | pending-deposit |
| 11 | T2 c4 (p.1238) | German LO | 0.010 (0.083) *** | [0.114, 0.127] | none | *** | 0.206 (0.065) *** → agrees-printed *** but via coef 0.206 (≫0.010) ⇒ supports the 0.010 coef being the misprint | pending-deposit |
| 12 | T2 c4 (p.1238) | Socialist LO | −0.119 (0.031), none | [3.762, 3.918] | *** | none | −0.110 (0.082) none → agrees-printed (ns) but via SE 0.082 (≫0.031) ⇒ supports the 0.031 SE being the misprint | pending-deposit |

Plus **fn 17 (p. 1236)**: war-incidence "mean … 0.03 with a standard deviation of 0.73" is
impossible for a share in [0,1] (max sd at mean ≤0.035 ≈ 0.18); suspected misprint of 0.073 —
`pending-deposit`. **WP cross-check:** the WP (w13028, p. 26) prints the *same* "mean … 0.03
with a standard deviation of 0.73" — the suspected misprint recurs in the WP and is **not
corrected there**, so the WP does not resolve it. In every suspect cell at least one of
{stars, coefficient, SE} is misprinted; which one is a deposit question.

**Reading the WP column (evidence, not adjudication).** The WP (regional-FE spec) corroborates
the *merited* star on rows 2, 3, 8 (and the printed "none" on 1, 4); on rows 7, 11, 12 the WP
reproduces the *printed* stars but only via a coefficient/SE far from the AER's printed one,
which points at the AER coefficient (rows 7, 11) or SE (row 12) as the likely misprint rather
than the star; rows 5, 6, 9, 10 carry WP stars that are legitimate on the WP's own (different)
numbers and so neither confirm nor overturn the AER cell. No cell is adjudicated — the deposit
remains the arbiter.

## Limitations & binding page-facing surfaces

- **DB discontinuation (Y2/Y3):** Doing Business was discontinued in September 2021 after
  data-irregularity findings; cols 2–3 are bridge columns outside all verdict counts for that
  reason.
- **X2 label travel:** every X2 number is labelled *descriptive (contemporaneous-war
  caveat)*; X2 never enters a verdict (post-2000 wars overlap the outcome window —
  simultaneity, not history).
- **Y4 non-independence (WGI/ICRG successor caveat):** WGI rule of law is partially fed by
  ICRG (the `PRS` source column is present in the WGI dataset), so Y4 is a successor to, not
  an independent check on, the paper's ICRG-based column.
- **Y6 ends 2015:** Hanson–Sigman v1 ends 2015 (window 2000–2015).
- **GRD vintage drift / concept:** GRD 2025 `Merged` sheet (General primary, Central merged);
  "Taxes" = excluding social contributions (%GDP); Caution1–3 country-years are retained in
  the main estimate and excluded in `results/grd_nocaution.csv` (pre-declared leave-out
  sensitivity).
- **ICRG exclusion:** raw/current ICRG is proprietary — honest exclusion; Y4–Y6 are the
  successors.
- **Branch R deviations (see report.md):** (i) no Phase-1 reconstruction estimate file exists,
  so paper-era standardized anchors for the attenuation clause were **reconstructed in-study**
  by running the paper's X0 spec on the earliest observable window of each successor
  instrument (GFDD/V-Dem/GRD 1980–2000) — labelled `pending-deposit`; (ii) the NBER w13028 WP
  is now staged (`shared-data/nber_w13028_2007.pdf`, orchestrator backfill), and the typo-table
  WP cross-check column has been **filled from its Tables 1–2** (study 003-C1) — the WP being
  the regional-FE spec, it is star-pattern evidence, not a cell-for-cell match, and adjudication
  stays pending-deposit; (iii) the X0 war
  reconstruction correlates 0.61 with the authors' `avg_war00` (window/coding/independence
  differences; the exact AER war variable is deposit-only) — X1 (`avg_war00`) is the headline.

**Novelty line (card, verbatim):** the first re-estimation of the AER 2009 Tables 1–2
specification (external-war incidence 1816–1975 + democracy and parliamentary-democracy
incidence to 1975 + legal origins, on the paper's outcome battery or its successors) on any
post-publication data, and the first grading of those patterns out of sample.

**Interpretation (out of grading scope).** The durability of the war and legal-origin
correlates on the successor battery, alongside the newly significant democracy pattern, is
consistent with the paper's complementarity reading (legal and fiscal capacity as joint
investments) — but this paragraph grades nothing and the complementarity trajectory is
study 002's object.
