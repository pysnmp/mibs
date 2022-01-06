#
# PySNMP MIB module SYNOLOGY-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-DISK-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:50:29 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
enterprises, ObjectIdentity, Bits, Counter64, ModuleIdentity, Gauge32, TimeTicks, NotificationType, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Counter32", "IpAddress")
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
mibBuilder.exportSymbols("SYNOLOGY-DISK-MIB", diskID=diskID, diskType=diskType, diskGroups=diskGroups, diskModel=diskModel, diskStatus=diskStatus, diskIndex=diskIndex, diskTemperature=diskTemperature, synology=synology, diskConformance=diskConformance, diskCompliances=diskCompliances, diskGroup=diskGroup, diskTable=diskTable, diskCompliance=diskCompliance, diskEntry=diskEntry, synoDisk=synoDisk, PYSNMP_MODULE_ID=synoDisk)
