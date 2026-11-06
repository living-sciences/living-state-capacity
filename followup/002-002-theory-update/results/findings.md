# Follow-up study 002 — theory-update — findings

**Paper.** Besley & Persson, "The Origins of State Capacity: Property Rights, Taxation,
and Politics," *AER* 99(4): 1218–1244, 2009. Cells cited by table/page: Figure 1 p. 1220,
Table 1 p. 1237, Table 2 p. 1238, Section IV pp. 1235–1239, fns 17–24 pp. 1236–1238.

**Branch.** This study ran on **Branch R (reconstruction; deposit pending)**, the same
branch as study 001. The Phase-1 replication on disk is an extension-first scaffold: the
openICPSR 113314 deposit (`AER.dta`) was never unlocked (human gate). Per the Branch-R
rule, every cell in the rule-defined suspect set carries `pending-deposit`, no study text
asserts which printed cells are typos, and suspect-cell printed **stars** are never used
as evidence in prose. This study re-estimates the paper's *observable* complementarity
proposition on successor data and does not touch the suspect-cell adjudication (that is
001's surface and the deposit's job).

## What this study asks (binding framing)

The paper's core observable proposition is that legal and fiscal capacity are
**complements** — Figure 1 (p. 1220): income-tax share of GDP rises with private credit
within both halves of the income distribution. This study asks three pre-declared
questions the 2021 ten-year update (CEPR DP16256) left open:

- **Q1** — has the legal–fiscal complementarity **strengthened / stable / weakened /
  rotated** across eras E0 1975–2000, E1 2000–2012, E2 2012–2024?
- **Q2** — do the paper's three historical determinants (external war, parliamentary
  democracy, legal origin) predict the **successor composite** capacity measures
  (Hanson–Sigman 2000–2015; V-Dem property rights `v2xcl_prpty` 2000–2025; the authors'
  own 2021 collective-capacity index `mcollective16`, for 2016)?
- **Q3** — did DP16256's headline fiscal-capacity fact — countries with trade-tax share
  > 40% of total taxes fell from ~20 (2000) to 7 (2010), DP16256 §4 Fig 7 — continue
  through **2023** on GRD 2025?

**Identification caveat (verbatim).** These are conditional cross-country correlations,
exactly as the paper itself labels its evidence (pp. 1235, 1241); nothing here is causal,
and no verdict below upgrades or downgrades the paper's causal claims, because it made none.

**No outcome regression was run at spec time.**

Era boundaries 2000 (the paper's own outcome-window edge) and 2012 `[SPEC-CHOICE:
post-GFC slowbalisation + the autocratization wave's onset; sensitivity boundary 2010
aligns with DP16256's cross-section]` carry this label wherever they appear.

## Engagement with DP16256 (the 2021 ten-year update)

(i) **What DP16256 did to Figure 1's substance.** Besley–Dann–Persson, CEPR DP16256
(June 2021), re-examined the legal–fiscal correlation on a 2010 cross-section of
ICTD/Fraser data and reported that it **"still holds up"** (its own words); it re-created
the *book's* charts with the book's battery. (ii) **What is new here.** Q1's era-by-era
fit of the complementarity, Q2's reconciliation of the paper's determinants with the
successor composite capacity measures, and Q3's extension of the trade-tax fact to 2023
are each **absent from DP16256**. (iii) **Q3 is a direct continuation of the update's own
printed fact** — its Figure 7 count of **7** trade-tax-dependent countries in 2010.
Source cited as **CEPR DP16256 (2021)**; staged copy is the Wayback snapshot (2023-03-27)
of CEPR's public RePEc posting (`extension-assets/literature/
besley-persson-dann-2021-dp16256.pdf`, sha256 `0f3762f1…`; `PROVENANCE.md`).

## Prior art and novelty (novelty-scope bound)

This is **the first re-estimation of the AER 2009 Tables 1–2 specification (external-war
incidence 1816–1975 + democracy and parliamentary-democracy incidence to 1975 + legal
origins, on the paper's outcome battery or its successors) on any post-publication data,
and the first grading of those patterns out of sample.** Verification basis: checked
against the update's published do-files and dataset; literature search 2026-11-05. The two
closest prior works: (a) **Besley–Dann–Persson, CEPR DP16256 (2021)** (above), which
re-examined the Figure-1 correlation on 2010 data and found it "still holds up" but never
fit it by era, reconciled the determinants with the successor composites, or extended the
trade-tax fact past 2010; and (b) **Cárdenas & Tuzemen (Brookings WP, 2011)**, a panel
re-examination of the BP cross-section claims on pre-modern data — the closest early
re-estimation. Adjacent work exists; only the narrow battery claim above is asserted.

## Gates (results/gates.json)

- **A1 sha256:** 57/57 staged files verify OK against `sha256sums.txt`.
- **A2 locate 001 outputs:** `results/frame_update.csv` (239 rows) present → reused
  read-only (not rebuilt).
- **A3 GRD concept:** `Merged` sheet; "Taxes" = excluding social contributions (%GDP,
  col 24); income tax = Taxes on Income/Profits/CapGains total (%GDP, col 32); trade tax
  = Taxes on International Trade total (%GDP, col 48) — identical concept to 001 seam S1.
- **A4 coverage-count gate (Q2 composites, X0-between estimation sample):**
  Hanson–Sigman **N = 133** → verdicted; V-Dem `v2xcl_prpty` **N = 134** → verdicted;
  `mcollective16` **merged N = 63** (index non-missing set **N = 67**, DP16256's full set)
  → **`not separable (coverage)`** by the 001 G5 floor (N ≥ 80), reported descriptively
  with N stated.
- **A5 Q1 slope-difference method (chosen before Block B):** **stacked** — pooled stacked
  OLS of era-mean income-tax(%GDP) on era-mean private credit, stacking the E0 and E2
  country observations with an E2 era dummy and a credit × E2 interaction, HC1 robust SEs;
  the interaction coefficient is the E2-vs-E0 slope difference and its HC1 p-value is the
  Q1 step-3 test. Decided on the common-sample variant; full-sample reported beside it.

## Q1 — complementarity trajectory: **stable**

Fixed evaluation order: (1) common sample N = **148** ≥ 60 → not `not separable`;
(2) E2 pooled slope **+0.000557** (p = 8e-06) and both E2 half-slopes positive (low
+0.000239, high +0.000592) → not `rotated`; (3) stacked E2-vs-E0 slope difference
**−0.000259** (HC1 SE 0.000211, p = 0.220) → not significant → **stable**.

The complementarity is **positive and significant in all three eras** and shows no
significant change out of sample. Natural-unit slopes are small only because income tax is
a GDP-fraction while GFDD credit is a percent; the scale-free standardized slope
(= correlation r) is the legible magnitude:

| Era (common sample, pooled) | slope (income-tax/GDP on credit) | HC1 p | std. slope r |
|---|---|---|---|
| E0 1975–2000 (tax 1980–2000) | +0.000815 | 1.6e-06 | **0.50** |
| E1 2000–2012 | +0.000743 | 4.0e-12 | **0.64** |
| E2 2012–2024 (credit ends 2021) | +0.000557 | 7.9e-06 | **0.52** |

By income half (the paper's Figure-1 design, split at era-median PWT income per capita):
the complementarity is carried by the **high-income half** (r: E0 0.36, E1 0.58, E2 0.50,
all significant) and is **weaker in the low-income half** (r: E0 0.17 ns, E1 0.35 sig,
E2 0.28 sig p = 0.0395). [Erratum (003-C2): the low-income-half figures here were corrected
after a `half_label` fix that was silently bucketing missing-income countries into the low
half; the clean E2 low-half common-sample estimate is **p = 0.0395, significant** (was reported
p = 0.074 marginal), E1 low r 0.30→0.35. The Q1 verdict is **unchanged** (stable) — the slope-
difference test is run on the pooled sample, not the halves.] The WGI rule-of-law variant (legal-capacity proxy, E1/E2 only)
is strongly positive and if anything strengthens in the high half (r ≈ 0.40→0.47). Era
slopes E0/E1/E2, both halves, full and common samples: `results/complementarity_by_era.csv`;
trajectory with Fisher 95% CI: `results/fig_complementarity_eras.png`.

## Q2 — successor reconciliation (001 X0 spec; V-between primary, V-within beside)

Same verdict vocabulary as 001 rows, collapsed to one column per composite: right sign +
p<0.05 = `persists`; right sign only = `weakens`; opposite sign significant = `reverses`;
anything else (e.g. opposite sign short of significance) = `mixed`.

| Composite (N merged) | R-war | R-parl | R-legor (German + Scandinavian) |
|---|---|---|---|
| **Hanson–Sigman 2000–2015** (N=133, verdicted) | weakens (β 0.21, p=0.089) | weakens (p=0.55) | **persists** (both, p=1.6e-10 / 1.7e-24) |
| **V-Dem property 2000–2025** (N=134, verdicted) | weakens (β 0.04, p=0.73) | weakens (p=0.57) | **persists** (both, p=1.7e-4 / 3.0e-6) |
| **`mcollective16`** (merged N=63; index N=67) | *not separable (coverage)* — descr. β 0.22, p=0.011 | *not separable (coverage)* — descr. p=0.74 | *not separable (coverage)* — descr. German p=0.002, Scand p=0.014 |

Verdicts (per spec II.1(2), issued on the two verdicted columns):
- **R-legor (German + Scandinavian) persists** on both verdicted composites — the most
  durable of the paper's determinants, exactly as 001 found on the paper's own battery.
  (V-within: persists on Hanson–Sigman; `mixed (split)` on V-Dem property, where German
  weakens and Scandinavian turns mildly negative short of significance — reported beside
  the between verdict, which is the paper's published spec.)
- **R-war weakens** on both composites: the paper's positive sign survives on Hanson–Sigman
  (near-significant, p = 0.089) but is a far weaker predictor of V-Dem property rights
  (p = 0.73), and V-within V-Dem is `mixed`.
- **R-parl weakens** on both: positive-to-flat, never significant.
- **`mcollective16`** ships **descriptive-only** (`not separable (coverage)`, N stated
  everywhere): descriptively war and legal origin are its strongest correlates, but no
  verdict is issued because merged N = 63 (index N = 67) < 80.

This is the pre-named `weaken`/`reverse` direction for Q2: the successor composites weight
bureaucratic and information capacity that the paper's narrow legal- and fiscal-capacity
outcomes do not, so the war and parliamentary-democracy correlates attenuate while legal
origin — a deep, slow-moving determinant — persists. Full cells (coef, SE, p, std beta,
both variants): `results/successor_reconciliation.csv`.

## Q3 — fiscal march away from trade taxation: **direction only (vintage mismatch); decline continues to 6 in 2023**

Count of countries with trade-tax share > 40% of total taxes (GRD 2025, same concept as
001 seam S1): **27 (2000) → 15 (2010) → 6 (2023)** (`results/tradetax_march.csv`;
`results/fig_tradetax_march.png`).

**Reproduce-then-extend rule triggered.** GRD 2025 yields **15** trade-tax-dependent
countries in 2010 — outside ±3 of DP16256's **7** — so by the pre-declared rule the 2023
count is **graded direction-only, not as a level**. The gap is a **vintage difference, not
a concept choice**: every denominator variant (taxes excl. SC, incl. SC, non-resource
tax) gives 14–15 in 2010, so the GRD-2025 revision/coverage vintage simply carries more
high-trade-tax countries than DP16256's 2021 ICTD vintage at the same date. **Direction:**
the march continues unambiguously and monotonically downward; the 2023 level (6) is in fact
**below DP16256's own 2010 level of 7**. (Had the level been gradeable, count(2023)=6 ≤ 7
would read `continued`; it is reported as direction-only per the rule.) **Coverage caveat
(003-C4):** GRD 2025's 2023 cross-section has data for only **116** countries versus **169**
in 2000 (the `n_countries_with_data` column of `results/tradetax_march.csv`), so the shrinking
raw count at the right edge partly reflects a thinner denominator pool toward the present —
another reason the 2023 figure is read as direction, not level.

## Interpretation (out of grading scope)

The complementarity between legal and fiscal capacity is statistically **stable** across
1975–2024, legal origin remains its single most durable determinant on the successor
composites, and the structural move from trade taxes toward income/broad taxation
continues — a configuration consistent with the paper's reading of legal and fiscal
capacity as joint, slow-moving investments (the complementarity proposition, Sections
I–III). This paragraph grades no model proposition and draws no causal inference.

## Limitations & binding surfaces

- **Era windows / data ends:** E0 tax data start **1980** (GRD begins 1980; the pre-1980
  gap of the 1975–2000 era is stated). GFDD private credit ends **2021** (E2 credit leg
  2012–2021). Hanson–Sigman ends **2015** (Q2 window 2000–2015).
- **`mcollective16` coverage:** the authors' 2021 collective-capacity index is defined for
  **67** countries (DP16256's full non-missing set); merged with the X0 histories + legal
  origins it leaves **63** — below the N ≥ 80 floor, so it is `not separable (coverage)`
  and reported descriptively, with N shown on every surface. No substitution (the
  `coll_cap` panel mean would change the construct).
- **Q3 vintage mismatch:** GRD 2025 vs DP16256's 2021 ICTD vintage — direction-only grade,
  as above.
- **Era boundaries** 2000 and 2012 are `[SPEC-CHOICE]` (2010 sensitivity boundary noted).
- **Successor-measure caveats (inherited):** WGI rule of law is partially ICRG-fed, so it
  is a successor to — not an independent check on — the paper's ICRG column; raw/current
  ICRG is proprietary (honest exclusion).
- **Branch R:** deposit pending; suspect cells carry `pending-deposit`; no typo
  adjudicated here and no suspect-cell stars used as evidence.

**Novelty line (card, verbatim):** the first re-estimation of the AER 2009 Tables 1–2
specification (external-war incidence 1816–1975 + democracy and parliamentary-democracy
incidence to 1975 + legal origins, on the paper's outcome battery or its successors) on any
post-publication data, and the first grading of those patterns out of sample.
