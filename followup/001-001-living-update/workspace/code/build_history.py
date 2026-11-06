#!/usr/bin/env python3
"""Block C (part 1): build the history variables X0/X1/X2 per country and the
COW<->ISO3<->VDEM crosswalk. Branch R (reconstruction; deposit pending)."""
import pandas as pd, numpy as np, json, os
SD="/workspace/eval/followup_staging/shared-data/"
OUT="/workspace/eval/followup/001-001-living-update/workspace/data/"
os.makedirs(OUT, exist_ok=True)

# ---------- crosswalk from V-Dem (COWcode <-> country_text_id iso3) ----------
vd=pd.read_csv(OUT+"vdem_core.csv", encoding="latin-1")
vd=vd[vd.year>=1789].copy()
# canonical COW<->iso3 from the most recent year each country has a COWcode
cw=vd.dropna(subset=['COWcode','country_text_id']).copy()
cw['COWcode']=cw.COWcode.astype(int)
cw=cw.sort_values('year').groupby('country_text_id').tail(1)[['COWcode','country_text_id','country_name']]
cw=cw.rename(columns={'country_text_id':'iso3'}).drop_duplicates('COWcode')
# QoG backup crosswalk
q=pd.read_csv(SD+"legal-origins/qog_std_cs_jan21.csv", low_memory=False, encoding='latin-1')
qcw=q.dropna(subset=['ccodecow','ccodealp'])[['ccodecow','ccodealp']].copy()
qcw['ccodecow']=qcw.ccodecow.astype(int)
qcw=qcw.rename(columns={'ccodecow':'COWcode','ccodealp':'iso3'}).drop_duplicates('COWcode')
# merge: prefer vdem, fill from qog
xwalk=cw.set_index('COWcode')
for _,r in qcw.iterrows():
    if r.COWcode not in xwalk.index:
        xwalk.loc[r.COWcode]={'iso3':r.iso3,'country_name':np.nan}
xwalk=xwalk.reset_index()
cow2iso=dict(zip(xwalk.COWcode, xwalk.iso3))
print("crosswalk COW->iso3 entries:", len(cow2iso))

# ---------- Pillars 2: avg_war00, parl_dem, legal origins, indep year ----------
import pyreadstat
pil,_=pyreadstat.read_dta(SD+"pillars/2021/Pillars 2.dta")
pil=pil.rename(columns={'ccode':'iso3'})  # Pillars 'ccode' is actually ISO3
# country-constant vars (take first non-null per iso3)
const=pil.groupby('iso3').agg(
    avg_war00=('avg_war00','first'),
    l_eng=('l_eng','max'), l_soc=('l_soc','max'), l_sca=('l_sca','max'),
    l_ger=('l_ger','max'), l_fre=('l_fre','max'),
    c_year=('c_year','first'), country=('country','first')).reset_index()
# parl_dem X0: share of years 1800-1975 with parl_dem==1
p75=pil[(pil.year>=1800)&(pil.year<=1975)]
parl_x0=p75.groupby('iso3').apply(lambda g: g.parl_dem.mean() if g.parl_dem.notna().any() else np.nan).rename('parl_x0')
parl_x0_n=p75.groupby('iso3').parl_dem.apply(lambda s: s.notna().sum()).rename('parl_x0_n')
# parl_dem chain through 2016 (Pillars max year)
pall=pil[(pil.year>=1800)&(pil.year<=2016)]
parl_2016_yrs=pall.groupby('iso3').apply(lambda g: pd.Series({
    'parl_sum':g.parl_dem.sum(min_count=1), 'parl_n':g.parl_dem.notna().sum()}))
hist=const.merge(parl_x0,on='iso3',how='left').merge(parl_x0_n,on='iso3',how='left').merge(parl_2016_yrs,on='iso3',how='left')
print("Pillars countries (iso3):", hist.iso3.nunique())

# ---------- V-Dem democracy X0 / X1 ----------
vd['COWcode']=vd.COWcode
# use iso3 key from vdem itself
vd=vd.rename(columns={'country_text_id':'iso3'})
def dem_share(df, y0, y1, col='e_polity2', thr=0.0):
    d=df[(df.year>=y0)&(df.year<=y1)]
    g=d.groupby('iso3')[col]
    num=g.apply(lambda s:(s>thr).sum())
    den=g.apply(lambda s:s.notna().sum())
    return num, den
# X0 democracy 1800-1975, polity2>0
n0,d0=dem_share(vd,1800,1975,'e_polity2',0.0)
dem_x0=(n0/d0.replace(0,np.nan)).rename('dem_x0'); dem_x0_n=d0.rename('dem_x0_n')
# X1 democracy: polity2>0 1800-2018 part + LIED>=4 2019-2024 part
# polity part counts
pol=vd[(vd.year>=1800)&(vd.year<=2018)]
gp=pol.groupby('iso3')
pol_num=gp.e_polity2.apply(lambda s:(s>0).sum()); pol_den=gp.e_polity2.apply(lambda s:s.notna().sum())
lied=vd[(vd.year>=2019)&(vd.year<=2024)]
gl=lied.groupby('iso3')
lied_num=gl.e_lexical_index.apply(lambda s:(s>=4).sum()); lied_den=gl.e_lexical_index.apply(lambda s:s.notna().sum())
demdf=pd.DataFrame({'pol_num':pol_num,'pol_den':pol_den}).join(
      pd.DataFrame({'lied_num':lied_num,'lied_den':lied_den}),how='outer').fillna(0)
dem_x1=((demdf.pol_num+demdf.lied_num)/(demdf.pol_den+demdf.lied_den).replace(0,np.nan)).rename('dem_x1')
dem_x1_2018=(demdf.pol_num/demdf.pol_den.replace(0,np.nan)).rename('dem_x1_2018')  # fail-branch: ends 2018

vdemh=pd.DataFrame(dem_x0).join(dem_x0_n).join(dem_x1).join(dem_x1_2018)
vdemh.index.name='iso3'; vdemh=vdemh.reset_index()

# ---------- V-Dem + BR parliamentary X1 chain ----------
br=pd.read_excel(SD+"bjornskov-rode/Bjornskov-Rode-integrated-dataset-v7.1.xlsx", sheet_name="Regime characteristics")
br=br.rename(columns={'country isocode':'iso3','DD regime':'dd','year':'year'})
br=br[['iso3','year','dd']].dropna(subset=['iso3'])
br['parl_br']=(br.dd==0).astype(float)  # DD regime 0 = parliamentary democracy
# merge BR with vdem democracy (polity>0 OR LIED>=4) for 2017-2024
vsel=vd[['iso3','year','e_polity2','e_lexical_index']].copy()
m=br.merge(vsel,on=['iso3','year'],how='left')
m['dem_ok']=((m.e_polity2>0)|(m.e_lexical_index>=4)).astype(float)
m['parl_chain']=((m.dd==0)&(m.dem_ok==1)).astype(float)
ext=m[(m.year>=2017)&(m.year<=2024)].groupby('iso3').agg(ext_sum=('parl_chain','sum'),ext_n=('parl_chain','size')).reset_index()

# ---------- COW war X0: share years 1816(/indep)-1975 in interstate/extrastate war ----------
def cow_years(path):
    c=pd.read_csv(path, encoding="latin-1")
    ccol='ccode' if 'ccode' in c.columns else 'ccode1'
    rows=[]
    for _,r in c.iterrows():
        cc=r[ccol]
        if pd.isna(cc) or cc<0: continue
        for s,e in [('StartYear1','EndYear1'),('StartYear2','EndYear2')]:
            y0,y1=r.get(s),r.get(e)
            if pd.notna(y0) and y0>0:
                y1=y1 if (pd.notna(y1) and y1>0) else y0
                for y in range(int(y0),int(y1)+1):
                    rows.append((int(cc),y))
    return pd.DataFrame(rows,columns=['ccode','year'])
inter=cow_years(SD+"cow/Inter-StateWarData_v4.0.csv")
extra=cow_years(SD+"cow/Extra-StateWarData_v4.0.csv")
waryrs=pd.concat([inter,extra]).drop_duplicates()
waryrs['iso3']=waryrs.ccode.map(cow2iso)
waryrs=waryrs.dropna(subset=['iso3'])
waryrs['atwar']=1
# per country (iso3): window max(1816, indep)-1975
def war_share(iso3, c_year, y_end):
    start=1816
    if pd.notna(c_year) and c_year>1816: start=int(c_year)
    win=range(start, y_end+1)
    n=len(list(win))
    wy=set(waryrs[waryrs.iso3==iso3].year)
    k=sum(1 for y in win if y in wy)
    return k/n if n>0 else np.nan
war_x0={}
for _,r in hist.iterrows():
    war_x0[r.iso3]=war_share(r.iso3, r.c_year, 1975)
hist['war_x0']=hist.iso3.map(war_x0)

# ---------- UCDP X2 war splice 2001-2024 (type 1+2 participant) ----------
u=pd.read_csv(SD+"ucdp/UcdpPrioConflict_v26_1.csv", encoding="latin-1")
u12=u[u.type_of_conflict.isin([1,2])].copy()
# participant gwno codes (a and b, comma/space separated)
def parse_gw(x):
    if pd.isna(x): return []
    return [int(float(t)) for t in str(x).replace(';',',').replace(' ',',').split(',') if t.strip() not in ('','nan')]
part=[]
for _,r in u12.iterrows():
    for g in parse_gw(r.gwno_a)+parse_gw(r.gwno_b):
        part.append((g, int(r.year)))
ucdp_part=pd.DataFrame(part,columns=['gw','year']).drop_duplicates()
# gwno ~ COW ccode (same for most); map to iso3
ucdp_part['iso3']=ucdp_part.gw.map(cow2iso)
ucdp_part=ucdp_part.dropna(subset=['iso3']); ucdp_part['atwar_ucdp']=1
ucdp_part.to_csv(OUT+"ucdp_extwar_yearly.csv",index=False)
# X2: war_x0 window extended with 2001-2024 UCDP years, denominator extends to 2024
war_x2={}
for _,r in hist.iterrows():
    start=1816
    if pd.notna(r.c_year) and r.c_year>1816: start=int(r.c_year)
    win=list(range(start,2025))
    cowy=set(waryrs[waryrs.iso3==r.iso3].year)
    ucy=set(ucdp_part[(ucdp_part.iso3==r.iso3)&(ucdp_part.year>=2001)].year)
    k=sum(1 for y in win if (y in cowy) or (y>=2001 and y in ucy))
    war_x2[r.iso3]=k/len(win) if win else np.nan
hist['war_x2']=hist.iso3.map(war_x2)
# save COW yearly for gate G3
waryrs.to_csv(OUT+"cow_extwar_yearly.csv",index=False)

hist.to_csv(OUT+"hist_pillars.csv",index=False)
vdemh.to_csv(OUT+"hist_vdem.csv",index=False)
ext.to_csv(OUT+"hist_parl_ext.csv",index=False)
xwalk.to_csv(OUT+"crosswalk.csv",index=False)

# save the raw yearly series needed for gates (G1,G2)
vsel.to_csv(OUT+"vdem_yearly.csv",index=False)
br.to_csv(OUT+"br_yearly.csv",index=False)
# pillars parl_dem yearly for gate G1
pil[['iso3','year','parl_dem']].to_csv(OUT+"pillars_parl_yearly.csv",index=False)
print("saved history intermediates. dem_x0 n:", vdemh.dem_x0.notna().sum(), "dem_x1 n:", vdemh.dem_x1.notna().sum())
print("DONE build_history")
