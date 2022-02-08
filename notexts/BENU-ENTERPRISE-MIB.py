#
# PySNMP MIB module BENU-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-ENTERPRISE-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:27:12 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, TimeTicks, NotificationType, Counter32, iso, Bits, Counter64, MibIdentifier, Integer32, Unsigned32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "TimeTicks", "NotificationType", "Counter32", "iso", "Bits", "Counter64", "MibIdentifier", "Integer32", "Unsigned32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benu = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406))
benu.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benu.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benu.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-ENTERPRISE-MIB", PYSNMP_MODULE_ID=benu, benu=benu)
