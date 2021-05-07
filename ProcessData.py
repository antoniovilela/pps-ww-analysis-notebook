import os
from processing import *
import ROOT

class ProcessData:
    def __init__( self, labels, fileNames ):
        self.labels_ = labels
        self.fileNames_ = fileNames

        cmssw_release_base_ = os.environ[ 'CMSSW_RELEASE_BASE' ]
        print ( cmssw_release_base_ )
        cmssw_base_ = os.environ[ 'CMSSW_BASE' ]
        print( cmssw_base_ )

        libraries_ = ROOT.gSystem.GetLibraries().split()
        found_ = False
        for item in libraries_:
            if item.find( "libCondFormatsJetMETObjects.so" ) >= 0: found_ = True

        if not found_:
            lib_path_ = cmssw_release_base_ + "/lib/slc7_amd64_gcc900/libCondFormatsJetMETObjects.so"
            print ( "Loading {}".format( lib_path_ ) )
            ROOT.gSystem.Load( lib_path_ )

        self.jecPars_ = ROOT.JetCorrectorParameters( cmssw_base_ + "/src/PhysicsTools/NanoAODTools/data/jme/" + "Fall17_17Nov2017_V32_MC_Uncertainty_AK8PFchs.txt" )
        print ( self.jecPars_ )
        self.jecUncertainty_ = ROOT.JetCorrectionUncertainty( self.jecPars_ )
        print ( self.jecUncertainty_ )

    def getJetUncertainty( self, jet_eta, jet_pt ):
        self.jecUncertainty_.setJetEta( jet_eta )
        self.jecUncertainty_.setJetPt( jet_pt )
        unc_ = self.jecUncertainty_.getUncertainty(True)
        return unc_

    def calculateJets( self, df ):
        label_ = "_nom"
        df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ]
        df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ]
        df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ]
        df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ]
        df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
        label_ = "_jes_up"
        df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ] * ( 1. + df.loc[ :, "jet0_unc" ] ) 
        df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ] * ( 1. + df.loc[ :, "jet0_unc" ] ) 
        df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ] * ( 1. + df.loc[ :, "jet0_unc" ] )
        df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ] * ( 1. + df.loc[ :, "jet0_unc" ] )
        df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
        label_ = "_jes_dw"
        df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ] * ( 1. - df.loc[ :, "jet0_unc" ] ) 
        df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ] * ( 1. - df.loc[ :, "jet0_unc" ] ) 
        df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ] * ( 1. - df.loc[ :, "jet0_unc" ] )
        df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ] * ( 1. - df.loc[ :, "jet0_unc" ] )
        df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )

    def calculateMuons( self, df ):
        label_ = "_nom"
        df.loc[ :, "muon0_pt" + label_ ]     = df.loc[ :, "muon0_pt" ]
        df.loc[ :, "muon0_energy" + label_ ] = df.loc[ :, "muon0_energy" ]
        df.loc[ :, "muon0_px" + label_ ]     = ( df.loc[ :, "muon0_pt" + label_ ] * np.cos( df.loc[ :, "muon0_phi" ] ) )
        df.loc[ :, "muon0_py" + label_ ]     = ( df.loc[ :, "muon0_pt" + label_ ] * np.sin( df.loc[ :, "muon0_phi" ] ) )
        df.loc[ :, "muon0_pz" + label_ ]     = ( df.loc[ :, "muon0_pt" + label_ ] * np.sinh( df.loc[ :, "muon0_eta" ] ) )

    def calculateWLep( self, df ):
        label_ = "_nom"
        df.loc[ :, "WLeptonicPt" + label_ ]  = df.loc[ :, "WLeptonicPt" ]
        df.loc[ :, "WLeptonicPx" + label_ ]  = ( df.loc[ :, "WLeptonicPt" + label_ ] * np.cos( df.loc[ :, "WLeptonicPhi" ] ) )
        df.loc[ :, "WLeptonicPy" + label_ ]  = ( df.loc[ :, "WLeptonicPt" + label_ ] * np.sin( df.loc[ :, "WLeptonicPhi" ] ) )
        df.loc[ :, "WLeptonicPz" + label_ ]  = ( df.loc[ :, "WLeptonicPt" + label_ ] * np.sinh( df.loc[ :, "WLeptonicEta" ] ) )
        df.loc[ :, "WLeptonicE" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WLeptonicPt" + label_ ] * np.cosh( df.loc[ :, "WLeptonicEta" ] ) )**2 + df.loc[ :, "recoMWlep" ] **2 ) )
        df.loc[ :, "WLeptonicM" + label_ ]   = ( np.sqrt( df.loc[ :, "WLeptonicE" + label_ ]**2 -
                                                 df.loc[ :, "WLeptonicPx" + label_ ]**2 -
                                                 df.loc[ :, "WLeptonicPy" + label_ ]**2 -
                                                 df.loc[ :, "WLeptonicPz" + label_ ]**2 ) ) 

    def calculateWW( self, df ):
        label_ = "_nom"
        df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + label_ ] + df.loc[ :, "jet0_energy" + label_ ] )
        df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + label_ ] + df.loc[ :, "jet0_pz" + label_ ] )
        df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPx" + label_ ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPy" + label_ ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                   ( df.loc[ :, "WW_pz" + label_ ] )**2 ) )
        df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
        label_ = "_jes_up"
        df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label_ ] )
        df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label_ ] )
        df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                   ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
        df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
        label_ = "_jes_dw"
        df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label_ ] )
        df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label_ ] )
        df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                   ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
        df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
        
    def __call__( self, apply_fiducial=True, within_aperture=False, random_protons=False, mix_protons=False, select_2protons=True, runOnMC=False ):

        df_counts = {}
        df_protons_multiRP_index = {}
        df_protons_multiRP_events = {}
        
        for label_ in self.labels_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()
        
            with pd.HDFStore( "reduced-data-store-{}.h5".format( label_ ), complevel=5 ) as store_:
        
                df_counts_, df_protons_multiRP_, df_protons_singleRP_, df_ppstracks_ = get_data( self.fileNames_[ label_ ] )

                f_jecUncertainty_ = lambda row_: self.getJetUncertainty( row_[ "jet0_eta" ], row_[ "jet0_pt" ] )
                df_protons_multiRP_.loc[ :, "jet0_unc" ] = df_protons_multiRP_[ [ "jet0_pt", "jet0_eta" ] ].apply( f_jecUncertainty_, axis=1 )
                print ( df_protons_multiRP_.loc[ :, "jet0_unc" ] )
                # df_protons_multiRP_.loc[ :, "jet0_pt_up" ] = df_protons_multiRP_.loc[ :, "jet0_pt" ] * ( 1. + df_protons_multiRP_.loc[ :, "jet0_unc" ] )
                # df_protons_multiRP_.loc[ :, "jet0_pt_dw" ] = df_protons_multiRP_.loc[ :, "jet0_pt" ] * ( 1. - df_protons_multiRP_.loc[ :, "jet0_unc" ] )
                self.calculateJets( df_protons_multiRP_ )
                self.calculateMuons( df_protons_multiRP_ )
                self.calculateWLep( df_protons_multiRP_ )
                self.calculateWW( df_protons_multiRP_ )

                df_protons_multiRP_index_, df_protons_multiRP_events_, df_ppstracks_index_ = process_data_protons_multiRP(
                    df_protons_multiRP_, df_ppstracks_,
                    apply_fiducial=apply_fiducial,
                    within_aperture=within_aperture,
                    random_protons=random_protons,
                    mix_protons=mix_protons,
                    select_2protons=select_2protons,
                    runOnMC=runOnMC
                    )

                store_[ "counts" ] = df_counts_
                store_[ "protons_multiRP"] = df_protons_multiRP_index_
                store_[ "events_multiRP" ] = df_protons_multiRP_events_
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

            with pd.HDFStore( "reduced-data-store-{}.h5".format( label_ ), 'r' ) as store_:
                print ( list( store_ ) )