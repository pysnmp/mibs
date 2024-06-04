#
# PySNMP MIB module VMWARE-VA-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VA-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 11:51:42 2024
# On host fv-az1427-842 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, IpAddress, TimeTicks, Unsigned32, Counter32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, MibIdentifier, ModuleIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "TimeTicks", "Unsigned32", "Counter32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VMWARE-VA-AGENTCAP-MIB", vmwVAAgentCapabilityMIB=vmwVAAgentCapabilityMIB, vmwVACapability=vmwVACapability, PYSNMP_MODULE_ID=vmwVAAgentCapabilityMIB, vmwVCSA2017x=vmwVCSA2017x, vmwVCSA2020x=vmwVCSA2020x, vmwVA2015x=vmwVA2015x, vmwVCSA2016x=vmwVCSA2016x)
