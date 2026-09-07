#
# PySNMP MIB module DLINKSW-LED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-LED-MIB
# Source digest sha256:41646266fd88141a4d3b3eb3c10eebac28ba085ae4df097a5925bcbd412a3827
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwLedMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 163))
dlinkSwLedMIB.setRevisions(('2013-09-13 00:00', '2013-09-06 00:00',))
if mibBuilder.loadTexts: dlinkSwLedMIB.setLastUpdated('2013-09-13 00:00')
if mibBuilder.loadTexts: dlinkSwLedMIB.setOrganization('D-Link Corp.')
dLedMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 0))
dLedMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 1))
dLedMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 2))
dLedInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dLedInfoTable.setStatus('current')
dLedInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "DLINKSW-LED-MIB", "dLedBoxId"))
if mibBuilder.loadTexts: dLedInfoEntry.setStatus('current')
dLedBoxId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1, 1), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dLedBoxId.setStatus('current')
dLedSysLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dLedSysLedStatus.setStatus('current')
dLedIfLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 163, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dLedIfLedStatus.setStatus('current')
dLedMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 1))
dLedMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 2))
dLedMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 1, 1)).setObjects(("DLINKSW-LED-MIB", "dLedInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLedMIBCompliance = dLedMIBCompliance.setStatus('current')
dLedInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 163, 2, 2, 1)).setObjects(("DLINKSW-LED-MIB", "dLedSysLedStatus"), ("DLINKSW-LED-MIB", "dLedIfLedStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLedInfoGroup = dLedInfoGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-LED-MIB", PYSNMP_MODULE_ID=dlinkSwLedMIB, dLedBoxId=dLedBoxId, dLedIfLedStatus=dLedIfLedStatus, dLedInfoEntry=dLedInfoEntry, dLedInfoGroup=dLedInfoGroup, dLedInfoTable=dLedInfoTable, dLedMIBCompliance=dLedMIBCompliance, dLedMIBCompliances=dLedMIBCompliances, dLedMIBConformance=dLedMIBConformance, dLedMIBGroups=dLedMIBGroups, dLedMIBNotifications=dLedMIBNotifications, dLedMIBObjects=dLedMIBObjects, dLedSysLedStatus=dLedSysLedStatus, dlinkSwLedMIB=dlinkSwLedMIB)
