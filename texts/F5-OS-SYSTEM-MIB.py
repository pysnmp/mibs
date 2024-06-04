#
# PySNMP MIB module F5-OS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-OS-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:06:10 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
platform, = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, IpAddress, TimeTicks, ObjectIdentity, NotificationType, Unsigned32, ModuleIdentity, MibIdentifier, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "IpAddress", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
f5OsSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 3))
f5OsSystem.setRevisions(('2022-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f5OsSystem.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: f5OsSystem.setLastUpdated('202204070000Z')
if mibBuilder.loadTexts: f5OsSystem.setOrganization('F5 Networks, Inc.')
if mibBuilder.loadTexts: f5OsSystem.setContactInfo('postal: F5 Networks, Inc.\n                  801 Fifth Avenue\n                  Seattle, WA 98104\n          phone:  (206) 272-6500\n          email:  support@f5.com')
if mibBuilder.loadTexts: f5OsSystem.setDescription('Top-level infrastructure of the F5OS System MIB tree.')
f5OsSystemModelOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1))
f5OsAppR5x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 1))
f5OsAppR10x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 2))
f5OsAppR2x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 3))
f5OsAppR4x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 4))
f5OsVelosCx410 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 5))
f5OsVelosCx410Partition = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 6))
mibBuilder.exportSymbols("F5-OS-SYSTEM-MIB", f5OsSystemModelOIDs=f5OsSystemModelOIDs, PYSNMP_MODULE_ID=f5OsSystem, f5OsVelosCx410=f5OsVelosCx410, f5OsAppR2x00=f5OsAppR2x00, f5OsAppR10x00=f5OsAppR10x00, f5OsSystem=f5OsSystem, f5OsAppR4x00=f5OsAppR4x00, f5OsVelosCx410Partition=f5OsVelosCx410Partition, f5OsAppR5x00=f5OsAppR5x00)
