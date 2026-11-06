#!/usr/bin/env python3
"""Block D figures: fig1_update (Figure 1 reproduction) + fig_war_coefficients."""
import pandas as pd, numpy as np, json
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
RES="/workspace/eval/followup/001-001-living-update/results/"
OKABE=["#0072B2","#E69F00","#009E73","#D55E00","#CC79A7","#56B4E9","#F0E442","#000000"]
plt.rcParams.update({"figure.figsize":(7.5,4.5),"figure.dpi":150,"savefig.dpi":150,
 "savefig.bbox":"tight","font.size":12,"axes.titlesize":13,"axes.labelsize":12,
 "axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"grid.alpha":0.25,
 "axes.prop_cycle":plt.cycler(color=OKABE)})

F=pd.read_csv(RES+"frame_update.csv")

# ---------- Figure 1 update: Y9 (income tax/GDP) vs Y1 (private credit/GDP), split at median income ----------
# use PWT log income if present else recompute from WDI already stored? use frame columns
import pyreadstat
pwt,_=pyreadstat.read_dta("/workspace/eval/followup_staging/shared-data/pwt/pwt110.dta")
pwt=pwt[['countrycode','year','rgdpe','pop']].dropna()
pwt['ypc']=pwt['rgdpe']/pwt['pop']; pwt=pwt[(pwt.year>=2000)&(pwt.year<=2024)]
ypc=pwt.groupby('countrycode').ypc.mean()
F['loginc']=np.log(F.iso3.map(ypc))
d=F.dropna(subset=['Y1','Y9','loginc']).copy()
med=d.loginc.median()
d['half']=np.where(d.loginc>=med,'High income','Low income')
fig,ax=plt.subplots()
slopes={}
for i,(hv,col) in enumerate([('Low income',OKABE[0]),('High income',OKABE[1])]):
    s=d[d.half==hv]
    ax.scatter(s.Y1,s.Y9,s=22,color=col,alpha=0.75,label=f"{hv} (n={len(s)})")
    if len(s)>2:
        b=np.polyfit(s.Y1,s.Y9,1); xs=np.linspace(s.Y1.min(),s.Y1.max(),50)
        ax.plot(xs,np.polyval(b,xs),color=col,lw=2)
        r=np.corrcoef(s.Y1,s.Y9)[0,1]
        slopes[hv]={'slope':float(b[0]),'corr':float(r),'n':int(len(s))}
ax.set_xlabel("Private credit / GDP, mean 2000–2021 (GFDD di01)")
ax.set_ylabel("Income taxes / GDP, mean 2000–2023 (GRD)")
ax.legend(frameon=False,fontsize=10)
fig.savefig(RES+"fig1_update.png",facecolor="white"); plt.close(fig)
# overall
ball=np.polyfit(d.Y1,d.Y9,1); slopes['All']={'slope':float(ball[0]),'corr':float(np.corrcoef(d.Y1,d.Y9)[0,1]),'n':int(len(d))}
pd.DataFrame(slopes).T.reset_index().rename(columns={'index':'half'}).to_csv(RES+"fig1_update.csv",index=False)
print("fig1_update slopes:",slopes)

# ---------- fig_war_coefficients: standardized war beta across 8 columns, X1 between/within ----------
t1=pd.read_csv(RES+"table1_update.csv"); t2=pd.read_csv(RES+"table2_update.csv")
A=pd.concat([t1,t2]); VERDICT=['Y1','Y4','Y5','Y6','Y7','Y8','Y9','Y10']
labels={'Y1':'Priv.credit','Y4':'WGI RoL','Y5':'VDem prop','Y6':'Hanson-Sig','Y7':'1-trade','Y8':'1-tr+ind','Y9':'Inc.tax/GDP','Y10':'Tax/GDP'}
anc=pd.read_csv(RES+"anchors.csv"); anchor=float(anc[anc.role=='war'].paper_era_std_beta.median())
fig,ax=plt.subplots(figsize=(8.2,4.6))
x=np.arange(len(VERDICT)); w=0.38
for j,(var,col) in enumerate([('between',OKABE[1]),('within',OKABE[0])]):
    d=A[(A.role=='war')&(A.generation=='X1')&(A.variant==var)].set_index('y_col').reindex(VERDICT)
    vals=d.std_beta.values; sig=(d.p<0.05).values
    bars=ax.bar(x+(j-0.5)*w,vals,w,color=col,label=f"X1 {var}-regions",
        edgecolor=['black' if s else 'none' for s in sig],linewidth=1.3)
ax.axhline(anchor,color=OKABE[3],ls='--',lw=1.6,label=f"paper-era anchor (recon. β*={anchor:.2f})")
ax.axhline(0,color='gray',lw=0.8)
ax.set_xticks(x); ax.set_xticklabels([labels[y] for y in VERDICT],rotation=35,ha='right',fontsize=9)
ax.set_ylabel("Standardized war coefficient (2000–2024 outcomes)")
ax.legend(frameon=False,fontsize=9,loc='upper right')
ax.set_title("War-incidence correlate, X1 history (avg_war00 1816–2000)",fontsize=12)
fig.text(0.01,-0.02,"Black-edged bars: p<0.05 (HC1).",fontsize=8)
fig.savefig(RES+"fig_war_coefficients.png",facecolor="white"); plt.close(fig)
print("fig_war_coefficients written; anchor=",round(anchor,4))
