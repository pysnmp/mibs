#
# PySNMP MIB module F5-OS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-OS-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 08:18:10 2023
# On host fv-az585-225 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
platform, = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Counter64, Gauge32, IpAddress, Integer32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, MibIdentifier, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Counter64", "Gauge32", "IpAddress", "Integer32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "MibIdentifier", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
f5OsSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 3))
f5OsSystem.setRevisions(('2022-04-07 00:00',))
if mibBuilder.loadTexts: f5OsSystem.setLastUpdated('202204070000Z')
if mibBuilder.loadTexts: f5OsSystem.setOrganization('F5 Networks, Inc.')
f5OsSystemModelOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1))
f5OsAppR5x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 1))
f5OsAppR10x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 2))
f5OsAppR2x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 3))
f5OsAppR4x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 4))
f5OsVelosCx410 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 5))
f5OsVelosCx410Partition = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 6))
mibBuilder.exportSymbols("F5-OS-SYSTEM-MIB", PYSNMP_MODULE_ID=f5OsSystem, f5OsVelosCx410=f5OsVelosCx410, f5OsAppR4x00=f5OsAppR4x00, f5OsSystemModelOIDs=f5OsSystemModelOIDs, f5OsAppR5x00=f5OsAppR5x00, f5OsAppR10x00=f5OsAppR10x00, f5OsVelosCx410Partition=f5OsVelosCx410Partition, f5OsSystem=f5OsSystem, f5OsAppR2x00=f5OsAppR2x00)
