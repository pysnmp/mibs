#
# PySNMP MIB module BENU-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 13:28:28 2023
# On host fv-az163-847 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter64, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, NotificationType, Gauge32, Integer32, IpAddress, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "NotificationType", "Gauge32", "Integer32", "IpAddress", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatform = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1))
benuPlatform.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatform.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benuPlatform.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-MIB", benuPlatform=benuPlatform, PYSNMP_MODULE_ID=benuPlatform)
