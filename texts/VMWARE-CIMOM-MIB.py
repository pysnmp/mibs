#
# PySNMP MIB module VMWARE-CIMOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-CIMOM-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:42:52 2024
# On host fv-az1766-730 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Bits, NotificationType, Counter32, ObjectIdentity, Counter64, MibIdentifier, IpAddress, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Bits", "NotificationType", "Counter32", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "ModuleIdentity", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VMWARE-CIMOM-MIB", vmwCimOmMIBConformance=vmwCimOmMIBConformance, vmwCimOmMIBBasicCompliance=vmwCimOmMIBBasicCompliance, PYSNMP_MODULE_ID=vmwCIMOMMIB, vmwCIMOMMIB=vmwCIMOMMIB, vmwCimOmMIBCompliances=vmwCimOmMIBCompliances, vmwCimOm=vmwCimOm, vmwCimOmNotifications=vmwCimOmNotifications, vmwCimOmHeartbeat=vmwCimOmHeartbeat, vmwCimOmNotificationGroup=vmwCimOmNotificationGroup, vmwCimOmMIBGroups=vmwCimOmMIBGroups)
