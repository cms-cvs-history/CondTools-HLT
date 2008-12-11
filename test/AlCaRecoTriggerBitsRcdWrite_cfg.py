import FWCore.ParameterSet.Config as cms

process = cms.Process("WRITEDB")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr = cms.untracked.PSet(placeholder = cms.untracked.bool(True))
process.MessageLogger.cout = cms.untracked.PSet(INFO = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(1)
    ))

# the module writing to DB
process.load("CondTools.HLT.AlCaRecoTriggerBitsRcdWrite_cfi")
process.AlCaRecoTriggerBitsRcdWrite.firstRunIOV = 1 # default is 1
# -1 means infinity (must be -1 if appending to existing tag):
process.AlCaRecoTriggerBitsRcdWrite.lastRunIOV = -1
process.AlCaRecoTriggerBitsRcdWrite.triggerLists = [ #is a VPSet, order not preserved in DB!
    cms.PSet(listName = cms.string('TkAlMinBias'),
             hltPaths = cms.vstring('HLT_MinBiasEcal', 'HLT_MinBiasHcal',
                                    'HLT_MinBiasPixel')
             ),
    cms.PSet(listName = cms.string('TkAlMuonIsolated'),
             hltPaths = cms.vstring('HLT_Mu3', 'HLT_Mu5', 'HLT_IsoMu11', 'HLT_Mu15')
             ),
    cms.PSet(listName = cms.string('MuAlCalIsolatedMu'),
             hltPaths = cms.vstring('HLT_L1MuOpen', 'HLT_L1Mu', 'HLT_Mu3',
                                    'HLT_Mu5', 'HLT_Mu7', 'HLT_Mu9',
                                    'HLT_Mu11', 'HLT_Mu13', 'HLT_Mu15',
                                    'HLT_L2Mu9', 'HLT_IsoMu9', 'HLT_IsoMu11',
                                    'HLT_IsoMu13', 'HLT_IsoMu15')
             )
    ] # end VPSet

# No data, have to run on one event:
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

# DB output service:
import CondCore.DBCommon.CondDBSetup_cfi
process.PoolDBOutputService = cms.Service(
    "PoolDBOutputService",
    CondCore.DBCommon.CondDBSetup_cfi.CondDBSetup,
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:AlCaRecoTriggerBits.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('AlCaRecoTriggerBitsRcd'),
        tag = cms.string('TestTag') # choose tag you want
        )
                      )
    )

# Put module in path:
process.p = cms.Path(process.AlCaRecoTriggerBitsRcdWrite)


