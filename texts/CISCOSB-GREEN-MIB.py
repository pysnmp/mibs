#
# PySNMP MIB module CISCOSB-GREEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-GREEN-MIB
# Source digest sha256:985c4229e7fced3b6ce63bc429edfa2daabc73ee48f5fba7999a64998cc7c4de
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlGreenEth = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134))
rlGreenEth.setRevisions(('2008-08-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlGreenEth.setRevisionsDescriptions(('Add Green Ethernet Energy Detect and Short Reach support per port and per system rlGreenEthernet',))
if mibBuilder.loadTexts: rlGreenEth.setLastUpdated('2008-08-15 00:00')
if mibBuilder.loadTexts: rlGreenEth.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlGreenEth.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlGreenEth.setDescription('The private MIB module definition for Green Ethernet Energy Detect feature.')
rlGreenEthEnergyDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setDescription('This scalar defines Green Ethernet Enrgy-Detect Globaly')
rlGreenEthShortReachEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setDescription('This scalar defines Green Ethernet Short-Reach Globaly')
rlGreenEthCurrentEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 3), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setDescription('This scalar define Green Ethernet all modes current Energy consumption per system in mWatt\n         in order to calculate current energy consumption in percent proportional to Consumption without Green Ethernet feature\n         please use the following formula:\n         (rlGreenEthCurrentEnergyConsumption/rlGreenEthCurrentMaxEnergyConsumption)*100')
rlGreenEthCurrentMaxEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 4), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setDescription('This scalar define Green Ethernet current maximum consumption Energy consumption per system in mWatt,\n         as it was without Green Ethernet feature.')
rlGreenEthCumulativePowerSaveMeter = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 5), Unsigned32()).setUnits('Watt*Hour').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setDescription('This scalar define Green Ethernet cumulative power save per system in Watt*Hour')
rlGreenEthShortReachThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 70))).setUnits('meter').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setDescription('The usage threshold expressed in meter for\n                determinate the cable length for Short-Reach')
rlGreenEthCumulativePowerSaveMeterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setDescription("The rlGreenEthCumulativePowerSaveMeterReset indicates that rlGreenEthCumulativePowerSaveMeter\n            should be set to ziro.\n\n            This object behaviors as write-only than\n            reading this object will always return 'false'.")
class RlGreenSavingType(TextualConvention, Integer32):
    description = 'Green saving types:\n         energyDetect(1)  uses energy detect\n         shortReach(2)  uses Short Reach'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("energyDetect", 1), ("shortReach", 2))

class NonOperReasonType(TextualConvention, Integer32):
    description = 'Reason why Green Ethernet is not activated saving on a port\n         NP(1)                  Port is not present - Applicable in ED & SR\n         LT(2)                  Link Type is not supported(fiber, auto media setect) - Applicable in ED & SR\n         LU(3)                  Port link is up - Applicable only in ED\n         LS(4)                  Link speed is not supported (100M,10M,10G) - Applicable only in SR\n         LL(5)                  Link length received from VCT test exceed threshold - Applicable only in SR\n         ER(6)                  Errors detected on line and port revered back to Long Reach(only in enhanced mode) - Applicable only in SR\n         LD(7)                  Port link is Down - Applicable only in SR\n         unknown(8)             In case that green Active or disable on port'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("np", 1), ("lt", 2), ("lu", 3), ("ls", 4), ("ll", 5), ("er", 6), ("ld", 7), ("unknown", 8))

class CableLengthRange(TextualConvention, Integer32):
    description = 'cable length calculated when link is up\n\t\tRelevant only for SR'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("lengthUnknown", 0), ("lengthLessThan50M", 1), ("length50MTo80M", 2), ("length80MTo110M", 3), ("length110MTo140M", 4), ("lengthMoreThan140M", 5))

rlGreenEthPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlGreenEthPortTable.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortTable.setDescription('A table of green state of ports')
rlGreenEthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCOSB-GREEN-MIB", "rlGreenEthPortSavingTypeValue"))
if mibBuilder.loadTexts: rlGreenEthPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortEntry.setDescription('An entry of green state of port')
rlGreenEthPortSavingTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 1), RlGreenSavingType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setDescription('Green saving types')
rlGreenEthPortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setDescription('Active\\non Active')
rlGreenEthPortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortOperState.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortOperState.setDescription('Active\\non Active')
rlGreenEthPortNonOperReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 4), NonOperReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setDescription('Reason why saving mode is not activated')
rlGreenEthPortCableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 5), CableLengthRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortCableLength.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortCableLength.setDescription('cable length calculated when link is up')
rlGreenEthForceShortReachIfIndexList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 9), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setDescription('The ports that forced enable the Green Ethernet Short Reach configuration\n          not considering VCT results.')
rlGreenEthMaskLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthMaskLedStatus.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthMaskLedStatus.setDescription('Mask all ports led  according to the configuration.')
mibBuilder.exportSymbols("CISCOSB-GREEN-MIB", CableLengthRange=CableLengthRange, NonOperReasonType=NonOperReasonType, PYSNMP_MODULE_ID=rlGreenEth, RlGreenSavingType=RlGreenSavingType, rlGreenEth=rlGreenEth, rlGreenEthCumulativePowerSaveMeter=rlGreenEthCumulativePowerSaveMeter, rlGreenEthCumulativePowerSaveMeterReset=rlGreenEthCumulativePowerSaveMeterReset, rlGreenEthCurrentEnergyConsumption=rlGreenEthCurrentEnergyConsumption, rlGreenEthCurrentMaxEnergyConsumption=rlGreenEthCurrentMaxEnergyConsumption, rlGreenEthEnergyDetectEnable=rlGreenEthEnergyDetectEnable, rlGreenEthForceShortReachIfIndexList=rlGreenEthForceShortReachIfIndexList, rlGreenEthMaskLedStatus=rlGreenEthMaskLedStatus, rlGreenEthPortAdminState=rlGreenEthPortAdminState, rlGreenEthPortCableLength=rlGreenEthPortCableLength, rlGreenEthPortEntry=rlGreenEthPortEntry, rlGreenEthPortNonOperReason=rlGreenEthPortNonOperReason, rlGreenEthPortOperState=rlGreenEthPortOperState, rlGreenEthPortSavingTypeValue=rlGreenEthPortSavingTypeValue, rlGreenEthPortTable=rlGreenEthPortTable, rlGreenEthShortReachEnable=rlGreenEthShortReachEnable, rlGreenEthShortReachThreshold=rlGreenEthShortReachThreshold)
