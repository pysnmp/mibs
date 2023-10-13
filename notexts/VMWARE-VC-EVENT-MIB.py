#
# PySNMP MIB module VMWARE-VC-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VC-EVENT-MIB
# Produced by pysmi-1.1.8 at Fri Oct 13 14:15:09 2023
# On host fv-az877-675 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, iso, Gauge32, IpAddress, MibIdentifier, Counter64, Bits, ObjectIdentity, Unsigned32, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "iso", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "Bits", "ObjectIdentity", "Unsigned32", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwVC, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwVC")
VmwLongSnmpAdminString, = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwLongSnmpAdminString")
vmwVCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1))
vmwVCMIB.setRevisions(('2009-12-15 00:00', '2009-09-08 00:00', '2009-05-27 00:00', '2009-04-06 00:00', '2009-03-17 00:00', '2008-02-22 00:00',))
if mibBuilder.loadTexts: vmwVCMIB.setLastUpdated('200912150000Z')
if mibBuilder.loadTexts: vmwVCMIB.setOrganization('VMware, Inc')
vmwVCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0))
vpxdAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 201)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
if mibBuilder.loadTexts: vpxdAlarm.setStatus('obsolete')
vpxdDiagnostic = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 202))
if mibBuilder.loadTexts: vpxdDiagnostic.setStatus('current')
vpxdAlarmInfo = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 203)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
if mibBuilder.loadTexts: vpxdAlarmInfo.setStatus('current')
vmwVpxdTrapType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 301), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTrapType.setStatus('obsolete')
vmwVpxdHostName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 302), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdHostName.setStatus('obsolete')
vmwVpxdVMName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 303), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdVMName.setStatus('obsolete')
vmwVpxdOldStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 304), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdOldStatus.setStatus('current')
vmwVpxdNewStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 305), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdNewStatus.setStatus('current')
vmwVpxdObjValue = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 306), VmwLongSnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdObjValue.setStatus('current')
vmwVpxdTargetObj = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 307), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTargetObj.setStatus('current')
vmwVpxdTargetObjType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 308), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("host", 2), ("vm", 3), ("other", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTargetObjType.setStatus('current')
vmwVCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2))
vmwVCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1))
vmwVCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2))
vmwVCMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 2)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVCAlarmInfoGroup"), ("VMWARE-VC-EVENT-MIB", "vmwVCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCMIBBasicCompliance = vmwVCMIBBasicCompliance.setStatus('obsolete')
vmwVCMIBBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 3)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVCAlarmGroup"), ("VMWARE-VC-EVENT-MIB", "vmwVCAlarmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCMIBBasicComplianceRev2 = vmwVCMIBBasicComplianceRev2.setStatus('current')
vmwVCAlarmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 1)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmInfoGroup = vmwVCAlarmInfoGroup.setStatus('obsolete')
vmwVCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 2)).setObjects(("VMWARE-VC-EVENT-MIB", "vpxdAlarm"), ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCNotificationGroup = vmwVCNotificationGroup.setStatus('obsolete')
vmwVCAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 3)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmGroup = vmwVCAlarmGroup.setStatus('current')
vmwVCAlarmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 4)).setObjects(("VMWARE-VC-EVENT-MIB", "vpxdAlarmInfo"), ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmNotificationGroup = vmwVCAlarmNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-VC-EVENT-MIB", vmwVCMIB=vmwVCMIB, vmwVCAlarmInfoGroup=vmwVCAlarmInfoGroup, vmwVCNotifications=vmwVCNotifications, vmwVpxdNewStatus=vmwVpxdNewStatus, vmwVCNotificationGroup=vmwVCNotificationGroup, vmwVpxdTargetObjType=vmwVpxdTargetObjType, vpxdAlarm=vpxdAlarm, PYSNMP_MODULE_ID=vmwVCMIB, vmwVCMIBBasicComplianceRev2=vmwVCMIBBasicComplianceRev2, vpxdDiagnostic=vpxdDiagnostic, vmwVpxdTargetObj=vmwVpxdTargetObj, vmwVpxdVMName=vmwVpxdVMName, vmwVCAlarmGroup=vmwVCAlarmGroup, vmwVCMIBGroups=vmwVCMIBGroups, vmwVpxdHostName=vmwVpxdHostName, vmwVpxdTrapType=vmwVpxdTrapType, vmwVpxdObjValue=vmwVpxdObjValue, vmwVCMIBBasicCompliance=vmwVCMIBBasicCompliance, vmwVCAlarmNotificationGroup=vmwVCAlarmNotificationGroup, vmwVpxdOldStatus=vmwVpxdOldStatus, vpxdAlarmInfo=vpxdAlarmInfo, vmwVCMIBConformance=vmwVCMIBConformance, vmwVCMIBCompliances=vmwVCMIBCompliances)
