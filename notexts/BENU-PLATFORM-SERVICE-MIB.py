#
# PySNMP MIB module BENU-PLATFORM-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-SERVICE-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 11:10:25 2024
# On host fv-az1493-704 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, MibIdentifier, Gauge32, TimeTicks, Unsigned32, ModuleIdentity, IpAddress, ObjectIdentity, NotificationType, Counter64, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "Unsigned32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "NotificationType", "Counter64", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuPlatSerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2))
benuPlatSerMIB.setRevisions(('2012-12-12 00:00',))
if mibBuilder.loadTexts: benuPlatSerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: benuPlatSerMIB.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-SERVICE-MIB", PYSNMP_MODULE_ID=benuPlatSerMIB, benuPlatSerMIB=benuPlatSerMIB)
