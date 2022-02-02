#
# PySNMP MIB module VMWARE-ESX-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-ESX-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:31:36 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Gauge32, IpAddress, ModuleIdentity, Bits, Counter32, Counter64, NotificationType, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "ModuleIdentity", "Bits", "Counter32", "Counter64", "NotificationType", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 1))
vmwAgentCapabilityMIB.setRevisions(('2020-03-27 00:00', '2017-10-13 00:00', '2016-04-22 00:00', '2015-01-12 00:00', '2014-08-02 00:00', '2012-10-03 00:00', '2012-07-13 00:00', '2010-10-18 00:00', '2008-10-27 00:00',))
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setLastUpdated('202003270000Z')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwEsxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1))
vmwESX70x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX70x = vmwESX70x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX70x = vmwESX70x.setStatus('current')
vmwESX67x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX67x = vmwESX67x.setProductRelease('6.7.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX67x = vmwESX67x.setStatus('current')
vmwESX65x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX65x = vmwESX65x.setProductRelease('6.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX65x = vmwESX65x.setStatus('current')
vmwESX60x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX60x = vmwESX60x.setProductRelease('6.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX60x = vmwESX60x.setStatus('current')
vmwESX55 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX55 = vmwESX55.setProductRelease('5.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX55 = vmwESX55.setStatus('current')
vmwESX51x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setProductRelease('5.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setStatus('current')
vmwESX50x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setProductRelease('5.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setStatus('current')
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
mibBuilder.exportSymbols("VMWARE-ESX-AGENTCAP-MIB", vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, vmwESX60x=vmwESX60x, vmwESX51x=vmwESX51x, vmwESX40x=vmwESX40x, vmwEsxCapability=vmwEsxCapability, vmwESX55=vmwESX55, vmwESX70x=vmwESX70x, vmwESX65x=vmwESX65x, vmwESX67x=vmwESX67x, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB, vmwESX50x=vmwESX50x, vmwESX41x=vmwESX41x)
