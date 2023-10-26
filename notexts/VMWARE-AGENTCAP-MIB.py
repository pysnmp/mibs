#
# PySNMP MIB module VMWARE-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-AGENTCAP-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 13:16:21 2023
# On host fv-az247-868 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, NotificationType, iso, MibIdentifier, Bits, TimeTicks, ModuleIdentity, Counter64, Unsigned32, IpAddress, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "iso", "MibIdentifier", "Bits", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "IpAddress", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 1))
vmwAgentCapabilityMIB.setRevisions(('2008-10-27 00:00',))
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setLastUpdated('200810270000Z')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwEsxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1))
vmwESX41x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setProductRelease('4.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setStatus('current')
vmwESX40x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setProductRelease('4.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setStatus('current')
mibBuilder.exportSymbols("VMWARE-AGENTCAP-MIB", vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB, vmwESX41x=vmwESX41x, vmwEsxCapability=vmwEsxCapability, vmwESX40x=vmwESX40x)
