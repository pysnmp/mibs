#
# PySNMP MIB module CTRON-SSR-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-TRAP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 15:28:35 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
capCPUCurrentUtilization, = mibBuilder.importSymbols("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization")
sysHwPowerSupply, sysHwTemperature, sysHwModuleSlotNumber, sysHwFan = mibBuilder.importSymbols("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply", "sysHwTemperature", "sysHwModuleSlotNumber", "sysHwFan")
polAclName, polAclItem = mibBuilder.importSymbols("CTRON-SSR-POLICY-MIB", "polAclName", "polAclItem")
ssrTraps, ssrMibs = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrTraps", "ssrMibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Gauge32, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, Integer32, TimeTicks, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "Integer32", "TimeTicks", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ssrTrapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300))
ssrTrapsMIB.setRevisions(('2002-07-23 17:20', '2001-02-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ssrTrapsMIB.setRevisionsDescriptions(('Update contact information. Add notifications for access\n                 denial by access control list (ACL) entry.', 'Add notifications for backup control module failure, line\n                 card failure, and CPU threshold exceeded.',))
if mibBuilder.loadTexts: ssrTrapsMIB.setLastUpdated('200207231720Z')
if mibBuilder.loadTexts: ssrTrapsMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: ssrTrapsMIB.setContactInfo('Postal: Enterasys Networks, Inc.\n             35 Industrial Way, P.O. Box 5005\n             Rochester, NH 03867-0505\n     Phone:  +1 603 332 9400\n     E-mail: support@enterasys.com\n     WWW:    http://www.enterasys.com')
if mibBuilder.loadTexts: ssrTrapsMIB.setDescription('This module describes the traps specific to the Smart Switch Router.')
trapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 1))
envTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2))
polTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3))
envPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyFailed.setStatus('current')
if mibBuilder.loadTexts: envPowerSupplyFailed.setDescription('A power supply on the sending device has failed. The \n            sysHwPowerSupply object identifies the failed supply.')
envPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
if mibBuilder.loadTexts: envPowerSupplyRecovered.setStatus('current')
if mibBuilder.loadTexts: envPowerSupplyRecovered.setDescription('A power supply on the sending device has recovered \n            after failure. The sysHwPowerSupply object identifies \n            the recovered supply.')
envFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanFailed.setStatus('current')
if mibBuilder.loadTexts: envFanFailed.setDescription('A Fan tray on the sending device has failed. The\n            sysHwFan object identifies the failed fan tray.')
envFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
if mibBuilder.loadTexts: envFanRecovered.setStatus('current')
if mibBuilder.loadTexts: envFanRecovered.setDescription('A Fan tray on the sending device has recovered\n            after failure. The sysHwFan object identifies\n            the recovered Fan tray.')
envTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 5)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempExceeded.setStatus('current')
if mibBuilder.loadTexts: envTempExceeded.setDescription('A temperature inside the chassis on the sending device has exceeded\n            normal operating temperature. The sysHwTemperature object\n            identifies the current status.')
envTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 6)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
if mibBuilder.loadTexts: envTempNormal.setStatus('current')
if mibBuilder.loadTexts: envTempNormal.setDescription('A temperature inside the chassis on the sending device has returned\n            to normal operating temperature. The sysHwTemperature\n            object identifies the current status.')
envHotSwapIn = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 7)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapIn.setStatus('current')
if mibBuilder.loadTexts: envHotSwapIn.setDescription('A module has been inserted into the chassis.\n            sysHwModuleSlotNumber identifies the slot the module was inserted into.')
envHotSwapOut = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 8)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envHotSwapOut.setStatus('current')
if mibBuilder.loadTexts: envHotSwapOut.setDescription('A module has been turned off or removed from the chassis.\n            sysHwModuleSlotNumber identifies the slot the module was removed from.')
envBackupControlModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 9)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleOnline.setStatus('current')
if mibBuilder.loadTexts: envBackupControlModuleOnline.setDescription('A backup control module that was in standby mode has taken over \n            for a failed primary control module. Poll sysHwControlModuleBackupState \n            for current state of backup control module. sysHwModuleSlotNumber is the index\n            into the sysHwModuleTable for the now active control module.')
envBackupControlModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 10)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envBackupControlModuleFailure.setStatus('current')
if mibBuilder.loadTexts: envBackupControlModuleFailure.setDescription('A backup control module that was in standby mode has changed to \n            inactive or notInstalled. Poll sysHwControlModuleBackupState \n            for current state of backup control module.')
envLineModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 11)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: envLineModuleFailure.setStatus('current')
if mibBuilder.loadTexts: envLineModuleFailure.setDescription('A line card module which was in the online state changed to the \n            offline state indicating an error condition.')
envCPUThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 12)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"))
if mibBuilder.loadTexts: envCPUThresholdExceeded.setStatus('current')
if mibBuilder.loadTexts: envCPUThresholdExceeded.setDescription('The CPU utilization has exceeded the value of capCPUMaxThreshold\n            after having been below the value of capCPUMinThreshold. Once \n            this trap has occurred it will not occurred again until the\n            utilization has dropped below capCPUMinThreshold. Poll\n            capCPUMinThreshold and capCPUMaxThreshold to determine the\n            configured threshold settings.')
polNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0))
polAclDenied = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0, 1)).setObjects(("CTRON-SSR-POLICY-MIB", "polAclName"), ("CTRON-SSR-POLICY-MIB", "polAclItem"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: polAclDenied.setStatus('current')
if mibBuilder.loadTexts: polAclDenied.setDescription("The polAclDenied trap indicates that a message was\n          dropped because of a 'deny' ACL. The polAclName and polAclItem\n          identify the entry in the polAclTable. The ifIndex value identifies\n          the interface on which the deny ACL was applied.")
ssrTrapsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2))
ssrTrapsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 1))
ssrTrapsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2))
ssrTrapsComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV10 = ssrTrapsComplianceV10.setStatus('obsolete')
if mibBuilder.loadTexts: ssrTrapsComplianceV10.setDescription('The compliance statement for the CTRON-SSR-TRAPS-MIB.')
ssrTrapsComplianceV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV20 = ssrTrapsComplianceV20.setStatus('deprecated')
if mibBuilder.loadTexts: ssrTrapsComplianceV20.setDescription('The compliance statement for the CTRON-SSR-TRAPS-MIB.')
ssrTrapsComplianceV30 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV30"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV30 = ssrTrapsComplianceV30.setStatus('deprecated')
if mibBuilder.loadTexts: ssrTrapsComplianceV30.setDescription('The compliance statement for the CTRON-SSR-TRAPS-MIB.')
ssrTrapsComplianceV40 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV40"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV40 = ssrTrapsComplianceV40.setStatus('current')
if mibBuilder.loadTexts: ssrTrapsComplianceV40.setDescription('The compliance statement for the CTRON-SSR-TRAPS-MIB.')
ssrTrapsComplianceV50 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "ssrTrapsConfGroupV50"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsComplianceV50 = ssrTrapsComplianceV50.setStatus('current')
if mibBuilder.loadTexts: ssrTrapsComplianceV50.setDescription('The compliance statement for the CTRON-SSR-TRAPS-MIB.')
ssrTrapsConfGroupV10 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV10 = ssrTrapsConfGroupV10.setStatus('obsolete')
if mibBuilder.loadTexts: ssrTrapsConfGroupV10.setDescription('A set of managed objects that make up version 1.0 of the SSR Trap MIB.')
ssrTrapsConfGroupV20 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV20 = ssrTrapsConfGroupV20.setStatus('deprecated')
if mibBuilder.loadTexts: ssrTrapsConfGroupV20.setDescription('A set of managed objects that make up version 2.0 of the SSR Trap MIB.')
ssrTrapsConfGroupV30 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV30 = ssrTrapsConfGroupV30.setStatus('deprecated')
if mibBuilder.loadTexts: ssrTrapsConfGroupV30.setDescription('A set of managed objects that make up version 3.0 of the SSR Trap MIB.')
ssrTrapsConfGroupV40 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV40 = ssrTrapsConfGroupV40.setStatus('deprecated')
if mibBuilder.loadTexts: ssrTrapsConfGroupV40.setDescription('A set of managed objects that make up version 4.0 of the SSR Trap MIB.')
ssrTrapsConfGroupV50 = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5)).setObjects(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"), ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"), ("CTRON-SSR-TRAP-MIB", "envFanFailed"), ("CTRON-SSR-TRAP-MIB", "envFanRecovered"), ("CTRON-SSR-TRAP-MIB", "envTempExceeded"), ("CTRON-SSR-TRAP-MIB", "envTempNormal"), ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"), ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"), ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"), ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"), ("CTRON-SSR-TRAP-MIB", "polAclDenied"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssrTrapsConfGroupV50 = ssrTrapsConfGroupV50.setStatus('current')
if mibBuilder.loadTexts: ssrTrapsConfGroupV50.setDescription('A set of managed objects that make up version 5.0 of the SSR Trap MIB.')
mibBuilder.exportSymbols("CTRON-SSR-TRAP-MIB", trapControl=trapControl, polAclDenied=polAclDenied, envHotSwapIn=envHotSwapIn, envTrapGroup=envTrapGroup, envCPUThresholdExceeded=envCPUThresholdExceeded, ssrTrapsComplianceV20=ssrTrapsComplianceV20, ssrTrapsComplianceV40=ssrTrapsComplianceV40, envTempNormal=envTempNormal, ssrTrapsConfGroupV40=ssrTrapsConfGroupV40, ssrTrapsConfGroupV30=ssrTrapsConfGroupV30, envPowerSupplyFailed=envPowerSupplyFailed, envHotSwapOut=envHotSwapOut, ssrTrapsConformance=ssrTrapsConformance, ssrTrapsComplianceV50=ssrTrapsComplianceV50, ssrTrapsMIB=ssrTrapsMIB, polTrapGroup=polTrapGroup, envPowerSupplyRecovered=envPowerSupplyRecovered, ssrTrapsConfGroupV50=ssrTrapsConfGroupV50, polNotifications=polNotifications, envFanRecovered=envFanRecovered, envBackupControlModuleOnline=envBackupControlModuleOnline, ssrTrapsConfGroupV20=ssrTrapsConfGroupV20, ssrTrapsComplianceV30=ssrTrapsComplianceV30, envTempExceeded=envTempExceeded, envBackupControlModuleFailure=envBackupControlModuleFailure, envLineModuleFailure=envLineModuleFailure, ssrTrapsComplianceV10=ssrTrapsComplianceV10, ssrTrapsGroups=ssrTrapsGroups, PYSNMP_MODULE_ID=ssrTrapsMIB, envFanFailed=envFanFailed, ssrTrapsCompliances=ssrTrapsCompliances, ssrTrapsConfGroupV10=ssrTrapsConfGroupV10)
