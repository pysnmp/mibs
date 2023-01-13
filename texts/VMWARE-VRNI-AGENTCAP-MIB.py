#
# PySNMP MIB module VMWARE-VRNI-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VRNI-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan 13 12:15:34 2023
# On host fv-az218-3 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, NotificationType, ModuleIdentity, IpAddress, Bits, ObjectIdentity, Counter32, Gauge32, Integer32, iso, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress", "Bits", "ObjectIdentity", "Counter32", "Gauge32", "Integer32", "iso", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwVRNIAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 125))
vmwVRNIAgentCapabilityMIB.setRevisions(('2020-05-20 00:00', '2019-08-19 00:00', '2019-06-06 00:00', '2019-03-22 00:00', '2018-12-04 00:00', '2018-09-12 00:00', '2017-10-13 00:00', '2017-09-05 00:00', '2017-06-01 00:00', '2017-03-02 00:00', '2016-11-22 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setRevisionsDescriptions(('Notifications sent by VRNI as updated in 5.1 and 5.2 release', 'Notifications sent by VRNI as updated in 5.0 release', 'Notifications sent by VRNI as updated in 4.2 release', 'Notifications sent by VRNI as updated in 4.1 release', 'Notifications sent by VRNI as updated in 4.0 release', 'Notifications sent by VRNI as updated in 3.9 release', 'Change vmwVRNIAgentCapabilityMIB root oid to fix duplicate oid.', 'Notifications send by VRNI as updated in 3.5 release', 'Notifications send by VRNI as updated in 3.4 release', 'Notifications send by VRNI as updated in 3.3 release', 'Describe SNMP agent capabilities for each VRNI appliance release.',))
if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setLastUpdated('202005200000Z')
if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setContactInfo('VMware, Inc\n      3401 Hillview Ave\n      Palo Alto, CA 94304\n      Tel: 1-877-486-9273 or 650-427-5000\n      Fax: 650-427-5001\n      Web: http://kb.vmware.com/kb/1013445\n      ')
if mibBuilder.loadTexts: vmwVRNIAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VRNI agents by release.\n     It is compatible with vRNI v3.8 and onwards')
vmwVRNICapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10))
vmwVRNIAgent2020v520 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2020v520 = vmwVRNIAgent2020v520.setProductRelease('5.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2020v520 = vmwVRNIAgent2020v520.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2020v520.setDescription('Release 5.2.0 for VMware VRNI.\n    It describes all the notifications sent from this version of VRNI appliance.')
vmwVRNIAgent2020v520.setReference('http://www.vmware.com/products')
vmwVRNIAgent2019v500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v500 = vmwVRNIAgent2019v500.setProductRelease('5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v500 = vmwVRNIAgent2019v500.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2019v500.setDescription('Release 5.0.0 for VMware VRNI.\n    It describes all the notifications sent from this version of VRNI appliance.')
vmwVRNIAgent2019v500.setReference('http://www.vmware.com/products')
vmwVRNIAgent2019v420 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v420 = vmwVRNIAgent2019v420.setProductRelease('4.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v420 = vmwVRNIAgent2019v420.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2019v420.setDescription('Release 4.2.0 for VMware VRNI.\n    It describes all the notifications sent from this version of VRNI appliance.')
vmwVRNIAgent2019v420.setReference('http://www.vmware.com/products')
vmwVRNIAgent2019v410 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v410 = vmwVRNIAgent2019v410.setProductRelease('4.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2019v410 = vmwVRNIAgent2019v410.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2019v410.setDescription('Release 4.1.0 for VMware VRNI.\n    It describes all the notifications sent from this version of VRNI appliance.')
vmwVRNIAgent2019v410.setReference('http://www.vmware.com/products')
vmwVRNIAgent2018v400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v400 = vmwVRNIAgent2018v400.setProductRelease('4.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v400 = vmwVRNIAgent2018v400.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2018v400.setDescription('Release 4.0.0 for VMware VRNI.\n    It describes all the notifications sent from this version of VRNI appliance.')
vmwVRNIAgent2018v400.setReference('http://www.vmware.com/products')
vmwVRNIAgent2018v390 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v390 = vmwVRNIAgent2018v390.setProductRelease('3.9.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2018v390 = vmwVRNIAgent2018v390.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2018v390.setDescription('Release 3.9.0 for VMware VRNI.\n    It describes all the notifications sent from the VRNI appliance.')
vmwVRNIAgent2018v390.setReference('http://www.vmware.com/products')
vmwVRNIAgent2016v350 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v350 = vmwVRNIAgent2016v350.setProductRelease('3.5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v350 = vmwVRNIAgent2016v350.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2016v350.setDescription('Release 3.5.0 for VMware VRNI supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the VRNI appliance.')
vmwVRNIAgent2016v350.setReference('http://www.vmware.com/products')
vmwVRNIAgent2017v340 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v340 = vmwVRNIAgent2017v340.setProductRelease('3.4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v340 = vmwVRNIAgent2017v340.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2017v340.setDescription('Release 3.4.0 for VMware VRNI supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the VRNI appliance.\n     This mib module is backward compatible with next version.')
vmwVRNIAgent2017v340.setReference('http://www.vmware.com/products')
vmwVRNIAgent2017v330 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v330 = vmwVRNIAgent2017v330.setProductRelease('3.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2017v330 = vmwVRNIAgent2017v330.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2017v330.setDescription("Release 3.3.0 for VMware VRNI supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the VRNI appliance.\n     This mib module is backward compatible with next version. It\n     extends 3.2 release events by appending eventName managed object\n     to each notification's variable binding and adding a new set of\n     notifications.")
vmwVRNIAgent2017v330.setReference('http://www.vmware.com/products')
vmwVRNIAgent2016v320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v320 = vmwVRNIAgent2016v320.setProductRelease('3.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVRNIAgent2016v320 = vmwVRNIAgent2016v320.setStatus('current')
if mibBuilder.loadTexts: vmwVRNIAgent2016v320.setDescription('Release 3.2.0 for VMware VRNI supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the VRNI appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwVRNIAgent2016v320.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-VRNI-AGENTCAP-MIB", vmwVRNIAgent2019v420=vmwVRNIAgent2019v420, vmwVRNIAgent2019v500=vmwVRNIAgent2019v500, vmwVRNIAgentCapabilityMIB=vmwVRNIAgentCapabilityMIB, vmwVRNIAgent2018v400=vmwVRNIAgent2018v400, vmwVRNIAgent2017v330=vmwVRNIAgent2017v330, vmwVRNIAgent2018v390=vmwVRNIAgent2018v390, vmwVRNIAgent2017v340=vmwVRNIAgent2017v340, vmwVRNICapability=vmwVRNICapability, vmwVRNIAgent2016v320=vmwVRNIAgent2016v320, vmwVRNIAgent2019v410=vmwVRNIAgent2019v410, vmwVRNIAgent2020v520=vmwVRNIAgent2020v520, PYSNMP_MODULE_ID=vmwVRNIAgentCapabilityMIB, vmwVRNIAgent2016v350=vmwVRNIAgent2016v350)
