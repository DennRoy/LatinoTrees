#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Look for samples via:
#
#    https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2F*%2FRunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_*%2FMINIAODSIM
#    https://cmsweb.cern.ch/das/request?view=plain&limit=150&instance=prod%2Fglobal&input=dataset%3D%2F*%2FRunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_*%2FMINIAODSIM
#    https://cmsweb.cern.ch/das/request?view=plain&limit=150&instance=prod%2Fglobal&input=dataset%3D%2F*%2FRunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_*%2FMINIAODSIM
#
# And for signals:
#   https://cmsweb.cern.ch/das/request?view=plain&limit=150&instance=prod%2Fglobal&input=dataset%3D%2F*%2FRunIISpring16MiniAODv2*mcRun2_asymptotic_2016_*%2FMINIAODSIM       
#
# Only 125:
#   https://cmsweb.cern.ch/das/request?view=plain&limit=150&instance=prod%2Fglobal&input=dataset%3D%2FGluGlu*125*%2FRunIISpring16MiniAODv2*mcRun2_asymptotic_2016_*%2FMINIAODSIM
#
# For GT and more, see https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alicia
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## W+jets >> Alicia                   
samples['WJetsToLNu']                = ['/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                 ['label=WJetsToLNu',             'id=00001', 'doMCweights=True']]
#samples['WJetsToLNu_HT100_200']     = ['/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=WJetsToLNuHT100to200',   'id=20001', 'doMCweights=True']]
samples['WJetsToLNu_HT100_200_ext1'] = ['/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=WJetsToLNuHT100to200',   'id=20001', 'doMCweights=True']]
samples['WJetsToLNu_HT200_400']      = ['/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=WJetsToLNuHT200to400',   'id=20002', 'doMCweights=True']]
samples['WJetsToLNu_HT200_400_ext1'] = ['/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=WJetsToLNuHT200to400',   'id=20002', 'doMCweights=True']]
samples['WJetsToLNu_HT400_600']      = ['/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM ',     ['label=WJetsToLNuHT400to600',   'id=20003', 'doMCweights=True']]
#samples['WJetsToLNu_HT600_inf']     = ['/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                ['label=WJetsToLNuHT600toinf',   'id=20004', 'doMCweights=True']]
samples['WJetsToLNu_HT600_800']      = ['/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM ',     ['label=WJetsToLNuHT600to800',   'id=20005', 'doMCweights=True']]
#samples['WJetsToLNu_HT800_1200']    = ['/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',               ['label=WJetsToLNuHT800to1200',  'id=20006', 'doMCweights=True']]
samples['WJetsToLNu_HT1200_2500']    = ['/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM ',   ['label=WJetsToLNuHT1200to2500', 'id=20007', 'doMCweights=True']]
samples['WJetsToLNu_HT2500_inf']     = ['/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=WJetsToLNuHT2500toinf',  'id=20008', 'doMCweights=True']]


## DY >> Alicia
samples['DYJetsToLL_M-10to50-LO']           = ['/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                   ['label=DYJetsToLL_M-10to50-LO',          'id=30002',     'doMCweights=True']]
samples['DYJetsToLL_M-10to50']              = ['/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                  ['label=DYJetsToLL_M-10to50',             'id=00002',     'doMCweights=True']]
samples['DYJetsToLL_M-50']                  = ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                      ['label=DYJetsToLL_M-50',                 'id=00003',     'doMCweights=True']]
samples['DYJetsToLL_M-5to50-LO']            = ['/DYJetsToLL_M-5to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                    ['label=DYJetsToLL_M-5to50-LO',           'id=30002',     'doMCweights=True']]
samples['DYJetsToLL_M-50-LO-ext1']          = ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',                  ['label=DYJetsToLL_M-50-LO-ext1',         'id=30003',     'doMCweights=True']]
samples['DYJetsToLL_M-50_HT-100to200_ext1'] = ['/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM ',     ['label=DYJetsToLL_M-50_HT-100to200_ext', 'id=001002001', 'doMCweights=True']]
samples['DYJetsToLL_M-50_HT-200to400_ext1'] = ['/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM ',     ['label=DYJetsToLL_M-50_HT-200to400_ext', 'id=002004001', 'doMCweights=True']]
samples['DYJetsToLL_M-50_HT-400to600_ext1'] = ['/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM ',     ['label=DYJetsToLL_M-50_HT-400to600_ext', 'id=004006001', 'doMCweights=True']]
samples['DYJetsToLL_M-50_HT-600toInf_ext1'] = ['/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM ',     ['label=DYJetsToLL_M-50_HT-600toInf_ext', 'id=006000001', 'doMCweights=True']]
samples['DYJetsToLL_M-50_HT-600toInf']      = ['/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM  ',         ['label=DYJetsToLL_M-50_HT-600toInf',     'id=00600000',  'doMCweights=True']]
samples['DYJetsToEE_Pow']                   = ['/DYToEE_NNPDF30_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                                          ['label=DYJetsToEE_POW',                  'id=30004',     'doMCweights=True']]
samples['DYJetsToTT_MuEle_M-50']            = ['/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=DYJetsToTT_MuEle_M-50',           'id=30005',     'doMCweights=True']]


## VV >> Alicia
samples['WW-LO']        = ['/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=WW-LO',        'id=00004', 'doMCweights=True']]
samples['WWTo2L2Nu']    = ['/WWTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',        ['label=WWTo2L2Nu',    'id=00004', 'doMCweights=True']]
samples['WWToLNuQQ']    = ['/WWToLNuQQ_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',        ['label=WWToLNuQQ',    'id=00031', 'doMCweights=True']]
samples['WWToLNuQQext'] = ['/WWToLNuQQ_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',   ['label=WWToLNuQQext', 'id=00033', 'doMCweights=True']]
samples['WWTo4Q']       = ['/WWTo4Q_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',           ['label=WWTo4Q',       'id=00034', 'doMCweights=True']]




#--------------------
# Sangil
#--------------------


samples['WZ']          = ['/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                  ['label=WZ',        'id=00005', 'doLHE=False']]
samples['WZTo3LNu']    = ['/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=WZTo3LNu',  'id=00006', 'doMCweights=True']]
samples['WZTo3LNu_mllmin01']    = ['/WZTo3LNu_mllmin01_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=WZTo3LNu_mllmin01',  'id=00006', 'doMCweights=True']]
#samples['WZJets']     = ['/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM', ['label=WZJets',    'id=00007', 'doMCweights=True']]
samples['WZTo2L2Q']    = ['/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',    ['label=WZTo2L2Q',  'id=00008', 'doMCweights=True']]
samples['WZTo1L3Nu']   = ['/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',   ['label=WZTo1L3Nu',  'id=00008', 'doMCweights=True']]
samples['WZTo1L1Nu2Q'] = ['/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=WZTo1L1Nu2Q',  'id=00008', 'doMCweights=True']]

samples['VVTo2L2Nu']   = ['/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',   ['label=VVTo2L2Nu', 'id=00032', 'doMCweights=True']]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ankita
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## ggWW >> Ankita
samples['GluGluWWTo2L2Nu_MCFM']      = ['/GluGluWWTo2L2Nu_MCFM_13TeV/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',       ['label=GluGluWWTo2L2Nu_MCFM', 'id=00033', 'doMCweights=True', 'metNoHF=\"\"', 'LHEweightSource=source', 'LHERunInfo=source' ]]
samples['GluGluWWTo2L2NuHiggs_MCFM'] = ['/GluGluWWTo2L2Nu_HInt_MCFM_13TeV/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',   ['label=GluGluWWTo2L2NuHiggs_MCFM', 'id=00034', 'doMCweights=True','LHEweightSource=source', 'LHERunInfo=source']]





## ZZ >> Ankita
samples['ZZ']         = ['/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                  ['label=ZZ',        'id=00009', 'doLHE=False']]
samples['ZZTo2L2Q']   = ['/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',    ['label=ZZTo2L2Q',  'id=00010', 'doMCweights=True']]
samples['ZZTo4L']     = ['/ZZTo4L_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                    ['label=ZZTo4L',    'id=00011', 'doMCweights=True']]
samples['ZZTo2L2Nu']  = ['/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                 ['label=ZZTo2L2Nu', 'id=00030', 'doMCweights=True']]
#samples['ggZZ4e']     = ['/GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',       ['label=ggZZ4e',    'id=00040', 'LHEweightSource=source']]
#samples['ggZZ4m']     = ['/GluGluToZZTo4mu_BackgroundOnly_13TeV_MCFM/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',      ['label=ggZZ4m',    'id=00041', 'LHEweightSource=source']]
#samples['ggZZ4t']     = ['/GluGluToZZTo4tau_BackgroundOnly_13TeV_MCFM/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',     ['label=ggZZ4t',    'id=00042', 'LHEweightSource=source']]
#samples['ggZZ2e2m']   = ['/GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',    ['label=ggZZ2e2m',  'id=00043', 'LHEweightSource=source']]
#samples['ggZZ2e2t']   = ['/GluGluToZZTo2e2tau_BackgroundOnly_13TeV_MCFM/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',   ['label=ggZZ2e2t',  'id=00044', 'LHEweightSource=source']]
#samples['ggZZ2m2t']   = ['/GluGluToZZTo2mu2tau_BackgroundOnly_13TeV_MCFM/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=ggZZ2m2t',  'id=00045', 'LHEweightSource=source']]


## Single top >> Ankita
samples['ST_t-channel_antitop'] = ['/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=ST_t-channel_antitop', 'id=00012', 'doMCweights=True', 'LHEweightSource=source', 'LHERunInfo=source']]
#samples['ST_t-channel_top']     = ['/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',     ['label=ST_t-channel_top',     'id=00013', 'doMCweights=True', 'LHEweightSource=source']]
#samples['ST_t-channel']         = ['/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',       ['label=ST_t-channel',         'id=00014', 'doMCweights=True']]
samples['ST_tW_antitop']        = ['/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=ST_tW_antitop',        'id=00015', 'doMCweights=True']]
samples['ST_tW_top']            = ['/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',         ['label=ST_tW_top',            'id=00016', 'doMCweights=True']]
samples['ST_s-channel']         = ['/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',       ['label=ST_s-channel',         'id=00022', 'doMCweights=True']]
samples['ST_tW_antitop_noHad']            = ['/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=ST_tW_antitop_noHad',      'id=00024', 'doMCweights=True']]
samples['ST_tW_top_noHad']            = ['/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=ST_tW_top_noHad',      'id=00025', 'doMCweights=True']]




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Top >> Ankita
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#samples['TT']                          = ['/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                   ['label=TT',                           'id=00017', 'doMCweights=True']]
samples['TTJets']                       = ['/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=TTJets',                       'id=00018', 'doMCweights=True']]
#samples['TTTo2L2Nu']                   = ['/TTTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM',                                            ['label=TTTo2L2Nu',                    'id=00019', 'doMCweights=True']]
samples['TTTo2L2Nu_ext1']               = ['/TTTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',                                  ['label=TTTo2L2Nu',                    'id=00019', 'doMCweights=True']]
samples['TTWJetsToLNu']                 = ['/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=TTWJetsToLNu',                 'id=00020', 'doMCweights=True']]
samples['TTZToLLNuNu_M-10']             = ['/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',         ['label=TTZToLLNuNu_M-10',             'id=00021', 'doMCweights=True']]
samples['TTWJetsToQQ']                  = ['/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=TTWJetsToQQ',                  'id=00022', 'doMCweights=True']]
#samples['TTJetsDiLep-LO']              = ['/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM',                   ['label=TTJetsDiLep-LO',               'id=00023', 'doMCweights=True']]
samples['TTJetsDiLep-LO-ext1']          = ['/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM',              ['label=TTJetsDiLep-LO-ext1',          'id=00026', 'doMCweights=True']]
samples['TTZToQQ']                      = ['/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                  ['label=TTZToQQ',                      'id=00027', 'doMCweights=True']]
samples['TTZjets']                      = ['/ttZJets_13TeV_madgraphMLM/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                                    ['label=TTZjets',                      'id=00027', 'doMCweights=True']]
samples['TTTo2L2Nu_alphaS01108']        = ['/TTTo2L2Nu_TuneCUETP8M1T4_alphaS01108_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',              ['label=TTTo2L2Nu_alphaS01108',        'id=00028', 'doMCweights=True']]
samples['TTToSemiLeptonic_alphaS01108'] = ['/TTToSemiLeptonic_TuneCUETP8M1T4_alphaS01108_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',       ['label=TTToSemiLeptonic_alphaS01108', 'id=00029', 'doMCweights=True']]




### GluGluH >> Ankita

#samples['GluGluHToWWTo2L2Nu_Mlarge']       = ['/GluGluHToWWTo2L2Nu_M125_W10_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv1-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_Mlarge',       'id=01125', 'doMCweights=True']]


samples['GluGluHToWWTo2L2Nu_alternative_M120']    = ['/GluGluHToWWTo2L2Nu_M120_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_alternative_M120',       'id=01120', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_alternative_M125']    = ['/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_alternative_M125',       'id=01125', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_alternative_M130']    = ['/GluGluHToWWTo2L2Nu_M130_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_alternative_M130',       'id=01130', 'doMCweights=True']]

##samples['GluGluHToWWTo2L2Nu_M120']       = ['/GluGluHToWWTo2L2Nu_M120_13TeV_powheg_JHUgenv628_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M120',       'id=01120', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M124']       = ['/GluGluHToWWTo2L2Nu_M124_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M124',       'id=01124', 'doMCweights=True']]
##samples['GluGluHToWWTo2L2Nu_M125']       = ['/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M125',       'id=01125', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M126']       = ['/GluGluHToWWTo2L2Nu_M126_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M126',       'id=01126', 'doMCweights=True']]
##samples['GluGluHToWWTo2L2Nu_M130']       = ['/GluGluHToWWTo2L2Nu_M130_13TeV_powheg_JHUgenv628_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M130',       'id=01130', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M135']       = ['/GluGluHToWWTo2L2Nu_M135_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M135',       'id=01135', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M140']       = ['/GluGluHToWWTo2L2Nu_M140_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M140',       'id=01140', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M145']       = ['/GluGluHToWWTo2L2Nu_M145_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M145',       'id=01145', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M150']       = ['/GluGluHToWWTo2L2Nu_M150_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M150',       'id=01150', 'doMCweights=True']] 
samples['GluGluHToWWTo2L2Nu_M155']       = ['/GluGluHToWWTo2L2Nu_M155_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M155',       'id=01155', 'doMCweights=True']] 
samples['GluGluHToWWTo2L2Nu_M160']       = ['/GluGluHToWWTo2L2Nu_M160_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M160',       'id=01160', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M165']       = ['/GluGluHToWWTo2L2Nu_M165_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M165',       'id=01165', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M170']       = ['/GluGluHToWWTo2L2Nu_M170_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M170',       'id=01170', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M175']       = ['/GluGluHToWWTo2L2Nu_M175_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M175',       'id=01175', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M180']       = ['/GluGluHToWWTo2L2Nu_M180_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M180',       'id=01180', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M190']       = ['/GluGluHToWWTo2L2Nu_M190_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M190',       'id=01190', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M200']       = ['/GluGluHToWWTo2L2Nu_M200_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M200',       'id=01200', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M210']       = ['/GluGluHToWWTo2L2Nu_M210_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M210',       'id=01210', 'doMCweights=True']]
#samples['GluGluHToWWTo2L2Nu_M230']      = ['/GluGluHToWWTo2L2Nu_M230_13TeV_powheg_JHUgenv628_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',             ['label=GluGluHToWWTo2L2Nu_M230',       'id=01230', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M250']       = ['/GluGluHToWWTo2L2Nu_M250_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M250',       'id=01250', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M300']       = ['/GluGluHToWWTo2L2Nu_M300_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M300',       'id=01300', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M350']       = ['/GluGluHToWWTo2L2Nu_M350_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M350',       'id=01350', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M400']       = ['/GluGluHToWWTo2L2Nu_M400_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M400',       'id=01400', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M450']       = ['/GluGluHToWWTo2L2Nu_M450_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M450',       'id=01450', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M500']       = ['/GluGluHToWWTo2L2Nu_M500_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M500',       'id=01500', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M550']       = ['/GluGluHToWWTo2L2Nu_M550_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M550',       'id=01550', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M600']       = ['/GluGluHToWWTo2L2Nu_M600_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M600',       'id=01600', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M650']       = ['/GluGluHToWWTo2L2Nu_M650_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M650',       'id=01650', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M700']       = ['/GluGluHToWWTo2L2Nu_M700_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M700',       'id=01700', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M750']       = ['/GluGluHToWWTo2L2Nu_M750_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M750',       'id=01750', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M800']       = ['/GluGluHToWWTo2L2Nu_M800_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M800',       'id=01800', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M900']       = ['/GluGluHToWWTo2L2Nu_M900_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M900',       'id=01900', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M1000']      = ['/GluGluHToWWTo2L2Nu_M1000_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=GluGluHToWWTo2L2Nu_M1000',      'id=02000', 'doMCweights=True']]

samples['GluGluHToWWTo2L2Nu_M750_NWA']   = ['/GluGluHToWWTo2L2Nu_M750_NWA_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_M750_NWA',       'id=017501', 'doMCweights=True']]


samples['GluGluHToWWTo2L2Nu_JHUGen698_M300']       = ['/GluGluHToWWTo2L2Nu_M300_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M300',       'id=01300', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M350']       = ['/GluGluHToWWTo2L2Nu_M350_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M350',       'id=01350', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M400']       = ['/GluGluHToWWTo2L2Nu_M400_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M400',       'id=01400', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M450']       = ['/GluGluHToWWTo2L2Nu_M450_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M450',       'id=01450', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M500']       = ['/GluGluHToWWTo2L2Nu_M500_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M500',       'id=01500', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M550']       = ['/GluGluHToWWTo2L2Nu_M550_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M550',       'id=01550', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M600']       = ['/GluGluHToWWTo2L2Nu_M600_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M600',       'id=01600', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M650']       = ['/GluGluHToWWTo2L2Nu_M650_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M650',       'id=01650', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M700']       = ['/GluGluHToWWTo2L2Nu_M700_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M700',       'id=01700', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M750']       = ['/GluGluHToWWTo2L2Nu_M750_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M750',       'id=01750', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M800']       = ['/GluGluHToWWTo2L2Nu_M800_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M800',       'id=01800', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M900']       = ['/GluGluHToWWTo2L2Nu_M900_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M900',       'id=01900', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M1000']       = ['/GluGluHToWWTo2L2Nu_M1000_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M1000',       'id=011000', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M1500']       = ['/GluGluHToWWTo2L2Nu_M1500_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M1500',       'id=011500', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M2000']       = ['/GluGluHToWWTo2L2Nu_M2000_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M2000',       'id=012000', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M2500']       = ['/GluGluHToWWTo2L2Nu_M2500_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M2500',       'id=012500', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_JHUGen698_M3000']       = ['/GluGluHToWWTo2L2Nu_M3000_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=GluGluHToWWTo2L2Nu_JHUGen698_M3000',       'id=013000', 'doMCweights=True']]



samples['GluGluHToWWTo2L2NuAMCNLO_M125'] = ['/GluGluHToWWTo2L2Nu_M125_13TeV_amcatnloFXFX_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',   ['label=GluGluHToWWTo2L2NuAMCNLO_M125', 'id=07125', 'doMCweights=True']]
samples['GluGluHToWWTo2L2NuPowheg_M125'] = ['/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',          ['label=GluGluHToWWTo2L2NuPowheg_M125', 'id=07125', 'doMCweights=True']]
samples['GluGluHToWWToLNuQQ_M450']       = [' /GluGluHToWWToLNuQQ_M450_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM ',  ['label=GluGluHToWWToLNuQQ_M450',       'id=60450', 'doMCweights=True']]
samples['GluGluHToWWToLNuQQ_M650']       = ['/GluGluHToWWToLNuQQ_M650_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=GluGluHToWWToLNuQQ_M650',       'id=60650', 'doMCweights=True']]
samples['GluGluHToWWToLNuQQ_M1000']      = ['/GluGluHToWWToLNuQQ_M1000_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=GluGluHToWWToLNuQQ_M1000',      'id=61000', 'doMCweights=True']]
#samples['GluGluHToZZTo4L_M125']          = ['/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISpring16MiniAODv1-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM',     ['label=GluGluHToZZTo4L_M125',          'id=11125', 'doMCweights=True']]
###samples['GluGluHToTauTau_M120']          = ['/GluGluHToTauTau_M120_13TeV_powheg_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',            ['label=GluGluHToTauTau_M120',          'id=21120', 'doMCweights=True']]
samples['GluGluHToTauTau_M125']          = ['/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',            ['label=GluGluHToTauTau_M125',          'id=21125', 'doMCweights=True']]
###samples['GluGluHToTauTau_M130']          = ['/GluGluHToTauTau_M130_13TeV_powheg_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',            ['label=GluGluHToTauTau_M130',          'id=21130', 'doMCweights=True']]

samples['GluGluHToWWTo2L2Nu_M125_herwigpp'] = ['/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=GluGluHToWWTo2L2Nu_M125_herwigpp', 'id=07125', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M125_CUETDown'] = ['/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=GluGluHToWWTo2L2Nu_M125_CUETDown', 'id=07125', 'doMCweights=True']]
samples['GluGluHToWWTo2L2Nu_M125_CUETUp']   = ['/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=GluGluHToWWTo2L2Nu_M125_CUETUp', 'id=07125', 'doMCweights=True']]



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Arun
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### WH Inclusive============

samples['HWminusJ_HToWW_M125']     = ['/HWminusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',  ['label=HWminusJ_HToWW_M125',     'id=02125', 'doMCweights=True']]
samples['HWminusJ_HToWW_M130']     = ['/HWminusJ_HToWW_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',  ['label=HWminusJ_HToWW_M130',     'id=02130', 'doMCweights=True']]
samples['HWminusJ_HToWW_M120']     = ['/HWminusJ_HToWW_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',  ['label=HWminusJ_HToWW_M120',     'id=02120', 'doMCweights=True']]
samples['HWplusJ_HToWW_M120']      = ['/HWplusJ_HToWW_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',   ['label=HWplusJ_HToWW_M120',      'id=03120', 'doMCweights=True']]
samples['HWplusJ_HToWW_M125']      = ['/HWplusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',   ['label=HWplusJ_HToWW_M125',      'id=03125', 'doMCweights=True']]
samples['HWplusJ_HToWW_M130']      = ['/HWplusJ_HToWW_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',   ['label=HWplusJ_HToWW_M130',      'id=03130', 'doMCweights=True']]
samples['HWminusJ_HToTauTau_M120'] = ['/WminusHToTauTau_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HWminusJ_HToTauTau_M120', 'id=52120', 'doMCweights=True']]
samples['HWminusJ_HToTauTau_M125'] = ['/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HWminusJ_HToTauTau_M125', 'id=52125', 'doMCweights=True']]
samples['HWminusJ_HToTauTau_M130'] = ['/WminusHToTauTau_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HWminusJ_HToTauTau_M130', 'id=52130', 'doMCweights=True']]
samples['HWplusJ_HToTauTau_M120']  = ['/WplusHToTauTau_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=HWplusJ_HToTauTau_M120',  'id=53120', 'doMCweights=True']]
samples['HWplusJ_HToTauTau_M125']  = ['/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=HWplusJ_HToTauTau_M125',  'id=53125', 'doMCweights=True']]
samples['HWplusJ_HToTauTau_M130']  = ['/WplusHToTauTau_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=HWplusJ_HToTauTau_M130',  'id=53130', 'doMCweights=True']]


#### ZH Inclusive ======== 

samples['HZJ_HToWW_M120']     = ['/HZJ_HToWW_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',  ['label=HZJ_HToWW_M120',     'id=06120', 'doMCweights=True']]
samples['HZJ_HToWW_M125']     = ['/HZJ_HToWW_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',  ['label=HZJ_HToWW_M125',     'id=06125', 'doMCweights=True']]
samples['HZJ_HToWW_M130']     = ['/HZJ_HToWW_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',  ['label=HZJ_HToWW_M130',     'id=06130', 'doMCweights=True']]
samples['HZJ_HToTauTau_M120'] = ['/ZHToTauTau_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HZJ_HToTauTau_M120', 'id=53120', 'doMCweights=True']]
samples['HZJ_HToTauTau_M125'] = ['/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HZJ_HToTauTau_M125', 'id=53125', 'doMCweights=True']]
samples['HZJ_HToTauTau_M130'] = ['/ZHToTauTau_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HZJ_HToTauTau_M130', 'id=53130', 'doMCweights=True']]


#### ttH >> Daniel
###samples['ttHJetToNonbb_M120']   = ['/ttHJetToNonbb_M120_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',      ['label=ttHJetToNonbb_M120',   'id=04120', 'doMCweights=True']]
###samples['ttHJetToNonbb_M125']   = ['/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',      ['label=ttHJetToNonbb_M125',   'id=04125', 'doMCweights=True']]
###samples['ttHJetToNonbb_M130']   = ['/ttHJetToNonbb_M130_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',      ['label=ttHJetToNonbb_M130',   'id=04130', 'doMCweights=True']]
###samples['ttHJetToNonbb_M125_A'] = ['/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2_ext1-v1/MINIAODSIM', ['label=ttHJetToNonbb_M125_A', 'id=04125', 'doMCweights=True']]
###samples['ttHJetTobb_M120']      = ['/ttHJetTobb_M120_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',         ['label=ttHJetTobb_M120',      'id=34120', 'doMCweights=True']]
###samples['ttHJetTobb_M125']      = ['/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',         ['label=ttHJetTobb_M125',      'id=34125', 'doMCweights=True']]
###samples['ttHJetTobb_M130']      = ['/ttHJetTobb_M130_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',         ['label=ttHJetTobb_M130',      'id=34130', 'doMCweights=True']] 

samples['ttHJetToNonbb_M125']   = ['/ttHToNonbb_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=ttHJetToNonbb_M125',   'id=04125', 'doMCweights=True']]

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Khakim
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### bbH
samples['bbHToWWTo2L2Nu_M125_yb2']  = ['/bbHToWWTo2L2Nu_M-125_4FS_yb2_13TeV_amcatnlo/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=bbHToWWTo2L2Nu_M125_yb2','id=051198', 'doMCweights=True','LHEweightSource=source', 'LHERunInfo=source']]
samples['bbHToWWTo2L2Nu_M125_ybyt'] = ['/bbHToWWTo2L2Nu_M-125_4FS_ybyt_13TeV_amcatnlo/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=bbHToWWTo2L2Nu_M125_ybyt','id=051199', 'doMCweights=True','LHEweightSource=source', 'LHERunInfo=source']]

#### VBFH >> Khakim
samples['VBFHToWWTo2L2Nu_alternative_M120'] = ['/VBFHToWWTo2L2Nu_M120_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_alternative_M120','id=05120', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_alternative_M125'] = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_alternative_M125', 'id=05125', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_alternative_M130'] = ['/VBFHToWWTo2L2Nu_M130_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_alternative_M130', 'id=05130', 'doMCweights=True']]

samples['VBFHToWWTo2L2Nu_M115']         = ['/VBFHToWWTo2L2Nu_M115_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M115', 'id=05115', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M120']         = ['/VBFHToWWTo2L2Nu_M120_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M120', 'id=05120', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M124']         = ['/VBFHToWWTo2L2Nu_M124_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M124', 'id=05124', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M125']         = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M125',     'id=05125', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M126']         = ['/VBFHToWWTo2L2Nu_M126_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M126',     'id=05126', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M130']         = ['/VBFHToWWTo2L2Nu_M130_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M130',     'id=05130', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M135']         = ['/VBFHToWWTo2L2Nu_M135_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M135',     'id=05135', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M140']         = ['/VBFHToWWTo2L2Nu_M140_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M140',     'id=05140', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M145']         = ['/VBFHToWWTo2L2Nu_M145_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M145',     'id=05145', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M150']         = ['/VBFHToWWTo2L2Nu_M150_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M150',     'id=05150', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M155']         = ['/VBFHToWWTo2L2Nu_M155_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M155',     'id=05155', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M160']         = ['/VBFHToWWTo2L2Nu_M160_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M160',     'id=05160', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M165']         = ['/VBFHToWWTo2L2Nu_M165_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M165',     'id=05165', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M170']         = ['/VBFHToWWTo2L2Nu_M170_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M170',     'id=05170', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M175']         = ['/VBFHToWWTo2L2Nu_M175_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M175',     'id=05175', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M180']         = ['/VBFHToWWTo2L2Nu_M180_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M180',     'id=05180', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M190']         = ['/VBFHToWWTo2L2Nu_M190_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M190',     'id=05190', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M200']         = ['/VBFHToWWTo2L2Nu_M200_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M200',     'id=05200', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M210']         = ['/VBFHToWWTo2L2Nu_M210_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M210',     'id=05210', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M230']         = ['/VBFHToWWTo2L2Nu_M230_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M230',     'id=05230', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M250']         = ['/VBFHToWWTo2L2Nu_M250_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M250',     'id=05250', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M270']         = ['/VBFHToWWTo2L2Nu_M270_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M270',     'id=05270', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M300']         = ['/VBFHToWWTo2L2Nu_M300_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M300',     'id=05300', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M350']         = ['/VBFHToWWTo2L2Nu_M350_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M350',     'id=05350', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M400']         = ['/VBFHToWWTo2L2Nu_M400_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M400',     'id=05400', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M450']         = ['/VBFHToWWTo2L2Nu_M450_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M450',     'id=05450', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M500']         = ['/VBFHToWWTo2L2Nu_M500_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M500',     'id=05500', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M550']         = ['/VBFHToWWTo2L2Nu_M550_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M550',     'id=05550', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M600']         = ['/VBFHToWWTo2L2Nu_M600_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M600',     'id=05600', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M650']         = ['/VBFHToWWTo2L2Nu_M650_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M650',     'id=05650', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M700']         = ['/VBFHToWWTo2L2Nu_M700_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M700',     'id=05700', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M750']         = ['/VBFHToWWTo2L2Nu_M750_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M750',     'id=05750', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M750_NWA']         = ['/VBFHToWWTo2L2Nu_M750_NWA_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M750_NWA',     'id=057501', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M800']         = ['/VBFHToWWTo2L2Nu_M800_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M800',     'id=05800', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M900']         = ['/VBFHToWWTo2L2Nu_M900_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M900',     'id=05900', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M1000']         = ['/VBFHToWWTo2L2Nu_M1000_13TeV_powheg_JHUgenv628_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_M1000',     'id=051000', 'doMCweights=True']]

samples['VBFHToWWTo2L2Nu_JHUGen698_M300']       = ['/VBFHToWWTo2L2Nu_M300_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M300',       'id=01300',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M350']       = ['/VBFHToWWTo2L2Nu_M350_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M350',       'id=01350',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M400']       = ['/VBFHToWWTo2L2Nu_M400_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M400',       'id=01400',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M450']       = ['/VBFHToWWTo2L2Nu_M450_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M450',       'id=01450',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M500']       = ['/VBFHToWWTo2L2Nu_M500_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M500',       'id=01500',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M550']       = ['/VBFHToWWTo2L2Nu_M550_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M550',       'id=01550',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M600']       = ['/VBFHToWWTo2L2Nu_M600_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M600',       'id=01600',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M650']       = ['/VBFHToWWTo2L2Nu_M650_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M650',       'id=01650',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M700']       = ['/VBFHToWWTo2L2Nu_M700_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M700',       'id=01700',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M750']       = ['/VBFHToWWTo2L2Nu_M750_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M750',       'id=01750',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M800']       = ['/VBFHToWWTo2L2Nu_M800_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M800',       'id=01800',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M900']       = ['/VBFHToWWTo2L2Nu_M900_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=VBFHToWWTo2L2Nu_JHUGen698_M900',       'id=01900',  'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M1000']      = ['/VBFHToWWTo2L2Nu_M1000_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_JHUGen698_M1000',      'id=011000', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M1500']      = ['/VBFHToWWTo2L2Nu_M1500_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_JHUGen698_M1500',      'id=011500', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M2000']      = ['/VBFHToWWTo2L2Nu_M2000_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_JHUGen698_M2000',      'id=012000', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M2500']      = ['/VBFHToWWTo2L2Nu_M2500_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_JHUGen698_M2500',      'id=012500', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_JHUGen698_M3000']      = ['/VBFHToWWTo2L2Nu_M3000_13TeV_powheg_JHUgenv698_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=VBFHToWWTo2L2Nu_JHUGen698_M3000',      'id=013000', 'doMCweights=True']]


samples['VBFHToWWTo2L2NuPowheg_M125']   = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM',        ['label=VBFHToWWTo2L2NuPowheg_M125',         'id=05125', 'doMCweights=True']]
samples['VBFHToWWTo2L2NuAMCNLO_M125']   = ['/VBFHToWWTo2L2Nu_M125_13TeV_amcatnlo_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',      ['label=VBFHToWWTo2L2NuAMCNLO_M125',   'id=08125', 'doMCweights=True']]
##samples['VBFHToWWTo2L2NuHerwigPS_M125'] = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',      ['label=VBFHToWWTo2L2NuHerwigPS_M125', 'id=09125', 'doMCweights=True']]

samples['VBFHToWWToNuQQ_M450']          = ['/VBF_HToWWToLNuQQ_M450_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=VBFHToWWToNuQQ_M450',      'id=7450', 'doMCweights=True']]
samples['VBFHToWWToNuQQ_M650']          = ['/VBF_HToWWToLNuQQ_M650_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=VBFHToWWToNuQQ_M650',      'id=7650', 'doMCweights=True']]
samples['VBFHToWWToNuQQ_M1000']         = ['/VBF_HToWWToLNuQQ_M1000_13TeV_powheg_JHUgen_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=VBFHToWWToNuQQ_M1000',      'id=71000', 'doMCweights=True']]
##samples['VBFHToWWToNuQQ_M750']         = ['/VBFHToWWToLNuQQ_M750_13TeV_powheg_JHUgenv628_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=VBFHToWWToNuQQ_M750',      'id=77500', 'doMCweights=True']]
##samples['VBFHToWWToNuQQ_M750_NWA']         = ['/VBFHToWWToLNuQQ_M750_NWA_13TeV_powheg_JHUgenv628_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=VBFHToWWToNuQQ_M750_NWA',      'id=775001', 'doMCweights=True']]

##samples['VBFHToTauTau_M120']            = ['/VBFHToTauTau_M120_13TeV_powheg_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',           ['label=VBFHToTauTau_M120',          'id=51120', 'doMCweights=True']]
samples['VBFHToTauTau_M125']            = ['/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',           ['label=VBFHToTauTau_M125',          'id=51125', 'doMCweights=True']]
##samples['VBFHToTauTau_M130']            = ['/VBFHToTauTau_M130_13TeV_powheg_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',           ['label=VBFHToTauTau_M130',          'id=51130', 'doMCweights=True']]

samples['VBFHToTauTau_M125_HerwigPS']             = ['/VBFHToTauTau_M125_13TeV_powheg_herwigpp/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                    ['label=VBFHToTauTau_M125_HerwigPS',                   'id=52125', 'doMCweights=True']]
samples['VBFHToTauTau_M125_PythiaFragment_Up']    = ['/VBFHToTauTau_M125_13TeV_powheg_pythia8_PythiaFragment_Up/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',   ['label=VBFHToTauTau_M125_PythiaFragment_Up',          'id=52125', 'doMCweights=True']]
samples['VBFHToTauTau_M125_PythiaFragment_Down']  = ['/VBFHToTauTau_M125_13TeV_powheg_pythia8_PythiaFragment_Down/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=VBFHToTauTau_M125_PythiaFragment_Down',        'id=52125', 'doMCweights=True']]

samples['VBFHToWWTo2L2Nu_M125_herwigpp'] = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=VBFHToWWTo2L2Nu_M125_herwigpp', 'id=05125', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M125_CUETDown'] = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=VBFHToWWTo2L2Nu_M125_CUETDown', 'id=05125', 'doMCweights=True']]
samples['VBFHToWWTo2L2Nu_M125_CUETUp']   = ['/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=VBFHToWWTo2L2Nu_M125_CUETUp', 'id=05125', 'doMCweights=True']]


## ggZH
samples['ggZH_HToWW_M120']      = ['/GluGluZH_HToWW_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=ggZH_HToWW_M120',  'id=07120', 'doMCweights=True']]
samples['ggZH_HToWW_M125']      = ['/GluGluZH_HToWW_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM',  ['label=ggZH_HToWW_M125',  'id=07125', 'doMCweights=True']]
samples['ggZH_HToWW_M130']      = ['/GluGluZH_HToWW_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/MINIAODSIM',  ['label=ggZH_HToWW_M130',  'id=07130', 'doMCweights=True']]

### ZH tautau 
##samples['HZJ_HToTauTau_M120'] = ['/ZHToTauTau_M120_13TeV_powheg_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM', ['label=HZJ_HToTauTau_M120', 'id=53120', 'doMCweights=True']]
#samples['HZJ_HToTauTau_M125'] = ['/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM', ['label=HZJ_HToTauTau_M125', 'id=53125', 'doMCweights=True']]
##samples['HZJ_HToTauTau_M130'] = ['/ZHToTauTau_M130_13TeV_powheg_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM', ['label=HZJ_HToTauTau_M130', 'id=53130', 'doMCweights=True']]

#### VVV >> Khakim
samples['WWW']  = ['/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',   ['label=WWW', 'id=00001', 'doMCweights=True']]
samples['WWZ']  = ['/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=WWZ', 'id=00001', 'doMCweights=True']]
samples['WZZ']  = ['/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=WZZ', 'id=00001', 'doMCweights=True']]
samples['ZZZ']  = ['/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=ZZZ', 'id=00001', 'doMCweights=True']]
samples['WWG']  = ['/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v3/MINIAODSIM', ['label=WWG', 'id=00001', 'doMCweights=True']]

#### Vg >> Khakim
samples['Wg_MADGRAPHMLM']      = ['/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',        ['label=Wg',     'id=00001', 'doMCweights=True']]
samples['Wg500']   = ['/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=Wg500',  'id=00001', 'doMCweights=True']]

samples['WgStarLNuEE'] = ['/WGstarToLNuEE_012Jets_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',      ['label=WgStarLNuEE', 'id=00001', 'doMCweights=True']]
samples['WgStarLNuMuMu'] = ['/WGstarToLNuMuMu_012Jets_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=WgStarLNuMuMu', 'id=00001', 'doMCweights=True']]

### WW PS
samples['WWTo2L2NuHerwigPS']    = ['/WWTo2L2Nu_13TeV-powheg-herwigpp/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',         ['label=WWTo2L2NuHerwigPS',    'id=00042', 'doMCweights=True']]
                                    
### WW CUET variations
samples['WWTo2L2Nu_CUETUp']  = ['/WWTo2L2Nu_13TeV-powheg-CUETP8M1Up/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',  ['label=WWTo2L2Nu_CUETUp', 'id=10012', 'doMCweights=True']]
samples['WWTo2L2Nu_CUETDown']  = ['/WWTo2L2Nu_13TeV-powheg-CUETP8M1Down/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',  ['label=WWTo2L2Nu_CUETDown', 'id=10013', 'doMCweights=True']]

samples['Zg']      = ['/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',         ['label=Zg',     'id=00001', 'doMCweights=True']]
####samples['ZgStar'] = ['',                                                                                                                       ['label=ZgStar', 'id=00001', 'doMCweights=True']]


#### QCD >> Khakim
samples['QCD_Pt-15to20_MuEnrichedPt5']     = ['/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',          ['label=QCD_Pt-15to20_MuEnrichedPt5',     'id=10001', 'doLHE=False' ]]
samples['QCD_Pt-20toInf_MuEnrichedPt15']   = ['/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',              ['label=QCD_Pt-20toInf_MuEnrichedPt15',   'id=10002', 'doLHE=False' ]]
samples['QCD_Pt-15to20_EMEnriched']        = ['/QCD_Pt-15to20_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',                   ['label=QCD_Pt-15to20_EMEnriched',        'id=10003', 'doLHE=False' ]]
samples['QCD_Pt-20to30_EMEnriched']        = ['/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                   ['label=QCD_Pt-20to30_EMEnriched',        'id=10004', 'doLHE=False' ]]
samples['QCD_Pt-30to50_EMEnriched']        = ['/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                   ['label=QCD_Pt-30to50_EMEnriched',        'id=10005', 'doLHE=False' ]]
samples['QCD_Pt-50to80_EMEnriched']        = ['/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',                   ['label=QCD_Pt-50to80_EMEnriched',        'id=10006', 'doLHE=False' ]]
samples['QCD_Pt-30toInf_DoubleEMEnriched'] = ['/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=QCD_Pt-30toInf_DoubleEMEnriched', 'id=10007', 'doLHE=False' ]]

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Jasper
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### VBS
samples['WpWpJJ_EWK_QCD']               = ['/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',          ['label=WpWpJJ_EWK_QCD',               'id=40001', 'doMCweights=True']]
samples['WpWpJJ_EWK']                   = ['/WpWpJJ_EWK_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',              ['label=WpWpJJ_EWK',                   'id=40002', 'doMCweights=True']]
samples['WpWpJJ_QCD']                   = ['/WpWpJJ_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                              ['label=WpWpJJ_QCD',                   'id=40003', 'doMCweights=True']]
samples['WpWpJJ_EWK_powheg']         	= ['/WpWpJJ_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=WpWpJJ_EWK_powheg',     'id=40030', 'doLHE=False']]
samples['WmWmJJ_EWK_powheg']            = ['/WmWmJJ_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=WmWmJJ_EWK_powheg', 'id=40031', 'doLHE=False']]
samples['WpWmJJ_EWK_QCD_noTop']         = ['/WWJJToLNuLNu_EWK_QCD_noTop_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',           ['label=WpWmJJ_EWK_QCD_noTop',         'id=40004', 'doMCweights=True']]
samples['WpWmJJ_EWK_noTop']             = ['/WWJJToLNuLNu_EWK_noTop_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',                               ['label=WpWmJJ_EWK_noTop',             'id=40005', 'doMCweights=True']]
samples['WpWmJJ_QCD_noTop']             = ['/WWJJToLNuLNu_QCD_noTop_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',                               ['label=WpWmJJ_QCD_noTop',             'id=40006', 'doMCweights=True']]
###samples['WpWmJJ_EWK_QCD_noTop_noHiggs'] = ['/WWJJToLNuLNu_EWK_QCD_noTop-noHiggs_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                   ['label=WpWmJJ_EWK_QCD_noTop_noHiggs', 'id=40007', 'doMCweights=True']]
###samples['WpWmJJ_EWK']                   = ['/WWJJToLNuLNu_EWK_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                     ['label=WpWmJJ_EWK',                   'id=40008', 'doMCweights=True']]
###samples['TWJ']                          = ['/TWJToLNuLNu_EWK_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                      ['label=TWJ',                          'id=40009', 'doMCweights=True']]
samples['WLLJJToLNu_M-60_EWK_QCD']      = ['/WLLJJToLNu_M-60_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=WLLJJToLNu_M-60_EWK_QCD',      'id=40010', 'doMCweights=True']]
##samples['WLLJJToLNu_M-60_EWK']          = ['/WLLJJToLNu_M-60_EWK_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                  ['label=WLLJJToLNu_M-60_EWK',          'id=40011', 'doMCweights=True']]
##samples['WLLJJToLNu_M-60_QCD']          = ['/WLLJJToLNu_M-60_QCD_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                  ['label=WLLJJToLNu_M-60_QCD',          'id=40012', 'doMCweights=True']]
samples['WLLJJToLNu_M-4to60_EWK_QCD']   = ['/WLLJJToLNu_M-4to60_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_bwcutoff15_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',              ['label=WLLJJToLNu_M-4to60_EWK_QCD',   'id=40013', 'doMCweights=True']]
##samples['WZJJ_EWK_QCD']                 = ['/WZJJ_EWK_QCD_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                         ['label=WZJJ_EWK_QCD',                 'id=40014', 'doMCweights=True']]
###samples['WZJJ_EWK']                     = ['/WZJJ_EWK_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                                             ['label=WZJJ_EWK',                     'id=40015', 'doMCweights=True']]
##samples['WZJJ_QCD']                     = ['/WZJJ_QCD_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',                             ['label=WZJJ_QCD',                     'id=40016', 'doMCweights=True']]
samples['WW_DoubleScattering']          = ['/WW_DoubleScattering_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',                           ['label=WW_DoubleScattering',          'id=40017', 'doLHE=False']]

samples['WGJJ']                         = ['/WGJJToLNu_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=WGJJ',                   'id=40019', 'doMCweights=True']]
##samples['EWKZ2Jets']                    = ['/EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',     ['label=EWKZ2Jets',                        'id=40020', 'doMCweights=True']]
samples['TTToSemiLeptonic']             = ['/TTToSemiLeptonic_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v2/MINIAODSIM',     ['label=TTToSemiLeptonic',                          'id=40021', 'doMCweights=True']]

### QCD
##samples['QCD_Pt_15to20_bcToE']             = ['/QCD_Pt_15to20_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',     ['label=QCD_Pt_15to20_bcToE',                  	'id=40022', 'doLHE=False']]
##samples['QCD_Pt_20to30_bcToE']             = ['/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM',     ['label=QCD_Pt_20to30_bcToE',                  	'id=40023', 'ddoLHE=False']]
samples['QCD_Pt_30to80_bcToE']		= ['/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',     ['label=QCD_Pt_30to80_bcToE',                  	'id=40024', 'doLHE=False']]
samples['QCD_Pt_80to170_bcToE']		= ['/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM',     ['label=QCD_Pt_80to170_bcToE',                  'id=40025', 'doLHE=False']]
samples['QCD_Pt_170to250_bcToE'] 	= ['/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=QCD_Pt_170to250_bcToE', 'id=40026', 'doLHE=False']]
samples['QCD_Pt_250toInf_bcToE']	= ['/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=QCD_Pt_250toInf_bcToE',                  'id=40027', 'doLHE=False']]

### DYNJets
samples['DY2JetsToLL']                  = ['/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=DY2JetsToLL',                  'id=40018', 'doMCweights=True']]
samples['DY3JetsToLL']                  = ['/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=DY3JetsToLL',                  'id=40028', 'doMCweights=True']]
samples['DY4JetsToLL']                  = ['/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=DY4JetsToLL',                  'id=40029', 'doMCweights=True']]
samples['DY1JetsToLL']                  = ['/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',     ['label=DY1JetsToLL',                  'id=40033', 'doMCweights=True']]

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Juan
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### ttDM
samples['ttDM0001scalar00010'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00010', 'id=90025', 'doLHE=False']]
samples['ttDM0001scalar00020'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00020', 'id=90026', 'doLHE=False']]
samples['ttDM0001scalar00050'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00050', 'id=90027', 'doLHE=False']]
samples['ttDM0001scalar00100'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00100', 'id=90028', 'doLHE=False']]
samples['ttDM0001scalar00200'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00200', 'id=90029', 'doLHE=False']]
samples['ttDM0001scalar00300'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00300', 'id=90030', 'doLHE=False']]
samples['ttDM0001scalar00500'] = ['/TTbarDMJets_scalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001scalar00500', 'id=90031', 'doLHE=False']]


samples['ttDM0010scalar00010'] = ['/TTbarDMJets_scalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010scalar00010', 'id=90035', 'doLHE=False']]
samples['ttDM0010scalar00015'] = ['/TTbarDMJets_scalar_Mchi-10_Mphi-15_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010scalar00015', 'id=90036', 'doLHE=False']]
samples['ttDM0010scalar00050'] = ['/TTbarDMJets_scalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010scalar00050', 'id=90037', 'doLHE=False']]
samples['ttDM0010scalar00100'] = ['/TTbarDMJets_scalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010scalar00100', 'id=90038', 'doLHE=False']]

samples['ttDM0050scalar00010'] = ['/TTbarDMJets_scalar_Mchi-50_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050scalar00010', 'id=90040', 'doLHE=False']]
samples['ttDM0050scalar00050'] = ['/TTbarDMJets_scalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050scalar00050', 'id=90041', 'doLHE=False']]
samples['ttDM0050scalar00095'] = ['/TTbarDMJets_scalar_Mchi-50_Mphi-95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050scalar00095', 'id=90042', 'doLHE=False']]
samples['ttDM0050scalar00200'] = ['/TTbarDMJets_scalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050scalar00200', 'id=90043', 'doLHE=False']]
samples['ttDM0050scalar00300'] = ['/TTbarDMJets_scalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050scalar00300', 'id=90044', 'doLHE=False']]







samples['ttDM0001pseudo00010'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00010', 'id=90061', 'doLHE=False']]
samples['ttDM0001pseudo00020'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00020', 'id=90062', 'doLHE=False']]
samples['ttDM0001pseudo00050'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00050', 'id=90063', 'doLHE=False']]
samples['ttDM0001pseudo00100'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00100', 'id=90064', 'doLHE=False']]
samples['ttDM0001pseudo00200'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00200', 'id=90065', 'doLHE=False']]
samples['ttDM0001pseudo00300'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00300', 'id=90066', 'doLHE=False']]
samples['ttDM0001pseudo00500'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo00500', 'id=90067', 'doLHE=False']]

samples['ttDM0001pseudo10000'] = ['/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0001pseudo10000', 'id=90070', 'doLHE=False']]
samples['ttDM0010pseudo00010'] = ['/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010pseudo00010', 'id=90071', 'doLHE=False']]
samples['ttDM0010pseudo00015'] = ['/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-15_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010pseudo00015', 'id=90072', 'doLHE=False']]
samples['ttDM0010pseudo00050'] = ['/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010pseudo00050', 'id=90073', 'doLHE=False']]
samples['ttDM0010pseudo00100'] = ['/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0010pseudo00100', 'id=90074', 'doLHE=False']]

samples['ttDM0050pseudo00010'] = ['/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050pseudo00010', 'id=90076', 'doLHE=False']]
samples['ttDM0050pseudo00050'] = ['/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050pseudo00050', 'id=90077', 'doLHE=False']]
samples['ttDM0050pseudo00095'] = ['/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050pseudo00095', 'id=90078', 'doLHE=False']]
samples['ttDM0050pseudo00200'] = ['/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050pseudo00200', 'id=90079', 'doLHE=False']]
samples['ttDM0050pseudo00300'] = ['/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM', ['label=ttDM0050pseudo00300', 'id=90080', 'doLHE=False']]



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Nicolo'
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### monoHiggs 80X

samples['monoH_2HDM_MZp-600_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-600_MA0-300', 'id=80001', 'doLHE=False']]
samples['monoH_2HDM_MZp-600_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-600_MA0-400', 'id=80002', 'doLHE=False']]
samples['monoH_2HDM_MZp-600_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-600_MA0-500', 'id=80003', 'doLHE=False']]
samples['monoH_2HDM_MZp-600_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-600_MA0-600', 'id=80004', 'doLHE=False']]
samples['monoH_2HDM_MZp-600_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-600_MA0-700', 'id=80005', 'doLHE=False']]
samples['monoH_2HDM_MZp-600_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-600_MA0-800', 'id=80006', 'doLHE=False']]

samples['monoH_2HDM_MZp-800_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-800_MA0-300', 'id=80007', 'doLHE=False']]
samples['monoH_2HDM_MZp-800_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-800_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-800_MA0-400', 'id=80008', 'doLHE=False']]
samples['monoH_2HDM_MZp-800_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-800_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-800_MA0-500', 'id=80009', 'doLHE=False']]
samples['monoH_2HDM_MZp-800_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-800_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-800_MA0-600', 'id=80010', 'doLHE=False']]
samples['monoH_2HDM_MZp-800_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-800_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-800_MA0-700', 'id=80011', 'doLHE=False']]
samples['monoH_2HDM_MZp-800_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-800_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-800_MA0-800', 'id=80012', 'doLHE=False']]

samples['monoH_2HDM_MZp-1000_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1000_MA0-300', 'id=80043', 'doLHE=False']]
samples['monoH_2HDM_MZp-1000_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1000_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1000_MA0-400', 'id=800044', 'doLHE=False']]
samples['monoH_2HDM_MZp-1000_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1000_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1000_MA0-500', 'id=80045', 'doLHE=False']]
samples['monoH_2HDM_MZp-1000_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1000_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1000_MA0-600', 'id=80046', 'doLHE=False']]
samples['monoH_2HDM_MZp-1000_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1000_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1000_MA0-700', 'id=80047', 'doLHE=False']]
samples['monoH_2HDM_MZp-1000_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1000_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1000_MA0-800', 'id=80048', 'doLHE=False']]

samples['monoH_2HDM_MZp-1200_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1200_MA0-300', 'id=80013', 'doLHE=False']]
samples['monoH_2HDM_MZp-1200_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1200_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1200_MA0-400', 'id=800014', 'doLHE=False']]
samples['monoH_2HDM_MZp-1200_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1200_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1200_MA0-500', 'id=80015', 'doLHE=False']]
samples['monoH_2HDM_MZp-1200_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1200_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1200_MA0-600', 'id=80016', 'doLHE=False']]
samples['monoH_2HDM_MZp-1200_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1200_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1200_MA0-700', 'id=80017', 'doLHE=False']]
samples['monoH_2HDM_MZp-1200_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1200_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1200_MA0-800', 'id=80018', 'doLHE=False']]

samples['monoH_2HDM_MZp-1400_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1400_MA0-300', 'id=80019', 'doLHE=False']]
samples['monoH_2HDM_MZp-1400_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1400_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1400_MA0-400', 'id=80020', 'doLHE=False']]
samples['monoH_2HDM_MZp-1400_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1400_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1400_MA0-500', 'id=80021', 'doLHE=False']]
samples['monoH_2HDM_MZp-1400_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1400_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1400_MA0-600', 'id=80022', 'doLHE=False']]
samples['monoH_2HDM_MZp-1400_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1400_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1400_MA0-700', 'id=80023', 'doLHE=False']]
samples['monoH_2HDM_MZp-1400_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1400_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1400_MA0-800', 'id=80024', 'doLHE=False']]

samples['monoH_2HDM_MZp-1700_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1700_MA0-300', 'id=80025', 'doLHE=False']]
samples['monoH_2HDM_MZp-1700_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1700_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1700_MA0-400', 'id=80026', 'doLHE=False']]
samples['monoH_2HDM_MZp-1700_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1700_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1700_MA0-500', 'id=80027', 'doLHE=False']]
samples['monoH_2HDM_MZp-1700_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1700_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1700_MA0-600', 'id=80028', 'doLHE=False']]
samples['monoH_2HDM_MZp-1700_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1700_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1700_MA0-700', 'id=80029', 'doLHE=False']]
samples['monoH_2HDM_MZp-1700_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-1700_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-1700_MA0-800', 'id=80030', 'doLHE=False']]

samples['monoH_2HDM_MZp-2000_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2000_MA0-300', 'id=80031', 'doLHE=False']]
samples['monoH_2HDM_MZp-2000_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2000_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2000_MA0-400', 'id=80032', 'doLHE=False']]
samples['monoH_2HDM_MZp-2000_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2000_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2000_MA0-500', 'id=80033', 'doLHE=False']]
samples['monoH_2HDM_MZp-2000_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2000_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2000_MA0-600', 'id=80034', 'doLHE=False']]
samples['monoH_2HDM_MZp-2000_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2000_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2000_MA0-700', 'id=80035', 'doLHE=False']]
samples['monoH_2HDM_MZp-2000_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2000_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2000_MA0-800', 'id=80036', 'doLHE=False']]

samples['monoH_2HDM_MZp-2500_MA0-300'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2500_MA0-300', 'id=80037', 'doLHE=False']]
samples['monoH_2HDM_MZp-2500_MA0-400'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2500_MA0-400_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2500_MA0-400', 'id=80038', 'doLHE=False']]
samples['monoH_2HDM_MZp-2500_MA0-500'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2500_MA0-500_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2500_MA0-500', 'id=80039', 'doLHE=False']]
samples['monoH_2HDM_MZp-2500_MA0-600'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2500_MA0-600_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2500_MA0-600', 'id=80040', 'doLHE=False']]
samples['monoH_2HDM_MZp-2500_MA0-700'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2500_MA0-700_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2500_MA0-700', 'id=80041', 'doLHE=False']]
samples['monoH_2HDM_MZp-2500_MA0-800'] = ['/ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-2500_MA0-800_13TeV-madgraph/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=monoH_2HDM_MZp-2500_MA0-800', 'id=80042', 'doLHE=False']]

# Z' Baryonic

samples['monoH_ZpBaryonic_MZp-995_MChi-500']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-995_MChi-500_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-995_MChi-500', 'id=80201', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-95_MChi-50']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-95_MChi-50_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-95_MChi-50', 'id=80202', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-50_MChi-50']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-50_MChi-50_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-50_MChi-50', 'id=80203', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-50_MChi-1']       = ['/MonoHWWllnunu_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',       ['label=ZpBaryonic_MZp-50_MChi-1', 'id=80204', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-50_MChi-10']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-50_MChi-10_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-50_MChi-10', 'id=80205', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-500_MChi-500']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-500_MChi-500_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-500_MChi-500', 'id=80206', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-500_MChi-1']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-500_MChi-1', 'id=80207', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-500_MChi-150']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-500_MChi-150_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-500_MChi-150', 'id=80208', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-300_MChi-50']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-300_MChi-50_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-300_MChi-50', 'id=80209', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-300_MChi-1']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-300_MChi-1', 'id=80210', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-295_MChi-150']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-295_MChi-150_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-295_MChi-150', 'id=80211', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-20_MChi-1']       = ['/MonoHWWllnunu_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',       ['label=ZpBaryonic_MZp-20_MChi-1', 'id=80212', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-200_MChi-50']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-200_MChi-50_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-200_MChi-50', 'id=80213', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-200_MChi-1']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-200_MChi-1', 'id=80214', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-200_MChi-150']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-200_MChi-150', 'id=80215', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-2000_MChi-500']   = ['/MonoHWWllnunu_ZpBaryonic_MZp-2000_MChi-500_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',   ['label=ZpBaryonic_MZp-2000_MChi-500', 'id=80216', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-2000_MChi-1']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-2000_MChi-1', 'id=80217', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-1995_MChi-1000']  = ['/MonoHWWllnunu_ZpBaryonic_MZp-1995_MChi-1000_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=ZpBaryonic_MZp-1995_MChi-1000', 'id=80218', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-15_MChi-10']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-15_MChi-10_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-15_MChi-10', 'id=80219', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10_MChi-50']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-10_MChi-50_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-10_MChi-50', 'id=80220', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10_MChi-500']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-10_MChi-500_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-10_MChi-500', 'id=80221', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10_MChi-1']       = ['/MonoHWWllnunu_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',       ['label=ZpBaryonic_MZp-10_MChi-1', 'id=80222', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10_MChi-150']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-10_MChi-150_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-10_MChi-150', 'id=80223', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10_MChi-10']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-10_MChi-10_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-10_MChi-10', 'id=80224', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10_MChi-1000']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-10_MChi-1000_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-10_MChi-1000', 'id=80225', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-100_MChi-1']      = ['/MonoHWWllnunu_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',      ['label=ZpBaryonic_MZp-100_MChi-1', 'id=80226', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-100_MChi-10']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-100_MChi-10_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-100_MChi-10', 'id=80227', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-1000_MChi-1']     = ['/MonoHWWllnunu_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',     ['label=ZpBaryonic_MZp-1000_MChi-1', 'id=80228', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-1000_MChi-150']   = ['/MonoHWWllnunu_ZpBaryonic_MZp-1000_MChi-150_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',   ['label=ZpBaryonic_MZp-1000_MChi-150', 'id=80229', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-1000_MChi-1000']  = ['/MonoHWWllnunu_ZpBaryonic_MZp-1000_MChi-1000_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=ZpBaryonic_MZp-1000_MChi-1000', 'id=80230', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10000_MChi-50']   = ['/MonoHWWllnunu_ZpBaryonic_MZp-10000_MChi-50_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',   ['label=ZpBaryonic_MZp-10000_MChi-50', 'id=80231', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10000_MChi-500']  = ['/MonoHWWllnunu_ZpBaryonic_MZp-10000_MChi-500_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=ZpBaryonic_MZp-10000_MChi-500', 'id=80232', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10000_MChi-1']    = ['/MonoHWWllnunu_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',    ['label=ZpBaryonic_MZp-10000_MChi-1', 'id=80233', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10000_MChi-150']  = ['/MonoHWWllnunu_ZpBaryonic_MZp-10000_MChi-150_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',  ['label=ZpBaryonic_MZp-10000_MChi-150', 'id=80234', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10000_MChi-10']   = ['/MonoHWWllnunu_ZpBaryonic_MZp-10000_MChi-10_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM',   ['label=ZpBaryonic_MZp-10000_MChi-10', 'id=80235', 'doLHE=False']]
samples['monoH_ZpBaryonic_MZp-10000_MChi-1000'] = ['/MonoHWWllnunu_ZpBaryonic_MZp-10000_MChi-1000_13TeV-madgraph/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=ZpBaryonic_MZp-10000_MChi-1000', 'id=80236', 'doLHE=False']]



### ZH -> vv/ll WW -> vv lv lv 
# noHLT version is working now

samples['GluGluZH_HToWWTo2L2Nu_M125_noHLT'] = ['/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=GluGluZH_HToWWTo2L2Nu_M125_noHLT', 'id=80113', 'doLHE=False']]
samples['GluGluZH_HToWWTo2L2Nu_M120_noHLT'] = ['/GluGluZH_HToWWTo2L2Nu_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=GluGluZH_HToWWTo2L2Nu_M120_noHLT', 'id=80114', 'doLHE=False']]
samples['GluGluZH_HToWWTo2L2Nu_M130_noHLT'] = ['/GluGluZH_HToWWTo2L2Nu_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=GluGluZH_HToWWTo2L2Nu_M130_noHLT', 'id=80115', 'doLHE=False']]

samples['HZJ_HToWWTo2L2Nu_M125_noHLT'] = ['/HZJ_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=HZJ_HToWWTo2L2Nu_M125_noHLT', 'id=80103', 'doLHE=False']]
samples['HZJ_HToWWTo2L2Nu_M120_noHLT'] = ['/HZJ_HToWWTo2L2Nu_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=HZJ_HToWWTo2L2Nu_M120_noHLT', 'id=80104', 'doLHE=False']]
samples['HZJ_HToWWTo2L2Nu_M130_noHLT'] = ['/HZJ_HToWWTo2L2Nu_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=HZJ_HToWWTo2L2Nu_M130_noHLT', 'id=80105', 'doLHE=False']]


# samples['HZJ_HToWWTo2L2Nu_M125'] = ['/HZJ_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HZJ_HToWWTo2L2Nu_M125', 'id=80100','doLHE=False']]
# samples['HZJ_HToWWTo2L2Nu_M120'] = ['/HZJ_HToWWTo2L2Nu_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HZJ_HToWWTo2L2Nu_M120', 'id=80101','doLHE=False']]
# samples['HZJ_HToWWTo2L2Nu_M130'] = ['/HZJ_HToWWTo2L2Nu_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=HZJ_HToWWTo2L2Nu_M130', 'id=80102','doLHE=False']]

# # samples['GluGluZH_HToWWTo2L2Nu_M125'] = ['/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=GluGluZH_HToWWTo2L2Nu_M125', 'id=80110','doLHE=False']]
# # samples['GluGluZH_HToWWTo2L2Nu_M120'] = ['/GluGluZH_HToWWTo2L2Nu_M120_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=GluGluZH_HToWWTo2L2Nu_M120', 'id=80111','doLHE=False']]
# # samples['GluGluZH_HToWWTo2L2Nu_M130'] = ['/GluGluZH_HToWWTo2L2Nu_M130_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM', ['label=GluGluZH_HToWWTo2L2Nu_M130', 'id=80112','doLHE=False']]


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Luca
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####### Stop 80X
##### T2tt
### FullSim
samples['T2tt_mStop425_mLSP325'] = ['/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_mStop425_mLSP325', 'id=00061', 'doLHE=False', 'doSusy=True']]
samples['T2tt_mStop500_mLSP325'] = ['/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM', ['label=T2tt_mStop500_mLSP325', 'id=00062', 'doLHE=False', 'doSusy=True']]
samples['T2tt_mStop850_mLSP100'] = ['/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_mStop850_mLSP100', 'id=00063', 'doLHE=False', 'doSusy=True']]
### FastSim mass scans
samples['T2tt_mStop-150to250'] = ['/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_mStop150to250', 'id=00197', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]
samples['T2tt_mStop-250to350'] = ['/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_mStop250to350', 'id=00149', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]
samples['T2tt_mStop-350to400'] = ['/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_mStop350to400', 'id=00145', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]
samples['T2tt_mStop-400to1200'] = ['/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_mStop400to1200', 'id=00135', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]
### FastSim dM
samples['T2tt_dM10to80'] = ['/SMS-T2tt_dM-10to80_2Lfilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_dM10to80', 'id=00148', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]
samples['T2tt_dM10to80_genHT160_genMET80'] = ['/SMS-T2tt_dM-10to80_genHT-160_genMET-80_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2tt_dM10to80_genHT160_genMET80', 'id=00210', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]
##### T2bW
samples['T2bW'] = ['/SMS-T2bW_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM', ['label=T2bW', 'id=00147', 'doLHE=False', 'doSusy=True', 'isFastSim=True']]

########
# Additional global configuration
########

#config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/amassiro/RunII/2016/Jun03/MC/v2/'
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/amassiro/RunII/2016/Jun07/MC/v2/'
# this name is used partially in the post-processing.
# Let's try not to change it for a given production era

pyCfgParams.append('globalTag=80X_mcRun2_asymptotic_2016_miniAODv2')



