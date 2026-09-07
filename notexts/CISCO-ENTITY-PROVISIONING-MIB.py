#
# PySNMP MIB module CISCO-ENTITY-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-PROVISIONING-MIB
# Source digest sha256:e4dbd5f62a0a4edb5a169f3738552df6722bd262a6abc8d06b7ad6f7cb7853ed
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
AutonomousType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "TextualConvention")
ciscoEntityProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 139))
if mibBuilder.loadTexts: ciscoEntityProvMIB.setLastUpdated('1999-07-08 20:52')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 1))
ceProvContainerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceProvContainerTable.setStatus('current')
ceProvContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceProvContainerEntry.setStatus('current')
ceProvContainerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unequipped", 1), ("provisioned", 2), ("mismatched", 3), ("invalid", 4), ("equipped", 5), ("failed", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerStatus.setStatus('current')
ceProvContainerEquipped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 2), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceProvContainerEquipped.setStatus('current')
ceProvContainerDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerDetected.setStatus('current')
ceProvMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2))
ceProvMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2, 0))
ceProvMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3))
ceProvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1))
ceProvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2))
ceProvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvMIBCompliance = ceProvMIBCompliance.setStatus('current')
ceProvContainerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerStatus"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerEquipped"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvContainerGroup = ceProvContainerGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PROVISIONING-MIB", PYSNMP_MODULE_ID=ciscoEntityProvMIB, ceProvContainerDetected=ceProvContainerDetected, ceProvContainerEntry=ceProvContainerEntry, ceProvContainerEquipped=ceProvContainerEquipped, ceProvContainerGroup=ceProvContainerGroup, ceProvContainerStatus=ceProvContainerStatus, ceProvContainerTable=ceProvContainerTable, ceProvMIBCompliance=ceProvMIBCompliance, ceProvMIBCompliances=ceProvMIBCompliances, ceProvMIBConformance=ceProvMIBConformance, ceProvMIBGroups=ceProvMIBGroups, ceProvMIBNotifications=ceProvMIBNotifications, ceProvMIBNotificationsPrefix=ceProvMIBNotificationsPrefix, ciscoEntityProvMIB=ciscoEntityProvMIB, ciscoEntityProvMIBObjects=ciscoEntityProvMIBObjects)
