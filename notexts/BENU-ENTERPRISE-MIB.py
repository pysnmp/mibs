#
# PySNMP MIB module BENU-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-ENTERPRISE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:15:07 2024
# On host fv-az1385-751 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, MibIdentifier, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, enterprises, Gauge32, iso, Counter32, Counter64, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "MibIdentifier", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "enterprises", "Gauge32", "iso", "Counter32", "Counter64", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benu = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406))
benu.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benu.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benu.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-ENTERPRISE-MIB", PYSNMP_MODULE_ID=benu, benu=benu)
