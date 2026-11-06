# V-Dem derived data: CC BY-SA 4.0 notice

The files in this repository that embed V-Dem v16 values are **derived from the V-Dem
v16 country-year dataset** (V-Dem Institute, release 2026-03-17) and are distributed
under the same **CC BY-SA 4.0** license (share-alike): if you redistribute or adapt
them, you must attribute V-Dem and license your derivative under CC BY-SA 4.0 as well.

Covered files:

- `extension-assets/vdem/vdem_v16_extra_lied_uds.csv` (column extract from the v16
  release; 1950 onward)
- `followup/001-001-living-update/workspace/data/vdem_core.csv`, `vdem_yearly.csv`,
  `hist_vdem.csv` (the run's own extracts via `extract_vdem.R`)
- V-Dem-derived columns inside the merged frames and results (`history_merged.csv`,
  `frame_update.csv`, and downstream outputs using `e_polity2`, `e_lexical_index`,
  `v2xcl_prpty`)

Cite: Coppedge, Michael, et al. 2026. "V-Dem Country-Year Dataset v16." Varieties of
Democracy (V-Dem) Project. https://www.v-dem.net. The Polity2 series used (`e_polity2`)
is the Polity5 copy embedded in V-Dem; cite Marshall & Gurr (Center for Systemic Peace)
for it as well. The full `vdem_v16.RData` (34 MB) is not shipped here; see
`LARGE_FILES_OMITTED.md` for the URL and sha256.
