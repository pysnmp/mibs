#
# PySNMP MIB module AT-HHM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-HHM-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 19:55:50 2021
# On host fv-az36-522 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, Integer32, ModuleIdentity, Bits, MibIdentifier, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "Integer32", "ModuleIdentity", "Bits", "MibIdentifier", "Counter32", "NotificationType")
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
mibBuilder.exportSymbols("AT-HHM-MIB", atHhmLogMessage=atHhmLogMessage, PYSNMP_MODULE_ID=atHwHealthMon, atHhmLogNotify=atHhmLogNotify, atHwHealthMon=atHwHealthMon, atHhmNotifications=atHhmNotifications, atHhmNotificationVariables=atHhmNotificationVariables)
