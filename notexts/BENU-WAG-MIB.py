#
# PySNMP MIB module BENU-WAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-WAG-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:54:34 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
benuPlatSerMIB, = mibBuilder.importSymbols("BENU-PLATFORM-SERVICE-MIB", "benuPlatSerMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, iso, ModuleIdentity, Integer32, Counter64, Bits, MibIdentifier, ObjectIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "iso", "ModuleIdentity", "Integer32", "Counter64", "Bits", "MibIdentifier", "ObjectIdentity", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuWAG = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1))
benuWAG.setRevisions(('2012-10-08 00:00',))
if mibBuilder.loadTexts: benuWAG.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: benuWAG.setOrganization('Benu Networks')
mibBuilder.exportSymbols("BENU-WAG-MIB", benuWAG=benuWAG, PYSNMP_MODULE_ID=benuWAG)
