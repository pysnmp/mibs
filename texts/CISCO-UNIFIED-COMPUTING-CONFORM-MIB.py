#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-CONFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-UNIFIED-COMPUTING-CONFORM-MIB
# Source digest sha256:a94c07d18565e5cb27e9d942b8bf35d70b56ce0c94ceaad0810cff13ad913433
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cucsFaultAffectedObjectDn, cucsFaultAffectedObjectId, cucsFaultCode, cucsFaultCreationTime, cucsFaultDescription, cucsFaultLastModificationTime, cucsFaultOccur, cucsFaultProbableCause, cucsFaultSeverity, cucsFaultType = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn", "cucsFaultAffectedObjectId", "cucsFaultCode", "cucsFaultCreationTime", "cucsFaultDescription", "cucsFaultLastModificationTime", "cucsFaultOccur", "cucsFaultProbableCause", "cucsFaultSeverity", "cucsFaultType")
ciscoUnifiedComputingMIB, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIB", "ciscoUnifiedComputingMIBObjects")
cucsFaultActiveNotif, cucsFaultClearNotif = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultActiveNotif", "cucsFaultClearNotif")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoUnifiedComputingMIBConform = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 2))
ciscoUnifiedComputingMIBConform.setRevisions(('2010-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setLastUpdated('2010-01-29 00:00')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setOrganization('Cisco')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: savbu-snmp-dev@cisco.com')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBConform.setDescription('Cisco UCS MIB conformance')
cucsFaultMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1))
cucsFaultMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1))
cucsFaultMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2))
cucsFaultMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", "cucsFaultsNotifGroup"), ("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", "cucsFaultsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultMIBCompliance = cucsFaultMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cucsFaultMIBCompliance.setDescription('The compliance statement for entities that support\n        the Cisco UCS Fault Managed Objects.')
cucsFaultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultsGroup = cucsFaultsGroup.setStatus('current')
if mibBuilder.loadTexts: cucsFaultsGroup.setDescription('A collection of objects providing UCS fault information.')
cucsFaultsNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultActiveNotif"), ("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", "cucsFaultClearNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultsNotifGroup = cucsFaultsNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cucsFaultsNotifGroup.setDescription('The set of UCS notifications defined by this MIB.')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-CONFORM-MIB", PYSNMP_MODULE_ID=ciscoUnifiedComputingMIBConform, ciscoUnifiedComputingMIBConform=ciscoUnifiedComputingMIBConform, cucsFaultMIBCompliance=cucsFaultMIBCompliance, cucsFaultMIBCompliances=cucsFaultMIBCompliances, cucsFaultMIBConform=cucsFaultMIBConform, cucsFaultMIBGroups=cucsFaultMIBGroups, cucsFaultsGroup=cucsFaultsGroup, cucsFaultsNotifGroup=cucsFaultsNotifGroup)
