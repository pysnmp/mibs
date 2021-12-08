#
# PySNMP MIB module PRVT-CONFIGCHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-CONFIGCHANGE-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:20:51 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ObjectIdentity, ModuleIdentity, MibIdentifier, iso, TimeTicks, Unsigned32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "iso", "TimeTicks", "Unsigned32", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtConfigChangeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 150))
prvtConfigChangeMIB.setRevisions(('2010-09-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtConfigChangeMIB.setRevisionsDescriptions(('Initial release',))
if mibBuilder.loadTexts: prvtConfigChangeMIB.setLastUpdated('201009010000Z')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setDescription('Initial version. This MIB will provied traps for change')
prvtConfigChangeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 0))
prvtConfigChangeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 1))
prvtConfigChangeAlarmNamespace = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmNamespace.setStatus('current')
if mibBuilder.loadTexts: prvtConfigChangeAlarmNamespace.setDescription('The configChangeAlarmNamespace specifies the Namespace\n         of an object whose value has been changed.')
prvtConfigChangeAlarmKeypath = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 1, 2), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmKeypath.setStatus('current')
if mibBuilder.loadTexts: prvtConfigChangeAlarmKeypath.setDescription('The configChangeAlarmKeypath specifies the Keypath\n         of an object whose entry has been changed.')
prvtConfigChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 0, 1)).setObjects(("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmNamespace"), ("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmKeypath"))
if mibBuilder.loadTexts: prvtConfigChangeAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtConfigChangeAlarm.setDescription('This notification is generated when the value of configurable\n         attribute has been changed. The notification can be used\n         to trigger maintenance polling of the running configuration\n         on the device. There is flood prevention that notification\n         with same varbinds will not be sent for certain time - i.e. 1 min')
mibBuilder.exportSymbols("PRVT-CONFIGCHANGE-MIB", prvtConfigChangeMIB=prvtConfigChangeMIB, prvtConfigChangeAlarmNamespace=prvtConfigChangeAlarmNamespace, PYSNMP_MODULE_ID=prvtConfigChangeMIB, prvtConfigChangeNotifications=prvtConfigChangeNotifications, prvtConfigChangeAlarm=prvtConfigChangeAlarm, prvtConfigChangeAlarmKeypath=prvtConfigChangeAlarmKeypath, prvtConfigChangeObjects=prvtConfigChangeObjects)
