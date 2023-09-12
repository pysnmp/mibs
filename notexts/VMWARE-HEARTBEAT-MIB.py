#
# PySNMP MIB module VMWARE-HEARTBEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-HEARTBEAT-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 12:24:56 2023
# On host fv-az615-431 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
iso, MibIdentifier, NotificationType, Integer32, Gauge32, Bits, Counter64, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "Bits", "Counter64", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity")
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
mibBuilder.exportSymbols("VMWARE-HEARTBEAT-MIB", vmwHbNotificationGroup=vmwHbNotificationGroup, vmwHBMIB=vmwHBMIB, vmwHbMIBConformance=vmwHbMIBConformance, vmwHbMIBGroups=vmwHbMIBGroups, vmwHb=vmwHb, PYSNMP_MODULE_ID=vmwHBMIB, vmwHbHeartbeat=vmwHbHeartbeat, vmwHbMIBCompliances=vmwHbMIBCompliances, vmwHbNotifications=vmwHbNotifications, vmwHbMIBBasicCompliance=vmwHbMIBBasicCompliance)
