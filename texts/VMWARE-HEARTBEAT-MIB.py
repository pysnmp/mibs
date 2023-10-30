#
# PySNMP MIB module VMWARE-HEARTBEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-HEARTBEAT-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:26:11 2023
# On host fv-az443-612 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
iso, TimeTicks, Bits, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ObjectIdentity, Unsigned32, NotificationType, MibIdentifier, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwProductSpecific, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific")
vmwHBMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 190, 66))
vmwHBMIB.setRevisions(('2016-02-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwHBMIB.setRevisionsDescriptions(('First version.',))
if mibBuilder.loadTexts: vmwHBMIB.setLastUpdated('201602100000Z')
if mibBuilder.loadTexts: vmwHBMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwHBMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwHBMIB.setDescription('This MIB module provides a reverse poll for systems that do not yet support polling.\n      See http://kb.vmware.com/kb/2020271 for details on reverse polling in VMware SNMP agents.')
vmwHb = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190))
vmwHbNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 0))
vmwHbHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 190, 0, 401)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: vmwHbHeartbeat.setStatus('current')
if mibBuilder.loadTexts: vmwHbHeartbeat.setDescription('This notification, if the agent is so configured, will be sent\n         on a periodic basis to indicate cimom indication delivery is functioning.')
vmwHbMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2))
vmwHbMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1))
vmwHbMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2))
vmwHbMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1, 4)).setObjects(("VMWARE-HEARTBEAT-MIB", "vmwHbNotificationGroup"), ("VMWARE-HEARTBEAT-MIB", "vmwHbNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHbMIBBasicCompliance = vmwHbMIBBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: vmwHbMIBBasicCompliance.setDescription('The compliance statement for entities which implement the\n    VMWARE-HEARTBEAT-MIB.')
vmwHbNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2, 2)).setObjects(("VMWARE-HEARTBEAT-MIB", "vmwHbHeartbeat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHbNotificationGroup = vmwHbNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vmwHbNotificationGroup.setDescription('Notifications related to snmp agent reverse poll feature.')
mibBuilder.exportSymbols("VMWARE-HEARTBEAT-MIB", vmwHbMIBBasicCompliance=vmwHbMIBBasicCompliance, vmwHbNotificationGroup=vmwHbNotificationGroup, vmwHbMIBConformance=vmwHbMIBConformance, vmwHbMIBCompliances=vmwHbMIBCompliances, vmwHbMIBGroups=vmwHbMIBGroups, vmwHBMIB=vmwHBMIB, PYSNMP_MODULE_ID=vmwHBMIB, vmwHbNotifications=vmwHbNotifications, vmwHbHeartbeat=vmwHbHeartbeat, vmwHb=vmwHb)
