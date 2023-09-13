#
# PySNMP MIB module AT-HHM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-HHM-MIB
# Produced by pysmi-1.1.8 at Wed Sep 13 14:50:21 2023
# On host fv-az629-233 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Gauge32, Unsigned32, IpAddress, NotificationType, ObjectIdentity, Counter64, iso, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "NotificationType", "ObjectIdentity", "Counter64", "iso", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AT-HHM-MIB", PYSNMP_MODULE_ID=atHwHealthMon, atHhmLogNotify=atHhmLogNotify, atHhmLogMessage=atHhmLogMessage, atHwHealthMon=atHwHealthMon, atHhmNotifications=atHhmNotifications, atHhmNotificationVariables=atHhmNotificationVariables)
