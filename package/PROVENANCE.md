# Package provenance — besley-persson-2009-state-capacity

Status as of 2026-11-05: **the official replication deposit is identified but NOT staged — it sits behind the openICPSR human gate.** Nothing in this directory is author package material yet.

## The official deposit (HUMAN GATE)

- Besley & Persson, "Replication data for: The Origins of State Capacity: Property Rights, Taxation, and Politics", openICPSR project 113314, doi:10.3886/E113314V1 (V1, last modified Oct 2019 — the AEA's bulk migration of the legacy AER data archive).
- URL: https://www.openicpsr.org/openicpsr/project/113314/version/V1/view (confirmed live 2026-11-05; the page serves 403 to scripted fetches, per the standing openICPSR rule).
- Contents per the project listing (seen via search metadata 2026-11-05): `AER.dta` (Stata, 36.9 KB), a ReadMe PDF, `LICENSE.txt`. **Data-only, no do-files expected** — standard for 2009-era AER deposits; the regressions are plain cross-section OLS and are re-coded from the paper text.
- **Unlock procedure (human, ~2 minutes):** log in to openICPSR (any free ICPSR account), open the project page, click "Download This Project", accept the click-through terms, and drop the zip here as `package/openicpsr-113314.zip`. Never scripted — openICPSR blocks automation and the ToS click is the license act.

## Legacy AEA archive

The pre-migration zip URLs under `aeaweb.org/aer/data/` 404 (probed 2026-11-05); the openICPSR deposit is the only official copy.

## Underlying raw sources (for reconstruction or extension; none staged yet — Phase 1/2a pulls what it needs)

| Variable (paper) | Source | Access class |
|---|---|---|
| Incidence of external conflict 1816–1975 | Correlates of War (inter-state + extra-state war lists), correlatesofwar.org | open |
| Incidence of democracy / parliamentary democracy 1800–1975 | Polity IV `polity2` (Center for Systemic Peace) + a parliamentary-regime classification (readme will name it; likely DPI/Persson-Tabellini style) | open |
| Legal origin dummies | La Porta, Lopez-de-Silanes, Shleifer, Vishny (1998) | open (Shleifer site/Dataverse) |
| Private credit to GDP, avg 1975+ (Table 1 col 1) | provided by Giovanni Favara; open equivalent = Beck–Demirgüç-Kunt–Levine Financial Structure Database / WB Global Financial Development Database | open equivalent |
| Ease of access to credit, investor protection ranks (Table 1 cols 2–3) | World Bank Doing Business, ~2006/07 vintage | open but **discontinued** (DB killed 2021; historical snapshots archived — vintage matching needed) |
| Index of government anti-diversion policies, avg early-1980s–late-1990s (Table 1 col 4) | ICRG (PRS Group) via the Hall–Jones (1999) GADP aggregate | **raw ICRG proprietary**; the GADP average as used is openly redistributed with the Hall–Jones replication data (Chad Jones's site — verify in Phase 1) and ships inside AER.dta |
| Tax structure: trade/indirect/income tax shares, tax/GDP, avg 1975+ (Table 2) | IMF GFS-based dataset of Baunsgaard & Keen (2005 IMF WP; 2010 JPubE), provided privately by Mick Keen | the exact vintage lives in AER.dta (gated deposit); B&K's JPubE 2010 supplement and the ICTD/UNU-WIDER GRD are the open routes |

Classification summary: **no honest-exclusion blocker for the replication** — everything needed sits in the 37 KB AER.dta behind a one-click human gate, and the one proprietary-origin variable (ICRG GADP) is in the deposit and openly redistributed in derived form. Raw ICRG remains proprietary for any extension that wants post-2000 ICRG values (substitute: WGI rule of law / V-Dem, both open).
