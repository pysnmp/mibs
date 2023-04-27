#
# PySNMP MIB module VMWARE-ESX-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-ESX-AGENTCAP-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:36:16 2023
# On host fv-az842-726 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, ObjectIdentity, NotificationType, IpAddress, Bits, iso, ModuleIdentity, Counter32, Unsigned32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "NotificationType", "IpAddress", "Bits", "iso", "ModuleIdentity", "Counter32", "Unsigned32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 1))
vmwAgentCapabilityMIB.setRevisions(('2020-03-27 00:00', '2017-10-13 00:00', '2016-04-22 00:00', '2015-01-12 00:00', '2014-08-02 00:00', '2012-10-03 00:00', '2012-07-13 00:00', '2010-10-18 00:00', '2008-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for VMware VSphere (Release 7.0) ESXi 2020 added.', 'Capabilities for VMware VSphere (Release 6.7) ESXi 2017 added.', 'Capabilities for VMware VSphere ESXi 2016 added.', 'Renamed mib module to reflect this contains only the VMware ESX agent.', 'Capabilities for VMware VSphere ESXi 2015 added.', 'Capabilities for VMware ESX 5.5 agent added.', 'Capabilities for VMware ESX 5.1 agent added.', 'Capabilities for VMware ESX 5.0 added.', 'Capabilities for VMware ESX 4.0 added.',))
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setLastUpdated('202003270000Z')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setContactInfo('VMware, Inc\n      3401 Hillview Ave\n      Palo Alto, CA 94304\n      Tel: 1-877-486-9273 or 650-427-5000\n      Fax: 650-427-5001\n      Web: Downloading MIB modules http://kb.vmware.com/kb/1013445\n      OID list http://kb.vmware.com/kb/2054359\n      ')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VMware ESX agents by release.')
vmwEsxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1))
vmwESX70x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX70x = vmwESX70x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX70x = vmwESX70x.setStatus('current')
if mibBuilder.loadTexts: vmwESX70x.setDescription('Release 7.0 for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3.\n      Changes in this release were primarily bug fixing related.\n     ')
vmwESX70x.setReference('http://www.vmware.com/products')
vmwESX67x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX67x = vmwESX67x.setProductRelease('6.7.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX67x = vmwESX67x.setStatus('current')
if mibBuilder.loadTexts: vmwESX67x.setDescription('Release 6.7 for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3.\n      VMWARE-ENV-MIB was fully implmented, now possible to poll BMC (IPMI) System Event Log.\n      New notifications were created for specific SDR sensors and agent will now notify\n      when IPMI SEL becomes full/capacity.\n      Other changes for this release were primarily bug fixing related.\n     ')
vmwESX67x.setReference('http://www.vmware.com/products')
vmwESX65x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX65x = vmwESX65x.setProductRelease('6.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX65x = vmwESX65x.setStatus('current')
if mibBuilder.loadTexts: vmwESX65x.setDescription('Release 6.5 for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3 with a stand-alone snmpd process.\n     NSX VDS now supported by BRIDGE MIB modules.\n     No vDR instrumentation is yet available.\n     Agent can now handle slow responses from SAN Storage when reporting LUN storage, see\n     https://kb.vmware.com/kb/2135500\n     This agent supports read-only protocol operations. This implies that configuring the SNMPv3 Agent\n     can not be done via SET operations. Hence IETF standard SNMPv3 agent configuration mibs are not provided.\n     The SNMPv3 protocol is fully supported once configured via the CLI command interface (esxcli system snmp)\n     command set or vCenter Server host profiles. Lastly this SNMP agent provides one read-only view of\n     the entire system to which all SNMPv3 users configured are assigned.\n     ')
vmwESX65x.setReference('http://www.vmware.com/products')
vmwESX60x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX60x = vmwESX60x.setProductRelease('6.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX60x = vmwESX60x.setStatus('current')
if mibBuilder.loadTexts: vmwESX60x.setDescription('Release 6.0 for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3 with a stand-alone snmpd process.\n\n     Only Minor changes and bug fixes in this release of the SNMP Agent.\n\n     No vDR instrumentation is yet available.\n\n     This agent supports read-only protocol operations. This implies that configuring the SNMPv3 Agent\n     can not be done via SET operations. Hence IETF standard SNMPv3 agent configuration mibs are not provided.\n     The SNMPv3 protocol is fully supported once configured via the CLI command interface (esxcli system snmp)\n     command set or vCenter Server host profiles. Lastly this SNMP agent provides one read-only view of\n     the entire system to which all SNMPv3 users configured are assigned.\n     ')
vmwESX60x.setReference('http://www.vmware.com/products')
vmwESX55 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX55 = vmwESX55.setProductRelease('5.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX55 = vmwESX55.setStatus('current')
if mibBuilder.loadTexts: vmwESX55.setDescription("Release 5.5 for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3 with a stand-alone snmpd process.\n\n     This release features support for monitoring multiple IP Stacks. The standard IP-MIB, UDP-MIB, and TCP-MIB\n     may be used with a context set to the IP Stack Name as found in ENTITY-MIB entLogicalTable\n     or via command: esxcli network ip netstack list\n     An example using net-snmp's snmpwalk command:: snmpwalk -v2c -n defaultTcpipStack ip\n\n     No vDR instrumentation is yet available.\n\n     This agent supports read-only protocol operations. This implies that configuring the SNMPv3 Agent\n     can not be done via SET operations. Hence IETF standard SNMPv3 agent configuration mibs are not provided.\n     The SNMPv3 protocol is fully supported once configured via the CLI command interface (esxcli system snmp)\n     command set or vCenter Server host profiles. Lastly this SNMP agent provides one read-only view of\n     the entire system to which all SNMPv3 users configured are assigned.\n     ")
vmwESX55.setReference('http://www.vmware.com/products')
vmwESX51x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setProductRelease('5.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setStatus('current')
if mibBuilder.loadTexts: vmwESX51x.setDescription('Release 5.1.x for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3 with a stand-alone snmpd process.\n      This agent supports read-only protocol operations. This implies that configuring the SNMPv3 Agent\n      can not be done via SET operations. Hence IETF standard SNMPv3 agent configuration mibs are not provided.\n      SNMPv3 protocol is fully supported once configured via the CLI command interface (esxcli system snmp)\n      command set or host profiles. Lastly this SNMP agent provides one read-only view of\n      the entire system to which all SNMPv3 users configured are assigned.\n     ')
vmwESX51x.setReference('http://www.vmware.com/products')
vmwESX50x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setProductRelease('5.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setStatus('current')
if mibBuilder.loadTexts: vmwESX50x.setDescription('Release 5.0.x for VMware ESXi. The SNMPv1/v2c agent is a subsystem in the hostd process')
vmwESX50x.setReference('http://www.vmware.com/products')
vmwESX41x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setProductRelease('4.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setStatus('current')
if mibBuilder.loadTexts: vmwESX41x.setDescription('Release 4.1.x for VMware ESX, the SNMP agent is now a subsystem in the hostd process on ESXi.')
vmwESX41x.setReference('http://www.vmware.com/products')
vmwESX40x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setProductRelease('4.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setStatus('current')
if mibBuilder.loadTexts: vmwESX40x.setDescription('Release 4.0.x for VMware ESX. The SNMP agent is now part of the hostd process')
vmwESX40x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-ESX-AGENTCAP-MIB", vmwESX50x=vmwESX50x, vmwESX40x=vmwESX40x, vmwEsxCapability=vmwEsxCapability, vmwESX67x=vmwESX67x, vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, vmwESX65x=vmwESX65x, vmwESX55=vmwESX55, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB, vmwESX70x=vmwESX70x, vmwESX41x=vmwESX41x, vmwESX60x=vmwESX60x, vmwESX51x=vmwESX51x)
