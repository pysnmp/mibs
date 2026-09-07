#
# PySNMP MIB module CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB
# Source digest sha256:1e9437b07bbab7d1d03d26462936170d84ddc05dd83c4c149dc9629647f52ef8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoWanPersistentXgcpEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 18))
ciscoWanPersistentXgcpEventsMIB.setRevisions(('2003-10-20 00:00',))
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setLastUpdated('2003-10-20 00:00')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanPersistentXgcpEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1))
persistentXgcpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1))
persistentXgcpEventsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: persistentXgcpEventsTable.setStatus('current')
persistentXgcpEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"))
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setStatus('current')
persistentXgcpEventNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: persistentXgcpEventNum.setStatus('current')
persistentXgcpEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventName.setStatus('current')
persistentXgcpEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setStatus('current')
persistentXgcpEventsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2))
persistentXgcpEventsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1))
persistentXgcpEventsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2))
persistentXgcpEventsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBCompliance = persistentXgcpEventsMIBCompliance.setStatus('current')
persistentXgcpEventsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"), ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBGroup = persistentXgcpEventsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", PYSNMP_MODULE_ID=ciscoWanPersistentXgcpEventsMIB, ciscoWanPersistentXgcpEventsMIB=ciscoWanPersistentXgcpEventsMIB, ciscoWanPersistentXgcpEventsMIBObjects=ciscoWanPersistentXgcpEventsMIBObjects, persistentXgcpEventName=persistentXgcpEventName, persistentXgcpEventNum=persistentXgcpEventNum, persistentXgcpEventRowStatus=persistentXgcpEventRowStatus, persistentXgcpEvents=persistentXgcpEvents, persistentXgcpEventsEntry=persistentXgcpEventsEntry, persistentXgcpEventsMIBCompliance=persistentXgcpEventsMIBCompliance, persistentXgcpEventsMIBCompliances=persistentXgcpEventsMIBCompliances, persistentXgcpEventsMIBConformance=persistentXgcpEventsMIBConformance, persistentXgcpEventsMIBGroup=persistentXgcpEventsMIBGroup, persistentXgcpEventsMIBGroups=persistentXgcpEventsMIBGroups, persistentXgcpEventsTable=persistentXgcpEventsTable)
