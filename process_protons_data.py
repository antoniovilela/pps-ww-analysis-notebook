from ProcessProtons import *
from dask.distributed import Client, LocalCluster
import dask
# dask.config.set({"array.chunk-size": "100 MiB"})
# dask.config.set({"optimization.fuse.active": False})
# dask.config.set({
#     'distributed.nanny.timeouts.startup': '60s',
#     'distributed.nanny.timeouts.connect': '60s'
# })

debug = False

lepton_type_ = "muon"
# lepton_type_ = "electron"

# data_sample = '2017'
data_sample = '2018'

label__ = "data-{}-{}".format( data_sample, lepton_type_ )

# base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output"
base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output_test"

labels_ = []
fileNames_data_ = {}
if data_sample == '2017':
    labels_ = [ label__ ]
    if lepton_type_ == 'muon':
        fileNames_data_[ label__ ] = [
            'output-data-muon-2017B.h5',
            'output-data-muon-2017C.h5',
            'output-data-muon-2017D.h5',
            'output-data-muon-2017E.h5',
            'output-data-muon-2017F.h5'
        ]
    elif lepton_type_ == 'electron':
        fileNames_data_[ label__ ] = [
            'output-data-electron-2017B.h5',
            'output-data-electron-2017C.h5',
            'output-data-electron-2017D.h5',
            'output-data-electron-2017E.h5',
            'output-data-electron-2017F.h5'
        ]
elif data_sample == '2018':
    labels_ = []
    if lepton_type_ == 'muon':
        labels_.append( label__ + "-2018A" )
        fileNames_data_[ ( label__ + "-2018A" ) ] = {}
        fileNames_data_[ ( label__ + "-2018A" ) ][ 'protons_multiRP' ] = [ 'process_data-data-2018-muon-2018A-protons_multiRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018A" ) ][ 'protons_singleRP' ] = [ 'table_protons-data-2018-muon-2018A-protons_singleRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018A" ) ][ 'ppstracks' ] = [ 'table_protons-data-2018-muon-2018A-ppstracks.parquet' ]
        fileNames_data_[ ( label__ + "-2018A" ) ][ 'event_counts' ] = [ 'event_counts-data-2018-muon-2018A.parquet' ]

        labels_.append( label__ + "-2018B" )
        fileNames_data_[ ( label__ + "-2018B" ) ] = {}
        fileNames_data_[ ( label__ + "-2018B" ) ][ 'protons_multiRP' ] = [ 'process_data-data-2018-muon-2018B-protons_multiRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018B" ) ][ 'protons_singleRP' ] = [ 'table_protons-data-2018-muon-2018B-protons_singleRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018B" ) ][ 'ppstracks' ] = [ 'table_protons-data-2018-muon-2018B-ppstracks.parquet' ]
        fileNames_data_[ ( label__ + "-2018B" ) ][ 'event_counts' ] = [ 'event_counts-data-2018-muon-2018B.parquet' ]

        labels_.append( label__ + "-2018C" )
        fileNames_data_[ ( label__ + "-2018C" ) ] = {}
        fileNames_data_[ ( label__ + "-2018C" ) ][ 'protons_multiRP' ] = [ 'process_data-data-2018-muon-2018C-protons_multiRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018C" ) ][ 'protons_singleRP' ] = [ 'table_protons-data-2018-muon-2018C-protons_singleRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018C" ) ][ 'ppstracks' ] = [ 'table_protons-data-2018-muon-2018C-ppstracks.parquet' ]
        fileNames_data_[ ( label__ + "-2018C" ) ][ 'event_counts' ] = [ 'event_counts-data-2018-muon-2018C.parquet' ]

        labels_.append( label__ + "-2018D" )
        fileNames_data_[ ( label__ + "-2018D" ) ] = {}
        fileNames_data_[ ( label__ + "-2018D" ) ][ 'protons_multiRP' ] = [ 'process_data-data-2018-muon-2018D-protons_multiRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018D" ) ][ 'protons_singleRP' ] = [ 'table_protons-data-2018-muon-2018D-protons_singleRP.parquet' ]
        fileNames_data_[ ( label__ + "-2018D" ) ][ 'ppstracks' ] = [ 'table_protons-data-2018-muon-2018D-ppstracks.parquet' ]
        fileNames_data_[ ( label__ + "-2018D" ) ][ 'event_counts' ] = [ 'event_counts-data-2018-muon-2018D.parquet' ]

    elif lepton_type_ == 'electron':
        labels_.append( label__ + "-2018A" )
        fileNames_data_[ ( label__ + "-2018A" ) ] = [ 'output-data-2018-electron-2018A.h5' ]
        labels_.append( label__ + "-2018B" )
        fileNames_data_[ ( label__ + "-2018B" ) ] = [ 'output-data-2018-electron-2018B.h5' ]
        labels_.append( label__ + "-2018C" )
        fileNames_data_[ ( label__ + "-2018C" ) ] = [ 'output-data-2018-electron-2018C.h5' ]
        labels_.append( label__ + "-2018D" )
        fileNames_data_[ ( label__ + "-2018D" ) ] = [ 'output-data-2018-electron-2018D.h5' ]

for key1_ in fileNames_data_:
    for key2_ in fileNames_data_[ key1_ ]:
        fileNames_data_[ key1_ ][ key2_ ] = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_data_[ key1_ ][ key2_ ] ]
print ( labels_ )
print ( fileNames_data_ )

# output_dir_ = ""
output_dir_ = "output_test"

if __name__ == "__main__":
    if debug:
        print ( dask.config.config )

    # client = Client()
    # cluster = LocalCluster( n_workers=1, threads_per_worker=1 )
    cluster = LocalCluster()
    client = Client( cluster )
    # print ( client.dashboard_link )

    process_protons_ = ProcessProtons( lepton_type=lepton_type_, data_sample=data_sample, labels=labels_, fileNames=fileNames_data_, runOnMC=False, output_dir=output_dir_ )

    process_protons_( apply_fiducial=True, within_aperture=True, select_2protons=True, debug=debug )

    client.close()

