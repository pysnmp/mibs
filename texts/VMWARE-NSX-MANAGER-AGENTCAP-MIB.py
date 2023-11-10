#
# PySNMP MIB module VMWARE-NSX-MANAGER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-NSX-MANAGER-AGENTCAP-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 13:29:06 2023
# On host fv-az1435-737 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Bits, Counter32, IpAddress, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Counter64, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Counter64", "iso", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwNSXAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 25))
vmwNSXAgentCapabilityMIB.setRevisions(('2020-06-03 00:00', '2016-10-24 00:01', '2016-10-24 00:00', '2016-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for NSX Manager 6.4.x releases.', 'Capabilities for NSX Manager 6.3.x releases.', 'Update release version for 2016x to was 6.2.x from 6.5.', 'Capabilities for NSX Manager releases.',))
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setLastUpdated('202006030000Z')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setContactInfo('VMware, Inc\n      3401 Hillview Ave\n      Palo Alto, CA 94304\n      Tel: 1-877-486-9273 or 650-427-5000\n      Fax: 650-427-5001\n      Web: http://kb.vmware.com/kb/1013445\n      ')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VMware NSX Manager agents by release.')
vmwNSXMCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1))
vmwNSXManager2020x647 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2020x647 = vmwNSXManager2020x647.setProductRelease('6.4.7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2020x647 = vmwNSXManager2020x647.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2020x647.setDescription('Release 6.4.7 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2020x647.setReference('http://www.vmware.com/products')
vmwNSXManager2019x646 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x646 = vmwNSXManager2019x646.setProductRelease('6.4.6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x646 = vmwNSXManager2019x646.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2019x646.setDescription('Release 6.4.6 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2019x646.setReference('http://www.vmware.com/products')
vmwNSXManager2019x645 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x645 = vmwNSXManager2019x645.setProductRelease('6.4.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x645 = vmwNSXManager2019x645.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2019x645.setDescription('Release 6.4.5 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2019x645.setReference('http://www.vmware.com/products')
vmwNSXManager2018x642 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x642 = vmwNSXManager2018x642.setProductRelease('6.4.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x642 = vmwNSXManager2018x642.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2018x642.setDescription('Release 6.4.2 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2018x642.setReference('http://www.vmware.com/products')
vmwNSXManager2018x637 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x637 = vmwNSXManager2018x637.setProductRelease('6.3.7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x637 = vmwNSXManager2018x637.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2018x637.setDescription('Release 6.3.7 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2018x637.setReference('http://www.vmware.com/products')
vmwNSXManager2018x641 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x641 = vmwNSXManager2018x641.setProductRelease('6.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x641 = vmwNSXManager2018x641.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2018x641.setDescription('Release 6.4.1 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2018x641.setReference('http://www.vmware.com/products')
vmwNSXManager2018x636 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x636 = vmwNSXManager2018x636.setProductRelease('6.3.6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x636 = vmwNSXManager2018x636.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2018x636.setDescription('Release 6.3.6 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2018x636.setReference('http://www.vmware.com/products')
vmwNSXManager2017x640 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x640 = vmwNSXManager2017x640.setProductRelease('6.4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x640 = vmwNSXManager2017x640.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2017x640.setDescription('Release 6.4.0 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2017x640.setReference('http://www.vmware.com/products')
vmwNSXManager2017x630 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x630 = vmwNSXManager2017x630.setProductRelease('6.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x630 = vmwNSXManager2017x630.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2017x630.setDescription('Release 6.3.0 for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     WARNING: This mib module will not be backward compatible with next version.\n     ')
vmwNSXManager2017x630.setReference('http://www.vmware.com/products')
vmwNSXManager2016x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setProductRelease('6.2.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2016x.setDescription('Release 6.2.x for VMware NSX Manager supporting only SNMPv2c trap PDUs.\n     It describes all the notifications sent from the NSX Manager appliance.\n     ')
vmwNSXManager2016x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-NSX-MANAGER-AGENTCAP-MIB", vmwNSXManager2018x641=vmwNSXManager2018x641, vmwNSXManager2020x647=vmwNSXManager2020x647, vmwNSXManager2017x630=vmwNSXManager2017x630, vmwNSXManager2018x637=vmwNSXManager2018x637, PYSNMP_MODULE_ID=vmwNSXAgentCapabilityMIB, vmwNSXManager2017x640=vmwNSXManager2017x640, vmwNSXManager2019x645=vmwNSXManager2019x645, vmwNSXManager2016x=vmwNSXManager2016x, vmwNSXMCapability=vmwNSXMCapability, vmwNSXAgentCapabilityMIB=vmwNSXAgentCapabilityMIB, vmwNSXManager2018x642=vmwNSXManager2018x642, vmwNSXManager2018x636=vmwNSXManager2018x636, vmwNSXManager2019x646=vmwNSXManager2019x646)
