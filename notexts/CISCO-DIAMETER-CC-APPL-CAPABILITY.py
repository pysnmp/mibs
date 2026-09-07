#
# PySNMP MIB module CISCO-DIAMETER-CC-APPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DIAMETER-CC-APPL-CAPABILITY
# Source digest sha256:6e4eaa3628d35cb36721ca4f3b8ada3c5ac6540a983e887cebdec2f251da03ce
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterCCACapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 516))
ciscoDiameterCCACapability.setRevisions(('2006-09-06 00:00',))
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setLastUpdated('2006-09-06 00:00')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setOrganization('Cisco Systems, Inc.')
ciscoDiameterCCACapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 516, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIAMETER-CC-APPL-CAPABILITY", PYSNMP_MODULE_ID=ciscoDiameterCCACapability, ciscoDiameterCCACapability=ciscoDiameterCCACapability, ciscoDiameterCCACapabilityV12R0409XG=ciscoDiameterCCACapabilityV12R0409XG)
