#
# PySNMP MIB module SYNOLOGY-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-RAID-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 15:20:59 2024
# On host fv-az979-188 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Bits, Counter64, ObjectIdentity, iso, IpAddress, Integer32, NotificationType, TimeTicks, Counter32, Gauge32, enterprises, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "ObjectIdentity", "iso", "IpAddress", "Integer32", "NotificationType", "TimeTicks", "Counter32", "Gauge32", "enterprises", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoRaid = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 3))
synoRaid.setRevisions(('2013-09-11 00:00',))
if mibBuilder.loadTexts: synoRaid.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoRaid.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
raidTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 3, 1), )
if mibBuilder.loadTexts: raidTable.setStatus('current')
raidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1), ).setIndexNames((0, "SYNOLOGY-RAID-MIB", "raidIndex"))
if mibBuilder.loadTexts: raidEntry.setStatus('current')
raidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: raidIndex.setStatus('current')
raidName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidName.setStatus('current')
raidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidStatus.setStatus('current')
raidFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidFreeSize.setStatus('current')
raidTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidTotalSize.setStatus('current')
raidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2))
raidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1))
raidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2))
raidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidCompliance = raidCompliance.setStatus('current')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidName"), ("SYNOLOGY-RAID-MIB", "raidStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-RAID-MIB", raidFreeSize=raidFreeSize, raidIndex=raidIndex, raidGroups=raidGroups, raidTotalSize=raidTotalSize, raidCompliances=raidCompliances, PYSNMP_MODULE_ID=synoRaid, raidStatus=raidStatus, synology=synology, raidName=raidName, raidConformance=raidConformance, raidGroup=raidGroup, raidEntry=raidEntry, raidTable=raidTable, synoRaid=synoRaid, raidCompliance=raidCompliance)
