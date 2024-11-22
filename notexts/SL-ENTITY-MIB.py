#
# PySNMP MIB module SL-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ENTITY-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:46:59 2024
# On host fv-az1437-189 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, mib_2, ModuleIdentity, Counter64, Gauge32, Unsigned32, iso, Counter32, IpAddress, ObjectIdentity, NotificationType, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "mib-2", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "iso", "Counter32", "IpAddress", "ObjectIdentity", "NotificationType", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, AutonomousType, DisplayString, TAddress, TimeStamp, RowStatus, TextualConvention, PhysAddress, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "AutonomousType", "DisplayString", "TAddress", "TimeStamp", "RowStatus", "TextualConvention", "PhysAddress", "TDomain")
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
mibBuilder.exportSymbols("SL-ENTITY-MIB", slEntPhysicalCleiCode=slEntPhysicalCleiCode, slEntPhysicalAdminStatus=slEntPhysicalAdminStatus, slEntPhysicalHardwareRev=slEntPhysicalHardwareRev, slEntPhysicalDescr=slEntPhysicalDescr, slEntPhysicalOperStatus=slEntPhysicalOperStatus, slEntPhysicalSysSubType=slEntPhysicalSysSubType, slEntityPhysical=slEntityPhysical, PhysicalType=PhysicalType, slEntPhysicalSysAlias=slEntPhysicalSysAlias, PYSNMP_MODULE_ID=slmEntity, slEntPhysicalOemSerialNum=slEntPhysicalOemSerialNum, slEntPhysicalPartNumber=slEntPhysicalPartNumber, slEntPhysicalSysTemp=slEntPhysicalSysTemp, slEntPhysicalSysUptime=slEntPhysicalSysUptime, slmEntity=slmEntity, slEntPhysicalSoftwareRev=slEntPhysicalSoftwareRev, slEntityNotification=slEntityNotification, CleiCode=CleiCode, slEntPhysicalClass=slEntPhysicalClass, slEntPhysicalSerialNum=slEntPhysicalSerialNum, slEntPhysicalIndex=slEntPhysicalIndex, PhysicalClass=PhysicalClass, slEntPhysicalTable=slEntPhysicalTable, slEntPhysicalProtectionEntity=slEntPhysicalProtectionEntity, PhysicalIndex=PhysicalIndex, slEntPhysicalProductionDate=slEntPhysicalProductionDate, slEntPhysicalEntry=slEntPhysicalEntry, slEntPhysicalProtectState=slEntPhysicalProtectState, slEntPhysicalFailureDescription=slEntPhysicalFailureDescription, slEntPhysicalProtectMode=slEntPhysicalProtectMode, slEntPhysicalFirmwareRev=slEntPhysicalFirmwareRev, slEntPhysicalStatus=slEntPhysicalStatus, slEntPhysicalType=slEntPhysicalType)
