#
# PySNMP MIB module F5-OS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-OS-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:06:23 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
platform, = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, IpAddress, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, iso, Unsigned32, Bits, Gauge32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "iso", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "Counter64")
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
mibBuilder.exportSymbols("F5-OS-SYSTEM-MIB", PYSNMP_MODULE_ID=f5OsSystem, f5OsAppR10x00=f5OsAppR10x00, f5OsAppR2x00=f5OsAppR2x00, f5OsVelosCx410=f5OsVelosCx410, f5OsSystemModelOIDs=f5OsSystemModelOIDs, f5OsAppR5x00=f5OsAppR5x00, f5OsAppR4x00=f5OsAppR4x00, f5OsVelosCx410Partition=f5OsVelosCx410Partition, f5OsSystem=f5OsSystem)
