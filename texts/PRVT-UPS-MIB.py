#
# PySNMP MIB module PRVT-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-UPS-MIB
# Produced by pysmi-1.1.3 at Sat Nov 20 17:22:42 2021
# On host fv-az121-977 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter32, Counter64, ObjectIdentity, MibIdentifier, Unsigned32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtUPSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 103))
prvtUPSMib.setRevisions(('2008-01-01 00:00', '2005-02-16 00:00', '2003-05-08 00:00', '2002-01-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtUPSMib.setRevisionsDescriptions(('Removed redefined OIDs in private vendor extension definitions.', 'Fixed spelling errors and changed the contact info.', 'Move to SMI-V2.', 'Initial version.',))
if mibBuilder.loadTexts: prvtUPSMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtUPSMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtUPSMib.setContactInfo('BATM/Telco Systems Support team\n\t\t\t\tEmail: \n\t\t\t\tFor North America: techsupport@telco.com\n\t\t\t\tFor North Europe: support@batm.de, info@batm.de\n\t\t\t\tFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtUPSMib.setDescription('MIB module for monitoring the UPS connected to switch or ipSwitch')
prvtUPSNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 0))
upsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1))
prvtUPSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2))
upsConnectedStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("disconnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConnectedStatus.setStatus('current')
if mibBuilder.loadTexts: upsConnectedStatus.setDescription('This object indicates, if a UPS is connected to the device.')
upsLinePowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("fromExternalConnection", 2), ("fromInternalBattery", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsLinePowerStatus.setStatus('current')
if mibBuilder.loadTexts: upsLinePowerStatus.setDescription('This object indicates the external AD power line status: \n             the UPS is supplying the power from the internal battery\n             or from an external AC power connection.')
upsBatteryStorageStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("moreThan30Minutes", 2), ("lessThan30Minutes", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryStorageStatus.setStatus('current')
if mibBuilder.loadTexts: upsBatteryStorageStatus.setDescription('This object shows the estimated time left until the UPS battery \n             will discharge to the level at which the UPS must shutdown.')
upsInternalStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("ok", 2), ("failure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInternalStatus.setStatus('current')
if mibBuilder.loadTexts: upsInternalStatus.setDescription('This object shows if the UPS has some kind of an internal \n             failure.')
upsStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 0, 1)).setObjects(("PRVT-UPS-MIB", "upsConnectedStatus"), ("PRVT-UPS-MIB", "upsLinePowerStatus"), ("PRVT-UPS-MIB", "upsBatteryStorageStatus"), ("PRVT-UPS-MIB", "upsInternalStatus"))
if mibBuilder.loadTexts: upsStatusChange.setStatus('current')
if mibBuilder.loadTexts: upsStatusChange.setDescription('The upsStatusChange trap indicates that the sending \n                  agent monitor detected a change in the status of the external \n                  UPS, connected to the device.')
prvtUPSMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2, 2))
prvtUPSNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2, 2, 3)).setObjects(("PRVT-UPS-MIB", "upsStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtUPSNotificationGroup = prvtUPSNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: prvtUPSNotificationGroup.setDescription('Private Notification Group.')
mibBuilder.exportSymbols("PRVT-UPS-MIB", upsStatus=upsStatus, upsBatteryStorageStatus=upsBatteryStorageStatus, prvtUPSMIBGroups=prvtUPSMIBGroups, prvtUPSNotifications=prvtUPSNotifications, upsConnectedStatus=upsConnectedStatus, prvtUPSNotificationGroup=prvtUPSNotificationGroup, PYSNMP_MODULE_ID=prvtUPSMib, prvtUPSMib=prvtUPSMib, prvtUPSConformance=prvtUPSConformance, upsInternalStatus=upsInternalStatus, upsStatusChange=upsStatusChange, upsLinePowerStatus=upsLinePowerStatus)
