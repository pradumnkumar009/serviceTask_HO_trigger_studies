import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

# For RAW
process = cms.Process("RECO", eras.Run2_2017)

# For RAW-RECO
#process = cms.Process("DTNT")

# process = cms.Process("DTNTandRPC")
#process = cms.Process("RECLUSTERIZATION")

 
##process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration/StandardSequences/Services_cff")

process.load("Configuration/StandardSequences/GeometryRecoDB_cff")  ##  solve STA problem
process.load("Configuration/EventContent/EventContent_cff")
process.load("Geometry.DTGeometryBuilder.dtGeometryDB_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")

process.load("EventFilter.DTRawToDigi.dtunpackerDDUGlobal_cfi")
process.dtunpacker.readOutParameters.debug = False
process.dtunpacker.readOutParameters.rosParameters.debug = False

# for DTTF (Not used from 2016)
#process.load("EventFilter.DTTFRawToDigi.dttfunpacker_cfi")
#process.load("EventFilter.DTTFRawToDigi.dttfpacker_cfi")

# for TWINMUX (Start to use in 2016)
process.load("EventFilter.L1TXRawToDigi.twinMuxStage2Digis_cfi")

# for HO-TP
process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")

#for RAW
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

# For DT segments from RAW
process.load("RecoLocalMuon.Configuration.RecoLocalMuon_cff")
process.dt1DRecHits.dtDigiLabel = "dtunpacker"

# For global muons from RAW
from RecoTracker.Configuration.RecoTracker_cff import *  ## Needed at least in  710pre8 to avoid an error in RecoMuon file (GroupedCkfTrajectoryBuilder)
from RecoMuon.Configuration.RecoMuon_cff import *
from RecoVertex.BeamSpotProducer.BeamSpot_cff import *
from TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagator_cfi import *
ancientMuonSeed.EnableCSCMeasurement = False
standAloneMuons.STATrajBuilderParameters.FilterParameters.EnableCSCMeasurement = False
standAloneMuons.STATrajBuilderParameters.FilterParameters.EnableRPCMeasurement = False
standAloneMuons.STATrajBuilderParameters.BWFilterParameters.EnableCSCMeasurement = False
standAloneMuons.STATrajBuilderParameters.BWFilterParameters.EnableRPCMeasurement = False
globalreco = cms.Sequence(process.offlineBeamSpot * process.standAloneMuonSeeds * process.standAloneMuons)


process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("RecoMuon.TrackingTools.MuonServiceProxy_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")  #DB v2, at least since GR_E_V42
process.GlobalTag.globaltag = "92X_dataRun2_Prompt_v8"

#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_data", "")

# for the emulator
process.load("L1TriggerConfig.DTTPGConfigProducers.L1DTTPGConfigFromDB_cff")
process.load("L1Trigger.DTTrigger.dtTriggerPrimitiveDigis_cfi")
process.dtTriggerPrimitiveDigis.debug = False
process.L1DTConfigFromDB.debug = False

process.load("EventFilter.ScalersRawToDigi.ScalersRawToDigi_cfi")
process.load("RecoLuminosity.LumiProducer.lumiProducer_cfi")

# process.load("EventFilter.L1TRawToDigi.l1tRawtoDigiBMTF_cfi")
process.load("EventFilter.L1TRawToDigi.bmtfDigis_cfi")

#maxEvents = -1
#maxEvents = 10 * pow(10, 3)
maxEvents = 100

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(maxEvents))

fNames = []

#sourceFileNames = cms.untracked.vstring([
#    # DAS name: /ExpressPhysics/Run2016H-Express-v2/FEVT
#    #"root://cms-xrd-global.cern.ch//store/express/Run2016H/ExpressPhysics/FEVT/Express-v2/000/283/820/00000/000BE88F-ED97-E611-B962-02163E011D7E.root",
#    #"root://cms-xrd-global.cern.ch//store/express/Run2016H/ExpressPhysics/FEVT/Express-v2/000/283/820/00000/0092B080-0798-E611-AD7E-02163E01184D.root",
#    #"root://cms-xrd-global.cern.ch//store/express/Run2016H/ExpressPhysics/FEVT/Express-v2/000/283/820/00000/00958F3E-FE97-E611-A000-02163E014255.root",
#    #"root://cms-xrd-global.cern.ch//store/express/Run2016H/ExpressPhysics/FEVT/Express-v2/000/283/820/00000/00B04838-E597-E611-882E-02163E0120A4.root",
#    #"root://cms-xrd-global.cern.ch//store/express/Run2016H/ExpressPhysics/FEVT/Express-v2/000/283/820/00000/00C5C0B0-EE97-E611-A10B-FA163EE76B26.root",
#
#    #"root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/RAW-RECO/ZMu-PromptReco-v3/000/300/742/00000/0C29534C-007E-E711-93CA-02163E01A458.root",
#    "root://cms-xrd-global.cern.ch//store/data/Run2017B/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/298/853/00000/1E44504F-8968-E711-9E26-02163E01A737.root",
#])


#sourceFile = "sourceFiles/SingleMuon/SingleMuon-Run2017A-ZMu-PromptReco-v2-RAW-RECO.txt"
#sourceFile = "sourceFiles/SingleMuon/SingleMuon-Run2017B-ZMu-PromptReco-v1-RAW-RECO.txt"
#
#sourceFile = "sourceFiles/ZeroBias/ZeroBias9-Run2017B-v1-RAW.txt"
#sourceFile = "sourceFiles/ZeroBias/ZeroBias10-Run2017C-v1-RAW.txt"
#sourceFile = "sourceFiles/SingleMuon/SingleMuon-Run2017F-v1-RAW.txt"
#sourceFile = "sourceFiles/SingleMuon/SingleMuon-Run2017C-ZMu-PromptReco-v3-RAW-RECO.txt"
#sourceFile = "sourceFiles/MET/MET-Run2017F-v1-RAW.txt"
#sourceFile = "sourceFiles/MET/MET-Run2017F-v1-RAW_mod.txt"

#with open(sourceFile) as f:
#    
#    fNames = f.readlines()


sourceFileNames = cms.untracked.vstring(fNames)


process.source = cms.Source("PoolSource",
    fileNames = sourceFileNames,
    secondaryFileNames = cms.untracked.vstring()
)

#this is to select collisions
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   cut = cms.string("!isFake && ndof > 4"), # && abs(z) <= 15 && position.Rho <= 2" # tracksSize() > 3 for the older cut
   filter = cms.bool(True),   # otherwise it won"t filter the events, just produce an empty vertex collection.
)

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
)

process.DTMuonSelection = cms.EDFilter("DTMuonSelection",
                                 src = cms.InputTag("muons"),
                                 Muons = cms.InputTag("muons"),
                                 SAMuons = cms.InputTag("standAloneMuons"),
                                 dtSegmentLabel = cms.InputTag("dt4DSegments"),
                                 etaMin = cms.double(-1.25),
                                 etaMax = cms.double(1.25),
                                 ptMin = cms.double(0.),#3.),
                                 tightness = cms.int32(1) # 0 = loose (e.g. unstable collisions, minimum bias, requires a DT segment)
                                                          # 1 = medium (e.g. cosmics, requires a stand alone muon)
                                                          # 2 = tight (good collisions, requires a global muon)
)


process.load("UserCode/DTDPGAnalysis/DTTTreGenerator_cfi")
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))

process.myDTNtuple.localDTmuons = cms.untracked.bool(False)
process.myDTNtuple.outputFile = "DTNtuple.root"
process.myDTNtuple.dtTrigSimDCCLabel = cms.InputTag("dtTriggerPrimitiveDigis")
process.myDTNtuple.dtDigiLabel = cms.InputTag("dtunpacker")

process.myDTNtuple.bmtfOutputDigis = cms.InputTag("bmtfDigis", "BMTF")
#process.myDTNtuple.bmtfOutputDigis = cms.InputTag("gmtStage2Digis", "BMTF")
#process.myDTNtuple.bmtfOutputDigis = cms.InputTag("BMTFStage2Digis")

# muon track extrapolation to 1st station
process.myDTNtuple.muProp1st = cms.PSet(
    useTrack = cms.string("tracker"),  # 'none' to use Candidate P4; or 'tracker', 'muon', 'global'
    useState = cms.string("atVertex"), # 'innermost' and 'outermost' require the TrackExtra
    useSimpleGeometry = cms.bool(True),
    useStation2 = cms.bool(False),
)

# muon track extrapolation to 2nd station
process.myDTNtuple.muProp2nd = cms.PSet(
    useTrack = cms.string("tracker"),  # 'none' to use Candidate P4; or 'tracker', 'muon', 'global'
    useState = cms.string("atVertex"), # 'innermost' and 'outermost' require the TrackExtra
    useSimpleGeometry = cms.bool(True),
    useStation2 = cms.bool(True),
    fallbackToME1 = cms.bool(False),
)

## RPC unpacking
process.load("EventFilter.RPCRawToDigi.rpcUnpackingModule_cfi")

## RPC recHit
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")
process.rpcRecHits.rpcDigiLabel = cms.InputTag("rpcUnpackingModule")


# For RAW
process.p = cms.Path(
    process.lumiProducer
    *process.dtunpacker
    *process.rpcUnpackingModule
    *process.rpcRecHits
    *process.RawToDigi
    *process.reconstruction
    *process.myDTNtuple
)


#process.p = cms.Path(
#    #process.DTMuonSelection
#    process.dtunpacker
#    #*process.twinMuxStage2Digis
#    #*process.dt1DRecHits
#    #*process.dt2DSegments
#    #*process.dt4DSegments
#    #*process.bmtfDigis
#    #*process.scalersRawToDigi
#    #*process.lumiProducer
#    #*process.dtTriggerPrimitiveDigis
#    *process.rpcUnpackingModule
#    *process.rpcRecHits
#    #*process.hcalDigis
#    *process.myDTNtuple
#)


# For RAW-RECO, FEVT, etc
#process.p = cms.Path(
#    #process.DTMuonSelection
#    process.dtunpacker
#    *process.twinMuxStage2Digis
#    *process.scalersRawToDigi
#    *process.lumiProducer
#    *process.dtTriggerPrimitiveDigis
#    *process.bmtfDigis
#    *process.rpcUnpackingModule
#    *process.rpcRecHits
#    *process.hcalDigis
#    *process.myDTNtuple
#)


# Output
process.TFileService = cms.Service("TFileService", fileName = cms.string("DTNtuple.root"))

#process.out = cms.OutputModule("PoolOutputModule", 
#    outputCommands = cms.untracked.vstring(
#        "keep *",
#        "keep *_*_*_testRPCTwinMuxRawToDigi",
#        "keep *_*_*_DTNTandRPC"
#    ),
#    fileName = cms.untracked.string("debug.root"),
#    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p"))
#)

process.schedule = cms.Schedule(process.p)

# Debug
#process.out = cms.OutputModule("PoolOutputModule", 
#    fileName = cms.untracked.string("debug.root")
#)
#
#process.output_step = cms.EndPath(process.out)
#process.schedule.extend([process.output_step])
