# import sys
# sys.path.insert( 0, "/afs/cern.ch/work/a/antoniov/env/uproot/lib/python3.6/site-packages" )
# print ( sys.path )

from CreateTableEvents import *

lepton_type = 'muon'
# lepton_type = 'electron'

# data_sample = '2017'
data_sample = '2018'

label = "Bkg-{}-{}".format( data_sample, lepton_type )

tree_path = "demo/SlimmedNtuple"
step_size = 100000
debug = False
# debug = True

fileNames_ = {}
if data_sample == '2017':
	    fileNames_[ "TTJets" ] = [
    ]
elif data_sample == '2018':
    fileNames_[ "TTJets" ] = [
        "/eos/home-a/antoniov/Workspace/analysis/data/PPS/WW_MC_Bkg_2018/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"
    ]

# output_dir_=""
output_dir_="output"
create_table_events_ = CreateTableEvents( label=label, lepton_type=lepton_type, data_sample=data_sample, fileNames=fileNames_, tree_path=tree_path, output_dir=output_dir_ )

create_table_events_( runOnMC=True, step_size=step_size, firstEvent=None, entryStop=None, debug=debug ) 
