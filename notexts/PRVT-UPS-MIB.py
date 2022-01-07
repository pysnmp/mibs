#
# PySNMP MIB module PRVT-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-UPS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:06:23 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, Counter32, IpAddress, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Integer32, TimeTicks, MibIdentifier, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "IpAddress", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Integer32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtUPSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 103))
prvtUPSMib.setRevisions(('2008-01-01 00:00', '2005-02-16 00:00', '2003-05-08 00:00', '2002-01-28 00:00',))
if mibBuilder.loadTexts: prvtUPSMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtUPSMib.setOrganization('BATM Advanced Communication')
prvtUPSNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 0))
upsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1))
prvtUPSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2))
upsConnectedStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("disconnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConnectedStatus.setStatus('current')
upsLinePowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("fromExternalConnection", 2), ("fromInternalBattery", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsLinePowerStatus.setStatus('current')
upsBatteryStorageStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("moreThan30Minutes", 2), ("lessThan30Minutes", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryStorageStatus.setStatus('current')
upsInternalStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("ok", 2), ("failure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInternalStatus.setStatus('current')
upsStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 0, 1)).setObjects(("PRVT-UPS-MIB", "upsConnectedStatus"), ("PRVT-UPS-MIB", "upsLinePowerStatus"), ("PRVT-UPS-MIB", "upsBatteryStorageStatus"), ("PRVT-UPS-MIB", "upsInternalStatus"))
if mibBuilder.loadTexts: upsStatusChange.setStatus('current')
prvtUPSMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2, 2))
prvtUPSNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2, 2, 3)).setObjects(("PRVT-UPS-MIB", "upsStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtUPSNotificationGroup = prvtUPSNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-UPS-MIB", upsConnectedStatus=upsConnectedStatus, upsStatus=upsStatus, prvtUPSMib=prvtUPSMib, upsStatusChange=upsStatusChange, PYSNMP_MODULE_ID=prvtUPSMib, upsInternalStatus=upsInternalStatus, upsBatteryStorageStatus=upsBatteryStorageStatus, prvtUPSNotifications=prvtUPSNotifications, upsLinePowerStatus=upsLinePowerStatus, prvtUPSMIBGroups=prvtUPSMIBGroups, prvtUPSNotificationGroup=prvtUPSNotificationGroup, prvtUPSConformance=prvtUPSConformance)
