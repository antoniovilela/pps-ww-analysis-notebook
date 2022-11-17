import os
import numpy as np
import pandas as pd
import h5py
# from processing import *
# from processing import df_run_ranges_2017, df_run_ranges_2018, df_run_ranges_mixing_2017, df_run_ranges_mixing_2018, lumi_periods_2017, lumi_periods_2018
from processing import df_run_ranges_2017, df_run_ranges_2018
import ROOT

class ProcessDataEvents:

    def __init__( self, lepton_type, data_sample, labels, fileNames, runOnMC=False, output_dir="" ):

        if lepton_type not in ( 'muon', 'electron' ):
            raise RuntimeError( "Invalid lepton_type argument." )

        if data_sample not in ( '2017', '2018' ):
            raise RuntimeError( "Invalid data_sample argument." )

        self.lepton_type_ = lepton_type
        self.data_sample_ = data_sample
        self.labels_ = labels
        self.fileNames_ = fileNames
        self.output_dir_ = None
        if output_dir is not None and output_dir != "": self.output_dir_ = output_dir
        # self.use_hash_index_ = use_hash_index
        self.runOnMC_ = runOnMC
        self.data_periods_ = None
        if self.data_sample_ == '2017':
            self.data_periods_ = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
        elif self.data_sample_ == '2018':
            self.data_periods_ = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

        self.jecPars_ = None
        self.jecUncertainty_ = None
        if self.runOnMC_:
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
            
            # if self.data_sample_ == '2017' or self.data_sample_ == '2018':
            #     self.jecPars_ = ROOT.JetCorrectorParameters( cmssw_base_ + "/src/PhysicsTools/NanoAODTools/data/jme/" + "Fall17_17Nov2017_V32_MC_Uncertainty_AK8PFchs.txt" )
            if self.data_sample_ == '2017':
                self.jecPars_ = ROOT.JetCorrectorParameters( "jes_jer/2017-JEC-JER/" + "Summer19UL17_V5_MC_Uncertainty_AK8PFchs.txt" )
            elif self.data_sample_ == '2018':
                self.jecPars_ = ROOT.JetCorrectorParameters( "jes_jer/2018-JEC-JER/" + "Summer19UL18_V5_MC_Uncertainty_AK8PFchs.txt" )
            print ( self.jecPars_ )
            self.jecUncertainty_ = ROOT.JetCorrectionUncertainty( self.jecPars_ )
            print ( self.jecUncertainty_ )


    def getJetUncertainty( self, jet_eta, jet_pt ):
        self.jecUncertainty_.setJetEta( jet_eta )
        self.jecUncertainty_.setJetPt( jet_pt )
        unc_ = self.jecUncertainty_.getUncertainty(True)
        return unc_

    def fetchDataPeriod( self, df ):
        run_str_ = "run"
        if self.runOnMC_:
            run_str_ = "run_mc"

        if "period" not in df.columns:
            df_run_ranges_ = None
            if self.data_sample_ == '2017':
                df_run_ranges_ = df_run_ranges_2017
            elif self.data_sample_ == '2018':
                df_run_ranges_ = df_run_ranges_2018

            df.loc[ :, "period" ] = np.nan
            for idx_ in range( df_run_ranges_.shape[0] ):
                msk_period_ = ( ( df.loc[ :, run_str_ ] >= df_run_ranges_.iloc[ idx_ ][ "min" ] ) & ( df.loc[ :, run_str_ ] <= df_run_ranges_.iloc[ idx_ ][ "max" ] ) )
                sum_period_ = np.sum( msk_period_ )
                if sum_period_ > 0:
                    period_key_ = df_run_ranges_.index[ idx_ ]
                    df.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
                    print ( "{}: {}".format( period_key_, sum_period_ ) )
            print ( df.loc[ :, "period" ] )

    def calculateJets( self, df ):
        label_ = "_nom"
        df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" ]
        df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" ]
        df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ]
        df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ]
        df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
        df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
        if self.runOnMC_:
            label_ = "_nom"
            'jet0_cjer', 'jet0_cjer_up', 'jet0_cjer_down'
            # df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ] * ( df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ] * ( df.loc[ :, "C_JER_ref" ] )
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" ] * ( df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" ] * ( df.loc[ :, "jet0_cjer" ] )

            label_ = "_jes_up"
            df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" + "_nom" ] * ( 1. + df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" + "_nom" ] * ( 1. + df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" + "_nom" ]
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" + "_nom" ] * ( 1. + df.loc[ :, "jet0_unc" ] )
            df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
            label_ = "_jes_dw"
            df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" + "_nom" ] * ( 1. - df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" + "_nom" ] * ( 1. - df.loc[ :, "jet0_unc" ] ) 
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" + "_nom" ]
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" + "_nom" ] * ( 1. - df.loc[ :, "jet0_unc" ] )
            df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )

            label_ = "_jer_up"
            # df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" + "_nom" ] * ( df.loc[ :, "C_JER_jer_up" ] / df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" + "_nom" ] * ( df.loc[ :, "C_JER_jer_up" ] / df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" + "_nom" ] * ( df.loc[ :, "C_JER_jer_up" ] / df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" + "_nom" ] * ( df.loc[ :, "C_JER_jer_up" ] / df.loc[ :, "C_JER_ref" ] )
            df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" + "_nom" ] * ( df.loc[ :, "jet0_cjer_up" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" + "_nom" ] * ( df.loc[ :, "jet0_cjer_up" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" + "_nom" ] * ( df.loc[ :, "jet0_cjer_up" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" + "_nom" ] * ( df.loc[ :, "jet0_cjer_up" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_px" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.cos( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_py" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sin( df.loc[ :, "jet0_phi" ] ) )
            df.loc[ :, "jet0_pz" + label_ ]       = ( df.loc[ :, "jet0_pt" + label_ ] * np.sinh( df.loc[ :, "jet0_eta" ] ) )
            label_ = "_jer_dw"
            # df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" + "_nom" ] * ( df.loc[ :, "C_JER_jer_dw" ] / df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" + "_nom" ] * ( df.loc[ :, "C_JER_jer_dw" ] / df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" + "_nom" ] * ( df.loc[ :, "C_JER_jer_dw" ] / df.loc[ :, "C_JER_ref" ] )
            # df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" + "_nom" ] * ( df.loc[ :, "C_JER_jer_dw" ] / df.loc[ :, "C_JER_ref" ] )
            df.loc[ :, "jet0_pt" + label_ ]       = df.loc[ :, "jet0_pt" + "_nom" ] * ( df.loc[ :, "jet0_cjer_down" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_energy" + label_ ]   = df.loc[ :, "jet0_energy" + "_nom" ] * ( df.loc[ :, "jet0_cjer_down" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_mass" + label_ ]     = df.loc[ :, "jet0_mass" + "_nom" ] * ( df.loc[ :, "jet0_cjer_down" ] / df.loc[ :, "jet0_cjer" ] )
            df.loc[ :, "jet0_corrmass" + label_ ] = df.loc[ :, "jet0_corrmass" + "_nom" ] * ( df.loc[ :, "jet0_cjer_down" ] / df.loc[ :, "jet0_cjer" ] )
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
        if self.runOnMC_:
            # Muon scale factors
            from muon_efficiency import MuonIDScaleFactor, MuonTRGScaleFactor 
            # ID
            # file_eff_MuID = ROOT.TFile.Open( "efficiencies/muon/RunBCDEF_SF_MuID.root", "READ" )
            file_eff_MuID_ = None
            histName_MuID_ = None
            if self.data_sample_ == '2017':
                file_eff_MuID_ = ROOT.TFile.Open( "efficiencies/muon/id/2017/Efficiencies_muon_generalTracks_Z_Run2017_UL_ID.root", "READ" )
                histName_MuID_ = "NUM_TrkHighPtID_DEN_TrackerMuons_abseta_pt"
            elif self.data_sample_ == '2018':
                file_eff_MuID_ = ROOT.TFile.Open( "efficiencies/muon/id/2018/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.root", "READ" )
                histName_MuID_ = "NUM_TrkHighPtID_DEN_TrackerMuons_abseta_pt"

            # muon_scale_factor_ = MuonScaleFactor( histos={ "MuID": file_eff_MuID.Get( "NUM_TightID_DEN_genTracks_pt_abseta" ) } )
            muon_scale_factor_ID_ = MuonIDScaleFactor(
                histos={ "MuID": file_eff_MuID_.Get( histName_MuID_ ),
                         "MuID_stat": file_eff_MuID_.Get( histName_MuID_ + "_stat" ),
                         "MuID_syst": file_eff_MuID_.Get( histName_MuID_ + "_syst" ) }
                )
            # f_sf_muon_id_ = lambda row: muon_scale_factor_( row["muon0_pt"], row["muon0_eta"] )[ 0 ]
            # f_sf_muon_id_unc_ = lambda row: muon_scale_factor_( row["muon0_pt"], row["muon0_eta"] )[ 1 ]
            f_sf_muon_id_ = lambda row: muon_scale_factor_ID_( row["muon0_eta"], row["muon0_pt"] )[ 0 ]
            f_sf_muon_id_unc_ = lambda row: muon_scale_factor_ID_( row["muon0_eta"], row["muon0_pt"] )[ 1 ]
            df.loc[ :, 'sf_muon_id' ] = df[ [ "muon0_eta", "muon0_pt" ] ].apply( f_sf_muon_id_, axis=1 )
            df.loc[ :, 'sf_muon_id_unc' ] = df[ [ "muon0_eta", "muon0_pt" ] ].apply( f_sf_muon_id_unc_, axis=1 )
            df.loc[ :, 'sf_muon_id_up' ] = ( df.loc[ :, 'sf_muon_id' ] + df.loc[ :, 'sf_muon_id_unc' ] )
            df.loc[ :, 'sf_muon_id_dw' ] = ( df.loc[ :, 'sf_muon_id' ] - df.loc[ :, 'sf_muon_id_unc' ] )

            # TRG
            file_eff_MuTRG_ = None
            histName_MuTRG_ = None
            if self.data_sample_ == '2017':
                file_eff_MuTRG_ = ROOT.TFile.Open( "efficiencies/muon/trigger/2017/Efficiencies_muon_generalTracks_Z_Run2017_UL_SingleMuonTriggers.root", "READ" )
                histName_MuTRG_ = "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"
            elif self.data_sample_ == '2018':
                file_eff_MuTRG_ = ROOT.TFile.Open( "efficiencies/muon/trigger/2018/Efficiencies_muon_generalTracks_Z_Run2018_UL_SingleMuonTriggers.root", "READ" )
                histName_MuTRG_ = "NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"

            muon_scale_factor_TRG_ = MuonTRGScaleFactor(
                histos={ "MuTRG": file_eff_MuTRG_.Get( histName_MuTRG_ ),
                         "MuTRG_stat": file_eff_MuTRG_.Get( histName_MuTRG_ + "_stat" ),
                         "MuTRG_syst": file_eff_MuTRG_.Get( histName_MuTRG_ + "_syst" ) }
                )
            f_sf_muon_trigger_ = lambda row: muon_scale_factor_TRG_( row["muon0_eta"], row["muon0_pt"] )[ 0 ]
            f_sf_muon_trigger_unc_ = lambda row: muon_scale_factor_TRG_( row["muon0_eta"], row["muon0_pt"] )[ 1 ]
            df.loc[ :, 'sf_muon_trigger' ] = df[ [ "muon0_eta", "muon0_pt" ] ].apply( f_sf_muon_trigger_, axis=1 )
            df.loc[ :, 'sf_muon_trigger_unc' ] = df[ [ "muon0_eta", "muon0_pt" ] ].apply( f_sf_muon_trigger_unc_, axis=1 )
            df.loc[ :, 'sf_muon_trigger_up' ] = ( df.loc[ :, 'sf_muon_trigger' ] + df.loc[ :, 'sf_muon_trigger_unc' ] )
            df.loc[ :, 'sf_muon_trigger_dw' ] = ( df.loc[ :, 'sf_muon_trigger' ] - df.loc[ :, 'sf_muon_trigger_unc' ] )

    def calculateElectrons( self, df ):
        label_ = "_nom"
        df.loc[ :, "electron0_pt" + label_ ]     = df.loc[ :, "electron0_pt" ]
        df.loc[ :, "electron0_energy" + label_ ] = df.loc[ :, "electron0_energy" ]
        df.loc[ :, "electron0_px" + label_ ]     = ( df.loc[ :, "electron0_pt" + label_ ] * np.cos( df.loc[ :, "electron0_phi" ] ) )
        df.loc[ :, "electron0_py" + label_ ]     = ( df.loc[ :, "electron0_pt" + label_ ] * np.sin( df.loc[ :, "electron0_phi" ] ) )
        df.loc[ :, "electron0_pz" + label_ ]     = ( df.loc[ :, "electron0_pt" + label_ ] * np.sinh( df.loc[ :, "electron0_eta" ] ) )
        if self.runOnMC_:
            # Electron scale factor
            from electron_efficiency import ElectronScaleFactor
            # ID
            # file_eff_EleID = ROOT.TFile.Open( "efficiencies/electron/2017_ElectronTight.root", "READ" )
            file_eff_EleID_ = None
            histName_EleID_ = "EGamma_SF2D"
            if self.data_sample_ == '2017':
                file_eff_EleID_ = ROOT.TFile.Open( "efficiencies/electron/id/2017/egammaEffi.txt_EGM2D_Tight_UL17.root", "READ" )
            elif self.data_sample_ == '2018':
                file_eff_EleID_ = ROOT.TFile.Open( "efficiencies/electron/id/2018/egammaEffi.txt_Ele_Tight_EGM2D.root", "READ" )

            electron_scale_factor_ID_ = ElectronScaleFactor( histos={ "EleID": file_eff_EleID_.Get( histName_EleID_ ) } )
            f_sf_electron_id_ = lambda row: electron_scale_factor_ID_( row["electron0_eta"], row["electron0_pt"] )[ 0 ]
            f_sf_electron_id_unc_ = lambda row: electron_scale_factor_ID_( row["electron0_eta"], row["electron0_pt"] )[ 1 ]
            df.loc[ :, 'sf_electron_id' ] = df[ [ "electron0_eta", "electron0_pt" ] ].apply( f_sf_electron_id_, axis=1 )
            df.loc[ :, 'sf_electron_id_unc' ] = df[ [ "electron0_eta", "electron0_pt" ] ].apply( f_sf_electron_id_unc_, axis=1 )
            df.loc[ :, 'sf_electron_id_up' ] = ( df.loc[ :, 'sf_electron_id' ] + df.loc[ :, 'sf_electron_id_unc' ] )
            df.loc[ :, 'sf_electron_id_dw' ] = ( df.loc[ :, 'sf_electron_id' ] - df.loc[ :, 'sf_electron_id_unc' ] )

            # TRG
            file_eff_EleTRG_ = None
            histName_EleTRG_ = "EGamma_SF2D"
            if self.data_sample_ == '2017':
                file_eff_EleTRG_ = ROOT.TFile.Open( "", "READ" )
            elif self.data_sample_ == '2018':
                file_eff_EleTRG_ = ROOT.TFile.Open( "efficiencies/electron/trigger/2018/egammaEffi.txt_EGM2D-Trigger.root", "READ" )

            electron_scale_factor_TRG_ = ElectronScaleFactor( histos={ "EleTRG": file_eff_EleTRG_.Get( histName_EleTRG_ ) } )
            f_sf_electron_trigger_ = lambda row: electron_scale_factor_TRG_( row["electron0_eta"], row["electron0_pt"] )[ 0 ]
            f_sf_electron_trigger_unc_ = lambda row: electron_scale_factor_TRG_( row["electron0_eta"], row["electron0_pt"] )[ 1 ]
            df.loc[ :, 'sf_electron_trigger' ] = df[ [ "electron0_eta", "electron0_pt" ] ].apply( f_sf_electron_trigger_, axis=1 )
            df.loc[ :, 'sf_electron_trigger_unc' ] = df[ [ "electron0_eta", "electron0_pt" ] ].apply( f_sf_electron_trigger_unc_, axis=1 )
            df.loc[ :, 'sf_electron_trigger_up' ] = ( df.loc[ :, 'sf_electron_trigger' ] + df.loc[ :, 'sf_electron_trigger_unc' ] )
            df.loc[ :, 'sf_electron_trigger_dw' ] = ( df.loc[ :, 'sf_electron_trigger' ] - df.loc[ :, 'sf_electron_trigger_unc' ] )

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
        if self.runOnMC_: pass

    def calculateWW( self, df ):
        label_ = "_nom"
        df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + label_ ] + df.loc[ :, "jet0_energy" + label_ ] )
        df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + label_ ] + df.loc[ :, "jet0_pz" + label_ ] )
        df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPx" + label_ ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
                                                   ( df.loc[ :, "WLeptonicPy" + label_ ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
                                                   ( df.loc[ :, "WW_pz" + label_ ] )**2 ) )
        df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
        if self.runOnMC_:
            # label_ = "_jes_up"
            # df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label_ ] )
            # df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label_ ] )
            # df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
            #                                            ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
            #                                            ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
            #                                            ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
            # df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
            # label_ = "_jes_dw"
            # df.loc[ :, "WW_energy" + label_ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label_ ] )
            # df.loc[ :, "WW_pz" + label_ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label_ ] )
            # df.loc[ :, "MWW" + label_ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
            #                                            ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label_ ] )**2 -
            #                                            ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label_ ] )**2 -
            #                                            ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
            # df.loc[ :, "YWW" + label_ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label_ ] + df.loc[ :, "WW_pz" + label_ ] ) / ( df.loc[ :, "WW_energy" + label_ ] - df.loc[ :, "WW_pz" + label_ ] ) ) )
            labels__ = [ "_jes_up", "_jes_dw", "_jer_up", "_jer_dw" ]
            for label__ in labels__:
                df.loc[ :, "WW_energy" + label__ ]  = ( df.loc[ :, "WLeptonicE" + "_nom" ] + df.loc[ :, "jet0_energy" + label__ ] )
                df.loc[ :, "WW_pz" + label__ ]      = ( df.loc[ :, "WLeptonicPz" + "_nom" ] + df.loc[ :, "jet0_pz" + label__ ] )
                df.loc[ :, "MWW" + label__ ]   = ( np.sqrt( ( df.loc[ :, "WW_energy" + "_nom" ] )**2 -
                                                           ( df.loc[ :, "WLeptonicPx" + "_nom" ] + df.loc[ :, "jet0_px" + label__ ] )**2 -
                                                           ( df.loc[ :, "WLeptonicPy" + "_nom" ] + df.loc[ :, "jet0_py" + label__ ] )**2 -
                                                           ( df.loc[ :, "WW_pz" + "_nom" ] )**2 ) )
                df.loc[ :, "YWW" + label__ ]   = ( 0.5 * np.log( ( df.loc[ :, "WW_energy" + label__ ] + df.loc[ :, "WW_pz" + label__ ] ) / ( df.loc[ :, "WW_energy" + label__ ] - df.loc[ :, "WW_pz" + label__ ] ) ) )

    def calculateXiCMS( self, df ):
        label_ = "_nom"
        df.loc[ :, "xiCMS_45" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
                                                              df.loc[ :, "jet0_pt" + "_nom" ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
        df.loc[ :, "xiCMS_56" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
                                                              df.loc[ :, "jet0_pt" + "_nom" ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )
        if self.runOnMC_:
           # label_ = "_jes_up"
           # df.loc[ :, "xiCMS_45" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
           #                                                       df.loc[ :, "jet0_pt" + label_ ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
           # df.loc[ :, "xiCMS_56" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
           #                                                       df.loc[ :, "jet0_pt" + label_ ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )
           # label_ = "_jes_dw"
           # df.loc[ :, "xiCMS_45" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
           #                                                       df.loc[ :, "jet0_pt" + label_ ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
           # df.loc[ :, "xiCMS_56" + label_ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
           #                                                       df.loc[ :, "jet0_pt" + label_ ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )
           labels__ = [ "_jes_up", "_jes_dw", "_jer_up", "_jer_dw" ]
           for label__ in labels__:
               df.loc[ :, "xiCMS_45" + label__ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( df.loc[ :, "WLeptonicEta" ] ) +
                                                                     df.loc[ :, "jet0_pt" + label__ ] * np.exp( df.loc[ :, "jet0_eta" ] ) )
               df.loc[ :, "xiCMS_56" + label__ ] = ( 1. / 13000 ) * ( df.loc[ :, "WLeptonicPt" + "_nom" ] * np.exp( -df.loc[ :, "WLeptonicEta" ] ) +
                                                                     df.loc[ :, "jet0_pt" + label__ ] * np.exp( -df.loc[ :, "jet0_eta" ] ) )
    def get_data( self, fileNames ):

        df_events_list = []
        df_counts_list = []
    
        for file_ in fileNames:
            print ( file_ )
            with h5py.File( file_, 'r' ) as f:
                print ( list(f.keys()) )
    
                dset_events = f['events']
                print ( dset_events.shape )
                print ( dset_events[:,:] )
    
                dset_columns_events = f['columns_events']
                print ( dset_columns_events.shape )
                columns_events = [ item.decode("utf-8") for item in list( dset_columns_events ) ]
                print ( columns_events )
    
                dset_selections = f['selections']
                selections_ = [ item.decode("utf-8") for item in dset_selections ]
                print ( selections_ )
    
                dset_counts = f['event_counts']
                df_counts_list.append( pd.Series( dset_counts, index=selections_ ) )
                print ( df_counts_list[-1] )
    
                chunk_size = 1000000
                entries_events = dset_events.shape[0]
                start_ = list( range( 0, entries_events, chunk_size ) )
                stop_ = start_[1:]
                stop_.append( entries_events )
                print ( start_ )
                print ( stop_ )
                astype_dict_events_ = {
                    "run": "int64", "lumiblock": "int64", "event": "int64",
                    "nVertices": "int32",
                    "num_bjets_ak8": "int32", "num_bjets_ak4": "int32", "num_jets_ak4": "int32",
                    "pfcand_nextracks": "int32", "pfcand_nextracks_noDRl": "int32"
                    }
                astype_dict_events_ = astype_dict_events_.copy()
    
                if "muon0_charge" in columns_events:
                    astype_dict_events_.update( { "muon0_charge": "int32" } )
     
                if "electron0_charge" in columns_events:
                    astype_dict_events_.update( { "electron0_charge": "int32" } )
    
                if "run_mc" in columns_events:
                    astype_dict_events_.update( { "run_mc": "int64" } )
    
                for idx in range( len( start_ ) ):
                    print ( start_[idx], stop_[idx] )
                    #print ( dset[ start_[idx] : stop_[idx] ] )
                    df_ = pd.DataFrame( dset_events[ start_[idx] : stop_[idx] ], columns=columns_events ).astype( astype_dict_events_ )
                    df_events_list.append( df_ )
                    print ( df_events_list[-1].head() )
                    print ( "Data set size: {}".format( len( df_events_list[-1] ) ) )
    
        df_counts = df_counts_list[0]
        for idx in range( 1, len( df_counts_list ) ):
            df_counts = df_counts.add( df_counts_list[idx] )
        print ( df_counts )
    
        df_events = pd.concat( df_events_list )
        print ( df_events )
    
        return ( df_counts, df_events )

    def __call__( self ):

        df_counts = {}
        df_events = {}
        
        for label_ in self.labels_:
            import time
            print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
            time_s_ = time.time()

            file_path_ = None
            file_name_label_ =  "data-store-{}.h5".format( label_ )
            if self.output_dir_ is not None and self.output_dir_ != "":
                file_path_ = "{}/{}".format( self.output_dir_, file_name_label_ )
            else:
                file_path_ = file_name_label_
            print ( file_path_ )
            with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
        
                df_counts_, df_events_ = self.get_data( self.fileNames_[ label_ ] )

                self.fetchDataPeriod( df_events_ ) 

                if self.runOnMC_:
                    f_jecUncertainty_ = lambda row_: self.getJetUncertainty( row_[ "jet0_eta" ], row_[ "jet0_pt" ] )
                    df_events_.loc[ :, "jet0_unc" ] = df_events_[ [ "jet0_pt", "jet0_eta" ] ].apply( f_jecUncertainty_, axis=1 )
                    print ( df_events_.loc[ :, "jet0_unc" ] )
                    # df_events_.loc[ :, "jet0_pt_up" ] = df_events_.loc[ :, "jet0_pt" ] * ( 1. + df_events_.loc[ :, "jet0_unc" ] )
                    # df_events_.loc[ :, "jet0_pt_dw" ] = df_events_.loc[ :, "jet0_pt" ] * ( 1. - df_events_.loc[ :, "jet0_unc" ] )
                    df_events_.loc[ :, 'jet0_pt_unsmeared' ] = np.sqrt(
                        df_events_.loc[ :, 'jet0_px' ] ** 2 +
                        df_events_.loc[ :, 'jet0_py' ] ** 2 )
                    df_events_.loc[ :, 'C_JER_ref' ] = ( df_events_.loc[ :, 'jet0_pt' ] / df_events_.loc[ :, 'jet0_pt_unsmeared' ] )
                    deltaPhi_jet_genjet_ = ( df_events_.loc[ :, "jet0_phi"] - df_events_.loc[ :, "gen_jet0_phi"] )
                    msk_dphi_ = ( deltaPhi_jet_genjet_ < -np.pi )
                    deltaPhi_jet_genjet_.loc[ msk_dphi_ ] = deltaPhi_jet_genjet_.loc[ msk_dphi_ ] + 2*np.pi
                    msk_dphi_ = ( deltaPhi_jet_genjet_ >= np.pi )
                    deltaPhi_jet_genjet_.loc[ msk_dphi_ ] = deltaPhi_jet_genjet_.loc[ msk_dphi_ ] - 2*np.pi
                    deltaEta_jet_genjet_ = ( df_events_.loc[ :, "jet0_eta"] - df_events_.loc[ :, "gen_jet0_eta"] )
                    deltaR_jet_genjet_ = np.sqrt( ( deltaPhi_jet_genjet_ ) ** 2 + ( deltaEta_jet_genjet_ ) ** 2 )
                    df_events_.loc[ :, 'deltaR_jet_genjet' ] = deltaR_jet_genjet_
                    df_events_.loc[ :, 'deltaPt_jet_genjet' ] = np.abs( df_events_.loc[ :, 'jet0_pt_unsmeared' ] - df_events_.loc[ :, 'gen_jet0_pt' ] )
                    df_events_.loc[ :, 'match_jet_genjet' ] = (
                        ( df_events_.loc[ :, 'deltaR_jet_genjet' ] < ( 0.8 / 2 ) ) &
                        ( df_events_.loc[ :, 'deltaPt_jet_genjet' ] < ( 3. * df_events_.loc[ :, 'jet0_jer_res' ] * df_events_.loc[ :, 'jet0_pt_unsmeared' ] ) )
                        )
                    print ( df_events_.loc[ :, 'match_jet_genjet' ] )
                    print ( np.sum( df_events_.loc[ :, 'match_jet_genjet' ] ) )
                    print ( np.sum( df_events_.loc[ :, 'match_jet_genjet' ] ) / df_events_.shape[0] )
                    df_events_.loc[ :, 'C_JER' ] = np.nan
                    df_events_.loc[ :, 'JER_rand' ] = np.nan
                    df_events_.loc[ :, 'C_JER_jer_up' ] = np.nan
                    df_events_.loc[ :, 'C_JER_jer_dw' ] = np.nan
                    msk_match_ = df_events_.loc[ :, 'match_jet_genjet' ]
                    
                    df_events_.loc[ :, 'C_JER' ].where( ~msk_match_,
                        ( 1. + ( df_events_.loc[ :, 'jet0_jer_sf' ] - 1. ) *
                               ( ( df_events_.loc[ :, 'jet0_pt_unsmeared' ] - df_events_.loc[ :, 'gen_jet0_pt' ] ) / df_events_.loc[ :, 'jet0_pt_unsmeared' ] ) 
                        ), inplace=True )
                    df_events_.loc[ :, 'C_JER' ].where( msk_match_, df_events_.loc[ :, 'C_JER_ref' ], inplace=True )
                    df_events_.loc[ :, 'JER_rand' ].where( msk_match_,
                        ( ( df_events_.loc[ :, 'C_JER_ref' ] - 1. ) / np.sqrt( np.max( ( ( df_events_.loc[ :, 'jet0_jer_sf' ] ** 2 ) - 1. ) , 0. ) ) ),
                        inplace=True
                        )
                    df_events_.loc[ :, 'C_JER_jer_up' ].where( ~msk_match_,
                        ( 1. + ( df_events_.loc[ :, 'jet0_jer_sfup' ] - 1. ) *
                               ( ( df_events_.loc[ :, 'jet0_pt_unsmeared' ] - df_events_.loc[ :, 'gen_jet0_pt' ] ) / df_events_.loc[ :, 'jet0_pt_unsmeared' ] )
                        ), inplace=True )
                    df_events_.loc[ :, 'C_JER_jer_dw' ].where( ~msk_match_,
                        ( 1. + ( df_events_.loc[ :, 'jet0_jer_sfdown' ] - 1. ) *
                               ( ( df_events_.loc[ :, 'jet0_pt_unsmeared' ] - df_events_.loc[ :, 'gen_jet0_pt' ] ) / df_events_.loc[ :, 'jet0_pt_unsmeared' ] )
                        ), inplace=True )
                    df_events_.loc[ :, 'C_JER_jer_up' ].where( msk_match_, ( 1. + df_events_.loc[ :, 'JER_rand' ] * np.sqrt( np.max( ( ( df_events_.loc[ :, 'jet0_jer_sfup' ] ** 2 ) - 1. ) , 0. ) ) ), inplace=True )
                    df_events_.loc[ :, 'C_JER_jer_dw' ].where( msk_match_, ( 1. + df_events_.loc[ :, 'JER_rand' ] * np.sqrt( np.max( ( ( df_events_.loc[ :, 'jet0_jer_sfdown' ] ** 2 ) - 1. ) , 0. ) ) ), inplace=True )
                    print ( df_events_.loc[ :, 'C_JER' ] )
                    print ( df_events_.loc[ :, 'C_JER_jer_up' ] )
                    print ( df_events_.loc[ :, 'C_JER_jer_dw' ] )

                self.calculateJets( df_events_ )

                if self.lepton_type_ == 'muon':
                    self.calculateMuons( df_events_ )
                elif self.lepton_type_ == 'electron':
                    self.calculateElectrons( df_events_ )

                self.calculateWLep( df_events_ )
                self.calculateWW( df_events_ )
                self.calculateXiCMS( df_events_ )

                store_[ "counts" ] = df_counts_
                store_[ "events" ] = df_events_
            
            time_e_ = time.time()
            print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

            # with pd.HDFStore( "reduced-data-store-{}.h5".format( label_ ), 'r' ) as store_:
            with pd.HDFStore( file_path_, 'r' ) as store_:
                print ( list( store_ ) )
