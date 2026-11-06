#!/usr/bin/env python3
"""Study 002 figures: complementarity slopes by era (CIs), and the trade-tax march."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, pandas as pd, numpy as np
RES="/workspace/eval/followup/002-002-theory-update/results/"
OKABE=["#0072B2","#E69F00","#009E73","#D55E00","#CC79A7","#56B4E9","#F0E442","#000000"]
plt.rcParams.update({"figure.figsize":(7.5,4.5),"figure.dpi":150,"savefig.dpi":150,
 "savefig.bbox":"tight","font.size":12,"axes.titlesize":13,"axes.labelsize":12,
 "axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"grid.alpha":0.25,
 "axes.prop_cycle":plt.cycler(color=OKABE)})

c=pd.read_csv(RES+"complementarity_by_era.csv")
pc=c[(c.x_var=='private_credit_GFDD_di01')&(c['sample']=='common')].copy()
eras=['E0','E1','E2']; elab=['E0\n1975-2000','E1\n2000-2012','E2\n2012-2024']
halves=[('all','pooled',OKABE[7]),('high','high-income half',OKABE[1]),('low','low-income half',OKABE[0])]

# ---- Fig 1: standardized slope = correlation r, with Fisher-z 95% CI, by era x half ----
# (natural-unit slopes are tiny because income-tax is a GDP-fraction and credit a percent;
#  r is scale-free and is the simple-OLS standardized slope. CIs via Fisher z.)
def fisher_ci(r,n):
    if np.isnan(r) or n<4: return (np.nan,np.nan)
    z=np.arctanh(r); se=1/np.sqrt(n-3)
    return (np.tanh(z-1.96*se), np.tanh(z+1.96*se))
fig,ax=plt.subplots()
x=np.arange(len(eras)); off={'all':-0.22,'high':0.0,'low':0.22}
for half,lab,col in halves:
    sub=pc[pc.income_half==half].set_index('era').reindex(eras)
    rv=sub['r'].values; nn=sub['n'].values
    lo=[]; hi=[]
    for r,n in zip(rv,nn):
        a,b=fisher_ci(r,n); lo.append(r-a); hi.append(b-r)
    ax.errorbar(x+off[half], rv, yerr=[lo,hi], fmt='o', color=col, capsize=4,
                markersize=8, label=lab, lw=2)
ax.axhline(0,color='gray',lw=1,ls='--')
ax.set_xticks(x); ax.set_xticklabels(elab)
ax.set_ylabel("Standardized slope (corr. r): income-tax vs private credit")
ax.set_xlabel("Era [boundaries 2000, 2012 SPEC-CHOICE]")
ax.legend(frameon=False, fontsize=10, loc='lower left')
ax.set_ylim(-0.1,0.8)
ax.set_title("Legal-fiscal complementarity by era (common sample N=148, Fisher 95% CI)")
fig.savefig(RES+"fig_complementarity_eras.png",facecolor="white"); plt.close(fig)
print("fig_complementarity_eras.png written")

# ---- Fig 2: trade-tax march ----
march=pd.read_csv(RES+"tradetax_march.csv")
yrs=march.year.tolist(); cnt=march.n_countries_trade_share_gt_40pct.tolist()
fig,ax=plt.subplots()
ax.plot(yrs,cnt,'-o',color=OKABE[1],markersize=10,lw=2.5,label="GRD 2025, this study (trade/taxes > 40%)")
for xi,yi in zip(yrs,cnt): ax.annotate(str(yi),(xi,yi),textcoords="offset points",xytext=(0,10),ha='center',fontsize=11,color=OKABE[1])
# DP16256 reference vintage (Fig 7): ~20 in 2000, 7 in 2010
ax.plot([2000,2010],[20,7],'s--',color=OKABE[0],markersize=9,lw=1.8,alpha=0.8,label="DP16256 (2021) Fig 7 vintage")
for xi,yi in zip([2000,2010],[20,7]): ax.annotate(f"~{yi}",(xi,yi),textcoords="offset points",xytext=(0,-16),ha='center',fontsize=10,color=OKABE[0])
ax.set_xticks([2000,2010,2023]); ax.set_ylim(0,30)
ax.set_ylabel("# countries with trade tax > 40% of total taxes")
ax.set_xlabel("Year")
ax.set_title("Fiscal-capacity march away from trade taxation (Q3)")
ax.legend(frameon=False,fontsize=10,loc='upper right')
fig.savefig(RES+"fig_tradetax_march.png",facecolor="white"); plt.close(fig)
print("fig_tradetax_march.png written")
import os; open("/workspace/eval/followup/002-002-theory-update/workspace/checkpoints/B4.done","w").close()
