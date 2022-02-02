#
# PySNMP MIB module VMWARE-VA-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VA-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:08:18 2022
# On host fv-az121-846 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Bits, IpAddress, Counter32, Gauge32, ObjectIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Bits", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwVAAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 5))
vmwVAAgentCapabilityMIB.setRevisions(('2020-03-27 00:00', '2017-10-13 00:00', '2016-04-22 00:00', '2015-01-12 00:00',))
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setLastUpdated('202003270000Z')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwVACapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1))
vmwVCSA2020x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2020x = vmwVCSA2020x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2020x = vmwVCSA2020x.setStatus('current')
vmwVCSA2017x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2017x = vmwVCSA2017x.setProductRelease('6.7.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2017x = vmwVCSA2017x.setStatus('current')
vmwVCSA2016x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2016x = vmwVCSA2016x.setProductRelease('6.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2016x = vmwVCSA2016x.setStatus('current')
vmwVA2015x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVA2015x = vmwVA2015x.setProductRelease('6.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVA2015x = vmwVA2015x.setStatus('current')
mibBuilder.exportSymbols("VMWARE-VA-AGENTCAP-MIB", vmwVA2015x=vmwVA2015x, vmwVCSA2020x=vmwVCSA2020x, vmwVCSA2017x=vmwVCSA2017x, vmwVACapability=vmwVACapability, PYSNMP_MODULE_ID=vmwVAAgentCapabilityMIB, vmwVCSA2016x=vmwVCSA2016x, vmwVAAgentCapabilityMIB=vmwVAAgentCapabilityMIB)
