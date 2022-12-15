#
# PySNMP MIB module VMWARE-ESX-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-ESX-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Thu Dec 15 08:36:01 2022
# On host fv-az193-683 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, ObjectIdentity, iso, Bits, Counter64, Unsigned32, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "iso", "Bits", "Counter64", "Unsigned32", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ModuleIdentity", "MibIdentifier", "Counter32")
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
mibBuilder.exportSymbols("VMWARE-ESX-AGENTCAP-MIB", vmwEsxCapability=vmwEsxCapability, vmwESX70x=vmwESX70x, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB, vmwESX41x=vmwESX41x, vmwESX65x=vmwESX65x, vmwESX55=vmwESX55, vmwESX51x=vmwESX51x, vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, vmwESX67x=vmwESX67x, vmwESX40x=vmwESX40x, vmwESX50x=vmwESX50x, vmwESX60x=vmwESX60x)
