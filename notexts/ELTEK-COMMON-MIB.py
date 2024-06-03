#
# PySNMP MIB module ELTEK-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltek/ELTEK-COMMON-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:38:37 2024
# On host fv-az1210-277 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Unsigned32, ObjectIdentity, enterprises, Counter64, IpAddress, mib_2, Bits, TimeTicks, iso, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Unsigned32", "ObjectIdentity", "enterprises", "Counter64", "IpAddress", "mib-2", "Bits", "TimeTicks", "iso", "MibIdentifier", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltek = ModuleIdentity((1, 3, 6, 1, 4, 1, 12148))
eltek.setRevisions(('2015-01-03 08:25', '2010-10-29 08:29', '2009-03-12 15:15', '2008-01-30 11:49', '2007-06-22 11:27', '2005-09-07 12:38', '2005-06-28 11:30',))
if mibBuilder.loadTexts: eltek.setLastUpdated('201501030825Z')
if mibBuilder.loadTexts: eltek.setOrganization('ELTEK dcSystem MIB Working Group')
mibBuilder.exportSymbols("ELTEK-COMMON-MIB", PYSNMP_MODULE_ID=eltek, eltek=eltek)
