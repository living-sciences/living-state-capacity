# Recency research — Besley & Persson (2009), "The Origins of State Capacity" (AER 99(4))

Phase 2a note, written 2026-11-05. Every data endpoint below was verified live on
2026-11-05 (hashes in `extension-assets/PROVENANCE.md` and `extension-assets/sha256sums.txt`);
every "the paper says X" cites the staged AER version (`paper.pdf`, publisher typeset) by
table/page, re-read directly for this note.

## 1. Phase-1 state (binding context for the spec)

**The replication has NOT run yet.** It waits on the openICPSR 113314 human gate (AER.dta,
37 KB) or launches on the open-reconstruction branch (briefing §5). Consequences:

- This spec anchors on the PAPER's printed values (verified from `paper.pdf` pp. 1237–1238
  for this note), not on replication outputs.
- The printed tables contain star/SE inconsistencies the briefing mandates adjudicating.
  Re-verified here from the page text: Table 1 col 1 democracy 0.953 (0.059) with no stars
  (p. 1237; WP prints 0.102 (0.079), so ~0.095 is the likely true cell); Table 2 col 3
  German legal origin 0.171* (0.010) and col 4 German 0.010*** (0.083) — a coefficient/SE
  shift across those two cells is the simplest reading; Table 2 col 2 Scandinavian 0.068**
  (0.084) (t ≈ 0.8 cannot be **); Table 2 col 4 Socialist −0.119 (0.031) with no stars
  (t ≈ 3.8); fn 17 (p. 1236) states war-incidence mean 0.03, sd 0.73 — impossible for a
  [0,1] share with that mean (max sd ≈ 0.17; 0.073 is the likely true value).
- The spec therefore carries TWO launch branches (deposit-based or reconstruction-based
  Phase 1), and its comparison anchors are defined per-branch: where Phase 1 evidences a
  printed cell as a typo from the deposit, the extension grades against the deposit
  re-estimate; on the reconstruction branch the suspect cells are compared qualitatively
  and tagged `pending-deposit`.

## 2. The current world, 2009 → 2026

### 2a. The authors' own successor work (the baseline to beat)

- **Besley & Persson, *Pillars of Prosperity* (Princeton UP, 2011)** expanded the AER
  empirics into a book; the book dataset (`Pillars.dta`, 45,540 country-years, 65 vars)
  is openly posted on the STICERD book site with chapter do-files — **staged**.
- **Besley, Dann & Persson, "Pillars of Prosperity: A Ten-Year Update" (CEPR DP16256,
  June 2021)** — **a lawful copy is staged and was read in full** (obtained from the
  Wayback snapshot of CEPR's public RePEc distribution copy; the live CEPR endpoints
  Cloudflare-block scripts). What it does, precisely:
  - Rebuilds the BOOK's charts and tables on a cross-section "ten years later" —
    anchored on **2010** outcomes (Figures 1–3 right panels: ICTD tax data and the Fraser
    Institute "legal quality" index for 2010, vs the book's ~2000 cross-section).
  - Adds **collective capacity** (avg. of Barro-Lee educational attainment + WDI life
    expectancy) as a third capacity dimension; adds norms/values variables; runs
    unsupervised clustering ("state spaces", 1990/2000/2016).
  - Headline empirical updates: the legal–fiscal capacity correlation "still holds up"
    in 2010 data (DP16256 §2, Figs. 1–3); fiscal capacity rose globally — countries with
    trade-tax revenue share > 40% fell from ~20 in 1999/2000 to 7 in 2010 (§4, Fig. 7);
    civil-war prevalence stopped declining and leveled near 10% in the 2010s, and
    repression (CNTS purges) rose sharply after 2006 (§5, Fig. 9, Tables 1–2).
  - **Its dataset (`Pillars 2.dta`, 48,421 × 156, panel to 2016, with codebook and all
    do-files) is openly posted on STICERD — staged.** Key inherited variables verified:
    `parl_dem` (polity2>0 ∧ Bjørnskov–Rode parliamentary, 1800–2016), the five legal-origin
    dummies, `avg_war00` (external-war incidence 1816–2000, COW, kept from the book),
    ICTD tax structure 1980–2016, `mgadp97` (the ICRG/Hall–Jones GADP aggregate, openly
    redistributed by the authors), DB-2016-vintage credit/property ranks.
  - What it does NOT do (the novelty seam, §4 below): it never re-estimates the AER
    2009 Tables 1–2 regressions (war 1816–1975 + democracy/parliamentary incidence +
    legal origins on the four-plus-four outcome battery); its cross-section stops at
    2010 (panel at 2016); it predates Polity's termination, Doing Business's cancellation,
    the full autocratization wave, COVID fiscal shocks, and every interstate war of the
    2020s. Its own closing question (§4): whether COVID acted "like a positive shock to
    common interests … in analogy to the threats of external war" — asked, not answered.
- Related authors' companions (context, not graded): Besley & Persson JEEA 2008 ("Wars
  and State Capacity"), EMA 2010 ("State Capacity, Conflict, and Development"),
  Besley & Dray (EJ 2024, trust and state effectiveness).

### 2b. Successor measurement (what did not exist in 2007)

- **Hanson & Sigman, "Leviathan's Latent Dimensions" (JOP 2021)**: Bayesian latent
  state-capacity index, 177 countries, **1960–2015** (v1). Staged twice over: the OWID
  redistribution (CSV) and the CC0 JOP Dataverse replication package. This is the
  field-standard general-purpose capacity measure the paper's outcome battery predates.
  **Newest-vintage verification (2b judge, independent, 2026-11-05): no v2 exists** —
  the authors' site (websites.umich.edu/~jkhanson/state_capacity.html), the QoG
  datafinder (`lld_capacity`, source-updated 2020-12-10) and OWID's state-capacity-index
  page all carry v1, 1960–2015, as the latest. Recorded here so the next tick's judge
  inherits it.
- **V-Dem v16** (staged, to 2025): `v2xcl_prpty` (property-rights protection),
  `v2x_rule`-family, polyarchy; also the embedded Polity5 (`e_polity2`, ends 2018 — the
  Polity project was discontinued) and LIED (`e_lexical_index`, to 2024).
- **WGI 2026 release** (staged): rule of law 1996–2025, 216 economies — the natural open
  successor to the proprietary ICRG index the paper used in Table 1 col 4 (via Hall–Jones
  GADP). Raw/current ICRG remains PRS-proprietary → honest exclusion, unchanged.
- **ICTD/UNU-WIDER GRD 2025** (staged): tax structure 1980–2023, ~192 countries —
  the successor to the privately-provided Baunsgaard–Keen vintage behind Table 2.
  **Not registration-gated**: direct keyless download verified (the briefing's
  "if gated → human gate" branch is moot).
- **GFDD (Sept 2022, final)** (staged): `di01` private credit by deposit money banks
  (% GDP) 1960–2021 — the same King–Levine construct as Table 1 col 1; WDI
  `FS.AST.PRVT.GD.ZS` (staged, to 2025) available for a declared splice check.
- **Doing Business**: discontinued September 2021 after the data-irregularities scandal —
  itself a material fact about Table 1 cols 2–3's measurement base. The full historical
  archive DB2004–DB2020 is staged (covers both the paper's ~2006/07 vintage and the final
  2020 vintage). B-READY (2024–) is a different instrument and is left out of scope
  (no comparable rank construct; named as a next-tick candidate).
- **Bjørnskov–Rode regime data v7.1** (staged, 1950–2026): the Cheibub-DD successor that
  Pillars 2's own `parl_dem` uses — the parliamentary-classification chain through 2026.
- **UCDP/PRIO ACD v26.1** (staged, 1946–2025) + **COW War Data v4** (staged,
  inter-state to 2007, extra-state to 2006): the war-incidence extension legs.

### 2c. Follow-on literature (prior art on the substance)

- **Cárdenas & Tuzemen (Brookings WP, 2011)**: panel re-examination of the BP
  cross-section claims; finds smaller effects in panel with high persistence. Pre-dates
  the modern data; closest early re-estimation.
- **Gennaioli & Voth (ReStud 2015, "State Capacity and Military Conflict")**: conditions
  the war→capacity (Tilly) channel on the era in which "money matters" for war — the main
  theoretical qualification of the paper's war comparative-static.
- **Acemoglu, García-Jimeno & Robinson (AER 2015)**: network/spatial state-capacity
  estimation (Colombia) — the within-country identification turn the cross-country
  literature took.
- **Johnson & Koyama (Explorations in Economic History 2017)**: survey of state-capacity
  origins; **Muñoz-Sobrado, Piolatto, Zerbini & Braccioli (BSE WP 1432, rev. 2024,
  staged)**: the current fiscal-capacity survey (conflict, compliance, tax-mix channels).
- **Queralt, *Pawned States* (Princeton UP 2022)**: external war finance through debt
  weakens the war→fiscal-capacity link after ~1816 — directly relevant to whether the
  war coefficient should persist out of sample.
- **Schenoni (ECPR The Loop, 2024; *Bringing War Back In*, CUP)**: applies the Tilly
  frame to Russia–Ukraine; notes Ukraine's foreign-financed war effort sits oddly with
  the classic prediction — the qualitative frontier of exactly our question.
- **Hanson & Sigman (JOP 2021)** doubles as literature and measurement (above);
  O'Reilly & Murphy (2021) and Savoia & Sen offer alternative composite indices (named
  in DP16256 fn 6).
- **Search outcome on direct competitors (2026-11-05, standard + extended passes):** no
  published or working-paper re-estimation of the AER 2009 Tables 1–2 / Figure 1 on
  post-2015 data was found. The DP16256 update is the only re-assembly by anyone, and it
  targets the book's charts on 2010 data. The lane is open.

### 2d. The post-2020 world (why the update is informative now)

Computed from the staged UCDP/PRIO v26.1 (not from memory): interstate + extrasystemic
conflict-years 1976–2025 = 96 across 32 conflicts (~41 participant governments); the
2020s already hold 22 of them — the most conflict-dense decade since the 1980s; at war
intensity (1,000+ battle deaths/yr): Russia–Ukraine 2022–2025 (the first large interstate
war between major states since the paper's sample-frame spirit froze in 1975) and
Iran–Israel 2025. Meanwhile V-Dem/LIED document the autocratization wave and DP16256
itself documents the repression surge after 2006. The paper's three history variables
(war, democracy incidence, parliamentary incidence) and all its outcome windows can now
be observed 20–49 years past the originals, over a world whose institutional drift ran
*against* several of the paper's cross-sectional alignments — the out-of-sample test is
genuinely two-sided.

## 3. Verified data legs (all staged; full table in extension-assets/PROVENANCE.md)

| Leg | Vintage | Coverage verified | Role |
|---|---|---|---|
| GRD 2025 (UNU-WIDER) | 2025 | 1980–2023; 2000–2023 tax/GDP: 4,094 obs / 191 countries; all four Table-2 constructs rebuildable | Table 2 outcomes, rolled window |
| GFDD Sept 2022 | final | `di01` 1960–2021 | Table 1 col 1, rolled window |
| WDI (API, 7 indicators) | live 2026-11-05 | credit to 2025; GC.TAX.* to 2024; GDP pc | splice checks, income split, C4 |
| WGI 2026 release | 2026 | rule of law 1996–2025, 216 economies | Table 1 col 4 successor |
| V-Dem v16 (+LIED/Polity5 extract) | v16 (2026-03) | 1789–2025; e_polity2 to 2018; LIED to 2024; v2xcl_prpty to 2025 | history extension + legal-capacity successor |
| Hanson–Sigman v1 (OWID + CC0 Dataverse) | v1 | 1960–2015, 177 countries | successor-composite reconciliation (002) |
| UCDP/PRIO ACD v26.1 | 2026 | 1946–2025 | war extension 2008–2024/25 |
| COW Inter-/Extra-State War v4 | v4 | 1816–2007 / 1816–2006 | war extension 1976–2007 + paper-source continuity |
| Pillars.dta (2011) + Pillars 2.dta (2021) + codebooks + do-files | authors' own | panel to 2016; parl_dem 1800–2016; legal origins; avg_war00; mgadp97 | succession anchors; DP16256 engagement |
| Bjørnskov–Rode v7.1 | 2026 | 1950–2026 | parliamentary classification chain |
| QoG std CS jan21 | jan 2021 | `lp_legor` (53/76/13/6/5 across origins) | legal-origin dummies (second source besides Pillars 2) |
| DB historical DB04–DB20 | final archive | paper-vintage and final-vintage getting-credit / investor-protection | Table 1 cols 2–3 bridge |
| PWT 11.0 | to 2023 | income per capita | C4 re-run, income split |

Footprint ≈ 174 MB + 16 MB literature (< 1 GB bar). Everything keyless; world-readable.

## 4. Novelty vs the 2021 ten-year update (the judge's §2b question)

The spec adds, beyond DP16256, specifically:

1. **The AER 2009 tables themselves.** DP16256 re-creates the BOOK's charts; nobody —
   including the authors — has re-estimated the AER Tables 1–2 regressions (war
   1816–1975, democracy and parliamentary incidence, legal origins → the 4+4 outcome
   battery) on any later data. Study 001 does exactly that, on windows ending 2021–2025.
2. **Thirteen-plus more years of data.** DP16256's cross-section is 2010 (panel to 2016).
   Our outcome windows run 2000–2024 (GRD to 2023, WGI to 2025, V-Dem to 2025), and the
   history variables extend to 2024 where succession gates pass.
3. **The 2020s out-of-sample world.** DP16256 predates Russia–Ukraine, the COVID fiscal
   shock it explicitly flags as an open question, Polity's death, and DB's cancellation.
   The update's war-decade computation (above) is from data DP16256 could not have had.
4. **Measure succession made explicit.** DP16256 swaps measures silently (ICRG→Fraser,
   B&K→ICTD); our studies run pre-declared succession gates with disclosed,
   preview-calibrated agreement thresholds (the econ4 Democracy pattern), so measurement
   drift is separated from substantive change.
5. **Successor-composite reconciliation (002).** Whether the paper's three history
   variables predict Hanson–Sigman/V-Dem capacity — measures built by the literature the
   paper seeded — has not been computed anywhere we could find.
6. **Extending DP16256's own headline fact.** Their trade-tax fact (>40% share: ~20
   countries in 2000 → 7 in 2010) is recomputed through 2023 on GRD 2025 — a direct,
   citable continuation of the update itself.

## 5. Data seams (binding for the spec)

- **S1 GRD vs Baunsgaard–Keen.** Table 2's original tax vintage is private (in the gated
  deposit). GRD 2025 is a different assembly (resource-tax exclusions, General vs Central
  government). Rule: use the GRD `Merged` sheet, default tax concept per its User Guide,
  compute both General and Central where both exist, and treat level offsets vs the
  paper-era values as vintage drift — graded only on sign/significance patterns, never on
  cell-level equality. The caution-flagged country-years (GRD Caution1–3) run as a
  pre-declared sensitivity.
- **S2 war splice.** COW v4 ends 2007 (inter) / 2006 (extra); UCDP type 1+2 starts 1946.
  The splice is COW-to-2007 + UCDP-2008-onward, with the 1946–2006 overlap agreement
  reported; UCDP's state-participant mapping (gwno codes) differs from COW country-years
  and is reconciled by COW country codes. Contemporaneity: wars after 2000 overlap the
  outcome window — so the headline extended-history column stops war at 2000 (exactly
  `avg_war00` in Pillars 2, the authors' own frozen variable), and war-to-2024 is a
  labeled variant, never the headline (simultaneity caveat pre-declared).
- **S3 parliamentary/democracy succession.** Polity5 ends 2018; Pillars 2's `parl_dem`
  ends 2016. Chain: `parl_dem` → BR∧polity2>0 (to 2018) → BR∧LIED≥4 (to 2024). Previews
  computed at spec time (PREVIEW-CALIBRATED, mandatory labels): BR∧polity2 vs `parl_dem`
  on 1950–2016 overlap: agreement 0.9982, κ 0.9942 (n = 8,355); BR∧LIED≥4: 0.9939,
  κ 0.9802 (n = 8,369); BR alone: 0.9973, κ 0.9912. Democracy: LIED≥4 vs e_polity2>0 on
  1950–2018: agreement 0.9245, κ 0.8493 (n = 9,533).
- **S4 credit splice.** GFDD `di01` ends 2021; WDI private credit runs to 2025 but is a
  broader construct (all financial institutions vs deposit money banks). Primary window
  2000–2021 on `di01`; the WDI-extended window is a sensitivity behind a correlation
  gate (no preview computed; threshold declared as a convention, see spec G4).
- **S5 Doing Business.** Ranks are relative and vintage-specific, and the program died
  for integrity reasons. Cols 2–3 are therefore graded only as (a) paper-vintage
  reproduction (Phase 1's job) and (b) final-vintage (DB2020) direction-of-association —
  with the battery's weight shifted to the col-1/col-4-successor columns. Stated on every
  surface where cols 2–3 appear.
- **S6 ICRG.** Proprietary post-1990s → honest exclusion; WGI rule of law is the primary
  successor (itself partially ICRG-fed — noted as a non-independence caveat), with V-Dem
  `v2xcl_prpty` and Hanson–Sigman as independent successors.
- **S7 scaling.** The paper scales all outcomes to [0,1] (p. 1237 header note). The
  update reproduces that scaling per column and reports standardized coefficients beside
  raw ones so magnitudes are comparable across vintages.

## 6. Power and discrimination (why this can fail)

- Sample: the paper's N = 93–122 (T1) / 103 (T2). The rolled frames carry ~160 (GFDD),
  ~190 (GRD), ~200+ (WGI/V-Dem) countries before history-variable attrition; attrition
  binds at the war/parl variables (~150 post-merge expected) — still larger than the
  originals. No power problem for the *** patterns being tested.
- Discrimination: the war row can genuinely reverse — post-1975 interstate war
  concentrates in poorer, institutionally weaker states (UCDP computation above), the
  opposite of the 1816–1975 European pattern the paper itself flags as the driver
  (fn 20, p. 1236: within-region the correlation weakens). The spec pre-declares the
  within-region (8 regional dummies) variant as a first-class column, so "persists
  between regions only" is a reachable, pre-named outcome.
- The parliamentary-democracy row can fail via the autocratization wave (incidence shares
  move little when a long-democratic country backslides late — the X1 vs X2 contrast
  detects exactly this).
- The complementarity (002) can weaken: post-GFC financial deepening decoupled from tax
  development in several resource and financial-center states; the era-split slope test
  is two-sided by construction.
- All verdict vocabulary is fixed before any outcome regression is run: **no outcome
  regression was run at spec time** — the only previews taken were measurement-agreement
  rates (S3) and coverage counts, and they are labeled PREVIEW-CALIBRATED where they set
  thresholds.

## 7. Human gates

1. **openICPSR 113314** (Phase 0/1 gate, unchanged): unlocks the deposit branch and the
   typo adjudication at exact-vintage fidelity. The extension runs on either branch.
2. **None for the extension.** Every extension leg is staged, keyless, verified. GRD is
   not registration-gated (checked). ICRG stays honestly excluded (never pursue).
3. *(Optional, zero-blocker)* Hanson–Sigman v1 from the author's umich page if a direct
   author copy is ever wanted — Cloudflare-blocked to scripts, trivial for a human; the
   OWID + CC0 Dataverse copies staged here already cover the need.

## 8. Privacy note

No reader question was submitted and no submitter identity exists for this paper. Nothing
in this corpus, the spec, the runs, or the page may imply one. Per the current skill
rules the page carries NO reader sentence.
