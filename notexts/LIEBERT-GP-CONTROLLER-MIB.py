#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:28:20 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
liebertControllerModuleReg, lgpController = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertControllerModuleReg", "lgpController")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, Counter32, NotificationType, MibIdentifier, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity, Unsigned32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Counter32", "NotificationType", "MibIdentifier", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertControllerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7, 1))
liebertControllerModule.setRevisions(('2008-07-02 00:00', '2008-01-10 00:00', '2006-02-22 00:00',))
if mibBuilder.loadTexts: liebertControllerModule.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: liebertControllerModule.setOrganization('Liebert Corporation')
lgpCtrlNumberInstalledControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberInstalledControlModules.setStatus('current')
lgpCtrlNumberFailedControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberFailedControlModules.setStatus('current')
lgpCtrlNumberRedundantControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberRedundantControlModules.setStatus('current')
lgpCtrlNumberControlModuleWarnings = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberControlModuleWarnings.setStatus('current')
lgpCtrlBoardBatteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 6), Unsigned32()).setUnits('.01 Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlBoardBatteryVoltage.setStatus('current')
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, PYSNMP_MODULE_ID=liebertControllerModule, liebertControllerModule=liebertControllerModule, lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage)
