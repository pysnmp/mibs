#
# PySNMP MIB module RAPID-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 01:42:13 2024
# On host fv-az1446-447 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Gauge32, Unsigned32, ModuleIdentity, NotificationType, ObjectIdentity, MibIdentifier, Bits, Integer32, iso, TimeTicks, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibIdentifier", "Bits", "Integer32", "iso", "TimeTicks", "IpAddress", "enterprises")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
rsInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 1))
if mibBuilder.loadTexts: rsInfoSystem.setStatus('current')
rsInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setStatus('current')
mibBuilder.exportSymbols("RAPID-INFO-SYSTEM-MIB", rsInfoModule=rsInfoModule, rsInfoSystem=rsInfoSystem, rsInfoSystemCurrentTime=rsInfoSystemCurrentTime, PYSNMP_MODULE_ID=rsInfoModule)
