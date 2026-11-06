#!/usr/bin/env python3
"""Study 002 Block B — constructions 1-4.
1. complementarity_by_era.csv  (Q1)
2. successor_reconciliation.csv (Q2)
3. tradetax_march.csv           (Q3)
(figures in figures_002.py)
OLS + HC1 robust SEs throughout. Eras E0 1975-2000 (tax from 1980), E1 2000-2012,
E2 2012-2024 (credit ends 2021). Legal-fiscal complementarity = income-tax(%GDP)
on private credit (GFDD di01); rule-of-law alt = WGI rl (E1/E2 only).
Income halves split at era-median PWT real GDP per capita (rgdpe/pop)."""
import pandas as pd, numpy as np, statsmodels.api as sm, pyreadstat, json, os
SD="/workspace/eval/followup_staging/shared-data/"
RES="/workspace/eval/followup/002-002-theory-update/results/"
OUT="/workspace/eval/followup/002-002-theory-update/workspace/data/"
CKP="/workspace/eval/followup/002-002-theory-update/workspace/checkpoints/"
ERAS={'E0':(1980,2000),'E1':(2000,2012),'E2':(2012,2024)}
ERA_LABEL={'E0':'1975-2000 (tax 1980-2000)','E1':'2000-2012','E2':'2012-2024 (credit ends 2021)'}

def hc1_slope(y, x):
    """OLS y~x with HC1; return slope (natural units),se,p,n,intercept,r2, and
    r = Pearson corr (= standardized/scale-free slope for simple OLS)."""
    d=pd.DataFrame({'y':y,'x':x}).dropna()
    if len(d)<5: return dict(slope=np.nan,se=np.nan,p=np.nan,n=int(len(d)),b0=np.nan,r2=np.nan,r=np.nan)
    X=sm.add_constant(d['x'].astype(float),has_constant='add')
    m=sm.OLS(d['y'].astype(float),X).fit(cov_type='HC1')
    r=float(np.corrcoef(d['y'].astype(float),d['x'].astype(float))[0,1])
    return dict(slope=float(m.params['x']),se=float(m.bse['x']),p=float(m.pvalues['x']),
                n=int(len(d)),b0=float(m.params['const']),r2=float(m.rsquared),r=r)

# ---------- load panels, build era-means per country ----------
# GRD income-tax (%GDP)
raw=pd.read_excel(SD+"grd/UNUWIDERGRD_2025.xlsx", sheet_name="Merged", header=None)
d=raw.iloc[2:].copy()
GRD=pd.DataFrame({'iso3':d[8].astype(str).str.strip(),'year':pd.to_numeric(d[7],errors='coerce'),
  'taxes':pd.to_numeric(d[24],errors='coerce'),'income':pd.to_numeric(d[32],errors='coerce'),
  'trade':pd.to_numeric(d[48],errors='coerce')})
# GFDD private credit di01
g=pd.read_excel(SD+"gfdd/GFDD_sept2022.xlsx", sheet_name="Data - August 2022")[['iso3','year','di01']]
g['di01']=pd.to_numeric(g.di01,errors='coerce')
# WGI rule of law
w=pd.read_excel(SD+"wgi/wgidataset_with_sourcedata-2026.xlsx", sheet_name="rl").rename(
    columns={'Economy (code)':'iso3','Year':'year','Governance estimate (approx. -2.5 to +2.5)':'rl'})
w['rl']=pd.to_numeric(w.rl,errors='coerce'); w['year']=pd.to_numeric(w.year,errors='coerce')
# PWT income per capita
pwt,_=pyreadstat.read_dta(SD+"pwt/pwt110.dta")
pwt=pwt[['countrycode','year','rgdpe','pop']].rename(columns={'countrycode':'iso3'}).dropna(subset=['rgdpe','pop'])
pwt['ypc']=pwt['rgdpe']/pwt['pop']

def eramean(df,val,y0,y1,key='iso3'):
    s=df[(df.year>=y0)&(df.year<=y1)].dropna(subset=[val]).groupby(key)[val].mean()
    return s

era_frames={}
for E,(y0,y1) in ERAS.items():
    inc=eramean(GRD,'income',y0,y1)
    cr =eramean(g,'di01',y0, min(y1,2021))     # credit ends 2021
    rl =eramean(w,'rl',max(y0,1996),y1) if E in ('E1','E2') else pd.Series(dtype=float)
    yp =eramean(pwt,'ypc',y0,min(y1,2023))
    df=pd.DataFrame({'income':inc,'credit':cr,'rl':rl,'ypc':yp})
    df['era']=E
    era_frames[E]=df

# ---------- Construction 1: complementarity_by_era.csv ----------
# common sample = iso3 with income & credit present in ALL three eras
present={E:set(era_frames[E].dropna(subset=['income','credit']).index) for E in ERAS}
common=set.intersection(*present.values())
rows=[]
def half_label(df):
    med=df['ypc'].median()
    return np.where(df['ypc']>=med,'high','low')
for E in ERAS:
    df=era_frames[E].copy()
    for sample,idx in [('full',df.index),('common',[i for i in df.index if i in common])]:
        sub=df.loc[list(idx)]
        # income-tax on private credit
        for half in ['all','low','high']:
            if half=='all': s=sub
            else:
                hl=half_label(sub); s=sub[hl==half]
            r=hc1_slope(s['income'], s['credit'])
            rows.append(dict(era=E,era_window=ERA_LABEL[E],x_var='private_credit_GFDD_di01',
                sample=sample,income_half=half,**r))
        # income-tax on WGI rule of law (E1/E2 only)
        if E in ('E1','E2') and sub['rl'].notna().sum()>=5:
            for half in ['all','low','high']:
                if half=='all': s=sub
                else:
                    hl=half_label(sub); s=sub[hl==half]
                r=hc1_slope(s['income'], s['rl'])
                rows.append(dict(era=E,era_window=ERA_LABEL[E],x_var='wgi_rule_of_law',
                    sample=sample,income_half=half,**r))
comp=pd.DataFrame(rows)
comp.to_csv(RES+"complementarity_by_era.csv",index=False)
print("complementarity_by_era.csv:",len(comp),"rows; common sample N =",len(common))

# ---------- Q1 slope-difference test (stacked, HC1) on common sample, pooled ----------
def stacked_diff(xvar):
    """income ~ credit + E2 + credit:E2, stacking E0 & E2 common-sample obs; HC1.
       interaction coef = E2 - E0 slope difference, with its HC1 p."""
    frames=[]
    for E in ['E0','E2']:
        s=era_frames[E].loc[[i for i in era_frames[E].index if i in common]].copy()
        s=s.dropna(subset=['income',xvar]); s['E2']=1.0 if E=='E2' else 0.0
        s=s.rename(columns={xvar:'x'}); frames.append(s[['income','x','E2']])
    st=pd.concat(frames,ignore_index=True)
    st['xE2']=st['x']*st['E2']
    X=sm.add_constant(st[['x','E2','xE2']].astype(float),has_constant='add')
    m=sm.OLS(st['income'].astype(float),X).fit(cov_type='HC1')
    return dict(diff_E2_minus_E0=float(m.params['xE2']),se=float(m.bse['xE2']),
                p=float(m.pvalues['xE2']),n=int(len(st)),
                slope_E0=float(m.params['x']),slope_E2=float(m.params['x']+m.params['xE2']))
q1_diff=stacked_diff('credit')
print("Q1 stacked slope-diff (credit, common):",q1_diff)

# ---------- Q1 verdict (fixed evaluation order) ----------
def era_pooled(E,xvar='credit',sample='common'):
    idx=[i for i in era_frames[E].index if i in common] if sample=='common' else era_frames[E].index
    return hc1_slope(era_frames[E].loc[list(idx)]['income'], era_frames[E].loc[list(idx)][xvar])
pooled={E:era_pooled(E) for E in ERAS}
def era_half(E,half,sample='common'):
    idx=[i for i in era_frames[E].index if i in common] if sample=='common' else era_frames[E].index
    sub=era_frames[E].loc[list(idx)]
    hl=half_label(sub); return hc1_slope(sub[hl==half]['income'], sub[hl==half]['credit'])
e2_halves={h:era_half('E2',h) for h in ['low','high']}
def q1_verdict():
    if len(common)<60: return "not separable", "common sample < 60 countries"
    # step 2: rotated if any E2 half slope or pooled E2 slope non-positive
    e2pool=pooled['E2']['slope']
    nonpos=[('pooled',e2pool)]+[(h,e2_halves[h]['slope']) for h in ['low','high']]
    bad=[k for k,v in nonpos if (not np.isnan(v)) and v<=0]
    if bad: return "rotated", f"E2 non-positive slope(s): {bad}"
    # step 3: stacked diff test
    if q1_diff['p']<0.10 and q1_diff['diff_E2_minus_E0']>0: return "strengthened", f"E2>E0 p={q1_diff['p']:.3f}"
    if q1_diff['p']<0.10 and q1_diff['diff_E2_minus_E0']<0: return "weakened", f"E2<E0 p={q1_diff['p']:.3f}"
    # step 4
    return "stable", f"slope-diff not significant (p={q1_diff['p']:.3f})"
q1v,q1why=q1_verdict()
print("Q1 VERDICT:",q1v,"|",q1why)

# ---------- Construction 2: successor_reconciliation.csv (Q2) ----------
F=pd.read_csv(OUT+"frame_with_mcollective.csv")
LEG=['l_eng','l_ger','l_sca','l_soc']; X0=['war_x0','dem_x0','parl_x0']
def region_dummies(df):
    return pd.get_dummies(df['region'].astype('object'),prefix='reg',dummy_na=False).astype(float)
def run_one(df, ycol, variant):
    xcols=X0+LEG
    sub=df.dropna(subset=[ycol]+xcols).copy()
    if variant=='within':
        rd=region_dummies(sub); keep=[c for c in rd.columns if rd[c].sum()>=2]; rd=rd[keep]
        if rd.shape[1]>0: rd=rd.iloc[:,1:]
        X=pd.concat([sub[xcols].reset_index(drop=True),rd.reset_index(drop=True)],axis=1)
    else:
        X=sub[xcols].reset_index(drop=True)
    y=sub[ycol].reset_index(drop=True).astype(float); X=X.astype(float)
    Xc=sm.add_constant(X,has_constant='add')
    if len(sub)<10 or np.linalg.matrix_rank(Xc.values)<Xc.shape[1]:
        Xc=sm.add_constant(sub[xcols].reset_index(drop=True).astype(float),has_constant='add')
    m=sm.OLS(y,Xc).fit(cov_type='HC1')
    sy=y.std(ddof=0); out={}
    for rc in xcols:
        if rc not in m.params.index: out[rc]=dict(coef=np.nan,se=np.nan,p=np.nan,std_beta=np.nan); continue
        sx=sub[rc].astype(float).std(ddof=0)
        out[rc]=dict(coef=float(m.params[rc]),se=float(m.bse[rc]),p=float(m.pvalues[rc]),
                     std_beta=float(m.params[rc]*sx/sy) if sy>0 else np.nan)
    return out,int(len(sub)),float(m.rsquared)

COMPOS={'Hanson_Sigman_2000_2015':'Y6','VDem_v2xcl_prpty_2000_2025':'Y5','mcollective16_2016':'mcollective16'}
G5_floor=80
def verdict_single(coef,p,expect_sign=+1):
    if np.isnan(coef): return "n/a"
    same = (coef>0 and expect_sign>0) or (coef<0 and expect_sign<0)
    if same and p<0.05: return "persists"
    if same: return "weakens"                      # right sign, not significant
    if (not same) and p<0.05: return "reverses"    # opposite sign, significant
    return "mixed"                                  # opposite sign short of significance
rows2=[]
for cname,ycol in COMPOS.items():
    N=len(F.dropna(subset=[ycol]+X0+LEG))
    graded = N>=G5_floor
    for variant in ['between','within']:
        res,n,r2=run_one(F,ycol,variant)
        for role,rc in [('R-war','war_x0'),('R-parl','parl_x0'),
                        ('R-legor-German','l_ger'),('R-legor-Scandinavian','l_sca')]:
            v=res[rc]
            vd = verdict_single(v['coef'],v['p']) if graded else "not separable (coverage)"
            rows2.append(dict(composite=cname,y_col=ycol,variant=variant,role=role,regressor=rc,
                coef=v['coef'],se=v['se'],p=v['p'],std_beta=v['std_beta'],n=n,r2=r2,
                N_merged=N,gradeable=graded,verdict=vd))
recon=pd.DataFrame(rows2)
recon.to_csv(RES+"successor_reconciliation.csv",index=False)
print("successor_reconciliation.csv:",len(recon),"rows")

# ---------- Construction 3: tradetax_march.csv (Q3) ----------
def march_count(year):
    s=GRD[(GRD.year==year)].dropna(subset=['trade','taxes']).copy()
    s=s[s.taxes>0]; s['share']=s.trade/s.taxes
    hi=s[s.share>0.40]
    return int(len(hi)), sorted(hi.iso3.tolist()), int(len(s))
rows3=[]
counts={}
for yr in [2000,2010,2023]:
    c,iso,total=march_count(yr)
    counts[yr]=c
    rows3.append(dict(year=yr,n_countries_trade_share_gt_40pct=c,n_countries_with_data=total,
        iso3_list=";".join(iso)))
march=pd.DataFrame(rows3)
march.to_csv(RES+"tradetax_march.csv",index=False)
dp16256_2010=7
reproduce_ok = abs(counts[2010]-dp16256_2010)<=3
# Q3 verdict (conditional on reproduce-then-extend)
if reproduce_ok:
    c23=counts[2023]
    q3v = "continued" if c23<=7 else ("stalled" if c23<=19 else "reversed")
    q3basis=f"reproduce-check OK (2010 count {counts[2010]} within +/-3 of DP16256's 7); 2023 count = {c23}"
else:
    q3v = "direction only (vintage mismatch)"
    q3basis=f"2010 count {counts[2010]} NOT within +/-3 of DP16256's 7; grade direction only"
print("tradetax counts:",counts,"| reproduce_ok:",reproduce_ok,"| Q3:",q3v)

# ---------- write verdicts.json ----------
verdicts={
 "Q1":{"verdict":q1v,"basis":q1why,
   "common_sample_N":len(common),
   "pooled_slopes_common":{E:{k:pooled[E][k] for k in ['slope','se','p','n']} for E in ERAS},
   "E2_halves_common":{h:{k:e2_halves[h][k] for k in ['slope','se','p','n']} for h in ['low','high']},
   "stacked_diff_E2_vs_E0_credit_common":q1_diff,
   "method":"stacked OLS + credit x E2 interaction, HC1 (gates A5)"},
 "Q2":{"gradeable":{c:(len(F.dropna(subset=[COMPOS[c]]+X0+LEG))>=G5_floor) for c in COMPOS},
   "merged_N":{c:int(len(F.dropna(subset=[COMPOS[c]]+X0+LEG))) for c in COMPOS},
   "mcollective16_index_N":67},
 "Q3":{"verdict":q3v,"basis":q3basis,"counts":counts,"reproduce_ok":bool(reproduce_ok),
   "dp16256_2010_count":dp16256_2010}}
json.dump(verdicts, open(RES+"verdicts.json","w"), indent=2, default=str)
print("verdicts.json written.")
for b in ['B1','B2','B3']: open(CKP+f"{b}.done","w").close()
