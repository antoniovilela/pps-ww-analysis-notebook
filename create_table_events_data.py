# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTableEvents import *

lepton_type = 'muon'
# lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

label = "data-{}-{}".format( data_sample, lepton_type )

tree_path = "SlimmedNtuple"
# tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False

fileNames_data = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        fileNames_data[ "2017B" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017B-withDilepton/SlimmedNtuple_merged_noduplicates.root"
        ]
        fileNames_data[ "2017C" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017C-withDilepton/SlimmedNtuple_merged_noduplicates.root"
        ]
        fileNames_data[ "2017D" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017D-withDilepton/SlimmedNtuple_merged_noduplicates.root"
        ]
        fileNames_data[ "2017E" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017E-withDilepton/SlimmedNtuple_merged_noduplicates.root"
        ]
        fileNames_data[ "2017F" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon-Run2017F-withDilepton/SlimmedNtuple_merged_noduplicates.root"
        ]
    elif lepton_type == 'electron':
        fileNames_data[ "2017B" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017B/SingleElectron-Run2017B_merged.root"
        ]
        fileNames_data[ "2017C" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017C/SingleElectron-Run2017C_merged.root"
        ]
        fileNames_data[ "2017D" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017D/SingleElectron-Run2017D_merged.root"
        ]
        fileNames_data[ "2017E" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017E/SingleElectron-Run2017E_merged.root"
        ]
        fileNames_data[ "2017F" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleElectron-Run2017F/SingleElectron-Run2017F_merged.root"
        ]
elif data_sample == '2018':
    if lepton_type == 'muon':
        fileNames_data[ "2018A" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon_UL2018A_MiniAODv2-v3_noduplicates.root"
        ]
        fileNames_data[ "2018B" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon_UL2018B_MiniAODv2-v2_noduplicates.root"
        ]
        fileNames_data[ "2018C" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon_UL2018C_MiniAODv2-v2_noduplicates.root"
        ]
        fileNames_data[ "2018D" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/SingleMuon_UL2018D_MiniAODv2-v3_noduplicates.root"
        ]
    elif lepton_type == 'electron':
        fileNames_data[ "2018A" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/EGamma-Run2018A/EGamma-Run2018A_merged.root"
        ]
        fileNames_data[ "2018B" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/EGamma-Run2018B/EGamma-Run2018B_merged.root"
        ]
        fileNames_data[ "2018C" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/EGamma-Run2018C/EGamma-Run2018C_merged.root"
        ]
        fileNames_data[ "2018D" ] = [
            "/eos/home-a/antoniov/Workspace/analysis/data/PPS/EGamma-Run2018D/EGamma-Run2018D_merged.root"
        ]

create_table_ = CreateTableEvents( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_data, tree_path=tree_path, output_dir="output" )

create_table_( step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
