#!/usr/bin/env python3
"""Block C (part 3): merge history + outcomes + bridges into frame_update.csv;
legal-origin cross-check Pillars l_* vs QoG lp_legor; crosswalk unmatched list."""
import pandas as pd, numpy as np
SD="/workspace/eval/followup_staging/shared-data/"
OUT="data/"; RES="/workspace/eval/followup/001-001-living-update/results/"
import os; os.makedirs(RES,exist_ok=True)

H=pd.read_csv(OUT+"history_merged.csv").dropna(subset=['iso3'])
# recompute parl_x1 chain columns here (ensure present)
H['parl_x1']=(H.parl_sum.fillna(0)+H.ext_sum.fillna(0))/(H.parl_n.fillna(0)+H.ext_n.fillna(0)).replace(0,np.nan)
H['parl_x1_2016']=H.parl_sum/H.parl_n.replace(0,np.nan)
O=pd.read_csv(OUT+"outcomes.csv")
db=pd.read_csv(OUT+"db2020.csv")
F=H.merge(O,on='iso3',how='outer').merge(db,on='iso3',how='left')

# legal-origin cross-check vs QoG lp_legor (1 eng,2 fre,3 soc,4 ger,5 sca)
q=pd.read_csv(SD+"legal-origins/qog_std_cs_jan21.csv", low_memory=False, encoding='latin-1')
q=q.dropna(subset=['ccodealp']).copy(); q=q.rename(columns={'ccodealp':'iso3'})
legmap={1:'eng',2:'fre',3:'soc',4:'ger',5:'sca'}
q['qog_lo']=q.lp_legor.map(legmap)
ql=q[['iso3','qog_lo']]
F=F.merge(ql,on='iso3',how='left')
def pil_lo(r):
    for k in ['eng','fre','soc','ger','sca']:
        if r.get('l_'+k)==1: return k
    return np.nan
F['pil_lo']=F.apply(pil_lo,axis=1)
disagree=F[(F.qog_lo.notna())&(F.pil_lo.notna())&(F.qog_lo!=F.pil_lo)][['iso3','country','pil_lo','qog_lo']]
disagree.to_csv(RES+"legal_origin_disagreements.csv",index=False)
print("legal-origin disagreements (Pillars vs QoG):", len(disagree))
print(disagree.to_string())

F.to_csv(RES+"frame_update.csv",index=False)
# crosswalk unmatched: iso3 present in history but no outcomes, or vice versa
xwalk=pd.read_csv(OUT+"crosswalk.csv")
hist_iso=set(H.iso3); out_iso=set(O.iso3)
only_hist=sorted(hist_iso-out_iso); only_out=sorted(out_iso-hist_iso)
pd.DataFrame({'only_in_history':pd.Series(only_hist)}).to_csv(RES+"crosswalk_unmatched_history_only.csv",index=False)
pd.DataFrame({'only_in_outcomes':pd.Series(only_out)}).to_csv(RES+"crosswalk_unmatched_outcomes_only.csv",index=False)
print("iso3 only in history:",len(only_hist)," only in outcomes:",len(only_out))
print("frame rows:", len(F), "-> results/frame_update.csv")
# quick coverage of estimation-ready rows (legal origin + >=1 outcome)
lo_ok=F[['l_eng','l_fre','l_ger','l_sca','l_soc']].notna().any(axis=1)
print("rows with legal origin:", lo_ok.sum())
