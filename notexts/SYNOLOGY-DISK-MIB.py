#
# PySNMP MIB module SYNOLOGY-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-DISK-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:34:31 2024
# On host fv-az883-167 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, MibIdentifier, iso, Counter64, ObjectIdentity, Counter32, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "MibIdentifier", "iso", "Counter64", "ObjectIdentity", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32")
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
mibBuilder.exportSymbols("SYNOLOGY-DISK-MIB", diskType=diskType, diskCompliances=diskCompliances, diskID=diskID, diskCompliance=diskCompliance, PYSNMP_MODULE_ID=synoDisk, diskTable=diskTable, diskEntry=diskEntry, diskModel=diskModel, synoDisk=synoDisk, diskTemperature=diskTemperature, diskConformance=diskConformance, synology=synology, diskStatus=diskStatus, diskGroup=diskGroup, diskGroups=diskGroups, diskIndex=diskIndex)
