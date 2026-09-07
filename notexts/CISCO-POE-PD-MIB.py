#
# PySNMP MIB module CISCO-POE-PD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-POE-PD-MIB
# Source digest sha256:eae4d27a3dbe0d1ffd0b60dda69b19d82edd419e5aafea8239ef36e9d3af36c6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPoePdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 414))
ciscoPoePdMIB.setRevisions(('2004-05-05 00:00',))
if mibBuilder.loadTexts: ciscoPoePdMIB.setLastUpdated('2004-05-05 00:00')
if mibBuilder.loadTexts: ciscoPoePdMIB.setOrganization('Cisco Systems Inc.')
cpoePdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 0))
cpoePdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1))
cpoePdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2))
cpoePdInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1))
class CpoePdPowerSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pending", 1), ("acAdaptor", 2), ("thirdParty", 3), ("classic", 4), ("midspan", 5), ("cdpNegotiated", 6), ("highPowerClassic", 7))

cpoePdCurrentPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setStatus('current')
cpoePdCurrentPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 2), CpoePdPowerSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setStatus('current')
cpoePdSupportedPowerLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setStatus('current')
cpoePdSupportedPowerLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-POE-PD-MIB", "cpoePdSupportedPowerLevel"))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setStatus('current')
cpoePdSupportedPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setStatus('current')
cpoePdSupportedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPower.setStatus('current')
cpoePdSupportedPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setStatus('current')
cpoePdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1))
cpoePdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2))
cpoePdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdMIBCompliance = cpoePdMIBCompliance.setStatus('current')
cpoePdInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdCurrentPowerLevel"), ("CISCO-POE-PD-MIB", "cpoePdCurrentPowerSource"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPower"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPowerMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdInformationGroup = cpoePdInformationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-POE-PD-MIB", CpoePdPowerSourceType=CpoePdPowerSourceType, PYSNMP_MODULE_ID=ciscoPoePdMIB, ciscoPoePdMIB=ciscoPoePdMIB, cpoePdCurrentPowerLevel=cpoePdCurrentPowerLevel, cpoePdCurrentPowerSource=cpoePdCurrentPowerSource, cpoePdInformation=cpoePdInformation, cpoePdInformationGroup=cpoePdInformationGroup, cpoePdMIBCompliance=cpoePdMIBCompliance, cpoePdMIBCompliances=cpoePdMIBCompliances, cpoePdMIBConformance=cpoePdMIBConformance, cpoePdMIBGroups=cpoePdMIBGroups, cpoePdMIBNotifications=cpoePdMIBNotifications, cpoePdMIBObjects=cpoePdMIBObjects, cpoePdSupportedPower=cpoePdSupportedPower, cpoePdSupportedPowerLevel=cpoePdSupportedPowerLevel, cpoePdSupportedPowerLevelEntry=cpoePdSupportedPowerLevelEntry, cpoePdSupportedPowerLevelTable=cpoePdSupportedPowerLevelTable, cpoePdSupportedPowerMode=cpoePdSupportedPowerMode)
