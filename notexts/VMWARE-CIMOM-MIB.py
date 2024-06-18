#
# PySNMP MIB module VMWARE-CIMOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-CIMOM-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 01:44:38 2024
# On host fv-az1446-447 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, iso, ModuleIdentity, MibIdentifier, ObjectIdentity, Bits, Unsigned32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "iso", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Bits", "Unsigned32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("VMWARE-CIMOM-MIB", vmwCimOmHeartbeat=vmwCimOmHeartbeat, vmwCIMOMMIB=vmwCIMOMMIB, vmwCimOmMIBConformance=vmwCimOmMIBConformance, vmwCimOmMIBGroups=vmwCimOmMIBGroups, vmwCimOmMIBCompliances=vmwCimOmMIBCompliances, vmwCimOmMIBBasicCompliance=vmwCimOmMIBBasicCompliance, vmwCimOmNotificationGroup=vmwCimOmNotificationGroup, vmwCimOm=vmwCimOm, vmwCimOmNotifications=vmwCimOmNotifications, PYSNMP_MODULE_ID=vmwCIMOMMIB)
