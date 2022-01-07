#
# PySNMP MIB module VMWARE-CIMOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-CIMOM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 01:26:48 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, IpAddress, iso, Unsigned32, Gauge32, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "IpAddress", "iso", "Unsigned32", "Gauge32", "MibIdentifier", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwEnvIndicationTime, = mibBuilder.importSymbols("VMWARE-ENV-MIB", "vmwEnvIndicationTime")
vmwProductSpecific, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific")
vmwCIMOMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 90, 10))
vmwCIMOMMIB.setRevisions(('2010-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwCIMOMMIB.setRevisionsDescriptions(('Information on a CIM object manager subsystem.',))
if mibBuilder.loadTexts: vmwCIMOMMIB.setLastUpdated('201008200000Z')
if mibBuilder.loadTexts: vmwCIMOMMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwCIMOMMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwCIMOMMIB.setDescription('This MIB module provides instrumentation of a CIM Object Manager.')
vmwCimOm = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90))
vmwCimOmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 0))
vmwCimOmHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 90, 0, 401)).setObjects(("VMWARE-ENV-MIB", "vmwEnvIndicationTime"))
if mibBuilder.loadTexts: vmwCimOmHeartbeat.setStatus('current')
if mibBuilder.loadTexts: vmwCimOmHeartbeat.setDescription('This notification, if the agent is so configured, will be sent \n         on a periodic basis to indicate cimom indication delivery is functioning.')
vmwCimOmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2))
vmwCimOmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1))
vmwCimOmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2))
vmwCimOmMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1, 4)).setObjects(("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"), ("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwCimOmMIBBasicCompliance = vmwCimOmMIBBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: vmwCimOmMIBBasicCompliance.setDescription('The compliance statement for entities which implement the \n    VMWARE-CIMOM-MIB.')
vmwCimOmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2, 2)).setObjects(("VMWARE-CIMOM-MIB", "vmwCimOmHeartbeat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwCimOmNotificationGroup = vmwCimOmNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vmwCimOmNotificationGroup.setDescription('Notifications related to CIM Object Manager subsystem.')
mibBuilder.exportSymbols("VMWARE-CIMOM-MIB", vmwCimOmMIBConformance=vmwCimOmMIBConformance, vmwCimOmNotificationGroup=vmwCimOmNotificationGroup, vmwCimOmMIBGroups=vmwCimOmMIBGroups, vmwCimOmMIBCompliances=vmwCimOmMIBCompliances, vmwCimOmNotifications=vmwCimOmNotifications, vmwCIMOMMIB=vmwCIMOMMIB, PYSNMP_MODULE_ID=vmwCIMOMMIB, vmwCimOmHeartbeat=vmwCimOmHeartbeat, vmwCimOm=vmwCimOm, vmwCimOmMIBBasicCompliance=vmwCimOmMIBBasicCompliance)
