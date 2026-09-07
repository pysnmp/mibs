#
# PySNMP MIB module CISCO-ACCESS-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ACCESS-ENVMON-MIB
# Source digest sha256:6e561e5fff736d4bd3cd14a2a1440055dfe9d5d889c4a19d445d728de1958a4f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoEnvMonSupplyStatusEntry, ciscoEnvMonTemperatureState, ciscoEnvMonTemperatureStatusDescr, ciscoEnvMonVoltageState, ciscoEnvMonVoltageStatusDescr = mibBuilder.importSymbols("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusEntry", "ciscoEnvMonTemperatureState", "ciscoEnvMonTemperatureStatusDescr", "ciscoEnvMonVoltageState", "ciscoEnvMonVoltageStatusDescr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAccessEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 61))
ciscoAccessEnvMonMIB.setRevisions(('1998-08-05 00:00',))
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setLastUpdated('1998-08-05 00:00')
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setOrganization('Cisco Systems, Inc.')
caemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 1))
caemSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caemSupplyStatusTable.setStatus('current')
caemSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1), ).setMaxAccess("notaccessible")
ciscoEnvMonSupplyStatusEntry.registerAugmentions(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyStatusEntry"))
caemSupplyStatusEntry.setIndexNames(*ciscoEnvMonSupplyStatusEntry.getIndexNames())
if mibBuilder.loadTexts: caemSupplyStatusEntry.setStatus('current')
caemSupplyFailedComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("inputVoltage", 2), ("dcOutputVoltage", 3), ("thermal", 4), ("multiple", 5), ("fan", 6), ("overvoltage", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caemSupplyFailedComponent.setStatus('current')
caemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2))
caemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0))
caemTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 1)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
if mibBuilder.loadTexts: caemTemperatureNotification.setStatus('current')
caemVoltageNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
if mibBuilder.loadTexts: caemVoltageNotification.setStatus('current')
caemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3))
caemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1))
caemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2))
caemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemCompliance = caemCompliance.setStatus('current')
caemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyFailedComponent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemGroup = caemGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ACCESS-ENVMON-MIB", PYSNMP_MODULE_ID=ciscoAccessEnvMonMIB, caemCompliance=caemCompliance, caemCompliances=caemCompliances, caemConformance=caemConformance, caemGroup=caemGroup, caemGroups=caemGroups, caemMIBNotificationPrefix=caemMIBNotificationPrefix, caemMIBNotifications=caemMIBNotifications, caemObjects=caemObjects, caemSupplyFailedComponent=caemSupplyFailedComponent, caemSupplyStatusEntry=caemSupplyStatusEntry, caemSupplyStatusTable=caemSupplyStatusTable, caemTemperatureNotification=caemTemperatureNotification, caemVoltageNotification=caemVoltageNotification, ciscoAccessEnvMonMIB=ciscoAccessEnvMonMIB)
