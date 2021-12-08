#
# PySNMP MIB module VMWARE-HEARTBEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-HEARTBEAT-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:24:06 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Bits, NotificationType, ObjectIdentity, ModuleIdentity, TimeTicks, Unsigned32, iso, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Unsigned32", "iso", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "MibIdentifier", "Integer32")
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
mibBuilder.exportSymbols("VMWARE-HEARTBEAT-MIB", vmwHbNotifications=vmwHbNotifications, vmwHbNotificationGroup=vmwHbNotificationGroup, vmwHbMIBConformance=vmwHbMIBConformance, vmwHBMIB=vmwHBMIB, vmwHb=vmwHb, vmwHbMIBBasicCompliance=vmwHbMIBBasicCompliance, PYSNMP_MODULE_ID=vmwHBMIB, vmwHbHeartbeat=vmwHbHeartbeat, vmwHbMIBGroups=vmwHbMIBGroups, vmwHbMIBCompliances=vmwHbMIBCompliances)
