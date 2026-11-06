#!/usr/bin/env python3
"""Blocks B + D: paper-era anchors, rolled-window estimates (Table 1 & 2),
C4 income rerun. OLS + HC1 robust SEs. V-between / V-within x X0 / X1 (+X2 descr)."""
import pandas as pd, numpy as np, statsmodels.api as sm, json
RES="/workspace/eval/followup/001-001-living-update/results/"; OUT="data/"
SD="/workspace/eval/followup_staging/shared-data/"
F=pd.read_csv(RES+"frame_update.csv")

LEG=['l_eng','l_ger','l_sca','l_soc']        # l_fre excluded (base)
GEN={'X0':{'war':'war_x0','dem':'dem_x0','parl':'parl_x0'},
     'X1':{'war':'avg_war00','dem':'dem_x1','parl':'parl_x1'},
     'X2':{'war':'war_x2','dem':'dem_x1','parl':'parl_x1'}}
# legal-capacity side (Table 1 successors) and fiscal side (Table 2 successors)
T1=['Y1','Y2','Y3','Y4','Y5','Y6']; T2=['Y7','Y8','Y9','Y10']

def region_dummies(df):
    d=pd.get_dummies(df['region'].astype('object'),prefix='reg',dummy_na=False)
    return d.astype(float)

def run_one(df, ycol, gen, variant):
    g=GEN[gen]
    xcols=[g['war'],g['dem'],g['parl']]+LEG
    sub=df.dropna(subset=[ycol]+xcols).copy()
    if variant=='within':
        rd=region_dummies(sub)
        # drop one region to avoid collinearity; keep regions with >=2 obs
        keep=[c for c in rd.columns if rd[c].sum()>=2]
        rd=rd[keep]
        if rd.shape[1]>0: rd=rd.iloc[:,1:]  # drop first region as base
        X=pd.concat([sub[xcols].reset_index(drop=True), rd.reset_index(drop=True)],axis=1)
    else:
        X=sub[xcols].reset_index(drop=True)
    y=sub[ycol].reset_index(drop=True).astype(float)
    X=X.astype(float)
    Xc=sm.add_constant(X,has_constant='add')
    if len(sub)<10 or np.linalg.matrix_rank(Xc.values)<Xc.shape[1]:
        # fall back: drop region dummies causing rank deficiency
        Xc=sm.add_constant(sub[xcols].reset_index(drop=True).astype(float),has_constant='add')
    m=sm.OLS(y,Xc).fit(cov_type='HC1')
    # standardized betas (z-score X and Y on estimation sample) for the 3 history regressors
    out=[]
    sy=y.std(ddof=0)
    for rc in xcols:
        if rc not in m.params.index:
            out.append((rc,np.nan,np.nan,np.nan,np.nan)); continue
        sx=sub[rc].astype(float).std(ddof=0)
        std_beta=m.params[rc]*sx/sy if sy>0 else np.nan
        out.append((rc,m.params[rc],m.bse[rc],m.pvalues[rc],std_beta))
    return out, int(len(sub)), float(m.rsquared)

def est_table(cols, gens, variants, tablename, window_tag):
    rows=[]
    for yc in cols:
        for gen in gens:
            for var in variants:
                res,n,r2=run_one(F, yc, gen, var)
                for rc,coef,se,p,sb in res:
                    role={'war_x0':'war','avg_war00':'war','war_x2':'war',
                          'dem_x0':'dem','dem_x1':'dem','parl_x0':'parl','parl_x1':'parl'}.get(rc,'legor')
                    rows.append({'table':tablename,'y_col':yc,'generation':gen,'variant':var,
                        'regressor':rc,'role':role,'coef':coef,'se':se,'p':p,'n':n,'r2':r2,'std_beta':sb,
                        'window':window_tag})
    return pd.DataFrame(rows)

# ---- Block D: rolled-window estimates ----
t1=est_table(T1,['X0','X1','X2'],['between','within'],'Table1_legal','2000-2024 rolled')
t2=est_table(T2,['X0','X1','X2'],['between','within'],'Table2_fiscal','2000-2023 rolled')
t1.to_csv(RES+"table1_update.csv",index=False)
t2.to_csv(RES+"table2_update.csv",index=False)
print("Table1/2 estimates written. rows:",len(t1),len(t2))

# ---- Block B: paper-era anchors (printed + in-study reconstruction on paper-era windows) ----
# Printed AER coefficients (Table 1 p.1237, Table 2 p.1238): regressor-> (coef, se, stars)
printed={
 'Table1': {  # DV order: priv credit(c1), credit access(c2), investor prot(c3), anti-diversion ICRG(c4)
   'war': {'c1':(0.510,0.143,'***'),'c2':(0.647,0.191,'**'),'c3':(0.598,0.241,'***'),'c4':None},
   'parl':{'c3':(0.339,0.0,'**'),'c4':(0.112,0.0,'*')},
 },
 'Table2': {  # DV: 1-tradeshare(c1), 1-(trade+indirect)(c2), incometax/GDP(c3), tax/GDP(c4)
   'war': {'c1':(0.555,0.0,'**'),'c2':(0.762,0.0,'***')},
   'parl':{'c3':(0.212,0.0,'***'),'c4':(0.160,0.0,'**')},
 }}
# paper-era reconstruction windows per successor instrument (earliest comparable)
# run X0 spec on paper-era windows so std betas are comparable to the rolled ones
def winmean_series(df,yr,val,y0,y1,key='iso3'):
    d=df[(df[yr]>=y0)&(df[yr]<=y1)].dropna(subset=[val])
    return d.groupby(key)[val].mean()
# rebuild paper-era outcome columns on F2 = copy of history+legal with early-window outcomes
F2=F[['iso3','country','war_x0','dem_x0','parl_x0']+LEG+['region']].copy()
import pyreadstat
g=pd.read_excel(SD+"gfdd/GFDD_sept2022.xlsx", sheet_name="Data - August 2022")[['iso3','year','di01']]
g['di01']=pd.to_numeric(g.di01,errors='coerce')
F2['Y1']=F2.iso3.map(winmean_series(g,'year','di01',1980,2000))
vd=pd.read_csv(OUT+"vdem_core.csv",encoding='latin-1').rename(columns={'country_text_id':'iso3'})
F2['Y5']=F2.iso3.map(winmean_series(vd,'year','v2xcl_prpty',1980,2000))
# GRD paper-era (1980-2000)
grd=pd.read_csv(OUT+"grd_main.csv")  # this is 2000-2023; need 1980-2000 build
# rebuild GRD 1980-2000 quickly
raw=pd.read_excel(SD+"grd/UNUWIDERGRD_2025.xlsx", sheet_name="Merged", header=None)
d=raw.iloc[2:].copy()
G=pd.DataFrame({'iso3':d[8].astype(str).str.strip(),'year':pd.to_numeric(d[7],errors='coerce'),
  'taxes':pd.to_numeric(d[24],errors='coerce'),'income':pd.to_numeric(d[32],errors='coerce'),
  'indirect':pd.to_numeric(d[41],errors='coerce'),'trade':pd.to_numeric(d[48],errors='coerce')})
Gp=G[(G.year>=1980)&(G.year<=2000)].copy()
Gp['y7']=1-Gp.trade/Gp.taxes; Gp['y8']=1-(Gp.trade+Gp.indirect)/Gp.taxes
gp=Gp.groupby('iso3').agg(Y7=('y7','mean'),Y8=('y8','mean'),Y9=('income','mean'),Y10=('taxes','mean'))
for c in ['Y7','Y8','Y9','Y10']: F2[c]=F2.iso3.map(gp[c])

def anchor_std(F2df, ycol):
    xcols=['war_x0','dem_x0','parl_x0']+LEG
    sub=F2df.dropna(subset=[ycol]+xcols)
    if len(sub)<15: return {}
    X=sm.add_constant(sub[xcols].astype(float),has_constant='add')
    m=sm.OLS(sub[ycol].astype(float),X).fit(cov_type='HC1')
    sy=sub[ycol].std(ddof=0); out={}
    for rc in ['war_x0','dem_x0','parl_x0']+LEG:
        sx=sub[rc].std(ddof=0)
        out[rc]={'coef':float(m.params[rc]),'se':float(m.bse[rc]),'p':float(m.pvalues[rc]),
                 'std_beta':float(m.params[rc]*sx/sy),'n':int(len(sub))}
    return out
anchor_recon={yc:anchor_std(F2,yc) for yc in ['Y1','Y5','Y7','Y8','Y9','Y10']}

# write anchors.csv (printed + reconstruction std betas)
arows=[]
for yc,res in anchor_recon.items():
    for rc,v in res.items():
        role={'war_x0':'war','dem_x0':'dem','parl_x0':'parl'}.get(rc,'legor')
        arows.append({'y_col':yc,'regressor':rc,'role':role,'paper_era_coef_recon':v['coef'],
          'paper_era_se':v['se'],'paper_era_p':v['p'],'paper_era_std_beta':v['std_beta'],'n':v['n'],
          'source':'Branch R in-study reconstruction, X0 history x paper-era window (GFDD 1980-2000 / VDem 1980-2000 / GRD 1980-2000)','tag':'pending-deposit'})
pd.DataFrame(arows).to_csv(RES+"anchors.csv",index=False)
json.dump({'printed_AER':printed,'reconstruction_std_betas':anchor_recon}, open(RES+"anchors_printed.json","w"),indent=2)
print("anchors written. reconstruction cols:",list(anchor_recon.keys()))

# ---- C4 income rerun: DV = log income per capita (PWT rgdpe/pop mean 2000-2023; WDI sens) ----
pwt,_=pyreadstat.read_dta(SD+"pwt/pwt110.dta")
pwt=pwt[['countrycode','year','rgdpe','pop']].dropna(subset=['rgdpe','pop'])
pwt['ypc']=pwt['rgdpe']/pwt['pop']
pwt=pwt[(pwt.year>=2000)&(pwt.year<=2023)]
ypc=pwt.groupby('countrycode').ypc.mean().rename('ypc')
F['loginc_pwt']=np.log(F.iso3.map(ypc))
# WDI sensitivity
def wdi_long(path,name):
    j=json.load(open(path)); recs=j[1]
    rows=[(r.get('countryiso3code'),int(r['date']),r['value']) for r in recs if r.get('value') is not None and r.get('countryiso3code')]
    return pd.DataFrame(rows,columns=['iso3','year',name])
wd=wdi_long(SD+"wdi/wdi_NY.GDP.PCAP.KD.json",'ypc_wdi')
wd=wd[(wd.year>=2000)&(wd.year<=2023)].groupby('iso3').ypc_wdi.mean()
F['loginc_wdi']=np.log(F.iso3.map(wd))
inc_rows=[]
for dv,tag in [('loginc_pwt','PWT rgdpe/pop'),('loginc_wdi','WDI NY.GDP.PCAP.KD')]:
    for gen in ['X0','X1']:
        for var in ['between','within']:
            res,n,r2=run_one(F,dv,gen,var)
            for rc,coef,se,p,sb in res:
                role={'war_x0':'war','avg_war00':'war','dem_x0':'dem','dem_x1':'dem','parl_x0':'parl','parl_x1':'parl'}.get(rc,'legor')
                inc_rows.append({'dv':dv,'dv_source':tag,'generation':gen,'variant':var,'regressor':rc,
                    'role':role,'coef':coef,'se':se,'p':p,'n':n,'r2':r2,'std_beta':sb})
pd.DataFrame(inc_rows).to_csv(RES+"income_rerun.csv",index=False)
print("income_rerun written, rows:",len(inc_rows))
print("DONE estimate")
