# Follow-up study 002 — theory-update

Besley & Persson, "The Origins of State Capacity: Property Rights, Taxation, and Politics,"
*AER* 99(4): 1218–1244 (2009). Branch **R** (reconstruction; openICPSR 113314 deposit
pending the human gate), same branch as study 001.

## Question

The paper's core *observable* proposition is that legal and fiscal capacity are
complements — Figure 1 (p. 1220): the income-tax share of GDP rises with private credit in
both halves of the income distribution. The 2021 ten-year update (CEPR DP16256) re-examined
this on a 2010 cross-section and found it "still holds up." This study answers three
pre-declared questions the update left open: **(Q1)** has the legal–fiscal complementarity
strengthened / stayed stable / weakened / rotated across eras 1975–2000, 2000–2012,
2012–2024? **(Q2)** do the paper's three historical determinants (external war,
parliamentary democracy, legal origin) predict the *successor composite* capacity measures
(Hanson–Sigman 2000–2015, V-Dem property rights 2000–2025, the authors' own 2021
collective-capacity index `mcollective16` for 2016)? **(Q3)** did DP16256's headline fact —
countries with trade-tax share > 40% of total taxes falling from ~20 (2000) to 7 (2010),
Fig 7 — continue through 2023 on GRD 2025? All three were allowed to come out against the
paper or against the update.

## Approach

**Reused from study 001 (read-only):** `results/frame_update.csv` (the 239-row
country-level frame with the X0 history determinants, four legal-origin dummies, WB
regions, and the successor-outcome battery incl. Y5 = V-Dem property mean 2000–2025 and
Y6 = Hanson–Sigman mean 2000–2015), 001's OLS+HC1 estimation recipe (V-between = no regional
controls, the paper's published spec; V-within = +WB region dummies), and its verdict
vocabulary and gate labels. Cited from `/workspace/eval/followup/001-001-living-update/`.

**Built new (study 002):**
- *Q1* — era-mean panels per country for income tax (%GDP, GRD 2025), private credit
  (GFDD `di01`), WGI rule of law, and PWT income per capita; pooled OLS (income tax on
  credit) with HC1 SEs per era, within both income halves (split at era-median PWT income),
  full and common-sample (countries present in all three eras) variants. The Q1
  slope-difference method (**stacked** OLS with a credit × E2 interaction, HC1) was written
  into `results/gates.json` in Block A, before estimation.
- *Q2* — the 001 X0 spec (war/dem/parl + 4 legal-origin dummies, V-between and V-within) on
  the three successor composites. `mcollective16` was read from the staged cluster file
  `pillars/2021/dofiles/Chapter 8 cluster analysis/2016 index components.dta` (67 rows, keyed
  by iso3) — **not** from `Pillars 2.dta` — and merged onto the frame.
- *Q3* — single-year counts of trade-tax share > 40% (GRD 2025) at 2000/2010/2023, with the
  reproduce-then-extend check against DP16256's 2010 count of 7.

**Environment:** the replication venv was gone; rebuilt a fresh `uv` venv (Python 3.12) with
pandas 3.1.1, numpy, statsmodels 0.15, pyreadstat, openpyxl, matplotlib, scipy. All 57 staged
files verified against `sha256sums.txt` (57/57 OK) before use. No network fetch was needed.

## Results

### Q1 — complementarity trajectory: **stable**

Common sample N = 148 (≥ 60); E2 slope positive and both E2 half-slopes positive (not
rotated); stacked E2-vs-E0 slope difference −0.000259 (HC1 p = 0.220) → not significant →
**stable**. The complementarity is positive and significant in all three eras; the scale-free
standardized slope (= correlation r) is the legible magnitude (natural-unit slopes are tiny
only because income tax is a GDP-fraction while GFDD credit is a percent).

| Era (common sample, pooled) | slope | HC1 p | std. slope r |
|---|---|---|---|
| E0 1975–2000 (tax 1980–2000) | +0.000815 | 1.6e-06 | 0.50 |
| E1 2000–2012 | +0.000743 | 4.0e-12 | 0.64 |
| E2 2012–2024 (credit ends 2021) | +0.000557 | 7.9e-06 | 0.52 |

The co-movement is carried by the high-income half (r 0.36→0.58→0.50) and is weaker in the
low-income half (r 0.17 ns → 0.35 sig → 0.28 sig) — the paper's own Figure-1 texture. See
`results/complementarity_by_era.csv`, `results/fig_complementarity_eras.png`.

> **Erratum (study 003, correction 002-C2).** The low-income-half figures above were corrected
> after a `half_label` bug fix: the original code bucketed missing-income (NaN PWT income)
> countries into the low half, contaminating it. With those countries dropped, the clean E2
> low-half common-sample slope is significant — **p = 0.0395 (not the 0.074 marginal originally
> reported)** — and E1 low r rises 0.30→0.35. The **Q1 verdict is unchanged (stable)**: the
> E2-vs-E0 slope-difference test runs on the pooled common sample (p = 0.220), not the halves.
> Corrected estimates in `results/complementarity_by_era.csv`; figure regenerated.

### Q2 — successor reconciliation

| Composite (N merged) | R-war | R-parl | R-legor (Ger+Scand) |
|---|---|---|---|
| Hanson–Sigman 2000–2015 (N=133) | weakens (p=0.089) | weakens | **persists** |
| V-Dem property 2000–2025 (N=134) | weakens (p=0.73) | weakens | **persists** |
| `mcollective16` (merged N=63; index N=67) | not separable (coverage) | not separable (coverage) | not separable (coverage) |

**Legal origin (German + Scandinavian) persists** on both verdicted composites — the most
durable determinant, matching 001's finding on the paper's own battery. **War and
parliamentary democracy weaken** on these broader composites (which weight bureaucratic and
information capacity the paper's narrow outcomes do not) — the pre-named weaken direction.
`mcollective16` ships descriptive-only (N < 80 floor), descriptively with war and legal
origin as its strongest correlates. See `results/successor_reconciliation.csv`.

### Q3 — fiscal march: direction-only (vintage mismatch); decline continues to 6 in 2023

Counts of trade-tax-share > 40% countries: **27 (2000) → 15 (2010) → 6 (2023)**. GRD 2025's
2010 count (15) is outside ±3 of DP16256's 7, so by the reproduce-then-extend rule the level
is **not graded** — direction only. The gap is a vintage difference, not a concept choice
(every tax denominator gives 14–15 in 2010). The decline is monotone and the 2023 level (6)
sits **below DP16256's 2010 level of 7**. A further reason the 2023 count is read as direction,
not level: **GRD 2025 country coverage at 2023 (116 countries with trade+taxes data) is thinner
than at 2000 (169)** — the denominator pool shrinks toward the present, so the falling raw count
partly reflects fewer reporting countries, reinforcing the direction-only grade (both counts
ship in `results/tradetax_march.csv`). See `results/tradetax_march.csv`,
`results/fig_tradetax_march.png`.

## Comparison to the original / to DP16256

| Quantity | Original / baseline | This study | Source of baseline | Note |
|---|---|---|---|---|
| Legal–fiscal correlation (Figure 1 substance) | "still holds up" on 2010 cross-section (qualitative) | **stable** across 1975–2024 (r 0.50 / 0.64 / 0.52; E2-vs-E0 diff p=0.22) | DP16256 (2021) §Fig 1 re-exam | era-by-era fit absent from DP16256; confirms & quantifies |
| R-legor (German+Scand) on capacity | persists on the paper's battery (001) | **persists** on Hanson–Sigman & V-Dem composites | 001 `scorecard.csv` / findings | most durable determinant, reconfirmed on composites |
| R-war on capacity | persists between / weakens within (001, X1) | **weakens** on both composites | 001 findings.md | composites weight bureaucracy/info capacity |
| Trade-tax > 40% count, 2010 | 7 | 15 | DP16256 Fig 7 (printed) | vintage mismatch → direction-only grade |
| Trade-tax > 40% count, 2023 | — (not in DP16256) | 6 | — | new; below DP16256's 2010 level of 7 |

## Deviations & limitations

- **`mcollective16` graded `not separable (coverage)`** — the authors' 2021 index covers 67
  countries (merged N = 63 with X0 + legal origins), below 001's N ≥ 80 floor. Pre-declared
  in spec II.1(2); reported descriptively with N stated on every surface. No substitution.
- **Q3 vintage mismatch** — reproduce-then-extend rule triggered (2010: 15 vs 7); the 2023
  count is graded direction-only, not as a level. This is a pre-named outcome, not a failure.
- **Data ends / era edges** — E0 tax from 1980 (GRD starts 1980); GFDD credit ends 2021;
  Hanson–Sigman ends 2015. Era boundaries 2000/2012 are `[SPEC-CHOICE]`.
- **Branch R** — deposit pending; suspect cells carry `pending-deposit`; this study adjudicates
  no printed typo and uses no suspect-cell star as evidence.
- **Reused 001 outputs as the baseline side of every comparison**, read from disk
  (`001-001-living-update/results/…`), not re-derived.
- These are conditional cross-country correlations, exactly as the paper labels its evidence
  (pp. 1235, 1241); nothing here is causal.

Full narrative with every cell and the fixed binding sentences: `results/findings.md`.
