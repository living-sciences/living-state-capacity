#!/usr/bin/env python3
"""Block A3: succession gates G1-G5 -> results/gates.json."""
import pandas as pd, numpy as np, json
SD="/workspace/eval/followup_staging/shared-data/"
OUT="data/"; RES="/workspace/eval/followup/001-001-living-update/results/"

def kappa(a,b):
    a=np.asarray(a); b=np.asarray(b)
    po=(a==b).mean()
    # expected agreement
    pe=0.0
    for v in [0,1]:
        pe+=(a==v).mean()*(b==v).mean()
    return po,(po-pe)/(1-pe) if (1-pe)>0 else np.nan

def wdi_long(path, name):
    j=json.load(open(path))
    recs=j[1]
    rows=[(r.get('countryiso3code'), int(r['date']), r['value']) for r in recs if r.get('value') is not None and r.get('countryiso3code')]
    return pd.DataFrame(rows,columns=['iso3','year',name])

# ---- build yearly dummies panel ----
vd=pd.read_csv(OUT+"vdem_yearly.csv")        # iso3,year,e_polity2,e_lexical_index
br=pd.read_csv(OUT+"br_yearly.csv")          # iso3,year,dd,parl_br
pp=pd.read_csv(OUT+"pillars_parl_yearly.csv")# iso3,year,parl_dem

gates={}
# G1 parliamentary chain, 1950-2016
P=pp[(pp.year>=1950)&(pp.year<=2016)].dropna(subset=['parl_dem'])
M=P.merge(br[['iso3','year','dd']],on=['iso3','year'],how='inner').merge(
        vd[['iso3','year','e_polity2','e_lexical_index']],on=['iso3','year'],how='left')
m1=M.dropna(subset=['dd','e_polity2'])
chain1=((m1.dd==0)&(m1.e_polity2>0)).astype(int)
a1,k1=kappa(chain1, m1.parl_dem.astype(int))
m2=M.dropna(subset=['dd','e_lexical_index'])
chain2=((m2.dd==0)&(m2.e_lexical_index>=4)).astype(int)
a2,k2=kappa(chain2, m2.parl_dem.astype(int))
g1_pass = (a1>=0.99 and k1>=0.97) and (a2>=0.985 and k2>=0.96)
gates['G1']={'label':'parliamentary chain','rule':'agreement of BR(DD=0)&(e_polity2>0) vs Pillars 2 parl_dem, 1950-2016 overlap; and BR(DD=0)&(LIED>=4) vs same',
  'threshold':'>= 0.99 and kappa >= 0.97; >= 0.985 and kappa >= 0.96 [PREVIEW-CALIBRATED: 0.9982/k0.9942 (n=8,355); 0.9939/k0.9802 (n=8,369)]',
  'computed':{'agree_polity':round(a1,4),'kappa_polity':round(k1,4),'n_polity':int(len(m1)),
              'agree_lied':round(a2,4),'kappa_lied':round(k2,4),'n_lied':int(len(m2))},
  'pass':bool(g1_pass),'fail_branch':'parliamentary extension ends 2016 (parl_dem only); stated on card'}

# G2 democracy chain 1950-2018: (LIED>=4) vs (polity2>0)
D=vd[(vd.year>=1950)&(vd.year<=2018)].dropna(subset=['e_lexical_index','e_polity2'])
a,k=kappa((D.e_lexical_index>=4).astype(int),(D.e_polity2>0).astype(int))
g2_pass=(a>=0.90 and k>=0.80)
gates['G2']={'label':'democracy chain','rule':'agreement of (LIED>=4) vs (e_polity2>0), 1950-2018',
  'threshold':'>= 0.90 and kappa >= 0.80 [PREVIEW-CALIBRATED: 0.9245/k0.8493 (n=9,533)]',
  'computed':{'agree':round(a,4),'kappa':round(k,4),'n':int(len(D))},
  'pass':bool(g2_pass),'fail_branch':'democracy extension ends 2018'}

# G3 war splice, COW vs UCDP type1+2, 1946-2006
F=pd.read_csv(RES+"frame_update.csv")
isos=sorted(set(F.iso3.dropna()))
cow=pd.read_csv(OUT+"cow_extwar_yearly.csv")      # iso3,year (atwar)
uc=pd.read_csv(OUT+"ucdp_extwar_yearly.csv")      # iso3,year
cowset=set(zip(cow.iso3,cow.year)); ucset=set(zip(uc.iso3,uc.year))
rows=[]
for iso in isos:
    for y in range(1946,2007):
        rows.append(( int((iso,y) in cowset), int((iso,y) in ucset) ))
ca=np.array([r[0] for r in rows]); ua=np.array([r[1] for r in rows])
a3=(ca==ua).mean()
g3_pass=a3>=0.95
gates['G3']={'label':'war splice','rule':'country-year external-war dummy agreement, COW v4 vs UCDP type 1+2 splice, 1946-2006 overlap',
  'threshold':'>= 0.95 [SPEC-DECLARED, no preview. Reference note, not a preview: the Pillars-2 codebook\'s reported 0.984 is the CIVIL-war dummy\'s vintage-update agreement (old Pillars vintage vs its UCDP-19.1 recreation, internal conflict) - a same-source-family reference on a different conflict type, not an external-war COW-vs-UCDP cross-source quantity]',
  'computed':{'agree':round(float(a3),4),'n':int(len(rows))},
  'pass':bool(g3_pass),'fail_branch':'X2 column not built; X1 (avg_war00) unaffected'}

# G4 credit splice, corr(GFDD di01, WDI FS.AST.PRVT.GD.ZS) 2000-2021 pooled
g=pd.read_excel(SD+"gfdd/GFDD_sept2022.xlsx", sheet_name="Data - August 2022")[['iso3','year','di01']]
g['di01']=pd.to_numeric(g.di01,errors='coerce')
wdi=wdi_long(SD+"wdi/wdi_FS.AST.PRVT.GD.ZS.json",'wdicred')
mm=g.merge(wdi,on=['iso3','year'],how='inner')
mm=mm[(mm.year>=2000)&(mm.year<=2021)].dropna(subset=['di01','wdicred'])
c4=np.corrcoef(mm.di01,mm.wdicred)[0,1]
g4_pass=c4>=0.90
gates['G4']={'label':'credit splice','rule':'corr(GFDD di01, WDI FS.AST.PRVT.GD.ZS), 2000-2021 overlap, pooled',
  'threshold':'>= 0.90 [SPEC-DECLARED, no preview]',
  'computed':{'corr':round(float(c4),4),'n':int(len(mm))},
  'pass':bool(g4_pass),'fail_branch':'Y1 stays 2000-2021 (GFDD only); the WDI-extended sensitivity is dropped, stated'}

# G5 frame sanity: per-column N after merge (estimation samples computed later; here report outcome coverage within legal-origin frame)
lo=F[F[['l_eng','l_fre','l_ger','l_sca','l_soc']].notna().any(axis=1)]
colN={c:int(lo[c].notna().sum()) for c in ['Y1','Y4','Y5','Y6','Y7','Y8','Y9','Y10']}
gates['G5']={'label':'frame sanity','rule':'per-column N >= 80 after merge; X0 vs Phase-1 X agreement = exact on Branch D',
  'threshold':'N>=80 per column; expected N ~ 150-190',
  'computed':{'col_N_within_legalorigin_frame':colN},
  'pass':bool(all(v>=80 for v in colN.values())),
  'fail_branch':'a column under N=80 grades not separable (coverage), never silently dropped',
  'branch_note':'Branch R: deposit pending, X0-vs-Phase-1 exactness check N/A (no Phase-1 reconstruction estimate file on disk)'}

json.dump(gates, open(RES+"gates.json","w"), indent=2)
for g,v in gates.items():
    print(g, "PASS" if v['pass'] else "FAIL", v['computed'])
