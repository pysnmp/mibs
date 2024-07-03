#
# PySNMP MIB module PACKETLOGIC-OVERVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-OVERVIEW-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 13:33:29 2024
# On host fv-az693-695 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, TimeTicks, IpAddress, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, NotificationType, ModuleIdentity, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "NotificationType", "ModuleIdentity", "ObjectIdentity", "iso", "Unsigned32")
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
mibBuilder.exportSymbols("PACKETLOGIC-OVERVIEW-MIB", overviewEntry=overviewEntry, overviewEntryIndex=overviewEntryIndex, configMd5Sum=configMd5Sum, machineId=machineId, overview=overview, firmwareVersion=firmwareVersion, PYSNMP_MODULE_ID=systemOverview, systemOverview=systemOverview, model=model)
