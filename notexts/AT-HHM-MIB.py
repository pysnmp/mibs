#
# PySNMP MIB module AT-HHM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-HHM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:34:13 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Counter64, IpAddress, NotificationType, TimeTicks, Counter32, ModuleIdentity, iso, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "IpAddress", "NotificationType", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atHwHealthMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24))
atHwHealthMon.setRevisions(('2013-06-28 00:00',))
if mibBuilder.loadTexts: atHwHealthMon.setLastUpdated('201306280000Z')
if mibBuilder.loadTexts: atHwHealthMon.setOrganization('Allied Telesis, Inc')
atHhmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 0))
atHhmLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 0, 1)).setObjects(("AT-HHM-MIB", "atHhmLogMessage"))
if mibBuilder.loadTexts: atHhmLogNotify.setStatus('current')
atHhmNotificationVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 1))
atHhmLogMessage = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 1, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: atHhmLogMessage.setStatus('current')
mibBuilder.exportSymbols("AT-HHM-MIB", PYSNMP_MODULE_ID=atHwHealthMon, atHhmNotificationVariables=atHhmNotificationVariables, atHhmLogNotify=atHhmLogNotify, atHhmLogMessage=atHhmLogMessage, atHhmNotifications=atHhmNotifications, atHwHealthMon=atHwHealthMon)
