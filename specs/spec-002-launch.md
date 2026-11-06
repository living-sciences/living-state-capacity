<!-- LAUNCH FILE: study 002-theory-update ONLY. Where this spec reuses 001 outputs, read them from this run's followup/ directory. -->

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


# PART II: Follow-up study 002, theory-update (complementarity by era + successor reconciliation)

**LAUNCH LINE:** same branch line as 001 (fixed text, orchestrator fills), plus
`RUNS AFTER 001 (reuses results/frame_update.csv read-only; if absent, rebuilds via the
same declared code path)`.

**Launcher settings:** the study launcher ran as `followup <run_dir> --instruction-file <part-II.md>
--name theory-update --timeout 14400`.

## II.0 What this study is (binding framing)

The paper's core observable proposition is that legal and fiscal capacity are
complements — shown as Figure 1 (p. 1220): income-tax share of GDP rises with private
credit within both halves of the income distribution. DP16256 (staged, read) found the
book-version of this correlation "still holds up" on a 2010 cross-section. This study
asks three pre-declared questions the update left open:
(Q1) has the legal–fiscal complementarity strengthened, stayed, weakened, or rotated
across eras 1975–2000 / 2000–2012 / 2012–2024;
(Q2) do the paper's three historical determinants predict the SUCCESSOR composite
capacity measures (Hanson–Sigman 2000–2015, V-Dem property rights 2000–2025, the
authors' own 2021 collective-capacity index for 2016);
(Q3) did DP16256's headline fiscal-capacity fact — countries with trade-tax revenue
share > 40% fell from ~20 (2000) to 7 (2010) (DP16256 §4, Fig. 7) — continue through
2023 on GRD 2025?
All three can come out against the paper (or against the update), per §II.3.

Era boundaries: 2000 (the paper's own outcome-window edge) and 2012
`[SPEC-CHOICE: post-GFC slowbalisation + the autocratization wave's onset; sensitivity
boundary 2010 aligns with DP16256's cross-section]`. Both boundaries carry this label
wherever they appear.

## II.1 Pre-declared constructions

1. `results/complementarity_by_era.csv`: for each era E0 1975–2000, E1 2000–2012,
   E2 2012–2024 — era-mean income-tax share of GDP (GRD; E0 from GRD 1980–2000, the
   pre-1980 gap stated) vs era-mean private credit (GFDD di01; E2 ends 2021) and vs
   era-mean WGI rule of law (E1/E2 only): pooled OLS slope with HC1 SEs, plus within
   both income halves (halves split at era-median PWT income, the paper's Figure-1
   design); common-sample variant (countries present in all eras) beside the
   full-sample one.
2. `results/successor_reconciliation.csv`: the 001 specification (X0 histories +
   legal origins, V-between and V-within) on three successor composites: Hanson–Sigman
   mean 2000–2015, V-Dem `v2xcl_prpty` mean 2000–2025, and `mcollective16` (the 2021
   update's collective-capacity index). **Source correction (binding):**
   `mcollective16` is NOT in `Pillars 2.dta` (whose related variable is the panel
   `coll_cap`, 1789–2016, ~107 countries); it exists only in the staged cluster file
   `pillars/2021/dofiles/Chapter 8 cluster analysis/2016 index components.dta` —
   **67 rows**, which DP16256 itself states is the full non-missing set — and is read
   from there. **Pre-declared small-N handling (chosen now, before launch):** 67 < the
   001 G5 floor of N ≥ 80, so the `mcollective16` column is graded
   `not separable (coverage)` by the G5 rule; its estimates are still computed and
   reported **descriptively**, with N = 67 stated on every surface that shows them
   (tables, findings, card). No exception and no substitution: the update's own 2021
   index is the named object of Q2, and substituting the `coll_cap` panel mean would
   change the construct. Q2's verdicts are therefore issued on the Hanson–Sigman and
   V-Dem columns; the collective-capacity column ships descriptive-only. Same verdict
   vocabulary as 001 rows for the verdicted columns.
3. `results/tradetax_march.csv`: count of countries with trade-tax share of total taxes
   > 40%, years 2000, 2010, 2023 (GRD 2025, same concept rules as 001 S1).
   **Reproduce-then-extend rule:** the 2023 count is gradeable only if GRD 2025
   reproduces DP16256's 2010 count within ±3 (their count: 7) — otherwise report the
   vintage mismatch and grade direction only.
4. `results/fig_complementarity_eras.png` (slopes by era, both halves, CIs);
   `results/fig_tradetax_march.png`.

## II.2 Pre-declared verdict rules

- **Q1 complementarity trajectory** (one verdict; **fixed evaluation order, applied in
  sequence so every outcome maps to exactly one word**):
  1. `not separable` if the common sample < 60 countries; else
  2. `rotated` if any E2 half-sample slope, or the pooled E2 slope, is non-positive;
     else
  3. the pooled E2-vs-E0 slope-difference test decides (HC1; seemingly-unrelated stack
     or bootstrap — **the method is chosen and written into `results/gates.json` in
     Block A, before Block B runs**, not at write-up time): `strengthened` if E2 > E0
     significant at p < 0.10; `weakened` if E2 < E0 significant at p < 0.10 (E2 still
     positive is guaranteed by step 2); else
  4. `stable` (the difference not significant; all era slopes E0/E1/E2, both halves,
     are reported beside the word).
  The common-sample variant decides; the full-sample variant is reported beside it.
- **Q2 reconciliation** (per-composite column verdicts, 001 vocabulary): for each
  successor composite, R-war/R-parl/R-legor graded by the 001 rules collapsed to that
  single column (sign + p < 0.05 = `persists`; sign only = `weakens`; opposite sign
  significant = `reverses`; **`mixed` = anything not matching those three named
  patterns**, e.g. opposite sign short of significance — the catch-all inherited from
  001; **`not separable (coverage)`** = merged estimation N < 80 by the 001 G5 rule —
  per §II.1(2) the `mcollective16` column, N = 67, is graded this way and reported
  descriptively).
- **Q3 fiscal march** (one verdict, conditional on the reproduce-then-extend rule):
  `continued` if count(2023) ≤ 7; `stalled` if 8–19; `reversed` if ≥ 20.
- Against-outcomes, named now: Q1 can come out `rotated` (post-GFC financial deepening
  decoupled from tax development; autocratic high-capacity states); Q2 can `reverse`
  (the successor composites weight bureaucracy and information capacity the paper's
  outcomes do not); Q3 can show `reversed` (post-COVID trade-tax resurgence /
  tariff wave). Each of these is as publishable as confirmation.

## II.3 Blocks

- **A gates:** sha256; locate 001 outputs (else rebuild frames via the same code);
  GRD concept checks; **coverage-count gate** — the merged estimation N of each Q2
  composite (Hanson–Sigman, V-Dem, `mcollective16`) is computed and written to
  `results/gates.json` with the bound rule (N ≥ 80 → verdicted column; N < 80 →
  `not separable (coverage)`, reported descriptively with N on every surface); the Q1
  slope-difference **method choice (stacked SUR or bootstrap) is stated in
  `results/gates.json` here, before Block B runs**.
- **B constructions 1–4** (each writes its csv + `.done`).
- **C verdicts + findings:** `results/findings.md` with: the fixed identification
  sentence; **the DP16256 engagement paragraph with this fixed content** (the 002 face
  of the shared novelty-scope constraint — the two surfaces must not drift): (i) what
  DP16256 did to Figure 1's substance — it re-examined the legal–fiscal correlation on
  2010 ICTD/Fraser data and found it "still holds up" (its own words); (ii) that Q1's
  era-fit, Q2's successor reconciliation, and Q3's 2023 extension are each absent from
  DP16256; (iii) that Q3 is a direct continuation of the update's OWN printed fact
  (its Figure 7 count of 7 in 2010); cited as CEPR DP16256 with the staged copy's
  provenance; the one allowed interpretation paragraph (labelled); limitations (HS
  ends 2015, GFDD ends 2021, E0 tax data starts 1980, era boundaries
  SPEC-CHOICE-labelled, the `mcollective16` N = 67 coverage rule);
  `report.md`, `followup_summary.json`, `result_card.json`.

Card metrics (≤ 5): M1 era slopes (E0/E1/E2, pooled, with CIs); M2 Q1 verdict; M3 Q2
three-column tally (the `mcollective16` column shown as `not separable (coverage)`
with N = 67); M4 the trade-tax counts 2000/2010/2023 with the reproduce check;
M5 gate outcomes. The card also carries the one-line novelty-scope sentence exactly as
the shared constraint fixes it.

## II.4 Out of scope (002)

- Any causal claim about the complementarity; refitting the two-capacity investment
  model (the briefing's theory boundary — one labelled interpretive paragraph max).
- Collective-capacity reconstruction beyond the authors' own staged index (Barro–Lee
  rebuild = next-tick note).
- DP16256's clustering/state-space analyses (engaged in prose only).
- Everything in 001's out-of-scope list.

---

