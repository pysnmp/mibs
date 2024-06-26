#
# PySNMP MIB module OMNITRON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/omnitron/OMNITRON-TC-MIB
# Produced by pysmi-1.1.12 at Wed Jun 26 13:37:32 2024
# On host fv-az1984-994 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Counter32, enterprises, Gauge32, MibIdentifier, IpAddress, iso, Counter64, Unsigned32, ModuleIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "enterprises", "Gauge32", "MibIdentifier", "IpAddress", "iso", "Counter64", "Unsigned32", "ModuleIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ostOmnitronTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7342, 11))
ostOmnitronTcMib.setRevisions(('2015-05-13 12:00', '2015-01-21 12:00',))
if mibBuilder.loadTexts: ostOmnitronTcMib.setLastUpdated('201505131200Z')
if mibBuilder.loadTexts: ostOmnitronTcMib.setOrganization('Omnitron Systems Technology, Inc.')
omnitron = MibIdentifier((1, 3, 6, 1, 4, 1, 7342))
icAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 1))
class OstAccessibiltyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

class OstClassOfService(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class OstClockFreq(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'

class OstCosL2cpDstAddr(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 20)

class OstCosNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstCosNameStringOrNone(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 45)

class OstCosTrustType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cosTrust", 1), ("cosUsePri", 2), ("cosUseClass", 3), ("cosUsePriClass", 4), ("cosGreenYellow", 5))

class OstEgressSchedulingProfileIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class OstEgressQueueIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class OstElpsProtectType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("e1plus1UniNoAps", 1), ("e1plus1UniAps", 2), ("e1plus1BiAps", 3), ("e1to1", 4), ("notAvailable", 5))

class OstElpsRequestStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16))
    namedValues = NamedValues(("noRequest", 0), ("doNotRevert", 1), ("revertRequest", 2), ("exercise", 4), ("waitToRestore", 5), ("manualSwitchWorking", 6), ("manualSwitch", 7), ("signalDegrade", 9), ("signalFailWorking", 11), ("forcedSwitch", 13), ("signalFailProtection", 14), ("lockoutProtection", 15), ("notAvailable", 16))

class OstElpsSignalStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nullSignal", 0), ("normalSignal", 1), ("notAvailable", 2))

class OstErpsLinkState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class OstErpsPortState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("forward", 1), ("blocked", 2))

class OstErpsPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rp0", 1), ("rp1", 2))

class OstErpsRingStates(TextualConvention, Integer32):
    reference = '[ITU-T G.8032] Table 10-1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("noRequest", 0), ("rapsNr", 1), ("rapsNrRb", 2), ("wtbRunning", 3), ("wtbExpires", 4), ("wtrRunning", 5), ("wtrExpires", 6), ("manualSwitch", 7), ("rapsManualSwitch", 8), ("rapsSignalFail", 9), ("localClearSignalFail", 10), ("localSignalFail", 11), ("rapsForcedSwitch", 12), ("forcedSwtich", 13), ("clear", 14))

class OstErpsRingStatus(TextualConvention, Integer32):
    reference = '[ITU-T G.8032] Table 10-2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initializing", 1), ("idle", 2), ("protection", 3), ("manualSwitch", 4), ("forcedSwitch", 5), ("pending", 6))

class OstErrorString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class OstEvcNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstEvcNameStringOrNone(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 45)

class OstFileNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstFingerprintString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class OstFloatValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class OstFrameCount64(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class OstFrameSizeList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class OstIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class OstIpPriorityList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class OstIpv6Addr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class OstIpAddr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 39)

class OstMhfCreation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ostMHFdefault", 1), ("ostMHFexplicit", 2))

class OstMipdMethodOfCreation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ostExplicit", 1), ("ostImplicitMa", 2), ("ostImplicitMde", 3), ("ostExplicitImplicitMa", 4))

class OstModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("ap", 2), ("sp", 3))

class OstModuleSingleIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(101, 9999)

class OstPcpPriorityList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class OstPortClockType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("adaptiveIdle", 1), ("adaptiveAcqu", 2), ("adaptiveTrk1", 3), ("adaptiveTrk2", 4), ("holdOver", 5), ("coax", 6), ("internal", 7), ("line", 8))

class OstPortList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'

class OstPortNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 99)

class OstPortSingleIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(10101, 999999)

class OstPriority(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class OstProbeNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstProfileNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstTestResultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pass", 1), ("fail", 2), ("oversubscribe", 3))

class OstTestStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("testNotStarted", 1), ("testInProcess", 2), ("testStopped", 3), ("testCompleted", 4), ("testInitializing", 5))

class OstUnsigned64(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class OstUserNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class OstVlanId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class OstVlanIdList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 110)

mibBuilder.exportSymbols("OMNITRON-TC-MIB", OstErpsRingStatus=OstErpsRingStatus, OstEgressSchedulingProfileIndexType=OstEgressSchedulingProfileIndexType, OstFileNameString=OstFileNameString, OstElpsRequestStates=OstElpsRequestStates, OstUserNameString=OstUserNameString, OstMhfCreation=OstMhfCreation, OstCosL2cpDstAddr=OstCosL2cpDstAddr, OstPcpPriorityList=OstPcpPriorityList, OstCosNameString=OstCosNameString, OstTestStatusType=OstTestStatusType, OstEgressQueueIndexType=OstEgressQueueIndexType, icAgent=icAgent, OstClassOfService=OstClassOfService, OstAccessibiltyType=OstAccessibiltyType, OstFrameCount64=OstFrameCount64, OstFingerprintString=OstFingerprintString, OstIndexIntegerNextFree=OstIndexIntegerNextFree, OstEvcNameStringOrNone=OstEvcNameStringOrNone, OstFloatValue=OstFloatValue, OstClockFreq=OstClockFreq, OstErrorString=OstErrorString, OstVlanId=OstVlanId, OstErpsPortType=OstErpsPortType, OstPriority=OstPriority, OstProbeNameString=OstProbeNameString, OstMipdMethodOfCreation=OstMipdMethodOfCreation, OstFrameSizeList=OstFrameSizeList, OstElpsProtectType=OstElpsProtectType, OstCosTrustType=OstCosTrustType, OstProfileNameString=OstProfileNameString, OstPortNumber=OstPortNumber, OstCosNameStringOrNone=OstCosNameStringOrNone, OstModuleSingleIndex=OstModuleSingleIndex, OstErpsPortState=OstErpsPortState, OstIpPriorityList=OstIpPriorityList, OstTestResultType=OstTestResultType, ostOmnitronTcMib=ostOmnitronTcMib, PYSNMP_MODULE_ID=ostOmnitronTcMib, OstPortClockType=OstPortClockType, OstVlanIdList=OstVlanIdList, OstElpsSignalStates=OstElpsSignalStates, OstIpv6Addr=OstIpv6Addr, OstErpsRingStates=OstErpsRingStates, OstModeType=OstModeType, OstErpsLinkState=OstErpsLinkState, OstPortList=OstPortList, OstPortSingleIndex=OstPortSingleIndex, OstEvcNameString=OstEvcNameString, OstIpAddr=OstIpAddr, OstUnsigned64=OstUnsigned64, omnitron=omnitron)
