#
# PySNMP MIB module AT-PTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-PTP-MIB
# Produced by pysmi-1.1.8 at Thu Feb  3 20:58:20 2022
# On host fv-az36-616 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, iso, ObjectIdentity, IpAddress, ModuleIdentity, NotificationType, Counter64, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ObjectIdentity", "IpAddress", "ModuleIdentity", "NotificationType", "Counter64", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32")
TextualConvention, AutonomousType, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "DisplayString", "TruthValue")
atPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504))
atPtpMIB.setRevisions(('2017-01-23 00:00',))
if mibBuilder.loadTexts: atPtpMIB.setLastUpdated('201701230000Z')
if mibBuilder.loadTexts: atPtpMIB.setOrganization('Allied Telesis, Inc.')
class PtpClockDomainType(TextualConvention, Unsigned32):
    reference = 'Section 7.1 Domains, Table 2 of [IEEE 1588-2008]'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class PtpClockIdentity(TextualConvention, OctetString):
    reference = 'Section 7.5.2.2.1 of [IEEE 1588-2008]'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class PtpClockInstanceType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class PtpClockIntervalBase2(TextualConvention, Integer32):
    reference = 'Section 7.7.2.1 General interval specification of [IEEE 1588-2008]'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class PtpClockMechanismType(TextualConvention, Integer32):
    reference = 'Sections 8.2.5.4.4 portDS.delayMechanism, 6.6.4 Measuring link propagation delay in clocks supporting peer-to-peer path correction, 7.4.2 communication Path asymmetry of [IEEE 1588-2008].'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 254))
    namedValues = NamedValues(("e2e", 1), ("p2p", 2), ("disabled", 254))

class PtpClockPortNumber(TextualConvention, Unsigned32):
    reference = 'Sections 7.5.2.3 portNumber and 5.3.5 PortIdentity of [IEEE 1588-2008]'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PtpClockPortState(TextualConvention, Integer32):
    reference = 'Section 8.2.5.3.1 portState and 9.2.5 State machines of [IEEE 1588-2008]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("initializing", 1), ("faulty", 2), ("disabled", 3), ("listening", 4), ("preMaster", 5), ("master", 6), ("passive", 7), ("uncalibrated", 8), ("slave", 9))

class PtpClockPortTransportTypeAddress(TextualConvention, OctetString):
    reference = 'Annex D (IPv4), Annex E (IPv6), Annex F (Ethernet), Annex G (DeviceNET), Annex H (ControlNET) and Annex I (IEC61158) of [IEEE 1588-2008]'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class PtpClockProfileType(TextualConvention, Integer32):
    reference = 'Section 3.1.30 profile and 19.3 PTP profiles of [IEEE 1588-2008]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("telecom", 2), ("vendorspecific", 3))

class PtpClockQualityAccuracyType(TextualConvention, Integer32):
    reference = 'Section 5.3.7 ClockQuality, 7.6.2.5 clockAccuracy and Table 6 clockAccuracy enumeration of [IEEE 1588-2008]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 254))
    namedValues = NamedValues(("nanoSecond25", 32), ("nanoSecond100", 33), ("nanoSecond250", 34), ("microSec1", 35), ("microSec2dot5", 36), ("microSec10", 37), ("microSec25", 38), ("microSec100", 39), ("microSec250", 40), ("milliSec1", 41), ("milliSec2dot5", 42), ("milliSec10", 43), ("milliSec25", 44), ("milliSec100", 45), ("milliSec250", 46), ("second1", 47), ("second10", 48), ("secondGreater10", 49), ("unknown", 254))

class PtpClockQualityClassType(TextualConvention, Integer32):
    reference = 'Section 5.3.7, 7.6.2.4 and Table 5 of [IEEE 1588-2008].'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(6, 7, 13, 14, 52, 58))
    namedValues = NamedValues(("clockclass6", 6), ("clockclass7", 7), ("clockclass13", 13), ("clockclass14", 14), ("clockclass52", 52), ("clockclass58", 58))

class PtpClockRoleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("master", 1), ("slave", 2))

class PtpClockStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("freerun", 1), ("holdover", 2), ("acquiring", 3), ("frequencyLocked", 4), ("phaseAligned", 5))

class PtpClockTimeInterval(TextualConvention, OctetString):
    reference = 'Section 5.3.2 TimeInterval and section 7.7.2.1 Timer interval specification of [IEEE 1588-2008]'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class PtpClockTimeSourceType(TextualConvention, Integer32):
    reference = 'Section 5.3.7, 7.6.2.6 and Table 7 of [IEEE 1588-2008].'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16, 32, 48, 64, 80, 96, 144, 160))
    namedValues = NamedValues(("atomicClock", 16), ("gps", 32), ("terrestrialRadio", 48), ("ptp", 64), ("ntp", 80), ("handSet", 96), ("other", 144), ("internalOscillator", 160))

class PtpClockTxModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("multicastmix", 3))

class PtpClockType(TextualConvention, Integer32):
    reference = 'Section 6.5.1 PTP device types of [IEEE 1588-2008].'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ordinaryClock", 1), ("boundaryClock", 2), ("transparentClock", 3), ("boundaryNode", 4))

ptpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 0))
ptpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1))
ptpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2))
ptpMIBSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1))
ptpMIBClockInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2))
ptpSystemTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1), )
if mibBuilder.loadTexts: ptpSystemTable.setStatus('current')
ptpSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpDomainIndex"), (0, "AT-PTP-MIB", "ptpInstanceIndex"))
if mibBuilder.loadTexts: ptpSystemEntry.setStatus('current')
ptpDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpDomainIndex.setStatus('current')
ptpInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1, 2), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpInstanceIndex.setStatus('current')
ptpDomainClockPortsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1, 3), Gauge32()).setUnits('ptp ports').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpDomainClockPortsTotal.setStatus('current')
ptpSystemDomainTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2), )
if mibBuilder.loadTexts: ptpSystemDomainTable.setStatus('current')
ptpSystemDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpSystemDomainClockTypeIndex"))
if mibBuilder.loadTexts: ptpSystemDomainEntry.setStatus('current')
ptpSystemDomainClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2, 1, 1), PtpClockType())
if mibBuilder.loadTexts: ptpSystemDomainClockTypeIndex.setStatus('current')
ptpSystemDomainTotals = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2, 1, 2), Unsigned32()).setUnits('domains').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpSystemDomainTotals.setStatus('current')
ptpSystemProfile = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 3), PtpClockProfileType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpSystemProfile.setStatus('current')
ptpClockCurrentDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1), )
if mibBuilder.loadTexts: ptpClockCurrentDSTable.setStatus('current')
ptpClockCurrentDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockCurrentDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockCurrentDSClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockCurrentDSInstanceIndex"))
if mibBuilder.loadTexts: ptpClockCurrentDSEntry.setStatus('current')
ptpClockCurrentDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockCurrentDSDomainIndex.setStatus('current')
ptpClockCurrentDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockCurrentDSClockTypeIndex.setStatus('current')
ptpClockCurrentDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockCurrentDSInstanceIndex.setStatus('current')
ptpClockCurrentDSStepsRemoved = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 4), Unsigned32()).setUnits('Steps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockCurrentDSStepsRemoved.setStatus('current')
ptpClockCurrentDSOffsetFromMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 5), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockCurrentDSOffsetFromMaster.setStatus('current')
ptpClockCurrentDSMeanPathDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 6), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockCurrentDSMeanPathDelay.setStatus('current')
ptpClockParentDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2), )
if mibBuilder.loadTexts: ptpClockParentDSTable.setStatus('current')
ptpClockParentDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockParentDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockParentDSClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockParentDSInstanceIndex"))
if mibBuilder.loadTexts: ptpClockParentDSEntry.setStatus('current')
ptpClockParentDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockParentDSDomainIndex.setStatus('current')
ptpClockParentDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockParentDSClockTypeIndex.setStatus('current')
ptpClockParentDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockParentDSInstanceIndex.setStatus('current')
ptpClockParentDSParentPortIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSParentPortIdentity.setStatus('current')
ptpClockParentDSParentStats = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSParentStats.setStatus('current')
ptpClockParentDSOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 6), PtpClockIntervalBase2().subtype(subtypeSpec=ValueRangeConstraint(-128, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSOffset.setStatus('current')
ptpClockParentDSClockPhChRate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSClockPhChRate.setStatus('current')
ptpClockParentDSGMClockIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 8), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSGMClockIdentity.setStatus('current')
ptpClockParentDSGMClockPriority1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSGMClockPriority1.setStatus('current')
ptpClockParentDSGMClockPriority2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSGMClockPriority2.setStatus('current')
ptpClockParentDSGMClockQualityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 11), PtpClockQualityClassType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSGMClockQualityClass.setStatus('current')
ptpClockParentDSGMClockQualityAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 12), PtpClockQualityAccuracyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSGMClockQualityAccuracy.setStatus('current')
ptpClockParentDSGMClockQualityOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockParentDSGMClockQualityOffset.setStatus('current')
ptpClockDefaultDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3), )
if mibBuilder.loadTexts: ptpClockDefaultDSTable.setStatus('current')
ptpClockDefaultDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockDefaultDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockDefaultDSClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockDefaultDSInstanceIndex"))
if mibBuilder.loadTexts: ptpClockDefaultDSEntry.setStatus('current')
ptpClockDefaultDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockDefaultDSDomainIndex.setStatus('current')
ptpClockDefaultDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockDefaultDSClockTypeIndex.setStatus('current')
ptpClockDefaultDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockDefaultDSInstanceIndex.setStatus('current')
ptpClockDefaultDSTwoStepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSTwoStepFlag.setStatus('current')
ptpClockDefaultDSClockIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 5), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSClockIdentity.setStatus('current')
ptpClockDefaultDSPriority1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSPriority1.setStatus('current')
ptpClockDefaultDSPriority2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSPriority2.setStatus('current')
ptpClockDefaultDSSlaveOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSSlaveOnly.setStatus('current')
ptpClockDefaultDSQualityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 9), PtpClockQualityClassType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSQualityClass.setStatus('current')
ptpClockDefaultDSQualityAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 10), PtpClockQualityAccuracyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSQualityAccuracy.setStatus('current')
ptpClockDefaultDSQualityOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockDefaultDSQualityOffset.setStatus('current')
ptpClockRunningTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4), )
if mibBuilder.loadTexts: ptpClockRunningTable.setStatus('current')
ptpClockRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockRunningDomainIndex"), (0, "AT-PTP-MIB", "ptpClockRunningClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockRunningInstanceIndex"))
if mibBuilder.loadTexts: ptpClockRunningEntry.setStatus('current')
ptpClockRunningDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockRunningDomainIndex.setStatus('current')
ptpClockRunningClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockRunningClockTypeIndex.setStatus('current')
ptpClockRunningInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockRunningInstanceIndex.setStatus('current')
ptpClockRunningState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 4), PtpClockStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockRunningState.setStatus('current')
ptpClockRunningPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockRunningPacketsSent.setStatus('current')
ptpClockRunningPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockRunningPacketsReceived.setStatus('current')
ptpClockTimePropertiesDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5), )
if mibBuilder.loadTexts: ptpClockTimePropertiesDSTable.setStatus('current')
ptpClockTimePropertiesDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockTimePropertiesDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockTimePropertiesDSClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockTimePropertiesDSInstanceIndex"))
if mibBuilder.loadTexts: ptpClockTimePropertiesDSEntry.setStatus('current')
ptpClockTimePropertiesDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockTimePropertiesDSDomainIndex.setStatus('current')
ptpClockTimePropertiesDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockTimePropertiesDSClockTypeIndex.setStatus('current')
ptpClockTimePropertiesDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockTimePropertiesDSInstanceIndex.setStatus('current')
ptpClockTimePropertiesDSCurrentUTCOffsetValid = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSCurrentUTCOffsetValid.setStatus('current')
ptpClockTimePropertiesDSCurrentUTCOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSCurrentUTCOffset.setStatus('current')
ptpClockTimePropertiesDSLeap59 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSLeap59.setStatus('current')
ptpClockTimePropertiesDSLeap61 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSLeap61.setStatus('current')
ptpClockTimePropertiesDSTimeTraceable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSTimeTraceable.setStatus('current')
ptpClockTimePropertiesDSFreqTraceable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSFreqTraceable.setStatus('current')
ptpClockTimePropertiesDSPTPTimescale = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSPTPTimescale.setStatus('current')
ptpClockTimePropertiesDSSource = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 11), PtpClockTimeSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTimePropertiesDSSource.setStatus('current')
ptpClockTransDefaultDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6), )
if mibBuilder.loadTexts: ptpClockTransDefaultDSTable.setStatus('current')
ptpClockTransDefaultDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockTransDefaultDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockTransDefaultDSInstanceIndex"))
if mibBuilder.loadTexts: ptpClockTransDefaultDSEntry.setStatus('current')
ptpClockTransDefaultDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockTransDefaultDSDomainIndex.setStatus('current')
ptpClockTransDefaultDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 2), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockTransDefaultDSInstanceIndex.setStatus('current')
ptpClockTransDefaultDSClockIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 3), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTransDefaultDSClockIdentity.setStatus('current')
ptpClockTransDefaultDSNumOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTransDefaultDSNumOfPorts.setStatus('current')
ptpClockTransDefaultDSDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 5), PtpClockMechanismType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTransDefaultDSDelay.setStatus('current')
ptpClockTransDefaultDSPrimaryDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 6), PtpClockDomainType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockTransDefaultDSPrimaryDomain.setStatus('current')
ptpClockPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7), )
if mibBuilder.loadTexts: ptpClockPortTable.setStatus('current')
ptpClockPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockPortDomainIndex"), (0, "AT-PTP-MIB", "ptpClockPortClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockPortClockInstanceIndex"), (0, "AT-PTP-MIB", "ptpClockPortTablePortNumberIndex"))
if mibBuilder.loadTexts: ptpClockPortEntry.setStatus('current')
ptpClockPortDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockPortDomainIndex.setStatus('current')
ptpClockPortClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockPortClockTypeIndex.setStatus('current')
ptpClockPortClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockPortClockInstanceIndex.setStatus('current')
ptpClockPortTablePortNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpClockPortTablePortNumberIndex.setStatus('current')
ptpClockPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortName.setStatus('current')
ptpClockPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 6), PtpClockRoleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRole.setStatus('current')
ptpClockPortSyncTwoStep = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortSyncTwoStep.setStatus('current')
ptpClockPortCurrentPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 8), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortCurrentPeerAddressType.setStatus('current')
ptpClockPortCurrentPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 9), PtpClockPortTransportTypeAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortCurrentPeerAddress.setStatus('current')
ptpClockPortNumOfAssociatedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortNumOfAssociatedPorts.setStatus('current')
ptpClockPortDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8), )
if mibBuilder.loadTexts: ptpClockPortDSTable.setStatus('current')
ptpClockPortDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockPortDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockPortDSClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockPortDSClockInstanceIndex"), (0, "AT-PTP-MIB", "ptpClockPortDSPortNumberIndex"))
if mibBuilder.loadTexts: ptpClockPortDSEntry.setStatus('current')
ptpClockPortDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockPortDSDomainIndex.setStatus('current')
ptpClockPortDSClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockPortDSClockTypeIndex.setStatus('current')
ptpClockPortDSClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockPortDSClockInstanceIndex.setStatus('current')
ptpClockPortDSPortNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpClockPortDSPortNumberIndex.setStatus('current')
ptpClockPortDSName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSName.setStatus('current')
ptpClockPortDSPortIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSPortIdentity.setStatus('current')
ptpClockPortDSlogAnnouncementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 7), PtpClockIntervalBase2()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSlogAnnouncementInterval.setStatus('current')
ptpClockPortDSAnnounceRctTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSAnnounceRctTimeout.setStatus('current')
ptpClockPortDSlogSyncInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 9), PtpClockIntervalBase2()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSlogSyncInterval.setStatus('current')
ptpClockPortDSMinDelayReqInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSMinDelayReqInterval.setStatus('current')
ptpClockPortDSPeerDelayReqInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSPeerDelayReqInterval.setStatus('current')
ptpClockPortDSDelayMech = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 12), PtpClockMechanismType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSDelayMech.setStatus('current')
ptpClockPortDSPeerMeanPathDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 13), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSPeerMeanPathDelay.setStatus('current')
ptpClockPortDSGrantDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 14), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSGrantDuration.setStatus('current')
ptpClockPortDSPTPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortDSPTPVersion.setStatus('current')
ptpClockPortRunningTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9), )
if mibBuilder.loadTexts: ptpClockPortRunningTable.setStatus('current')
ptpClockPortRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockPortRunningDomainIndex"), (0, "AT-PTP-MIB", "ptpClockPortRunningClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockPortRunningClockInstanceIndex"), (0, "AT-PTP-MIB", "ptpClockPortRunningPortNumberIndex"))
if mibBuilder.loadTexts: ptpClockPortRunningEntry.setStatus('current')
ptpClockPortRunningDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockPortRunningDomainIndex.setStatus('current')
ptpClockPortRunningClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockPortRunningClockTypeIndex.setStatus('current')
ptpClockPortRunningClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockPortRunningClockInstanceIndex.setStatus('current')
ptpClockPortRunningPortNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpClockPortRunningPortNumberIndex.setStatus('current')
ptpClockPortRunningName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningName.setStatus('current')
ptpClockPortRunningState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 6), PtpClockPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningState.setStatus('current')
ptpClockPortRunningRole = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 7), PtpClockRoleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningRole.setStatus('current')
ptpClockPortRunningInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningInterfaceIndex.setStatus('current')
ptpClockPortRunningTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 9), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningTransport.setStatus('current')
ptpClockPortRunningEncapsulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 10), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningEncapsulationType.setStatus('current')
ptpClockPortRunningTxMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 11), PtpClockTxModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningTxMode.setStatus('current')
ptpClockPortRunningRxMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 12), PtpClockTxModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningRxMode.setStatus('current')
ptpClockPortRunningPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 13), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningPacketsReceived.setStatus('current')
ptpClockPortRunningPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 14), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortRunningPacketsSent.setStatus('current')
ptpClockPortTransDSTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10), )
if mibBuilder.loadTexts: ptpClockPortTransDSTable.setStatus('current')
ptpClockPortTransDSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockPortTransDSDomainIndex"), (0, "AT-PTP-MIB", "ptpClockPortTransDSInstanceIndex"), (0, "AT-PTP-MIB", "ptpClockPortTransDSPortNumberIndex"))
if mibBuilder.loadTexts: ptpClockPortTransDSEntry.setStatus('current')
ptpClockPortTransDSDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockPortTransDSDomainIndex.setStatus('current')
ptpClockPortTransDSInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 2), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockPortTransDSInstanceIndex.setStatus('current')
ptpClockPortTransDSPortNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 3), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpClockPortTransDSPortNumberIndex.setStatus('current')
ptpClockPortTransDSPortIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 4), PtpClockIdentity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortTransDSPortIdentity.setStatus('current')
ptpClockPortTransDSlogMinPdelayReqInt = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 5), PtpClockIntervalBase2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortTransDSlogMinPdelayReqInt.setStatus('current')
ptpClockPortTransDSFaultyFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortTransDSFaultyFlag.setStatus('current')
ptpClockPortTransDSPeerMeanPathDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 7), PtpClockTimeInterval()).setUnits('Time Interval').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortTransDSPeerMeanPathDelay.setStatus('current')
ptpClockPortAssociateTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11), )
if mibBuilder.loadTexts: ptpClockPortAssociateTable.setStatus('current')
ptpWellKnownTransportTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12))
ptpTransportTypeIPversion4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 1))
if mibBuilder.loadTexts: ptpTransportTypeIPversion4.setStatus('current')
ptpTransportTypeIPversion6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 2))
if mibBuilder.loadTexts: ptpTransportTypeIPversion6.setStatus('current')
ptpTransportTypeEthernet = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 3))
if mibBuilder.loadTexts: ptpTransportTypeEthernet.setStatus('current')
ptpTransportTypeDeviceNET = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 4))
if mibBuilder.loadTexts: ptpTransportTypeDeviceNET.setStatus('current')
ptpTransportTypeControlNET = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 5))
if mibBuilder.loadTexts: ptpTransportTypeControlNET.setStatus('current')
ptpTransportTypeIEC61158 = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 6))
if mibBuilder.loadTexts: ptpTransportTypeIEC61158.setStatus('current')
ptpWellKnownEncapsulationTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13))
ptpEncapsulationTypeEthernet = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 1))
if mibBuilder.loadTexts: ptpEncapsulationTypeEthernet.setStatus('current')
ptpEncapsulationTypeVLAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 2))
if mibBuilder.loadTexts: ptpEncapsulationTypeVLAN.setStatus('current')
ptpEncapsulationTypeUDPIPLSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 3))
if mibBuilder.loadTexts: ptpEncapsulationTypeUDPIPLSP.setStatus('current')
ptpEncapsulationTypePWUDPIPLSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 4))
if mibBuilder.loadTexts: ptpEncapsulationTypePWUDPIPLSP.setStatus('current')
ptpEncapsulationTypePWEthernetLSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 5))
if mibBuilder.loadTexts: ptpEncapsulationTypePWEthernetLSP.setStatus('current')
ptpClockPortAssociateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1), ).setIndexNames((0, "AT-PTP-MIB", "ptpClockPortCurrentDomainIndex"), (0, "AT-PTP-MIB", "ptpClockPortCurrentClockTypeIndex"), (0, "AT-PTP-MIB", "ptpClockPortCurrentClockInstanceIndex"), (0, "AT-PTP-MIB", "ptpClockPortCurrentPortNumberIndex"), (0, "AT-PTP-MIB", "ptpClockPortAssociatePortIndex"))
if mibBuilder.loadTexts: ptpClockPortAssociateEntry.setStatus('current')
ptpClockPortCurrentDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 1), PtpClockDomainType())
if mibBuilder.loadTexts: ptpClockPortCurrentDomainIndex.setStatus('current')
ptpClockPortCurrentClockTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 2), PtpClockType())
if mibBuilder.loadTexts: ptpClockPortCurrentClockTypeIndex.setStatus('current')
ptpClockPortCurrentClockInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 3), PtpClockInstanceType())
if mibBuilder.loadTexts: ptpClockPortCurrentClockInstanceIndex.setStatus('current')
ptpClockPortCurrentPortNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 4), PtpClockPortNumber())
if mibBuilder.loadTexts: ptpClockPortCurrentPortNumberIndex.setStatus('current')
ptpClockPortAssociatePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ptpClockPortAssociatePortIndex.setStatus('current')
ptpClockPortAssociateAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 6), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortAssociateAddressType.setStatus('current')
ptpClockPortAssociateAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 7), PtpClockPortTransportTypeAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortAssociateAddress.setStatus('current')
ptpClockPortAssociatePacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 8), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortAssociatePacketsSent.setStatus('current')
ptpClockPortAssociatePacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 9), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortAssociatePacketsReceived.setStatus('current')
ptpClockPortAssociateInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 10), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortAssociateInErrors.setStatus('current')
ptpClockPortAssociateOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 11), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpClockPortAssociateOutErrors.setStatus('current')
ptpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1))
ptpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2))
ptpMIBCompliancesSystemInfo = ModuleCompliance((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 1)).setObjects(("AT-PTP-MIB", "ptpMIBSystemInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBCompliancesSystemInfo = ptpMIBCompliancesSystemInfo.setStatus('current')
ptpMIBCompliancesClockInfo = ModuleCompliance((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 2)).setObjects(("AT-PTP-MIB", "ptpMIBClockCurrentDSGroup"), ("AT-PTP-MIB", "ptpMIBClockParentDSGroup"), ("AT-PTP-MIB", "ptpMIBClockDefaultDSGroup"), ("AT-PTP-MIB", "ptpMIBClockRunningGroup"), ("AT-PTP-MIB", "ptpMIBClockTimepropertiesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBCompliancesClockInfo = ptpMIBCompliancesClockInfo.setStatus('current')
ptpMIBCompliancesClockPortInfo = ModuleCompliance((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 3)).setObjects(("AT-PTP-MIB", "ptpMIBClockPortGroup"), ("AT-PTP-MIB", "ptpMIBClockPortDSGroup"), ("AT-PTP-MIB", "ptpMIBClockPortRunningGroup"), ("AT-PTP-MIB", "ptpMIBClockPortAssociateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBCompliancesClockPortInfo = ptpMIBCompliancesClockPortInfo.setStatus('current')
ptpMIBCompliancesTransparentClockInfo = ModuleCompliance((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 4)).setObjects(("AT-PTP-MIB", "ptpMIBClockTranparentDSGroup"), ("AT-PTP-MIB", "ptpMIBClockPortTransDSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBCompliancesTransparentClockInfo = ptpMIBCompliancesTransparentClockInfo.setStatus('current')
ptpMIBSystemInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 1)).setObjects(("AT-PTP-MIB", "ptpSystemDomainTotals"), ("AT-PTP-MIB", "ptpDomainClockPortsTotal"), ("AT-PTP-MIB", "ptpSystemProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBSystemInfoGroup = ptpMIBSystemInfoGroup.setStatus('current')
ptpMIBClockCurrentDSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 2)).setObjects(("AT-PTP-MIB", "ptpClockCurrentDSStepsRemoved"), ("AT-PTP-MIB", "ptpClockCurrentDSOffsetFromMaster"), ("AT-PTP-MIB", "ptpClockCurrentDSMeanPathDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockCurrentDSGroup = ptpMIBClockCurrentDSGroup.setStatus('current')
ptpMIBClockParentDSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 3)).setObjects(("AT-PTP-MIB", "ptpClockParentDSParentPortIdentity"), ("AT-PTP-MIB", "ptpClockParentDSParentStats"), ("AT-PTP-MIB", "ptpClockParentDSOffset"), ("AT-PTP-MIB", "ptpClockParentDSClockPhChRate"), ("AT-PTP-MIB", "ptpClockParentDSGMClockIdentity"), ("AT-PTP-MIB", "ptpClockParentDSGMClockPriority1"), ("AT-PTP-MIB", "ptpClockParentDSGMClockPriority2"), ("AT-PTP-MIB", "ptpClockParentDSGMClockQualityClass"), ("AT-PTP-MIB", "ptpClockParentDSGMClockQualityAccuracy"), ("AT-PTP-MIB", "ptpClockParentDSGMClockQualityOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockParentDSGroup = ptpMIBClockParentDSGroup.setStatus('current')
ptpMIBClockDefaultDSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 4)).setObjects(("AT-PTP-MIB", "ptpClockDefaultDSTwoStepFlag"), ("AT-PTP-MIB", "ptpClockDefaultDSClockIdentity"), ("AT-PTP-MIB", "ptpClockDefaultDSPriority1"), ("AT-PTP-MIB", "ptpClockDefaultDSPriority2"), ("AT-PTP-MIB", "ptpClockDefaultDSSlaveOnly"), ("AT-PTP-MIB", "ptpClockDefaultDSQualityClass"), ("AT-PTP-MIB", "ptpClockDefaultDSQualityAccuracy"), ("AT-PTP-MIB", "ptpClockDefaultDSQualityOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockDefaultDSGroup = ptpMIBClockDefaultDSGroup.setStatus('current')
ptpMIBClockRunningGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 5)).setObjects(("AT-PTP-MIB", "ptpClockRunningState"), ("AT-PTP-MIB", "ptpClockRunningPacketsSent"), ("AT-PTP-MIB", "ptpClockRunningPacketsReceived"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockRunningGroup = ptpMIBClockRunningGroup.setStatus('current')
ptpMIBClockTimepropertiesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 6)).setObjects(("AT-PTP-MIB", "ptpClockTimePropertiesDSCurrentUTCOffsetValid"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSCurrentUTCOffset"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSLeap59"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSLeap61"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSTimeTraceable"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSFreqTraceable"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSPTPTimescale"), ("AT-PTP-MIB", "ptpClockTimePropertiesDSSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockTimepropertiesGroup = ptpMIBClockTimepropertiesGroup.setStatus('current')
ptpMIBClockTranparentDSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 7)).setObjects(("AT-PTP-MIB", "ptpClockTransDefaultDSClockIdentity"), ("AT-PTP-MIB", "ptpClockTransDefaultDSNumOfPorts"), ("AT-PTP-MIB", "ptpClockTransDefaultDSDelay"), ("AT-PTP-MIB", "ptpClockTransDefaultDSPrimaryDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockTranparentDSGroup = ptpMIBClockTranparentDSGroup.setStatus('current')
ptpMIBClockPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 8)).setObjects(("AT-PTP-MIB", "ptpClockPortName"), ("AT-PTP-MIB", "ptpClockPortSyncTwoStep"), ("AT-PTP-MIB", "ptpClockPortCurrentPeerAddress"), ("AT-PTP-MIB", "ptpClockPortNumOfAssociatedPorts"), ("AT-PTP-MIB", "ptpClockPortCurrentPeerAddressType"), ("AT-PTP-MIB", "ptpClockPortRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockPortGroup = ptpMIBClockPortGroup.setStatus('current')
ptpMIBClockPortDSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 9)).setObjects(("AT-PTP-MIB", "ptpClockPortDSName"), ("AT-PTP-MIB", "ptpClockPortDSPortIdentity"), ("AT-PTP-MIB", "ptpClockPortDSlogAnnouncementInterval"), ("AT-PTP-MIB", "ptpClockPortDSAnnounceRctTimeout"), ("AT-PTP-MIB", "ptpClockPortDSlogSyncInterval"), ("AT-PTP-MIB", "ptpClockPortDSMinDelayReqInterval"), ("AT-PTP-MIB", "ptpClockPortDSPeerDelayReqInterval"), ("AT-PTP-MIB", "ptpClockPortDSDelayMech"), ("AT-PTP-MIB", "ptpClockPortDSPeerMeanPathDelay"), ("AT-PTP-MIB", "ptpClockPortDSGrantDuration"), ("AT-PTP-MIB", "ptpClockPortDSPTPVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockPortDSGroup = ptpMIBClockPortDSGroup.setStatus('current')
ptpMIBClockPortRunningGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 10)).setObjects(("AT-PTP-MIB", "ptpClockPortRunningName"), ("AT-PTP-MIB", "ptpClockPortRunningState"), ("AT-PTP-MIB", "ptpClockPortRunningRole"), ("AT-PTP-MIB", "ptpClockPortRunningInterfaceIndex"), ("AT-PTP-MIB", "ptpClockPortRunningTransport"), ("AT-PTP-MIB", "ptpClockPortRunningEncapsulationType"), ("AT-PTP-MIB", "ptpClockPortRunningTxMode"), ("AT-PTP-MIB", "ptpClockPortRunningRxMode"), ("AT-PTP-MIB", "ptpClockPortRunningPacketsReceived"), ("AT-PTP-MIB", "ptpClockPortRunningPacketsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockPortRunningGroup = ptpMIBClockPortRunningGroup.setStatus('current')
ptpMIBClockPortTransDSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 11)).setObjects(("AT-PTP-MIB", "ptpClockPortTransDSPortIdentity"), ("AT-PTP-MIB", "ptpClockPortTransDSlogMinPdelayReqInt"), ("AT-PTP-MIB", "ptpClockPortTransDSFaultyFlag"), ("AT-PTP-MIB", "ptpClockPortTransDSPeerMeanPathDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockPortTransDSGroup = ptpMIBClockPortTransDSGroup.setStatus('current')
ptpMIBClockPortAssociateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 12)).setObjects(("AT-PTP-MIB", "ptpClockPortAssociatePacketsSent"), ("AT-PTP-MIB", "ptpClockPortAssociatePacketsReceived"), ("AT-PTP-MIB", "ptpClockPortAssociateAddress"), ("AT-PTP-MIB", "ptpClockPortAssociateAddressType"), ("AT-PTP-MIB", "ptpClockPortAssociateInErrors"), ("AT-PTP-MIB", "ptpClockPortAssociateOutErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptpMIBClockPortAssociateGroup = ptpMIBClockPortAssociateGroup.setStatus('current')
mibBuilder.exportSymbols("AT-PTP-MIB", ptpSystemTable=ptpSystemTable, ptpClockCurrentDSTable=ptpClockCurrentDSTable, ptpClockDefaultDSTable=ptpClockDefaultDSTable, PtpClockTimeInterval=PtpClockTimeInterval, ptpMIBNotifs=ptpMIBNotifs, ptpClockRunningInstanceIndex=ptpClockRunningInstanceIndex, ptpClockPortAssociateTable=ptpClockPortAssociateTable, ptpMIBClockRunningGroup=ptpMIBClockRunningGroup, ptpClockPortRunningEncapsulationType=ptpClockPortRunningEncapsulationType, ptpClockDefaultDSInstanceIndex=ptpClockDefaultDSInstanceIndex, ptpClockDefaultDSSlaveOnly=ptpClockDefaultDSSlaveOnly, PtpClockTxModeType=PtpClockTxModeType, ptpSystemDomainEntry=ptpSystemDomainEntry, ptpClockCurrentDSDomainIndex=ptpClockCurrentDSDomainIndex, ptpSystemDomainTotals=ptpSystemDomainTotals, ptpClockRunningState=ptpClockRunningState, ptpDomainClockPortsTotal=ptpDomainClockPortsTotal, ptpMIBClockParentDSGroup=ptpMIBClockParentDSGroup, ptpMIBClockPortGroup=ptpMIBClockPortGroup, ptpClockPortDSClockTypeIndex=ptpClockPortDSClockTypeIndex, ptpClockDefaultDSClockTypeIndex=ptpClockDefaultDSClockTypeIndex, PtpClockPortNumber=PtpClockPortNumber, ptpMIBCompliancesSystemInfo=ptpMIBCompliancesSystemInfo, ptpClockDefaultDSEntry=ptpClockDefaultDSEntry, ptpMIBClockCurrentDSGroup=ptpMIBClockCurrentDSGroup, ptpSystemDomainTable=ptpSystemDomainTable, ptpMIBClockPortDSGroup=ptpMIBClockPortDSGroup, ptpClockParentDSTable=ptpClockParentDSTable, ptpClockDefaultDSTwoStepFlag=ptpClockDefaultDSTwoStepFlag, ptpClockPortCurrentClockTypeIndex=ptpClockPortCurrentClockTypeIndex, ptpClockTimePropertiesDSFreqTraceable=ptpClockTimePropertiesDSFreqTraceable, ptpMIBCompliancesTransparentClockInfo=ptpMIBCompliancesTransparentClockInfo, ptpClockPortAssociatePacketsSent=ptpClockPortAssociatePacketsSent, ptpSystemProfile=ptpSystemProfile, ptpWellKnownEncapsulationTypes=ptpWellKnownEncapsulationTypes, ptpClockPortRunningTable=ptpClockPortRunningTable, ptpClockParentDSGMClockQualityOffset=ptpClockParentDSGMClockQualityOffset, ptpClockPortRunningEntry=ptpClockPortRunningEntry, ptpClockPortRunningPacketsSent=ptpClockPortRunningPacketsSent, ptpClockParentDSDomainIndex=ptpClockParentDSDomainIndex, ptpClockDefaultDSQualityAccuracy=ptpClockDefaultDSQualityAccuracy, ptpClockTimePropertiesDSTimeTraceable=ptpClockTimePropertiesDSTimeTraceable, ptpClockTimePropertiesDSPTPTimescale=ptpClockTimePropertiesDSPTPTimescale, ptpClockPortDSDomainIndex=ptpClockPortDSDomainIndex, PtpClockMechanismType=PtpClockMechanismType, atPtpMIB=atPtpMIB, ptpClockPortEntry=ptpClockPortEntry, ptpClockPortClockInstanceIndex=ptpClockPortClockInstanceIndex, ptpClockDefaultDSDomainIndex=ptpClockDefaultDSDomainIndex, ptpClockPortTransDSPortIdentity=ptpClockPortTransDSPortIdentity, ptpClockDefaultDSPriority2=ptpClockDefaultDSPriority2, ptpClockRunningEntry=ptpClockRunningEntry, ptpClockRunningPacketsSent=ptpClockRunningPacketsSent, ptpMIBClockInfo=ptpMIBClockInfo, ptpEncapsulationTypeUDPIPLSP=ptpEncapsulationTypeUDPIPLSP, ptpMIBClockTranparentDSGroup=ptpMIBClockTranparentDSGroup, ptpMIBSystemInfo=ptpMIBSystemInfo, ptpClockPortDSPeerDelayReqInterval=ptpClockPortDSPeerDelayReqInterval, ptpClockDefaultDSClockIdentity=ptpClockDefaultDSClockIdentity, ptpClockPortRunningClockTypeIndex=ptpClockPortRunningClockTypeIndex, ptpClockParentDSOffset=ptpClockParentDSOffset, ptpClockTransDefaultDSNumOfPorts=ptpClockTransDefaultDSNumOfPorts, ptpClockTimePropertiesDSInstanceIndex=ptpClockTimePropertiesDSInstanceIndex, ptpClockParentDSEntry=ptpClockParentDSEntry, ptpClockPortName=ptpClockPortName, ptpClockPortRunningPacketsReceived=ptpClockPortRunningPacketsReceived, ptpClockCurrentDSMeanPathDelay=ptpClockCurrentDSMeanPathDelay, ptpTransportTypeDeviceNET=ptpTransportTypeDeviceNET, ptpClockPortCurrentPeerAddressType=ptpClockPortCurrentPeerAddressType, PtpClockStateType=PtpClockStateType, ptpClockTimePropertiesDSTable=ptpClockTimePropertiesDSTable, ptpClockCurrentDSOffsetFromMaster=ptpClockCurrentDSOffsetFromMaster, ptpClockParentDSParentStats=ptpClockParentDSParentStats, ptpClockPortCurrentPeerAddress=ptpClockPortCurrentPeerAddress, ptpClockDefaultDSQualityClass=ptpClockDefaultDSQualityClass, ptpClockTransDefaultDSTable=ptpClockTransDefaultDSTable, ptpClockPortDSlogAnnouncementInterval=ptpClockPortDSlogAnnouncementInterval, ptpClockPortAssociateInErrors=ptpClockPortAssociateInErrors, ptpClockDefaultDSPriority1=ptpClockDefaultDSPriority1, ptpClockPortTransDSInstanceIndex=ptpClockPortTransDSInstanceIndex, ptpClockPortAssociateOutErrors=ptpClockPortAssociateOutErrors, ptpClockPortCurrentClockInstanceIndex=ptpClockPortCurrentClockInstanceIndex, ptpClockPortRunningTransport=ptpClockPortRunningTransport, ptpMIBClockPortRunningGroup=ptpMIBClockPortRunningGroup, ptpInstanceIndex=ptpInstanceIndex, ptpMIBConformance=ptpMIBConformance, PYSNMP_MODULE_ID=atPtpMIB, ptpClockRunningDomainIndex=ptpClockRunningDomainIndex, ptpTransportTypeIEC61158=ptpTransportTypeIEC61158, ptpClockParentDSInstanceIndex=ptpClockParentDSInstanceIndex, ptpClockPortSyncTwoStep=ptpClockPortSyncTwoStep, ptpClockPortRunningInterfaceIndex=ptpClockPortRunningInterfaceIndex, ptpEncapsulationTypePWUDPIPLSP=ptpEncapsulationTypePWUDPIPLSP, ptpDomainIndex=ptpDomainIndex, PtpClockQualityAccuracyType=PtpClockQualityAccuracyType, ptpClockParentDSGMClockQualityClass=ptpClockParentDSGMClockQualityClass, PtpClockInstanceType=PtpClockInstanceType, ptpClockPortRunningRxMode=ptpClockPortRunningRxMode, ptpClockParentDSGMClockPriority1=ptpClockParentDSGMClockPriority1, ptpClockTimePropertiesDSCurrentUTCOffset=ptpClockTimePropertiesDSCurrentUTCOffset, PtpClockTimeSourceType=PtpClockTimeSourceType, ptpClockPortDSPortIdentity=ptpClockPortDSPortIdentity, ptpMIBCompliancesClockPortInfo=ptpMIBCompliancesClockPortInfo, ptpClockPortRunningState=ptpClockPortRunningState, ptpClockParentDSParentPortIdentity=ptpClockParentDSParentPortIdentity, ptpMIBCompliancesClockInfo=ptpMIBCompliancesClockInfo, PtpClockPortState=PtpClockPortState, ptpClockCurrentDSInstanceIndex=ptpClockCurrentDSInstanceIndex, ptpEncapsulationTypePWEthernetLSP=ptpEncapsulationTypePWEthernetLSP, ptpClockParentDSGMClockIdentity=ptpClockParentDSGMClockIdentity, ptpClockTimePropertiesDSCurrentUTCOffsetValid=ptpClockTimePropertiesDSCurrentUTCOffsetValid, PtpClockIntervalBase2=PtpClockIntervalBase2, ptpClockTransDefaultDSClockIdentity=ptpClockTransDefaultDSClockIdentity, ptpClockPortTransDSPeerMeanPathDelay=ptpClockPortTransDSPeerMeanPathDelay, ptpClockPortAssociatePortIndex=ptpClockPortAssociatePortIndex, ptpClockPortRunningRole=ptpClockPortRunningRole, PtpClockQualityClassType=PtpClockQualityClassType, ptpClockPortTransDSTable=ptpClockPortTransDSTable, ptpTransportTypeIPversion4=ptpTransportTypeIPversion4, ptpMIBClockDefaultDSGroup=ptpMIBClockDefaultDSGroup, ptpEncapsulationTypeVLAN=ptpEncapsulationTypeVLAN, ptpMIBObjects=ptpMIBObjects, ptpClockPortDSPeerMeanPathDelay=ptpClockPortDSPeerMeanPathDelay, ptpClockPortAssociateAddressType=ptpClockPortAssociateAddressType, ptpClockPortCurrentPortNumberIndex=ptpClockPortCurrentPortNumberIndex, ptpClockPortNumOfAssociatedPorts=ptpClockPortNumOfAssociatedPorts, ptpClockPortDSName=ptpClockPortDSName, ptpClockTimePropertiesDSDomainIndex=ptpClockTimePropertiesDSDomainIndex, ptpMIBSystemInfoGroup=ptpMIBSystemInfoGroup, ptpClockPortDSDelayMech=ptpClockPortDSDelayMech, ptpClockPortTablePortNumberIndex=ptpClockPortTablePortNumberIndex, ptpClockCurrentDSEntry=ptpClockCurrentDSEntry, ptpSystemDomainClockTypeIndex=ptpSystemDomainClockTypeIndex, ptpClockPortAssociateEntry=ptpClockPortAssociateEntry, PtpClockProfileType=PtpClockProfileType, ptpClockTransDefaultDSDomainIndex=ptpClockTransDefaultDSDomainIndex, ptpClockRunningClockTypeIndex=ptpClockRunningClockTypeIndex, ptpClockPortDSClockInstanceIndex=ptpClockPortDSClockInstanceIndex, ptpClockPortAssociatePacketsReceived=ptpClockPortAssociatePacketsReceived, ptpClockTimePropertiesDSSource=ptpClockTimePropertiesDSSource, ptpClockTimePropertiesDSLeap59=ptpClockTimePropertiesDSLeap59, ptpClockPortCurrentDomainIndex=ptpClockPortCurrentDomainIndex, ptpClockTransDefaultDSEntry=ptpClockTransDefaultDSEntry, ptpClockParentDSClockPhChRate=ptpClockParentDSClockPhChRate, ptpTransportTypeEthernet=ptpTransportTypeEthernet, ptpClockPortDSGrantDuration=ptpClockPortDSGrantDuration, ptpClockPortRunningName=ptpClockPortRunningName, ptpClockTimePropertiesDSClockTypeIndex=ptpClockTimePropertiesDSClockTypeIndex, ptpClockPortTransDSFaultyFlag=ptpClockPortTransDSFaultyFlag, PtpClockIdentity=PtpClockIdentity, ptpClockParentDSGMClockQualityAccuracy=ptpClockParentDSGMClockQualityAccuracy, ptpSystemEntry=ptpSystemEntry, ptpClockTransDefaultDSInstanceIndex=ptpClockTransDefaultDSInstanceIndex, ptpClockPortAssociateAddress=ptpClockPortAssociateAddress, ptpClockPortDSPTPVersion=ptpClockPortDSPTPVersion, ptpClockTimePropertiesDSLeap61=ptpClockTimePropertiesDSLeap61, ptpClockTransDefaultDSPrimaryDomain=ptpClockTransDefaultDSPrimaryDomain, ptpClockPortDSTable=ptpClockPortDSTable, PtpClockPortTransportTypeAddress=PtpClockPortTransportTypeAddress, ptpClockPortDomainIndex=ptpClockPortDomainIndex, ptpClockTransDefaultDSDelay=ptpClockTransDefaultDSDelay, ptpClockPortRunningDomainIndex=ptpClockPortRunningDomainIndex, ptpTransportTypeControlNET=ptpTransportTypeControlNET, ptpClockPortDSEntry=ptpClockPortDSEntry, ptpClockPortTable=ptpClockPortTable, ptpClockDefaultDSQualityOffset=ptpClockDefaultDSQualityOffset, ptpClockTimePropertiesDSEntry=ptpClockTimePropertiesDSEntry, ptpClockPortClockTypeIndex=ptpClockPortClockTypeIndex, ptpWellKnownTransportTypes=ptpWellKnownTransportTypes, ptpClockPortDSAnnounceRctTimeout=ptpClockPortDSAnnounceRctTimeout, PtpClockType=PtpClockType, ptpClockPortRunningClockInstanceIndex=ptpClockPortRunningClockInstanceIndex, ptpClockPortRole=ptpClockPortRole, ptpClockCurrentDSClockTypeIndex=ptpClockCurrentDSClockTypeIndex, ptpClockPortRunningPortNumberIndex=ptpClockPortRunningPortNumberIndex, ptpMIBClockPortAssociateGroup=ptpMIBClockPortAssociateGroup, ptpClockRunningPacketsReceived=ptpClockRunningPacketsReceived, PtpClockDomainType=PtpClockDomainType, ptpMIBClockTimepropertiesGroup=ptpMIBClockTimepropertiesGroup, ptpClockPortTransDSEntry=ptpClockPortTransDSEntry, ptpClockPortDSPortNumberIndex=ptpClockPortDSPortNumberIndex, ptpClockPortRunningTxMode=ptpClockPortRunningTxMode, ptpClockPortTransDSlogMinPdelayReqInt=ptpClockPortTransDSlogMinPdelayReqInt, ptpClockPortTransDSPortNumberIndex=ptpClockPortTransDSPortNumberIndex, ptpClockParentDSGMClockPriority2=ptpClockParentDSGMClockPriority2, ptpClockRunningTable=ptpClockRunningTable, ptpClockPortDSMinDelayReqInterval=ptpClockPortDSMinDelayReqInterval, ptpMIBCompliances=ptpMIBCompliances, ptpClockParentDSClockTypeIndex=ptpClockParentDSClockTypeIndex, ptpClockPortTransDSDomainIndex=ptpClockPortTransDSDomainIndex, ptpEncapsulationTypeEthernet=ptpEncapsulationTypeEthernet, ptpTransportTypeIPversion6=ptpTransportTypeIPversion6, PtpClockRoleType=PtpClockRoleType, ptpMIBGroups=ptpMIBGroups, ptpClockCurrentDSStepsRemoved=ptpClockCurrentDSStepsRemoved, ptpMIBClockPortTransDSGroup=ptpMIBClockPortTransDSGroup, ptpClockPortDSlogSyncInterval=ptpClockPortDSlogSyncInterval)
