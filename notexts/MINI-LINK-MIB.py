#
# PySNMP MIB module MINI-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/MINI-LINK-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:48:25 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, NotificationType, Counter64, Counter32, ModuleIdentity, IpAddress, Bits, ObjectIdentity, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "NotificationType", "Counter64", "Counter32", "ModuleIdentity", "IpAddress", "Bits", "ObjectIdentity", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
miniLink = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223))
miniLink.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: miniLink.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: miniLink.setOrganization('Ericsson')
ericsson = MibIdentifier((1, 3, 6, 1, 4, 1, 193))
mibBuilder.exportSymbols("MINI-LINK-MIB", PYSNMP_MODULE_ID=miniLink, ericsson=ericsson, miniLink=miniLink)
