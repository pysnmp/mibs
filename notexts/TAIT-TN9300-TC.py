#
# PySNMP MIB module TAIT-TN9300-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-TN9300-TC
# Produced by pysmi-1.1.8 at Thu Dec 15 08:35:07 2022
# On host fv-az193-683 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, Counter64, iso, Gauge32, TimeTicks, NotificationType, IpAddress, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Counter64", "iso", "Gauge32", "TimeTicks", "NotificationType", "IpAddress", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
taitModules, = mibBuilder.importSymbols("TAIT-COMMON-MIB", "taitModules")
taittn9300TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 11, 1))
taittn9300TC.setRevisions(('2018-12-04 12:00', '2018-07-17 10:05', '2018-03-18 22:03', '2017-03-16 01:23', '2016-08-22 12:00', '2015-10-30 12:00', '2015-03-17 22:08', '2012-06-27 09:02', '2012-05-28 23:17',))
if mibBuilder.loadTexts: taittn9300TC.setLastUpdated('201812041200Z')
if mibBuilder.loadTexts: taittn9300TC.setOrganization('www.taitworld.com')
class NodeRequestedState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("offline", 1), ("program", 2), ("online", 3))

class NodeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("offline", 1), ("program", 2), ("switching", 3), ("control", 4))

class NetworkCheckState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notConfigured", 0), ("ok", 1), ("failed", 2))

class ChannelState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("disabled", 1), ("idle", 2), ("control", 3), ("traffic", 4), ("data", 5), ("failed", 6))

class SipLineRegistrationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("inbound", 1), ("outbound", 2), ("ais", 3))

class SipLineIncomingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("pstni", 1), ("pabxi", 2))

class SipCallSpeechVotingPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("normal", 1), ("override", 2))

class SipLineState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("disabled", 1), ("up", 2), ("down", 3))

class DipLineState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("unconfigured", 1), ("idle", 2), ("active", 3), ("failed", 4))

class NgwLinkState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2))

class Mpt1327LinkState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2))

class Mpt1327ChannelState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("idle", 1), ("traffic", 2), ("control", 3), ("failed", 4))

class RemoteNodeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("offline", 1), ("program", 2), ("switching", 3), ("control", 4), ("failed", 5), ("gracefulShutdown", 6))

class UnitStatusMessageId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 128))
    namedValues = NamedValues(("clearAll", 0), ("pppLinkToMpcDown", 1), ("gpsSignalLost", 2), ("gpsSignalRegainedAfterLoss", 3), ("terminalAntennaConnectionFailureVswrOutOfRange", 4), ("terminalSupplyVoltageOutOfRange", 5), ("radioTemperatureT0NormalRange", 6), ("radioTemperatureT1OverTemp", 7), ("radioTemperatureT2OverTemp", 8), ("radioTemperatureT3OverTemp", 9), ("terminalLossOfService", 10), ("radioFrequencyOutOfLockServiceRegained", 11), ("mcpConfigurationError", 12), ("terminalAntennaConnectionGood", 13), ("terminalUnsolicitedReset", 14), ("terminalGainedService", 15), ("unknown", 128))

class EventSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ok", 0), ("minor", 1), ("major", 2))

class LicenseValidity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("valid", 0), ("fileNotFound", 1), ("invalidHostId", 2), ("invalidProductCode", 3), ("invalidVersion", 4), ("invalidExpiryDate", 5), ("expired", 6), ("corruptSignature", 7), ("conflictingFeatures", 8), ("invalidTierMode", 9), ("invalidLicenseFormat", 10))

class UnitAuthentication(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notPolled", 0), ("polling", 1), ("notHome", 2), ("busy", 3), ("badAuthentication", 4), ("badCrcReceived", 5), ("goodAuthenticationReceived", 6), ("rejected", 7), ("notRegistered", 8))

class RemoteNodeSyncState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("failed", 1), ("unknown", 2), ("none", 3))

mibBuilder.exportSymbols("TAIT-TN9300-TC", SipLineIncomingType=SipLineIncomingType, SipCallSpeechVotingPriority=SipCallSpeechVotingPriority, UnitStatusMessageId=UnitStatusMessageId, LicenseValidity=LicenseValidity, taittn9300TC=taittn9300TC, RemoteNodeSyncState=RemoteNodeSyncState, UnitAuthentication=UnitAuthentication, NodeRequestedState=NodeRequestedState, SipLineRegistrationType=SipLineRegistrationType, SipLineState=SipLineState, NetworkCheckState=NetworkCheckState, PYSNMP_MODULE_ID=taittn9300TC, ChannelState=ChannelState, NodeState=NodeState, Mpt1327ChannelState=Mpt1327ChannelState, DipLineState=DipLineState, Mpt1327LinkState=Mpt1327LinkState, RemoteNodeState=RemoteNodeState, EventSeverity=EventSeverity, NgwLinkState=NgwLinkState)
