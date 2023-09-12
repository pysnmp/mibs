#
# PySNMP MIB module RAPID-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 08:10:40 2023
# On host fv-az447-19 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, IpAddress, Bits, NotificationType, ModuleIdentity, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, iso, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "IpAddress", "Bits", "NotificationType", "ModuleIdentity", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "iso", "TimeTicks", "ObjectIdentity")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
rsInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 1))
if mibBuilder.loadTexts: rsInfoSystem.setStatus('current')
rsInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setStatus('current')
mibBuilder.exportSymbols("RAPID-INFO-SYSTEM-MIB", rsInfoModule=rsInfoModule, rsInfoSystem=rsInfoSystem, rsInfoSystemCurrentTime=rsInfoSystemCurrentTime, PYSNMP_MODULE_ID=rsInfoModule)
