#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ETHERLIKE-EXT-MIB
# Source digest sha256:5306c99a91e5840090e1c12acf7012b4ebbc25345aa412a2e6aef34c855a244d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dot3StatsIndex, = mibBuilder.importSymbols("EtherLike-MIB", "dot3StatsIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 645))
ciscoEtherExtMIB.setRevisions(('2010-06-04 00:00', '2008-10-15 00:00', '2008-01-09 00:00',))
if mibBuilder.loadTexts: ciscoEtherExtMIB.setLastUpdated('2010-06-04 00:00')
if mibBuilder.loadTexts: ciscoEtherExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEtherExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 0))
ciscoEtherExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1))
ciscoEtherExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2))
ceeDot3PauseExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1))
ceeSubIf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2))
ceeDot3PauseExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceeDot3PauseExtTable.setStatus('current')
ceeDot3PauseExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: ceeDot3PauseExtEntry.setStatus('current')
ceeDot3PauseExtAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("txDesired", 0), ("rxDesired", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceeDot3PauseExtAdminMode.setStatus('current')
ceeDot3PauseExtOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("txDisagree", 0), ("rxDisagree", 1), ("txDesired", 2), ("rxDesired", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceeDot3PauseExtOperMode.setStatus('current')
ceeSubInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceeSubInterfaceTable.setStatus('current')
ceeSubInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ceeSubInterfaceEntry.setStatus('current')
ceeSubInterfaceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('subifs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceeSubInterfaceCount.setStatus('current')
ceeEtherExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1))
ceeEtherExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2))
ceeEtherExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 1)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtPauseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeEtherExtMIBCompliance = ceeEtherExtMIBCompliance.setStatus('deprecated')
ceeEtherExtMIBComplianceR01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 2)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtPauseGroup"), ("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeEtherExtMIBComplianceR01 = ceeEtherExtMIBComplianceR01.setStatus('current')
ciscoEtherExtPauseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 1)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtAdminMode"), ("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherExtPauseGroup = ciscoEtherExtPauseGroup.setStatus('current')
ciscoEtherExtSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 2)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ceeSubInterfaceCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherExtSubIfGroup = ciscoEtherExtSubIfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-MIB", PYSNMP_MODULE_ID=ciscoEtherExtMIB, ceeDot3PauseExt=ceeDot3PauseExt, ceeDot3PauseExtAdminMode=ceeDot3PauseExtAdminMode, ceeDot3PauseExtEntry=ceeDot3PauseExtEntry, ceeDot3PauseExtOperMode=ceeDot3PauseExtOperMode, ceeDot3PauseExtTable=ceeDot3PauseExtTable, ceeEtherExtMIBCompliance=ceeEtherExtMIBCompliance, ceeEtherExtMIBComplianceR01=ceeEtherExtMIBComplianceR01, ceeEtherExtMIBCompliances=ceeEtherExtMIBCompliances, ceeEtherExtMIBGroups=ceeEtherExtMIBGroups, ceeSubIf=ceeSubIf, ceeSubInterfaceCount=ceeSubInterfaceCount, ceeSubInterfaceEntry=ceeSubInterfaceEntry, ceeSubInterfaceTable=ceeSubInterfaceTable, ciscoEtherExtMIB=ciscoEtherExtMIB, ciscoEtherExtMIBConform=ciscoEtherExtMIBConform, ciscoEtherExtMIBNotifs=ciscoEtherExtMIBNotifs, ciscoEtherExtMIBObjects=ciscoEtherExtMIBObjects, ciscoEtherExtPauseGroup=ciscoEtherExtPauseGroup, ciscoEtherExtSubIfGroup=ciscoEtherExtSubIfGroup)
