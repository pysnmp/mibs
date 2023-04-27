#
# PySNMP MIB module AT-HHM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-HHM-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:55:14 2023
# On host fv-az338-106 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, Integer32, iso, TimeTicks, Gauge32, MibIdentifier, Unsigned32, IpAddress, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Integer32", "iso", "TimeTicks", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
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
mibBuilder.exportSymbols("AT-HHM-MIB", atHhmNotifications=atHhmNotifications, atHhmLogMessage=atHhmLogMessage, PYSNMP_MODULE_ID=atHwHealthMon, atHwHealthMon=atHwHealthMon, atHhmLogNotify=atHhmLogNotify, atHhmNotificationVariables=atHhmNotificationVariables)
