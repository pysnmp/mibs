#
# PySNMP MIB module MINI-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/MINI-LINK-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:13:39 2022
# On host fv-az445-955 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, enterprises, Integer32, Counter64, MibIdentifier, Unsigned32, Bits, Counter32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "enterprises", "Integer32", "Counter64", "MibIdentifier", "Unsigned32", "Bits", "Counter32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
miniLink = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223))
miniLink.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: miniLink.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: miniLink.setOrganization('Ericsson')
ericsson = MibIdentifier((1, 3, 6, 1, 4, 1, 193))
mibBuilder.exportSymbols("MINI-LINK-MIB", miniLink=miniLink, ericsson=ericsson, PYSNMP_MODULE_ID=miniLink)
