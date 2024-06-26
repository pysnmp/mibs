#
# PySNMP MIB module BENU-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-MIB
# Produced by pysmi-1.1.12 at Wed Jun 26 13:31:41 2024
# On host fv-az1984-994 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter32, ObjectIdentity, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter32", "ObjectIdentity", "iso", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuPlatform = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1))
benuPlatform.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatform.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benuPlatform.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-MIB", PYSNMP_MODULE_ID=benuPlatform, benuPlatform=benuPlatform)
