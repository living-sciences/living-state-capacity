# Corrective study: 003-corrections — audit conformance fixes for 001 and 002

The provenance audit passed both studies (every spot-recomputed statistic exact; reforms,
privacy, honesty clean) with twelve bounded corrections. This study applies exactly those
and nothing else. No verdict word changes. Record every old → new change in this study's
`results/card_corrections.csv` (file, item, old, new, reason).

Framing rules (binding): nothing upgraded; a code fix whose corrected value changes a
printed number ships the TRUE value with a one-line erratum; the WP cross-check fills
from the real PDF, never from memory.

## Corrections — study 001 (`followup/001-001-living-update/`)

1. **001-C1.** The WP is NOW staged at `shared-data/nber_w13028_2007.pdf` (orchestrator
   backfill). Fill the typo table's WP cross-check column by reading the WP's Tables 1-2
   from the PDF itself; replace "not staged" wording with the filled values. Where the WP
   agrees with the merited stars, say so; where it differs, record it — evidence, not
   adjudication (that stays pending-deposit).
2. **001-C2.** Fix `results/anchors_printed.json`: correct the misattributed printed war
   cells (T1c3/T1c4; T2 c1-c4 order), fill the placeholder SEs, tag the two suspect-set
   cells pending-deposit. Verify against the staged AER PDF.
3. **001-C3.** Restore the full fixed identification sentence on the 001 card (note 5
   currently truncates at "nothing here is causal.").
4. **001-C4.** Headline-order conformance: carry "X0 between: weakens (3/8),
   reconstruction-degraded (corr 0.61)" inside the headline sentence (findings + card),
   per the I.5 template, keeping X1 as the designated headline estimate.
5. **001-C5.** followup_summary.json: "T2 0.555**-0.762***" → "0.555***-0.762***".
6. **001-C6.** Add one line to findings.md naming the pre-1950 read route (R load() →
   extract_vdem.R) and the A4 assertion result (e_polity2 populated to 1789).
7. **001-C7.** Implement the R-legor pooled attenuation arm in the verdict code (run it;
   the audit verified it is non-binding on this data — confirm and state so).
8. **001-C8.** Add the "descriptive (contemporaneous-war caveat)" string as a column on
   the X2 rows of table1_update.csv / table2_update.csv.

## Corrections — study 002 (`followup/002-002-theory-update/`)

9. **002-C1.** Reword report.md's "first era-by-era fit" to absence-framing ("era-by-era
   fit absent from DP16256"); the fixed battery sentence stays the only first-ness claim.
10. **002-C2.** Fix half_label to drop missing-income countries from the half-samples;
    re-run the affected E2 low-half estimate; add the one-line erratum (clean p = 0.0395,
    significant, not 0.074 marginal; verdict unchanged). File the corrected estimates.
11. **002-C3.** Add the [SPEC-CHOICE] era-boundary label beside the era mentions in the
    card metrics (M1's value line).
12. **002-C4.** Add one sentence beside the Q3 direction-only grade noting 2023 GRD
    coverage (116 countries) is thinner than 2000 (169); the counts already ship in
    tradetax_march.csv.

## Where things live

001: `followup/001-001-living-update/`; 002: `followup/002-002-theory-update/`; staged
data read-only at `followup_staging/shared-data/`. Edit files in place.

## Deliverables

report.md (one short section per item incl. the 001-C7 true outcome and 002-C2 erratum);
results/card_corrections.csv; corrected files in place; result_card.json for THIS study
(status completed when all twelve are done).

## Rules

Foreground only; no fetches; no new packages; `--timeout 7200`.