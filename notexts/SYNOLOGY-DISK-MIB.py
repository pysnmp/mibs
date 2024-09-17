#
# PySNMP MIB module SYNOLOGY-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-DISK-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:36:56 2024
# On host fv-az975-559 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, ModuleIdentity, MibIdentifier, Bits, TimeTicks, Unsigned32, Gauge32, Integer32, Counter64, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "ModuleIdentity", "MibIdentifier", "Bits", "TimeTicks", "Unsigned32", "Gauge32", "Integer32", "Counter64", "enterprises", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoDisk = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 2))
synoDisk.setRevisions(('2013-09-11 00:00',))
if mibBuilder.loadTexts: synoDisk.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoDisk.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
diskTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 2, 1), )
if mibBuilder.loadTexts: diskTable.setStatus('current')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1), ).setIndexNames((0, "SYNOLOGY-DISK-MIB", "diskIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
diskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: diskIndex.setStatus('current')
diskID = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskID.setStatus('current')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('current')
diskType = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskType.setStatus('current')
diskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskStatus.setStatus('current')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
diskConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 2, 2))
diskCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 2, 2, 1))
diskGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 2, 2, 2))
diskCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 2, 2, 1, 1)).setObjects(("SYNOLOGY-DISK-MIB", "diskGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diskCompliance = diskCompliance.setStatus('current')
diskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 2, 2, 2, 1)).setObjects(("SYNOLOGY-DISK-MIB", "diskID"), ("SYNOLOGY-DISK-MIB", "diskModel"), ("SYNOLOGY-DISK-MIB", "diskType"), ("SYNOLOGY-DISK-MIB", "diskStatus"), ("SYNOLOGY-DISK-MIB", "diskTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diskGroup = diskGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-DISK-MIB", diskID=diskID, diskType=diskType, diskCompliance=diskCompliance, diskCompliances=diskCompliances, diskGroup=diskGroup, diskTable=diskTable, PYSNMP_MODULE_ID=synoDisk, diskEntry=diskEntry, diskConformance=diskConformance, synoDisk=synoDisk, diskIndex=diskIndex, diskTemperature=diskTemperature, diskStatus=diskStatus, diskGroups=diskGroups, synology=synology, diskModel=diskModel)
