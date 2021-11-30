#
# PySNMP MIB module PACKETLOGIC-OVERVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-OVERVIEW-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 02:28:54 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, TimeTicks, Gauge32, ObjectIdentity, NotificationType, Integer32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "TimeTicks", "Gauge32", "ObjectIdentity", "NotificationType", "Integer32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter64", "MibIdentifier")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PACKETLOGIC-OVERVIEW-MIB", overviewEntry=overviewEntry, configMd5Sum=configMd5Sum, machineId=machineId, firmwareVersion=firmwareVersion, systemOverview=systemOverview, overview=overview, model=model, PYSNMP_MODULE_ID=systemOverview, overviewEntryIndex=overviewEntryIndex)
