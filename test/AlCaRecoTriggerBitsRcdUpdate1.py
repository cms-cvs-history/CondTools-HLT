# Config file template to write new/update AlCaRecoTriggerBits stored
# in AlCaRecoTriggerBitsRcd that is used to get selected HLT paths for
# the HLTHighLevel filter for AlCaReco production.
# See comments inside, especially the WARNING.
# 
#  Author    : Gero Flucke
#  Date      : February 2009
#  $Revision: 1.2 $
#  $Date: 2009/02/11 14:25:12 $
#  (last update by $Author: flucke $)

import FWCore.ParameterSet.Config as cms

process = cms.Process("UPDATEDB")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr = cms.untracked.PSet(placeholder = cms.untracked.bool(True))
process.MessageLogger.cout = cms.untracked.PSet(INFO = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(1)
    ))

# the module writing to DB
process.load("CondTools.HLT.AlCaRecoTriggerBitsRcdUpdate_cfi")
# The IOV that you want to write out, defaut is 1 to -1/inf. 
#process.AlCaRecoTriggerBitsRcdUpdate.firstRunIOV = 1 # docu see...
#process.AlCaRecoTriggerBitsRcdUpdate.lastRunIOV = -1 # ...cfi
# If you want to update, uncomment the next line:
#process.AlCaRecoTriggerBitsRcdUpdate.startEmpty = False
# In case you want to remove 'keys', use this possibly comma separated list.
# Also if you want to replace settings for one 'key', you have to remove it first.
#process.AlCaRecoTriggerBitsRcdUpdate.listNamesRemove = ["TkAlZMuMu"]
# Here specifiy 'key' and corresponding paths for new entries or updated ones:
#process.AlCaRecoTriggerBitsRcdUpdate.triggerListsAdd = [
#    cms.PSet(listName = cms.string('TkAlZMuMu'),
#             hltPaths = cms.vstring('path_1','path_2','path_3')),
#    cms.PSet(listName = cms.string('Bla'),
#             hltPaths = cms.vstring('p1','p2'))
#    ]
process.AlCaRecoTriggerBitsRcdUpdate.triggerListsAdd = [
    # TkAl
    cms.PSet(listName = cms.string('TkAlMinBiasNOT'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', 'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3',
                                    'HLT_TrackerCosmics'
                                    )),
    cms.PSet(listName = cms.string('TkAlMuonIsolated'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3')),
    cms.PSet(listName = cms.string('TkAlJpsiMuMu'),
             hltPaths = cms.vstring('HLT_DoubleMu3')),
    cms.PSet(listName = cms.string('TkAlUpsilonMuMu'),
             hltPaths = cms.vstring('HLT_DoubleMu3')),
    cms.PSet(listName = cms.string('TkAlZMuMu'),
             hltPaths = cms.vstring('HLT_DoubleMu3')),
    cms.PSet(listName = cms.string('TkAlCosmics'),
             hltPaths = cms.vstring('HLT_TrackerCosmics')),
    cms.PSet(listName = cms.string('TkAlCosmics0T'),
             hltPaths = cms.vstring('HLT_TrackerCosmics')),
    #cms.PSet(listName = cms.string('TkAlBeamHalo'),
    #         hltPaths = cms.vstring()), # no HLT filter in yet
    # MuAlCal
    cms.PSet(listName = cms.string('MuAlCalIsolatedMu'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3')),
    # MuAl
    # MuAlZMuMu: # FIXME: add in AlCaRecoStreams.py
    cms.PSet(listName = cms.string('MuAlZMuMu'), 
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3'
                                    )),
    cms.PSet(listName = cms.string('MuAlOverlaps'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3')),
    cms.PSet(listName = cms.string('MuAlStandAloneCosmics'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3',
                                    'HLT_TrackerCosmics'
                                    )),
    cms.PSet(listName = cms.string('MuAlGlobalCosmics'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_L2Mu9',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5', 'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    'HLT_DoubleMu3',
                                    'HLT_TrackerCosmics'
                                    )),
    cms.PSet(listName = cms.string('MuAlBeamHalo'),
             hltPaths = cms.vstring('HLT_CSCBeamHalo',
                                    'HLT_CSCBeamHaloRing2or3'
                                    )),
    cms.PSet(listName = cms.string('MuAlBeamHaloOverlaps'), 
             hltPaths = cms.vstring('HLT_CSCBeamHaloOverlapRing1',
                                    'HLT_CSCBeamHaloOverlapRing2')),
    # Pixel obsolete for now!
    #    cms.PSet(listName = cms.string('SiPixelLorentzAngle'),
    #             hltPaths = cms.vstring('HLT_IsoMu11', 'HLT_DoubleMu3', # old menu!
    #                                    'HLT_DoubleMu3_JPsi', 'HLT_DoubleMu3_Upsilon',
    #                                    'HLT_DoubleMu7_Z' , 'HLT_DoubleMu3_SameSign'
    #                                    )),
    # SiStrip Cal
    cms.PSet(listName = cms.string('SiStripCalZeroBias'),
             hltPaths = cms.vstring('HLT_ZeroBias' #,
                                    # FIXME: Gordon: next used for cosmics, but neither menu
                                    # on twiki nor ConfDB?
                                    #'RandomPath'
                                    )),
    # ECAL
    cms.PSet(listName = cms.string('EcalCalElectron'),
             hltPaths = cms.vstring('HLT_Ele15_SW_L1R', 'HLT_DoubleEle10_SW_L1R', # 1E31
                                    'HLT_Ele10_LW_L1R', 'HLT_DoubleEle5_SW_L1R'  # 8E29
                                    )),
    cms.PSet(listName = cms.string('EcalCalPhiSym'),
             hltPaths = cms.vstring('AlCa_EcalPhiSym')),
    cms.PSet(listName = cms.string('EcalCalPi0Calib'),
             hltPaths = cms.vstring('AlCa_EcalPi0')),
    cms.PSet(listName = cms.string('EcalCalEtaCalib'), # eta is new
             hltPaths = cms.vstring('AlCa_EcalEta')),
    #HCAL
    cms.PSet(listName = cms.string('HcalCalDijets'),
             hltPaths = cms.vstring('HLT_Jet30', 'HLT_Jet50', 'HLT_Jet80',# for 1e31
                                    'HLT_Jet15U', 'HLT_Jet30U', 'HLT_Jet50U' # for 8e29
                                    )),
    # obsolete at beginning
    #cms.PSet(listName = cms.string('HcalCalGammaJet'),
    #         hltPaths = cms.vstring('HLT_IsoPhoton30_L1I', 'HLT_IsoPhoton15_L1R'
    #                                # both not in 8e29 nor 1e31
    #                                )),
    cms.PSet(listName = cms.string('HcalCalHO'),
             hltPaths = cms.vstring('HLT_IsoMu3',   #for 8E29
                                    'HLT_IsoMu9')), #for 1E31
    cms.PSet(listName = cms.string('HcalCalHOCosmics'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_Mu3',  'HLT_Mu5')),
    cms.PSet(listName = cms.string('HcalCalMinBias'),
             hltPaths = cms.vstring('AlCa_HcalPhiSym')),
    cms.PSet(listName = cms.string('HcalCalIsoTrk'),
             hltPaths = cms.vstring('HLT_IsoTrack', # new, was 'AlCa_IsoTrack'
                                    'HLT_IsoTrack_8E29', # FIXME: specials for 8e29
                                    'HLT_IsoTrack_1E31'  #   and 1e31 for now (?) 
                                    )),
    # RPC
    cms.PSet(listName = cms.string('RpcCalHLT'), # FIXME: old triggers???
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu',
                                    'HLT_Mu3', # not in 1e31, but in 8e29
                                    'HLT_Mu5',
                                    #GF 'HLT_Mu7', # FIXME: not in 8e29 nor 1e31
                                    'HLT_Mu9',
                                    'HLT_Mu11', # not in 8e29, but in 1e31
                                    #GF 'HLT_Mu13', # FIXME: not in 8e29 nor 1e31
                                    'HLT_Mu15', # not in 8e29, but in 1e31
                                    # (Stephanie: the above claimed missing?)
                                    # GF'HLT_Mu15_L1Mu7',# FIXME: not in 8e29 nor 1e31
                                    'HLT_L2Mu9', # in 8e29, but 1e31 unclear
                                    'HLT_IsoMu9', # not in 8e29, but in 1e31
                                    #GF 'HLT_IsoMu11', 'HLT_IsoMu13', 'HLT_IsoMu15'
                                    # FIXME: all three above not in 8e29 nor 1e31
                                    ))
    ]


# No data, but have to specify run number if you do not want 1, see below:
process.source = cms.Source("EmptySource",
                            #numberEventsInRun = cms.untracked.uint32(1),
                            #firstRun = cms.untracked.uint32(1) # 1 is default
                            )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

# DB input - needed only for AlCaRecoTriggerBitsRcdUpdate.startEmpty = False
# WARNING:
# Take care in case the input tag has an IOV: The run number that will be used
# to define which payload you get is defined by the run number in the
# EmptySource above!
# import CondCore.DBCommon.CondDBSetup_cfi
#process.dbInput = cms.ESSource(
#    "PoolDBESSource",
#    CondCore.DBCommon.CondDBSetup_cfi.CondDBSetup,
#    connect = cms.string('sqlite_file:AlCaRecoTriggerBits.db'),
#    toGet = cms.VPSet(cms.PSet(
#        record = cms.string('AlCaRecoTriggerBitsRcd'),
#        tag = cms.string('TestTag') # choose old tag to update
#        )
#                      )
#    )

# DB output service:
import CondCore.DBCommon.CondDBSetup_cfi
process.PoolDBOutputService = cms.Service(
    "PoolDBOutputService",
    CondCore.DBCommon.CondDBSetup_cfi.CondDBSetup,
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:AlCaRecoTriggerBits4.db'),
#    connect = cms.string('sqlite_file:AlCaRecoTriggerBitsUpdate.db'),
#    connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_HLT'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('AlCaRecoTriggerBitsRcd'),
        tag = cms.string('AlCaRecoHLTpaths8e29_1e31_v4') # choose tag you want
        )
                      )
    )


# Put module in path:
process.p = cms.Path(process.AlCaRecoTriggerBitsRcdUpdate)


