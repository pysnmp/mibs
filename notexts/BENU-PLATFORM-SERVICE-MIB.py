#
# PySNMP MIB module BENU-PLATFORM-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-SERVICE-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:05:08 2024
# On host fv-az883-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Gauge32, NotificationType, iso, Bits, ModuleIdentity, Integer32, Counter32, IpAddress, MibIdentifier, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Gauge32", "NotificationType", "iso", "Bits", "ModuleIdentity", "Integer32", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatSerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2))
benuPlatSerMIB.setRevisions(('2012-12-12 00:00',))
if mibBuilder.loadTexts: benuPlatSerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: benuPlatSerMIB.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-SERVICE-MIB", PYSNMP_MODULE_ID=benuPlatSerMIB, benuPlatSerMIB=benuPlatSerMIB)
