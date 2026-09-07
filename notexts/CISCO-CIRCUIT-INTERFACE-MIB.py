#
# PySNMP MIB module CISCO-CIRCUIT-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CIRCUIT-INTERFACE-MIB
# Source digest sha256:56a72f4ae06494b3871056a772d823dd9a946ef17636f9ebcd00bb3eb7567316
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoCircuitInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 160))
ciscoCircuitInterfaceMIB.setRevisions(('2000-05-09 00:00',))
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setLastUpdated('2000-05-09 00:00')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setOrganization('Cisco Systems, Inc.')
ciscoCircuitInterfaceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1))
cciDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1))
cciDescriptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cciDescriptionTable.setStatus('current')
cciDescriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cciDescriptionEntry.setStatus('current')
cciDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciDescr.setStatus('current')
cciStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciStatus.setStatus('current')
ciscoCircuitInterfaceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3))
ciscoCircuitInterfaceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1))
ciscoCircuitInterfaceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2))
ciscoCircuitInterfaceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "ciscoCircuitInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceMIBCompliance = ciscoCircuitInterfaceMIBCompliance.setStatus('current')
ciscoCircuitInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "cciDescr"), ("CISCO-CIRCUIT-INTERFACE-MIB", "cciStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceGroup = ciscoCircuitInterfaceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CIRCUIT-INTERFACE-MIB", PYSNMP_MODULE_ID=ciscoCircuitInterfaceMIB, cciDescr=cciDescr, cciDescription=cciDescription, cciDescriptionEntry=cciDescriptionEntry, cciDescriptionTable=cciDescriptionTable, cciStatus=cciStatus, ciscoCircuitInterfaceGroup=ciscoCircuitInterfaceGroup, ciscoCircuitInterfaceMIB=ciscoCircuitInterfaceMIB, ciscoCircuitInterfaceMIBCompliance=ciscoCircuitInterfaceMIBCompliance, ciscoCircuitInterfaceMIBCompliances=ciscoCircuitInterfaceMIBCompliances, ciscoCircuitInterfaceMIBConformance=ciscoCircuitInterfaceMIBConformance, ciscoCircuitInterfaceMIBGroups=ciscoCircuitInterfaceMIBGroups, ciscoCircuitInterfaceMIBObjects=ciscoCircuitInterfaceMIBObjects)
