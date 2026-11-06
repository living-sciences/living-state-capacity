<!-- LAUNCH FILE: study 001-living-update ONLY. Study 002 is out of scope for this session. -->

<!-- SPEC PAIR for the Phase 2b judge. At launch each part is copied to its own
--instruction-file. Paper: Besley & Persson, "The Origins of State Capacity: Property
Rights, Taxation, and Politics", AER 99(4): 1218-1244, 2009 (econ7). -->

# Extension specs: besley-persson-2009-state-capacity

**Status:** REVISED resubmission to the Phase 2b judge (Round 1 items BP-A1–A6,
BP-B1–B3, BP-C1–C3 addressed; see "Revision log (2b judge round 1)" at the end).
Originally prepared 2026-11-05 by the Phase 2a recency-research agent; revised
2026-11-05. Every data source verified live 2026-11-05 (`recency-research.md`;
hashes in `extension-assets/PROVENANCE.md` + `sha256sums.txt`).

**What this pair is, in one sentence.** Study 001 re-estimates the paper's Tables 1–2
with the outcome windows rolled from "1975–early-2000s averages" to **2000–2024** and the
history variables optionally extended through 2024 behind pre-declared succession gates,
issuing per-row verdicts on whether the war, parliamentary-democracy, and legal-origin
patterns persist, weaken, or reverse out of sample; Study 002 takes the paper's core
observable proposition — legal and fiscal capacity move together (Figure 1) — and fits it
by era (1975–2000 / 2000–2012 / 2012–2024), reconciles the paper's determinants with the
successor capacity measures (Hanson–Sigman, V-Dem, the authors' own 2021 collective
capacity), and extends the 2021 ten-year update's headline fiscal-capacity fact through
2023.

**Reader question: NONE.** No extension question was submitted and no submitter identity
exists. The page carries **no reader sentence** (current skill rules). Nothing in these
studies, their outputs, run metadata, or transcripts may name or imply a submitter.

## Shared binding constraints (both parts)

- **Phase-1 branch rule (BLOCKING).** These studies launch only after the Phase 1
  replication's `result_card.json` exists. The orchestrator sets exactly one launch line
  (see each part) naming the branch Phase 1 finished on:
  - **Branch D (deposit):** openICPSR 113314 was unlocked; Phase 1 re-estimated every
    cell from `AER.dta` and produced the per-cell adjudication table
    (`matched | divergent | printed-typo-with-evidence`). The extension's paper-era
    anchors are then the **deposit re-estimates** for cells adjudicated
    `printed-typo-with-evidence` and the printed cells elsewhere.
  - **Branch R (reconstruction):** Phase 1 ran on the open-source rebuild. Paper-era
    anchors are the printed cells plus the Phase-1 reconstruction estimates (read from
    the launch line's `<path>`); every cell in the **rule-defined suspect set** (next
    bullet) is compared **qualitatively only** and every surface touching it carries
    the tag `pending-deposit`. No study text may assert which printed cells are typos
    on this branch — that adjudication belongs to the deposit. On Branch R no suspect
    cell's printed STARS are used as evidence in any prose: signs may be cited, stars
    may not.
  Everything else in this spec is branch-invariant: the rolled-window frames are built
  from the staged open legs on both branches.
- **Suspect-cell rule (binding, both branches; replaces any enumeration).** A printed
  cell of Tables 1–2 is **suspect** when its printed stars are impossible given its
  printed coefficient and SE at the rounding extremes — i.e., when NO pair
  (coef ∈ [c−0.0005, c+0.0005], SE ∈ [s−0.0005, s+0.0005]) yields the printed star
  level under the paper's two-sided 10/5/1 convention. Critical values used: normal
  1.645 / 1.960 / 2.576; every verdict below is unchanged under t(N−k) critical values
  (df = 86–114 here: 1.66 / 1.98–1.99 / 2.62–2.63; the only effect is to widen one
  merited band marginally, noted in the table). Applying the rule to every printed
  cell of Tables 1–2 (pp. 1237–1238) gives the following enumerated set — each cell's
  |t| interval computed from the printed numbers at the rounding extremes:

  | # | Cell (page) | Regressor | Printed coef (SE) stars | \|t\| at rounding extremes | Stars merited | Stars printed |
  |---|---|---|---|---|---|---|
  | 1 | T1 c1 (p. 1237) | democracy | 0.953 (0.059), none | [16.008, 16.299] | *** | none |
  | 2 | T1 c2 (p. 1237) | external conflict | 0.647 (0.191) ** | [3.376, 3.399] | *** | ** |
  | 3 | T1 c4 (p. 1237) | Socialist LO | 0.010 (0.035) *** | [0.268, 0.304] | none | *** |
  | 4 | T2 c1 (p. 1238) | democracy | 0.143 (0.077), none | [1.839, 1.876] | * | none |
  | 5 | T2 c2 (p. 1238) | external conflict | 0.598 (0.241) *** | [2.474, 2.489] | ** | *** |
  | 6 | T2 c2 (p. 1238) | German LO | 0.196 (0.090) *** | [2.160, 2.196] | ** | *** |
  | 7 | T2 c2 (p. 1238) | Scandinavian LO | 0.068 (0.084) ** | [0.799, 0.820] | none | ** |
  | 8 | T2 c3 (p. 1238) | German LO | 0.171 (0.010) * | [16.238, 18.053] | *** | * |
  | 9 | T2 c3 (p. 1238) | Socialist LO | −0.109 (0.065) *** | [1.656, 1.698] | * (under t(95): none-to-*) | *** |
  | 10 | T2 c3 (p. 1238) | Scandinavian LO | 0.258 (0.134) ** | [1.914, 1.936] | * | ** |
  | 11 | T2 c4 (p. 1238) | German LO | 0.010 (0.083) *** | [0.114, 0.127] | none | *** |
  | 12 | T2 c4 (p. 1238) | Socialist LO | −0.119 (0.031), none | [3.762, 3.918] | *** | none |

  Plus **fn 17 (p. 1236)**: the war-incidence variable's printed "mean … 0.03 with a
  standard deviation of 0.73" is impossible for a share bounded in [0,1] (max sd at
  mean ≤ 0.035 is ≈ 0.18); suspected misprint of 0.073. In every suspect cell at least
  one of {stars, coefficient, SE} must be misprinted; which one is a deposit question.
  This set strictly contains the briefing's four-cell mandate list and this spec's
  previous five-cell enumeration (reconciliation in the Revision log). **Every cell in
  this set carries `pending-deposit` on Branch R and appears in the typo-adjudication
  table on both branches (§I.3).**
- **Novelty scope (binding on every page-facing surface: 001's prior-art paragraph,
  002's DP16256 engagement paragraph, both cards' one-line novelty sentence, and the
  Phase-3 page).** The only first-ness claim permitted, verbatim or narrower: "the
  first re-estimation of the AER 2009 Tables 1–2 specification (external-war incidence
  1816–1975 + democracy and parliamentary-democracy incidence to 1975 + legal origins,
  on the paper's outcome battery or its successors) on any post-publication data, and
  the first grading of those patterns out of sample." The prior-art paragraph names
  both of the closest prior works: (a) **Besley–Dann–Persson, CEPR DP16256 (2021)** —
  re-created the BOOK's charts on a 2010 cross-section with the book's battery
  (`avg_war00` + executive constraints + gamma + ethnic fractionalization) and
  re-examined the Figure-1 legal–fiscal correlation on 2010 ICTD/Fraser data, finding
  it "still holds up"; and (b) **Cárdenas & Tuzemen (Brookings WP, 2011)** — panel
  re-examination of the BP cross-section claims, pre-modern data, the closest early
  re-estimation. The verification basis is stated wherever the first-ness claim
  appears: "checked against the update's published do-files and dataset; literature
  search 2026-11-05." Banned on all surfaces: any form of "nobody has
  revisited/re-examined the paper's empirics" (false — adjacent work exists; only the
  narrow battery claim above is true).
- **Anchor citation rule.** Every "the paper finds/says X" cites the AER version by
  table/page (Table 1 p. 1237, Table 2 p. 1238, Figure 1 p. 1220, Section IV pp.
  1235–1239, fns 17–24 pp. 1236–1238). The WP (`supplementary/nber_w13028_2007.pdf`) is
  cited only for cross-version evidence on suspect cells.
- **Theory boundary (binding).** The model's eight propositions (Sections I–III) are
  never graded. Study 002 may include at most one interpretive paragraph per study
  connecting results to the complementarity proposition, labelled
  "interpretation, out of grading scope".
- **Identification caveat (fixed sentence, verbatim in both findings.md and on both
  cards):** "These are conditional cross-country correlations, exactly as the paper
  itself labels its evidence (pp. 1235, 1241); nothing here is causal, and no verdict
  below upgrades or downgrades the paper's causal claims, because it made none."
- **Preview-calibration labels (mandatory).** The succession-gate thresholds in §I.2
  were set AFTER computing agreement previews on the staged files. Wherever a G1/G2
  threshold appears (gates.json, findings.md, result_card.json), it carries
  `[PREVIEW-CALIBRATED: preview values stated]` with the §I.2 preview numbers beside it.
  The words "pre-registered" and "validated" are banned for these gates. G3/G4
  thresholds were set WITHOUT previews (stated as such: `[SPEC-DECLARED, no preview]`).
  **No outcome regression was run at spec time** — this sentence ships verbatim in both
  findings.md.
- **Scaling rule.** The paper scales outcomes to [0,1] (Table 1 header note, p. 1237)
  by constructions that are only fully observable in the deposit. To keep magnitudes
  comparable without guessing: every updated regression reports (a) natural-unit
  coefficients and (b) standardized coefficients (both X and Y z-scored on the
  estimation sample); the persist/weaken magnitude wording (§I.3) uses the standardized
  ones. On Branch D, a continuity column additionally reproduces the deposit's exact
  scaling.
- **Fetch policy.** Staged data only (`shared-data/` mirror of `extension-assets/`),
  after sha256 verification against `sha256sums.txt`. ONE declared in-run branch: if a
  staged WDI JSON fails to parse, re-pull the identical API endpoint (keyless), log it
  in `results/fetch_log.json`, and continue. No other fetch, no logins, no
  registration walls, no circumvention of bot blocks (ICRG, umich, CEPR live endpoints
  stay untouched). If an input is missing, stop that block and report; never substitute
  from memory.
- **FOREGROUND RULE.** Every command runs in the foreground; a single shell call stays
  under ~8 minutes (hard cap 10). Never background a job (`&`, `nohup`,
  background-task tools) and never end the turn "to wait". (Everything here is OLS on
  ≤ ~200 observations; expect seconds per block.)
- **Continuation rule.** Every block writes its outputs to `results/` and a
  `workspace/checkpoints/<block>.done` marker when it finishes, and updates
  `followup_summary.json` (with a `remaining` list). If the session ends before
  `result_card.json` completes, the orchestrator relaunches the same instruction as
  `NNN-<name>-cont`; the continuation reuses `workspace/` and `results/`, skips `.done`
  blocks, and finishes `remaining`. Every pre-declared column, window and era runs;
  nothing is dropped for time or budget.
- **Uniform-evaluator rule.** Any grading-artifact or schema problem found while running
  is reported for a pipeline-level fix; nothing is special-cased inside the studies.
- **Banned vocabulary** anywhere in outputs: "proves", "debunks", "causal effect",
  "vindicated", "the paper is right/wrong" unqualified; "pre-registered"/"validated"
  for the preview-calibrated gates; any form of "nobody has revisited/re-examined the
  paper's empirics" (see the novelty-scope constraint above).

---


# PART I: Follow-up study 001, living-update

**LAUNCH LINE (orchestrator fills exactly one, fixed text):**
- Branch D: `REPLICATION: DEPOSIT-COMPLETE (openICPSR 113314 unlocked; per-cell adjudication table at <path>)`
- Branch R: `REPLICATION: RECONSTRUCTION-COMPLETE (open-source rebuild at <path>; deposit pending — suspect cells run pending-deposit)`

**Launcher settings:** the study launcher ran as `followup <run_dir> --instruction-file <part-I.md>
--name living-update --timeout 14400`. The timeout is crash protection only; measured
Phase 2a probes put every block in seconds-to-minutes on one core.

## I.0 What this study is (binding framing)

The paper's empirical section is a cross-section frozen at "history up to 1975 →
outcomes averaged 1975–early 2000s" (Section IV A, pp. 1235–1236). This study asks the
natural living question: **do the same three historical determinants — external-war
incidence 1816–1975, parliamentary-democracy incidence to 1975, German/Scandinavian
legal origin — still predict legal and fiscal capacity when the outcomes are measured
2000–2024 on the successor instruments, and does anything change when the history
variables themselves are extended?** Besley–Dann–Persson's DP16256 (2021, staged) and
Cárdenas & Tuzemen (2011) are the named prior art and are engaged by name under the
shared **novelty-scope constraint** (the only permitted first-ness wording, the fixed
description of what each prior work did, the stated verification basis, and the banned
overbroad forms all live there); DP16256 re-created the BOOK's charts on a 2010
cross-section and never re-estimated these AER tables (novelty argument:
`recency-research.md` §4, scope bound by the shared constraint).

## I.1 Frames

**History variables (X), three generations per determinant:**

| Gen | War | Democracy | Parliamentary | Source |
|---|---|---|---|---|
| X0 (the paper's) | share of years 1816(/indep.)–1975 with COW interstate/extrastate war (fn 17) | share of years 1800–1975 with polity2 > 0 (fn 18) | share of years 1800–1975 parliamentary democracy | Branch D: AER.dta variables; Branch R: Phase 1's reconstruction (COW v4 + V-Dem e_polity2 + Pillars-2 `parl_dem` restricted ≤1975) |
| X1 (extended, headline) | share of years 1816–2000 in external war = Pillars 2 `avg_war00` (the authors' own frozen variable; COW-based) | share of years 1800–2018 with e_polity2 > 0, then LIED≥4 to 2024 (gate G2) | share of years 1800–2024 via the G1 chain | staged |
| X2 (descriptive only) | war extended 2001–2024 via UCDP type 1+2 participant splice (gate G3) | — | — | staged |

X2 exists because post-2000 wars (Russia–Ukraine 2022–25, Iran–Israel 2025, etc.)
overlap the outcome window — simultaneity, not history. X2 columns are labelled
`descriptive (contemporaneous-war caveat)` and never enter any verdict.

**Pre-1950 history route (binding).** The derived extract
`vdem/vdem_v16_extra_lied_uds.csv` covers **1950 onward only**; every pre-1950
`e_polity2`/LIED value — i.e., all of the 1800–1975 (X0) and 1800–2018/2024 (X1)
democracy and parliamentary constructions — is read from `vdem/vdem_v16.RData`
directly. Read route: R (`load("vdem_v16.RData")`, then export the needed columns), or
Python via `pyreadr.read_r()`; whichever is used is logged in findings. Block A
asserts at run start that the loaded series actually reaches the needed years
(§I.4 A4); on a miss the affected construction follows its declared fail branch,
never an improvised substitute.

**Outcome battery (Y), rolled windows:**

| Col | Paper outcome (home) | Successor construct | Window | Leg |
|---|---|---|---|---|
| Y1 | private credit / GDP, avg 1975+ (T1c1) | GFDD `di01` (same King–Levine construct), country mean | 2000–2021 | gfdd/ |
| Y2 | ease of access to credit, DB rank ~2006/07 (T1c2) | DB2020-vintage getting-credit score (final observable vintage) | DB2020 | doingbusiness/ — **bridge column, reported, outside verdict counts (seam S5)** |
| Y3 | investor protection, DB rank (T1c3) | DB2020-vintage protecting-minority-investors score | DB2020 | same status as Y2 |
| Y4 | ICRG anti-diversion avg 1980s–90s (T1c4) | WGI rule-of-law estimate, country mean | 2000–2025 | wgi/ (ICRG itself: honest exclusion, proprietary) |
| Y5 | — (new successor) | V-Dem `v2xcl_prpty`, country mean | 2000–2025 | vdem/ |
| Y6 | — (new successor) | Hanson–Sigman capacity, country mean | 2000–2015 | hanson-sigman/ (v1 ends 2015 — stated in the column header) |
| Y7 | 1 − trade-tax share of taxes (T2c1) | GRD 2025: 1 − Taxes-on-International-Trade / Taxes | 2000–2023 | grd/ |
| Y8 | 1 − (trade+indirect) share (T2c2) | GRD: 1 − (Trade + Indirect)/Taxes | 2000–2023 | grd/ |
| Y9 | income taxes / GDP (T2c3) | GRD: Taxes on Income, Profits & Capital Gains (% GDP) | 2000–2023 | grd/ |
| Y10 | taxes / GDP (T2c4) | GRD: Taxes (% GDP) | 2000–2023 | grd/ |

GRD rules (seam S1): `Merged` sheet; default tax concept per the GRD 2025 User Guide;
where General and Central government both exist, General is primary and Central is a
reported sensitivity; country-years flagged Caution1–3 run as a pre-declared
leave-out sensitivity. Verdict columns: **Y1, Y4, Y5, Y6, Y7, Y8, Y9, Y10 (8 columns)**;
Y2/Y3 are bridge columns.

**Specification** (the paper's, T1/T2 notes p. 1237–1238): OLS, HC1 robust SEs,
regressors = war + democracy + parliamentary + four legal-origin dummies (French
excluded; legal origins from Pillars 2 `l_*`, cross-checked against QoG `lp_legor` —
disagreements listed in findings). Two variants per column, both first-class:
- **V-between** (the paper's published spec, no regional controls);
- **V-within** (plus eight regional dummies — the paper's own fn 20 robustness, which it
  reports weakens the war correlation; regions = the deposit's regions on Branch D, else
  World Bank regions, mapping stated).

## I.2 Succession gates (run before any Block C estimate; write `results/gates.json`)

| Gate | Rule | Threshold | Preview (computed 2026-11-05, staged files) | Fail branch |
|---|---|---|---|---|
| G1 parliamentary chain | agreement of BR(DD=0)∧(e_polity2>0) vs Pillars 2 `parl_dem`, 1950–2016 overlap; and BR(DD=0)∧(LIED≥4) vs same | ≥ 0.99 and κ ≥ 0.97; ≥ 0.985 and κ ≥ 0.96 `[PREVIEW-CALIBRATED: 0.9982/κ0.9942 (n=8,355); 0.9939/κ0.9802 (n=8,369)]` | 0.9982 / 0.9939 | parliamentary extension ends 2016 (`parl_dem` only); stated on card |
| G2 democracy chain | agreement of (LIED≥4) vs (e_polity2>0), 1950–2018 | ≥ 0.90 and κ ≥ 0.80 `[PREVIEW-CALIBRATED: 0.9245/κ0.8493 (n=9,533)]` | 0.9245 | democracy extension ends 2018 |
| G3 war splice | country-year external-war dummy agreement, COW v4 vs UCDP type 1+2 splice, 1946–2006 overlap | ≥ 0.95 `[SPEC-DECLARED, no preview. Reference note, not a preview: the Pillars-2 codebook's reported 0.984 is the CIVIL-war dummy's vintage-update agreement (old Pillars vintage vs its UCDP-19.1 recreation, internal conflict) — a same-source-family reference on a different conflict type, not an external-war COW-vs-UCDP cross-source quantity]` | none | X2 column not built; X1 (avg_war00) unaffected |
| G4 credit splice | corr(GFDD di01, WDI FS.AST.PRVT.GD.ZS), 2000–2021 overlap, pooled | ≥ 0.90 `[SPEC-DECLARED, no preview]` | none | Y1 stays 2000–2021 (GFDD only); the WDI-extended sensitivity is dropped, stated |
| G5 frame sanity | per-column N ≥ 80 after merge; X0 vs Phase-1 X agreement = exact on Branch D | — | expected N ≈ 150–190 | a column under N=80 grades `not separable (coverage)`, never silently dropped |

Every gate's label above ships verbatim wherever that gate appears — `gates.json`,
findings.md, result_card.json — including G3's corrected reference note in full.

## I.3 Pre-declared verdict rules (per history-determinant row; fixed now)

Grid: 8 verdict columns × {V-between, V-within} × {X0, X1}. Verdict words per row, per
(variant, generation):

- **`persists`**: coefficient has the paper's sign AND p < 0.05 in ≥ 5 of 8 columns,
  including ≥ 2 legal-capacity (Y1,Y4,Y5,Y6) and ≥ 2 fiscal-capacity (Y7–Y10) columns.
- **`weakens`**: the paper's sign in ≥ 6 of 8 columns but significance short of
  `persists`; OR `persists` passes while the median standardized coefficient is less
  than half the paper-era standardized anchor (anchor from Branch D deposit
  re-estimates, or Branch R Phase-1 estimates) — then worded
  "persists in sign, attenuated by more than half".
- **`reverses`**: opposite sign AND p < 0.05 in ≥ 3 of 8 columns AND no column with the
  paper's sign at p < 0.05.
- **`mixed`**: anything else — the full grid shown, no summary word beyond "mixed".
- **`not separable (coverage)`**: G5 failure as described.

**Word precedence (all rows):** when both the `persists` bound and the attenuation
clause fire, the scorecard verdict WORD is **`weakens`** — the machine surfaces
(scorecard.csv, result_card.json) carry the single word `weakens`, and the prose
always attaches the fixed phrase "persists in sign, attenuated by more than half".

Rows graded: **R-war** (headline; the paper's most distinctive correlate — T1c1 0.510***
(0.143), T2 row 0.555***–0.762***, pp. 1237–1238); **R-parl** (paper: significant for
investor protection 0.339**, ICRG 0.112*, income-tax/GDP 0.212***, tax/GDP 0.160**);
**R-legor** (German AND Scandinavian graded as one joint row, full pre-declared
mapping: `persists` = each of the two dummies positive at p < 0.05 in ≥ 4 of 8;
`weakens` = each positive by sign in ≥ 5 of 8 with significance short of the
`persists` bound, OR the `persists` bound passes while the median standardized
coefficient — pooled over both dummies × 8 columns — is less than half the paper-era
standardized anchor, then worded "persists in sign, attenuated by more than half"
under the word-precedence rule above; `reverses` = either dummy opposite-sign at
p < 0.05 in ≥ 3 of 8 with no column supporting that same dummy at p < 0.05;
`mixed` = anything else, including the split case, which is reported per-origin and
worded `mixed (split: German [word], Scandinavian [word])`); **R-dem** (the paper's own democracy row is null-to-weak —
graded with the same vocabulary against "null", i.e. `persists` here means staying
insignificant in ≥ 6 of 8; a newly significant pattern is reported as
"new out-of-sample pattern", not as a paper error). The headline sentence always reports
V-between and V-within side by side — the paper itself flags the within-region weakening
(fn 20, p. 1236), so "persists between regions, absent within" is a pre-named,
first-class outcome, not a failure of the study.

**C4 rerun (Section IV D, p. 1239):** the same regressions with log income per capita
(PWT 11.0 `rgdpe`/pop, mean 2000–2023; WDI sensitivity) as the dependent variable;
graded `holds / does not hold` against the paper's qualitative claim of "very similar
patterns of sign and significance" (war + legal origins significant, same signs).

**Figure 1 update (C1):** reproduce the scatter (income-tax share of GDP vs private
credit, split at median income, fitted lines) on the 2000–2024 windows →
`results/fig1_update.png` + slopes/correlations by half in `results/fig1_update.csv`.
Descriptive here; GRADING of the complementarity trajectory belongs to study 002
(stated in both, so nothing is double-graded).

**Typo-adjudication surface (both branches):** one table in findings.md covering every
cell in the rule-defined suspect set (shared constraints), with the WP cross-check
column (`supplementary/nber_w13028_2007.pdf`, Tables 1–2). On Branch D it maps each
suspect cell to its deposit re-estimate, confirming or refuting each suspected typo.
On Branch R the same table appears with every row tagged `pending-deposit` and no
resolution claimed; printed stars of suspect cells are never used as evidence in prose
(signs may be, stars may not — shared constraints).

## I.4 Blocks (checkpointed; any order after A)

- **A gates:** A1 sha256 of every used file vs `sha256sums.txt`; A2 branch detection
  (read the launch line; locate Phase-1 outputs — on Branch R the reconstruction
  estimates at the launch line's `<path>`; set anchors); A3 gates G1–G5 →
  `results/gates.json` (every gate: computed value, threshold, label, pass/fail);
  A4 V-Dem history assertion: after loading `vdem_v16.RData`, assert that `e_polity2`
  (and `e_lexical_index`) are populated for pre-1950 years back to 1800 for the
  frame's countries (the derived csv starts 1950 and cannot supply them); on a miss,
  the affected X generation takes its declared fail branch (X1 democracy → G2's fail
  branch; an X0 miss stops that block and reports per the fetch policy) — never an
  improvised substitute.
- **B anchors:** paper-era anchor table (printed cells + Phase-1 re-estimates per
  branch; on Branch R the Phase-1 reconstruction estimates read from the launch
  line's `<path>` are the anchor source for the §I.3 attenuation clause) →
  `results/anchors.csv`; standardized paper-era betas.
- **C frames:** build X0/X1/X2 and Y1–Y10 country-level frame →
  `results/frame_update.csv` (one row per country, every variable, with per-leg
  coverage columns); country-code crosswalk table (COW ↔ ISO3 ↔ V-Dem) with the
  unmatched list printed.
- **D estimates:** 8 verdict columns + Y2/Y3 bridges, × V-between/V-within × X0/X1
  (+X2 descriptive) → `results/table1_update.csv`, `results/table2_update.csv`
  (coefficients, HC1 SEs, p, N, R², standardized betas); C4 → `results/income_rerun.csv`;
  Figure 1 → `fig1_update.png/csv`; figures `fig_war_coefficients.png` (R-war
  coefficient across the 8 columns, paper anchor marked).
- **E verdicts + card:** `results/scorecard.csv` (row, generation, variant, verdict,
  decision statistic, one-line basis, seams touched); `results/findings.md` (method
  paragraph incl. the fixed identification sentence; the prior-art paragraph, bound by
  the shared novelty-scope constraint — fixed first-ness wording, DP16256 AND
  Cárdenas & Tuzemen named with what each did, verification basis stated; per-row
  results; the typo table per branch; gate outcomes with labels verbatim; limitations —
  Y2/Y3 bridge status, Y6 ends 2015, GRD vintage drift, ICRG exclusion, the Y4 WGI
  caveat below); `report.md`, `followup_summary.json`, `result_card.json`.

**Binding page-facing surface list (travels verbatim to findings.md AND
result_card.json/the card; Phase 3 inherits it):**
- **DB discontinuation (Y2/Y3):** "Doing Business was discontinued in September 2021
  after data-irregularity findings; cols 2–3 are bridge columns outside all verdict
  counts for that reason." — in the findings limitations block and on the card
  wherever Y2/Y3 appear.
- **X2 label travel:** wherever an X2 number appears — findings text, any table,
  card metrics — the label `descriptive (contemporaneous-war caveat)` appears beside
  it (the §I.1 column label, extended to every surface).
- **Y4 non-independence (WGI/ICRG successor caveat):** the limitations block states
  that WGI rule of law is partially fed by ICRG, so Y4 is a successor to, not an
  independent check on, the paper's ICRG-based column (worded as recency §5-S6).
- **Novelty line:** the card carries the one-line first-ness sentence exactly as the
  shared novelty-scope constraint fixes it.

## I.5 Headline template (fixed) and card

> "On outcomes measured 2000–2024 with the paper's own 1816–1975 war history, the war
> correlation [verdict phrase]: [k] of 8 successor outcomes at p<0.05 between regions
> ([k'] within regions), median standardized coefficient [b] against [b0] in the paper's
> era; parliamentary democracy [verdict]; German/Scandinavian legal origins [verdict];
> with history extended to [2016/2018/2024 per gates], [one sentence on what changes]."

Card metrics (≤ 5): M1 the R-war grid tally (between/within); M2 war standardized beta,
paper era vs 2000–2024 (Y9 income-tax/GDP column — the paper's central fiscal outcome);
M3 R-parl tally; M4 R-legor tally; M5 gate outcomes (G1–G5, with labels). Standard
followup card schema (this is a scored replication paper; no schema deviation).

## I.6 Out of scope (001)

- Any causal design (IV, panel event studies) — a different study, named next-tick
  candidate (Cárdenas–Tuzemen-style panel).
- B-READY as a Y2/Y3 successor (non-comparable instrument; next-tick note).
- Raw/current ICRG (proprietary — honest exclusion; Y4–Y6 are the successors).
- The eight propositions; any model refitting.
- Resolution of the rule-defined suspect cells on Branch R (pending-deposit; the set
  itself is in the shared constraints).
- Re-grading Phase-1 claims; any outward message; any model/API spend beyond the session.

---

