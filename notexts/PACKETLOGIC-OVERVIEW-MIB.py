#
# PySNMP MIB module PACKETLOGIC-OVERVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-OVERVIEW-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 19:52:15 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Integer32, ObjectIdentity, NotificationType, IpAddress, Counter32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType", "IpAddress", "Counter32", "iso", "ModuleIdentity")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
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
mibBuilder.exportSymbols("PACKETLOGIC-OVERVIEW-MIB", configMd5Sum=configMd5Sum, overview=overview, systemOverview=systemOverview, overviewEntry=overviewEntry, firmwareVersion=firmwareVersion, overviewEntryIndex=overviewEntryIndex, PYSNMP_MODULE_ID=systemOverview, model=model, machineId=machineId)
