#
# PySNMP MIB module CISCO-VIRTUAL-SWITCH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VIRTUAL-SWITCH-CAPABILITY
# Source digest sha256:2c0b85fddd1e09ec2cee7b1751c668c06befb04758adc760068808bccd6fadd0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVirtualSwitchCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 563))
ciscoVirtualSwitchCapability.setRevisions(('2012-09-07 00:00', '2011-09-26 00:00', '2010-03-29 00:00', '2008-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setRevisionsDescriptions(('Added capability statement cvsCapV15R0101SYPCat6K.', 'Added capability statement cvsCapV15R0001SYPCat6K.', 'Added capability statement cvsCapV12R0233SXI4PCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setLastUpdated('2012-09-07 00:00')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setDescription('The Agent capabilities for CISCO-VIRTUAL-SWITCH-MIB.')
cvsCapV12R0233SXH01PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV12R0233SXH01PCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV12R0233SXI4PCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV15R0001SYPCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV15R0101SYPCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VIRTUAL-SWITCH-CAPABILITY", PYSNMP_MODULE_ID=ciscoVirtualSwitchCapability, ciscoVirtualSwitchCapability=ciscoVirtualSwitchCapability, cvsCapV12R0233SXH01PCat6K=cvsCapV12R0233SXH01PCat6K, cvsCapV12R0233SXI4PCat6K=cvsCapV12R0233SXI4PCat6K, cvsCapV15R0001SYPCat6K=cvsCapV15R0001SYPCat6K, cvsCapV15R0101SYPCat6K=cvsCapV15R0101SYPCat6K)
