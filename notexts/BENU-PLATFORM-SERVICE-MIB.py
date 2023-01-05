#
# PySNMP MIB module BENU-PLATFORM-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-SERVICE-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 11:24:43 2023
# On host fv-az280-773 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Unsigned32, TimeTicks, Counter32, NotificationType, Gauge32, ObjectIdentity, Counter64, Integer32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "Counter64", "Integer32", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuPlatSerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2))
benuPlatSerMIB.setRevisions(('2012-12-12 00:00',))
if mibBuilder.loadTexts: benuPlatSerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: benuPlatSerMIB.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-SERVICE-MIB", benuPlatSerMIB=benuPlatSerMIB, PYSNMP_MODULE_ID=benuPlatSerMIB)
