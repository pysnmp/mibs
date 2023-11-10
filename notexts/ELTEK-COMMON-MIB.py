#
# PySNMP MIB module ELTEK-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltek/ELTEK-COMMON-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:43:13 2023
# On host fv-az566-171 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, iso, Bits, Counter64, TimeTicks, Integer32, IpAddress, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, Counter32, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "Bits", "Counter64", "TimeTicks", "Integer32", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltek = ModuleIdentity((1, 3, 6, 1, 4, 1, 12148))
eltek.setRevisions(('2015-01-03 08:25', '2010-10-29 08:29', '2009-03-12 15:15', '2008-01-30 11:49', '2007-06-22 11:27', '2005-09-07 12:38', '2005-06-28 11:30',))
if mibBuilder.loadTexts: eltek.setLastUpdated('201501030825Z')
if mibBuilder.loadTexts: eltek.setOrganization('ELTEK dcSystem MIB Working Group')
mibBuilder.exportSymbols("ELTEK-COMMON-MIB", PYSNMP_MODULE_ID=eltek, eltek=eltek)
