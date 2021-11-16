#
# PySNMP MIB module CTRON-SSR-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-TRAP-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 12:09:08 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
capCPUCurrentUtilization, = mibBuilder.importSymbols("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization")
sysHwTemperature, sysHwModuleSlotNumber, sysHwFan, sysHwPowerSupply = mibBuilder.importSymbols("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature", "sysHwModuleSlotNumber", "sysHwFan", "sysHwPowerSupply")
polAclItem, polAclName = mibBuilder.importSymbols("CTRON-SSR-POLICY-MIB", "polAclItem", "polAclName")
ssrMibs, ssrTraps = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs", "ssrTraps")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, NotificationType, TimeTicks, ObjectIdentity, Gauge32, Integer32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "NotificationType", "TimeTicks", "ObjectIdentity", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ssrTrapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300))
ssrTrapsMIB.setRevisions(('2002-07-23 17:20', '2001-02-16 00:00',))
if mibBuilder.loadTexts: ssrTrapsMIB.setLastUpdated('200207231720Z')
if mibBuilder.loadTexts: ssrTrapsMIB.setOrganization('Enterasys Networks, Inc.')
trapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 1))
envTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2))
polTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3))
envPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyFailed.setStatus('current')
envPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyRecovered.setStatus('current')
envFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanFailed.setStatus('current')
envFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanRecovered.setStatus('current')
envTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 5)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempExceeded.setStatus('current')
envTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 6)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempNormal.setStatus('current')
envHotSwapIn = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 7)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapIn.setStatus('current')
envHotSwapOut = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 8)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapOut.setStatus('current')
envBackupControlModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 9)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleOnline.setStatus('current')
envBackupControlModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 10)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleFailure.setStatus('current')
envLineModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 11)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envLineModuleFailure.setStatus('current')
envCPUThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 12)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"))
if mibBuilder.loadTexts: envCPUThresholdExceeded.setStatus('current')
polNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0))
polAclDenied = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0, 1)).setObjects(("CTRON-SSR-POLICY-MIB", "polAclName"), ("CTRON-SSR-POLICY-MIB", "polAclItem"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: polAclDenied.setStatus('current')
ssrTrapsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2))
ssrTrapsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 1))
ssrTrapsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2))
ssrTrapsComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV10 = ssrTrapsComplianceV10.setStatus('obsolete')
ssrTrapsComplianceV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV20 = ssrTrapsComplianceV20.setStatus('deprecated')
ssrTrapsComplianceV30 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV30"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV30 = ssrTrapsComplianceV30.setStatus('deprecated')
ssrTrapsComplianceV40 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV40"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV40 = ssrTrapsComplianceV40.setStatus('current')
ssrTrapsComplianceV50 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV50"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV50 = ssrTrapsComplianceV50.setStatus('current')
ssrTrapsConfGroupV10 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV10 = ssrTrapsConfGroupV10.setStatus('obsolete')
ssrTrapsConfGroupV20 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV20 = ssrTrapsConfGroupV20.setStatus('deprecated')
ssrTrapsConfGroupV30 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV30 = ssrTrapsConfGroupV30.setStatus('deprecated')
ssrTrapsConfGroupV40 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV40 = ssrTrapsConfGroupV40.setStatus('deprecated')
ssrTrapsConfGroupV50 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"), ("CTRON-SSR-TRAP-MIB", "polAclDenied"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV50 = ssrTrapsConfGroupV50.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-TRAP-MIB", ssrTrapsComplianceV10=ssrTrapsComplianceV10, envBackupControlModuleOnline=envBackupControlModuleOnline, ssrTrapsConfGroupV50=ssrTrapsConfGroupV50, polAclDenied=polAclDenied, ssrTrapsConfGroupV40=ssrTrapsConfGroupV40, ssrTrapsComplianceV50=ssrTrapsComplianceV50, ssrTrapsConformance=ssrTrapsConformance, polTrapGroup=polTrapGroup, ssrTrapsComplianceV20=ssrTrapsComplianceV20, PYSNMP_MODULE_ID=ssrTrapsMIB, envHotSwapOut=envHotSwapOut, envFanFailed=envFanFailed, ssrTrapsCompliances=ssrTrapsCompliances, ssrTrapsComplianceV40=ssrTrapsComplianceV40, envCPUThresholdExceeded=envCPUThresholdExceeded, ssrTrapsGroups=ssrTrapsGroups, ssrTrapsConfGroupV10=ssrTrapsConfGroupV10, polNotifications=polNotifications, envBackupControlModuleFailure=envBackupControlModuleFailure, envHotSwapIn=envHotSwapIn, ssrTrapsComplianceV30=ssrTrapsComplianceV30, envPowerSupplyFailed=envPowerSupplyFailed, envPowerSupplyRecovered=envPowerSupplyRecovered, envTrapGroup=envTrapGroup, envTempExceeded=envTempExceeded, ssrTrapsConfGroupV30=ssrTrapsConfGroupV30, envTempNormal=envTempNormal, ssrTrapsConfGroupV20=ssrTrapsConfGroupV20, ssrTrapsMIB=ssrTrapsMIB, envLineModuleFailure=envLineModuleFailure, trapControl=trapControl, envFanRecovered=envFanRecovered)
