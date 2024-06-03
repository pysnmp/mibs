#
# PySNMP MIB module BENU-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-ENTERPRISE-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:40:24 2024
# On host fv-az1530-906 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, NotificationType, iso, IpAddress, MibIdentifier, Gauge32, Bits, Unsigned32, enterprises, ModuleIdentity, Integer32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "NotificationType", "iso", "IpAddress", "MibIdentifier", "Gauge32", "Bits", "Unsigned32", "enterprises", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benu = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406))
benu.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benu.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benu.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-ENTERPRISE-MIB", PYSNMP_MODULE_ID=benu, benu=benu)
