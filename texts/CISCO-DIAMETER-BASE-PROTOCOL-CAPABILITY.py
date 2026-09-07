#
# PySNMP MIB module CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY
# Source digest sha256:a524dbe68127aa8743737322b4d6024164a5a9434726badbf44eb44e6efc5805
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterBasePCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 517))
ciscoDiameterBasePCapability.setRevisions(('2006-09-06 11:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setLastUpdated('2006-09-06 11:30')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setDescription('The capabilities description of\n            CISCO-DIAMETER-BASE-PROTOCOL-MIB.')
ciscoDiameterBasePCapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 517, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterBasePCapabilityV12R0409XG.setDescription('Cisco Diameter Base Protocol MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY", PYSNMP_MODULE_ID=ciscoDiameterBasePCapability, ciscoDiameterBasePCapability=ciscoDiameterBasePCapability, ciscoDiameterBasePCapabilityV12R0409XG=ciscoDiameterBasePCapabilityV12R0409XG)
