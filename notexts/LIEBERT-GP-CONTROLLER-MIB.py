#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 15:50:36 2023
# On host fv-az551-95 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
liebertControllerModuleReg, lgpController = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertControllerModuleReg", "lgpController")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter32, TimeTicks, Unsigned32, IpAddress, Gauge32, ObjectIdentity, Counter64, ModuleIdentity, iso, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter32", "TimeTicks", "Unsigned32", "IpAddress", "Gauge32", "ObjectIdentity", "Counter64", "ModuleIdentity", "iso", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules, liebertControllerModule=liebertControllerModule, lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, PYSNMP_MODULE_ID=liebertControllerModule, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules)
