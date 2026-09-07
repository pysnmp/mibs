#
# PySNMP MIB module CISCO-MGX82XX-MODULE-RSRC-PART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MGX82XX-MODULE-RSRC-PART-MIB
# Source digest sha256:1f224e485472bdc84edb6bd374d9cf0dbb9af610ab022997a3862c0c3e5ce01d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxModuleRsrcPartMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 73))
ciscoMgx82xxModuleRsrcPartMIB.setRevisions(('2003-04-18 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxModuleRsrcPartMIB.setLastUpdated('2003-04-18 00:00')
if mibBuilder.loadTexts: ciscoMgx82xxModuleRsrcPartMIB.setOrganization('Cisco Systems, Inc.')
cardResourcePartition = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 9))
cardLcnPartitionType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noPartition", 1), ("controllerBased", 2), ("portControllerBased", 3))).clone('noPartition')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardLcnPartitionType.setStatus('current')
cardResPartGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cardResPartGrpTable.setStatus('current')
cardResPartGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"))
if mibBuilder.loadTexts: cardResPartGrpEntry.setStatus('current')
cardResPartCtrlrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("par", 1), ("pnni", 2), ("tag", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardResPartCtrlrNum.setStatus('current')
cardResPartRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardResPartRowStatus.setStatus('current')
cardResPartNumOfLcnAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardResPartNumOfLcnAvail.setStatus('current')
cmmRsrcPartMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2))
cmmRsrcPartMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1))
cmmRsrcPartMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2))
cmmRsrcPartCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1, 1)).setObjects(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cmmRsrcPartGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmRsrcPartCompliance = cmmRsrcPartCompliance.setStatus('current')
cmmRsrcPartGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2, 1)).setObjects(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardLcnPartitionType"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartRowStatus"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartNumOfLcnAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmRsrcPartGroup = cmmRsrcPartGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", PYSNMP_MODULE_ID=ciscoMgx82xxModuleRsrcPartMIB, cardLcnPartitionType=cardLcnPartitionType, cardResPartCtrlrNum=cardResPartCtrlrNum, cardResPartGrpEntry=cardResPartGrpEntry, cardResPartGrpTable=cardResPartGrpTable, cardResPartNumOfLcnAvail=cardResPartNumOfLcnAvail, cardResPartRowStatus=cardResPartRowStatus, cardResourcePartition=cardResourcePartition, ciscoMgx82xxModuleRsrcPartMIB=ciscoMgx82xxModuleRsrcPartMIB, cmmRsrcPartCompliance=cmmRsrcPartCompliance, cmmRsrcPartGroup=cmmRsrcPartGroup, cmmRsrcPartMIBCompliances=cmmRsrcPartMIBCompliances, cmmRsrcPartMIBConformance=cmmRsrcPartMIBConformance, cmmRsrcPartMIBGroups=cmmRsrcPartMIBGroups)
