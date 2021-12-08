#
# PySNMP MIB module VMWARE-HEARTBEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-HEARTBEAT-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:22:56 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibIdentifier, ModuleIdentity, Counter64, NotificationType, TimeTicks, Counter32, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter64", "NotificationType", "TimeTicks", "Counter32", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwProductSpecific, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific")
vmwHBMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 190, 66))
vmwHBMIB.setRevisions(('2016-02-10 00:00',))
if mibBuilder.loadTexts: vmwHBMIB.setLastUpdated('201602100000Z')
if mibBuilder.loadTexts: vmwHBMIB.setOrganization('VMware, Inc')
vmwHb = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190))
vmwHbNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 0))
vmwHbHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 190, 0, 401)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: vmwHbHeartbeat.setStatus('current')
vmwHbMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2))
vmwHbMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1))
vmwHbMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2))
vmwHbMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1, 4)).setObjects(("VMWARE-HEARTBEAT-MIB", "vmwHbNotificationGroup"), ("VMWARE-HEARTBEAT-MIB", "vmwHbNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHbMIBBasicCompliance = vmwHbMIBBasicCompliance.setStatus('current')
vmwHbNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2, 2)).setObjects(("VMWARE-HEARTBEAT-MIB", "vmwHbHeartbeat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHbNotificationGroup = vmwHbNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-HEARTBEAT-MIB", vmwHbMIBCompliances=vmwHbMIBCompliances, vmwHbHeartbeat=vmwHbHeartbeat, vmwHbMIBConformance=vmwHbMIBConformance, vmwHbMIBGroups=vmwHbMIBGroups, vmwHbNotifications=vmwHbNotifications, vmwHBMIB=vmwHBMIB, vmwHbMIBBasicCompliance=vmwHbMIBBasicCompliance, vmwHbNotificationGroup=vmwHbNotificationGroup, vmwHb=vmwHb, PYSNMP_MODULE_ID=vmwHBMIB)
