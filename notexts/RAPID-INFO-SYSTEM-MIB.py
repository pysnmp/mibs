#
# PySNMP MIB module RAPID-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 15:21:35 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Counter64, Integer32, MibIdentifier, Bits, TimeTicks, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, enterprises, Unsigned32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter64", "Integer32", "MibIdentifier", "Bits", "TimeTicks", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "enterprises", "Unsigned32", "NotificationType", "IpAddress")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
rsInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 1))
if mibBuilder.loadTexts: rsInfoSystem.setStatus('current')
rsInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setStatus('current')
mibBuilder.exportSymbols("RAPID-INFO-SYSTEM-MIB", rsInfoModule=rsInfoModule, rsInfoSystemCurrentTime=rsInfoSystemCurrentTime, rsInfoSystem=rsInfoSystem, PYSNMP_MODULE_ID=rsInfoModule)
