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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setRevisionsDescriptions(('Update descriptions in the MIB.\n                ',))
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setLastUpdated('2003-10-20 00:00')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setContactInfo('       Cisco Systems\n                    Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setDescription('The MIB module for managing CA(Call Agent) events.\n            ')
ciscoWanPersistentXgcpEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1))
persistentXgcpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1))
persistentXgcpEventsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: persistentXgcpEventsTable.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsTable.setDescription('The persistentXgcpEventsTable contains\n            configuration information about xGCP events\n            which involve a persistent notification request.\n           ')
persistentXgcpEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"))
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setDescription("An entry in the persistentXgcpEventsTable. Each\n         entry consists of persistentXgcpEventNum - Index\n         to the persistentXgcpEventsTable. \n\n         persistentXgcpEventName - Name of the xGCP\n         event that needs persistent notification\n         to the call agent for example 't/hd'.\n\n         persistentXgcpEventRowStatus -This indicates\n         whether an xGCP event is added in this entry\n         or not.\n\n         This table is not created implicitly. The user\n         can add xGCP event or delete an xGCP event.\n        ")
persistentXgcpEventNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: persistentXgcpEventNum.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventNum.setDescription('This object is a index to persistentXgcpEventsTable.\n        ')
persistentXgcpEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventName.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventName.setDescription("This object holds the name of the event\n         for example 't/hd' or 't/hu'.\n        ")
persistentXgcpEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setDescription("This object allows to add or delete an entry. \n            Modifying an entry is not allowed.\n\n            An entry may be created using the 'createAndGo' option.\n            When the row is successfully created, the RowStatus would\n            be set to 'active' by the agent. An entry may be deleted\n            by setting the RowStatus to 'destroy'. Other options\n            such as `CreateAndWait', 'notInService', 'notReady' will\n            not be used.\n\n            For creating an entry the persistentXgcpEventNum and \n            persistentXgcpEventName must be provided.\n  \n            This object tells call control whether or not a particular \n            xGCP event is added or not, based on this the call control \n            module will decide  whether or not to notify (NTFY) call \n            agent when a particular xGCP event is received,\n            without waiting for CA to request for that event.\n           ")
persistentXgcpEventsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2))
persistentXgcpEventsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1))
persistentXgcpEventsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2))
persistentXgcpEventsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBCompliance = persistentXgcpEventsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsMIBCompliance.setDescription(' The complaince statement for persistent Xgcp events\n              which implement persistentXgcpEvents MIB.')
persistentXgcpEventsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"), ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBGroup = persistentXgcpEventsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsMIBGroup.setDescription('This group contains objects related to\n             configuration of persistent xGCP events.\n            ')
mibBuilder.exportSymbols("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", PYSNMP_MODULE_ID=ciscoWanPersistentXgcpEventsMIB, ciscoWanPersistentXgcpEventsMIB=ciscoWanPersistentXgcpEventsMIB, ciscoWanPersistentXgcpEventsMIBObjects=ciscoWanPersistentXgcpEventsMIBObjects, persistentXgcpEventName=persistentXgcpEventName, persistentXgcpEventNum=persistentXgcpEventNum, persistentXgcpEventRowStatus=persistentXgcpEventRowStatus, persistentXgcpEvents=persistentXgcpEvents, persistentXgcpEventsEntry=persistentXgcpEventsEntry, persistentXgcpEventsMIBCompliance=persistentXgcpEventsMIBCompliance, persistentXgcpEventsMIBCompliances=persistentXgcpEventsMIBCompliances, persistentXgcpEventsMIBConformance=persistentXgcpEventsMIBConformance, persistentXgcpEventsMIBGroup=persistentXgcpEventsMIBGroup, persistentXgcpEventsMIBGroups=persistentXgcpEventsMIBGroups, persistentXgcpEventsTable=persistentXgcpEventsTable)
