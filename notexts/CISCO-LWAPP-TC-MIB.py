#
# PySNMP MIB module CISCO-LWAPP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-TC-MIB
# Source digest sha256:25636c6315f67bdcd1a802d11882b285e462d0585534afc8e0302531c8db6bdf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 514))
ciscoLwappTextualConventions.setRevisions(('2019-11-29 00:00', '2016-08-23 00:00', '2011-09-13 00:00', '2010-02-23 00:00', '2007-09-11 00:00', '2007-02-05 00:00', '2006-10-31 00:00', '2006-04-13 00:00',))
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setLastUpdated('2019-11-29 00:00')
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setOrganization('Cisco Systems, Inc.')
class CLApIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("dot11bg", 1), ("dot11a", 2), ("uwb", 3), ("dot11abgn", 4), ("unknown", 5))

class CLDot11Channel(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), )
class CLDot11ClientStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("idle", 1), ("aaaPending", 2), ("authenticated", 3), ("associated", 4), ("powersave", 5), ("disassociated", 6), ("tobedeleted", 7), ("probing", 8), ("excluded", 9))

class CLEventFrames(TextualConvention, Bits):
    reference = 'Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications, Section 7.1.3.1.2 - Type and Subtype fields'
    status = 'current'
    namedValues = NamedValues(("cLAssocRequestFrm", 0), ("cLAssocResponseFrm", 1), ("cLReAssocRequestFrm", 2), ("cLReAssocResponseFrm", 3), ("cLProbeRequestFrm", 4), ("cLProbeResponseFrm", 5), ("cLReserved1", 6), ("cLReserved2", 7), ("cLBeaconFrm", 8), ("cLAtimFrm", 9), ("cLDissociationFrm", 10), ("cLAuthenticationFrm", 11), ("cLDeAuthenticationFrm", 12))

class CLMfpEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 16, 17, 19, 20, 21, 22, 23, 24, 32, 33, 34))
    namedValues = NamedValues(("invalidMic", 1), ("invalidSeq", 2), ("noMic", 3), ("unexpectedMic", 4), ("ccmpNoEncryptError", 16), ("ccmpDecryptError", 17), ("ccmpInvalidReplayCtr", 19), ("tkipNoEncryptError", 20), ("tkipInvalidIcv", 21), ("tkipInvalidMic", 22), ("tkipInvalidMhdrIe", 23), ("tkipInvalidReplayCtr", 24), ("bcastDisassociationFrameRcvd", 32), ("bcastDeauthenticationFrameRcvd", 33), ("bcastActionFrameRcvd", 34))

class CLMfpEventSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("infrastructureMfp", 1), ("clientMfp", 2))

class CLMfpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mfpv1", 1), ("mfpv2", 2))

class CLTimeBaseStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cTimeBaseInSync", 1), ("cTimeBaseNotInSync", 2))

class CLSecEncryptType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("tkip", 0), ("aes", 1))

class CLSecKeyFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("hex", 2), ("ascii", 3))

class CLDot11RfParamMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("custom", 2), ("auto", 3))

class CLTsmDot11CurrentPackets(TextualConvention, Gauge32):
    status = 'current'

class CLCdpAdvtVersionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cdpv1", 1), ("cdpv2", 2))

class CLDot11ChannelBandwidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("five", 1), ("ten", 2), ("twenty", 3), ("aboveforty", 4), ("belowforty", 5))

class CLDot11Band(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("band2dot4", 1), ("band5", 2))

class CLApAssocFailureReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("notSupported", 2))

class CLWebAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("internalDefault", 1), ("internalCustom", 2), ("external", 3))

class CLClientPowerSaveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("powersave", 2))

class CLApDot11RadioSubband(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("all", 1), ("sub49", 2), ("sub52", 3), ("sub54", 4), ("sub58", 5))

class CLApDot11RadioRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("shutdown", 0), ("upDownlink", 1), ("uplink", 2), ("downlink", 3), ("access", 4), ("uplinkAccess", 5), ("downlinkAccess", 6), ("upDownlinkAccess", 7), ("unknown", 8))

class CcxServiceVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("version1", 2), ("version2", 3))

class CLApMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("local", 0), ("monitor", 1), ("remote", 2), ("rogueDetector", 3), ("sniffer", 4), ("bridge", 5), ("seConnect", 6), ("remoteBridge", 7), ("remoteHybrid", 8), ("sensor", 9))

class CLApNtpStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notValid", 1), ("none", 2), ("unreachable", 3), ("synched", 4), ("notSynched", 5), ("waitSynch", 6), ("authFail", 7), ("notSuitable", 8), ("unknown", 9))

class Dscp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

mibBuilder.exportSymbols("CISCO-LWAPP-TC-MIB", CLApAssocFailureReason=CLApAssocFailureReason, CLApDot11RadioRole=CLApDot11RadioRole, CLApDot11RadioSubband=CLApDot11RadioSubband, CLApIfType=CLApIfType, CLApMode=CLApMode, CLApNtpStatus=CLApNtpStatus, CLCdpAdvtVersionType=CLCdpAdvtVersionType, CLClientPowerSaveMode=CLClientPowerSaveMode, CLDot11Band=CLDot11Band, CLDot11Channel=CLDot11Channel, CLDot11ChannelBandwidth=CLDot11ChannelBandwidth, CLDot11ClientStatus=CLDot11ClientStatus, CLDot11RfParamMode=CLDot11RfParamMode, CLEventFrames=CLEventFrames, CLMfpEventSource=CLMfpEventSource, CLMfpEventType=CLMfpEventType, CLMfpVersion=CLMfpVersion, CLSecEncryptType=CLSecEncryptType, CLSecKeyFormat=CLSecKeyFormat, CLTimeBaseStatus=CLTimeBaseStatus, CLTsmDot11CurrentPackets=CLTsmDot11CurrentPackets, CLWebAuthType=CLWebAuthType, CcxServiceVersion=CcxServiceVersion, Dscp=Dscp, PYSNMP_MODULE_ID=ciscoLwappTextualConventions, ciscoLwappTextualConventions=ciscoLwappTextualConventions)
