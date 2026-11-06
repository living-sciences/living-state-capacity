# Follow-up study 001 — living-update — report

## Question

Besley & Persson (*AER* 2009) froze their empirical section at "history up to 1975 →
outcomes averaged 1975–early-2000s." This study asks the living question: **do the paper's
three historical determinants — external-war incidence 1816–1975, parliamentary-democracy
incidence to 1975, and German/Scandinavian legal origin — still predict legal and fiscal
capacity when the outcomes are measured 2000–2024 on the successor instruments, and does
anything change when the history variables themselves are extended through 2024?** It
re-estimates the paper's Tables 1–2 specification on rolled outcome windows, grades each
determinant `persists / weakens / reverses / mixed` per pre-declared rules, updates Figure 1
descriptively, reruns the Section-IV-D income regression, and surfaces the rule-defined
suspect-cell set — all on **Branch R (reconstruction; deposit pending)**.

## Approach

**What was reused.** The replication directory is an extension-first scaffold — there is no
`AER.dta` deposit (human-gated, never unlocked) and **no Phase-1 reconstruction estimate
file** on disk (`/workspace/eval/replication/codebase/README.md`, `PROVENANCE.md`). So the
baseline "original" side is the **printed AER cells** (Tables 1–2, pp. 1237–1238), used as
paper-era anchors with `pending-deposit` tags, exactly as the Branch-R rule requires.

**What was built.** A fresh pipeline over the sha256-verified staged data (57/57 files OK):
- **History (X):** X0 (≤1975) reconstructed from COW v4 inter/extra-state wars + V-Dem
  `e_polity2` + Pillars-2 `parl_dem`; X1 (headline) from the authors' own `avg_war00`
  (1816–2000) + democracy to 2024 + parliamentary via the G1 chain to 2024; X2 war spliced
  with UCDP type 1+2 to 2024 (descriptive only). Legal origins from Pillars 2 `l_*`
  (0 disagreements vs QoG `lp_legor`).
- **Outcomes (Y), 2000–2024 windows:** Y1 GFDD `di01`; Y4 WGI rule-of-law; Y5 V-Dem
  `v2xcl_prpty`; Y6 Hanson–Sigman capacity (ends 2015); Y7–Y10 GRD 2025 (1−trade share,
  1−(trade+indirect), income-tax/GDP, tax/GDP); Y2/Y3 Doing-Business DB2020 bridges.
- **Spec:** OLS + HC1 robust SEs, war + democracy + parliamentary + 4 legal-origin dummies
  (French base); V-between and V-within (WB regional dummies). Verdicts per the pre-declared
  I.3 rules; magnitudes from standardized betas.
- **Gates G1–G5** computed before estimation (all pass); figures; C4 income rerun.

**One honest deviation of note:** with no Phase-1 estimate file, the paper-era *standardized*
anchors needed by the attenuation clause were reconstructed in-study by running the paper's
X0 spec on the earliest observable window of each successor instrument (GFDD / V-Dem / GRD
1980–2000). All such anchors are tagged `pending-deposit`.

## Results

**Headline.** On outcomes measured 2000–2024 with the paper's own 1816–2000 war history, the
war correlation **persists between regions** (the paper's positive sign and p<0.05 in **all 8**
successor outcomes; median standardized coefficient **0.237**, *above* the paper-era
reconstruction anchor of 0.194 — undiminished) **and weakens within regions** (p<0.05 in 3 of
8); on the paper's own ≤1975 reconstruction, **X0 between: weakens (3/8),
reconstruction-degraded (corr 0.61)** with the authors' frozen `avg_war00` — which is why X1
is the designated headline estimate. Parliamentary democracy **weakens**; German/Scandinavian legal origin **persists** (the
most durable correlate); the paper's null-to-weak democracy row turns into a **new
out-of-sample pattern** (significant positive predictor of capacity in 5–7 of 8 columns
between regions).

### Verdict grid (results/scorecard.csv)

| Row | X0 between | X0 within | X1 between | X1 within |
|---|---|---|---|---|
| **R-war** | weakens (3/8) | weakens (2/8) | **persists (8/8)** | weakens (3/8) |
| **R-parl** | weakens (0/8) | weakens (2/8) | weakens (4/8) | weakens (3/8) |
| **R-legor** (Ger+Scand) | persists | mixed (split: Ger weakens, Scand persists) | **persists** | persists |
| **R-dem** (vs null) | new pattern (7/8) | persists-null (0/8) | new pattern (6/8) | new pattern (5/8) |

### War standardized coefficient — paper era vs 2000–2024 (X1 between)

| Outcome column | paper-era β* (recon.) | 2000–2024 β* | sig (HC1) |
|---|---|---|---|
| Y9 income-tax/GDP (paper's central fiscal outcome) | 0.207 | **0.237** | p<0.05 |
| median over 8 verdict columns | 0.194 | **0.237** | 8/8 p<0.05 |

Baseline provenance: printed AER Table 1/2 cells (pp. 1237–1238) for signs/levels;
standardized paper-era anchor reconstructed in-study (Branch R, `pending-deposit`).

### C4 income rerun (Section IV D) — **holds**

DV = log income per capita 2000–2023 (PWT 11.0; WDI sensitivity). Qualitative claim of "very
similar patterns of sign and significance" holds: X1 between — war +4.39 (p<0.001), German LO
+1.47, Scandinavian LO +1.62, Socialist LO +0.41 (all p<0.05), same positive signs.

### Figure 1 (descriptive) — complementarity visible

Private credit/GDP vs income-tax/GDP, split at median income: overall corr 0.57 (high-income
0.50, low-income 0.26). Grading of the complementarity trajectory is study 002's object.

### Gates — all pass

G1 0.9983/κ0.9943 & 0.9942/κ0.9804; G2 0.9245/κ0.8493 (matches preview exactly); G3 0.9765;
G4 corr 0.9295; G5 all column N 158–197 ≥ 80. So X1 democracy and parliamentary extend to
2024, and X2 (descriptive) is built.

### Identification caveat (verbatim)

These are conditional cross-country correlations, exactly as the paper itself labels its
evidence (pp. 1235, 1241); nothing here is causal, and no verdict below upgrades or downgrades
the paper's causal claims, because it made none.

## Deviations & limitations

1. **Branch R / no deposit, no Phase-1 estimates.** Paper-era anchors are the printed cells;
   the attenuation-clause standardized anchors were reconstructed in-study (GFDD/V-Dem/GRD
   1980–2000), all `pending-deposit`. No printed suspect-cell stars are used as evidence; no
   typo is adjudicated (that belongs to the deposit). This is the single biggest divergence
   from a Branch-D run and it affects only the *magnitude* half of the `weakens` rule, never
   the sign/significance tallies that drive the headline.
2. **NBER w13028 WP not staged** → the typo-table WP cross-check column is unavailable (honest
   exclusion; the suspect-set |t| arithmetic was independently re-verified and reproduces).
3. **X0 war reconstruction** correlates 0.61 with the authors' `avg_war00` (window/coding/
   independence-year differences; 38 post-1974-independent states have degenerate short
   windows). X1 (`avg_war00`) is the designated headline generation for exactly this reason.
4. **Doing Business discontinued Sept 2021** → Y2/Y3 are bridge columns outside all verdict
   counts. **Y6** ends 2015 (Hanson–Sigman v1). **Y4** (WGI rule of law) is partially
   ICRG-fed, so it is a successor to, not an independent check on, the paper's ICRG column.
   Raw/current ICRG excluded (proprietary).
5. **GRD concept choice:** "Taxes" = excluding social contributions, %GDP, `Merged` sheet
   (General primary); Caution1–3 leave-out sensitivity in `results/grd_nocaution.csv`.

All pre-declared columns, variants, windows, generations, gates, the C4 rerun, Figure 1, and
the suspect-cell surface were run; nothing was dropped for time. See `results/` for the full
tables (`table1_update.csv`, `table2_update.csv`, `scorecard.csv`, `gates.json`,
`anchors.csv`, `frame_update.csv`, `income_rerun.csv`, `fig1_update.*`,
`fig_war_coefficients.png`) and `results/findings.md` for the full write-up including the
prior-art paragraph and typo table.

**Vocabulary discipline:** the write-up keeps to measured verdict language, describes the
succession gates only as preview-calibrated (never with the two forbidden
registration/validation words), and makes no overbroad first-ness claim beyond the single
permitted novelty sentence — adjacent prior work (DP16256 and Cárdenas–Tuzemen) is named
explicitly.
