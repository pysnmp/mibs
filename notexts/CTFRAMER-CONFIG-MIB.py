#
# PySNMP MIB module CTFRAMER-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTFRAMER-CONFIG-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:04:28 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ctIfPortPortNumber, ctFramerConfig = mibBuilder.importSymbols("CTIF-EXT-MIB", "ctIfPortPortNumber", "ctFramerConfig")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, Integer32, Counter32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "Counter32", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFramerBaseConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1))
ctFramerSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 2))
ctFramerDS3Config = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 3))
ctFramerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1), )
if mibBuilder.loadTexts: ctFramerConfigTable.setStatus('mandatory')
ctFramerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctFramerConfigEntry.setStatus('mandatory')
ctFramerStatsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerStatsConfig.setStatus('mandatory')
ctFramerAlarmsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerAlarmsConfig.setStatus('mandatory')
ctFramerMediumConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2))).clone('sonet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerMediumConfig.setStatus('mandatory')
ctFramerIdleCellsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("unassigned", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerIdleCellsConfig.setStatus('mandatory')
ctFramerCellPayScramConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerCellPayScramConfig.setStatus('mandatory')
mibBuilder.exportSymbols("CTFRAMER-CONFIG-MIB", ctFramerCellPayScramConfig=ctFramerCellPayScramConfig, ctFramerDS3Config=ctFramerDS3Config, ctFramerSonetConfig=ctFramerSonetConfig, ctFramerStatsConfig=ctFramerStatsConfig, ctFramerConfigEntry=ctFramerConfigEntry, ctFramerIdleCellsConfig=ctFramerIdleCellsConfig, ctFramerMediumConfig=ctFramerMediumConfig, ctFramerAlarmsConfig=ctFramerAlarmsConfig, ctFramerBaseConfig=ctFramerBaseConfig, ctFramerConfigTable=ctFramerConfigTable)
