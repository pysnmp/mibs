#
# PySNMP MIB module CISCO-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MRP-MIB
# Source digest sha256:1c8cc63e96b261f7e5daf0b8603b84eb42238dd8985f1e6e9a31564053ce5981
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 850))
ciscoMrpMIB.setRevisions(('2017-09-12 00:00',))
if mibBuilder.loadTexts: ciscoMrpMIB.setLastUpdated('2017-09-12 00:00')
if mibBuilder.loadTexts: ciscoMrpMIB.setOrganization('Cisco Systems, Inc.')
ciscoMrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 0))
ciscoMrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 1))
ciscoMrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2))
ciscoMrpDomainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoMrpDomainTable.setStatus('current')
ciscoMrpDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-MRP-MIB", "ciscoMrpDomainIndex"))
if mibBuilder.loadTexts: ciscoMrpDomainEntry.setStatus('current')
ciscoMrpDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoMrpDomainIndex.setStatus('current')
ciscoMrpDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainID.setStatus('current')
ciscoMrpDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainName.setStatus('current')
ciscoMrpDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainState.setStatus('current')
ciscoMrpRingOpen = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 850, 0, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpDomainID"), ("CISCO-MRP-MIB", "ciscoMrpDomainName"), ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
if mibBuilder.loadTexts: ciscoMrpRingOpen.setStatus('current')
ciscoMrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1))
ciscoMrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2))
ciscoMrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpMIBMainObjectGroup"), ("CISCO-MRP-MIB", "ciscoMrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBCompliance = ciscoMrpMIBCompliance.setStatus('current')
ciscoMrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpDomainID"), ("CISCO-MRP-MIB", "ciscoMrpDomainName"), ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBMainObjectGroup = ciscoMrpMIBMainObjectGroup.setStatus('current')
ciscoMrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 2)).setObjects(("CISCO-MRP-MIB", "ciscoMrpRingOpen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBNotificationGroup = ciscoMrpMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MRP-MIB", PYSNMP_MODULE_ID=ciscoMrpMIB, ciscoMrpDomainEntry=ciscoMrpDomainEntry, ciscoMrpDomainID=ciscoMrpDomainID, ciscoMrpDomainIndex=ciscoMrpDomainIndex, ciscoMrpDomainName=ciscoMrpDomainName, ciscoMrpDomainState=ciscoMrpDomainState, ciscoMrpDomainTable=ciscoMrpDomainTable, ciscoMrpMIB=ciscoMrpMIB, ciscoMrpMIBCompliance=ciscoMrpMIBCompliance, ciscoMrpMIBCompliances=ciscoMrpMIBCompliances, ciscoMrpMIBConform=ciscoMrpMIBConform, ciscoMrpMIBGroups=ciscoMrpMIBGroups, ciscoMrpMIBMainObjectGroup=ciscoMrpMIBMainObjectGroup, ciscoMrpMIBNotificationGroup=ciscoMrpMIBNotificationGroup, ciscoMrpMIBNotifs=ciscoMrpMIBNotifs, ciscoMrpMIBObjects=ciscoMrpMIBObjects, ciscoMrpRingOpen=ciscoMrpRingOpen)
