#
# PySNMP MIB module VMWARE-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:26:59 2024
# On host fv-az1380-78 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Unsigned32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Integer32, NotificationType, Counter32, Gauge32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Integer32", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 1))
vmwAgentCapabilityMIB.setRevisions(('2008-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for VMware ESX 4.0 added.',))
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setLastUpdated('200810270000Z')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setContactInfo('VMware, Inc\n      3401 Hillview Ave\n      Palo Alto, CA 94304\n      Tel: 1-877-486-9273 or 650-427-5000\n      Fax: 650-427-5001\n      Web: http://communities.vmware.com/community/developer/forums/managementapi\n      ')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setDescription('This module defines agent capabilities for VMware agents.')
vmwEsxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1))
vmwESX41x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setProductRelease('4.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setStatus('current')
if mibBuilder.loadTexts: vmwESX41x.setDescription('Release 4.1.x for VMware ESX')
vmwESX41x.setReference('http://www.vmware.com/products')
vmwESX40x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setProductRelease('4.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setStatus('current')
if mibBuilder.loadTexts: vmwESX40x.setDescription('Release 4.0.x for VMware ESX')
vmwESX40x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-AGENTCAP-MIB", vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, vmwESX41x=vmwESX41x, vmwESX40x=vmwESX40x, vmwEsxCapability=vmwEsxCapability, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB)
