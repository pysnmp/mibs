#
# PySNMP MIB module CTFRAMER-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTFRAMER-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Sep 18 06:45:17 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ctFramerConfig, ctIfPortPortNumber = mibBuilder.importSymbols("CTIF-EXT-MIB", "ctFramerConfig", "ctIfPortPortNumber")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, IpAddress, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "IpAddress", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CTFRAMER-CONFIG-MIB", ctFramerConfigEntry=ctFramerConfigEntry, ctFramerSonetConfig=ctFramerSonetConfig, ctFramerIdleCellsConfig=ctFramerIdleCellsConfig, ctFramerStatsConfig=ctFramerStatsConfig, ctFramerConfigTable=ctFramerConfigTable, ctFramerBaseConfig=ctFramerBaseConfig, ctFramerCellPayScramConfig=ctFramerCellPayScramConfig, ctFramerAlarmsConfig=ctFramerAlarmsConfig, ctFramerMediumConfig=ctFramerMediumConfig, ctFramerDS3Config=ctFramerDS3Config)
