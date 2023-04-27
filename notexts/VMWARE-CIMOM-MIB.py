#
# PySNMP MIB module VMWARE-CIMOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-CIMOM-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:46:54 2023
# On host fv-az988-178 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, IpAddress, Gauge32, Integer32, Bits, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "Bits", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwEnvIndicationTime, = mibBuilder.importSymbols("VMWARE-ENV-MIB", "vmwEnvIndicationTime")
vmwProductSpecific, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific")
vmwCIMOMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 90, 10))
vmwCIMOMMIB.setRevisions(('2010-08-20 00:00',))
if mibBuilder.loadTexts: vmwCIMOMMIB.setLastUpdated('201008200000Z')
if mibBuilder.loadTexts: vmwCIMOMMIB.setOrganization('VMware, Inc')
vmwCimOm = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90))
vmwCimOmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 0))
vmwCimOmHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 90, 0, 401)).setObjects(("VMWARE-ENV-MIB", "vmwEnvIndicationTime"))
if mibBuilder.loadTexts: vmwCimOmHeartbeat.setStatus('current')
vmwCimOmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2))
vmwCimOmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1))
vmwCimOmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2))
vmwCimOmMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1, 4)).setObjects(("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"), ("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwCimOmMIBBasicCompliance = vmwCimOmMIBBasicCompliance.setStatus('current')
vmwCimOmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2, 2)).setObjects(("VMWARE-CIMOM-MIB", "vmwCimOmHeartbeat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwCimOmNotificationGroup = vmwCimOmNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-CIMOM-MIB", vmwCimOm=vmwCimOm, vmwCimOmNotifications=vmwCimOmNotifications, vmwCIMOMMIB=vmwCIMOMMIB, vmwCimOmMIBBasicCompliance=vmwCimOmMIBBasicCompliance, PYSNMP_MODULE_ID=vmwCIMOMMIB, vmwCimOmMIBConformance=vmwCimOmMIBConformance, vmwCimOmNotificationGroup=vmwCimOmNotificationGroup, vmwCimOmMIBGroups=vmwCimOmMIBGroups, vmwCimOmHeartbeat=vmwCimOmHeartbeat, vmwCimOmMIBCompliances=vmwCimOmMIBCompliances)
