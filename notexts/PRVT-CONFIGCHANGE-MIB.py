#
# PySNMP MIB module PRVT-CONFIGCHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-CONFIGCHANGE-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:20 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Unsigned32, Integer32, TimeTicks, ModuleIdentity, Counter64, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Unsigned32", "Integer32", "TimeTicks", "ModuleIdentity", "Counter64", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtConfigChangeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 150))
prvtConfigChangeMIB.setRevisions(('2010-09-01 00:00',))
if mibBuilder.loadTexts: prvtConfigChangeMIB.setLastUpdated('201009010000Z')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setOrganization('BATM Advanced Communication')
prvtConfigChangeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 0))
prvtConfigChangeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 1))
prvtConfigChangeAlarmNamespace = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmNamespace.setStatus('current')
prvtConfigChangeAlarmKeypath = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 1, 2), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmKeypath.setStatus('current')
prvtConfigChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 150, 0, 1)).setObjects(("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmNamespace"), ("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmKeypath"))
if mibBuilder.loadTexts: prvtConfigChangeAlarm.setStatus('current')
mibBuilder.exportSymbols("PRVT-CONFIGCHANGE-MIB", prvtConfigChangeObjects=prvtConfigChangeObjects, prvtConfigChangeAlarm=prvtConfigChangeAlarm, prvtConfigChangeMIB=prvtConfigChangeMIB, prvtConfigChangeAlarmKeypath=prvtConfigChangeAlarmKeypath, PYSNMP_MODULE_ID=prvtConfigChangeMIB, prvtConfigChangeNotifications=prvtConfigChangeNotifications, prvtConfigChangeAlarmNamespace=prvtConfigChangeAlarmNamespace)
