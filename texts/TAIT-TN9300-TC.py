#
# PySNMP MIB module TAIT-TN9300-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-TN9300-TC
# Produced by pysmi-1.1.8 at Thu Sep  7 14:05:35 2023
# On host fv-az444-965 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Gauge32, ModuleIdentity, Integer32, iso, ObjectIdentity, Bits, Unsigned32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Gauge32", "ModuleIdentity", "Integer32", "iso", "ObjectIdentity", "Bits", "Unsigned32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
taitModules, = mibBuilder.importSymbols("TAIT-COMMON-MIB", "taitModules")
taittn9300TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 11, 1))
taittn9300TC.setRevisions(('2018-12-04 12:00', '2018-07-17 10:05', '2018-03-18 22:03', '2017-03-16 01:23', '2016-08-22 12:00', '2015-10-30 12:00', '2015-03-17 22:08', '2012-06-27 09:02', '2012-05-28 23:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: taittn9300TC.setRevisionsDescriptions(('Defined the EventSeverity, LicenseValidity, UnitAuthentication, and RemoteNodeSyncState textual conventions.', 'Changed to Tait International Limited', 'Changed naming on new terminal alarm definitions to camel case.', 'Fixed syntax on new terminal alarm definitions.', 'Added 3 Terminal alarm descriptions', 'Changed some descriptions', 'added UnitStatusMessageId enum', 'Changed type of the syscode value to string', 'Version 1.00.01\n       Status  [under review]',))
if mibBuilder.loadTexts: taittn9300TC.setLastUpdated('201812041200Z')
if mibBuilder.loadTexts: taittn9300TC.setOrganization('www.taitworld.com')
if mibBuilder.loadTexts: taittn9300TC.setContactInfo('postal:   Tait International Limited\n                 558 Wairakei Road\n                 Christchurch\n                 PO Box 1645\n                 Christchurch\n                 New Zealand\n\n       phone:    +64 3358 3399\n       email:    support@taitworld.com')
if mibBuilder.loadTexts: taittn9300TC.setDescription('Textual conventions used in the TN9300 MIB.')
class NodeRequestedState(TextualConvention, Integer32):
    description = 'The state that a node has been instructed to enter. Status types are: Unknown (0), Offline(1), Program (2), or Online (3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("offline", 1), ("program", 2), ("online", 3))

class NodeState(TextualConvention, Integer32):
    description = 'The state in which a node is operating. Status types are Unknown (0), Offline (1), Program (2), Switching (3) or Control (4).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("offline", 1), ("program", 2), ("switching", 3), ("control", 4))

class NetworkCheckState(TextualConvention, Integer32):
    description = 'The status of a network check. Status types are Not Configured (0), OK (1) or Failed (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notConfigured", 0), ("ok", 1), ("failed", 2))

class ChannelState(TextualConvention, Integer32):
    description = 'The state in which a channel is operating. Status types are Unknown (0), Disabled (1), Idle (2), Control (3), Traffic (4), Data (5) or Failed (6).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("disabled", 1), ("idle", 2), ("control", 3), ("traffic", 4), ("data", 5), ("failed", 6))

class SipLineRegistrationType(TextualConvention, Integer32):
    description = 'The types of SIP line registration. Registration types are Unknown (0), Outbound (1), Inbound (2) or AIS (3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("inbound", 1), ("outbound", 2), ("ais", 3))

class SipLineIncomingType(TextualConvention, Integer32):
    description = 'The ident of the A party in an incoming phone call. Ident types are Unknown (0), PSTNI (1) or PABXI (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("pstni", 1), ("pabxi", 2))

class SipCallSpeechVotingPriority(TextualConvention, Integer32):
    description = 'The speech voting priority for SIP calls. Priority types are Unknown (0), Normal (1) or Override (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("normal", 1), ("override", 2))

class SipLineState(TextualConvention, Integer32):
    description = 'The state in which a SIP line is operating. Status types are Unknown (0), Disabled (1), Up (2) or Down (3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("disabled", 1), ("up", 2), ("down", 3))

class DipLineState(TextualConvention, Integer32):
    description = 'The state in which a DIP line is operating. Status types are Unknown (0), Unconfigured (1), Idle (2), Active (3) or Failed (4).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("unconfigured", 1), ("idle", 2), ("active", 3), ("failed", 4))

class NgwLinkState(TextualConvention, Integer32):
    description = 'The state of the link to the network gateway. Status types are Unknown (0), OK (1) or Failed (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2))

class Mpt1327LinkState(TextualConvention, Integer32):
    description = 'The state of the link to the MPT gateway. Status types are Unknown (0), OK (1) or Failed (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2))

class Mpt1327ChannelState(TextualConvention, Integer32):
    description = 'The state in which an MPT 1327 channel is operating. Status types are Unknown (0), Idle (1), Traffic (2), Control (3) or Failed (4).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("idle", 1), ("traffic", 2), ("control", 3), ("failed", 4))

class RemoteNodeState(TextualConvention, Integer32):
    description = 'The state in which a remote node is operating. Status types are Unknown (0), Offline (1), Program (2), Switching (3), Control (4), Failed (5) or Graceful Shutdown (6).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("offline", 1), ("program", 2), ("switching", 3), ("control", 4), ("failed", 5), ("gracefulShutdown", 6))

class UnitStatusMessageId(TextualConvention, Integer32):
    description = 'Unit alarm status message IDs:\n        PPP link to MPC down (1),\n        GPS signal lost (2),\n        GPS signal regained (after loss) (3),\n        Unit antenna connection failure (VSWR out of range) (4),\n        Unit supply voltage out of range (5),\n        Unit temperature T0 (normal range) (6),\n        Unit temperature T1 (over temp) (7),\n        Unit temperature T2 (over temp) (8),\n        Unit temperature T3 (over temp) (9),\n        Unit loss of service (10),\n        Radio frequency out of lock (service regained) (11),\n        MCP configuration error (12),\n        Unit antenna connection good (13),\n        Unit unsolicited reset (14),\n        Unit gained service (15)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 128))
    namedValues = NamedValues(("clearAll", 0), ("pppLinkToMpcDown", 1), ("gpsSignalLost", 2), ("gpsSignalRegainedAfterLoss", 3), ("terminalAntennaConnectionFailureVswrOutOfRange", 4), ("terminalSupplyVoltageOutOfRange", 5), ("radioTemperatureT0NormalRange", 6), ("radioTemperatureT1OverTemp", 7), ("radioTemperatureT2OverTemp", 8), ("radioTemperatureT3OverTemp", 9), ("terminalLossOfService", 10), ("radioFrequencyOutOfLockServiceRegained", 11), ("mcpConfigurationError", 12), ("terminalAntennaConnectionGood", 13), ("terminalUnsolicitedReset", 14), ("terminalGainedService", 15), ("unknown", 128))

class EventSeverity(TextualConvention, Integer32):
    description = 'The severity of an event. Types are OK (0), Minor (1), or Major (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ok", 0), ("minor", 1), ("major", 2))

class LicenseValidity(TextualConvention, Integer32):
    description = 'The current validity of the license. Types are as follows:\n                Valid (0),\n                File Not Found (1),\n                Invalid Host ID (2),\n                Invalid Product Code(3),\n                Invalid Version (4),\n                Invalid Expiry Date (5),\n                Expired (6),\n                Corrupt Signature (7),\n                Conflicting Features (8),\n                Invalid Tier Mode (9),\n                Invalid License Format (10)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("valid", 0), ("fileNotFound", 1), ("invalidHostId", 2), ("invalidProductCode", 3), ("invalidVersion", 4), ("invalidExpiryDate", 5), ("expired", 6), ("corruptSignature", 7), ("conflictingFeatures", 8), ("invalidTierMode", 9), ("invalidLicenseFormat", 10))

class UnitAuthentication(TextualConvention, Integer32):
    description = 'The authentication state of a unit. Types are as follows:\n                Not Polled (0),\n                Polling (1),\n                Not Home (2),\n                Busy (3),\n                Bad Authentication (4),\n                Bad CRC Received (5),\n                Good Authentication Received (6),\n                Rejected (7),\n                Not Registered (8)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notPolled", 0), ("polling", 1), ("notHome", 2), ("busy", 3), ("badAuthentication", 4), ("badCrcReceived", 5), ("goodAuthenticationReceived", 6), ("rejected", 7), ("notRegistered", 8))

class RemoteNodeSyncState(TextualConvention, Integer32):
    description = 'The state of synchronisation between the control and a remote node. Types are OK (0), Failed (1), Unknown (2), or None (3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("failed", 1), ("unknown", 2), ("none", 3))

mibBuilder.exportSymbols("TAIT-TN9300-TC", Mpt1327ChannelState=Mpt1327ChannelState, SipLineIncomingType=SipLineIncomingType, EventSeverity=EventSeverity, DipLineState=DipLineState, NodeRequestedState=NodeRequestedState, NetworkCheckState=NetworkCheckState, LicenseValidity=LicenseValidity, taittn9300TC=taittn9300TC, UnitStatusMessageId=UnitStatusMessageId, UnitAuthentication=UnitAuthentication, ChannelState=ChannelState, NgwLinkState=NgwLinkState, Mpt1327LinkState=Mpt1327LinkState, RemoteNodeSyncState=RemoteNodeSyncState, SipLineRegistrationType=SipLineRegistrationType, SipLineState=SipLineState, PYSNMP_MODULE_ID=taittn9300TC, NodeState=NodeState, RemoteNodeState=RemoteNodeState, SipCallSpeechVotingPriority=SipCallSpeechVotingPriority)
