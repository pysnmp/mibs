#
# PySNMP MIB module VMWARE-NSX-MANAGER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-NSX-MANAGER-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:16:41 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Unsigned32, Bits, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ObjectIdentity, iso, Counter64, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Unsigned32", "Bits", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "Counter64", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwNSXAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 25))
vmwNSXAgentCapabilityMIB.setRevisions(('2020-06-03 00:00', '2016-10-24 00:01', '2016-10-24 00:00', '2016-06-02 00:00',))
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setLastUpdated('202006030000Z')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwNSXMCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1))
vmwNSXManager2020x647 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2020x647 = vmwNSXManager2020x647.setProductRelease('6.4.7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2020x647 = vmwNSXManager2020x647.setStatus('current')
vmwNSXManager2019x646 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x646 = vmwNSXManager2019x646.setProductRelease('6.4.6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x646 = vmwNSXManager2019x646.setStatus('current')
vmwNSXManager2019x645 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x645 = vmwNSXManager2019x645.setProductRelease('6.4.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x645 = vmwNSXManager2019x645.setStatus('current')
vmwNSXManager2018x642 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x642 = vmwNSXManager2018x642.setProductRelease('6.4.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x642 = vmwNSXManager2018x642.setStatus('current')
vmwNSXManager2018x637 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x637 = vmwNSXManager2018x637.setProductRelease('6.3.7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x637 = vmwNSXManager2018x637.setStatus('current')
vmwNSXManager2018x641 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x641 = vmwNSXManager2018x641.setProductRelease('6.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x641 = vmwNSXManager2018x641.setStatus('current')
vmwNSXManager2018x636 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x636 = vmwNSXManager2018x636.setProductRelease('6.3.6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x636 = vmwNSXManager2018x636.setStatus('current')
vmwNSXManager2017x640 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x640 = vmwNSXManager2017x640.setProductRelease('6.4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x640 = vmwNSXManager2017x640.setStatus('current')
vmwNSXManager2017x630 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x630 = vmwNSXManager2017x630.setProductRelease('6.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x630 = vmwNSXManager2017x630.setStatus('current')
vmwNSXManager2016x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setProductRelease('6.2.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setStatus('current')
mibBuilder.exportSymbols("VMWARE-NSX-MANAGER-AGENTCAP-MIB", vmwNSXManager2017x630=vmwNSXManager2017x630, vmwNSXManager2018x637=vmwNSXManager2018x637, vmwNSXManager2020x647=vmwNSXManager2020x647, vmwNSXManager2018x642=vmwNSXManager2018x642, vmwNSXManager2019x646=vmwNSXManager2019x646, vmwNSXManager2018x641=vmwNSXManager2018x641, vmwNSXManager2019x645=vmwNSXManager2019x645, vmwNSXManager2017x640=vmwNSXManager2017x640, vmwNSXManager2018x636=vmwNSXManager2018x636, vmwNSXManager2016x=vmwNSXManager2016x, PYSNMP_MODULE_ID=vmwNSXAgentCapabilityMIB, vmwNSXAgentCapabilityMIB=vmwNSXAgentCapabilityMIB, vmwNSXMCapability=vmwNSXMCapability)
