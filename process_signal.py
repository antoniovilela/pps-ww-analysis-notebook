from ProcessData import *

lepton_type = "muon"
# lepton_type = "electron"

# data_sample = '2017'
data_sample = '2018'

# use_hash_index_ = True

# labels_signals = [ "GGToWW-AQGC-A0W1e-6" ]
# labels_signals = [ "GGToWW-AQGC-A0W1e-6", "GGToWW-AQGC-A0W2e-6", "GGToWW-AQGC-A0W5e-6" ]

# base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output_test"
# output_dir_ = "output"
output_dir_ = "output_test"

labels_signals_ = []
fileNames_signals_ = {}
if data_sample == '2017':
    if lepton_type == 'muon':
        labels_signals_ = [ "GGToWW-AQGC-2017-muon-A0W1e-6", "GGToWW-AQGC-2017-muon-A0W2e-6", "GGToWW-AQGC-2017-muon-A0W5e-6" ]
        fileNames_signals_ = {
            "GGToWW-AQGC-2017-muon-A0W1e-6": [ "output-GGToWW-AQGC-2017-muon-A0W1e-6.h5" ],
            "GGToWW-AQGC-2017-muon-A0W2e-6": [ "output-GGToWW-AQGC-2017-muon-A0W2e-6.h5" ],
            "GGToWW-AQGC-2017-muon-A0W5e-6": [ "output-GGToWW-AQGC-2017-muon-A0W5e-6.h5" ]
            }
    elif lepton_type == 'electron':
        labels_signals_ = [ "GGToWW-AQGC-2017-electron-A0W1e-6", "GGToWW-AQGC-2017-electron-A0W2e-6", "GGToWW-AQGC-2017-electron-A0W5e-6" ]
        fileNames_signals_ = {
            "GGToWW-AQGC-2017-electron-A0W1e-6": [ "output-GGToWW-AQGC-2017-electron-A0W1e-6.h5" ],
            "GGToWW-AQGC-2017-electron-A0W2e-6": [ "output-GGToWW-AQGC-2017-electron-A0W2e-6.h5" ],
            "GGToWW-AQGC-2017-electron-A0W5e-6": [ "output-GGToWW-AQGC-2017-electron-A0W5e-6.h5" ]
            }
elif data_sample == '2018':
    if lepton_type == 'muon':
        # labels_signals_ = [ "GGToWW-AQGC-2018-muon-A0W5e-7", "GGToWW-AQGC-2018-muon-A0W1e-6", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]
        labels_signals_ = [ "GGToWW-AQGC-2018-muon-A0W1e-6", "GGToWW-AQGC-2018-muon-A0W2e-6", "GGToWW-AQGC-2018-muon-A0W5e-6" ]

        fileNames_signals_ = {}

        # fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-7"] = {}
        # fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-7"]['protons_multiRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W5e-7-protons_multiRP.parquet" ]
        # fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-7"]['protons_singleRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W5e-7-protons_singleRP.parquet" ]
        # fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-7"]['ppstracks'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W5e-7-ppstracks.parquet" ]
        # fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-7"]['event_counts'] = [ "event_counts-GGToWW-AQGC-2018-muon-A0W5e-7.parquet" ]

        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W1e-6"] = {}
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W1e-6"]['protons_multiRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W1e-6-protons_multiRP.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W1e-6"]['protons_singleRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W1e-6-protons_singleRP.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W1e-6"]['ppstracks'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W1e-6-ppstracks.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W1e-6"]['event_counts'] = [ "event_counts-GGToWW-AQGC-2018-muon-A0W1e-6.parquet" ]

        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W2e-6"] = {}
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W2e-6"]['protons_multiRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W2e-6-protons_multiRP.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W2e-6"]['protons_singleRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W2e-6-protons_singleRP.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W2e-6"]['ppstracks'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W2e-6-ppstracks.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W2e-6"]['event_counts'] = [ "event_counts-GGToWW-AQGC-2018-muon-A0W2e-6.parquet" ]

        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-6"] = {}
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-6"]['protons_multiRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W5e-6-protons_multiRP.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-6"]['protons_singleRP'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W5e-6-protons_singleRP.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-6"]['ppstracks'] = [ "table_protons-GGToWW-AQGC-2018-muon-A0W5e-6-ppstracks.parquet" ]
        fileNames_signals_["GGToWW-AQGC-2018-muon-A0W5e-6"]['event_counts'] = [ "event_counts-GGToWW-AQGC-2018-muon-A0W5e-6.parquet" ]

    elif lepton_type == 'electron':
        # labels_signals_ = [ "GGToWW-AQGC-2018-electron-A0W5e-7", "GGToWW-AQGC-2018-electron-A0W1e-6", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]
        labels_signals_ = [ "GGToWW-AQGC-2018-electron-A0W1e-6", "GGToWW-AQGC-2018-electron-A0W2e-6", "GGToWW-AQGC-2018-electron-A0W5e-6" ]
        fileNames_signals_ = {
            # "GGToWW-AQGC-2018-electron-A0W5e-7": [ "table_protons-GGToWW-AQGC-2018-electron-A0W5e-7.parquet" ],
            "GGToWW-AQGC-2018-electron-A0W1e-6": [ "table_protons-GGToWW-AQGC-2018-electron-A0W1e-6.parquet" ],
            "GGToWW-AQGC-2018-electron-A0W2e-6": [ "table_protons-GGToWW-AQGC-2018-electron-A0W2e-6.parquet" ],
            "GGToWW-AQGC-2018-electron-A0W5e-6": [ "table_protons-GGToWW-AQGC-2018-electron-A0W5e-6.parquet" ]
            }

for key1_ in fileNames_signals_:
    for key2_ in fileNames_signals_[ key1_ ]:
        fileNames_signals_[ key1_ ][ key2_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_signals_[ key1_ ][ key2_ ] ]
print ( labels_signals_ )
print ( fileNames_signals_ )

process_data_ = ProcessData( lepton_type=lepton_type, data_sample=data_sample, labels=labels_signals_, fileNames=fileNames_signals_, runOnMC=True, output_dir=output_dir_ )

process_data_()

