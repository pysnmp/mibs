#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:08:12 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
liebertControllerModuleReg, lgpController = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertControllerModuleReg", "lgpController")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, MibIdentifier, Counter32, TimeTicks, NotificationType, Bits, ObjectIdentity, Counter64, Gauge32, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibIdentifier", "Counter32", "TimeTicks", "NotificationType", "Bits", "ObjectIdentity", "Counter64", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", PYSNMP_MODULE_ID=liebertControllerModule, liebertControllerModule=liebertControllerModule, lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules)
