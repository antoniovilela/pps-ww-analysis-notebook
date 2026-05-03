import os
from processing import *
from random_experiment import get_systematics_vs_xi_h5
# import dask.array as da
import dask.dataframe as dd

class ProcessProtons:
    def __init__( self, lepton_type, data_sample, labels, fileNames, random_protons=False, mix_protons=False, runOnMC=False, output_dir="", use_hash_index=False ):

        if lepton_type not in ( 'muon', 'electron' ):
            raise RuntimeError( "Invalid lepton_type argument." )

        if data_sample not in ( '2017', '2018' ):
            raise RuntimeError( "Invalid data_sample argument." )

        self.use_dask = True
        self.lepton_type_ = lepton_type
        self.data_sample_ = data_sample
        self.labels_ = labels
        self.fileNames_ = fileNames
        self.output_dir_ = None
        if output_dir is not None and output_dir != "": self.output_dir_ = output_dir
        self.use_hash_index_ = use_hash_index
        self.random_protons_ = random_protons 
        self.mix_protons_ = mix_protons
        self.runOnMC_ = runOnMC
        self.data_periods_ = None
        if self.data_sample_ == '2017':
            self.data_periods_ = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
        elif self.data_sample_ == '2018':
            self.data_periods_ = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

        self.systematics_Xi_X_, self.systematics_Xi_Y_ = 2 * [ None ]
        if self.runOnMC_:
            self.systematics_Xi_X_, self.systematics_Xi_Y_ = get_systematics_vs_xi_h5(
                data_periods=self.data_periods_,
                fileName="reco_characteristics/reco_characteristics_version1.h5"
                )

    def getSigmaXi( self, df ):
        df__ = df[ [ 'period', 'random', 'arm', 'xi' ] ]
        msk_random_ = ( df__[ "random" ] == 0 )
        print ( msk_random_, np.sum( msk_random_ ) )
        sigma_var_ = np.zeros( df__.shape[0] ) 
        var_ = 'xi'
        # f_low_edge_ = lambda row: np.invert( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] <= row[ var_ ] ).argmax() - 1
        # f_high_edge_ = lambda row: ( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] >= row[ var_ ] ).argmax()
        f_low_edge_ = lambda row: np.invert( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] <= row[ var_ ] ).argmax() - 1
        f_high_edge_ = lambda row: ( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ] > row[ var_ ] ).argmax()
        if np.sum( msk_random_ ) > 0:
            sigma_var_[ msk_random_ ] = df__[ msk_random_ ].apply(
                lambda row:
                    ( ( self.systematics_Xi_Y_[ row[ "period" ] ][ row[ "arm" ] ][ f_high_edge_( row ) ] -
                        self.systematics_Xi_Y_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ) /
                      ( self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ][ f_high_edge_( row ) ] -
                        self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ) *
                      ( row[ var_ ] - self.systematics_Xi_X_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ) +
                        self.systematics_Xi_Y_[ row[ "period" ] ][ row[ "arm" ] ][ f_low_edge_( row ) ] ),
                axis=1 ).values 
        print ( sigma_var_, sigma_var_.size )
        return sigma_var_

    def fetchDataPeriod( self, df ):
        run_str_ = "run"
        if self.random_protons_ or self.mix_protons_:
            run_str_ = "run_rnd"
        elif self.runOnMC_ and not self.mix_protons_:
            run_str_ = "run_mc"

        if "period" not in df.columns:
            df_run_ranges_ = None
            if self.data_sample_ == '2017':
                df_run_ranges_ = df_run_ranges_2017
            elif self.data_sample_ == '2018':
                df_run_ranges_ = df_run_ranges_2018

            df[ "period" ] = np.nan
            for idx_ in range( df_run_ranges_.shape[0] ):
                msk_period_ = ( ( df[ run_str_ ] >= df_run_ranges_.iloc[ idx_ ][ "min" ] ) & ( df[ run_str_ ] <= df_run_ranges_.iloc[ idx_ ][ "max" ] ) )
                sum_period_ = np.sum( msk_period_.compute() )
                if sum_period_ > 0:
                    period_key_ = df_run_ranges_.index[ idx_ ]
                    df[ "period" ] = df[ "period" ].mask( msk_period_, period_key_ )
                    print ( "{}: {}".format( period_key_, sum_period_ ) )
            print ( df[ "period" ].compute() )

    def calculateXiSmeared( self, df ):
        # Gaussian shift
        sigma_xi_ = self.getSigmaXi( df )
        df_arr_xi_ = df[ "xi" ].compute()
        smeared_xi_arr_ = df_arr_xi_.values + ( 0. + np.random.randn( df_arr_xi_.size ) * sigma_xi_ )
        print ( smeared_var_arr_, smeared_var_arr_.size )
        df[ "sigma_xi" ] = sigma_xi_
        df[ "xi_smeared" ] = smeared_xi_arr_

    def calculateProtons( self, df ):
        df_arr_xi_ = df[ "xi" ]
        df[ "xi" + "_nom" ] = df_arr_xi_
        if self.runOnMC_:
           sigma_xi_ = self.getSigmaXi( df )
           # variations_ = [ 0.10, 0.30, 0.60, 1.0 ]
           # names_varplus_ = [ "_p10", "_p30", "_p60", "_p100" ]
           # names_varminus_ = [ "_m10", "_m30", "_m60", "_m100" ]
           variations_ = [ 1.0 ]
           names_varplus_ = [ "_p100" ]
           names_varminus_ = [ "_m100" ]
           for idx_, val_ in enumerate( variations_ ):
               df[ "xi" + names_varplus_[ idx_ ] ] = df_arr_xi_ + val_ * sigma_xi_
               df[ "xi" + names_varminus_[ idx_ ] ] = df_arr_xi_ - val_ * sigma_xi_
           df[ "sigma_xi" ] = sigma_xi_

    def get_data( self, fileNames, runMin=None, runMax=None ):
        """
        fileNames dict:
            'protons_multiRP': list of paths,
            'protons_singleRP': list of paths,
            'ppstracks': list of paths,
            'event_counts': list of paths
       
        """
    
        runMin_ = runMin
        runMax_ = runMax

        fileNames_multiRP_      = fileNames[ 'protons_multiRP' ]
        fileNames_singleRP_     = fileNames[ 'protons_singleRP' ]
        fileNames_ppstracks_    = fileNames[ 'ppstracks' ]
        fileNames_counts_       = fileNames[ 'event_counts' ]
        if len( fileNames_multiRP_ ) == 1: fileNames_multiRP_ = fileNames_multiRP_[0]
        if len( fileNames_singleRP_ ) == 1: fileNames_singleRP_ = fileNames_singleRP_[0]
        if len( fileNames_ppstracks_ ) == 1: fileNames_ppstracks_ = fileNames_ppstracks_[0]
        if len( fileNames_counts_ ) == 1: fileNames_counts_ = fileNames_counts_[0]
    
        df_protons_multiRP_  = None
        df_protons_singleRP_ = None
        df_ppstracks_        = None
        df_event_counts_     = None
        if self.use_dask:
            df_protons_multiRP_  = dd.read_parquet( fileNames_multiRP_ )
            df_protons_singleRP_ = dd.read_parquet( fileNames_singleRP_ )
            df_ppstracks_        = dd.read_parquet( fileNames_ppstracks_ )
            df_event_counts_     = dd.read_parquet( fileNames_counts_ )
        else:
            df_protons_multiRP_  = pd.read_parquet( fileNames_multiRP_ )
            df_protons_singleRP_ = pd.read_parquet( fileNames_singleRP_ )
            df_ppstracks_        = pd.read_parquet( fileNames_ppstracks_ )
            df_event_counts_     = pd.read_parquet( fileNames_counts_ )
        
        return ( df_event_counts_, df_protons_multiRP_, df_protons_singleRP_, df_ppstracks_ )

    def __call__( self, apply_fiducial=True, within_aperture=False, calculate_vars_pp=True, select_2protons=True, debug=False, runMin=None, runMax=None ):

        if runMin is not None and runMin <= 0:
            raise RuntimeError( "Invalid data_sample argument." )
        if runMax is not None and runMax <= 0:
            raise RuntimeError( "Invalid data_sample argument." )

        runMin_ = runMin
        runMax_ = runMax

        # df_protons_multiRP_index = {}
        # df_protons_multiRP_events = {}
        
        for label_ in self.labels_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()

            file_path_protons_multiRP_ = None
            file_path_events_multiRP_ = None
            file_name_label_protons_multiRP_ =  "process_protons-{}-protons_multiRP.parquet".format( label_ )
            file_name_label_events_multiRP_ =  "process_protons-{}-events_multiRP.parquet".format( label_ )
            if self.output_dir_ is not None and self.output_dir_ != "":
                file_path_protons_multiRP_ = "{}/{}".format( self.output_dir_, file_name_label_protons_multiRP_ )
                file_path_events_multiRP_ = "{}/{}".format( self.output_dir_, file_name_label_events_multiRP_ )
            else:
                file_path_protons_multiRP_ = file_name_label_protons_multiRP_
                file_path_events_multiRP_ = file_name_label_events_multiRP_
            print ( file_path_protons_multiRP_ )
            print ( file_path_events_multiRP_ )

            df_counts_, df_protons_multiRP_, df_protons_singleRP_, df_ppstracks_ = self.get_data( self.fileNames_[ label_ ], runMin=runMin_, runMax=runMax_ )

            self.fetchDataPeriod( df_protons_multiRP_ ) 

            if self.runOnMC_:
                pass

            self.calculateProtons( df_protons_multiRP_ )

            df_protons_multiRP_index_, df_protons_multiRP_events_, df_ppstracks_index_ = process_data_protons_multiRP(
                self.lepton_type_,
                self.data_sample_,
                df_protons_multiRP_,
                df_ppstracks_,
                apply_fiducial=apply_fiducial,
                within_aperture=within_aperture,
                random_protons=self.random_protons_,
                mix_protons=self.mix_protons_,
                calculate_vars_pp=calculate_vars_pp,
                select_2protons=select_2protons,
                runOnMC=self.runOnMC_,
                use_hash_index=self.use_hash_index_,
                debug=debug
                )

            
            if self.use_dask:
                df_protons_multiRP_index_ = df_protons_multiRP_index_.compute()
                df_protons_multiRP_events_ = df_protons_multiRP_events_.compute()
            print ( df_protons_multiRP_index_ )
            df_protons_multiRP_index_.to_parquet( file_path_protons_multiRP_, engine='pyarrow' )
            print ( df_protons_multiRP_events_ )
            df_protons_multiRP_events_.to_parquet( file_path_events_multiRP_, engine='pyarrow' )
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

