#!/usr/bin/env python3
"""Block E: per-row verdicts (I.3 rules) -> results/scorecard.csv."""
import pandas as pd, numpy as np, json
RES="/workspace/eval/followup/001-001-living-update/results/"
t1=pd.read_csv(RES+"table1_update.csv"); t2=pd.read_csv(RES+"table2_update.csv")
A=pd.concat([t1,t2])
VERDICT=['Y1','Y4','Y5','Y6','Y7','Y8','Y9','Y10']
LEGAL=['Y1','Y4','Y5','Y6']; FISCAL=['Y7','Y8','Y9','Y10']
anc=pd.read_csv(RES+"anchors.csv")  # paper-era reconstruction std betas (X0 history)

def sel(role,gen,var,reg=None):
    d=A[(A.generation==gen)&(A.variant==var)&(A.y_col.isin(VERDICT))]
    if role in ('war','dem','parl'):
        d=d[d.role==role]
    else:
        d=d[d.regressor==reg]
    return d.set_index('y_col').reindex(VERDICT)

def tally(d, sign=+1):
    pos=(np.sign(d.coef)==sign)
    sig=(d.p<0.05)
    nsign=int((pos).sum()); nsig_sign=int((pos&sig).sum())
    nlegal_sig=int((pos&sig&d.index.isin(LEGAL)).sum())
    nfiscal_sig=int((pos&sig&d.index.isin(FISCAL)).sum())
    nopp_sig=int(((np.sign(d.coef)==-sign)&sig).sum())
    return dict(nsign=nsign,nsig_sign=nsig_sign,nlegal_sig=nlegal_sig,nfiscal_sig=nfiscal_sig,
                nopp_sig=nopp_sig,median_std=float(np.nanmedian(d.std_beta)))

def paper_anchor_std(role):
    rc={'war':'war_x0','dem':'dem_x0','parl':'parl_x0'}[role]
    v=anc[anc.regressor==rc].paper_era_std_beta
    return float(np.nanmedian(v)) if len(v) else np.nan

def verdict_capacity(role,gen,var):
    d=sel(role,gen,var); t=tally(d,+1)
    persists = (t['nsig_sign']>=5 and t['nlegal_sig']>=2 and t['nfiscal_sig']>=2)
    reverses = (t['nopp_sig']>=3 and t['nsig_sign']==0)
    weakens_sign = (t['nsign']>=6)
    anchor=paper_anchor_std(role)
    atten = (not np.isnan(anchor)) and (abs(t['median_std']) < 0.5*abs(anchor))
    word='mixed'; phrase=''
    if reverses: word='reverses'
    elif persists and atten: word='weakens'; phrase='persists in sign, attenuated by more than half'
    elif persists: word='persists'
    elif weakens_sign: word='weakens'
    return word,phrase,t,anchor,atten

def verdict_dem(gen,var):  # paper row is null-to-weak; graded vs "null"
    d=sel('dem',gen,var); nsig=int((d.p<0.05).sum()); ninsig=8-nsig
    pos_sig=int(((d.coef>0)&(d.p<0.05)).sum())
    if ninsig>=6: word='persists (stays null-to-weak)'; note=f'{ninsig}/8 insignificant'
    elif pos_sig>=5: word='new out-of-sample pattern'; note=f'{pos_sig}/8 newly positive & significant'
    else: word='mixed'; note=f'{nsig}/8 significant'
    return word,note,{'nsig':nsig,'ninsig':ninsig,'pos_sig':pos_sig,'median_std':float(np.nanmedian(d.std_beta))}

def verdict_legor(gen,var):
    res={}
    words={}
    for reg,name in [('l_ger','German'),('l_sca','Scandinavian')]:
        d=sel('legor',gen,var,reg); t=tally(d,+1)
        persists=(t['nsig_sign']>=4)
        reverses=(t['nopp_sig']>=3 and t['nsig_sign']==0)
        weakens_sign=(t['nsign']>=5)
        if reverses: w='reverses'
        elif persists: w='persists'
        elif weakens_sign: w='weakens'
        else: w='mixed'
        words[name]=w; res[name]=t
    if words['German']==words['Scandinavian']:
        word=words['German']
    else:
        word=f"mixed (split: German {words['German']}, Scandinavian {words['Scandinavian']})"
    return word,words,res

rows=[]
for role in ['war','parl']:
    for gen in ['X0','X1']:
        for var in ['between','within']:
            w,ph,t,anchor,atten=verdict_capacity(role,gen,var)
            rows.append({'row':f'R-{role}','generation':gen,'variant':var,'verdict':w,
              'phrase':ph,'nsign':t['nsign'],'nsig_sign':t['nsig_sign'],
              'nlegal_sig':t['nlegal_sig'],'nfiscal_sig':t['nfiscal_sig'],'nopp_sig':t['nopp_sig'],
              'median_std_beta':round(t['median_std'],4),'paper_era_std_anchor':round(anchor,4) if not np.isnan(anchor) else None,
              'attenuated_half':bool(atten),
              'basis':f"{t['nsig_sign']}/8 sign&p<.05 ({t['nlegal_sig']} legal,{t['nfiscal_sig']} fiscal); {t['nsign']}/8 paper-sign",
              'seams':'S1(GRD) S4(WGI/ICRG) ' + ('S5(Y2/Y3 excluded from count)' if False else '')})
for gen in ['X0','X1']:
    for var in ['between','within']:
        w,note,t=verdict_dem(gen,var)
        rows.append({'row':'R-dem','generation':gen,'variant':var,'verdict':w,'phrase':note,
          'nsign':None,'nsig_sign':t['nsig'],'nlegal_sig':None,'nfiscal_sig':None,'nopp_sig':None,
          'median_std_beta':round(t['median_std'],4),'paper_era_std_anchor':None,'attenuated_half':None,
          'basis':note,'seams':'graded vs null (paper democracy row is null-to-weak)'})
for gen in ['X0','X1']:
    for var in ['between','within']:
        w,words,res=verdict_legor(gen,var)
        rows.append({'row':'R-legor','generation':gen,'variant':var,'verdict':w,
          'phrase':f"German={words['German']}, Scandinavian={words['Scandinavian']}",
          'nsign':None,'nsig_sign':None,'nlegal_sig':None,'nfiscal_sig':None,'nopp_sig':None,
          'median_std_beta':None,'paper_era_std_anchor':None,'attenuated_half':None,
          'basis':f"German {res['German']['nsig_sign']}/8 sig, Scand {res['Scandinavian']['nsig_sign']}/8 sig",
          'seams':'joint German+Scandinavian row'})
sc=pd.DataFrame(rows)
sc.to_csv(RES+"scorecard.csv",index=False)
pd.set_option('display.width',240); pd.set_option('display.max_columns',30)
print(sc[['row','generation','variant','verdict','phrase','basis']].to_string())
PY_DONE=True
