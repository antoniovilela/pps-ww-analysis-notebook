# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTable import *

# lepton_type = 'muon'
lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

# label = "GGToWW-AQGC-mix_protons-{}".format( lepton_type )
label = "GGToWW-AQGC-mix_protons-{}-{}".format( data_sample, lepton_type )

tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False

fileNames_A0W_ACW = {}
proton_files = None
if data_sample == '2017':
    fileNames_A0W_ACW[ "A0W1e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "A0W2e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "A0W5e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW5e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW8e-6" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    fileNames_A0W_ACW[ "ACW2e-5" ] = [
        "/eos/user/a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-signal-proton-propagation-dilepton/SlimmedNtuple_merged.root"
    ]
    
    proton_files = [
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged_noduplicates.root",
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged_noduplicates.root"
    ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        fileNames_A0W_ACW[ "A0W5e-7" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-7_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "A0W1e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "ACW8e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-5" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_mu.root"
        ]
    elif lepton_type == 'electron':
        fileNames_A0W_ACW[ "A0W5e-7" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-7_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "A0W1e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "A0W2e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W2e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "A0W5e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-A0W5e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "ACW5e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW5e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "ACW8e-6" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW8e-6_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]
        fileNames_A0W_ACW[ "ACW2e-5" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/GGToWW_bSM-ACW2e-5_13TeV-fpmc-herwig6-2018/SlimmedNtuple_merged_e.root"
        ]

    proton_files = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018A/SingleMuon-Run2018A_merged.root",
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018B/SingleMuon-Run2018B_merged.root",
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018C/SingleMuon-Run2018C_merged.root",
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2018D/SingleMuon-Run2018D_merged.root"
    ]

create_table_mix_protons_ = CreateTable( label=label, data_sample=data_sample, lepton_type=lepton_type, fileNames=fileNames_A0W_ACW, tree_path=tree_path, output_dir="output" )

create_table_mix_protons_( mix_protons=True, proton_files=proton_files, runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug)