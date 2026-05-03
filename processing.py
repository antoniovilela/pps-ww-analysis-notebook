import numpy as np
import pandas as pd
import dask.dataframe as dd
# import ROOT

run_ranges_periods_2017 = {}
run_ranges_periods_2017[ "2017B" ]  = (297020,299329)
run_ranges_periods_2017[ "2017C1" ] = (299337,300785)
run_ranges_periods_2017[ "2017C2" ] = (300806,302029)
run_ranges_periods_2017[ "2017D" ]  = (302030,303434)
run_ranges_periods_2017[ "2017E" ]  = (303435,304826)
run_ranges_periods_2017[ "2017F1" ] = (304911,305114)
run_ranges_periods_2017[ "2017F2" ] = (305178,305902)
run_ranges_periods_2017[ "2017F3" ] = (305965,306462)
df_run_ranges_2017 = pd.DataFrame( run_ranges_periods_2017, index=("min","max") ).transpose()
run_ranges_periods_mixing_2017 = run_ranges_periods_2017
df_run_ranges_mixing_2017 = df_run_ranges_2017
run_ranges_periods_2018 = {}
run_ranges_periods_2018[ "2018A" ]  = (315252,316995)
run_ranges_periods_2018[ "2018B1" ] = (316998,317696)
run_ranges_periods_2018[ "2018B2" ] = (318622,319312)
run_ranges_periods_2018[ "2018C" ]  = (319313,320393)
run_ranges_periods_2018[ "2018D1" ] = (320394,322633)
run_ranges_periods_2018[ "2018D2" ] = (323363,325273)
df_run_ranges_2018 = pd.DataFrame( run_ranges_periods_2018, index=("min","max") ).transpose()
run_ranges_periods_mixing_2018 = {}
run_ranges_periods_mixing_2018[ "2018A" ]  = (315252,316995)
run_ranges_periods_mixing_2018[ "2018B" ]  = (316998,319312)
run_ranges_periods_mixing_2018[ "2018C" ]  = (319313,320393)
run_ranges_periods_mixing_2018[ "2018D1" ] = (320394,322633)
run_ranges_periods_mixing_2018[ "2018D2" ] = (323363,325273)
df_run_ranges_mixing_2018 = pd.DataFrame( run_ranges_periods_mixing_2018, index=("min","max") ).transpose()

# L_2017B = 2.360904801;
# L_2017C1 = 5.313012839;
# L_2017E = 8.958810514;
# L_2017F1 = 1.708478656;
# L_2017C2 = 3.264135878;
# L_2017D = 4.074723964;
# L_2017F2 = 7.877903151;
# L_2017F3 = 3.632463163;
L_2017B = 4.799881474;
L_2017C1 = 5.785813941;
L_2017E = 9.312832062;
L_2017F1 = 1.738905587;
L_2017C2 = 3.786684323;
L_2017D = 4.247682053;
L_2017F2 = 8.125575961;
L_2017F3 = 3.674404546;
lumi_periods_2017 = {}
lumi_periods_2017[ 'muon' ] = {}
lumi_periods_2017[ 'muon' ][ "2017B" ]  = L_2017B
lumi_periods_2017[ 'muon' ][ "2017C1" ] = L_2017C1
lumi_periods_2017[ 'muon' ][ "2017C2" ] = L_2017C2
lumi_periods_2017[ 'muon' ][ "2017D" ]  = L_2017D
lumi_periods_2017[ 'muon' ][ "2017E" ]  = L_2017E
lumi_periods_2017[ 'muon' ][ "2017F1" ] = L_2017F1
lumi_periods_2017[ 'muon' ][ "2017F2" ] = L_2017F2
lumi_periods_2017[ 'muon' ][ "2017F3" ] = L_2017F3
lumi_periods_2017[ 'electron' ] = {}
lumi_periods_2017[ 'electron' ][ "2017B" ]  = L_2017B * 0.957127
lumi_periods_2017[ 'electron' ][ "2017C1" ] = L_2017C1 * 0.954282
lumi_periods_2017[ 'electron' ][ "2017C2" ] = L_2017C2 * 0.954282
lumi_periods_2017[ 'electron' ][ "2017D" ]  = L_2017D * 0.9539
lumi_periods_2017[ 'electron' ][ "2017E" ]  = L_2017E * 0.956406
lumi_periods_2017[ 'electron' ][ "2017F1" ] = L_2017F1 * 0.953733
lumi_periods_2017[ 'electron' ][ "2017F2" ] = L_2017F2 * 0.953733
lumi_periods_2017[ 'electron' ][ "2017F3" ] = L_2017F3 * 0.953733
print ( lumi_periods_2017 )
print ( "Luminosity 2017 muon: {}".format( np.sum( list( lumi_periods_2017[ 'muon' ].values() ) ) ) )
print ( "Luminosity 2017 electron: {}".format( np.sum( list( lumi_periods_2017[ 'electron' ].values() ) ) ) )

# L_2018A  = 12.10
# L_2018B1 = 6.38
# L_2018B2 = 0.40
# L_2018C  = 6.5297
# L_2018D1 = 19.88
# L_2018D2 = 10.4157
L_2018A  = 14.027047499
L_2018B1 = 6.629673574
L_2018B2 = 0.430948924
L_2018C  = 6.891747024
L_2018D1 = 20.962647459
L_2018D2 = 10.868724698
lumi_periods_2018 = {}
lumi_periods_2018[ 'muon' ] = {}
lumi_periods_2018[ 'muon' ][ "2018A" ]  = L_2018A * 0.999913
lumi_periods_2018[ 'muon' ][ "2018B1" ] = L_2018B1 * 0.998672
lumi_periods_2018[ 'muon' ][ "2018B2" ] = L_2018B2 * 0.998672
lumi_periods_2018[ 'muon' ][ "2018C" ]  = L_2018C * 0.999991
lumi_periods_2018[ 'muon' ][ "2018D1" ] = L_2018D1 * 0.998915
lumi_periods_2018[ 'muon' ][ "2018D2" ] = L_2018D2 * 0.998915
lumi_periods_2018[ 'electron' ] = {}
lumi_periods_2018[ 'electron' ][ "2018A" ]  = L_2018A * 0.933083
lumi_periods_2018[ 'electron' ][ "2018B1" ] = L_2018B1 * 0.999977
lumi_periods_2018[ 'electron' ][ "2018B2" ] = L_2018B2 * 0.999977
lumi_periods_2018[ 'electron' ][ "2018C" ]  = L_2018C * 0.999978
lumi_periods_2018[ 'electron' ][ "2018D1" ] = L_2018D1 * 0.999389
lumi_periods_2018[ 'electron' ][ "2018D2" ] = L_2018D2 * 0.999389
print ( lumi_periods_2018 )
print ( "Luminosity 2018 muon: {}".format( np.sum( list( lumi_periods_2018[ 'muon' ].values() ) ) ) )
print ( "Luminosity 2018 electron: {}".format( np.sum( list( lumi_periods_2018[ 'electron' ].values() ) ) ) )

aperture_period_map = {
    "2016_preTS2"  : "2016_preTS2",
    "2016_postTS2" : "2016_postTS2",
    "2017B"        : "2017_preTS2",
    "2017C1"       : "2017_preTS2",
    "2017C2"       : "2017_preTS2",
    "2017D"        : "2017_preTS2",
    "2017E"        : "2017_postTS2",
    "2017F1"       : "2017_postTS2",
    "2017F2"       : "2017_postTS2",
    "2017F3"       : "2017_postTS2",
    "2018A"        : "2018",
    "2018B1"       : "2018",
    "2018B2"       : "2018",
    "2018C"        : "2018",
    "2018D1"       : "2018",
    "2018D2"       : "2018"
}
reco_period_map = {
    "2016_preTS2"  : "2016_preTS2",
    "2016_postTS2" : "2016_postTS2",
    "2017B"        : "2017_preTS2",
    "2017C1"       : "2017_preTS2",
    "2017C2"       : "2017_preTS2",
    "2017D"        : "2017_preTS2",
    "2017E"        : "2017_postTS2",
    "2017F1"       : "2017_postTS2",
    "2017F2"       : "2017_postTS2",
    "2017F3"       : "2017_postTS2",
    "2018A"        : "2018_preTS1",
    "2018B1"       : "2018_TS1_TS2",
    "2018B2"       : "2018_TS1_TS2",
    "2018C"        : "2018_TS1_TS2",
    "2018D1"       : "2018_postTS2",
    "2018D2"       : "2018_postTS2"
}

# Fiducial cuts (UL)
# Periods: "2017B", "2017C1", "2017E", "2017F1", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2"
def fiducial_cuts():
    # Per data period, arm=(0,1), station=(0,2)
    fiducialXLow_ = {}
    fiducialXHigh_ = {}
    fiducialYLow_ = {}
    fiducialYHigh_ = {}

    # data_periods = [ "2017B", "2017C1", "2017E", "2017F1", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]
    data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

    for period_ in data_periods:
        fiducialXLow_[ period_ ] = {}
        fiducialXLow_[ period_ ][ 0 ] = {}
        fiducialXLow_[ period_ ][ 1 ] = {}
        fiducialXHigh_[ period_ ] = {}
        fiducialXHigh_[ period_ ][ 0 ] = {}
        fiducialXHigh_[ period_ ][ 1 ] = {}
        fiducialYLow_[ period_ ] = {}
        fiducialYLow_[ period_ ][ 0 ] = {}
        fiducialYLow_[ period_ ][ 1 ] = {}
        fiducialYHigh_[ period_ ] = {}
        fiducialYHigh_[ period_ ][ 0 ] = {}
        fiducialYHigh_[ period_ ][ 1 ] = {}
        
    # 2017B
    # Sector 45, RP 220
    fiducialXLow_[ "2017B" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017B" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017B" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017B" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017B" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017B" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017B" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017B" ][ 1 ][ 2 ] =   4.698;

    # 2017C1
    # Sector 45, RP 220
    fiducialXLow_[ "2017C1" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017C1" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017C1" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017C1" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017C1" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017C1" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017C1" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017C1" ][ 1 ][ 2 ] =   4.698;

    # 2017C2
    # Sector 45, RP 220
    fiducialXLow_[ "2017C2" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017C2" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017C2" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017C2" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017C2" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017C2" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017C2" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017C2" ][ 1 ][ 2 ] =   4.698;

    # 2017D
    # Sector 45, RP 220
    fiducialXLow_[ "2017D" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017D" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017D" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017D" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017D" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017D" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017D" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017D" ][ 1 ][ 2 ] =   4.698;

    # 2017E
    # Sector 45, RP 220
    fiducialXLow_[ "2017E" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017E" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017E" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017E" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017E" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017E" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017E" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017E" ][ 1 ][ 2 ] =  5.398;

    # 2017F1
    # Sector 45, RP 220
    fiducialXLow_[ "2017F1" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F1" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F1" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F1" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F1" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F1" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F1" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F1" ][ 1 ][ 2 ] =  5.398;

    # 2017F2
    # Sector 45, RP 220
    fiducialXLow_[ "2017F2" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F2" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F2" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F2" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F2" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F2" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F2" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F2" ][ 1 ][ 2 ] =  5.398;

    # 2017F3
    # Sector 45, RP 220
    fiducialXLow_[ "2017F3" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F3" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F3" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F3" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F3" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F3" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F3" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F3" ][ 1 ][ 2 ] =  5.398;

    # 2018A
    # Sector 45, RP 210
    fiducialXLow_[ "2018A" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018A" ][ 0 ][ 0 ] =  17.927;
    fiducialYLow_[ "2018A" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018A" ][ 0 ][ 0 ] =   3.698;
    # Sector 45, RP 220
    fiducialXLow_[ "2018A" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018A" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018A" ][ 0 ][ 2 ]  = -10.898;
    fiducialYHigh_[ "2018A" ][ 0 ][ 2 ] =   4.398;
    # Sector 56, RP 210
    fiducialXLow_[ "2018A" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018A" ][ 1 ][ 0 ] =  18.498;
    fiducialYLow_[ "2018A" ][ 1 ][ 0 ]  = -11.298;
    fiducialYHigh_[ "2018A" ][ 1 ][ 0 ] =   3.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2018A" ][ 1 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018A" ][ 1 ][ 2 ] =  20.045;
    fiducialYLow_[ "2018A" ][ 1 ][ 2 ]  = -10.398;
    fiducialYHigh_[ "2018A" ][ 1 ][ 2 ] =   5.098;

    # 2018B1
    # Sector 45, RP 210
    fiducialXLow_[ "2018B1" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018B1" ][ 0 ][ 0 ] =  17.927;
    fiducialYLow_[ "2018B1" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018B1" ][ 0 ][ 0 ] =   3.698;
    # Sector 45, RP 220
    fiducialXLow_[ "2018B1" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018B1" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018B1" ][ 0 ][ 2 ]  = -10.898;
    fiducialYHigh_[ "2018B1" ][ 0 ][ 2 ] =   4.198;
    # Sector 56, RP 210
    fiducialXLow_[ "2018B1" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018B1" ][ 1 ][ 0 ] =  18.070;
    fiducialYLow_[ "2018B1" ][ 1 ][ 0 ]  = -11.198;
    fiducialYHigh_[ "2018B1" ][ 1 ][ 0 ] =   4.098;
    # Sector 56, RP 220
    fiducialXLow_[ "2018B1" ][ 1 ][ 2 ]  =   2.564;
    fiducialXHigh_[ "2018B1" ][ 1 ][ 2 ] =  20.045;
    fiducialYLow_[ "2018B1" ][ 1 ][ 2 ]  = -10.398;
    fiducialYHigh_[ "2018B1" ][ 1 ][ 2 ] =   5.098;

    # 2018B2
    # Sector 45, RP 210
    fiducialXLow_[ "2018B2" ][ 0 ][ 0 ]  =   2.564;
    fiducialXHigh_[ "2018B2" ][ 0 ][ 0 ] =  17.640;
    fiducialYLow_[ "2018B2" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018B2" ][ 0 ][ 0 ] =   4.198;
    # Sector 45, RP 220
    fiducialXLow_[ "2018B2" ][ 0 ][ 2 ]  =   2.140;
    fiducialXHigh_[ "2018B2" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2018B2" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018B2" ][ 0 ][ 2 ] =   3.798;
    # Sector 56, RP 210
    fiducialXLow_[ "2018B2" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018B2" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018B2" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018B2" ][ 1 ][ 0 ] =   4.098;
    # Sector 56, RP 220
    fiducialXLow_[ "2018B2" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018B2" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018B2" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018B2" ][ 1 ][ 2 ] =   4.498;

    # 2018C
    # Sector 45, RP 210
    fiducialXLow_[ "2018C" ][ 0 ][ 0 ]  =   2.564;
    fiducialXHigh_[ "2018C" ][ 0 ][ 0 ] =  17.930;
    fiducialYLow_[ "2018C" ][ 0 ][ 0 ]  = -11.098;
    fiducialYHigh_[ "2018C" ][ 0 ][ 0 ] =   4.198;
    # Sector 45, RP 220
    fiducialXLow_[ "2018C" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018C" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018C" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018C" ][ 0 ][ 2 ] =   3.698;
    # Sector 56, RP 210
    fiducialXLow_[ "2018C" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018C" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018C" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018C" ][ 1 ][ 0 ] =   4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018C" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018C" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018C" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018C" ][ 1 ][ 2 ] =   4.398;

    # 2018D1
    # Sector 45, RP 210
    fiducialXLow_[ "2018D1" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018D1" ][ 0 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D1" ][ 0 ][ 0 ]  = -11.098;
    fiducialYHigh_[ "2018D1" ][ 0 ][ 0 ] =   4.098;
    # Sector 45, RP 220
    fiducialXLow_[ "2018D1" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018D1" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018D1" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018D1" ][ 0 ][ 2 ] =   3.698;
    # Sector 56, RP 210
    fiducialXLow_[ "2018D1" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018D1" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D1" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018D1" ][ 1 ][ 0 ] =   4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018D1" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018D1" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018D1" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018D1" ][ 1 ][ 2 ] =   4.398;

    # 2018D2
    # Sector 45, RP 210
    fiducialXLow_[ "2018D2" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018D2" ][ 0 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D2" ][ 0 ][ 0 ]  = -10.598;
    fiducialYHigh_[ "2018D2" ][ 0 ][ 0 ] =   4.498;
    # Sector 45, RP 220
    fiducialXLow_[ "2018D2" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018D2" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018D2" ][ 0 ][ 2 ]  = -11.698;
    fiducialYHigh_[ "2018D2" ][ 0 ][ 2 ] =   3.298;
    # Sector 56, RP 210
    fiducialXLow_[ "2018D2" ][ 1 ][ 0 ]  =  3.275;
    fiducialXHigh_[ "2018D2" ][ 1 ][ 0 ] = 17.931;
    fiducialYLow_[ "2018D2" ][ 1 ][ 0 ]  = -9.998;
    fiducialYHigh_[ "2018D2" ][ 1 ][ 0 ] =  4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018D2" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018D2" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018D2" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018D2" ][ 1 ][ 2 ] =   3.898;
      
    return (  fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )


def fiducial_cuts_all( data_sample ):

    data_periods = None
    if data_sample == '2017':
        # data_periods = [ "2017B", "2017C1", "2017E", "2017F1" ]
        data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
    elif data_sample == '2018':
        data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

    fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ = fiducial_cuts()
    print ( fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )
    
    # Per data period, arm=(0,1), station=(0,2)
    fiducialXLow_all = {}
    fiducialXHigh_all = {}
    fiducialYLow_all = {}
    fiducialYHigh_all = {}
    for arm_ in (0,1):
        fiducialXLow_all[ arm_ ] = {}
        fiducialXLow_all[ arm_ ][ 2 ] = []
        fiducialXHigh_all[ arm_ ] = {}
        fiducialXHigh_all[ arm_ ][ 2 ] = []
        fiducialYLow_all[ arm_ ] = {}
        fiducialYLow_all[ arm_ ][ 2 ] = []
        fiducialYHigh_all[ arm_ ] = {}
        fiducialYHigh_all[ arm_ ][ 2 ] = []

    for period_ in data_periods:
        for arm_ in (0,1):
            fiducialXLow_all[ arm_ ][ 2 ].append( fiducialXLow_[ period_ ][ arm_][ 2 ] )
            fiducialXHigh_all[ arm_ ][ 2 ].append( fiducialXHigh_[ period_ ][ arm_][ 2 ] )
            fiducialYLow_all[ arm_ ][ 2 ].append( fiducialYLow_[ period_ ][ arm_][ 2 ] )
            fiducialYHigh_all[ arm_ ][ 2 ].append( fiducialYHigh_[ period_ ][ arm_][ 2 ] )

    for arm_ in (0,1):
        fiducialXLow_all[ arm_ ][ 2 ] = np.max( fiducialXLow_all[ arm_ ][ 2 ] )
        fiducialXHigh_all[ arm_ ][ 2 ] = np.min( fiducialXHigh_all[ arm_ ][ 2 ] )
        fiducialYLow_all[ arm_ ][ 2 ] = np.max( fiducialYLow_all[ arm_ ][ 2 ] )
        fiducialYHigh_all[ arm_ ][ 2 ] = np.min( fiducialYHigh_all[ arm_ ][ 2 ] )

    print ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )
    
    return ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )


# Per data period, arm=(0,1)
# Periods: "2016_preTS2", "2016_postTS2", "2017_preTS2", "2017_postTS2", "2018"
def aperture_parametrisation( period, arm, xangle, xi ):

    #https://github.com/cms-sw/cmssw/tree/916cb3d20213734a0465240720c8c8c392b92eac/Validation/CTPPS/python/simu_config

    if (period == "2016_preTS2"):
        if   (arm == 0): return 3.76296E-05+((xi<0.117122)*0.00712775+(xi>=0.117122)*0.0148651)*(xi-0.117122);
        elif (arm == 1): return 1.85954E-05+((xi<0.14324)*0.00475349+(xi>=0.14324)*0.00629514)*(xi-0.14324);
    elif (period == "2016_postTS2"):
        if   (arm == 0): return 6.10374E-05+((xi<0.113491)*0.00795942+(xi>=0.113491)*0.01935)*(xi-0.113491);
        elif (arm == 1): return (xi-0.110)/130.0;
    elif (period == "2017_preTS2"):
        if   (arm == 0): return -(8.71198E-07*xangle-0.000134726)+((xi<(0.000264704*xangle+0.081951))*-(4.32065E-05*xangle-0.0130746)+(xi>=(0.000264704*xangle+0.081951))*-(0.000183472*xangle-0.0395241))*(xi-(0.000264704*xangle+0.081951));
        elif (arm == 1): return 3.43116E-05+((xi<(0.000626936*xangle+0.061324))*0.00654394+(xi>=(0.000626936*xangle+0.061324))*-(0.000145164*xangle-0.0272919))*(xi-(0.000626936*xangle+0.061324));
    elif (period == "2017_postTS2"):
        if   (arm == 0): return -(8.92079E-07*xangle-0.000150214)+((xi<(0.000278622*xangle+0.0964383))*-(3.9541e-05*xangle-0.0115104)+(xi>=(0.000278622*xangle+0.0964383))*-(0.000108249*xangle-0.0249303))*(xi-(0.000278622*xangle+0.0964383));
        elif (arm == 1): return 4.56961E-05+((xi<(0.00075625*xangle+0.0643361))*-(3.01107e-05*xangle-0.00985126)+(xi>=(0.00075625*xangle+0.0643361))*-(8.95437e-05*xangle-0.0169474))*(xi-(0.00075625*xangle+0.0643361));
    elif (period == "2018"):
        if   (arm == 0): return -(8.44219E-07*xangle-0.000100957)+((xi<(0.000247185*xangle+0.101599))*-(1.40289E-05*xangle-0.00727237)+(xi>=(0.000247185*xangle+0.101599))*-(0.000107811*xangle-0.0261867))*(xi-(0.000247185*xangle+0.101599));
        elif (arm == 1): return -(-4.74758E-07*xangle+3.0881E-05)+((xi<(0.000727859*xangle+0.0722653))*-(2.43968E-05*xangle-0.0085461)+(xi>=(0.000727859*xangle+0.0722653))*-(7.19216E-05*xangle-0.0148267))*(xi-(0.000727859*xangle+0.0722653));
    else:
        return -999.

def check_aperture( period, arm, xangle, xi, theta_x ):
    return ( theta_x < -aperture_parametrisation( period, arm, xangle, xi ) )

def get_data( fileNames, runMin=None, runMax=None ):
    """
    fileNames dict:
        'multiRP': list of paths,
        'singleRP': list of paths,
        'ppstracks': list of paths,
        'event_counts': list of paths
   
    """
    if runMin is not None and runMin <= 0:
        raise RuntimeError( "Invalid data_sample argument." )
    if runMax is not None and runMax <= 0:
        raise RuntimeError( "Invalid data_sample argument." )

    runMin_ = runMin
    runMax_ = runMax

    # df_protons_multiRP_list = []
    # df_protons_singleRP_list = []
    # df_ppstracks_list = []
    # df_counts_list = []

    # for file_ in fileNames:
    #     print ( file_ )
    #     with h5py.File( file_, 'r' ) as f:
    #         print ( list(f.keys()) )

    #         dset_protons_multiRP = f['protons_multiRP']
    #         print ( dset_protons_multiRP.shape )
    #         print ( dset_protons_multiRP[:,:] )

    #         dset_protons_singleRP = f['protons_singleRP']
    #         print ( dset_protons_singleRP.shape )
    #         print ( dset_protons_singleRP[:,:] )

    #         dset_ppstracks = f['ppstracks']
    #         print ( dset_ppstracks.shape )
    #         print ( dset_ppstracks[:,:] )

    #         dset_columns_protons_multiRP = f['columns_protons_multiRP']
    #         print ( dset_columns_protons_multiRP.shape )
    #         columns_protons_multiRP = [ item.decode("utf-8") for item in list( dset_columns_protons_multiRP ) ]
    #         print ( columns_protons_multiRP )

    #         dset_columns_protons_singleRP = f['columns_protons_singleRP']
    #         print ( dset_columns_protons_singleRP.shape )
    #         columns_protons_singleRP = [ item.decode("utf-8") for item in list( dset_columns_protons_singleRP ) ]
    #         print ( columns_protons_singleRP )
    #         
    #         dset_columns_ppstracks = f['columns_ppstracks']
    #         print ( dset_columns_ppstracks.shape )
    #         columns_ppstracks = [ item.decode("utf-8") for item in list( dset_columns_ppstracks ) ]
    #         print ( columns_ppstracks )

    #         dset_selections = f['selections']
    #         selections_ = [ item.decode("utf-8") for item in dset_selections ]
    #         print ( selections_ )

    #         dset_counts = f['event_counts']
    #         df_counts_list.append( pd.Series( dset_counts, index=selections_ ) )
    #         print ( df_counts_list[-1] )

    #         chunk_size = 1000000
    #         entries_protons_multiRP = dset_protons_multiRP.shape[0]
    #         start_ = list( range( 0, entries_protons_multiRP, chunk_size ) )
    #         stop_ = start_[1:]
    #         stop_.append( entries_protons_multiRP )
    #         print ( start_ )
    #         print ( stop_ )
    #         astype_dict_protons_ = {
    #             "run": "int64", "lumiblock": "int64", "event": "int64", "slice": "int32",
    #             "ismultirp": "int32", "rpid": "int32", "arm": "int32", "random": "int32",
    #             "nVertices": "int32",
    #             "num_bjets_ak8": "int32", "num_bjets_ak4": "int32", "num_jets_ak4": "int32",
    #             "pfcand_nextracks": "int32", "pfcand_nextracks_noDRl": "int32",
    #             "trackpixshift1": "int32", "rpid1": "int32"
    #             }
    #         astype_dict_multiRP_ = astype_dict_protons_.copy()

    #         if "muon0_charge" in columns_protons_multiRP:
    #             astype_dict_multiRP_.update( { "muon0_charge": "int32" } )
 
    #         if "electron0_charge" in columns_protons_multiRP:
    #             astype_dict_multiRP_.update( { "electron0_charge": "int32" } )

    #         if "rpid2" in columns_protons_multiRP: 
    #             astype_dict_multiRP_.update( { "trackpixshift2": "int32", "rpid2": "int32" } )

    #         if "run_mc" in columns_protons_multiRP:
    #             astype_dict_multiRP_.update( { "run_mc": "int64" } )

    #         if "run_rnd" in columns_protons_multiRP: 
    #             # astype_dict_multiRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64", "slice_rnd": "int32" } )
    #             astype_dict_multiRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64" } )

    #         for idx in range( len( start_ ) ):
    #             print ( start_[idx], stop_[idx] )
    #             #print ( dset[ start_[idx] : stop_[idx] ] )
    #             df_ = pd.DataFrame( dset_protons_multiRP[ start_[idx] : stop_[idx] ], columns=columns_protons_multiRP ).astype( astype_dict_multiRP_ )

    #             if runMin_ is not None:
    #                 msk__ = ( df_.loc[ 'run' ] >= runMin_ )
    #                 print ( msk__ )
    #                 df_ = df_.loc[ msk__ ]
    #             if runMax_ is not None and df_.shape[0] > 0:
    #                 msk__ = ( df_.loc[ 'run' ] <= runMax_ )
    #                 print ( msk__ )
    #                 df_ = df_.loc[ msk__ ]

    #             if df_.shape[0] > 0:
    #                 df_protons_multiRP_list.append( df_ )
    #                 print ( df_protons_multiRP_list[-1].head() )
    #                 print ( "Data set size: {}".format( len( df_protons_multiRP_list[-1] ) ) )

    #         entries_protons_singleRP = dset_protons_singleRP.shape[0]
    #         start_ = list( range( 0, entries_protons_singleRP, chunk_size ) )
    #         stop_ = start_[1:]
    #         stop_.append( entries_protons_singleRP )
    #         print ( start_ )
    #         print ( stop_ )
    #         astype_dict_singleRP_ = astype_dict_protons_.copy()

    #         if "run_mc" in columns_protons_singleRP:
    #             astype_dict_singleRP_.update( { "run_mc": "int64" } )

    #         if "run_rnd" in columns_protons_singleRP: 
    #             # astype_dict_singleRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64", "slice_rnd": "int32" } )
    #             astype_dict_singleRP_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64" } )

    #         for idx in range( len( start_ ) ):
    #             print ( start_[idx], stop_[idx] )
    #             #print ( dset[ start_[idx] : stop_[idx] ] )
    #             df_ = pd.DataFrame( dset_protons_singleRP[ start_[idx] : stop_[idx] ], columns=columns_protons_singleRP ).astype( astype_dict_singleRP_ )

    #             if runMin_ is not None:
    #                 msk__ = ( df_.loc[ 'run' ] >= runMin_ )
    #                 print ( msk__ )
    #                 df_ = df_.loc[ msk__ ]
    #             if runMax_ is not None and df_.shape[0] > 0:
    #                 msk__ = ( df_.loc[ 'run' ] <= runMax_ )
    #                 print ( msk__ )
    #                 df_ = df_.loc[ msk__ ]

    #             if df_.shape[0] > 0:
    #                 df_protons_singleRP_list.append( df_ )
    #                 print ( df_protons_singleRP_list[-1].head() )
    #                 print ( "Data set size: {}".format( len( df_protons_singleRP_list[-1] ) ) )

    #         entries_ppstracks = dset_ppstracks.shape[0]
    #         start_ = list( range( 0, entries_ppstracks, chunk_size ) )
    #         stop_ = start_[1:]
    #         stop_.append( entries_ppstracks )
    #         print ( start_ )
    #         print ( stop_ )
    #         astype_dict_ppstracks_ = { "run": "int64", "lumiblock": "int64", "event": "int64", "slice": "int32", "rpid": "int32" }

    #         if "run_mc" in columns_ppstracks:
    #             astype_dict_ppstracks_.update( { "run_mc": "int64" } )

    #         if "run_rnd" in columns_ppstracks: 
    #             # astype_dict_ppstracks_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64", "slice_rnd": "int32" } )
    #             astype_dict_ppstracks_.update( { "run_rnd": "int64", "lumiblock_rnd": "int64", "event_rnd": "int64" } )

    #         for idx in range( len( start_ ) ):
    #             print ( start_[idx], stop_[idx] )
    #             #print ( dset[ start_[idx] : stop_[idx] ] )
    #             df_ = pd.DataFrame( dset_ppstracks[ start_[idx] : stop_[idx] ], columns=columns_ppstracks ).astype( astype_dict_ppstracks_ )

    #             if runMin_ is not None:
    #                 msk__ = ( df_.loc[ 'run' ] >= runMin_ )
    #                 print ( msk__ )
    #                 df_ = df_.loc[ msk__ ]
    #             if runMax_ is not None and df_.shape[0] > 0:
    #                 msk__ = ( df_.loc[ 'run' ] <= runMax_ )
    #                 print ( msk__ )
    #                 df_ = df_.loc[ msk__ ]

    #             if df_.shape[0] > 0:
    #                 df_ppstracks_list.append( df_ )
    #                 print ( df_ppstracks_list[-1].head() )
    #                 print ( "Data set size: {}".format( len( df_ppstracks_list[-1] ) ) )

    # df_counts = df_counts_list[0]
    # for idx in range( 1, len( df_counts_list ) ):
    #     df_counts = df_counts.add( df_counts_list[idx] )
    # print ( df_counts )

    # df_protons_multiRP = pd.concat( df_protons_multiRP_list )
    # print (df_protons_multiRP)

    # df_protons_singleRP = pd.concat( df_protons_singleRP_list )
    # print (df_protons_singleRP)

    # df_ppstracks = pd.concat( df_ppstracks_list )
    # print (df_ppstracks)

    fileNames_multiRP_      = fileNames[ 'protons_multiRP' ]
    fileNames_singleRP_     = fileNames[ 'protons_singleRP' ]
    fileNames_ppstracks_    = fileNames[ 'ppstracks' ]
    fileNames_counts_       = fileNames[ 'event_counts' ]
    if len( fileNames_multiRP_ ) == 1: fileNames_multiRP_ = fileNames_multiRP_[0]
    if len( fileNames_singleRP_ ) == 1: fileNames_singleRP_ = fileNames_singleRP_[0]
    if len( fileNames_ppstracks_ ) == 1: fileNames_ppstracks_ = fileNames_ppstracks_[0]
    if len( fileNames_counts_ ) == 1: fileNames_counts_ = fileNames_counts_[0]

    df_protons_multiRP_  = pd.read_parquet( fileNames_multiRP_ )
    df_protons_singleRP_ = pd.read_parquet( fileNames_singleRP_ )
    df_ppstracks_        = pd.read_parquet( fileNames_ppstracks_ )
    df_event_counts_     = pd.read_parquet( fileNames_counts_ )
    
    return ( df_event_counts_, df_protons_multiRP_, df_protons_singleRP_, df_ppstracks_ )

def process_data_protons_multiRP( lepton_type, data_sample, df_protons_multiRP, df_ppstracks=None, apply_fiducial=True, within_aperture=False, random_protons=False, mix_protons=False, calculate_vars_pp=True, select_2protons=True, runOnMC=False, use_hash_index=False, debug=False ):

    # if runOnMC and not mix_protons:
    #     print ( "Turning within_aperture OFF for MC." )
    #     within_aperture = False

    fiducialXLow_all = None
    fiducialXHigh_all = None
    fiducialYLow_all = None
    fiducialYHigh_all = None
    if apply_fiducial:
        # fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all = fiducial_cuts_all()
        fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all = fiducial_cuts_all( data_sample )
    
    df_ppstracks_index = None
#     if df_ppstracks is not None:
#         index_vars_ = None
#         if not use_hash_index:
#             index_vars_ = ['run', 'lumiblock', 'event', 'slice']
#         else:
#             from pandas.util import hash_array
#             arr_hash_id_ppstracks_x_ = hash_array( df_ppstracks.loc[ :, 'x' ].values  )
#             df_ppstracks.loc[ :, "hash_id" ] = arr_hash_id_ppstracks_x_
#             print ( df_ppstracks.loc[ :, "hash_id" ] )
#             index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
#         print ( index_vars_ )
#         # df_ppstracks_index = df_ppstracks.set_index( ['run', 'lumiblock', 'event', 'slice'] )
#         df_ppstracks_index = df_ppstracks.set_index( index_vars_ )
# #        
# #        df_protons_multiRP_index.loc[ :, "track_x1" ] = np.nan
# #        df_protons_multiRP_index.loc[ :, "track_x2" ] = np.nan
# #        df_protons_multiRP_index.loc[ :, "track_y1" ] = np.nan
# #        df_protons_multiRP_index.loc[ :, "track_y2" ] = np.nan
# #        
# #        df_protons_multiRP_index.loc[ :, "track_x1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 3 ]
# #        df_protons_multiRP_index.loc[ :, "track_x2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 23 ]
# #        df_protons_multiRP_index.loc[ :, "track_y1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 3 ]
# #        df_protons_multiRP_index.loc[ :, "track_y2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 0 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 23 ]
# #        df_protons_multiRP_index.loc[ :, "track_x1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 103 ]
# #        df_protons_multiRP_index.loc[ :, "track_x2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "x"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 123 ]
# #        df_protons_multiRP_index.loc[ :, "track_y1" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 103 ]
# #        df_protons_multiRP_index.loc[ :, "track_y2" ].loc[ df_protons_multiRP_index.loc[ :, "arm" ] == 1 ] = df_ppstracks_index.loc[:, "y"].loc[ df_ppstracks_index.loc[ :, "rpid" ] == 123 ]

    # run_str_ = "run_rnd" if ( random_protons or mix_protons ) else "run"
    run_str_ = "run"
    if random_protons or mix_protons:
        run_str_ = "run_rnd"
    elif runOnMC and not mix_protons:
        run_str_ = "run_mc"

    xangle_str_ = "crossingAngle"
    if random_protons or mix_protons:
        xangle_str_ = "crossingAngle_rnd"

    if "period" not in df_protons_multiRP.columns:
        df_protons_multiRP[ "period" ] = np.nan
        for idx_ in range( df_run_ranges.shape[0] ):
            msk_period_ = ( ( df_protons_multiRP[ run_str_ ] >= df_run_ranges.iloc[ idx_ ][ "min" ] ) & ( df_protons_multiRP[ run_str_ ] <= df_run_ranges.iloc[ idx_ ][ "max" ] ) )
            sum_period_ = np.sum( msk_period_.compute() )
            if sum_period_ > 0:
                period_key_ = df_run_ranges.index[ idx_ ]
                df_protons_multiRP[ "period" ] = df_protons_multiRP[ "period" ].mask( msk_period_, period_key_ )
                print ( "{}: {}".format( period_key_, sum_period_ ) )
        print ( df_protons_multiRP.loc[ :, "period" ] )

    if within_aperture:
        df_protons_multiRP[ "within_aperture" ] = df_protons_multiRP[ [ "period", xangle_str_, "arm", "xi", "thx" ] ].apply(
                lambda row: check_aperture( aperture_period_map[ row[ "period" ] ], row[ "arm" ], row[ xangle_str_ ], row[ "xi" ], row[ "thx" ] ),
                axis=1, meta=( 'within_aperture', 'bool' )
                )
        if debug:
            df_wa__ = df_protons_multiRP[ "within_aperture" ].compute()
            print ( df_wa__ )
            print ( "Within aperture: {}".format( np.sum( df_wa__ ) ) )
    
    index_vars_ = None
    if not use_hash_index:
        index_vars_ = ['run', 'lumiblock', 'event', 'slice']
    else:
        from pandas.util import hash_array
        arr_hash_id_protons_multiRP_jet0_pt_ = hash_array( df_protons_multiRP[ 'jet0_pt' ].compute()  )
        df_protons_multiRP[ "hash_id" ] = arr_hash_id_protons_multiRP_jet0_pt_
        print ( df_protons_multiRP[ "hash_id" ].compute() )
        index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
    print ( index_vars_ )

    # FIXME: Cannot use multi-index here
    # df_protons_multiRP_index = df_protons_multiRP.set_index( ['run', 'lumiblock', 'event', 'slice'] )
    # df_protons_multiRP_index = df_protons_multiRP.set_index( index_vars_ )
    df_protons_multiRP_index = df_protons_multiRP

    msk_multiRP = ( df_protons_multiRP_index[ "ismultirp" ] == 1 )
    df_protons_multiRP_index = df_protons_multiRP_index[ msk_multiRP ]

    msk1_arm = ( df_protons_multiRP_index[ "arm" ] == 0 )
    msk2_arm = ( df_protons_multiRP_index[ "arm" ] == 1 )

    msk_pixshift = ( ( df_protons_multiRP_index[ "trackpixshift1" ] == 0 ) &
                     ( df_protons_multiRP_index[ "trackpixshift2" ] == 0 ) )

    # track_angle_cut_ = 0.02
    msk_fid = None
    if apply_fiducial:
        df_protons_multiRP_index[ "xlow" ] = np.nan
        df_protons_multiRP_index[ "xhigh" ] = np.nan
        df_protons_multiRP_index[ "ylow" ] = np.nan
        df_protons_multiRP_index[ "yhigh" ] = np.nan
        df_protons_multiRP_index[ "xlow" ] = df_protons_multiRP_index[ "xlow" ].where( ~msk1_arm, fiducialXLow_all[ 0 ][ 2 ] )
        df_protons_multiRP_index[ "xhigh" ] = df_protons_multiRP_index[ "xhigh" ].where( ~msk1_arm, fiducialXHigh_all[ 0 ][ 2 ] )
        df_protons_multiRP_index[ "ylow" ] = df_protons_multiRP_index[ "ylow" ].where( ~msk1_arm, fiducialYLow_all[ 0 ][ 2 ] )
        df_protons_multiRP_index[ "yhigh"  ]= df_protons_multiRP_index[ "yhigh" ].where( ~msk1_arm, fiducialYHigh_all[ 0 ][ 2 ] )
        df_protons_multiRP_index[ "xlow" ] = df_protons_multiRP_index[ "xlow" ].where( ~msk2_arm, fiducialXLow_all[ 1 ][ 2 ] )
        df_protons_multiRP_index[ "xhigh" ] = df_protons_multiRP_index[ "xhigh" ].where( ~msk2_arm, fiducialXHigh_all[ 1 ][ 2 ] )
        df_protons_multiRP_index[ "ylow" ] = df_protons_multiRP_index[ "ylow" ].where( ~msk2_arm, fiducialYLow_all[ 1 ][ 2 ] )
        df_protons_multiRP_index[ "yhigh" ] = df_protons_multiRP_index[ "yhigh" ].where( ~msk2_arm, fiducialYHigh_all[ 1 ][ 2 ] )

#        msk_fid = ( ( np.abs(df_protons_multiRP_index[""]) <= track_angle_cut_ ) &
#                    ( np.abs(df_protons_multiRP_index[""]) <= track_angle_cut_ ) )

        msk_fid = ( ( df_protons_multiRP_index[ "trackx2"] >= df_protons_multiRP_index[ "xlow" ] ) &
                    ( df_protons_multiRP_index[ "trackx2"] <= df_protons_multiRP_index[ "xhigh" ] ) &
                    ( df_protons_multiRP_index[ "tracky2"] >= df_protons_multiRP_index[ "ylow" ] ) &
                    ( df_protons_multiRP_index[ "tracky2"] <= df_protons_multiRP_index[ "yhigh" ] ) )

    msk_aperture = None
    if within_aperture:
        msk_aperture = df_protons_multiRP_index[ "within_aperture" ]

    msk1 = msk1_arm & msk_pixshift
    msk2 = msk2_arm & msk_pixshift
    if msk_fid is not None:
        msk1 = msk1 & msk_fid
        msk2 = msk2 & msk_fid
    if msk_aperture is not None:
        msk1 = msk1 & msk_aperture
        msk2 = msk2 & msk_aperture

    df_protons_multiRP_index = df_protons_multiRP_index[ msk1 | msk2 ]

    # df_protons_multiRP_groupby = df_protons_multiRP_index[ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
    # msk_2protons = df_protons_multiRP_groupby[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) >= 1 ) & ( np.sum( s_ == 1 ) >= 1 ) )
    # df_protons_multiRP_index = df_protons_multiRP_index.loc[ msk_2protons ]

    columns_eff_ = []

    if runOnMC and not mix_protons:
        if data_sample == '2017': 
            # efficiencies_2017
            from proton_efficiency import efficiencies_2017, strict_zero_efficiencies, proton_efficiency_uncertainty
            strips_multitrack_efficiency, strips_sensor_efficiency, multiRP_efficiency, file_eff_strips, file_eff_multiRP = efficiencies_2017()
            sz_efficiencies = strict_zero_efficiencies()

            data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]

            lumi_periods_ = None
            if lepton_type == 'muon':
                lumi_periods_ = lumi_periods_2017[ 'muon' ]
            elif lepton_type == 'electron':
                lumi_periods_ = lumi_periods_2017[ 'electron' ]

            proton_eff_unc_per_arm_ = proton_efficiency_uncertainty[ "2017" ]

            df_protons_multiRP_index.loc[ :, 'eff_proton_all_weighted' ] = 0.
            # df_protons_multiRP_index.loc[ :, 'eff_all_weighted' ] = 0.
            df_protons_multiRP_index.loc[ :, 'eff_multitrack_weighted' ] = 0.
            df_protons_multiRP_index.loc[ :, 'eff_strictzero_weighted' ] = 0.
            for period_ in data_periods:
                f_eff_strips_multitrack_ = lambda row: strips_multitrack_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent( 1 )
    
                f_eff_strips_sensor_     = lambda row: strips_sensor_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                strips_sensor_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx2"], row["tracky2"] )
                                                )
    
                f_eff_multiRP_           = lambda row: multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                                )
    
                f_eff_strips_strictzero_ = lambda row: sz_efficiencies[ period_ ][ "45" if row["arm"] == 0 else "56" ][ int( ( row["crossingAngle"] // 10 ) * 10 ) ]

                f_eff_proton_all_        = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row)

                # f_eff_all_               = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row) * f_eff_strips_multitrack_(row)

                df_protons_multiRP_index[ 'eff_proton_all_' + period_ ] = df_protons_multiRP_index[ ["arm", "trackx1", "tracky1", "trackx2", "tracky2"] ].apply( f_eff_proton_all_, axis=1 )
                df_protons_multiRP_index[ 'eff_proton_all_weighted' ]   = df_protons_multiRP_index[ 'eff_proton_all_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index[ 'eff_proton_all_' + period_ ]
                # df_protons_multiRP_index[ 'eff_all_' + period_ ]      = df_protons_multiRP_index[ ["arm", "trackx1", "tracky1", "trackx2", "tracky2"] ].apply( f_eff_all_, axis=1 )
                # df_protons_multiRP_index[ 'eff_all_weighted' ]        = df_protons_multiRP_index[ 'eff_all_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index[ 'eff_all_' + period_ ]
                df_protons_multiRP_index[ 'eff_multitrack_' + period_ ] = df_protons_multiRP_index[ [ "arm" ] ].apply( f_eff_strips_multitrack_, axis=1 )
                df_protons_multiRP_index[ 'eff_multitrack_weighted' ]   = df_protons_multiRP_index[ 'eff_multitrack_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index[ 'eff_multitrack_' + period_ ]
                df_protons_multiRP_index[ 'eff_strictzero_' + period_ ] = df_protons_multiRP_index[ [ "arm", "crossingAngle" ] ].apply( f_eff_strips_strictzero_, axis=1 )
                df_protons_multiRP_index[ 'eff_strictzero_weighted' ]   = df_protons_multiRP_index[ 'eff_strictzero_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index[ 'eff_strictzero_' + period_ ]
                columns_eff_.append( 'eff_proton_all_' + period_ )        
                # columns_eff_.append( 'eff_all_' + period_ )        
                columns_eff_.append( 'eff_multitrack_' + period_ )        
                columns_eff_.append( 'eff_strictzero_' + period_ )        
            columns_eff_.append( 'eff_proton_all_weighted' ) 
            # columns_eff_.append( 'eff_all_weighted' ) 
            columns_eff_.append( 'eff_multitrack_weighted' ) 
            columns_eff_.append( 'eff_strictzero_weighted' )

            lumi_ = np.sum( list( lumi_periods_.values() ) )
            df_protons_multiRP_index[ 'eff_proton_all_weighted' ] = df_protons_multiRP_index[ 'eff_proton_all_weighted' ] / lumi_
            # df_protons_multiRP_index[ 'eff_all_weighted' ] = df_protons_multiRP_index[ 'eff_all_weighted' ] / lumi_
            df_protons_multiRP_index[ 'eff_multitrack_weighted' ] = df_protons_multiRP_index[ 'eff_multitrack_weighted' ] / lumi_
            df_protons_multiRP_index[ 'eff_strictzero_weighted' ] = df_protons_multiRP_index[ 'eff_strictzero_weighted' ] / lumi_

            f_eff_strips_multitrack_ = lambda row: strips_multitrack_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent( 1 )
    
            f_eff_strips_sensor_     = lambda row: strips_sensor_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            strips_sensor_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx2"], row["tracky2"] )
                                            )
    
            f_eff_multiRP_           = lambda row: multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                            )
    
            f_eff_strips_strictzero_ = lambda row: sz_efficiencies[ row["period"] ][ "45" if row["arm"] == 0 else "56" ][ int( ( row["crossingAngle"] // 10 ) * 10 ) ]

            f_eff_proton_all_        = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row)
            df_protons_multiRP_index[ 'eff_proton_all' ] = df_protons_multiRP_index[ [ "period", "arm", "trackx1", "tracky1", "trackx2", "tracky2" ] ].apply( f_eff_proton_all_, axis=1 )
            df_protons_multiRP_index[ 'eff_multitrack' ] = df_protons_multiRP_index[ [ "period", "arm" ] ].apply( f_eff_strips_multitrack_, axis=1 )
            df_protons_multiRP_index[ 'eff_strictzero' ] = df_protons_multiRP_index[ [ "period", "arm", "crossingAngle" ] ].apply( f_eff_strips_strictzero_, axis=1 )
            columns_eff_.append( 'eff_proton_all' ) 
            columns_eff_.append( 'eff_multitrack' ) 
            columns_eff_.append( 'eff_strictzero' )

            f_eff_proton_unc_ = lambda row: proton_eff_unc_per_arm_[ "45" if row["arm"] == 0 else "56" ]
            df_protons_multiRP_index[ 'eff_proton_unc' ] = df_protons_multiRP_index[ [ "arm" ] ].apply( f_eff_proton_unc_, axis=1 )
            columns_eff_.append( 'eff_proton_unc' ) 
        elif data_sample == '2018': 
            # efficiencies_2018
            from proton_efficiency import efficiencies_2018, proton_efficiency_uncertainty
            sensor_near_efficiency, multiRP_efficiency, file_eff_rad_near, file_eff_multiRP = efficiencies_2018()

            data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

            lumi_periods_ = None
            if lepton_type == 'muon':
                lumi_periods_ = lumi_periods_2018[ 'muon' ]
            elif lepton_type == 'electron':
                lumi_periods_ = lumi_periods_2018[ 'electron' ]

            proton_eff_unc_per_arm_ = proton_efficiency_uncertainty[ "2018" ]

            df_protons_multiRP_index[ 'eff_proton_all_weighted' ] = 0.
            for period_ in data_periods:
                f_eff_sensor_near_       = lambda row: sensor_near_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                sensor_near_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                                )
    
                f_eff_multiRP_           = lambda row: multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                                multiRP_efficiency[ period_ ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                                )

                f_eff_proton_all_        = lambda row: f_eff_sensor_near_(row) * f_eff_multiRP_(row)

                df_protons_multiRP_index[ 'eff_proton_all_' + period_ ] = df_protons_multiRP_index[ ["arm", "trackx1", "tracky1"] ].apply( f_eff_proton_all_, axis=1 )
                df_protons_multiRP_index[ 'eff_proton_all_weighted' ] = df_protons_multiRP_index[ 'eff_proton_all_weighted' ] + lumi_periods_[ period_ ] * df_protons_multiRP_index[ 'eff_proton_all_' + period_ ]
                columns_eff_.append( 'eff_proton_all_' + period_ )        
            columns_eff_.append( 'eff_proton_all_weighted' ) 

            lumi_ = np.sum( list( lumi_periods_.values() ) )
            df_protons_multiRP_index[ 'eff_proton_all_weighted' ] = df_protons_multiRP_index[ 'eff_proton_all_weighted' ] / lumi_

            f_eff_sensor_near_       = lambda row: sensor_near_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            sensor_near_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                            )
    
            f_eff_multiRP_           = lambda row: multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].GetBinContent(
                                            multiRP_efficiency[ row["period"] ][ "45" if row["arm"] == 0 else "56" ].FindBin( row["trackx1"], row["tracky1"] )
                                            )
    
            f_eff_proton_all_        = lambda row: f_eff_sensor_near_(row) * f_eff_multiRP_(row)
            df_protons_multiRP_index[ 'eff_proton_all' ] = df_protons_multiRP_index[ [ "period", "arm", "trackx1", "tracky1" ] ].apply( f_eff_proton_all_, axis=1 )
            columns_eff_.append( 'eff_proton_all' ) 

            f_eff_proton_unc_ = lambda row: proton_eff_unc_per_arm_[ "45" if row["arm"] == 0 else "56" ]
            df_protons_multiRP_index[ 'eff_proton_unc' ] = df_protons_multiRP_index[ [ "arm" ] ].apply( f_eff_proton_unc_, axis=1 )
            columns_eff_.append( 'eff_proton_unc' ) 

    if runOnMC and mix_protons:
        df_protons_multiRP_index[ "eff_proton_all" ] = 1.0
        df_protons_multiRP_index[ "eff_proton_all_weighted" ] = 1.0
        df_protons_multiRP_index[ "eff_proton_unc" ] = 0.0
        if data_sample == '2017':
            df_protons_multiRP_index[ "eff_multitrack" ] = 1.0
            df_protons_multiRP_index[ "eff_strictzero" ] = 1.0
            df_protons_multiRP_index[ "eff_multitrack_weighted" ] = 1.0
            df_protons_multiRP_index[ "eff_strictzero_weighted" ] = 1.0

    columns_drop_ = [ "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
                      "trackx1", "tracky1", "trackpixshift1", "rpid1",
                      "trackx2", "tracky2", "trackpixshift2", "rpid2" ]
    if runOnMC:
        columns_drop_.extend( columns_eff_ )
    print ( columns_drop_ )

    if calculate_vars_pp:
        # df_protons_multiRP_events, df_protons_multiRP_index_2protons = process_events( data_sample, df_protons_multiRP_index, runOnMC=runOnMC, mix_protons=mix_protons, columns_drop=columns_drop_ )
        df_protons_multiRP_events, df_protons_multiRP_index_2protons = process_events( data_sample, df_protons_multiRP_index, runOnMC=runOnMC, mix_protons=mix_protons, columns_drop=columns_drop_, use_hash_index=use_hash_index, debug=debug )
        if select_2protons:
            df_protons_multiRP_index = df_protons_multiRP_index_2protons
    else:
        labels_xi_ = [ "_nom", "_p100", "_m100" ]
        if runOnMC:
            columns_drop_.extend( [ "xi" + label_ for label_ in labels_xi_ ] )
        df_protons_multiRP_events = df_protons_multiRP_index.drop( columns=columns_drop_ )
        df_protons_multiRP_events = df_protons_multiRP_events[ ~df_protons_multiRP_events.index.duplicated(keep='first') ]
        print ( "Number of events: {}".format( df_protons_multiRP_events.shape[0] ) )

    if debug:
        print ( df_protons_multiRP_index )

    return (df_protons_multiRP_index, df_protons_multiRP_events, df_ppstracks_index)

def process_events( data_sample, df_protons_multiRP_index, runOnMC=False, mix_protons=False, columns_drop=None, use_hash_index=False, debug=False ):

    index_vars_ = None
    if not use_hash_index:
        index_vars_ = ['run', 'lumiblock', 'event', 'slice']
    else:
        index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
    print ( index_vars_ )

    # Keep protons with the max xi per event and arm

    groupby_vars_ = index_vars_.copy()
    # groupby_vars_.append( 'arm' )
    # df_protons_multiRP_groupby_byarm_xi_max = df_protons_multiRP_index[ [ "arm", "xi" ] ].groupby( groupby_vars_ )

    groupby_vars_.append( 'arm' )
    vars__ = groupby_vars_.copy()
    vars__.extend( [ "xi" ] )
    print ( df_protons_multiRP_index.columns )
    if debug:
        print ( groupby_vars_ )
        print ( vars__ )
        print ( df_protons_multiRP_index[ vars__ ].compute() )

    # Calculate mask in pandas
    df__ = df_protons_multiRP_index[ vars__ ].compute()
    df_protons_multiRP_groupby_byarm_xi_max = df__.groupby( groupby_vars_ )
    msk_xi_max = df_protons_multiRP_groupby_byarm_xi_max[ "xi" ].transform( lambda s_: ( s_ == s_.max() ) )
    # msk_xi_max = df_protons_multiRP_groupby_byarm_xi_max[ "xi" ].transform( lambda s_: ( s_ == s_.max() ), meta=( 'xi', 'bool' ) )
    print ( msk_xi_max )
    df_protons_multiRP_index[ 'msk_ximax' ] = msk_xi_max
    if debug:
        print ( df_protons_multiRP_index[ 'msk_ximax' ].compute() )
    df_protons_multiRP_index_xi_max = df_protons_multiRP_index[ df_protons_multiRP_index[ 'msk_ximax' ] == True ]
    if debug:
        print ( df_protons_multiRP_index_xi_max[ vars__ ].compute() )

    # Keep events with at least one proton per arm

    groupby_vars_ = index_vars_.copy()
    vars__ = groupby_vars_.copy()
    vars__.extend( [ "arm" ] )
    if debug:
        print ( groupby_vars_ )
        print ( vars__ )

    # Calculate mask in pandas
    df__ = df_protons_multiRP_index_xi_max[ vars__ ].compute()
    # df_protons_multiRP_groupby_arm = df_protons_multiRP_index_xi_max[ [ "arm" ] ].groupby( index_vars_ )
    # df_protons_multiRP_groupby_arm = df_protons_multiRP_index_xi_max[ vars__  ].groupby( groupby_vars_ )
    df_protons_multiRP_groupby_arm = df__.groupby( groupby_vars_ )
    msk_2protons = df_protons_multiRP_groupby_arm[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ) )
    # msk_2protons = df_protons_multiRP_groupby_arm[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ), meta=( 'arm', 'bool' ) )
    print ( msk_2protons )
    print ( msk_2protons.sum() )
    df_protons_multiRP_index_xi_max[ 'msk_2protons' ] = msk_2protons
    if debug:
        print ( df_protons_multiRP_index_xi_max[ 'msk_2protons' ].compute() )
    df_protons_multiRP_index_2protons = df_protons_multiRP_index_xi_max[ df_protons_multiRP_index_xi_max[ 'msk_2protons' ] == True ]

    # Compute the dataframe before next groupby
    # res_ = df_protons_multiRP_index_2protons.compute()
    # if debug:
    #     print ( res_ )
    # df_protons_multiRP_index_2protons = dd.from_pandas( res_ )

    # Event table from protons

    var_list_ = None
    if data_sample == '2017':
        # var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_multitrack_weighted", "eff_strictzero_weighted", "eff_proton_all", "eff_multitrack", "eff_strictzero", "eff_proton_unc" ] if ( runOnMC and not mix_protons ) else [ "arm", "xi" ]
        # var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_multitrack_weighted", "eff_strictzero_weighted", "eff_proton_all", "eff_multitrack", "eff_strictzero", "eff_proton_unc" ]
        var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_multitrack_weighted", "eff_strictzero_weighted", "eff_proton_all", "eff_multitrack", "eff_strictzero", "eff_proton_unc" ] if ( runOnMC ) else [ "arm", "xi" ]
    elif data_sample == '2018':
        # var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_proton_all", "eff_proton_unc" ] if ( runOnMC and not mix_protons ) else [ "arm", "xi" ]
        # var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_proton_all", "eff_proton_unc" ]
        var_list_ = [ "arm", "xi", "eff_proton_all_weighted", "eff_proton_all", "eff_proton_unc" ] if ( runOnMC ) else [ "arm", "xi" ]

    # labels_xi_ = [ "_nom", "_p10", "_p30", "_p60", "_p100", "_m10", "_m30", "_m60", "_m100" ]
    labels_xi_ = [ "_nom", "_p100", "_m100" ]
    if runOnMC:
        var_list_.extend( [ "xi" + label_ for label_ in labels_xi_ ] )
    print ( var_list_ )

    groupby_vars_ = index_vars_.copy()
    vars__ = index_vars_.copy()
    vars__.extend( var_list_ )
    if debug:
        print ( groupby_vars_ )
        print ( vars__ )

    # df_protons_multiRP_2protons_groupby = df_protons_multiRP_index_2protons[ var_list_ ].groupby( index_vars_ )
    df_protons_multiRP_2protons_groupby = df_protons_multiRP_index_2protons[ vars__ ].groupby( groupby_vars_ )

    if runOnMC:
        columns_drop.extend( [ "xi" + label_ for label_ in labels_xi_ ] )
    
    # df_protons_multiRP_events = df_protons_multiRP_events[ ~df_protons_multiRP_events.index.duplicated(keep='first') ]
    df_protons_multiRP_events = df_protons_multiRP_index_2protons[ df_protons_multiRP_index_2protons[ "arm" ] == 0 ]
    df_protons_multiRP_events = df_protons_multiRP_events.drop( columns=columns_drop )
    df_protons_multiRP_events[ "original_index" ] = df_protons_multiRP_events.index
    df_protons_multiRP_events = df_protons_multiRP_events.reset_index()
    print ( "Number of events: {}".format( df_protons_multiRP_events[ 'event' ].compute().shape[0] ) )

    # df_protons_multiRP_index_2protons[ "MX" ] = df_protons_multiRP_2protons_groupby[ "xi" ].apply(
    #     lambda s_: 13000. * np.sqrt( s_.iloc[0] * s_.iloc[1] ),
    #     meta=( 'MX', 'float64' )
    #     )
    # vars__.extend( [ "MX" ] )
    # print ( df_protons_multiRP_index_2protons[ vars__ ].compute() )
    # 
    # df_protons_multiRP_events.loc[ :, "YX" ] = df_protons_multiRP_2protons_groupby[ ["arm", "xi"] ].apply(
    #     lambda df__: 0.5 * np.log( df__[ "xi" ][ df__[ "arm" ] == 0 ].iloc[0] / df__[ "xi" ][ df__[ "arm" ] == 1 ].iloc[0] )
    #     )
    # print ( df_protons_multiRP_events.loc[ :, "YX" ] )

    def get_MX_YX( df, xi_label="xi" ):
        # print ( df )
        xi1_ = df[ xi_label ][ df[ "arm" ] == 0 ].iloc[0]
        xi2_ = df[ xi_label ][ df[ "arm" ] == 1 ].iloc[0]
        MX_ = 13000. * np.sqrt( xi1_ * xi2_ )
        YX_ = 0.5 * np.log( xi1_ / xi2_ )
        return pd.Series( { 'MX': MX_, 'YX': YX_ } )
        
    res_ = df_protons_multiRP_2protons_groupby[ ["arm", "xi"] ].apply(
        get_MX_YX, xi_label="xi", meta={ 'MX': 'float64', 'YX': 'float64' }
        )
    res_ = res_.reset_index()
    if debug:
        print ( res_ )
        print ( res_.compute() )

    # def repeat_rows( df ):
    #     df_ = df.loc[ df.index.repeat(2) ]
    #     # print ( df_ )
    #     # print ( df_.reset_index() )
    #     return df_.reset_index()
    # res_repeat_ = res_.map_partitions(
    #     # lambda df: df.loc[ df.index.repeat(2) ]
    #     repeat_rows,
    #     meta={ 'MX': 'float64', 'YX': 'float64' }
    # )
    # res_ = res_repeat_
    # print ( res_ )
    # print ( res_.compute() )
    # df_protons_multiRP_index_2protons[ "MX" ] = res_[ 'MX' ]
    # df_protons_multiRP_index_2protons[ "YX" ] = res_[ 'YX' ]
    # print ( df_protons_multiRP_index_2protons[ [ "MX", "YX" ] ].compute() )
    
    df_protons_multiRP_events[ "MX" ] = res_[ 'MX' ]
    df_protons_multiRP_events[ "YX" ] = res_[ 'YX' ]
    if debug:
        print ( df_protons_multiRP_events[ [ "MX", "YX" ] ].compute() )

    df_protons_multiRP_events[ "diffMWW_MX" ]  = df_protons_multiRP_events[ "recoMWW" ] - df_protons_multiRP_events[ "MX" ]
    df_protons_multiRP_events[ "ratioMWW_MX" ] = df_protons_multiRP_events[ "recoMWW" ] / df_protons_multiRP_events[ "MX" ]
    df_protons_multiRP_events[ "shiftedRatioMWW_MX" ] = df_protons_multiRP_events[ "ratioMWW_MX" ] - 1.
    df_protons_multiRP_events[ "diffYWW_YX" ]  = df_protons_multiRP_events[ "recoRapidityWW" ] - df_protons_multiRP_events[ "YX" ]
    df_protons_multiRP_events[ "MX" + "_nom" ] = df_protons_multiRP_events[ "MX" ]
    df_protons_multiRP_events[ "YX" + "_nom" ] = df_protons_multiRP_events[ "YX" ]
    df_protons_multiRP_events[ "R_MWW_MX" + "_nom" ] = ( df_protons_multiRP_events[ "MWW" + "_nom" ] / df_protons_multiRP_events[ "MX" + "_nom" ] )
    df_protons_multiRP_events[ "Diff_YWW_YX" + "_nom" ] = ( df_protons_multiRP_events[ "YWW" + "_nom" ] - df_protons_multiRP_events[ "YX" + "_nom" ] )

    if runOnMC:
        # for label_ in [ "_jes_up", "_jes_dw" ]:
        for label_ in [ "_jes_up", "_jes_dw", "_jer_up", "_jer_dw" ]:
            df_protons_multiRP_events[ "R_MWW_MX" + label_ ] = ( df_protons_multiRP_events[ "MWW" + label_ ] / df_protons_multiRP_events[ "MX" + "_nom" ] ) 
            df_protons_multiRP_events[ "Diff_YWW_YX" + label_ ] = ( df_protons_multiRP_events[ "YWW" + label_ ] - df_protons_multiRP_events[ "YX" + "_nom" ] )

        for label0_ in labels_xi_:
            for label1_ in labels_xi_:
                # FIXME
                vars__ = [ "arm", "xi" + label0_ ] if label0_ == label1_  else [ "arm", "xi" + label0_, "xi" + label1_ ]
                print ( "MX" + label0_ + label1_ )
                df_protons_multiRP_2protons_groupby_apply_MX_ = df_protons_multiRP_2protons_groupby[ vars__ ].apply(
                    lambda df__: 13000. * np.sqrt( df__[ "xi" + label0_ ][ df__[ "arm" ] == 0 ].iloc[0] * df__[ "xi" + label1_ ][ df__[ "arm" ] == 1 ].iloc[0] )
                    )
                df_protons_multiRP_events[ "MX" + label0_ + label1_ ] = df_protons_multiRP_2protons_groupby_apply_MX_
                # print ( df_protons_multiRP_events[ "MX" + label0_ + label1_ ] )
                print ( "YX" + label0_ + label1_ )
                df_protons_multiRP_2protons_groupby_apply_YX_ = df_protons_multiRP_2protons_groupby[ vars__ ].apply(
                    lambda df__: 0.5 * np.log( df__[ "xi" + label0_ ][ df__[ "arm" ] == 0 ].iloc[0] / df__[ "xi" + label1_ ][ df__[ "arm" ] == 1 ].iloc[0] )
                    )
                df_protons_multiRP_events[ "YX" + label0_ + label1_ ] = df_protons_multiRP_2protons_groupby_apply_YX_
                # print ( df_protons_multiRP_events[ "YX" + label0_ + label1_ ] )

                print ( "R_MWW_MX" + label0_ + label1_ )
                df_protons_multiRP_events[ "R_MWW_MX" + label0_ + label1_ ] = ( df_protons_multiRP_events[ "MWW" + "_nom" ] / df_protons_multiRP_events[ "MX" + label0_ + label1_ ] )
                # print ( df_protons_multiRP_events[ "R_MWW_MX" + label0_ + label1_ ] )
                print ( "Diff_YWW_YX" + label0_ + label1_ )
                df_protons_multiRP_events[ "Diff_YWW_YX" + label0_ + label1_ ] = ( df_protons_multiRP_events[ "YWW" + "_nom" ] - df_protons_multiRP_events[ "YX" + label0_ + label1_ ] )
                # print ( df_protons_multiRP_events[ "Diff_YWW_YX" + label0_ + label1_ ] )

    # if runOnMC and not mix_protons:
    if runOnMC:
        # FIXME
        df_protons_multiRP_events[ "eff_proton_all_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_all_weighted" ].agg(
            lambda s_: ( s_.iloc[0] * s_.iloc[1] )
            )
        print ( df_protons_multiRP_events[ "eff_proton_all_weighted" ] )
        # df_protons_multiRP_events[ "eff_all_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_all_weighted" ].agg(
        #     lambda s_: ( s_.iloc[0] * s_.iloc[1] )
        #     )
        # print ( df_protons_multiRP_events[ "eff_all_weighted" ] )
        if data_sample == '2017':
            df_protons_multiRP_events[ "eff_multitrack_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_multitrack_weighted" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events[ "eff_multitrack_weighted" ] )
            df_protons_multiRP_events[ "eff_strictzero_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_strictzero_weighted" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events[ "eff_strictzero_weighted" ] )

        df_protons_multiRP_events[ "eff_proton_all" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_all" ].agg(
            lambda s_: ( s_.iloc[0] * s_.iloc[1] )
            )
        print ( df_protons_multiRP_events[ "eff_proton_all" ] )
        if data_sample == '2017':
            df_protons_multiRP_events[ "eff_multitrack" ] = df_protons_multiRP_2protons_groupby[ "eff_multitrack" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events[ "eff_multitrack" ] )
            df_protons_multiRP_events[ "eff_strictzero" ] = df_protons_multiRP_2protons_groupby[ "eff_strictzero" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events[ "eff_strictzero" ] )

        df_protons_multiRP_events[ "eff_proton_unc" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_unc" ].agg(
            lambda s_: np.sqrt( s_.iloc[0] ** 2 + s_.iloc[1] ** 2 )
            )
        print ( df_protons_multiRP_events[ "eff_proton_unc" ] )
        df_protons_multiRP_events[ "eff_proton_var_up" ] = ( 1. + df_protons_multiRP_events[ "eff_proton_unc" ] )
        df_protons_multiRP_events[ "eff_proton_var_dw" ] = ( 1. - df_protons_multiRP_events[ "eff_proton_unc" ] )
        print ( df_protons_multiRP_events[ "eff_proton_var_up" ] )
        print ( df_protons_multiRP_events[ "eff_proton_var_dw" ] )

    return ( df_protons_multiRP_events, df_protons_multiRP_index_2protons )


def process_signal_plus_mix_events( data_sample, labels_signals, labels_signals_mix_protons, label_signal_to_mix_protons, base_path='output', output_dir='output', use_hash_index=True ):

    base_path_ = base_path
    output_dir_ = output_dir

    df_counts_signals = {}
    df_signals_protons_multiRP_index = {}
    df_signals_protons_multiRP_events = {}
    for label_ in labels_signals:
        print ( label_ )
        file_path_ = "{}/data-store-{}.h5".format( base_path_, label_ )
        print ( file_path_ )
        with pd.HDFStore( file_path_, 'r' ) as store_:
            print ( list( store_ ) )
            df_counts_signals[ label_ ] = store_[ "counts" ]
            df_signals_protons_multiRP_index[ label_ ] = store_[ "protons_multiRP" ]
            df_signals_protons_multiRP_events[ label_ ] = store_[ "events_multiRP" ]
    
    df_counts_signals_mix_protons = {}
    df_signals_protons_multiRP_mix_protons_index = {}
    df_signals_protons_multiRP_mix_protons_events = {}
    for label_ in labels_signals_mix_protons:
        print ( label_ )
        file_path_ = "{}/data-store-{}.h5".format( base_path_, label_ )
        print ( file_path_ )
        with pd.HDFStore( file_path_, 'r' ) as store_:
            print ( list( store_ ) )
            df_counts_signals_mix_protons[ label_ ] = store_[ "counts" ]
            df_signals_protons_multiRP_mix_protons_index[ label_ ] = store_[ "protons_multiRP" ]
            df_signals_protons_multiRP_mix_protons_events[ label_ ] = store_[ "events_multiRP" ]
    
    # Signal with event mixing
    
    df_signals_protons_multiRP_eff_sel_index = {}
    df_signals_protons_multiRP_sig_plus_mix_index = {}
    
    np.random.seed( 12345 )
    
    index_vars_ = None
    if not use_hash_index:
        index_vars_ = ['run', 'lumiblock', 'event', 'slice']
    else:
        index_vars_ = ['run', 'lumiblock', 'event', 'hash_id', 'slice']
    print ( index_vars_ )
    
    for label_ in labels_signals:
        print ( label_ )
        # df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_all" ] = 1.0
        # df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_all_weighted" ] = 1.0
        # df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_unc" ] = 0.0
        # if data_sample == '2017':
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_multitrack" ] = 1.0
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_strictzero" ] = 1.0
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_multitrack_weighted" ] = 1.0
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_strictzero_weighted" ] = 1.0
    
        # Random selection by efficiency weights
        msk_eff_proton_ = np.random.rand( df_signals_protons_multiRP_index[ label_ ].shape[0] ) < df_signals_protons_multiRP_index[ label_ ].loc[ :, "eff_proton_all" ]
        print ( msk_eff_proton_ )
        df_signals_protons_multiRP_eff_sel_index[ label_ ] = df_signals_protons_multiRP_index[ label_ ].loc[ msk_eff_proton_ ]
        df_signals_protons_multiRP_eff_sel_index[ label_ ][ 'random' ] = 1
        
        df_signals_protons_multiRP_sig_plus_mix_index[ label_ ] = pd.concat(
            [ df_signals_protons_multiRP_eff_sel_index[ label_ ],
              df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ] ] ).sort_index()
    
    df_signals_protons_multiRP_sig_plus_mix_2protons = {}
    for label_ in labels_signals:
        print ( label_ )
        if data_sample == '2017':
            # df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
            df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( index_vars_ )
            msk_2protons_single_proton_ = df_protons_multiRP_groupby_arm_[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ) )
            print ( msk_2protons_single_proton_, np.sum( msk_2protons_single_proton_ ) )
            df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ].loc[ msk_2protons_single_proton_ ]
        elif data_sample == '2018':
            # df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( ["run","lumiblock","event","slice"] )
            df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "arm" ] ].groupby( index_vars_ )
            msk_2protons_ = df_protons_multiRP_groupby_arm_[ "arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) >= 1 ) & ( np.sum( s_ == 1 ) >= 1 ) )
            print ( msk_2protons_, np.sum( msk_2protons_ ) )
            df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ].loc[ msk_2protons_ ]
    
    # Divide in categories
    df_signals_protons_multiRP_sig_plus_mix_2protons_sig = {}
    df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0 = {}
    df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1 = {}
    df_signals_protons_multiRP_sig_plus_mix_2protons_mix = {}
    for label_ in labels_signals:
        print ( label_ )
        
        df__ = df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ]
        # df_protons_multiRP_groupby__ = df__[ [ "arm", "random" ] ].groupby( ["run","lumiblock","event","slice"] )
        df_protons_multiRP_groupby__ = df__[ [ "arm", "random" ] ].groupby( index_vars_ )
        msk_sig_Arm0_ = df_protons_multiRP_groupby__.apply( lambda __df: np.sum( ( __df[ 'arm' ] == 0 ) & ( __df[ 'random' ] == 0 ) ) == 1 )
        msk_sig_Arm1_ = df_protons_multiRP_groupby__.apply( lambda __df: np.sum( ( __df[ 'arm' ] == 1 ) & ( __df[ 'random' ] == 0 ) ) == 1 )
        msk_2protons_ = ( msk_sig_Arm0_ & msk_sig_Arm1_ )
        msk_1proton_sig_Arm0_ = ( msk_sig_Arm0_ & ~msk_sig_Arm1_ )
        msk_1proton_sig_Arm1_ = ( ~msk_sig_Arm0_ & msk_sig_Arm1_ )
        msk_2protons_mix_ = ( ~msk_sig_Arm0_ & ~msk_sig_Arm1_ )
        print ( msk_2protons_, np.sum( msk_2protons_ ) )
        print ( msk_1proton_sig_Arm0_, np.sum( msk_1proton_sig_Arm0_ ) )
        print ( msk_1proton_sig_Arm1_, np.sum( msk_1proton_sig_Arm1_ ) )
        print ( msk_2protons_mix_, np.sum( msk_2protons_mix_ ) )
        
        if np.sum( msk_2protons_ ) > 0:
            df_signals_protons_multiRP_sig_plus_mix_2protons_sig[ label_ ] = df__.loc[ msk_2protons_ ]
        if np.sum( msk_1proton_sig_Arm0_ ) > 0:
            df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0[ label_ ] = df__.loc[ msk_1proton_sig_Arm0_ ]
        if np.sum( msk_1proton_sig_Arm1_ ) > 0:
            df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1[ label_ ] = df__.loc[ msk_1proton_sig_Arm1_ ]
        if np.sum( msk_2protons_mix_ ) > 0:
            df_signals_protons_multiRP_sig_plus_mix_2protons_mix[ label_ ] = df__.loc[ msk_2protons_mix_ ]
    
    df_signals_protons_multiRP_sig_plus_mix_2protons_events = {}
    df_signals_protons_multiRP_sig_plus_mix_events_categories = {}
    
    for label_ in labels_signals:
        print ( label_ )
        columns_protons_multiRP_ = df_signals_protons_multiRP_index[ label_ ].columns.values
        columns_ = columns_protons_multiRP_
        columns_eff_ = columns_[ [ key_[ : len('eff') ] == 'eff' for key_ in columns_ ] ]
        columns_xi_  = columns_[ [ key_[ : len('xi_') ] == 'xi_' for key_ in columns_ ] ]
        
        columns_drop_ = [ "xi", "thx", "thy", "t", "ismultirp", "rpid", "arm", "random",
                          "trackx1", "tracky1", "trackpixshift1", "rpid1",
                          "trackx2", "tracky2", "trackpixshift2", "rpid2" ]
        columns_drop_eff_xi_ = columns_drop_.copy()
        columns_drop_eff_xi_.extend( columns_eff_ )
        columns_drop_eff_xi_.extend( columns_xi_ )
    
        # file_path_ = "data-store-signal-plus-mix-events-{}.h5".format( label_ )
        file_path_ = None
        file_name_label_ = "data-store-signal-plus-mix-events-{}.h5".format( label_ )
        if output_dir_ is not None and output_dir_ != "":
            file_path_ = "{}/{}".format( output_dir_, file_name_label_ )
        else:
            file_path_ = file_name_label_
        print ( file_path_ )
        with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
            df__ = df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ]
            df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
            df_signals_protons_multiRP_sig_plus_mix_2protons_events[ label_ ] = df_protons_multiRP_events__
    
            df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ] = {}
            if label_ in df_signals_protons_multiRP_sig_plus_mix_2protons_sig.keys():
                print ( "2protons_sig" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_2protons_sig[ label_ ]
                df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
                # df_signals_protons_multiRP_sig_plus_mix_2protons_sig_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '2protons_sig' ] = df_protons_multiRP_events__
            if label_ in df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0.keys():
                print ( "1proton_sig_Arm0" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0[ label_ ]
                df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
                # df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '1proton_sig_Arm0' ] = df_protons_multiRP_events__
            if label_ in df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1.keys():
                print ( "1proton_sig_Arm1" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1[ label_ ]
                df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
                # df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '1proton_sig_Arm1' ] = df_protons_multiRP_events__
            if label_ in df_signals_protons_multiRP_sig_plus_mix_2protons_mix.keys():
                print ( "2protons_mix" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_2protons_mix[ label_ ]
                df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, runOnMC=True, mix_protons=False, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index )
                # df_signals_protons_multiRP_sig_plus_mix_2protons_mix_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '2protons_mix' ] = df_protons_multiRP_events__
            
            store_[ "events_multiRP/all" ] = df_signals_protons_multiRP_sig_plus_mix_2protons_events[ label_ ]
            for key_ in df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ]:
                store_[ "events_multiRP/{}".format( key_ ) ] = df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ key_ ]
            print ( list( store_ ) )

