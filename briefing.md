# Briefing: Besley & Persson (2009), "The Origins of State Capacity: Property Rights, Taxation, and Politics"

Prepared 2026-11-05 (Phase 0, econ7 batch). Corpus: `econ7_papers/corpus/besley-persson-2009-state-capacity/`.

## 0. Feasibility assessment first, because this paper is unusual for the program

**This is primarily a theory paper.** Sections I–III (about 18 of its 27 pages) build a two-period model of investments in legal capacity (contract/property-rights enforcement, parameter π) and fiscal capacity (the enforceable tax rate, parameter τ) and derive eight propositions; the headline contribution is the complementarity result (legal and fiscal capacity are typically complements) and the comparative statics (external war, political stability, and inclusive institutions build state capacity). The empirical content is one section (IV, "A Look at the Data"): **one scatter figure and two cross-country OLS tables of 93–122 countries**, which the authors themselves repeatedly label "conditional correlations", "preliminary", and explicitly *not* causal. There is no econometric identification strategy to stress-test, no panel, no IV.

Consequences for the pipeline:

- The replication target list is short and computationally trivial (minutes of CPU). The scientific weight of the replication sits in data reconstruction and in adjudicating several apparent typesetting errors in the published tables (see C2/C3 notes — a genuinely interesting deliverable).
- The analytical propositions are not replication claims. They can be spot-verified symbolically if the Phase 1 agent wants (the Appendix derivations are self-contained), but they should be listed as out of scope for scoring, the way proofs were handled in earlier batches.
- The living-update surface is unusually rich for a 2007/2009 paper: the empirics are a cross-section frozen at "history up to 1975 → outcomes 1975–2000s", and seventeen more years of outcome data plus a whole successor measurement literature (including the authors' own ten-year update of their 2011 book) now exist. A 2b judge should find the natural update questions informative either way (section 8).
- No extension question was submitted with the nomination (and no submitter identity exists; keep it that way). The recency phase owns the final question; section 8 proposes candidates.

**Tier: A for the empirical section** conditional on one trivial human gate (openICPSR login+click for a 37 KB Stata file), **B without it** (reconstruction from open raw sources, with vintage-drift tolerance). No proprietary blocker: the one ICRG-derived variable ships in the deposit and is openly redistributed in derived form (Hall–Jones GADP).

## 1. Identity

- Timothy Besley (LSE) and Torsten Persson (IIES, Stockholm). **"The Origins of State Capacity: Property Rights, Taxation, and Politics", *American Economic Review* 99(4): 1218–1244, September 2009. doi:10.1257/aer.99.4.1218.** This published version is canonical: it is refereed, it differs materially from the working paper (see below), and the AEA replication deposit matches it.
- Nominated as **NBER WP 13028 (April 2007)** — the URL the reader submitted. Also circulated as CEPR DP 6370. The WP and AER versions differ in the empirics, not just prose: the WP's Tables 1–2 include regional fixed effects (eight regions) and report different coefficients (e.g., war→private credit 0.573 in the WP vs 0.510 in AER col 1; WP N=94/104 vs AER N=93/103); the AER version dropped the regional FE from the main tables and demoted them to a robustness remark (fn 20: the war correlation weakens within region). The AER version also reworks the model exposition and adds the growth-correlates discussion (Section III E).
- Staged `paper.pdf` = publisher-typeset AER version via LSE Research Online (eprints 33768, the authors' institutional repository; legal OA copy with an LSE cover page). sha256 3e6cf54a… The AEA's own PDF is Cloudflare-gated to scripts.
- `supplementary/nber_w13028_2007.pdf` = the nominated WP (sha256 1f38e565…), kept for cross-version comparison.

## 2. Plain-language summary

Economists usually assume the state can enforce contracts and collect taxes; historians treat the emergence of those abilities as the thing to explain. Besley and Persson model a two-period economy where the group in power chooses how much to invest in two kinds of state capacity: legal capacity (institutions that support private contracts and credit markets) and fiscal capacity (institutions that make income taxation enforceable). Because better legal capacity raises incomes and hence what taxes can collect, and fiscal capacity determines who captures the gains, the two investments are typically complements: forces that build one build the other. The model predicts that a history of external war (a common-interest public good that demands revenue), political stability, and more inclusive/representative political institutions all raise investment in both capacities, and that purely redistributive politics depresses them. The empirical section checks these predictions as cross-country correlations: countries that spent more of 1816–1975 in external war, were more often parliamentary democracies up to 1975, and have German or Scandinavian legal origins show deeper credit markets, better property-rights protection, and tax systems that rely on income taxes rather than border taxes. The paper is the seed of the authors' "Pillars of Prosperity" research program (EMA 2010, the 2011 Princeton book, and a 2021 ten-year data update).

## 3. Main claims (replication targets)

All from the AER version. Outcome variables are scaled to [0,1]; cross-section OLS with robust SEs; French legal origin is the excluded legal-origin category; no regional FE in the published tables. All numbers below were read from page renders of the published PDF (pages 1237–1238), not from text extraction alone.

| ID | Claim | Key numbers | Home |
|---|---|---|---|
| C1 | Legal and fiscal capacity are positively correlated across countries (the complementarity's observable footprint): income-tax share of GDP rises with private credit to GDP, within both richer and poorer halves of the sample | Scatter + fitted line, positive slope; split above/below median income. No printed coefficient — replicate as the figure plus the slope/correlation | Figure 1, p.1220 |
| C2 (headline, legal capacity) | War incidence 1816–1975 and German/Scandinavian legal origin predict legal capacity; parliamentary democracy predicts the Doing-Business and ICRG measures | War: 0.510*** (0.143) private credit; 0.647** (0.191) access to credit; 0.029 (0.209) investor protection (n.s.); 0.576*** (0.170) ICRG anti-diversion. Parl. democracy: 0.001 / 0.145 / 0.339** / 0.112*. German LO: 0.406*** / 0.295*** / −0.008 / 0.248***. Scand. LO: 0.112*** / 0.204*** / 0.087 / 0.254***. N = 93 / 122 / 120 / 115; R² 0.524 / 0.334 / 0.256 / 0.596 | Table 1, p.1237 |
| C3 (headline, fiscal capacity) | War incidence predicts all four fiscal-capacity measures; parliamentary democracy predicts the income-tax and total-tax shares | War: 0.762*** (0.250) one-minus-trade-tax share; 0.598*** (0.241) one-minus-trade+indirect; 0.579*** (0.220) income tax/GDP; 0.555*** (0.162) tax/GDP. Parl. democracy: 0.031 / 0.122 / 0.212*** / 0.160**. German LO: 0.175*** / 0.196*** / 0.171* / 0.010***(sic). Scand. LO: 0.189** / 0.068** / 0.258** / 0.292***. N = 103 all; R² 0.356 / 0.305 / 0.600 / 0.576 | Table 2, p.1238 |
| C4 | The same regressions with income per capita as the dependent variable give "very similar patterns of sign and significance" | No printed numbers; qualitative claim | Section IV D, p.1239 |
| C5 | Data-construction facts | War = share of years 1816 (or independence)–1975 with interstatewar or extrastatewar = 1 (COW); stated mean 0.03, sd 0.73 (fn 17 — flag: sd ≫ mean is odd for a [0,1] share, verify against the data). Democracy = share of years 1800–1975 with polity2 > 0. Outcomes averaged from 1975 onward (credit, taxes) or early-1980s–late-1990s (ICRG) | Section IV A, fns 17–24 |

**Printed-value anomalies the replication must adjudicate (do not grade these as replication failures without checking):** the published Table 1 col 1 shows democracy = 0.953 (0.059) with *no* stars — a coefficient 16× its SE cannot be insignificant, and the WP prints 0.102 (0.079), so 0.953 is almost certainly a typo for ~0.095; Table 1 col 4 Socialist LO 0.010*** (0.035) and Table 2 col 4 German LO 0.010*** (0.083) carry stars that are incompatible with their SEs (and Table 2 col 4 Socialist −0.119 (0.031) lacks stars it should have — the stars look shifted by one row between those cells). The deposit's AER.dta re-estimation is the authority here; resolving which printed cells are typos is a legitimate headline finding. The verification approach for C2/C3 is therefore: reproduce every cell from AER.dta, match to the printed values, and classify each mismatch as (replication divergence | printed typo evidenced by SE/star inconsistency + WP cross-check).

Verification approach per claim: C1–C3 exact re-estimation from the deposit (or reconstruction, section 5) in Python/R, robust (HC1) SEs; C4 re-run with income per capita (from the deposit if present, else PWT/WDI, documented); C5 descriptive checks against the constructed variables. Nothing stochastic — point grading throughout, no band_source rules needed.

## 4. Asset inventory (all accessed 2026-11-05)

| Asset | Status | Location / URL |
|---|---|---|
| Published AER article (publisher typeset, via LSE Research Online) | **STAGED as `paper.pdf`**, sha256 3e6cf54a… | https://researchonline.lse.ac.uk/id/eprint/33768/1/The_origins_of_state_capacity_property_rights%2C_taxation%2C_and_politics%28lsero%29.pdf ; canonical https://doi.org/10.1257/aer.99.4.1218 |
| NBER WP 13028 (April 2007; the nominated version) | STAGED `supplementary/nber_w13028_2007.pdf`, sha256 1f38e565… | https://www.nber.org/system/files/working_papers/w13028/w13028.pdf |
| **Official replication deposit** (AEA legacy archive, migrated 2019): `AER.dta` (36.9 KB) + ReadMe PDF + LICENSE.txt, V1 | **NOT staged — openICPSR HUMAN GATE** (login + click-through ToS; page 403s to scripts). Unlock procedure in `package/PROVENANCE.md`; ~2 minutes of human time | https://doi.org/10.3886/E113314V1 (project 113314) |
| Legacy aeaweb.org data-archive zip | gone (404, probed 2026-11-05) | — |
| AEA article page (confirms the deposit link) | provenance reference | https://www.aeaweb.org/articles?id=10.1257/aer.99.4.1218 |
| Raw-source reconstruction table (COW, Polity, La Porta LO, Financial Structure DB, Doing Business archive, Hall–Jones GADP, Baunsgaard–Keen/ICTD) | documented, not yet pulled (Phase 1 pulls on demand; all small) | `package/PROVENANCE.md` |

Staged footprint: < 1 MB. Nothing over 1 GB was pulled or is anticipated; no BATCH.md size log entries needed. Everything chmod a+rX.

## 5. Gating and data classification (per source)

- **openICPSR 113314 — registration/human gate (the only gate on the replication).** Free account + ToS click. This is the exact-vintage assembled dataset; unlocking it turns the whole empirical section into Tier A. Never automate.
- **Open:** COW war data; Polity IV/Polity5 annual files; La Porta et al. legal origins; Beck–Demirgüç-Kunt–Levine Financial Structure Database (open substitute for the Favara-provided private-credit series); World Bank Doing Business historical archive (program discontinued 2021; the 2006/07-vintage ranks need an archived snapshot — open but vintage-matching work).
- **Proprietary origin, openly redistributed as used:** the ICRG "government anti-diversion policies" average is the Hall–Jones (1999) GADP aggregate, redistributed with their replication data and inside AER.dta. Raw/current ICRG is PRS-proprietary → **honest exclusion for any extension wanting post-1990s ICRG**; substitutes are WGI rule-of-law and V-Dem indices (open).
- **Privately provided to the authors, with open successors:** the Baunsgaard–Keen IMF tax-structure panel (Mick Keen). Exact vintage only in AER.dta; open routes are the B&K (2010 JPubE) supplement and, for extensions, the ICTD/UNU-WIDER Government Revenue Dataset.
- If the human gate is declined: Tier B reconstruction from the open sources above, with documented vintage drift as an approved substitution in `operator_notes.md` — the correlational claims are coarse enough (robust *** patterns) that sign/significance replication should survive reasonable drift, but exact cells will not match.

## 6. Environment fit

- No code ships (data-only deposit expected); the original analysis was evidently Stata (AER.dta), but everything is plain OLS + robust SEs on ≤122 observations: `pandas.read_stata` + statsmodels (HC1), or R `fixest`/`estimatr`. The container (Python 3.12, R 4.x, no Stata) is more than sufficient; this follows the usual Stata→Python/R lane with trivial porting risk.
- Compute: seconds. No GPU, negligible RAM/disk. Figure 1 is a two-group scatter with a fitted line — matplotlib.
- Anti-cheating posture: the deposit is data+readme, so there are no author result files to gate. The printed tables live in paper.pdf as always.

## 7. Feasibility tier: **A** (conditional on the openICPSR click; B otherwise)

The empirical section is small, deterministic, and fully covered by a 37 KB archived dataset behind a two-minute human gate; the interesting work is adjudicating the printed-table anomalies and documenting vintages. The main risk is not feasibility but *thinness* — mitigated by the extension surface below, which is where this living paper earns its keep.

## 8. Extension landscape (sketch; the recency phase owns the final question — none was submitted with the nomination)

What makes this paper natural living-paper material despite its preliminary empirics: its measurement frontier is frozen in ~2007 (outcomes averaged to the early 2000s, Doing Business since discontinued, Polity IV since abandoned, ICRG unchanged-proprietary), while the state-capacity literature it seeded built exactly the datasets needed to re-ask its questions today.

1. **The authors' own successor work defines the baseline to beat.** Besley & Persson, *Pillars of Prosperity* (Princeton, 2011; book dataset openly hosted by CSAE Oxford) expanded these empirics; **Besley, Dann & Persson, "Pillars of Prosperity: A Ten-Year Update" (CEPR DP16256, June 2021)** re-assembled the data and "recreated almost all charts and tables with better data for a cross-section ten years later". The living update must go beyond DP16256: (a) another 5+ years of data (to ~2023–25 vintages), and (b) the AER 2009 tables specifically, which the update treats only via the book's versions. The DP16256 PDF is member-gated at CEPR (a free LSE/STICERD copy likely exists; a human can fetch it if scripts fail — minor gate).
2. **Natural living-update question (proposed for the 2b judge):** *do the 2009 cross-sectional patterns hold when the outcome windows are rolled forward ~20 years and the discontinued/proprietary measures are replaced by their modern successors?* Concretely: re-estimate Tables 1–2 with outcomes averaged over 2000–2024 (GFDD private credit; WGI rule-of-law / V-Dem `v2xcl_prpty`-family in place of ICRG; ICTD/UNU-WIDER GRD tax structure in place of Baunsgaard–Keen; B-READY or archived-DB-final-vintage in place of Doing Business), and with the history variables extended (war incidence through 2007/2014 via COW v5 or UCDP/PRIO through 2024; democracy/parliamentary incidence via V-Dem v15/16, since Polity5 ends in 2018). Informative either way: the war→state-capacity correlation is the paper's most distinctive prediction, and the post-1990s world (few interstate wars, post-Soviet state-building, the 2010s autocratization wave, resource-state divergence) is a genuine out-of-sample test the 2007 authors could not run.
3. **New outcome measures that did not exist in 2007:** Hanson & Sigman's latent state-capacity index (JOP 2021, open, long panel), V-Dem fiscal/administrative capacity proxies, UNU-WIDER GRD. A tidy extension column: do war history, parliamentary incidence, and legal origins predict the *modern composite* capacity measures?
4. **Theory-update candidate:** the model's complementarity prediction (legal and fiscal capacity move together) as a fitted relationship by era — has the legal–fiscal capacity correlation (Figure 1) strengthened, weakened, or rotated between the 1975–2000 and 2000–2024 windows, and does a simple two-capacity investment model calibrated by era rationalize the change? Follow-on literature to engage: Besley & Persson EMA 2010 and QJE 2009–2011 companions; Gennaioli & Voth (ReStud 2015) on war and state capacity (which conditions the Tilly effect on the money-matters era); Dincecco; Johnson & Koyama's 2017 survey; Hanson–Sigman.
5. **Data for all of this is open** (V-Dem, UCDP, COW, WGI, GRD, GFDD, Hanson–Sigman, CSAE book data). The only closed door is current ICRG (honest exclusion; substitutes named above).

## 9. Human-gated items (action list)

1. **openICPSR 113314** — log in, click "Download This Project", accept terms, drop the zip at `corpus/besley-persson-2009-state-capacity/package/openicpsr-113314.zip`. ~2 minutes. This is the one gate that matters for Phase 1.
2. *(Optional, Phase 2a)* CEPR DP16256 PDF if no free STICERD/LSE copy surfaces to scripts.
3. *(Not requested)* Raw ICRG would need a PRS license — do not pursue; honest exclusion with WGI/V-Dem substitutes.

## 10. Hand-off notes for Phase 1

- Replication target list: C1–C5; headline cells are Table 1 cols 1–2–4 (war row) and Table 2 all columns (war row), plus the parliamentary-democracy rows.
- Treat the printed-table anomalies (section 3) as an adjudication task: every cell gets (matched | divergent | printed-typo-with-evidence). Cross-check suspect cells against the WP tables in `supplementary/`.
- Record vintages for every source actually used; if reconstruction (no deposit) is the route, write the substitutions into `operator_notes.md` so they grade as approved substitutions, not method-fidelity anomalies.
- The theory sections are out of scoring scope; say so in the claims file notes so the planner does not manufacture pseudo-claims from propositions.
