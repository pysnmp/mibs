#
# PySNMP MIB module PACKETLOGIC-OVERVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-OVERVIEW-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 13:27:55 2023
# On host fv-az552-501 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, ObjectIdentity, Bits, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, TimeTicks, iso, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Bits", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "iso", "Counter32", "Integer32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
systemOverview = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 40))
systemOverview.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: systemOverview.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: systemOverview.setOrganization('Procera Networks, Inc.')
overview = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1), )
if mibBuilder.loadTexts: overview.setStatus('current')
overviewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1), ).setIndexNames((0, "PACKETLOGIC-OVERVIEW-MIB", "overviewEntryIndex"))
if mibBuilder.loadTexts: overviewEntry.setStatus('current')
overviewEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: overviewEntryIndex.setStatus('current')
model = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: model.setStatus('current')
configMd5Sum = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configMd5Sum.setStatus('current')
machineId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: machineId.setStatus('current')
firmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 40, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-OVERVIEW-MIB", configMd5Sum=configMd5Sum, overview=overview, machineId=machineId, overviewEntryIndex=overviewEntryIndex, PYSNMP_MODULE_ID=systemOverview, model=model, firmwareVersion=firmwareVersion, systemOverview=systemOverview, overviewEntry=overviewEntry)
