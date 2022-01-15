#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:49:01 2022
# On host fv-az83-73 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
liebertControllerModuleReg, lgpController = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertControllerModuleReg", "lgpController")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, MibIdentifier, NotificationType, ModuleIdentity, Gauge32, iso, IpAddress, Bits, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "NotificationType", "ModuleIdentity", "Gauge32", "iso", "IpAddress", "Bits", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32")
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
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", liebertControllerModule=liebertControllerModule, lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, PYSNMP_MODULE_ID=liebertControllerModule, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules)
