#
# PySNMP MIB module VMWARE-VA-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VA-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Sat Jul  6 01:14:29 2024
# On host fv-az1532-138 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, Unsigned32, iso, Gauge32, IpAddress, Counter64, MibIdentifier, NotificationType, TimeTicks, ModuleIdentity, Bits, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "iso", "Gauge32", "IpAddress", "Counter64", "MibIdentifier", "NotificationType", "TimeTicks", "ModuleIdentity", "Bits", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwVAAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 5))
vmwVAAgentCapabilityMIB.setRevisions(('2020-03-27 00:00', '2017-10-13 00:00', '2016-04-22 00:00', '2015-01-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for VMware VSphere (Release 7.0) VCenter added.', 'Capabilities for VMware VSphere (Release 6.7) VCenter added.', 'Agent updates for 6.5 Release.', 'Capabilities for VMware Virtual Appliance, 6.0 release.',))
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setLastUpdated('202003270000Z')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setContactInfo('VMware, Inc\n      3401 Hillview Ave\n      Palo Alto, CA 94304\n      Tel: 1-877-486-9273 or 650-427-5000\n      Fax: 650-427-5001\n      Web: http://communities.vmware.com/community/developer/forums/managementapi\n      ')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VMware Virtual Appliance agents\n      by release.')
vmwVACapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1))
vmwVCSA2020x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2020x = vmwVCSA2020x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2020x = vmwVCSA2020x.setStatus('current')
if mibBuilder.loadTexts: vmwVCSA2020x.setDescription("Release 7.0 for VMware Virtual Appliance (VCSA) supporting SNMPv1, SNMPv2c, and SNMPv3.\n      Added REST API configuration/status/test support for appliance similar to vicfg-snmp CLI,\n      Service is off by default, see 'systemctl status snmpcfgd' and systemctl enable/start to use.\n      Added a configuration option for HOST-RESOURCES-MIB added for reporting java processes clearly.\n      Remaining changes for this release were bug fixes.\n     ")
vmwVCSA2020x.setReference('http://www.vmware.com/products')
vmwVCSA2017x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2017x = vmwVCSA2017x.setProductRelease('6.7.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2017x = vmwVCSA2017x.setStatus('current')
if mibBuilder.loadTexts: vmwVCSA2017x.setDescription('Release 6.7 for VMware Virtual Appliance (VCSA) supporting SNMPv1, SNMPv2c, and SNMPv3.\n      Changes for this release were primarily bug fixing related.\n     ')
vmwVCSA2017x.setReference('http://www.vmware.com/products')
vmwVCSA2016x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2016x = vmwVCSA2016x.setProductRelease('6.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCSA2016x = vmwVCSA2016x.setStatus('current')
if mibBuilder.loadTexts: vmwVCSA2016x.setDescription("Release 6.5 for VMware Virtual Appliance supporting SNMPv1, SNMPv2c, and SNMPv3.\n     Adds VMWARE-VCHA-MIB module support.\n     This agent supports read-only protocol operations, shares same configuration file as VMware ESXi agent.\n     This implies that configuring the SNMPv3 Agent can not be done via SET operations or use SET PDU to\n     discover engine id. Hence IETF standard SNMPv3 agent configuration mibs are not provided.\n     The SNMPv3 protocol is fully supported once configured via the CLI command interface, run\n     appliancesh shell using the 'snmp' command set. Lastly this SNMP agent provides one read-only view of\n     the entire system to which all SNMPv3 users configured are assigned.\n     ")
vmwVCSA2016x.setReference('http://www.vmware.com/products')
vmwVA2015x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVA2015x = vmwVA2015x.setProductRelease('6.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVA2015x = vmwVA2015x.setStatus('current')
if mibBuilder.loadTexts: vmwVA2015x.setDescription("Release 2015 aka 6.0 for VMware Virtual Appliance supporting SNMPv1, SNMPv2c, and SNMPv3.\n\n     This agent supports read-only protocol operations, shares same configuration file as VMware ESXi agent.\n     This implies that configuring the SNMPv3 Agent can not be done via SET operations or use SET PDU to\n     discover engine id. Hence IETF standard SNMPv3 agent configuration mibs are not provided.\n     The SNMPv3 protocol is fully supported once configured via the CLI command interface, run\n     appliancesh shell using the 'snmp' command set. Lastly this SNMP agent provides one read-only view of\n     the entire system to which all SNMPv3 users configured are assigned.\n\n     This initial release does not have: UDP-MIB, TCP-MIB modules.\n     ")
vmwVA2015x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-VA-AGENTCAP-MIB", vmwVCSA2020x=vmwVCSA2020x, vmwVACapability=vmwVACapability, vmwVCSA2016x=vmwVCSA2016x, PYSNMP_MODULE_ID=vmwVAAgentCapabilityMIB, vmwVCSA2017x=vmwVCSA2017x, vmwVA2015x=vmwVA2015x, vmwVAAgentCapabilityMIB=vmwVAAgentCapabilityMIB)
