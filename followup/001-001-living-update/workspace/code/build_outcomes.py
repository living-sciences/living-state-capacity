#!/usr/bin/env python3
"""Block C (part 2): build outcome battery Y1-Y10 + bridges Y2/Y3 per ISO3,
rolled to 2000-2024 windows, plus WB regions for V-within."""
import pandas as pd, numpy as np, json, os
SD="/workspace/eval/followup_staging/shared-data/"
OUT="data/"

def winmean(df, iso, yr, val, y0, y1):
    d=df[(df[yr]>=y0)&(df[yr]<=y1)].dropna(subset=[val])
    g=d.groupby(iso)[val]
    return g.mean(), g.size()

Y={}  # dict iso3-> {col:val}
cov={}

# ---- Y1 GFDD di01 (private credit %GDP) 2000-2021 ----
g=pd.read_excel(SD+"gfdd/GFDD_sept2022.xlsx", sheet_name="Data - August 2022")
g=g[['iso3','year','di01','region','income']].copy()
g['di01']=pd.to_numeric(g.di01,errors='coerce')
m,n=winmean(g,'iso3','year','di01',2000,2021)
Y['Y1']=m; cov['Y1_n']=n
regions=g.dropna(subset=['region']).groupby('iso3').region.first()

# ---- Y4 WGI rule of law estimate 2000-2025 ----
w=pd.read_excel(SD+"wgi/wgidataset_with_sourcedata-2026.xlsx", sheet_name="rl")
w=w.rename(columns={'Economy (code)':'iso3','Year':'year',
    'Governance estimate (approx. -2.5 to +2.5)':'rl'})
w['rl']=pd.to_numeric(w.rl,errors='coerce')
m,n=winmean(w[['iso3','year','rl']],'iso3','year','rl',2000,2025)
Y['Y4']=m; cov['Y4_n']=n
wgi_region=w.dropna(subset=['Region']).groupby('iso3').Region.first() if 'Region' in w.columns else None

# ---- Y5 V-Dem v2xcl_prpty (property rights) 2000-2025 ----
vd=pd.read_csv(OUT+"vdem_core.csv", encoding="latin-1")
vd=vd.rename(columns={'country_text_id':'iso3'})
m,n=winmean(vd[['iso3','year','v2xcl_prpty']].dropna(subset=['v2xcl_prpty']),'iso3','year','v2xcl_prpty',2000,2025)
Y['Y5']=m; cov['Y5_n']=n

# ---- Y6 Hanson-Sigman capacity 2000-2015 ----
hs=pd.read_csv(SD+"hanson-sigman/owid_state_capacity_index.csv")
hs=hs.rename(columns={'code':'iso3','capacity':'cap'})
m,n=winmean(hs[['iso3','year','cap']].dropna(subset=['cap']),'iso3','year','cap',2000,2015)
Y['Y6']=m; cov['Y6_n']=n

# ---- Y7-Y10 GRD 2000-2023 ----
raw=pd.read_excel(SD+"grd/UNUWIDERGRD_2025.xlsx", sheet_name="Merged", header=None)
# positional columns (see inspection): Country3 Year7 ISO8 Caution1=10 C2=12 C3=13
# Taxes incl SC=23 excl SC=24 Income total=32 Indirect total=41 Trade total=48
data=raw.iloc[2:].copy()
grd=pd.DataFrame({
 'iso3':data[8].astype(str).str.strip(),
 'year':pd.to_numeric(data[7],errors='coerce'),
 'c1':data[10],'c2':data[12],'c3':data[13],
 'taxes':pd.to_numeric(data[24],errors='coerce'),   # Taxes excluding SC (%GDP)
 'income':pd.to_numeric(data[32],errors='coerce'),  # Income/Profits/CapGains total (%GDP)
 'indirect':pd.to_numeric(data[41],errors='coerce'),# Indirect total (%GDP)
 'trade':pd.to_numeric(data[48],errors='coerce'),   # Taxes on Int'l Trade total (%GDP)
})
grd=grd[(grd.year>=2000)&(grd.year<=2023)].copy()
grd['caution']=grd[['c1','c2','c3']].notna().any(axis=1)
def grd_build(df):
    df=df.copy()
    df['trade_share']=df.trade/df.taxes
    df['ind_share']=df.indirect/df.taxes
    df['y7']=1-df.trade_share
    df['y8']=1-(df.trade_share+df.ind_share)
    g=df.groupby('iso3')
    out=pd.DataFrame({
      'Y7':g.y7.mean(),'Y8':g.y8.mean(),
      'Y9':g.income.mean(),'Y10':g.taxes.mean(),
      'Y7_n':g.y7.count(),'Y9_n':g.income.count(),'Y10_n':g.taxes.count()})
    return out
grd_main=grd_build(grd)
grd_noc=grd_build(grd[~grd.caution])  # leave-out sensitivity
for c in ['Y7','Y8','Y9','Y10']: Y[c]=grd_main[c]
cov['Y7_n']=grd_main['Y7_n']; cov['Y9_n']=grd_main['Y9_n']; cov['Y10_n']=grd_main['Y10_n']
grd_main.to_csv(OUT+"grd_main.csv"); grd_noc.to_csv(OUT+"grd_nocaution.csv")

# ---- Y2/Y3 Doing Business DB2020 (bridge) ----
db=pd.read_excel(SD+"doingbusiness/Historical-Data--DB04-DB20-.xlsx", sheet_name="DB20 Data", header=None, nrows=4)
print("DB20 first rows preview:")
print(db.head(4).to_string()[:800])

# assemble Y table
ydf=pd.DataFrame(index=sorted(set().union(*[set(s.index) for s in Y.values()])))
for k,s in Y.items(): ydf[k]=s
for k,s in cov.items(): ydf[k]=s
ydf.index.name='iso3'; ydf=ydf.reset_index()
ydf['region']=ydf.iso3.map(regions)
if wgi_region is not None:
    ydf['region']=ydf['region'].fillna(ydf.iso3.map(wgi_region))
ydf.to_csv(OUT+"outcomes.csv",index=False)
print("outcomes built. coverage:")
for c in ['Y1','Y4','Y5','Y6','Y7','Y8','Y9','Y10']:
    print(f"  {c}: n={ydf[c].notna().sum()}")
print("regions non-null:", ydf.region.notna().sum())
