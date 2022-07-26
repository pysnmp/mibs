#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 16:21:09 2022
# On host fv-az377-45 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
lgpController, liebertControllerModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpController", "liebertControllerModuleReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Counter32, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Bits, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Bits", "Integer32", "TimeTicks")
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
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules, liebertControllerModule=liebertControllerModule, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, PYSNMP_MODULE_ID=liebertControllerModule, lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules)
