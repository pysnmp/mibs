#
# PySNMP MIB module CISCO-INTERFACETOPN-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-INTERFACETOPN-EXT-MIB
# Source digest sha256:855986b86f130ac5a78fe5507a55fd705b14c61d3df7b9acf682383af16d6726
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
interfaceTopNControlEntry, = mibBuilder.importSymbols("INTERFACETOPN-MIB", "interfaceTopNControlEntry")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoInterfaceTopNExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 482))
ciscoInterfaceTopNExtMIB.setRevisions(('2010-10-19 00:00', '2008-01-15 00:00', '2006-03-15 00:00',))
if mibBuilder.loadTexts: ciscoInterfaceTopNExtMIB.setLastUpdated('2010-10-19 00:00')
if mibBuilder.loadTexts: ciscoInterfaceTopNExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoInterfaceTopNExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 0))
ciscoInterfaceTopNExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 1))
ciscoInterfaceTopNExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 2))
citneInterfaceTopNCaps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 1), Bits().clone(namedValues=NamedValues(("utilization", 0), ("bytes", 1), ("packets", 2), ("broadcast", 3), ("multicast", 4), ("overflow", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: citneInterfaceTopNCaps.setStatus('current')
citneInterfaceTopNControlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: citneInterfaceTopNControlTable.setStatus('current')
citneInterfaceTopNControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1), ).setMaxAccess("notaccessible")
interfaceTopNControlEntry.registerAugmentions(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNControlEntry"))
citneInterfaceTopNControlEntry.setIndexNames(*interfaceTopNControlEntry.getIndexNames())
if mibBuilder.loadTexts: citneInterfaceTopNControlEntry.setStatus('current')
citneInterfaceTopNCounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("utilization", 2), ("bytes", 3), ("packets", 4), ("broadcast", 5), ("multicast", 6), ("overflow", 7))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citneInterfaceTopNCounterType.setStatus('current')
citneInterfaceTopNInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("all", 1), ("ethernet", 2), ("fastEthernet", 3), ("gigaEthernet", 4), ("tenGigaEthernet", 5), ("portChannel", 6), ("layer2", 7), ("layer3", 8), ("fortyGigaEthernet", 9))).clone('all')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citneInterfaceTopNInterfaceType.setStatus('current')
citneInterfaceTopNVlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 3), VlanIndex().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citneInterfaceTopNVlanNumber.setStatus('current')
ciscoIfTopNExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1))
ciscoIfTopNExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2))
ciscoIfTopNExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1, 1)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtCapsGroup"), ("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtControlGroup"), ("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtCtrlVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtMIBCompliance = ciscoIfTopNExtMIBCompliance.setStatus('current')
ciscoIfTopNExtCapsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 1)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCaps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtCapsGroup = ciscoIfTopNExtCapsGroup.setStatus('current')
ciscoIfTopNExtControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 2)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCounterType"), ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNInterfaceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtControlGroup = ciscoIfTopNExtControlGroup.setStatus('current')
ciscoIfTopNExtCtrlVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 3)).setObjects(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNVlanNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfTopNExtCtrlVlanGroup = ciscoIfTopNExtCtrlVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-EXT-MIB", PYSNMP_MODULE_ID=ciscoInterfaceTopNExtMIB, ciscoIfTopNExtCapsGroup=ciscoIfTopNExtCapsGroup, ciscoIfTopNExtControlGroup=ciscoIfTopNExtControlGroup, ciscoIfTopNExtCtrlVlanGroup=ciscoIfTopNExtCtrlVlanGroup, ciscoIfTopNExtMIBCompliance=ciscoIfTopNExtMIBCompliance, ciscoIfTopNExtMIBCompliances=ciscoIfTopNExtMIBCompliances, ciscoIfTopNExtMIBGroups=ciscoIfTopNExtMIBGroups, ciscoInterfaceTopNExtMIB=ciscoInterfaceTopNExtMIB, ciscoInterfaceTopNExtMIBConform=ciscoInterfaceTopNExtMIBConform, ciscoInterfaceTopNExtMIBNotifs=ciscoInterfaceTopNExtMIBNotifs, ciscoInterfaceTopNExtMIBObjects=ciscoInterfaceTopNExtMIBObjects, citneInterfaceTopNCaps=citneInterfaceTopNCaps, citneInterfaceTopNControlEntry=citneInterfaceTopNControlEntry, citneInterfaceTopNControlTable=citneInterfaceTopNControlTable, citneInterfaceTopNCounterType=citneInterfaceTopNCounterType, citneInterfaceTopNInterfaceType=citneInterfaceTopNInterfaceType, citneInterfaceTopNVlanNumber=citneInterfaceTopNVlanNumber)
