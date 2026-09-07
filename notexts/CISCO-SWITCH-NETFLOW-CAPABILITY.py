#
# PySNMP MIB module CISCO-SWITCH-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-NETFLOW-CAPABILITY
# Source digest sha256:58243aa618fb5dd1132907fc9ae21eca14f6b94552b1e98f33eeb00fdad4d53a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 602))
ciscoSwitchNetflowCapability.setRevisions(('2012-09-11 00:00', '2010-11-17 00:00',))
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setLastUpdated('2012-09-11 00:00')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setOrganization('Cisco Systems, Inc.')
csnCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setStatus('current')
csnCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchNetflowCapability, ciscoSwitchNetflowCapability=ciscoSwitchNetflowCapability, csnCapV12R0250SYPCat6kPfc4=csnCapV12R0250SYPCat6kPfc4, csnCapV15R0101SYPCat6kPfc3=csnCapV15R0101SYPCat6kPfc3)
