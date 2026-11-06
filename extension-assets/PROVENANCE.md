# Extension assets — besley-persson-2009-state-capacity (Phase 2a staging)

Staged 2026-11-05 during the recency research for this paper. All downloads keyless; no
logins, no registration walls, no scraping around bot blocks (the two Cloudflare-blocked
pages are documented below with their lawful open routes). Total staged footprint ≈ 174 MB
(`du -sb --apparent-size` = 181,932,066 bytes ≈ 173.5 MiB; +16 MB literature,
16,562,544 bytes). This register describes the FULL staged set the studies ran against;
what ships in this public repository is the license-permitted subset (see the top-level
`LARGE_FILES_OMITTED.md` for everything omitted and how to re-fetch it — the sha256
hashes below and in `sha256sums.txt` verify any re-fetch).

Reuse note: four legs ("econ4 copy" below) are byte-identical copies from an earlier
batch's verified staging of the same sources (the Acemoglu et al. 2019 democracy corpus,
staged and pre-verified 2026-10-14); their original URLs and hashes are restated here and
the hashes were re-verified after copying.

| File | Source URL | Version / coverage (verified) | sha256 | License / access notes |
|---|---|---|---|---|
| `vdem/vdem_v16.RData` | https://raw.githubusercontent.com/vdeminstitute/vdemdata/master/data/vdem.RData (official vdemdata R package, v16 release 2026-03-17) — copied from econ4 staging | V-Dem v16 country-year, 28,092 × 4,618, 1789–2025. Includes `e_polity2`/`e_p_polity` (Polity5 copy, to 2018), `e_lexical_index` (LIED, to 2024), `v2x_polyarchy`, `v2xcl_prpty` (property rights, to 2025), `v2x_rule` etc. | `39b412d3…3d95ea` | CC BY-SA 4.0; keyless GitHub copy of the release (v-dem.net form is optional-email) |
| `vdem/codebook_v16.pdf` | https://v-dem.net/documents/70/codebook_v16.pdf (econ4 copy) | v16 | `d3c4130e…4ac8d4` | open |
| `vdem/vdem_v16_extra_lied_uds.csv` | derived in econ4 from the RData (columns: e_lexical_index, e_uds_mean, e_polity2, v2x_partipdem, v2x_delibdem, v2x_egaldem, e_democracy_omitteddata) | **1950–2025/2024/2018 per var — the extract starts at 1950 for all variables; pre-1950 values live in `vdem_v16.RData` only** (corrected 2026-11-05, 2b round 1: the earlier "1789–2024/2018 per var" described the RData, not this extract) | `590b89e6…` | derived |
| `ucdp/ucdp-prio-acd-261-csv.zip` → `UcdpPrioConflict_v26_1.csv` | https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-261-csv.zip (econ4 copy) | UCDP/PRIO ACD v26.1, 1946–**2025**. Verified here: type 1+2 (extrasystemic+interstate) = 272 conflict-years; 1976–2025 = 96 conflict-years over 32 conflicts; war-intensity (1,000+ deaths/yr) 2014–2025 incl. Russia–Ukraine 2022–2025 and Iran–Israel 2025 | zip `5f951743…`, csv `2aea044f…` | CC BY 4.0, keyless |
| `ucdp/ucdp-prio-acd-261.pdf` | https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-261.pdf | codebook v26.1 | `6d757183…` | open |
| `cow/Inter-StateWarData_v4.0.csv` | https://correlatesofwar.org/wp-content/uploads/Inter-StateWarData_v4.0.csv | COW Inter-State War v4.0, 337 rows / 95 wars, 1823–2003 (participant spells; dataset frame 1816–2007). Verified 2026-11-05 | `2535e30b…` | COW terms (free academic use), keyless |
| `cow/Extra-StateWarData_v4.0.csv` | https://correlatesofwar.org/wp-content/uploads/Extra-StateWarData_v4.0.csv | COW Extra-State War v4.0, 198 rows / 163 wars, 1816–2006 | `529c325f…` | same |
| `grd/UNUWIDERGRD_2025.xlsx` | https://www.wider.unu.edu/sites/default/files/Data/UNUWIDERGRD_2025.xlsx (direct file; the old GRD landing page moved but the Data path serves 200, verified 2026-11-05) | UNU-WIDER Government Revenue Dataset **2025**, sheet `Merged`: 8,605 rows, 1980–**2023**, 196 ISO codes. Verified 2000–2023: Taxes (%GDP) 4,094 obs/191 countries; income-tax leg 3,821/189; trade-tax 3,866/190; indirect 4,022/192 | `59a146f4…` | **NOT registration-gated** — direct keyless download; CC-style academic license per User Guide. (The briefing's "if registration-gated" branch is moot.) |
| `grd/User_Guide_2025.pdf` | https://www.wider.unu.edu/sites/default/files/Data/User_Guide_2025.pdf | GRD 2025 guide | `59ae449c…` | open |
| `gfdd/GFDD_sept2022.xlsx` | https://thedocs.worldbank.org/en/doc/5882f2b2117b882d58a78f9c64ea3613-0050062022/original/20220909-global-financial-development-database.xlsx | World Bank GFDD, September 2022 release (final to date); `di01` = private credit by deposit money banks (% GDP), verified 1960–**2021**, 8,594 obs | `bb86ad8c…` | CC BY 4.0, keyless |
| `wgi/wgidataset_with_sourcedata-2026.xlsx` | https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2026.xlsx (linked from govindicators.org) | WGI **2026 release**; rule-of-law sheet `rl` verified 1996–**2025**, 216 economies | `67c38d2e…` | CC BY 4.0, keyless |
| `hanson-sigman/owid_state_capacity_index.csv` + `.metadata.json` | https://ourworldindata.org/grapher/state-capacity-index.csv?v=1&csvType=full&useColumnShortNames=true | Hanson–Sigman State Capacity Dataset v1 as redistributed by OWID; 8,917 rows, 1960–**2015** | csv `ab6f3696…`, json `3d9d4858…` | OWID CC BY; underlying dataset citation Hanson & Sigman (JOP 2021, doi:10.1086/715066). Author's umich page is Cloudflare-blocked to scripts (a human browser can fetch v1 directly; not needed — OWID + Dataverse cover it) |
| `hanson-sigman/HansonSigman_source.dta`, `cross-sectional-table5.dta` | https://dataverse.harvard.edu/api/access/datafile/4103950 and /4103946 (`?format=original`; doi:10.7910/DVN/IFZXQX, JOP Dataverse) | JOP replication package V1 (2020-12-10) | `072a823f…`, `4772f4e9…` | **CC0 1.0**, keyless API |
| `legal-origins/qog_std_cs_jan21.csv` | https://www.qogdata.pol.gu.se/data/qog_std_cs_jan21.csv | QoG Standard cross-section, Jan 2021 (the last vintage carrying `lp_legor`, La Porta et al. legal origin: 53 English / 76 French / 13 Socialist / 6 German / 5 Scandinavian; the Jan 2025 vintage dropped the lp_ block — probed 2026-11-05) | `5348dab8…` | QoG free use with citation |
| `pillars/2011/{Pillars.zip→Pillars.dta, codebook.pdf, do-files.zip→dofiles/}` | https://sticerd.lse.ac.uk/textonly/_STICERD/publications/BOOKS/Pillars-of-Prosperity/data/2011/ | The authors' 2011 book dataset: 45,540 × 65 country-year panel | dta `9b543911…` | posted openly by the authors (STICERD book site), keyless |
| `pillars/2021/{Pillars_2_dta.zip→"Pillars 2.dta", pillars_2_codebook.pdf, do-files.zip→dofiles/}` | https://sticerd.lse.ac.uk/textonly/_STICERD/publications/BOOKS/Pillars-of-Prosperity/data/2021/ | **The ten-year-update dataset (Besley–Dann–Persson 2021)**: 48,421 × 156, 1789–**2016**. Verified: `parl_dem` (polity2>0 ∧ Bjørnskov–Rode parliamentary) 1800–2016; `l_eng/l_soc/l_sca/l_ger/l_fre` legal-origin dummies; `avg_war00` (share of years in external war 1816–2000, COW, kept from the book); ICTD tax vars 1980–2016; `mgadp97` (the Hall–Jones ICRG GADP aggregate, openly redistributed here by the authors); Doing Business 2016-vintage `mcredit16`/`mproperty16`; Fraser `fi_legprop_pd` | dta `3af97bd9…` | posted openly by the authors, keyless. The .do files reproduce every chart/table of DP16256 |
| `bjornskov-rode/Bjornskov-Rode-integrated-dataset-v7.1.xlsx` | http://www.christianbjoernskov.com/wp-content/uploads/2026/08/Bjornskov-Rode-integrated-dataset-v7.1.xlsx | Bjørnskov–Rode regime data v7.1 (2026), 16,016 rows, 1950–**2026**; `DD regime`=0 is parliamentary democracy (Cheibub-DD successor — the same source Pillars 2's `parl_dem` uses) | `d82d63b3…` | posted openly by the authors, free academic use with citation |
| `doingbusiness/Historical-Data--DB04-DB20-.xlsx` | https://archive.doingbusiness.org/content/dam/doingBusiness/excel/db-2021/Historical-Data--DB04-DB20-.xlsx | World Bank Doing Business historical archive, DB2004–DB2020 vintages (program discontinued Sept 2021) — covers BOTH the paper's ~DB2006/07 vintage and the final DB2020 vintage for getting-credit / protecting-minority-investors | `95bce841…` | World Bank archive, keyless |
| `wdi/wdi_<IND>.json` (7 files) | https://api.worldbank.org/v2/country/all/indicator/<IND>?format=json&per_page=20000&date=1972:2025 (pulled 2026-11-05; NY.GDP.PCAP.KD copied from econ4, same API) | GC.TAX.TOTL.GD.ZS, GC.TAX.YPKG.RV.ZS, GC.TAX.INTT.RV.ZS, GC.TAX.GSRV.RV.ZS all 1972–**2024**; FS.AST.PRVT.GD.ZS 1972–**2025**; NY.GDP.PCAP.PP.KD 1990–2025; NY.GDP.PCAP.KD through 2025 | see sha list | CC BY 4.0, keyless API |
| `pwt/pwt110.dta` | https://dataverse.nl (PWT 11.0, econ4 copy; see econ4 provenance) | PWT 11.0, to 2023 | `2a0d2149…` | CC BY 4.0 |
| `../literature/besley-persson-dann-2021-dp16256.pdf` | Wayback Machine snapshot 2023-03-27 of https://repec.cepr.org/repec/cpr/ceprdp/DP16256.pdf (CEPR's own public RePEc distribution copy; the live host now serves Cloudflare challenges to scripts — the snapshot is of CEPR's lawful public posting) | CEPR DP16256, June 2021, 38 pp. | `0f3762f1…` | CEPR DP, author copyright; staged for internal reading, cite as CEPR DP16256 |
| `../literature/munoz-sobrado-etal-2024-fiscal-capacity-review-bse-wp1432.pdf` | https://bse.eu/sites/default/files/working_paper_pdfs/1432.pdf | Muñoz-Sobrado, Piolatto, Zerbini & Braccioli, "Fiscal Capacity", BSE WP 1432 (2024 revision) — current survey of the fiscal-capacity literature | `d471aa81…` | open WP |

## Full sha256 manifest

See `sha256sums.txt` beside this file (generated 2026-11-05; regenerate with
`find . -type f ! -name 'sha256sums.txt' ! -name 'PROVENANCE.md' -exec sha256sum {} \;`).

## Blocked-to-scripts pages (documented, not circumvented)

- openICPSR 113314 (the AER.dta deposit): the standing human gate (Phase 0/1 item, see
  `../package/PROVENANCE.md`). Never automated.
- websites.umich.edu/~jkhanson (Hanson–Sigman v1 direct): Cloudflare; covered by the OWID
  redistribution + the CC0 JOP Dataverse package staged above.
- cepr.org / repec.cepr.org live endpoints: Cloudflare; the DP16256 PDF was obtained from the
  Wayback snapshot of CEPR's public RePEc copy (above).
- systemicpeace.org (Polity5 direct): bot-filtered (econ4 precedent); the Polity5 series is used
  via its V-Dem v16 embedded copy (`e_polity2`, to 2018) — the econ4-validated route.
