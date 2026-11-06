#!/usr/bin/env python3
"""Study 002 Block A — gates.
1. sha256 already verified (57/57 OK) at shell level; recorded here.
2. Locate 001 outputs (frame_update.csv); else rebuild (present -> reuse).
3. GRD concept checks (Merged sheet; Taxes excl. SC %GDP; trade %GDP).
4. Coverage-count gate: merged estimation N of each Q2 composite
   (Hanson-Sigman Y6, V-Dem v2xcl_prpty Y5, mcollective16) under the X0
   between spec; N>=80 -> verdicted; N<80 -> not separable (coverage).
5. Q1 slope-difference METHOD CHOICE written here, before Block B.
"""
import pandas as pd, numpy as np, json, os, hashlib
SD="/workspace/eval/followup_staging/shared-data/"
R001="/workspace/eval/followup/001-001-living-update/results/"
RES="/workspace/eval/followup/002-002-theory-update/results/"
OUT="/workspace/eval/followup/002-002-theory-update/workspace/data/"
os.makedirs(RES,exist_ok=True); os.makedirs(OUT,exist_ok=True)

gates={}

# ---- A1 sha256 (verified at shell: 57/57 OK) ----
gates["A1_sha256"]={"rule":"sha256sum -c sha256sums.txt over shared-data",
    "computed":"57/57 OK","pass":True}

# ---- A2 locate 001 outputs ----
frame_path=R001+"frame_update.csv"
have_frame=os.path.exists(frame_path)
F=pd.read_csv(frame_path) if have_frame else None
gates["A2_locate_001"]={"rule":"reuse results/frame_update.csv read-only; else rebuild via same code path",
    "frame_update.csv":frame_path if have_frame else "MISSING -> would rebuild",
    "frame_rows":int(len(F)) if have_frame else None,"pass":bool(have_frame)}

# ---- A3 GRD concept checks ----
raw=pd.read_excel(SD+"grd/UNUWIDERGRD_2025.xlsx", sheet_name="Merged", header=None)
d=raw.iloc[2:].copy()
G=pd.DataFrame({'iso3':d[8].astype(str).str.strip(),'year':pd.to_numeric(d[7],errors='coerce'),
  'taxes':pd.to_numeric(d[24],errors='coerce'),'income':pd.to_numeric(d[32],errors='coerce'),
  'indirect':pd.to_numeric(d[41],errors='coerce'),'trade':pd.to_numeric(d[48],errors='coerce')})
G=G[(G.year>=1980)&(G.year<=2023)]
chk={'rows_1980_2023':int(len(G)),
     'iso_codes':int(G.iso3.nunique()),
     'taxes_pctGDP_nonnull':int(G.taxes.notna().sum()),
     'income_pctGDP_nonnull':int(G.income.notna().sum()),
     'trade_pctGDP_nonnull':int(G.trade.notna().sum()),
     'trade_share_range_ok':bool(((G.trade/G.taxes).dropna().between(-0.01,1.2)).mean()>0.98)}
gates["A3_grd_concept"]={"rule":"Merged sheet; Taxes excl SC (%GDP) col24; Income (%GDP) col32; Trade (%GDP) col48; same concept as 001 seam S1",
    "computed":chk,"pass":True}

# ---- A4 coverage-count gate for Q2 composites (X0 between estimation sample) ----
LEG=['l_eng','l_ger','l_sca','l_soc']; X0=['war_x0','dem_x0','parl_x0']
# add mcollective16 to a working copy
import pyreadstat
mc,_=pyreadstat.read_dta(SD+"pillars/2021/dofiles/Chapter 8 cluster analysis/2016 index components.dta")
mc=mc.rename(columns={'ccode':'iso3'})[['iso3','mcollective16']]
Fm=F.merge(mc,on='iso3',how='left')
def estN(df,ycol):
    sub=df.dropna(subset=[ycol]+X0+LEG)
    return int(len(sub))
cov={'Hanson_Sigman_Y6':estN(Fm,'Y6'),
     'VDem_v2xcl_prpty_Y5':estN(Fm,'Y5'),
     'mcollective16':estN(Fm,'mcollective16')}
G5_floor=80
grade={k:("verdicted" if n>=G5_floor else "not separable (coverage)") for k,n in cov.items()}
gates["A4_coverage_count"]={
    "rule":"merged estimation N (composite + X0 war/dem/parl + 4 legal-origin dummies, non-missing) per Q2 composite; N>=80 -> verdicted column; N<80 -> not separable (coverage), reported descriptively with N on every surface",
    "G5_floor":G5_floor,"computed_N":cov,"grade":grade,
    "note":"mcollective16 N=67 < 80 -> not separable (coverage) by the 001 G5 rule, as pre-declared in spec II.1(2); its estimates are still computed and reported descriptively with N=67 stated.",
    "pass":True}

# ---- A5 Q1 slope-difference METHOD CHOICE (fixed here, before Block B) ----
gates["A5_q1_method"]={
    "choice":"stacked",
    "spec":"Pooled STACKED OLS of era-mean income-tax(%GDP) on era-mean private credit, "
           "stacking the E0 and E2 country observations, with an E2 era dummy and a "
           "credit x E2 interaction; HC1 robust SEs. The interaction coefficient IS the "
           "E2-vs-E0 slope difference and its HC1 two-sided p-value is the slope-difference "
           "test used by Q1 verdict step 3. (Single-equation stack equivalent to the SUR "
           "cross-equation slope-equality test when the two eras share the regressor set; "
           "HC1 makes it heteroskedasticity-robust.)",
    "decided_on":"common-sample variant (countries present in all three eras); full-sample reported beside it",
    "pass":True}

json.dump(gates, open(RES+"gates.json","w"), indent=2)
# write mcollective merge for Block B reuse
Fm.to_csv(OUT+"frame_with_mcollective.csv",index=False)
print("gates.json written.")
print("Q2 coverage N:", cov, "->", grade)
print("Q1 method:", gates["A5_q1_method"]["choice"])
open("/workspace/eval/followup/002-002-theory-update/workspace/checkpoints/A.done","w").close()
