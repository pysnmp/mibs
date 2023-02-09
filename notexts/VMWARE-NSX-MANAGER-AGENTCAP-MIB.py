#
# PySNMP MIB module VMWARE-NSX-MANAGER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-NSX-MANAGER-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Thu Feb  9 13:34:24 2023
# On host fv-az255-593 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ObjectIdentity, ModuleIdentity, TimeTicks, Unsigned32, NotificationType, MibIdentifier, iso, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "MibIdentifier", "iso", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VMWARE-NSX-MANAGER-AGENTCAP-MIB", vmwNSXMCapability=vmwNSXMCapability, vmwNSXManager2017x630=vmwNSXManager2017x630, vmwNSXManager2019x645=vmwNSXManager2019x645, vmwNSXManager2018x637=vmwNSXManager2018x637, vmwNSXManager2019x646=vmwNSXManager2019x646, vmwNSXManager2018x641=vmwNSXManager2018x641, vmwNSXManager2017x640=vmwNSXManager2017x640, vmwNSXManager2018x642=vmwNSXManager2018x642, vmwNSXManager2018x636=vmwNSXManager2018x636, PYSNMP_MODULE_ID=vmwNSXAgentCapabilityMIB, vmwNSXManager2016x=vmwNSXManager2016x, vmwNSXAgentCapabilityMIB=vmwNSXAgentCapabilityMIB, vmwNSXManager2020x647=vmwNSXManager2020x647)
