from ProcessDataEvents import *

lepton_type = "muon"
# lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

# use_hash_index_ = True

base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
labels_ = []
fileNames_ = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_ = [ ]
        fileNames_ = {
            }
    elif lepton_type == 'electron':
        labels_ = [ ]
        fileNames_ = {
            }
elif data_sample == '2018':
    if lepton_type == 'muon':
        labels_ = [ "Bkg-2018-muon-TTJets", "Bkg-2018-muon-WJetsToLNu_0J", "Bkg-2018-muon-WJetsToLNu_1J", "Bkg-2018-muon-WJetsToLNu_2J" ]
        # labels_ = [ "Bkg-2018-muon-WJetsToLNu_0J", "Bkg-2018-muon-WJetsToLNu_1J", "Bkg-2018-muon-WJetsToLNu_2J" ]
        fileNames_ = {
            "Bkg-2018-muon-TTJets": [ "output-Bkg-2018-muon-TTJets.h5" ],
            "Bkg-2018-muon-WJetsToLNu_0J": [ "output-Bkg-2018-muon-WJetsToLNu_0J.h5" ],
            "Bkg-2018-muon-WJetsToLNu_1J": [ "output-Bkg-2018-muon-WJetsToLNu_1J.h5" ],
            "Bkg-2018-muon-WJetsToLNu_2J": [ "output-Bkg-2018-muon-WJetsToLNu_2J.h5" ],
            }
    elif lepton_type == 'electron':
        labels_ = [ "Bkg-2018-electron-TTJets" ]
        fileNames_ = {
            "Bkg-2018-electron-TTJets": [ "output-Bkg-2018-electron-TTJets.h5" ],
            }

for key_ in fileNames_:
    fileNames_[ key_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_[ key_ ] ]
print ( labels_ )
print ( fileNames_ )

# output_dir_=""
output_dir_="output"
process_data_events_ = ProcessDataEvents( lepton_type=lepton_type, data_sample=data_sample, labels=labels_, fileNames=fileNames_, runOnMC=True, output_dir=output_dir_ )

process_data_events_()
