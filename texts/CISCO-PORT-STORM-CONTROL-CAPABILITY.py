#
# PySNMP MIB module CISCO-PORT-STORM-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PORT-STORM-CONTROL-CAPABILITY
# Source digest sha256:aa74dfe3888d77ad9a6aeb64fd273d248a6f3fe35734967f2abd7c9d43caec97
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPortStormControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 542))
ciscoPortStormControlCapability.setRevisions(('2014-04-04 00:00', '2012-09-07 00:00', '2011-03-24 00:00', '2007-07-03 00:00', '2007-07-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortStormControlCapability.setRevisionsDescriptions(('Added capability statement cpscCapabilityV06R0002U0301PN3K.', 'Added capability statement cpscCapabilityV15R0101SYPCat6k.', 'Added capability statement cpscCapabilityV12R0233SXJPCat6k.', 'Added capability statement cpscCapabilityV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setLastUpdated('2014-04-04 00:00')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n            Tel: +1 800 553-NETS \n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setDescription('Agent capabilities for CISCO-PORT-STORM-CONTROL-MIB.')
cpscCapabilityV12R0240SGCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setProductRelease('Cisco IOS 12.2(40)SG on Cat4K platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0240SGCat4K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities')
cpscCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0233SXHPCat6K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0233SXJPCat6k.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV15R0101SYPCat6k.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV06R0002U0301PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setProductRelease('Cisco NX-OS 6.0(2)U3(1) on Nexus 3000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV06R0002U0301PN3K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PORT-STORM-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoPortStormControlCapability, ciscoPortStormControlCapability=ciscoPortStormControlCapability, cpscCapabilityV06R0002U0301PN3K=cpscCapabilityV06R0002U0301PN3K, cpscCapabilityV12R0233SXHPCat6K=cpscCapabilityV12R0233SXHPCat6K, cpscCapabilityV12R0233SXJPCat6k=cpscCapabilityV12R0233SXJPCat6k, cpscCapabilityV12R0240SGCat4K=cpscCapabilityV12R0240SGCat4K, cpscCapabilityV15R0101SYPCat6k=cpscCapabilityV15R0101SYPCat6k)
