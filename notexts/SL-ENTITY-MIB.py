#
# PySNMP MIB module SL-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ENTITY-MIB
# Produced by pysmi-1.1.12 at Wed May 29 07:26:27 2024
# On host fv-az2021-913 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, mib_2, Integer32, IpAddress, MibIdentifier, Counter64, iso, Unsigned32, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "mib-2", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "iso", "Unsigned32", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Bits")
TruthValue, PhysAddress, TimeStamp, DisplayString, AutonomousType, TAddress, TextualConvention, RowStatus, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "PhysAddress", "TimeStamp", "DisplayString", "AutonomousType", "TAddress", "TextualConvention", "RowStatus", "TDomain")
slmEntity = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6))
if mibBuilder.loadTexts: slmEntity.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slmEntity.setOrganization('PacketLight Networks Ltd.')
class PhysicalIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11))

class PhysicalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 14, 15, 16, 21, 100))
    namedValues = NamedValues(("powerModule", 1), ("fanModule", 2), ("switchModule", 3), ("edfaModule", 14), ("ocmModule", 15), ("otdrModule", 16), ("lc400G", 21), ("unknown", 100))

class CleiCode(DisplayString):
    reference = 'GR-383-CORE'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

slEntityPhysical = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1))
slEntityNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 2))
slEntPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1), )
if mibBuilder.loadTexts: slEntPhysicalTable.setStatus('current')
slEntPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1), ).setIndexNames((0, "SL-ENTITY-MIB", "slEntPhysicalIndex"))
if mibBuilder.loadTexts: slEntPhysicalEntry.setStatus('current')
slEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalIndex.setStatus('current')
slEntPhysicalDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalDescr.setStatus('current')
slEntPhysicalClass = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 3), PhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalClass.setStatus('current')
slEntPhysicalHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalHardwareRev.setStatus('current')
slEntPhysicalFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalFirmwareRev.setStatus('current')
slEntPhysicalSoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSoftwareRev.setStatus('current')
slEntPhysicalSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSerialNum.setStatus('current')
slEntPhysicalProtectionEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 8), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalProtectionEntity.setStatus('current')
slEntPhysicalProtectState = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protecting", 2), ("noProtection", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalProtectState.setStatus('current')
slEntPhysicalProtectMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lock", 1), ("force", 2), ("automatic", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalProtectMode.setStatus('current')
slEntPhysicalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalStatus.setStatus('current')
slEntPhysicalFailureDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalFailureDescription.setStatus('current')
slEntPhysicalAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("warmBoot", 4), ("coldBoot", 5), ("hotBoot", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalAdminStatus.setStatus('current')
slEntPhysicalOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("notPresent", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalOperStatus.setStatus('current')
slEntPhysicalSysUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 19), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSysUptime.setStatus('current')
slEntPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 20), PhysicalType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalType.setStatus('current')
slEntPhysicalCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 21), CleiCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalCleiCode.setStatus('current')
slEntPhysicalPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 22), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalPartNumber.setStatus('current')
slEntPhysicalOemSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 23), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalOemSerialNum.setStatus('current')
slEntPhysicalProductionDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 24), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalProductionDate.setStatus('current')
slEntPhysicalSysTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSysTemp.setStatus('current')
slEntPhysicalSysAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 26), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalSysAlias.setStatus('current')
slEntPhysicalSysSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSysSubType.setStatus('current')
mibBuilder.exportSymbols("SL-ENTITY-MIB", slEntPhysicalSerialNum=slEntPhysicalSerialNum, slEntPhysicalProtectionEntity=slEntPhysicalProtectionEntity, slEntPhysicalSysUptime=slEntPhysicalSysUptime, PhysicalType=PhysicalType, slEntPhysicalHardwareRev=slEntPhysicalHardwareRev, slEntPhysicalClass=slEntPhysicalClass, CleiCode=CleiCode, slEntPhysicalDescr=slEntPhysicalDescr, slEntPhysicalSysAlias=slEntPhysicalSysAlias, slmEntity=slmEntity, slEntPhysicalOperStatus=slEntPhysicalOperStatus, slEntPhysicalOemSerialNum=slEntPhysicalOemSerialNum, PhysicalClass=PhysicalClass, slEntPhysicalProtectState=slEntPhysicalProtectState, slEntPhysicalFailureDescription=slEntPhysicalFailureDescription, slEntPhysicalType=slEntPhysicalType, slEntPhysicalSysTemp=slEntPhysicalSysTemp, slEntPhysicalAdminStatus=slEntPhysicalAdminStatus, slEntPhysicalStatus=slEntPhysicalStatus, slEntPhysicalSoftwareRev=slEntPhysicalSoftwareRev, slEntPhysicalProductionDate=slEntPhysicalProductionDate, slEntityNotification=slEntityNotification, slEntPhysicalProtectMode=slEntPhysicalProtectMode, slEntPhysicalCleiCode=slEntPhysicalCleiCode, PhysicalIndex=PhysicalIndex, slEntPhysicalPartNumber=slEntPhysicalPartNumber, slEntPhysicalSysSubType=slEntPhysicalSysSubType, PYSNMP_MODULE_ID=slmEntity, slEntPhysicalIndex=slEntPhysicalIndex, slEntPhysicalFirmwareRev=slEntPhysicalFirmwareRev, slEntityPhysical=slEntityPhysical, slEntPhysicalEntry=slEntPhysicalEntry, slEntPhysicalTable=slEntPhysicalTable)
