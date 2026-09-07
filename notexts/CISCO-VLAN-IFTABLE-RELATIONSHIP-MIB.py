#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB
# Source digest sha256:077d2871498cdb8456e942d5ce1ebc33921709faa67fd2f64ab5e816b83824e8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelationshipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 128))
ciscoVlanIfTableRelationshipMIB.setRevisions(('2013-07-15 00:00',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setLastUpdated('1999-04-01 05:30')
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setOrganization('Cisco Systems, Inc.')
cviMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1))
cviGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1))
cviVlanInterfaceIndexTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cviVlanInterfaceIndexTable.setStatus('current')
cviVlanInterfaceIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviVlanId"), (0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviPhysicalIfIndex"))
if mibBuilder.loadTexts: cviVlanInterfaceIndexEntry.setStatus('current')
cviVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 1), VlanIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cviVlanId.setStatus('current')
cviPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cviPhysicalIfIndex.setStatus('current')
cviRoutedVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cviRoutedVlanIfIndex.setStatus('current')
cviMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3))
cviMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1))
cviMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2))
cviMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBCompliance = cviMIBCompliance.setStatus('current')
cviMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviRoutedVlanIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBGroup = cviMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", PYSNMP_MODULE_ID=ciscoVlanIfTableRelationshipMIB, ciscoVlanIfTableRelationshipMIB=ciscoVlanIfTableRelationshipMIB, cviGlobals=cviGlobals, cviMIBCompliance=cviMIBCompliance, cviMIBCompliances=cviMIBCompliances, cviMIBConformance=cviMIBConformance, cviMIBGroup=cviMIBGroup, cviMIBGroups=cviMIBGroups, cviMIBObjects=cviMIBObjects, cviPhysicalIfIndex=cviPhysicalIfIndex, cviRoutedVlanIfIndex=cviRoutedVlanIfIndex, cviVlanId=cviVlanId, cviVlanInterfaceIndexEntry=cviVlanInterfaceIndexEntry, cviVlanInterfaceIndexTable=cviVlanInterfaceIndexTable)
