#
# PySNMP MIB module F5-OS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-OS-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed May 29 06:45:04 2024
# On host fv-az1019-850 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
platform, = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, ObjectIdentity, IpAddress, Gauge32, Counter32, Bits, Counter64, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "ObjectIdentity", "IpAddress", "Gauge32", "Counter32", "Bits", "Counter64", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("F5-OS-SYSTEM-MIB", f5OsSystemModelOIDs=f5OsSystemModelOIDs, f5OsVelosCx410Partition=f5OsVelosCx410Partition, f5OsSystem=f5OsSystem, f5OsAppR4x00=f5OsAppR4x00, f5OsAppR2x00=f5OsAppR2x00, PYSNMP_MODULE_ID=f5OsSystem, f5OsAppR5x00=f5OsAppR5x00, f5OsAppR10x00=f5OsAppR10x00, f5OsVelosCx410=f5OsVelosCx410)
